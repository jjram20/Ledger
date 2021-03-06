#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import click
from utils.print import print_file, print_files, get_files

@click.group()
def cli():
    pass

@click.command(name = 'printfile')
@click.option('--file')
@click.argument('file')
def printfile(file):
    print_file(file)

@click.command(name = 'printall')
def printfiles():
    print_files(get_files())

cli.add_command(printfile)
cli.add_command(printfiles)

if __name__ == '__main__':
    cli()