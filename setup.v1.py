#!/usr/bin/env python

from setuptools import setup

setup(name='rake_nlp',
      version='1.0',
      description='Rapid Automatic Keyword Extraction (RAKE) algorithm',
      long_description='A Python implementation of the Rapid Automatic Keyword Extraction (RAKE) algorithm as described in: Rose, S., Engel, D., Cramer, N., & Cowley, W. (2010). Automatic Keyword Extraction from Individual Documents. In M. W. Berry & J. Kogan (Eds.), Text Mining: Theory and Applications: John Wiley & Sons.',
      author='zelandiya, aneesha',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['rake_nlp'],
      package_dir={'rake_nlp': './'},
      package_data={'rake_nlp': ['data/']},
      include_package_data = True,
     )
