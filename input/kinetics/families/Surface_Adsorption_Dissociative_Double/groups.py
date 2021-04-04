#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Dissociation_Double/groups"
shortDesc = u""
longDesc = u"""
A gas phase double bonded species dissociatively adsorbing to the surface with double bonds.

*2=*3                                     *2          *3
           +           +          ---->   ||    +     ||
               ~*1~        ~*4~          ~*1~        ~*4~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2) * (mol/m3)
so k should be in (m5/mol2/s). We will use sticking coefficients.
"""

template(reactants=["Adsorbate","VacantSite1","VacantSite2"], products=["Adsorbate1","Adsorbate2"], ownReverse=False)

reverse = "Surface_Association_Double"

reactantNum=3
productNum=2

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*2', -1, '*3'],
    ['BREAK_BOND', '*2', 1, '*3'],
    ['FORM_BOND', '*3', 1, '*4'],
    ['CHANGE_BOND', '*3', 1, '*4'],
])

entry(
    index = 1,
    label = "Adsorbate",
    group =
"""
multiplicity [1]
1 *2 R!H u0 px cx {2,D}
2 *3 R!H u0 px cx {1,D}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "VacantSite1",
    group =
"""
1 *1 Xv u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "VacantSite2",
    group =
"""
1 *4 Xv u0 p0 c0
""",
    kinetics = None,
)

#Keep the dissociative adsorption reaction of triplet O2 in kinetic libraries,
#and forbid the singlet O=O entry here
#entry(
#    index = 4,
#    label = "OO",
#    group =
#"""
#multiplicity [1]
#1 *3 O  u0 p2 c0 {2,D}
#2 *2 O  u0 p2 c0 {1,D}
#""",
#    kinetics = None,
#)

entry(
    index = 5,
    label = "OC",
    group =
"""
multiplicity [1]
1 *2 O  u0 p2 c0 {2,D}
2 *3 C  u0 p0 c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "CO2",
    group =
"""
multiplicity [1]
1    O  u0 p2 c0 {3,D}
2 *2 O  u0 p2 c0 {3,D}
3 *3 C  u0 p0 c0 {1,D} {2,D}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "ON",
    group =
"""
multiplicity [1]
1 *3 N  u0 px cx {2,D}
2 *2 O  u0 p2 c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "ONR",
    group =
"""
multiplicity [1]
1 *3 N  u0 p1 c0 {2,D} {3,S}
2 *2 O  u0 p2 c0 {1,D}
3    R  u0 px c0 {1,S}
""",
    kinetics = None,
)

entry(
     index = 9,
     label = "CC",
     group =
 """
 multiplicity [1]
 1 *2 C  u0 p0 c0 {2,D}
 2 *3 C  u0 p0 c0 {1,D} 
 """,
     kinetics = None,
)

entry(
    index = 10,
    label = "NN",
    group =
"""
multiplicity [1]
1 *2 N  u0 p1 c0 {2,D}
2 *3 N  u0 p1 c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "NC",
    group =
"""
multiplicity [1]
1 *2 N  u0 p1 c0 {2,D}
2 *3 C  u0 p1 c0 {1,D}
""",
    kinetics = None,
)

tree(
"""
L1: Adsorbate
    L2: CC
    L2: NN
    L2: NC
    L2: OC
        L3: CO2
    L2: ON
        L3: ONR
L1: VacantSite1
L1: VacantSite2
"""
)

forbidden(
    label = "CO",
    group =
"""
1 *2 C  ux {2,D}
2 *3 O  ux {1,D}
""",
    shortDesc = u"""""",
    longDesc =u"""
Any CO should not match *2 and *3 respectively because of duplicate reactions
""",
)

forbidden(
    label = "NO",
    group =
"""
1 *2 N  ux {2,D}
2 *3 O  ux {1,D}
""",
    shortDesc = u"""""",
    longDesc =u"""
Any NO should not match *2 and *3 respectively because of duplicate reactions
""",
)

forbidden(
    label = "CN",
    group =
"""
1 *2 C  ux {2,D}
2 *3 N  ux {1,D}
""",
    shortDesc = u"""""",
    longDesc =u"""
Any CN should not match *2 and *3 respectively because of duplicate reactions
""",
)

forbidden(
    label = "OO",
    group =
"""
1 *3 O  u0 p2 c0 {2,D}
2 *2 O  u0 p2 c0 {1,D}
""",
    shortDesc = u"""""",
    longDesc =u"""
The ground electronic state of gas phase O2 is triplet by default
""",
)