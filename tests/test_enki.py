#!/usr/bin/env python3
# encoding: utf-8

"""
test_enki
=========

Tests for the `enki` package.
"""

# Import 3rd-party libraries
import unittest

# Import the library being tested
import enki


class TestEnki(unittest.TestCase):
    """
    Class for `enki` tests.
    """

    def test_temp(self):
        assert 2 + 2 == 4

    def test_error(self):
        assert 2 + 2 == 5

    def test_quick(self):
        enki.quick_enki.main()
