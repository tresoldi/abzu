#!/usr/bin/env python3
# encoding: utf-8

"""
test_enki
=========

Tests for the `enki` package.
"""

# Import Python standard libraries
import logging
import sys
import unittest

# Import the library being tested
import enki

# Setup the logger
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
LOGGER = logging.getLogger("TestLog")

class TestEnki(unittest.TestCase):
    """
    Class for `enki` tests.
    """

    def test_random_labels(self):
        assert tuple(enki.random_labels(5, "myseed")) == ("Netio", "Soei",
        "Datmisav", "Bevave", "Zosumo")

    def test_random_species(self):
        assert tuple(enki.random_species(3, "myseed")) == ('Netio sbevaves', 'Soeis zosummo', 'Datmissaves ginuces')

if __name__ == "__main__":
    sys.exit(unittest.main())
