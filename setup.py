# -*- coding: utf-8 -*-
#
# Copyright (C) 2014-2015 Alexander Shorin
# All rights reserved.
#
# This software is licensed as described in the file LICENSE, which
# you should have received as part of this distribution.
#

import imp
import os
import sys
from os.path import join
from setuptools import setup, find_packages

setup_dir = os.path.dirname(__file__)
mod = imp.load_module(
    'version', *imp.find_module('version', [join(setup_dir, 'aiocouchdb')]))

if sys.version_info < (3, 5):
    raise RuntimeError('aiocouchdb requires Python 3.5+')

long_description = ''.join([
    open(join(setup_dir, 'README.rst')).read().strip(),
    '''

Changes
=======

''',
    open(join(setup_dir, 'CHANGES.rst')).read().strip()
])


setup(
    name='aiocouchdb',
    version=mod.__version__,
    license='BSD',
    url='https://github.com/kaiw/aiocouchdb',

    description='CouchDB client built on top of aiohttp (asyncio)',
    long_description=long_description,

    author='Alexander Shorin, Kai Willadsen',
    author_email='kai.willadsen@gmail.com',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Database :: Front-Ends',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],

    packages=find_packages(),
    test_suite='nose.collector',
    zip_safe=False,

    install_requires=[
        'aiohttp>=3.0',
        'multidict>=4.0,<5.0',
    ],
    extras_require={
        'oauth': [
            'oauthlib==1.0.3'
        ],
        'docs': [
            'sphinx==1.3.1'
        ]
    },
    tests_require=[
        'flake8==2.4.1',
        'nose==1.3.7'
    ]
)
