#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Installation script for openfmri package '''
import sys

# For some commands, use setuptools.
if len(set(('develop', 'bdist_egg', 'bdist_rpm', 'bdist', 'bdist_dumb',
            'install_egg_info', 'egg_info', 'easy_install', 'bdist_wheel',
            'bdist_mpkg')).intersection(sys.argv)) > 0:
    import setuptools

from distutils.core import setup

import versioneer

CMDCLASS = versioneer.get_cmdclass()

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
      package_data = {'openfmri': [
          'tests/ds105',
          'tests/ds114',
      ]},
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
