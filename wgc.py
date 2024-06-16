from ipaddress import IPv4Address, IPv4Interface, IPv4Network
import ipaddress
from typing import List
import click
import subprocess

class Peer:
    def __init__(self, public_key = '', allowed_ips = [], endpoint = '', persistent_keepalive = -1):
        self.public_key: str = public_key
        self.allowed_ips: List[str] = allowed_ips
        self.endpoint: str = endpoint
        self.persistent_keepalive: int = persistent_keepalive


class Config:
    def __init__(self, config_file = '', address = '', listen_port = -1, private_key = '', mtu = -1):
        self.config_file: str = config_file
        self.address: IPv4Interface|None = None
        if address != '':
            self.address = IPv4Interface(address)
        self.listen_port: int = listen_port
        self.private_key: str = private_key
        self.mtu: int = mtu
        self.peers: List[Peer] = []
        self.network: IPv4Network|None = None
    
    
    def parse_from_file(self):
        with open(self.config_file, "r") as f:
            config_lines = f.readlines()
            line_ptr = 0
            line_count = config_lines.__len__()
            while line_ptr < line_count:
                line = config_lines[line_ptr]
                print(f"line: {line}")
                if line.startswith("Address"):
                    self.address = IPv4Interface(line.split("=")[1].strip())
                    self.network = self.address.network
                    
                elif line.startswith("ListenPort"):
                    self.listen_port = int(line.split("=")[1].strip())
                elif line.startswith("PrivateKey"):
                    self.private_key = line.split("=")[1].strip()
                elif line.startswith("MTU"):
                    self.mtu = int(line.split("=")[1].strip())
                elif line.startswith("[Peer]"):
                    line_ptr += 1
                    peer = Peer()
                    while line != '\n' and line_ptr < line_count:
                        line = config_lines[line_ptr]
                        if line.startswith("PublicKey"):
                            peer.public_key = line.split("=")[1].strip()
                        elif line.startswith("AllowedIPs"):
                            peer.allowed_ips = line.split("=")[1].strip().split(",")
                        elif line.startswith("Endpoint"):
                            peer.endpoint = line.split("=")[1].strip()
                        elif line.startswith("PersistentKeepalive"):
                            peer.persistent_keepalive = int(line.split("=")[1].strip())
                        line_ptr += 1
                    self.peers.append(peer)
                else:
                    pass
                line_ptr += 1


@click.group()
def cli():
    pass


@click.command()
def genkey():
    result = subprocess.run(["wg", "genkey"], capture_output=True, check=True)
    output = result.stdout.decode("utf-8")
    click.echo(f"{output}")
    
@click.command()
@click.option("--config-file", "-c", required=True, help="Path to the WireGuard configuration file")
def test_parse_config(config_file):
    config = Config(config_file)
    config.parse_from_file()
    print(f"Config: {config.__dict__}")


cli.add_command(genkey)
cli.add_command(test_parse_config)

if __name__ == "__main__":
    cli()

# END