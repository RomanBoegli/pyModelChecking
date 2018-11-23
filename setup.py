#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.md') as f:
    long_desc = f.read()

setup(name='pyModelChecking',
      version='0.2',
      description='A simple Python model checking package',
      long_description=long_desc,
      long_description_content_type='text/markdown', 
      keywords = "model checking temporal logics kripke structure",
      author='Alberto Casagrande',
      author_email='acasagrande@units.it',
      license='GNU General Public License, version 2',
      url='https://github.com/albertocasagrande/pyModelChecking',
      packages=find_packages(),
      test_suite="tests",
      classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Topic :: Scientific/Engineering",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
      ]
     )
