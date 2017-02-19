#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionS_isomerization/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["XSYJ"], products=["XSYJ"], ownReverse=True)

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "XSYJ",
    group = "OR{XSR3J, XSR4J, XSR5J, XSR6J, XSR7J}",
    kinetics = None,
)

boundaryAtoms = ["*1", "*3"]

entry(
    index = 2,
    label = "YJ",
    group = 
"""
1 *3 R!H u1
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "S-RR",
    group = 
"""
1 *1 Ss  u0 {2,S} {3,S}
2    R   u0 {1,S}
3 *2 R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "XSR3J",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *2 R!H u0 {1,[S,D]} {3,S}
3 *1 Ss  u0 {2,S} {4,S}
4    R   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "XSR3J_S",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *2 R!H u0 {1,S} {3,S}
3 *1 Ss  u0 {2,S} {4,S}
4    R   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "XSR3J_D",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *2 R!H u0 {1,D} {3,S}
3 *1 Ss  u0 {2,S} {4,S}
4    R   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "XSR4J",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *4 R!H u0 {1,[S,D]} {3,[S,D]}
3 *2 R!H u0 {2,[S,D]} {4,S}
4 *1 Ss  u0 {3,S} {5,S}
5    R   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "XSR4J_SS",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *2 R!H u0 {2,S} {4,S}
4 *1 Ss  u0 {3,S} {5,S}
5    R   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "XSR4J_SD",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *4 R!H u0 {1,D} {3,S}
3 *2 R!H u0 {2,S} {4,S}
4 *1 Ss  u0 {3,S} {5,S}
5    R   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "XSR4J_DS",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,D}
3 *2 R!H u0 {2,D} {4,S}
4 *1 Ss  u0 {3,S} {5,S}
5    R   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "XSR4J_DD",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *4 R!H u0 {1,D} {3,D}
3 *2 R!H u0 {2,D} {4,S}
4 *1 Ss  u0 {3,S} {5,S}
5    R   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "XSR5J",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *4 R!H u0 {1,[S,D]} {3,[S,D]}
3 *5 R!H u0 {2,[S,D]} {4,[S,D]}
4 *2 R!H u0 {3,[S,D]} {5,S}
5 *1 Ss  u0 {4,S} {6,S}
6    R   u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "XSR5J_SSS",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 R!H u0 {3,S} {5,S}
5 *1 Ss  u0 {4,S} {6,S}
6    R   u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "XSR5J_SSD",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *4 R!H u0 {1,D} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 R!H u0 {3,S} {5,S}
5 *1 Ss  u0 {4,S} {6,S}
6    R   u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "XSR5J_SDS",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,D}
3 *5 R!H u0 {2,D} {4,S}
4 *2 R!H u0 {3,S} {5,S}
5 *1 Ss  u0 {4,S} {6,S}
6    R   u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "XSR5J_DSS",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *5 R!H u0 {2,S} {4,D}
4 *2 R!H u0 {3,D} {5,S}
5 *1 Ss  u0 {4,S} {6,S}
6    R   u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "XSR5J_DDS",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,D}
3 *5 R!H u0 {2,D} {4,D}
4 *2 R!H u0 {3,D} {5,S}
5 *1 Ss  u0 {4,S} {6,S}
6    R   u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "XSR5J_DSD",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *4 R!H u0 {1,D} {3,S}
3 *5 R!H u0 {2,S} {4,D}
4 *2 R!H u0 {3,D} {5,S}
5 *1 Ss  u0 {4,S} {6,S}
6    R   u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "XSR5J_SDD",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *4 R!H u0 {1,D} {3,D}
3 *5 R!H u0 {2,D} {4,S}
4 *2 R!H u0 {3,S} {5,S}
5 *1 Ss  u0 {4,S} {6,S}
6    R   u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "XSR5J_DDD",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *4 R!H u0 {1,D} {3,D}
3 *5 R!H u0 {2,D} {4,D}
4 *2 R!H u0 {3,D} {5,S}
5 *1 Ss  u0 {4,S} {6,S}
6    R   u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "XSR6J",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *4 R!H u0 {1,[S,D]} {3,[S,D]}
3 *5 R!H u0 {2,[S,D]} {4,[S,D]}
4 *6 R!H u0 {3,[S,D]} {5,[S,D]}
5 *2 R!H u0 {4,[S,D]} {6,S}
6 *1 Ss  u0 {5,S} {7,S}
7    R   u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "XSR7J",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *4 R!H u0 {1,[S,D]} {3,[S,D]}
3 *5 R!H u0 {2,[S,D]} {4,[S,D]}
4 *6 R!H u0 {3,[S,D]} {5,[S,D]}
5 *7 R!H u0 {4,[S,D]} {6,[S,D]}
6 *2 R!H u0 {5,[S,D]} {7,S}
7 *1 Ss  u0 {6,S} {8,S}
8    R   u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "CJ",
    group = "OR{CsJ, CdsJ}",
    kinetics = None,
)

