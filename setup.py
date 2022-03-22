#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pipenv install twine --dev

import io
import os
from os import path
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'win10toast'
DESCRIPTION = (
    'An easy-to-use Python library for displaying'
    'Windows 10 Toast Notifications'
)
URL = 'https://github.com/jithurjacob/Windows-10-Toast-Notifications'
EMAIL = 'mtroalson@gmail.com'
AUTHOR = 'Malcolm Roalson'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.9'

# What packages are required for this module to be executed?
REQUIRED = [
    "pypiwin32",
    "setuptools"
]

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()


def from_here(relative_path):
    return path.join(path.dirname(__file__), relative_path)


setup(
    name=NAME,
    version=VERSION,
    install_requires=REQUIRED,
    packages=["win10toast"],
    license="BSD",
    url=URL,
    download_url='https://github.com/jithurjacob/Windows-10-Toast-Notifications/tarball/0.9',
    description=DESCRIPTION,
    include_package_data=True,
    package_data={
        '': ['*.txt'],
        'win10toast': ['data/*.ico'],
    },
    long_description=read('README.md'),
    author="Jithu R Jacob",
    author_email="jithurjacob@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        'Operating System :: Microsoft',
        'Environment :: Win32 (MS Windows)',
        "License :: OSI Approved :: MIT License",
    ],
)
