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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 R  0 {1,S}
3    R  0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    C  0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
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
    group = 
"""
1 *1 Ss     0 {2,S} {3,S}
2 *2 H      0 {1,S}
3    Cs     0 {1,S} {4,S} {5,S} {6,S}
4    {H,Cs} 0 {3,S}
5    {H,Cs} 0 {3,S}
6    {H,Cs} 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S} {4,S} {5,S} {6,S}
4    H  0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    Cs 0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss            0 {2,S} {3,S}
2 *2 H             0 {1,S}
3    Cs            0 {1,S} {4,S} {5,S} {6,S}
4    {H,Cs}        0 {3,S}
5    {H,Cs}        0 {3,S}
6    {Cd,CO,Ct,Cb} 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cd 0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cd 0 {3,S}
5    Cs 0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cd 0 {3,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Ct 0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Ct 0 {3,S}
5    Cs 0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Ct 0 {3,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss            0 {2,S} {3,S}
2 *2 H             0 {1,S}
3    Cs            0 {1,S} {4,S} {5,S} {6,S}
4    {H,Cs}        0 {3,S}
5    {Cd,CO,Ct,Cb} 0 {3,S}
6    {Cd,CO,Ct,Cb} 0 {3,S}
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
    group = 
"""
1 *1 Ss            0 {2,S} {3,S}
2 *2 H             0 {1,S}
3    Cs            0 {1,S} {4,S} {5,S} {6,S}
4    {Cd,CO,Ct,Cb} 0 {3,S}
5    {Cd,CO,Ct,Cb} 0 {3,S}
6    {Cd,CO,Ct,Cb} 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    CO 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 H  0 {1,S}
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
    index = 24,
    label = "S-Cds(H)H",
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S} {4,D} {5,S}
4    C  0 {3,D}
5    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S} {4,D} {5,S}
4    C  0 {3,D}
5    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S} {4,D}
4    Sd 0 {3,D}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 C  0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 Cs 0 {1,S}
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
    group = 
"""
1 *1 Ss           0 {2,S} {3,S}
2    H            0 {1,S}
3 *2 Cs           0 {1,S} {4,S} {5,S} {6,S}
4    {H,Cs,Os,Ss} 0 {3,S}
5    {H,Cs,Os,Ss} 0 {3,S}
6    {H,Cs,Os,Ss} 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
4    H  0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    Cs 0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    Os 0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss            0 {2,S} {3,S}
2    H             0 {1,S}
3 *2 Cs            0 {1,S} {4,S} {5,S} {6,S}
4    {H,Cs}        0 {3,S}
5    {H,Cs}        0 {3,S}
6    {Cd,CO,Ct,Cb} 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cd 0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cd 0 {3,S}
5    Cs 0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cd 0 {3,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Ct 0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Ct 0 {3,S}
5    Cs 0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Ct 0 {3,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss            0 {2,S} {3,S}
2    H             0 {1,S}
3 *2 Cs            0 {1,S} {4,S} {5,S} {6,S}
4    {H,Cs}        0 {3,S}
5    {Cd,CO,Ct,Cb} 0 {3,S}
6    {Cd,CO,Ct,Cb} 0 {3,S}
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
    group = 
"""
1 *1 Ss            0 {2,S} {3,S}
2    H             0 {1,S}
3 *2 Cs            0 {1,S} {4,S} {5,S} {6,S}
4    {Cd,CO,Ct,Cb} 0 {3,S}
5    {Cd,CO,Ct,Cb} 0 {3,S}
6    {Cd,CO,Ct,Cb} 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 Ct 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 Cb 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 CO 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 CO 0 {1,S} {4,S}
4    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 Cd 0 {1,S} {4,D}
4    C  0 {3,D}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 Cd 0 {1,S} {4,D} {5,S}
4    C  0 {3,D}
5    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 Cd 0 {1,S} {4,D} {5,S}
4    C  0 {3,D}
5    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 Cd 0 {1,S} {4,D}
4    Sd 0 {3,D}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 C  0 {1,S}
3    C  0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cs 0 {1,S}
3    Cs 0 {1,S}
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
    group = 
