#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='asynchronous-rabi-experiment',
      version='1.0.0',
      description='Test the TopChef stack by running remote experiments',
      author='Michal Kononenko',
      author_email='mkononen@uwaterloo.ca',
      packages=find_packages(exclude=['*.tests.', '*.tests', 'tests.*']),
      install_requires=[
          'requests==2.18.1'
      ]
)
