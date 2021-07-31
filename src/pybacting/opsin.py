# -*- coding: utf-8 -*-

"""Java components via :mod:`scyjava`."""

from scyjava import config, jimport

__all__ = [
    "opsin",
]

WORKSPACE_ROOT = "."

ENDPOINT = "io.github.egonw.bacting:managers-opsin:0.0.20"
MANAGER_PATH = "net.bioclipse.managers.OpsinManager"
config.add_endpoints(ENDPOINT)
opsin_class = jimport(MANAGER_PATH)
opsin = opsin_class(WORKSPACE_ROOT)


