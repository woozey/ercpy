#!python
"""Setup for testing, building, distributing and installing the 'Pyramid'-package"""


import os
import sys
import re
import numpy
from setuptools import setup, find_packages


DISTNAME = 'ercpy'
DESCRIPTION = 'PYthon based Reconstruction Algorithm for MagnetIc Distributions'
MAINTAINER = 'Martial Duchamp, Jan Caron, Vadim Migunov'
MAINTAINER_EMAIL = 'martial.duchampl@gmail.com, j.caron@fz-juelich.de, v.migunov@fz-juelich.de'
URL = 'https://github.com/ERCpy/ercpy'
VERSION = '0.1.0-dev'
PYTHON_VERSION = (2, 7)
DEPENDENCIES = {'numpy': (1, 6)}  # TODO: Put all dependencies with recquired version here!
LONG_DESCRIPTION = 'long description (TODO!)'  # TODO: Long description!


def get_package_version(package):
    version = []
    for version_attr in ('version', 'VERSION', '__version__'):
        if (hasattr(package, version_attr) and
                isinstance(getattr(package, version_attr), str)):
            version_info = getattr(package, version_attr, '')
            for part in re.split('\D+', version_info):
                try:
                    version.append(int(part))
                except ValueError:
                    pass
    return tuple(version)


def write_version_py(filename='ercpy/version.py'):
    version_string = "# THIS FILE IS GENERATED BY THE ERCPY SETUP.PY\n" + \
        'version = "{}"\n'.format(VERSION)
    with open(os.path.join(os.path.dirname(__file__), filename), 'w') as vfile:
        vfile.write(version_string)


def check_requirements():
    if sys.version_info < PYTHON_VERSION:
        raise SystemExit('You need Python version %d.%d or later.'
                         % PYTHON_VERSION)
    for package_name, min_version in DEPENDENCIES.items():
        dep_error = False
        try:
            package = __import__(package_name)
        except ImportError:
            dep_error = True
        else:
            package_version = get_package_version(package)
            if min_version > package_version:
                dep_error = True
        if dep_error:
            raise ImportError('You need `%s` version %d.%d or later.'
                              % ((package_name, ) + min_version))


def get_files(rootdir):
    '''Returns a list of .py-files inside rootdir'''
    filepaths = []
    for root, dirs, files in os.walk(rootdir):
        for filename in files:
            if filename.endswith('.py'):
                filepaths.append(os.path.join(root, filename))
    return filepaths


print '\n-------------------------------------------------------------------------------'
print 'checking requirements'
check_requirements()
print 'write version.py'
write_version_py()
setup(name=DISTNAME,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      url=URL,
      download_url=URL,
      version=VERSION,
      packages=find_packages(exclude=['tests']),
      include_dirs=[numpy.get_include()],
      requires=['numpy', 'matplotlib', 'mayavi'],
      scripts=get_files('scripts'),
      test_suite='nose.collector'
      )
print '-------------------------------------------------------------------------------\n'
