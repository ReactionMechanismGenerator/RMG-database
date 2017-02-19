#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionCS_cyclization/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["XSYJ"], products=["SY", "XJ"], ownReverse=False)

reverse = "Ring_Opening_bySradical"

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

boundaryAtoms = ["*1", "*3"]

entry(
    index = 1,
    label = "XSYJ",
    group = "OR{XSR3J, XSR4J, XSR5J, XSR6J, XSR7J}",
    kinetics = None,
)

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
    index = 2,
    label = "C",
    group = 
"""
1 *1 C u0
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "Cs",
    group = 
"""
1 *1 Cs u0
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "Cds",
    group = 
"""
1 *1 Cd u0
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "Ct",
    group = 
"""
1 *1 Ct u0
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "C-RRR",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S}
2    R  u0 {1,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "S",
    group = 
"""
1 *2 S u0
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "XSR3J",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *4 R!H u0 {1,[S,D]} {3,S}
3 *1 C  u0 {2,S} {4,S}
4 *2 S  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "XSR3J_S",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *1 C  u0 {2,S} {4,S}
4 *2 S  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "XSR3J_D",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *4 R!H u0 {1,D} {3,S}
3 *1 C  u0 {2,S} {4,S}
4 *2 S  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "XSR4J",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *5 R!H u0 {1,[S,D]} {3,[S,D]}
3 *4 R!H u0 {2,[S,D]} {4,S}
4 *1 C  u0 {3,S} {5,S}
5 *2 S  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "XSR4J_SS",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *5 R!H u0 {1,S} {3,S}
3 *4 R!H u0 {2,S} {4,S}
4 *1 C  u0 {3,S} {5,S}
5 *2 S  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "XSR4J_SD",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *5 R!H u0 {1,D} {3,S}
3 *4 R!H u0 {2,S} {4,S}
4 *1 C  u0 {3,S} {5,S}
5 *2 S  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "XSR4J_DS",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *5 R!H u0 {1,S} {3,D}
3 *4 R!H u0 {2,D} {4,S}
4 *1 C  u0 {3,S} {5,S}
5 *2 S  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "XSR4J_DD",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *5 R!H u0 {1,D} {3,D}
3 *4 R!H u0 {2,D} {4,S}
4 *1 C  u0 {3,S} {5,S}
5 *2 S  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "XSR5J",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *5 R!H u0 {1,[S,D]} {3,[S,D]}
3 *6 R!H u0 {2,[S,D]} {4,[S,D]}
4 *4 R!H u0 {3,[S,D]} {5,S}
5 *1 C  u0 {4,S} {6,S}
6 *2 S  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "XSR5J_SSS",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *5 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *4 R!H u0 {3,S} {5,S}
5 *1 C  u0 {4,S} {6,S}
6 *2 S  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "XSR5J_SSD",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *5 R!H u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *4 R!H u0 {3,S} {5,S}
5 *1 C  u0 {4,S} {6,S}
6 *2 S  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "XSR5J_SDS",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *5 R!H u0 {1,S} {3,D}
3 *6 R!H u0 {2,D} {4,S}
4 *4 R!H u0 {3,S} {5,S}
5 *1 C  u0 {4,S} {6,S}
6 *2 S  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "XSR5J_DSS",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *5 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,D}
4 *4 R!H u0 {3,D} {5,S}
5 *1 C  u0 {4,S} {6,S}
6 *2 S  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "XSR5J_DDS",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *5 R!H u0 {1,S} {3,D}
3 *6 R!H u0 {2,D} {4,D}
4 *4 R!H u0 {3,D} {5,S}
5 *1 C  u0 {4,S} {6,S}
6 *2 S  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "XSR5J_DSD",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *5 R!H u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,D}
4 *4 R!H u0 {3,D} {5,S}
5 *1 C  u0 {4,S} {6,S}
6 *2 S  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "XSR5J_SDD",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *5 R!H u0 {1,D} {3,D}
3 *6 R!H u0 {2,D} {4,S}
4 *4 R!H u0 {3,S} {5,S}
5 *1 C  u0 {4,S} {6,S}
6 *2 S  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "XSR5J_DDD",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *5 R!H u0 {1,D} {3,D}
3 *6 R!H u0 {2,D} {4,D}
4 *4 R!H u0 {3,D} {5,S}
5 *1 C  u0 {4,S} {6,S}
6 *2 S  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "XSR6J",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *5 R!H u0 {1,[S,D]} {3,[S,D]}
3 *6 R!H u0 {2,[S,D]} {4,[S,D]}
4 *7 R!H u0 {3,[S,D]} {5,[S,D]}
5 *4 R!H u0 {4,[S,D]} {6,S}
6 *1 C  u0 {5,S} {7,S}
7 *2 S  u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "XSR7J",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *5 R!H u0 {1,[S,D]} {3,[S,D]}
3 *6 R!H u0 {2,[S,D]} {4,[S,D]}
4 *7 R!H u0 {3,[S,D]} {5,[S,D]}
5 *8 R!H u0 {4,[S,D]} {6,[S,D]}
6 *4 R!H u0 {5,[S,D]} {7,S}
7 *1 C  u0 {6,S} {8,S}
8 *2 S  u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "CJ",
    group = "OR{CsJ, CdsJ, CdsJ-2}",
    kinetics = None,
)

entry(
    index = 25,
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
    index = 26,
    label = "CdsJ-H",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    C u0 {1,D}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "CdsJ-Cs",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "CdsJ-Ss",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D}
3    Ss u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "CdsJ-Cd",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D}
3    Cd u0 {1,S} {4,D}
4    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "CsJ",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    R u0 {1,S}
3    R u0 {1,S}
4    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "CsJ-Cs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cs u0 {1,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "CsJ-CsHH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cs u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "CsJ-CsCsH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cs u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "CsJ-CsCsCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cs u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)


entry(
    index = 52,
    label = "CsJ-Cd",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "CsJ-CdHH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "CsJ-CdCsH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "CsJ-CdCsCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "CsJ-CdSsH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S}
3    Ss u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "CsJ-CdSsSs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S}
3    Ss u0 {1,S}
4    Ss u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "CsJ-CdCsSs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S}
3    Cs u0 {1,S}
4    Ss u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "CsJ-Ss",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ss u0 {1,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "CsJ-SsHH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ss u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "CsJ-SsCsH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ss u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "CsJ-SsCsCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ss u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "CsJ-SsSsH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ss u0 {1,S}
3    Ss u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "CsJ-SsSsSs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ss u0 {1,S}
3    Ss u0 {1,S}
4    Ss u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "CsJ-SsCsSs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ss u0 {1,S}
3    Cs u0 {1,S}
4    Ss u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "SJ",
    group = 
"""
1 *3 S u1 {2,S}
2    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 82,
    label = "SsJ",
    group = 
"""
1 *3 Ss u1 {2,S}
2    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 83,
    label = "SsJ-Cs",
    group = 
"""
1 *3 Ss u1 {2,S}
2    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 84,
    label = "SsJ-Ss",
    group = 
"""
1 *3 Ss u1 {2,S}
2    Ss u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 85,
    label = "SsJ-OneDe",
    group = 
"""
1 *3 Ss            u1 {2,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 86,
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
    index = 150,
    label = "C-RRC",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S}
2      C  u0 {1,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 151,
    label = "C-(NonDe)C",
    group = 
"""
1 *1 Cs           u0 {2,S} {3,S} {4,S}
2      C            u0 {1,S}
3    [H,Cs,Os,Ss] u0 {1,S}
4    [H,Cs,Os,Ss] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 152,
    label = "C-HHC",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S}
2      C  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 153,
    label = "C-CsHC",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S}
2      C  u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 154,
    label = "C-CsCsC",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S}
2      C  u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 155,
    label = "C-(OneDe)C",
    group = 
"""
1 *1 Cs            u0 {2,S} {3,S} {4,S}
2      C             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [H,Cs,Os,Ss]  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 156,
    label = "C-(TwoDe)C",
    group = 
"""
1 *1 Cs            u0 {2,S} {3,S} {4,S}
2      C             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 157,
    label = "C-RRS",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S}
2      S  u0 {1,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 158,
    label = "C-(NonDe)S",
    group = 
"""
1 *1 Cs           u0 {2,S} {3,S} {4,S}
2      S            u0 {1,S}
3    [H,Cs,Os,Ss] u0 {1,S}
4    [H,Cs,Os,Ss] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 159,
    label = "C-HHS",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S}
2      S  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 160,
    label = "C-CsHS",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S}
