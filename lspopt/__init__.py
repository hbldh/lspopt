#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

try:
    from lspopt.lsp import lspopt, spectrogram_lspopt
    from tests.lspopt_ref import lspopt_ref
    from lspopt import utils

    __all__ = ['lspopt', 'spectrogram_lspopt', 'utils']
except ImportError:
    # We will end up here in installation case.
    pass

# Version information.  An empty _version_extra corresponds to a full
# release.  'dev' as a _version_extra string means this is a development
# version.
_version_major = 1
_version_minor = 0
_version_patch = 0
# _version_extra = 'dev1'
# _version_extra = 'a6'
_version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor, _version_patch]

__version__ = '.'.join(map(str, _ver))
if _version_extra:
    __version__ += _version_extra

version = __version__  # backwards compatibility name
version_info = (_version_major, _version_minor, _version_patch, _version_extra)

__name__ = 'lspopt'
__author__ = 'Henrik Blidh'
__author_email__ = 'henrik.blidh@nedomkull.com'
__maintainer__ = 'Henrik Blidh'
__maintainer_email__ = 'henrik.blidh@nedomkull.com'
__license__ = 'MIT'
__description__ = "A Python implementation of a multitaper window method for " \
                  "estimating Wigner spectra for certain locally stationary processes"
__url__ = 'https://github.com/hbldh/lspopt'
__download_url__ = 'https://github.com/hbldh/lspopt/tarball/' + '.'.join(map(str, _ver))
__platforms__ = ['Linux', 'Mac OSX', 'Windows XP/Vista/7/8']
__keywords__ = ['Mathmatical Statistics', 'Multitaper', 'Spectrogram']
__classifiers__ = [
                  'Development Status :: 5 - Production/Stable',
                  'Intended Audience :: Science/Research',
                  'Intended Audience :: Developers',
                  'License :: MIT',
                  'Topic :: Scientific/Engineering',
                  'Operating System :: Microsoft :: Windows',
                  'Operating System :: POSIX',
                  'Operating System :: Unix',
                  'Operating System :: MacOS',
                  'Programming Language :: Python',
                  'Programming Language :: Python :: 2',
                  'Programming Language :: Python :: 2.6',
                  'Programming Language :: Python :: 2.7',
                  'Programming Language :: Python :: 3',
                  'Programming Language :: Python :: 3.3',
                  'Programming Language :: Python :: 3.4',
                  'Programming Language :: Python :: 3.5',
              ],
