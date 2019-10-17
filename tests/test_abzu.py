#!/usr/bin/env python3
# encoding: utf-8

"""
test_abzu
=========

Tests for the `abzu` package.
"""

# Import Python standard libraries
import logging
import random
import sys
import unittest

# Import the library being tested
import abzu

# Setup the logger
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
LOGGER = logging.getLogger("TestLog")


class TestAbzu(unittest.TestCase):
    """
    Class for `abzu` tests.
    """

    def test_random_labels(self):
        assert tuple(abzu.random_labels(5, "myseed")) == (
            "Netio",
            "Soei",
            "Datmisav",
            "Bevave",
            "Zosumo",
        )

    def test_random_species(self):
        assert tuple(abzu.random_species(3, "myseed")) == (
            "Netio sbevaves",
            "Soeis zosummo",
            "Datmissaves ginuces",
        )

    def test_kiss_random_vowel_int(self):
        assert tuple(abzu.kiss.random_vowel_inv(seed="myseed")) == (
            "a",
            "e",
            "i",
            "o",
            "u",
            "ɔ",
            "ɛ",
        )

    def test_kiss_random_syll_pattern(self):
        # testing with non-string seed
        assert abzu.kiss.random_syll_pattern(seed=42) == "CCVC"

    def test_kiss_random_cons_inv(self):
        pattern = abzu.kiss.random_syll_pattern(seed="myseed")
        distr = {
            key: value
            for key, value in abzu.kiss.CONS_INV.items()
            if value["PATTERN"] == pattern
        }
        initials, medials, finals = abzu.kiss.random_cons_inv(distr, seed="myseed")

        assert tuple(initials) == (
            "b",
            "d",
            "f",
            "g",
            "h",
            "j",
            "k",
            "m",
            "n",
            "s",
            "t",
            "w",
            "x",
            "ŋ",
            "θ",
        )
        assert tuple(medials) == (
            "b",
            "d",
            "f",
            "g",
            "h",
            "j",
            "k",
            "m",
            "n",
            "s",
            "t",
            "w",
            "x",
            "ŋ",
            "θ",
        )
        assert tuple(finals) == ()

    def test_kiss_random_frequency(self):
        pattern = abzu.kiss.random_syll_pattern(seed="myseed")
        inv = {}
        inv["vowels"] = abzu.kiss.random_vowel_inv(seed="myseed")
        cons_distr = {
            key: value
            for key, value in abzu.kiss.CONS_INV.items()
            if value["PATTERN"] == pattern
        }
        inv["initials"], inv["medials"], inv["finals"] = abzu.kiss.random_cons_inv(
            cons_distr, seed="myseed"
        )
        phonology = abzu.kiss.random_phonology(inv, param={}, seed="myseed")

        # Testing only some values, it is enough
        self.assertAlmostEqual(phonology["vowels"]["o"], 0.145642, places=4)
        self.assertAlmostEqual(phonology["vowels"]["a"], 0.175801, places=4)
        self.assertAlmostEqual(phonology["vowels"]["u"], 0.185078, places=4)
        self.assertAlmostEqual(phonology["initials"]["g"], 0.084629, places=4)
        self.assertAlmostEqual(phonology["initials"]["w"], 0.083057, places=4)
        self.assertAlmostEqual(phonology["initials"]["n"], 0.086462, places=4)
        self.assertAlmostEqual(phonology["medials"]["x"], 0.011540, places=4)
        self.assertAlmostEqual(phonology["medials"]["d"], 0.086774, places=4)
        self.assertAlmostEqual(phonology["medials"]["h"], 0.059325, places=4)

    def test_kiss_random_words(self):
        assert tuple(abzu.kiss.random_words(5, param={}, seed="myseed")) == (
            "m e n e a w",
            "s e i",
            "ŋ i a g ɔ",
            "ɲ a",
            "m u k a",
        )

    def test_kiss_single_random_word(self):
        assert abzu.kiss.single_random_word(seed="enki") == "ɔ l uː kʰ uː ɛ"


if __name__ == "__main__":
    sys.exit(unittest.main())
