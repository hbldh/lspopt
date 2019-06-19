#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

.. moduleauthor:: hbldh <henrik.blidh@nedomkull.com>

Created on 2015-11-13

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from pkg_resources import resource_filename

import numpy as np

__all__ = ["C", "WEIGHTS", "f_h"]

# An array of C parameter values for which weights have been pre-calculated.
C = np.load(resource_filename("lspopt.data", "c.npy")).flatten()
# The pre-calculated Hermite polynomial coefficients
# for the C parameter values above.
WEIGHTS = np.load(resource_filename("lspopt.data", "weights.npy"))


def f_h(n, k):
    """Returns f_h value.

    :param n: Window length of multitaper windows.
    :type n: int
    :param k: Length of non-zero Hermite polynomial coefficient array.
    :type k: int
    :return: The f_h value.
    :rtype: float

    """
    return n / _K_TO_VALUE_.get(k)


# Given length of Hermite polynomial coefficient array, return
# a value to divide N with.
_K_TO_VALUE_ = {
    1: 5.4,
    2: 6.0,
    3: 7.3,
    4: 8.1,
    5: 8.7,
    6: 9.3,
    7: 9.8,
    8: 10.3,
    9: 10.9,
    10: 11.2,
}
