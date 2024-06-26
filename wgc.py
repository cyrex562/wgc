import click
import subprocess

from click import Context
import pathlib

from app_settings import AppSettings
from wireguard_config import Config
import wireguard_ops as ops



# CLI object
@click.group()
@click.option(
    "--verbose", "-v", is_flag=True, help="Enable verbose mode", default=False
)
@click.option(
    "--config-file",
    "-c",
    help="Path to the WireGuard configuration file",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, writable=True, allow_dash=False, path_type=pathlib.Path,),
    default=None,
)
@click.option(
    "--settings-file",
    "-s",
    help="Path to the WireGuard configuration file",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, writable=True, allow_dash=False, path_type=pathlib.Path,),
    default=None,
)
@click.pass_context
def cli(ctx: click.Context, verbose: bool, config_file: pathlib.Path|None, settings_file: pathlib.Path|None):
    ctx.ensure_object(dict)

    ctx.obj["VERBOSE"] = verbose

    if config_file is not None:
        ctx.obj["CONFIG_FILE"] = config_file
        config = Config.from_file(str(config_file))
        ctx.obj["CONFIG"] = config

    if settings_file is not None:
        ctx.obj["SETTINGS_FILE"] = settings_file
        settings = AppSettings.from_file(str(settings_file))
        ctx.obj["SETTINGS"] = settings


@cli.group()
def show():
    pass


def check_config_exists(ctx: Context):
    """check if the context object has a config object. If not, raise a ValueError

    :param ctx: a click Context object
    :type ctx: Context
    :raises ValueError: when config is not present
    """
    if "CONFIG" not in ctx.obj:
        raise ValueError("Config not loaded")


@show.command(name="config")
@click.pass_context
def show_config(ctx: Context):
    check_config_exists(ctx)
    config: Config = ctx.obj["CONFIG"]
    config_json = config.to_json()
    click.echo(f"{config_json}")


@show.command(name="peers")
@click.pass_context
def show_peers(ctx: Context):
    check_config_exists(ctx)
    config: Config = ctx.obj["CONFIG"]
    peers = config.peers
    


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
    check_config_exists(ctx)
    click.edit(filename=ctx.obj["CONFIG_FILE"], require_save=True)


# add commands to the cli
# cli.add_command(genkey)
# cli.add_command(test_parse_config)
# cli.add_command(pubkey)
# cli.add_command(edit_config)

# entry point

if __name__ == "__main__":
    cli(auto_envvar_prefix="WGC")

# END
