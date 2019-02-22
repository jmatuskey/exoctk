#!/usr/bin/env python
from setuptools import setup
from setuptools.command.build_ext import build_ext as _build_ext

class build_ext(_build_ext):
    def finalize_options(self):
        _build_ext.finalize_options(self)
        # Prevent numpy from thinking it is still in its setup process:
        __builtins__.__NUMPY_SETUP__ = False
        import numpy
        self.include_dirs.append(numpy.get_include())


REQUIRES = ['numpy',
            'asteval',
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
      cmdclass={'build_ext': build_ext},
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
