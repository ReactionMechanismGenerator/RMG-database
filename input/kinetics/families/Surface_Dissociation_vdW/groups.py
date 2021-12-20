#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_vdW/groups"
shortDesc = u""
longDesc = u"""
Surface bond fission of one vdW species into two distinct adsorbates. Atom *3 is vdW, but we leave that out of the graph.

 *1--*2                 *1     *2
  :            ---->     |      |
~*3~ + ~*4~~           ~*3~ + ~*4~~


The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s)
"""

template(reactants=["Combined", "VacantSite"], products=["Adsorbate1", "Adsorbate2"], ownReverse=False)

reverse = "Surface_Association_vdW"

reactantNum=2
productNum=2

recipe(actions=[
    ['CHANGE_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*4'],
    ['BREAK_BOND', '*1', 1, '*2'],
])

entry(
    index = 1,
    label = "Combined",
    group =
"""
multiplicity [1]
1 *1 R!H ux px cx {2,S}
2 *2 R   ux px cx {1,S}
3 *3 Xv  u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 2,
    label="VacantSite",
    group =
"""
1 *4 Xv u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "C-OH",
    group =
"""
1 *1 C   u0 p0 c0 {2,S}
2 *2 O   u0 p2 c0 {1,S} {4,S}
3 *3 Xv  u0 p0 c0
4    H   u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "C-H",
    group =
"""
1 *1 C   u0 p0 c0 {2,S}
2 *2 H   u0 p0 c0 {1,S}
3 *3 Xv  u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "H2O",
    group =
"""
multiplicity [1]
1 *1 O  u0 p2 c0 {2,S} {3,S}
2 *2 H  u0 p0 c0 {1,S}
3    H  u0 p0 c0 {1,S}
4 *3 Xv u0 p0 c0
""",
    kinetics = None,
)

tree(
"""
L1: Combined
	L2: C-H
	L2: C-OH
	L2: H2O
L1: VacantSite
"""
)

#forbidden(
#    label = "CH4",
#    group =
#"""
#multiplicity [1]
#1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
#2 *2 H u0 p0 c0 {1,S}
#3    H u0 p0 c0 {1,S}
#4    H u0 p0 c0 {1,S}
#5    H u0 p0 c0 {1,S}
#6 *3 Xv u0 p0 c0
#""",
#    shortDesc = u"""CH4 adsorbs on Ni but doesn't lead to anything, that's why it is forbidden BK""",
#    longDesc =
#u"""
#""",
#)
