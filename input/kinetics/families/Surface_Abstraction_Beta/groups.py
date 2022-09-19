#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_Beta_vdW/groups"
shortDesc = u""
longDesc = u"""
Surface abstraction of one atom to another adsorbate. The bond fission occurs not at the binding atom, but in the beta position of the adsorbate, that is the bond between Atom *2 and *3 is broken. Atom *1 is bonded to the surface (*5). The bond order between *1/*3 and the surface decreases. An example for this reaction is: COH* + CH2* = CO* + CH3*. The bond between *2 and *3 must be single.


 *1-*2--*3  *4             *1=*2   *3-*4
  ||        ||      ---->   |       |
~*5~ +    ~*6~~           ~*5~ +  ~*6~~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s). 
"""

template(reactants=["Donating", "Abstracting"], products=["Adsorbate2","Adsorbate3"], ownReverse=False)

reverse = "Surface_Abstraction_reverse_Beta_vdW"

reactantNum=2
productNum=2

recipe(actions=[
    ['FORM_BOND', '*3', 1, '*4'],
    ['CHANGE_BOND', '*1', -1, '*5'],
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*2', 1, '*3'],
    ['CHANGE_BOND', '*4',-1,'*6']
])

entry(
    index = 1,
    label = "Donating",
    group =
"""
1 *1 R!H u0 px c0 {2,S} {4,[D,T]}
2 *2 R!H u0 px c0 {1,S} {3,S}
3 *3 R   u0 {2,S}
4 *5 Xo  u0 {1,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="Abstracting",
    group =
"""
1 *6 Xo  u0 {2,[D,T,Q]}
2 *4 R!H u0 px c0 {1,[D,T,Q]}	
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "R-C-H",
    group =
"""
1 *1 R!H u0 px c0 {2,S} {4,[D,T]}
2 *2 C u0 px c0 {1,S} {3,S}
3 *3 H   u0 {2,S}
4 *5 Xo  u0 {1,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "R-O-H",
    group =
"""
1 *1 R!H u0 px c0 {2,S} {4,[D,T]}
2 *2 O   u0 p2 c0 {1,S} {3,S}
3 *3 H   u0 {2,S}
4 *5 Xo  u0 {1,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "O",
    group =
"""
1 *4 O   u0 p2 c0 {2,D}
2 *6 Xo  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "C=*",
    group =
"""
1 *4 C  u0 p0 c0 {2,D}
2 *6 Xo u0 p0 c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "C#*",
    group =
"""
1 *4 C  u0 p0 c0 {2,T}
2 *6 Xo u0 p0 c0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "C$*",
    group =
"""
1 *4 C  u0 p0 c0 {2,Q}
2 *6 Xo u0 p0 c0 {1,Q}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "R-R-H",
    group =
"""
1 *1 R!H u0 px c0 {2,S} {4,[D,T]}
2 *2 R!H u0 px c0 {1,S} {3,S}
3 *3 H   u0 {2,S}
4 *5 Xo  u0 {1,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "R-CH3",
    group =
"""
1 *1 R!H u0 px c0 {2,S} {4,[D,T]}
2 *2 C   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 *3 H   u0 {2,S}
4 *5 Xo  u0 {1,[D,T]}
5    H   u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "C",
    group =
"""
1 *4 C  ux px cx {2,[D,T,Q]}
2 *6 Xo u0 p0 c0 {1,[D,T,Q]}
""",
    kinetics = None,
)

tree(
"""
L1: Abstracting
    L2: C
        L3: C=*
        L3: C#*
        L3: C$*
    L2: O
L1: Donating
    L2: R-R-H
        L3: R-C-H
	   L4: R-CH3
        L3: R-O-H
"""
)

