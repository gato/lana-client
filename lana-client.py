#!python3
import click

from lana.cmd import LanaCmd
from lana.intro import intro

DEFAULT_HOST='http://localhost'
DEFAULT_PORT=8080

@click.command()
@click.option('--host', '-h', help='lana server host (default {})'.format(DEFAULT_HOST))
@click.option('--port', '-p', help='lana server port (default {})'.format(DEFAULT_PORT))

def command(host, port):
  if host == None:
    host = DEFAULT_HOST
  if port == None:
    port = DEFAULT_PORT
  cmd = LanaCmd(host, port)
  cmd.cmdloop(intro)

command()