#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from distutils.core import setup

requirements = [x.strip() for x in open('requirements.txt').readlines()]

setup(
    name='tusubtitulo',
    version='0.0.1',
    author='Luis López',
    author_email='ldotlopez@gmail.com',
    py_modules=['tusubtitulo'],
    scripts=[],
    url='https://github.com/ldotlopez/tusubtitulo',
    license='LICENSE.txt',
    description='API and command line downloader for tusubtitulo.com',
    long_description=open('README.md').read(),
    install_requires=requirements
)
