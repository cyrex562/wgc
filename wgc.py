from ipaddress import IPv4Address, IPv4Interface, IPv4Network
from typing import List
import click
import subprocess
import re
import yaml
import os
import pathlib

import jsonpickle
from loguru import logger


class AppSettings:
    def __init__(self):
        wg_path = "/usr/bin/wg"
        wg_quick_path = "/usr/bin/wg-quick"
        wg_dir = "/etc/wireguard"
        peer_config_dir = "/etc/wireguard"


class Peer:
    def __init__(
        self,
        private_key: str = "",
        public_key: str = "",
        endpoint: str = "",
        persistent_keepalive: int = -1,
        ip_interface: IPv4Interface = IPv4Interface("0.0.0.0/0"),
        allowed_ips: List[IPv4Interface] = [],
    ):
        self.private_key: str = private_key
        self.public_key: str = public_key
        self.allowed_ips = allowed_ips
        self.address: IPv4Interface = ip_interface
        self.endpoint: str = endpoint
        self.persistent_keepalive: int = persistent_keepalive


class Config:
    def __init__(
        self,
        config_file: str = "",
        address: str = "",
        listen_port: int = -1,
        private_key: str = "",
        mtu: int = -1,
    ):
        self.config_file: str = config_file
        self.address: IPv4Interface = IPv4Interface("0.0.0.0/0")
        if address != "":
            self.address = IPv4Interface(address)
        self.listen_port: int = listen_port
        self.private_key: str = private_key
        self.mtu: int = mtu
        self.peers: List[Peer] = []
        self.network: IPv4Network = IPv4Network("0.0.0.0/0")

    def loads(self, config_data: str):
        splits = re.split(r"\[\W+\]", config_data, flags=re.MULTILINE)
        for split in splits:
            section = split.strip()
            sec_lines = section.split("\n")
            if sec_lines[0] == "Interface":
                for line in sec_lines:
                    if line.startswith("Address"):
                        self.address = IPv4Interface(line.split("=")[1].strip())
                        self.network = self.address.network
                    elif line.startswith("ListenPort"):
                        self.listen_port = int(line.split("=")[1].strip())
                    elif line.startswith("PrivateKey"):
                        self.private_key = line.split("=")[1].strip()
                    elif line.startswith("MTU"):
                        self.mtu = int(line.split("=")[1].strip())
                    else:
                        pass
            elif sec_lines[0] == "Peer":
                peer = Peer()
                for line in sec_lines:
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
                    else:
                        pass
                self.peers.append(peer)

    def loadf(self, config_file: str):
        self.config_file = config_file
        if not os.path.exists(config_file):
            raise ValueError(f"Config file {config_file} does not exist")

        with open(config_file, "r") as f:
            config_buf = f.read()
            self.loads(config_buf)

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

    def get_next_avail_ip(self):
        unused_ips = self.get_unused_ip_addrs()
        if unused_ips.__len__() > 0:
            return unused_ips[0]
        else:
            return None

    def add_client_peer(self, allowed_ips: List[IPv4Interface] = []) -> str:
        next_ip = self.get_next_avail_ip()
        if next_ip is None:
            raise ValueError("No more IP addresses available")
        priv_key = int_gen_priv_key()
        pub_key = calc_pub_key(priv_key)
        peer = Peer(
            private_key=priv_key,
            public_key=pub_key,
            ip_interface=IPv4Interface(f"{next_ip}/32"),
            allowed_ips=allowed_ips,
        )
        peer_config = gen_client_peer_config(peer)
        # TODO: write peer config to file

        addr = peer.address
        exploded = addr.exploded.split('.') 
        peer_config_file_path = pathlib.Path(f'peer_{exploded[0]}_{exploded[1]}_{exploded[2]}_{exploded[3]}.conf')
        peer_config_file_path = pathlib.Path()
        # TODO: add peer to main config


def int_gen_priv_key() -> str:
    result = subprocess.run(["wg", "genkey"], capture_output=True, check=True)
    output = result.stdout.decode("utf-8")
    return output.strip()


def calc_pub_key(private_key: str) -> str:
    result = subprocess.run(
        ["wg", "pubkey"],
        input=private_key.encode("utf-8"),
        capture_output=True,
        check=True,
    )
    pub_key = result.stdout.decode("utf-8").strip()
    return pub_key


def gen_client_peer_config() -> str:
    pass


# CLI object
@click.group()
@click.option(
    "--verbose", "-v", is_flag=True, help="Enable verbose mode", default=False
)
@click.option("--config-file", "-c", help="Path to the WireGuard configuration file")
@click.option("--settings-file", "-s", help="Path to the WireGuard configuration file")
@click.pass_context
def cli(ctx: click.Context, verbose: bool, config_file: str, settings_file: str):
    ctx.ensure_object(dict)
    ctx.obj["VERBOSE"] = verbose
    ctx.obj["CONFIG_FILE"] = config_file
    ctx.obj["SETTINGS_FILE"] = settings_file

    if os.path.exists(settings_file):
        with open(settings_file, "r") as f:
            settings = yaml.load(f, Loader=yaml.FullLoader)
            ctx.obj["SETTINGS"] = settings

    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            config = Config()
            config.config_file = config_file
            config.loadf()
            ctx.obj["CONFIG"] = config


@cli.command()
def gen_priv_key():
    val = int_gen_priv_key()
    click.echo(f"{val}")


@cli.command()
@click.option("--private-key", "-p", help="Private key", type=str, default="")
@click.option("--input-file", "-i", help="Input file", type=str, default="")
def pubkey(private_key: str, input_file: str):
    if private_key != "" and input_file != "":
        raise click.UsageError(
            "Only one of private-key or input-file should be provided"
        )
    elif private_key == "" and input_file == "":
        raise click.UsageError("One of private-key or input-file should be provided")
    elif private_key != "":
        key = private_key.encode("utf-8")
    else:
        with open(input_file, "r") as f:
            key = f.read().encode("utf-8")
    result = subprocess.run(
        ["wg", "pubkey"], input=key, capture_output=True, check=True
    )
    pub_key = result.stdout.decode("utf-8").strip()
    click.echo(f"{pub_key}")


@cli.command()
@click.pass_context
def show_config(ctx: Context):
    config_file = ctx.obj["CONFIG_FILE"]
    if not os.path.exists(config_file):
        raise click.UsageError(f"Config file {config_file} does not exist")
    config = Config(config_file)
    config.loadf()
    json_str: str = jsonpickle.encode(config, unpicklable=False, indent=2)  # type: ignore
    click.echo(f"Config: {json_str}")


@cli.command()
@click.option(
    "--config-file",
    "-c",
    required=True,
    help="Path to the WireGuard configuration file",
)
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
