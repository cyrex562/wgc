import subprocess


def gen_priv_key() -> str:
    result = subprocess.run(["wg", "genkey"], capture_output=True, check=True)
    output = result.stdout.decode("utf-8")
    return output.strip()


def gen_psk() -> str:
    result = subprocess.run(["wg", "genpsk"], capture_output=True, check=True)
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

