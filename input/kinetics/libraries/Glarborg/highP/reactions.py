#!/usr/bin/env python
# encoding: utf-8

name = "Glarborg/highP"
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
    label = "CO + OH <=> HOCO",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(5.5e+44, 'cm^3/(mol*s)'), n=-11, Ea=(7948, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (2.7e+67, 'cm^3/(mol*s)'),
                n = -17,
                Ea = (22851, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(1e+74, 'cm^3/(mol*s)'), n=-18, Ea=(37157, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 25,
    label = "HOCO <=> CO2 + H",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(2.8e+58, 's^-1'), n=-15, Ea=(46500, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2e+71, 's^-1'), n=-18, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 27,
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
    index = 29,
    label = "HOCO + OH <=> CO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 30,
    label = "HOCO + O2 <=> CO2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.9e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 31,
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
    index = 32,
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
    index = 33,
    label = "CH2O + O2 <=> HCO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(240000, 'cm^3/(mol*s)'), n=2.5, Ea=(36461, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 34,
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
    index = 35,
    label = "CH2O + HO2 <=> HCO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 36,
    label = "CH2O + CH3 <=> HCO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(32, 'cm^3/(mol*s)'), n=3.36, Ea=(4310, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 37,
    label = "HCO <=> H + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+13, 's^-1'), n=-0.865, Ea=(16755, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 38,
    label = "HCO + H <=> CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 39,
    label = "HCO + O <=> CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 40,
    label = "HCO + O <=> CO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 41,
    label = "HCO + OH <=> CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 42,
    label = "HCO + O2 <=> CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 43,
    label = "HCO + HO2 <=> CO2 + OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 44,
    label = "HCO + HCO <=> CO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 45,
    label = "CH4 + H <=> CH3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4100, 'cm^3/(mol*s)'), n=3.156, Ea=(8755, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 46,
    label = "CH4 + O <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(440000, 'cm^3/(mol*s)'), n=2.5, Ea=(6577, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 47,
    label = "CH4 + OH <=> CH3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+06, 'cm^3/(mol*s)'), n=2.182, Ea=(2506, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 48,
    label = "CH4 + HO2 <=> CH3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(47000, 'cm^3/(mol*s)'), n=2.5, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 49,
    label = "CH4 + CH2 <=> CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(10030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 50,
    label = "CH4 + CH2(S) <=> CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 51,
    label = "CH3 + H <=> CH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(15100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 52,
    label = "CH2(S) + H2 <=> CH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 53,
    label = "CH3 + O <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 54,
    label = "CH3 + O <=> H2 + CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 55,
    label = "CH3 + OH <=> CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1100, 'cm^3/(mol*s)'), n=3, Ea=(2780, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 56,
    label = "CH2(S) + H2O <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+15, 'cm^3/(mol*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 57,
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
    index = 58,
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
    index = 59,
    label = "CH3 + O2 <=> CH3O + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(28297, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 60,
    label = "CH3 + O2 <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+11, 'cm^3/(mol*s)'), n=0, Ea=(9842, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 61,
    label = "CH3 + O2 <=> CH3OO",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.1e+19, 'cm^3/(mol*s)'),
                n = -2.3,
                Ea = (1800, 'cal/mol'),
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
)

entry(
    index = 63,
    label = "CH3 + HCO <=> CH4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 64,
    label = "CH3 + CH3 <=> C2H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(16055, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 65,
    label = "CH2 + O <=> CO + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 66,
    label = "CH2 + O <=> CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 67,
    label = "CH2 + OH <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 68,
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
    index = 69,
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
    index = 70,
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
    index = 71,
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
    index = 72,
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
    index = 73,
    label = "CH2 + CO2 <=> CO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 74,
    label = "CH2(S) + H <=> CH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 75,
    label = "CH2(S) + O <=> CO + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 76,
    label = "CH2(S) + OH <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 77,
    label = "CH2(S) + O2 <=> CO + OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 78,
    label = "CH2(S) + H2O <=> CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 79,
    label = "CH2(S) + CO2 <=> CH2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 80,
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
    index = 81,
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
    index = 82,
    label = "CH3OH + O <=> CH2OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(5305, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 83,
    label = "CH3OH + O <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(5305, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 84,
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
    index = 85,
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
    index = 86,
    label = "CH3OH + HO2 <=> CH2OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 87,
    label = "CH3OH + O2 <=> CH2OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(46600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 88,
    label = "CH3OH + O2 <=> CH3O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(54800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 89,
    label = "CH2OH + H <=> CH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 90,
    label = "CH2OH + H <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 91,
    label = "CH2OH + O <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(-693, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 92,
    label = "CH2OH + OH <=> CH2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 93,
    label = "CH2OH + HO2 <=> CH2O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 94,
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
    index = 96,
    label = "CH2OH + HCO <=> CH3OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 97,
    label = "CH2OH + HCO <=> CH2O + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 98,
    label = "CH2OH + CH2O <=> CH3OH + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5500, 'cm^3/(mol*s)'), n=2.81, Ea=(5862, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 99,
    label = "CH2OH + CH2OH <=> CH3OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 100,
    label = "CH2OH + CH3O <=> CH3OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 101,
    label = "CH2OH + CH4 <=> CH3OH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(22, 'cm^3/(mol*s)'), n=3.1, Ea=(16227, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 102,
    label = "CH3O + H <=> CH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(745, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 103,
    label = "CH3O + H <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(745, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 104,
    label = "CH3O + O <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 105,
    label = "CH3O + OH <=> CH2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 106,
    label = "CH3O + HO2 <=> CH2O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 107,
    label = "CH3O + O2 <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+10, 'cm^3/(mol*s)'), n=0, Ea=(1749, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 108,
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
    index = 109,
    label = "CH3O + CH3 <=> CH2O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 110,
    label = "CH3O + CH4 <=> CH3OH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+14, 'cm^3/(mol*s)'), n=0, Ea=(15073, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 111,
    label = "CH3O + CH2O <=> CH3OH + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(2981, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 112,
    label = "CH3O + CH3O <=> CH3OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 113,
    label = "CH3OOH <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+17, 's^-1'), n=-0.42, Ea=(44622, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 114,
    label = "CH3OOH + H <=> CH2O + OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.4e+10, 'cm^3/(mol*s)'), n=0, Ea=(1860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 115,
    label = "CH3OOH + H <=> CH3OO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.4e+10, 'cm^3/(mol*s)'), n=0, Ea=(1860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 116,
    label = "CH3OOH + H <=> CH3O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+10, 'cm^3/(mol*s)'), n=0, Ea=(1860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 117,
    label = "CH3OOH + O <=> CH2O + OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 118,
    label = "CH3OOH + O <=> CH3OO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 119,
    label = "CH3OOH + OH <=> CH3OO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-437, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 120,
    label = "CH3OOH + OH <=> CH2O + OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-258, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 121,
    label = "CH3OOH + HO2 <=> CH3OO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 122,
    label = "CH3OO + H <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 123,
    label = "CH3OO + O <=> CH3O + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(-445, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 124,
    label = "CH3OO + OH <=> CH3OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+15, 'cm^3/(mol*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 125,
    label = "CH3OO + OH <=> CH3O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+11, 'cm^3/(mol*s)'), n=0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 126,
    label = "CH3OO + HO2 <=> CH3OOH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 127,
    label = "CH3OO + CH3 <=> CH3O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1411, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 128,
    label = "CH3OO + CH4 <=> CH3OOH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(47000, 'cm^3/(mol*s)'), n=2.5, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 129,
    label = "CH3OO + HCO <=> CH3O + H + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 130,
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
    index = 131,
    label = "CH3OO + CH2O <=> CH3OOH + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 132,
    label = "CH3OO + CH3O <=> CH2O + CH3OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 133,
    label = "CH3OO + CH3OH <=> CH3OOH + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(19400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 134,
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
    index = 136,
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
    index = 137,
    label = "CH3OO + C2H5 <=> CH3O + CH3CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1410, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 138,
    label = "CH3OO + C2H6 <=> CH3OOH + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(19, 'cm^3/(mol*s)'), n=3.64, Ea=(17100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 139,
    label = "C2H6 + H <=> C2H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(9220, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 140,
    label = "C2H6 + O <=> C2H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e-07, 'cm^3/(mol*s)'), n=6.5, Ea=(274, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 141,
    label = "C2H6 + OH <=> C2H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(990, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 142,
    label = "C2H6 + HO2 <=> C2H5 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(110000, 'cm^3/(mol*s)'), n=2.5, Ea=(16850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 143,
    label = "C2H6 + O2 <=> C2H5 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(730000, 'cm^3/(mol*s)'), n=2.5, Ea=(49160, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 144,
    label = "C2H6 + CH3 <=> C2H5 + CH4",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(5.6e+10, 'cm^3/(mol*s)'), n=0, Ea=(9418, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.4e+14, 'cm^3/(mol*s)'), n=0, Ea=(22250, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 146,
    label = "C2H6 + CH2(S) <=> C2H5 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 147,
    label = "C2H5 + O <=> CH3 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 148,
    label = "C2H5 + O <=> CH3CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 149,
    label = "C2H5 + O <=> C2H4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 150,
    label = "C2H5 + OH <=> C2H4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 151,
    label = "C2H5 + HO2 <=> CH3CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 152,
    label = "C2H5 + O2 <=> C2H4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+07, 'cm^3/(mol*s)'),
        n = 1.09,
        Ea = (-1975, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 153,
    label = "C2H5 + CH2O <=> C2H6 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5500, 'cm^3/(mol*s)'), n=2.81, Ea=(5860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 154,
    label = "C2H5 + HCO <=> C2H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 155,
    label = "C2H5 + CH3 <=> C2H4 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 156,
    label = "C2H5 + C2H5 <=> C2H6 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 157,
    label = "C2H4 + H <=> C2H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(240, 'cm^3/(mol*s)'), n=3.62, Ea=(11266, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 158,
    label = "CH3 + CH2 <=> C2H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 159,
    label = "CH3 + CH2(S) <=> C2H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 160,
    label = "C2H4 + O <=> CH3 + HCO",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(3.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(1494, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(6855, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 162,
    label = "C2H4 + O <=> CH2CHO + H",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(1494, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(6855, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 164,
    label = "C2H4 + OH <=> C2H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.4e+07, 'cm^3/(mol*s)'), n=1.8, Ea=(4166, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 165,
    label = "C2H4 + OH <=> CH3 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+13, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (11455, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 166,
    label = "C2H4 + OH <=> CH3CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.8e+09, 'cm^3/(mol*s)'),
        n = 0.81,
        Ea = (13867, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 167,
    label = "C2H4 + OH <=> CH2CHOH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.5e+10, 'cm^3/(mol*s)'),
        n = 0.75,
        Ea = (11491, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 168,
    label = "C2H4 + OH <=> CH2CH2OH",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (6e+37, 'cm^3/(mol*s)'),
                n = -7.44,
                Ea = (14269, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.8e+19, 'cm^3/(mol*s)'),
                n = -2.41,
                Ea = (1011, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 170,
    label = "C2H4 + HO2 <=> cC2H4O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 171,
    label = "C2H4 + O2 <=> C2H3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(60010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 172,
    label = "C2H4 + CH3 <=> C2H3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+07, 'cm^3/(mol*s)'), n=1.56, Ea=(16630, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 173,
    label = "C2H3 + H <=> C2H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 174,
    label = "C2H3 + O <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 175,
    label = "C2H3 + OH <=> C2H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 176,
    label = "C2H3 + HO2 <=> CH2CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 177,
    label = "C2H3 + O2 <=> CH2CHOO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+36, 'cm^3/(mol*s)'), n=-8, Ea=(5680, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 178,
    label = "C2H3 + O2 <=> CH2O + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(3130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 179,
    label = "C2H3 + O2 <=> CH2CHO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(4800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 180,
    label = "C2H3 + O2 <=> C2H2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.6e+11, 'cm^3/(mol*s)'), n=0, Ea=(7930, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 181,
    label = "C2H3 + O2 <=> CH3O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(3130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 182,
    label = "C2H3 + O2 <=> CH3 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+10, 'cm^3/(mol*s)'), n=0, Ea=(3130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 183,
    label = "C2H3 + CH2O <=> C2H4 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5400, 'cm^3/(mol*s)'), n=2.81, Ea=(5860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 184,
    label = "C2H3 + HCO <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 185,
    label = "C2H3 + CH3 <=> C2H2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 186,
    label = "C2H3 + C2H3 <=> C2H4 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 187,
    label = "C2H3 + C2H <=> C2H2 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 188,
    label = "CH2 + CH2 <=> C2H2 + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 189,
    label = "C2H2 + O <=> HCCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+07, 'cm^3/(mol*s)'), n=2, Ea=(1900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 190,
    label = "C2H2 + O <=> CH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.1e+06, 'cm^3/(mol*s)'), n=2, Ea=(1900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 191,
    label = "C2H2 + O <=> C2H + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+15, 'cm^3/(mol*s)'),
        n = -0.6,
        Ea = (15000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 192,
    label = "C2H2 + OH <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(830000, 'cm^3/(mol*s)'), n=1.77, Ea=(4697, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 193,
    label = "C2H2 + OH <=> HCCOH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.3e+06, 'cm^3/(mol*s)'),
        n = 1.89,
        Ea = (13603, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 194,
    label = "C2H2 + OH <=> CHCHOH",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.1e+08, 'cm^3/(mol*s)'), n=1.34, Ea=(332, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6e+07, 'cm^3/(mol*s)'), n=1.62, Ea=(240, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 196,
    label = "C2H2 + OH <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(15000, 'cm^3/(mol*s)'), n=2.45, Ea=(4477, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 197,
    label = "C2H2 + HO2 <=> CH2O + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 198,
    label = "C2H2 + HO2 <=> CH2CHO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 199,
    label = "C2H2 + O2 <=> HCO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+07, 'cm^3/(mol*s)'), n=1.8, Ea=(30600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 200,
    label = "C2H2 + CH2(S) <=> C2H2 + CH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 201,
    label = "H2CC <=> C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+07, 's^-1'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 202,
    label = "H2CC + H <=> C2H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 203,
    label = "H2CC + OH <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 204,
    label = "H2CC + O2 <=> CH2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 205,
    label = "C2 + H2 <=> C2H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(400000, 'cm^3/(mol*s)'), n=2.4, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 206,
    label = "C2H + OH <=> HCCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 207,
    label = "C2H + OH <=> C2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+07, 'cm^3/(mol*s)'), n=2, Ea=(8000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 208,
    label = "C2H + H2 <=> C2H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(410000, 'cm^3/(mol*s)'), n=2.39, Ea=(864, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 209,
    label = "C2H + O2 <=> CO + CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.7e+13, 'cm^3/(mol*s)'), n=-0.16, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 210,
    label = "C2H + CH4 <=> CH3 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(976, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 211,
    label = "C2 + OH <=> C2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 212,
    label = "C2 + O2 <=> CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(980, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 213,
    label = "CH3CH2OH + H <=> CH3CHOH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+07, 'cm^3/(mol*s)'),
        n = 1.65,
        Ea = (2827, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 214,
    label = "CH3CH2OH + H <=> CH2CH2OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+07, 'cm^3/(mol*s)'), n=1.8, Ea=(5098, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 215,
    label = "CH3CH2OH + H <=> CH3CH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+07, 'cm^3/(mol*s)'),
        n = 1.65,
        Ea = (3038, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 216,
    label = "CH3CH2OH + O <=> CH3CHOH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.9e+07, 'cm^3/(mol*s)'),
        n = 1.85,
        Ea = (1824, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 217,
    label = "CH3CH2OH + O <=> CH2CH2OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.4e+07, 'cm^3/(mol*s)'), n=1.7, Ea=(5459, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 218,
    label = "CH3CH2OH + O <=> CH3CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+07, 'cm^3/(mol*s)'), n=2, Ea=(4448, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 219,
    label = "CH3CH2OH + OH <=> CH3CHOH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.6e+11, 'cm^3/(mol*s)'), n=0.15, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 220,
    label = "CH3CH2OH + OH <=> CH2CH2OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+11, 'cm^3/(mol*s)'), n=0.27, Ea=(600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 221,
    label = "CH3CH2OH + OH <=> CH3CH2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+11, 'cm^3/(mol*s)'), n=0.3, Ea=(1634, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 222,
    label = "CH3CH2OH + HO2 <=> CH3CHOH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8200, 'cm^3/(mol*s)'), n=2.55, Ea=(10750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 223,
    label = "CH3CH2OH + HO2 <=> CH2CH2OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(12000, 'cm^3/(mol*s)'), n=2.55, Ea=(15750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 224,
    label = "CH3CH2OH + HO2 <=> CH3CH2O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(24000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 225,
    label = "CH3CH2OH + CH3 <=> CH3CHOH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(730, 'cm^3/(mol*s)'), n=2.99, Ea=(7948, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 226,
    label = "CH3CH2OH + CH3 <=> CH2CH2OH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(220, 'cm^3/(mol*s)'), n=3.18, Ea=(9622, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 227,
    label = "CH3CH2OH + CH3 <=> CH3CH2O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(150, 'cm^3/(mol*s)'), n=2.99, Ea=(7649, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 228,
    label = "CH3CHOH + O <=> CH3CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 229,
    label = "CH3CHOH + H <=> CH2OH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 230,
    label = "CH3CHOH + H <=> C2H4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 231,
    label = "CH3CHOH + OH <=> CH3CHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 232,
    label = "CH3CHOH + HO2 <=> CH3CHO + OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 233,
    label = "CH3CHOH + O2 <=> CH3CHO + HO2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(8.4e+15, 'cm^3/(mol*s)'), n=-1.2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.8e+14, 'cm^3/(mol*s)'), n=0, Ea=(5017, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 235,
    label = "CH2CH2OH <=> CH2CHOH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(220000, 's^-1'), n=2.84, Ea=(32920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 236,
    label = "CH3CH2O <=> CH2CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e-29, 's^-1'), n=11.9, Ea=(4450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 237,
    label = "CH2CH2OH + H <=> CH3 + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 238,
    label = "CH2CH2OH + O <=> CH2O + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 239,
    label = "CH2CH2OH + OH <=> CH2CHOH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 240,
    label = "CH2CH2OH + HO2 <=> CH3CH2OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 241,
    label = "CH2CH2OH + HO2 => CH2OH + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 242,
    label = "CH2CH2OH + O2 <=> CH2CHOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+07, 'cm^3/(mol*s)'),
        n = 1.09,
        Ea = (-1975, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 243,
    label = "CH3CH2O <=> CH3CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+13, 's^-1'), n=0, Ea=(20060, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 244,
    label = "CH3CH2O + H <=> CH3CHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 245,
    label = "CH3CH2O + OH <=> CH3CHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 246,
    label = "CH3CH2O + O2 <=> CH3CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(645, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 247,
    label = "CH3CH2O + CO <=> C2H5 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.5e+25, 'cm^3/(mol*s)'),
        n = -4.93,
        Ea = (9080, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 248,
    label = "CH3CHO + H <=> CH3CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.7e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (3000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 249,
    label = "CH3CHO + H <=> CH2CHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+12, 'cm^3/(mol*s)'), n=0.4, Ea=(5359, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 250,
    label = "CH3CHO + O <=> CH3CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+18, 'cm^3/(mol*s)'),
        n = -1.9,
        Ea = (2975, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 251,
    label = "CH3CHO + O <=> CH2CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+13, 'cm^3/(mol*s)'),
        n = -0.2,
        Ea = (3556, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 252,
    label = "CH3CHO + OH <=> CH3CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+11, 'cm^3/(mol*s)'),
        n = 0.3,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 253,
    label = "CH3CHO + OH <=> CH2CHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=-0.6, Ea=(800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 254,
    label = "CH3CHO + HO2 <=> CH3CO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+19, 'cm^3/(mol*s)'),
        n = -2.2,
        Ea = (14030, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 255,
    label = "CH3CHO + HO2 <=> CH2CHO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+11, 'cm^3/(mol*s)'),
        n = 0.4,
        Ea = (14864, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 256,
    label = "CH3CHO + O2 <=> CH3CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(120000, 'cm^3/(mol*s)'), n=2.5, Ea=(37554, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 257,
    label = "CH3CHO + CH3 <=> CH3CO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.9e-07, 'cm^3/(mol*s)'), n=5.8, Ea=(2200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 258,
    label = "CH3CHO + CH3 <=> CH2CHO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(25, 'cm^3/(mol*s)'), n=3.15, Ea=(5727, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 259,
    label = "cC2H4O <=> CH2CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 's^-1'), n=0.2, Ea=(71780, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 260,
    label = "cC2H4O <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+13, 's^-1'), n=0.4, Ea=(61880, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 261,
    label = "cC2H4O <=> CH3CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 's^-1'), n=0.25, Ea=(65310, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 262,
    label = "cC2H4O <=> CH2CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+12, 's^-1'), n=-0.2, Ea=(63030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 263,
    label = "cC2H4O <=> CH3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 's^-1'), n=-0.75, Ea=(46424, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 264,
    label = "cC2H4O <=> C2H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.6e+12, 's^-1'), n=0.06, Ea=(69530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 265,
    label = "cC2H4O + H <=> cC2H3O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(8310, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 266,
    label = "cC2H4O + H <=> C2H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+09, 'cm^3/(mol*s)'), n=0, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 267,
    label = "cC2H4O + H <=> C2H4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 268,
    label = "cC2H4O + O <=> cC2H3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(5250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 269,
    label = "cC2H4O + OH <=> cC2H3O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(3610, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 270,
    label = "cC2H4O + HO2 <=> cC2H3O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 271,
    label = "cC2H4O + O2 <=> cC2H3O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(61500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 272,
    label = "cC2H4O + CH3 <=> cC2H3O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(11830, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 273,
    label = "CH2CHOH + H <=> CHCHOH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(240, 'cm^3/(mol*s)'), n=3.63, Ea=(11266, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 274,
    label = "CH2CHOH + H <=> CH2CHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+07, 'cm^3/(mol*s)'), n=1.7, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 275,
    label = "CH2CHOH + O <=> CH2OH + HCO",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(3.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(1494, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(6855, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 277,
    label = "CH2CHOH + O <=> CH2CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+07, 'cm^3/(mol*s)'), n=2, Ea=(4400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 278,
    label = "CH2CHOH + OH <=> CHCHOH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.13, 'cm^3/(mol*s)'), n=4.2, Ea=(-860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 279,
    label = "CH2CHOH + OH <=> CH2CHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+11, 'cm^3/(mol*s)'), n=0.3, Ea=(1600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 280,
    label = "CH2CHOH + O2 => CH2O + HCO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.5e+07, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (39000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 281,
    label = "CHCHOH <=> HCCOH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.5e+29, 's^-1'), n=-5.057, Ea=(52377, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 282,
    label = "CHCHOH + H <=> CH2CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 283,
    label = "CHCHOH + O <=> OCHCHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 284,
    label = "CHCHOH + O2 <=> HCCOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(140, 'cm^3/(mol*s)'), n=3.4, Ea=(3700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 285,
    label = "cC2H3O <=> CH2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.7e+31, 's^-1'), n=-6.9, Ea=(14994, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 286,
    label = "cC2H3O <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 's^-1'), n=0, Ea=(14863, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 287,
    label = "cC2H3O <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.1e+12, 's^-1'), n=0, Ea=(14280, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 288,
    label = "CH2CHO <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+15, 's^-1'), n=-0.15, Ea=(45606, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 289,
    label = "CH2CHO <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 's^-1'), n=0.29, Ea=(40326, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 290,
    label = "CH2CHO + H <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 291,
    label = "CH2CHO + H <=> CH3CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 292,
    label = "CH2CHO + H <=> CH2CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 293,
    label = "CH2CHO + O <=> CH2CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 294,
    label = "CH2CHO + OH <=> CH2CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 295,
    label = "CH2CHO + OH <=> CH2OH + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 296,
    label = "CH2CHO + O2 <=> CH2O + CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e-10, 'cm^3/(mol*s)'),
        n = 6.69,
        Ea = (4868, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 297,
    label = "CH2CHO + CH3 <=> C2H5 + CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.9e+14, 'cm^3/(mol*s)'), n=-0.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 298,
    label = "CH2CHO + HO2 <=> CH2O + HCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=-0.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 299,
    label = "CH2CHO + HO2 <=> CH3CHO + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=-0.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 300,
    label = "CH2CHO + CH2 <=> C2H4 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 301,
    label = "CH3CO <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+12, 's^-1'), n=0.63, Ea=(16895, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 302,
    label = "CH2CO + H <=> CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+08, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (2627, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 303,
    label = "CH3CO + H <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 304,
    label = "CH3CO + H <=> CH2CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 305,
    label = "CH3CO + O <=> CH3 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 306,
    label = "CH3CO + O <=> CH2CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 307,
    label = "CH3CO + OH <=> CH2CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 308,
    label = "CH3CO + CH3OO <=> CH3 + CO2 + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 309,
    label = "CH3CO + CH3 <=> C2H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 310,
    label = "CH3CO + CH3 <=> CH2CO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 311,
    label = "CH3CO + O2 <=> CH2O + CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 312,
    label = "CH2CO + H <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+10, 'cm^3/(mol*s)'),
        n = 0.851,
        Ea = (2840, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 313,
    label = "CH2CO + H <=> HCCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+07, 'cm^3/(mol*s)'), n=2, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 314,
    label = "CH2CO + O <=> CO2 + CH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(1350, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 315,
    label = "CH2CO + O <=> HCCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+07, 'cm^3/(mol*s)'), n=2, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 316,
    label = "CH2CO + OH <=> CH2OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1013, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 317,
    label = "CH2CO + OH <=> CH3 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.7e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1013, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 318,
    label = "CH2CO + OH <=> HCCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+07, 'cm^3/(mol*s)'), n=2, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 319,
    label = "CH2CO + CH2(S) <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 320,
    label = "HCCOH + H <=> HCCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+07, 'cm^3/(mol*s)'), n=2, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 321,
    label = "HCCOH + O <=> HCCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+07, 'cm^3/(mol*s)'), n=2, Ea=(1900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 322,
    label = "HCCOH + OH <=> HCCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+07, 'cm^3/(mol*s)'), n=2, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 323,
    label = "HCCO + H <=> CH2(S) + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 324,
    label = "HCCO + O <=> CO + CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 325,
    label = "HCCO + OH <=> HCO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 326,
    label = "HCCO + OH <=> C2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 327,
    label = "HCCO + O2 <=> CO2 + CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.9e+12, 'cm^3/(mol*s)'),
        n = -0.142,
        Ea = (1150, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 328,
    label = "HCCO + O2 <=> CO + CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+11, 'cm^3/(mol*s)'),
        n = -0.02,
        Ea = (1020, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 329,
    label = "HCCO + O2 <=> HCO + CO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(220, 'cm^3/(mol*s)'), n=2.69, Ea=(3540, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 330,
    label = "HCCO + CH2 <=> C2H3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 331,
    label = "HCCO + HCCO <=> C2H2 + CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 332,
    label = "C2O + O <=> CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 333,
    label = "C2O + OH <=> CO + CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 334,
    label = "C2O + O2 <=> CO + CO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(2600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 335,
    label = "C2O + O2 <=> CO + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(2600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 336,
    label = "CH3CH2OOH <=> CH3CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+17, 's^-1'), n=-0.42, Ea=(44622, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 337,
    label = "CH3CH2OOH + H <=> CH3CHO + OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(1860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 338,
    label = "CH3CH2OOH + H <=> CH3CH2OO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.3e+10, 'cm^3/(mol*s)'), n=0, Ea=(1860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 339,
    label = "CH3CH2OOH + H <=> CH3CH2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+10, 'cm^3/(mol*s)'), n=0, Ea=(1860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 340,
    label = "CH3CH2OOH + O <=> CH3CHO + OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 341,
    label = "CH3CH2OOH + O <=> CH3CH2OO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 342,
    label = "CH3CH2OOH + OH <=> CH3CHO + OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-258, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 343,
    label = "CH3CH2OOH + OH <=> CH3CH2OO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-437, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 344,
    label = "CH3CH2OOH + HO2 <=> CH3CH2OO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 345,
    label = "CH3CH2OO + H <=> CH3CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 346,
    label = "CH3CH2OO + O <=> CH3CH2O + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(-145, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 347,
    label = "CH3CH2OO + OH <=> CH3CH2OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+15, 'cm^3/(mol*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 348,
    label = "CH3CH2OO + OH <=> CH3CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+11, 'cm^3/(mol*s)'), n=0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 349,
    label = "CH3CH2OO + HO2 <=> CH3CH2OOH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1391, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 350,
    label = "CH3CH2OO + CO <=> CH3CH2O + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (160000, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (17940, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 351,
    label = "CH3CH2OO + CH3 <=> CH3CH2O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1411, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 352,
    label = "CH3CH2OO + CH4 <=> CH3CH2OOH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(47000, 'cm^3/(mol*s)'), n=2.5, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 353,
    label = "CH3CH2OO + CH3OH <=> CH3CH2OOH + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(19400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 354,
    label = "CH3CH2OO + CH2O <=> CH3CH2OOH + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 355,
    label = "CH3CH2OO + C2H5 <=> CH3CH2O + CH3CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1411, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 356,
    label = "CH3CH2OO + C2H6 <=> CH3CH2OOH + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.6, 'cm^3/(mol*s)'), n=3.76, Ea=(17200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 357,
    label = "CH3CH2OO + CH3CHO <=> CH3CH2OOH + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+19, 'cm^3/(mol*s)'),
        n = -2.2,
        Ea = (14030, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 358,
    label = "CH3CH2OO + CH3CHO <=> CH3CH2OOH + CH2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+11, 'cm^3/(mol*s)'),
        n = 0.4,
        Ea = (14864, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 359,
    label = "CH3CH2OO + CH3CH2OO <=> CH3CH2O + CH3CH2O + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+11, 'cm^3/(mol*s)'),
        n = -0.27,
        Ea = (408, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 360,
    label = "CH3CH2OO + CH3CH2OO <=> CH3CHO + CH3CH2OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.3e+09, 'cm^3/(mol*s)'), n=0, Ea=(-850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 361,
    label = "CH2CH2OOH <=> cC2H4O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+10, 's^-1'), n=0.72, Ea=(15380, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 362,
    label = "CH2CH2OOH <=> CH3CH2OO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+07, 's^-1'), n=1.04, Ea=(17980, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 363,
    label = "CH2CH2OOH <=> C2H4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+11, 's^-1'), n=0.52, Ea=(16150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 364,
    label = "CH2CHOOH <=> CH2CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+17, 's^-1'), n=-0.42, Ea=(44622, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 365,
    label = "CH2CHOOH + H <=> CH2CHOO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.3e+10, 'cm^3/(mol*s)'), n=0, Ea=(1860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 366,
    label = "CH2CHOOH + H <=> CH2CHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+10, 'cm^3/(mol*s)'), n=0, Ea=(1860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 367,
    label = "CH2CHOOH + O <=> CH2CHOO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 368,
    label = "CH2CHOOH + OH <=> CH2CHOO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-437, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 369,
    label = "CH2CHOOH + HO2 <=> CH2CHOO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 370,
    label = "CH2CHOO <=> C2H2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+48, 's^-1'), n=-8.868, Ea=(110591, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 371,
    label = "CH2CHOO <=> CH2O + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.1e+47, 's^-1'), n=-8.701, Ea=(111046, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 372,
    label = "CH2CHOO + H <=> CH2CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 373,
    label = "CH2CHOO + O <=> CH2CHO + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(-145, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 374,
    label = "CH2CHOO + OH <=> CH2CHOH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+15, 'cm^3/(mol*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 375,
    label = "CH2CHOO + OH <=> CH2CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+11, 'cm^3/(mol*s)'), n=0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 376,
    label = "CH2CHOO + HO2 <=> CH2CHOOH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1391, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 377,
    label = "CH2CHOO + CO <=> CH2CHO + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (160000, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (17940, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 378,
    label = "CH2CHOO + CH3 <=> CH2CHO + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1411, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 379,
    label = "CH2CHOO + CH4 <=> CH2CHOOH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(47000, 'cm^3/(mol*s)'), n=2.5, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 380,
    label = "CH2CHOO + CH3OH <=> CH2CHOOH + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(19400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 381,
    label = "CH2CHOO + CH2O <=> CH2CHOOH + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 382,
    label = "CH2CHOO + C2H6 <=> CH2CHOOH + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.6, 'cm^3/(mol*s)'), n=3.76, Ea=(17200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 383,
    label = "OCHCHO + H <=> CH2O + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 384,
    label = "OCHCHO + OH <=> HCO + CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 385,
    label = "C2H5 + HCO <=> C2H5CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 386,
    label = "C2H5 + CO <=> C2H5CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(4800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 387,
    label = "CH2CHO + CH3 <=> C2H5CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 388,
    label = "C2H5CHO + H <=> C2H5CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 389,
    label = "C2H5CHO + O <=> C2H5CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(1730, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 390,
    label = "C2H5CHO + OH <=> C2H5CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 391,
    label = "C3H6 <=> C2H2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.5e+12, 's^-1'), n=0, Ea=(70000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 392,
    label = "C3H6 <=> H2CCCH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 's^-1'), n=0, Ea=(80000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 393,
    label = "C3H6 + H <=> C2H4 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(1302, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 394,
    label = "C3H6 + H <=> CH2CHCH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(170000, 'cm^3/(mol*s)'), n=2.5, Ea=(2492, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 395,
    label = "C3H6 + H <=> CH3CCH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(410000, 'cm^3/(mol*s)'), n=2.5, Ea=(9794, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 396,
    label = "C3H6 + H <=> CH3CHCH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(800000, 'cm^3/(mol*s)'), n=2.5, Ea=(12284, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 397,
    label = "C3H6 + O <=> C2H5 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+07, 'cm^3/(mol*s)'),
        n = 1.76,
        Ea = (-1220, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 398,
    label = "C3H6 + O <=> CH2CHCH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.2e+11, 'cm^3/(mol*s)'), n=0.7, Ea=(5884, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 399,
    label = "C3H6 + O <=> CH3CHCH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0.7, Ea=(8959, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 400,
    label = "C3H6 + O <=> CH3CCH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+10, 'cm^3/(mol*s)'), n=0.7, Ea=(7632, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 401,
    label = "C3H6 + O <=> CH3CHCO + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+07, 'cm^3/(mol*s)'), n=1.76, Ea=(76, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 402,
    label = "C3H6 + OH <=> CH2CHCH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.1e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 403,
    label = "C3H6 + OH <=> CH3CCH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+06, 'cm^3/(mol*s)'), n=2, Ea=(1451, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 404,
    label = "C3H6 + OH <=> CH3CHCH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1e+06, 'cm^3/(mol*s)'), n=2, Ea=(2778, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 405,
    label = "C3H6 + HO2 <=> CH2CHCH2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9600, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 406,
    label = "C3H6 + HCO <=> CH2CHCH2 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (17010, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 407,
    label = "C3H6 + CH3 <=> CH2CHCH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 408,
    label = "C3H6 + CH3 <=> CH3CCH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.84, 'cm^3/(mol*s)'), n=3.5, Ea=(11656, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 409,
    label = "C3H6 + CH3 <=> CH3CHCH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4, 'cm^3/(mol*s)'), n=3.5, Ea=(12848, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 410,
    label = "CH3CHCH + H <=> C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 411,
    label = "CH3CCH2 + H <=> C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 412,
    label = "CH3CHCH + HO2 <=> C3H6 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 413,
    label = "CH2CHCH2 + HO2 <=> C3H6 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 414,
    label = "CH3CCH2 + HO2 <=> C3H6 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 415,
    label = "CH2CHCH2 + CH2CHCH2 <=> C3H6 + H2CCCH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 416,
    label = "C2H2 + CH3 <=> CH3CHCH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+35, 'cm^3/(mol*s)'),
        n = -7.76,
        Ea = (13300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 417,
    label = "CH3CHCH + H <=> CH2CHCH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 418,
    label = "CH3CHCH + H <=> H3CCCH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 419,
    label = "CH3CHCH + O <=> CH3CHCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 420,
    label = "CH3CHCH + OH <=> H3CCCH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 421,
    label = "CH3CHCH + O2 <=> CH3CHO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+23, 'cm^3/(mol*s)'),
        n = -3.29,
        Ea = (3892, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 422,
    label = "CH3CHCH + O2 <=> CH3CHCO + H + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+15, 'cm^3/(mol*s)'),
        n = -0.78,
        Ea = (3135, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 423,
    label = "C2H2 + CH3 <=> CH3CCH2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+22, 'cm^3/(mol*s)'),
        n = -4.39,
        Ea = (18850, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 424,
    label = "CH3CCH2 + H <=> CH2CHCH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 425,
    label = "CH3CCH2 + H <=> H3CCCH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 426,
    label = "CH3CCH2 + O <=> CH2CO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 427,
    label = "CH3CCH2 + OH <=> H3CCCH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 428,
    label = "CH3CCH2 + O2 <=> CH3CO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+22, 'cm^3/(mol*s)'),
        n = -3.29,
        Ea = (3892, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 429,
    label = "CH3CCH2 + CH3 <=> H3CCCH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 430,
    label = "C2H4 + CH2(S) <=> CH2CHCH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 431,
    label = "C2H3 + CH3 <=> CH2CHCH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(470, 'cm^3/(mol*s)'), n=3.7, Ea=(5677, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 432,
    label = "C2H2 + CH3 <=> CH2CHCH2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+53, 'cm^3/(mol*s)'),
        n = -12.82,
        Ea = (35730, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 433,
    label = "CH2CHCH2 + H <=> H2CCCH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 434,
    label = "CH2CHCH2 + O <=> CH2CHCHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 435,
    label = "CH2CHCH2 + OH <=> H2CCCH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 436,
    label = "CH2CHCH2 + HO2 <=> CH2CHCHO + H + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 437,
    label = "CH2CHCH2 + O2 <=> H2CCCH2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+15, 'cm^3/(mol*s)'), n=-1.4, Ea=(22428, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 438,
    label = "CH2CHCH2 + O2 <=> CH2CHO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+10, 'cm^3/(mol*s)'),
        n = 0.34,
        Ea = (12840, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 439,
    label = "CH2CHCH2 + O2 <=> C2H2 + CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+25, 'cm^3/(mol*s)'),
        n = -4.8,
        Ea = (15468, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 440,
    label = "CH2CHCH2 + O2 <=> CH2CHCHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+13, 'cm^3/(mol*s)'),
        n = -0.41,
        Ea = (22860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 441,
    label = "CH2CHCH2 + CH3 <=> H2CCCH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=-0.3, Ea=(-131, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 442,
    label = "C2H3 + CH2 <=> H2CCCH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 443,
    label = "C2H2 + CH3 <=> H2CCCH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.1e+09, 'cm^3/(mol*s)'),
        n = 0.86,
        Ea = (22153, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 444,
    label = "H2CCCH2 <=> H3CCCH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+14, 's^-1'), n=0, Ea=(68100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 445,
    label = "H2CCCH2 + H <=> H3CCCH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 446,
    label = "H2CCCH2 + H <=> H2CCCH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+07, 'cm^3/(mol*s)'), n=2, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 447,
    label = "H2CCCH2 + H <=> CH3CHCH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+30, 'cm^3/(mol*s)'),
        n = -6.52,
        Ea = (15200, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 448,
    label = "H2CCCH2 + H <=> CH3CCH2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.2e+38, 'cm^3/(mol*s)'),
        n = -8.65,
        Ea = (7000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 449,
    label = "H2CCCH2 + H <=> CH2CHCH2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+61, 'cm^3/(mol*s)'),
        n = -14.67,
        Ea = (26000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 450,
    label = "H2CCCH2 + O <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+07, 'cm^3/(mol*s)'), n=1.8, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 451,
    label = "H2CCCH2 + OH <=> H2CCCH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+07, 'cm^3/(mol*s)'), n=2, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 452,
    label = "H2CCCH2 + CH3 <=> H2CCCH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 453,
    label = "H2CCCH2 + C2H <=> C2H2 + H2CCCH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 454,
    label = "C2H2 + CH3 <=> H3CCCH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+09, 'cm^3/(mol*s)'),
        n = 1.1,
        Ea = (13644, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 455,
    label = "H3CCCH + H <=> H2CCCH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+07, 'cm^3/(mol*s)'), n=2, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 456,
    label = "H3CCCH + O <=> HCCO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(2250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 457,
    label = "H3CCCH + O <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(2250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 458,
    label = "H3CCCH + OH <=> H2CCCH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+07, 'cm^3/(mol*s)'), n=2, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 459,
    label = "H3CCCH + O2 => CH3 + HCO + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(4e+14, 'cm^3/(mol*s)'), n=0, Ea=(41900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 460,
    label = "H3CCCH + CH3 <=> H2CCCH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 461,
    label = "H3CCCH + C2H <=> C2H2 + H2CCCH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 462,
    label = "C2H2 + CH2 <=> H2CCCH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(6621, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 463,
    label = "C2H2 + CH2(S) <=> H2CCCH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 464,
    label = "C2H2 + HCCO <=> H2CCCH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 465,
    label = "C2H3 + C2H3 <=> H2CCCH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 466,
    label = "H2CCCH <=> C3H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.2e+12, 's^-1'), n=0, Ea=(78447, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 467,
    label = "H2CCCH + H <=> C3H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 468,
    label = "H2CCCH + O <=> CH2O + C2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 469,
    label = "H2CCCH + OH <=> C3H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 470,
    label = "H2CCCH + OH <=> CH2O + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 471,
    label = "H2CCCH + OH <=> C2H3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 472,
    label = "H2CCCH + HO2 <=> H2CCCH2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 473,
    label = "H2CCCH + HO2 <=> H3CCCH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 474,
    label = "H2CCCH + O2 <=> CH2CO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(170000, 'cm^3/(mol*s)'), n=1.7, Ea=(1500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 475,
    label = "H2CCCH + HCO <=> H2CCCH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 476,
    label = "H2CCCH + HCO <=> H3CCCH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 477,
    label = "C3H2 + O <=> C2H2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 478,
    label = "C3H2 + OH <=> C2H2 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 479,
    label = "C3H2 + O2 <=> HCCO + CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

