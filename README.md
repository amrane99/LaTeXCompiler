# Convenient LaTeX Compiler
This repository represents a convenient LaTeX Compiler, that can be used to compile LaTeX `.tex` files with only one command by specifying the desired engines that should be used -- LaTeX and BibTeX. The simple fact that LaTeX previewers like [TeXShop](https://pages.uoregon.edu/koch/texshop/) -- for MacOS Systems at least -- do not provide the function to store the auxiliary files into an extra folder was the originator of this work. The auxiliary files are simply stashed in the working directory instead. [TeXstudio](https://www.texstudio.org) eg. provides the --`-aux-directory <directory>` command for Windows users to specify the folder in which the auxiliary files will be stashed instead. With this module, it is possible (for each system -- Linux, MacOS or Windows) to compile LaTeX files in such a way, that the auxiliary files will be stored in an extra folder. Further is the process embedded into a function, which enables the possibility to use this work for compiling generated LaTeX files in an autonomous way without compiling the generated file using LaTeX and BibTex engines by hand.

## Table Of Contents

[Installation](#installation)

[Application](#application)
  * [Conventional use from Terminal](#conventional-use-from-terminal)
  * [Advanced use in Python program](#advanced-use-in-python-program)

[License](#license)


## Installation
To install the module simply using PyPi, like:

`pip install LatexCompiler`

or directly from the repository:

`pip install git+https://github.com/amrane99/LatexCompiler`


## Application
The LatexCompiler can be used for just compiling a .tex file or it can be embedded in a system that generates .tex files to compile it after the creation. 

### Conventional use from Terminal
To compile a .tex file it is very important to understand, that the auxiliary files are generated where the *python command* is executed from, for instance the location from where the *LaTeX and BibTeX engines commands* are launched. This means, LaTeX searches for the files like pictures or other .tex files that are included/referenced in a .tex file in the directory where the LaTeX command is launched, not the directory where the .tex file itself is located. In such cases, LaTeX will throw errors like `file not found`, for reference see [this post](https://tex.stackexchange.com/questions/95617/includegraphics-file-not-found-even-when-in-same-directory). So before using this method, it is important to navigate to the directory where the .tex file lives that needs to be compiled:
```bash
		  ~ $ source ~/.bashrc
		  ~ $ source activate <your_anaconda_env>
<your_anaconda_env> $ cd LaTeX_project_XX
<your_anaconda_env> $ LatexCompiler -file <file_name>.tex
```
Note that the first and second commands are only necessary, if this module is installed in an anaconda environment. If it is installed in the systems environment, these steps can be skipped. The execution of the fourth command will compile the LaTeX file `<file_name>.tex` with the default settings the following way:
```bash
 pdflatex --file-line-error --synctex=1 <full_path_to_file_name>.tex
 pdflatex --file-line-error --synctex=1 <full_path_to_file_name>.tex
 biber <file_name>.tex
 pdflatex --file-line-error --synctex=1 <full_path_to_file_name>.tex
```
Further the auxiliary files will be stashed in the auxiliary `.latex/` directory that is on the same level located as  `<full_path_to_file_name>.tex`.
Note that the algorithm will first check if the auxiliary directory already exists, in which case the auxiliary files can be used in the LaTeX command. That way, `<full_path_to_file_name>.tex` only needs to be compiled once before using BibTeX to include the changes. With the following flags, the used engines and name of auxiliary folder can be specified:

| Tag_name | description | required | choices | default | 
|:-:|-|:-:|:-:|:-:|
| `-file` | Specify *[full] path* to the main .tex file. | yes | -- | -- |
| `-tex_engine` | Specify which LaTeX engine to use. | no | `pdflatex, lualatex, xelatex` | `pdflatex` |
| `-bib_engine` | Specify which BibTeX engine to use. | no | `biber, bibtex` | `biber` |
| `-no_bib_engine` | Use this flag if the BibTeX engine should not be used, ie. .tex file has no Bibliography. | no | -- | `False` |
| `-aux_folder` | Specify the name of the folder in which the auxiliary files will be stashed. | no | -- | `.latex` |

#### Example use cases
1. If the LaTeX `example.tex` file, located at `/LaTeX_project_XX` needs to be executed using LuaLaTeX and BibTeX, by stashing the auxiliary files into `/LaTeX_project_XX/.aux` the command would be the following: 
```bash
		  ~ $ source ~/.bashrc
		  ~ $ source activate <your_anaconda_env>
<your_anaconda_env> $ cd LaTeX_project_XX
<your_anaconda_env> $ LatexCompiler
					  -file example.tex
					  -tex_engine lualatex -bib_engine bibtex
					  -aux_folder .aux
```
2. If the LaTeX `example.tex` file, located at `/LaTeX_project_XX` needs to be executed using XeLaTeX without using a BibTeX engine since it does not have a bibliography and stashing the auxiliary files into `/LaTeX_project_XX/auxiliary_files` the command would be the following: 
```bash
		  ~ $ source ~/.bashrc
		  ~ $ source activate <your_anaconda_env>
<your_anaconda_env> $ cd LaTeX_project_XX
<your_anaconda_env> $ LatexCompiler
					  -file example.tex
					  -tex_engine xelatex -no_bib_engine
					  -aux_folder auxiliary_files
```
Note that in the second example no BibTeX engine will be used, so the command
```bash
 xelatex /LaTeX_project_XX/example.tex
```

would be executed only once, if the auxiliary files at `/LaTeX_project_XX/auxiliary_files` exist and twice otherwise. In both examples, the first two steps can be omitted, if this module is installed in the systems environment. Further, if the command will be executed within the folder of the .tex file, only the .tex file itself and not the full path needs to be provided.

### Advanced use in Python program
Let's assume there is a Python algorithm/program that automatically generates a .tex file. The in this module provided function `compile_document(tex_engine, bib_engine, no_bib, path, folder_name)` can then be used in the program after saving the generated file to compile the file as well:
```python
from LatexCompiler.LatexCompiler import LC
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