"""
1 *1 Ss     0 {2,S} {3,S}
2 *2 Cs     0 {1,S} {4,S} {5,S} {6,S}
3    Cs     0 {1,S} {7,S} {8,S} {9,S}
4    {H,Cs} 0 {2,S}
5    {H,Cs} 0 {2,S}
6    {H,Cs} 0 {2,S}
7    {H,Cs} 0 {3,S}
8    {H,Cs} 0 {3,S}
9    {H,Cs} 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
3    Cs 0 {1,S} {7,S} {8,S} {9,S}
4    H  0 {2,S}
5    H  0 {2,S}
6    H  0 {2,S}
7    H  0 {3,S}
8    H  0 {3,S}
9    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
3    Cs 0 {1,S} {7,S} {8,S} {9,S}
4    Cs 0 {2,S}
5    H  0 {2,S}
6    H  0 {2,S}
7    H  0 {3,S}
8    H  0 {3,S}
9    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cs 0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs 0 {1,S} {7,S} {8,S} {9,S}
4    Cs 0 {2,S}
5    H  0 {2,S}
6    H  0 {2,S}
7    H  0 {3,S}
8    H  0 {3,S}
9    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
3    Cs 0 {1,S} {7,S} {8,S} {9,S}
4    Cs 0 {2,S}
5    Cs 0 {2,S}
6    H  0 {2,S}
7    H  0 {3,S}
8    H  0 {3,S}
9    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cs 0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs 0 {1,S} {7,S} {8,S} {9,S}
4    Cs 0 {2,S}
5    Cs 0 {2,S}
6    H  0 {2,S}
7    H  0 {3,S}
8    H  0 {3,S}
9    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
3    Cs 0 {1,S} {7,S} {8,S} {9,S}
4    Cs 0 {2,S}
5    Cs 0 {2,S}
6    Cs 0 {2,S}
7    H  0 {3,S}
8    H  0 {3,S}
9    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cs 0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs 0 {1,S} {7,S} {8,S} {9,S}
4    Cs 0 {2,S}
5    Cs 0 {2,S}
6    Cs 0 {2,S}
7    H  0 {3,S}
8    H  0 {3,S}
9    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
3    Cs 0 {1,S} {7,S} {8,S} {9,S}
4    Cs 0 {2,S}
5    H  0 {2,S}
6    H  0 {2,S}
7    Cs 0 {3,S}
8    H  0 {3,S}
9    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
3    Cs 0 {1,S} {7,S} {8,S} {9,S}
4    Cs 0 {2,S}
5    Cs 0 {2,S}
6    H  0 {2,S}
7    Cs 0 {3,S}
8    H  0 {3,S}
9    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cs 0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs 0 {1,S} {7,S} {8,S} {9,S}
4    Cs 0 {2,S}
5    Cs 0 {2,S}
6    H  0 {2,S}
7    Cs 0 {3,S}
8    H  0 {3,S}
9    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
3    Cs 0 {1,S} {7,S} {8,S} {9,S}
4    Cs 0 {2,S}
5    Cs 0 {2,S}
6    Cs 0 {2,S}
7    Cs 0 {3,S}
8    H  0 {3,S}
9    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cs 0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs 0 {1,S} {7,S} {8,S} {9,S}
4    Cs 0 {2,S}
5    Cs 0 {2,S}
6    Cs 0 {2,S}
7    Cs 0 {3,S}
8    H  0 {3,S}
9    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
3    Cs 0 {1,S} {7,S} {8,S} {9,S}
4    Cs 0 {2,S}
5    Cs 0 {2,S}
6    H  0 {2,S}
7    Cs 0 {3,S}
8    Cs 0 {3,S}
9    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
3    Cs 0 {1,S} {7,S} {8,S} {9,S}
4    Cs 0 {2,S}
5    Cs 0 {2,S}
6    Cs 0 {2,S}
7    Cs 0 {3,S}
8    Cs 0 {3,S}
9    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cs 0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs 0 {1,S} {7,S} {8,S} {9,S}
4    Cs 0 {2,S}
5    Cs 0 {2,S}
6    Cs 0 {2,S}
7    Cs 0 {3,S}
8    Cs 0 {3,S}
9    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
3    Cs 0 {1,S} {7,S} {8,S} {9,S}
4    Cs 0 {2,S}
5    Cs 0 {2,S}
6    Cs 0 {2,S}
7    Cs 0 {3,S}
8    Cs 0 {3,S}
9    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss            0 {2,S} {3,S}
2    Cs            0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs            0 {1,S} {7,S} {8,S} {9,S}
4    {H,Cs}        0 {2,S}
5    {H,Cs}        0 {2,S}
6    {H,Cs}        0 {2,S}
7    {Cd,Ct,Cb,CO} 0 {3,S}
8    R             0 {3,S}
9    R             0 {3,S}
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
    group = 
"""
1 *1 Ss            0 {2,S} {3,S}
2    Cs            0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs            0 {1,S} {7,S} {8,S} {9,S}
4    {H,Cs}        0 {2,S}
5    {H,Cs}        0 {2,S}
6    {H,Cs}        0 {2,S}
7    {Cd,Ct,Cb,CO} 0 {3,S}
8    {H,Cs}        0 {3,S}
9    {H,Cs}        0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cs 0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs 0 {1,S} {7,S} {8,S} {9,S}
4    H  0 {2,S}
5    H  0 {2,S}
6    H  0 {2,S}
7    Cd 0 {3,S}
8    H  0 {3,S}
9    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cs 0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs 0 {1,S} {7,S} {8,S} {9,S}
4    H  0 {2,S}
5    H  0 {2,S}
6    H  0 {2,S}
7    Cd 0 {3,S}
8    Cs 0 {3,S}
9    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cs 0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs 0 {1,S} {7,S} {8,S} {9,S}
4    H  0 {2,S}
5    H  0 {2,S}
6    H  0 {2,S}
7    Cd 0 {3,S}
8    Cs 0 {3,S}
9    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cs 0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs 0 {1,S} {7,S} {8,S} {9,S}
4    H  0 {2,S}
5    H  0 {2,S}
6    H  0 {2,S}
7    Ct 0 {3,S}
8    H  0 {3,S}
9    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cs 0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs 0 {1,S} {7,S} {8,S} {9,S}
4    H  0 {2,S}
5    H  0 {2,S}
6    H  0 {2,S}
7    Ct 0 {3,S}
8    Cs 0 {3,S}
9    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cs 0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs 0 {1,S} {7,S} {8,S} {9,S}
4    H  0 {2,S}
5    H  0 {2,S}
6    H  0 {2,S}
7    Ct 0 {3,S}
8    Cs 0 {3,S}
9    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss            0 {2,S} {3,S}
2    Cs            0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs            0 {1,S} {7,S} {8,S} {9,S}
4    {H,Cs}        0 {2,S}
5    {H,Cs}        0 {2,S}
6    {H,Cs}        0 {2,S}
7    {Cd,Ct,Cb,CO} 0 {3,S}
8    {Cd,Ct,Cb,CO} 0 {3,S}
9    {H,Cs}        0 {3,S}
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
    group = 
