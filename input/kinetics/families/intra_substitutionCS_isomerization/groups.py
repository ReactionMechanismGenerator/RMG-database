#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionCS_isomerization/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["XSYJ"], products=["XSYJ"], ownReverse=True)

recipe(actions=[
    ['BREAK_BOND', '*1', 'S', '*2'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "XSYJ",
    group = "OR{XSR3J, XSR4J, XSR5J, XSR6J, XSR7J}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "YJ",
    group = "OR{CJ, SJ, CJ-3, SJ-3}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "C",
    group = "OR{C-RRR, Cds-R, Ct}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "XSR3J",
    group = 
"""
1 *3 R!H 1 {2,{S,D}}
2 *2 Ss  0 {1,{S,D}} {3,S}
3 *1 C   0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "XSR3J_S",
    group = 
"""
1 *3 R!H 1 {2,S}
2 *2 Ss  0 {1,S} {3,S}
3 *1 C   0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "XSR4J",
    group = 
"""
1 *3 R!H 1 {2,{S,D}}
2 *4 R!H 0 {1,{S,D}} {3,{S,D}}
3 *2 Ss  0 {2,{S,D}} {4,S}
4 *1 C   0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "XSR4J_SS",
    group = 
"""
1 *3 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *2 Ss  0 {2,S} {4,S}
4 *1 C   0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "XSR4J_SD",
    group = 
"""
1 *3 R!H 1 {2,D}
2 *4 R!H 0 {1,D} {3,S}
3 *2 Ss  0 {2,S} {4,S}
4 *1 C   0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "XSR5J",
    group = 
"""
1 *3 R!H 1 {2,{S,D}}
2 *4 R!H 0 {1,{S,D}} {3,{S,D}}
3 *5 R!H 0 {2,{S,D}} {4,{S,D}}
4 *2 Ss  0 {3,{S,D}} {5,S}
5 *1 C   0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "XSR5J_SSS",
    group = 
"""
1 *3 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 Ss  0 {3,S} {5,S}
5 *1 C   0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "XSR5J_SSD",
    group = 
"""
1 *3 R!H 1 {2,D}
2 *4 R!H 0 {1,D} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 Ss  0 {3,S} {5,S}
5 *1 C   0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "XSR5J_SDS",
    group = 
"""
1 *3 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,D}
3 *5 R!H 0 {2,D} {4,S}
4 *2 Ss  0 {3,S} {5,S}
5 *1 C   0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "XSR5J_SDD",
    group = 
"""
1 *3 R!H 1 {2,D}
2 *4 R!H 0 {1,D} {3,D}
3 *5 R!H 0 {2,D} {4,S}
4 *2 Ss  0 {3,S} {5,S}
5 *1 C   0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "XSR6J",
    group = 
"""
1 *3 R!H 1 {2,{S,D}}
2 *4 R!H 0 {1,{S,D}} {3,{S,D}}
3 *5 R!H 0 {2,{S,D}} {4,{S,D}}
4 *6 R!H 0 {3,{S,D}} {5,{S,D}}
5 *2 Ss  0 {4,{S,D}} {6,S}
6 *1 C   0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "XSR7J",
    group = 
"""
1 *3 R!H 1 {2,{S,D}}
2 *4 R!H 0 {1,{S,D}} {3,{S,D}}
3 *5 R!H 0 {2,{S,D}} {4,{S,D}}
4 *6 R!H 0 {3,{S,D}} {5,{S,D}}
5 *7 R!H 0 {4,{S,D}} {6,{S,D}}
6 *2 Ss  0 {5,{S,D}} {7,S}
7 *1 C   0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "CJ",
    group = "OR{CsJ, CdsJ, CdsJ-2}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "CdsJ",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2 *4 C 0 {1,D}
3    R 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "CdsJ-H",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2 *4 C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "CdsJ-Cs",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2 *4 C  0 {1,D}
3    Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "CdsJ-Ss",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2 *4 C  0 {1,D}
3    Ss 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "CdsJ-Cd",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2 *4 C  0 {1,D}
3    Cd 0 {1,S} {4,D}
4    C  0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "CdsJ-2",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    R 0 {1,D}
3 *4 R 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "CdsJ_C-2",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3 *4 R 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "CdsJ_C-Cs2",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3 *4 Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "CdsJ_C-Ss2",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3 *4 Ss 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "CdsJ_S-2",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    S 0 {1,D}
3 *4 R 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "CdsJ_C-Cd2",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3 *4 Cd 0 {1,S} {4,D}
4    C  0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "CsJ",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2 *4 R 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "CsJ-Cs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Cs 0 {1,S}
3    R  0 {1,S}
4    R  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "CsJ-CsHH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Cs 0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "CsJ-CsCsH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Cs 0 {1,S}
3    Cs 0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "CsJ-CsCsCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "CsJ-CsSsH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Cs 0 {1,S}
3    Ss 0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "CsJ-CsSsSs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Cs 0 {1,S}
3    Ss 0 {1,S}
4    Ss 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "CsJ-CsCsSs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Cs 0 {1,S}
3    Cs 0 {1,S}
4    Ss 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "CsJ-CsOneDe",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2 *4 Cs            0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {H,Cs,Os,Ss}  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "CsJ-CsOneDeH",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2 *4 Cs            0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "CsJ-CsCdH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Cs 0 {1,S}
3    Cd 0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "CsJ-CsOneDeCs",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2 *4 Cs            0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    Cs            0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "CsJ-CsCdCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Cs 0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "CsJ-CsOneDeSs",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2 *4 Cs            0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    Ss            0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "CsJ-CsCdSs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Cs 0 {1,S}
3    Cd 0 {1,S}
4    Ss 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "CsJ-CsTwoDe",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2 *4 Cs            0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "CsJ-Cd",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Cd 0 {1,S}
3    R  0 {1,S}
4    R  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "CsJ-CdHH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Cd 0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "CsJ-CdCsH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Cd 0 {1,S}
3    Cs 0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "CsJ-CdCsCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Cd 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "CsJ-CdSsH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Cd 0 {1,S}
3    Ss 0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "CsJ-CdSsSs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Cd 0 {1,S}
3    Ss 0 {1,S}
4    Ss 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "CsJ-CdCsSs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Cd 0 {1,S}
3    Cs 0 {1,S}
4    Ss 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "CsJ-CdOneDe",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2 *4 Cd            0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {H,Cs,Os,Ss}  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "CsJ-CdOneDeH",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2 *4 Cd            0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "CsJ-CdCdH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Cd 0 {1,S}
3    Cd 0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "CsJ-CdOneDeCs",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2 *4 Cd            0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    Cs            0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "CsJ-CdCdCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Cd 0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "CsJ-CdOneDeSs",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2 *4 Cd            0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    Ss            0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "CsJ-CdCdSs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Cd 0 {1,S}
3    Cd 0 {1,S}
4    Ss 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "CsJ-CdTwoDe",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2 *4 Cd            0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "CsJ-Ss",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Ss 0 {1,S}
3    R  0 {1,S}
4    R  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "CsJ-SsHH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Ss 0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "CsJ-SsCsH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Ss 0 {1,S}
3    Cs 0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "CsJ-SsCsCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Ss 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "CsJ-SsSsH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Ss 0 {1,S}
3    Ss 0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "CsJ-SsSsSs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Ss 0 {1,S}
3    Ss 0 {1,S}
4    Ss 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "CsJ-SsCsSs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Ss 0 {1,S}
3    Cs 0 {1,S}
4    Ss 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "CsJ-SsOneDe",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2 *4 Ss            0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {H,Cs,Os,Ss}  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "CsJ-SsOneDeH",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2 *4 Ss            0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "CsJ-SsCdH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Ss 0 {1,S}
3    Cd 0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "CsJ-SsOneDeCs",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2 *4 Ss            0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    Cs            0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "CsJ-SsCdCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Ss 0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "CsJ-SsOneDeSs",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2 *4 Ss            0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    Ss            0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "CsJ-SsCdSs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *4 Ss 0 {1,S}
3    Cd 0 {1,S}
4    Ss 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "SJ",
    group = 
"""
1 *3 S 1 {2,S}
2 *4 R  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "SsJ",
    group = 
"""
1 *3 Ss 1 {2,S}
2 *4 R  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "SsJ-Cs",
    group = 
"""
1 *3 Ss 1 {2,S}
2 *4 Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "SsJ-Ss",
    group = 
"""
1 *3 Ss 1 {2,S}
2 *4 Ss 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "SsJ-OneDe",
    group = 
"""
1 *3 Ss            1 {2,S}
2 *4 {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "SsJ-Cd",
    group = 
"""
1 *3 Ss 1 {2,S}
2 *4 Cd 0 {1,S} {3,D}
3    C  0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "CJ-3",
    group = "OR{CsJ-3, CdsJ-3}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "CdsJ-3",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    R  0 {1,D}
3 *2 Ss 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "CsJ-3",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *2 Ss 0 {1,S}
3    R  0 {1,S}
4    R  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "CsJ-3-SsHH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *2 Ss 0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "CsJ-3-SsCsH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *2 Ss 0 {1,S}
3    Cs 0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "CsJ-3-SsCsCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *2 Ss 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "CsJ-3-SsSsH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *2 Ss 0 {1,S}
3    Ss 0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "CsJ-3-SsSsSs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *2 Ss 0 {1,S}
3    Ss 0 {1,S}
4    Ss 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "CsJ-3-SsCsSs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *2 Ss 0 {1,S}
3    Cs 0 {1,S}
4    Ss 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "CsJ-3-SsOneDe",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2 *2 Ss            0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {H,Cs,Os,Ss}  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "CsJ-3-SsOneDeH",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2 *2 Ss            0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "CsJ-3-SsCdH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *2 Ss 0 {1,S}
3    Cd 0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "CsJ-3-SsOneDeCs",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2 *2 Ss            0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    Cs            0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "CsJ-3-SsCdCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *2 Ss 0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "CsJ-3-SsOneDeSs",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2 *2 Ss            0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    Ss            0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "CsJ-3-SsCdSs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2 *2 Ss 0 {1,S}
3    Cd 0 {1,S}
4    Ss 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "CsJ-3-SsTwoDe",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2 *2 Ss            0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "SJ-3",
    group = 
"""
1 *3 Ss 1 {2,S}
2 *2 Ss 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "Ct",
    group = 
"""
1 *1 Ct 0
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "Cds-R",
    group = 
"""
1 *1 Cd 0 {2,S} {3,D}
2    R  0 {1,S}
3    R  0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "C-RRR",
    group = 
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2    R 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "C-NonDe",
    group = 
"""
1 *1 C            0 {2,S} {3,S} {4,S}
2    {H,Cs,Os,Ss} 0 {1,S}
3    {H,Cs,Os,Ss} 0 {1,S}
4    {H,Cs,Os,Ss} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "C-HHH",
    group = 
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "C-CsHH",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "C-CsCsH",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "C-CsCsCs",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "C-OneS",
    group = 
"""
1 *1 C         0 {2,S} {3,S} {4,S}
2    Ss        0 {1,S}
3    {H,Cs,Os} 0 {1,S}
4    {H,Cs,Os} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "C-SsHH",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S}
2    Ss 0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "C-SsCsH",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S}
2    Ss 0 {1,S}
3    Cs 0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "C-SsCsCs",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S}
2    Ss 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    label = "C-OneDe",
    group = 
"""
1 *1 C             0 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    R             0 {1,S}
4    R             0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "C-CdHH",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "C-CdCsH",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cs 0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "C-CdCsCs",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "C-CdSsH",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Ss 0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "C-CdSsCs",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Ss 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    label = "C-CdSsSs",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Ss 0 {1,S}
4    Ss 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "C-CtHH",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    label = "C-CtCsH",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cs 0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "C-CtCsCs",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "C-CtSsH",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Ss 0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
    label = "C-CtSsCs",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Ss 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    label = "C-CtSsSs",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Ss 0 {1,S}
4    Ss 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: XSYJ
    L2: XSR3J
        L3: XSR3J_S
    L2: XSR4J
        L3: XSR4J_SS
        L3: XSR4J_SD
    L2: XSR5J
        L3: XSR5J_SSS
        L3: XSR5J_SSD
        L3: XSR5J_SDS
        L3: XSR5J_SDD
    L2: XSR6J
    L2: XSR7J
L1: YJ
    L2: CJ
        L3: CdsJ
            L4: CdsJ-H
            L4: CdsJ-Cs
            L4: CdsJ-Ss
            L4: CdsJ-Cd
        L3: CdsJ-2
            L4: CdsJ_C-2
            L4: CdsJ_C-Cs2
            L4: CdsJ_C-Ss2
            L4: CdsJ_S-2
            L4: CdsJ_C-Cd2
        L3: CsJ
            L4: CsJ-Cs
                L5: CsJ-CsHH
                L5: CsJ-CsCsH
                L5: CsJ-CsCsCs
                L5: CsJ-CsSsH
                L5: CsJ-CsSsSs
                L5: CsJ-CsCsSs
                L5: CsJ-CsOneDe
                    L6: CsJ-CsOneDeH
                        L7: CsJ-CsCdH
                    L6: CsJ-CsOneDeCs
                        L7: CsJ-CsCdCs
                    L6: CsJ-CsOneDeSs
                        L7: CsJ-CsCdSs
                L5: CsJ-CsTwoDe
            L4: CsJ-Cd
                L5: CsJ-CdHH
                L5: CsJ-CdCsH
                L5: CsJ-CdCsCs
                L5: CsJ-CdSsH
                L5: CsJ-CdSsSs
                L5: CsJ-CdCsSs
                L5: CsJ-CdOneDe
                    L6: CsJ-CdOneDeH
                        L7: CsJ-CdCdH
                    L6: CsJ-CdOneDeCs
                        L7: CsJ-CdCdCs
                    L6: CsJ-CdOneDeSs
                        L7: CsJ-CdCdSs
                L5: CsJ-CdTwoDe
            L4: CsJ-Ss
                L5: CsJ-SsHH
                L5: CsJ-SsCsH
                L5: CsJ-SsCsCs
                L5: CsJ-SsSsH
                L5: CsJ-SsSsSs
                L5: CsJ-SsCsSs
                L5: CsJ-SsOneDe
                    L6: CsJ-SsOneDeH
                        L7: CsJ-SsCdH
                    L6: CsJ-SsOneDeCs
                        L7: CsJ-SsCdCs
                    L6: CsJ-SsOneDeSs
                        L7: CsJ-SsCdSs
    L2: SJ
        L3: SsJ
            L4: SsJ-Cs
            L4: SsJ-Ss
            L4: SsJ-OneDe
                L5: SsJ-Cd
    L2: CJ-3
        L3: CdsJ-3
        L3: CsJ-3
            L4: CsJ-3-SsHH
            L4: CsJ-3-SsCsH
            L4: CsJ-3-SsCsCs
            L4: CsJ-3-SsSsH
            L4: CsJ-3-SsSsSs
            L4: CsJ-3-SsCsSs
            L4: CsJ-3-SsOneDe
                L5: CsJ-3-SsOneDeH
                    L6: CsJ-3-SsCdH
                L5: CsJ-3-SsOneDeCs
                    L6: CsJ-3-SsCdCs
                L5: CsJ-3-SsOneDeSs
                    L6: CsJ-3-SsCdSs
            L4: CsJ-3-SsTwoDe
    L2: SJ-3
L1: C
    L2: Ct
    L2: Cds-R
    L2: C-RRR
        L3: C-NonDe
            L4: C-HHH
            L4: C-CsHH
            L4: C-CsCsH
            L4: C-CsCsCs
            L4: C-OneS
                L5: C-SsHH
                L5: C-SsCsH
                L5: C-SsCsCs
        L3: C-OneDe
            L4: C-CdHH
            L4: C-CdCsH
            L4: C-CdCsCs
            L4: C-CdSsH
            L4: C-CdSsCs
            L4: C-CdSsSs
            L4: C-CtHH
            L4: C-CtCsH
            L4: C-CtCsCs
            L4: C-CtSsH
            L4: C-CtSsCs
            L4: C-CtSsSs
"""
)

forbidden(
    label = "RR_13",
    group = 
"""
1 *1 R 0 {2,{S,D}}
2 *3 R 1 {1,{S,D}}
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
1 *3 R 1 {2,{S,D}}
2    R 1 {1,{S,D}}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

