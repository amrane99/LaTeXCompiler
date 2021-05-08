#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='LaTeX Compiler',
    version='1.0',
    description='A program for compiling LaTeX files the convenient way by stashing the auxiliary files into a specified folder.',
    url='https://github.com/amrane99/LaTeX-Compiler',
    keywords='python latex',
    package_dir={"": "lc"},
    packages=find_packages(include=['lc', 'lc.*']),
    author='Amin Ranem',
    author_email='aminranem@googlemail.com',
    license='MIT License',
    entry_points={'console_scripts': [
        'lc=lc.LC:main',
    ]},
)