"""
1 *1 Ss            0 {2,S} {3,S}
2    Cs            0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs            0 {1,S} {7,S} {8,S} {9,S}
4    {H,Cs}        0 {2,S}
5    {H,Cs}        0 {2,S}
6    {H,Cs}        0 {2,S}
7    {Cd,Ct,Cb,CO} 0 {3,S}
8    {Cd,Ct,Cb,CO} 0 {3,S}
9    {Cd,Ct,Cb,CO} 0 {3,S}
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
    group = 
"""
1 *1 Ss            0 {2,S} {3,S}
2 *2 Cs            0 {1,S} {4,S} {5,S} {6,S}
3    Cs            0 {1,S} {7,S} {8,S} {9,S}
4    {H,Cs}        0 {2,S}
5    {H,Cs}        0 {2,S}
6    {H,Cs}        0 {2,S}
7    {Cd,Ct,Cb,CO} 0 {3,S}
8    R             0 {3,S}
9    R             0 {3,S}
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
    group = 
"""
1 *1 Ss            0 {2,S} {3,S}
2 *2 Cs            0 {1,S} {4,S} {5,S} {6,S}
3    Cs            0 {1,S} {7,S} {8,S} {9,S}
4    {H,Cs}        0 {2,S}
5    {H,Cs}        0 {2,S}
6    {H,Cs}        0 {2,S}
7    {Cd,Ct,Cb,CO} 0 {3,S}
8    {H,Cs}        0 {3,S}
9    {H,Cs}        0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
3    Cs 0 {1,S} {7,S} {8,S} {9,S}
4    H  0 {2,S}
5    H  0 {2,S}
6    H  0 {2,S}
7    Cd 0 {3,S}
8    H  0 {3,S}
9    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
3    Cs 0 {1,S} {7,S} {8,S} {9,S}
4    H  0 {2,S}
5    H  0 {2,S}
6    H  0 {2,S}
7    Cd 0 {3,S}
8    Cs 0 {3,S}
9    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
3    Cs 0 {1,S} {7,S} {8,S} {9,S}
4    H  0 {2,S}
5    H  0 {2,S}
6    H  0 {2,S}
7    Cd 0 {3,S}
8    Cs 0 {3,S}
9    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
3    Cs 0 {1,S} {7,S} {8,S} {9,S}
4    H  0 {2,S}
5    H  0 {2,S}
6    H  0 {2,S}
7    Ct 0 {3,S}
8    H  0 {3,S}
9    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
3    Cs 0 {1,S} {7,S} {8,S} {9,S}
4    H  0 {2,S}
5    H  0 {2,S}
6    H  0 {2,S}
7    Ct 0 {3,S}
8    Cs 0 {3,S}
9    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
3    Cs 0 {1,S} {7,S} {8,S} {9,S}
4    H  0 {2,S}
5    H  0 {2,S}
6    H  0 {2,S}
7    Ct 0 {3,S}
8    Cs 0 {3,S}
9    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss            0 {2,S} {3,S}
2 *2 Cs            0 {1,S} {4,S} {5,S} {6,S}
3    Cs            0 {1,S} {7,S} {8,S} {9,S}
4    {H,Cs}        0 {2,S}
5    {H,Cs}        0 {2,S}
6    {H,Cs}        0 {2,S}
7    {Cd,Ct,Cb,CO} 0 {3,S}
8    {Cd,Ct,Cb,CO} 0 {3,S}
9    {H,Cs}        0 {3,S}
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
    group = 
"""
1 *1 Ss            0 {2,S} {3,S}
2 *2 Cs            0 {1,S} {4,S} {5,S} {6,S}
3    Cs            0 {1,S} {7,S} {8,S} {9,S}
4    {H,Cs}        0 {2,S}
5    {H,Cs}        0 {2,S}
6    {H,Cs}        0 {2,S}
7    {Cd,Ct,Cb,CO} 0 {3,S}
8    {Cd,Ct,Cb,CO} 0 {3,S}
9    {Cd,Ct,Cb,CO} 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ct 0 {1,S}
3    Cs 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ct 0 {1,S}
3    Cs 0 {1,S} {4,S} {5,S} {6,S}
4    H  0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ct 0 {1,S}
3    Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ct 0 {1,S}
3    Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    Cs 0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ct 0 {1,S}
3    Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ct 0 {1,S}
3 *2 Cs 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ct 0 {1,S}
3 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
4    H  0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ct 0 {1,S}
3 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ct 0 {1,S}
3 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    Cs 0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ct 0 {1,S}
3 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cb 0 {1,S}
3    Cs 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cb 0 {1,S}
3    Cs 0 {1,S} {4,S} {5,S} {6,S}
4    H  0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cb 0 {1,S}
3    Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cb 0 {1,S}
3    Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    Cs 0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cb 0 {1,S}
3    Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cb 0 {1,S}
3 *2 Cs 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cb 0 {1,S}
3 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
4    H  0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cb 0 {1,S}
3 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cb 0 {1,S}
3 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    Cs 0 {3,S}
6    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cb 0 {1,S}
3 *2 Cs 0 {1,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 CO 0 {1,S}
3    Cs 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    CO 0 {1,S}
3 *2 Cs 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ct 0 {1,S}
3    Ct 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cb 0 {1,S}
3    Ct 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cb 0 {1,S}
3 *2 Ct 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 CO 0 {1,S}
3    Ct 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    CO 0 {1,S}
3 *2 Ct 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cb 0 {1,S}
3    Cb 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 CO 0 {1,S}
3    Cb 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    CO 0 {1,S}
3 *2 Cb 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 CO 0 {1,S}
3    CO 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cd 0 {1,S} {4,D}
3    Cs 0 {1,S}
4    C  0 {2,D}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cd 0 {1,S} {4,D} {5,S}
3    Cs 0 {1,S} {6,S} {7,S} {8,S}
4    C  0 {2,D}
5    H  0 {2,S}
6    H  0 {3,S}
7    H  0 {3,S}
8    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cd 0 {1,S} {4,D} {5,S}
3    Cs 0 {1,S} {6,S} {7,S} {8,S}
4    C  0 {2,D}
5    H  0 {2,S}
6    Cs 0 {3,S}
7    H  0 {3,S}
8    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cd 0 {1,S} {4,D} {5,S}
3    Cs 0 {1,S} {6,S} {7,S} {8,S}
4    C  0 {2,D}
5    H  0 {2,S}
6    Cs 0 {3,S}
7    Cs 0 {3,S}
8    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cd 0 {1,S} {4,D} {5,S}
3    Cs 0 {1,S} {6,S} {7,S} {8,S}
4    C  0 {2,D}
5    H  0 {2,S}
6    Cs 0 {3,S}
7    Cs 0 {3,S}
8    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cd 0 {1,S} {4,D} {5,S}
3    Cs 0 {1,S} {6,S} {7,S} {8,S}
4    C  0 {2,D}
5    Cs 0 {2,S}
6    H  0 {3,S}
7    H  0 {3,S}
8    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cd 0 {1,S} {4,D} {5,S}
3    Cs 0 {1,S} {6,S} {7,S} {8,S}
4    C  0 {2,D}
5    Cs 0 {2,S}
6    Cs 0 {3,S}
7    H  0 {3,S}
8    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cd 0 {1,S} {4,D} {5,S}
3    Cs 0 {1,S} {6,S} {7,S} {8,S}
4    C  0 {2,D}
5    Cs 0 {2,S}
6    Cs 0 {3,S}
7    Cs 0 {3,S}
8    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cd 0 {1,S} {4,D} {5,S}
3    Cs 0 {1,S} {6,S} {7,S} {8,S}
4    C  0 {2,D}
5    Cs 0 {2,S}
6    Cs 0 {3,S}
7    Cs 0 {3,S}
8    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cd 0 {1,S} {4,D}
3 *2 Cs 0 {1,S}
4    C  0 {2,D}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cd 0 {1,S} {4,D} {5,S}
3 *2 Cs 0 {1,S} {6,S} {7,S} {8,S}
4    C  0 {2,D}
5    H  0 {2,S}
6    H  0 {3,S}
7    H  0 {3,S}
8    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cd 0 {1,S} {4,D} {5,S}
3 *2 Cs 0 {1,S} {6,S} {7,S} {8,S}
4    C  0 {2,D}
5    H  0 {2,S}
6    Cs 0 {3,S}
7    H  0 {3,S}
8    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cd 0 {1,S} {4,D} {5,S}
3 *2 Cs 0 {1,S} {6,S} {7,S} {8,S}
4    C  0 {2,D}
5    H  0 {2,S}
6    Cs 0 {3,S}
7    Cs 0 {3,S}
8    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cd 0 {1,S} {4,D} {5,S}
3 *2 Cs 0 {1,S} {6,S} {7,S} {8,S}
4    C  0 {2,D}
5    H  0 {2,S}
6    Cs 0 {3,S}
7    Cs 0 {3,S}
8    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cd 0 {1,S} {4,D} {5,S}
3 *2 Cs 0 {1,S} {6,S} {7,S} {8,S}
4    C  0 {2,D}
5    Cs 0 {2,S}
6    H  0 {3,S}
7    H  0 {3,S}
8    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cd 0 {1,S} {4,D} {5,S}
3 *2 Cs 0 {1,S} {6,S} {7,S} {8,S}
4    C  0 {2,D}
5    Cs 0 {2,S}
6    Cs 0 {3,S}
7    H  0 {3,S}
8    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cd 0 {1,S} {4,D} {5,S}
3 *2 Cs 0 {1,S} {6,S} {7,S} {8,S}
4    C  0 {2,D}
5    Cs 0 {2,S}
6    Cs 0 {3,S}
7    Cs 0 {3,S}
8    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cd 0 {1,S} {4,D} {5,S}
3 *2 Cs 0 {1,S} {6,S} {7,S} {8,S}
4    C  0 {2,D}
5    Cs 0 {2,S}
6    Cs 0 {3,S}
7    Cs 0 {3,S}
8    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cd 0 {1,S} {4,D}
3    Cs 0 {1,S}
4    Sd 0 {2,D}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cd 0 {1,S} {4,D}
3 *2 Cs 0 {1,S}
4    Sd 0 {2,D}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ct 0 {1,S}
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
    index = 143,
    label = "S-CtCd",
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ct 0 {1,S}
3 *2 Cd 0 {1,S} {4,D}
4    C  0 {3,D}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cb 0 {1,S}
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
    index = 145,
    label = "S-CbCd",
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cb 0 {1,S}
3 *2 Cd 0 {1,S} {4,D}
4    C  0 {3,D}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 CO 0 {1,S}
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
    index = 147,
    label = "S-COCd",
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    CO 0 {1,S}
3 *2 Cd 0 {1,S} {4,D}
4    C  0 {3,D}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cd 0 {1,S} {4,D}
3    Ct 0 {1,S}
4    Sd 0 {2,D}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cd 0 {1,S} {4,D}
3 *2 Ct 0 {1,S}
4    Sd 0 {2,D}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cd 0 {1,S} {4,D}
3    Cb 0 {1,S}
4    Sd 0 {2,D}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cd 0 {1,S} {4,D}
3 *2 Cb 0 {1,S}
4    Sd 0 {2,D}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cd 0 {1,S} {4,D}
3    CO 0 {1,S}
4    Sd 0 {2,D}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cd 0 {1,S} {4,D}
3 *2 CO 0 {1,S}
4    Sd 0 {2,D}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cd 0 {1,S} {5,D}
3    Cd 0 {1,S} {4,D}
4    C  0 {3,D}
5    C  0 {2,D}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cd 0 {1,S} {5,D}
3    Cd 0 {1,S} {4,D}
4    C  0 {3,D}
5    Sd 0 {2,D}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Cd 0 {1,S} {5,D}
3 *2 Cd 0 {1,S} {4,D}
4    C  0 {3,D}
5    Sd 0 {2,D}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Cd 0 {1,S} {4,D}
3    Cd 0 {1,S} {5,D}
4    Sd 0 {2,D}
5    Sd 0 {3,D}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 S  0 {1,S}
3    C  0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S}
3    Cs 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S} {4,S}
3    Cs 0 {1,S} {5,S} {6,S} {7,S}
4    H  0 {2,S}
5    H  0 {3,S}
6    H  0 {3,S}
7    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S} {4,S}
3    Cs 0 {1,S} {5,S} {6,S} {7,S}
4    H  0 {2,S}
5    Cs 0 {3,S}
6    H  0 {3,S}
7    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S} {4,S}
3    Cs 0 {1,S} {5,S} {6,S} {7,S}
4    H  0 {2,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
7    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S} {4,S}
3    Cs 0 {1,S} {5,S} {6,S} {7,S}
4    H  0 {2,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
7    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S} {4,S}
3    Cs 0 {1,S} {5,S} {6,S} {7,S}
4    Cs 0 {2,S}
5    H  0 {3,S}
6    H  0 {3,S}
7    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S} {4,S}
3    Cs 0 {1,S} {5,S} {6,S} {7,S}
4    Cs 0 {2,S}
5    Cs 0 {3,S}
6    H  0 {3,S}
7    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S} {4,S}
3    Cs 0 {1,S} {5,S} {6,S} {7,S}
4    Cs 0 {2,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
7    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S} {4,S}
3    Cs 0 {1,S} {5,S} {6,S} {7,S}
4    Cs 0 {2,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
7    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S} {4,S}
3    Cs 0 {1,S} {5,S} {6,S} {7,S}
4    Ss 0 {2,S}
5    H  0 {3,S}
6    H  0 {3,S}
7    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S} {4,S}
3    Cs 0 {1,S} {5,S} {6,S} {7,S}
4    Ss 0 {2,S}
5    Cs 0 {3,S}
6    H  0 {3,S}
7    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S} {4,S}
3    Cs 0 {1,S} {5,S} {6,S} {7,S}
4    Ss 0 {2,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
7    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S} {4,S}
3    Cs 0 {1,S} {5,S} {6,S} {7,S}
4    Ss 0 {2,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
7    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S}
3    Ct 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S}
3    Cb 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S}
3    CO 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S}
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
    index = 176,
    label = "S-Cds(H)Ss(H)",
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S} {6,S}
3    Cd 0 {1,S} {4,D} {5,S}
4    C  0 {3,D}
5    H  0 {3,S}
6    H  0 {2,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S} {6,S}
3    Cd 0 {1,S} {4,D} {5,S}
4    C  0 {3,D}
5    H  0 {3,S}
6    Cs 0 {2,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S} {6,S}
3    Cd 0 {1,S} {4,D} {5,S}
4    C  0 {3,D}
5    H  0 {3,S}
6    Ss 0 {2,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S} {6,S}
3    Cd 0 {1,S} {4,D} {5,S}
4    C  0 {3,D}
5    Cs 0 {3,S}
6    H  0 {2,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S} {6,S}
3    Cd 0 {1,S} {4,D} {5,S}
4    C  0 {3,D}
5    Cs 0 {3,S}
6    Cs 0 {2,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S} {6,S}
3    Cd 0 {1,S} {4,D} {5,S}
4    C  0 {3,D}
5    Cs 0 {3,S}
6    Ss 0 {2,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S}
3    Cd 0 {1,S} {4,D}
4    Sd 0 {3,D}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    S  0 {1,S}
3 *2 C  0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S}
3 *2 Cs 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S} {4,S}
3 *2 Cs 0 {1,S} {5,S} {6,S} {7,S}
4    H  0 {2,S}
5    H  0 {3,S}
6    H  0 {3,S}
7    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S} {4,S}
3 *2 Cs 0 {1,S} {5,S} {6,S} {7,S}
4    H  0 {2,S}
5    Cs 0 {3,S}
6    H  0 {3,S}
7    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S} {4,S}
3 *2 Cs 0 {1,S} {5,S} {6,S} {7,S}
4    H  0 {2,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
7    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S} {4,S}
3 *2 Cs 0 {1,S} {5,S} {6,S} {7,S}
4    H  0 {2,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
7    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S} {4,S}
3 *2 Cs 0 {1,S} {5,S} {6,S} {7,S}
4    Cs 0 {2,S}
5    H  0 {3,S}
6    H  0 {3,S}
7    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S} {4,S}
3 *2 Cs 0 {1,S} {5,S} {6,S} {7,S}
4    Cs 0 {2,S}
5    Cs 0 {3,S}
6    H  0 {3,S}
7    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S} {4,S}
3 *2 Cs 0 {1,S} {5,S} {6,S} {7,S}
4    Cs 0 {2,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
7    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S} {4,S}
3 *2 Cs 0 {1,S} {5,S} {6,S} {7,S}
4    Cs 0 {2,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
7    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S} {4,S}
3 *2 Cs 0 {1,S} {5,S} {6,S} {7,S}
4    Ss 0 {2,S}
5    H  0 {3,S}
6    H  0 {3,S}
7    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S} {4,S}
3 *2 Cs 0 {1,S} {5,S} {6,S} {7,S}
4    Ss 0 {2,S}
5    Cs 0 {3,S}
6    H  0 {3,S}
7    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S} {4,S}
3 *2 Cs 0 {1,S} {5,S} {6,S} {7,S}
4    Ss 0 {2,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
7    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S} {4,S}
3 *2 Cs 0 {1,S} {5,S} {6,S} {7,S}
4    Ss 0 {2,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
7    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S}
3 *2 Ct 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S}
3 *2 Cb 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S}
3 *2 CO 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S}
3 *2 Cd 0 {1,S} {4,D}
4    C  0 {3,D}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S} {6,S}
3 *2 Cd 0 {1,S} {4,D} {5,S}
4    C  0 {3,D}
5    H  0 {3,S}
6    H  0 {2,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S} {6,S}
3 *2 Cd 0 {1,S} {4,D} {5,S}
4    C  0 {3,D}
5    H  0 {3,S}
6    Cs 0 {2,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S} {6,S}
3 *2 Cd 0 {1,S} {4,D} {5,S}
4    C  0 {3,D}
5    H  0 {3,S}
6    Ss 0 {2,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S} {6,S}
3 *2 Cd 0 {1,S} {4,D} {5,S}
4    C  0 {3,D}
5    Cs 0 {3,S}
6    H  0 {2,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S} {6,S}
3 *2 Cd 0 {1,S} {4,D} {5,S}
4    C  0 {3,D}
5    Cs 0 {3,S}
6    Cs 0 {2,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S} {6,S}
3 *2 Cd 0 {1,S} {4,D} {5,S}
4    C  0 {3,D}
5    Cs 0 {3,S}
6    Ss 0 {2,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S}
3 *2 Cd 0 {1,S} {4,D}
4    Sd 0 {3,D}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ss 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ss 0 {1,S} {4,S}
4    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ss 0 {1,S} {4,S}
4    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ss 0 {1,S} {4,S}
4    Ss 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 Ss 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 Ss 0 {1,S} {4,S}
4    H  0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 Ss 0 {1,S} {4,S}
4    Cs 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    H  0 {1,S}
3 *2 Ss 0 {1,S} {4,S}
4    Ss 0 {3,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S}
3    Ss 0 {1,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S} {5,S}
3    Ss 0 {1,S} {4,S}
4    H  0 {3,S}
5    H  0 {2,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S} {5,S}
3    Ss 0 {1,S} {4,S}
4    Cs 0 {3,S}
5    H  0 {2,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S} {5,S}
3 *2 Ss 0 {1,S} {4,S}
4    Cs 0 {3,S}
5    H  0 {2,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S} {5,S}
3    Ss 0 {1,S} {4,S}
4    Ss 0 {3,S}
5    H  0 {2,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S} {5,S}
3 *2 Ss 0 {1,S} {4,S}
4    Ss 0 {3,S}
5    H  0 {2,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S} {5,S}
3    Ss 0 {1,S} {4,S}
4    Cs 0 {3,S}
5    Cs 0 {2,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S} {5,S}
3    Ss 0 {1,S} {4,S}
4    Cs 0 {3,S}
5    Ss 0 {2,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2    Ss 0 {1,S} {5,S}
3 *2 Ss 0 {1,S} {4,S}
4    Cs 0 {3,S}
5    Ss 0 {2,S}
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
    group = 
"""
1 *1 Ss 0 {2,S} {3,S}
2 *2 Ss 0 {1,S} {5,S}
3    Ss 0 {1,S} {4,S}
4    Ss 0 {3,S}
5    Ss 0 {2,S}
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
    group = 
"""
1 *3 H 1
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
    group = 
"""
1 *3 C 1
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
    group = 
"""
1 *3 Cb 1
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
    group = 
"""
1 *3 Ct 1 {2,T}
2    C  0 {1,T}
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
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    R 0 {1,S}
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
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cs 0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Ct 0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cb 0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    CO 0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Os 0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Ss 0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
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
    index = 239,
    label = "CdsJ-C=S",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cd 0 {1,S} {4,D}
4    Sd 0 {3,D}
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
    group = 
"""
1 *3 Cd 1 {2,D} {3,S}
2    Sd 0 {1,D}
3    R  0 {1,S}
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
    group = 
"""
1 *3 Cd 1 {2,D} {3,S}
2    Sd 0 {1,D}
3    H  0 {1,S}
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
    group = 
"""
1 *3 Cd 1 {2,D} {3,S}
2    Sd 0 {1,D}
3    Cs 0 {1,S}
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
    group = 
"""
1 *3 Cd 1 {2,D} {3,S}
2    Sd 0 {1,D}
3    Ct 0 {1,S}
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
    group = 
"""
1 *3 Cd 1 {2,D} {3,S}
2    Sd 0 {1,D}
3    Cb 0 {1,S}
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
    group = 
"""
1 *3 Cd 1 {2,D} {3,S}
2    Sd 0 {1,D}
3    CO 0 {1,S}
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
    group = 
"""
1 *3 Cd 1 {2,D} {3,S}
2    Sd 0 {1,D}
3    Os 0 {1,S}
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
    group = 
"""
1 *3 Cd 1 {2,D} {3,S}
2    Sd 0 {1,D}
3    Ss 0 {1,S}
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
    group = 
"""
1 *3 Cd 1 {2,D} {3,S}
2    Sd 0 {1,D}
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
    index = 249,
    label = "C=SJ-C=S",
    group = 
"""
1 *3 Cd 1 {2,D} {3,S}
2    Sd 0 {1,D}
3    Cd 0 {1,S} {4,D}
4    Sd 0 {3,D}
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
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    O 0 {1,D}
3    R 0 {1,S}
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
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    O 0 {1,D}
3    H 0 {1,S}
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
    group = 
"""
1 *3 C   1 {2,D} {3,S}
2    O   0 {1,D}
3    R!H 0 {1,S}
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
    group = 
"""
1 *3 C      1 {2,D} {3,S}
2    O      0 {1,D}
3    {Cs,O} 0 {1,S}
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
    group = 
"""
1 *3 C             1 {2,D} {3,S}
2    O             0 {1,D}
3    {Cd,Ct,Cb,CO} 0 {1,S}
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
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
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
    index = 256,
    label = "CsJ-HHH",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
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
    index = 257,
    label = "CsJ-CsHH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
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
    index = 258,
    label = "CsJ-CsCsH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
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
    index = 259,
    label = "CsJ-CsCsCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
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
    index = 260,
    label = "CsJ-OsHH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Os 0 {1,S}
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
    index = 261,
    label = "CsJ-OsCsH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Os 0 {1,S}
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
    index = 262,
    label = "CsJ-OsCsCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Os 0 {1,S}
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
    index = 263,
    label = "CsJ-OsOsH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Os 0 {1,S}
3    Os 0 {1,S}
4    H  0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Os 0 {1,S}
3    Os 0 {1,S}
4    Cs 0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Os 0 {1,S}
3    Os 0 {1,S}
4    Os 0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
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
    index = 267,
    label = "CsJ-SsCsH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
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
    index = 268,
    label = "CsJ-SsCsCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
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
    index = 269,
    label = "CsJ-SsSsH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ss 0 {1,S}
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
    index = 270,
    label = "CsJ-SsSsCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ss 0 {1,S}
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
    index = 271,
    label = "CsJ-SsSsSs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ss 0 {1,S}
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
    index = 272,
    label = "CsJ-OneDe",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    {H,Cs,Os,Ss}  0 {1,S}
4    {H,Cs,Os,Ss}  0 {1,S}
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
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    H             0 {1,S}
4    H             0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
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
    index = 275,
    label = "CsJ-CbHH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
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
    index = 276,
    label = "CsJ-COHH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    CO 0 {1,S}
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
    index = 277,
    label = "CsJ-CdHH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S} {5,D}
3    H  0 {1,S}
4    H  0 {1,S}
5    C  0 {2,D}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S} {5,D}
3    H  0 {1,S}
4    H  0 {1,S}
5    Sd 0 {2,D}
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
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    Cs            0 {1,S}
4    H             0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
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
    index = 281,
    label = "CsJ-CbCsH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
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
    index = 282,
    label = "CsJ-COCsH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    CO 0 {1,S}
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
    index = 283,
    label = "CsJ-CdCsH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S} {5,D}
