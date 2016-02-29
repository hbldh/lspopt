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
import matplotlib
matplotlib.rcParams['text.usetex'] = True
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


def generate_lsp_processes_figures():
    """Generates Figure 1 and Figure 2 from the paper."""
    N = 256
    Fs = 7.0
    t_vector = np.arange(-(N/2), N/2, 1) / Fs
    X, Y = np.meshgrid(t_vector, t_vector)

    random_seed = 1

    x_1, _, Rx_1 = utils.create_lsp_realisation(N, 1.1, Fs, random_seed)
    x_2, _, Rx_2 = utils.create_lsp_realisation(N, 3.0, Fs, random_seed)
    x_3, _, Rx_3 = utils.create_lscp_realisation(N, 1.1, Fs, 2.0, -2.0, random_seed)
    x_4, _, Rx_4 = utils.create_mlsp_realisation(N, (1.1, 20.0), Fs, random_seed)

    Rxs = [
        ('$R_x^{LSP}, c=1.1$', Rx_1),
        ('$R_x^{LSP}, c=3$', Rx_2),
        ('$R_x^{LSCP}, c=1.1, m=2, d=-2$', Rx_3),
        ('$R_x^{MLSP}, c_1=1.1, c_2=20$', Rx_4)
    ]

    for k in six.moves.range(1, 5):
        ax = plt.subplot(2, 2, k)
        ax.contour(X, Y, np.real(Rxs[k - 1][1]))
        ax.axis('square')
        ax.set_title(Rxs[k - 1][0])
        ax.set_xlim([-5.0, 5.0])
        ax.set_ylim([-5.0, 5.0])
        ax.set_xlabel('t')
        ax.set_ylabel('s')

    plt.show()

    xs = [
        ('$x^{LSP}, c=1.1$', x_1),
        ('$x^{LSP}, c=3$', x_2),
        ('$x^{LSCP}, c=1.1, m=2, d=-2$', x_3),
        ('$x^{MLSP}, c_1=1.1, c_2=20$', x_4)
    ]

    for k in six.moves.range(1, 5):
        ax = plt.subplot(2, 2, k)
        ax.plot(t_vector, np.real(xs[k - 1][1]))
        ax.set_title(xs[k - 1][0])
        ax.set_xlim([-10.0, 10.0])
        ax.set_ylim([-1.5, 1.5])
        ax.set_xlabel('t')

    plt.show()


def main():
    #generate_chirp_spectrogram_plot()
    generate_lsp_processes_figures()

if __name__ == "__main__":
    main()
