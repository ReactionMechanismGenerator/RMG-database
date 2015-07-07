#!/usr/bin/env python
# encoding: utf-8

name = "Dooley/methylformate_2"
shortDesc = u""
longDesc = u"""
mechanism used in
S. Dooley, M. P. Burke, M. Chaos, Y. Stein, F. L. Dryer, V. P. Zhukov, O. Finch, J. M. Simmie, H. J. Curran, Int. J. Chem. Kinet. 42 (9) (2010) 527-549.
"""
entry(
    index = 1,
    label = "H + CH2OCHO <=> CH3OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "H + CH3OCO <=> CH3OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "CH3OCHO + H <=> CH2OCHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(665000, 'cm^3/(mol*s)'), n=2.5, Ea=(6494, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "CH3OCHO + OH <=> CH2OCHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.86e+12, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (3340, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 5,
    label = "CH3OCHO + CH3 <=> CH2OCHO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.291, 'cm^3/(mol*s)'), n=3.7, Ea=(6823, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "CH3OCHO + HO2 <=> CH2OCHO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(56600, 'cm^3/(mol*s)'), n=2.4, Ea=(16594, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "CH3OCHO + CH3O2 <=> CH2OCHO + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(56600, 'cm^3/(mol*s)'), n=2.4, Ea=(16594, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 8,
    label = "CH3OCHO + CH3O <=> CH2OCHO + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.59e+09, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (4823, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 9,
    label = "CH3OCHO + O <=> CH2OCHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(884000, 'cm^3/(mol*s)'), n=2.4, Ea=(4593, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 10,
    label = "CH3OCHO + O2 <=> CH2OCHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.53e+13, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (51749, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 11,
    label = "CH3OCHO + HCO <=> CH2OCHO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(102000, 'cm^3/(mol*s)'), n=2.5, Ea=(18430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 12,
    label = "CH3OCHO + OCHO <=> CH2OCHO + HCOOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(56600, 'cm^3/(mol*s)'), n=2.4, Ea=(16594, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "CH3OCHO + C2H5 <=> CH2OCHO + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 14,
    label = "CH3OCHO + C2H3 <=> CH2OCHO + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 15,
    label = "CH3OCHO + H <=> CH3OCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(258000, 'cm^3/(mol*s)'), n=2.5, Ea=(5736, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 16,
    label = "CH3OCHO + OH <=> CH3OCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.22e+16, 'cm^3/(mol*s)'), n=-1, Ea=(4946, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 17,
    label = "CH3OCHO + CH3 <=> CH3OCO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0921, 'cm^3/(mol*s)'), n=3.7, Ea=(6052, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 18,
    label = "CH3OCHO + HO2 <=> CH3OCO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(157000, 'cm^3/(mol*s)'), n=2.2, Ea=(16544, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 19,
    label = "CH3OCHO + CH3O2 <=> CH3OCO + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(157000, 'cm^3/(mol*s)'), n=2.2, Ea=(16544, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 20,
    label = "CH3OCHO + CH3O <=> CH3OCO + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.27e+09, 'cm^3/(mol*s)'),
        n = 0.8,
        Ea = (2912, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 21,
    label = "CH3OCHO + O <=> CH3OCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(245000, 'cm^3/(mol*s)'), n=2.5, Ea=(4047, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 22,
    label = "CH3OCHO + O2 <=> CH3OCO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.85e+12, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (50759, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 23,
    label = "CH3OCHO + OCHO <=> CH3OCO + HCOOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(157000, 'cm^3/(mol*s)'), n=2.2, Ea=(16544, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 24,
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
    index = 25,
    label = "CH3OCHO + C2H5 <=> CH3OCO + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 26,
    label = "CH3OCHO + C2H3 <=> CH3OCO + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 27,
    label = "CH3 + CO2 <=> CH3OCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.76e+07, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (34700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 28,
    label = "CH3O + CO <=> CH3OCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.55e+06, 'cm^3/(mol*s)'), n=2, Ea=(5730, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 29,
    label = "CH2OCHO <=> CH3OCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.62e+11, 's^-1'), n=0, Ea=(38178, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 30,
    label = "CH2O + HCO <=> CH2OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.89e+11, 'cm^3/(mol*s)'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 31,
    label = "CH3OCO + CH3OCHO <=> CH3OCHO + CH2OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 32,
    label = "CH3 + CH2OCHO <=> CH3CH2OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 33,
    label = "CH3 + CH3OCO <=> CH3CO2CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 34,
    label = "CH2OCHO + HO2 <=> HO2CH2OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 35,
    label = "CH3OCO + HO2 <=> CH3OCOO2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 36,
    label = "OCH2OCHO + OH <=> HO2CH2OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.55e+06, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (-4132, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 37,
    label = "CH3OCOO + OH <=> CH3OCOO2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.55e+06, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (-4132, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 38,
    label = "CO2 + CH3O <=> CH3OCOO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(9200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 39,
    label = "CH2O + OCHO <=> OCH2OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.89e+11, 'cm^3/(mol*s)'), n=0, Ea=(2500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 40,
    label = "CH3OCO + O2 <=> CH3OCOOO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 41,
    label = "CH2OCHO + O2 <=> OOCH2OCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 42,
    label = "OOCH2OCHO <=> HOOCH2OCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.47e+11, 's^-1'), n=0, Ea=(28900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 43,
    label = "CH3OCOOO <=> CH2OCOOOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.41e+11, 's^-1'), n=0, Ea=(28900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 44,
    label = "CH2O2H + CO2 <=> HOOCH2OCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+06, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (36591, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 45,
    label = "OCH2O2H + CO <=> HOOCH2OCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+07, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (5588, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 46,
    label = "OH + CH2O <=> CH2O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+10, 'cm^3/(mol*s)'), n=0, Ea=(12900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 47,
    label = "OCH2O2H <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.27e+18, 's^-1'), n=-1.8, Ea=(10460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 48,
    label = "CH2OCOOOH <=> CH2O + CO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+18, 's^-1'), n=-1.5, Ea=(37360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 49,
    label = "CH2OCOOOH <=> CH2O + CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+18, 's^-1'), n=-1.5, Ea=(37360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 50,
    label = "CH2OCOOOH <=> cyOCH2OCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 51,
    label = "HOOCH2OCO <=> cyOCH2OCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 52,
    label = "CH2OCOOOH + O2 <=> OOCH2OCOOOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 53,
    label = "HOOCH2OCO + O2 <=> HOOCH2OCOOO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 54,
    label = "OOCH2OCOOOH <=> OCHOCOOOH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.89e+10, 's^-1'), n=0, Ea=(21863, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 55,
    label = "HOOCH2OCOOO <=> OCHOCOOOH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.48e+11, 's^-1'), n=0, Ea=(20900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 56,
    label = "OCHOCOOOH <=> CO2 + OCHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(41600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 57,
    label = "cyOCH2OCO + H <=> CHOOCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(2005, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 58,
    label = "cyOCH2OCO + OH <=> CHOOCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 59,
    label = "cyOCH2OCO + HO2 <=> CHOOCO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(12976, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 60,
    label = "OCHO + CO <=> CHOOCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+07, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (5588, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 61,
    label = "HCO + CO2 <=> CHOOCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+06, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (36591, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 62,
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
        alpha = 0.239,
        T3 = (555.1, 'K'),
        T1 = (8.43e+09, 'K'),
        T2 = (8.21e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 63,
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
        alpha = 0.179,
        T3 = (357.5, 'K'),
        T1 = (9.918e+09, 'K'),
        T2 = (3.28e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 64,
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
        alpha = 0.781,
        T3 = (6.49e+09, 'K'),
        T1 = (618, 'K'),
        T2 = (6.71e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 65,
    label = "CH3OCHO <=> CH3 + OCHO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.17e+24, 's^-1'), n=-2.4, Ea=(92600, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.71e+47, 'cm^3/(mol*s)'),
            n = -8.43,
            Ea = (98490, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 6.89e-15,
        T3 = (4730, 'K'),
        T1 = (9.33e+09, 'K'),
        T2 = (1.78e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 66,
    label = "CH3OCHO <=> CH3O + HCO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.18e+16, 's^-1'), n=0, Ea=(97400, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.27e+63, 'cm^3/(mol*s)'),
            n = -12.3,
            Ea = (109180, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.894,
        T3 = (7.49e+09, 'K'),
        T1 = (647, 'K'),
        T2 = (6.69e+08, 'K'),
        efficiencies = {},
    ),
)

