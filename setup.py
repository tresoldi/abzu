import pathlib
from setuptools import setup

# The directory containing this file
LOCAL_PATH = pathlib.Path(__file__).parent

# The text of the README file
README_FILE = (LOCAL_PATH / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="enki",
    version="0.0.1",
    description="Simulate language evolution.",
    long_description=README_FILE,
    long_description_content_type="text/markdown",
    url="https://github.com/tresoldi/enki",
    author="Tiago Tresoldi",
    author_email="tresoldi@shh.mpg.de",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=["enki", "resources"],
    keywords=["language", "evolution", "simulation", "conlang"],
    include_package_data=True,
    install_requires=["alteruphono", "numpy"],
    entry_points={"console_scripts": ["enki=enki.__main__:main"]},
    test_suite="tests",
    tests_require=[],
    zip_safe=False,
)
