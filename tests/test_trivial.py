# -*- coding: utf-8 -*-

"""Trivial tests for :mod:`pybacting`."""

import unittest


class TestImport(unittest.TestCase):
    """Test importing :mod:`pybacting`."""

    def test_import(self):
        """Test import."""
        from pybacting import cdk

        self.assertIsNotNone(cdk)
