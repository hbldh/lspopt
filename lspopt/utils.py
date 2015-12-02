#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`utils`
==================

.. module:: utils
    :platform: Unix, Windows
    :synopsis: 

.. moduleauthor:: hbldh <henrik.blidh@nedomkull.com>

Created on 2015-11-15, 22:47

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import numpy as np


def create_lsp_realisation(N, c, random_seed=None):
    """Create a realisation of a locally stationary process (LSP).

    For details, see section 2 in [1].

    Parameters
    ----------
    N : int
        Length of the process to generate
    c: float
        Measure of stationarity of the process to generate.
    random_seed: int
        Random seed to apply before generating process.

    Returns
    -------
    p : ndarray
        The process realisation

    References
    ----------
    ...[1] Hansson-Sandsten, M. (2011). Optimal multitaper Wigner spectrum
           estimation of a class of locally stationary processes using Hermite functions.
           EURASIP Journal on Advances in Signal Processing, 2011, 10.

    """
    raise NotImplementedError()


def create_lscp_realisation(N, c, random_seed=None):
    """Create a realisation of a locally stationary chirp process.

    For details, see section 2 in [1].

    Parameters
    ----------
    N : int
        Length of the process to generate
    c: float
        Measure of stationarity of the process to generate.
    random_seed: int
        Random seed to apply before generating process.

    Returns
    -------
    p : ndarray
        The process realisation

    References
    ----------
    ...[1] Hansson-Sandsten, M. (2011). Optimal multitaper Wigner spectrum
           estimation of a class of locally stationary processes using Hermite functions.
           EURASIP Journal on Advances in Signal Processing, 2011, 10.

    """
    raise NotImplementedError()


def create_mlsp_realisation(N, c, random_seed=None):
    """Create a realisation of a Multicomponent locally stationary process.

    For details, see section 2 in [1].

    Parameters
    ----------
    N : int
        Length of the process to generate
    c: float
        Measure of stationarity of the process to generate.
    random_seed: int
        Random seed to apply before generating process.

    Returns
    -------
    p : ndarray
        The process realisation

    References
    ----------
    ...[1] Hansson-Sandsten, M. (2011). Optimal multitaper Wigner spectrum
           estimation of a class of locally stationary processes using Hermite functions.
           EURASIP Journal on Advances in Signal Processing, 2011, 10.

    """
    raise NotImplementedError()
