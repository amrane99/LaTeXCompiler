#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This embodies an example on how to use this module in a Python program once it
hase been installed using pip.
@author: Amin Ranem (GitHub: https://github.com/amrane99, LinkedIn: https://www.linkedin.com/in/amin-ranem-4b79b5195)
"""

# -- Import installed module -- #
from LatexCompiler import LC

# -- Compile existing tex file at path -- #
tex_name = '<full_path_to_tex_file>'      # <-- Specify your tex file there

# -- Now compile the file using module. Module needs to be installed first! -- #
LC.compile_document(tex_engine = 'pdflatex',    # Change engine if desired
                    bib_engine = 'biber',       # Value is not necessary if no_bib = True
                    no_bib = True, path = tex_name, # Provide the full path to the file!
                    folder_name = '.auxiliary_files')
