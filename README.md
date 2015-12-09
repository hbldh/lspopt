# LSPOpt

[![Build Status](https://travis-ci.org/hbldh/lspopt.svg)](https://travis-ci.org/hbldh/lspopt)

This module is a Python implementation of the multitaper window method 
described in [\[1\]](#references) for estimating Wigner spectra for certain locally
stationary processes.

Abstract from [\[1\]](#references):

> This paper investigates the time-discrete multitapers that give a mean square error optimal Wigner spectrum estimate for a class
> of locally stationary processes (LSPs). The accuracy in the estimation of the time-variable Wigner spectrum of the LSP is evaluated
> and compared with other frequently used methods. The optimal multitapers are also approximated by Hermite functions, which is
> computationally more efficient, and the errors introduced by this approximation are studied. Additionally, the number of windows
> included in a multitaper spectrum estimate is often crucial and an investigation of the error caused by limiting this number is made.
> Finally, the same optimal set of weights can be stored and utilized for different window lengths. As a result, the optimal multitapers
> are shown to be well approximated by Hermite functions, and a limited number of windows can be used for a mean square error
> optimal spectrogram estimate.
    
## Installation

Install via pip:

    pip install git+https://github.com/hbldh/lspopt.git#egg=lspopt

## Testing

Test with `nosetests`:

    nosetests tests/ 

Tests are run at every commit to GitHub and the results of this, as well as test 
coverage, can be studied at [Travis CI](https://travis-ci.org/hbldh/lspopt).

## Usage

To generate the taper windows only, use the `lspopt` method:

```python
from lspopt import lspopt
H, w = lspopt(N=256, c_parameter=20.0)
```
    
There is also a convenience method for using the [SciPy spectrogram method](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.spectrogram.html#scipy.signal.spectrogram)
with the `lspopt` multitaper windows:

```python
from lspopt import spectrogram_lspopt
f, t, Sxx = spectrogram_lspopt(x, fs, c_parameter=20.0)
```
    
This can then be plotted with e.g. [matplotlib](http://matplotlib.org/).

### Example

One can generate a [chirp](https://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.signal.chirp.html)
process realisation and run spectrogram methods on this. 

```python
import numpy as np
from scipy.signal import chirp, spectrogram
import matplotlib.pyplot as plt

from lspopt.lsp import spectrogram_lspopt

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
```

![Spectrogram plot](https://hbldh.github.com/lspopt/images/plot.png)
*Top: Using SciPy's spectrogram method. Bottom: Using LSPOpt's spectrogram solution.*

## References

\[1\] [Hansson-Sandsten, M. (2011). Optimal multitaper Wigner spectrum 
estimation of a class of locally stationary processes using Hermite functions. 
EURASIP Journal on Advances in Signal Processing, 2011, 10.](http://asp.eurasipjournals.com/content/pdf/1687-6180-2011-980805.pdf)
