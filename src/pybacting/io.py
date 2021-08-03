# -*- coding: utf-8 -*-

"""Wrappers around I/O functions in bacting."""

from typing import Any

from scyjava import to_python

from .api import cdk, inchi, opsin

Molecule = Any


def from_smiles(smiles: str) -> Molecule:
    """Load a molecule from SMILES."""
    return cdk.fromSMILES(smiles)


def from_iupac_name(name: str) -> Molecule:
    """Create a molecule from an IUPAC name."""
    return opsin.parseIUPACName(name)


def get_inchi(mol: Molecule) -> str:
    """Get an InChI string from a molecule."""
    return inchi.generate(mol).getValue()


def get_inchi_key(mol: Molecule) -> str:
    """Get an InChI key from a molecule."""
    return inchi.generate(mol).getKey()


def get_svg(mol: Molecule) -> str:
    """Get an SVG depicting for a molecule."""
    return to_python(cdk.asSVG(mol))


if __name__ == "__main__":
    print(from_smiles("COC"))
