#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import click
from utils.print import printFiles, getFiles

@click.group()
def cli():
    pass

@click.command()
def printfiles():
    printFiles(getFiles())

cli.add_command(printfiles)

if __name__ == '__main__':
    cli()