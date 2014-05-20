#!/usr/bin/env python
# encoding: utf-8

name = "Substitution_O/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["O-RR_or_RRrad", "YJ"], products=["O-RR_or_RRrad", "YJ"], ownReverse=True)

recipe(actions=[
    ['BREAK_BOND', '*1', 'S', '*2'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "O-RR_or_RRrad",
    group = "OR{O-RR, O-RRrad}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "YJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R U{1,2,3,4}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "O-RR",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 R  U0 {1,S}
3    R  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "O-HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "O-CH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    C  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "O-CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "O-Cs(NonDe)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os     U0 {2,S} {3,S}
2 *2 H      U0 {1,S}
3    Cs     U0 {1,S} {4,S} {5,S} {6,S}
4    {H,Cs} U0 {3,S}
5    {H,Cs} U0 {3,S}
6    {H,Cs} U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "O-Cs(HHH)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Cs U0 {1,S} {4,S} {5,S} {6,S}
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
    index = 9,
    label = "O-Cs(CsHH)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Cs U0 {1,S} {4,S} {5,S} {6,S}
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
    index = 10,
    label = "O-Cs(CsCsH)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Cs U0 {1,S} {4,S} {5,S} {6,S}
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
    index = 11,
    label = "O-Cs(CsCsCs)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Cs U0 {1,S} {4,S} {5,S} {6,S}
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
    index = 12,
    label = "O-Cs(OneDe)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os            U0 {2,S} {3,S}
2 *2 H             U0 {1,S}
3    Cs            U0 {1,S} {4,S} {5,S} {6,S}
4    {H,Cs}        U0 {3,S}
5    {H,Cs}        U0 {3,S}
6    {Cd,CO,Ct,Cb} U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "O-Cs(CdHH)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Cs U0 {1,S} {4,S} {5,S} {6,S}
4    Cd U0 {3,S}
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
    index = 14,
    label = "O-Cs(CdCsH)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Cs U0 {1,S} {4,S} {5,S} {6,S}
4    Cd U0 {3,S}
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
    index = 15,
    label = "O-Cs(CdCsCs)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Cs U0 {1,S} {4,S} {5,S} {6,S}
4    Cd U0 {3,S}
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
    index = 16,
    label = "O-Cs(CtHH)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Cs U0 {1,S} {4,S} {5,S} {6,S}
4    Ct U0 {3,S}
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
    index = 17,
    label = "O-Cs(CtCsH)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Cs U0 {1,S} {4,S} {5,S} {6,S}
4    Ct U0 {3,S}
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
    index = 18,
    label = "O-Cs(CtCsCs)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Cs U0 {1,S} {4,S} {5,S} {6,S}
4    Ct U0 {3,S}
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
    index = 19,
    label = "O-Cs(TwoDe)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os            U0 {2,S} {3,S}
2 *2 H             U0 {1,S}
3    Cs            U0 {1,S} {4,S} {5,S} {6,S}
4    {H,Cs}        U0 {3,S}
5    {Cd,CO,Ct,Cb} U0 {3,S}
6    {Cd,CO,Ct,Cb} U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "O-Cs(ThreeDe)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os            U0 {2,S} {3,S}
2 *2 H             U0 {1,S}
3    Cs            U0 {1,S} {4,S} {5,S} {6,S}
4    {Cd,CO,Ct,Cb} U0 {3,S}
5    {Cd,CO,Ct,Cb} U0 {3,S}
6    {Cd,CO,Ct,Cb} U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "O-CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "O-CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "O-COH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "O-CdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
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
    index = 25,
    label = "O-Cds(H)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Cd U0 {1,S} {4,D} {5,S}
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
    index = 26,
    label = "O-Cds(Cs)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Cd U0 {1,S} {4,D} {5,S}
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
    index = 27,
    label = "O-C=OH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Cd U0 {1,S} {4,D}
4    Od U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "O-HC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    H  U0 {1,S}
3 *2 C  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "O-HCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    H  U0 {1,S}
3 *2 Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "O-HCs(NonDe)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os     U0 {2,S} {3,S}
2    H      U0 {1,S}
3 *2 Cs     U0 {1,S} {4,S} {5,S} {6,S}
4    {H,Cs} U0 {3,S}
5    {H,Cs} U0 {3,S}
6    {H,Cs} U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "O-HCs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    H  U0 {1,S}
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
    index = 32,
    label = "O-HCs(CsHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    H  U0 {1,S}
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
    index = 33,
    label = "O-HCs(CsCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    H  U0 {1,S}
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
    index = 34,
    label = "O-HCs(CsCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    H  U0 {1,S}
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
    index = 35,
    label = "O-HCs(OneDe)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os            U0 {2,S} {3,S}
2    H             U0 {1,S}
3 *2 Cs            U0 {1,S} {4,S} {5,S} {6,S}
4    {H,Cs}        U0 {3,S}
5    {H,Cs}        U0 {3,S}
6    {Cd,CO,Ct,Cb} U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "O-HCs(CdHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    H  U0 {1,S}
3 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
4    Cd U0 {3,S}
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
    index = 37,
    label = "O-HCs(CdCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    H  U0 {1,S}
3 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
4    Cd U0 {3,S}
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
    index = 38,
    label = "O-HCs(CdCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    H  U0 {1,S}
3 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
4    Cd U0 {3,S}
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
    index = 39,
    label = "O-HCs(CtHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    H  U0 {1,S}
3 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
4    Ct U0 {3,S}
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
    index = 40,
    label = "O-HCs(CtCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    H  U0 {1,S}
3 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
4    Ct U0 {3,S}
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
    index = 41,
    label = "O-HCs(CtCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    H  U0 {1,S}
3 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
4    Ct U0 {3,S}
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
    index = 42,
    label = "O-HCs(TwoDe)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os            U0 {2,S} {3,S}
2    H             U0 {1,S}
3 *2 Cs            U0 {1,S} {4,S} {5,S} {6,S}
4    {H,Cs}        U0 {3,S}
5    {Cd,CO,Ct,Cb} U0 {3,S}
6    {Cd,CO,Ct,Cb} U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "O-HCs(ThreeDe)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os            U0 {2,S} {3,S}
2    H             U0 {1,S}
3 *2 Cs            U0 {1,S} {4,S} {5,S} {6,S}
4    {Cd,CO,Ct,Cb} U0 {3,S}
5    {Cd,CO,Ct,Cb} U0 {3,S}
6    {Cd,CO,Ct,Cb} U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "O-HCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    H  U0 {1,S}
3 *2 Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "O-HCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    H  U0 {1,S}
3 *2 Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "O-HCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    H  U0 {1,S}
3 *2 CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "O-HCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    H  U0 {1,S}
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
    index = 48,
    label = "O-HCds(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    H  U0 {1,S}
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
    index = 49,
    label = "O-HCds(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    H  U0 {1,S}
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
    index = 50,
    label = "O-HC=O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    H  U0 {1,S}
3 *2 Cd U0 {1,S} {4,D}
4    Od U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "O-CC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 C  U0 {1,S}
3    C  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "O-CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cs U0 {1,S}
3    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "O-Cs(NonDe)Cs(NonDe)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os     U0 {2,S} {3,S}
2 *2 Cs     U0 {1,S} {4,S} {5,S} {6,S}
3    Cs     U0 {1,S} {7,S} {8,S} {9,S}
4    {H,Cs} U0 {2,S}
5    {H,Cs} U0 {2,S}
6    {H,Cs} U0 {2,S}
7    {H,Cs} U0 {3,S}
8    {H,Cs} U0 {3,S}
9    {H,Cs} U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "O-Cs(HHH)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3    Cs U0 {1,S} {7,S} {8,S} {9,S}
4    H  U0 {2,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
7    H  U0 {3,S}
8    H  U0 {3,S}
9    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "O-Cs(HHH)Cs(CsHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3    Cs U0 {1,S} {7,S} {8,S} {9,S}
4    Cs U0 {2,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
7    H  U0 {3,S}
8    H  U0 {3,S}
9    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "O-Cs(CsHH)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cs U0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs U0 {1,S} {7,S} {8,S} {9,S}
4    Cs U0 {2,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
7    H  U0 {3,S}
8    H  U0 {3,S}
9    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "O-Cs(HHH)Cs(CsCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3    Cs U0 {1,S} {7,S} {8,S} {9,S}
4    Cs U0 {2,S}
5    Cs U0 {2,S}
6    H  U0 {2,S}
7    H  U0 {3,S}
8    H  U0 {3,S}
9    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "O-Cs(CsCsH)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cs U0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs U0 {1,S} {7,S} {8,S} {9,S}
4    Cs U0 {2,S}
5    Cs U0 {2,S}
6    H  U0 {2,S}
7    H  U0 {3,S}
8    H  U0 {3,S}
9    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "O-Cs(HHH)Cs(CsCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3    Cs U0 {1,S} {7,S} {8,S} {9,S}
4    Cs U0 {2,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
7    H  U0 {3,S}
8    H  U0 {3,S}
9    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "O-Cs(CsCsCs)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cs U0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs U0 {1,S} {7,S} {8,S} {9,S}
4    Cs U0 {2,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
7    H  U0 {3,S}
8    H  U0 {3,S}
9    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "O-Cs(CsHH)Cs(CsHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3    Cs U0 {1,S} {7,S} {8,S} {9,S}
4    Cs U0 {2,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
7    Cs U0 {3,S}
8    H  U0 {3,S}
9    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "O-Cs(CsHH)Cs(CsCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3    Cs U0 {1,S} {7,S} {8,S} {9,S}
4    Cs U0 {2,S}
5    Cs U0 {2,S}
6    H  U0 {2,S}
7    Cs U0 {3,S}
8    H  U0 {3,S}
9    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "O-Cs(CsCsH)Cs(CsHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cs U0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs U0 {1,S} {7,S} {8,S} {9,S}
4    Cs U0 {2,S}
5    Cs U0 {2,S}
6    H  U0 {2,S}
7    Cs U0 {3,S}
8    H  U0 {3,S}
9    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "O-Cs(CsHH)Cs(CsCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3    Cs U0 {1,S} {7,S} {8,S} {9,S}
4    Cs U0 {2,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
7    Cs U0 {3,S}
8    H  U0 {3,S}
9    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "O-Cs(CsCsCs)Cs(CsHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cs U0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs U0 {1,S} {7,S} {8,S} {9,S}
4    Cs U0 {2,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
7    Cs U0 {3,S}
8    H  U0 {3,S}
9    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "O-Cs(CsCsH)Cs(CsCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3    Cs U0 {1,S} {7,S} {8,S} {9,S}
4    Cs U0 {2,S}
5    Cs U0 {2,S}
6    H  U0 {2,S}
7    Cs U0 {3,S}
8    Cs U0 {3,S}
9    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "O-Cs(CsCsH)Cs(CsCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3    Cs U0 {1,S} {7,S} {8,S} {9,S}
4    Cs U0 {2,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
7    Cs U0 {3,S}
8    Cs U0 {3,S}
9    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "O-Cs(CsCsCs)Cs(CsCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cs U0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs U0 {1,S} {7,S} {8,S} {9,S}
4    Cs U0 {2,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
7    Cs U0 {3,S}
8    Cs U0 {3,S}
9    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "O-Cs(CsCsCs)Cs(CsCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3    Cs U0 {1,S} {7,S} {8,S} {9,S}
4    Cs U0 {2,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
7    Cs U0 {3,S}
8    Cs U0 {3,S}
9    Cs U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "O-Cs(NonDe)Cs(De)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os            U0 {2,S} {3,S}
2    Cs            U0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs            U0 {1,S} {7,S} {8,S} {9,S}
4    {H,Cs}        U0 {2,S}
5    {H,Cs}        U0 {2,S}
6    {H,Cs}        U0 {2,S}
7    {Cd,Ct,Cb,CO} U0 {3,S}
8    R             U0 {3,S}
9    R             U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "O-Cs(NonDe)Cs(OneDe)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os            U0 {2,S} {3,S}
2    Cs            U0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs            U0 {1,S} {7,S} {8,S} {9,S}
4    {H,Cs}        U0 {2,S}
5    {H,Cs}        U0 {2,S}
6    {H,Cs}        U0 {2,S}
7    {Cd,Ct,Cb,CO} U0 {3,S}
8    {H,Cs}        U0 {3,S}
9    {H,Cs}        U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "O-Cs(HHH)Cs(CdHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cs U0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs U0 {1,S} {7,S} {8,S} {9,S}
4    H  U0 {2,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
7    Cd U0 {3,S}
8    H  U0 {3,S}
9    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "O-Cs(HHH)Cs(CdCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cs U0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs U0 {1,S} {7,S} {8,S} {9,S}
4    H  U0 {2,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
7    Cd U0 {3,S}
8    Cs U0 {3,S}
9    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "O-Cs(HHH)Cs(CdCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cs U0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs U0 {1,S} {7,S} {8,S} {9,S}
4    H  U0 {2,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
7    Cd U0 {3,S}
8    Cs U0 {3,S}
9    Cs U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "O-Cs(HHH)Cs(CtHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cs U0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs U0 {1,S} {7,S} {8,S} {9,S}
4    H  U0 {2,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
7    Ct U0 {3,S}
8    H  U0 {3,S}
9    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "O-Cs(HHH)Cs(CtCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cs U0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs U0 {1,S} {7,S} {8,S} {9,S}
4    H  U0 {2,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
7    Ct U0 {3,S}
8    Cs U0 {3,S}
9    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "O-Cs(HHH)Cs(CtCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cs U0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs U0 {1,S} {7,S} {8,S} {9,S}
4    H  U0 {2,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
7    Ct U0 {3,S}
8    Cs U0 {3,S}
9    Cs U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "O-Cs(NonDe)Cs(TwoDe)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os            U0 {2,S} {3,S}
2    Cs            U0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs            U0 {1,S} {7,S} {8,S} {9,S}
4    {H,Cs}        U0 {2,S}
5    {H,Cs}        U0 {2,S}
6    {H,Cs}        U0 {2,S}
7    {Cd,Ct,Cb,CO} U0 {3,S}
8    {Cd,Ct,Cb,CO} U0 {3,S}
9    {H,Cs}        U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "O-Cs(NonDe)Cs(ThreeDe)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os            U0 {2,S} {3,S}
2    Cs            U0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs            U0 {1,S} {7,S} {8,S} {9,S}
4    {H,Cs}        U0 {2,S}
5    {H,Cs}        U0 {2,S}
6    {H,Cs}        U0 {2,S}
7    {Cd,Ct,Cb,CO} U0 {3,S}
8    {Cd,Ct,Cb,CO} U0 {3,S}
9    {Cd,Ct,Cb,CO} U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "O-Cs(De)Cs(NonDe)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os            U0 {2,S} {3,S}
2 *2 Cs            U0 {1,S} {4,S} {5,S} {6,S}
3    Cs            U0 {1,S} {7,S} {8,S} {9,S}
4    {H,Cs}        U0 {2,S}
5    {H,Cs}        U0 {2,S}
6    {H,Cs}        U0 {2,S}
7    {Cd,Ct,Cb,CO} U0 {3,S}
8    R             U0 {3,S}
9    R             U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "O-Cs(OneDe)Cs(NonDe)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os            U0 {2,S} {3,S}
2 *2 Cs            U0 {1,S} {4,S} {5,S} {6,S}
3    Cs            U0 {1,S} {7,S} {8,S} {9,S}
4    {H,Cs}        U0 {2,S}
5    {H,Cs}        U0 {2,S}
6    {H,Cs}        U0 {2,S}
7    {Cd,Ct,Cb,CO} U0 {3,S}
8    {H,Cs}        U0 {3,S}
9    {H,Cs}        U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "O-Cs(CdHH)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3    Cs U0 {1,S} {7,S} {8,S} {9,S}
4    H  U0 {2,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
7    Cd U0 {3,S}
8    H  U0 {3,S}
9    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "O-Cs(CdCsH)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3    Cs U0 {1,S} {7,S} {8,S} {9,S}
4    H  U0 {2,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
7    Cd U0 {3,S}
8    Cs U0 {3,S}
9    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "O-Cs(CdCsCs)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3    Cs U0 {1,S} {7,S} {8,S} {9,S}
4    H  U0 {2,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
7    Cd U0 {3,S}
8    Cs U0 {3,S}
9    Cs U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "O-Cs(CtHH)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3    Cs U0 {1,S} {7,S} {8,S} {9,S}
4    H  U0 {2,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
7    Ct U0 {3,S}
8    H  U0 {3,S}
9    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "O-Cs(CtCsH)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3    Cs U0 {1,S} {7,S} {8,S} {9,S}
4    H  U0 {2,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
7    Ct U0 {3,S}
8    Cs U0 {3,S}
9    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "O-Cs(CtCsCs)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
3    Cs U0 {1,S} {7,S} {8,S} {9,S}
4    H  U0 {2,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
7    Ct U0 {3,S}
8    Cs U0 {3,S}
9    Cs U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "O-Cs(TwoDe)Cs(NonDe)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os            U0 {2,S} {3,S}
2 *2 Cs            U0 {1,S} {4,S} {5,S} {6,S}
3    Cs            U0 {1,S} {7,S} {8,S} {9,S}
4    {H,Cs}        U0 {2,S}
5    {H,Cs}        U0 {2,S}
6    {H,Cs}        U0 {2,S}
7    {Cd,Ct,Cb,CO} U0 {3,S}
8    {Cd,Ct,Cb,CO} U0 {3,S}
9    {H,Cs}        U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "O-Cs(ThreeDe)Cs(NonDe)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os            U0 {2,S} {3,S}
2 *2 Cs            U0 {1,S} {4,S} {5,S} {6,S}
3    Cs            U0 {1,S} {7,S} {8,S} {9,S}
4    {H,Cs}        U0 {2,S}
5    {H,Cs}        U0 {2,S}
6    {H,Cs}        U0 {2,S}
7    {Cd,Ct,Cb,CO} U0 {3,S}
8    {Cd,Ct,Cb,CO} U0 {3,S}
9    {Cd,Ct,Cb,CO} U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "O-CsCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Ct U0 {1,S}
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
    label = "O-Cs(HHH)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Ct U0 {1,S}
3    Cs U0 {1,S} {4,S} {5,S} {6,S}
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
    index = 92,
    label = "O-Cs(CsHH)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Ct U0 {1,S}
3    Cs U0 {1,S} {4,S} {5,S} {6,S}
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
    index = 93,
    label = "O-Cs(CsCsH)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Ct U0 {1,S}
3    Cs U0 {1,S} {4,S} {5,S} {6,S}
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
    index = 94,
    label = "O-Cs(CsCsCs)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Ct U0 {1,S}
3    Cs U0 {1,S} {4,S} {5,S} {6,S}
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
    index = 95,
    label = "O-CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Ct U0 {1,S}
3 *2 Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "O-CtCs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Ct U0 {1,S}
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
    index = 97,
    label = "O-CtCs(CsHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Ct U0 {1,S}
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
    index = 98,
    label = "O-CtCs(CsCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Ct U0 {1,S}
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
    index = 99,
    label = "O-CtCs(CsCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Ct U0 {1,S}
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
    index = 100,
    label = "O-CsCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cb U0 {1,S}
3    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "O-Cs(HHH)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cb U0 {1,S}
3    Cs U0 {1,S} {4,S} {5,S} {6,S}
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
    index = 102,
    label = "O-Cs(CsHH)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cb U0 {1,S}
3    Cs U0 {1,S} {4,S} {5,S} {6,S}
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
    index = 103,
    label = "O-Cs(CsCsH)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cb U0 {1,S}
3    Cs U0 {1,S} {4,S} {5,S} {6,S}
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
    index = 104,
    label = "O-Cs(CsCsCs)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cb U0 {1,S}
3    Cs U0 {1,S} {4,S} {5,S} {6,S}
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
    index = 105,
    label = "O-CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cb U0 {1,S}
3 *2 Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "O-CbCs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cb U0 {1,S}
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
    index = 107,
    label = "O-CbCs(CsHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cb U0 {1,S}
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
    index = 108,
    label = "O-CbCs(CsCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cb U0 {1,S}
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
    index = 109,
    label = "O-CbCs(CsCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cb U0 {1,S}
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
    index = 110,
    label = "O-CsCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 CO U0 {1,S}
3    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "O-COCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    CO U0 {1,S}
3 *2 Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "O-CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Ct U0 {1,S}
3    Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "O-CtCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cb U0 {1,S}
3    Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "O-CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cb U0 {1,S}
3 *2 Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    label = "O-CtCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 CO U0 {1,S}
3    Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "O-COCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    CO U0 {1,S}
3 *2 Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    label = "O-CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cb U0 {1,S}
3    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "O-CbCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 CO U0 {1,S}
3    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "O-COCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    CO U0 {1,S}
3 *2 Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
    label = "O-COCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 CO U0 {1,S}
3    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    label = "O-CsCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {4,D}
3    Cs U0 {1,S}
4    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 122,
    label = "O-Cs(HHH)Cds(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {4,D} {5,S}
3    Cs U0 {1,S} {6,S} {7,S} {8,S}
4    C  U0 {2,D}
5    H  U0 {2,S}
6    H  U0 {3,S}
7    H  U0 {3,S}
8    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "O-Cs(CsHH)Cds(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {4,D} {5,S}
3    Cs U0 {1,S} {6,S} {7,S} {8,S}
4    C  U0 {2,D}
5    H  U0 {2,S}
6    Cs U0 {3,S}
7    H  U0 {3,S}
8    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 124,
    label = "O-Cs(CsCsH)Cds(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {4,D} {5,S}
3    Cs U0 {1,S} {6,S} {7,S} {8,S}
4    C  U0 {2,D}
5    H  U0 {2,S}
6    Cs U0 {3,S}
7    Cs U0 {3,S}
8    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 125,
    label = "O-Cs(CsCsCs)Cds(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {4,D} {5,S}
3    Cs U0 {1,S} {6,S} {7,S} {8,S}
4    C  U0 {2,D}
5    H  U0 {2,S}
6    Cs U0 {3,S}
7    Cs U0 {3,S}
8    Cs U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 126,
    label = "O-Cs(HHH)Cds(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {4,D} {5,S}
3    Cs U0 {1,S} {6,S} {7,S} {8,S}
4    C  U0 {2,D}
5    Cs U0 {2,S}
6    H  U0 {3,S}
7    H  U0 {3,S}
8    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 127,
    label = "O-Cs(CsHH)Cds(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {4,D} {5,S}
3    Cs U0 {1,S} {6,S} {7,S} {8,S}
4    C  U0 {2,D}
5    Cs U0 {2,S}
6    Cs U0 {3,S}
7    H  U0 {3,S}
8    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 128,
    label = "O-Cs(CsCsH)Cds(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {4,D} {5,S}
3    Cs U0 {1,S} {6,S} {7,S} {8,S}
4    C  U0 {2,D}
5    Cs U0 {2,S}
6    Cs U0 {3,S}
7    Cs U0 {3,S}
8    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 129,
    label = "O-Cs(CsCsCs)Cds(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {4,D} {5,S}
3    Cs U0 {1,S} {6,S} {7,S} {8,S}
4    C  U0 {2,D}
5    Cs U0 {2,S}
6    Cs U0 {3,S}
7    Cs U0 {3,S}
8    Cs U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 130,
    label = "O-CdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cd U0 {1,S} {4,D}
3 *2 Cs U0 {1,S}
4    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 131,
    label = "O-Cds(H)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cd U0 {1,S} {4,D} {5,S}
3 *2 Cs U0 {1,S} {6,S} {7,S} {8,S}
4    C  U0 {2,D}
5    H  U0 {2,S}
6    H  U0 {3,S}
7    H  U0 {3,S}
8    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 132,
    label = "O-Cds(H)Cs(CsHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cd U0 {1,S} {4,D} {5,S}
3 *2 Cs U0 {1,S} {6,S} {7,S} {8,S}
4    C  U0 {2,D}
5    H  U0 {2,S}
6    Cs U0 {3,S}
7    H  U0 {3,S}
8    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 133,
    label = "O-Cds(H)Cs(CsCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cd U0 {1,S} {4,D} {5,S}
3 *2 Cs U0 {1,S} {6,S} {7,S} {8,S}
4    C  U0 {2,D}
5    H  U0 {2,S}
6    Cs U0 {3,S}
7    Cs U0 {3,S}
8    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 134,
    label = "O-Cds(H)Cs(CsCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cd U0 {1,S} {4,D} {5,S}
3 *2 Cs U0 {1,S} {6,S} {7,S} {8,S}
4    C  U0 {2,D}
5    H  U0 {2,S}
6    Cs U0 {3,S}
7    Cs U0 {3,S}
8    Cs U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
    label = "O-Cds(Cs)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cd U0 {1,S} {4,D} {5,S}
3 *2 Cs U0 {1,S} {6,S} {7,S} {8,S}
4    C  U0 {2,D}
5    Cs U0 {2,S}
6    H  U0 {3,S}
7    H  U0 {3,S}
8    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
    label = "O-Cds(Cs)Cs(CsHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cd U0 {1,S} {4,D} {5,S}
3 *2 Cs U0 {1,S} {6,S} {7,S} {8,S}
4    C  U0 {2,D}
5    Cs U0 {2,S}
6    Cs U0 {3,S}
7    H  U0 {3,S}
8    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "O-Cds(Cs)Cs(CsCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cd U0 {1,S} {4,D} {5,S}
3 *2 Cs U0 {1,S} {6,S} {7,S} {8,S}
4    C  U0 {2,D}
5    Cs U0 {2,S}
6    Cs U0 {3,S}
7    Cs U0 {3,S}
8    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
    label = "O-Cds(Cs)Cs(CsCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cd U0 {1,S} {4,D} {5,S}
3 *2 Cs U0 {1,S} {6,S} {7,S} {8,S}
4    C  U0 {2,D}
5    Cs U0 {2,S}
6    Cs U0 {3,S}
7    Cs U0 {3,S}
8    Cs U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    label = "O-CsC=O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {4,D}
3    Cs U0 {1,S}
4    Od U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
    label = "O-C=OCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cd U0 {1,S} {4,D}
3 *2 Cs U0 {1,S}
4    Od U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    label = "O-CdCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Ct U0 {1,S}
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
    index = 142,
    label = "O-CtCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Ct U0 {1,S}
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
    index = 143,
    label = "O-CdCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cb U0 {1,S}
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
    index = 144,
    label = "O-CbCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cb U0 {1,S}
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
    index = 145,
    label = "O-CdCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 CO U0 {1,S}
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
    index = 146,
    label = "O-COCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    CO U0 {1,S}
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
    index = 147,
    label = "O-CtC=O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {4,D}
3    Ct U0 {1,S}
4    Od U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    label = "O-C=OCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cd U0 {1,S} {4,D}
3 *2 Ct U0 {1,S}
4    Od U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 149,
    label = "O-CbC=O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {4,D}
3    Cb U0 {1,S}
4    Od U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 150,
    label = "O-C=OCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cd U0 {1,S} {4,D}
3 *2 Cb U0 {1,S}
4    Od U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 151,
    label = "O-COC=O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {4,D}
3    CO U0 {1,S}
4    Od U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 152,
    label = "O-C=OCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cd U0 {1,S} {4,D}
3 *2 CO U0 {1,S}
4    Od U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 153,
    label = "O-CdCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {5,D}
3    Cd U0 {1,S} {4,D}
4    C  U0 {3,D}
5    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 154,
    label = "O-CdC=O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {5,D}
3    Cd U0 {1,S} {4,D}
4    C  U0 {3,D}
5    Od U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 155,
    label = "O-C=OCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Cd U0 {1,S} {5,D}
3 *2 Cd U0 {1,S} {4,D}
4    C  U0 {3,D}
5    Od U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 156,
    label = "O-C=OC=O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {4,D}
3    Cd U0 {1,S} {5,D}
4    Od U0 {2,D}
5    Od U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 157,
    label = "O-CS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 O  U0 {1,S}
3    C  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 158,
    label = "O-COss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S}
3    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 159,
    label = "O-Cs(HHH)Os(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S} {4,S}
3    Cs U0 {1,S} {5,S} {6,S} {7,S}
4    H  U0 {2,S}
5    H  U0 {3,S}
6    H  U0 {3,S}
7    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 160,
    label = "O-Cs(CsHH)Os(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S} {4,S}
3    Cs U0 {1,S} {5,S} {6,S} {7,S}
4    H  U0 {2,S}
5    Cs U0 {3,S}
6    H  U0 {3,S}
7    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 161,
    label = "O-Cs(CsCsH)Os(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S} {4,S}
3    Cs U0 {1,S} {5,S} {6,S} {7,S}
4    H  U0 {2,S}
5    Cs U0 {3,S}
6    Cs U0 {3,S}
7    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 162,
    label = "O-Cs(CsCsCs)Os(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S} {4,S}
3    Cs U0 {1,S} {5,S} {6,S} {7,S}
4    H  U0 {2,S}
5    Cs U0 {3,S}
6    Cs U0 {3,S}
7    Cs U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 163,
    label = "O-Cs(HHH)Os(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S} {4,S}
3    Cs U0 {1,S} {5,S} {6,S} {7,S}
4    Cs U0 {2,S}
5    H  U0 {3,S}
6    H  U0 {3,S}
7    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 164,
    label = "O-Cs(CsHH)Os(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S} {4,S}
3    Cs U0 {1,S} {5,S} {6,S} {7,S}
4    Cs U0 {2,S}
5    Cs U0 {3,S}
6    H  U0 {3,S}
7    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 165,
    label = "O-Cs(CsCsH)Os(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S} {4,S}
3    Cs U0 {1,S} {5,S} {6,S} {7,S}
4    Cs U0 {2,S}
5    Cs U0 {3,S}
6    Cs U0 {3,S}
7    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 166,
    label = "O-Cs(CsCsCs)Os(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S} {4,S}
3    Cs U0 {1,S} {5,S} {6,S} {7,S}
4    Cs U0 {2,S}
5    Cs U0 {3,S}
6    Cs U0 {3,S}
7    Cs U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 167,
    label = "O-Cs(HHH)Os(Os)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S} {4,S}
3    Cs U0 {1,S} {5,S} {6,S} {7,S}
4    Os U0 {2,S}
5    H  U0 {3,S}
6    H  U0 {3,S}
7    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 168,
    label = "O-Cs(CsHH)Os(Os)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S} {4,S}
3    Cs U0 {1,S} {5,S} {6,S} {7,S}
4    Os U0 {2,S}
5    Cs U0 {3,S}
6    H  U0 {3,S}
7    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 169,
    label = "O-Cs(CsCsH)Os(Os)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S} {4,S}
3    Cs U0 {1,S} {5,S} {6,S} {7,S}
4    Os U0 {2,S}
5    Cs U0 {3,S}
6    Cs U0 {3,S}
7    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 170,
    label = "O-Cs(CsCsCs)Os(Os)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S} {4,S}
3    Cs U0 {1,S} {5,S} {6,S} {7,S}
4    Os U0 {2,S}
5    Cs U0 {3,S}
6    Cs U0 {3,S}
7    Cs U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 171,
    label = "O-CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S}
3    Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 172,
    label = "O-CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S}
3    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 173,
    label = "O-COOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S}
3    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 174,
    label = "O-CdOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S}
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
    index = 175,
    label = "O-Cds(H)Os(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S} {6,S}
3    Cd U0 {1,S} {4,D} {5,S}
4    C  U0 {3,D}
5    H  U0 {3,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 176,
    label = "O-Cds(H)Os(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S} {6,S}
3    Cd U0 {1,S} {4,D} {5,S}
4    C  U0 {3,D}
5    H  U0 {3,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 177,
    label = "O-Cds(H)Os(Os)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S} {6,S}
3    Cd U0 {1,S} {4,D} {5,S}
4    C  U0 {3,D}
5    H  U0 {3,S}
6    Os U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 178,
    label = "O-Cds(Cs)Os(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S} {6,S}
3    Cd U0 {1,S} {4,D} {5,S}
4    C  U0 {3,D}
5    Cs U0 {3,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 179,
    label = "O-Cds(Cs)Os(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S} {6,S}
3    Cd U0 {1,S} {4,D} {5,S}
4    C  U0 {3,D}
5    Cs U0 {3,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 180,
    label = "O-Cds(Cs)Os(Os)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S} {6,S}
3    Cd U0 {1,S} {4,D} {5,S}
4    C  U0 {3,D}
5    Cs U0 {3,S}
6    Os U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 181,
    label = "O-C=OOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S}
3    Cd U0 {1,S} {4,D}
4    Od U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 182,
    label = "O-SC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    O  U0 {1,S}
3 *2 C  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 183,
    label = "O-OsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S}
3 *2 Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 184,
    label = "O-Os(H)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S} {4,S}
3 *2 Cs U0 {1,S} {5,S} {6,S} {7,S}
4    H  U0 {2,S}
5    H  U0 {3,S}
6    H  U0 {3,S}
7    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 185,
    label = "O-Os(H)Cs(CsHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S} {4,S}
3 *2 Cs U0 {1,S} {5,S} {6,S} {7,S}
4    H  U0 {2,S}
5    Cs U0 {3,S}
6    H  U0 {3,S}
7    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 186,
    label = "O-Os(H)Cs(CsCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S} {4,S}
3 *2 Cs U0 {1,S} {5,S} {6,S} {7,S}
4    H  U0 {2,S}
5    Cs U0 {3,S}
6    Cs U0 {3,S}
7    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 187,
    label = "O-Os(H)Cs(CsCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S} {4,S}
3 *2 Cs U0 {1,S} {5,S} {6,S} {7,S}
4    H  U0 {2,S}
5    Cs U0 {3,S}
6    Cs U0 {3,S}
7    Cs U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 188,
    label = "O-Os(Cs)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S} {4,S}
3 *2 Cs U0 {1,S} {5,S} {6,S} {7,S}
4    Cs U0 {2,S}
5    H  U0 {3,S}
6    H  U0 {3,S}
7    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 189,
    label = "O-Os(Cs)Cs(CsHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S} {4,S}
3 *2 Cs U0 {1,S} {5,S} {6,S} {7,S}
4    Cs U0 {2,S}
5    Cs U0 {3,S}
6    H  U0 {3,S}
7    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 190,
    label = "O-Os(Cs)Cs(CsCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S} {4,S}
3 *2 Cs U0 {1,S} {5,S} {6,S} {7,S}
4    Cs U0 {2,S}
5    Cs U0 {3,S}
6    Cs U0 {3,S}
7    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 191,
    label = "O-Os(Cs)Cs(CsCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S} {4,S}
3 *2 Cs U0 {1,S} {5,S} {6,S} {7,S}
4    Cs U0 {2,S}
5    Cs U0 {3,S}
6    Cs U0 {3,S}
7    Cs U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 192,
    label = "O-Os(Os)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S} {4,S}
3 *2 Cs U0 {1,S} {5,S} {6,S} {7,S}
4    Os U0 {2,S}
5    H  U0 {3,S}
6    H  U0 {3,S}
7    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 193,
    label = "O-Os(Os)Cs(CsHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S} {4,S}
3 *2 Cs U0 {1,S} {5,S} {6,S} {7,S}
4    Os U0 {2,S}
5    Cs U0 {3,S}
6    H  U0 {3,S}
7    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 194,
    label = "O-Os(Os)Cs(CsCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S} {4,S}
3 *2 Cs U0 {1,S} {5,S} {6,S} {7,S}
4    Os U0 {2,S}
5    Cs U0 {3,S}
6    Cs U0 {3,S}
7    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 195,
    label = "O-Os(Os)Cs(CsCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S} {4,S}
3 *2 Cs U0 {1,S} {5,S} {6,S} {7,S}
4    Os U0 {2,S}
5    Cs U0 {3,S}
6    Cs U0 {3,S}
7    Cs U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 196,
    label = "O-OsCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S}
3 *2 Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 197,
    label = "O-OsCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S}
3 *2 Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 198,
    label = "O-OsCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S}
3 *2 CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 199,
    label = "O-OsCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S}
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
    index = 200,
    label = "O-Os(H)Cds(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S} {6,S}
3 *2 Cd U0 {1,S} {4,D} {5,S}
4    C  U0 {3,D}
5    H  U0 {3,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 201,
    label = "O-Os(Cs)Cds(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S} {6,S}
3 *2 Cd U0 {1,S} {4,D} {5,S}
4    C  U0 {3,D}
5    H  U0 {3,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 202,
    label = "O-Os(Os)Cds(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S} {6,S}
3 *2 Cd U0 {1,S} {4,D} {5,S}
4    C  U0 {3,D}
5    H  U0 {3,S}
6    Os U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 203,
    label = "O-Os(H)Cds(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S} {6,S}
3 *2 Cd U0 {1,S} {4,D} {5,S}
4    C  U0 {3,D}
5    Cs U0 {3,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 204,
    label = "O-Os(Cs)Cds(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S} {6,S}
3 *2 Cd U0 {1,S} {4,D} {5,S}
4    C  U0 {3,D}
5    Cs U0 {3,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 205,
    label = "O-Os(Os)Cds(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S} {6,S}
3 *2 Cd U0 {1,S} {4,D} {5,S}
4    C  U0 {3,D}
5    Cs U0 {3,S}
6    Os U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 206,
    label = "O-OsC=O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S}
3 *2 Cd U0 {1,S} {4,D}
4    Od U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 207,
    label = "O-OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Os U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 208,
    label = "O-Os(H)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Os U0 {1,S} {4,S}
4    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 209,
    label = "O-Os(Cs)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Os U0 {1,S} {4,S}
4    Cs U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 210,
    label = "O-Os(Os)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Os U0 {1,S} {4,S}
4    Os U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 211,
    label = "O-HOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    H  U0 {1,S}
3 *2 Os U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 212,
    label = "O-HOs(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    H  U0 {1,S}
3 *2 Os U0 {1,S} {4,S}
4    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 213,
    label = "O-HOs(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    H  U0 {1,S}
3 *2 Os U0 {1,S} {4,S}
4    Cs U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 214,
    label = "O-HOs(Os)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    H  U0 {1,S}
3 *2 Os U0 {1,S} {4,S}
4    Os U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 215,
    label = "O-OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S}
3    Os U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 216,
    label = "O-Os(H)Os(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S} {5,S}
3    Os U0 {1,S} {4,S}
4    H  U0 {3,S}
5    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 217,
    label = "O-Os(Cs)Os(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S} {5,S}
3    Os U0 {1,S} {4,S}
4    Cs U0 {3,S}
5    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 218,
    label = "O-Os(H)Os(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S} {5,S}
3 *2 Os U0 {1,S} {4,S}
4    Cs U0 {3,S}
5    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 219,
    label = "O-Os(Os)Os(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S} {5,S}
3    Os U0 {1,S} {4,S}
4    Os U0 {3,S}
5    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 220,
    label = "O-Os(H)Os(Os)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S} {5,S}
3 *2 Os U0 {1,S} {4,S}
4    Os U0 {3,S}
5    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 221,
    label = "O-Os(Cs)Os(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S} {5,S}
3    Os U0 {1,S} {4,S}
4    Cs U0 {3,S}
5    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 222,
    label = "O-Os(Cs)Os(Os)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S} {5,S}
3    Os U0 {1,S} {4,S}
4    Cs U0 {3,S}
5    Os U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 223,
    label = "O-Os(Os)Os(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2    Os U0 {1,S} {5,S}
3 *2 Os U0 {1,S} {4,S}
4    Cs U0 {3,S}
5    Os U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 224,
    label = "O-Os(Os)Os(Os)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0 {2,S} {3,S}
2 *2 Os U0 {1,S} {5,S}
3    Os U0 {1,S} {4,S}
4    Os U0 {3,S}
5    Os U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 225,
    label = "O-RRrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Os U0       {2,S} {3,S}
2 *2 R  U{1,2,3} {1,S}
3    R  U0       {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 226,
    label = "Y_1centerbirad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 {Cs,Cd,CO,O,N} U2
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 227,
    label = "HJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 H U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 228,
    label = "CJ",
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
    index = 229,
    label = "CbJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cb U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 230,
    label = "CtJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ct U1 {2,T}
2    C  U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 231,
    label = "CdsJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
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
    index = 232,
    label = "CdsJ-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
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
    index = 233,
    label = "CdsJ-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
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
    index = 234,
    label = "CdsJ-Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
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
    index = 235,
    label = "CdsJ-Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
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
    index = 236,
    label = "CdsJ-CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
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
    index = 238,
    label = "CdsJ-Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
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
    index = 238,
    label = "CdsJ-Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
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
    index = 239,
    label = "CdsJ-Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
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
    index = 240,
    label = "CdsJ-C=O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    C  U0 {1,D}
3    Cd U0 {1,S} {4,D}
4    Od U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 241,
    label = "C=OJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
2    Od U0 {1,D}
3    R  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 242,
    label = "C=OJ-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
2    Od U0 {1,D}
3    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 243,
    label = "C=OJ-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
2    Od U0 {1,D}
3    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 244,
    label = "C=OJ-Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
2    Od U0 {1,D}
3    Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 245,
    label = "C=OJ-Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
2    Od U0 {1,D}
3    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 246,
    label = "C=OJ-CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
2    Od U0 {1,D}
3    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 248,
    label = "C=OJ-Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
2    Od U0 {1,D}
3    Os U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 248,
    label = "C=OJ-Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
2    Od U0 {1,D}
3    Os U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 249,
    label = "C=OJ-Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
2    Od U0 {1,D}
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
    index = 250,
    label = "C=OJ-C=O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
2    Od U0 {1,D}
3    Cd U0 {1,S} {4,D}
4    Od U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 251,
    label = "CsJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
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
    index = 252,
    label = "CsJ-HHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
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
    index = 253,
    label = "CsJ-CsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 254,
    label = "CsJ-CsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 255,
    label = "CsJ-CsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 262,
    label = "CsJ-OsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 263,
    label = "CsJ-OsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 264,
    label = "CsJ-OsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 265,
    label = "CsJ-OsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 266,
    label = "CsJ-OsOsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 267,
    label = "CsJ-OsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 262,
    label = "CsJ-OsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 263,
    label = "CsJ-OsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 264,
    label = "CsJ-OsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 265,
    label = "CsJ-OsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 266,
    label = "CsJ-OsOsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 267,
    label = "CsJ-OsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 268,
    label = "CsJ-OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    {H,Cs,Os,Os}  U0 {1,S}
4    {H,Cs,Os,Os}  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 269,
    label = "CsJ-OneDeHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 270,
    label = "CsJ-CtHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 271,
    label = "CsJ-CbHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 272,
    label = "CsJ-COHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 273,
    label = "CsJ-CdHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 274,
    label = "CsJ-C=OHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Od U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 275,
    label = "CsJ-OneDeCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 276,
    label = "CsJ-CtCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 277,
    label = "CsJ-CbCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 278,
    label = "CsJ-COCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 279,
    label = "CsJ-CdCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 280,
    label = "CsJ-C=OCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Od U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 282,
    label = "CsJ-OneDeOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 282,
    label = "CsJ-OneDeOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 283,
    label = "CsJ-OneDeCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 284,
    label = "CsJ-CtCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 285,
    label = "CsJ-CbCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 286,
    label = "CsJ-COCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 287,
    label = "CsJ-CdCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 288,
    label = "CsJ-C=OCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Od U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 290,
    label = "CsJ-OneDeOsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 290,
    label = "CsJ-OneDeOsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 293,
    label = "CsJ-OneDeOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 292,
    label = "CsJ-OneDeOOss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 293,
    label = "CsJ-OneDeOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 294,
    label = "CsJ-TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {H,Cs,Os,Os}  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 295,
    label = "CsJ-TwoDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 296,
    label = "CsJ-CtCtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 297,
    label = "CsJ-CtCbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 298,
    label = "CsJ-CtCOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 299,
    label = "CsJ-CbCbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 300,
    label = "CsJ-CbCOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 301,
    label = "CsJ-COCOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 302,
    label = "CsJ-CdCtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 303,
    label = "CsJ-CdCbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 304,
    label = "CsJ-CdCOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 305,
    label = "CsJ-CtC=OH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    Cd U0 {1,S} {5,D}
4    H  U0 {1,S}
5    Od U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 306,
    label = "CsJ-CbC=OH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cb U0 {1,S}
3    Cd U0 {1,S} {5,D}
4    H  U0 {1,S}
5    Od U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 307,
    label = "CsJ-COC=OH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    CO U0 {1,S}
3    Cd U0 {1,S} {5,D}
4    H  U0 {1,S}
5    Od U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 308,
    label = "CsJ-CdCdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 309,
    label = "CsJ-CdC=OH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cd U0 {1,S} {6,D}
4    H  U0 {1,S}
5    C  U0 {2,D}
6    Od U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 310,
    label = "CsJ-C=OC=OH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cd U0 {1,S} {6,D}
4    H  U0 {1,S}
5    Od U0 {2,D}
6    Od U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 311,
    label = "CsJ-TwoDeCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 312,
    label = "CsJ-CtCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 313,
    label = "CsJ-CtCbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 314,
    label = "CsJ-CtCOCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 315,
    label = "CsJ-CbCbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 316,
    label = "CsJ-CbCOCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 317,
    label = "CsJ-COCOCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 318,
    label = "CsJ-CdCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 319,
    label = "CsJ-CdCbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 320,
    label = "CsJ-CdCOCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 321,
    label = "CsJ-CtC=OCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    Cd U0 {1,S} {5,D}
4    Cs U0 {1,S}
5    Od U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 322,
    label = "CsJ-CbC=OCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cb U0 {1,S}
3    Cd U0 {1,S} {5,D}
4    Cs U0 {1,S}
5    Od U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 323,
    label = "CsJ-COC=OCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    CO U0 {1,S}
3    Cd U0 {1,S} {5,D}
4    Cs U0 {1,S}
5    Od U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 324,
    label = "CsJ-CdCdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 325,
    label = "CsJ-CdC=OCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cd U0 {1,S} {6,D}
4    Cs U0 {1,S}
5    C  U0 {2,D}
6    Od U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 326,
    label = "CsJ-C=OC=OCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cd U0 {1,S} {6,D}
4    Cs U0 {1,S}
5    Od U0 {2,D}
6    Od U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 328,
    label = "CsJ-TwoDeOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 328,
    label = "CsJ-TwoDeOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 329,
    label = "CsJ-ThreeDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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

entry(
    index = 333,
    label = "OJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Os U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 334,
    label = "OsJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Os U1 {2,S}
2    R  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 335,
    label = "OsJ-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Os U1 {2,S}
2    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 336,
    label = "OsJ-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Os U1 {2,S}
2    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 337,
    label = "OsJ-Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Os U1 {2,S}
2    Os U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 338,
    label = "OsJ-OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Os            U1 {2,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 339,
    label = "OsJ-Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Os U1 {2,S}
2    Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 340,
    label = "OsJ-Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Os U1 {2,S}
2    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 341,
    label = "OsJ-CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Os U1 {2,S}
2    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 342,
    label = "OsJ-Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Os U1 {2,S}
2    Cd U0 {1,S} {3,D}
3    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 343,
    label = "OsJ-C=O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Os U1 {2,S}
2    Cd U0 {1,S} {3,D}
3    Od U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 350,
    label = "NJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 330,
    label = "Y_2centeradjbirad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 {Ct,Os} U1 {2,{S,T}}
2    {Ct,Os} U1 {1,{S,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 331,
    label = "O2b",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O U1 {2,S}
2    O U1 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 332,
    label = "C2b",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,T}
2    C U1 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: O-RR_or_RRrad
    L2: O-RR
        L3: O-HH
        L3: O-CH
            L4: O-CsH
                L5: O-Cs(NonDe)H
                    L6: O-Cs(HHH)H
                    L6: O-Cs(CsHH)H
                    L6: O-Cs(CsCsH)H
                    L6: O-Cs(CsCsCs)H
                L5: O-Cs(OneDe)H
                    L6: O-Cs(CdHH)H
                    L6: O-Cs(CdCsH)H
                    L6: O-Cs(CdCsCs)H
                    L6: O-Cs(CtHH)H
                    L6: O-Cs(CtCsH)H
                    L6: O-Cs(CtCsCs)H
                L5: O-Cs(TwoDe)H
                L5: O-Cs(ThreeDe)H
            L4: O-CtH
            L4: O-CbH
            L4: O-COH
            L4: O-CdH
                L5: O-Cds(H)H
                L5: O-Cds(Cs)H
            L4: O-C=OH
        L3: O-HC
            L4: O-HCs
                L5: O-HCs(NonDe)
                    L6: O-HCs(HHH)
                    L6: O-HCs(CsHH)
                    L6: O-HCs(CsCsH)
                    L6: O-HCs(CsCsCs)
                L5: O-HCs(OneDe)
                    L6: O-HCs(CdHH)
                    L6: O-HCs(CdCsH)
                    L6: O-HCs(CdCsCs)
                    L6: O-HCs(CtHH)
                    L6: O-HCs(CtCsH)
                    L6: O-HCs(CtCsCs)
                L5: O-HCs(TwoDe)
                L5: O-HCs(ThreeDe)
            L4: O-HCt
            L4: O-HCb
            L4: O-HCO
            L4: O-HCd
                L5: O-HCds(H)
                L5: O-HCds(Cs)
            L4: O-HC=O
        L3: O-CC
            L4: O-CsCs
                L5: O-Cs(NonDe)Cs(NonDe)
                    L6: O-Cs(HHH)Cs(HHH)
                    L6: O-Cs(HHH)Cs(CsHH)
                    L6: O-Cs(CsHH)Cs(HHH)
                    L6: O-Cs(HHH)Cs(CsCsH)
                    L6: O-Cs(CsCsH)Cs(HHH)
                    L6: O-Cs(HHH)Cs(CsCsCs)
                    L6: O-Cs(CsCsCs)Cs(HHH)
                    L6: O-Cs(CsHH)Cs(CsHH)
                    L6: O-Cs(CsHH)Cs(CsCsH)
                    L6: O-Cs(CsCsH)Cs(CsHH)
                    L6: O-Cs(CsHH)Cs(CsCsCs)
                    L6: O-Cs(CsCsCs)Cs(CsHH)
                    L6: O-Cs(CsCsH)Cs(CsCsH)
                    L6: O-Cs(CsCsH)Cs(CsCsCs)
                    L6: O-Cs(CsCsCs)Cs(CsCsH)
                    L6: O-Cs(CsCsCs)Cs(CsCsCs)
                L5: O-Cs(NonDe)Cs(De)
                    L6: O-Cs(NonDe)Cs(OneDe)
                        L7: O-Cs(HHH)Cs(CdHH)
                        L7: O-Cs(HHH)Cs(CdCsH)
                        L7: O-Cs(HHH)Cs(CdCsCs)
                        L7: O-Cs(HHH)Cs(CtHH)
                        L7: O-Cs(HHH)Cs(CtCsH)
                        L7: O-Cs(HHH)Cs(CtCsCs)
                    L6: O-Cs(NonDe)Cs(TwoDe)
                    L6: O-Cs(NonDe)Cs(ThreeDe)
                L5: O-Cs(De)Cs(NonDe)
                    L6: O-Cs(OneDe)Cs(NonDe)
                        L7: O-Cs(CdHH)Cs(HHH)
                        L7: O-Cs(CdCsH)Cs(HHH)
                        L7: O-Cs(CdCsCs)Cs(HHH)
                        L7: O-Cs(CtHH)Cs(HHH)
                        L7: O-Cs(CtCsH)Cs(HHH)
                        L7: O-Cs(CtCsCs)Cs(HHH)
                    L6: O-Cs(TwoDe)Cs(NonDe)
                    L6: O-Cs(ThreeDe)Cs(NonDe)
            L4: O-CsCt
                L5: O-Cs(HHH)Ct
                L5: O-Cs(CsHH)Ct
                L5: O-Cs(CsCsH)Ct
                L5: O-Cs(CsCsCs)Ct
            L4: O-CtCs
                L5: O-CtCs(HHH)
                L5: O-CtCs(CsHH)
                L5: O-CtCs(CsCsH)
                L5: O-CtCs(CsCsCs)
            L4: O-CsCb
                L5: O-Cs(HHH)Cb
                L5: O-Cs(CsHH)Cb
                L5: O-Cs(CsCsH)Cb
                L5: O-Cs(CsCsCs)Cb
            L4: O-CbCs
                L5: O-CbCs(HHH)
                L5: O-CbCs(CsHH)
                L5: O-CbCs(CsCsH)
                L5: O-CbCs(CsCsCs)
            L4: O-CsCO
            L4: O-COCs
            L4: O-CtCt
            L4: O-CtCb
            L4: O-CbCt
            L4: O-CtCO
            L4: O-COCt
            L4: O-CbCb
            L4: O-CbCO
            L4: O-COCb
            L4: O-COCO
            L4: O-CsCd
                L5: O-Cs(HHH)Cds(H)
                L5: O-Cs(CsHH)Cds(H)
                L5: O-Cs(CsCsH)Cds(H)
                L5: O-Cs(CsCsCs)Cds(H)
                L5: O-Cs(HHH)Cds(Cs)
                L5: O-Cs(CsHH)Cds(Cs)
                L5: O-Cs(CsCsH)Cds(Cs)
                L5: O-Cs(CsCsCs)Cds(Cs)
            L4: O-CdCs
                L5: O-Cds(H)Cs(HHH)
                L5: O-Cds(H)Cs(CsHH)
                L5: O-Cds(H)Cs(CsCsH)
                L5: O-Cds(H)Cs(CsCsCs)
                L5: O-Cds(Cs)Cs(HHH)
                L5: O-Cds(Cs)Cs(CsHH)
                L5: O-Cds(Cs)Cs(CsCsH)
                L5: O-Cds(Cs)Cs(CsCsCs)
            L4: O-CsC=O
            L4: O-C=OCs
            L4: O-CdCt
            L4: O-CtCd
            L4: O-CdCb
            L4: O-CbCd
            L4: O-CdCO
            L4: O-COCd
            L4: O-CtC=O
            L4: O-C=OCt
            L4: O-CbC=O
            L4: O-C=OCb
            L4: O-COC=O
            L4: O-C=OCO
            L4: O-CdCd
            L4: O-CdC=O
            L4: O-C=OCd
            L4: O-C=OC=O
        L3: O-CS
            L4: O-COss
                L5: O-Cs(HHH)Os(H)
                L5: O-Cs(CsHH)Os(H)
                L5: O-Cs(CsCsH)Os(H)
                L5: O-Cs(CsCsCs)Os(H)
                L5: O-Cs(HHH)Os(Cs)
                L5: O-Cs(CsHH)Os(Cs)
                L5: O-Cs(CsCsH)Os(Cs)
                L5: O-Cs(CsCsCs)Os(Cs)
                L5: O-Cs(HHH)Os(Os)
                L5: O-Cs(CsHH)Os(Os)
                L5: O-Cs(CsCsH)Os(Os)
                L5: O-Cs(CsCsCs)Os(Os)
            L4: O-CtOs
            L4: O-CbOs
            L4: O-COOs
            L4: O-CdOs
                L5: O-Cds(H)Os(H)
                L5: O-Cds(H)Os(Cs)
                L5: O-Cds(H)Os(Os)
                L5: O-Cds(Cs)Os(H)
                L5: O-Cds(Cs)Os(Cs)
                L5: O-Cds(Cs)Os(Os)
            L4: O-C=OOs
        L3: O-SC
            L4: O-OsCs
                L5: O-Os(H)Cs(HHH)
                L5: O-Os(H)Cs(CsHH)
                L5: O-Os(H)Cs(CsCsH)
                L5: O-Os(H)Cs(CsCsCs)
                L5: O-Os(Cs)Cs(HHH)
                L5: O-Os(Cs)Cs(CsHH)
                L5: O-Os(Cs)Cs(CsCsH)
                L5: O-Os(Cs)Cs(CsCsCs)
                L5: O-Os(Os)Cs(HHH)
                L5: O-Os(Os)Cs(CsHH)
                L5: O-Os(Os)Cs(CsCsH)
                L5: O-Os(Os)Cs(CsCsCs)
            L4: O-OsCt
            L4: O-OsCb
            L4: O-OsCO
            L4: O-OsCd
                L5: O-Os(H)Cds(H)
                L5: O-Os(Cs)Cds(H)
                L5: O-Os(Os)Cds(H)
                L5: O-Os(H)Cds(Cs)
                L5: O-Os(Cs)Cds(Cs)
                L5: O-Os(Os)Cds(Cs)
            L4: O-OsC=O
        L3: O-OsH
            L4: O-Os(H)H
            L4: O-Os(Cs)H
            L4: O-Os(Os)H
        L3: O-HOs
            L4: O-HOs(H)
            L4: O-HOs(Cs)
            L4: O-HOs(Os)
        L3: O-OsOs
            L4: O-Os(H)Os(H)
            L4: O-Os(Cs)Os(H)
            L4: O-Os(H)Os(Cs)
            L4: O-Os(Os)Os(H)
            L4: O-Os(H)Os(Os)
            L4: O-Os(Cs)Os(Cs)
            L4: O-Os(Cs)Os(Os)
            L4: O-Os(Os)Os(Cs)
            L4: O-Os(Os)Os(Os)
    L2: O-RRrad
L1: YJ
    L2: Y_1centerbirad
    L2: HJ
    L2: CJ
        L3: CbJ
        L3: CtJ
        L3: CdsJ
            L4: CdsJ-H
            L4: CdsJ-Cs
            L4: CdsJ-Ct
            L4: CdsJ-Cb
            L4: CdsJ-CO
            L4: CdsJ-Os
            L4: CdsJ-Os
            L4: CdsJ-Cd
            L4: CdsJ-C=O
        L3: C=OJ
            L4: C=OJ-H
            L4: C=OJ-Cs
            L4: C=OJ-Ct
            L4: C=OJ-Cb
            L4: C=OJ-CO
            L4: C=OJ-Os
            L4: C=OJ-Os
            L4: C=OJ-Cd
            L4: C=OJ-C=O
        L3: CsJ
            L4: CsJ-HHH
            L4: CsJ-CsHH
            L4: CsJ-CsCsH
            L4: CsJ-CsCsCs
            L4: CsJ-OsHH
            L4: CsJ-OsCsH
            L4: CsJ-OsCsCs
            L4: CsJ-OsOsH
            L4: CsJ-OsOsCs
            L4: CsJ-OsOsOs
            L4: CsJ-OsHH
            L4: CsJ-OsCsH
            L4: CsJ-OsCsCs
            L4: CsJ-OsOsH
            L4: CsJ-OsOsCs
            L4: CsJ-OsOsOs
            L4: CsJ-OneDe
                L5: CsJ-OneDeHH
                    L6: CsJ-CtHH
                    L6: CsJ-CbHH
                    L6: CsJ-COHH
                    L6: CsJ-CdHH
                    L6: CsJ-C=OHH
                L5: CsJ-OneDeCsH
                    L6: CsJ-CtCsH
                    L6: CsJ-CbCsH
                    L6: CsJ-COCsH
                    L6: CsJ-CdCsH
                    L6: CsJ-C=OCsH
                L5: CsJ-OneDeOsH
                L5: CsJ-OneDeOsH
                L5: CsJ-OneDeCsCs
                    L6: CsJ-CtCsCs
                    L6: CsJ-CbCsCs
                    L6: CsJ-COCsCs
                    L6: CsJ-CdCsCs
                    L6: CsJ-C=OCsCs
                L5: CsJ-OneDeOsCs
                L5: CsJ-OneDeOsCs
                L5: CsJ-OneDeOsOs
                L5: CsJ-OneDeOOss
                L5: CsJ-OneDeOsOs
            L4: CsJ-TwoDe
                L5: CsJ-TwoDeH
                    L6: CsJ-CtCtH
                    L6: CsJ-CtCbH
                    L6: CsJ-CtCOH
                    L6: CsJ-CbCbH
                    L6: CsJ-CbCOH
                    L6: CsJ-COCOH
                    L6: CsJ-CdCtH
                    L6: CsJ-CdCbH
                    L6: CsJ-CdCOH
                    L6: CsJ-CtC=OH
                    L6: CsJ-CbC=OH
                    L6: CsJ-COC=OH
                    L6: CsJ-CdCdH
                    L6: CsJ-CdC=OH
                    L6: CsJ-C=OC=OH
                L5: CsJ-TwoDeCs
                    L6: CsJ-CtCtCs
                    L6: CsJ-CtCbCs
                    L6: CsJ-CtCOCs
                    L6: CsJ-CbCbCs
                    L6: CsJ-CbCOCs
                    L6: CsJ-COCOCs
                    L6: CsJ-CdCtCs
                    L6: CsJ-CdCbCs
                    L6: CsJ-CdCOCs
                    L6: CsJ-CtC=OCs
                    L6: CsJ-CbC=OCs
                    L6: CsJ-COC=OCs
                    L6: CsJ-CdCdCs
                    L6: CsJ-CdC=OCs
                    L6: CsJ-C=OC=OCs
                L5: CsJ-TwoDeOs
                L5: CsJ-TwoDeOs
            L4: CsJ-ThreeDe
    L2: OJ
        L3: OsJ
            L4: OsJ-H
            L4: OsJ-Cs
            L4: OsJ-Os
            L4: OsJ-OneDe
                L5: OsJ-Ct
                L5: OsJ-Cb
                L5: OsJ-CO
                L5: OsJ-Cd
                L5: OsJ-C=O
    L2: NJ
    L2: Y_2centeradjbirad
        L3: O2b
        L3: C2b
"""
)

