# __init__.py

# Version of the package
__version__ = "0.1"
__author__ = "Tiago Tresoldi"
__email__ = "tresoldi@shh.mpg.de"

# Build the namespace
from abzu import kiss
from abzu.language import Language

from .textgen import random_labels, random_species
