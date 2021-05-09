#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
  name = 'lc',         # How you named your package folder (MyLib)
  packages = ['lc'],   # Chose the same as "name"
  version = '0.1',     # Start with a small number and increase it with every change you make
  license='MIT',       # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A program for compiling LaTeX files the convenient way by stashing the auxiliary files into a specified folder.',   # Give a short description about your library
  author = 'Amin Ranem',                   # Type in your name
  author_email = 'aminranem@googlemail.com',      # Type in your E-Mail
  url = 'https://github.com/amrane99/',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/amrane99/LaTeX-Compiler',
  keywords = ['LaTeX', 'Python'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'tqdm',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers, Users',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
  ],
  entry_points={
    'console_scripts': [
        'LaTeX-Compiler = lc.LC:_main',
    ],
  },
)