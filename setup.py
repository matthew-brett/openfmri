#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Installation script for openfmri package '''
import sys
import os
from os.path import join as pjoin, relpath, sep as psep
import fnmatch

# For some commands, use setuptools.
if len(set(('develop', 'bdist_egg', 'bdist_rpm', 'bdist', 'bdist_dumb',
            'install_egg_info', 'egg_info', 'easy_install', 'bdist_wheel',
            'bdist_mpkg')).intersection(sys.argv)) > 0:
    import setuptools

from distutils.core import setup

import versioneer

CMDCLASS = versioneer.get_cmdclass()


def find_files(root, subdir, globber='*'):
    paths = []
    path = pjoin(root, subdir)
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, globber):
            paths.append(relpath(pjoin(dirpath, filename), root))
    if psep != '/':
        paths = [p.replace(psep, '/') for p in paths]
    return paths


setup(name='openfmri',
      version=versioneer.get_version(),
      cmdclass=CMDCLASS,
      description='Access to local OpenFMRI dataset data from Python',
      author='Matthew Brett',
      author_email='matthew.brett@gmail.com',
      maintainer='Matthew Brett',
      maintainer_email='matthew.brett@gmail.com',
      url='http://github.com/matthew-brett/openfmri',
      packages=['openfmri',
                'openfmri.tests'],
      package_data = {'openfmri.tests':
                      find_files(pjoin('openfmri', 'tests'), 'ds105') +
                      find_files(pjoin('openfmri', 'tests'), 'ds114')},
      license='BSD license',
      classifiers = [
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Scientific/Engineering',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Operating System :: MacOS',
        ],
      long_description = open('README.rst', 'rt').read(),
      )
