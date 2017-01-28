#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/GlarborgBozzelli"
shortDesc = u"SOx, HSxOx, HxS, and SOx-NOx reactions"
longDesc = u"""
Contains: SOx, HSxOy, HxS, SOx-NOx

The effect of SO2 on moist CO oxidation with and without NO

Taken from:
Impact of SO2 and NO on CO oxidation under post-flame conditions
Peter Glarborg, Dorte Kubel, Kim Dam-Johansen, Hong-Ming Chiang, Joseph W. Bozzelli
International Journal of Chemical Kinetics, 28 (1996) 773-790
DOI: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
"""

entry(
    index = 1,
    label = "SO3 + H <=> HOSO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+05, 'cm^3/(mol*s)'),
        n = 2.92,
        Ea = (50.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [45]
""",
)

entry(
    index = 2,
    label = "SO3 + O <=> SO2 + O2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.3e+12, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (6.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
[59]
""",
)

entry(
    index = 3,
    label = "SO3 + SO <=> SO2 + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.0e+12, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (4.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
[65], activation energy estimated
""",
)

entry(
    index = 4,
    label = "SO2 + O <=> SO3",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.0e+28, 'cm^6/(mol^2*s)'),
            n = -4.00,
            Ea = (5.25, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'N#N': 1.3, 'O': 10},
    ),
    longDesc = 
u"""
[56]
""",
)

entry(
    index = 5,
    label = "SO2 + OH <=> HOSO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.0e+25, 'cm^3/(mol*s)'),
        n = -4.34,
        Ea = (3.05, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [45]
""",
)

entry(
    index = 6,
    label = "SO2 + OH <=> HOSO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.9e+08, 'cm^3/(mol*s)'),
        n = 1.89,
        Ea = (76.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [45]
""",
)

entry(
    index = 7,
    label = "SO2 + OH <=> SO3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.9e+02, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (23.8, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [45]
""",
)

entry(
    index = 8,
    label = "SO2 + CO <=> SO + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+12, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (48.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
[66]
""",
)

entry(
    index = 9,
    label = "SO <=> S + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.0e+14, 's^-1'),
        n = 0.00,
        Ea = (107.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
[67]
""",
)

entry(
    index = 10,
    label = "SO + H <=> HSO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.0e+15, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Rate constant estimated
""",
)

entry(
    index = 11,
    label = "SO + O <=> SO2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.1e+22, 'cm^6/(mol^2*s)'),
            n = -1.84,
            Ea = (0, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'N#N': 1.5, 'O': 10},
    ),
    longDesc = 
u"""
[68]
""",
)

entry(
    index = 12,
    label = "SO + OH <=> SO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.2e+13, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
[69]
""",
)

entry(
    index = 13,
    label = "SO + OH <=> HOSO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.0e+21, 'cm^3/(mol*s)'),
        n = -2.16,
        Ea = (0.83, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [35]
""",
)

entry(
    index = 14,
    label = "SO + O2 <=> SO2 + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.2e+03, 'cm^3/(mol*s)'),
        n = 2.42,
        Ea = (3.05, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
[39,70]
""",
)

entry(
    index = 15,
    label = "SO + SO <=> SO2 + S",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.0e+12, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (4.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
[71], activation energy estimated
""",
)

entry(
    index = 16,
    label = "HSO + H <=> HSOH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+20, 'cm^3/(mol*s)'),
        n = -3.14,
        Ea = (0.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [45]
""",
)

entry(
    index = 17,
    label = "HSO + H <=> SH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.9e+19, 'cm^3/(mol*s)'),
        n = -1.86,
        Ea = (1.56, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [45]
""",
)

entry(
    index = 18,
    label = "HSO + H <=> S + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+09, 'cm^3/(mol*s)'),
        n = 1.37,
        Ea = (-0.34, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [45]
""",
)

entry(
    index = 19,
    label = "HSO + H <=> H2SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+17, 'cm^3/(mol*s)'),
        n = -2.47,
        Ea = (0.05, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [45]
""",
)

entry(
    index = 20,
    label = "HSO + H <=> H2S + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+06, 'cm^3/(mol*s)'),
        n = 1.03,
        Ea = (10.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [45]
""",
)

entry(
    index = 21,
    label = "HSO + H <=> SO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.0e+12, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (0.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
rate constant estimated
""",
)

entry(
    index = 22,
    label = "HSO + O <=> SO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.5e+14, 'cm^3/(mol*s)'),
        n = -0.40,
        Ea = (0.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [35]
""",
)

entry(
    index = 23,
    label = "HSO + O <=> HOS + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.8e+08, 'cm^3/(mol*s)'),
        n = 1.02,
        Ea = (5.34, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [35]
""",
)

entry(
    index = 24,
    label = "HSO + O <=> SO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+13, 'cm^3/(mol*s)'),
        n = 0.15,
        Ea = (0.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [35]
""",
)

entry(
    index = 25,
    label = "HSO + O <=> HOSO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.9e+19, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1.59, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [35]
""",
)

entry(
    index = 26,
    label = "HSO + O <=> HSO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+19, 'cm^3/(mol*s)'),
        n = -1.73,
        Ea = (-0.05, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [35]
""",
)

entry(
    index = 27,
    label = "HSO + OH <=> HOSHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.2e+28, 'cm^3/(mol*s)'),
        n = -5.44,
        Ea = (3.17, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [45]
""",
)

entry(
    index = 28,
    label = "HSO + OH <=> HOSO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.3e+07, 'cm^3/(mol*s)'),
        n = 1.57,
        Ea = (3.75, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [45]
Typo in paper (HOSO, not HOSHO)
""",
)

entry(
    index = 29,
    label = "HSO + OH <=> SO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+09, 'cm^3/(mol*s)'),
        n = 1.03,
        Ea = (0.47, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [45]
""",
)

entry(
    index = 30,
    label = "HSO + O2 <=> SO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.0e+12, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (10, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
rate constant estimated
""",
)

entry(
    index = 31,
    label = "HSOH <=> SH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+39, 's^-1'),
        n = -8.75,
        Ea = (75.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [45]
""",
)

entry(
    index = 32,
    label = "HSOH <=> S + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.8e+29, 's^-1'),
        n = -5.60,
        Ea = (54.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [45]
""",
)

entry(
    index = 33,
    label = "HSOH <=> H2S + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.8e+16, 's^-1'),
        n = -3.40,
        Ea = (86.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [45]
""",
)

entry(
    index = 34,
    label = "H2SO <=> H2S + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.9e+28, 's^-1'),
        n = -6.66,
        Ea = (71.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [45]
""",
)

entry(
    index = 35,
    label = "HOSO <=> HOS + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+30, 's^-1'),
        n = -4.80,
        Ea = (119.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [35]
""",
)

entry(
    index = 36,
    label = "HOSO <=> SO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.9e+34, 's^-1'),
        n = -5.67,
        Ea = (50.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [35]
""",
)

entry(
    index = 37,
    label = "HOSO + H <=> SO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e-10, 'cm^3/(mol*s)'),
        n = 6.29,
        Ea = (-1.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [45]
""",
)

entry(
    index = 38,
    label = "HOSO + OH <=> SO2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.0e+12, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (0.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
rate constant estimated
""",
)

entry(
    index = 39,
    label = "HOSO + O2 <=> SO2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.0e+12, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (1.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
[39]
""",
)

entry(
    index = 40,
    label = "HSO2 <=> SO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+28, 's^-1'),
        n = -4.14,
        Ea = (18.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [35]
""",
)

entry(
    index = 41,
    label = "HSO2 <=> HOSO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+21, 's^-1'),
        n = -1.99,
        Ea = (29.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [35]
""",
)

entry(
    index = 42,
    label = "HOSO2 <=> HOSO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.4e+18, 's^-1'),
        n = -2.34,
        Ea = (106.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [45]
""",
)

entry(
    index = 43,
    label = "HOSO2 <=> SO3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+18, 's^-1'),
        n = -2.91,
        Ea = (54.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [45]
""",
)

entry(
    index = 44,
    label = "HOSO2 + H <=> SO2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.0e+12, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (0.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
rate constant estimated
""",
)

entry(
    index = 45,
    label = "HOSO2 + O <=> SO3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.0e+12, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (0.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
rate constant estimated
""",
)

entry(
    index = 46,
    label = "HOSO2 + OH <=> SO3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.0e+12, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (0.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
rate constant estimated
""",
)

entry(
    index = 47,
    label = "HOSO2 + O2 <=> SO3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.8e+11, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (0.656, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
[39]
""",
)

entry(
    index = 48,
    label = "HOSHO <=> HOSO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.4e+30, 's^-1'),
        n = -5.89,
        Ea = (73.8, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [45]
""",
)

entry(
    index = 49,
    label = "HOSHO <=> SO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+24, 's^-1'),
        n = -3.59,
        Ea = (59.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
QRRK estimate for 300-1500 K, 1 atm [45]
""",
)

entry(
    index = 50,
    label = "HOSHO + H <=> HOSO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.0e+12, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (0.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
rate constant estimated
""",
)

entry(
    index = 51,
    label = "HOSHO + O <=> HOSO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.0e+12, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (0.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
rate constant estimated
""",
)

entry(
    index = 52,
    label = "HOSHO + OH <=> HOSO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.0e+12, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (0.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
rate constant estimated
""",
)

entry(
    index = 53,
    label = "H2S <=> S + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.0e+14, 's^-1'),
        n = 0.00,
        Ea = (66.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
[72,73]
""",
)

entry(
    index = 54,
    label = "H2S + H <=> SH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+07, 'cm^3/(mol*s)'),
        n = 2.10,
        Ea = (0.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
[74]
""",
)

entry(
    index = 55,
    label = "H2S + O <=> SH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.4e+07, 'cm^3/(mol*s)'),
        n = 1.78,
        Ea = (2.84, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
[39,75]
""",
)

entry(
    index = 56,
    label = "H2S + OH <=> SH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+12, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (0.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
[76]
""",
)

entry(
    index = 57,
    label = "H2S + S <=> SH + SH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.0e+14, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (15.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
[77]
""",
)

entry(
    index = 58,
    label = "S + H2 <=> SH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.0e+14, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (24.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
[77]
""",
)

entry(
    index = 59,
    label = "SH + O <=> SO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.0e+14, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (0.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
[69,75]
""",
)

entry(
    index = 60,
    label = "SH + OH <=> S + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.0e+13, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (0.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
rate constant estimated
""",
)

entry(
    index = 61,
    label = "SH + HO2 <=> HSO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.0e+12, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (0.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
rate constant estimated
""",
)

entry(
    index = 62,
    label = "SH + O2 <=> SO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.0e+12, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (10.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
rate constant estimated
""",
)

entry(
    index = 63,
    label = "S + OH <=> SO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.0e+13, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (10.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
[69]
""",
)

entry(
    index = 64,
    label = "S + O2 <=> SO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.0e+06, 'cm^3/(mol*s)'),
        n = 1.93,
        Ea = (-1.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
[39,70]
""",
)

entry(
    index = 65,
    label = "SO + NO2 <=> SO2 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.4e+12, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (0.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
[39]
""",
)

entry(
    index = 66,
    label = "SO2 + NO2 <=> SO3 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+12, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (27.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
[78]
""",
)

entry(
    index = 67,
    label = "HSO + NO2 <=> HOSO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.8e+12, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (0.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
[39]
""",
)

