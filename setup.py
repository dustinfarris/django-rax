#!/usr/bin/env python
"""
django-rax
==========

Django-rax implements pyrax allowing you to synchronize your static
files with Rackspace Cloud Files.  It also provides an optional
storage backend for your media files if you so desire.

:copyright: (c) 2013 by Dustin Farris
:license: BSD, see LICENSE for more details

"""

from setuptools import setup, find_packages


tests_require = []

install_requires = [
    'Django>=1.4',
    'pyrax==1.3.5']

setup(
    name='django-rax',
    version='0.5',
    author='Dustin Farris',
    author_email='dustin@dustinfarris.com',
    url='https://github.com/dustinfarris/django-rax',
    description='PyRax implementation for Django.',
    long_description=__doc__,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite='runtests.runtests',
    license='BSD',
    include_package_data=True,
    classifiers=['Framework :: Django']
)
