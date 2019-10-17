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


def random_word():
    c = "kgtdszfvpb"
    v = "aeiou"

    syl = [
        random.choice(c),
        random.choice(v),
        random.choice(c),
        random.choice(v),
        random.choice(c),
    ]

    return "".join(syl)


def entry(args):
    epoch = 0

    lang_a = [random_word() for r in range(5)]
    print("Creating random langs at epoch 0")
    print(lang_a)

    for i in range(10):
        epoch += 1
        if random.randint(0, 10) == 7:
            w = random_word()
            lang_a[random.randint(0, len(lang_a) - 1)] = w
            print("Random new word in lang_a at epoch %i" % epoch)

    print(lang_a)

    enki.quick_enki.main()


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