3    Cs 0 {1,S}
4    H  0 {1,S}
5    C  0 {2,D}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S} {5,D}
3    Cs 0 {1,S}
4    H  0 {1,S}
5    Sd 0 {2,D}
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
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    Os            0 {1,S}
4    H             0 {1,S}
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
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    Ss            0 {1,S}
4    H             0 {1,S}
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
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    Cs            0 {1,S}
4    Cs            0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
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
    index = 289,
    label = "CsJ-CbCsCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
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
    index = 290,
    label = "CsJ-COCsCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    CO 0 {1,S}
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
    index = 291,
    label = "CsJ-CdCsCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S} {5,D}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    C  0 {2,D}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S} {5,D}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Sd 0 {2,D}
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
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    Os            0 {1,S}
4    Cs            0 {1,S}
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
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    Ss            0 {1,S}
4    Cs            0 {1,S}
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
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    Os            0 {1,S}
4    Os            0 {1,S}
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
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    Os            0 {1,S}
4    Ss            0 {1,S}
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
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    Ss            0 {1,S}
4    Ss            0 {1,S}
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
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 299,
    label = "CsJ-TwoDeH",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 300,
    label = "CsJ-CtCtH",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Ct 0 {1,S}
4    H  0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cb 0 {1,S}
4    H  0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    CO 0 {1,S}
4    H  0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    Cb 0 {1,S}
4    H  0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    CO 0 {1,S}
4    H  0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    CO 0 {1,S}
3    CO 0 {1,S}
4    H  0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S} {5,D}
3    Ct 0 {1,S}
4    H  0 {1,S}
5    C  0 {2,D}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S} {5,D}
3    Cb 0 {1,S}
4    H  0 {1,S}
5    C  0 {2,D}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S} {5,D}
3    CO 0 {1,S}
4    H  0 {1,S}
5    C  0 {2,D}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cd 0 {1,S} {5,D}
4    H  0 {1,S}
5    Sd 0 {3,D}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    Cd 0 {1,S} {5,D}
4    H  0 {1,S}
5    Sd 0 {3,D}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    CO 0 {1,S}
3    Cd 0 {1,S} {5,D}
4    H  0 {1,S}
5    Sd 0 {3,D}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S} {5,D}
3    Cd 0 {1,S} {6,D}
4    H  0 {1,S}
5    C  0 {2,D}
6    C  0 {3,D}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S} {5,D}
3    Cd 0 {1,S} {6,D}
4    H  0 {1,S}
5    C  0 {2,D}
6    Sd 0 {3,D}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S} {5,D}
3    Cd 0 {1,S} {6,D}
4    H  0 {1,S}
5    Sd 0 {2,D}
6    Sd 0 {3,D}
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
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 316,
    label = "CsJ-CtCtCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    CO 0 {1,S}