2      S  u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 161,
    label = "C-CsCsS",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S}
2      S  u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 162,
    label = "C-(OneDe)S",
    group = 
"""
1 *1 Cs            u0 {2,S} {3,S} {4,S}
2      S             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [H,Cs,Os,Ss]  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 163,
    label = "C-(TwoDe)S",
    group = 
"""
1 *1 Cs            u0 {2,S} {3,S} {4,S}
2      S             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 164,
    label = "S-H",
    group = 
"""
1 *2 S u0 {2,S}
2    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 165,
    label = "S-Cs",
    group = 
"""
1 *2 S  u0 {2,S}
2    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 166,
    label = "S-Ss",
    group = 
"""
1 *2 S  u0 {2,S}
2    Ss u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 167,
    label = "S-SJ",
    group = 
"""
1 *2 S  u0 {2,S}
2    S  u1 {1,S}
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
  
L1: C
    L2: Cs
        L3: C-RRR
            L4: C-RRC
                L5: C-(NonDe)C
                    L6: C-HHC
                    L6: C-CsHC
                    L6: C-CsCsC
                L5: C-(OneDe)C
                L5: C-(TwoDe)C
            L4: C-RRS
                L5: C-(NonDe)S
                    L6: C-HHS
                    L6: C-CsHS
                    L6: C-CsCsS
                L5: C-(OneDe)S
                L5: C-(TwoDe)S
    L2: Cds
    L2: Ct 
   
L1: S
    L2: S-H
    L2: S-Cs
    L2: S-Ss
    L2: S-SJ
"""
)

forbidden(
    label = "1and3_bound",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *1 Cs  u0 {1,[S,D]}
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

