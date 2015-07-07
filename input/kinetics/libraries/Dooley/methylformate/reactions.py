#!/usr/bin/env python
# encoding: utf-8

name = "Dooley/methylformate"
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
    label = "C2H6 + H <=> C2H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15e+08, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (7530, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 140,
    label = "C2H6 + O <=> C2H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.55e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (5830, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 141,
    label = "C2H6 + OH <=> C2H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.48e+07, 'cm^3/(mol*s)'), n=1.9, Ea=(950, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 142,
    label = "C2H6 + O2 <=> C2H5 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(51870, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 143,
    label = "C2H6 + CH3 <=> C2H5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.51e-07, 'cm^3/(mol*s)'), n=6, Ea=(6047, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 144,
    label = "C2H6 + HO2 <=> C2H5 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(34.6, 'cm^3/(mol*s)'), n=3.61, Ea=(16920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 145,
    label = "C2H6 + CH3O2 <=> C2H5 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(19.4, 'cm^3/(mol*s)'), n=3.64, Ea=(17100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 146,
    label = "C2H6 + CH3O <=> C2H5 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+11, 'cm^3/(mol*s)'), n=0, Ea=(7090, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 147,
    label = "C2H6 + CH <=> C2H5 + CH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(-260, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 148,
    label = "CH2(S) + C2H6 <=> CH3 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 149,
    label = "H2 + CH3O2 <=> H + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+14, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 150,
    label = "H2 + C2H5O2 <=> H + C2H5O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+14, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 151,
    label = "C2H4 + C2H4 <=> C2H5 + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+14, 'cm^3/(mol*s)'), n=0, Ea=(71530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 152,
    label = "CH3 + C2H5 <=> CH4 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(11800, 'cm^3/(mol*s)'), n=2.45, Ea=(-2921, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 153,
    label = "C2H5 + H <=> C2H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 154,
    label = "C2H5 + O <=> CH3CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 155,
    label = "C2H5 + HO2 <=> C2H5O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 156,
    label = "CH3O2 + C2H5 <=> CH3O + C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 157,
    label = "C2H5O + O2 <=> CH3CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.28e+10, 'cm^3/(mol*s)'), n=0, Ea=(1097, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 158,
    label = "CH3CHO + H <=> C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(6400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 159,
    label = "C2H5 + O2 <=> C2H5O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.876e+56, 'cm^3/(mol*s)'),
        n = -13.82,
        Ea = (14620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 160,
    label = "C2H5O2 + CH2O <=> C2H5O2H + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.99e+12, 'cm^3/(mol*s)'), n=0, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 161,
    label = "CH4 + C2H5O2 <=> CH3 + C2H5O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+11, 'cm^3/(mol*s)'), n=0, Ea=(18480, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 162,
    label = "CH3OH + C2H5O2 <=> CH2OH + C2H5O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+12, 'cm^3/(mol*s)'), n=0, Ea=(13710, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 163,
    label = "C2H5O2 + HO2 <=> C2H5O2H + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 164,
    label = "C2H6 + C2H5O2 <=> C2H5 + C2H5O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.6, 'cm^3/(mol*s)'), n=3.76, Ea=(17200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 165,
    label = "C2H5O2H <=> C2H5O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.31e+14, 's^-1'), n=0, Ea=(42300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 166,
    label = "C2H5 + O2 <=> C2H4O2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.814e+45, 'cm^3/(mol*s)'),
        n = -11.5,
        Ea = (14600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 167,
    label = "C2H5 + O2 <=> C2H4 + HO2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (7.561e+14, 'cm^3/(mol*s)'),
                n = -1.01,
                Ea = (4749, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(0.4, 'cm^3/(mol*s)'), n=3.88, Ea=(13620, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 169,
    label = "C2H5 + O2 <=> C2H4O1-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.626e+11, 'cm^3/(mol*s)'),
        n = -0.31,
        Ea = (6150, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 170,
    label = "C2H5 + O2 <=> CH3CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(826.5, 'cm^3/(mol*s)'), n=2.41, Ea=(5285, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 171,
    label = "C2H4O2H <=> C2H5O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.203e+36, 's^-1'), n=-8.13, Ea=(27020, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 172,
    label = "C2H5O2 <=> CH3CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.52e+41, 's^-1'), n=-10.2, Ea=(43710, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 173,
    label = "C2H5O2 <=> C2H4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.815e+38, 's^-1'), n=-8.45, Ea=(37890, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 174,
    label = "C2H5O2 <=> C2H4O1-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+43, 's^-1'), n=-10.46, Ea=(45580, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 175,
    label = "C2H4O2H <=> C2H4O1-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.848e+30, 's^-1'), n=-6.08, Ea=(20660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 176,
    label = "C2H4O2H <=> C2H4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.98e+34, 's^-1'), n=-7.25, Ea=(23250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 177,
    label = "C2H4O2H <=> CH3CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.188e+34, 's^-1'), n=-9.02, Ea=(29210, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 178,
    label = "C2H4O1-2 <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.63e+13, 's^-1'), n=0, Ea=(57200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 179,
    label = "C2H4O1-2 <=> CH3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.407e+12, 's^-1'), n=0, Ea=(53800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 180,
    label = "C2H4O1-2 + OH <=> C2H3O1-2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.78e+13, 'cm^3/(mol*s)'), n=0, Ea=(3610, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 181,
    label = "C2H4O1-2 + H <=> C2H3O1-2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(9680, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 182,
    label = "C2H4O1-2 + HO2 <=> C2H3O1-2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 183,
    label = "C2H4O1-2 + CH3O2 <=> C2H3O1-2 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 184,
    label = "C2H4O1-2 + C2H5O2 <=> C2H3O1-2 + C2H5O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 185,
    label = "C2H4O1-2 + CH3 <=> C2H3O1-2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.07e+12, 'cm^3/(mol*s)'), n=0, Ea=(11830, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 186,
    label = "C2H4O1-2 + CH3O <=> C2H3O1-2 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(6750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 187,
    label = "C2H3O1-2 <=> CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.5e+14, 's^-1'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 188,
    label = "C2H3O1-2 <=> CH2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 189,
    label = "CH3 + HCO <=> CH3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 190,
    label = "CH3CHO + H <=> CH3CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.11e+13, 'cm^3/(mol*s)'), n=0, Ea=(3110, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 191,
    label = "CH3CHO + O <=> CH3CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.94e+12, 'cm^3/(mol*s)'), n=0, Ea=(1868, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 192,
    label = "CH3CHO + OH <=> CH3CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+06, 'cm^3/(mol*s)'), n=1.8, Ea=(1300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 193,
    label = "CH3CHO + O2 <=> CH3CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(39150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 194,
    label = "CH3CHO + CH3 <=> CH3CO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1760, 'cm^3/(mol*s)'), n=2.79, Ea=(4950, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 195,
    label = "CH3CHO + HO2 <=> CH3CO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 196,
    label = "CH3O2 + CH3CHO <=> CH3O2H + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 197,
    label = "CH3CHO + CH3CO3 <=> CH3CO + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 198,
    label = "CH3CHO + OH <=> CH3 + HCOOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+15, 'cm^3/(mol*s)'), n=-1.08, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 199,
    label = "CH3CHO + OH <=> CH2CHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(172000, 'cm^3/(mol*s)'), n=2.4, Ea=(815, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 200,
    label = "CH3CO + H <=> CH2CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 201,
    label = "CH3CO + O <=> CH2CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 202,
    label = "CH3CO + CH3 <=> CH2CO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 203,
    label = "CH3CO + O2 <=> CH3CO3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 204,
    label = "CH3CO3 + HO2 <=> CH3CO3H + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 205,
    label = "H2O2 + CH3CO3 <=> HO2 + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(9936, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 206,
    label = "CH4 + CH3CO3 <=> CH3 + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+11, 'cm^3/(mol*s)'), n=0, Ea=(18480, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 207,
    label = "CH2O + CH3CO3 <=> HCO + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.99e+12, 'cm^3/(mol*s)'), n=0, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 208,
    label = "C2H6 + CH3CO3 <=> C2H5 + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 209,
    label = "CH3CO3H <=> CH3CO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+14, 's^-1'), n=0, Ea=(40150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 210,
    label = "CH2CO + H <=> CH2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(12300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 211,
    label = "CH2CHO + O2 <=> CH2O + CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(4200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 212,
    label = "CH2CO + H <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(3400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 213,
    label = "CH2CO + H <=> HCCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(8000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 214,
    label = "CH2CO + O <=> CH2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+12, 'cm^3/(mol*s)'), n=0, Ea=(1350, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 215,
    label = "CH2CO + O <=> HCCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(8000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 216,
    label = "CH2CO + OH <=> HCCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 217,
    label = "CH2CO + OH <=> CH2OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 218,
    label = "CH2(S) + CH2CO <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 219,
    label = "HCCO + OH <=> H2 + CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 220,
    label = "H + HCCO <=> CH2(S) + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 221,
    label = "HCCO + O <=> H + CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 222,
    label = "HCCO + O2 <=> OH + CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.2e+10, 'cm^3/(mol*s)'), n=0, Ea=(850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 223,
    label = "CH + CH2O <=> H + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.46e+13, 'cm^3/(mol*s)'), n=0, Ea=(-515, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 224,
    label = "CH + HCCO <=> CO + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 225,
    label = "C2H4 + H <=> C2H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.07e+07, 'cm^3/(mol*s)'),
        n = 1.93,
        Ea = (12950, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 226,
    label = "C2H4 + O <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.564e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (183, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 227,
    label = "C2H4 + O <=> CH2CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.986e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (183, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 228,
    label = "C2H4 + OH <=> C2H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+06, 'cm^3/(mol*s)'), n=2, Ea=(2500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 229,
    label = "C2H4 + CH3 <=> C2H3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.62, 'cm^3/(mol*s)'), n=3.7, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 230,
    label = "C2H4 + O2 <=> C2H3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(58200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 231,
    label = "C2H4 + CH3O <=> C2H3 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(6750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 232,
    label = "C2H4 + CH3O2 <=> C2H3 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.23e+12, 'cm^3/(mol*s)'), n=0, Ea=(17190, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 233,
    label = "C2H4 + C2H5O2 <=> C2H3 + C2H5O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.23e+12, 'cm^3/(mol*s)'), n=0, Ea=(17190, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 234,
    label = "C2H4 + CH3CO3 <=> C2H3 + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 235,
    label = "C2H4 + CH3O2 <=> C2H4O1-2 + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.82e+12, 'cm^3/(mol*s)'), n=0, Ea=(17110, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 236,
    label = "C2H4 + C2H5O2 <=> C2H4O1-2 + C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.82e+12, 'cm^3/(mol*s)'), n=0, Ea=(17110, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 237,
    label = "C2H4 + HO2 <=> C2H4O1-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.23e+12, 'cm^3/(mol*s)'), n=0, Ea=(17190, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 238,
    label = "CH + CH4 <=> C2H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 239,
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
    index = 240,
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
    index = 241,
    label = "C2H3 + O2 <=> O + CH2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0.29, Ea=(11, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 242,
    label = "CH3 + C2H3 <=> CH4 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.92e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 243,
    label = "C2H3 + H <=> C2H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 244,
    label = "C2H3 + OH <=> C2H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 245,
    label = "C2H2 + O2 <=> HCCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(30100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 246,
    label = "O + C2H2 <=> C2H + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6e+19, 'cm^3/(mol*s)'),
        n = -1.4,
        Ea = (28950, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 247,
    label = "C2H2 + O <=> CH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.94e+06, 'cm^3/(mol*s)'), n=2, Ea=(1900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 248,
    label = "C2H2 + O <=> HCCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.35e+07, 'cm^3/(mol*s)'), n=2, Ea=(1900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 249,
    label = "C2H2 + OH <=> C2H + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.37e+07, 'cm^3/(mol*s)'), n=2, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 250,
    label = "C2H2 + OH <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.236e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 251,
    label = "C2H2 + OH <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.000483, 'cm^3/(mol*s)'), n=4, Ea=(-2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 252,
    label = "OH + C2H2 <=> H + HCCOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(504000, 'cm^3/(mol*s)'), n=2.3, Ea=(13500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 253,
    label = "H + HCCOH <=> H + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 254,
    label = "C2H5OH + O2 <=> PC2H4OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(52800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 255,
    label = "C2H5OH + O2 <=> SC2H4OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(50150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 256,
    label = "C2H5OH + OH <=> PC2H4OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.74e+11, 'cm^3/(mol*s)'),
        n = 0.27,
        Ea = (600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 257,
    label = "C2H5OH + OH <=> SC2H4OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.64e+11, 'cm^3/(mol*s)'), n=0.15, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 258,
    label = "C2H5OH + OH <=> C2H5O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.46e+11, 'cm^3/(mol*s)'),
        n = 0.3,
        Ea = (1634, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 259,
    label = "C2H5OH + H <=> PC2H4OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.23e+07, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (5098, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 260,
    label = "C2H5OH + H <=> SC2H4OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.58e+07, 'cm^3/(mol*s)'),
        n = 1.65,
        Ea = (2827, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 261,
    label = "C2H5OH + H <=> C2H5O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+07, 'cm^3/(mol*s)'), n=1.6, Ea=(3038, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 262,
    label = "C2H5OH + HO2 <=> PC2H4OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(12300, 'cm^3/(mol*s)'), n=2.55, Ea=(15750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 263,
    label = "C2H5OH + HO2 <=> SC2H4OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8200, 'cm^3/(mol*s)'), n=2.55, Ea=(10750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 264,
    label = "C2H5OH + HO2 <=> C2H5O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(24000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 265,
    label = "C2H5OH + CH3O2 <=> PC2H4OH + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(12300, 'cm^3/(mol*s)'), n=2.55, Ea=(15750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 266,
    label = "C2H5OH + CH3O2 <=> SC2H4OH + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8200, 'cm^3/(mol*s)'), n=2.55, Ea=(10750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 267,
    label = "C2H5OH + CH3O2 <=> C2H5O + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(24000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 268,
    label = "C2H5OH + O <=> PC2H4OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.41e+07, 'cm^3/(mol*s)'),
        n = 1.7,
        Ea = (5459, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 269,
    label = "C2H5OH + O <=> SC2H4OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+07, 'cm^3/(mol*s)'),
        n = 1.85,
        Ea = (1824, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 270,
    label = "C2H5OH + O <=> C2H5O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.58e+07, 'cm^3/(mol*s)'), n=2, Ea=(4448, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 271,
    label = "C2H5OH + CH3 <=> PC2H4OH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(133, 'cm^3/(mol*s)'), n=3.18, Ea=(9362, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 272,
    label = "C2H5OH + CH3 <=> SC2H4OH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(444, 'cm^3/(mol*s)'), n=2.9, Ea=(7690, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 273,
    label = "C2H5OH + CH3 <=> C2H5O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(134, 'cm^3/(mol*s)'), n=2.92, Ea=(7452, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 274,
    label = "C2H5OH + C2H5 <=> PC2H4OH + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 275,
    label = "C2H5OH + C2H5 <=> SC2H4OH + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 276,
    label = "C2H4 + OH <=> PC2H4OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.17e+20, 'cm^3/(mol*s)'),
        n = -2.84,
        Ea = (1240, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 277,
    label = "O2C2H4OH <=> PC2H4OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.9e+16, 's^-1'), n=-1, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 278,
    label = "O2C2H4OH <=> OH + CH2O + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.125e+09, 's^-1'), n=0, Ea=(18900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 279,
    label = "SC2H4OH + O2 <=> CH3CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.81e+06, 'cm^3/(mol*s)'), n=2, Ea=(1641, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 280,
    label = "CH3COCH3 + OH <=> CH3COCH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(125000, 'cm^3/(mol*s)'), n=2.48, Ea=(445, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 281,
    label = "CH3COCH3 + H <=> CH3COCH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(980000, 'cm^3/(mol*s)'), n=2.43, Ea=(5160, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 282,
    label = "CH3COCH3 + O <=> CH3COCH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.13e+11, 'cm^3/(mol*s)'),
        n = 0.21,
        Ea = (4890, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 283,
    label = "CH3COCH3 + CH3 <=> CH3COCH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.96e+11, 'cm^3/(mol*s)'), n=0, Ea=(9784, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 284,
    label = "CH3COCH3 + CH3O <=> CH3COCH2 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.34e+11, 'cm^3/(mol*s)'), n=0, Ea=(6460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 285,
    label = "CH3COCH3 + O2 <=> CH3COCH2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(48500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 286,
    label = "CH3COCH3 + HO2 <=> CH3COCH2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 287,
    label = "CH3COCH3 + CH3O2 <=> CH3COCH2 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 288,
    label = "CH3COCH2 <=> CH2CO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(31000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 289,
    label = "CH3COCH2 + O2 <=> CH3COCH2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 290,
    label = "CH3COCH3 + CH3COCH2O2 <=> CH3COCH2 + CH3COCH2O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 291,
    label = "CH2O + CH3COCH2O2 <=> HCO + CH3COCH2O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.288e+11, 'cm^3/(mol*s)'), n=0, Ea=(9000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 292,
    label = "HO2 + CH3COCH2O2 <=> CH3COCH2O2H + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 293,
    label = "CH3COCH2O2H <=> CH3COCH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 294,
    label = "CH3CO + CH2O <=> CH3COCH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 295,
    label = "C2H3 + HCO <=> C2H3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 296,
    label = "C2H3CHO + H <=> C2H3CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.34e+13, 'cm^3/(mol*s)'), n=0, Ea=(3300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 297,
    label = "C2H3CHO + O <=> C2H3CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.94e+12, 'cm^3/(mol*s)'), n=0, Ea=(1868, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 298,
    label = "C2H3CHO + H <=> C2H4 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(3500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 299,
    label = "C2H3CHO + O <=> CH2CO + HCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+07, 'cm^3/(mol*s)'), n=1.76, Ea=(76, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 300,
    label = "C2H3CHO + OH <=> C2H3CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.24e+06, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-962, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 301,
    label = "C2H3CHO + O2 <=> C2H3CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.005e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (40700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 302,
    label = "C2H3CHO + HO2 <=> C2H3CO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 303,
    label = "C2H3CHO + CH3 <=> C2H3CO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.608e+06, 'cm^3/(mol*s)'),
        n = 1.78,
        Ea = (5911, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 304,
    label = "C2H3CHO + C2H3 <=> C2H3CO + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.74e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 305,
    label = "C2H3CHO + CH3O <=> C2H3CO + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(3300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 306,
    label = "C2H3CHO + CH3O2 <=> C2H3CO + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 307,
    label = "C2H3 + CO <=> C2H3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.51e+11, 'cm^3/(mol*s)'), n=0, Ea=(4810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 308,
    label = "C2H3CO + O2 <=> CH2CHO + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.4e+20, 'cm^3/(mol*s)'),
        n = -2.72,
        Ea = (7000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 309,
    label = "C2H3CO + O <=> C2H3 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 310,
    label = "C2H5 + HCO <=> C2H5CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 311,
    label = "C2H5CHO + H <=> C2H5CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(4200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 312,
    label = "C2H5CHO + O <=> C2H5CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(1790, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 313,
    label = "C2H5CHO + OH <=> C2H5CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.69e+10, 'cm^3/(mol*s)'),
        n = 0.76,
        Ea = (-340, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 314,
    label = "C2H5CHO + CH3 <=> C2H5CO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.608e+06, 'cm^3/(mol*s)'),
        n = 1.78,
        Ea = (5911, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 315,
    label = "C2H5CHO + HO2 <=> C2H5CO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 316,
    label = "C2H5CHO + CH3O <=> C2H5CO + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(3300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 317,
    label = "C2H5CHO + CH3O2 <=> C2H5CO + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 318,
    label = "C2H5CHO + C2H5 <=> C2H5CO + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(8000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 319,
    label = "C2H5CHO + C2H5O <=> C2H5CO + C2H5OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.026e+11, 'cm^3/(mol*s)'), n=0, Ea=(3300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 320,
    label = "C2H5CHO + C2H5O2 <=> C2H5CO + C2H5O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 321,
    label = "C2H5CHO + O2 <=> C2H5CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.005e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (40700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 322,
    label = "C2H5CHO + CH3CO3 <=> C2H5CO + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 323,
    label = "C2H5CHO + C2H3 <=> C2H5CO + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 324,
    label = "C2H5 + CO <=> C2H5CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.51e+11, 'cm^3/(mol*s)'), n=0, Ea=(4810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 325,
    label = "CH3OCH3 + OH <=> CH3OCH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(935000, 'cm^3/(mol*s)'), n=2.29, Ea=(-781, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 326,
    label = "CH3OCH3 + H <=> CH3OCH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(36120, 'cm^3/(mol*s)'), n=2.88, Ea=(2996, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 327,
    label = "CH3OCH3 + O <=> CH3OCH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.75e+08, 'cm^3/(mol*s)'),
        n = 1.36,
        Ea = (2250, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 328,
    label = "CH3OCH3 + HO2 <=> CH3OCH2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.344e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17690, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 329,
    label = "CH3OCH3 + CH3O2 <=> CH3OCH2 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.344e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17690, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 330,
    label = "CH3OCH3 + CH3 <=> CH3OCH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.445e-06, 'cm^3/(mol*s)'),
        n = 5.73,
        Ea = (5699, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 331,
    label = "CH3OCH3 + O2 <=> CH3OCH2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(44910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 332,
    label = "CH3OCH3 + CH3O <=> CH3OCH2 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.02e+11, 'cm^3/(mol*s)'), n=0, Ea=(4074, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 333,
    label = "CH3OCH3 + CH3OCH2O2 <=> CH3OCH2 + CH3OCH2O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17690, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 334,
    label = "CH3OCH3 + O2CHO <=> CH3OCH2 + HO2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(44250, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 335,
    label = "CH3OCH3 + OCHO <=> CH3OCH2 + HCOOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(17690, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 336,
    label = "CH3OCH2 <=> CH2O + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 's^-1'), n=0, Ea=(25500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 337,
    label = "CH3OCH2 + CH3O <=> CH3OCH3 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 338,
    label = "CH3OCH2 + CH2O <=> CH3OCH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5490, 'cm^3/(mol*s)'), n=2.8, Ea=(5862, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 339,
    label = "CH3OCH2 + CH3CHO <=> CH3OCH3 + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.26e+12, 'cm^3/(mol*s)'), n=0, Ea=(8499, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 340,
    label = "CH3OCH2 + O2 <=> CH3OCH2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 341,
    label = "CH3OCH2O2 + CH2O <=> CH3OCH2O2H + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 342,
    label = "CH3OCH2O2 + CH3CHO <=> CH3OCH2O2H + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 343,
    label = "CH3OCH2O2 + CH3OCH2O2 <=> O2 + CH3OCH2O + CH3OCH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.21e+23, 'cm^3/(mol*s)'), n=-4.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 344,
    label = "CH3OCH2O + OH <=> CH3OCH2O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 345,
    label = "CH3O + CH2O <=> CH3OCH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 346,
    label = "CH3OCH2O2 <=> CH2OCH2O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+10, 's^-1'), n=0, Ea=(21580, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 347,
    label = "CH2OCH2O2H <=> OH + CH2O + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 's^-1'), n=0, Ea=(20760, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 348,
    label = "CH2OCH2O2H + O2 <=> O2CH2OCH2O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 349,
    label = "O2CH2OCH2O2H <=> HOOCH2OCHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+10, 's^-1'), n=0, Ea=(18580, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 350,
    label = "NC3H7 + H <=> C3H8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 351,
    label = "IC3H7 + H <=> C3H8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 352,
    label = "C3H8 + O2 <=> IC3H7 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(49640, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 353,
    label = "C3H8 + O2 <=> NC3H7 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(52290, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 354,
    label = "H + C3H8 <=> H2 + IC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+06, 'cm^3/(mol*s)'), n=2.4, Ea=(4471, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 355,
    label = "H + C3H8 <=> H2 + NC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.33e+06, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 356,
    label = "C3H8 + O <=> IC3H7 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(549000, 'cm^3/(mol*s)'), n=2.5, Ea=(3140, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 357,
    label = "C3H8 + O <=> NC3H7 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.71e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (5505, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 358,
    label = "C3H8 + OH <=> NC3H7 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.054e+10, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (1586, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 359,
    label = "C3H8 + OH <=> IC3H7 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.67e+07, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-35, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 360,
    label = "C3H8 + HO2 <=> IC3H7 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(58800, 'cm^3/(mol*s)'), n=2.5, Ea=(14860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 361,
    label = "C3H8 + HO2 <=> NC3H7 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(81000, 'cm^3/(mol*s)'), n=2.5, Ea=(16690, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 362,
    label = "CH3 + C3H8 <=> CH4 + IC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(64000, 'cm^3/(mol*s)'), n=2.17, Ea=(7520, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 363,
    label = "CH3 + C3H8 <=> CH4 + NC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.904, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 364,
    label = "IC3H7 + C3H8 <=> NC3H7 + C3H8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+10, 'cm^3/(mol*s)'), n=0, Ea=(12900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 365,
    label = "C2H3 + C3H8 <=> C2H4 + IC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 366,
    label = "C2H3 + C3H8 <=> C2H4 + NC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 367,
    label = "C2H5 + C3H8 <=> C2H6 + IC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 368,
    label = "C2H5 + C3H8 <=> C2H6 + NC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 369,
    label = "C3H8 + C3H5-A <=> NC3H7 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(20500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 370,
    label = "C3H8 + C3H5-A <=> IC3H7 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(16200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 371,
    label = "C3H8 + CH3O <=> NC3H7 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 372,
    label = "C3H8 + CH3O <=> IC3H7 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 373,
    label = "CH3O2 + C3H8 <=> CH3O2H + NC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(81000, 'cm^3/(mol*s)'), n=2.5, Ea=(16690, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 374,
    label = "CH3O2 + C3H8 <=> CH3O2H + IC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(58800, 'cm^3/(mol*s)'), n=2.5, Ea=(14860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 375,
    label = "C2H5O2 + C3H8 <=> C2H5O2H + NC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(81000, 'cm^3/(mol*s)'), n=2.5, Ea=(16690, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 376,
    label = "C2H5O2 + C3H8 <=> C2H5O2H + IC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(58800, 'cm^3/(mol*s)'), n=2.5, Ea=(14860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 377,
    label = "NC3H7O2 + C3H8 <=> NC3H7O2H + NC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 378,
    label = "NC3H7O2 + C3H8 <=> NC3H7O2H + IC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 379,
    label = "IC3H7O2 + C3H8 <=> IC3H7O2H + NC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 380,
    label = "IC3H7O2 + C3H8 <=> IC3H7O2H + IC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 381,
    label = "C3H8 + CH3CO3 <=> IC3H7 + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 382,
    label = "C3H8 + CH3CO3 <=> NC3H7 + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 383,
    label = "C3H8 + O2CHO <=> NC3H7 + HO2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(55200, 'cm^3/(mol*s)'), n=2.55, Ea=(16480, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 384,
    label = "C3H8 + O2CHO <=> IC3H7 + HO2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14750, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 385,
    label = "H + C3H6 <=> IC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.64e+13, 'cm^3/(mol*s)'), n=0, Ea=(2160, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 386,
    label = "IC3H7 + H <=> C2H5 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 387,
    label = "IC3H7 + O2 <=> C3H6 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.5e-19, 'cm^3/(mol*s)'), n=0, Ea=(5020, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 388,
    label = "IC3H7 + OH <=> C3H6 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 389,
    label = "IC3H7 + O <=> CH3COCH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.818e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 390,
    label = "IC3H7 + O <=> CH3CHO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.818e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 391,
    label = "NC3H7 <=> CH3 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.97e+40, 's^-1'), n=-8.6, Ea=(41430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 392,
    label = "NC3H7 <=> H + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.78e+39, 's^-1'), n=-8.1, Ea=(46580, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 393,
    label = "NC3H7 + O2 <=> C3H6 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e-19, 'cm^3/(mol*s)'), n=0, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 394,
    label = "C2H5CHO + NC3H7 <=> C2H5CO + C3H8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 395,
    label = "C2H5CHO + IC3H7 <=> C2H5CO + C3H8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 396,
    label = "C2H5CHO + C3H5-A <=> C2H5CO + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 397,
    label = "C3H6 <=> C3H5-S + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.71e+69, 's^-1'), n=-16.09, Ea=(140000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 398,
    label = "C3H6 <=> C3H5-T + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.62e+71, 's^-1'), n=-16.58, Ea=(139300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 399,
    label = "C3H6 + O <=> C2H5 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+07, 'cm^3/(mol*s)'),
        n = 1.76,
        Ea = (-1216, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 400,
    label = "C3H6 + O <=> CH2CO + CH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+07, 'cm^3/(mol*s)'), n=1.76, Ea=(76, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 401,
    label = "C3H6 + O <=> CH3CHCO + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+07, 'cm^3/(mol*s)'), n=1.76, Ea=(76, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 402,
    label = "C3H6 + O <=> C3H5-A + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.24e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (5884, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 403,
    label = "C3H6 + O <=> C3H5-S + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0.7, Ea=(8959, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 404,
    label = "C3H6 + O <=> C3H5-T + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+10, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (7632, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 405,
    label = "C3H6 + OH <=> C3H5-A + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 406,
    label = "C3H6 + OH <=> C3H5-S + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.11e+06, 'cm^3/(mol*s)'), n=2, Ea=(2778, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 407,
    label = "C3H6 + OH <=> C3H5-T + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.11e+06, 'cm^3/(mol*s)'), n=2, Ea=(1451, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 408,
    label = "C3H6 + HO2 <=> C3H5-A + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27000, 'cm^3/(mol*s)'), n=2.5, Ea=(12340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 409,
    label = "C3H6 + HO2 <=> C3H5-S + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(18000, 'cm^3/(mol*s)'), n=2.5, Ea=(27620, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 410,
    label = "C3H6 + HO2 <=> C3H5-T + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9000, 'cm^3/(mol*s)'), n=2.5, Ea=(23590, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 411,
    label = "C3H6 + H <=> C2H4 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+24, 'cm^3/(mol*s)'),
        n = -3.04,
        Ea = (15610, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 412,
    label = "C3H6 + H <=> C3H5-A + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(173000, 'cm^3/(mol*s)'), n=2.5, Ea=(2490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 413,
    label = "C3H6 + H <=> C3H5-T + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(400000, 'cm^3/(mol*s)'), n=2.5, Ea=(9790, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 414,
    label = "C3H6 + H <=> C3H5-S + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(804000, 'cm^3/(mol*s)'), n=2.5, Ea=(12283, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 415,
    label = "C3H6 + O2 <=> C3H5-A + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(39900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 416,
    label = "C3H6 + O2 <=> C3H5-S + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(62900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 417,
    label = "C3H6 + O2 <=> C3H5-T + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(60700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 418,
    label = "C3H6 + CH3 <=> C3H5-A + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.21, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 419,
    label = "C3H6 + CH3 <=> C3H5-S + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.348, 'cm^3/(mol*s)'), n=3.5, Ea=(12850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 420,
    label = "C3H6 + CH3 <=> C3H5-T + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.84, 'cm^3/(mol*s)'), n=3.5, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 421,
    label = "C3H6 + C2H5 <=> C3H5-A + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(9800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 422,
    label = "C3H6 + CH3CO3 <=> C3H5-A + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.24e+11, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 423,
    label = "C3H6 + CH3O2 <=> C3H5-A + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.24e+11, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 424,
    label = "C3H6 + HO2 <=> C3H6O1-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.29e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 425,
    label = "C3H6 + C2H5O2 <=> C3H5-A + C2H5O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.24e+11, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 426,
    label = "C3H6 + NC3H7O2 <=> C3H5-A + NC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.24e+11, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 427,
    label = "C3H6 + IC3H7O2 <=> C3H5-A + IC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.24e+11, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 428,
    label = "C3H6 + OH <=> C3H6OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.93e+11, 'cm^3/(mol*s)'), n=0, Ea=(-960, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 429,
    label = "C3H6OH + O2 <=> HOC3H6O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 430,
    label = "HOC3H6O2 <=> CH3CHO + CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(18900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 431,
    label = "C3H5-A + H <=> C3H4-A + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 432,
    label = "C3H5-A + O <=> C2H3CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 433,
    label = "C3H5-A + OH <=> C2H3CHO + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+20, 'cm^3/(mol*s)'),
        n = -1.56,
        Ea = (26330, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 434,
    label = "C3H5-A + OH <=> C3H4-A + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 435,
    label = "C3H5-A + O2 <=> C3H4-A + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.18e+21, 'cm^3/(mol*s)'),
        n = -2.85,
        Ea = (30755, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 436,
    label = "C3H5-A + O2 <=> CH3CO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.14e+15, 'cm^3/(mol*s)'),
        n = -1.21,
        Ea = (21046, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 437,
    label = "C3H5-A + O2 <=> C2H3CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.47e+13, 'cm^3/(mol*s)'),
        n = -0.45,
        Ea = (23017, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 438,
    label = "C3H5-A + HCO <=> C3H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 439,
    label = "C3H5-A + CH3 <=> C3H4-A + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=-0.32, Ea=(-131, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 440,
    label = "C3H5-A <=> C3H5-T",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.86e+53, 's^-1'), n=-12.81, Ea=(75883, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 441,
    label = "C3H5-A <=> C3H5-S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.7e+48, 's^-1'), n=-11.73, Ea=(73700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 442,
    label = "C2H2 + CH3 <=> C3H5-A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.04e+51, 'cm^3/(mol*s)'),
        n = -11.89,
        Ea = (36476, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 443,
    label = "C3H5-A + CH3O2 <=> C3H5O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 444,
    label = "C3H5-A + C2H5 <=> C2H6 + C3H4-A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 445,
    label = "C3H5-A + C2H5 <=> C2H4 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 446,
    label = "C3H5-A + C2H3 <=> C2H4 + C3H4-A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 447,
    label = "C3H5-A + C3H5-A <=> C3H4-A + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.43e+10, 'cm^3/(mol*s)'), n=0, Ea=(-262, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 448,
    label = "C3H5-A + HO2 <=> C3H5O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 449,
    label = "C2H2 + CH3 <=> C3H5-S",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+38, 'cm^3/(mol*s)'),
        n = -8.21,
        Ea = (17100, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 450,
    label = "C3H5-S + H <=> C3H4-P + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.34e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 451,
    label = "C3H5-S + O <=> C2H4 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 452,
    label = "C3H5-S + OH <=> C2H4 + HCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 453,
    label = "C3H5-S + O2 <=> CH3CHO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 454,
    label = "C3H5-S + HO2 <=> C2H4 + HCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 455,
    label = "C3H5-S + HCO <=> C3H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 456,
    label = "C3H5-S + CH3 <=> C3H4-P + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 457,
    label = "C2H2 + CH3 <=> C3H5-T",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.31e+25, 'cm^3/(mol*s)'),
        n = -5.06,
        Ea = (21150, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 458,
    label = "C3H5-T <=> C3H5-S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.1e+52, 's^-1'), n=-13.37, Ea=(57200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 459,
    label = "C3H5-T + H <=> C3H4-P + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.34e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 460,
    label = "C3H5-T + O <=> CH3 + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 461,
    label = "C3H5-T + OH <=> CH3 + CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 462,
    label = "C3H5-T + O2 <=> CH3CO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 463,
    label = "C3H5-T + HO2 <=> CH3 + CH2CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 464,
    label = "C3H5-T + HCO <=> C3H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 465,
    label = "C3H5-T + CH3 <=> C3H4-P + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 466,
    label = "C2H2 + CH3 <=> C3H4-A + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.2e+10, 'cm^3/(mol*s)'),
        n = 0.54,
        Ea = (23950, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 467,
    label = "C3H4-A + H <=> C3H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+06, 'cm^3/(mol*s)'), n=2, Ea=(5500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 468,
    label = "C3H4-A + H <=> C3H5-S",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+31, 'cm^3/(mol*s)'),
        n = -6.23,
        Ea = (18700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 469,
    label = "C3H4-A + H <=> C3H5-T",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.98e+44, 'cm^3/(mol*s)'),
        n = -9.7,
        Ea = (14032, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 470,
    label = "C3H4-A + H <=> C3H5-A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.34e+54, 'cm^3/(mol*s)'),
        n = -12.09,
        Ea = (26187, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 471,
    label = "C3H4-A + O <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+07, 'cm^3/(mol*s)'), n=1.8, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 472,
    label = "C3H4-A + OH <=> C3H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+06, 'cm^3/(mol*s)'), n=2, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 473,
    label = "C3H4-A + CH3 <=> C3H3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 474,
    label = "C3H4-A + C2H <=> C2H2 + C3H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 475,
    label = "C3H4-A + C3H4-A <=> C3H5-A + C3H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+14, 'cm^3/(mol*s)'), n=0, Ea=(64746.7, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 476,
    label = "C3H4-A + C3H5-A <=> C3H3 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 477,
    label = "C3H4-P <=> CC3H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.92e+40, 's^-1'), n=-8.69, Ea=(68706, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 478,
    label = "C3H4-P <=> C3H4-A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+58, 's^-1'), n=-13.07, Ea=(92680, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 479,
    label = "C3H4-P + H <=> C3H4-A + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.93e+18, 'cm^3/(mol*s)'),
        n = -1.01,
        Ea = (11523, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 480,
    label = "C3H4-P + H <=> C3H5-T",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.62e+47, 'cm^3/(mol*s)'),
        n = -10.55,
        Ea = (15910, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 481,
    label = "C3H4-P + H <=> C3H5-S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+34, 'cm^3/(mol*s)'), n=-6.88, Ea=(8900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 482,
    label = "C3H4-P + H <=> C3H5-A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.02e+59, 'cm^3/(mol*s)'),
        n = -13.89,
        Ea = (33953, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 483,
    label = "C3H4-P + H <=> C3H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+06, 'cm^3/(mol*s)'), n=2, Ea=(5500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 484,
    label = "C3H4-P + C3H3 <=> C3H4-A + C3H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.14e+06, 'cm^3/(mol*s)'),
        n = 1.74,
        Ea = (10450, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 485,
    label = "C3H4-P + O <=> HCCO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(2250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 486,
    label = "C3H4-P + O <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(2250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 487,
    label = "C3H4-P + OH <=> C3H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+06, 'cm^3/(mol*s)'), n=2, Ea=(100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 488,
    label = "C3H4-P + C2H <=> C2H2 + C3H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 489,
    label = "C3H4-P + CH3 <=> C3H3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 490,
    label = "C2H2 + CH3 <=> C3H4-P + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e+11, 'cm^3/(mol*s)'),
        n = 0.56,
        Ea = (15453, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 491,
    label = "C3H4-P + C2H3 <=> C3H3 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 492,
    label = "C3H4-P + C3H5-A <=> C3H3 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 493,
    label = "CC3H4 <=> C3H4-A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.33e+41, 's^-1'), n=-8.93, Ea=(50475, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 494,
    label = "C3H3 + H <=> C3H4-P",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 495,
    label = "C3H3 + H <=> C3H4-A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 496,
    label = "C3H3 + H <=> C3H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 497,
    label = "C3H3 + O <=> CH2O + C2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 498,
    label = "C3H3 + OH <=> C3H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 499,
    label = "C3H3 + O2 <=> CH2CO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+10, 'cm^3/(mol*s)'), n=0, Ea=(2868, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 500,
    label = "C3H3 + HO2 <=> OH + CO + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 501,
    label = "C3H3 + HO2 <=> C3H4-A + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 502,
    label = "C3H3 + HO2 <=> C3H4-P + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 503,
    label = "C3H3 + HCO <=> C3H4-A + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 504,
    label = "C3H3 + HCO <=> C3H4-P + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 505,
    label = "C3H3 + HCCO <=> C4H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 506,
    label = "C3H3 + CH <=> C4H3-I + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 507,
    label = "C3H3 + CH2 <=> C4H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 508,
    label = "C2H5 + C2H <=> C3H3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 509,
    label = "C3H2 + H <=> C3H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 510,
    label = "C3H2 + O <=> C2H2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/doi:10.1016/S0010-2180(99)00070-X atrributes this to [estimated]!
""",
)

entry(
    index = 511,
    label = "C3H2 + OH <=> HCO + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 512,
    label = "C3H2 + O2 <=> HCCO + H + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 513,
    label = "C3H2 + CH <=> C4H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 514,
    label = "C3H2 + CH2 <=> C4H3-N + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 515,
    label = "C3H2 + CH3 <=> C4H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 516,
    label = "C3H2 + HCCO <=> C4H3-N + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 517,
    label = "C3H2 + O2 <=> HCO + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 518,
    label = "CH3CHCO + OH <=> C2H5 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.73e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 519,
    label = "CH3CHCO + OH <=> SC2H4OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 520,
    label = "CH3CHCO + H <=> C2H5 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(1459, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 521,
    label = "CH3CHCO + O <=> CH3CHO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(-437, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 522,
    label = "NC3H7 + HO2 <=> NC3H7O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 523,
    label = "IC3H7 + HO2 <=> IC3H7O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 524,
    label = "CH3O2 + NC3H7 <=> CH3O + NC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 525,
    label = "CH3O2 + IC3H7 <=> CH3O + IC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 526,
    label = "NC3H7 + O2 <=> NC3H7O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 527,
    label = "IC3H7 + O2 <=> IC3H7O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 528,
    label = "NC3H7O2 + CH2O <=> NC3H7O2H + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 529,
    label = "NC3H7O2 + CH3CHO <=> NC3H7O2H + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 530,
    label = "IC3H7O2 + CH2O <=> IC3H7O2H + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 531,
    label = "IC3H7O2 + CH3CHO <=> IC3H7O2H + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 532,
    label = "NC3H7O2 + HO2 <=> NC3H7O2H + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 533,
    label = "IC3H7O2 + HO2 <=> IC3H7O2H + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 534,
    label = "C2H4 + NC3H7O2 <=> C2H3 + NC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 535,
    label = "C2H4 + IC3H7O2 <=> C2H3 + IC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 536,
    label = "CH3OH + NC3H7O2 <=> CH2OH + NC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 537,
    label = "CH3OH + IC3H7O2 <=> CH2OH + IC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 538,
    label = "C2H3CHO + NC3H7O2 <=> C2H3CO + NC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 539,
    label = "C2H3CHO + IC3H7O2 <=> C2H3CO + IC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 540,
    label = "CH4 + NC3H7O2 <=> CH3 + NC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(24640, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 541,
    label = "CH4 + IC3H7O2 <=> CH3 + IC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(24640, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 542,
    label = "NC3H7O2 + CH3O2 <=> NC3H7O + CH3O + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 543,
    label = "IC3H7O2 + CH3O2 <=> IC3H7O + CH3O + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 544,
    label = "H2 + NC3H7O2 <=> H + NC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 545,
    label = "H2 + IC3H7O2 <=> H + IC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 546,
    label = "IC3H7O2 + C2H6 <=> IC3H7O2H + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 547,
    label = "NC3H7O2 + C2H6 <=> NC3H7O2H + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 548,
    label = "IC3H7O2 + C2H5CHO <=> IC3H7O2H + C2H5CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 549,
    label = "NC3H7O2 + C2H5CHO <=> NC3H7O2H + C2H5CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 550,
    label = "IC3H7O2 + CH3CO3 <=> IC3H7O + CH3CO2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 551,
    label = "NC3H7O2 + CH3CO3 <=> NC3H7O + CH3CO2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 552,
    label = "IC3H7O2 + C2H5O2 <=> IC3H7O + C2H5O + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 553,
    label = "NC3H7O2 + C2H5O2 <=> NC3H7O + C2H5O + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 554,
    label = "IC3H7O2 + IC3H7O2 <=> O2 + IC3H7O + IC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 555,
    label = "NC3H7O2 + NC3H7O2 <=> O2 + NC3H7O + NC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 556,
    label = "IC3H7O2 + NC3H7O2 <=> IC3H7O + NC3H7O + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 557,
    label = "IC3H7O2 + CH3 <=> IC3H7O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 558,
    label = "IC3H7O2 + C2H5 <=> IC3H7O + C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 559,
    label = "IC3H7O2 + IC3H7 <=> IC3H7O + IC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 560,
    label = "IC3H7O2 + NC3H7 <=> IC3H7O + NC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 561,
    label = "IC3H7O2 + C3H5-A <=> IC3H7O + C3H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 562,
    label = "NC3H7O2 + CH3 <=> NC3H7O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 563,
    label = "NC3H7O2 + C2H5 <=> NC3H7O + C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 564,
    label = "NC3H7O2 + IC3H7 <=> NC3H7O + IC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 565,
    label = "NC3H7O2 + NC3H7 <=> NC3H7O + NC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 566,
    label = "NC3H7O2 + C3H5-A <=> NC3H7O + C3H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 567,
    label = "NC3H7O2H <=> NC3H7O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 568,
    label = "IC3H7O2H <=> IC3H7O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.45e+15, 's^-1'), n=0, Ea=(42600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 569,
    label = "C2H5 + CH2O <=> NC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(3496, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 570,
    label = "C2H5CHO + H <=> NC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(6260, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 571,
    label = "CH3 + CH3CHO <=> IC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(9256, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 572,
    label = "CH3COCH3 + H <=> IC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(7270, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 573,
    label = "IC3H7O + O2 <=> CH3COCH3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.09e+09, 'cm^3/(mol*s)'), n=0, Ea=(390, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 574,
    label = "NC3H7O2 <=> C3H6OOH1-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(26850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 575,
    label = "NC3H7O2 <=> C3H6OOH1-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.125e+11, 's^-1'), n=0, Ea=(24400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 576,
    label = "IC3H7O2 <=> C3H6OOH2-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+12, 's^-1'), n=0, Ea=(29400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 577,
    label = "IC3H7O2 <=> CH3COCH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.23e+35, 's^-1'), n=-6.96, Ea=(48880, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 578,
    label = "C3H6OOH1-2 <=> C3H6O1-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 579,
    label = "C3H6OOH1-3 <=> C3H6O1-3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 580,
    label = "C3H6OOH2-1 <=> C3H6O1-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 581,
    label = "C3H6 + HO2 <=> C3H6OOH1-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 582,
    label = "C3H6 + HO2 <=> C3H6OOH2-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 583,
    label = "C3H6OOH1-3 <=> OH + CH2O + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.035e+15, 's^-1'), n=-0.79, Ea=(27400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 584,
    label = "C3H6OOH2-1 <=> C2H3OOH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.54e+27, 's^-1'), n=-5.14, Ea=(38320, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 585,
    label = "C3H6OOH1-2 <=> C2H4 + CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.31e+33, 's^-1'), n=-7.01, Ea=(48120, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 586,
    label = "C3H6OOH1-2 + O2 <=> C3H6OOH1-2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 587,
    label = "C3H6OOH1-3 + O2 <=> C3H6OOH1-3O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 588,
    label = "C3H6OOH2-1 + O2 <=> C3H6OOH2-1O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 589,
    label = "C3H6OOH1-2O2 <=> C3KET12 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(26400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 590,
    label = "C3H6OOH1-3O2 <=> C3KET13 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(21400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 591,
    label = "C3H6OOH2-1O2 <=> CH3COCH2O2H + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 's^-1'), n=0, Ea=(23850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 592,
    label = "C3H6OOH2-1O2 <=> C3H51-2,3OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.125e+11, 's^-1'), n=0, Ea=(24400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 593,
    label = "C3H6OOH1-2O2 <=> C3H51-2,3OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+11, 's^-1'), n=0, Ea=(29400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 594,
    label = "C3H51-2,3OOH <=> AC3H5OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.56e+13, 's^-1'), n=-0.49, Ea=(17770, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 595,
    label = "C3H6OOH1-3O2 <=> C3H52-1,3OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(26850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 596,
    label = "C3H52-1,3OOH <=> AC3H5OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.15e+14, 's^-1'), n=-0.63, Ea=(17250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 597,
    label = "C3KET12 <=> CH3CHO + HCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.45e+15, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 598,
    label = "C3KET13 <=> CH2O + CH2CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 599,
    label = "CH3COCH2O2H <=> CH2O + CH3CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 600,
    label = "C3H5O + OH <=> AC3H5OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 601,
    label = "C3H5O <=> C2H3CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(29100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 602,
    label = "C2H3 + CH2O <=> C3H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(10600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 603,
    label = "C3H5O + O2 <=> C2H3CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(6000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 604,
    label = "C2H3OOH <=> CH2CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.4e+14, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 605,
    label = "C3H6O1-2 <=> C2H4 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+14, 's^-1'), n=0, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 606,
    label = "C3H6O1-2 + OH <=> CH2O + C2H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 607,
    label = "C3H6O1-2 + H <=> CH2O + C2H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.63e+07, 'cm^3/(mol*s)'), n=2, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 608,
    label = "C3H6O1-2 + O <=> CH2O + C2H3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.43e+13, 'cm^3/(mol*s)'), n=0, Ea=(5200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 609,
    label = "C3H6O1-2 + HO2 <=> CH2O + C2H3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 610,
    label = "C3H6O1-2 + CH3O2 <=> CH2O + C2H3 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 611,
    label = "C3H6O1-2 + CH3 <=> CH2O + C2H3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 612,
    label = "C3H6O1-3 <=> C2H4 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+14, 's^-1'), n=0, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 613,
    label = "C3H6O1-3 + OH <=> CH2O + C2H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 614,
    label = "C3H6O1-3 + O <=> CH2O + C2H3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.43e+13, 'cm^3/(mol*s)'), n=0, Ea=(5200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 615,
    label = "C3H6O1-3 + H <=> CH2O + C2H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.63e+07, 'cm^3/(mol*s)'), n=2, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 616,
    label = "C3H6O1-3 + CH3O2 <=> CH2O + C2H3 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 617,
    label = "C3H6O1-3 + HO2 <=> CH2O + C2H3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 618,
    label = "C3H6O1-3 + CH3 <=> CH2O + C2H3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 619,
    label = "IC3H7O2 <=> C3H6 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.015e+43, 's^-1'), n=-9.41, Ea=(41490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 620,
    label = "NC3H7O2 <=> C3H6 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.044e+38, 's^-1'), n=-8.11, Ea=(40490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 621,
    label = "CH2CCH2OH + H2O2 <=> C3H5OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+09, 'cm^3/(mol*s)'), n=0, Ea=(2583, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 622,
    label = "C3H5OH + OH <=> CH2CCH2OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.06e+12, 'cm^3/(mol*s)'), n=0, Ea=(5960, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 623,
    label = "C3H5OH + H <=> CH2CCH2OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(390000, 'cm^3/(mol*s)'), n=2.5, Ea=(5821, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 624,
    label = "C3H5OH + O2 <=> CH2CCH2OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(60690, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 625,
    label = "C3H5OH + CH3 <=> CH2CCH2OH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+11, 'cm^3/(mol*s)'), n=0, Ea=(8030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 626,
    label = "CH2CCH2OH + H <=> C3H5OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 627,
    label = "CH2CCH2OH + O2 <=> CH2OH + CO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.335e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 628,
    label = "CH2CCH2OH <=> C2H2 + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.163e+40, 's^-1'), n=-8.31, Ea=(45110, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 629,
    label = "C3H4-A + OH <=> CH2CCH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 630,
    label = "H + CH2OCHO <=> CH3OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 631,
    label = "H + CH3OCO <=> CH3OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 632,
    label = "CH3OCHO + H <=> CH2OCHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (665417, 'cm^3/(mol*s)'),
        n = 2.537,
        Ea = (6494.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 633,
    label = "CH3OCHO + OH <=> CH2OCHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.858e+12, 'cm^3/(mol*s)'),
        n = 0.054,
        Ea = (3340.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 634,
    label = "CH3OCHO + CH3 <=> CH2OCHO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.291, 'cm^3/(mol*s)'), n=3.7, Ea=(6823.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 635,
    label = "CH3OCHO + HO2 <=> CH2OCHO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (56594.9, 'cm^3/(mol*s)'),
        n = 2.44,
        Ea = (16594.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 636,
    label = "CH3OCHO + CH3O2 <=> CH2OCHO + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (56594.9, 'cm^3/(mol*s)'),
        n = 2.44,
        Ea = (16594.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 637,
    label = "CH3OCHO + CH3O <=> CH2OCHO + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.59e+09, 'cm^3/(mol*s)'),
        n = 0.45,
        Ea = (4823.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 638,
    label = "CH3OCHO + O <=> CH2OCHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (884347, 'cm^3/(mol*s)'),
        n = 2.44,
        Ea = (4593.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 639,
    label = "CH3OCHO + O2 <=> CH2OCHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.533e+13, 'cm^3/(mol*s)'),
        n = 0.0796,
        Ea = (51749.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 640,
    label = "CH3OCHO + HCO <=> CH2OCHO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(102500, 'cm^3/(mol*s)'), n=2.5, Ea=(18430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 641,
    label = "CH3OCHO + C2H5 <=> CH2OCHO + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 642,
    label = "CH3OCHO + C2H3 <=> CH2OCHO + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 643,
    label = "CH3OCHO + OCHO <=> CH2OCHO + HCOOH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (56594.9, 'cm^3/(mol*s)'),
        n = 2.44,
        Ea = (16594.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 644,
    label = "CH3OCHO + H <=> CH3OCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (257664, 'cm^3/(mol*s)'),
        n = 2.52,
        Ea = (5736.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 645,
    label = "CH3OCHO + OH <=> CH3OCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.22e+16, 'cm^3/(mol*s)'),
        n = -0.981,
        Ea = (4946.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 646,
    label = "CH3OCHO + CH3 <=> CH3OCO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.09212, 'cm^3/(mol*s)'),
        n = 3.69,
        Ea = (6052.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 647,
    label = "CH3OCHO + CH3O2 <=> CH3OCO + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (156602, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (16544.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 648,
    label = "CH3OCHO + HO2 <=> CH3OCO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (156602, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (16544.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 649,
    label = "CH3OCHO + CH3O <=> CH3OCO + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.27e+09, 'cm^3/(mol*s)'),
        n = 0.83,
        Ea = (2912.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 650,
    label = "CH3OCHO + O <=> CH3OCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (245142, 'cm^3/(mol*s)'),
        n = 2.47,
        Ea = (4047.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 651,
    label = "CH3OCHO + O2 <=> CH3OCO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.847e+12, 'cm^3/(mol*s)'),
        n = 0.113,
        Ea = (50759.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 652,
    label = "CH3OCHO + HCO <=> CH3OCO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.4e+06, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (17010, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 653,
    label = "CH3OCHO + C2H5 <=> CH3OCO + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 654,
    label = "CH3OCHO + C2H3 <=> CH3OCO + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 655,
    label = "CH3OCHO + OCHO <=> CH3OCO + HCOOH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (156602, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (16544.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 656,
    label = "CH3OCO + CH3OCHO <=> CH3OCHO + CH2OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 657,
    label = "CH3 + CO2 <=> CH3OCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.76e+07, 'cm^3/(mol*s)'),
        n = 1.54,
        Ea = (34700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 658,
    label = "CH3O + CO <=> CH3OCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.55e+06, 'cm^3/(mol*s)'),
        n = 2.02,
        Ea = (5730, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 659,
    label = "CH2OCHO <=> CH3OCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.62e+11, 's^-1'), n=-0.03, Ea=(38178, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 660,
    label = "CH2O + HCO <=> CH2OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.89e+11, 'cm^3/(mol*s)'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 661,
    label = "OCH2OCHO <=> HOCH2OCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 662,
    label = "HOCH2OCO <=> HOCH2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.238e+19, 's^-1'), n=-2.02, Ea=(19690, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 663,
    label = "HOCH2OCO <=> CH2OH + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.413e+17, 's^-1'), n=-1.57, Ea=(22120, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 664,
    label = "CH2O + OCHO <=> OCH2OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.89e+11, 'cm^3/(mol*s)'), n=0, Ea=(2500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 665,
    label = "CH3OCO + HCO <=> CH3OCHO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 666,
    label = "CH2OCHO + HCO <=> CH3OCHO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 667,
    label = "CH2OCHO + HO2 <=> HOOCH2OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 668,
    label = "OCH2OCHO + OH <=> HOOCH2OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.55e+06, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (-4132, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 669,
    label = "CH3OCO + CH3O <=> OCH2OCHO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 670,
    label = "CH2OCHO + O2 <=> OOCH2OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 671,
    label = "OCH2O2H + CO <=> HOOCH2OC*O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+07, 'cm^3/(mol*s)'),
        n = 1.633,
        Ea = (5588, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 672,
    label = "OCHO + CO <=> CHOOCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 673,
    label = "HCO + CO2 <=> CHOOCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(36730, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 674,
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
    index = 675,
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
    index = 676,
    label = "O + H <=> OH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.714e+18, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'O=C=O': 3.8, 'O': 12, '[H][H]': 2.5, '[He]': 0.75, '[C]=O': 1.9, '[Ar]': 0.75},
    ),
)

entry(
    index = 677,
    label = "H + OH <=> H2O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.8e+22, 'cm^6/(mol^2*s)'), n=-2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'O=C=O': 3.8, 'O': 12, '[H][H]': 2.5, '[He]': 0.38, '[C]=O': 1.9, '[Ar]': 0.38},
    ),
)

entry(
    index = 678,
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
    index = 679,
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
    index = 680,
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
    index = 681,
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
    index = 682,
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
    index = 683,
    label = "CH2O <=> CO + H2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.1e+45, 'cm^3/(mol*s)'), n=-8, Ea=(97510, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[H][H]': 2.5, '[C]=O': 1.9, 'O=C=O': 3.8, 'O': 12, '[Ar]': 0.7},
    ),
)

entry(
    index = 684,
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
    index = 685,
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
    index = 686,
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
    index = 687,
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
    index = 688,
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
    index = 689,
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
    index = 690,
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
    index = 691,
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
    index = 692,
    label = "CH2(S) <=> CH2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(600, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[C]=O': 0, 'O=C=O': 0, 'O': 0, '[Ar]': 0},
    ),
)

entry(
    index = 693,
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
    index = 694,
    label = "CH2OH <=> CH2O + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(25100, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

entry(
    index = 695,
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
    index = 696,
    label = "HCOOH <=> CO + H2O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(50000, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

entry(
    index = 697,
    label = "HCOOH <=> CO2 + H2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.5e+16, 'cm^3/(mol*s)'), n=0, Ea=(57000, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

entry(
    index = 698,
    label = "C2H5 + H <=> C2H6",
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
        alpha = 0.842,
        T3 = (125, 'K'),
        T1 = (2219, 'K'),
        T2 = (6882, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 699,
    label = "H + C2H4 <=> C2H5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (8.1e+11, 'cm^3/(mol*s)'),
            n = 0.454,
            Ea = (1820, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (9e+41, 'cm^6/(mol^2*s)'),
            n = -7.62,
            Ea = (6970, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.9753,
        T3 = (210, 'K'),
        T1 = (984, 'K'),
        T2 = (4374, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 700,
    label = "CH3CO <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(3e+12, 's^-1'), n=0, Ea=(16720, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(1.2e+15, 'cm^3/(mol*s)'), n=0, Ea=(12518, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

entry(
    index = 701,
    label = "CH3CO2 <=> CH3 + CO2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.4e+15, 'cm^3/(mol*s)'), n=0, Ea=(10500, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

entry(
    index = 702,
    label = "HCCO <=> CH + CO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(6.5e+15, 'cm^3/(mol*s)'), n=0, Ea=(58820, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

entry(
    index = 703,
    label = "C2H3 + H <=> C2H4",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.36e+14, 'cm^3/(mol*s)'),
            n = 0.17,
            Ea = (660, 'cal/mol'),
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
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 704,
    label = "C2H4 <=> C2H2 + H2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8e+12, 's^-1'), n=0.44, Ea=(88770, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.58e+51, 'cm^3/(mol*s)'),
            n = -9.3,
            Ea = (97800, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.735,
        T3 = (180, 'K'),
        T1 = (1035, 'K'),
        T2 = (5417, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 705,
    label = "C2H2 + H <=> C2H3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(2400, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.8e+40, 'cm^6/(mol^2*s)'),
            n = -7.27,
            Ea = (7220, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.751,
        T3 = (98.5, 'K'),
        T1 = (1302, 'K'),
        T2 = (4167, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 706,
    label = "C2H + H <=> C2H2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+17, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.75e+33, 'cm^6/(mol^2*s)'),
            n = -4.8,
            Ea = (1900, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.646,
        T3 = (132, 'K'),
        T1 = (1315, 'K'),
        T2 = (5566, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 707,
    label = "C2H5OH <=> CH2OH + CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.71e+23, 's^-1'), n=-1.68, Ea=(94400, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.11e+85, 'cm^3/(mol*s)'),
            n = -18.84,
            Ea = (113100, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (550, 'K'),
        T1 = (825, 'K'),
        T2 = (6100, 'K'),
        efficiencies = {'[H][H]': 2, '[C]=O': 2, 'O=C=O': 3, 'O': 5},
    ),
)

entry(
    index = 708,
    label = "C2H5OH <=> C2H5 + OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.4e+23, 's^-1'), n=-1.62, Ea=(99540, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.11e+85, 'cm^3/(mol*s)'),
            n = -18.8,
            Ea = (118770, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (650, 'K'),
        T1 = (800, 'K'),
        T2 = (1e+15, 'K'),
        efficiencies = {'[H][H]': 2, '[C]=O': 2, 'O=C=O': 3, 'O': 5},
    ),
)

entry(
    index = 709,
    label = "C2H5OH <=> C2H4 + H2O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.79e+13, 's^-1'), n=0.09, Ea=(66140, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.57e+83, 'cm^3/(mol*s)'),
            n = -18.85,
            Ea = (86453, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7,
        T3 = (350, 'K'),
        T1 = (800, 'K'),
        T2 = (3800, 'K'),
        efficiencies = {'O': 5},
    ),
)

entry(
    index = 710,
    label = "C2H5OH <=> CH3CHO + H2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(7.24e+11, 's^-1'), n=0.1, Ea=(91010, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.46e+87, 'cm^3/(mol*s)'),
            n = -19.42,
            Ea = (115580, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.9,
        T3 = (900, 'K'),
        T1 = (1100, 'K'),
        T2 = (3500, 'K'),
        efficiencies = {'O': 5},
    ),
)

entry(
    index = 711,
    label = "SC2H4OH <=> CH3CHO + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(25000, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

entry(
    index = 712,
    label = "CH3COCH3 <=> CH3CO + CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(7.108e+21, 's^-1'), n=-1.57, Ea=(84680, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (7.013e+89, 'cm^3/(mol*s)'),
            n = -20.38,
            Ea = (107150, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.863,
        T3 = (1e+10, 'K'),
        T1 = (416.4, 'K'),
        T2 = (3.29e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 713,
    label = "CH3OCH3 <=> CH3 + CH3O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.848e+21, 's^-1'), n=-1.56, Ea=(83130, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.118e+71, 'cm^3/(mol*s)'),
            n = -14.53,
            Ea = (100430, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.843,
        T3 = (9.49e+09, 'K'),
        T1 = (556.36, 'K'),
        T2 = (6.71e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 714,
    label = "C3H8 <=> CH3 + C2H5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.29e+37, 's^-1'), n=-5.84, Ea=(97380, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.64e+74, 'cm^3/(mol*s)'),
            n = -15.74,
            Ea = (98714, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.31,
        T3 = (50, 'K'),
        T1 = (3000, 'K'),
        T2 = (9000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 715,
    label = "C3H5-A + H <=> C3H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.33e+60, 'cm^6/(mol^2*s)'),
            n = -12,
            Ea = (5967.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.02,
        T3 = (1096.6, 'K'),
        T1 = (1096.6, 'K'),
        T2 = (6859.5, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 716,
    label = "C2H3 + CH3 <=> C3H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.27e+58, 'cm^6/(mol^2*s)'),
            n = -11.94,
            Ea = (9769.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.175,
        T3 = (1340.6, 'K'),
        T1 = (60000, 'K'),
        T2 = (10139.8, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, 'C=C': 3, 'C#C': 3, '[Ar]': 0.7},
    ),
)

entry(
    index = 717,
    label = "C3H5-A + CH3 <=> C4H8-1",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1e+14, 'cm^3/(mol*s)'),
            n = -0.32,
            Ea = (-262.3, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.91e+60, 'cm^6/(mol^2*s)'),
            n = -12.81,
            Ea = (6250, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.104,
        T3 = (1606, 'K'),
        T1 = (60000, 'K'),
        T2 = (6118.4, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 718,
    label = "CH3OCHO <=> CH3OH + CO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2e+13, 's^-1'), n=0, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.4e+59, 'cm^3/(mol*s)'),
            n = -11.8,
            Ea = (71400, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.23991,
        T3 = (555.11, 'K'),
        T1 = (8.33678e+09, 'K'),
        T2 = (8.21394e+09, 'K'),
        efficiencies = {'O=C=O': 5.4, 'O': 6, '[H][H]': 3, '[He]': 1.2, '[O][O]': 1.1, '[C]=O': 2.7},
    ),
)

entry(
    index = 719,
    label = "CH3OCHO <=> CH4 + CO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.5e+12, 's^-1'), n=0, Ea=(59700, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.63e+61, 'cm^3/(mol*s)'),
            n = -12.79,
            Ea = (71100, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.179405,
        T3 = (357.541, 'K'),
        T1 = (9.91871e+09, 'K'),
        T2 = (3.2899e+09, 'K'),
        efficiencies = {'O=C=O': 5.4, 'O': 6, '[H][H]': 3, '[He]': 1.2, '[O][O]': 1.1, '[C]=O': 2.7},
    ),
)

entry(
    index = 720,
    label = "CH3OCHO <=> CH2O + CH2O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+12, 's^-1'), n=0, Ea=(60500, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.55e+57, 'cm^3/(mol*s)'),
            n = -11.57,
            Ea = (71700, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.780745,
        T3 = (6.49013e+09, 'K'),
        T1 = (618.799, 'K'),
        T2 = (6.7101e+09, 'K'),
        efficiencies = {'O=C=O': 5.4, 'O': 6, '[H][H]': 3, '[He]': 1.2, '[O][O]': 1.1, '[C]=O': 2.7},
    ),
)

entry(
    index = 721,
    label = "CH3OCHO <=> CH3 + OCHO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.17e+24, 's^-1'), n=-2.401, Ea=(92600, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.71e+47, 'cm^3/(mol*s)'),
            n = -8.43,
            Ea = (98490, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 6.8932e-15,
        T3 = (4734.1, 'K'),
        T1 = (9.3302e+09, 'K'),
        T2 = (1.786e+09, 'K'),
        efficiencies = {'O=C=O': 5.4, 'O': 6, '[H][H]': 3, '[He]': 1.2, '[O][O]': 1.1, '[C]=O': 2.7},
    ),
)

entry(
    index = 722,
    label = "CH3OCHO <=> CH3O + HCO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.18e+16, 's^-1'), n=0, Ea=(97000, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.27e+63, 'cm^3/(mol*s)'),
            n = -12.32,
            Ea = (109180, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.89375,
        T3 = (7.4991e+09, 'K'),
        T1 = (647.04, 'K'),
        T2 = (6.698e+08, 'K'),
        efficiencies = {'O=C=O': 5.4, 'O': 6, '[H][H]': 3, '[He]': 1.2, '[O][O]': 1.1, '[C]=O': 2.7},
    ),
)

