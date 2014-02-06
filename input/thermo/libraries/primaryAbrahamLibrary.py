#!/usr/bin/env python
# encoding: utf-8

name = "primaryAbrahamLibrary"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    label = "O2",
    molecule = 
"""
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    thermo = u'0.0',
    shortDesc = u"""0.0 0.0 -0.723 0.0 0.191 !experimental descriptors for molecular oxygen""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Feb  6 13:58:32 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> added this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "HOJ",
    molecule = 
"""
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    thermo = u'0.524',
    shortDesc = u"""0.378 0.309 0.802 0.348 0.146 !descriptors for H2O but with the contribution of 1 OH group to A""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Feb  6 13:58:32 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> added this entry by importing the old RMG database."""),
    ],
)

