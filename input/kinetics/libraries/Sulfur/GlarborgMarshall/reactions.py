#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/GlarborgMarshall"
shortDesc = u""
longDesc = u"""
OCS chemistry

Taken from:
Oxidation of Reduced S Species: Carbonyl Sulfide
Peter Glarborg, Paul Marshall
International Journal of Chemical Kinetics, 45(7) (2013) 429-439
DOI: 10.1002/kin.20778
"""

entry(
    index = 1,
    label = "OCS <=> CO + S",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.5e+14, 'cm^3/(mol*s)'), n=0, Ea=(61400, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    longDesc = 
u"""
OYAMAT94
""",
)

entry(
    index = 2,
    label = "OCS + H <=> CO + SH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+11, 'cm^3/(mol*s)'),
        n = 1.022,
        Ea = (5584, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
SAHSHA12
""",
)

entry(
    index = 3,
    label = "OCS + O <=> CO + SO",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (4.7e+13, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (5200, 'cal/mol'),
                T0 = (1, 'K'),
                comment = 'SINCVE88 (ktot)',
            ),
            Arrhenius(
                A = (-2e+13, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (7385, 'cal/mol'),
                T0 = (1, 'K'),
                comment = 'pw',
            ),
        ],
    ),
)

entry(
    index = 4,
    label = "OCS + O <=> CO2 + S",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7385, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'pw',
    ),
    longDesc = 
u"""
pw
""",
)

entry(
    index = 5,
    label = "OCS + OH <=> CO2 + SH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (16040, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
SAHSHA12 (fit graph)
""",
)

entry(
    index = 6,
    label = "OCS + O2 <=> CO + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (32000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
estimated kinetics
""",
)

entry(
    index = 7,
    label = "OCS + S <=> CO + S2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000, 'cm^3/(mol*s)'),
        n = 2.57,
        Ea = (2345, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
LULIN06
""",
)

entry(
    index = 8,
    label = "OCS + S <=> OCS2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (2.4e+34, 'cm^3/(mol*s)'),
                n = -8.22,
                Ea = (9476, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.7e+31, 'cm^3/(mol*s)'),
                n = -6.98,
                Ea = (8357, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
0.66 atm  LULIN06
""",
)

entry(
    index = 9,
    label = "OCS2 + O <=> OCS + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
estimated kinetics
""",
)

entry(
    index = 10,
    label = "OCS2 + S <=> OCS + S2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
LULIN06
""",
)

entry(
    index = 11,
    label = "OCS + SO <=> S2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (37700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
see text
""",
)

entry(
    index = 12,
    label = "S2 + O2 <=> S2O + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17000, 'cm^3/(mol*s)'),
        n = 2.539,
        Ea = (34376, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Ryan Zhou/Haynes G3 barrier
""",
)

entry(
    index = 13,
    label = "S2O + O <=> SO + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.3e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Ryan Zhou/Haynes BSH NIST
""",
)

entry(
    index = 36,
    label = "O2 + O <=> O3",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(5.6e+20, 'cm^6/(mol^2*s)'), n=-2.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    longDesc = 
u"""
ATKTRO04
""",
)

entry(
    index = 37,
    label = "O3 + O <=> O2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4100, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
ATKTRO04
""",
)

entry(
    index = 38,
    label = "O3 + OH <=> O2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
ATKTRO04
""",
)

entry(
    index = 39,
    label = "O3 + HO2 <=> O2 + O2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00058, 'cm^3/(mol*s)'),
        n = 4.57,
        Ea = (-1377, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
ATKTRO04
""",
)

entry(
    index = 47,
    label = "H2S <=> S + H2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.6e+24, 'cm^3/(mol*s)'),
            n = -2.613,
            Ea = (89100, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=S=O': 10, 'O': 10, 'N#N': 1.5},
    ),
    longDesc = 
u"""
ALZ/GLA01 SHI/MAT98
""",
)

entry(
    index = 48,
    label = "H2S + H <=> SH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.5e+07, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (904, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
PEN/MAR99
""",
)

entry(
    index = 49,
    label = "H2S + O <=> SH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.5e+07, 'cm^3/(mol*s)'),
        n = 1.75,
        Ea = (2900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
ALZ/GLA01 GOU/MAR95
""",
)

entry(
    index = 50,
    label = "H2S + OH <=> SH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
ALZ/GLA01 TYN/RAV91
""",
)

entry(
    index = 51,
    label = "H2S + O2 <=> SH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (280000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (38200, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
MON/HAY05
""",
)

entry(
    index = 52,
    label = "H2S + S <=> SH + SH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
ALZ/GLA01 SHI/MAT96
""",
)

entry(
    index = 53,
    label = "H2S + SO2 <=> S2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+06, 'cm^3/(mol*s)'),
        n = 1.857,
        Ea = (37740, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
*          SEN/HAY05
""",
)

entry(
    index = 54,
    label = "H2S + S2O <=> S3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+07, 'cm^3/(mol*s)'),
        n = 1.506,
        Ea = (33910, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
*          SEN/HAY05
""",
)

entry(
    index = 55,
    label = "S + H <=> SH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(6.2e+16, 'cm^6/(mol^2*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    longDesc = 
u"""
SEN/HAY02 estimated kinetics
""",
)

entry(
    index = 56,
    label = "S + H2 <=> SH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (19300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
ALZ/GLA01 SHI/MAT98
""",
)

entry(
    index = 57,
    label = "SH + O <=> H + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.3e+11, 'cm^3/(mol*s)'),
        n = 0.724,
        Ea = (-1027, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
*          SEN/HAY07
""",
)

entry(
    index = 58,
    label = "SH + O <=> S + OH",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.8e+12, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (0, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.3e+06, 'cm^3/(mol*s)'),
                n = 2.103,
                Ea = (3583, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
*          SEN/HAY07
""",
)

entry(
    index = 59,
    label = "SH + OH <=> S + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
ALZ/GLA01 GLA/BOZ96
""",
)

entry(
    index = 60,
    label = "SH + HO2 <=> HSO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
ALZ/GLA01 GLA/BOZ96
""",
)

entry(
    index = 61,
    label = "SH + O2 <=> HSO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17925, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
ALZ/GLA01 TSU/MAT97
""",
)

entry(
    index = 62,
    label = "SH + O2 <=> HSO2",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=-0.26, Ea=(298, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.3e+14, 'cm^6/(mol^2*s)'),
            n = -0.201,
            Ea = (20, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc = 
u"""
GOU/MAR05
""",
)

entry(
    index = 63,
    label = "SH + SH <=> S2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
ALZ/GLA01 estimated kinetics
""",
)

entry(
    index = 64,
    label = "SH + S <=> S2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
ALZ/GLA01 estimated kinetics
""",
)

entry(
    index = 65,
    label = "S + OH <=> H + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+13, 'cm^3/(mol*s)'),
        n = 0.191,
        Ea = (-1361, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
*          SEN/HAY07
""",
)

entry(
    index = 66,
    label = "S + O2 <=> SO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (540000, 'cm^3/(mol*s)'),
        n = 2.11,
        Ea = (-1450, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
LU/LIN04
""",
)

entry(
    index = 67,
    label = "SO <=> S + O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4e+14, 'cm^3/(mol*s)'), n=0, Ea=(107000, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    longDesc = 
u"""
ALZ/GLA01 PLA/TRO84
""",
)

entry(
    index = 68,
    label = "SO + H <=> HSO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.9e+20, 'cm^6/(mol^2*s)'),
            n = -1.31,
            Ea = (662, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=S=O': 10, 'O': 10, 'N#N': 1.5},
    ),
    longDesc = 
u"""
PM ab initio
""",
)

entry(
    index = 69,
    label = "SO + O <=> SO2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.1e+22, 'cm^6/(mol^2*s)'),
            n = -2.17,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=S=O': 10, 'O': 10, 'N#N': 1.5},
    ),
    longDesc = 
u"""
LULIN03
""",
)

entry(
    index = 70,
    label = "SO + OH <=> SO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+17, 'cm^3/(mol*s)'),
        n = -1.35,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
ALZ/GLA01 BLI/PIL00
""",
)

entry(
    index = 71,
    label = "SO + OH <=> HOSO",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1.6e+12, 'cm^3/(mol*s)'), n=0.5, Ea=(-400, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (9.5e+27, 'cm^6/(mol^2*s)'),
            n = -3.48,
            Ea = (970, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=S=O': 10, 'O': 10, 'N#N': 1.5},
    ),
    longDesc = 
u"""
ALZ/GLA01 GOU/MAR99
""",
)

entry(
    index = 72,
    label = "SO + HO2 <=> SO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3655, 'cm^3/(mol*s)'),
        n = 2.42,
        Ea = (7660, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07
""",
)

entry(
    index = 73,
    label = "SO + O2 <=> SO2 + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7600, 'cm^3/(mol*s)'),
        n = 2.37,
        Ea = (2970, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
ALZ/GLA01 TSU/MAT97
""",
)

#entry(
#    index = 74,
#    label = "SO(S) <=> SO",
#    degeneracy = 1,
#    kinetics = ThirdBody(
#        arrheniusLow = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
#        efficiencies = {},
#    ),
#    longDesc = 
#u"""
#RAS/MAR07
#""",
#)

#entry(
#    index = 75,
#    label = "SO(S) + O2 <=> SO2 + O",
#    degeneracy = 1,
#    kinetics = Arrhenius(
#        A = (1e+13, 'cm^3/(mol*s)'),
#        n = 0,
#        Ea = (0, 'cal/mol'),
#        T0 = (1, 'K'),
#    ),
#    longDesc = 
#u"""
#RAS/MAR07
#""",
#)

entry(
    index = 76,
    label = "SO2 + H <=> HSO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.3e+08, 'cm^3/(mol*s)'),
            n = 1.59,
            Ea = (2470, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.4e+31, 'cm^6/(mol^2*s)'),
            n = -5.19,
            Ea = (4510, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.39,
        T3 = (167, 'K'),
        T1 = (2191, 'K'),
        efficiencies = {'O=S=O': 10, 'O': 10, 'N#N': 1},
    ),
    longDesc = 
u"""
RAS/MAR07 BLI/ROB05
""",
)

entry(
    index = 77,
    label = "SO2 + H <=> HOSO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2.4e+08, 'cm^3/(mol*s)'),
            n = 1.63,
            Ea = (7340, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.8e+37, 'cm^6/(mol^2*s)'),
            n = -6.14,
            Ea = (11070, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.283,
        T3 = (272, 'K'),
        T1 = (3995, 'K'),
        efficiencies = {'O=S=O': 10, 'O': 10, 'N#N': 1},
    ),
    longDesc = 
u"""
RAS/MAR07 BLI/ROB05
""",
)

entry(
    index = 78,
    label = "SO2 + O <=> SO3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.7e+11, 'cm^3/(mol*s)'), n=0, Ea=(1689, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.4e+27, 'cm^6/(mol^2*s)'),
            n = -3.6,
            Ea = (5186, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.442,
        T3 = (316, 'K'),
        T1 = (7442, 'K'),
        efficiencies = {'O=S=O': 10, 'O': 10, 'N#N': 0},
    ),
    longDesc = 
u"""
HIN/MAR06 NAI/MAR04 (Ar)
""",
)

entry(
    index = 79,
    label = "SO2 + O + N2 <=> SO3 + N2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.7e+11, 'cm^6/(mol^2*s)'), n=0, Ea=(1689, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.9e+27, 'cm^9/(mol^3*s)'),
            n = -3.58,
            Ea = (5206, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.43,
        T3 = (371, 'K'),
        T1 = (7442, 'K'),
        efficiencies = {},
    ),
    longDesc = 
u"""
HIN/MAR06 YIL/MAR05
""",
)

entry(
    index = 80,
    label = "SO2 + OH <=> HOSO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.7e+12, 'cm^3/(mol*s)'), n=-0.27, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.7e+27, 'cm^6/(mol^2*s)'),
            n = -4.09,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.1,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'O=S=O': 5, 'O': 5, 'N#N': 1},
    ),
    longDesc = 
u"""
HIN/MAR06 BLI/PIL03
""",
)

entry(
    index = 81,
    label = "SO2 + OH <=> HOSO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.9e+08, 'cm^3/(mol*s)'),
        n = 1.89,
        Ea = (76000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 82,
    label = "SO2 + CO <=> SO + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (65900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 BAC/MAC05
""",
)

entry(
    index = 83,
    label = "SO2 + S <=> SO + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e-16, 'cm^3/(mol*s)'),
        n = 8.21,
        Ea = (9600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 MUR/MAT03
""",
)

entry(
    index = 84,
    label = "SO2 + SO2 <=> SO3 + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (75000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
HIN/MAR06 estimated kinetics
""",
)

entry(
    index = 85,
    label = "SO3 + H <=> SO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.4e+09, 'cm^3/(mol*s)'),
        n = 1.22,
        Ea = (3320, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
HIN/MAR06
""",
)

entry(
    index = 86,
    label = "SO3 + H <=> HOSO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (250000, 'cm^3/(mol*s)'),
        n = 2.92,
        Ea = (50300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
HIN/MAR06 GLA/BOZ96
""",
)

entry(
    index = 87,
    label = "SO3 + O <=> SO2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.57,
        Ea = (29200, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
HIN/MAR06
""",
)

entry(
    index = 88,
    label = "SO3 + OH <=> SO2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (48000, 'cm^3/(mol*s)'),
        n = 2.46,
        Ea = (27250, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
HIN/MAR06
""",
)

entry(
    index = 89,
    label = "HSO <=> HOS",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(5.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(32720, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'N#N': 0},
    ),
    longDesc = 
u"""
SEN/HAY07 (Ar)
""",
)

entry(
    index = 90,
    label = "HSO + N2 <=> HOS + N2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (24600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
SEN/HAY07
""",
)

#entry(
#    index = 91,
#    label = "HSO + H <=> SO(S) + H2",
#    degeneracy = 1,
#    kinetics = Arrhenius(
#        A = (1e+13, 'cm^3/(mol*s)'),
#        n = 0,
#        Ea = (0, 'cal/mol'),
#        T0 = (1, 'K'),
#    ),
#    longDesc = 
#u"""
#RAS/MAR07 estimated kinetics (UL?)
#""",
#)

#entry(
#    index = 92,
#    label = "HSO + OH <=> SO(S) + H2O",
#    degeneracy = 1,
#    kinetics = Arrhenius(
#        A = (1e+13, 'cm^3/(mol*s)'),
#        n = 0,
#        Ea = (0, 'cal/mol'),
#        T0 = (1, 'K'),
#    ),
#    longDesc = 
#u"""
#RAS/MAR07 estimated kinetics (UL?)
#""",
#)

entry(
    index = 93,
    label = "HSO + H <=> HSOH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+20, 'cm^3/(mol*s)'),
        n = -3.14,
        Ea = (920, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 94,
    label = "HSO + H <=> SH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.9e+19, 'cm^3/(mol*s)'),
        n = -1.86,
        Ea = (1560, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 95,
    label = "HSO + H <=> S + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+09, 'cm^3/(mol*s)'),
        n = 1.37,
        Ea = (-340, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 96,
    label = "HSO + H <=> H2SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+17, 'cm^3/(mol*s)'),
        n = -2.47,
        Ea = (50, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 97,
    label = "HSO + H <=> H2S + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+06, 'cm^3/(mol*s)'),
        n = 1.03,
        Ea = (10400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 98,
    label = "HSO + H <=> SO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 estimated kinetics
""",
)

entry(
    index = 99,
    label = "HSO + O <=> HSO2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.1e+19, 'cm^6/(mol^2*s)'),
            n = -1.73,
            Ea = (-50, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 100,
    label = "HSO + O <=> SO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.5e+14, 'cm^3/(mol*s)'),
        n = -0.4,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 101,
    label = "HSO + O <=> HOSO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6.9e+19, 'cm^6/(mol^2*s)'),
            n = -1.61,
            Ea = (1590, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 102,
    label = "HSO + O <=> O + HOS",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.8e+08, 'cm^3/(mol*s)'),
        n = 1.02,
        Ea = (5340, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 103,
    label = "HSO + O <=> OH + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+13, 'cm^3/(mol*s)'),
        n = 0.15,
        Ea = (300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 104,
    label = "HSO + OH <=> HOSHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.2e+28, 'cm^3/(mol*s)'),
        n = -5.44,
        Ea = (3170, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 105,
    label = "HSO + OH <=> HOSO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.3e+07, 'cm^3/(mol*s)'),
        n = 1.57,
        Ea = (3750, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 106,
    label = "HSO + OH <=> SO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+09, 'cm^3/(mol*s)'),
        n = 1.03,
        Ea = (470, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96 see reverse
""",
)

entry(
    index = 107,
    label = "HSO + O2 <=> HSO2 + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.4e-07, 'cm^3/(mol*s)'),
        n = 5.1,
        Ea = (11312, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07
""",
)

entry(
    index = 108,
    label = "HSOH <=> SH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+39, 's^-1'),
        n = -8.75,
        Ea = (75200, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 109,
    label = "HSOH <=> S + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.8e+29, 's^-1'),
        n = -5.6,
        Ea = (54500, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 110,
    label = "HSOH <=> H2S + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.8e+16, 's^-1'),
        n = -3.4,
        Ea = (86500, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 111,
    label = "HOSO <=> HSO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+09, 's^-1'), n=1.03, Ea=(50000, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.7e+35, 'cm^3/(mol*s)'),
            n = -5.64,
            Ea = (55400, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.4,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'O=S=O': 10, 'O': 10, 'N#N': 1},
    ),
    longDesc = 
u"""
RAS/MAR07 GOU/MAR99
""",
)

entry(
    index = 112,
    label = "HOSO <=> O + HOS",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (2.5e+30, 'cm^3/(mol*s)'),
            n = -4.8,
            Ea = (119000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 113,
    label = "HOSO + H <=> SO2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+07, 'cm^3/(mol*s)'),
        n = 1.72,
        Ea = (-1286, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 HU/MAR05
""",
)

entry(
    index = 114,
    label = "HOSO + H <=> SO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 HU/MAR05
Original reaction: HOSO + H <=> SO(S) + H2O
""",
)

entry(
    index = 115,
    label = "HOSO + OH <=> SO2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 rough estimated kinetics
""",
)

entry(
    index = 116,
    label = "HOSO + O2 <=> HO2 + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (96, 'cm^3/(mol*s)'),
        n = 2.355,
        Ea = (-10130, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 (T>400K)
""",
)

entry(
    index = 117,
    label = "HSO2 + H <=> SO2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0.46,
        Ea = (-262, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 HU/MAR05
""",
)

entry(
    index = 118,
    label = "HSO2 + OH <=> SO2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 ALZ/GLA01 estimated kinetics
""",
)

entry(
    index = 119,
    label = "HSO2 + O2 <=> HO2 + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1100, 'cm^3/(mol*s)'),
        n = 3.2,
        Ea = (-235, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 ab initio
""",
)

entry(
    index = 120,
    label = "H2SO <=> H2S + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.9e+28, 's^-1'),
        n = -6.66,
        Ea = (71700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 121,
    label = "HOSHO <=> HOSO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.4e+30, 's^-1'),
        n = -5.89,
        Ea = (73800, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 122,
    label = "HOSHO <=> SO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+24, 's^-1'),
        n = -3.59,
        Ea = (59500, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 123,
    label = "HOSHO + H <=> HOSO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 124,
    label = "HOSHO + O <=> HOSO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 125,
    label = "HOSHO + OH <=> HOSO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 126,
    label = "HOSO2 <=> HOSO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.4e+18, 's^-1'),
        n = -2.34,
        Ea = (106300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 127,
    label = "HOSO2 <=> SO3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+18, 's^-1'),
        n = -2.91,
        Ea = (54900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 128,
    label = "HOSO2 + H <=> SO2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 129,
    label = "HOSO2 + O <=> SO3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 130,
    label = "HOSO2 + OH <=> SO3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 GLA/BOZ96
""",
)

entry(
    index = 131,
    label = "HOSO2 + O2 <=> HO2 + SO3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.8e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (656, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
RAS/MAR07 ATK/TRO92
""",
)

entry(
    index = 132,
    label = "S2 <=> S + S",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(77000, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    longDesc = 
u"""
ALZ/GLA01 HIG/MUR80
""",
)

entry(
    index = 133,
    label = "S2 + H <=> HSS",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.2e+25, 'cm^6/(mol^2*s)'),
            n = -2.84,
            Ea = (1665, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc = 
u"""
SEN/HAY02
""",
)

entry(
    index = 134,
    label = "S2 + O <=> SO + S",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
ALZ/GLA01 SIN/CVE88
""",
)

entry(
    index = 135,
    label = "HSS + H <=> SH + SH",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (9.7e+07, 'cm^3/(mol*s)'),
                n = 1.62,
                Ea = (-1030, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.1e+13, 'cm^3/(mol*s)'),
                n = 0.353,
                Ea = (210, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
SEN/HAY02
""",
)

entry(
    index = 136,
    label = "HSS + H <=> S2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+08, 'cm^3/(mol*s)'),
        n = 1.653,
        Ea = (-1105, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
SEN/HAY02
""",
)

entry(
    index = 137,
    label = "HSS + H <=> H2S + S",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6326, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
SEN/HAY02
""",
)

entry(
    index = 138,
    label = "HSS + O <=> S2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.5e+07, 'cm^3/(mol*s)'),
        n = 1.75,
        Ea = (2900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
ALZ/GLA01 estimated kinetics h2s+o
""",
)

entry(
    index = 139,
    label = "HSS + OH <=> S2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
ALZ/GLA01 estimated kinetics h2s+oh
""",
)

entry(
    index = 140,
    label = "HSS + S <=> S2 + SH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+06, 'cm^3/(mol*s)'),
        n = 2.2,
        Ea = (-600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
SEN/HAY02
""",
)

entry(
    index = 141,
    label = "HSS + SH <=> H2S + S2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6300, 'cm^3/(mol*s)'),
        n = 3.05,
        Ea = (-1105, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
SEN/HAY02
""",
)

entry(
    index = 142,
    label = "HSS + HSS <=> HSSH + S2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6, 'cm^3/(mol*s)'),
        n = 3.37,
        Ea = (-1672, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
SEN/HAY02
""",
)

entry(
    index = 143,
    label = "HSSH <=> SH + SH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(6.9e+14, 'cm^3/(mol*s)'), n=1, Ea=(57030, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    longDesc = 
u"""
SEN/HAY02
""",
)

entry(
    index = 144,
    label = "HSSH + H <=> HSS + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+07, 'cm^3/(mol*s)'),
        n = 1.933,
        Ea = (-1408, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
SEN/HAY02
""",
)

entry(
    index = 145,
    label = "HSSH + H <=> H2S + SH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
SEN/HAY02
""",
)

entry(
    index = 146,
    label = "HSSH + O <=> HSS + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.5e+07, 'cm^3/(mol*s)'),
        n = 1.75,
        Ea = (2900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
ALZ/GLA01 estimated kinetics h2s+o
""",
)

entry(
    index = 147,
    label = "HSSH + OH <=> HSS + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
ALZ/GLA01 estimated kinetics h2s+oh
""",
)

entry(
    index = 148,
    label = "HSSH + S <=> HSS + SH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+06, 'cm^3/(mol*s)'),
        n = 2.31,
        Ea = (1204, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
SEN/HAY02
""",
)

entry(
    index = 149,
    label = "HSSH + SH <=> HSS + H2S",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6400, 'cm^3/(mol*s)'),
        n = 2.98,
        Ea = (-1480, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
SEN/HAY02
""",
)

