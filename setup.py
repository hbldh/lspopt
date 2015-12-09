# -*- coding: utf-8 -*-
"""

Release data for the lspopt project.

Copyright (c) 2015, Nedomkull Mathematical Modeling AB.
Created on 2015-11-15 by hbldh <henrik.blidh@nedomkull.com>

"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
from setuptools import setup, find_packages

import lspopt

basedir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(basedir, 'README.md')) as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='lspopt',
    version=lspopt.__version__,
    author=lspopt.__author__,
    author_email=lspopt.__author_email__,
    maintainer=lspopt.__maintainer__,
    maintainer_email=lspopt.__maintainer_email__,
    url=lspopt.__url__,
    download_url=lspopt.__download_url__,
    description=lspopt.__description__,
    long_description=LONG_DESCRIPTION,
    license=lspopt.__license__,
    platforms=lspopt.__platforms__,
    keywords=lspopt.__keywords__,
    classifiers=lspopt.__classifiers__,
    packages=find_packages(exclude=('tests', )),
    package_data={
        'lspopt.data': ['*.npy']
    },
    install_requires=[
        'numpy>=1.6.2',
        'scipy>=0.16.1',
        'six>=1.10.0'
    ],
    dependency_links=[],
    ext_modules=[],
    entry_points={}
)

