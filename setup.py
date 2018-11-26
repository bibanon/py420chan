#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""420chan Python Library.

py420chan is a Python library that gives access to the 420chan API
and an object-oriented way to browse and get board and thread
information quickly and easily.

This program is free software. It comes without any warranty, to
the extent permitted by applicable law. You can redistribute it
and/or modify it under the terms of the Do What The Fuck You Want
To Public License, Version 2, as published by Sam Hocevar. See
the LICENSE file for more details.
"""

from setuptools import setup

setup(
    name='py420chan',
    version='0.0.3',
    description=("Python 420chan API Wrapper. Based on the BASC-py4chan 4chan API Wrapper."),
    long_description=open('README.rst').read(),
    license=open('LICENSE').read(),
    author='Antonizoon Overtwater',
    author_email='antonizoon@bibanon.org',
    url='http://github.com/bibanon/py420chan',
    packages=['py420chan'],
    package_dir={
        'py420chan': 'py420chan',
    },
    package_data={'': ['README.rst', 'LICENSE']},
    install_requires=['requests >= 1.0.0'],
    keywords='420chan api',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
