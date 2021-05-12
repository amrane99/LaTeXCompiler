#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module includes helpful functions and the logic behind the program.
@author: Amin Ranem (GitHub: https://github.com/amrane99, LinkedIn: https://www.linkedin.com/in/amin-ranem-4b79b5195)
"""

import os
from tqdm import tqdm
import shutil

def compile_tex_files(tex_engine, bib_engine, no_bib, basedir, auxdir, path, folder_name):
    r"""This function compiles the .pdf file using the passed information."""
    # 1. Make directory for auxiliary files if it does not exist and define dicts for engines
    empty = False
    if not os.path.exists(auxdir):
        os.makedirs(auxdir)
        empty = True
    # Build engines dicts
    tex_engines = {'pdflatex': 'pdflatex --file-line-error --synctex=1 ',
                   'lualatex': 'lualatex ', 'xelatex': 'xelatex '}
    bib_engines = {'biber': 'biber ', 'bibtex': 'bibtex '}

    # 2. Based on engines compile documents
    if no_bib:  # Do not use BibLaTeX
        # Only compile .tex file
        # Compile .tex file two times since Table Of Content can be included, etc.
        for i in tqdm(range(2), ascii=True, desc="Compile LaTeX file(s)"):
            if empty and i != 0:
                # Move auxiliary files
                _move_files(auxdir, basedir)
            # Execute LaTeX engine
            _compile_file(tex_engines[tex_engine], basedir, path)

    # Use BibLaTex --> compile 2 times LaTeX -- 1 time BibLaTex -- 1 time LaTeX
    else:
        # Compile .tex file two times since Table Of Content can be included, etc.
        for i in tqdm(range(4), ascii=True, desc="Compile LaTeX file(s)"):
            if empty and i != 0:
                # Move auxiliary files
                _move_files(auxdir, basedir)
            if i == 2:
                # Execute BibTeX engine
                _compile_file(bib_engines[bib_engine], path.replace('.tex', ''))
            else:
                # Execute LaTeX engine
                _compile_file(tex_engines[tex_engine], basedir, path)

    # Stash auxiliary files
    _stash_auxiliary_files(basedir, auxdir, folder_name)

def _compile_file(engine, path, e_file):
    r"""This function executes a file using the correspodning (provided) engine."""
    # Change directory and execute engine
    os.chdir(path)
    os.system(engine + e_file)
    
def _move_files(dest, target):
    r"""This function extracts all files from a given folder and moves them to the desired path."""
    # Extract all file names
    content = os.listdir(dest)
    for x in content:
        # Move auxiliary files
        shutil.move(os.path.join(dest, x), os.path.join(target, x))

def _stash_auxiliary_files(dest, target, folder_name):
    r"""This function moves all auxiliary files from dest into target. Everything that is not a folder,
        does not end with .pdf or .tex is classified as an auxiliary file."""
    # Stash all auxiliary files into target
    content = os.listdir(dest)
    # Move content to target
    for x in content:
        # Only move auxiliary files
        if not (folder_name in x or '.tex' in x or '.pdf' in x or '.' not in x):
            shutil.move(os.path.join(dest, x), os.path.join(target, x))