entry(
    index = 24,
    label = "CdsJ",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    C u0 {1,D}
3    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "CdsJ-H",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2      C u0 {1,D}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "CdsJ-Cs",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2      C  u0 {1,D}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "CdsJ-Ss",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2      C  u0 {1,D}
3    Ss u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "CdsJ-Cd",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2      C  u0 {1,D}
3    Cd u0 {1,S} {4,D}
4    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "CsJ",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2      R u0 {1,S}
3    R u0 {1,S}
4    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "CsJ-Cs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2      Cs u0 {1,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "CsJ-CsHH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2      Cs u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "CsJ-CsCsH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2      Cs u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "CsJ-CsCsCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2      Cs u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "CsJ-Cd",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2      Cd u0 {1,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "CsJ-CdHH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2      Cd u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "CsJ-CdCsH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2      Cd u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "CsJ-CdCsCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2      Cd u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "CsJ-CdSsH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2      Cd u0 {1,S}
3    Ss u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "CsJ-CdSsSs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2      Cd u0 {1,S}
3    Ss u0 {1,S}
4    Ss u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "CsJ-CdCsSs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2      Cd u0 {1,S}
3    Cs u0 {1,S}
4    Ss u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "CsJ-Ss",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2      Ss u0 {1,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "CsJ-SsHH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2      Ss u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "CsJ-SsCsH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2      Ss u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "CsJ-SsCsCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2      Ss u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "CsJ-SsSsH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2      Ss u0 {1,S}
3    Ss u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "CsJ-SsSsSs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2      Ss u0 {1,S}
3    Ss u0 {1,S}
4    Ss u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "CsJ-SsCsSs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2      Ss u0 {1,S}
3    Cs u0 {1,S}
4    Ss u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "SJ",
    group = 
"""
1 *3 S u1 {2,S}
2      R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "SsJ",
    group = 
"""
1 *3 Ss u1 {2,S}
2      R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 82,
    label = "SsJ-Cs",
    group = 
"""
1 *3 Ss u1 {2,S}
2      Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 83,
    label = "SsJ-Ss",
    group = 
"""
1 *3 Ss u1 {2,S}
2      Ss u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 84,
    label = "SsJ-OneDe",
    group = 
"""
1 *3 Ss            u1 {2,S}
2      [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 85,
    label = "SsJ-Cd",
    group = 
"""
1 *3 Ss u1 {2,S}
2    Cd u0 {1,S} {3,D}
3    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 149,
    label = "S-HC",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    H  u0 {1,S}
3 *2 C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 150,
    label = "S-CC",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    C  u0 {1,S}
3 *2 C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 151,
    label = "S-CsC",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    Cs u0 {1,S}
3 *2 C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 152,
    label = "S-Cs(NonDe)C",
    group = 
"""
1 *1 Ss     u0 {2,S} {3,S}
2    Cs     u0 {1,S} {4,S} {5,S} {6,S}
3 *2 C      u0 {1,S}
4    [H,Cs] u0 {2,S}
5    [H,Cs] u0 {2,S}
6    [H,Cs] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 153,
    label = "S-Cs(HHH)C",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    Cs u0 {1,S} {4,S} {5,S} {6,S}
3 *2 C  u0 {1,S}
4    H  u0 {2,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 154,
    label = "S-Cs(CsHH)C",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    Cs u0 {1,S} {4,S} {5,S} {6,S}
3 *2 C  u0 {1,S}
4    H  u0 {2,S}
5    H  u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 155,
    label = "S-Cs(CsCsH)C",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    Cs u0 {1,S} {4,S} {5,S} {6,S}
3 *2 C  u0 {1,S}
4    H  u0 {2,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 156,
    label = "S-Cs(CsCsCs)C",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    Cs u0 {1,S} {4,S} {5,S} {6,S}
3 *2 C  u0 {1,S}
4    Cs u0 {2,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 157,
    label = "S-Cs(De)C",
    group = 
"""
1 *1 Ss            u0 {2,S} {3,S}
2    Cs            u0 {1,S} {4,S} {5,S} {6,S}
3 *2 C             u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {2,S}
5    R             u0 {2,S}
6    R             u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 158,
    label = "S-Cs(OneDe)C",
    group = 
"""
1 *1 Ss            u0 {2,S} {3,S}
2    Cs            u0 {1,S} {4,S} {5,S} {6,S}
3 *2 C             u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {2,S}
5    [H,Cs]        u0 {2,S}
6    [H,Cs]        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 159,
    label = "S-Cs(CdHH)C",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    Cs u0 {1,S} {4,S} {5,S} {6,S}
3 *2 C  u0 {1,S}
4    Cd u0 {2,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 160,
    label = "S-Cs(CdCsH)C",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    Cs u0 {1,S} {4,S} {5,S} {6,S}
3 *2 C  u0 {1,S}
4    Cd u0 {2,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 161,
    label = "S-Cs(CdCsCs)C",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    Cs u0 {1,S} {4,S} {5,S} {6,S}
3 *2 C  u0 {1,S}
4    Cd u0 {2,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 162,
    label = "S-Cs(CtHH)C",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    Cs u0 {1,S} {4,S} {5,S} {6,S}
3 *2 C  u0 {1,S}
4    Ct u0 {2,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 163,
    label = "S-Cs(CtCsH)C",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    Cs u0 {1,S} {4,S} {5,S} {6,S}
3 *2 C  u0 {1,S}
4    Ct u0 {2,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 164,
    label = "S-Cs(CtCsCs)C",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    Cs u0 {1,S} {4,S} {5,S} {6,S}
3 *2 C  u0 {1,S}
4    Ct u0 {2,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 165,
    label = "S-Cs(TwoDe)C",
    group = 
"""
1 *1 Ss            u0 {2,S} {3,S}
2    Cs            u0 {1,S} {4,S} {5,S} {6,S}
3 *2 C             u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {2,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
6    [H,Cs]        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 166,
    label = "S-Cs(ThreeDe)C",
    group = 
"""
1 *1 Ss            u0 {2,S} {3,S}
2    Cs            u0 {1,S} {4,S} {5,S} {6,S}
3 *2 C             u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {2,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 167,
    label = "S-CtC",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    Ct u0 {1,S}
3 *2 C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 168,
    label = "S-CbC",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    Cb u0 {1,S}
3 *2 C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 169,
    label = "S-CdC",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    Cd u0 {1,S} {4,D}
3 *2 C  u0 {1,S}
4    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 170,
    label = "S-Cds(H)C",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    Cd u0 {1,S} {4,D} {5,S}
3 *2 C  u0 {1,S}
4    C  u0 {2,D}
5    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 171,
    label = "S-Cds(Cs)C",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    Cd u0 {1,S} {4,D} {5,S}
3 *2 C  u0 {1,S}
4    C  u0 {2,D}
5    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 172,
    label = "S-CSs",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2 *2 S  u0 {1,S}
3    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 173,
    label = "S-CsSs",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2 *2 Ss u0 {1,S}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 174,
    label = "S-Cs(HHH)Ss",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2 *2 Ss u0 {1,S}
3    Cs u0 {1,S} {4,S} {5,S} {6,S}
4    H  u0 {3,S}
5    H  u0 {3,S}
6    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 175,
    label = "S-Cs(CsHH)Ss",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2 *2 Ss u0 {1,S}
3    Cs u0 {1,S} {4,S} {5,S} {6,S}
4    Cs u0 {3,S}
5    H  u0 {3,S}
6    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 176,
    label = "S-Cs(CsCsH)Ss",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2 *2 Ss u0 {1,S}
3    Cs u0 {1,S} {4,S} {5,S} {6,S}
4    Cs u0 {3,S}
5    Cs u0 {3,S}
6    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 177,
    label = "S-Cs(CsCsCs)Ss",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2 *2 Ss u0 {1,S}
3    Cs u0 {1,S} {4,S} {5,S} {6,S}
4    Cs u0 {3,S}
5    Cs u0 {3,S}
6    Cs u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 178,
    label = "S-CtSs",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2 *2 Ss u0 {1,S}
3    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 179,
    label = "S-CbSs",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2 *2 Ss u0 {1,S}
3    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 180,
    label = "S-CdSs",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2 *2 Ss u0 {1,S}
3    Cd u0 {1,S} {4,D}
4    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 181,
    label = "S-Cds(H)Ss",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2 *2 Ss u0 {1,S}
3    Cd u0 {1,S} {4,D} {5,S}
4    C  u0 {3,D}
5    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 182,
    label = "S-Cds(Cs)Ss",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2 *2 Ss u0 {1,S}
3    Cd u0 {1,S} {4,D} {5,S}
4    C  u0 {3,D}
5    Cs u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 183,
    label = "S-SC",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    S  u0 {1,S}
3 *2 C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 184,
    label = "S-SsC",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    Ss u0 {1,S}
3 *2 C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 185,
    label = "S-Ss(H)C",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    Ss u0 {1,S} {4,S}
3 *2 C  u0 {1,S}
4    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 186,
    label = "S-Ss(Cs)C",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    Ss u0 {1,S} {4,S}
3 *2 C  u0 {1,S}
4    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 187,
    label = "S-Ss(Ss)C",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    Ss u0 {1,S} {4,S}
3 *2 C  u0 {1,S}
4    Ss u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 188,
    label = "S-HSs",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    H  u0 {1,S}
3 *2 Ss u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 189,
    label = "S-SsSs",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2 *2 Ss u0 {1,S}
3    Ss u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 190,
    label = "S-Ss(H)Ss",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2 *2 Ss u0 {1,S}
3    Ss u0 {1,S} {4,S}
4    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 191,
    label = "S-Ss(Cs)Ss",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2 *2 Ss u0 {1,S}
3    Ss u0 {1,S} {4,S}
4    Cs u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 192,
    label = "S-Ss(Ss)Ss",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2    Ss u0 {1,S}
3 *2 Ss u0 {1,S} {4,S}
4    Ss u0 {3,S}
""",
    kinetics = None,
)

tree(
"""
L1: XSYJ
    L2: XSR3J
        L3: XSR3J_S
        L3: XSR3J_D
    L2: XSR4J
        L3: XSR4J_SS
        L3: XSR4J_SD
        L3: XSR4J_DS
        L3: XSR4J_DD
    L2: XSR5J
        L3: XSR5J_SSS
        L3: XSR5J_SSD
        L3: XSR5J_SDS
        L3: XSR5J_DSS
        L3: XSR5J_DDS
        L3: XSR5J_DSD
        L3: XSR5J_SDD
        L3: XSR5J_DDD
    L2: XSR6J
    L2: XSR7J
L1: YJ
    L2: CJ
        L3: CdsJ
            L4: CdsJ-H
            L4: CdsJ-Cs
            L4: CdsJ-Ss
            L4: CdsJ-Cd
        L3: CsJ
            L4: CsJ-Cs
                L5: CsJ-CsHH
                L5: CsJ-CsCsH
                L5: CsJ-CsCsCs
            L4: CsJ-Cd
                L5: CsJ-CdHH
                L5: CsJ-CdCsH
                L5: CsJ-CdCsCs
                L5: CsJ-CdSsH
                L5: CsJ-CdSsSs
                L5: CsJ-CdCsSs
            L4: CsJ-Ss
                L5: CsJ-SsHH
                L5: CsJ-SsCsH
                L5: CsJ-SsCsCs
                L5: CsJ-SsSsH
                L5: CsJ-SsSsSs
                L5: CsJ-SsCsSs
    L2: SJ
        L3: SsJ
            L4: SsJ-Cs
            L4: SsJ-Ss
            L4: SsJ-OneDe
                L5: SsJ-Cd
L1: S-RR
    L2: S-HC
    L2: S-CC
        L3: S-CsC
            L4: S-Cs(NonDe)C
                L5: S-Cs(HHH)C
                L5: S-Cs(CsHH)C
                L5: S-Cs(CsCsH)C
                L5: S-Cs(CsCsCs)C
            L4: S-Cs(De)C
                L5: S-Cs(OneDe)C
                    L6: S-Cs(CdHH)C
                    L6: S-Cs(CdCsH)C
                    L6: S-Cs(CdCsCs)C
                    L6: S-Cs(CtHH)C
                    L6: S-Cs(CtCsH)C
                    L6: S-Cs(CtCsCs)C
                L5: S-Cs(TwoDe)C
                L5: S-Cs(ThreeDe)C
        L3: S-CtC
        L3: S-CbC
        L3: S-CdC
            L4: S-Cds(H)C
            L4: S-Cds(Cs)C
    L2: S-CSs
        L3: S-CsSs
            L4: S-Cs(HHH)Ss
            L4: S-Cs(CsHH)Ss
            L4: S-Cs(CsCsH)Ss
            L4: S-Cs(CsCsCs)Ss
        L3: S-CtSs
        L3: S-CbSs
        L3: S-CdSs
            L4: S-Cds(H)Ss
            L4: S-Cds(Cs)Ss
    L2: S-SC
        L3: S-SsC
            L4: S-Ss(H)C
            L4: S-Ss(Cs)C
            L4: S-Ss(Ss)C
    L2: S-HSs
    L2: S-SsSs
        L3: S-Ss(H)Ss
        L3: S-Ss(Cs)Ss
        L3: S-Ss(Ss)Ss
"""
)

forbidden(
    label = "RR_13",
    group = 
"""
1 *1 R u0 {2,[S,D]}
2 *3 R u1 {1,[S,D]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

forbidden(
    label = "RR_birad",
    group = 
"""
1 *3 R u1 {2,[S,D]}
2    R u1 {1,[S,D]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

