#!python3
import click

from lana.cmd import LanaCmd
from lana.intro import intro

@click.command()
@click.option('--host', '-h', help='lana server host (default localhost)')
@click.option('--port', '-p', help='lana server port (default 8080)')

def command(host, port):
  if host == None:
    host = "localhost"
  if port == None:
    port = "8080"
  cmd = LanaCmd(host, port)
  cmd.cmdloop(intro)

command()