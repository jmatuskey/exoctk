#!/usr/bin/env python
from setuptools import setup

REQUIRES = ['asteval',
            'astropy',
            'astroquery',
            'batman-package',
            'bibtexparser',
            'bokeh',
            'cython',
            'flask',
            'h5py',
            'lmfit',
            'matplotlib',
            'numba',
            'pandas',
            'pysynphot',
            'scipy',
            'sphinx',
            'svo_filters']

SETUP_REQUIRES = ['numpy']

setup(name='exoctk',
      version='0.2.2',
      description='Observation reduction and planning tools for exoplanet science',
      setup_requires=SETUP_REQUIRES,
      install_requires=REQUIRES,
      author='The ExoCTK Group',
      author_email='exoctk@gmail.com',
      license='MIT',
      url='https://github.com/ExoCTK/exoctk',
      long_description='',
      zip_safe=True,
      use_2to3=False
)
