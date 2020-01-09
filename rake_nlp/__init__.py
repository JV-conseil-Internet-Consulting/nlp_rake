# -*- coding: utf-8 -*-



"""
rake-nlp module
~~~~~~~~~~~~~

Usage of Rake class:

    >>> from rake_nlp import Rake
    >>> r = Rake() # With language as English
    >>> r = Rake(language=<language>) # With language set to <language>
    >>> r = Rake(ranking_metric=Metric.<ranking_metric>)

:copyright: (c) 2019 by JV conseil – Internet Consulting.
:license: BSD 3-Clause License, see LICENSE for more details.
"""

from .rake import Rake
