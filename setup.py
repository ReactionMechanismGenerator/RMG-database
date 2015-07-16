#!/usr/bin/python
# -*- coding: utf-8 -*-

################################################################################
#
#   RMG - Reaction Mechanism Generator
#
#   Copyright (c) 2002-2010 Prof. William H. Green (whgreen@mit.edu) and the
#   RMG Team (rmg_dev@mit.edu)
#
#   Permission is hereby granted, free of charge, to any person obtaining a
#   copy of this software and associated documentation files (the 'Software'),
#   to deal in the Software without restriction, including without limitation
#   the rights to use, copy, modify, merge, publish, distribute, sublicense,
#   and/or sell copies of the Software, and to permit persons to whom the
#   Software is furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#   FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#   DEALINGS IN THE SOFTWARE.
#
################################################################################

try:
    from distutils.core import setup
    from distutils.extension import Extension
except ImportError:
    print 'The distutils package is required to build or install RMG Py.'
    

scripts=['evansPolanyi.py', 'exportKineticsLibraryToChemkin.py',
'exportOldDatabase.py','importChemkinLibrary.py','importJavaKineticsLibrary.py','importJavaThermoLibrary.py',
'importOldDatabase.py','kineticsGroups.py','kineticsTraining.py']

scripts = ['scripts/' + scriptName for scriptName in scripts]


# Initiate the build and/or installation
setup(name='RMG-database',
    version='1.0.0',
    description='Reaction Mechanism Generator Database',
    author='William H. Green and the RMG Team',
    author_email='rmg_dev@mit.edu',
    url='http://reactionmechanismgenerator.github.io/',
    scripts=scripts,
)
