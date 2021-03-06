#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup

setup(name='climate_explorer',
      version='1.0',
      description='Provenance tools used by PyWPS with NetCDFs',
      author='Andrej Mihajlovski, Alessandro Spinuso',
      author_email='esgf@knmi.nl',
      packages=['climexp','wpsproc'],
      )
