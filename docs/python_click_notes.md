# Python click cli tool notes

* detecting the source of a parameter, e.g. command line, enviironment variable or config map: [https://click.palletsprojects.com/en/8.1.x/advanced/#detecting-the-source-of-a-parameter]
  * ex:

    ```python
    @click.command()
    @click.argument('port', nargs=1, default=8080, envvar="PORT")
    @click.pass_context
    def cli(ctx, port):
        source = ctx.get_parameter_source("port")
        click.echo(f"Port came from {source.name}")
    ```

* resource management: [https://click.palletsprojects.com/en/8.1.x/advanced/#managing-resources]

* global context access: access current context from anywhere within the same thread through the use of `get_current_context()`.
  * ex:

    ```python
    import click

    @click.command()
    def cli():
        ctx = click.get_current_context()
        click.echo(f"Command: {ctx.command.name}")
    ```

* invoke one command from another command - discouraged with click
  * ex:

    ```python
    cli = click.Group()

    @cli.command()
    @click.option('--count', default=1)
    def test(count):
        click.echo(f'Count: {count}')

    @cli.command()
    @click.option('--count', default=1)
    @click.pass_context
    def dist(ctx, count):
        ctx.forward(test)
        ctx.invoke(test, count=42)
    ```

* parameter modifications: [https://click.palletsprojects.com/en/8.1.x/advanced/#parameter-modifications]
  * parameters are forwarded to the command callbacks. This pattern is not recommended. 
  * ex:

    ```python
    import urllib

    def open_url(ctx, param, value):
        if value is not None:
            ctx.params['fp'] = urllib.urlopen(value)
            return value

    @click.command()
    @click.option('--url', callback=open_url)
    def cli(url, fp=None):
        if fp is not None:
            click.echo(f"{url}: {fp.code}")
    ```

* waiting for keypress: [https://click.palletsprojects.com/en/8.1.x/utils/#waiting-for-key-press]
  * wait until user presses any key on the keyboard
  * prints a quick message to the terminal and wiat for the user to press a key
  * becomes a nop if the script is run non-interactively
  * ex:

    ```python
    import click
    click.pause()
    ```

* screen clearing: [https://click.palletsprojects.com/en/8.1.x/utils/#screen-clearing]
  * clear the screen
  * ex:

      ```python
      import click
      click.clear()
      ```

* pager support: [https://click.palletsprojects.com/en/8.1.x/utils/#pager-support]
  * show long text on the terminal and enable the user to scroll through it
  * ex:

    ```python
    @click.command()
    def less():
        click.echo_via_pager("\n".join(f"Line {idx}" for idx in range(200)))
    ```

* finding application folders: [https://click.palletsprojects.com/en/8.1.x/utils/#finding-application-folders]
  * return the most appropriate location for per-user config files, based on OS
  * ex:

    ```python
    import os
    import click
    import ConfigParser

    APP_NAME = 'My Application'

    def read_config():
        cfg = os.path.join(click.get_app_dir(APP_NAME), 'config.ini')
        parser = ConfigParser.RawConfigParser()
        parser.read([cfg])
        rv = {}
        for section in parser.sections():
            for key, value in parser.items(section):
                rv[f"{section}.{key}"] = value
        return rv
    ```

* intelligent file opening: [https://click.palletsprojects.com/en/8.1.x/utils/#intelligent-file-opening]
  * intelligently open stdin/stdout as well as any other file
  * ex:

    ```python
    import click

    stdout = click.open_file('-', 'w')
    test_file = click.open_file('test.txt', 'w')
    ```

* launching applications: [https://click.palletsprojects.com/en/8.1.x/utils/#launching-applications]
  * open default application associated with a url or a file type