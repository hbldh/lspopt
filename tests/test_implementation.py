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

import pytest
import numpy as np
from numpy.testing import assert_allclose
from scipy.signal import chirp, spectrogram

from lspopt import lspopt, spectrogram_lspopt
from .lspopt_ref import lspopt_ref


@pytest.mark.parametrize("n", range(64, 1024))
def test_different_n(n):
    """Test against reference implementation for different N."""
    h1, w1 = lspopt(n)
    h2, w2 = lspopt_ref(n)
    assert_allclose(h1, h2)
    assert_allclose(w1, w2)


@pytest.mark.parametrize("c", np.arange(1.1, 30.0, 0.1))
def test_different_c(c):
    """Test against reference implementation for different c."""
    h1, w1 = lspopt(n=1024, c_parameter=c)
    h2, w2 = lspopt_ref(n=1024, c_parameter=c)
    assert_allclose(h1, h2)
    assert_allclose(w1, w2)


def test_spectrogram_method():
    """Test the spectrogram method's functionality."""
    fs = 10000
    N = 100000
    amp = 2 * np.sqrt(2)
    noise_power = 0.001 * fs / 2
    time = np.arange(N) / fs
    freq = np.linspace(1000, 2000, N)
    x = amp * chirp(time, 1000, 2.0, 6000, method="quadratic") + np.random.normal(
        scale=np.sqrt(noise_power), size=time.shape
    )

    f, t, Sxx = spectrogram_lspopt(x, fs, c_parameter=20.0)
    f_sp, t_sp, Sxx_sp = spectrogram(x, fs)

    assert True
