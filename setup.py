#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

PROJECT_DIR = os.path.dirname(__file__)

setup(
    name='django_sendmail_backend',
    version='0.1.0',
    url='https://github.com/perenecabuto/django_sendmail_backend.git',
    author="Felipe Ramos",
    author_email="perenecabuto@gmail.com",
    description="Its a simple command line sendmail backend for Django",
    long_description=open(os.path.join(PROJECT_DIR, 'README.md')).read(),
    keywords="Django, Python, sendmail, EMAIL_BACKEND, command line, mta",
    license='BSD',
    packages=find_packages(exclude=["tests/"]),
    include_package_data=True,
    install_requires=['Django>=1.4'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