4    Cs 0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    CO 0 {1,S}
4    Cs 0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    CO 0 {1,S}
3    CO 0 {1,S}
4    Cs 0 {1,S}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S} {5,D}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
5    C  0 {2,D}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S} {5,D}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
5    C  0 {2,D}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S} {5,D}
3    CO 0 {1,S}
4    Cs 0 {1,S}
5    C  0 {2,D}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cd 0 {1,S} {5,D}
4    Cs 0 {1,S}
5    Sd 0 {3,D}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    Cd 0 {1,S} {5,D}
4    Cs 0 {1,S}
5    Sd 0 {3,D}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    CO 0 {1,S}
3    Cd 0 {1,S} {5,D}
4    Cs 0 {1,S}
5    Sd 0 {3,D}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S} {5,D}
3    Cd 0 {1,S} {6,D}
4    Cs 0 {1,S}
5    C  0 {2,D}
6    C  0 {3,D}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S} {5,D}
3    Cd 0 {1,S} {6,D}
4    Cs 0 {1,S}
5    C  0 {2,D}
6    Sd 0 {3,D}
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
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S} {5,D}
3    Cd 0 {1,S} {6,D}
4    Cs 0 {1,S}
5    Sd 0 {2,D}
6    Sd 0 {3,D}
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
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    Os            0 {1,S}
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
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 333,
    label = "CsJ-ThreeDe",
    group = 
