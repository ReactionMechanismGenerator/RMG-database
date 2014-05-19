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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,{S,D}}
2 *2 Ss  U0 {1,{S,D}} {3,S}
3 *1 C   U0 {2,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,S}
2 *2 Ss  U0 {1,S} {3,S}
3 *1 C   U0 {2,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,{S,D}}
2 *4 R!H U0 {1,{S,D}} {3,{S,D}}
3 *2 Ss  U0 {2,{S,D}} {4,S}
4 *1 C   U0 {3,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,S}
2 *4 R!H U0 {1,S} {3,S}
3 *2 Ss  U0 {2,S} {4,S}
4 *1 C   U0 {3,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,D}
2 *4 R!H U0 {1,D} {3,S}
3 *2 Ss  U0 {2,S} {4,S}
4 *1 C   U0 {3,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,{S,D}}
2 *4 R!H U0 {1,{S,D}} {3,{S,D}}
3 *5 R!H U0 {2,{S,D}} {4,{S,D}}
4 *2 Ss  U0 {3,{S,D}} {5,S}
5 *1 C   U0 {4,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,S}
2 *4 R!H U0 {1,S} {3,S}
3 *5 R!H U0 {2,S} {4,S}
4 *2 Ss  U0 {3,S} {5,S}
5 *1 C   U0 {4,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,D}
2 *4 R!H U0 {1,D} {3,S}
3 *5 R!H U0 {2,S} {4,S}
4 *2 Ss  U0 {3,S} {5,S}
5 *1 C   U0 {4,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,S}
2 *4 R!H U0 {1,S} {3,D}
3 *5 R!H U0 {2,D} {4,S}
4 *2 Ss  U0 {3,S} {5,S}
5 *1 C   U0 {4,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,D}
2 *4 R!H U0 {1,D} {3,D}
3 *5 R!H U0 {2,D} {4,S}
4 *2 Ss  U0 {3,S} {5,S}
5 *1 C   U0 {4,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,{S,D}}
2 *4 R!H U0 {1,{S,D}} {3,{S,D}}
3 *5 R!H U0 {2,{S,D}} {4,{S,D}}
4 *6 R!H U0 {3,{S,D}} {5,{S,D}}
5 *2 Ss  U0 {4,{S,D}} {6,S}
6 *1 C   U0 {5,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,{S,D}}
2 *4 R!H U0 {1,{S,D}} {3,{S,D}}
3 *5 R!H U0 {2,{S,D}} {4,{S,D}}
4 *6 R!H U0 {3,{S,D}} {5,{S,D}}
5 *7 R!H U0 {4,{S,D}} {6,{S,D}}
6 *2 Ss  U0 {5,{S,D}} {7,S}
7 *1 C   U0 {6,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2 *4 C U0 {1,D}
3    R U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2 *4 C U0 {1,D}
3    H U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2 *4 C  U0 {1,D}
3    Cs U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2 *4 C  U0 {1,D}
3    Ss U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2 *4 C  U0 {1,D}
3    Cd U0 {1,S} {4,D}
4    C  U0 {3,D}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2    R U0 {1,D}
3 *4 R U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2    C U0 {1,D}
3 *4 R U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    C  U0 {1,D}
3 *4 Cs U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    C  U0 {1,D}
3 *4 Ss U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2    S U0 {1,D}
3 *4 R U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    C  U0 {1,D}
3 *4 Cd U0 {1,S} {4,D}
4    C  U0 {3,D}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
2 *4 R U0 {1,S}
3    R U0 {1,S}
4    R U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Cs U0 {1,S}
3    R  U0 {1,S}
4    R  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Cs U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Cs U0 {1,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Cs U0 {1,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Cs U0 {1,S}
3    Ss U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Cs U0 {1,S}
3    Ss U0 {1,S}
4    Ss U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Cs U0 {1,S}
3    Cs U0 {1,S}
4    Ss U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *4 Cs            U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {H,Cs,Os,Ss}  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *4 Cs            U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    H             U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Cs U0 {1,S}
3    Cd U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *4 Cs            U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    Cs            U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Cs U0 {1,S}
3    Cd U0 {1,S}
4    Cs U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *4 Cs            U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    Ss            U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Cs U0 {1,S}
3    Cd U0 {1,S}
4    Ss U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *4 Cs            U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Cd U0 {1,S}
3    R  U0 {1,S}
4    R  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Cd U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Cd U0 {1,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Cd U0 {1,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Cd U0 {1,S}
3    Ss U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Cd U0 {1,S}
3    Ss U0 {1,S}
4    Ss U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Cd U0 {1,S}
3    Cs U0 {1,S}
4    Ss U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *4 Cd            U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {H,Cs,Os,Ss}  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *4 Cd            U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    H             U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Cd U0 {1,S}
3    Cd U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *4 Cd            U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    Cs            U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Cd U0 {1,S}
3    Cd U0 {1,S}
4    Cs U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *4 Cd            U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    Ss            U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Cd U0 {1,S}
3    Cd U0 {1,S}
4    Ss U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *4 Cd            U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Ss U0 {1,S}
3    R  U0 {1,S}
4    R  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Ss U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Ss U0 {1,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Ss U0 {1,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Ss U0 {1,S}
3    Ss U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Ss U0 {1,S}
3    Ss U0 {1,S}
4    Ss U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Ss U0 {1,S}
3    Cs U0 {1,S}
4    Ss U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *4 Ss            U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {H,Cs,Os,Ss}  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *4 Ss            U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    H             U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Ss U0 {1,S}
3    Cd U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *4 Ss            U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    Cs            U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Ss U0 {1,S}
3    Cd U0 {1,S}
4    Cs U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *4 Ss            U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    Ss            U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Ss U0 {1,S}
3    Cd U0 {1,S}
4    Ss U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2 *4 R  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2 *4 R  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2 *4 Cs U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2 *4 Ss U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss            U1 {2,S}
2 *4 {Cd,Ct,Cb,CO} U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2 *4 Cd U0 {1,S} {3,D}
3    C  U0 {2,D}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    R  U0 {1,D}
3 *2 Ss U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *2 Ss U0 {1,S}
3    R  U0 {1,S}
4    R  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *2 Ss U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *2 Ss U0 {1,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *2 Ss U0 {1,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *2 Ss U0 {1,S}
3    Ss U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *2 Ss U0 {1,S}
3    Ss U0 {1,S}
4    Ss U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *2 Ss U0 {1,S}
3    Cs U0 {1,S}
4    Ss U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *2 Ss            U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {H,Cs,Os,Ss}  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *2 Ss            U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    H             U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *2 Ss U0 {1,S}
3    Cd U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *2 Ss            U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    Cs            U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *2 Ss U0 {1,S}
3    Cd U0 {1,S}
4    Cs U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *2 Ss            U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    Ss            U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *2 Ss U0 {1,S}
3    Cd U0 {1,S}
4    Ss U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *2 Ss            U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2 *2 Ss U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,S} {3,D}
2    R  U0 {1,S}
3    R  U0 {1,D}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,S} {3,S} {4,S}
2    R U0 {1,S}
3    R U0 {1,S}
4    R U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C            U0 {2,S} {3,S} {4,S}
2    {H,Cs,Os,Ss} U0 {1,S}
3    {H,Cs,Os,Ss} U0 {1,S}
4    {H,Cs,Os,Ss} U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    H U0 {1,S}
4    H U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cs U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cs U0 {1,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cs U0 {1,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C         U0 {2,S} {3,S} {4,S}
2    Ss        U0 {1,S}
3    {H,Cs,Os} U0 {1,S}
4    {H,Cs,Os} U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Ss U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Ss U0 {1,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Ss U0 {1,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    R             U0 {1,S}
4    R             U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cd U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cd U0 {1,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cd U0 {1,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cd U0 {1,S}
3    Ss U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cd U0 {1,S}
3    Ss U0 {1,S}
4    Cs U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cd U0 {1,S}
3    Ss U0 {1,S}
4    Ss U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    Ss U0 {1,S}
4    H  U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    Ss U0 {1,S}
4    Cs U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    Ss U0 {1,S}
4    Ss U0 {1,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R U0 {2,{S,D}}
2 *3 R U1 {1,{S,D}}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "RR_birad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R U1 {2,{S,D}}
2    R U1 {1,{S,D}}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

