#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
LaTeX Compiler:
    This program can be used to conveniently compile LaTeX documents with a single command.
    NOTE: It is not important that the referenced (LaTeX or image) files are in the same directory as the tex file,
            that will be used in this program, but the referenced files should be in the working directory,
            where the LaTeX/BibTeX commands (program) are executed.
            To use this program the right way, navigate to the directory of the main .tex file and execute the program there, so there
            won't be any LaTeX/BibTeX (No File Found) errors. For more informations on how to use this program read the
            instructions on the GitHub repository: https://github.com/amrane99/LaTeX-Compiler
    @author: Amin Ranem (GitHub: https://github.com/amrane99, LinkedIn: https://www.linkedin.com/in/amin-ranem-4b79b5195)
"""

import os
import argparse
import traceback
from lc.utils.compile_tex_files import compile_tex_files

def compile_document(tex_engine, bib_engine, no_bib, path, folder_name):
    r"""This function compiles .tex files into .pdf files using the submitted information.
        NOTE: It can especially be used for programs that generate (LaTeX) file to compile them
              afterwards into reports (pdf) in an autmoated manner without human steps, e.g.:
              import JC._compile_document as compile_document
              # Code that generates a .tex file
              # ...
              compile_document(...) # Compile the generated .tex file LaTeX using the specified engines etc.
        """
    # 1. Extract necessary paths
    # Get current directory to texfile
    basedir = os.path.dirname(os.path.realpath(path))
    # Define directory /<foldername> for auxiliary files
    auxdir = os.path.join(basedir, folder_name)
    
    # 2. Compile document(s) using tex_engine and bib_engine if no_bib = False
    compile_tex_files(tex_engine, bib_engine, no_bib, basedir, auxdir, path, folder_name)
    
def _main():
    # 1. Build Argumentparser
    parser = argparse.ArgumentParser(description='Compile a Latex file the convenient way by using only one command.'+
                                                  ' The auxiliary files will be stored in a seperate folder, so only the'+
                                                  ' .pdf and .tex files will remain in the working directory.')
    parser.add_argument('-tex_engine', choices=['pdflatex', 'lualatex', 'xelatex'], required=False, default='pdflatex',
                        help='Specify which LaTeX engine to use: pdflatex, lualatex or xelatex.'+
                             ' Default: pdflatex engine will be used to compile.')
    parser.add_argument('-bib_engine', choices=['biber', 'bibtex'], required=False, default='biber',
                        help='Specify which BibTeX engine to use: biber or bibtex.'+
                             ' Default: biber engine will be used to compile.')
    parser.add_argument('-no_bib_engine', action='store_const', const=True, default=False,
                        help='Use this flag if the BibTeX engine should not be used, ie. .tex file has no Bibliography.'+
                            ' Default: BibTex engine will be used.')
    parser.add_argument('-file', action='store', type=str, nargs=1, required=True,
                        help='Specify full path to the main .tex file.')
    parser.add_argument('-aux_folder', action='store', type=str, nargs=1, required=False, default='.latex',
                        help='Specify the name of the folder in which the auxiliary files will be stashed.'+
                             ' Default: All auxiliary files will be saved into /.latex.')

    # 2. Extract arguments
    args = parser.parse_args()
    tex_engine = args.tex_engine
    bib_engine = args.bib_engine
    path = args.file
    folder_name = args.aux_folder
    no_bib = args.no_bib_engine
    if isinstance(path, list):
        path = path[0]
    if isinstance(folder_name, list):
        folder_name = folder_name[0]

    # 3. Compile document(s)
    try:
        compile_document(tex_engine, bib_engine, no_bib, path, folder_name)
        print('Compilation sucessfully finished.')
    except:
        # Print error message
        error = traceback.format_exc()
        print('During the compilation of the files the following error occured: {}.'.format(error))

if __name__ == "__main__":
    _main()