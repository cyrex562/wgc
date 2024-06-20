from ipaddress import IPv4Address, IPv4Interface, IPv4Network
import ipaddress
from typing import List
import click
import subprocess

import jsonpickle
from loguru import logger

class Peer:
    def __init__(self, public_key = '', endpoint = '', persistent_keepalive = -1):
        self.public_key: str = public_key
        self.allowed_ips: List[IPv4Interface] = []
        self.endpoint: str = endpoint
        self.persistent_keepalive: int = persistent_keepalive


class Config:
    def __init__(self, config_file = '', address = '', listen_port = -1, private_key = '', mtu = -1):
        self.config_file: str = config_file
        self.address: IPv4Interface = IPv4Interface('0.0.0.0/0')
        if address != '':
            self.address = IPv4Interface(address)
        self.listen_port: int = listen_port
        self.private_key: str = private_key
        self.mtu: int = mtu
        self.peers: List[Peer] = []
        self.network: IPv4Network = IPv4Network('0.0.0.0/0')
    
    
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
                            allowed_ip_strings = line.split("=")[1].strip().split(",")
                            for ais in allowed_ip_strings:
                                peer.allowed_ips.append(IPv4Interface(ais.strip()))
                        elif line.startswith("Endpoint"):
                            peer.endpoint = line.split("=")[1].strip()
                        elif line.startswith("PersistentKeepalive"):
                            peer.persistent_keepalive = int(line.split("=")[1].strip())
                        elif line == '\n':
                            break
                        else:
                            print(f"Unknown line: {line}")
                        line_ptr += 1
                    self.peers.append(peer)
                else:
                    pass
                line_ptr += 1
    
    
    def get_used_ip_addrs(self) -> List[IPv4Address]:
        our_net = self.network
        member_ips: List[IPv4Address] = []
        member_ips.append(self.address.ip)
        for peer in self.peers:
            for allowed_ip in peer.allowed_ips:
                if allowed_ip.network.subnet_of(our_net):
                    member_ips.append(allowed_ip.ip)
        return member_ips
    
    
    def get_unused_ip_addrs(self) -> List[IPv4Address]:
        our_net = self.network
        all_ips = list(our_net.hosts())
        used_ips = self.get_used_ip_addrs()
        unused_ips = [ip for ip in all_ips if ip not in used_ips]
        return unused_ips


# CLI object
@click.group()
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose mode", default = False)
@click.option("--config-file", "-c", help="Path to the WireGuard configuration file")
@click.pass_context
def cli(ctx, verbose, config_file):
    ctx.ensure_object(dict)
    ctx.obj['VERBOSE'] = verbose
    ctx.obj['CONFIG_FILE'] = config_file


@cli.command()
def genkey():
    result = subprocess.run(["wg", "genkey"], capture_output=True, check=True)
    output = result.stdout.decode("utf-8")
    click.echo(f"{output}")
    
@cli.command()
@click.option("--private-key", "-p", help="Private key", type=str, default='')
@click.option("--input-file", "-i", help="Input file", type=str, default='')
def pubkey(private_key, input_file):
    if private_key != '' and input_file != '':
        raise click.UsageError("Only one of private-key or input-file should be provided")
    elif private_key == '' and input_file == '':
        raise click.UsageError("One of private-key or input-file should be provided")
    elif private_key != '':
        key = private_key.encode("utf-8")
    else:
        with open(input_file, "r") as f:
            key = f.read().encode("utf-8")
    result = subprocess.run(["wg", "pubkey"], input=key, capture_output=True, check=True)
    pub_key = result.stdout.decode("utf-8").strip()
    print(f"{pub_key}")
    

@cli.command()
@click.pass_context
def test_parse_config(ctx):
    config_file = ctx.obj['CONFIG_FILE']
    if not os.path.exists(config_file):
        raise click.UsageError(f"Config file {config_file} does not exist")
    config = Config(config_file)
    config.parse_from_file()
    json_str = jsonpickle.encode(config, unpicklable=False, indent=2)
    print(f"Config: {json_str}")


@cli.command()
@click.option("--config-file", "-c", required=True, help="Path to the WireGuard configuration file")
def edit_config(config_file):
    click.edit(filename=config_file, require_save=True)



# add commands to the cli
# cli.add_command(genkey)
# cli.add_command(test_parse_config)
# cli.add_command(pubkey)
# cli.add_command(edit_config)

# entry point

if __name__ == "__main__":
    cli(auto_envvar_prefix="WGC")

# END