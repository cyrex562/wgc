from click.testing import CliRunner
import click
from wgc import cli

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