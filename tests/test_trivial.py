# -*- coding: utf-8 -*-

"""Trivial tests for :mod:`pybacting`."""

import unittest

import pybacting


class TestImport(unittest.TestCase):
    """Test importing :mod:`pybacting`."""

    def test_from_smiles(self):
        """Test loading via cdk."""
        mol = pybacting.from_smiles("COOC")
        self.assertIsNotNone(mol)

    def test_from_iupac(self):
        """Test loading via opsin."""
        mol = pybacting.from_iupac_name("benzene")
        self.assertIsNotNone(mol)

    # FIXME issue with loading JNI InChI native code.
    # def test_inchi(self):
    #     """Test getting InChI."""
    #     mol = pybacting.from_iupac_name("methane")
    #     self.assertEqual("InChI=1S/CH4/h1H4", pybacting.get_inchi(mol))
    #     self.assertEqual("VNWKTOKETHGBQD-UHFFFAOYSA-N", pybacting.get_inchi_key(mol))
