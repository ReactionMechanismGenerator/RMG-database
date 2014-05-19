#!/usr/bin/env python
# encoding: utf-8

name = "1,2_shiftS/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["XSYJ"], products=["XSYJ"], ownReverse=False)

reverse = "1,2_S_radical_shift"

recipe(actions=[
    ['BREAK_BOND', '*1', 'S', '*2'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "XSYJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U0 {2,S}
2 *2 S   U0 {1,S} {3,S}
3 *3 R!H U1 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "YJ-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "X-Ss",
    group = "OR{C-Ss}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "CJ-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "CdsJ-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D}
2    C  U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "CsJ-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U1 {2,S} {3,S}
2    R  U0 {1,S}
3    R  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "CsJ-SsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U1 {2,S} {3,S}
2    H  U0 {1,S}
3    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "CsJ-SsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U1 {2,S} {3,S}
2    Cs U0 {1,S}
3    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "CsJ-SsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U1 {2,S} {3,S}
2    Cs U0 {1,S}
3    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "CsJ-SsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U1 {2,S} {3,S}
2    Ss U0 {1,S}
3    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "CsJ-SsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U1 {2,S} {3,S}
2    Ss U0 {1,S}
3    Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "CsJ-SsCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U1 {2,S} {3,S}
2    Cs U0 {1,S}
3    Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "CsJ-SsOneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs            U1 {2,S} {3,S}
2    R             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "CsJ-SsOneDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs            U1 {2,S} {3,S}
2    H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "CsJ-SsCdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U1 {2,S} {3,S}
2    H  U0 {1,S}
3    Cd U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "CsJ-SsOneDeCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs            U1 {2,S} {3,S}
2    Cs            U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "CsJ-SsCdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U1 {2,S} {3,S}
2    Cs U0 {1,S}
3    Cd U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "CsJ-SsOneDeSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs            U1 {2,S} {3,S}
2    Ss            U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "CsJ-SsCdSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U1 {2,S} {3,S}
2    Ss U0 {1,S}
3    Cd U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "SJ-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "C-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "Cb-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb U0
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "Ct-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T}
2    C  U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "Cds-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,D} {3,S}
2    C U0 {1,D}
3    R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "Cds-SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,D} {3,S}
2    C U0 {1,D}
3    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "Cds-SsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,D} {3,S}
2    C  U0 {1,D}
3    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "Cds-SsCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,D} {3,S}
2    C  U0 {1,D}
3    Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "Cds-SsCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,D} {3,S}
2    C  U0 {1,D}
3    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "Cds-SsCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,D} {3,S}
2    C  U0 {1,D}
3    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "Cds-SsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,D} {3,S}
2    C  U0 {1,D}
3    Os U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "Cds-SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,D} {3,S}
2    C  U0 {1,D}
3    Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "Cds-SsCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,D} {3,S}
2    C  U0 {1,D}
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
    index = 33,
    label = "Cds-SsC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,D} {3,S}
2    C  U0 {1,D}
3    Cd U0 {1,S} {4,D}
4    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "C=S-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S}
2    Sd U0 {1,D}
3    R  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "C=S-SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S}
2    Sd U0 {1,D}
3    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "C=S-SsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S}
2    Sd U0 {1,D}
3    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "C=S-SsCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S}
2    Sd U0 {1,D}
3    Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "C=S-SsCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S}
2    Sd U0 {1,D}
3    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "C=S-SsCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S}
2    Sd U0 {1,D}
3    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "C=S-SsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S}
2    Sd U0 {1,D}
3    Os U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "C=S-SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S}
2    Sd U0 {1,D}
3    Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "C=S-SsCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S}
2    Sd U0 {1,D}
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
    index = 43,
    label = "C=S-SsC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S}
2    Sd U0 {1,D}
3    Cd U0 {1,S} {4,D}
4    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "Cs-Ss",
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
    index = 45,
    label = "Cs-SsHHH",
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
    index = 46,
    label = "Cs-SsCsHH",
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
    index = 47,
    label = "Cs-SsCsCsH",
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
    index = 48,
    label = "Cs-SsCsCsCs",
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
    index = 49,
    label = "Cs-SsOsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Os U0 {1,S}
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
    index = 50,
    label = "Cs-SsOsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Os U0 {1,S}
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
    index = 51,
    label = "Cs-SsOsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Os U0 {1,S}
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
    index = 52,
    label = "Cs-SsOsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Os U0 {1,S}
3    Os U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "Cs-SsOsOsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Os U0 {1,S}
3    Os U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "Cs-SsOsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Os U0 {1,S}
3    Os U0 {1,S}
4    Os U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "Cs-SsSsHH",
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
    index = 56,
    label = "Cs-SsSsCsH",
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
    index = 57,
    label = "Cs-SsSsCsCs",
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
    index = 58,
    label = "Cs-SsSsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Ss U0 {1,S}
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
    index = 59,
    label = "Cs-SsSsSsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Ss U0 {1,S}
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
    index = 60,
    label = "Cs-SsSsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Ss U0 {1,S}
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
    index = 61,
    label = "Cs-SsOneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    {H,Cs,Os,Ss}  U0 {1,S}
4    {H,Cs,Os,Ss}  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "Cs-SsOneDeHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    H             U0 {1,S}
4    H             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "Cs-SsCtHH",
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
    index = 64,
    label = "Cs-SsCbHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cb U0 {1,S}
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
    index = 65,
    label = "Cs-SsCOHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    CO U0 {1,S}
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
    index = 66,
    label = "Cs-SsCdHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "Cs-SsC=SHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Sd U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "Cs-SsOneDeCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    Cs            U0 {1,S}
4    H             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "Cs-SsCtCsH",
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
    index = 70,
    label = "Cs-SsCbCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cb U0 {1,S}
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
    index = 71,
    label = "Cs-SsCOCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    CO U0 {1,S}
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
    index = 72,
    label = "Cs-SsCdCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "Cs-SsC=SCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Sd U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "Cs-SsOneDeOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    Os            U0 {1,S}
4    H             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "Cs-SsOneDeSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    Ss            U0 {1,S}
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
    label = "Cs-SsOneDeCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    Cs            U0 {1,S}
4    Cs            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "Cs-SsCtCsCs",
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
    index = 78,
    label = "Cs-SsCbCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cb U0 {1,S}
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
    index = 79,
    label = "Cs-SsCOCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    CO U0 {1,S}
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
    index = 80,
    label = "Cs-SsCdCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "Cs-SsC=SCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Sd U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "Cs-SsOneDeOsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    Os            U0 {1,S}
4    Cs            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "Cs-SsOneDeSsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    Ss            U0 {1,S}
4    Cs            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "Cs-SsOneDeOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    Os            U0 {1,S}
4    Os            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "Cs-SsOneDeOsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    Os            U0 {1,S}
4    Ss            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "Cs-SsOneDeSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    Ss            U0 {1,S}
4    Ss            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "Cs-SsTwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
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
    index = 88,
    label = "Cs-SsTwoDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
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
    index = 89,
    label = "Cs-SsCtCtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "Cs-SsCtCbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    Cb U0 {1,S}
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
    label = "Cs-SsCtCOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    CO U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "Cs-SsCbCbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cb U0 {1,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "Cs-SsCbCOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cb U0 {1,S}
3    CO U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "Cs-SsCOCOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    CO U0 {1,S}
3    CO U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "Cs-SsCdCtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "Cs-SsCdCbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "Cs-SsCdCOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    CO U0 {1,S}
4    H  U0 {1,S}
5    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "Cs-SsCtC=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    Cd U0 {1,S} {5,D}
4    H  U0 {1,S}
5    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "Cs-SsCbC=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cb U0 {1,S}
3    Cd U0 {1,S} {5,D}
4    H  U0 {1,S}
5    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "Cs-SsCOC=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    CO U0 {1,S}
3    Cd U0 {1,S} {5,D}
4    H  U0 {1,S}
5    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "Cs-SsCdCdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cd U0 {1,S} {6,D}
4    H  U0 {1,S}
5    C  U0 {2,D}
6    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "Cs-SsCdC=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cd U0 {1,S} {6,D}
4    H  U0 {1,S}
5    C  U0 {2,D}
6    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "Cs-SsC=SC=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cd U0 {1,S} {6,D}
4    H  U0 {1,S}
5    Sd U0 {2,D}
6    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "Cs-SsTwoDeCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
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
    index = 105,
    label = "Cs-SsCtCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "Cs-SsCtCbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "Cs-SsCtCOCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    CO U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "Cs-SsCbCbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cb U0 {1,S}
3    Cb U0 {1,S}
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
    label = "Cs-SsCbCOCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cb U0 {1,S}
3    CO U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "Cs-SsCOCOCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    CO U0 {1,S}
3    CO U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "Cs-SsCdCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "Cs-SsCdCbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "Cs-SsCdCOCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    CO U0 {1,S}
4    Cs U0 {1,S}
5    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "Cs-SsCtC=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    Cd U0 {1,S} {5,D}
4    Cs U0 {1,S}
5    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    label = "Cs-SsCbC=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cb U0 {1,S}
3    Cd U0 {1,S} {5,D}
4    Cs U0 {1,S}
5    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "Cs-SsCOC=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    CO U0 {1,S}
3    Cd U0 {1,S} {5,D}
4    Cs U0 {1,S}
5    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    label = "Cs-SsCdCdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cd U0 {1,S} {6,D}
4    Cs U0 {1,S}
5    C  U0 {2,D}
6    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "Cs-SsCdC=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cd U0 {1,S} {6,D}
4    Cs U0 {1,S}
5    C  U0 {2,D}
6    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "Cs-SsC=SC=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cd U0 {1,S} {6,D}
4    Cs U0 {1,S}
5    Sd U0 {2,D}
6    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
    label = "Cs-SsTwoDeOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    Os            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    label = "Cs-SsTwoDeSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
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
    index = 122,
    label = "Cs-SsThreeDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
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
L1: YJ-Ss
    L2: CJ-Ss
        L3: CdsJ-Ss
        L3: CsJ-Ss
            L4: CsJ-SsHH
            L4: CsJ-SsCsH
            L4: CsJ-SsCsCs
            L4: CsJ-SsSsH
            L4: CsJ-SsSsSs
            L4: CsJ-SsCsSs
            L4: CsJ-SsOneDe
                L5: CsJ-SsOneDeH
                    L6: CsJ-SsCdH
                L5: CsJ-SsOneDeCs
                    L6: CsJ-SsCdCs
                L5: CsJ-SsOneDeSs
                    L6: CsJ-SsCdSs
    L2: SJ-Ss
L1: X-Ss
    L2: C-Ss
        L3: Cb-Ss
        L3: Ct-Ss
        L3: Cds-Ss
            L4: Cds-SsH
            L4: Cds-SsCs
            L4: Cds-SsCt
            L4: Cds-SsCb
            L4: Cds-SsCO
            L4: Cds-SsOs
            L4: Cds-SsSs
            L4: Cds-SsCd
            L4: Cds-SsC=S
        L3: C=S-Ss
            L4: C=S-SsH
            L4: C=S-SsCs
            L4: C=S-SsCt
            L4: C=S-SsCb
            L4: C=S-SsCO
            L4: C=S-SsOs
            L4: C=S-SsSs
            L4: C=S-SsCd
            L4: C=S-SsC=S
        L3: Cs-Ss
            L4: Cs-SsHHH
            L4: Cs-SsCsHH
            L4: Cs-SsCsCsH
            L4: Cs-SsCsCsCs
            L4: Cs-SsOsHH
            L4: Cs-SsOsCsH
            L4: Cs-SsOsCsCs
            L4: Cs-SsOsOsH
            L4: Cs-SsOsOsCs
            L4: Cs-SsOsOsOs
            L4: Cs-SsSsHH
            L4: Cs-SsSsCsH
            L4: Cs-SsSsCsCs
            L4: Cs-SsSsSsH
            L4: Cs-SsSsSsCs
            L4: Cs-SsSsSsSs
            L4: Cs-SsOneDe
                L5: Cs-SsOneDeHH
                    L6: Cs-SsCtHH
                    L6: Cs-SsCbHH
                    L6: Cs-SsCOHH
                    L6: Cs-SsCdHH
                    L6: Cs-SsC=SHH
                L5: Cs-SsOneDeCsH
                    L6: Cs-SsCtCsH
                    L6: Cs-SsCbCsH
                    L6: Cs-SsCOCsH
                    L6: Cs-SsCdCsH
                    L6: Cs-SsC=SCsH
                L5: Cs-SsOneDeOsH
                L5: Cs-SsOneDeSsH
                L5: Cs-SsOneDeCsCs
                    L6: Cs-SsCtCsCs
                    L6: Cs-SsCbCsCs
                    L6: Cs-SsCOCsCs
                    L6: Cs-SsCdCsCs
                    L6: Cs-SsC=SCsCs
                L5: Cs-SsOneDeOsCs
                L5: Cs-SsOneDeSsCs
                L5: Cs-SsOneDeOsOs
                L5: Cs-SsOneDeOsSs
                L5: Cs-SsOneDeSsSs
            L4: Cs-SsTwoDe
                L5: Cs-SsTwoDeH
                    L6: Cs-SsCtCtH
                    L6: Cs-SsCtCbH
                    L6: Cs-SsCtCOH
                    L6: Cs-SsCbCbH
                    L6: Cs-SsCbCOH
                    L6: Cs-SsCOCOH
                    L6: Cs-SsCdCtH
                    L6: Cs-SsCdCbH
                    L6: Cs-SsCdCOH
                    L6: Cs-SsCtC=SH
                    L6: Cs-SsCbC=SH
                    L6: Cs-SsCOC=SH
                    L6: Cs-SsCdCdH
                    L6: Cs-SsCdC=SH
                    L6: Cs-SsC=SC=SH
                L5: Cs-SsTwoDeCs
                    L6: Cs-SsCtCtCs
                    L6: Cs-SsCtCbCs
                    L6: Cs-SsCtCOCs
                    L6: Cs-SsCbCbCs
                    L6: Cs-SsCbCOCs
                    L6: Cs-SsCOCOCs
                    L6: Cs-SsCdCtCs
                    L6: Cs-SsCdCbCs
                    L6: Cs-SsCdCOCs
                    L6: Cs-SsCtC=SCs
                    L6: Cs-SsCbC=SCs
                    L6: Cs-SsCOC=SCs
                    L6: Cs-SsCdCdCs
                    L6: Cs-SsCdC=SCs
                    L6: Cs-SsC=SC=SCs
                L5: Cs-SsTwoDeOs
                L5: Cs-SsTwoDeSs
            L4: Cs-SsThreeDe
"""
)

