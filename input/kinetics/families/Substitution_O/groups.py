#!/usr/bin/env python
# encoding: utf-8

name = "Substitution_O/groups"
shortDesc = u""
longDesc = u"""
If a birad, the reacting site *3 must be a triplet instead of singlet for this reaction family.
"""

template(reactants=["O-RR_or_RRrad", "YJ"], products=["O-RR_or_RRrad", "YJ"], ownReverse=True)

reversible = True

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 0,
    label = "O-RR_or_RRrad",
    group = """
1 *1 O2s u0 {2,S} {3,S}
2 *2 R   u[0,1] {1,S}
3    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "YJ",
    group = """
1 *3 [H,C,O2s,N,S] u[1,2]
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "O-RR",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 R   u0 {1,S}
3    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "O-HH",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "O-CH",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "O-CsH",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "O-Cs(NonDe)H",
    group = 
"""
1    Cs     u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s    u0 {1,S} {6,S}
3    [H,Cs] u0 {1,S}
4    [H,Cs] u0 {1,S}
5    [H,Cs] u0 {1,S}
6 *2 H      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "O-Cs(HHH)H",
    group = 
"""
1    Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s u0 {1,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6 *2 H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "O-Cs(CsHH)H",
    group = 
"""
1    Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s u0 {1,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6 *2 H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "O-Cs(CsCsH)H",
    group = 
"""
1    Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s u0 {1,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    H   u0 {1,S}
6 *2 H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "O-Cs(CsCsCs)H",
    group = 
"""
1    Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s u0 {1,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    Cs  u0 {1,S}
6 *2 H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "O-Cs(OneDe)H",
    group = 
"""
1    Cs               u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s              u0 {1,S} {6,S}
3    [H,Cs]           u0 {1,S}
4    [H,Cs]           u0 {1,S}
5    [Cd,CO,CS,Ct,Cb] u0 {1,S}
6 *2 H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "O-Cs(CdHH)H",
    group = 
"""
1    Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s u0 {1,S} {6,S}
3    Cd  u0 {1,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6 *2 H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "O-Cs(CdCsH)H",
    group = 
"""
1    Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s u0 {1,S} {6,S}
3    Cd  u0 {1,S}
4    Cs  u0 {1,S}
5    H   u0 {1,S}
6 *2 H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "O-Cs(CdCsCs)H",
    group = 
"""
1    Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s u0 {1,S} {6,S}
3    Cd  u0 {1,S}
4    Cs  u0 {1,S}
5    Cs  u0 {1,S}
6 *2 H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "O-Cs(CtHH)H",
    group = 
"""
1    Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s u0 {1,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6 *2 H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "O-Cs(CtCsH)H",
    group = 
"""
1    Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s u0 {1,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    H   u0 {1,S}
6 *2 H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "O-Cs(CtCsCs)H",
    group = 
"""
1    Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s u0 {1,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    Cs  u0 {1,S}
6 *2 H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "O-Cs(TwoDe)H",
    group = 
"""
1    Cs               u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s              u0 {1,S} {6,S}
3    [H,Cs]           u0 {1,S}
4    [Cd,CO,CS,Ct,Cb] u0 {1,S}
5    [Cd,CO,CS,Ct,Cb] u0 {1,S}
6 *2 H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "O-Cs(ThreeDe)H",
    group = 
"""
1    Cs               u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s              u0 {1,S} {6,S}
3    [Cd,CO,CS,Ct,Cb] u0 {1,S}
4    [Cd,CO,CS,Ct,Cb] u0 {1,S}
5    [Cd,CO,CS,Ct,Cb] u0 {1,S}
6 *2 H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "O-CtH",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "O-CbH",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "O-COH",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "O-CSH",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "O-CdH",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    Cd  u0 {1,S} {4,D}
3 *2 H   u0 {1,S}
4    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "O-Cds(H)H",
    group = 
"""
1    Cd  u0 {2,S} {3,D} {4,S}
2 *1 O2s u0 {1,S} {5,S}
3    C   u0 {1,D}
4    H   u0 {1,S}
5 *2 H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "O-Cds(Cs)H",
    group = 
"""
1    Cd  u0 {2,S} {3,D} {4,S}
2 *1 O2s u0 {1,S} {5,S}
3    C   u0 {1,D}
4    Cs  u0 {1,S}
5 *2 H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "O-HC",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "O-HCs",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "O-HCs(NonDe)",
    group = 
"""
1 *2 Cs     u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s    u0 {1,S} {6,S}
3    [H,Cs] u0 {1,S}
4    [H,Cs] u0 {1,S}
5    [H,Cs] u0 {1,S}
6    H      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "O-HCs(HHH)",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s u0 {1,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "O-HCs(CsHH)",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s u0 {1,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "O-HCs(CsCsH)",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s u0 {1,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "O-HCs(CsCsCs)",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s u0 {1,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    Cs  u0 {1,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "O-HCs(OneDe)",
    group = 
"""
1 *2 Cs               u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s              u0 {1,S} {6,S}
3    [H,Cs]           u0 {1,S}
4    [H,Cs]           u0 {1,S}
5    [Cd,CO,CS,Ct,Cb] u0 {1,S}
6    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "O-HCs(CdHH)",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s u0 {1,S} {6,S}
3    Cd  u0 {1,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "O-HCs(CdCsH)",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s u0 {1,S} {6,S}
3    Cd  u0 {1,S}
4    Cs  u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "O-HCs(CdCsCs)",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s u0 {1,S} {6,S}
3    Cd  u0 {1,S}
4    Cs  u0 {1,S}
5    Cs  u0 {1,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "O-HCs(CtHH)",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s u0 {1,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "O-HCs(CtCsH)",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s u0 {1,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "O-HCs(CtCsCs)",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s u0 {1,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    Cs  u0 {1,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "O-HCs(TwoDe)",
    group = 
"""
1 *2 Cs               u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s              u0 {1,S} {6,S}
3    [H,Cs]           u0 {1,S}
4    [Cd,CO,CS,Ct,Cb] u0 {1,S}
5    [Cd,CO,CS,Ct,Cb] u0 {1,S}
6    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "O-HCs(ThreeDe)",
    group = 
"""
1 *2 Cs               u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s              u0 {1,S} {6,S}
3    [Cd,CO,CS,Ct,Cb] u0 {1,S}
4    [Cd,CO,CS,Ct,Cb] u0 {1,S}
5    [Cd,CO,CS,Ct,Cb] u0 {1,S}
6    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "O-HCt",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "O-HCb",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "O-HCO",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "O-HCS",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "O-HCd",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Cd  u0 {1,S} {4,D}
3    H   u0 {1,S}
4    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "O-HCds(H)",
    group = 
"""
1 *2 Cd  u0 {2,S} {3,D} {4,S}
2 *1 O2s u0 {1,S} {5,S}
3    C   u0 {1,D}
4    H   u0 {1,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "O-HCds(Cs)",
    group = 
"""
1 *2 Cd  u0 {2,S} {3,D} {4,S}
2 *1 O2s u0 {1,S} {5,S}
3    C   u0 {1,D}
4    Cs  u0 {1,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "O-CC",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 C   u0 {1,S}
3    C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "O-CsCs",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Cs  u0 {1,S}
3    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "O-Cs(NonDe)Cs(NonDe)",
    group = 
"""
1 *2 Cs     u0 {3,S} {4,S} {5,S} {6,S}
2    Cs     u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s    u0 {1,S} {2,S}
4    [H,Cs] u0 {1,S}
5    [H,Cs] u0 {1,S}
6    [H,Cs] u0 {1,S}
7    [H,Cs] u0 {2,S}
8    [H,Cs] u0 {2,S}
9    [H,Cs] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "O-Cs(HHH)Cs(HHH)",
    group = 
"""
1 *2 Cs  u0 {3,S} {4,S} {5,S} {6,S}
2    Cs  u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s u0 {1,S} {2,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    H   u0 {2,S}
8    H   u0 {2,S}
9    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "O-Cs(HHH)Cs(CsHH)",
    group = 
"""
1 *2 Cs  u0 {3,S} {4,S} {5,S} {6,S}
2    Cs  u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s u0 {1,S} {2,S}
4    Cs  u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    H   u0 {2,S}
8    H   u0 {2,S}
9    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "O-Cs(CsHH)Cs(HHH)",
    group = 
"""
1    Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cs  u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s u0 {1,S} {2,S}
4    Cs  u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    H   u0 {2,S}
8    H   u0 {2,S}
9    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "O-Cs(HHH)Cs(CsCsH)",
    group = 
"""
1 *2 Cs  u0 {3,S} {4,S} {5,S} {6,S}
2    Cs  u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s u0 {1,S} {2,S}
4    Cs  u0 {1,S}
5    Cs  u0 {1,S}
6    H   u0 {1,S}
7    H   u0 {2,S}
8    H   u0 {2,S}
9    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "O-Cs(CsCsH)Cs(HHH)",
    group = 
"""
1    Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cs  u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s u0 {1,S} {2,S}
4    Cs  u0 {1,S}
5    Cs  u0 {1,S}
6    H   u0 {1,S}
7    H   u0 {2,S}
8    H   u0 {2,S}
9    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "O-Cs(HHH)Cs(CsCsCs)",
    group = 
"""
1 *2 Cs  u0 {3,S} {4,S} {5,S} {6,S}
2    Cs  u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s u0 {1,S} {2,S}
4    Cs  u0 {1,S}
5    Cs  u0 {1,S}
6    Cs  u0 {1,S}
7    H   u0 {2,S}
8    H   u0 {2,S}
9    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "O-Cs(CsCsCs)Cs(HHH)",
    group = 
"""
1    Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cs  u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s u0 {1,S} {2,S}
4    Cs  u0 {1,S}
5    Cs  u0 {1,S}
6    Cs  u0 {1,S}
7    H   u0 {2,S}
8    H   u0 {2,S}
9    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "O-Cs(CsHH)Cs(CsHH)",
    group = 
"""
1 *2 Cs  u0 {3,S} {4,S} {5,S} {6,S}
2    Cs  u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s u0 {1,S} {2,S}
4    Cs  u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    Cs  u0 {2,S}
8    H   u0 {2,S}
9    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "O-Cs(CsHH)Cs(CsCsH)",
    group = 
"""
1 *2 Cs  u0 {3,S} {4,S} {5,S} {6,S}
2    Cs  u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s u0 {1,S} {2,S}
4    Cs  u0 {1,S}
5    Cs  u0 {1,S}
6    H   u0 {1,S}
7    Cs  u0 {2,S}
8    H   u0 {2,S}
9    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "O-Cs(CsCsH)Cs(CsHH)",
    group = 
"""
1    Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cs  u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s u0 {1,S} {2,S}
4    Cs  u0 {1,S}
5    Cs  u0 {1,S}
6    H   u0 {1,S}
7    Cs  u0 {2,S}
8    H   u0 {2,S}
9    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "O-Cs(CsHH)Cs(CsCsCs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
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
    index = 64,
    label = "O-Cs(CsCsCs)Cs(CsHH)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
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
    index = 65,
    label = "O-Cs(CsCsH)Cs(CsCsH)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
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
    index = 66,
    label = "O-Cs(CsCsH)Cs(CsCsCs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
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
    index = 67,
    label = "O-Cs(CsCsCs)Cs(CsCsH)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
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
    index = 68,
    label = "O-Cs(CsCsCs)Cs(CsCsCs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
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
    index = 69,
    label = "O-Cs(NonDe)Cs(De)",
    group = 
"""
1    Cs               u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cs               u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s              u0 {1,S} {2,S}
4    [H,Cs]           u0 {1,S}
5    [H,Cs]           u0 {1,S}
6    [H,Cs]           u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {2,S}
8    R                u0 {2,S}
9    R                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "O-Cs(NonDe)Cs(OneDe)",
    group = 
"""
1    Cs               u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cs               u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s              u0 {1,S} {2,S}
4    [H,Cs]           u0 {1,S}
5    [H,Cs]           u0 {1,S}
6    [H,Cs]           u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {2,S}
8    [H,Cs]           u0 {2,S}
9    [H,Cs]           u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "O-Cs(HHH)Cs(CdHH)",
    group = 
"""
1    Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cs  u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s u0 {1,S} {2,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    Cd  u0 {2,S}
8    H   u0 {2,S}
9    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "O-Cs(HHH)Cs(CdCsH)",
    group = 
"""
1    Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cs  u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s u0 {1,S} {2,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    Cd  u0 {2,S}
8    Cs  u0 {2,S}
9    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "O-Cs(HHH)Cs(CdCsCs)",
    group = 
"""
1    Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cs  u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s u0 {1,S} {2,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    Cd  u0 {2,S}
8    Cs  u0 {2,S}
9    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "O-Cs(HHH)Cs(CtHH)",
    group = 
"""
1    Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cs  u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s u0 {1,S} {2,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    Ct  u0 {2,S}
8    H   u0 {2,S}
9    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "O-Cs(HHH)Cs(CtCsH)",
    group = 
"""
1    Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cs  u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s u0 {1,S} {2,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    Ct  u0 {2,S}
8    Cs  u0 {2,S}
9    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "O-Cs(HHH)Cs(CtCsCs)",
    group = 
"""
1    Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cs  u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s u0 {1,S} {2,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    Ct  u0 {2,S}
8    Cs  u0 {2,S}
9    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 77,
    label = "O-Cs(NonDe)Cs(TwoDe)",
    group = 
"""
1    Cs               u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cs               u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s              u0 {1,S} {2,S}
4    [H,Cs]           u0 {1,S}
5    [H,Cs]           u0 {1,S}
6    [H,Cs]           u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {2,S}
8    [Cd,Ct,Cb,CO,CS] u0 {2,S}
9    [H,Cs]           u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "O-Cs(NonDe)Cs(ThreeDe)",
    group = 
"""
1    Cs               u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cs               u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s              u0 {1,S} {2,S}
4    [H,Cs]           u0 {1,S}
5    [H,Cs]           u0 {1,S}
6    [H,Cs]           u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {2,S}
8    [Cd,Ct,Cb,CO,CS] u0 {2,S}
9    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "O-Cs(De)Cs(NonDe)",
    group = 
"""
1 *2 Cs               u0 {3,S} {4,S} {5,S} {6,S}
2    Cs               u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s              u0 {1,S} {2,S}
4    [H,Cs]           u0 {1,S}
5    [H,Cs]           u0 {1,S}
6    [H,Cs]           u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {2,S}
8    R                u0 {2,S}
9    R                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "O-Cs(OneDe)Cs(NonDe)",
    group = 
"""
1 *2 Cs               u0 {3,S} {4,S} {5,S} {6,S}
2    Cs               u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s              u0 {1,S} {2,S}
4    [H,Cs]           u0 {1,S}
5    [H,Cs]           u0 {1,S}
6    [H,Cs]           u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {2,S}
8    [H,Cs]           u0 {2,S}
9    [H,Cs]           u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "O-Cs(CdHH)Cs(HHH)",
    group = 
"""
1 *2 Cs  u0 {3,S} {4,S} {5,S} {6,S}
2    Cs  u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s u0 {1,S} {2,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    Cd  u0 {2,S}
8    H   u0 {2,S}
9    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 82,
    label = "O-Cs(CdCsH)Cs(HHH)",
    group = 
"""
1 *2 Cs  u0 {3,S} {4,S} {5,S} {6,S}
2    Cs  u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s u0 {1,S} {2,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    Cd  u0 {2,S}
8    Cs  u0 {2,S}
9    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 83,
    label = "O-Cs(CdCsCs)Cs(HHH)",
    group = 
"""
1 *2 Cs  u0 {3,S} {4,S} {5,S} {6,S}
2    Cs  u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s u0 {1,S} {2,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    Cd  u0 {2,S}
8    Cs  u0 {2,S}
9    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 84,
    label = "O-Cs(CtHH)Cs(HHH)",
    group = 
"""
1 *2 Cs  u0 {3,S} {4,S} {5,S} {6,S}
2    Cs  u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s u0 {1,S} {2,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    Ct  u0 {2,S}
8    H   u0 {2,S}
9    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 85,
    label = "O-Cs(CtCsH)Cs(HHH)",
    group = 
"""
1 *2 Cs  u0 {3,S} {4,S} {5,S} {6,S}
2    Cs  u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s u0 {1,S} {2,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    Ct  u0 {2,S}
8    Cs  u0 {2,S}
9    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 86,
    label = "O-Cs(CtCsCs)Cs(HHH)",
    group = 
"""
1 *2 Cs  u0 {3,S} {4,S} {5,S} {6,S}
2    Cs  u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s u0 {1,S} {2,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    Ct  u0 {2,S}
8    Cs  u0 {2,S}
9    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 87,
    label = "O-Cs(TwoDe)Cs(NonDe)",
    group = 
"""
1 *2 Cs               u0 {3,S} {4,S} {5,S} {6,S}
2    Cs               u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s              u0 {1,S} {2,S}
4    [H,Cs]           u0 {1,S}
5    [H,Cs]           u0 {1,S}
6    [H,Cs]           u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {2,S}
8    [Cd,Ct,Cb,CO,CS] u0 {2,S}
9    [H,Cs]           u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 88,
    label = "O-Cs(ThreeDe)Cs(NonDe)",
    group = 
"""
1 *2 Cs               u0 {3,S} {4,S} {5,S} {6,S}
2    Cs               u0 {3,S} {7,S} {8,S} {9,S}
3 *1 O2s              u0 {1,S} {2,S}
4    [H,Cs]           u0 {1,S}
5    [H,Cs]           u0 {1,S}
6    [H,Cs]           u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {2,S}
8    [Cd,Ct,Cb,CO,CS] u0 {2,S}
9    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 89,
    label = "O-CsCt",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Ct  u0 {1,S}
3    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 90,
    label = "O-Cs(HHH)Ct",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Ct  u0 {1,S}
3    Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    H   u0 {3,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 91,
    label = "O-Cs(CsHH)Ct",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Ct  u0 {1,S}
3    Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 92,
    label = "O-Cs(CsCsH)Ct",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Ct  u0 {1,S}
3    Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    Cs  u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 93,
    label = "O-Cs(CsCsCs)Ct",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Ct  u0 {1,S}
3    Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 94,
    label = "O-CtCs",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    Ct  u0 {1,S}
3 *2 Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 95,
    label = "O-CtCs(HHH)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    Ct  u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    H   u0 {3,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 96,
    label = "O-CtCs(CsHH)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    Ct  u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 97,
    label = "O-CtCs(CsCsH)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    Ct  u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    Cs  u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 98,
    label = "O-CtCs(CsCsCs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    Ct  u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 99,
    label = "O-CsCb",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Cb  u0 {1,S}
3    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 100,
    label = "O-Cs(HHH)Cb",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Cb  u0 {1,S}
3    Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    H   u0 {3,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 101,
    label = "O-Cs(CsHH)Cb",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Cb  u0 {1,S}
3    Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 102,
    label = "O-Cs(CsCsH)Cb",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Cb  u0 {1,S}
3    Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    Cs  u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 103,
    label = "O-Cs(CsCsCs)Cb",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Cb  u0 {1,S}
3    Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 104,
    label = "O-CbCs",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    Cb  u0 {1,S}
3 *2 Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 105,
    label = "O-CbCs(HHH)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    Cb  u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    H   u0 {3,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 106,
    label = "O-CbCs(CsHH)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    Cb  u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 107,
    label = "O-CbCs(CsCsH)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    Cb  u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    Cs  u0 {3,S}
6    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 108,
    label = "O-CbCs(CsCsCs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    Cb  u0 {1,S}
3 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
4    Cs  u0 {3,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 109,
    label = "O-CsCO",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 CO  u0 {1,S}
3    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 110,
    label = "O-CsCS",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 CS  u0 {1,S}
3    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 111,
    label = "O-COCs",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    CO  u0 {1,S}
3 *2 Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 112,
    label = "O-CSCs",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    CS  u0 {1,S}
3 *2 Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 113,
    label = "O-CtCt",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Ct  u0 {1,S}
3    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 114,
    label = "O-CtCb",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Cb  u0 {1,S}
3    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 115,
    label = "O-CbCt",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    Cb  u0 {1,S}
3 *2 Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 116,
    label = "O-CtCO",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 CO  u0 {1,S}
3    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 117,
    label = "O-CtCS",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 CS  u0 {1,S}
3    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 118,
    label = "O-COCt",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    CO  u0 {1,S}
3 *2 Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 119,
    label = "O-CSCt",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    CS  u0 {1,S}
3 *2 Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 120,
    label = "O-CbCb",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Cb  u0 {1,S}
3    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 121,
    label = "O-CbCO",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 CO  u0 {1,S}
3    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 122,
    label = "O-CbCS",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 CS  u0 {1,S}
3    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 123,
    label = "O-COCb",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    CO  u0 {1,S}
3 *2 Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 124,
    label = "O-CSCb",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    CS  u0 {1,S}
3 *2 Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 125,
    label = "O-COCO",
    group = 
"""
1 *1 O2s     u0 {2,S} {3,S}
2 *2 CO      u0 {1,S}
3    [CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 126,
    label = "O-CSCS",
    group = 
"""
1 *1 O2s     u0 {2,S} {3,S}
2 *2 CS      u0 {1,S}
3    [CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 127,
    label = "O-CsCd",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Cd  u0 {1,S} {4,D}
3    Cs  u0 {1,S}
4    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 128,
    label = "O-Cs(HHH)Cds(H)",
    group = 
"""
1    Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cd  u0 {3,S} {7,D} {8,S}
3 *1 O2s u0 {1,S} {2,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    C   u0 {2,D}
8    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 129,
    label = "O-Cs(CsHH)Cds(H)",
    group = 
"""
1    Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cd  u0 {3,S} {7,D} {8,S}
3 *1 O2s u0 {1,S} {2,S}
4    Cs  u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    C   u0 {2,D}
8    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 130,
    label = "O-Cs(CsCsH)Cds(H)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
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
    index = 131,
    label = "O-Cs(CsCsCs)Cds(H)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
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
    index = 132,
    label = "O-Cs(HHH)Cds(Cs)",
    group = 
"""
1    Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cd  u0 {3,S} {7,D} {8,S}
3 *1 O2s u0 {1,S} {2,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    C   u0 {2,D}
8    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 133,
    label = "O-Cs(CsHH)Cds(Cs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
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
    index = 134,
    label = "O-Cs(CsCsH)Cds(Cs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
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
    index = 135,
    label = "O-Cs(CsCsCs)Cds(Cs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
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
    index = 136,
    label = "O-CdCs",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    Cd  u0 {1,S} {4,D}
3 *2 Cs  u0 {1,S}
4    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 137,
    label = "O-Cds(H)Cs(HHH)",
    group = 
"""
1 *2 Cs  u0 {3,S} {4,S} {5,S} {6,S}
2    Cd  u0 {3,S} {7,D} {8,S}
3 *1 O2s u0 {1,S} {2,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    C   u0 {2,D}
8    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 138,
    label = "O-Cds(H)Cs(CsHH)",
    group = 
"""
1 *2 Cs  u0 {3,S} {4,S} {5,S} {6,S}
2    Cd  u0 {3,S} {7,D} {8,S}
3 *1 O2s u0 {1,S} {2,S}
4    Cs  u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    C   u0 {2,D}
8    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 139,
    label = "O-Cds(H)Cs(CsCsH)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
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
    index = 140,
    label = "O-Cds(H)Cs(CsCsCs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
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
    index = 141,
    label = "O-Cds(Cs)Cs(HHH)",
    group = 
"""
1 *2 Cs  u0 {3,S} {4,S} {5,S} {6,S}
2    Cd  u0 {3,S} {7,D} {8,S}
3 *1 O2s u0 {1,S} {2,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    C   u0 {2,D}
8    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 142,
    label = "O-Cds(Cs)Cs(CsHH)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
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
    index = 143,
    label = "O-Cds(Cs)Cs(CsCsH)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
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
    index = 144,
    label = "O-Cds(Cs)Cs(CsCsCs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
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
    index = 145,
    label = "O-CdCt",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Ct  u0 {1,S}
3    Cd  u0 {1,S} {4,D}
4    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 146,
    label = "O-CtCd",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Cd  u0 {1,S} {4,D}
3    Ct  u0 {1,S}
4    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 147,
    label = "O-CdCb",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Cb  u0 {1,S}
3    Cd  u0 {1,S} {4,D}
4    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 148,
    label = "O-CbCd",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Cd  u0 {1,S} {4,D}
3    Cb  u0 {1,S}
4    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 149,
    label = "O-CdCO",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 CO  u0 {1,S}
3    Cd  u0 {1,S} {4,D}
4    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 150,
    label = "O-CdCS",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 CS  u0 {1,S}
3    Cd  u0 {1,S} {4,D}
4    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 151,
    label = "O-COCd",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Cd  u0 {1,S} {4,D}
3    CO  u0 {1,S}
4    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 152,
    label = "O-CSCd",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Cd  u0 {1,S} {4,D}
3    CS  u0 {1,S}
4    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 153,
    label = "O-CdCd",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {4,D}
4    C   u0 {3,D}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 154,
    label = "O-CS",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O   u0 {1,S}
3    C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 155,
    label = "O-COss",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S}
3    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 156,
    label = "O-Cs(HHH)O2s(H)",
    group = 
"""
1    Cs  u0 {2,S} {4,S} {5,S} {6,S}
2 *1 O2s u0 {1,S} {3,S}
3 *2 O2s u0 {2,S} {7,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 157,
    label = "O-Cs(CsHH)O2s(H)",
    group = 
"""
1    Cs  u0 {2,S} {4,S} {5,S} {6,S}
2 *1 O2s u0 {1,S} {3,S}
3 *2 O2s u0 {2,S} {7,S}
4    Cs  u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 158,
    label = "O-Cs(CsCsH)O2s(H)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S} {4,S}
3    Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    H   u0 {2,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 159,
    label = "O-Cs(CsCsCs)O2s(H)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S} {4,S}
3    Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    H   u0 {2,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
7    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 160,
    label = "O-Cs(HHH)O2s(Cs)",
    group = 
"""
1    Cs  u0 {2,S} {4,S} {5,S} {6,S}
2 *1 O2s u0 {1,S} {3,S}
3 *2 O2s u0 {2,S} {7,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 161,
    label = "O-Cs(CsHH)O2s(Cs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S} {4,S}
3    Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    Cs  u0 {2,S}
5    Cs  u0 {3,S}
6    H   u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 162,
    label = "O-Cs(CsCsH)O2s(Cs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S} {4,S}
3    Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    Cs  u0 {2,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 163,
    label = "O-Cs(CsCsCs)O2s(Cs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S} {4,S}
3    Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    Cs  u0 {2,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
7    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 164,
    label = "O-Cs(HHH)O2s(O2s)",
    group = 
"""
1    Cs  u0 {2,S} {4,S} {5,S} {6,S}
2 *1 O2s u0 {1,S} {3,S}
3 *2 O2s u0 {2,S} {7,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    O2s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 165,
    label = "O-Cs(CsHH)O2s(O2s)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S} {4,S}
3    Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    O2s u0 {2,S}
5    Cs  u0 {3,S}
6    H   u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 166,
    label = "O-Cs(CsCsH)O2s(O2s)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S} {4,S}
3    Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    O2s u0 {2,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 167,
    label = "O-Cs(CsCsCs)O2s(O2s)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S} {4,S}
3    Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    O2s u0 {2,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
7    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 168,
    label = "O-CtOs",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S}
3    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 169,
    label = "O-CbOs",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S}
3    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 170,
    label = "O-COOs",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S}
3    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 171,
    label = "O-CSOs",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S}
3    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 172,
    label = "O-CdOs",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    Cd  u0 {1,S} {4,D}
3 *2 O2s u0 {1,S}
4    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 173,
    label = "O-Cds(H)O2s(H)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S} {6,S}
3    Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    H   u0 {3,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 174,
    label = "O-Cds(H)O2s(Cs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S} {6,S}
3    Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    H   u0 {3,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 175,
    label = "O-Cds(H)O2s(O2s)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S} {6,S}
3    Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    H   u0 {3,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 176,
    label = "O-Cds(Cs)O2s(H)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S} {6,S}
3    Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    Cs  u0 {3,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 177,
    label = "O-Cds(Cs)O2s(Cs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S} {6,S}
3    Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    Cs  u0 {3,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 178,
    label = "O-Cds(Cs)O2s(O2s)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S} {6,S}
3    Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    Cs  u0 {3,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 179,
    label = "O-CSulfur",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 S   u0 {1,S}
3    C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 180,
    label = "O-SulfurC",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    S   u0 {1,S}
3 *2 C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 181,
    label = "O-SC",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O   u0 {1,S}
3 *2 C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 182,
    label = "O-OsCs",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S}
3 *2 Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 183,
    label = "O-O2s(H)Cs(HHH)",
    group = 
"""
1 *2 Cs  u0 {2,S} {4,S} {5,S} {6,S}
2 *1 O2s u0 {1,S} {3,S}
3    O2s u0 {2,S} {7,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 184,
    label = "O-O2s(H)Cs(CsHH)",
    group = 
"""
1 *2 Cs  u0 {2,S} {4,S} {5,S} {6,S}
2 *1 O2s u0 {1,S} {3,S}
3    O2s u0 {2,S} {7,S}
4    Cs  u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 185,
    label = "O-O2s(H)Cs(CsCsH)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S} {4,S}
3 *2 Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    H   u0 {2,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 186,
    label = "O-O2s(H)Cs(CsCsCs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S} {4,S}
3 *2 Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    H   u0 {2,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
7    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 187,
    label = "O-O2s(Cs)Cs(HHH)",
    group = 
"""
1 *2 Cs  u0 {2,S} {4,S} {5,S} {6,S}
2 *1 O2s u0 {1,S} {3,S}
3    O2s u0 {2,S} {7,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 188,
    label = "O-O2s(Cs)Cs(CsHH)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S} {4,S}
3 *2 Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    Cs  u0 {2,S}
5    Cs  u0 {3,S}
6    H   u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 189,
    label = "O-O2s(Cs)Cs(CsCsH)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S} {4,S}
3 *2 Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    Cs  u0 {2,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 190,
    label = "O-O2s(Cs)Cs(CsCsCs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S} {4,S}
3 *2 Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    Cs  u0 {2,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
7    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 191,
    label = "O-O2s(O2s)Cs(HHH)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S} {4,S}
3 *2 Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    O2s u0 {2,S}
5    H   u0 {3,S}
6    H   u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 192,
    label = "O-O2s(O2s)Cs(CsHH)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S} {4,S}
3 *2 Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    O2s u0 {2,S}
5    Cs  u0 {3,S}
6    H   u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 193,
    label = "O-O2s(O2s)Cs(CsCsH)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S} {4,S}
3 *2 Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    O2s u0 {2,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
7    H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 194,
    label = "O-O2s(O2s)Cs(CsCsCs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S} {4,S}
3 *2 Cs  u0 {1,S} {5,S} {6,S} {7,S}
4    O2s u0 {2,S}
5    Cs  u0 {3,S}
6    Cs  u0 {3,S}
7    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 195,
    label = "O-OsCt",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S}
3 *2 Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 196,
    label = "O-OsCb",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S}
3 *2 Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 197,
    label = "O-OsCO",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S}
3 *2 CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 198,
    label = "O-OsCS",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S}
3 *2 CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 199,
    label = "O-OsCd",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S}
3 *2 Cd  u0 {1,S} {4,D}
4    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 200,
    label = "O-O2s(H)Cds(H)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S} {6,S}
3 *2 Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    H   u0 {3,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 201,
    label = "O-O2s(Cs)Cds(H)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S} {6,S}
3 *2 Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    H   u0 {3,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 202,
    label = "O-O2s(O2s)Cds(H)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S} {6,S}
3 *2 Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    H   u0 {3,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 203,
    label = "O-O2s(H)Cds(Cs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S} {6,S}
3 *2 Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    Cs  u0 {3,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 204,
    label = "O-O2s(Cs)Cds(Cs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S} {6,S}
3 *2 Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    Cs  u0 {3,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 205,
    label = "O-O2s(O2s)Cds(Cs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S} {6,S}
3 *2 Cd  u0 {1,S} {4,D} {5,S}
4    C   u0 {3,D}
5    Cs  u0 {3,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 206,
    label = "O-OsH",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 207,
    label = "O-O2s(H)H",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S} {4,S}
3 *2 H   u0 {1,S}
4    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 208,
    label = "O-O2s(Cs)H",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S} {4,S}
3 *2 H   u0 {1,S}
4    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 209,
    label = "O-O2s(O2s)H",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    O2s u0 {1,S} {4,S}
4    O2s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 210,
    label = "O-HOs",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    H   u0 {1,S}
3 *2 O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 211,
    label = "O-HOs(H)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S} {4,S}
3    H   u0 {1,S}
4    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 212,
    label = "O-HOs(Cs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S} {4,S}
3    H   u0 {1,S}
4    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 213,
    label = "O-HOs(O2s)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S} {4,S}
3    H   u0 {1,S}
4    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 214,
    label = "O-OsOs",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S}
3    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 215,
    label = "O-O2s(H)O2s(H)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S} {5,S}
3    O2s u0 {1,S} {4,S}
4    H   u0 {3,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 216,
    label = "O-O2s(Cs)O2s(H)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S} {5,S}
3    O2s u0 {1,S} {4,S}
4    Cs  u0 {3,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 217,
    label = "O-O2s(H)O2s(Cs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S} {5,S}
3 *2 O2s u0 {1,S} {4,S}
4    Cs  u0 {3,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 218,
    label = "O-O2s(O2s)O2s(H)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S} {5,S}
3    O2s u0 {1,S} {4,S}
4    O2s u0 {3,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 219,
    label = "O-O2s(H)O2s(O2s)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S} {5,S}
3 *2 O2s u0 {1,S} {4,S}
4    O2s u0 {3,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 220,
    label = "O-O2s(Cs)O2s(Cs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S} {5,S}
3    O2s u0 {1,S} {4,S}
4    Cs  u0 {3,S}
5    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 221,
    label = "O-O2s(Cs)O2s(O2s)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S} {5,S}
3    O2s u0 {1,S} {4,S}
4    Cs  u0 {3,S}
5    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 222,
    label = "O-O2s(O2s)O2s(Cs)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2    O2s u0 {1,S} {5,S}
3 *2 O2s u0 {1,S} {4,S}
4    Cs  u0 {3,S}
5    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 223,
    label = "O-O2s(O2s)O2s(O2s)",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 O2s u0 {1,S} {5,S}
3    O2s u0 {1,S} {4,S}
4    O2s u0 {3,S}
5    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 224,
    label = "O-RRrad",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 R!H u1 {1,S}
3    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 225,
    label = "Y_2centeradjbirad",
    group = 
"""
1 *3 [O2s,Ct,S2s] u1 {2,[S,T]}
2    [O2s,Ct,S2s] u1 {1,[S,T]}
""",
    kinetics = None,
)

entry(
    index = 226,
    label = "O2b",
    group = 
"""
1 *3 O2s u1 {2,S}
2    O2s u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 227,
    label = "C2b",
    group = 
"""
1 *3 Ct u1 {2,T}
2    Ct u1 {1,T}
""",
    kinetics = None,
)

entry(
    index = 228,
    label = "S2b",
    group = 
"""
1 *3 S2s u1 {2,S}
2    S2s u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 229,
    label = "Y_1centerbirad",
    group = 
"""
1 *3 [Cs,Cd,CO,CS,O,N] u2
""",
    kinetics = None,
)

entry(
    index = 230,
    label = "HJ",
    group = 
"""
1 *3 H u1
""",
    kinetics = None,
)

entry(
    index = 231,
    label = "CJ",
    group = 
"""
1 *3 C u1
""",
    kinetics = None,
)

entry(
    index = 232,
    label = "CbJ",
    group = 
"""
1 *3 Cb u1
""",
    kinetics = None,
)

entry(
    index = 233,
    label = "CtJ",
    group = 
"""
1 *3 Ct u1 {2,T}
2    C  u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 234,
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
    index = 235,
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
    index = 236,
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
    index = 237,
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
    index = 238,
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
    index = 239,
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
    index = 240,
    label = "CdsJ-CS",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D}
3    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 241,
    label = "CdsJ-O2s",
    group = 
"""
1 *3 C   u1 {2,D} {3,S}
2    C   u0 {1,D}
3    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 242,
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
    index = 243,
    label = "C=OJ",
    group = 
"""
1 *3 CO u1 {2,S}
2    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 244,
    label = "C=OJ-H",
    group = 
"""
1 *3 CO u1 {2,S}
2    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 245,
    label = "C=OJ-Cs",
    group = 
"""
1 *3 CO u1 {2,S}
2    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 246,
    label = "C=OJ-Ct",
    group = 
"""
1 *3 CO u1 {2,S}
2    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 247,
    label = "C=OJ-Cb",
    group = 
"""
1 *3 CO u1 {2,S}
2    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 248,
    label = "C=OJ-CO",
    group = 
"""
1 *3 CO u1 {2,S}
2    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 249,
    label = "C=OJ-CS",
    group = 
"""
1 *3 CO u1 {2,S}
2    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 250,
    label = "C=OJ-O2s",
    group = 
"""
1 *3 CO  u1 {2,S}
2    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 251,
    label = "C=OJ-Cd",
    group = 
"""
1 *3 CO u1 {2,S}
2    Cd u0 {1,S} {3,D}
3    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 252,
    label = "C=SJ",
    group = 
"""
1 *3 CS u1 {2,S}
2    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 253,
    label = "C=SJ-H",
    group = 
"""
1 *3 CS u1 {2,S}
2    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 254,
    label = "C=SJ-Cs",
    group = 
"""
1 *3 CS u1 {2,S}
2    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 255,
    label = "C=SJ-Ct",
    group = 
"""
1 *3 CS u1 {2,S}
2    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 256,
    label = "C=SJ-Cb",
    group = 
"""
1 *3 CS u1 {2,S}
2    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 257,
    label = "C=SJ-CO",
    group = 
"""
1 *3 CS      u1 {2,S}
2    [CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 258,
    label = "C=SJ-O2s",
    group = 
"""
1 *3 CS  u1 {2,S}
2    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 259,
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
    index = 260,
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
    index = 261,
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
    index = 262,
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
    index = 263,
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
    index = 264,
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
    index = 265,
    label = "CsJ-OsHH",
    group = 
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 266,
    label = "CsJ-OsCsH",
    group = 
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 267,
    label = "CsJ-OsOsCs",
    group = 
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    O2s u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 268,
    label = "CsJ-OsOsOs",
    group = 
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    O2s u0 {1,S}
4    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 269,
    label = "CsJ-OsCsCs",
    group = 
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 270,
    label = "CsJ-OsOsH",
    group = 
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    O2s u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 271,
    label = "CsJ-OneDe",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [H,Cs,O2s]       u0 {1,S}
4    [H,Cs,O2s]       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 272,
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
    index = 273,
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
    index = 274,
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
    index = 275,
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
    index = 276,
    label = "CsJ-CSHH",
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
    index = 278,
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
    index = 279,
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
    index = 280,
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
    index = 281,
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
    index = 282,
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
    index = 283,
    label = "CsJ-OneDeOsH",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    O2s              u0 {1,S}
4    H                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 284,
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
    index = 285,
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
    index = 286,
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
    index = 287,
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
    index = 288,
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
    index = 289,
    label = "CsJ-OneDeOsCs",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    O2s              u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 290,
    label = "CsJ-OneDeOsOs",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    O2s              u0 {1,S}
4    O2s              u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 291,
    label = "CsJ-TwoDe",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [H,Cs,O2s,S2s]   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 292,
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
    index = 293,
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
    index = 294,
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
    index = 295,
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
    index = 296,
    label = "CsJ-CtCSH",
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
    index = 297,
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
    index = 298,
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
    index = 299,
    label = "CsJ-CbCSH",
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
    index = 300,
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
    index = 301,
    label = "CsJ-CSCSH",
    group = 
"""
1 *3 C       u1 {2,S} {3,S} {4,S}
2    CS      u0 {1,S}
3    [CO,CS] u0 {1,S}
4    H       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 302,
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
    index = 303,
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
    index = 304,
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
    index = 305,
    label = "CsJ-CdCSH",
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
    index = 306,
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
    index = 307,
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
    index = 308,
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
    index = 309,
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
    index = 310,
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
    index = 311,
    label = "CsJ-CtCSCs",
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
    index = 312,
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
    index = 313,
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
    index = 314,
    label = "CsJ-CbCSCs",
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
    index = 315,
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
    index = 316,
    label = "CsJ-CSCSCs",
    group = 
"""
1 *3 C       u1 {2,S} {3,S} {4,S}
2    CS      u0 {1,S}
3    [CO,CS] u0 {1,S}
4    Cs      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 317,
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
    index = 318,
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
    index = 319,
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
    index = 320,
    label = "CsJ-CdCSCs",
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
    index = 321,
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
    label = "CsJ-TwoDeOs",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    O2s              u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 323,
    label = "CsJ-TwoDeSs",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    S2s              u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 324,
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
    index = 325,
    label = "OJ",
    group = 
"""
1 *3 O2s u1
""",
    kinetics = None,
)

entry(
    index = 326,
    label = "OsJ",
    group = 
"""
1 *3 O2s u1 {2,S}
2    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 327,
    label = "OsJ-H",
    group = 
"""
1 *3 O2s u1 {2,S}
2    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 328,
    label = "OsJ-Cs",
    group = 
"""
1 *3 O2s u1 {2,S}
2    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 329,
    label = "OsJ-O2s",
    group = 
"""
1 *3 O2s u1 {2,S}
2    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 330,
    label = "OsJ-OneDe",
    group = 
"""
1 *3 O2s              u1 {2,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 331,
    label = "OsJ-Ct",
    group = 
"""
1 *3 O2s u1 {2,S}
2    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 332,
    label = "OsJ-Cb",
    group = 
"""
1 *3 O2s u1 {2,S}
2    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 333,
    label = "OsJ-CO",
    group = 
"""
1 *3 O2s u1 {2,S}
2    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 334,
    label = "OsJ-CS",
    group = 
"""
1 *3 O2s u1 {2,S}
2    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 335,
    label = "OsJ-Cd",
    group = 
"""
1 *3 O2s u1 {2,S}
2    Cd  u0 {1,S} {3,D}
3    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 336,
    label = "SJ",
    group = 
"""
1 *3 S u1
""",
    kinetics = None,
)

entry(
    index = 337,
    label = "SsJ",
    group = 
"""
1 *3 S2s u1 {2,S}
2    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 338,
    label = "SsJ-H",
    group = 
"""
1 *3 S2s u1 {2,S}
2    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 339,
    label = "SsJ-Cs",
    group = 
"""
1 *3 S2s u1 {2,S}
2    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 340,
    label = "SsJ-SOs",
    group = 
"""
1 *3 S2s u1 {2,S}
2    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 341,
    label = "SsJ-OneDe",
    group = 
"""
1 *3 S2s              u1 {2,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 342,
    label = "SsJ-Ct",
    group = 
"""
1 *3 S2s u1 {2,S}
2    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 343,
    label = "SsJ-Cb",
    group = 
"""
1 *3 S2s u1 {2,S}
2    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 344,
    label = "SsJ-CO",
    group = 
"""
1 *3 S2s     u1 {2,S}
2    [CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 345,
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
    index = 346,
    label = "NJ",
    group = 
"""
1 *3 N u1
""",
    kinetics = None,
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
            L4: O-CSH
            L4: O-CdH
                L5: O-Cds(H)H
                L5: O-Cds(Cs)H
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
            L4: O-HCS
            L4: O-HCd
                L5: O-HCds(H)
                L5: O-HCds(Cs)
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
            L4: O-CsCS
            L4: O-COCs
            L4: O-CSCs
            L4: O-CtCt
            L4: O-CtCb
            L4: O-CbCt
            L4: O-CtCO
            L4: O-CtCS
            L4: O-COCt
            L4: O-CSCt
            L4: O-CbCb
            L4: O-CbCO
            L4: O-CbCS
            L4: O-COCb
            L4: O-CSCb
            L4: O-COCO
            L4: O-CSCS
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
            L4: O-CdCt
            L4: O-CtCd
            L4: O-CdCb
            L4: O-CbCd
            L4: O-CdCO
            L4: O-CdCS
            L4: O-COCd
            L4: O-CSCd
            L4: O-CdCd
        L3: O-CS
            L4: O-COss
                L5: O-Cs(HHH)O2s(H)
                L5: O-Cs(CsHH)O2s(H)
                L5: O-Cs(CsCsH)O2s(H)
                L5: O-Cs(CsCsCs)O2s(H)
                L5: O-Cs(HHH)O2s(Cs)
                L5: O-Cs(CsHH)O2s(Cs)
                L5: O-Cs(CsCsH)O2s(Cs)
                L5: O-Cs(CsCsCs)O2s(Cs)
                L5: O-Cs(HHH)O2s(O2s)
                L5: O-Cs(CsHH)O2s(O2s)
                L5: O-Cs(CsCsH)O2s(O2s)
                L5: O-Cs(CsCsCs)O2s(O2s)
            L4: O-CtOs
            L4: O-CbOs
            L4: O-COOs
            L4: O-CSOs
            L4: O-CdOs
                L5: O-Cds(H)O2s(H)
                L5: O-Cds(H)O2s(Cs)
                L5: O-Cds(H)O2s(O2s)
                L5: O-Cds(Cs)O2s(H)
                L5: O-Cds(Cs)O2s(Cs)
                L5: O-Cds(Cs)O2s(O2s)
        L3: O-CSulfur
        L3: O-SulfurC
        L3: O-SC
            L4: O-OsCs
                L5: O-O2s(H)Cs(HHH)
                L5: O-O2s(H)Cs(CsHH)
                L5: O-O2s(H)Cs(CsCsH)
                L5: O-O2s(H)Cs(CsCsCs)
                L5: O-O2s(Cs)Cs(HHH)
                L5: O-O2s(Cs)Cs(CsHH)
                L5: O-O2s(Cs)Cs(CsCsH)
                L5: O-O2s(Cs)Cs(CsCsCs)
                L5: O-O2s(O2s)Cs(HHH)
                L5: O-O2s(O2s)Cs(CsHH)
                L5: O-O2s(O2s)Cs(CsCsH)
                L5: O-O2s(O2s)Cs(CsCsCs)
            L4: O-OsCt
            L4: O-OsCb
            L4: O-OsCO
            L4: O-OsCS
            L4: O-OsCd
                L5: O-O2s(H)Cds(H)
                L5: O-O2s(Cs)Cds(H)
                L5: O-O2s(O2s)Cds(H)
                L5: O-O2s(H)Cds(Cs)
                L5: O-O2s(Cs)Cds(Cs)
                L5: O-O2s(O2s)Cds(Cs)
        L3: O-OsH
            L4: O-O2s(H)H
            L4: O-O2s(Cs)H
            L4: O-O2s(O2s)H
        L3: O-HOs
            L4: O-HOs(H)
            L4: O-HOs(Cs)
            L4: O-HOs(O2s)
        L3: O-OsOs
            L4: O-O2s(H)O2s(H)
            L4: O-O2s(Cs)O2s(H)
            L4: O-O2s(H)O2s(Cs)
            L4: O-O2s(O2s)O2s(H)
            L4: O-O2s(H)O2s(O2s)
            L4: O-O2s(Cs)O2s(Cs)
            L4: O-O2s(Cs)O2s(O2s)
            L4: O-O2s(O2s)O2s(Cs)
            L4: O-O2s(O2s)O2s(O2s)
    L2: O-RRrad
L1: YJ
    L2: Y_2centeradjbirad
        L3: O2b
        L3: C2b
        L3: S2b
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
            L4: CdsJ-CS
            L4: CdsJ-O2s
            L4: CdsJ-Cd
        L3: C=OJ
            L4: C=OJ-H
            L4: C=OJ-Cs
            L4: C=OJ-Ct
            L4: C=OJ-Cb
            L4: C=OJ-CO
            L4: C=OJ-CS
            L4: C=OJ-O2s
            L4: C=OJ-Cd
        L3: C=SJ
            L4: C=SJ-H
            L4: C=SJ-Cs
            L4: C=SJ-Ct
            L4: C=SJ-Cb
            L4: C=SJ-CO
            L4: C=SJ-O2s
            L4: C=SJ-Cd
        L3: CsJ
            L4: CsJ-HHH
            L4: CsJ-CsHH
            L4: CsJ-CsCsH
            L4: CsJ-CsCsCs
            L4: CsJ-OsHH
            L4: CsJ-OsCsH
            L4: CsJ-OsOsCs
            L4: CsJ-OsOsOs
            L4: CsJ-OsCsCs
            L4: CsJ-OsOsH
            L4: CsJ-OneDe
                L5: CsJ-OneDeHH
                    L6: CsJ-CtHH
                    L6: CsJ-CbHH
                    L6: CsJ-COHH
                    L6: CsJ-CSHH
                    L6: CsJ-CdHH
                L5: CsJ-OneDeCsH
                    L6: CsJ-CtCsH
                    L6: CsJ-CbCsH
                    L6: CsJ-COCsH
                    L6: CsJ-CdCsH
                L5: CsJ-OneDeOsH
                L5: CsJ-OneDeCsCs
                    L6: CsJ-CtCsCs
                    L6: CsJ-CbCsCs
                    L6: CsJ-COCsCs
                    L6: CsJ-CdCsCs
                L5: CsJ-OneDeOsCs
                L5: CsJ-OneDeOsOs
            L4: CsJ-TwoDe
                L5: CsJ-TwoDeH
                    L6: CsJ-CtCtH
                    L6: CsJ-CtCbH
                    L6: CsJ-CtCOH
                    L6: CsJ-CtCSH
                    L6: CsJ-CbCbH
                    L6: CsJ-CbCOH
                    L6: CsJ-CbCSH
                    L6: CsJ-COCOH
                    L6: CsJ-CSCSH
                    L6: CsJ-CdCtH
                    L6: CsJ-CdCbH
                    L6: CsJ-CdCOH
                    L6: CsJ-CdCSH
                    L6: CsJ-CdCdH
                L5: CsJ-TwoDeCs
                    L6: CsJ-CtCtCs
                    L6: CsJ-CtCbCs
                    L6: CsJ-CtCOCs
                    L6: CsJ-CtCSCs
                    L6: CsJ-CbCbCs
                    L6: CsJ-CbCOCs
                    L6: CsJ-CbCSCs
                    L6: CsJ-COCOCs
                    L6: CsJ-CSCSCs
                    L6: CsJ-CdCtCs
                    L6: CsJ-CdCbCs
                    L6: CsJ-CdCOCs
                    L6: CsJ-CdCSCs
                    L6: CsJ-CdCdCs
                L5: CsJ-TwoDeOs
                L5: CsJ-TwoDeSs
            L4: CsJ-ThreeDe
    L2: OJ
        L3: OsJ
            L4: OsJ-H
            L4: OsJ-Cs
            L4: OsJ-O2s
            L4: OsJ-OneDe
                L5: OsJ-Ct
                L5: OsJ-Cb
                L5: OsJ-CO
                L5: OsJ-CS
                L5: OsJ-Cd
    L2: SJ
        L3: SsJ
            L4: SsJ-H
            L4: SsJ-Cs
            L4: SsJ-SOs
            L4: SsJ-OneDe
                L5: SsJ-Ct
                L5: SsJ-Cb
                L5: SsJ-CO
                L5: SsJ-Cd
    L2: NJ
"""
)

