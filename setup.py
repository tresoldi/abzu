import pathlib
import setuptools
from setuptools import setup, find_packages

# The directory containing this file
LOCAL_PATH = pathlib.Path(__file__).parent

# The text of the README file
README_FILE = (LOCAL_PATH / "README.md").read_text()

# Load requirements, so they are listed in a single place
with open("requirements.txt") as fp:
    install_requires = [dep.strip() for dep in fp.readlines()]

# This call to setup() does all the work
setup(
    name="abzu",
    version="0.1",
    description="System for the simulation of language evolution",
    long_description=README_FILE,
    long_description_content_type="text/markdown",
    url="https://github.com/tresoldi/abzu",
    author="Tiago Tresoldi",
    author_email="tresoldi@shh.mpg.de",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
    ],
    packages=["abzu", "resources"],
    keywords=["linguistics", "language evolution", "simulation", "conlang"],
    include_package_data=True,
    install_requires=install_requires,
    entry_points={"console_scripts": ["abzu=abzu.__main__:main"]},
    test_suite="tests",
    tests_require=[],
    zip_safe=False,
)
