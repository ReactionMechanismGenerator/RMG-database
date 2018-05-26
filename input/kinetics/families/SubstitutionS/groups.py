#!/usr/bin/env python
# encoding: utf-8

name = "SubstitutionS/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["S-RR_or_RRrad", "YJ"], products=["S-RR_or_RRrad", "YJ"], ownReverse=True)

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "S-RR_or_RRrad",
    group = "OR{S-RR, S-RRrad}",
    kinetics = None,
)

entry(
    index = 2,
    label = "YJ",
    group = "OR{Y_2centeradjbirad, HJ, CJ, O_rad, SJ, Y_1centerbirad}",
    kinetics = None,
)

entry(
    index = 3,
    label = "S-RR",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 R   u0 {1,S}
3    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "S-HH",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "S-CH",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "S-CsH",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "S-Cs(NonDe)H",
    group = 
"""
1 *1 S2s    u0 p2 c0 {2,S} {3,S}
2 *2 H      u0 {1,S}
3    Cs     u0 {1,S} {4,S} {5,S} {6,S}
4    [H,Cs] u0 {3,S}
5    [H,Cs] u0 {3,S}
6    [H,Cs] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "S-Cs(HHH)H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    H   u0 {3,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "S-Cs(CsHH)H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "S-Cs(CsCsH)H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    Cs  u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "S-Cs(CsCsCs)H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "S-Cs(OneDe)H",
    group = 
"""
1 *1 S2s           u0 p2 c0 {2,S} {3,S}
2 *2 H             u0 {1,S}
3    Cs            u0 {1,S} {4,S} {5,S} {6,S}
4    [H,Cs]        u0 {3,S}
5    [H,Cs]        u0 {3,S}
6    [Cd,CO,CS,Ct,Cb] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "S-Cs(CdHH)H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    Cs u0 {1,S} {4,S} {5,S} {6,S}
4    Cd u0 {3,S}
5    H  u0 {3,S}
6    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "S-Cs(CdCsH)H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    Cs u0 {1,S} {4,S} {5,S} {6,S}
4    Cd u0 {3,S}
5    Cs u0 {3,S}
6    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "S-Cs(CdCsCs)H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    Cs u0 {1,S} {4,S} {5,S} {6,S}
4    Cd u0 {3,S}
5    Cs u0 {3,S}
6    Cs u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "S-Cs(CtHH)H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    Cs u0 {1,S} {4,S} {5,S} {6,S}
4    Ct u0 {3,S}
5    H  u0 {3,S}
6    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "S-Cs(CtCsH)H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    Cs u0 {1,S} {4,S} {5,S} {6,S}
4    Ct u0 {3,S}
5    Cs u0 {3,S}
6    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "S-Cs(CtCsCs)H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    Cs u0 {1,S} {4,S} {5,S} {6,S}
4    Ct u0 {3,S}
5    Cs u0 {3,S}
6    Cs u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "S-Cs(TwoDe)H",
    group = 
"""
1 *1 S2s              u0 p2 c0 {2,S} {3,S}
2 *2 H                u0 {1,S}
3    Cs               u0 {1,S} {4,S} {5,S} {6,S}
4    [H,Cs]           u0 {3,S}
5    [Cd,CO,CS,Ct,Cb] u0 {3,S}
6    [Cd,CO,CS,Ct,Cb] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "S-Cs(ThreeDe)H",
    group = 
"""
1 *1 S2s              u0 p2 c0 {2,S} {3,S}
2 *2 H                u0 {1,S}
3    Cs               u0 {1,S} {4,S} {5,S} {6,S}
4    [Cd,CO,CS,Ct,Cb] u0 {3,S}
5    [Cd,CO,CS,Ct,Cb] u0 {3,S}
6    [Cd,CO,CS,Ct,Cb] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "S-CdH",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    Cd  u0 {1,S} {4,D}
4    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "S-Cds(H)H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "S-Cds(Cs)H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "S-CtH",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "S-CbH",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "S-COH",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "S-CSH",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "S-HC",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "S-HCs",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "S-HCs(NonDe)",
    group = 
"""
1 *1 S2s           u0 p2 c0 {2,S} {3,S}
2    H             u0 {1,S}
3 *2 Cs            u0 {1,S} {4,S} {5,S} {6,S}
4    [H,Cs,O2s,S2s] u0 {3,S}
5    [H,Cs,O2s,S2s] u0 {3,S}
6    [H,Cs,O2s,S2s] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "S-HCs(HHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    H   u0 {3,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "S-HCs(CsHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "S-HCs(CsCsH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    Cs  u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "S-HCs(CsCsCs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "S-HCs(CsOsH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    O2s  u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 403,
    label = "S-HCs(CsSH)",
    group =
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    S2s u0 p2 c0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "S-HCs(OneDe)",
    group = 
"""
1 *1 S2s              u0 p2 c0 {2,S} {3,S}
2    H                u0 {1,S}
3 *2 Cs               u0 {1,S} {4,S} {5,S} {6,S}
4    [H,Cs]           u0 {3,S}
5    [H,Cs]           u0 {3,S}
6    [Cd,CO,CS,Ct,Cb] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "S-HCs(CdHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cd  u0 {3,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "S-HCs(CdCsH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cd  u0 {3,S}
5    Cs  u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "S-HCs(CdCsCs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cd  u0 {3,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "S-HCs(CtHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Ct  u0 {3,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "S-HCs(CtCsH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Ct  u0 {3,S}
5    Cs  u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "S-HCs(CtCsCs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Ct  u0 {3,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "S-HCs(TwoDe)",
    group = 
"""
1 *1 S2s              u0 p2 c0 {2,S} {3,S}
2    H                u0 {1,S}
3 *2 Cs               u0 {1,S} {4,S} {5,S} {6,S}
4    [H,Cs]           u0 {3,S}
5    [Cd,CO,CS,Ct,Cb] u0 {3,S}
6    [Cd,CO,CS,Ct,Cb] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "S-HCs(ThreeDe)",
    group = 
"""
1 *1 S2s              u0 p2 c0 {2,S} {3,S}
2    H                u0 {1,S}
3 *2 Cs               u0 {1,S} {4,S} {5,S} {6,S}
4    [Cd,CO,CS,Ct,Cb] u0 {3,S}
5    [Cd,CO,CS,Ct,Cb] u0 {3,S}
6    [Cd,CO,CS,Ct,Cb] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "S-HCd",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 Cd  u0 {1,S} {4,D}
4    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "S-HCds(H)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "S-HCds(Cs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "S-HCt",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "S-HCb",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "S-HCO",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "S-HCO(H)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 CO  u0 {1,S} {4,S}
4    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "S-HCS",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "S-CC",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S}
3    C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "S-CsCs",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cs  u0 {1,S}
3    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "S-Cs(NonDe)Cs(NonDe)",
    group = 
"""
1 *1 S2s    u0 p2 c0 {2,S} {3,S}
2 *2 Cs     u0 {1,S} {4,S} {5,S} {6,S}
3    Cs     u0 {1,S} {7,S} {8,S} {9,S}
4    [H,Cs] u0 {2,S}
5    [H,Cs] u0 {2,S}
6    [H,Cs] u0 {2,S}
7    [H,Cs] u0 {3,S}
8    [H,Cs] u0 {3,S}
9    [H,Cs] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "S-Cs(HHH)Cs(HHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
3    Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    H   u0 {2,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
7    H   u0 {3,S}
8    H   u0 {3,S}
9    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "S-Cs(HHH)Cs(CsHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
3    Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    Cs  u0 {2,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
7    H   u0 {3,S}
8    H   u0 {3,S}
9    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "S-Cs(CsHH)Cs(HHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cs  u0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    Cs  u0 {2,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
7    H   u0 {3,S}
8    H   u0 {3,S}
9    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "S-Cs(HHH)Cs(CsCsH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
3    Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    Cs  u0 {2,S}
5    Cs  u0 {2,S}
6    H   u0 {2,S}
7    H   u0 {3,S}
8    H   u0 {3,S}
9    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "S-Cs(CsCsH)Cs(HHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cs  u0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    Cs  u0 {2,S}
5    Cs  u0 {2,S}
6    H   u0 {2,S}
7    H   u0 {3,S}
8    H   u0 {3,S}
9    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "S-Cs(HHH)Cs(CsCsCs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
3    Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    Cs  u0 {2,S}
5    Cs  u0 {2,S}
6    Cs  u0 {2,S}
7    H   u0 {3,S}
8    H   u0 {3,S}
9    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "S-Cs(CsCsCs)Cs(HHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cs  u0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    Cs  u0 {2,S}
5    Cs  u0 {2,S}
6    Cs  u0 {2,S}
7    H   u0 {3,S}
8    H   u0 {3,S}
9    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "S-Cs(CsHH)Cs(CsHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
3    Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    Cs  u0 {2,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
7    Cs  u0 {3,S}
8    H   u0 {3,S}
9    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "S-Cs(CsHH)Cs(CsCsH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
3    Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    Cs  u0 {2,S}
5    Cs  u0 {2,S}
6    H   u0 {2,S}
7    Cs  u0 {3,S}
8    H   u0 {3,S}
9    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "S-Cs(CsCsH)Cs(CsHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cs  u0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    Cs  u0 {2,S}
5    Cs  u0 {2,S}
6    H   u0 {2,S}
7    Cs  u0 {3,S}
8    H   u0 {3,S}
9    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "S-Cs(CsHH)Cs(CsCsCs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
3    Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    Cs  u0 {2,S}
5    Cs  u0 {2,S}
6    Cs  u0 {2,S}
7    Cs  u0 {3,S}
8    H   u0 {3,S}
9    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "S-Cs(CsCsCs)Cs(CsHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cs  u0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    Cs  u0 {2,S}
5    Cs  u0 {2,S}
6    Cs  u0 {2,S}
7    Cs  u0 {3,S}
8    H   u0 {3,S}
9    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "S-Cs(CsCsH)Cs(CsCsH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
3    Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    Cs  u0 {2,S}
5    Cs  u0 {2,S}
6    H   u0 {2,S}
7    Cs  u0 {3,S}
8    Cs  u0 {3,S}
9    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "S-Cs(CsCsH)Cs(CsCsCs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
3    Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    Cs  u0 {2,S}
5    Cs  u0 {2,S}
6    Cs  u0 {2,S}
7    Cs  u0 {3,S}
8    Cs  u0 {3,S}
9    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "S-Cs(CsCsCs)Cs(CsCsH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cs  u0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    Cs  u0 {2,S}
5    Cs  u0 {2,S}
6    Cs  u0 {2,S}
7    Cs  u0 {3,S}
8    Cs  u0 {3,S}
9    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "S-Cs(CsCsCs)Cs(CsCsCs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
3    Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    Cs  u0 {2,S}
5    Cs  u0 {2,S}
6    Cs  u0 {2,S}
7    Cs  u0 {3,S}
8    Cs  u0 {3,S}
9    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "S-Cs(NonDe)Cs(De)",
    group = 
"""
1 *1 S2s              u0 p2 c0 {2,S} {3,S}
2    Cs               u0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs               u0 {1,S} {7,S} {8,S} {9,S}
4    [H,Cs]           u0 {2,S}
5    [H,Cs]           u0 {2,S}
6    [H,Cs]           u0 {2,S}
7    [Cd,Ct,Cb,CO,CS] u0 {3,S}
8    R                u0 {3,S}
9    R                u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "S-Cs(NonDe)Cs(OneDe)",
    group = 
"""
1 *1 S2s              u0 p2 c0 {2,S} {3,S}
2    Cs               u0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs               u0 {1,S} {7,S} {8,S} {9,S}
4    [H,Cs]           u0 {2,S}
5    [H,Cs]           u0 {2,S}
6    [H,Cs]           u0 {2,S}
7    [Cd,Ct,Cb,CO,CS] u0 {3,S}
8    [H,Cs]           u0 {3,S}
9    [H,Cs]           u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "S-Cs(HHH)Cs(CdHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cs  u0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    H   u0 {2,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
7    Cd  u0 {3,S}
8    H   u0 {3,S}
9    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "S-Cs(HHH)Cs(CdCsH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cs  u0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    H   u0 {2,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
7    Cd  u0 {3,S}
8    Cs  u0 {3,S}
9    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "S-Cs(HHH)Cs(CdCsCs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cs  u0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    H   u0 {2,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
7    Cd  u0 {3,S}
8    Cs  u0 {3,S}
9    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "S-Cs(HHH)Cs(CtHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cs  u0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    H   u0 {2,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
7    Ct  u0 {3,S}
8    H   u0 {3,S}
9    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 77,
    label = "S-Cs(HHH)Cs(CtCsH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cs  u0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    H   u0 {2,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
7    Ct  u0 {3,S}
8    Cs  u0 {3,S}
9    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "S-Cs(HHH)Cs(CtCsCs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cs  u0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    H   u0 {2,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
7    Ct  u0 {3,S}
8    Cs  u0 {3,S}
9    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "S-Cs(NonDe)Cs(TwoDe)",
    group = 
"""
1 *1 S2s              u0 p2 c0 {2,S} {3,S}
2    Cs               u0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs               u0 {1,S} {7,S} {8,S} {9,S}
4    [H,Cs]           u0 {2,S}
5    [H,Cs]           u0 {2,S}
6    [H,Cs]           u0 {2,S}
7    [Cd,Ct,Cb,CO,CS] u0 {3,S}
8    [Cd,Ct,Cb,CO,CS] u0 {3,S}
9    [H,Cs]           u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "S-Cs(NonDe)Cs(ThreeDe)",
    group = 
"""
1 *1 S2s              u0 p2 c0 {2,S} {3,S}
2    Cs               u0 {1,S} {4,S} {5,S} {6,S}
3 *2 Cs               u0 {1,S} {7,S} {8,S} {9,S}
4    [H,Cs]           u0 {2,S}
5    [H,Cs]           u0 {2,S}
6    [H,Cs]           u0 {2,S}
7    [Cd,Ct,Cb,CO,CS] u0 {3,S}
8    [Cd,Ct,Cb,CO,CS] u0 {3,S}
9    [Cd,Ct,Cb,CO,CS] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "S-Cs(De)Cs(NonDe)",
    group = 
"""
1 *1 S2s              u0 p2 c0 {2,S} {3,S}
2 *2 Cs               u0 {1,S} {4,S} {5,S} {6,S}
3    Cs               u0 {1,S} {7,S} {8,S} {9,S}
4    [H,Cs]           u0 {2,S}
5    [H,Cs]           u0 {2,S}
6    [H,Cs]           u0 {2,S}
7    [Cd,Ct,Cb,CO,CS] u0 {3,S}
8    R                u0 {3,S}
9    R                u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 82,
    label = "S-Cs(OneDe)Cs(NonDe)",
    group = 
"""
1 *1 S2s              u0 p2 c0 {2,S} {3,S}
2 *2 Cs               u0 {1,S} {4,S} {5,S} {6,S}
3    Cs               u0 {1,S} {7,S} {8,S} {9,S}
4    [H,Cs]           u0 {2,S}
5    [H,Cs]           u0 {2,S}
6    [H,Cs]           u0 {2,S}
7    [Cd,Ct,Cb,CO,CS] u0 {3,S}
8    [H,Cs]           u0 {3,S}
9    [H,Cs]           u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 83,
    label = "S-Cs(CdHH)Cs(HHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
3    Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    H   u0 {2,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
7    Cd  u0 {3,S}
8    H   u0 {3,S}
9    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 84,
    label = "S-Cs(CdCsH)Cs(HHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
3    Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    H   u0 {2,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
7    Cd  u0 {3,S}
8    Cs  u0 {3,S}
9    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 85,
    label = "S-Cs(CdCsCs)Cs(HHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
3    Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    H   u0 {2,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
7    Cd  u0 {3,S}
8    Cs  u0 {3,S}
9    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 86,
    label = "S-Cs(CtHH)Cs(HHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
3    Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    H   u0 {2,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
7    Ct  u0 {3,S}
8    H   u0 {3,S}
9    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 87,
    label = "S-Cs(CtCsH)Cs(HHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
3    Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    H   u0 {2,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
7    Ct  u0 {3,S}
8    Cs  u0 {3,S}
9    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 88,
    label = "S-Cs(CtCsCs)Cs(HHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
3    Cs  u0 {1,S} {7,S} {8,S} {9,S}
4    H   u0 {2,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
7    Ct  u0 {3,S}
8    Cs  u0 {3,S}
9    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 89,
    label = "S-Cs(TwoDe)Cs(NonDe)",
    group = 
"""
1 *1 S2s              u0 p2 c0 {2,S} {3,S}
2 *2 Cs               u0 {1,S} {4,S} {5,S} {6,S}
3    Cs               u0 {1,S} {7,S} {8,S} {9,S}
4    [H,Cs]           u0 {2,S}
5    [H,Cs]           u0 {2,S}
6    [H,Cs]           u0 {2,S}
7    [Cd,Ct,Cb,CO,CS] u0 {3,S}
8    [Cd,Ct,Cb,CO,CS] u0 {3,S}
9    [H,Cs]           u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 90,
    label = "S-Cs(ThreeDe)Cs(NonDe)",
    group = 
"""
1 *1 S2s              u0 p2 c0 {2,S} {3,S}
2 *2 Cs               u0 {1,S} {4,S} {5,S} {6,S}
3    Cs               u0 {1,S} {7,S} {8,S} {9,S}
4    [H,Cs]           u0 {2,S}
5    [H,Cs]           u0 {2,S}
6    [H,Cs]           u0 {2,S}
7    [Cd,Ct,Cb,CO,CS] u0 {3,S}
8    [Cd,Ct,Cb,CO,CS] u0 {3,S}
9    [Cd,Ct,Cb,CO,CS] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 122,
    label = "S-CsCd",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cd  u0 {1,S} {4,D}
3    Cs  u0 {1,S}
4    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 123,
    label = "S-Cs(HHH)Cds(H)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cd  u0 {1,S} {4,D} {5,S}
3    Cs  u0 {1,S} {6,S} {7,S} {8,S}
4    C   u0 {2,D}
5    H   u0 {2,S}
6    H   u0 {3,S}
7    H   u0 {3,S}
8    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 124,
    label = "S-Cs(CsHH)Cds(H)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cd  u0 {1,S} {4,D} {5,S}
3    Cs  u0 {1,S} {6,S} {7,S} {8,S}
4    C   u0 {2,D}
5    H   u0 {2,S}
6    Cs  u0 {3,S}
7    H   u0 {3,S}
8    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 125,
    label = "S-Cs(CsCsH)Cds(H)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cd  u0 {1,S} {4,D} {5,S}
3    Cs  u0 {1,S} {6,S} {7,S} {8,S}
4    C   u0 {2,D}
5    H   u0 {2,S}
6    Cs  u0 {3,S}
7    Cs  u0 {3,S}
8    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 126,
    label = "S-Cs(CsCsCs)Cds(H)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cd  u0 {1,S} {4,D} {5,S}
3    Cs  u0 {1,S} {6,S} {7,S} {8,S}
4    C   u0 {2,D}
5    H   u0 {2,S}
6    Cs  u0 {3,S}
7    Cs  u0 {3,S}
8    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 127,
    label = "S-Cs(HHH)Cds(Cs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cd  u0 {1,S} {4,D} {5,S}
3    Cs  u0 {1,S} {6,S} {7,S} {8,S}
4    C   u0 {2,D}
5    Cs  u0 {2,S}
6    H   u0 {3,S}
7    H   u0 {3,S}
8    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 128,
    label = "S-Cs(CsHH)Cds(Cs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cd  u0 {1,S} {4,D} {5,S}
3    Cs  u0 {1,S} {6,S} {7,S} {8,S}
4    C   u0 {2,D}
5    Cs  u0 {2,S}
6    Cs  u0 {3,S}
7    H   u0 {3,S}
8    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 129,
    label = "S-Cs(CsCsH)Cds(Cs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cd  u0 {1,S} {4,D} {5,S}
3    Cs  u0 {1,S} {6,S} {7,S} {8,S}
4    C   u0 {2,D}
5    Cs  u0 {2,S}
6    Cs  u0 {3,S}
7    Cs  u0 {3,S}
8    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 130,
    label = "S-Cs(CsCsCs)Cds(Cs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cd  u0 {1,S} {4,D} {5,S}
3    Cs  u0 {1,S} {6,S} {7,S} {8,S}
4    C   u0 {2,D}
5    Cs  u0 {2,S}
6    Cs  u0 {3,S}
7    Cs  u0 {3,S}
8    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 131,
    label = "S-CdCs",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cd  u0 {1,S} {4,D}
3 *2 Cs  u0 {1,S}
4    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 132,
    label = "S-Cds(H)Cs(HHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cd  u0 {1,S} {4,D} {5,S}
3 *2 Cs  u0 {1,S} {6,S} {7,S} {8,S}
4    C   u0 {2,D}
5    H   u0 {2,S}
6    H   u0 {3,S}
7    H   u0 {3,S}
8    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 133,
    label = "S-Cds(H)Cs(CsHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cd  u0 {1,S} {4,D} {5,S}
3 *2 Cs  u0 {1,S} {6,S} {7,S} {8,S}
4    C   u0 {2,D}
5    H   u0 {2,S}
6    Cs  u0 {3,S}
7    H   u0 {3,S}
8    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 134,
    label = "S-Cds(H)Cs(CsCsH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cd  u0 {1,S} {4,D} {5,S}
3 *2 Cs  u0 {1,S} {6,S} {7,S} {8,S}
4    C   u0 {2,D}
5    H   u0 {2,S}
6    Cs  u0 {3,S}
7    Cs  u0 {3,S}
8    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 135,
    label = "S-Cds(H)Cs(CsCsCs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cd  u0 {1,S} {4,D} {5,S}
3 *2 Cs  u0 {1,S} {6,S} {7,S} {8,S}
4    C   u0 {2,D}
5    H   u0 {2,S}
6    Cs  u0 {3,S}
7    Cs  u0 {3,S}
8    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 136,
    label = "S-Cds(Cs)Cs(HHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cd  u0 {1,S} {4,D} {5,S}
3 *2 Cs  u0 {1,S} {6,S} {7,S} {8,S}
4    C   u0 {2,D}
5    Cs  u0 {2,S}
6    H   u0 {3,S}
7    H   u0 {3,S}
8    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 137,
    label = "S-Cds(Cs)Cs(CsHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cd  u0 {1,S} {4,D} {5,S}
3 *2 Cs  u0 {1,S} {6,S} {7,S} {8,S}
4    C   u0 {2,D}
5    Cs  u0 {2,S}
6    Cs  u0 {3,S}
7    H   u0 {3,S}
8    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 138,
    label = "S-Cds(Cs)Cs(CsCsH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cd  u0 {1,S} {4,D} {5,S}
3 *2 Cs  u0 {1,S} {6,S} {7,S} {8,S}
4    C   u0 {2,D}
5    Cs  u0 {2,S}
6    Cs  u0 {3,S}
7    Cs  u0 {3,S}
8    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 139,
    label = "S-Cds(Cs)Cs(CsCsCs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cd  u0 {1,S} {4,D} {5,S}
3 *2 Cs  u0 {1,S} {6,S} {7,S} {8,S}
4    C   u0 {2,D}
5    Cs  u0 {2,S}
6    Cs  u0 {3,S}
7    Cs  u0 {3,S}
8    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 91,
    label = "S-CsCt",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Ct  u0 {1,S}
3    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 92,
    label = "S-Cs(HHH)Ct",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Ct  u0 {1,S}
3    Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    H   u0 {3,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 93,
    label = "S-Cs(CsHH)Ct",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Ct  u0 {1,S}
3    Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 94,
    label = "S-Cs(CsCsH)Ct",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Ct  u0 {1,S}
3    Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    Cs  u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 95,
    label = "S-Cs(CsCsCs)Ct",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Ct  u0 {1,S}
3    Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 96,
    label = "S-CtCs",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Ct  u0 {1,S}
3 *2 Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 97,
    label = "S-CtCs(HHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Ct  u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    H   u0 {3,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 98,
    label = "S-CtCs(CsHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Ct  u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 99,
    label = "S-CtCs(CsCsH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Ct  u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    Cs  u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 100,
    label = "S-CtCs(CsCsCs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Ct  u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 101,
    label = "S-CsCb",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cb  u0 {1,S}
3    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 102,
    label = "S-Cs(HHH)Cb",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cb  u0 {1,S}
3    Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    H   u0 {3,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 103,
    label = "S-Cs(CsHH)Cb",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cb  u0 {1,S}
3    Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 104,
    label = "S-Cs(CsCsH)Cb",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cb  u0 {1,S}
3    Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    Cs  u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 105,
    label = "S-Cs(CsCsCs)Cb",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cb  u0 {1,S}
3    Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 106,
    label = "S-CbCs",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cb  u0 {1,S}
3 *2 Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 107,
    label = "S-CbCs(HHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cb  u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    H   u0 {3,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 108,
    label = "S-CbCs(CsHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cb  u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 109,
    label = "S-CbCs(CsCsH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cb  u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    Cs  u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 110,
    label = "S-CbCs(CsCsCs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cb  u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 111,
    label = "S-CsCO",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 CO  u0 {1,S}
3    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 112,
    label = "S-COCs",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    CO  u0 {1,S}
3 *2 Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 140,
    label = "S-CsC=S",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 CS  u0 {1,S}
3    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 141,
    label = "S-C=SCs",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    CS  u0 {1,S}
3 *2 Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 154,
    label = "S-CdCd",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {4,D}
4    C   u0 {3,D}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 142,
    label = "S-CdCt",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Ct  u0 {1,S}
3    Cd  u0 {1,S} {4,D}
4    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 143,
    label = "S-CtCd",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Ct  u0 {1,S}
3 *2 Cd  u0 {1,S} {4,D}
4    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 144,
    label = "S-CdCb",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cb  u0 {1,S}
3    Cd  u0 {1,S} {4,D}
4    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 145,
    label = "S-CbCd",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cb  u0 {1,S}
3 *2 Cd  u0 {1,S} {4,D}
4    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 146,
    label = "S-CdCO",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 CO  u0 {1,S}
3    Cd  u0 {1,S} {4,D}
4    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 147,
    label = "S-COCd",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    CO  u0 {1,S}
3 *2 Cd  u0 {1,S} {4,D}
4    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 155,
    label = "S-CdC=S",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 CS  u0 {1,S}
3    Cd  u0 {1,S} {4,D}
4    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 156,
    label = "S-C=SCd",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    CS  u0 {1,S}
3 *2 Cd  u0 {1,S} {4,D}
4    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 113,
    label = "S-CtCt",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Ct  u0 {1,S}
3    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 114,
    label = "S-CtCb",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cb  u0 {1,S}
3    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 115,
    label = "S-CbCt",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    Cb  u0 {1,S}
3 *2 Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 116,
    label = "S-CtCO",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 CO  u0 {1,S}
3    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 117,
    label = "S-COCt",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    CO  u0 {1,S}
3 *2 Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 148,
    label = "S-CtC=S",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 CS  u0 {1,S}
3    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 149,
    label = "S-C=SCt",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    CS  u0 {1,S}
3 *2 Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 118,
    label = "S-CbCb",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 Cb  u0 {1,S}
3    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 119,
    label = "S-CbCO",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 CO  u0 {1,S}
3    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 120,
    label = "S-COCb",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    CO  u0 {1,S}
3 *2 Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 150,
    label = "S-CbC=S",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 CS  u0 {1,S}
3    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 151,
    label = "S-C=SCb",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    CS  u0 {1,S}
3 *2 Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 121,
    label = "S-COCO",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 CO  u0 {1,S}
3    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 152,
    label = "S-COC=S",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 CS  u0 {1,S}
3    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 153,
    label = "S-C=SCO",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    CS  u0 {1,S}
3 *2 CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 157,
    label = "S-C=SC=S",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 CS  u0 {1,S}
3    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 158,
    label = "S-CS",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S   u0 {1,S}
3    C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 159,
    label = "S-CsSs",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S}
3    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 160,
    label = "S-Cs(HHH)S2s(H)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {4,S}
3    Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    H   u0 {2,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 161,
    label = "S-Cs(CsHH)S2s(H)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {4,S}
3    Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    H   u0 {2,S}
5    Cs  u0 {3,S}
6    H   u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 162,
    label = "S-Cs(CsCsH)S2s(H)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {4,S}
3    Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    H   u0 {2,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 163,
    label = "S-Cs(CsCsCs)S2s(H)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {4,S}
3    Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    H   u0 {2,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
7    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 164,
    label = "S-Cs(HHH)S2s(Cs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {4,S}
3    Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    Cs  u0 {2,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 165,
    label = "S-Cs(CsHH)S2s(Cs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {4,S}
3    Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    Cs  u0 {2,S}
5    Cs  u0 {3,S}
6    H   u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 166,
    label = "S-Cs(CsCsH)S2s(Cs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {4,S}
3    Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    Cs  u0 {2,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 167,
    label = "S-Cs(CsCsCs)S2s(Cs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {4,S}
3    Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    Cs  u0 {2,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
7    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 168,
    label = "S-Cs(HHH)S2s(S2s)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {4,S}
3    Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    S2s u0 p2 c0 {2,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 169,
    label = "S-Cs(CsHH)S2s(S2s)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {4,S}
3    Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    S2s u0 p2 c0 {2,S}
5    Cs  u0 {3,S}
6    H   u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 170,
    label = "S-Cs(CsCsH)S2s(S2s)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {4,S}
3    Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    S2s u0 p2 c0 {2,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 171,
    label = "S-Cs(CsCsCs)S2s(S2s)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {4,S}
3    Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    S2s u0 p2 c0 {2,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
7    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 175,
    label = "S-CdSs",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S}
3    Cd  u0 {1,S} {4,D}
4    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 176,
    label = "S-Cds(H)S2s(H)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {6,S}
3    Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    H   u0 {3,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 177,
    label = "S-Cds(H)S2s(Cs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {6,S}
3    Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    H   u0 {3,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 178,
    label = "S-Cds(H)S2s(S2s)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {6,S}
3    Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    H   u0 {3,S}
6    S2s u0 p2 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 179,
    label = "S-Cds(Cs)S2s(H)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {6,S}
3    Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    Cs  u0 {3,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 180,
    label = "S-Cds(Cs)S2s(Cs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {6,S}
3    Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    Cs  u0 {3,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 181,
    label = "S-Cds(Cs)S2s(S2s)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {6,S}
3    Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    Cs  u0 {3,S}
6    S2s u0 p2 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 172,
    label = "S-CtSs",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S}
3    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 173,
    label = "S-CbSs",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S}
3    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 174,
    label = "S-COSs",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S}
3    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 182,
    label = "S-C=SSs",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S}
3    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 183,
    label = "S-SC",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S   u0 {1,S}
3 *2 C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 184,
    label = "S-SsCs",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S}
3 *2 Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 185,
    label = "S-S2s(H)Cs(HHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S} {4,S}
3 *2 Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    H   u0 {2,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 186,
    label = "S-S2s(H)Cs(CsHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S} {4,S}
3 *2 Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    H   u0 {2,S}
5    Cs  u0 {3,S}
6    H   u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 187,
    label = "S-S2s(H)Cs(CsCsH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S} {4,S}
3 *2 Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    H   u0 {2,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 188,
    label = "S-S2s(H)Cs(CsCsCs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S} {4,S}
3 *2 Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    H   u0 {2,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
7    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 189,
    label = "S-S2s(Cs)Cs(HHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S} {4,S}
3 *2 Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    Cs  u0 {2,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 190,
    label = "S-S2s(Cs)Cs(CsHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S} {4,S}
3 *2 Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    Cs  u0 {2,S}
5    Cs  u0 {3,S}
6    H   u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 191,
    label = "S-S2s(Cs)Cs(CsCsH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S} {4,S}
3 *2 Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    Cs  u0 {2,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 192,
    label = "S-S2s(Cs)Cs(CsCsCs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S} {4,S}
3 *2 Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    Cs  u0 {2,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
7    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 193,
    label = "S-S2s(S2s)Cs(HHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S} {4,S}
3 *2 Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    S2s u0 p2 c0 {2,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 194,
    label = "S-S2s(S2s)Cs(CsHH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S} {4,S}
3 *2 Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    S2s u0 p2 c0 {2,S}
5    Cs  u0 {3,S}
6    H   u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 195,
    label = "S-S2s(S2s)Cs(CsCsH)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S} {4,S}
3 *2 Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    S2s u0 p2 c0 {2,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 196,
    label = "S-S2s(S2s)Cs(CsCsCs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S} {4,S}
3 *2 Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    S2s u0 p2 c0 {2,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
7    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 200,
    label = "S-SsCd",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S}
3 *2 Cd  u0 {1,S} {4,D}
4    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 201,
    label = "S-S2s(H)Cds(H)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S} {6,S}
3 *2 Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    H   u0 {3,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 202,
    label = "S-S2s(Cs)Cds(H)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S} {6,S}
3 *2 Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    H   u0 {3,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 203,
    label = "S-S2s(S2s)Cds(H)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S} {6,S}
3 *2 Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    H   u0 {3,S}
6    S2s u0 p2 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 204,
    label = "S-S2s(H)Cds(Cs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S} {6,S}
3 *2 Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    Cs  u0 {3,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 205,
    label = "S-S2s(Cs)Cds(Cs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S} {6,S}
3 *2 Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    Cs  u0 {3,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 206,
    label = "S-S2s(S2s)Cds(Cs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S} {6,S}
3 *2 Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    Cs  u0 {3,S}
6    S2s u0 p2 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 197,
    label = "S-SsCt",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S}
3 *2 Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 198,
    label = "S-SsCb",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S}
3 *2 Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 199,
    label = "S-SsCO",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S}
3 *2 CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 207,
    label = "S-SsC=S",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S}
3 *2 CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 208,
    label = "S-SsH",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    S2s u0 p2 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 209,
    label = "S-S2s(H)H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    S2s u0 p2 c0 {1,S} {4,S}
4    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 210,
    label = "S-S2s(Cs)H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    S2s u0 p2 c0 {1,S} {4,S}
4    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 211,
    label = "S-S2s(S2s)H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    S2s u0 p2 c0 {1,S} {4,S}
4    S2s u0 p2 c0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 212,
    label = "S-HSs",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 S2s u0 p2 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 213,
    label = "S-HSs(H)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 S2s u0 p2 c0 {1,S} {4,S}
4    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 214,
    label = "S-HSs(Cs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 S2s u0 p2 c0 {1,S} {4,S}
4    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 215,
    label = "S-HSs(S2s)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 S2s u0 p2 c0 {1,S} {4,S}
4    S2s u0 p2 c0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 216,
    label = "S-SsSs",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S}
3    S2s u0 p2 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 217,
    label = "S-S2s(H)S2s(H)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {5,S}
3    S2s u0 p2 c0 {1,S} {4,S}
4    H   u0 {3,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 218,
    label = "S-S2s(Cs)S2s(H)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {5,S}
3    S2s u0 p2 c0 {1,S} {4,S}
4    Cs  u0 {3,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 219,
    label = "S-S2s(H)S2s(Cs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S} {5,S}
3 *2 S2s u0 p2 c0 {1,S} {4,S}
4    Cs  u0 {3,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 220,
    label = "S-S2s(S2s)S2s(H)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {5,S}
3    S2s u0 p2 c0 {1,S} {4,S}
4    S2s u0 p2 c0 {3,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 221,
    label = "S-S2s(H)S2s(S2s)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S} {5,S}
3 *2 S2s u0 p2 c0 {1,S} {4,S}
4    S2s u0 p2 c0 {3,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 222,
    label = "S-S2s(Cs)S2s(Cs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {5,S}
3    S2s u0 p2 c0 {1,S} {4,S}
4    Cs  u0 {3,S}
5    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 223,
    label = "S-S2s(Cs)S2s(S2s)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {5,S}
3    S2s u0 p2 c0 {1,S} {4,S}
4    Cs  u0 {3,S}
5    S2s u0 p2 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 224,
    label = "S-S2s(S2s)S2s(Cs)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2    S2s u0 p2 c0 {1,S} {5,S}
3 *2 S2s u0 p2 c0 {1,S} {4,S}
4    Cs  u0 {3,S}
5    S2s u0 p2 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 225,
    label = "S-S2s(S2s)S2s(S2s)",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S2s u0 p2 c0 {1,S} {5,S}
3    S2s u0 p2 c0 {1,S} {4,S}
4    S2s u0 p2 c0 {3,S}
5    S2s u0 p2 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 227,
    label = "S-RRrad",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 R!H u1 {1,S}
3    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 337,
    label = "Y_2centeradjbirad",
    group = 
"""
1 *3 [Ct,O2s,S2s] u1 {2,[S,T]}
2    [Ct,O2s,S2s] u1 {1,[S,T]}
""",
    kinetics = None,
)

entry(
    index = 229,
    label = "S2b",
    group = 
"""
1 *3 S2s u1 {2,S}
2    S2s u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 338,
    label = "O2b",
    group = 
"""
1 *3 O2s u1 {2,S}
2    O2s u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 339,
    label = "C2b",
    group = 
"""
1 *3 Ct u1 {2,T}
2    Ct u1 {1,T}
""",
    kinetics = None,
)

entry(
    index = 334,
    label = "Y_1centerbirad",
    group = 
"""
1 *3 [Cs,Cd,O,S] u2
""",
    kinetics = None,
)

entry(
    index = 335,
    label = "O_atom_triplet",
    group = 
"""
1 *3 O u2
""",
    kinetics = None,
)

entry(
    index = 336,
    label = "CH2_triplet",
    group = 
"""
1 *3 Cs u2 {2,S} {3,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 226,
    label = "HJ",
    group = 
"""
1 *3 H u1
""",
    kinetics = None,
)

entry(
    index = 227,
    label = "CJ",
    group = 
"""
1 *3 C u1
""",
    kinetics = None,
)

entry(
    index = 255,
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
    index = 256,
    label = "CsJ-HHH",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 257,
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
    index = 258,
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
    index = 259,
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
    index = 260,
    label = "CsJ-OsHH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 261,
    label = "CsJ-OsCsH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 262,
    label = "CsJ-OsCsCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 263,
    label = "CsJ-OsOsH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    O2s u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 264,
    label = "CsJ-OsOsCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    O2s u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 265,
    label = "CsJ-OsOsOs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    O2s u0 {1,S}
4    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 266,
    label = "CsJ-SsHH",
    group = 
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    S2s u0 p2 c0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 267,
    label = "CsJ-SsCsH",
    group = 
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    S2s u0 p2 c0 {1,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 268,
    label = "CsJ-SsCsCs",
    group = 
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    S2s u0 p2 c0 {1,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 269,
    label = "CsJ-SsSsH",
    group = 
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    S2s u0 p2 c0 {1,S}
3    S2s u0 p2 c0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 270,
    label = "CsJ-SsSsCs",
    group = 
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    S2s u0 p2 c0 {1,S}
3    S2s u0 p2 c0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 271,
    label = "CsJ-SsSsSs",
    group = 
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    S2s u0 p2 c0 {1,S}
3    S2s u0 p2 c0 {1,S}
4    S2s u0 p2 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 272,
    label = "CsJ-OneDe",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [H,Cs,O2s,S2s]    u0 {1,S}
4    [H,Cs,O2s,S2s]    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 273,
    label = "CsJ-OneDeHH",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    H                u0 {1,S}
4    H                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 277,
    label = "CsJ-CdHH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 274,
    label = "CsJ-CtHH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 275,
    label = "CsJ-CbHH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 276,
    label = "CsJ-COHH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 278,
    label = "CsJ-C=SHH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 279,
    label = "CsJ-OneDeCsH",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    Cs               u0 {1,S}
4    H                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 283,
    label = "CsJ-CdCsH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 280,
    label = "CsJ-CtCsH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 281,
    label = "CsJ-CbCsH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 282,
    label = "CsJ-COCsH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 284,
    label = "CsJ-C=SCsH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 285,
    label = "CsJ-OneDeOsH",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    O2s               u0 {1,S}
4    H                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 286,
    label = "CsJ-OneDeSsH",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    S2s              u0 p2 c0 {1,S}
4    H                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 287,
    label = "CsJ-OneDeCsCs",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    Cs               u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 291,
    label = "CsJ-CdCsCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 288,
    label = "CsJ-CtCsCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 289,
    label = "CsJ-CbCsCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 290,
    label = "CsJ-COCsCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 292,
    label = "CsJ-C=SCsCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 293,
    label = "CsJ-OneDeOsCs",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    O2s               u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 294,
    label = "CsJ-OneDeSsCs",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    S2s              u0 p2 c0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 295,
    label = "CsJ-OneDeOsOs",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    O2s               u0 {1,S}
4    O2s               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 296,
    label = "CsJ-OneDeOsSs",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    O2s               u0 {1,S}
4    S2s              u0 p2 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 297,
    label = "CsJ-OneDeSsSs",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    S2s              u0 p2 c0 {1,S}
4    S2s              u0 p2 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 298,
    label = "CsJ-TwoDe",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [H,Cs,O2s,S2s]    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 299,
    label = "CsJ-TwoDeH",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 312,
    label = "CsJ-CdCdH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cd u0 {1,S} {6,D}
4    H  u0 {1,S}
5    C  u0 {2,D}
6    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 306,
    label = "CsJ-CdCtH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 307,
    label = "CsJ-CdCbH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 308,
    label = "CsJ-CdCOH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    CO u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 313,
    label = "CsJ-CdC=SH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    CS u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 300,
    label = "CsJ-CtCtH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 301,
    label = "CsJ-CtCbH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 302,
    label = "CsJ-CtCOH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    CO u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 309,
    label = "CsJ-CtC=SH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    CS u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 303,
    label = "CsJ-CbCbH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 304,
    label = "CsJ-CbCOH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    CO u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 310,
    label = "CsJ-CbC=SH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    CS u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 305,
    label = "CsJ-COCOH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    CO u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 311,
    label = "CsJ-COC=SH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    CS u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 314,
    label = "CsJ-C=SC=SH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    CS u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 315,
    label = "CsJ-TwoDeCs",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 328,
    label = "CsJ-CdCdCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cd u0 {1,S} {6,D}
4    Cs u0 {1,S}
5    C  u0 {2,D}
6    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 322,
    label = "CsJ-CdCtCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 323,
    label = "CsJ-CdCbCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 324,
    label = "CsJ-CdCOCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    CO u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 329,
    label = "CsJ-CdC=SCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    CS u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 316,
    label = "CsJ-CtCtCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 317,
    label = "CsJ-CtCbCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 318,
    label = "CsJ-CtCOCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 325,
    label = "CsJ-CtC=SCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 319,
    label = "CsJ-CbCbCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 320,
    label = "CsJ-CbCOCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 326,
    label = "CsJ-CbC=SCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 321,
    label = "CsJ-COCOCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 327,
    label = "CsJ-COC=SCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 330,
    label = "CsJ-C=SC=SCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 331,
    label = "CsJ-TwoDeOs",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    O2s               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 332,
    label = "CsJ-TwoDeSs",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    S2s               u0 p2 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 333,
    label = "CsJ-ThreeDe",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 230,
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
    index = 231,
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
    index = 232,
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
    index = 238,
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
    index = 233,
    label = "CdsJ-Ct",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D}
3    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 234,
    label = "CdsJ-Cb",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D}
3    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 235,
    label = "CdsJ-CO",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D}
3    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 239,
    label = "CdsJ-C=S",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D}
3    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 236,
    label = "CdsJ-O2s",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D}
3    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 237,
    label = "CdsJ-S2s",
    group = 
"""
1 *3 C   u1 {2,D} {3,S}
2    C   u0 {1,D}
3    S2s u0 p2 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 229,
    label = "CtJ",
    group = 
"""
1 *3 Ct u1 {2,T}
2    C  u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 228,
    label = "CbJ",
    group = 
"""
1 *3 Cb u1
""",
    kinetics = None,
)

entry(
    index = 240,
    label = "C=SJ",
    group = 
"""
1 *3 CS u1 {2,S}
2    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 241,
    label = "C=SJ-H",
    group = 
"""
1 *3 CS u1 {2,S}
2    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 242,
    label = "C=SJ-Cs",
    group = 
"""
1 *3 CS u1 {2,S}
2    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 248,
    label = "C=SJ-Cd",
    group = 
"""
1 *3 CS u1 {2,S}
2    Cd u0 {1,S} {3,D}
3    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 243,
    label = "C=SJ-Ct",
    group = 
"""
1 *3 CS u1 {2,S}
2    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 244,
    label = "C=SJ-Cb",
    group = 
"""
1 *3 CS u1 {2,S}
2    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 245,
    label = "C=SJ-CO",
    group = 
"""
1 *3 CS u1 {2,S}
2    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 249,
    label = "C=SJ-C=S",
    group = 
"""
1 *3 CS u1 {2,S}
2    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 246,
    label = "C=SJ-O2s",
    group = 
"""
1 *3 CS u1 {2,S}
2    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 247,
    label = "C=SJ-S2s",
    group = 
"""
1 *3 CS  u1 {2,S}
2    S2s u0 p2 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 250,
    label = "CO_rad",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    O u0 {1,D}
3    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 251,
    label = "CO_pri_rad",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    O u0 {1,D}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 252,
    label = "CO_sec_rad",
    group = 
"""
1 *3 C   u1 {2,D} {3,S}
2    O   u0 {1,D}
3    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 253,
    label = "CO_rad/NonDe",
    group = 
"""
1 *3 C          u1 {2,D} {3,S}
2    O          u0 {1,D}
3    [Cs,O,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 254,
    label = "CO_rad/OneDe",
    group = 
"""
1 *3 C                u1 {2,D} {3,S}
2    O                u0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 340,
    label = "O_rad",
    group = 
"""
1 *3 O u1 {2,S}
2    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 341,
    label = "O_pri_rad",
    group = 
"""
1 *3 O u1 {2,S}
2    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 342,
    label = "O_sec_rad",
    group = 
"""
1 *3 O   u1 {2,S}
2    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 343,
    label = "O_rad/NonDeC",
    group = 
"""
1 *3 O  u1 {2,S}
2    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 344,
    label = "O_rad/NonDeO",
    group = 
"""
1 *3 O u1 {2,S}
2    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 345,
    label = "O_rad/OneDe",
    group = 
"""
1 *3 O                u1 {2,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 346,
    label = "SJ",
    group = 
"""
1 *3 S u1
""",
    kinetics = None,
)

entry(
    index = 347,
    label = "SsJ",
    group = 
"""
1 *3 S2s u1 {2,S}
2    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 348,
    label = "SsJ-H",
    group = 
"""
1 *3 S2s u1 {2,S}
2    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 349,
    label = "SsJ-Cs",
    group = 
"""
1 *3 S2s u1 {2,S}
2    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 350,
    label = "SsJ-S2s",
    group = 
"""
1 *3 S2s u1 {2,S}
2    S2s u0 p2 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 351,
    label = "SsJ-OneDe",
    group = 
"""
1 *3 S2s              u1 {2,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 355,
    label = "SsJ-Cd",
    group = 
"""
1 *3 S2s u1 {2,S}
2    Cd  u0 {1,S} {3,D}
3    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 352,
    label = "SsJ-Ct",
    group = 
"""
1 *3 S2s u1 {2,S}
2    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 353,
    label = "SsJ-Cb",
    group = 
"""
1 *3 S2s u1 {2,S}
2    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 354,
    label = "SsJ-CO",
    group = 
"""
1 *3 S2s u1 {2,S}
2    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 356,
    label = "SsJ-C=S",
    group = 
"""
1 *3 S2s u1 {2,S}
2    CS  u0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: S-RR_or_RRrad
    L2: S-RR
        L3: S-HH
        L3: S-CH
            L4: S-CsH
                L5: S-Cs(NonDe)H
                    L6: S-Cs(HHH)H
                    L6: S-Cs(CsHH)H
                    L6: S-Cs(CsCsH)H
                    L6: S-Cs(CsCsCs)H
                L5: S-Cs(OneDe)H
                    L6: S-Cs(CdHH)H
                    L6: S-Cs(CdCsH)H
                    L6: S-Cs(CdCsCs)H
                    L6: S-Cs(CtHH)H
                    L6: S-Cs(CtCsH)H
                    L6: S-Cs(CtCsCs)H
                L5: S-Cs(TwoDe)H
                L5: S-Cs(ThreeDe)H
            L4: S-CdH
                L5: S-Cds(H)H
                L5: S-Cds(Cs)H
            L4: S-CtH
            L4: S-CbH
            L4: S-COH
            L4: S-CSH
        L3: S-HC
            L4: S-HCs
                L5: S-HCs(NonDe)
                    L6: S-HCs(HHH)
                    L6: S-HCs(CsHH)
                    L6: S-HCs(CsCsH)
                    L6: S-HCs(CsCsCs)
                    L6: S-HCs(CsOsH)
                    L6: S-HCs(CsSH)
                L5: S-HCs(OneDe)
                    L6: S-HCs(CdHH)
                    L6: S-HCs(CdCsH)
                    L6: S-HCs(CdCsCs)
                    L6: S-HCs(CtHH)
                    L6: S-HCs(CtCsH)
                    L6: S-HCs(CtCsCs)
                L5: S-HCs(TwoDe)
                L5: S-HCs(ThreeDe)
            L4: S-HCd
                L5: S-HCds(H)
                L5: S-HCds(Cs)
            L4: S-HCt
            L4: S-HCb
            L4: S-HCO
                L5: S-HCO(H)
            L4: S-HCS
        L3: S-CC
            L4: S-CsCs
                L5: S-Cs(NonDe)Cs(NonDe)
                    L6: S-Cs(HHH)Cs(HHH)
                    L6: S-Cs(HHH)Cs(CsHH)
                    L6: S-Cs(CsHH)Cs(HHH)
                    L6: S-Cs(HHH)Cs(CsCsH)
                    L6: S-Cs(CsCsH)Cs(HHH)
                    L6: S-Cs(HHH)Cs(CsCsCs)
                    L6: S-Cs(CsCsCs)Cs(HHH)
                    L6: S-Cs(CsHH)Cs(CsHH)
                    L6: S-Cs(CsHH)Cs(CsCsH)
                    L6: S-Cs(CsCsH)Cs(CsHH)
                    L6: S-Cs(CsHH)Cs(CsCsCs)
                    L6: S-Cs(CsCsCs)Cs(CsHH)
                    L6: S-Cs(CsCsH)Cs(CsCsH)
                    L6: S-Cs(CsCsH)Cs(CsCsCs)
                    L6: S-Cs(CsCsCs)Cs(CsCsH)
                    L6: S-Cs(CsCsCs)Cs(CsCsCs)
                L5: S-Cs(NonDe)Cs(De)
                    L6: S-Cs(NonDe)Cs(OneDe)
                        L7: S-Cs(HHH)Cs(CdHH)
                        L7: S-Cs(HHH)Cs(CdCsH)
                        L7: S-Cs(HHH)Cs(CdCsCs)
                        L7: S-Cs(HHH)Cs(CtHH)
                        L7: S-Cs(HHH)Cs(CtCsH)
                        L7: S-Cs(HHH)Cs(CtCsCs)
                    L6: S-Cs(NonDe)Cs(TwoDe)
                    L6: S-Cs(NonDe)Cs(ThreeDe)
                L5: S-Cs(De)Cs(NonDe)
                    L6: S-Cs(OneDe)Cs(NonDe)
                        L7: S-Cs(CdHH)Cs(HHH)
                        L7: S-Cs(CdCsH)Cs(HHH)
                        L7: S-Cs(CdCsCs)Cs(HHH)
                        L7: S-Cs(CtHH)Cs(HHH)
                        L7: S-Cs(CtCsH)Cs(HHH)
                        L7: S-Cs(CtCsCs)Cs(HHH)
                    L6: S-Cs(TwoDe)Cs(NonDe)
                    L6: S-Cs(ThreeDe)Cs(NonDe)
            L4: S-CsCd
                L5: S-Cs(HHH)Cds(H)
                L5: S-Cs(CsHH)Cds(H)
                L5: S-Cs(CsCsH)Cds(H)
                L5: S-Cs(CsCsCs)Cds(H)
                L5: S-Cs(HHH)Cds(Cs)
                L5: S-Cs(CsHH)Cds(Cs)
                L5: S-Cs(CsCsH)Cds(Cs)
                L5: S-Cs(CsCsCs)Cds(Cs)
            L4: S-CdCs
                L5: S-Cds(H)Cs(HHH)
                L5: S-Cds(H)Cs(CsHH)
                L5: S-Cds(H)Cs(CsCsH)
                L5: S-Cds(H)Cs(CsCsCs)
                L5: S-Cds(Cs)Cs(HHH)
                L5: S-Cds(Cs)Cs(CsHH)
                L5: S-Cds(Cs)Cs(CsCsH)
                L5: S-Cds(Cs)Cs(CsCsCs)
            L4: S-CsCt
                L5: S-Cs(HHH)Ct
                L5: S-Cs(CsHH)Ct
                L5: S-Cs(CsCsH)Ct
                L5: S-Cs(CsCsCs)Ct
            L4: S-CtCs
                L5: S-CtCs(HHH)
                L5: S-CtCs(CsHH)
                L5: S-CtCs(CsCsH)
                L5: S-CtCs(CsCsCs)
            L4: S-CsCb
                L5: S-Cs(HHH)Cb
                L5: S-Cs(CsHH)Cb
                L5: S-Cs(CsCsH)Cb
                L5: S-Cs(CsCsCs)Cb
            L4: S-CbCs
                L5: S-CbCs(HHH)
                L5: S-CbCs(CsHH)
                L5: S-CbCs(CsCsH)
                L5: S-CbCs(CsCsCs)
            L4: S-CsCO
            L4: S-COCs
            L4: S-CsC=S
            L4: S-C=SCs
            L4: S-CdCd
            L4: S-CdCt
            L4: S-CtCd
            L4: S-CdCb
            L4: S-CbCd
            L4: S-CdCO
            L4: S-COCd
            L4: S-CdC=S
            L4: S-C=SCd
            L4: S-CtCt
            L4: S-CtCb
            L4: S-CbCt
            L4: S-CtCO
            L4: S-COCt
            L4: S-CtC=S
            L4: S-C=SCt
            L4: S-CbCb
            L4: S-CbCO
            L4: S-COCb
            L4: S-CbC=S
            L4: S-C=SCb
            L4: S-COCO
            L4: S-COC=S
            L4: S-C=SCO
            L4: S-C=SC=S
        L3: S-CS
            L4: S-CsSs
                L5: S-Cs(HHH)S2s(H)
                L5: S-Cs(CsHH)S2s(H)
                L5: S-Cs(CsCsH)S2s(H)
                L5: S-Cs(CsCsCs)S2s(H)
                L5: S-Cs(HHH)S2s(Cs)
                L5: S-Cs(CsHH)S2s(Cs)
                L5: S-Cs(CsCsH)S2s(Cs)
                L5: S-Cs(CsCsCs)S2s(Cs)
                L5: S-Cs(HHH)S2s(S2s)
                L5: S-Cs(CsHH)S2s(S2s)
                L5: S-Cs(CsCsH)S2s(S2s)
                L5: S-Cs(CsCsCs)S2s(S2s)
            L4: S-CdSs
                L5: S-Cds(H)S2s(H)
                L5: S-Cds(H)S2s(Cs)
                L5: S-Cds(H)S2s(S2s)
                L5: S-Cds(Cs)S2s(H)
                L5: S-Cds(Cs)S2s(Cs)
                L5: S-Cds(Cs)S2s(S2s)
            L4: S-CtSs
            L4: S-CbSs
            L4: S-COSs
            L4: S-C=SSs
        L3: S-SC
            L4: S-SsCs
                L5: S-S2s(H)Cs(HHH)
                L5: S-S2s(H)Cs(CsHH)
                L5: S-S2s(H)Cs(CsCsH)
                L5: S-S2s(H)Cs(CsCsCs)
                L5: S-S2s(Cs)Cs(HHH)
                L5: S-S2s(Cs)Cs(CsHH)
                L5: S-S2s(Cs)Cs(CsCsH)
                L5: S-S2s(Cs)Cs(CsCsCs)
                L5: S-S2s(S2s)Cs(HHH)
                L5: S-S2s(S2s)Cs(CsHH)
                L5: S-S2s(S2s)Cs(CsCsH)
                L5: S-S2s(S2s)Cs(CsCsCs)
            L4: S-SsCd
                L5: S-S2s(H)Cds(H)
                L5: S-S2s(Cs)Cds(H)
                L5: S-S2s(S2s)Cds(H)
                L5: S-S2s(H)Cds(Cs)
                L5: S-S2s(Cs)Cds(Cs)
                L5: S-S2s(S2s)Cds(Cs)
            L4: S-SsCt
            L4: S-SsCb
            L4: S-SsCO
            L4: S-SsC=S
        L3: S-SsH
            L4: S-S2s(H)H
            L4: S-S2s(Cs)H
            L4: S-S2s(S2s)H
        L3: S-HSs
            L4: S-HSs(H)
            L4: S-HSs(Cs)
            L4: S-HSs(S2s)
        L3: S-SsSs
            L4: S-S2s(H)S2s(H)
            L4: S-S2s(Cs)S2s(H)
            L4: S-S2s(H)S2s(Cs)
            L4: S-S2s(S2s)S2s(H)
            L4: S-S2s(H)S2s(S2s)
            L4: S-S2s(Cs)S2s(Cs)
            L4: S-S2s(Cs)S2s(S2s)
            L4: S-S2s(S2s)S2s(Cs)
            L4: S-S2s(S2s)S2s(S2s)
    L2: S-RRrad
L1: YJ
    L2: Y_2centeradjbirad
        L3: S2b
        L3: O2b
        L3: C2b
    L2: Y_1centerbirad
        L3: O_atom_triplet
        L3: CH2_triplet
    L2: HJ
    L2: CJ
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
                    L6: CsJ-CdHH
                    L6: CsJ-CtHH
                    L6: CsJ-CbHH
                    L6: CsJ-COHH
                    L6: CsJ-C=SHH
                L5: CsJ-OneDeCsH
                    L6: CsJ-CdCsH
                    L6: CsJ-CtCsH
                    L6: CsJ-CbCsH
                    L6: CsJ-COCsH
                    L6: CsJ-C=SCsH
                L5: CsJ-OneDeOsH
                L5: CsJ-OneDeSsH
                L5: CsJ-OneDeCsCs
                    L6: CsJ-CdCsCs
                    L6: CsJ-CtCsCs
                    L6: CsJ-CbCsCs
                    L6: CsJ-COCsCs
                    L6: CsJ-C=SCsCs
                L5: CsJ-OneDeOsCs
                L5: CsJ-OneDeSsCs
                L5: CsJ-OneDeOsOs
                L5: CsJ-OneDeOsSs
                L5: CsJ-OneDeSsSs
            L4: CsJ-TwoDe
                L5: CsJ-TwoDeH
                    L6: CsJ-CdCdH
                    L6: CsJ-CdCtH
                    L6: CsJ-CdCbH
                    L6: CsJ-CdCOH
                    L6: CsJ-CdC=SH
                    L6: CsJ-CtCtH
                    L6: CsJ-CtCbH
                    L6: CsJ-CtCOH
                    L6: CsJ-CtC=SH
                    L6: CsJ-CbCbH
                    L6: CsJ-CbCOH
                    L6: CsJ-CbC=SH
                    L6: CsJ-COCOH
                    L6: CsJ-COC=SH
                    L6: CsJ-C=SC=SH
                L5: CsJ-TwoDeCs
                    L6: CsJ-CdCdCs
                    L6: CsJ-CdCtCs
                    L6: CsJ-CdCbCs
                    L6: CsJ-CdCOCs
                    L6: CsJ-CdC=SCs
                    L6: CsJ-CtCtCs
                    L6: CsJ-CtCbCs
                    L6: CsJ-CtCOCs
                    L6: CsJ-CtC=SCs
                    L6: CsJ-CbCbCs
                    L6: CsJ-CbCOCs
                    L6: CsJ-CbC=SCs
                    L6: CsJ-COCOCs
                    L6: CsJ-COC=SCs
                    L6: CsJ-C=SC=SCs
                L5: CsJ-TwoDeOs
                L5: CsJ-TwoDeSs
            L4: CsJ-ThreeDe
        L3: CdsJ
            L4: CdsJ-H
            L4: CdsJ-Cs
            L4: CdsJ-Cd
            L4: CdsJ-Ct
            L4: CdsJ-Cb
            L4: CdsJ-CO
            L4: CdsJ-C=S
            L4: CdsJ-O2s
            L4: CdsJ-S2s
        L3: CtJ
        L3: CbJ
        L3: C=SJ
            L4: C=SJ-H
            L4: C=SJ-Cs
            L4: C=SJ-Cd
            L4: C=SJ-Ct
            L4: C=SJ-Cb
            L4: C=SJ-CO
            L4: C=SJ-C=S
            L4: C=SJ-O2s
            L4: C=SJ-S2s
        L3: CO_rad
            L4: CO_pri_rad
            L4: CO_sec_rad
                L5: CO_rad/NonDe
                L5: CO_rad/OneDe
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
            L4: SsJ-S2s
            L4: SsJ-OneDe
                L5: SsJ-Cd
                L5: SsJ-Ct
                L5: SsJ-Cb
                L5: SsJ-CO
                L5: SsJ-C=S
"""
)

