#!/usr/bin/env python
# encoding: utf-8

name = "primaryAbrahamLibrary"
shortDesc = u""
longDesc = u"""

"""
entry(
    index        = 1,
    label        = "O2_(T)",
    multiplicity = 3,
    molecule = 
"""
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    thermo = u'0.0',
    shortDesc = u"""0.0 0.0 -0.723 0.0 0.191 !experimental descriptors for molecular oxygen""",
    longDesc = 
u"""

""",
)

entry(
    index        = 2,
    label        = "HOJ",
    multiplicity = 2,
    molecule = 
"""
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    thermo = u'0.524',
    shortDesc = u"""0.378 0.309 0.802 0.348 0.146 !descriptors for H2O but with the contribution of 1 OH group to A""",
    longDesc = 
u"""

""",
)

