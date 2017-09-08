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
    label = "Cs",
    group = 
"""
1 *1 Cs u0
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "Cs-RR",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S}
2    R  u0 {1,S}
3    R  u0 {1,S}
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
3 *1 Cs  u0 {2,S} {4,S}
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
3 *1 Cs  u0 {2,S} {4,S}
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
3 *1 Cs  u0 {2,S} {4,S}
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
4 *1 Cs  u0 {3,S} {5,S}
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
4 *1 Cs  u0 {3,S} {5,S}
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
4 *1 Cs  u0 {3,S} {5,S}
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
4 *1 Cs  u0 {3,S} {5,S}
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
4 *1 Cs  u0 {3,S} {5,S}
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
5 *1 Cs  u0 {4,S} {6,S}
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
5 *1 Cs  u0 {4,S} {6,S}
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
5 *1 Cs  u0 {4,S} {6,S}
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
5 *1 Cs  u0 {4,S} {6,S}
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
5 *1 Cs  u0 {4,S} {6,S}
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
5 *1 Cs  u0 {4,S} {6,S}
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
5 *1 Cs  u0 {4,S} {6,S}
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
5 *1 Cs  u0 {4,S} {6,S}
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
5 *1 Cs  u0 {4,S} {6,S}
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
6 *1 Cs  u0 {5,S} {7,S}
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
7 *1 Cs  u0 {6,S} {8,S}
8 *2 S  u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "CJ",
    group = 
"""
1 *3 C u1
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "CdsJ",
    group = 
"""
1 *3 [Cd,Cdd] u1
""",
    kinetics = None,
)

entry(
    index = 36,
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
    index = 37,
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
    index = 38,
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
    index = 39,
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
    index = 40,
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
    index = 52,
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
    index = 54,
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
    index = 55,
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
    index = 57,
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
    index = 67,
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
    index = 69,
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
    index = 70,
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
    index = 72,
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
    index = 82,
    label = "SsJ",
    group = 
"""
1 *3 S2s u1
""",
    kinetics = None,
)

entry(
    index = 150,
    label = "Cs-RC",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S}
2    C  u0 {1,S}
3    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 151,
    label = "Cs-(NonDe)C",
    group = 
"""
1 *1 Cs            u0 {2,S} {3,S}
2    C             u0 {1,S}
3    [H,Cs,Os,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 153,
    label = "Cs-HC",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S}
2    C  u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 154,
    label = "Cs-CsC",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S}
2    C  u0 {1,S}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 155,
    label = "Cs-(De)C",
    group = 
"""
1 *1 Cs               u0 {2,S} {3,S}
2    C                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 157,
    label = "Cs-RS",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S}
2    S  u0 {1,S}
3    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 158,
    label = "Cs-(NonDe)S",
    group = 
"""
1 *1 Cs            u0 {2,S} {3,S}
2    S             u0 {1,S}
3    [H,Cs,Os,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 160,
    label = "Cs-HS",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S}
2    S  u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 161,
    label = "Cs-CsS",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S}
2    S  u0 {1,S}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 162,
    label = "Cs-(De)S",
    group = 
"""
1 *1 Cs               u0 {2,S} {3,S}
2    S                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 162,
    label = "Cs-HH",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
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
    label = "S-S2s",
    group = 
"""
1 *2 S   u0 {2,S}
2    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 167,
    label = "S-SJ",
    group = 
"""
1 *2 S u0 {2,S}
2    S u1 {1,S}
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

L1: Cs
    L2: Cs-RR
        L3: Cs-RS
            L4: Cs-(De)S
            L4: Cs-(NonDe)S
                L5: Cs-CsS
                L5: Cs-HS
        L3: Cs-RC
            L4: Cs-(De)C
            L4: Cs-(NonDe)C
                L5: Cs-CsC
                L5: Cs-HC
        L3: Cs-HH

L1: S
    L2: S-Cs
    L2: S-S2s
    L2: S-SJ
    L2: S-H
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