"""
1 *3 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 334,
    label = "Y_1centerbirad",
    group = 
"""
1 *3 {Cs,Cd,O} 2T
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 335,
    label = "O_atom_triplet",
    group = 
"""
1 *3 O 2T
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 336,
    label = "CH2_triplet",
    group = 
"""
1 *3 Cs 2T {2,S} {3,S}
2    H 0       {1,S}
3    H 0       {1,S}
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
    group = 
"""
1 *3 {Ct,Os} 1 {2,{S,T}}
2    {Ct,Os} 1 {1,{S,T}}
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
    group = 
"""
1 *3 Os 1 {2,S}
2    Os 1 {1,S}
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
    group = 
"""
1 *3 Ct 1 {2,T}
2    Ct 1 {1,T}
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
    group = 
"""
1 *3 O 1 {2,S}
2    R 0 {1,S}
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
    group = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
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
    group = 
"""
1 *3 O   1 {2,S}
2    R!H 0 {1,S}
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
    group = 
"""
1 *3 O  1 {2,S}
2    Cs 0 {1,S}
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
    group = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
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
    group = 
"""
1 *3 O             1 {2,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
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
    group = 
"""
1 *3 S 1 {2,S}
2    R  0 {1,S}
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
    group = 
"""
1 *3 Ss 1 {2,S}
2    R  0 {1,S}
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
    group = 
"""
1 *3 Ss 1 {2,S}
2    H  0 {1,S}
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
    group = 
