#!/usr/bin/env python
# encoding: utf-8

name = "Dooley/C1"
shortDesc = u""
longDesc = u"""
mechanism used in
S. Dooley, M. P. Burke, M. Chaos, Y. Stein, F. L. Dryer, V. P. Zhukov, O. Finch, J. M. Simmie, H. J. Curran, Int. J. Chem. Kinet. 42 (9) (2010) 527-549.
"""
entry(
    index = 1,
    label = "H + O2 <=> O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.547e+15, 'cm^3/(mol*s)'),
        n = -0.406,
        Ea = (16599, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2,
    label = "O + H2 <=> H + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(50800, 'cm^3/(mol*s)'), n=2.67, Ea=(6290, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "H2 + OH <=> H2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.16e+08, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (3430, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 4,
    label = "O + H2O <=> OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.97e+06, 'cm^3/(mol*s)'),
        n = 2.02,
        Ea = (13400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 5,
    label = "HO2 + H <=> H2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.66e+13, 'cm^3/(mol*s)'), n=0, Ea=(823, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "HO2 + H <=> OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.079e+13, 'cm^3/(mol*s)'), n=0, Ea=(295, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "HO2 + O <=> O2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.25e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 8,
    label = "HO2 + OH <=> H2O + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.89e+13, 'cm^3/(mol*s)'), n=0, Ea=(-497, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 9,
    label = "HO2 + HO2 <=> H2O2 + O2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(4.2e+14, 'cm^3/(mol*s)'), n=0, Ea=(11982, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (1.3e+11, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (-1629.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 11,
    label = "H2O2 + H <=> H2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(3970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 12,
    label = "H2O2 + H <=> HO2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+13, 'cm^3/(mol*s)'), n=0, Ea=(7950, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "H2O2 + O <=> OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.55e+06, 'cm^3/(mol*s)'), n=2, Ea=(3970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 14,
    label = "H2O2 + OH <=> HO2 + H2O",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.8e+14, 'cm^3/(mol*s)'), n=0, Ea=(9557, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 16,
    label = "CO + O2 <=> CO2 + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.53e+12, 'cm^3/(mol*s)'), n=0, Ea=(47700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 17,
    label = "CO + HO2 <=> CO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(23000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 18,
    label = "CO + OH <=> CO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (222900, 'cm^3/(mol*s)'),
        n = 1.89,
        Ea = (-1158.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 19,
    label = "HCO + O2 <=> CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(410, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 20,
    label = "HCO + H <=> CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.23e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 21,
    label = "HCO + O <=> CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.02e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 22,
    label = "HCO + OH <=> CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.02e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 23,
    label = "HCO + O <=> CO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 24,
    label = "HCO + HO2 <=> CO2 + OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 25,
    label = "HCO + CH3 <=> CO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.65e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 26,
    label = "HCO + HCO <=> H2 + CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 27,
    label = "HCO + HCO <=> CH2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 28,
    label = "HCO + O2 <=> O2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 29,
    label = "CH2O + O2CHO <=> HCO + HO2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.99e+12, 'cm^3/(mol*s)'), n=0, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 30,
    label = "HO2CHO <=> OCHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+14, 's^-1'), n=0, Ea=(40150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 31,
    label = "CH2O + H <=> HCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.74e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (2748.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 32,
    label = "CH2O + O <=> HCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(3080, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 33,
    label = "CH2O + OH <=> HCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.43e+09, 'cm^3/(mol*s)'),
        n = 1.18,
        Ea = (-447, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 34,
    label = "CH2O + O2 <=> HCO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.23e+06, 'cm^3/(mol*s)'), n=3, Ea=(52000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 35,
    label = "CH2O + HO2 <=> HCO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41100, 'cm^3/(mol*s)'), n=2.5, Ea=(10210, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 36,
    label = "CH2O + CH3 <=> HCO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.636e-06, 'cm^3/(mol*s)'),
        n = 5.42,
        Ea = (998, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 37,
    label = "CH2O + HO2 <=> OCH2O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 38,
    label = "OCH2O2H <=> HOCH2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 's^-1'), n=0, Ea=(8600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 39,
    label = "HOCH2O2 + HO2 <=> HOCH2O2H + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 40,
    label = "HOCH2O + OH <=> HOCH2O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 41,
    label = "CH3 + O <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.43e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 42,
    label = "CH3 + O2 <=> CH3O + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.99e+18, 'cm^3/(mol*s)'),
        n = -1.57,
        Ea = (29230, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 43,
    label = "CH3 + O2 <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.351, 'cm^3/(mol*s)'), n=3.524, Ea=(7380, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 44,
    label = "CH3 + HO2 <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+10, 'cm^3/(mol*s)'),
        n = 0.76,
        Ea = (-2325, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 45,
    label = "CH4 + H <=> CH3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.47e+07, 'cm^3/(mol*s)'),
        n = 1.97,
        Ea = (11210, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 46,
    label = "CH4 + O <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.15e+12, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (10290, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 47,
    label = "CH4 + OH <=> CH3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.72e+06, 'cm^3/(mol*s)'),
        n = 1.96,
        Ea = (2639, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 48,
    label = "CH3 + HO2 <=> CH4 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.16e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 49,
    label = "CH4 + HO2 <=> CH3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+11, 'cm^3/(mol*s)'), n=0, Ea=(18580, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 50,
    label = "CH3 + CH3OH <=> CH4 + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(6935, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 51,
    label = "CH3O + CH3 <=> CH2O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 52,
    label = "CH3O + H <=> CH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 53,
    label = "CH3O2 + CH2O <=> CH3O2H + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.99e+12, 'cm^3/(mol*s)'), n=0, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 54,
    label = "CH4 + CH3O2 <=> CH3 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+11, 'cm^3/(mol*s)'), n=0, Ea=(18480, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 55,
    label = "CH3OH + CH3O2 <=> CH2OH + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+12, 'cm^3/(mol*s)'), n=0, Ea=(13710, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 56,
    label = "CH3O2 + CH3 <=> CH3O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.08e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1411, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 57,
    label = "CH3O2 + HO2 <=> CH3O2H + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.47e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1570, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 58,
    label = "CH3O2 + CH3O2 <=> CH2O + CH3OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.11e+14, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (-1051, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 59,
    label = "CH3O2 + CH3O2 <=> O2 + CH3O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 60,
    label = "CH3O2 + H <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 61,
    label = "CH3O2 + O <=> CH3O + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 62,
    label = "CH3O2 + OH <=> CH3OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 63,
    label = "CH3O2H <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.31e+14, 's^-1'), n=0, Ea=(42300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 64,
    label = "CH2OH + H <=> CH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 65,
    label = "CH2OH + H <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.635e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 66,
    label = "CH2OH + O <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 67,
    label = "CH2OH + OH <=> CH2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 68,
    label = "CH2OH + O2 <=> CH2O + HO2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(2.41e+14, 'cm^3/(mol*s)'), n=0, Ea=(5017, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.51e+15, 'cm^3/(mol*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 70,
    label = "CH2OH + HO2 <=> CH2O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 71,
    label = "CH2OH + HCO <=> CH3OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 72,
    label = "CH2OH + HCO <=> CH2O + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 73,
    label = "CH2OH + CH2OH <=> CH3OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 74,
    label = "CH2OH + CH3O <=> CH3OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 75,
    label = "CH2OH + HO2 <=> HOCH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 76,
    label = "CH3O + H <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 77,
    label = "CH3O + O <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 78,
    label = "CH3O + OH <=> CH2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 79,
    label = "CH3O + O2 <=> CH2O + HO2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (9.033e+13, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (11980, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(2.2e+10, 'cm^3/(mol*s)'), n=0, Ea=(1748, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 81,
    label = "CH3O + HO2 <=> CH2O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 82,
    label = "CH3O + CO <=> CH3 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(11800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 83,
    label = "CH3O + HCO <=> CH3OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 84,
    label = "CH3O + CH3O <=> CH3OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 85,
    label = "CH3OH + H <=> CH2OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(6095, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 86,
    label = "CH3OH + H <=> CH3O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(6095, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 87,
    label = "CH3OH + O <=> CH2OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(388000, 'cm^3/(mol*s)'), n=2.5, Ea=(3080, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 88,
    label = "CH3OH + OH <=> CH3O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+06, 'cm^3/(mol*s)'), n=2.1, Ea=(496.7, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 89,
    label = "CH3OH + OH <=> CH2OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.1e+06, 'cm^3/(mol*s)'), n=1.8, Ea=(-596, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 90,
    label = "CH3OH + O2 <=> CH2OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.05e+13, 'cm^3/(mol*s)'), n=0, Ea=(44900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 91,
    label = "CH3OH + HCO <=> CH2OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9635, 'cm^3/(mol*s)'), n=2.9, Ea=(13110, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 92,
    label = "CH3OH + HO2 <=> CH2OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.98e+13, 'cm^3/(mol*s)'), n=0, Ea=(19400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 93,
    label = "CH3OH + CH3 <=> CH2OH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(31.9, 'cm^3/(mol*s)'), n=3.17, Ea=(7172, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 94,
    label = "CH3O + CH3OH <=> CH3OH + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(4060, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 95,
    label = "CH3 + CH3 <=> H + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.99e+12, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (10600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 96,
    label = "CH4 + CH2 <=> CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.46e+06, 'cm^3/(mol*s)'), n=2, Ea=(8270, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 97,
    label = "CH4 + CH2(S) <=> CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(-570, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 98,
    label = "CH3 + OH <=> CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+07, 'cm^3/(mol*s)'), n=1.6, Ea=(5420, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 99,
    label = "CH3 + OH <=> CH2(S) + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.501e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 100,
    label = "CH3 + CH2 <=> C2H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 101,
    label = "CH3 + CH2(S) <=> C2H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(-570, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 102,
    label = "CH3O + H <=> CH2(S) + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 103,
    label = "CH2 + O <=> HCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 104,
    label = "CH2 + OH <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 105,
    label = "CH2 + H2 <=> H + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(500000, 'cm^3/(mol*s)'), n=2, Ea=(7230, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 106,
    label = "CH2 + O2 <=> HCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.32e+13, 'cm^3/(mol*s)'), n=0, Ea=(1500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 107,
    label = "CH2 + HO2 <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 108,
    label = "CH2 + CH2 <=> C2H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 109,
    label = "CH2(S) + H2O <=> CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 110,
    label = "CH2(S) + CO <=> CH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 111,
    label = "CH2(S) + CO2 <=> CH2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 112,
    label = "CH2(S) + O <=> CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 113,
    label = "CH2(S) + O <=> HCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 114,
    label = "CH2(S) + OH <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 115,
    label = "CH2(S) + H2 <=> CH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 116,
    label = "CH2(S) + O2 <=> H + OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 117,
    label = "CH2(S) + O2 <=> CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 118,
    label = "CH2(S) + CO2 <=> CH2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 119,
    label = "CH2(S) + H <=> CH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 120,
    label = "CH2 + H <=> CH + H2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1e+18, 'cm^3/(mol*s)'), n=-1.56, Ea=(0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (2.7e+11, 'cm^3/(mol*s)'),
                n = 0.67,
                Ea = (25700, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 122,
    label = "CH2 + OH <=> CH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+07, 'cm^3/(mol*s)'), n=2, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 123,
    label = "CH + O2 <=> HCO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 124,
    label = "CH + H <=> C + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 125,
    label = "CH + O <=> CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 126,
    label = "CH + OH <=> HCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 127,
    label = "CH + H2O <=> H + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.713e+13, 'cm^3/(mol*s)'), n=0, Ea=(-755, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 128,
    label = "CH + CO2 <=> HCO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(685, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 129,
    label = "HOCH2O <=> HCOOH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 130,
    label = "CH2O + OH <=> HOCH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.5e+15, 'cm^3/(mol*s)'), n=-1.11, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 131,
    label = "HCOOH <=> HCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.593e+18, 's^-1'), n=-0.46, Ea=(108300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 132,
    label = "HCOOH + OH <=> H2O + CO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.62e+06, 'cm^3/(mol*s)'),
        n = 2.06,
        Ea = (916, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 133,
    label = "HCOOH + OH <=> H2O + CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.85e+07, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (-962, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 134,
    label = "HCOOH + H <=> H2 + CO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.24e+06, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (4868, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 135,
    label = "HCOOH + H <=> H2 + CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (2988, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 136,
    label = "HCOOH + CH3 <=> CH4 + CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.9e-07, 'cm^3/(mol*s)'), n=5.8, Ea=(2200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 137,
    label = "HCOOH + HO2 <=> H2O2 + CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 138,
    label = "HCOOH + O <=> CO + OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.77e+18, 'cm^3/(mol*s)'),
        n = -1.9,
        Ea = (2975, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 139,
    label = "H2 <=> H + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.577e+19, 'cm^3/(mol*s)'),
            n = -1.4,
            Ea = (104380, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 3.8, 'O': 12, '[H][H]': 2.5, '[He]': 0, '[C]=O': 1.9, '[Ar]': 0},
    ),
)

entry(
    index = 140,
    label = "O + O <=> O2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6.165e+15, 'cm^6/(mol^2*s)'),
            n = -0.5,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 3.8, 'O': 12, '[H][H]': 2.5, '[He]': 0, '[C]=O': 1.9, '[Ar]': 0},
    ),
)

entry(
    index = 141,
    label = "O + H <=> OH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.714e+18, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'O=C=O': 3.8, 'O': 12, '[H][H]': 2.5, '[He]': 0.75, '[C]=O': 1.9, '[Ar]': 0.75},
    ),
)

entry(
    index = 142,
    label = "H + OH <=> H2O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.8e+22, 'cm^6/(mol^2*s)'), n=-2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'O=C=O': 3.8, 'O': 12, '[H][H]': 2.5, '[He]': 0.38, '[C]=O': 1.9, '[Ar]': 0.38},
    ),
)

entry(
    index = 143,
    label = "H + O2 <=> HO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.475e+12, 'cm^3/(mol*s)'), n=0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.366e+20, 'cm^6/(mol^2*s)'),
            n = -1.72,
            Ea = (524.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.8,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'[H][H]': 2, '[C]=O': 1.9, '[O][O]': 0.78, 'O=C=O': 3.8, 'O': 11},
    ),
)

entry(
    index = 144,
    label = "H2O2 <=> OH + OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.951e+14, 's^-1'), n=0, Ea=(48430, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.202e+17, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (45500, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'O=C=O': 3.8, 'O': 12, '[H][H]': 2.5, '[He]': 0.64, '[C]=O': 1.9, '[Ar]': 0.64},
    ),
)

entry(
    index = 145,
    label = "CO + O <=> CO2",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1.8e+10, 'cm^3/(mol*s)'), n=0, Ea=(2384, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.55e+24, 'cm^6/(mol^2*s)'),
            n = -2.79,
            Ea = (4191, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[H][H]': 2.5, '[C]=O': 1.9, 'O=C=O': 3.8, 'O': 12, '[Ar]': 0.87},
    ),
)

entry(
    index = 146,
    label = "HCO <=> H + CO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.7485e+11, 'cm^3/(mol*s)'),
            n = 0.659,
            Ea = (14874, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[H][H]': 2.5, '[C]=O': 1.9, 'O=C=O': 3.8, 'O': 6},
    ),
)

entry(
    index = 147,
    label = "CH2O <=> HCO + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (3.3e+39, 'cm^3/(mol*s)'),
            n = -6.3,
            Ea = (99900, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[H][H]': 2.5, '[C]=O': 1.9, 'O=C=O': 3.8, 'O': 12, '[Ar]': 0.7},
    ),
)

entry(
    index = 148,
    label = "CH2O <=> CO + H2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.1e+45, 'cm^3/(mol*s)'), n=-8, Ea=(97510, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[H][H]': 2.5, '[C]=O': 1.9, 'O=C=O': 3.8, 'O': 12, '[Ar]': 0.7},
    ),
)

entry(
    index = 149,
    label = "CH3 + CH3 <=> C2H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2.277e+15, 'cm^3/(mol*s)'),
            n = -0.69,
            Ea = (174.86, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (8.054e+31, 'cm^6/(mol^2*s)'),
            n = -3.75,
            Ea = (981.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        T3 = (570, 'K'),
        T1 = (1e-10, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'[C]=O': 2, 'O=C=O': 3, 'O': 5},
    ),
)

entry(
    index = 150,
    label = "CH3 + H <=> CH4",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.27e+16, 'cm^3/(mol*s)'),
            n = -0.63,
            Ea = (383, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.477e+33, 'cm^6/(mol^2*s)'),
            n = -4.76,
            Ea = (2440, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.783,
        T3 = (74, 'K'),
        T1 = (2941, 'K'),
        T2 = (6964, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 151,
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
    index = 152,
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
    index = 153,
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
    index = 154,
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
    index = 155,
    label = "CH2 + H <=> CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.5e+16, 'cm^3/(mol*s)'), n=-0.8, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.2e+27, 'cm^6/(mol^2*s)'),
            n = -3.14,
            Ea = (1230, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.68,
        T3 = (78, 'K'),
        T1 = (1995, 'K'),
        T2 = (5590, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 156,
    label = "CH2 + CO <=> CH2CO",
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
    index = 157,
    label = "CH2(S) <=> CH2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(600, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[C]=O': 0, 'O=C=O': 0, 'O': 0, '[Ar]': 0},
    ),
)

entry(
    index = 158,
    label = "H + CO2 <=> OCHO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (7.5e+13, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (29000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
)

entry(
    index = 159,
    label = "CH2OH <=> CH2O + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(25100, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

entry(
    index = 160,
    label = "CH3O <=> CH2O + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (8.3e+17, 'cm^3/(mol*s)'),
            n = -1.2,
            Ea = (15500, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
)

entry(
    index = 161,
    label = "HCOOH <=> CO + H2O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(50000, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

entry(
    index = 162,
    label = "HCOOH <=> CO2 + H2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.5e+16, 'cm^3/(mol*s)'), n=0, Ea=(57000, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

