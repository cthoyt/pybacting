# -*- coding: utf-8 -*-

"""CLI for PyBacting."""

import click

__all__ = [
    "main",
]


@click.command()
@click.version_option()
def main():
    """Run the PyBacting CLI."""


if __name__ == "__main__":
    main()
