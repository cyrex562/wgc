import os
import pathlib
import re
from ipaddress import IPv4Interface, IPv4Network, IPv4Address
from typing import List

import jsonpickle

from wireguard_ops import gen_priv_key, calc_pub_key, gen_client_peer_config
from wireguard_peer import Peer


class Config:
    def __init__(
        self,
        config_file: str = "",
        peer_config_dir: str = "",
        address: str = "",
        listen_port: int = -1,
        private_key: str = "",
        mtu: int = -1,
    ):
        self.config_file: str = config_file
        self.peer_config_dir: str = peer_config_dir
        self.address: IPv4Interface = IPv4Interface("0.0.0.0/0")
        if address != "":
            self.address = IPv4Interface(address)
        self.listen_port: int = listen_port
        self.private_key: str = private_key
        self.mtu: int = mtu
        self.peers: List[Peer] = []
        self.network: IPv4Network = IPv4Network("0.0.0.0/0")

    @classmethod
    def from_string(cls, config_data: str) -> 'Config':
        inst: Config = cls()
        splits = re.split(r"\[\W+]", config_data, flags=re.MULTILINE)
        for split in splits:
            section = split.strip()
            sec_lines = section.split("\n")
            if sec_lines[0] == "Interface":
                for line in sec_lines:
                    if line.startswith("Address"):
                        inst.address = IPv4Interface(line.split("=")[1].strip())
                        inst.network = inst.address.network
                    elif line.startswith("ListenPort"):
                        inst.listen_port = int(line.split("=")[1].strip())
                    elif line.startswith("PrivateKey"):
                        inst.private_key = line.split("=")[1].strip()
                    elif line.startswith("MTU"):
                        inst.mtu = int(line.split("=")[1].strip())
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
                inst.peers.append(peer)
        return inst

    @classmethod
    def from_file(cls, config_file: str) -> 'Config':
        # self.config_file = config_file
        if not os.path.exists(config_file):
            raise ValueError(f"Config file {config_file} does not exist")

        with open(config_file, "r") as f:
            config_buf = f.read()
            inst: Config = cls.from_string(config_buf)
            inst.config_file = config_file
            return inst


    def get_used_ip_addrs(self) -> List[IPv4Address]:
        our_net = self.network
        member_ips: List[IPv4Address] = [self.address.ip]
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
        priv_key = gen_priv_key()
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
        exploded = addr.exploded.split(".")
        peer_config_file_path = pathlib.Path(
            f"peer_{exploded[0]}_{exploded[1]}_{exploded[2]}_{exploded[3]}.conf"
        )
        peer_config_file_path = pathlib.Path()
        # TODO: add peer to main config


    def to_json(self) -> str:
        result: str = jsonpickle.encode(self, unpicklable=False, indent=2) # type: ignore
        return result # type: ignore