"""
1 *3 Ss 1 {2,S}
2    Cs 0 {1,S}
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
    group = 
"""
1 *3 Ss 1 {2,S}
2    Ss 0 {1,S}
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
    group = 
"""
1 *3 Ss            1 {2,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
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
    group = 
"""
1 *3 Ss 1 {2,S}
2    Ct 0 {1,S}
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
    group = 
"""
1 *3 Ss 1 {2,S}
2    Cb 0 {1,S}
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
    group = 
"""
1 *3 Ss 1 {2,S}
2    CO 0 {1,S}
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
    group = 
"""
1 *3 Ss 1 {2,S}
2    Cd 0 {1,S} {3,D}
3    C  0 {2,D}
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
    group = 
"""
1 *3 Ss 1 {2,S}
2    Cd 0 {1,S} {3,D}
3    Sd 0 {2,D}
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
        L3: O_atom_triplet
        L3: CH2_triplet
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

forbidden(
    label = "birad_singlet",
    group = 
"""
1 *3 {C,N,Si} 2S 0
""",
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

forbidden(
    label = "OS_birad_singlet",
    group = 
"""
1 *3 {O,S} 2S 2
""",
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

forbidden(
    label = "quadrad_singlet",
    group = 
"""
1 *3 {C,N,Si} 4S 0
""",
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)