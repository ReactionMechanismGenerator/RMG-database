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
1 *1 R!H u0 px cx {2,S}
2 *2 R   u0 px cx {1,S}
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
    label = "R-H",
    group =
"""
multiplicity [1]
1 *1 R!H u0 px cx {2,S}
2 *2 H   u0 p0 c0 {1,S}
3 *3 Xv  u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "C-H",
    group =
"""
multiplicity [1]
1 *1 C  u0 px cx {2,S}
2 *2 H  u0 p0 c0 {1,S}
3 *3 Xv u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "O-H",
    group =
"""
multiplicity [1]
1 *1 O  u0 px cx {2,S}
2 *2 H  u0 p0 c0 {1,S}
3 *3 Xv u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "N-H",
    group =
"""
multiplicity [1]
1 *1 N  u0 px cx {2,S}
2 *2 H  u0 p0 c0 {1,S}
3 *3 Xv u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "H2O",
    group =
"""
1 *1 O  u0 p2 c0 {2,S} {3,S}
2 *2 H  u0 p0 c0 {1,S}
3    H  u0 p0 c0 {1,S}
4 *3 Xv u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "C-OH",
    group =
"""
1 *2 O   u0 p2 c0 {2,S} {4,S}
2 *1 C   u0 p0 c0 {1,S}
3 *3 Xv  u0 p0 c0
4    H   u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "CH4",
    group =
"""
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *3 Xv u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "CH2R",
    group =
"""
1 *1 C   u0 px cx {2,S} {3,S} {4,D}
2 *2 H   u0 p0 c0 {1,S}
3    H   u0 p0 c0 {1,S}
4    R!H u0 px cx {1,D}
5 *3 Xv  u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "CH3R",
    group =
"""
1    R!H u0 px cx {2,S}
2 *1 C   u0 px cx {1,S} {3,S} {4,S} {5,S}
3 *2 H   u0 p0 c0 {2,S}
4    H   u0 p0 c0 {2,S}
5    H   u0 p0 c0 {2,S}
6 *3 Xv  u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "C-C",
    group =
"""
multiplicity [1]
1 *1 C  u0 p0 c0 {2,[S,D]}
2 *2 C  u0 p0 c0 {1,[S,D]}
3 *3 Xv u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "C-R",
    group =
"""
multiplicity [1]
1 *1 R!H u0 px cx {2,[S,D]}
2 *2 C   u0 p0 c0 {1,[S,D]}
3 *3 Xv  u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "C2H6",
    group =
"""
1 *1 C u0 p0 c0 {3,S} {4,S} {5,S} 
2    C u0 p0 c0 {6,S} {7,S} {8,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *3 Xv u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "C2H4",
    group =
"""
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7 *3 X u0 p0 c0
""",
    kinetics = None,
)

tree(
"""
L1: Combined
    L2: R-H
        L3: C-H
            	L4: CH4
	     	L4: CH2R
	    		L5: C2H4
	  	L4: CH3R
	    		L5: C2H6
        L3: O-H
        	L4: H2O
        L3: N-H
    L2: C-R
	L3: C-C
    	L3: C-OH       
L1: VacantSite
"""
)

forbidden(
    label = "C-O",
    group =
"""
1 *2 O u0 px cx {2,[S,D]}
2 *1 C u0 {1,[S,D]}
3 *3 Xv u0 p0 c0
""",
    shortDesc = u"""""",
    longDesc =
u"""
O should not match to *2 with a less heavy atom
""",
)

forbidden(
    label = "O-O",
    group =
"""
1 *1 O  u0 p2 {2,S}
2 *2 O  u0 p2 {1,S}
3 *3 Xv u0 p0 c0
""",
    shortDesc = u"""""",
    longDesc =
u"""
No rule for O-O breaking available
""",
)

forbidden(
    label = "H-C",
    group =
"""
1 *2 C u0 {2,S}
2 *1 H u0 {1,S}
3 *3 Xv u0 p0 c0
""",
    shortDesc = u"""""",
    longDesc =
u"""
C should not match to *2 with a less heavy atom
""",
)
