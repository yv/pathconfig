#!/usr/bin/env python
from setuptools import setup

setup(name='pathconfig',
      version='1.0',
      description='On-demand loading and configurable paths',
      author='Yannick Versley',
      author_email='versley@cl.uni-heidelberg.de',
      packages=['pathconfig'],
      package_dir={'': 'py_src'},
      install_requires=['setuptools>=17', 'pyyaml']
      )
