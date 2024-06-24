import click
import subprocess
import yaml
import os

import jsonpickle
from click import Context

from .app_settings import AppSettings
from wireguard_config import Config
import wireguard_ops as ops


# CLI object
@click.group()
@click.option(
    "--verbose", "-v", is_flag=True, help="Enable verbose mode", default=False
)
@click.option(
    "--config-file", "-c", help="Path to the WireGuard configuration file", default=""
)
@click.option(
    "--settings-file", "-s", help="Path to the WireGuard configuration file", type=click.File(), default=""
)
@click.pass_context
def cli(ctx: click.Context, verbose: bool, config_file: str, settings_file: str):
    ctx.ensure_object(dict)

    ctx.obj["VERBOSE"] = verbose

    # if config file is not provided, do nothing
    if config_file == "":
        pass
    # if config file is provided, check if it exists
    elif not os.path.exists(config_file):
        raise ValueError(f"Config file {config_file} does not exist")
    # if config file is provided and exists then load it
    else:
        config = Config.from_file(config_file)
        ctx.obj["CONFIG"] = config

    # if settings file is not provided, do nothing
    if settings_file == "":
        pass
    elif not os.path.exists(settings_file):
        raise ValueError(f"Settings file {settings_file} does not exist")
    else:
        settings = AppSettings.from_file(settings_file)
        ctx.obj["SETTINGS"] = settings


def check_load_config(ctx: Context):
    # first check if the config is already loaded
    if "CONFIG" in ctx.obj:
        return ctx.obj["CONFIG"]
    else:
        raise ValueError("Config not loaded")


@cli.group()
def show():
    pass


@show.command(name="config")
@click.pass_context
def show_config(ctx: Context):
    config: Config = ctx.obj["CONFIG"]
    config_json = config.to_json()
    click.echo(f"{config_json}")


@show.command(name="peers")
@click.pass_context
def show_peers(ctx: Context):
    raise NotImplemented()


@show.command(name="addresses")
@click.pass_context
def show_addresses(ctx: Context):
    raise NotImplemented()


@show.command(name="used-addresses")
@click.pass_context
def show_used_addresses(ctx: Context):
    raise NotImplemented


@show.command(name="unused-addresses")
@click.pass_context
def show_unused_addresses(ctx: Context):
    raise NotImplemented


@show.command(name="public-key")
@click.pass_context
@click.option(
    "--private-key", "-k", help="Private key to show public key for", type=str
)
def show_public_key(ctx: Context, private_key: str):
    result = subprocess.run(
        ["wg", "pubkey"], input=private_key, capture_output=True, check=True
    )
    pub_key = result.stdout.decode("utf-8").strip()
    click.echo(f"{pub_key}")


@cli.group()
def gen():
    pass


@gen.command(name="private-key")
def gen_private_key():
    val = ops.gen_priv_key()
    click.echo(f"{val}")


@gen.command(name="preshared-key")
def gen_preshared_key():
    val = ops.gen_psk()
    click.echo(f"{val}")


@cli.group()
def config():
    pass


@config.command(name="edit")
@click.pass_context
def edit_config(ctx: Context):

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
