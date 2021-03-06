#!/usr/bin/env python
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md")) as f:
    long_description = f.read()


# Get package and author details.
about = {}
with open(path.join(here, "rake_nlp", "__version__.py")) as f:
    exec(f.read(), about)

setup(
    # Name of the module
    name="rake_nlp",
    # Details
    version=about["__version__"],
    description=about["__description__"],
    long_description=long_description,
    # The project's main homepage.
    url=about["__url__"],
    # Author details
    author=about["__author__"],
    author_email=about["__author_email__"],
    # License
    license=about["__license__"],
    packages=["rake_nlp"],
    test_suite="tests",
    keywords="rake text-mining algorithms development",
    classifiers=[
        # Intended Audience.
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        # License.
        "License :: OSI Approved :: BSD 3-Clause",
        # Project maturity.
        "Development Status :: 3 - Alpha",
        # Operating Systems.
        "Operating System :: POSIX",
        # Supported Languages.
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        # Topic tags.
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[],
)
