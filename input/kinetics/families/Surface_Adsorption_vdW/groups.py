#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_vdW/groups"
shortDesc = u""
longDesc = u"""
Physisorption of a gas-phase species onto the surface.

 *1         *1
     ---->   :
~*2~       ~*2~~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m3)
so k should be in (m3/mol/s). We will use sticking coefficients.
"""

template(reactants=["Adsorbate", "VacantSite"], products=["Adsorbed"], ownReverse=False)

reverse = "Surface_Desorption_vdW"

reactantNum=2
productNum=1

recipe(actions=[
    ['FORM_BOND', '*1', 0, '*2']
])

entry(
    index = 1,
    label = "Adsorbate",
    group =
"""
multiplicity [1]
1 *1 R u0 px c0
""",
    kinetics = None,
)

entry(
    index = 2,
    label="VacantSite",
    group =
"""
1 *2 Xv u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "H",
    group =
"""
multiplicity [1]
1 *1 H u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "H2",
    group =
"""
multiplicity [1]
1 *1 H u0 p0 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "CH4",
    group =
"""
multiplicity [1]
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "NH3",
    group =
"""
multiplicity [1]
1    N u0 p1 c0 {2,S} {3,S} {4,S}
2 *1 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "C",
    group =
"""
multiplicity [1]
1 *1 C   u0 px c0 {2,[S,D,T,Q]}
2    R!H u0 px cx {1,[S,D,T,Q]}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "CC",
    group =
"""
multiplicity [1]
1 *1 C u0 px c0 {2,[S,D,T,Q]}
2    C u0 px cx {1,[S,D,T,Q]}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "C-C",
    group =
"""
multiplicity [1]
1 *1 C u0 px c0 {2,S}
2    C u0 px cx {1,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "C2H6",
    group =
"""
multiplicity [1]
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "C=C",
    group =
"""
multiplicity [1]
1 *1 C u0 px c0 {2,D}
2    C u0 px cx {1,D}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "C2H4",
    group =
"""
multiplicity [1]
1 *1 C u0 p0 c0 {2,D} {3,S} {5,S}
2    C u0 p0 c0 {1,D} {4,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "C#C",
    group =
"""
multiplicity [1]
1 *1 C u0 px c0 {2,T}
2    C u0 px cx {1,T}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "C2H2",
    group =
"""
multiplicity [1]
1 *1 C u0 p0 c0 {2,T} {3,S}
2    C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "CN",
    group =
"""
multiplicity [1]
1 *1 C u0 px c0 {2,[S,D,T]}
2    N u0 px cx {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "C-N",
    group =
"""
multiplicity [1]
1 *1 C u0 px c0 {2,S}
2    N u0 px cx {1,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "CH3NH2",
    group =
"""
multiplicity [1]
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    N u0 p1 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "C#N",
    group =
"""
multiplicity [1]
1 *1 C u0 px c0 {2,T}
2    N u0 px cx {1,T}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "CHN",
    group =
"""
multiplicity [1]
1    N u0 p1 c0 {2,T} 
2 *1 C u0 p0 c0 {1,T} {3,S}
3    H u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "CO",
    group =
"""
multiplicity [1]
1 *1 C u0 px c0 {2,[S,D]}
2    O u0 px cx {1,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "C-O",
    group =
"""
multiplicity [1]
1 *1 C u0 px c0 {2,S}
2    O u0 px cx {1,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "CH3OH",
    group =
"""
multiplicity [1]
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "C=O",
    group =
"""
multiplicity [1]
1 *1 C u0 px c0 {2,D}
2    O u0 px cx {1,D}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "CH2O",
    group =
"""
multiplicity [1]
1    O u0 p2 c0 {2,D}
2 *1 C u0 p0 c0 {1,D} {3,S} {4,S}
3    H u0 p0 c0 {2,S}
4    H u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "CO2",
    group =
"""
multiplicity [1]
1    O u0 p2 c0 {3,D}
2    O u0 p2 c0 {3,D}
3 *1 C u0 p0 c0 {1,D} {2,D}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "N",
    group =
"""
multiplicity [1]
1 *1 N   u0 px c0 {2,[S,D,T]}
2    R!H u0 px cx {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "NO",
    group =
"""
multiplicity [1]
1 *1 N u0 px c0 {2,[S,D]}
2    O u0 px cx {1,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "N-O",
    group =
"""
multiplicity [1]
1 *1 N u0 px c0 {2,S}
2    O u0 px cx {1,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "H3NO",
    group =
"""
multiplicity [1]
1    O u0 p2 c0 {2,S} {5,S}
2 *1 N u0 p1 c0 {1,S} {3,S} {4,S}
3    H u0 p0 c0 {2,S}
4    H u0 p0 c0 {2,S}
5    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "N=O",
    group =
"""
multiplicity [1]
1 *1 N u0 px c0 {2,D}
2    O u0 px cx {1,D}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "HNO",
    group =
"""
multiplicity [1]
 1    O u0 p2 c0 {2,D}
 2 *1 N u0 p1 c0 {1,D} {3,S}
 3    H u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "NN",
    group =
"""
multiplicity [1]
1 *1 N u0 px c0 {2,[S,D,T]}
2    N u0 px cx {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "N-N",
    group =
"""
multiplicity [1]
1 *1 N u0 px c0 {2,S}
2    N u0 px cx {1,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "N2H4",
    group =
"""
multiplicity [1]
1 *1 N u0 p1 c0 {2,S} {3,S} {4,S}
2    N u0 p1 c0 {1,S} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "N=N",
    group =
"""
multiplicity [1]
1 *1 N u0 px c0 {2,D}
2    N u0 px cx {1,D}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "N2H2",
    group =
"""
multiplicity [1]
1 *1 N u0 p1 c0 {2,D} {3,S}
2    N u0 p1 c0 {1,D} {4,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "N#N",
    group =
"""
multiplicity [1]
1 *1 N u0 px c0 {2,T}
2    N u0 px c0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "O",
    group =
"""
multiplicity [1]
1 *1 O u0 px c0
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "O-H",
    group =
"""
multiplicity [1]
1 *1 O u0 px c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "H2O",
    group =
"""
multiplicity [1]
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "H2O2",
    group =
"""
multiplicity [1]
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "O=N",
    group =
"""
multiplicity [1]
1 *1 O u0 px c0 {2,D}
2    N u0 px cx {1,D}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "N2O",
    group =
"""
multiplicity [1]
1 *1 O u0 p2 c0 {2,D}
2    N u0 p0 c+1 {1,D} {3,D}
3    N u0 p2 c-1 {2,D}
""",
    kinetics = None,
)



tree(
"""
L1: Adsorbate
    L2: H
        L3: H2
        L3: CH4
        L3: NH3
    L2: C
        L3: CC
            L4: C-C
                L5: C2H6
            L4: C=C
                L5: C2H4
            L4: C#C
                L5: C2H2
        L3: CN
            L4: C-N
                L5: CH3NH2
            L4: C#N
                L5: CHN
        L3: CO
            L4: C-O
                L5: CH3OH
            L4: C=O
                L5: CH2O
                L5: CO2
    L2: N
        L3: NO
            L4: N-O
                L5: H3NO
            L4: N=O
                L5: HNO
        L3: NN
            L4: N-N
                L5: N2H4
            L4: N=N
                L5: N2H2
            L4: N#N
    L2: O
        L3: O-H
            L4: H2O
            L4: H2O2
        L3: O=N
            L4: N2O

L1: VacantSite
"""
)

forbidden(
    label = "charge",
    group =
"""
1 R ux c[+1,-1]
""",
    shortDesc = u"""Charges not allowed""",
    longDesc =
u"""
""",
)
