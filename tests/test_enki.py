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
        assert tuple(enki.random_labels(5, "myseed")) == (
            "Netio",
            "Soei",
            "Datmisav",
            "Bevave",
            "Zosumo",
        )

    def test_random_species(self):
        assert tuple(enki.random_species(3, "myseed")) == (
            "Netio sbevaves",
            "Soeis zosummo",
            "Datmissaves ginuces",
        )

    def test_kiss_random_vowel_int(self):
        enki.kiss.random_vowel_inv()

    def test_kiss_random_syll_pattern(self):
        enki.kiss.random_syll_pattern()

    def test_kiss_random_cons_inv(self):
        pattern = enki.kiss.random_syll_pattern()
        distr = {
            key: value
            for key, value in enki.kiss.CONS_INV.items()
            if value["PATTERN"] == pattern
        }
        initials, medials, finals = enki.kiss.random_cons_inv(distr)

    def test_kiss_random_frequency(self):
        pattern = enki.kiss.random_syll_pattern()
        inv = {}
        inv["vowels"] = enki.kiss.random_vowel_inv()
        cons_distr = {
            key: value
            for key, value in enki.kiss.CONS_INV.items()
            if value["PATTERN"] == pattern
        }
        inv["initials"], inv["medials"], inv["finals"] = enki.kiss.random_cons_inv(
            cons_distr
        )
        param = {}
        phonology = enki.kiss.random_phonology(inv, param)

    def test_kiss_random_words(self):
        param = {}
        enki.kiss.random_words(5, param)


if __name__ == "__main__":
    sys.exit(unittest.main())
