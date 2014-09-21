# -*- coding: utf-8 -*-
"""Python packaging."""
import os
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))

NAME = 'django-plainpasswordhasher'
DESCRIPTION = 'Dummy (plain text) password hashing for Django.'
README = open(os.path.join(here, 'README.rst')).read()
VERSION = open(os.path.join(here, 'VERSION')).read().strip()
PACKAGES = [NAME.replace('-', '_')]
REQUIREMENTS = ['Django',
                'setuptools']
ENTRY_POINTS = {}
LICENSE = 'BSD'
AUTHOR = 'Boris Feld'
EMAIL = 'lothiraldan@gmail.com'
URL = 'https://github.com/novapost/django-plainpasswordhasher'
CLASSIFIERS = ['Development Status :: 4 - Beta',
               'License :: OSI Approved :: BSD License',
               'Programming Language :: Python :: 2',
               'Programming Language :: Python :: 3'
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3.2',
               'Programming Language :: Python :: 3.3',
               'Programming Language :: Python :: 3.4',
               'Programming Language :: Python :: Implementation :: CPython',
               'Programming Language :: Python :: Implementation :: PyPy',
               'Framework :: Django',
               'Topic :: Security :: Cryptography',
               'Topic :: Software Development :: Testing']
KEYWORDS = []


if __name__ == '__main__':  # Don't run setup() when we import this module.
    setup(name=NAME,
          version=VERSION,
          description=DESCRIPTION,
          long_description=README,
          classifiers=CLASSIFIERS,
          keywords=' '.join(KEYWORDS),
          license=LICENSE,
          author=AUTHOR,
          author_email=EMAIL,
          url=URL,
          packages=PACKAGES,
          include_package_data=True,
          zip_safe=False,
          install_requires=REQUIREMENTS,
          entry_points=ENTRY_POINTS)
