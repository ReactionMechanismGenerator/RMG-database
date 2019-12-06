#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Abstraction_vdW/groups"
shortDesc = u""
longDesc = u"""
Adsorbtion of a vdw species to the surface with a surface species.

*2=*3    *4-*5        *2-*3-*5    *4
  :   +   |    ---->   |       +  ||
~*1~    ~*6~         ~*1~~       ~*6~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m3)
so k should be in (m3/mol/s). We will use sticking coefficients.
"""

template(reactants=["AdsorbateVdW", "Adsorbate1"], products=["Adsorbate2","Adsorbate3"], ownReverse=False)

reverse = "Surface_Desorption_Abstraction_vdW"

reactantNum=2
productNum=2

recipe(actions=[
    ['CHANGE_BOND', '*2', -1, '*3'],
    ['FORM_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*4', 1, '*5'],
    ['FORM_BOND', '*3', 1, '*5'],
    ['CHANGE_BOND', '*4', 1, '*6'],
])

entry(
    index = 1,
    label = "AdsorbateVdW",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *2 R!H ux px cx {3,[D,T]}
3 *3 R!H ux px cx {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="Adsorbate1",
    group =
"""
1 *6 Xo  u0 p0 c0 {2,S}
2 *4 R!H ux px cx {1,S} {3,[S,D,T]}
3 *5 R   ux px cx {2,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "O",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *2 O   ux px cx {3,D}
3 *3 R!H ux px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "C",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *2 C   ux px cx {3,[D,T]}
3 *3 R!H ux px cx {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "O=C",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 O  ux p2 cx {3,D}
3 *3 C  ux px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "O=O",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 O  u0 p2 c0 {3,D}
3 *3 O  u0 p2 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "C=O",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,D}
3 *3 O  u0 p2 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "CO2",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,D} {4,D}
3 *3 O  u0 p2 c0 {2,D}
4    O  u0 p2 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 9,
    label="*C-R",
    group =
"""
1 *6 Xo u0 p0 c0 {2,S}
2 *4 C  ux px cx {1,S} {3,[S,D,T]}
3 *5 R  ux px cx {2,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 10,
    label="*O-R",
    group =
"""
1 *6 Xo u0 p0 c0 {2,S}
2 *4 O  u0 p2 c0 {1,S} {3,S}
3 *5 R  ux px cx {2,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label="*C-H",
    group =
"""
1 *6 Xo u0 p0 c0 {2,S}
2 *4 C  u0 p0 c0 {1,S} {3,S}
3 *5 H  u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "O=N",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 O  u0 p2 c0 {3,D}
3 *3 N  ux px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "NO",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 O  u0 p2 c0 {3,D}
3 *3 N  u1 p1 c0 {2,D}
""",
    kinetics = None,
)

# entry(
#     index = 14,
#     label = "NO2",
#     group =
# """
# 1 *1 Xv  u0 p0 c0
# 2 *2 O   u0 p2 c0  {3,D}
# 3 *3 N   u1 p1 c+1 {2,D} {4,S}
# 4    O   u0 p3 c-1 {3,S}
# """,
#     kinetics = None,
# )

entry(
    index = 15,
    label = "RNO3",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 O  u0 p2 c0  {3,D}
3 *3 N  u0 p0 c+1 {2,D} {4,S} {5,S}
4    O  u0 p3 c-1 {3,S}
5    O  u0 p2 c0  {3,S} {6,S}
6    R  u0 p0 c0  {5,S}
""",
    kinetics = None,
)


entry(
    index = 16,
    label = "HNO3",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 O  u0 p2 c0  {3,D}
3 *3 N  u0 p0 c+1 {2,D} {4,S} {5,S}
4    O  u0 p3 c-1 {3,S}
5    O  u0 p2 c0  {3,S} {6,S}
6    H  u0 p0 c0  {5,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "HONO",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 O  u0 p2 c0 {3,D}
3 *3 N  u0 p1 c0 {2,D} {4,S}
4    O  u0 p2 c0 {3,S} {5,S}
5    H  u0 p0 c0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "RONO",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 O  u0 p2 c0 {3,D}
3 *3 N  u0 p1 c0 {2,D} {4,S}
4    O  u0 p2 c0 {3,S} {5,S}
5    R  u0 p0 c0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "RNO",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 O  u0 p2 c0 {3,D}
3 *3 N  u0 p1 c0 {2,D} {4,S}
4    R  ux px cx {3,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "RN+=O",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *2 O   u0 p2 c0  {3,D}
3 *3 N   u0 p0 c+1 {2,D} {4,S}
4    R   ux px c-1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "RNO2",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *2 O   u0 p2 c0  {3,D}
3 *3 N   u0 p0 c+1 {2,D} {4,S} {5,S}
4    O   u0 p3 c-1 {3,S}
5    R   ux px cx  {3,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "HNO2",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *2 O   u0 p2 c0  {3,D}
3 *3 N   u0 p0 c+1 {2,D} {4,S} {5,S}
4    O   u0 p3 c-1 {3,S}
5    H   u0 p0 c0  {3,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "N2O4",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *2 O   u0 p2 c0  {3,D}
3 *3 N   u0 p0 c+1 {2,D} {4,S} {5,S}
4    O   u0 p3 c-1 {3,S}
5    N   u0 p0 c+1 {3,S} {6,S} {7,D}
6    O   u0 p3 c-1 {5,S}
7    O   u0 p2 c0  {5,D}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "N2O",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *2 O   u0 p2 c0  {3,D}
3 *3 N   u0 p0 c+1 {2,D} {4,D}
4    N   u0 p2 c-1 {3,D}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "CC",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,[D,T]}
3 *3 C  u0 p0 c0 {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "C=C",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,D}
3 *3 C  u0 p0 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "C#C",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,T}
3 *3 C  u0 p0 c0 {2,T}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "CN",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 C  ux px cx {3,[D,T]}
3 *3 N  ux px cx {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "C=N",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,D}
3 *3 N  u0 px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "C#N",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 C  u0 px cx {3,T}
3 *3 N  ux px cx {2,T}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "C=N-R",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,D}
3 *3 N  u0 px c0 {2,D} {4,S}
4    R  u0 px c0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "C=N=N",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0  {3,D}
3 *3 N  u0 p0 c+1 {2,D} {4,D}
4    N  u0 p2 c-1 {3,D}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "RC#N",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,T} {4,S}
3 *3 N  u0 p1 c0 {2,T}
4    R  u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = ":C#NR",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 C  u0 p1 c-1 {3,T}
3 *3 N  u0 p0 c+1 {2,T} {4,S}
4    R  u0 p0 c0  {3,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "C#NO",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0  {3,T}
3 *3 N  u0 p0 c+1 {2,T} {4,S}
4    O  u0 p3 c-1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "N",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *2 N   ux px cx {3,[D,T]}
3 *3 R!H ux px cx {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "N=O",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 N  ux px cx {3,D}
3 *3 O  u0 p2 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "NC",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 N  ux px cx {3,[D,T]}
3 *3 C  ux px cx {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "N=C",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 N  ux px cx {3,D}
3 *3 C  ux px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "N#C",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 N  ux px cx {3,T}
3 *3 C  ux px cx {2,T}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "R-N=C",
    group =
"""
1 *1 Xv u0 p0 c0
2 *3 C  u0 p0 c0 {3,D}
3 *2 N  u0 px c0 {2,D} {4,S}
4    R  u0 px c0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "N=N=C",
    group =
"""
1 *1 Xv u0 p0 c0
2 *3 C  u0 p0 c0  {3,D}
3 *2 N  u0 p0 c+1 {2,D} {4,D}
4    N  u0 p2 c-1 {3,D}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "N#CR",
    group =
"""
1 *1 Xv u0 p0 c0
2 *3 C  u0 p0 c0 {3,T} {4,S}
3 *2 N  u0 p1 c0 {2,T}
4    R  u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "RN#C:",
    group =
"""
1 *1 Xv u0 p0 c0
2 *3 C  u0 p1 c-1 {3,T}
3 *2 N  u0 p0 c+1 {2,T} {4,S}
4    R  u0 p0 c0  {3,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "ON#C",
    group =
"""
1 *1 Xv u0 p0 c0
2 *3 C  u0 p0 c0  {3,T}
3 *2 N  u0 p0 c+1 {2,T} {4,S}
4    O  u0 p3 c-1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "ON",
    group =
"""
1 *1 Xv u0 p0 c0
2 *3 O  u0 p2 c0 {3,D}
3 *2 N  u1 p1 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "O3NR",
    group =
"""
1 *1 Xv u0 p0 c0
2 *3 O  u0 p2 c0  {3,D}
3 *2 N  u0 p0 c+1 {2,D} {4,S} {5,S}
4    O  u0 p3 c-1 {3,S}
5    O  u0 p2 c0  {3,S} {6,S}
6    R  u0 p0 c0  {5,S}
""",
    kinetics = None,
)


entry(
    index = 44,
    label = "O3NH",
    group =
"""
1 *1 Xv u0 p0 c0
2 *3 O  u0 p2 c0  {3,D}
3 *2 N  u0 p0 c+1 {2,D} {4,S} {5,S}
4    O  u0 p3 c-1 {3,S}
5    O  u0 p2 c0  {3,S} {6,S}
6    H  u0 p0 c0  {5,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "ONOH",
    group =
"""
1 *1 Xv u0 p0 c0
2 *3 O  u0 p2 c0 {3,D}
3 *2 N  u0 p1 c0 {2,D} {4,S}
4    O  u0 p2 c0 {3,S} {5,S}
5    H  u0 p0 c0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "ONOR",
    group =
"""
1 *1 Xv u0 p0 c0
2 *3 O  u0 p2 c0 {3,D}
3 *2 N  u0 p1 c0 {2,D} {4,S}
4    O  u0 p2 c0 {3,S} {5,S}
5    R  u0 p0 c0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "ONR",
    group =
"""
1 *1 Xv u0 p0 c0
2 *3 O  u0 p2 c0 {3,D}
3 *2 N  u0 p1 c0 {2,D} {4,S}
4    R  ux px cx {3,S}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "O=N+R",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *3 O   u0 p2 c0  {3,D}
3 *2 N   u0 p0 c+1 {2,D} {4,S}
4    R   ux px c-1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "O2NR",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *3 O   u0 p2 c0  {3,D}
3 *2 N   u0 p0 c+1 {2,D} {4,S} {5,S}
4    O   u0 p3 c-1 {3,S}
5    R   ux px cx  {3,S}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "O2NH",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *3 O   u0 p2 c0  {3,D}
3 *2 N   u0 p0 c+1 {2,D} {4,S} {5,S}
4    O   u0 p3 c-1 {3,S}
5    H   u0 p0 c0  {3,S}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "O4N2",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *3 O   u0 p2 c0  {3,D}
3 *2 N   u0 p0 c+1 {2,D} {4,S} {5,S}
4    O   u0 p3 c-1 {3,S}
5    N   u0 p0 c+1 {3,S} {6,S} {7,D}
6    O   u0 p3 c-1 {5,S}
7    O   u0 p2 c0  {5,D}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "O2N",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *3 O   u0 p2 c0  {3,D}
3 *2 N   u0 p0 c+1 {2,D} {4,D}
4    N   u0 p2 c-1 {3,D}
""",
    kinetics = None,
)

entry(
    index = 53,
    label="*N-R",
    group =
"""
1 *6 Xo  u0 p0 c0 {2,S}
2 *4 N   ux px cx {1,S} {3,[S,D,T]}
3 *5 R   ux px cx {2,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "O=C=O",
    group =
"""
1    O  u0 p2 c0 {3,D}
2 *2 O  u0 p2 c0 {3,D}
3 *3 C  u0 p0 c0 {1,D} {2,D}
4 *1 Xv u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "HNO",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 O  u0 p2 c0 {3,D}
3 *3 N  u0 p1 c0 {2,D} {4,S}
4    H  u0 p0 c0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "2R-C=O",
    group =
"""
1 *1 Xv u0 p0 c0
2 *3 O  u0 p2 c0 {3,D}
3 *2 C  u0 p0 c0 {2,D} {4,S} {5,S}
4    R  ux px cx {3,S}
5    R  ux px cx {3,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "R=C=O",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *3 O   u0 p2 c0 {3,D}
3 *2 C   u0 p0 c0 {2,D} {4,D}
4    R!H ux px cx {3,D}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "NN",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 N  ux px cx {3,[D,T]}
3 *3 N  ux px cx {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "N=N",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 N  ux px cx {3,D}
3 *3 N  ux px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "N2",
    group =
"""
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
            L4: NO
            L4: RNO
                L5: RONO
                    L6: HONO
                L5: HNO
            L4: N2O
            L4: RN+=O
                L5: RNO3
                    L6: HNO3
                L5: RNO2
                    L6: HNO2
                    L6: N2O4
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
                L5: C=N=N
            L4: C#N
                L5: RC#N
                L5: :C#NR
                L5: C#NO
    L2: N
        L3: NC
            L4: N=C
                L5: R-N=C
                L5: N=N=C
            L4: N#C
                L5: N#CR
                L5: RN#C:
                L5: ON#C
        L3: N=O
            L4: ON
            L4: ONR
                L5: ONOR
                    L6: ONOH
            L4: O2N
            L4: O=N+R
                L5: O3NR
                    L6: O3NH
                L5: O2NR
                    L6: O2NH
                    L6: O4N2
        L3: NN
            L4: N=N
            L4: N2

L1: Adsorbate1
    L2: *C-R
        L3: *C-H
    L2: *O-R
    L2: *N-R
"""
)
