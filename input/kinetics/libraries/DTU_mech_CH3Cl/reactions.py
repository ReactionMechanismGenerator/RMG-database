#!/usr/bin/env python
# encoding: utf-8

name = "DTU_mech_CH3Cl"
shortDesc = u"DTU mechanism for CH3Cl, 2017 (DOI: 10.1039/c7cp07552a)"
longDesc = u"""
DTU mechanism for methyl chloride CH3Cl, 2017 (DOI: 10.1039/c7cp07552a)
"""


entry(
    index = 0,
    label = "H + CL <=> HCL",
    degeneracy = 1.0,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2e+23, 'cm^6/(mol^2*s)'), n=-2.45, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[H][H]': 2, '[Cl][Cl]': 2, 'N#N': 2},
    ),
    longDesc =
u"""

""",
)

entry(
    index = 1,
    label = "CL + H2 <=> HCL + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.5e+07, 'cm^3/(mol*s)'),
        n = 1.72,
        Ea = (3060, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 2,
    label = "HCL + O <=> CL + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (590000, 'cm^3/(mol*s)'),
        n = 2.114,
        Ea = (4024, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 3,
    label = "HCL + OH <=> CL + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (410000, 'cm^3/(mol*s)'),
        n = 2.12,
        Ea = (-1284, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 4,
    label = "CL + H2O2 <=> HCL + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(1950, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 5,
    label = "CL + HO2 <=> HCL + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.5e+14, 'cm^3/(mol*s)'), n=-0.63, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 6,
    label = "CL + HO2 <=> CLO + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(1133, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 7,
    label = "CL + O3 <=> CLO + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(417, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 8,
    label = "CL + CL <=> CL2",
    degeneracy = 1.0,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.3e+19, 'cm^6/(mol^2*s)'), n=-1.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[H][H]': 2, '[Cl][Cl]': 6.9, 'N#N': 2},
    ),
    longDesc =
u"""

""",
)

entry(
    index = 10,
    label = "CL2 + H <=> HCL + CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(1172, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 11,
    label = "CL2 + O <=> CL + CLO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(3279, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 12,
    label = "CL2 + OH <=> HOCL + CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.2e+08, 'cm^3/(mol*s)'),
        n = 1.35,
        Ea = (1480, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 13,
    label = "CL + OH <=> HOCL",
    degeneracy = 1.0,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.2e+19, 'cm^6/(mol^2*s)'),
            n = -1.43,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc =
u"""

""",
)

entry(
    index = 14,
    label = "HOCL <=> CLO + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.1e+14, 's^-1'), n=-2.09, Ea=(93690, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 15,
    label = "HOCL + H <=> CLO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.1e+07, 'cm^3/(mol*s)'), n=1.96, Ea=(421, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 16,
    label = "HOCL + O <=> CLO + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3300, 'cm^3/(mol*s)'), n=2.9, Ea=(1592, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 17,
    label = "HOCL + OH <=> CLO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.3, 'cm^3/(mol*s)'), n=3.61, Ea=(-2684, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 18,
    label = "HOCL + HO2 <=> CLO + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.8e-07, 'cm^3/(mol*s)'),
        n = 5.35,
        Ea = (6978, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 19,
    label = "HOCL + CL <=> HCL + CLO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.35, 'cm^3/(mol*s)'), n=4.07, Ea=(-337, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)


entry(
    index = 21,
    label = "CLO + H <=> CL + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 22,
    label = "CLO + H <=> HCL + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 23,
    label = "CLO + O <=> CL + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(-219, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 24,
    label = "CLO + OH <=> HCL + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (350000, 'cm^3/(mol*s)'),
        n = 1.67,
        Ea = (-3827, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 25,
    label = "CLO + HO2 <=> HOCL + O2",
    degeneracy = 1.0,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(7800, 'cm^3/(mol*s)'), n=2.37, Ea=(5111, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(840, 'cm^3/(mol*s)'), n=2.26, Ea=(-449, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    longDesc =
u"""

""",
)

entry(
    index = 26,
    label = "CLO + HO2 <=> HCL + O3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4600, 'cm^3/(mol*s)'), n=2.05, Ea=(1699, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 27,
    label = "CLO + HO2 <=> CLOO + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(460000, 'cm^3/(mol*s)'), n=1.8, Ea=(2116, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 28,
    label = "CLO + CLO <=> CL2 + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.6e+10, 'cm^3/(mol*s)'),
        n = 0.66,
        Ea = (3759, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 30,
    label = "CLO + CLO <=> CL + CLOO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.2e+10, 'cm^3/(mol*s)'),
        n = 0.77,
        Ea = (4308, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)


entry(
    index = 32,
    label = "CL + O2 <=> CLOO",
    degeneracy = 1.0,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6e+28, 'cm^6/(mol^2*s)'),
            n = -5.34,
            Ea = (1341, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc =
u"""

""",
)

entry(
    index = 33,
    label = "CLOO + H <=> CLO + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 34,
    label = "CLOO + O <=> CLO + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(1910, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 35,
    label = "CLOO + OH <=> HOCL + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 36,
    label = "CLOO + CL <=> CL2 + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.3e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 38,
    label = "CH2O + CL <=> HCO + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.9e+13, 'cm^3/(mol*s)'), n=0, Ea=(68, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 39,
    label = "CH2O + CLO <=> HCO + HOCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.2e+10, 'cm^3/(mol*s)'),
        n = 0.79,
        Ea = (5961, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 40,
    label = "HCO + CL <=> CO + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 41,
    label = "HCO + CL2 <=> CLCHO + CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(72, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 42,
    label = "HCO + CLO <=> CO + HOCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 43,
    label = "CO + CLO <=> CL + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (240000, 'cm^3/(mol*s)'),
        n = 2.02,
        Ea = (10500, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 44,
    label = "CH4 + CL <=> CH3 + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(340000, 'cm^3/(mol*s)'), n=2.49, Ea=(1210, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 45,
    label = "CH2 + HCL <=> CH3 + CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(866, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 46,
    label = "CH3 + CL <=> CH3CL",
    degeneracy = 1.0,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.2e+13, 'cm^3/(mol*s)'), n=0.05, Ea=(37, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (8.2e+32, 'cm^6/(mol^2*s)'),
            n = -4.67,
            Ea = (1680, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.379,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {},
    ),
    longDesc =
u"""

""",
)

entry(
    index = 47,
    label = "CH3CL <=> CH2 + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.5e+27, 's^-1'), n=-5.15, Ea=(109700, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 48,
    label = "CH2CL + H <=> CH3CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+25, 'cm^3/(mol*s)'), n=-4.47, Ea=(3490, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 49,
    label = "CH3CL + H <=> CH3 + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.1e+07, 'cm^3/(mol*s)'),
        n = 1.73,
        Ea = (7462, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 50,
    label = "CH3CL + H <=> CH2CL + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(280000, 'cm^3/(mol*s)'), n=2.59, Ea=(7645, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 51,
    label = "CH3CL + O <=> CH2CL + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.6e+13, 'cm^3/(mol*s)'),
        n = 0.31,
        Ea = (11188, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 52,
    label = "CH3CL + OH <=> CH2CL + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.8e+10, 'cm^3/(mol*s)'),
        n = 0.89,
        Ea = (2881, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 53,
    label = "CH3CL + HO2 <=> H2O2 + CH2CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(21660, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 54,
    label = "CH3CL + O2 <=> HO2 + CH2CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(54000, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 55,
    label = "CH2CL + CH4 <=> CH3CL + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.3e-07, 'cm^3/(mol*s)'),
        n = 5.406,
        Ea = (2466, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 56,
    label = "CH3CL + C2H3 <=> CH2CL + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6, 'cm^3/(mol*s)'), n=3.535, Ea=(4034, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 57,
    label = "CH3CL + CL <=> HCL + CH2CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.4e+10, 'cm^3/(mol*s)'),
        n = 0.92,
        Ea = (1580, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 59,
    label = "CH2CL + CL2 <=> CH2CL2 + CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.6e+07, 'cm^3/(mol*s)'), n=1.45, Ea=(84, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)


entry(
    index = 61,
    label = "CH3CL + CLO <=> CH2CL + HOCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(10700, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 63,
    label = "CH2CL + H <=> CH3 + CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.1e+14, 'cm^3/(mol*s)'),
        n = -0.22,
        Ea = (310, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 64,
    label = "CH2CL + H <=> CH2 + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(95000, 'cm^3/(mol*s)'), n=1.91, Ea=(2600, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 65,
    label = "CH2CL + O <=> CH2O + CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.6e+13, 'cm^3/(mol*s)'),
        n = -0.13,
        Ea = (710, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 66,
    label = "CH2CL + O <=> CH2CLO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.3e+15, 'cm^3/(mol*s)'),
        n = -1.98,
        Ea = (1100, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 67,
    label = "CH2CL + OH <=> CH2O + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.2e+22, 'cm^3/(mol*s)'),
        n = -2.72,
        Ea = (3860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 68,
    label = "CH2CL + OH <=> CH3O + CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0.29, Ea=(3270, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 69,
    label = "CH2CL + O2 <=> CLCHO + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(49, 'cm^3/(mol*s)'), n=2.723, Ea=(9430, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 70,
    label = "CH2CL + CH3 <=> C2H5CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.3e+40, 'cm^3/(mol*s)'),
        n = -8.49,
        Ea = (10590, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 71,
    label = "CH2CL + CH3 <=> C2H4 + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(-181, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 72,
    label = "CH2CL + CH3 <=> C2H5 + CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.3e+19, 'cm^3/(mol*s)'),
        n = -2.07,
        Ea = (10130, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 73,
    label = "CH2CL + CH2O <=> CH3CL + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(6000, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 74,
    label = "CH2CL + CLO <=> CLCHO + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.1e+19, 'cm^3/(mol*s)'),
        n = -2.22,
        Ea = (2360, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)


entry(
    index = 76,
    label = "CH2CL + CH2CL <=> C2H3CL + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.1e+15, 'cm^3/(mol*s)'), n=-0.85, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)


entry(
    index = 78,
    label = "CH2CLO <=> HCO + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.7e+09, 's^-1'), n=0, Ea=(9545, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 79,
    label = "CH2CLO + O2 <=> CLCHO + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(1856, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 80,
    label = "CLCHO <=> HCO + CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.9e+29, 's^-1'), n=-5.15, Ea=(92920, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 81,
    label = "CLCHO <=> CO + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+30, 's^-1'), n=-5.19, Ea=(92960, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 82,
    label = "CLCHO + H <=> CLCO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(990000, 'cm^3/(mol*s)'), n=2.25, Ea=(3861, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 83,
    label = "CLCHO + H <=> HCO + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.1e+06, 'cm^3/(mol*s)'),
        n = 2.12,
        Ea = (6905, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 84,
    label = "CLCHO + H <=> CH2O + CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7e+14, 'cm^3/(mol*s)'), n=-0.58, Ea=(6360, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 85,
    label = "CLCHO + O <=> CLCO + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.2e+11, 'cm^3/(mol*s)'),
        n = 0.57,
        Ea = (2760, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 86,
    label = "CLCHO + OH <=> CLCO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(2822, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 87,
    label = "CLCHO + O2 <=> CLCO + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(41800, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 88,
    label = "CLCHO + CL <=> CLCO + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(1620, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)


entry(
    index = 90,
    label = "CLCHO + CLO <=> CLCO + HOCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(500, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)


entry(
    index = 92,
    label = "CLCHO + CH3 <=> CLCO + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(6000, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 93,
    label = "CLCHO + CH3 <=> HCO + CH3CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(8800, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 94,
    label = "CL + CO <=> CLCO",
    degeneracy = 1.0,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.2e+24, 'cm^6/(mol^2*s)'), n=-3.8, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    longDesc =
u"""

""",
)

entry(
    index = 95,
    label = "CLCO + H <=> CO + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 96,
    label = "CLCO + O <=> CO + CLO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 97,
    label = "CLCO + O <=> CO2 + CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 98,
    label = "CLCO + OH <=> CO + HOCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 99,
    label = "CLCO + O2 <=> CO2 + CLO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.9e+10, 'cm^3/(mol*s)'), n=0, Ea=(3300, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 100,
    label = "CLCO + CL <=> CO + CL2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(1400, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 102,
    label = "C2H6 + CL <=> C2H5 + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.4e+11, 'cm^3/(mol*s)'), n=0.7, Ea=(-233, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 103,
    label = "C2H5 + CL <=> C2H4 + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.8e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 104,
    label = "C2H3 + HCL <=> C2H4 + CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+11, 'cm^3/(mol*s)'), n=0, Ea=(-670, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 105,
    label = "CH3CHO + CL <=> CH3CO + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 106,
    label = "CH3CO + CL <=> CH2CO + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 107,
    label = "CH2CL2 <=> CH2CL + CL",
    degeneracy = 1.0,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1.3e+16, 's^-1'), n=0, Ea=(77500, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(4e+15, 'cm^3/(mol*s)'), n=0, Ea=(56400, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    longDesc =
u"""

""",
)

entry(
    index = 108,
    label = "CH2CL2 + H <=> CH2CL + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.3e+07, 'cm^3/(mol*s)'),
        n = 1.79,
        Ea = (5884, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 109,
    label = "CH2CL2 + H <=> CHCL2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(92000, 'cm^3/(mol*s)'), n=2.66, Ea=(6091, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 110,
    label = "CH2CL2 + O <=> CHCL2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.6e+06, 'cm^3/(mol*s)'),
        n = 1.99,
        Ea = (5683, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 111,
    label = "CH2CL2 + OH <=> CHCL2 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+07, 'cm^3/(mol*s)'), n=1.66, Ea=(1033, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 112,
    label = "CH2CL2 + HO2 <=> CHCL2 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(18270, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 113,
    label = "CH2CL2 + O2 <=> CHCL2 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(49800, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 114,
    label = "CH2CL2 + CL <=> CHCL2 + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.9e+07, 'cm^3/(mol*s)'), n=1.58, Ea=(715, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)


entry(
    index = 116,
    label = "CH2CL2 + CH3 <=> CH3CL + CH2CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.4e+11, 'cm^3/(mol*s)'), n=0, Ea=(4900, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 117,
    label = "CH2CL2 + CH3 <=> CHCL2 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.8e+10, 'cm^3/(mol*s)'), n=0, Ea=(7200, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 118,
    label = "CHCL2 + H <=> CH2CL + CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.3e+14, 'cm^3/(mol*s)'),
        n = -0.03,
        Ea = (570, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 119,
    label = "CHCL2 + H <=> CH2CL2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.8e+26, 'cm^3/(mol*s)'),
        n = -4.82,
        Ea = (3810, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 120,
    label = "CHCL2 + O <=> CO + HCL + CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(407, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 121,
    label = "CHCL2 + CH3 <=> C2H3CL + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(-713, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 122,
    label = "CH2CLCH2CL <=> C2H3CL + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.2e+13, 's^-1'), n=0, Ea=(56300, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 123,
    label = "CH2CLCH2CL <=> CH2CLCH2 + CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.2e+15, 's^-1'), n=0, Ea=(78000, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 124,
    label = "CH2CLCH2CL + H <=> CH2CLCH2 + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(8525, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 125,
    label = "CH2CLCH2CL + O <=> CLCH2CHCL + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(4968, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 126,
    label = "CH2CLCH2CL + OH <=> CLCH2CHCL + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.2e+09, 'cm^3/(mol*s)'), n=1, Ea=(1639, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 127,
    label = "CH2CLCH2CL + O2 <=> CLCH2CHCL + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.8e+06, 'cm^3/(mol*s)'), n=2, Ea=(45026, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 128,
    label = "CH2CLCH2CL + CL <=> CLCH2CHCL + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(2166, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)


entry(
    index = 130,
    label = "CH2CLCH2CL + CH3 <=> CLCH2CHCL + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(20000, 'cm^3/(mol*s)'), n=2, Ea=(8520, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 131,
    label = "CLCH2CHCL <=> C2H3CL + CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.5e+13, 's^-1'), n=0, Ea=(19800, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 132,
    label = "C2H5CL <=> C2H4 + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.5e+10, 's^-1'), n=1.05, Ea=(57700, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 133,
    label = "C2H5CL + H <=> C2H5 + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+08, 'cm^3/(mol*s)'), n=1.46, Ea=(8110, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 134,
    label = "C2H5CL + H <=> CH3CHCL + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(660000, 'cm^3/(mol*s)'), n=2.38, Ea=(5410, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 135,
    label = "C2H5CL + H <=> CH2CLCH2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(13000, 'cm^3/(mol*s)'), n=2.9, Ea=(6900, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 136,
    label = "C2H5CL + O <=> CH3CHCL + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(6617, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 137,
    label = "C2H5CL + O <=> CH2CLCH2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(6617, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 138,
    label = "C2H5CL + OH <=> CH3CHCL + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(52000, 'cm^3/(mol*s)'), n=2.6, Ea=(-219, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 139,
    label = "C2H5CL + OH <=> CH2CLCH2 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(17000, 'cm^3/(mol*s)'), n=2.6, Ea=(-219, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 140,
    label = "C2H5CL + CL <=> CH3CHCL + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(904, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 142,
    label = "C2H5CL + CL <=> CH2CLCH2 + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(1568, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 144,
    label = "C2H3CL + H <=> CH3CHCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+10, 'cm^3/(mol*s)'), n=0.86, Ea=(149, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 145,
    label = "CH3CHCL + H <=> C2H3CL + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 146,
    label = "CH3CHCL + O <=> C2H3CL + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 147,
    label = "CH3CHCL + OH <=> C2H3CL + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 148,
    label = "CH3CHCL + CL <=> C2H3CL + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)


entry(
    index = 150,
    label = "C2H4 + CL <=> CH2CLCH2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.8e+10, 'cm^3/(mol*s)'),
        n = 1.31,
        Ea = (-1029, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 151,
    label = "C2H3CL + H <=> CH2CLCH2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(5800, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 152,
    label = "C2H3CL <=> C2H2 + HCL",
    degeneracy = 1.0,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(69400, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(5.3e+16, 'cm^3/(mol*s)'), n=0, Ea=(48700, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    longDesc =
u"""

""",
)

entry(
    index = 153,
    label = "C2H3CL <=> C2H3 + CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.7e+38, 's^-1'), n=-7.13, Ea=(96370, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 154,
    label = "C2H3CL + H <=> C2H3 + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 155,
    label = "C2H3CL + H <=> C2H4 + CL",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.6e+13, 'cm^3/(mol*s)'),
        n = -0.02,
        Ea = (5840, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""

""",
)

entry(
    index = 156,
    label = "C2H3CL + O <=> CHCLCH + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.6e+09, 'cm^3/(mol*s)'), n=0.87, Ea=(874, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 157,
    label = "C2H3CL + OH <=> CHCLCH + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.5e+07, 'cm^3/(mol*s)'), n=2, Ea=(6300, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 158,
    label = "C2H3CL + CL <=> CHCLCH + HCL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+14, 'cm^3/(mol*s)'), n=0, Ea=(13300, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)


entry(
    index = 160,
    label = "C2H2 + CL <=> CHCLCH",
    degeneracy = 1.0,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(4.8e+16, 'cm^3/(mol*s)'), n=-1.04, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.9e+23, 'cm^6/(mol^2*s)'),
            n = -2.09,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc =
u"""

""",
)

entry(
    index = 161,
    label = "CHCLCH + O2 <=> CH2O + CLCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(-330, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)
