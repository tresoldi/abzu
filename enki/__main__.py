#!/usr/bin/env python3
# encoding: utf-8

"""
__main__.py

Module for command-line execution of Enki.
"""

# Import Python standard libraries
import argparse
import logging
import random

import enki


def quick_test():
    param = {}

    print("--> random_vowel_inv()")
    for i in range(4):
        print("  %i %s" % (i, enki.kiss.random_vowel_inv()))
    print()

    print("--> random_syll_pattern()")
    for i in range(4):
        print("  %i %s" % (i, enki.kiss.random_syll_pattern()))
    print()

    print("--> random_cons_inv()")
    for i in range(4):
        pattern = enki.kiss.random_syll_pattern()
        distr = {
            key: value for key, value in enki.kiss.CONS_INV.items() if value["PATTERN"] == pattern
        }
        initials, medials, finals = enki.kiss.random_cons_inv(distr)
        print(
            "  %i %i/%i/%i (%s)"
            % (i, len(initials), len(medials), len(finals), pattern)
        )
    print()

    print("--> random_global_freq()")
    base_freq = {v["GRAPHEME"]: float(v["FREQUENCY"]) for v in enki.kiss.PHONEME_FREQ.values()}
    print("  items: %i" % len(base_freq))
    print()

    print("--> random_frequency()")
    for i in range(4):
        pattern = enki.kiss.random_syll_pattern()
        inv = {}
        inv["vowels"] = enki.kiss.random_vowel_inv()
        cons_distr = {
            key: value for key, value in enki.kiss.CONS_INV.items() if value["PATTERN"] == pattern
        }
        inv["initials"], inv["medials"], inv["finals"] = enki.kiss.random_cons_inv(cons_distr)
        phonology = enki.kiss.random_phonology(inv, param)

        print(
            "  items: %i/%i/%i/%i"
            % (
                len(phonology["vowels"]),
                len(phonology["initials"]),
                len(phonology["medials"]),
                len(phonology["finals"]),
            )
        )
    print()

    print("--> random_words()")
    for i in range(4):
        print("  l:", enki.kiss.random_words(5, param))
    print()


def entry(args):
    epoch = 0

    lang_a = enki.textgen.random_labels(5)
    print("Creating random langs at epoch 0")
    print(lang_a)

    for i in range(10):
        epoch += 1
        if random.randint(0, 10) == 7:
            w = enki.textgen.random_labels(1)[0]
            lang_a[random.randint(0, len(lang_a) - 1)] = w
            print("Random new word in lang_a at epoch %i" % epoch)

    print(lang_a)

    quick_test()


def main():
    # Define the parser for when called from command line
    parser = argparse.ArgumentParser(description="Enki language simulation.")
    parser.add_argument(
        "--seed", type=str, help="The RNG seed, for reproducibility. Defaults to None."
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Whether to log debug information. Defaults to False.",
    )
    ARGS = parser.parse_args()

    # Set the requested logging level (either DEBUG or INFO)
    if ARGS.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    # Log command-line options, if in debug
    logging.debug(str(ARGS))

    # Apply random seed, if any
    logging.debug("Setting the RNG seed to `%s`", ARGS.seed)
    random.seed(ARGS.seed)

    entry(ARGS)
