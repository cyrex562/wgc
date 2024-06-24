from ipaddress import IPv4Interface
from typing import List


class Peer:
    def __init__(
        self,
        private_key: str = "",
        public_key: str = "",
        endpoint: str = "",
        persistent_keepalive: int = -1,
        ip_interface: IPv4Interface = IPv4Interface("0.0.0.0/0"),
            allowed_ips: List[IPv4Interface]|None=None,
    ):
        if allowed_ips is None:
            allowed_ips = []
        self.private_key: str = private_key
        self.public_key: str = public_key
        self.allowed_ips: List[IPv4Interface] = allowed_ips
        self.address: IPv4Interface = ip_interface
        self.endpoint: str = endpoint
        self.persistent_keepalive: int = persistent_keepalive
