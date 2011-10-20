#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION = '0.0.2'

setup(name='brukva',
      version=VERSION,
      description='Asynchronous Redis client that works within the Tornado IO loop',
      maintainer='fzzbt',
      maintainere_email='juhanipm@gmail.com',
      license='WTFPL',
      url='http://github.com/fzzbt/brukva',
      keywords=['Redis', 'Tornado'],
      packages=['brukva'],
      test_suite='tests.all_tests',
     )
