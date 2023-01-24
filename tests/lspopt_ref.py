#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`lspopt_ref`
==================

.. module:: lspopt_ref
    :platform: Unix, Windows
    :synopsis:

.. moduleauthor:: hbldh <henrik.blidh@nedomkull.com>

Created on 2015-11-13

"""

import numpy as np

from lspopt.data import C, WEIGHTS


def lspopt_ref(n, c_parameter=20.0):
    """Reference implementation of the multitaper window calculation.

    A direct port of Matlab code obtained from the author of the paper.

    Parameters
    ----------
    n : int
        Length of multitaper windows
    c_parameter : float
        The parameter `c` in [1]. Default is 20.0

    Returns
    -------
    H : ndarray
        Multitaper windows, of size [n x n]
    w : ndarray
        Array of taper window weights.

    References
    ----------
    ...[1] Hansson-Sandsten, M. (2011). Optimal multitaper Wigner spectrum
           estimation of a class of locally stationary processes using Hermite functions.
           EURASIP Journal on Advances in Signal Processing, 2011, 10.

    """
    c = C
    Wmat = WEIGHTS

    k = int(round((c_parameter - 1) * 10))
    c = c[k]
    wei = Wmat[:, k]
    wei = wei[np.nonzero(wei)]
    K = len(wei)
    if K > 10:
        K = 10
        wei = wei[:K]
    wei /= np.sum(wei)

    t1 = np.arange(-(n / 2) + 1, (n / 2) + 0.1, step=1.0) / _get_f1(n, K)
    h = np.ones((n,))
    if K > 1:
        h = np.vstack((h, 2 * t1))
        if K > 2:
            for i in range(1, K - 1):
                h = np.vstack((h, (2 * t1 * h.T[:, i]) - 2 * i * h.T[:, i - 1]))
    H = h.T * np.outer(np.exp(-(t1 ** 2) / 2), np.ones((K,), "float"))

    for i in range(K):
        H[:, i] = H[:, i] / np.sqrt(H[:, i].T.dot(H[:, i]))  # Norm

    return H.T, wei


def _get_f1(N, K):
    if K == 1:
        return N / 5.4
    if K == 2:
        return N / 6.
    if K == 3:
        return N / 7.3
    if K == 4:
        return N / 8.1
    if K == 5:
        return N / 8.7
    if K == 6:
        return N / 9.3
    if K == 7:
        return N / 9.8
    if K == 8:
        return N / 10.3
    if K == 9:
        return N / 10.9
    if K == 10:
        return N / 11.2
    raise ValueError("K was not in [1, 10]!")
