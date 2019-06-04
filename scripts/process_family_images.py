#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
#                                                                             #
# RMG - Reaction Mechanism Generator                                          #
#                                                                             #
# Copyright (c) 2002-2019 Prof. William H. Green (whgreen@mit.edu),           #
# Prof. Richard H. West (r.west@neu.edu) and the RMG Team (rmg_dev@mit.edu)   #
#                                                                             #
# Permission is hereby granted, free of charge, to any person obtaining a     #
# copy of this software and associated documentation files (the 'Software'),  #
# to deal in the Software without restriction, including without limitation   #
# the rights to use, copy, modify, merge, publish, distribute, sublicense,    #
# and/or sell copies of the Software, and to permit persons to whom the       #
# Software is furnished to do so, subject to the following conditions:        #
#                                                                             #
# The above copyright notice and this permission notice shall be included in  #
# all copies or substantial portions of the Software.                         #
#                                                                             #
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,    #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER      #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING     #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER         #
# DEALINGS IN THE SOFTWARE.                                                   #
#                                                                             #
###############################################################################

"""
This script processes reaction family template images (saved as eps files)
into user friendly files (pdf and pngs).

To use, simply run ``python process_family_images.py``.

This should typically be run whenever a new family is added or an existing
family is updated.

Notes:
  - Make sure you have a working LaTeX installation with pdflatex
  - Make sure you have a working GhostScript installation for epstopdf
  - Make sure you have ImageMagick installed for png generation
  - ImageMagick may have security limitations in place which prevent reading
    eps files. To circumvent these, edit the ``/etc/ImageMagick-6/policy.xml``
    file by changing
        <policy domain="coder" rights="none" pattern="EPS" />
    to
        <policy domain="coder" rights="read|write" pattern="EPS" />
"""

import os
import shutil
import subprocess

try:
    from tqdm import tqdm
except ImportError:
    tqdm = None


def generate_family_pdf():
    """Compiles eps files into single pdf via latex"""
    database_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    fam_dir = os.path.join(database_directory, 'input', 'kinetics', 'families')
    dir_list = os.listdir(fam_dir)
    fam_list = sorted([item for item in dir_list if os.path.isdir(os.path.join(fam_dir, item))])  # Only keep folders

    temp_dir = os.path.join(database_directory, 'temp')
    img_dir = os.path.join(temp_dir, 'images')
    if not os.path.isdir(img_dir):
        os.makedirs(img_dir)

    latex_header = r"""\documentclass{article}
    
    \usepackage[margin=1in]{geometry}
    \usepackage{graphicx,color}
    \graphicspath{{""" + img_dir + '/' + r"""}}
    \usepackage{epstopdf}
    \setcounter{secnumdepth}{0}
    
    \begin{document}
    
    \begin{center}
    \huge
    RMG-Py Reaction Families
    \end{center}
    
    """

    latex_footer = r"""
    \end{document}
    """

    print('Preparing latex file...\n')
    with open(os.path.join(temp_dir, 'rmg_reaction_families.tex'), 'w') as f:
        f.write(latex_header)
        if tqdm is not None:
            iterator = tqdm(fam_list)
        else:
            iterator = fam_list
        for fam in iterator:
            cleaned_name = fam.replace('_', '\_')
            f.write(r'\section{{\texttt{{{0}}}}}'.format(cleaned_name))
            f.write('\n\n')
            img_file = os.path.join(fam_dir, fam, 'template.eps')
            f.write(r'\begin{center}')
            f.write('\n')
            if os.path.isfile(img_file):
                filename = fam + '.eps'
                new_file = os.path.join(temp_dir, 'images', filename)
                shutil.copyfile(img_file, new_file)
                f.write(r'\includegraphics[scale=0.8]{{{0}}}'.format(filename))
                f.write('\n')
            else:
                f.write(r'Image Not Available')
                f.write('\n')
            f.write(r'\end{center}')
            f.write('\n\n')

        f.write(latex_footer)

    print('Compiling latex file...\n')
    cwd = os.getcwd()
    os.chdir(temp_dir)
    subprocess.check_call(['pdflatex', '-shell-escape', '-interaction=nonstopmode', 'rmg_reaction_families.tex'])
    shutil.copyfile('rmg_reaction_families.pdf', os.path.join(database_directory, 'families', 'rmg_reaction_families.pdf'))
    os.chdir(cwd)
    shutil.rmtree(temp_dir)


def generate_family_pngs():
    """Converts eps files to png files located in RMG-database/families/images"""
    database_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    fam_dir = os.path.join(database_directory, 'input', 'kinetics', 'families')
    dir_list = os.listdir(fam_dir)
    fam_list = sorted([item for item in dir_list if os.path.isdir(os.path.join(fam_dir, item))])  # Only keep folders

    img_dir = os.path.join(database_directory, 'families', 'images')
    if not os.path.isdir(img_dir):
        os.makedirs(img_dir)

    print('Converting eps files to png files...\n')
    if tqdm is not None:
        iterator = tqdm(fam_list)
    else:
        iterator = fam_list
    for fam in iterator:
        eps_file = os.path.join(fam_dir, fam, 'template.eps')
        if os.path.isfile(eps_file):
            filename = fam + '.png'
            png_file = os.path.join(img_dir, filename)
            # -colorspace rgb gives transparent background, -density sets resolution
            subprocess.check_call(['convert', '-colorspace', 'rgb', '-density', '300', eps_file, png_file])


if __name__ == '__main__':
    generate_family_pdf()
    generate_family_pngs()
