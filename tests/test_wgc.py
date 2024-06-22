from ipaddress import IPv4Address
from click.testing import CliRunner
import click
from wgc import cli, Config

EXPECTED_CONFIG_IPS = [IPv4Address('10.70.0.1'), IPv4Address('10.70.0.3'), IPv4Address('10.70.0.4'), IPv4Address('10.70.0.5'), IPv4Address('10.70.0.6'), IPv4Address('10.70.0.7'), IPv4Address('10.70.0.8'), IPv4Address('10.70.0.9'), IPv4Address('10.70.0.10')]

def test_pubkey_input_opt():
    runner = CliRunner()
    exp_priv_key = click.open_file("test_data/test.priv.key", "r").read()
    exp_pub_key = click.open_file("test_data/test.pub.key", "r").read()
    result = runner.invoke(cli, ["pubkey", "-p", exp_priv_key])
    assert result.exit_code == 0
    assert result.output == exp_pub_key

def test_pubkey_input_file():
    runner = CliRunner()
    exp_priv_key = click.open_file("test_data/test.priv.key", "r").read()
    exp_pub_key = click.open_file("test_data/test.pub.key", "r").read()
    result = runner.invoke(cli, ["pubkey", "-i", "test_data/test.priv.key"])
    assert result.exit_code == 0
    assert result.output == exp_pub_key

def test_pubkey_no_opt():
    runner = CliRunner()
    result = runner.invoke(cli, ["pubkey"])
    assert result.exit_code == 2
    assert "One of private-key or input-file should be provided" in result.output

def test_pubkey_two_opt():
    runner = CliRunner()
    exp_priv_key = click.open_file("test_data/test.priv.key", "r").read()
    exp_pub_key = click.open_file("test_data/test.pub.key", "r").read()
    result = runner.invoke(cli, ["pubkey", "-p", exp_priv_key, "-i", "test_data/test.priv.key"])
    assert result.exit_code == 2
    assert "Only one of private-key or input-file should be provided" in result.output

def test_get_used_ip_addrs():
    config = Config()
    config.config_file = "test_data/test_server.conf"
    config.loadf()
    used_ips = config.get_used_ip_addrs()
    assert used_ips == EXPECTED_CONFIG_IPS
    
def test_get_unused_ip_addrs():
    config = Config()
    config.config_file = "test_data/test_server.conf"
    config.loadf()
    unused_ips = config.get_unused_ip_addrs()
    assert EXPECTED_CONFIG_IPS not in unused_ips