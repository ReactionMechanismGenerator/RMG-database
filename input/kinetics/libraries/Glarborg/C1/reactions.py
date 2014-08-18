#!/usr/bin/env python
# encoding: utf-8

name = "Glarborg/C1"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "H + O2 <=> O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.6e+15, 'cm^3/(mol*s)'),
        n = -0.41,
        Ea = (16600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2,
    label = "H + H + H2 <=> H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+17, 'cm^6/(mol^2*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "H + H + H2O <=> H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+19, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "O + H2 <=> OH + H",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(3.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(7948, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.8e+14, 'cm^3/(mol*s)'), n=0, Ea=(19175, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 6,
    label = "OH + OH <=> O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4300, 'cm^3/(mol*s)'), n=2.7, Ea=(-1822, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "OH + H2 <=> H + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+08, 'cm^3/(mol*s)'),
        n = 1.52,
        Ea = (3449, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 8,
    label = "H2 + O2 <=> HO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (740000, 'cm^3/(mol*s)'),
        n = 2.433,
        Ea = (53502, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 9,
    label = "HO2 + H <=> OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 10,
    label = "HO2 + H <=> H2O + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 11,
    label = "HO2 + O <=> OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(-445, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 12,
    label = "HO2 + OH <=> H2O + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.89e+13, 'cm^3/(mol*s)', '*|/', 1.58),
        n = 0,
        Ea = (-497, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 13,
    label = "HO2 + HO2 <=> H2O2 + O2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.9e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1408, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(11034, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 15,
    label = "H2O2 + H <=> H2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(3580, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 16,
    label = "H2O2 + H <=> HO2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(3760, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 17,
    label = "H2O2 + O <=> HO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+06, 'cm^3/(mol*s)'), n=2, Ea=(3970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 18,
    label = "H2O2 + OH <=> H2O + HO2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(427, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.6e+18, 'cm^3/(mol*s)'), n=0, Ea=(29410, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 20,
    label = "CO + O2 <=> CO2 + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(60500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 21,
    label = "CO + HO2 <=> CO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (160000, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (17943, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 22,
    label = "HOCO + OH <=> CO2 + H2O",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(4.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(-89, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.5e+06, 'cm^3/(mol*s)'), n=2, Ea=(-89, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 24,
    label = "HOCO + OH <=> CO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 25,
    label = "HOCO + O2 <=> CO2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.9e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 26,
    label = "CH2O + H <=> HCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.47,
        Ea = (2444, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 27,
    label = "CH2O + O <=> HCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+11, 'cm^3/(mol*s)'),
        n = 0.57,
        Ea = (2760, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 28,
    label = "CH2O + O2 <=> HCO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(240000, 'cm^3/(mol*s)'), n=2.5, Ea=(36461, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 29,
    label = "CH2O + OH <=> HCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.8e+07, 'cm^3/(mol*s)'),
        n = 1.63,
        Ea = (-1055, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 30,
    label = "CH2O + HO2 <=> HCO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 31,
    label = "CH2O + CH3 <=> HCO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(32, 'cm^3/(mol*s)'), n=3.36, Ea=(4310, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 32,
    label = "HCO + H <=> CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 33,
    label = "HCO + O <=> CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 34,
    label = "HCO + O <=> CO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 35,
    label = "HCO + OH <=> CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 36,
    label = "HCO + O2 <=> CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 37,
    label = "HCO + HO2 <=> CO2 + OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 38,
    label = "HCO + HCO <=> CO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 39,
    label = "CH4 + H <=> CH3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4100, 'cm^3/(mol*s)'), n=3.156, Ea=(8755, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 40,
    label = "CH4 + O <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(440000, 'cm^3/(mol*s)'), n=2.5, Ea=(6577, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 41,
    label = "CH4 + OH <=> CH3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+06, 'cm^3/(mol*s)'), n=2.182, Ea=(2506, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 42,
    label = "CH4 + HO2 <=> CH3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(47000, 'cm^3/(mol*s)'), n=2.5, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 43,
    label = "CH4 + CH2 <=> CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(10030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 44,
    label = "CH4 + CH2(S) <=> CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 45,
    label = "CH3 + H <=> CH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(15100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 46,
    label = "CH2(S) + H2 <=> CH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 47,
    label = "CH3 + O <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 48,
    label = "CH3 + O <=> H2 + CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 49,
    label = "CH3 + OH <=> CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1100, 'cm^3/(mol*s)'), n=3, Ea=(2780, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 50,
    label = "CH2(S) + H2O <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+15, 'cm^3/(mol*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 51,
    label = "CH3 + HO2 <=> CH4 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000, 'cm^3/(mol*s)'),
        n = 2.228,
        Ea = (-3020, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 52,
    label = "CH3 + HO2 <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0.2688,
        Ea = (-687.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 53,
    label = "CH3 + O2 <=> CH3O + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(28297, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 54,
    label = "CH3 + O2 <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+11, 'cm^3/(mol*s)'), n=0, Ea=(9842, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 55,
    label = "CH3 + HCO <=> CH4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 56,
    label = "CH3 + CH3 <=> C2H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(16055, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 57,
    label = "CH2 + O <=> CO + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 58,
    label = "CH2 + O <=> CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 59,
    label = "CH2 + OH <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 60,
    label = "CH2 + O2 <=> CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+22, 'cm^3/(mol*s)'),
        n = -3.3,
        Ea = (2867, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 61,
    label = "CH2 + O2 <=> CO2 + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+21, 'cm^3/(mol*s)'),
        n = -3.3,
        Ea = (2867, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 62,
    label = "CH2 + O2 <=> CH2O + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+21, 'cm^3/(mol*s)'),
        n = -3.3,
        Ea = (2867, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 63,
    label = "CH2 + O2 <=> CO2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+21, 'cm^3/(mol*s)'),
        n = -3.3,
        Ea = (2867, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 64,
    label = "CH2 + O2 <=> CO + OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+21, 'cm^3/(mol*s)'),
        n = -3.3,
        Ea = (2867, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 65,
    label = "CH2 + CO2 <=> CO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 66,
    label = "CH2(S) + H <=> CH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 67,
    label = "CH2(S) + O <=> CO + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 68,
    label = "CH2(S) + OH <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 69,
    label = "CH2(S) + O2 <=> CO + OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 70,
    label = "CH2(S) + H2O <=> CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 71,
    label = "CH2(S) + CO2 <=> CH2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 72,
    label = "CH3OH + H <=> CH2OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+09, 'cm^3/(mol*s)'),
        n = 1.24,
        Ea = (4491, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 73,
    label = "CH3OH + H <=> CH3O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.1e+08, 'cm^3/(mol*s)'),
        n = 1.24,
        Ea = (4491, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 74,
    label = "CH3OH + O <=> CH2OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(5305, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 75,
    label = "CH3OH + O <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(5305, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 76,
    label = "CH3OH + OH <=> CH2OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+08, 'cm^3/(mol*s)'),
        n = 1.4434,
        Ea = (113, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 77,
    label = "CH3OH + OH <=> CH3O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+07, 'cm^3/(mol*s)'),
        n = 1.4434,
        Ea = (113, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 78,
    label = "CH3OH + HO2 <=> CH2OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 79,
    label = "CH3OH + O2 <=> CH2OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(46600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 80,
    label = "CH3OH + O2 <=> CH3O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(54800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 81,
    label = "CH2OH + H <=> CH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 82,
    label = "CH2OH + H <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 83,
    label = "CH2OH + O <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(-693, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 84,
    label = "CH2OH + OH <=> CH2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 85,
    label = "CH2OH + HO2 <=> CH2O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 86,
    label = "CH2OH + O2 <=> CH2O + HO2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(7.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(3736, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.9e+16, 'cm^3/(mol*s)'), n=-1.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 88,
    label = "CH2OH + HCO <=> CH3OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 89,
    label = "CH2OH + HCO <=> CH2O + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 90,
    label = "CH2OH + CH2O <=> CH3OH + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5500, 'cm^3/(mol*s)'), n=2.81, Ea=(5862, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 91,
    label = "CH2OH + CH2OH <=> CH3OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 92,
    label = "CH2OH + CH3O <=> CH3OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 93,
    label = "CH2OH + CH4 <=> CH3OH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(22, 'cm^3/(mol*s)'), n=3.1, Ea=(16227, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 94,
    label = "CH3O + H <=> CH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(745, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 95,
    label = "CH3O + H <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(745, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 96,
    label = "CH3O + O <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 97,
    label = "CH3O + OH <=> CH2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 98,
    label = "CH3O + HO2 <=> CH2O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 99,
    label = "CH3O + O2 <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+10, 'cm^3/(mol*s)'), n=0, Ea=(1749, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 100,
    label = "CH3O + CO <=> CH3 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.5e+25, 'cm^3/(mol*s)'),
        n = -4.93,
        Ea = (9080, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 101,
    label = "CH3O + CH3 <=> CH2O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 102,
    label = "CH3O + CH4 <=> CH3OH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+14, 'cm^3/(mol*s)'), n=0, Ea=(15073, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 103,
    label = "CH3O + CH2O <=> CH3OH + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(2981, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 104,
    label = "CH3O + CH3O <=> CH3OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 105,
    label = "CH3OOH + H <=> CH2O + OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.4e+10, 'cm^3/(mol*s)'), n=0, Ea=(1860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 106,
    label = "CH3OOH + H <=> CH3OO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.4e+10, 'cm^3/(mol*s)'), n=0, Ea=(1860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 107,
    label = "CH3OOH + H <=> CH3O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+10, 'cm^3/(mol*s)'), n=0, Ea=(1860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 108,
    label = "CH3OOH + O <=> CH2O + OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 109,
    label = "CH3OOH + O <=> CH3OO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 110,
    label = "CH3OOH + OH <=> CH3OO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-437, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 111,
    label = "CH3OOH + OH <=> CH2O + OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-258, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 112,
    label = "CH3OOH + HO2 <=> CH3OO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 113,
    label = "CH3OO + H <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 114,
    label = "CH3OO + O <=> CH3O + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(-445, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 115,
    label = "CH3OO + OH <=> CH3OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+15, 'cm^3/(mol*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 116,
    label = "CH3OO + OH <=> CH3O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+11, 'cm^3/(mol*s)'), n=0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 117,
    label = "CH3OO + HO2 <=> CH3OOH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 118,
    label = "CH3OO + CH3 <=> CH3O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1411, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 119,
    label = "CH3OO + CH4 <=> CH3OOH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(47000, 'cm^3/(mol*s)'), n=2.5, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 120,
    label = "CH3OO + HCO <=> CH3O + H + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 121,
    label = "CH3OO + CO <=> CH3O + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (160000, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (17940, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 122,
    label = "CH3OO + CH2O <=> CH3OOH + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 123,
    label = "CH3OO + CH3O <=> CH2O + CH3OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 124,
    label = "CH3OO + CH3OH <=> CH3OOH + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(19400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 125,
    label = "CH3OO + CH3OO <=> CH3O + CH3O + O2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.1e+18, 'cm^3/(mol*s)'),
                n = -2.4,
                Ea = (1800, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(7e+10, 'cm^3/(mol*s)'), n=0, Ea=(800, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 127,
    label = "CH3OO + CH3OO <=> CH3OH + CH2O + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11, 'cm^3/(mol*s)'),
        n = -0.55,
        Ea = (-1600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 128,
    label = "CH3OO + C2H5 <=> CH3O + CH3CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1410, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 129,
    label = "CH3OO + C2H6 <=> CH3OOH + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(19, 'cm^3/(mol*s)'), n=3.64, Ea=(17100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 130,
    label = "CH2O <=> HCO + H",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(8e+15, 's^-1'), n=0, Ea=(87726, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.734e+15, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (73479, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, 'N#N': 1, '[C]=O': 1.5},
    ),
)

entry(
    index = 131,
    label = "CH2O <=> CO + H2",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(3.7e+13, 's^-1'), n=0, Ea=(71969, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.661e+15, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (65849, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, 'N#N': 1, '[C]=O': 1.5},
    ),
)

entry(
    index = 132,
    label = "H + O2 <=> HO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.5e+16, 'cm^6/(mol^2*s)'),
            n = -0.41,
            Ea = (-1116, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'[H][H]': 2, '[O][O]': 0.78, 'O': 11, 'N#N': 0, '[Ar]': 0},
    ),
)

entry(
    index = 133,
    label = "H2O2 <=> OH + OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4e+11, 's^-1'), n=0, Ea=(37137, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.291e+16, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (43638, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'[H][H]': 2.5, 'O': 12, '[Ar]': 0.64},
    ),
)

entry(
    index = 134,
    label = "CO + O <=> CO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.8e+10, 'cm^3/(mol*s)'), n=0, Ea=(2384, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.35e+24, 'cm^6/(mol^2*s)'),
            n = -2.79,
            Ea = (4191, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'[H][H]': 2.5, '[C]=O': 1.9, 'O=C=O': 3.8, 'O': 12},
    ),
)

entry(
    index = 135,
    label = "CH3 + H <=> CH4",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.467e+23, 'cm^6/(mol^2*s)'),
            n = -1.8,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.6376,
        T3 = (1e-30, 'K'),
        T1 = (3230, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'CC': 4.8, 'C': 1.9},
    ),
)

entry(
    index = 136,
    label = "CH2 + H <=> CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.8e+16, 'cm^3/(mol*s)'), n=-0.8, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.8e+27, 'cm^6/(mol^2*s)'),
            n = -3.14,
            Ea = (1230, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.68,
        T3 = (78, 'K'),
        T1 = (1995, 'K'),
        T2 = (5590, 'K'),
        efficiencies = {'O': 6, 'N#N': 1, '[Ar]': 0.7},
    ),
)

entry(
    index = 137,
    label = "CH3 + CH3 <=> C2H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.269e+41, 'cm^6/(mol^2*s)'),
            n = -7,
            Ea = (2762, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.62,
        T3 = (73, 'K'),
        T1 = (1180, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, 'N#N': 1, '[C]=O': 1.5},
    ),
)

entry(
    index = 138,
    label = "CH3OH <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.1e+18, 's^-1'), n=-0.6148, Ea=(92540, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.6e+49, 'cm^3/(mol*s)'),
            n = -8.8,
            Ea = (101500, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7656,
        T3 = (1910, 'K'),
        T1 = (59.51, 'K'),
        T2 = (9374, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, 'N#N': 1, '[C]=O': 1.5},
    ),
)

entry(
    index = 139,
    label = "CH2OH <=> CH2O + H",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.8e+14, 's^-1'), n=-0.73, Ea=(32820, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.01e+33, 'cm^3/(mol*s)'),
            n = -5.39,
            Ea = (36200, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.96,
        T3 = (67.6, 'K'),
        T1 = (1855, 'K'),
        T2 = (7543, 'K'),
        efficiencies = {'[H][H]': 2, '[C]=O': 2, 'O=C=O': 3, 'O': 5},
    ),
)

entry(
    index = 140,
    label = "CH2OH + H <=> CH3OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.3e+15, 'cm^3/(mol*s)'), n=-0.79, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.844e+37, 'cm^6/(mol^2*s)'),
            n = -6.21,
            Ea = (1333, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.25,
        T3 = (210, 'K'),
        T1 = (1434, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, 'N#N': 1, '[C]=O': 1.5},
    ),
)

entry(
    index = 141,
    label = "CH3O <=> CH2O + H",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.8e+13, 's^-1'), n=0, Ea=(26154, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.867e+25, 'cm^3/(mol*s)'),
            n = -3,
            Ea = (24291, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (1000, 'K'),
        T1 = (2000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, 'N#N': 1, '[C]=O': 1.5},
    ),
)

entry(
    index = 142,
    label = "CH3O + H <=> CH3OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0.515, Ea=(50, 'cal/mol'), T0=(1, 'K')),
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
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, 'N#N': 1, '[C]=O': 1.5},
    ),
)

entry(
    index = 143,
    label = "H + H <=> H2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(7e+17, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[H][H]': 0, 'O': 0, 'N#N': 0},
    ),
)

entry(
    index = 144,
    label = "H + O <=> OH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(6.2e+16, 'cm^6/(mol^2*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'O': 5},
    ),
)

entry(
    index = 145,
    label = "O + O <=> O2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.9e+13, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (-1788, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[O][O]': 1.5, 'O': 10, 'N#N': 1.5},
    ),
)

entry(
    index = 146,
    label = "OH + H <=> H2O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.5e+22, 'cm^6/(mol^2*s)'), n=-2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[H][H]': 0.73, 'O': 12, '[Ar]': 0.38},
    ),
)

entry(
    index = 147,
    label = "CH2(S) <=> CH2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[H]': 0, 'O': 0, 'N#N': 0, '[Ar]': 0},
    ),
)

entry(
    index = 148,
    label = "CO + OH <=> CO2 + H",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 1, 3, 10, 20, 50, 80, 100, 650, 2000], 'atm'),
                arrhenius = [
                    Arrhenius(A=(9.3e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(8e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(7e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(3.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(12518, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(11922, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(13909, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(1987, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(1987, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.3e+11, 'cm^3/(mol*s)'), n=0.2, Ea=(4968, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (3.7e+07, 'cm^3/(mol*s)'),
                        n = 1.34,
                        Ea = (2186, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 1, 3, 10, 20, 50, 80, 100, 650, 2000], 'atm'),
                arrhenius = [
                    Arrhenius(A=(710000, 'cm^3/(mol*s)'), n=1.8, Ea=(1133, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(880000, 'cm^3/(mol*s)'), n=1.77, Ea=(954, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(290000, 'cm^3/(mol*s)'), n=1.9, Ea=(397, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(9.3e+07, 'cm^3/(mol*s)'), n=1.1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.5e+07, 'cm^3/(mol*s)'), n=1.2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5.8e+06, 'cm^3/(mol*s)'), n=1.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(250000, 'cm^3/(mol*s)'), n=1.9, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(190000, 'cm^3/(mol*s)'), n=1.94, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(700000, 'cm^3/(mol*s)'), n=1.7, Ea=(298, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 150,
    label = "CO + OH <=> HOCO",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 1, 3, 10, 20, 50, 80, 100, 650, 2000], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1e+25, 'cm^3/(mol*s)'), n=-6, Ea=(2981, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(6e+26, 'cm^3/(mol*s)'), n=-5.6, Ea=(2881, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (2.2e+27, 'cm^3/(mol*s)'),
                        n = -5.6,
                        Ea = (3239, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(1.5e+25, 'cm^3/(mol*s)'), n=-5, Ea=(1987, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (4.2e+26, 'cm^3/(mol*s)'),
                        n = -5.7,
                        Ea = (1927, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.9e+25, 'cm^3/(mol*s)'),
                        n = -5.2,
                        Ea = (1987, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.2e+25, 'cm^3/(mol*s)'),
                        n = -5.2,
                        Ea = (1987, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(1.1e+28, 'cm^3/(mol*s)'), n=-6, Ea=(2384, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(3.2e+41, 'cm^3/(mol*s)'), n=-10, Ea=(6955, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5.5e+44, 'cm^3/(mol*s)'), n=-11, Ea=(7948, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 1, 3, 10, 20, 50, 80, 100, 650, 2000], 'atm'),
                arrhenius = [
                    Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (1.3e+37, 'cm^3/(mol*s)'),
                        n = -8.4,
                        Ea = (7948, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(7.5e+28, 'cm^3/(mol*s)'), n=-6, Ea=(3775, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4e+38, 'cm^3/(mol*s)'), n=-9, Ea=(6955, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(7.7e+35, 'cm^3/(mol*s)'), n=-8, Ea=(6557, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.8e+36, 'cm^3/(mol*s)'), n=-8, Ea=(7153, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (2.9e+66, 'cm^3/(mol*s)'),
                        n = -17.1,
                        Ea = (19870, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.7e+67, 'cm^3/(mol*s)'),
                        n = -17,
                        Ea = (22851, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 1, 3, 10, 20, 50, 80, 100, 650, 2000], 'atm'),
                arrhenius = [
                    Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4e+39, 'cm^3/(mol*s)'), n=-9, Ea=(9935, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5e+43, 'cm^3/(mol*s)'), n=-10, Ea=(13015, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (9e+47, 'cm^3/(mol*s)'),
                        n = -11.2,
                        Ea = (15499, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(2e+54, 'cm^3/(mol*s)'), n=-13, Ea=(19671, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (2e+63, 'cm^3/(mol*s)'),
                        n = -15.2,
                        Ea = (27421, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(1e+74, 'cm^3/(mol*s)'), n=-18, Ea=(37157, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 153,
    label = "HOCO <=> CO2 + H",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([1, 10, 20, 50, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(3.5e+56, 's^-1'), n=-15, Ea=(46500, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(3.2e+57, 's^-1'), n=-15, Ea=(46500, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(6e+57, 's^-1'), n=-15, Ea=(46500, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.4e+58, 's^-1'), n=-15, Ea=(46500, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.8e+58, 's^-1'), n=-15, Ea=(46500, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            PDepArrhenius(
                pressures = ([1, 10, 20, 50, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(2.5e+69, 's^-1'), n=-18, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.2e+70, 's^-1'), n=-18, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.3e+70, 's^-1'), n=-18, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1e+71, 's^-1'), n=-18, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2e+71, 's^-1'), n=-18, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 155,
    label = "HCO <=> H + CO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 20, 50, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(9.9e+11, 's^-1'), n=-0.865, Ea=(16755, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.2e+12, 's^-1'), n=-0.865, Ea=(16755, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.3e+13, 's^-1'), n=-0.865, Ea=(16755, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.9e+13, 's^-1'), n=-0.865, Ea=(16755, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.3e+13, 's^-1'), n=-0.865, Ea=(16755, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 156,
    label = "CH3 + O2 <=> CH3OO",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([1, 10, 20, 50, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(5e+22, 'cm^3/(mol*s)'), n=-3.85, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (3.4e+21, 'cm^3/(mol*s)'),
                        n = -3.2,
                        Ea = (2300, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.1e+20, 'cm^3/(mol*s)'),
                        n = -2.94,
                        Ea = (1900, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.8e+18, 'cm^3/(mol*s)'),
                        n = -2.2,
                        Ea = (1400, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.1e+19, 'cm^3/(mol*s)'),
                        n = -2.3,
                        Ea = (1800, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([1, 10, 20, 50, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (3.3e+29, 'cm^3/(mol*s)'),
                        n = -5.6,
                        Ea = (6850, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.6e+28, 'cm^3/(mol*s)'),
                        n = -5.25,
                        Ea = (6850, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.1e+30, 'cm^3/(mol*s)'),
                        n = -5.7,
                        Ea = (8750, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 158,
    label = "CH3OOH <=> CH3O + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 50, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(2e+35, 's^-1'), n=-6.7, Ea=(47450, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.1e+28, 's^-1'), n=-4.15, Ea=(46190, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.8e+26, 's^-1'), n=-3.5, Ea=(46340, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.2e+17, 's^-1'), n=-0.42, Ea=(44622, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

