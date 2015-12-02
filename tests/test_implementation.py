#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`test_implementation`
==================

.. module:: test_implementation
    :platform: Unix, Windows
    :synopsis:

.. moduleauthor:: hbldh <henrik.blidh@nedomkull.com>

Created on 2015-11-14

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import six
import numpy as np
from numpy.testing import assert_allclose

from lspopt import lspopt
from .lspopt_ref import lspopt_ref


class TestLSPOptSuite(object):

    def test_different_N(self):
        """Test against reference implementation for different N."""
        def test_fcn(n):
            h1, w1 = lspopt(n)
            h2, w2 = lspopt_ref(n)
            assert_allclose(h1, h2)
            assert_allclose(w1, w2)

        for n in six.moves.range(64, 1024):
            yield test_fcn, n

    def test_different_c(self):
        """Test against reference implementation for different N."""
        def test_fcn(c):
            h1, w1 = lspopt(n=1024, c_parameter=c)
            h2, w2 = lspopt_ref(n=1024, c_parameter=c)
            assert_allclose(h1, h2)
            assert_allclose(w1, w2)

        for c in np.arange(1.1, 30.0, 0.1):
            yield test_fcn, c
