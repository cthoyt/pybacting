# -*- coding: utf-8 -*-

"""Wrappers around I/O functions in bacting."""

from .api import cdk


def from_smiles(smiles: str):
    """Load a molecule from SMILES."""
    return cdk.fromSMILES(smiles)


if __name__ == "__main__":
    print(from_smiles("COC"))
