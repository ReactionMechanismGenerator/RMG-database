#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionS_cyclization/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["XSYJ"], products=["SY", "XJ"], ownReverse=False)

reverse = "Ring_OpeningS"

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
    label = "S-RR",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 R  U0 {1,S}
3 *4 R  U0 {1,S}
""",
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
2 *4 R!H U0 {1,{S,D}} {3,S}
3 *1 Ss  U0 {2,S} {4,S}
4 *2 R   U0 {3,S}
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
2 *4 R!H U0 {1,S} {3,S}
3 *1 Ss  U0 {2,S} {4,S}
4 *2 R   U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "XSR3J_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,D}
2 *4 R!H U0 {1,D} {3,S}
3 *1 Ss  U0 {2,S} {4,S}
4 *2 R   U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "XSR4J",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,{S,D}}
2 *5 R!H U0 {1,{S,D}} {3,{S,D}}
3 *4 R!H U0 {2,{S,D}} {4,S}
4 *1 Ss  U0 {3,S} {5,S}
5 *2 R   U0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "XSR4J_SS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,S}
2 *5 R!H U0 {1,S} {3,S}
3 *4 R!H U0 {2,S} {4,S}
4 *1 Ss  U0 {3,S} {5,S}
5 *2 R   U0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "XSR4J_SD",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,D}
2 *5 R!H U0 {1,D} {3,S}
3 *4 R!H U0 {2,S} {4,S}
4 *1 Ss  U0 {3,S} {5,S}
5 *2 R   U0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "XSR4J_DS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,S}
2 *5 R!H U0 {1,S} {3,D}
3 *4 R!H U0 {2,D} {4,S}
4 *1 Ss  U0 {3,S} {5,S}
5 *2 R   U0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "XSR4J_DD",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,D}
2 *5 R!H U0 {1,D} {3,D}
3 *4 R!H U0 {2,D} {4,S}
4 *1 Ss  U0 {3,S} {5,S}
5 *2 R   U0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "XSR5J",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,{S,D}}
2 *5 R!H U0 {1,{S,D}} {3,{S,D}}
3 *6 R!H U0 {2,{S,D}} {4,{S,D}}
4 *4 R!H U0 {3,{S,D}} {5,S}
5 *1 Ss  U0 {4,S} {6,S}
6 *2 R   U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "XSR5J_SSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,S}
2 *5 R!H U0 {1,S} {3,S}
3 *6 R!H U0 {2,S} {4,S}
4 *4 R!H U0 {3,S} {5,S}
5 *1 Ss  U0 {4,S} {6,S}
6 *2 R   U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "XSR5J_SSD",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,D}
2 *5 R!H U0 {1,D} {3,S}
3 *6 R!H U0 {2,S} {4,S}
4 *4 R!H U0 {3,S} {5,S}
5 *1 Ss  U0 {4,S} {6,S}
6 *2 R   U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "XSR5J_SDS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,S}
2 *5 R!H U0 {1,S} {3,D}
3 *6 R!H U0 {2,D} {4,S}
4 *4 R!H U0 {3,S} {5,S}
5 *1 Ss  U0 {4,S} {6,S}
6 *2 R   U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "XSR5J_DSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,S}
2 *5 R!H U0 {1,S} {3,S}
3 *6 R!H U0 {2,S} {4,D}
4 *4 R!H U0 {3,D} {5,S}
5 *1 Ss  U0 {4,S} {6,S}
6 *2 R   U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "XSR5J_DDS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,S}
2 *5 R!H U0 {1,S} {3,D}
3 *6 R!H U0 {2,D} {4,D}
4 *4 R!H U0 {3,D} {5,S}
5 *1 Ss  U0 {4,S} {6,S}
6 *2 R   U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "XSR5J_DSD",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,D}
2 *5 R!H U0 {1,D} {3,S}
3 *6 R!H U0 {2,S} {4,D}
4 *4 R!H U0 {3,D} {5,S}
5 *1 Ss  U0 {4,S} {6,S}
6 *2 R   U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "XSR5J_SDD",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,D}
2 *5 R!H U0 {1,D} {3,D}
3 *6 R!H U0 {2,D} {4,S}
4 *4 R!H U0 {3,S} {5,S}
5 *1 Ss  U0 {4,S} {6,S}
6 *2 R   U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "XSR5J_DDD",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,D}
2 *5 R!H U0 {1,D} {3,D}
3 *6 R!H U0 {2,D} {4,D}
4 *4 R!H U0 {3,D} {5,S}
5 *1 Ss  U0 {4,S} {6,S}
6 *2 R   U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "XSR6J",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,{S,D}}
2 *5 R!H U0 {1,{S,D}} {3,{S,D}}
3 *6 R!H U0 {2,{S,D}} {4,{S,D}}
4 *7 R!H U0 {3,{S,D}} {5,{S,D}}
5 *4 R!H U0 {4,{S,D}} {6,S}
6 *1 Ss  U0 {5,S} {7,S}
7 *2 R   U0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "XSR6J_SSSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,S}
2 *5 R!H U0 {1,S} {3,S}
3 *6 R!H U0 {2,S} {4,S}
4 *7 R!H U0 {3,S} {5,S}
5 *4 R!H U0 {4,S} {6,S}
6 *1 Ss  U0 {5,S} {7,S}
7 *2 R   U0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "XSR7J",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,{S,D}}
2 *5 R!H U0 {1,{S,D}} {3,{S,D}}
3 *6 R!H U0 {2,{S,D}} {4,{S,D}}
4 *7 R!H U0 {3,{S,D}} {5,{S,D}}
5 *8 R!H U0 {4,{S,D}} {6,{S,D}}
6 *4 R!H U0 {5,{S,D}} {7,S}
7 *1 Ss  U0 {6,S} {8,S}
8 *2 R   U0 {7,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "CJ",
    group = "OR{CsJ, CdsJ, CdsJ-2}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "CdsJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2 *5 C U0 {1,D}
3    R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "CdsJ-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2 *5 C U0 {1,D}
3    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "CdsJ-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2 *5 C  U0 {1,D}
3    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "CdsJ-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2 *5 C  U0 {1,D}
3    Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "CdsJ-Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2 *5 C  U0 {1,D}
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
    index = 30,
    label = "CdsJ-2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2    R U0 {1,D}
3 *5 R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "CdsJ_C-2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2    C U0 {1,D}
3 *5 R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "CdsJ_C-Cs2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    C  U0 {1,D}
3 *5 Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "CdsJ_C-Ss2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    C  U0 {1,D}
3 *5 Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "CdsJ_C-Cd2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    C  U0 {1,D}
3 *5 Cd U0 {1,S} {4,D}
4    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "CdsJ_S-2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2    S U0 {1,D}
3 *5 R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "CsJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
2 *5 R U0 {1,S}
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
    index = 37,
    label = "CsJ-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Cs U0 {1,S}
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
    index = 38,
    label = "CsJ-CsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Cs U0 {1,S}
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
    index = 39,
    label = "CsJ-CsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Cs U0 {1,S}
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
    index = 40,
    label = "CsJ-CsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Cs U0 {1,S}
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
    index = 41,
    label = "CsJ-CsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Cs U0 {1,S}
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
    index = 42,
    label = "CsJ-CsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Cs U0 {1,S}
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
    index = 43,
    label = "CsJ-CsCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Cs U0 {1,S}
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
    index = 44,
    label = "CsJ-CsOneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *5 Cs            U0 {1,S}
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
    index = 45,
    label = "CsJ-CsOneDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *5 Cs            U0 {1,S}
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
    index = 46,
    label = "CsJ-CsCdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Cs U0 {1,S}
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
    index = 47,
    label = "CsJ-CsOneDeCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *5 Cs            U0 {1,S}
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
    index = 48,
    label = "CsJ-CsCdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Cs U0 {1,S}
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
    index = 49,
    label = "CsJ-CsOneDeSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *5 Cs            U0 {1,S}
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
    index = 50,
    label = "CsJ-CsCdSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Cs U0 {1,S}
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
    index = 51,
    label = "CsJ-CsTwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *5 Cs            U0 {1,S}
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
    index = 52,
    label = "CsJ-Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Cd U0 {1,S}
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
    index = 53,
    label = "CsJ-CdHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Cd U0 {1,S}
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
    index = 54,
    label = "CsJ-CdCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Cd U0 {1,S}
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
    index = 55,
    label = "CsJ-CdCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Cd U0 {1,S}
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
    index = 56,
    label = "CsJ-CdSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Cd U0 {1,S}
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
    index = 57,
    label = "CsJ-CdSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Cd U0 {1,S}
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
    index = 58,
    label = "CsJ-CdCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Cd U0 {1,S}
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
    index = 59,
    label = "CsJ-CdOneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *5 Cd            U0 {1,S}
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
    index = 60,
    label = "CsJ-CdOneDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *5 Cd            U0 {1,S}
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
    index = 61,
    label = "CsJ-CdCdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Cd U0 {1,S}
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
    index = 62,
    label = "CsJ-CdOneDeCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *5 Cd            U0 {1,S}
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
    index = 63,
    label = "CsJ-CdCdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Cd U0 {1,S}
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
    index = 64,
    label = "CsJ-CdOneDeSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *5 Cd            U0 {1,S}
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
    index = 65,
    label = "CsJ-CdCdSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Cd U0 {1,S}
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
    index = 66,
    label = "CsJ-CdTwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *5 Cd            U0 {1,S}
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
    index = 67,
    label = "CsJ-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Ss U0 {1,S}
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
    index = 68,
    label = "CsJ-SsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Ss U0 {1,S}
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
    index = 69,
    label = "CsJ-SsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Ss U0 {1,S}
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
    index = 70,
    label = "CsJ-SsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Ss U0 {1,S}
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
    index = 71,
    label = "CsJ-SsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Ss U0 {1,S}
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
    index = 72,
    label = "CsJ-SsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Ss U0 {1,S}
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
    index = 73,
    label = "CsJ-SsCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Ss U0 {1,S}
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
    index = 74,
    label = "CsJ-SsOneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *5 Ss            U0 {1,S}
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
    index = 75,
    label = "CsJ-SsOneDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *5 Ss            U0 {1,S}
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
    index = 76,
    label = "CsJ-SsCdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Ss U0 {1,S}
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
    index = 77,
    label = "CsJ-SsOneDeCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *5 Ss            U0 {1,S}
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
    index = 78,
    label = "CsJ-SsCdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Ss U0 {1,S}
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
    index = 79,
    label = "CsJ-SsOneDeSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2 *5 Ss            U0 {1,S}
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
    index = 80,
    label = "CsJ-SsCdSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *5 Ss U0 {1,S}
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
    index = 81,
    label = "SJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2 *5 R  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "SsJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2 *5 R  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "SsJ-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2 *5 Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "SsJ-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2 *5 Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "SsJ-OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss            U1 {2,S}
2 *5 {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "SsJ-Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2 *5 Cd U0 {1,S} {3,D}
3    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "CJ-3",
    group = "OR{CsJ-3, CdsJ-3, CdsJ-3-2}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "CdsJ-3",
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
    index = 89,
    label = "CdsJ-3-H",
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
    index = 90,
    label = "CdsJ-3-Cs",
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
    index = 91,
    label = "CdsJ-3-Ss",
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
    index = 92,
    label = "CdsJ-3-Cd",
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
    index = 93,
    label = "CdsJ-3-2",
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
    index = 94,
    label = "CdsJ_C-3-2",
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
    index = 95,
    label = "CdsJ_C-3-Cs2",
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
    index = 96,
    label = "CdsJ_C-3-Ss2",
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
    index = 97,
    label = "CdsJ_C-3-Cd2",
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
    index = 98,
    label = "CdsJ_S-3-2",
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
    index = 99,
    label = "CsJ-3",
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
    index = 100,
    label = "CsJ-3-Cs",
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
    index = 101,
    label = "CsJ-3-CsHH",
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
    index = 102,
    label = "CsJ-3-CsCsH",
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
    index = 103,
    label = "CsJ-3-CsCsCs",
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
    index = 104,
    label = "CsJ-3-CsSsH",
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
    index = 105,
    label = "CsJ-3-CsSsSs",
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
    index = 106,
    label = "CsJ-3-CsCsSs",
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
    index = 107,
    label = "CsJ-3-CsOneDe",
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
    index = 108,
    label = "CsJ-3-CsOneDeH",
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
    index = 109,
    label = "CsJ-3-CsCdH",
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
    index = 110,
    label = "CsJ-3-CsOneDeCs",
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
    index = 111,
    label = "CsJ-3-CsCdCs",
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
    index = 112,
    label = "CsJ-3-CsOneDeSs",
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
    index = 113,
    label = "CsJ-3-CsCdSs",
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
    index = 114,
    label = "CsJ-3-CsTwoDe",
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
    index = 115,
    label = "CsJ-3-Cd",
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
    index = 116,
    label = "CsJ-3-CdHH",
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
    index = 117,
    label = "CsJ-3-CdCsH",
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
    index = 118,
    label = "CsJ-3-CdCsCs",
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
    index = 119,
    label = "CsJ-3-CdSsH",
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
    index = 120,
    label = "CsJ-3-CdSsSs",
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
    index = 121,
    label = "CsJ-3-CdCsSs",
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
    index = 122,
    label = "CsJ-3-CdOneDe",
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
    index = 123,
    label = "CsJ-3-CdOneDeH",
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
    index = 124,
    label = "CsJ-3-CdCdH",
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
    index = 125,
    label = "CsJ-3-CdOneDeCs",
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
    index = 126,
    label = "CsJ-3-CdCdCs",
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
    index = 127,
    label = "CsJ-3-CdOneDeSs",
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
    index = 128,
    label = "CsJ-3-CdCdSs",
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
    index = 129,
    label = "CsJ-3-CdTwoDe",
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
    index = 130,
    label = "CsJ-3-Ss",
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
    index = 131,
    label = "CsJ-3-SsHH",
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
    index = 132,
    label = "CsJ-3-SsCsH",
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
    index = 133,
    label = "CsJ-3-SsCsCs",
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
    index = 134,
    label = "CsJ-3-SsSsH",
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
    index = 135,
    label = "CsJ-3-SsSsSs",
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
    index = 136,
    label = "CsJ-3-SsCsSs",
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
    index = 137,
    label = "CsJ-3-SsOneDe",
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
    index = 138,
    label = "CsJ-3-SsOneDeH",
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
    index = 139,
    label = "CsJ-3-SsCdH",
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
    index = 140,
    label = "CsJ-3-SsOneDeCs",
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
    index = 141,
    label = "CsJ-3-SsCdCs",
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
    index = 142,
    label = "CsJ-3-SsOneDeSs",
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
    index = 143,
    label = "CsJ-3-SsCdSs",
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
    index = 144,
    label = "SJ-3",
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
    index = 145,
    label = "SsJ-3",
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
    index = 146,
    label = "SsJ-3-Cs",
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
    index = 147,
    label = "SsJ-3-Ss",
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
    index = 148,
    label = "SsJ-3-OneDe",
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
    index = 149,
    label = "SsJ-3-Cd",
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
    index = 150,
    label = "S-HC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3 *4 C  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 151,
    label = "S-CC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 C  U0 {1,S}
3 *4 C  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 152,
    label = "S-CsC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Cs U0 {1,S}
3 *4 C  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 153,
    label = "S-Cs(NonDe)C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss     U0 {2,S} {3,S}
2 *2 Cs     U0 {1,S} {4,S} {5,S} {6,S}
3 *4 C      U0 {1,S}
4    {H,Cs} U0 {2,S}
5    {H,Cs} U0 {2,S}
6    {H,Cs} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 154,
    label = "S-Cs(HHH)C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3 *4 C  U0 {1,S}
4    H  U0 {2,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 155,
    label = "S-Cs(CsHH)C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3 *4 C  U0 {1,S}
4    H  U0 {2,S}
5    H  U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 156,
    label = "S-Cs(CsCsH)C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3 *4 C  U0 {1,S}
4    H  U0 {2,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 157,
    label = "S-Cs(CsCsCs)C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3 *4 C  U0 {1,S}
4    Cs U0 {2,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 158,
    label = "S-Cs(De)C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss            U0 {2,S} {3,S}
2 *2 Cs            U0 {1,S} {4,S} {5,S} {6,S}
3 *4 C             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {2,S}
5    R             U0 {2,S}
6    R             U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 159,
    label = "S-Cs(OneDe)C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss            U0 {2,S} {3,S}
2 *2 Cs            U0 {1,S} {4,S} {5,S} {6,S}
3 *4 C             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {2,S}
5    {H,Cs}        U0 {2,S}
6    {H,Cs}        U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 160,
    label = "S-Cs(CdHH)C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3 *4 C  U0 {1,S}
4    Cd U0 {2,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 161,
    label = "S-Cs(CdCsH)C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3 *4 C  U0 {1,S}
4    Cd U0 {2,S}
5    Cs U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 162,
    label = "S-Cs(CdCsCs)C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3 *4 C  U0 {1,S}
4    Cd U0 {2,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 163,
    label = "S-Cs(CtHH)C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3 *4 C  U0 {1,S}
4    Ct U0 {2,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 164,
    label = "S-Cs(CtCsH)C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3 *4 C  U0 {1,S}
4    Ct U0 {2,S}
5    Cs U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 165,
    label = "S-Cs(CtCsCs)C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3 *4 C  U0 {1,S}
4    Ct U0 {2,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 166,
    label = "S-Cs(TwoDe)C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss            U0 {2,S} {3,S}
2 *2 Cs            U0 {1,S} {4,S} {5,S} {6,S}
3 *4 C             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {2,S}
5    {Cd,Ct,Cb,CO} U0 {2,S}
6    {H,Cs}        U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 167,
    label = "S-Cs(ThreeDe)C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss            U0 {2,S} {3,S}
2 *2 Cs            U0 {1,S} {4,S} {5,S} {6,S}
3 *4 C             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {2,S}
5    {Cd,Ct,Cb,CO} U0 {2,S}
6    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 168,
    label = "S-CtC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ct U0 {1,S}
3 *4 C  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 169,
    label = "S-CbC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Cb U0 {1,S}
3 *4 C  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 170,
    label = "S-CdC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {4,D}
3 *4 C  U0 {1,S}
4    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 171,
    label = "S-Cds(H)C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {4,D} {5,S}
3 *4 C  U0 {1,S}
4    C  U0 {2,D}
5    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 172,
    label = "S-Cds(Cs)C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {4,D} {5,S}
3 *4 C  U0 {1,S}
4    C  U0 {2,D}
5    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 173,
    label = "S-CSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *4 S  U0 {1,S}
3 *2 C  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 174,
    label = "S-CsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *4 Ss U0 {1,S}
3 *2 Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 175,
    label = "S-Cs(HHH)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *4 Ss U0 {1,S}
3 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
4    H  U0 {3,S}
5    H  U0 {3,S}
6    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 176,
    label = "S-Cs(CsHH)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *4 Ss U0 {1,S}
3 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
4    Cs U0 {3,S}
5    H  U0 {3,S}
6    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 177,
    label = "S-Cs(CsCsH)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *4 Ss U0 {1,S}
3 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
4    Cs U0 {3,S}
5    Cs U0 {3,S}
6    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 178,
    label = "S-Cs(CsCsCs)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *4 Ss U0 {1,S}
3 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
4    Cs U0 {3,S}
5    Cs U0 {3,S}
6    Cs U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 179,
    label = "S-CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *4 Ss U0 {1,S}
3 *2 Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 180,
    label = "S-CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *4 Ss U0 {1,S}
3 *2 Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 181,
    label = "S-CdSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *4 Ss U0 {1,S}
3 *2 Cd U0 {1,S} {4,D}
4    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 182,
    label = "S-Cds(H)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *4 Ss U0 {1,S}
3 *2 Cd U0 {1,S} {4,D} {5,S}
4    C  U0 {3,D}
5    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 183,
    label = "S-Cds(Cs)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *4 Ss U0 {1,S}
3 *2 Cd U0 {1,S} {4,D} {5,S}
4    C  U0 {3,D}
5    Cs U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 184,
    label = "S-SC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 S  U0 {1,S}
3 *4 C  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 185,
    label = "S-SsC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S}
3 *4 C  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 186,
    label = "S-Ss(H)C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {4,S}
3 *4 C  U0 {1,S}
4    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 187,
    label = "S-Ss(Cs)C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {4,S}
3 *4 C  U0 {1,S}
4    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 188,
    label = "S-Ss(Ss)C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {4,S}
3 *4 C  U0 {1,S}
4    Ss U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 189,
    label = "S-HSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3 *4 Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 190,
    label = "S-SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *4 Ss U0 {1,S}
3 *2 Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 191,
    label = "S-Ss(H)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *4 Ss U0 {1,S}
3 *2 Ss U0 {1,S} {4,S}
4    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 192,
    label = "S-Ss(Cs)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *4 Ss U0 {1,S}
3 *2 Ss U0 {1,S} {4,S}
4    Cs U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 193,
    label = "S-Ss(Ss)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S}
3 *4 Ss U0 {1,S} {4,S}
4    Ss U0 {3,S}
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
        L3: XSR6J_SSSS
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
                L5: CdsJ_C-Cs2
                L5: CdsJ_C-Ss2
                L5: CdsJ_C-Cd2
            L4: CdsJ_S-2
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
            L4: CdsJ-3-H
            L4: CdsJ-3-Cs
            L4: CdsJ-3-Ss
            L4: CdsJ-3-Cd
        L3: CdsJ-3-2
            L4: CdsJ_C-3-2
                L5: CdsJ_C-3-Cs2
                L5: CdsJ_C-3-Ss2
                L5: CdsJ_C-3-Cd2
            L4: CdsJ_S-3-2
        L3: CsJ-3
            L4: CsJ-3-Cs
                L5: CsJ-3-CsHH
                L5: CsJ-3-CsCsH
                L5: CsJ-3-CsCsCs
                L5: CsJ-3-CsSsH
                L5: CsJ-3-CsSsSs
                L5: CsJ-3-CsCsSs
                L5: CsJ-3-CsOneDe
                    L6: CsJ-3-CsOneDeH
                        L7: CsJ-3-CsCdH
                    L6: CsJ-3-CsOneDeCs
                        L7: CsJ-3-CsCdCs
                    L6: CsJ-3-CsOneDeSs
                        L7: CsJ-3-CsCdSs
                L5: CsJ-3-CsTwoDe
            L4: CsJ-3-Cd
                L5: CsJ-3-CdHH
                L5: CsJ-3-CdCsH
                L5: CsJ-3-CdCsCs
                L5: CsJ-3-CdSsH
                L5: CsJ-3-CdSsSs
                L5: CsJ-3-CdCsSs
                L5: CsJ-3-CdOneDe
                    L6: CsJ-3-CdOneDeH
                        L7: CsJ-3-CdCdH
                    L6: CsJ-3-CdOneDeCs
                        L7: CsJ-3-CdCdCs
                    L6: CsJ-3-CdOneDeSs
                        L7: CsJ-3-CdCdSs
                L5: CsJ-3-CdTwoDe
            L4: CsJ-3-Ss
                L5: CsJ-3-SsHH
                L5: CsJ-3-SsCsH
                L5: CsJ-3-SsCsCs
                L5: CsJ-3-SsSsH
                L5: CsJ-3-SsSsSs
                L5: CsJ-3-SsCsSs
                L5: CsJ-3-SsOneDe
                    L6: CsJ-3-SsOneDeH
                        L7: CsJ-3-SsCdH
                    L6: CsJ-3-SsOneDeCs
                        L7: CsJ-3-SsCdCs
                    L6: CsJ-3-SsOneDeSs
                        L7: CsJ-3-SsCdSs
    L2: SJ-3
        L3: SsJ-3
            L4: SsJ-3-Cs
            L4: SsJ-3-Ss
            L4: SsJ-3-OneDe
                L5: SsJ-3-Cd
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

