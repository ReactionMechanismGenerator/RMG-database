#!/usr/bin/env python
# encoding: utf-8

name = "GRI-Mech3.0-N"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "O(T) + H2 <=> H + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(38700, 'cm^3/(mol*s)'), n=2.7, Ea=(6260, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "O(T) + HO2 <=> OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "O(T) + H2O2 <=> OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.63e+06, 'cm^3/(mol*s)'), n=2, Ea=(4000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "O(T) + CH <=> H + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 5,
    label = "O(T) + CH2(T) <=> H + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "O(T) + CH2(S) <=> H2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "O(T) + CH2(S) <=> H + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 8,
    label = "O(T) + CH3 <=> H + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.06e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 9,
    label = "O(T) + CH4 <=> OH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (8600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 10,
    label = "O(T) + HCO <=> OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 11,
    label = "O(T) + HCO <=> H + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 12,
    label = "O(T) + CH2O <=> OH + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.9e+13, 'cm^3/(mol*s)'), n=0, Ea=(3540, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "O(T) + CH2OH <=> OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 14,
    label = "O(T) + CH3O <=> OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 15,
    label = "O(T) + CH3OH <=> OH + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(388000, 'cm^3/(mol*s)'), n=2.5, Ea=(3100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 16,
    label = "O(T) + CH3OH <=> OH + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(130000, 'cm^3/(mol*s)'), n=2.5, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 17,
    label = "O(T) + C2H <=> CH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 18,
    label = "O(T) + C2H2 <=> H + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.35e+07, 'cm^3/(mol*s)'), n=2, Ea=(1900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 19,
    label = "O(T) + C2H2 <=> OH + C2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6e+19, 'cm^3/(mol*s)'),
        n = -1.41,
        Ea = (28950, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 20,
    label = "O(T) + C2H2 <=> CO + CH2(T)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.94e+06, 'cm^3/(mol*s)'), n=2, Ea=(1900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 21,
    label = "O(T) + C2H3 <=> H + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 22,
    label = "O(T) + C2H4 <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.25e+07, 'cm^3/(mol*s)'),
        n = 1.83,
        Ea = (220, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 23,
    label = "O(T) + C2H5 <=> CH3 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.24e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 24,
    label = "O(T) + C2H6 <=> OH + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.98e+07, 'cm^3/(mol*s)'),
        n = 1.92,
        Ea = (5690, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 25,
    label = "O(T) + HCCO <=> H + CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 26,
    label = "O(T) + CH2CO <=> OH + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(8000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 27,
    label = "O(T) + CH2CO <=> CH2(T) + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+12, 'cm^3/(mol*s)'), n=0, Ea=(1350, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 28,
    label = "O2 + CO <=> O + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(47800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 29,
    label = "O2 + CH2O <=> HO2 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(40000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 30,
    label = "H + O2 + O2 <=> HO2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.08e+19, 'cm^6/(mol^2*s)'),
        n = -1.24,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 31,
    label = "H + O2 + H2O <=> HO2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.126e+19, 'cm^6/(mol^2*s)'),
        n = -0.76,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 32,
    label = "H + O2 + N2 <=> HO2 + N2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+19, 'cm^6/(mol^2*s)'),
        n = -1.24,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 33,
    label = "H + O2 <=> O(T) + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.65e+16, 'cm^3/(mol*s)'),
        n = -0.6707,
        Ea = (17041, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 34,
    label = "H + H + H2 <=> H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+16, 'cm^6/(mol^2*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 35,
    label = "H + H + H2O <=> H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+19, 'cm^6/(mol^2*s)'), n=-1.25, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 36,
    label = "H + H + CO2 <=> H2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.5e+20, 'cm^6/(mol^2*s)'), n=-2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 37,
    label = "H + HO2 <=> O(T) + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.97e+12, 'cm^3/(mol*s)'), n=0, Ea=(671, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 38,
    label = "H + HO2 <=> O2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.48e+13, 'cm^3/(mol*s)'), n=0, Ea=(1068, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 39,
    label = "H + HO2 <=> OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(635, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 40,
    label = "H + H2O2 <=> HO2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+07, 'cm^3/(mol*s)'), n=2, Ea=(5200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 41,
    label = "H + H2O2 <=> OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(3600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 42,
    label = "H + CH <=> C(T) + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.65e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 43,
    label = "H + CH2(S) <=> CH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 44,
    label = "H + CH4 <=> CH3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.6e+08, 'cm^3/(mol*s)'),
        n = 1.62,
        Ea = (10840, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 45,
    label = "H + HCO <=> H2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.34e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 46,
    label = "H + CH2O <=> HCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.74e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (2742, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 47,
    label = "H + CH2OH <=> H2 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 48,
    label = "H + CH2OH <=> OH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.65e+11, 'cm^3/(mol*s)'),
        n = 0.65,
        Ea = (-284, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 49,
    label = "H + CH2OH <=> CH2(S) + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.28e+13, 'cm^3/(mol*s)'),
        n = -0.09,
        Ea = (610, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 50,
    label = "H + CH3O <=> H + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.15e+07, 'cm^3/(mol*s)'),
        n = 1.63,
        Ea = (1924, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 51,
    label = "H + CH3O <=> H2 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 52,
    label = "H + CH3O <=> OH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0.5, Ea=(-110, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 53,
    label = "H + CH3O <=> CH2(S) + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.62e+14, 'cm^3/(mol*s)'),
        n = -0.23,
        Ea = (1070, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 54,
    label = "H + CH3OH <=> CH2OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+07, 'cm^3/(mol*s)'), n=2.1, Ea=(4870, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 55,
    label = "H + CH3OH <=> CH3O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.2e+06, 'cm^3/(mol*s)'), n=2.1, Ea=(4870, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 56,
    label = "H + C2H3 <=> H2 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 57,
    label = "H + C2H4 <=> C2H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.325e+06, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (12240, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 58,
    label = "H + C2H5 <=> H2 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 59,
    label = "H + C2H6 <=> C2H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15e+08, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (7530, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 60,
    label = "H + HCCO <=> CH2(S) + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 61,
    label = "H + CH2CO <=> HCCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(8000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 62,
    label = "H + CH2CO <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(3428, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 63,
    label = "H + HCCOH <=> H + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 64,
    label = "OH + H2 <=> H + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.16e+08, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (3430, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 65,
    label = "OH + OH <=> O(T) + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(35700, 'cm^3/(mol*s)'), n=2.4, Ea=(-2110, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 66,
    label = "OH + HO2 <=> O2 + H2O",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.45e+13, 'cm^3/(mol*s)'), n=0, Ea=(-500, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5e+15, 'cm^3/(mol*s)'), n=0, Ea=(17330, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 67,
    label = "OH + H2O2 <=> HO2 + H2O",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(427, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.7e+18, 'cm^3/(mol*s)'), n=0, Ea=(29410, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 69,
    label = "OH + C(T) <=> H + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 70,
    label = "OH + CH <=> H + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 71,
    label = "OH + CH2(T) <=> H + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 72,
    label = "OH + CH2(T) <=> CH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+07, 'cm^3/(mol*s)'), n=2, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 73,
    label = "OH + CH2(S) <=> H + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 74,
    label = "OH + CH3 <=> CH2(T) + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+07, 'cm^3/(mol*s)'), n=1.6, Ea=(5420, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 75,
    label = "OH + CH3 <=> CH2(S) + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.44e+17, 'cm^3/(mol*s)'),
        n = -1.34,
        Ea = (1417, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 76,
    label = "OH + CH4 <=> CH3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+08, 'cm^3/(mol*s)'), n=1.6, Ea=(3120, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 77,
    label = "OH + CO <=> H + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.76e+07, 'cm^3/(mol*s)'),
        n = 1.228,
        Ea = (70, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 78,
    label = "OH + HCO <=> H2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 79,
    label = "OH + CH2O <=> HCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.43e+09, 'cm^3/(mol*s)'),
        n = 1.18,
        Ea = (-447, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 80,
    label = "OH + CH2OH <=> H2O + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 81,
    label = "OH + CH3O <=> H2O + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 82,
    label = "OH + CH3OH <=> CH2OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.44e+06, 'cm^3/(mol*s)'), n=2, Ea=(-840, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 83,
    label = "OH + CH3OH <=> CH3O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+06, 'cm^3/(mol*s)'), n=2, Ea=(1500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 84,
    label = "OH + C2H <=> H + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 85,
    label = "OH + C2H2 <=> H + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000218, 'cm^3/(mol*s)'),
        n = 4.5,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 86,
    label = "OH + C2H2 <=> H + HCCOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(504000, 'cm^3/(mol*s)'), n=2.3, Ea=(13500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 87,
    label = "OH + C2H2 <=> C2H + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.37e+07, 'cm^3/(mol*s)'), n=2, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 88,
    label = "OH + C2H2 <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.000483, 'cm^3/(mol*s)'), n=4, Ea=(-2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 89,
    label = "OH + C2H3 <=> H2O + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 90,
    label = "OH + C2H4 <=> C2H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+06, 'cm^3/(mol*s)'), n=2, Ea=(2500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 91,
    label = "OH + C2H6 <=> C2H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.54e+06, 'cm^3/(mol*s)'),
        n = 2.12,
        Ea = (870, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 92,
    label = "OH + CH2CO <=> HCCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 93,
    label = "HO2 + HO2 <=> O2 + H2O2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.3e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1630, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.2e+14, 'cm^3/(mol*s)'), n=0, Ea=(12000, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 95,
    label = "HO2 + CH2(T) <=> OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 96,
    label = "HO2 + CH3 <=> O2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 97,
    label = "HO2 + CH3 <=> OH + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.78e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 98,
    label = "HO2 + CO <=> OH + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+14, 'cm^3/(mol*s)'), n=0, Ea=(23600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 99,
    label = "HO2 + CH2O <=> HCO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+06, 'cm^3/(mol*s)'), n=2, Ea=(12000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 100,
    label = "C(T) + O2 <=> O(T) + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(576, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 101,
    label = "C(T) + CH2(T) <=> H + C2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 102,
    label = "C(T) + CH3 <=> H + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 103,
    label = "CH + O2 <=> O(T) + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.71e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 104,
    label = "CH + H2 <=> H + CH2(T)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.08e+14, 'cm^3/(mol*s)'), n=0, Ea=(3110, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 105,
    label = "CH + H2O <=> H + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.71e+12, 'cm^3/(mol*s)'), n=0, Ea=(-755, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 106,
    label = "CH + CH2(T) <=> H + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 107,
    label = "CH + CH3 <=> H + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 108,
    label = "CH + CH4 <=> H + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 109,
    label = "CH + CO2 <=> HCO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+14, 'cm^3/(mol*s)'), n=0, Ea=(15792, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 110,
    label = "CH + CH2O <=> H + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.46e+13, 'cm^3/(mol*s)'), n=0, Ea=(-515, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 111,
    label = "CH + HCCO <=> CO + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 112,
    label = "CH2(T) + O2 => OH + H + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(1500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 113,
    label = "CH2(T) + H2 <=> H + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(500000, 'cm^3/(mol*s)'), n=2, Ea=(7230, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 114,
    label = "CH2(T) + CH2(T) <=> H2 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+15, 'cm^3/(mol*s)'), n=0, Ea=(11944, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 115,
    label = "CH2(T) + CH3 <=> H + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 116,
    label = "CH2(T) + CH4 <=> CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.46e+06, 'cm^3/(mol*s)'), n=2, Ea=(8270, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 117,
    label = "CH2(T) + HCCO <=> C2H3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 118,
    label = "CH2(S) + N2 <=> CH2(T) + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 119,
    label = "CH2(S) + O2 <=> H + OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 120,
    label = "CH2(S) + O2 <=> CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 121,
    label = "CH2(S) + H2 <=> CH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 122,
    label = "CH2(S) + H2O <=> CH2(T) + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 123,
    label = "CH2(S) + CH3 <=> H + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(-570, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 124,
    label = "CH2(S) + CH4 <=> CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(-570, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 125,
    label = "CH2(S) + CO <=> CH2(T) + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 126,
    label = "CH2(S) + CO2 <=> CH2(T) + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 127,
    label = "CH2(S) + CO2 <=> CO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 128,
    label = "CH2(S) + C2H6 <=> CH3 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(-550, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 129,
    label = "CH3 + O2 <=> O(T) + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.56e+13, 'cm^3/(mol*s)'), n=0, Ea=(30480, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 130,
    label = "CH3 + O2 <=> OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.31e+12, 'cm^3/(mol*s)'), n=0, Ea=(20315, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 131,
    label = "CH3 + H2O2 <=> HO2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(24500, 'cm^3/(mol*s)'), n=2.47, Ea=(5180, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 132,
    label = "CH3 + CH3 <=> H + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.84e+12, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (10600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 133,
    label = "CH3 + HCO <=> CH4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.648e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 134,
    label = "CH3 + CH2O <=> HCO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3320, 'cm^3/(mol*s)'), n=2.81, Ea=(5860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 135,
    label = "CH3 + CH3OH <=> CH2OH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+07, 'cm^3/(mol*s)'), n=1.5, Ea=(9940, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 136,
    label = "CH3 + CH3OH <=> CH3O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+07, 'cm^3/(mol*s)'), n=1.5, Ea=(9940, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 137,
    label = "CH3 + C2H4 <=> C2H3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(227000, 'cm^3/(mol*s)'), n=2, Ea=(9200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 138,
    label = "CH3 + C2H6 <=> C2H5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.14e+06, 'cm^3/(mol*s)'),
        n = 1.74,
        Ea = (10450, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 139,
    label = "HCO + H2O <=> H + CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+18, 'cm^3/(mol*s)'), n=-1, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 140,
    label = "HCO + O2 <=> HO2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.345e+13, 'cm^3/(mol*s)'), n=0, Ea=(400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 141,
    label = "CH2OH + O2 <=> HO2 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 142,
    label = "CH3O + O2 <=> HO2 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.28e-13, 'cm^3/(mol*s)'),
        n = 7.6,
        Ea = (-3530, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 143,
    label = "C2H + O2 <=> HCO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(-755, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 144,
    label = "C2H + H2 <=> H + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.68e+10, 'cm^3/(mol*s)'),
        n = 0.9,
        Ea = (1993, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 145,
    label = "C2H3 + O2 <=> HCO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.58e+16, 'cm^3/(mol*s)'),
        n = -1.39,
        Ea = (1015, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 146,
    label = "C2H5 + O2 <=> HO2 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.4e+11, 'cm^3/(mol*s)'), n=0, Ea=(3875, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 147,
    label = "HCCO + O2 <=> OH + CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(854, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 148,
    label = "HCCO + HCCO <=> CO + CO + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 149,
    label = "N + NO <=> N2 + O(T)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(355, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 150,
    label = "N + O2 <=> NO + O(T)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+09, 'cm^3/(mol*s)'), n=1, Ea=(6500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 151,
    label = "N + OH <=> NO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.36e+13, 'cm^3/(mol*s)'), n=0, Ea=(385, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 152,
    label = "N2O + O(T) <=> N2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 153,
    label = "N2O + O(T) <=> NO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+13, 'cm^3/(mol*s)'), n=0, Ea=(23150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 154,
    label = "N2O + H <=> N2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.87e+14, 'cm^3/(mol*s)'), n=0, Ea=(18880, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 155,
    label = "N2O + OH <=> N2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(21060, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 156,
    label = "HO2 + NO <=> NO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.11e+12, 'cm^3/(mol*s)'), n=0, Ea=(-480, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 157,
    label = "NO2 + O(T) <=> NO + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-240, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 158,
    label = "NO2 + H <=> NO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.32e+14, 'cm^3/(mol*s)'), n=0, Ea=(360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 159,
    label = "NH + O(T) <=> NO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 160,
    label = "NH + H <=> N + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(330, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 161,
    label = "NH + OH <=> HNO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 162,
    label = "NH + OH <=> N + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+09, 'cm^3/(mol*s)'), n=1.2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 163,
    label = "NH + O2 <=> HNO + O(T)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(461000, 'cm^3/(mol*s)'), n=2, Ea=(6500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 164,
    label = "NH + O2 <=> NO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.28e+06, 'cm^3/(mol*s)'), n=1.5, Ea=(100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 165,
    label = "NH + N <=> N2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 166,
    label = "NH + H2O <=> HNO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(13850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 167,
    label = "NH + NO <=> N2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.16e+13, 'cm^3/(mol*s)'), n=-0.23, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 168,
    label = "NH + NO <=> N2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.65e+14, 'cm^3/(mol*s)'), n=-0.45, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 169,
    label = "NH2 + O(T) <=> OH + NH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 170,
    label = "NH2 + O(T) <=> H + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 171,
    label = "NH2 + H <=> NH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(3650, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 172,
    label = "NH2 + OH <=> NH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+07, 'cm^3/(mol*s)'), n=1.5, Ea=(-460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 173,
    label = "NNH <=> N2 + H",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(A=(3.3e+08, 's^-1'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 174,
    label = "NNH + O2 <=> HO2 + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 175,
    label = "NNH + O(T) <=> OH + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 176,
    label = "NNH + O(T) <=> NH + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 177,
    label = "NNH + H <=> H2 + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 178,
    label = "NNH + OH <=> H2O + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 179,
    label = "NNH + CH3 <=> CH4 + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 180,
    label = "HNO + O(T) <=> NO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 181,
    label = "HNO + H <=> H2 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+11, 'cm^3/(mol*s)'), n=0.72, Ea=(660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 182,
    label = "HNO + OH <=> NO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+07, 'cm^3/(mol*s)'), n=1.9, Ea=(-950, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 183,
    label = "HNO + O2 <=> HO2 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(13000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 184,
    label = "CN + O(T) <=> CO + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 185,
    label = "CN + OH <=> NCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 186,
    label = "CN + H2O <=> HCN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(7460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 187,
    label = "CN + O2 <=> NCO + O(T)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.14e+12, 'cm^3/(mol*s)'), n=0, Ea=(-440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 188,
    label = "CN + H2 <=> HCN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(295000, 'cm^3/(mol*s)'), n=2.45, Ea=(2240, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 189,
    label = "NCO + O(T) <=> NO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 190,
    label = "NCO + H <=> NH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 191,
    label = "NCO + OH <=> NO + H + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 192,
    label = "NCO + N <=> N2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 193,
    label = "NCO + O2 <=> NO + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(20000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 194,
    label = "NCO + NO <=> N2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.9e+17, 'cm^3/(mol*s)'),
        n = -1.52,
        Ea = (740, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 195,
    label = "NCO + NO <=> N2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+18, 'cm^3/(mol*s)'), n=-2, Ea=(800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 196,
    label = "HCN + O(T) <=> NCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(20300, 'cm^3/(mol*s)'), n=2.64, Ea=(4980, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 197,
    label = "HCN + O(T) <=> NH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5070, 'cm^3/(mol*s)'), n=2.64, Ea=(4980, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 198,
    label = "HCN + O(T) <=> CN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.91e+09, 'cm^3/(mol*s)'),
        n = 1.58,
        Ea = (26600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 199,
    label = "HCN + OH <=> HOCN + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+06, 'cm^3/(mol*s)'),
        n = 2.03,
        Ea = (13370, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 200,
    label = "HCN + OH <=> HNCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4400, 'cm^3/(mol*s)'), n=2.26, Ea=(6400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 201,
    label = "HCN + OH <=> NH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(160, 'cm^3/(mol*s)'), n=2.56, Ea=(9000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 202,
    label = "H2CN + N <=> N2 + CH2(T)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 203,
    label = "C(T) + N2 <=> CN + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(46020, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 204,
    label = "CH + N2 <=> HCN + N",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.12e+09, 'cm^3/(mol*s)'),
        n = 0.88,
        Ea = (20130, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 205,
    label = "CH2(T) + N2 <=> HCN + NH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(74000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 206,
    label = "CH2(S) + N2 <=> NH + HCN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(65000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 207,
    label = "C(T) + NO <=> CN + O(T)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 208,
    label = "C(T) + NO <=> CO + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 209,
    label = "CH + NO <=> HCN + O(T)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 210,
    label = "CH + NO <=> H + NCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.62e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 211,
    label = "CH + NO <=> N + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.46e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 212,
    label = "CH2(T) + NO <=> H + HNCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+17, 'cm^3/(mol*s)'),
        n = -1.38,
        Ea = (1270, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 213,
    label = "CH2(T) + NO <=> OH + HCN",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+14, 'cm^3/(mol*s)'),
        n = -0.69,
        Ea = (760, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 214,
    label = "CH2(T) + NO <=> H + HCNO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+13, 'cm^3/(mol*s)'),
        n = -0.36,
        Ea = (580, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 215,
    label = "CH2(S) + NO <=> H + HNCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+17, 'cm^3/(mol*s)'),
        n = -1.38,
        Ea = (1270, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 216,
    label = "CH2(S) + NO <=> OH + HCN",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+14, 'cm^3/(mol*s)'),
        n = -0.69,
        Ea = (760, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 217,
    label = "CH2(S) + NO <=> H + HCNO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+13, 'cm^3/(mol*s)'),
        n = -0.36,
        Ea = (580, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 218,
    label = "CH3 + NO <=> HCN + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(28800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 219,
    label = "CH3 + NO <=> H2CN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(21750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 220,
    label = "HCNN + O(T) <=> CO + H + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 221,
    label = "HCNN + O(T) <=> HCN + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 222,
    label = "HCNN + O2 <=> O(T) + HCO + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 223,
    label = "HCNN + OH <=> H + HCO + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 224,
    label = "HCNN + H <=> CH2(T) + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 225,
    label = "HNCO + O(T) <=> NH + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.8e+07, 'cm^3/(mol*s)'),
        n = 1.41,
        Ea = (8500, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 226,
    label = "HNCO + O(T) <=> HNO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+08, 'cm^3/(mol*s)'),
        n = 1.57,
        Ea = (44000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 227,
    label = "HNCO + O(T) <=> NCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+06, 'cm^3/(mol*s)'),
        n = 2.11,
        Ea = (11400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 228,
    label = "HNCO + H <=> NH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.25e+07, 'cm^3/(mol*s)'),
        n = 1.7,
        Ea = (3800, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 229,
    label = "HNCO + H <=> H2 + NCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(105000, 'cm^3/(mol*s)'), n=2.5, Ea=(13300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 230,
    label = "HNCO + OH <=> NCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+07, 'cm^3/(mol*s)'), n=1.5, Ea=(3600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 231,
    label = "HNCO + OH <=> NH2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+06, 'cm^3/(mol*s)'), n=1.5, Ea=(3600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 232,
    label = "HCNO + H <=> H + HNCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+15, 'cm^3/(mol*s)'),
        n = -0.69,
        Ea = (2850, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 233,
    label = "HCNO + H <=> OH + HCN",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+11, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (2120, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 234,
    label = "HCNO + H <=> NH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+14, 'cm^3/(mol*s)'),
        n = -0.75,
        Ea = (2890, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 235,
    label = "HOCN + H <=> H + HNCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+07, 'cm^3/(mol*s)'), n=2, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 236,
    label = "HCCO + NO <=> HCNO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 237,
    label = "CH3 + N <=> H2CN + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.1e+14, 'cm^3/(mol*s)'),
        n = -0.31,
        Ea = (290, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 238,
    label = "CH3 + N <=> HCN + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.7e+12, 'cm^3/(mol*s)'), n=0.15, Ea=(-90, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 239,
    label = "NH3 + H <=> NH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(540000, 'cm^3/(mol*s)'), n=2.4, Ea=(9915, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 240,
    label = "NH3 + OH <=> NH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+07, 'cm^3/(mol*s)'), n=1.6, Ea=(955, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 241,
    label = "NH3 + O(T) <=> NH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.4e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (6460, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 242,
    label = "NH + CO2 <=> HNO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(14350, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 243,
    label = "CN + NO2 <=> NCO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.16e+15, 'cm^3/(mol*s)'),
        n = -0.752,
        Ea = (345, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 244,
    label = "NCO + NO2 <=> N2O + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.25e+12, 'cm^3/(mol*s)'), n=0, Ea=(-705, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 245,
    label = "N + CO2 <=> NO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(11300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 246,
    label = "O(T) + CH3 => H + H2 + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.37e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 247,
    label = "O(T) + C2H4 <=> H + CH2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.7e+06, 'cm^3/(mol*s)'), n=1.83, Ea=(220, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 248,
    label = "O(T) + C2H5 <=> H + CH3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.096e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 250,
    label = "OH + CH3 => H2 + CH2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8e+09, 'cm^3/(mol*s)'), n=0.5, Ea=(-1755, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 251,
    label = "CH2(T) + O2 => H + H + CO2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(1500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 252,
    label = "CH2(T) + O2 <=> O(T) + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(1500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 253,
    label = "CH2(T) + CH2(T) => H + H + C2H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(10989, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 254,
    label = "CH2(S) + H2O => H2 + CH2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (6.82e+10, 'cm^3/(mol*s)'),
        n = 0.25,
        Ea = (-935, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 255,
    label = "C2H3 + O2 <=> O(T) + CH2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.03e+11, 'cm^3/(mol*s)'), n=0.29, Ea=(11, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 256,
    label = "C2H3 + O2 <=> HO2 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.337e+06, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-384, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 257,
    label = "O(T) + CH3CHO <=> OH + CH2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.92e+12, 'cm^3/(mol*s)'), n=0, Ea=(1808, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 258,
    label = "O(T) + CH3CHO => OH + CH3 + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.92e+12, 'cm^3/(mol*s)'), n=0, Ea=(1808, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 259,
    label = "O2 + CH3CHO => HO2 + CH3 + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(39150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 260,
    label = "H + CH3CHO <=> CH2CHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.05e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2405, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 261,
    label = "H + CH3CHO => CH3 + H2 + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.05e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2405, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 262,
    label = "OH + CH3CHO => CH3 + H2O + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.343e+10, 'cm^3/(mol*s)'),
        n = 0.73,
        Ea = (-1113, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 263,
    label = "HO2 + CH3CHO => CH3 + H2O2 + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11923, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 264,
    label = "CH3 + CH3CHO => CH3 + CH4 + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.72e+06, 'cm^3/(mol*s)'),
        n = 1.77,
        Ea = (5920, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 265,
    label = "O(T) + CH2CHO => H + CH2(T) + CO2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 266,
    label = "O2 + CH2CHO => OH + CO + CH2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.81e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 267,
    label = "O2 + CH2CHO => OH + HCO + HCO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.35e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 268,
    label = "H + CH2CHO <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 269,
    label = "H + CH2CHO <=> CH2CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 270,
    label = "OH + CH2CHO <=> H2O + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 271,
    label = "OH + CH2CHO <=> HCO + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 272,
    label = "O(T) + O(T) <=> O2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.2e+17, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 15.4, '[H][H]': 2.4, '[C]=O': 1.75, '[Ar]': 0.83},
    ),
)

entry(
    index = 273,
    label = "O(T) + H <=> OH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(5e+17, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 274,
    label = "H + O2 <=> HO2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (2.8e+18, 'cm^6/(mol^2*s)'),
            n = -0.86,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 1.5, 'CC': 1.5, 'O': 0, '[O][O]': 0, 'N#N': 0, '[C]=O': 0.75, '[Ar]': 0},
    ),
)

entry(
    index = 275,
    label = "H + H <=> H2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1e+18, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 0, 'CC': 3, 'O': 0, '[H][H]': 0, '[Ar]': 0.63},
    ),
)

entry(
    index = 276,
    label = "H + OH <=> H2O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.2e+22, 'cm^6/(mol^2*s)'), n=-2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'CC': 3, 'C': 2, '[H][H]': 0.73, 'O': 3.65, '[Ar]': 0.38},
    ),
)

entry(
    index = 277,
    label = "HCO <=> H + CO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.87e+17, 'cm^3/(mol*s)'),
            n = -1,
            Ea = (17000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 0, '[H][H]': 2, '[C]=O': 1.5},
    ),
)

entry(
    index = 278,
    label = "NO + O(T) <=> NO2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.06e+20, 'cm^6/(mol^2*s)'),
            n = -1.41,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 279,
    label = "NNH <=> N2 + H",
    degeneracy = 1,
    duplicate = True,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.3e+14, 'cm^3/(mol*s)'),
            n = -0.11,
            Ea = (4980, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 280,
    label = "H + NO <=> HNO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.48e+19, 'cm^6/(mol^2*s)'),
            n = -1.32,
            Ea = (740, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 281,
    label = "NCO <=> N + CO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(54050, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 282,
    label = "HCN <=> H + CN",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.04e+29, 'cm^3/(mol*s)'),
            n = -3.3,
            Ea = (126600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 283,
    label = "HNCO <=> NH + CO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.18e+16, 'cm^3/(mol*s)'), n=0, Ea=(84720, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 284,
    label = "O(T) + CO <=> CO2",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1.8e+10, 'cm^3/(mol*s)'), n=0, Ea=(2385, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.02e+14, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (3000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 3.5, 'CC': 3, 'O': 6, '[H][H]': 2, '[O][O]': 6, '[C]=O': 1.5, '[Ar]': 0.5},
    ),
)

entry(
    index = 285,
    label = "N2O <=> N2 + O(T)",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(7.91e+10, 's^-1'), n=0, Ea=(56020, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(6.37e+14, 'cm^3/(mol*s)'), n=0, Ea=(56640, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.625},
    ),
)

entry(
    index = 286,
    label = "H + HCN <=> H2CN",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(3.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.4e+26, 'cm^6/(mol^2*s)'),
            n = -3.4,
            Ea = (1900, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 287,
    label = "H + CH2(T) <=> CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.04e+26, 'cm^6/(mol^2*s)'),
            n = -2.76,
            Ea = (1600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.562,
        T3 = (91, 'K'),
        T1 = (5836, 'K'),
        T2 = (8552, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 288,
    label = "H + CH3 <=> CH4",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.39e+16, 'cm^3/(mol*s)'),
            n = -0.534,
            Ea = (536, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.62e+33, 'cm^6/(mol^2*s)'),
            n = -4.76,
            Ea = (2440, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.783,
        T3 = (74, 'K'),
        T1 = (2941, 'K'),
        T2 = (6964, 'K'),
        efficiencies = {'C': 3, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 289,
    label = "H + HCO <=> CH2O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.09e+12, 'cm^3/(mol*s)'),
            n = 0.48,
            Ea = (-260, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.47e+24, 'cm^6/(mol^2*s)'),
            n = -2.57,
            Ea = (425, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7824,
        T3 = (271, 'K'),
        T1 = (2755, 'K'),
        T2 = (6570, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 290,
    label = "H + CH2O <=> CH2OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.4e+11, 'cm^3/(mol*s)'),
            n = 0.454,
            Ea = (3600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.27e+32, 'cm^6/(mol^2*s)'),
            n = -4.82,
            Ea = (6530, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7187,
        T3 = (103, 'K'),
        T1 = (1291, 'K'),
        T2 = (4160, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5},
    ),
)

entry(
    index = 291,
    label = "H + CH2O <=> CH3O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.4e+11, 'cm^3/(mol*s)'),
            n = 0.454,
            Ea = (2600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.2e+30, 'cm^6/(mol^2*s)'),
            n = -4.8,
            Ea = (5560, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.758,
        T3 = (94, 'K'),
        T1 = (1555, 'K'),
        T2 = (4200, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5},
    ),
)

entry(
    index = 292,
    label = "H + CH2OH <=> CH3OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.055e+12, 'cm^3/(mol*s)'), n=0.5, Ea=(86, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.36e+31, 'cm^6/(mol^2*s)'),
            n = -4.65,
            Ea = (5080, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.6,
        T3 = (100, 'K'),
        T1 = (90000, 'K'),
        T2 = (10000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5},
    ),
)

entry(
    index = 293,
    label = "H + CH3O <=> CH3OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2.43e+12, 'cm^3/(mol*s)'),
            n = 0.515,
            Ea = (50, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.66e+41, 'cm^6/(mol^2*s)'),
            n = -7.44,
            Ea = (14080, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7,
        T3 = (100, 'K'),
        T1 = (90000, 'K'),
        T2 = (10000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5},
    ),
)

entry(
    index = 294,
    label = "H + C2H <=> C2H2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+17, 'cm^3/(mol*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.75e+33, 'cm^6/(mol^2*s)'),
            n = -4.8,
            Ea = (1900, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.6464,
        T3 = (132, 'K'),
        T1 = (1315, 'K'),
        T2 = (5566, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 295,
    label = "H + C2H2 <=> C2H3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(2400, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.8e+40, 'cm^6/(mol^2*s)'),
            n = -7.27,
            Ea = (7220, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7507,
        T3 = (98.5, 'K'),
        T1 = (1302, 'K'),
        T2 = (4167, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 296,
    label = "H + C2H3 <=> C2H4",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (6.08e+12, 'cm^3/(mol*s)'),
            n = 0.27,
            Ea = (280, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.4e+30, 'cm^6/(mol^2*s)'),
            n = -3.86,
            Ea = (3320, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.782,
        T3 = (207.5, 'K'),
        T1 = (2663, 'K'),
        T2 = (6095, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 297,
    label = "H + C2H4 <=> C2H5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.4e+11, 'cm^3/(mol*s)'),
            n = 0.454,
            Ea = (1820, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6e+41, 'cm^6/(mol^2*s)'),
            n = -7.62,
            Ea = (6970, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.9753,
        T3 = (210, 'K'),
        T1 = (984, 'K'),
        T2 = (4374, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 298,
    label = "H + C2H5 <=> C2H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.21e+17, 'cm^3/(mol*s)'),
            n = -0.99,
            Ea = (1580, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.99e+41, 'cm^6/(mol^2*s)'),
            n = -7.08,
            Ea = (6685, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.8422,
        T3 = (125, 'K'),
        T1 = (2219, 'K'),
        T2 = (6882, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 299,
    label = "H2 + CO <=> CH2O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4.3e+07, 'cm^3/(mol*s)'),
            n = 1.5,
            Ea = (79600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (5.07e+27, 'cm^6/(mol^2*s)'),
            n = -3.42,
            Ea = (84350, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.932,
        T3 = (197, 'K'),
        T1 = (1540, 'K'),
        T2 = (10300, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 300,
    label = "OH + OH <=> H2O2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(7.4e+13, 'cm^3/(mol*s)'), n=-0.37, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.3e+18, 'cm^6/(mol^2*s)'),
            n = -0.9,
            Ea = (-1700, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7346,
        T3 = (94, 'K'),
        T1 = (1756, 'K'),
        T2 = (5182, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 301,
    label = "OH + CH3 <=> CH3OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2.79e+18, 'cm^3/(mol*s)'),
            n = -1.43,
            Ea = (1330, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4e+36, 'cm^6/(mol^2*s)'),
            n = -5.92,
            Ea = (3140, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.412,
        T3 = (195, 'K'),
        T1 = (5900, 'K'),
        T2 = (6394, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5},
    ),
)

entry(
    index = 302,
    label = "CH + CO <=> HCCO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.69e+28, 'cm^6/(mol^2*s)'),
            n = -3.74,
            Ea = (1936, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5757,
        T3 = (237, 'K'),
        T1 = (1652, 'K'),
        T2 = (5069, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 303,
    label = "CH2(T) + CO <=> CH2CO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8.1e+11, 'cm^3/(mol*s)'), n=0.5, Ea=(4510, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.69e+33, 'cm^6/(mol^2*s)'),
            n = -5.11,
            Ea = (7095, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5907,
        T3 = (275, 'K'),
        T1 = (1226, 'K'),
        T2 = (5185, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 304,
    label = "CH2(S) + H2O <=> CH3OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4.82e+17, 'cm^3/(mol*s)'),
            n = -1.16,
            Ea = (1145, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.88e+38, 'cm^6/(mol^2*s)'),
            n = -6.36,
            Ea = (5040, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.6027,
        T3 = (208, 'K'),
        T1 = (3922, 'K'),
        T2 = (10180, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5},
    ),
)

entry(
    index = 305,
    label = "CH3 + CH3 <=> C2H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (6.77e+16, 'cm^3/(mol*s)'),
            n = -1.18,
            Ea = (654, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.4e+41, 'cm^6/(mol^2*s)'),
            n = -7.03,
            Ea = (2762, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.619,
        T3 = (73.2, 'K'),
        T1 = (1180, 'K'),
        T2 = (9999, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 306,
    label = "C2H4 <=> H2 + C2H2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8e+12, 's^-1'), n=0.44, Ea=(86770, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.58e+51, 'cm^3/(mol*s)'),
            n = -9.3,
            Ea = (97800, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7345,
        T3 = (180, 'K'),
        T1 = (1035, 'K'),
        T2 = (5417, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 307,
    label = "CH + N2 <=> HCNN",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.1e+12, 'cm^3/(mol*s)'), n=0.15, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.3e+25, 'cm^6/(mol^2*s)'),
            n = -3.16,
            Ea = (740, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.667,
        T3 = (235, 'K'),
        T1 = (2117, 'K'),
        T2 = (4536, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 1},
    ),
)

entry(
    index = 308,
    label = "CH + H2 <=> CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.97e+12, 'cm^3/(mol*s)'),
            n = 0.43,
            Ea = (-370, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.82e+25, 'cm^6/(mol^2*s)'),
            n = -2.8,
            Ea = (590, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.578,
        T3 = (122, 'K'),
        T1 = (2535, 'K'),
        T2 = (9365, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 309,
    label = "H + CH2CO <=> CH2CHO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4.865e+11, 'cm^3/(mol*s)'),
            n = 0.422,
            Ea = (-1755, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.012e+42, 'cm^6/(mol^2*s)'),
            n = -7.63,
            Ea = (3854, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.465,
        T3 = (201, 'K'),
        T1 = (1773, 'K'),
        T2 = (5333, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 310,
    label = "CH3 + C2H5 <=> C3H8",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9.43e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.71e+74, 'cm^6/(mol^2*s)'),
            n = -16.82,
            Ea = (13065, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.1527,
        T3 = (291, 'K'),
        T1 = (2742, 'K'),
        T2 = (7748, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

