#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Addition_Single_vdW/groups"
shortDesc = u""
longDesc = u"""
A single bonded surface species adding to a vdW double, triple, or quadruple bonded species and adsorbing to a surface.

*2=*3       *4              *2-*3-*4
  :     +    |     ---->    |         +
~*1~       ~*5~           ~*1~            ~*5~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s).

"""

template(reactants=["AdsorbateVdW","Adsorbate1"], products=["VacantSite","Adsorbate2"], ownReverse=False)

reverse = "Surface_Deletion_Single_vdW"

reactantNum=2
productNum=2

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*2', -1, '*3'],
    ['FORM_BOND', '*3', 1, '*4'],
    ['BREAK_BOND', '*4', 1, '*5'],
])

entry(
    index = 1,
    label = "AdsorbateVdW",
    group =
"""
multiplicity [1]
1 *1 Xv  u0 p0 c0
2 *2 R!H ux px cx {3,[D,T]}
3 *3 R!H ux px cx {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "Adsorbate1",
    group =
"""
1 *5 Xo u0 p0 c0 {2,S}
2 *4 R  ux px cx {1,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "H*",
    group =
"""
1 *5 Xo u0 p0 c0 {2,S}
2 *4 H  u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "O*",
    group =
"""
1 *5 Xo u0 p0 c0 {2,S}
2 *4 O  u0 px c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "HO*",
    group =
"""
1 *5 Xo u0 p0 c0 {2,S}
2 *4 O  u0 p2 c0 {1,S} {3,S}
3    H  u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "N*",
    group =
"""
1 *5 Xo u0 p0 c0 {2,S}
2 *4 N  u0 p1 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "C*",
    group =
"""
1 *5 Xo u0 p0 c0 {2,S}
2 *4 C  u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "O",
    group =
"""
multiplicity [1]
1 *1 Xv  u0 p0 c0
2 *2 O   ux px cx {3,D}
3 *3 R!H ux px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "C",
    group =
"""
multiplicity [1]
1 *1 Xv  u0 p0 c0
2 *2 C   ux px cx {3,[D,T]}
3 *3 R!H ux px cx {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "O=C",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 O  ux p2 cx {3,D}
3 *3 C  ux px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "O=O",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 O  u0 p2 c0 {3,D}
3 *3 O  u0 p2 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "C=O",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,D}
3 *3 O  u0 p2 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "CO2",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,D} {4,D}
3 *3 O  u0 p2 c0 {2,D}
4    O  u0 p2 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "O=N",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 O  u0 p2 c0 {3,D}
3 *3 N  ux px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "HONO",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 O  u0 p2 c0 {3,D}
3 *3 N  u0 p1 c0 {2,D} {4,S}
4    O  u0 p2 c0 {3,S} {5,S}
5    H  u0 p0 c0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "RONO",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 O  u0 p2 c0 {3,D}
3 *3 N  u0 p1 c0 {2,D} {4,S}
4    O  u0 p2 c0 {3,S} {5,S}
5    R  u0 p0 c0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "RNO",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 O  u0 p2 c0 {3,D}
3 *3 N  u0 p1 c0 {2,D} {4,S}
4    R  ux px cx {3,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "CC",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,[D,T]}
3 *3 C  u0 p0 c0 {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "C=C",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,D}
3 *3 C  u0 p0 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "C#C",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,T}
3 *3 C  u0 p0 c0 {2,T}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "CN",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 C  ux px cx {3,[D,T]}
3 *3 N  ux px cx {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "C=N",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,D}
3 *3 N  u0 px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "C#N",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 C  u0 px cx {3,T}
3 *3 N  ux px cx {2,T}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "C=N-R",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,D}
3 *3 N  u0 px c0 {2,D} {4,S}
4    R  u0 px c0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "RC#N",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,T} {4,S}
3 *3 N  u0 p1 c0 {2,T}
4    R  u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "N",
    group =
"""
multiplicity [1]
1 *1 Xv  u0 p0 c0
2 *2 N   ux px cx {3,[D,T]}
3 *3 R!H ux px cx {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "N=O",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 N  ux px cx {3,D}
3 *3 O  u0 p2 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "NC",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 N  ux px cx {3,[D,T]}
3 *3 C  ux px cx {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "N=C",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 N  ux px cx {3,D}
3 *3 C  ux px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "N#C",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 N  ux px cx {3,T}
3 *3 C  ux px cx {2,T}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "R-N=C",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *3 C  u0 p0 c0 {3,D}
3 *2 N  u0 px c0 {2,D} {4,S}
4    R  u0 px c0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "N#CR",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *3 C  u0 p0 c0 {3,T} {4,S}
3 *2 N  u0 p1 c0 {2,T}
4    R  u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "ONOH",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *3 O  u0 p2 c0 {3,D}
3 *2 N  u0 p1 c0 {2,D} {4,S}
4    O  u0 p2 c0 {3,S} {5,S}
5    H  u0 p0 c0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "ONOR",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *3 O  u0 p2 c0 {3,D}
3 *2 N  u0 p1 c0 {2,D} {4,S}
4    O  u0 p2 c0 {3,S} {5,S}
5    R  u0 p0 c0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "ONR",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *3 O  u0 p2 c0 {3,D}
3 *2 N  u0 p1 c0 {2,D} {4,S}
4    R  ux px cx {3,S}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "O=C=O",
    group =
"""
multiplicity [1]
1    O  u0 p2 c0 {3,D}
2 *2 O  u0 p2 c0 {3,D}
3 *3 C  u0 p0 c0 {1,D} {2,D}
4 *1 Xv u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "HNO",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 O  u0 p2 c0 {3,D}
3 *3 N  u0 p1 c0 {2,D} {4,S}
4    H  u0 p0 c0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "2R-C=O",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *3 O  u0 p2 c0 {3,D}
3 *2 C  u0 p0 c0 {2,D} {4,S} {5,S}
4    R  ux px cx {3,S}
5    R  ux px cx {3,S}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "R=C=O",
    group =
"""
multiplicity [1]
1 *1 Xv  u0 p0 c0
2 *3 O   u0 p2 c0 {3,D}
3 *2 C   u0 p0 c0 {2,D} {4,D}
4    R!H ux px cx {3,D}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "NN",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 N  ux px cx {3,[D,T]}
3 *3 N  ux px cx {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "N=N",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 N  ux px cx {3,D}
3 *3 N  ux px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "N2",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 N  u0 p1 c0 {3,T}
3 *3 N  u0 p1 c0 {2,T}
""",
    kinetics = None,
)

tree(
"""
L1: AdsorbateVdW
    L2: O
        L3: O=C
            L4: O=C=O
        L3: O=O
        L3: O=N
            L4: RNO
                L5: RONO
                    L6: HONO
                L5: HNO
    L2: C
        L3: C=O
            L4: 2R-C=O
            L4: R=C=O
                L5: CO2
        L3: CC
            L4: C=C
            L4: C#C
        L3: CN
            L4: C=N
                L5: C=N-R
            L4: C#N
                L5: RC#N
    L2: N
        L3: NC
            L4: N=C
                L5: R-N=C
            L4: N#C
                L5: N#CR
        L3: N=O
            L4: ONR
                L5: ONOR
                    L6: ONOH
        L3: NN
            L4: N=N
            L4: N2

L1: Adsorbate1
    L2: H*
    L2: O*
        L3: HO*
    L2: N*
    L2: C*
"""
)

forbidden(
    label = "chargedBond",
    group =
"""
1 *2 R!H ux c[+1,-1] {2,[S,D,T]}
2 *3 R!H ux c[+1,-1] {1,[S,D,T]}
3 *1 Xv  u0 p0 c0
""",
    shortDesc = u"""""",
    longDesc =
u"""
The adsorbing molecule should not have a charge on the surface.
""",
)
