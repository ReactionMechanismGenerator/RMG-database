#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionCS_isomerization/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["XSYJ"], products=["XYSJ"], ownReverse=False)

reverse = "Ring_Opening_bySradical"
reversible = True

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

boundaryAtoms = ["*1", "*3"]

entry(
    index = 0,
    label = "XSYJ",
    group = "OR{XSR3J, XSR4J, XSR5J, XSR6J, XSR7J}",
    kinetics = None,
)

entry(
    index = 1,
    label = "C",
    group = 
"""
1 *1 C u0
""",
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
    index = 3,
    label = "XSR3J",
    group = 
"""
1 *2 S2s u0 p2 c0 {2,[S,D]} {3,S}
2 *3 R!H u1 {1,[S,D]}
3 *1 C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "XSR3J_S",
    group = 
"""
1 *2 S2s u0 p2 c0 {2,S} {3,S}
2 *3 R!H u1 {1,S}
3 *1 C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "XSR4J",
    group = 
"""
1 *4 R!H u0 {2,[S,D]} {3,[S,D]}
2 *2 S2s u0 p2 c0 {1,[S,D]} {4,S}
3 *3 R!H u1 {1,[S,D]}
4 *1 C   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "XSR4J_SS",
    group = 
"""
1 *4 R!H u0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {4,S}
3 *3 R!H u1 {1,S}
4 *1 C   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "XSR4J_SS_Cs",
    group = 
"""
1 *4 Cs  u0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {4,S}
3 *3 R!H u1 {1,S}
4 *1 C   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "XSR4J_SS_Ss",
    group = 
"""
1 *4 S2s u0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {4,S}
3 *3 R!H u1 {1,S}
4 *1 C   u0 {2,S}
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
3 *2 S2s u0 p2 c0 {2,S} {4,S}
4 *1 C   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "XSR5J",
    group = 
"""
1 *5 R!H u0 {2,[S,D]} {3,[S,D]}
2 *4 R!H u0 {1,[S,D]} {4,[S,D]}
3 *2 S2s u0 p2 c0 {1,[S,D]} {5,S}
4 *3 R!H u1 {2,[S,D]}
5 *1 C   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "XSR5J_SSS",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 S2s u0 p2 c0 {3,S} {5,S}
5 *1 C   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "XSR5J_SSD",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *4 R!H u0 {1,D} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 S2s u0 p2 c0 {3,S} {5,S}
5 *1 C   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "XSR5J_SDS",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,D}
3 *5 R!H u0 {2,D} {4,S}
4 *2 S2s u0 p2 c0 {3,S} {5,S}
5 *1 C   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "XSR5J_SDD",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *4 R!H u0 {1,D} {3,D}
3 *5 R!H u0 {2,D} {4,S}
4 *2 S2s u0 p2 c0 {3,S} {5,S}
5 *1 C   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "XSR6J",
    group = 
"""
1 *5 R!H u0 {2,[S,D]} {3,[S,D]}
2 *6 R!H u0 {1,[S,D]} {4,[S,D]}
3 *4 R!H u0 {1,[S,D]} {5,[S,D]}
4 *2 S2s u0 p2 c0 {2,[S,D]} {6,S}
5 *3 R!H u1 {3,[S,D]}
6 *1 C   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "XSR7J",
    group = 
"""
1 *6 R!H u0 {2,[S,D]} {3,[S,D]}
2 *5 R!H u0 {1,[S,D]} {4,[S,D]}
3 *7 R!H u0 {1,[S,D]} {5,[S,D]}
4 *4 R!H u0 {2,[S,D]} {6,[S,D]}
5 *2 S2s u0 p2 c0 {3,[S,D]} {7,S}
6 *3 R!H u1 {4,[S,D]}
7 *1 C   u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "Ct",
    group = 
"""
1 *1 Ct u0
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "Cds",
    group = 
"""
1 *1 Cd u0
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "C-RRR",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S}
2    R u0 {1,S}
3    R u0 {1,S}
4    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "C-OneDe",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    R                u0 {1,S}
4    R                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "C-CdCsCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "C-CdSsCs",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S}
2    Cd  u0 {1,S}
3    S2s u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "C-CdSsSs",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S}
2    Cd  u0 {1,S}
3    S2s u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "C-CtCsCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "C-CtSsCs",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S}
2    Ct  u0 {1,S}
3    S2s u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "C-CtSsSs",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S}
2    Ct  u0 {1,S}
3    S2s u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "C-CtSsH",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S}
2    Ct  u0 {1,S}
3    S2s u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "C-CtCsH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "C-CdSsH",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S}
2    Cd  u0 {1,S}
3    S2s u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "C-CdCsH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "C-CtHH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "C-CdHH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "C-NonDe",
    group = 
"""
1 *1 C              u0 {2,S} {3,S} {4,S}
2    [H,Cs,O2s,S2s] u0 {1,S}
3    [H,Cs,O2s,S2s] u0 {1,S}
4    [H,Cs,O2s,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "C-OneS",
    group = 
"""
1 *1 C          u0 {2,S} {3,S} {4,S}
2    S2s        u0 {1,S}
3    [H,Cs,O2s] u0 {1,S}
4    [H,Cs,O2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "C-SsCsCs",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "C-SsCsH",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "C-SsHH",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "C-CsCsCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cs u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "C-CsCsH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cs u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "C-CsHH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cs u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "C-HHH",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "CJ",
    group = 
"""
1 *3 C u1
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "CdsJ",
    group = 
"""
1 *3 Cd  u1 {2,D}
2    R!H u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "CsJ",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    R  u0 {1,S}
3    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "CsJ-Cd",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    Cd u0 {1,S}
3    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "CsJ-CdCs",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    Cd u0 {1,S}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "CsJ-CdSs",
    group = 
"""
1 *3 Cs  u1 {2,S} {3,S}
2    Cd  u0 {1,S}
3    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "CsJ-CdH",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    Cd u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "CsJ-S2s",
    group = 
"""
1 *3 Cs  u1 {2,S} {3,S}
2    S2s u0 {1,S}
3    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "CsJ-SsCs",
    group = 
"""
1 *3 Cs  u1 {2,S} {3,S}
2    S2s u0 {1,S}
3    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "CsJ-SsSs",
    group = 
"""
1 *3 Cs  u1 {2,S} {3,S}
2    S2s u0 {1,S}
3    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "CsJ-SsH",
    group = 
"""
1 *3 Cs  u1 {2,S} {3,S}
2    S2s u0 {1,S}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "CsJ-Cs",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    Cs u0 {1,S}
3    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "CsJ-CsCs",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    Cs u0 {1,S}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "CsJ-CsH",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    Cs u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "CsJ-HH",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "SsJ",
    group = 
"""
1 *3 S2s u1
""",
    kinetics = None,
)

tree(
"""
L1: XSYJ
    L2: XSR3J
        L3: XSR3J_S
    L2: XSR4J
        L3: XSR4J_SS
            L4: XSR4J_SS_Cs
            L4: XSR4J_SS_Ss
        L3: XSR4J_SD
    L2: XSR5J
        L3: XSR5J_SSS
        L3: XSR5J_SSD
        L3: XSR5J_SDS
        L3: XSR5J_SDD
    L2: XSR6J
    L2: XSR7J
L1: C
    L2: Ct
    L2: Cds
    L2: C-RRR
        L3: C-OneDe
            L4: C-CdCsCs
            L4: C-CdSsCs
            L4: C-CdSsSs
            L4: C-CtCsCs
            L4: C-CtSsCs
            L4: C-CtSsSs
            L4: C-CtSsH
            L4: C-CtCsH
            L4: C-CdSsH
            L4: C-CdCsH
            L4: C-CtHH
            L4: C-CdHH
        L3: C-NonDe
            L4: C-OneS
                L5: C-SsCsCs
                L5: C-SsCsH
                L5: C-SsHH
            L4: C-CsCsCs
            L4: C-CsCsH
            L4: C-CsHH
            L4: C-HHH
L1: YJ
    L2: CJ
        L3: CdsJ
        L3: CsJ
            L4: CsJ-Cd
                L5: CsJ-CdCs
                L5: CsJ-CdSs
                L5: CsJ-CdH
            L4: CsJ-S2s
                L5: CsJ-SsCs
                L5: CsJ-SsSs
                L5: CsJ-SsH
            L4: CsJ-Cs
                L5: CsJ-CsCs
                L5: CsJ-CsH
            L4: CsJ-HH
    L2: SsJ
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

