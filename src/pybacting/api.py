# -*- coding: utf-8 -*-

"""Java components via :mod:`scyjava`"""

from scyjava import config, jimport

__all__ = [
    'cdk',
]

ENDPOINT = 'io.github.egonw.bacting:managers-cdk:0.0.20'
CDKMANAGER_PATH = 'net.bioclipse.managers.CDKManager'
WORKSPACE_ROOT = '.'

config.add_endpoints(ENDPOINT)
cdk_class = jimport(CDKMANAGER_PATH)
cdk = cdk_class(WORKSPACE_ROOT)
