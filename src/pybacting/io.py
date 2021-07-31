# -*- coding: utf-8 -*-

"""Wrappers around I/O functions in bacting."""

from .cdk import cdk
from .opsin import opsin


def from_smiles(smiles: str):
    """Load a molecule from SMILES."""
    return cdk.fromSMILES(smiles)


def from_IUPAC_name(name: str):
    """Creates a molecule from an IUPAC name."""
    return opsin.parseIUPACName(name)


if __name__ == "__main__":
    print(from_smiles("COC"))
