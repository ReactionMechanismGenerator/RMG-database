#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_Double/groups"
shortDesc = u""
longDesc = u"""
Surface bond fission of one species with a double bond into two distinct adsorbates. Atom *1 binds to the surface (*3). The image below shows a single bond, but double is also possible. What matters is that the bond between *1 and *2 must be double.

 *1=*2                  *1     *2
  |             ---->   |||    ||
~*3~ + ~*4~~           ~*3~ + ~*4~~


The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s)
"""

template(reactants=["Combined", "VacantSite"], products=["Adsorbate1", "Adsorbate2"], ownReverse=False)

reverse = "Surface_Association_Double"

reactantNum=2
productNum=2

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*2', 1, '*4'],
    ['CHANGE_BOND', '*2', 1, '*4'],    
    ['CHANGE_BOND', '*1', 1, '*3'],
    ['CHANGE_BOND', '*1', 1, '*3'],	
])

entry(
    index = 1,
    label = "Combined",
    group =
"""
1 *1 R!H u0 px c0 {2,D} {3,[S,D]}
2 *2 R!H u0 px c0 {1,D}
3 *3 Xo  u0 {1,[S,D]}
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
    label = "C=R",
    group =
"""
1 *1 C   u0 px c0 {2,D} {3,[S,D]}
2 *2 R!H u0 px c0 {1,D}
3 *3 Xo  u0 {1,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "C=O",
    group =
"""
1 *1 C  u0 p0 c0 {2,D} {3,[S,D]}
2 *2 O  u0 px c0 {1,D}
3 *3 Xo u0 p0 {1,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "C=C",
    group =
"""
1 *1 C  u0 p0 c0 {2,D} {3,[S,D]}
2 *2 C  u0 px c0 {1,D}
3 *3 Xo u0 p0 {1,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "C=N",
    group =
"""
1 *1 C  u0 p0 c0 {2,D} {3,[S,D]}
2 *2 N  u0 p1 c0 {1,D}
3 *3 Xo u0 p0 {1,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "N=R",
    group =
"""
1 *1 N  u0 p1 c0 {2,D} {3,S}
2 *2 R  u0 px c0 {1,D}
3 *3 Xo u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "N=C",
    group =
"""
1 *1 N  u0 p1 c0 {2,D} {3,S}
2 *2 C  u0 p0 c0 {1,D}
3 *3 Xo u0 p0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: Combined
    L2: C=R
    	L3: C=O
	    L3: C=C
        L3: C=N
    L2: N=R
	L3: N=C
L1: VacantSite
"""
)

forbidden(
    label = "AdsorbateVdW",
    group =
"""
multiplicity [1]
1 *3 Xv  u0 p0 c0
2 *2 R!H ux px cx {3,D}
3 *1 R!H ux px cx {2,D}
"""
)

forbidden(
    label = "Surf",
    group =
"""
1 *1 R!H u0 px c0 {2,D} {3,[S,D]}
2 *2 R!H u0 px c0 {1,D} {4,[S,D,T]}
3 *3 Xo  u0 {1,[S,D]}
4 Xo u0 p0 c0 {2,[S,D,T]}
""",
)
