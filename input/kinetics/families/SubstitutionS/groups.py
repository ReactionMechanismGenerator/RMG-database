#!/usr/bin/env python
# encoding: utf-8

name = "SubstitutionS/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["S-RR", "YJ"], products=["S-RR", "YJ"], ownReverse=True)

recipe(actions=[
    ['BREAK_BOND', '*1', 'S', '*2'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "S-RR",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 2,
    label = "YJ",
    group = "OR{Y_2centeradjbirad, HJ, CJ, O_rad, SJ, Y_1centerbirad}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "S-HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 4,
    label = "S-CH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 5,
    label = "S-CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 6,
    label = "S-Cs(NonDe)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss     U0 {2,S} {3,S}
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
    index = 7,
    label = "S-Cs(HHH)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 8,
    label = "S-Cs(CsHH)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 9,
    label = "S-Cs(CsCsH)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 10,
    label = "S-Cs(CsCsCs)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 11,
    label = "S-Cs(OneDe)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss            U0 {2,S} {3,S}
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
    index = 12,
    label = "S-Cs(CdHH)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 13,
    label = "S-Cs(CdCsH)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 14,
    label = "S-Cs(CdCsCs)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 15,
    label = "S-Cs(CtHH)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 16,
    label = "S-Cs(CtCsH)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 17,
    label = "S-Cs(CtCsCs)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 18,
    label = "S-Cs(TwoDe)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss            U0 {2,S} {3,S}
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
    index = 19,
    label = "S-Cs(ThreeDe)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss            U0 {2,S} {3,S}
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
    index = 20,
    label = "S-CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 21,
    label = "S-CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 22,
    label = "S-COH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 23,
    label = "S-CdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 24,
    label = "S-Cds(H)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 25,
    label = "S-Cds(Cs)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 26,
    label = "S-C=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
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
    index = 27,
    label = "S-HC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 28,
    label = "S-HCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 29,
    label = "S-HCs(NonDe)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss           U0 {2,S} {3,S}
2    H            U0 {1,S}
3 *2 Cs           U0 {1,S} {4,S} {5,S} {6,S}
4    {H,Cs,Os,Ss} U0 {3,S}
5    {H,Cs,Os,Ss} U0 {3,S}
6    {H,Cs,Os,Ss} U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "S-HCs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 31,
    label = "S-HCs(CsHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 32,
    label = "S-HCs(CsCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 33,
    label = "S-HCs(CsCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 34,
    label = "S-HCs(CsOsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    H  U0 {1,S}
3 *2 Cs U0 {1,S} {4,S} {5,S} {6,S}
4    Cs U0 {3,S}
5    Os U0 {3,S}
6    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "S-HCs(OneDe)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss            U0 {2,S} {3,S}
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
    label = "S-HCs(CdHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    label = "S-HCs(CdCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    label = "S-HCs(CdCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    label = "S-HCs(CtHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    label = "S-HCs(CtCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    label = "S-HCs(CtCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    label = "S-HCs(TwoDe)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss            U0 {2,S} {3,S}
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
    label = "S-HCs(ThreeDe)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss            U0 {2,S} {3,S}
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
    label = "S-HCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    label = "S-HCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    label = "S-HCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    label = "S-HCO(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    H  U0 {1,S}
3 *2 CO U0 {1,S} {4,S}
4    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "S-HCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 49,
    label = "S-HCds(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 50,
    label = "S-HCds(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 51,
    label = "S-HC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    H  U0 {1,S}
3 *2 Cd U0 {1,S} {4,D}
4    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "S-CC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 53,
    label = "S-CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 54,
    label = "S-Cs(NonDe)Cs(NonDe)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss     U0 {2,S} {3,S}
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
    index = 55,
    label = "S-Cs(HHH)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 56,
    label = "S-Cs(HHH)Cs(CsHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 57,
    label = "S-Cs(CsHH)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 58,
    label = "S-Cs(HHH)Cs(CsCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 59,
    label = "S-Cs(CsCsH)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 60,
    label = "S-Cs(HHH)Cs(CsCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 61,
    label = "S-Cs(CsCsCs)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 62,
    label = "S-Cs(CsHH)Cs(CsHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 63,
    label = "S-Cs(CsHH)Cs(CsCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 64,
    label = "S-Cs(CsCsH)Cs(CsHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 65,
    label = "S-Cs(CsHH)Cs(CsCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 66,
    label = "S-Cs(CsCsCs)Cs(CsHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 67,
    label = "S-Cs(CsCsH)Cs(CsCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 68,
    label = "S-Cs(CsCsH)Cs(CsCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 69,
    label = "S-Cs(CsCsCs)Cs(CsCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 70,
    label = "S-Cs(CsCsCs)Cs(CsCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 71,
    label = "S-Cs(NonDe)Cs(De)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss            U0 {2,S} {3,S}
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
    index = 72,
    label = "S-Cs(NonDe)Cs(OneDe)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss            U0 {2,S} {3,S}
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
    index = 73,
    label = "S-Cs(HHH)Cs(CdHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 74,
    label = "S-Cs(HHH)Cs(CdCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 75,
    label = "S-Cs(HHH)Cs(CdCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 76,
    label = "S-Cs(HHH)Cs(CtHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 77,
    label = "S-Cs(HHH)Cs(CtCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 78,
    label = "S-Cs(HHH)Cs(CtCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 79,
    label = "S-Cs(NonDe)Cs(TwoDe)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss            U0 {2,S} {3,S}
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
    index = 80,
    label = "S-Cs(NonDe)Cs(ThreeDe)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss            U0 {2,S} {3,S}
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
    index = 81,
    label = "S-Cs(De)Cs(NonDe)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss            U0 {2,S} {3,S}
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
    index = 82,
    label = "S-Cs(OneDe)Cs(NonDe)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss            U0 {2,S} {3,S}
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
    index = 83,
    label = "S-Cs(CdHH)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 84,
    label = "S-Cs(CdCsH)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 85,
    label = "S-Cs(CdCsCs)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 86,
    label = "S-Cs(CtHH)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 87,
    label = "S-Cs(CtCsH)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 88,
    label = "S-Cs(CtCsCs)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 89,
    label = "S-Cs(TwoDe)Cs(NonDe)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss            U0 {2,S} {3,S}
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
    index = 90,
    label = "S-Cs(ThreeDe)Cs(NonDe)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss            U0 {2,S} {3,S}
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
    index = 91,
    label = "S-CsCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 92,
    label = "S-Cs(HHH)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 93,
    label = "S-Cs(CsHH)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 94,
    label = "S-Cs(CsCsH)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 95,
    label = "S-Cs(CsCsCs)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 96,
    label = "S-CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 97,
    label = "S-CtCs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 98,
    label = "S-CtCs(CsHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 99,
    label = "S-CtCs(CsCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 100,
    label = "S-CtCs(CsCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 101,
    label = "S-CsCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 102,
    label = "S-Cs(HHH)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 103,
    label = "S-Cs(CsHH)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 104,
    label = "S-Cs(CsCsH)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 105,
    label = "S-Cs(CsCsCs)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 106,
    label = "S-CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 107,
    label = "S-CbCs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 108,
    label = "S-CbCs(CsHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 109,
    label = "S-CbCs(CsCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 110,
    label = "S-CbCs(CsCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 111,
    label = "S-CsCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 112,
    label = "S-COCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 113,
    label = "S-CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 114,
    label = "S-CtCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 115,
    label = "S-CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 116,
    label = "S-CtCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 117,
    label = "S-COCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 118,
    label = "S-CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 119,
    label = "S-CbCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 120,
    label = "S-COCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 121,
    label = "S-COCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 122,
    label = "S-CsCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 123,
    label = "S-Cs(HHH)Cds(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 124,
    label = "S-Cs(CsHH)Cds(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 125,
    label = "S-Cs(CsCsH)Cds(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 126,
    label = "S-Cs(CsCsCs)Cds(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 127,
    label = "S-Cs(HHH)Cds(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 128,
    label = "S-Cs(CsHH)Cds(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 129,
    label = "S-Cs(CsCsH)Cds(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 130,
    label = "S-Cs(CsCsCs)Cds(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 131,
    label = "S-CdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 132,
    label = "S-Cds(H)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 133,
    label = "S-Cds(H)Cs(CsHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 134,
    label = "S-Cds(H)Cs(CsCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 135,
    label = "S-Cds(H)Cs(CsCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 136,
    label = "S-Cds(Cs)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 137,
    label = "S-Cds(Cs)Cs(CsHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 138,
    label = "S-Cds(Cs)Cs(CsCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 139,
    label = "S-Cds(Cs)Cs(CsCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 140,
    label = "S-CsC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {4,D}
3    Cs U0 {1,S}
4    Sd U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    label = "S-C=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Cd U0 {1,S} {4,D}
3 *2 Cs U0 {1,S}
4    Sd U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 142,
    label = "S-CdCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 143,
    label = "S-CtCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 144,
    label = "S-CdCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 145,
    label = "S-CbCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 146,
    label = "S-CdCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 147,
    label = "S-COCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 148,
    label = "S-CtC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {4,D}
3    Ct U0 {1,S}
4    Sd U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 149,
    label = "S-C=SCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Cd U0 {1,S} {4,D}
3 *2 Ct U0 {1,S}
4    Sd U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 150,
    label = "S-CbC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {4,D}
3    Cb U0 {1,S}
4    Sd U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 151,
    label = "S-C=SCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Cd U0 {1,S} {4,D}
3 *2 Cb U0 {1,S}
4    Sd U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 152,
    label = "S-COC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {4,D}
3    CO U0 {1,S}
4    Sd U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 153,
    label = "S-C=SCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Cd U0 {1,S} {4,D}
3 *2 CO U0 {1,S}
4    Sd U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 154,
    label = "S-CdCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
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
    index = 155,
    label = "S-CdC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {5,D}
3    Cd U0 {1,S} {4,D}
4    C  U0 {3,D}
5    Sd U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 156,
    label = "S-C=SCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Cd U0 {1,S} {5,D}
3 *2 Cd U0 {1,S} {4,D}
4    C  U0 {3,D}
5    Sd U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 157,
    label = "S-C=SC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Cd U0 {1,S} {4,D}
3    Cd U0 {1,S} {5,D}
4    Sd U0 {2,D}
5    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 158,
    label = "S-CS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 S  U0 {1,S}
3    C  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 159,
    label = "S-CsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S}
3    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 160,
    label = "S-Cs(HHH)Ss(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {4,S}
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
    index = 161,
    label = "S-Cs(CsHH)Ss(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {4,S}
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
    index = 162,
    label = "S-Cs(CsCsH)Ss(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {4,S}
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
    index = 163,
    label = "S-Cs(CsCsCs)Ss(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {4,S}
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
    index = 164,
    label = "S-Cs(HHH)Ss(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {4,S}
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
    index = 165,
    label = "S-Cs(CsHH)Ss(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {4,S}
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
    index = 166,
    label = "S-Cs(CsCsH)Ss(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {4,S}
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
    index = 167,
    label = "S-Cs(CsCsCs)Ss(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {4,S}
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
    index = 168,
    label = "S-Cs(HHH)Ss(Ss)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {4,S}
3    Cs U0 {1,S} {5,S} {6,S} {7,S}
4    Ss U0 {2,S}
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
    index = 169,
    label = "S-Cs(CsHH)Ss(Ss)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {4,S}
3    Cs U0 {1,S} {5,S} {6,S} {7,S}
4    Ss U0 {2,S}
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
    index = 170,
    label = "S-Cs(CsCsH)Ss(Ss)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {4,S}
3    Cs U0 {1,S} {5,S} {6,S} {7,S}
4    Ss U0 {2,S}
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
    index = 171,
    label = "S-Cs(CsCsCs)Ss(Ss)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {4,S}
3    Cs U0 {1,S} {5,S} {6,S} {7,S}
4    Ss U0 {2,S}
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
    index = 172,
    label = "S-CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S}
3    Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 173,
    label = "S-CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S}
3    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 174,
    label = "S-COSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S}
3    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 175,
    label = "S-CdSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S}
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
    index = 176,
    label = "S-Cds(H)Ss(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {6,S}
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
    index = 177,
    label = "S-Cds(H)Ss(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {6,S}
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
    index = 178,
    label = "S-Cds(H)Ss(Ss)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {6,S}
3    Cd U0 {1,S} {4,D} {5,S}
4    C  U0 {3,D}
5    H  U0 {3,S}
6    Ss U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 179,
    label = "S-Cds(Cs)Ss(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {6,S}
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
    index = 180,
    label = "S-Cds(Cs)Ss(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {6,S}
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
    index = 181,
    label = "S-Cds(Cs)Ss(Ss)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {6,S}
3    Cd U0 {1,S} {4,D} {5,S}
4    C  U0 {3,D}
5    Cs U0 {3,S}
6    Ss U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 182,
    label = "S-C=SSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S}
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
    index = 183,
    label = "S-SC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    S  U0 {1,S}
3 *2 C  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 184,
    label = "S-SsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S}
3 *2 Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 185,
    label = "S-Ss(H)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S} {4,S}
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
    index = 186,
    label = "S-Ss(H)Cs(CsHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S} {4,S}
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
    index = 187,
    label = "S-Ss(H)Cs(CsCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S} {4,S}
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
    index = 188,
    label = "S-Ss(H)Cs(CsCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S} {4,S}
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
    index = 189,
    label = "S-Ss(Cs)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S} {4,S}
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
    index = 190,
    label = "S-Ss(Cs)Cs(CsHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S} {4,S}
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
    index = 191,
    label = "S-Ss(Cs)Cs(CsCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S} {4,S}
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
    index = 192,
    label = "S-Ss(Cs)Cs(CsCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S} {4,S}
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
    index = 193,
    label = "S-Ss(Ss)Cs(HHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S} {4,S}
3 *2 Cs U0 {1,S} {5,S} {6,S} {7,S}
4    Ss U0 {2,S}
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
    index = 194,
    label = "S-Ss(Ss)Cs(CsHH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S} {4,S}
3 *2 Cs U0 {1,S} {5,S} {6,S} {7,S}
4    Ss U0 {2,S}
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
    index = 195,
    label = "S-Ss(Ss)Cs(CsCsH)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S} {4,S}
3 *2 Cs U0 {1,S} {5,S} {6,S} {7,S}
4    Ss U0 {2,S}
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
    index = 196,
    label = "S-Ss(Ss)Cs(CsCsCs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S} {4,S}
3 *2 Cs U0 {1,S} {5,S} {6,S} {7,S}
4    Ss U0 {2,S}
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
    index = 197,
    label = "S-SsCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S}
3 *2 Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 198,
    label = "S-SsCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S}
3 *2 Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 199,
    label = "S-SsCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S}
3 *2 CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 200,
    label = "S-SsCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S}
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
    index = 201,
    label = "S-Ss(H)Cds(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S} {6,S}
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
    index = 202,
    label = "S-Ss(Cs)Cds(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S} {6,S}
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
    index = 203,
    label = "S-Ss(Ss)Cds(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S} {6,S}
3 *2 Cd U0 {1,S} {4,D} {5,S}
4    C  U0 {3,D}
5    H  U0 {3,S}
6    Ss U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 204,
    label = "S-Ss(H)Cds(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S} {6,S}
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
    index = 205,
    label = "S-Ss(Cs)Cds(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S} {6,S}
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
    index = 206,
    label = "S-Ss(Ss)Cds(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S} {6,S}
3 *2 Cd U0 {1,S} {4,D} {5,S}
4    C  U0 {3,D}
5    Cs U0 {3,S}
6    Ss U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 207,
    label = "S-SsC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S}
3 *2 Cd U0 {1,S} {4,D}
4    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 208,
    label = "S-SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 209,
    label = "S-Ss(H)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Ss U0 {1,S} {4,S}
4    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 210,
    label = "S-Ss(Cs)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Ss U0 {1,S} {4,S}
4    Cs U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 211,
    label = "S-Ss(Ss)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Ss U0 {1,S} {4,S}
4    Ss U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 212,
    label = "S-HSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    H  U0 {1,S}
3 *2 Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 213,
    label = "S-HSs(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    H  U0 {1,S}
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
    index = 214,
    label = "S-HSs(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    H  U0 {1,S}
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
    index = 215,
    label = "S-HSs(Ss)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    H  U0 {1,S}
3 *2 Ss U0 {1,S} {4,S}
4    Ss U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 216,
    label = "S-SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S}
3    Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 217,
    label = "S-Ss(H)Ss(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {5,S}
3    Ss U0 {1,S} {4,S}
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
    index = 218,
    label = "S-Ss(Cs)Ss(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {5,S}
3    Ss U0 {1,S} {4,S}
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
    label = "S-Ss(H)Ss(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S} {5,S}
3 *2 Ss U0 {1,S} {4,S}
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
    index = 220,
    label = "S-Ss(Ss)Ss(H)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {5,S}
3    Ss U0 {1,S} {4,S}
4    Ss U0 {3,S}
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
    label = "S-Ss(H)Ss(Ss)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S} {5,S}
3 *2 Ss U0 {1,S} {4,S}
4    Ss U0 {3,S}
5    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 222,
    label = "S-Ss(Cs)Ss(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {5,S}
3    Ss U0 {1,S} {4,S}
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
    index = 223,
    label = "S-Ss(Cs)Ss(Ss)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {5,S}
3    Ss U0 {1,S} {4,S}
4    Cs U0 {3,S}
5    Ss U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 224,
    label = "S-Ss(Ss)Ss(Cs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    Ss U0 {1,S} {5,S}
3 *2 Ss U0 {1,S} {4,S}
4    Cs U0 {3,S}
5    Ss U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 225,
    label = "S-Ss(Ss)Ss(Ss)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S} {5,S}
3    Ss U0 {1,S} {4,S}
4    Ss U0 {3,S}
5    Ss U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 226,
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
    index = 227,
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
    index = 228,
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
    index = 229,
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
    index = 230,
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
    index = 231,
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
    index = 232,
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
    index = 233,
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
    index = 234,
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
    index = 235,
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
    index = 236,
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
    index = 237,
    label = "CdsJ-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
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
    index = 238,
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
    index = 239,
    label = "CdsJ-C=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
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
    index = 240,
    label = "C=SJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
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
    index = 241,
    label = "C=SJ-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
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
    index = 242,
    label = "C=SJ-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
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
    index = 243,
    label = "C=SJ-Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
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
    index = 244,
    label = "C=SJ-Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
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
    index = 245,
    label = "C=SJ-CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
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
    index = 246,
    label = "C=SJ-Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
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
    index = 247,
    label = "C=SJ-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
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
    index = 248,
    label = "C=SJ-Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
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
    index = 249,
    label = "C=SJ-C=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
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
    index = 250,
    label = "CO_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2    O U0 {1,D}
3    R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 251,
    label = "CO_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2    O U0 {1,D}
3    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 252,
    label = "CO_sec_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C   U1 {2,D} {3,S}
2    O   U0 {1,D}
3    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 253,
    label = "CO_rad/NonDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C      U1 {2,D} {3,S}
2    O      U0 {1,D}
3    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 254,
    label = "CO_rad/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,D} {3,S}
2    O             U0 {1,D}
3    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 255,
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
    index = 256,
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
    index = 257,
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
    index = 258,
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
    index = 259,
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
    index = 260,
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
    index = 261,
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
    index = 262,
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
    index = 263,
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
    index = 264,
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
    index = 265,
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
    index = 266,
    label = "CsJ-SsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 267,
    label = "CsJ-SsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 268,
    label = "CsJ-SsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 269,
    label = "CsJ-SsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 270,
    label = "CsJ-SsSsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 271,
    label = "CsJ-SsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 272,
    label = "CsJ-OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 273,
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
    index = 274,
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
    index = 275,
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
    index = 276,
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
    index = 277,
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
    index = 278,
    label = "CsJ-C=SHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 279,
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
    index = 280,
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
    index = 281,
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
    index = 282,
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
    index = 283,
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
    index = 284,
    label = "CsJ-C=SCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 285,
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
    index = 286,
    label = "CsJ-OneDeSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 287,
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
    index = 288,
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
    index = 289,
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
    index = 290,
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
    index = 291,
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
    index = 292,
    label = "CsJ-C=SCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 293,
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
    index = 294,
    label = "CsJ-OneDeSsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 295,
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
    index = 296,
    label = "CsJ-OneDeOsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 297,
    label = "CsJ-OneDeSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 298,
    label = "CsJ-TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 299,
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
    index = 300,
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
    index = 301,
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
    index = 302,
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
    index = 303,
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
    index = 304,
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
    index = 305,
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
    index = 306,
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
    index = 307,
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
    index = 308,
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
    index = 309,
    label = "CsJ-CtC=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 310,
    label = "CsJ-CbC=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 311,
    label = "CsJ-COC=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 312,
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
    index = 313,
    label = "CsJ-CdC=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 314,
    label = "CsJ-C=SC=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 315,
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
    index = 316,
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
    index = 317,
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
    index = 318,
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
    index = 319,
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
    index = 320,
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
    index = 321,
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
    index = 322,
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
    index = 323,
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
    index = 324,
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
    index = 325,
    label = "CsJ-CtC=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 326,
    label = "CsJ-CbC=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 327,
    label = "CsJ-COC=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 328,
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
    index = 329,
    label = "CsJ-CdC=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 330,
    label = "CsJ-C=SC=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 331,
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
    index = 332,
    label = "CsJ-TwoDeSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 333,
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
    index = 334,
    label = "Y_1centerbirad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 {Cs,Cd,O} U2
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 335,
    label = "O_(T)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O U2
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 336,
    label = "CH2_(T)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U2 {2,S} {3,S}
2    H U0 {1,S}
3    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 337,
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
    index = 338,
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
    index = 339,
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

entry(
    index = 340,
    label = "O_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O U1 {2,S}
2    R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 341,
    label = "O_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O U1 {2,S}
2    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 342,
    label = "O_sec_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O   U1 {2,S}
2    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 343,
    label = "O_rad/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O  U1 {2,S}
2    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 344,
    label = "O_rad/NonDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O U1 {2,S}
2    O U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 345,
    label = "O_rad/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O             U1 {2,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 346,
    label = "SJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2    R  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 347,
    label = "SsJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2    R  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 348,
    label = "SsJ-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 349,
    label = "SsJ-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 350,
    label = "SsJ-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2    Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 351,
    label = "SsJ-OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss            U1 {2,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 352,
    label = "SsJ-Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2    Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 353,
    label = "SsJ-Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 354,
    label = "SsJ-CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 355,
    label = "SsJ-Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
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
    index = 356,
    label = "SsJ-C=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2    Cd U0 {1,S} {3,D}
3    Sd U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: S-RR
    L2: S-HH
    L2: S-CH
        L3: S-CsH
            L4: S-Cs(NonDe)H
                L5: S-Cs(HHH)H
                L5: S-Cs(CsHH)H
                L5: S-Cs(CsCsH)H
                L5: S-Cs(CsCsCs)H
            L4: S-Cs(OneDe)H
                L5: S-Cs(CdHH)H
                L5: S-Cs(CdCsH)H
                L5: S-Cs(CdCsCs)H
                L5: S-Cs(CtHH)H
                L5: S-Cs(CtCsH)H
                L5: S-Cs(CtCsCs)H
            L4: S-Cs(TwoDe)H
            L4: S-Cs(ThreeDe)H
        L3: S-CtH
        L3: S-CbH
        L3: S-COH
        L3: S-CdH
            L4: S-Cds(H)H
            L4: S-Cds(Cs)H
        L3: S-C=SH
    L2: S-HC
        L3: S-HCs
            L4: S-HCs(NonDe)
                L5: S-HCs(HHH)
                L5: S-HCs(CsHH)
                L5: S-HCs(CsCsH)
                L5: S-HCs(CsCsCs)
                L5: S-HCs(CsOsH)
            L4: S-HCs(OneDe)
                L5: S-HCs(CdHH)
                L5: S-HCs(CdCsH)
                L5: S-HCs(CdCsCs)
                L5: S-HCs(CtHH)
                L5: S-HCs(CtCsH)
                L5: S-HCs(CtCsCs)
            L4: S-HCs(TwoDe)
            L4: S-HCs(ThreeDe)
        L3: S-HCt
        L3: S-HCb
        L3: S-HCO
            L4: S-HCO(H)
        L3: S-HCd
            L4: S-HCds(H)
            L4: S-HCds(Cs)
        L3: S-HC=S
    L2: S-CC
        L3: S-CsCs
            L4: S-Cs(NonDe)Cs(NonDe)
                L5: S-Cs(HHH)Cs(HHH)
                L5: S-Cs(HHH)Cs(CsHH)
                L5: S-Cs(CsHH)Cs(HHH)
                L5: S-Cs(HHH)Cs(CsCsH)
                L5: S-Cs(CsCsH)Cs(HHH)
                L5: S-Cs(HHH)Cs(CsCsCs)
                L5: S-Cs(CsCsCs)Cs(HHH)
                L5: S-Cs(CsHH)Cs(CsHH)
                L5: S-Cs(CsHH)Cs(CsCsH)
                L5: S-Cs(CsCsH)Cs(CsHH)
                L5: S-Cs(CsHH)Cs(CsCsCs)
                L5: S-Cs(CsCsCs)Cs(CsHH)
                L5: S-Cs(CsCsH)Cs(CsCsH)
                L5: S-Cs(CsCsH)Cs(CsCsCs)
                L5: S-Cs(CsCsCs)Cs(CsCsH)
                L5: S-Cs(CsCsCs)Cs(CsCsCs)
            L4: S-Cs(NonDe)Cs(De)
                L5: S-Cs(NonDe)Cs(OneDe)
                    L6: S-Cs(HHH)Cs(CdHH)
                    L6: S-Cs(HHH)Cs(CdCsH)
                    L6: S-Cs(HHH)Cs(CdCsCs)
                    L6: S-Cs(HHH)Cs(CtHH)
                    L6: S-Cs(HHH)Cs(CtCsH)
                    L6: S-Cs(HHH)Cs(CtCsCs)
                L5: S-Cs(NonDe)Cs(TwoDe)
                L5: S-Cs(NonDe)Cs(ThreeDe)
            L4: S-Cs(De)Cs(NonDe)
                L5: S-Cs(OneDe)Cs(NonDe)
                    L6: S-Cs(CdHH)Cs(HHH)
                    L6: S-Cs(CdCsH)Cs(HHH)
                    L6: S-Cs(CdCsCs)Cs(HHH)
                    L6: S-Cs(CtHH)Cs(HHH)
                    L6: S-Cs(CtCsH)Cs(HHH)
                    L6: S-Cs(CtCsCs)Cs(HHH)
                L5: S-Cs(TwoDe)Cs(NonDe)
                L5: S-Cs(ThreeDe)Cs(NonDe)
        L3: S-CsCt
            L4: S-Cs(HHH)Ct
            L4: S-Cs(CsHH)Ct
            L4: S-Cs(CsCsH)Ct
            L4: S-Cs(CsCsCs)Ct
        L3: S-CtCs
            L4: S-CtCs(HHH)
            L4: S-CtCs(CsHH)
            L4: S-CtCs(CsCsH)
            L4: S-CtCs(CsCsCs)
        L3: S-CsCb
            L4: S-Cs(HHH)Cb
            L4: S-Cs(CsHH)Cb
            L4: S-Cs(CsCsH)Cb
            L4: S-Cs(CsCsCs)Cb
        L3: S-CbCs
            L4: S-CbCs(HHH)
            L4: S-CbCs(CsHH)
            L4: S-CbCs(CsCsH)
            L4: S-CbCs(CsCsCs)
        L3: S-CsCO
        L3: S-COCs
        L3: S-CtCt
        L3: S-CtCb
        L3: S-CbCt
        L3: S-CtCO
        L3: S-COCt
        L3: S-CbCb
        L3: S-CbCO
        L3: S-COCb
        L3: S-COCO
        L3: S-CsCd
            L4: S-Cs(HHH)Cds(H)
            L4: S-Cs(CsHH)Cds(H)
            L4: S-Cs(CsCsH)Cds(H)
            L4: S-Cs(CsCsCs)Cds(H)
            L4: S-Cs(HHH)Cds(Cs)
            L4: S-Cs(CsHH)Cds(Cs)
            L4: S-Cs(CsCsH)Cds(Cs)
            L4: S-Cs(CsCsCs)Cds(Cs)
        L3: S-CdCs
            L4: S-Cds(H)Cs(HHH)
            L4: S-Cds(H)Cs(CsHH)
            L4: S-Cds(H)Cs(CsCsH)
            L4: S-Cds(H)Cs(CsCsCs)
            L4: S-Cds(Cs)Cs(HHH)
            L4: S-Cds(Cs)Cs(CsHH)
            L4: S-Cds(Cs)Cs(CsCsH)
            L4: S-Cds(Cs)Cs(CsCsCs)
        L3: S-CsC=S
        L3: S-C=SCs
        L3: S-CdCt
        L3: S-CtCd
        L3: S-CdCb
        L3: S-CbCd
        L3: S-CdCO
        L3: S-COCd
        L3: S-CtC=S
        L3: S-C=SCt
        L3: S-CbC=S
        L3: S-C=SCb
        L3: S-COC=S
        L3: S-C=SCO
        L3: S-CdCd
        L3: S-CdC=S
        L3: S-C=SCd
        L3: S-C=SC=S
    L2: S-CS
        L3: S-CsSs
            L4: S-Cs(HHH)Ss(H)
            L4: S-Cs(CsHH)Ss(H)
            L4: S-Cs(CsCsH)Ss(H)
            L4: S-Cs(CsCsCs)Ss(H)
            L4: S-Cs(HHH)Ss(Cs)
            L4: S-Cs(CsHH)Ss(Cs)
            L4: S-Cs(CsCsH)Ss(Cs)
            L4: S-Cs(CsCsCs)Ss(Cs)
            L4: S-Cs(HHH)Ss(Ss)
            L4: S-Cs(CsHH)Ss(Ss)
            L4: S-Cs(CsCsH)Ss(Ss)
            L4: S-Cs(CsCsCs)Ss(Ss)
        L3: S-CtSs
        L3: S-CbSs
        L3: S-COSs
        L3: S-CdSs
            L4: S-Cds(H)Ss(H)
            L4: S-Cds(H)Ss(Cs)
            L4: S-Cds(H)Ss(Ss)
            L4: S-Cds(Cs)Ss(H)
            L4: S-Cds(Cs)Ss(Cs)
            L4: S-Cds(Cs)Ss(Ss)
        L3: S-C=SSs
    L2: S-SC
        L3: S-SsCs
            L4: S-Ss(H)Cs(HHH)
            L4: S-Ss(H)Cs(CsHH)
            L4: S-Ss(H)Cs(CsCsH)
            L4: S-Ss(H)Cs(CsCsCs)
            L4: S-Ss(Cs)Cs(HHH)
            L4: S-Ss(Cs)Cs(CsHH)
            L4: S-Ss(Cs)Cs(CsCsH)
            L4: S-Ss(Cs)Cs(CsCsCs)
            L4: S-Ss(Ss)Cs(HHH)
            L4: S-Ss(Ss)Cs(CsHH)
            L4: S-Ss(Ss)Cs(CsCsH)
            L4: S-Ss(Ss)Cs(CsCsCs)
        L3: S-SsCt
        L3: S-SsCb
        L3: S-SsCO
        L3: S-SsCd
            L4: S-Ss(H)Cds(H)
            L4: S-Ss(Cs)Cds(H)
            L4: S-Ss(Ss)Cds(H)
            L4: S-Ss(H)Cds(Cs)
            L4: S-Ss(Cs)Cds(Cs)
            L4: S-Ss(Ss)Cds(Cs)
        L3: S-SsC=S
    L2: S-SsH
        L3: S-Ss(H)H
        L3: S-Ss(Cs)H
        L3: S-Ss(Ss)H
    L2: S-HSs
        L3: S-HSs(H)
        L3: S-HSs(Cs)
        L3: S-HSs(Ss)
    L2: S-SsSs
        L3: S-Ss(H)Ss(H)
        L3: S-Ss(Cs)Ss(H)
        L3: S-Ss(H)Ss(Cs)
        L3: S-Ss(Ss)Ss(H)
        L3: S-Ss(H)Ss(Ss)
        L3: S-Ss(Cs)Ss(Cs)
        L3: S-Ss(Cs)Ss(Ss)
        L3: S-Ss(Ss)Ss(Cs)
        L3: S-Ss(Ss)Ss(Ss)
L1: YJ
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
            L4: CdsJ-Ss
            L4: CdsJ-Cd
            L4: CdsJ-C=S
        L3: C=SJ
            L4: C=SJ-H
            L4: C=SJ-Cs
            L4: C=SJ-Ct
            L4: C=SJ-Cb
            L4: C=SJ-CO
            L4: C=SJ-Os
            L4: C=SJ-Ss
            L4: C=SJ-Cd
            L4: C=SJ-C=S
        L3: CO_rad
            L4: CO_pri_rad
            L4: CO_sec_rad
                L5: CO_rad/NonDe
                L5: CO_rad/OneDe
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
            L4: CsJ-SsHH
            L4: CsJ-SsCsH
            L4: CsJ-SsCsCs
            L4: CsJ-SsSsH
            L4: CsJ-SsSsCs
            L4: CsJ-SsSsSs
            L4: CsJ-OneDe
                L5: CsJ-OneDeHH
                    L6: CsJ-CtHH
                    L6: CsJ-CbHH
                    L6: CsJ-COHH
                    L6: CsJ-CdHH
                    L6: CsJ-C=SHH
                L5: CsJ-OneDeCsH
                    L6: CsJ-CtCsH
                    L6: CsJ-CbCsH
                    L6: CsJ-COCsH
                    L6: CsJ-CdCsH
                    L6: CsJ-C=SCsH
                L5: CsJ-OneDeOsH
                L5: CsJ-OneDeSsH
                L5: CsJ-OneDeCsCs
                    L6: CsJ-CtCsCs
                    L6: CsJ-CbCsCs
                    L6: CsJ-COCsCs
                    L6: CsJ-CdCsCs
                    L6: CsJ-C=SCsCs
                L5: CsJ-OneDeOsCs
                L5: CsJ-OneDeSsCs
                L5: CsJ-OneDeOsOs
                L5: CsJ-OneDeOsSs
                L5: CsJ-OneDeSsSs
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
                    L6: CsJ-CtC=SH
                    L6: CsJ-CbC=SH
                    L6: CsJ-COC=SH
                    L6: CsJ-CdCdH
                    L6: CsJ-CdC=SH
                    L6: CsJ-C=SC=SH
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
                    L6: CsJ-CtC=SCs
                    L6: CsJ-CbC=SCs
                    L6: CsJ-COC=SCs
                    L6: CsJ-CdCdCs
                    L6: CsJ-CdC=SCs
                    L6: CsJ-C=SC=SCs
                L5: CsJ-TwoDeOs
                L5: CsJ-TwoDeSs
            L4: CsJ-ThreeDe
    L2: Y_1centerbirad
        L3: O_(T)
        L3: CH2_(T)
    L2: Y_2centeradjbirad
        L3: O2b
        L3: C2b
    L2: O_rad
        L3: O_pri_rad
        L3: O_sec_rad
            L4: O_rad/NonDeC
            L4: O_rad/NonDeO
            L4: O_rad/OneDe
    L2: SJ
        L3: SsJ
            L4: SsJ-H
            L4: SsJ-Cs
            L4: SsJ-Ss
            L4: SsJ-OneDe
                L5: SsJ-Ct
                L5: SsJ-Cb
                L5: SsJ-CO
                L5: SsJ-Cd
                L5: SsJ-C=S
"""
)

