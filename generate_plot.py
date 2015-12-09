#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`generate_plot`
====================

Created by hbldh <henrik.blidh@nedomkull.com>
Created on 2015-12-02

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import six
import numpy as np
from scipy.signal import chirp, spectrogram
import matplotlib.pyplot as plt

from lspopt.lsp import spectrogram_lspopt
import lspopt.utils as utils


def generate_chirp_spectrogram_plot():
    fs = 10e3
    N = 1e5
    amp = 2 * np.sqrt(2)
    noise_power = 0.001 * fs / 2
    time = np.arange(N) / fs
    freq = np.linspace(1e3, 2e3, N)
    x = amp * chirp(time, 1e3, 2.0, 6e3, method='quadratic') + \
        np.random.normal(scale=np.sqrt(noise_power), size=time.shape)

    f, t, Sxx = spectrogram(x, fs)

    ax = plt.subplot(211)
    ax.pcolormesh(t, f, Sxx)
    ax.set_ylabel('Frequency [Hz]')
    ax.set_xlabel('Time [sec]')

    f, t, Sxx = spectrogram_lspopt(x, fs, c_parameter=20.0)

    ax = plt.subplot(212)
    ax.pcolormesh(t, f, Sxx)
    ax.set_ylabel('Frequency [Hz]')
    ax.set_xlabel('Time [sec]')

    plt.show()


def generate_lsp_processes_covariance_matrix_levelcurves():

    N = 256
    Fs = 7.0
    t_vector = np.arange(-(N/2), N/2, 1) / Fs
    X, Y = np.meshgrid(t_vector, t_vector)

    _, _, Rx_1 = utils.create_lsp_realisation(N, 1.1, Fs)
    _, _, Rx_2 = utils.create_lsp_realisation(N, 3.0, Fs)
    _, _, Rx_3 = utils.create_lscp_realisation(N, 1.1, Fs, 2.0, -2.0)
    _, _, Rx_4 = utils.create_mlsp_realisation(N, (1.1, 20.0), Fs)

    Rxs = [Rx_1, Rx_2, Rx_3, Rx_4]

    for k in six.moves.range(1, 5):
        ax = plt.subplot(2, 2, k)
        ax.contour(X, Y, np.real(Rxs[k - 1]))
        ax.axis('square')
        ax.set_xlim([-5.0, 5.0])
        ax.set_ylim([-5.0, 5.0])

    plt.show()


def main():
    generate_chirp_spectrogram_plot()
    generate_lsp_processes_covariance_matrix_levelcurves()

if __name__ == "__main__":
    main()
