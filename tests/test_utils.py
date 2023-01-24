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

import pytest
import numpy as np
from numpy.testing import assert_allclose

from lspopt import utils


def test_create_lsp_realisation():
    """Test that create method is working at least."""
    N = 256
    c = 20.0
    Fs = 8.0
    x, H, Rx = utils.create_lsp_realisation(N, c, Fs)
    assert len(x) == N
    assert_allclose(H.shape, (N, N))
    assert_allclose(Rx.shape, (N, N))


def test_create_lscp_realisation():
    """Test that create method is working at least."""
    N = 256
    c = 1.4
    Fs = 8.0
    m = 12.0
    d = 0.4
    x, H, Rx = utils.create_lscp_realisation(N, c, Fs, m, d)
    assert len(x) == N
    assert_allclose(H.shape, (N, N))
    assert_allclose(Rx.shape, (N, N))


def test_create_mlsp_realisation():
    """Test that create method is working at least."""
    N = 256
    c = [1.4, 20.0]
    Fs = 8.0
    x, H, Rx = utils.create_mlsp_realisation(N, c, Fs)
    assert len(x) == N
    assert_allclose(H.shape, (N, N))
    assert_allclose(Rx.shape, (N, N))
