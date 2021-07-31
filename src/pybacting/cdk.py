# -*- coding: utf-8 -*-

"""Java components via :mod:`scyjava`."""

from scyjava import config, jimport

__all__ = [
    "cdk",
]

WORKSPACE_ROOT = "."

ENDPOINT = "io.github.egonw.bacting:managers-cdk:0.0.20"
MANAGER_PATH = "net.bioclipse.managers.CDKManager"
config.add_endpoints(ENDPOINT)
cdk_class = jimport(MANAGER_PATH)
cdk = cdk_class(WORKSPACE_ROOT)


