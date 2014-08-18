#!/usr/bin/env python
# encoding: utf-8

name = "Nitrogen_Glarborg_Gimenez_et_al"
shortDesc = u""
longDesc = u"""
Jorge Gimenez Lopeza, Christian Lund Rasmussena, Maria U. Alzuetab, Yide Gaoc, Paul Marshall, Peter Glarborg
Experimental and kinetic modeling study of C2H4 oxidation at high pressure
Proceedings of the Combustion Institute Volume 32, Issue 1, 2009, Pages 367–375
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
    label = "H + H + N2 <=> H2 + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.4e+18, 'cm^6/(mol^2*s)'), n=-1.3, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "H + H + H2 <=> H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+17, 'cm^6/(mol^2*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "H + H + H2O <=> H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+19, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 5,
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
    index = 7,
    label = "OH + OH <=> O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4300, 'cm^3/(mol*s)'), n=2.7, Ea=(-1822, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 8,
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
    index = 9,
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
    index = 10,
    label = "HO2 + H <=> OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 11,
    label = "HO2 + H <=> H2O + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 12,
    label = "HO2 + O <=> OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(-445, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "HO2 + OH <=> H2O + O2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (3.6e+21, 'cm^3/(mol*s)'),
                n = -2.1,
                Ea = (9000, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(2e+15, 'cm^3/(mol*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 15,
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
    index = 17,
    label = "H2O2 + H <=> H2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(3580, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 18,
    label = "H2O2 + H <=> HO2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(3760, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 19,
    label = "H2O2 + O <=> HO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+06, 'cm^3/(mol*s)'), n=2, Ea=(3970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 20,
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
    index = 22,
    label = "CO + O2 <=> CO2 + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(60500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 23,
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
    index = 24,
    label = "CO + OH <=> CO2 + H",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(13909, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.8e+06, 'cm^3/(mol*s)'), n=1.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 26,
    label = "CO + OH <=> HOCO",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (4.9e+25, 'cm^3/(mol*s)'),
                n = -5.2,
                Ea = (1987, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(4e+38, 'cm^3/(mol*s)'), n=-9, Ea=(6955, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5e+43, 'cm^3/(mol*s)'), n=-10, Ea=(13015, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 29,
    label = "HOCO <=> CO2 + H",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.4e+58, 's^-1'), n=-15, Ea=(46500, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1e+71, 's^-1'), n=-18, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 31,
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
    index = 33,
    label = "HOCO + O2 <=> CO2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.9e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 34,
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
    index = 35,
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
    index = 36,
    label = "CH2O + O2 <=> HCO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(240000, 'cm^3/(mol*s)'), n=2.5, Ea=(36461, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 37,
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
    index = 38,
    label = "CH2O + HO2 <=> HCO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 39,
    label = "CH2O + CH3 <=> HCO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(32, 'cm^3/(mol*s)'), n=3.36, Ea=(4310, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 40,
    label = "HCO <=> H + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+13, 's^-1'), n=-0.865, Ea=(16755, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 41,
    label = "HCO + H <=> CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 42,
    label = "HCO + O <=> CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 43,
    label = "HCO + O <=> CO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 44,
    label = "HCO + OH <=> CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 45,
    label = "HCO + O2 <=> CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 46,
    label = "HCO + HO2 <=> CO2 + OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 47,
    label = "HCO + HCO <=> CO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 48,
    label = "CH4 + H <=> CH3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4100, 'cm^3/(mol*s)'), n=3.156, Ea=(8755, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 49,
    label = "CH4 + O <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(440000, 'cm^3/(mol*s)'), n=2.5, Ea=(6577, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 50,
    label = "CH4 + OH <=> CH3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+06, 'cm^3/(mol*s)'), n=2.182, Ea=(2506, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 51,
    label = "CH4 + HO2 <=> CH3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(47000, 'cm^3/(mol*s)'), n=2.5, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 52,
    label = "CH4 + CH2 <=> CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(10030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 53,
    label = "CH4 + CH2(S) <=> CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 54,
    label = "CH3 + H <=> CH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(15100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 55,
    label = "CH2(S) + H2 <=> CH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 56,
    label = "CH3 + O <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 57,
    label = "CH3 + O <=> H2 + CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 58,
    label = "CH3 + OH <=> CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1100, 'cm^3/(mol*s)'), n=3, Ea=(2780, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 59,
    label = "CH2(S) + H2O <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+15, 'cm^3/(mol*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 60,
    label = "CH3 + HO2 <=> CH4 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1800, 'cm^3/(mol*s)'), n=2.83, Ea=(-3730, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 61,
    label = "CH3 + HO2 <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(1075, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 62,
    label = "CH3 + O2 <=> CH3O + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(28297, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 63,
    label = "CH3 + O2 <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+11, 'cm^3/(mol*s)'), n=0, Ea=(9842, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 64,
    label = "CH3 + O2 <=> CH3OO",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (2.8e+18, 'cm^3/(mol*s)'),
                n = -2.2,
                Ea = (1400, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.6e+28, 'cm^3/(mol*s)'),
                n = -5.25,
                Ea = (6850, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 66,
    label = "CH3 + HCO <=> CH4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 67,
    label = "CH3 + CH3 <=> C2H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(16055, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 68,
    label = "CH2 <=> CH + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(5.6e+15, 'cm^3/(mol*s)'), n=0, Ea=(89000, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

entry(
    index = 69,
    label = "CH2 <=> C(T) + H2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (5.8e+12, 'cm^3/(mol*s)'),
            n = 0.5,
            Ea = (68500, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
)

entry(
    index = 70,
    label = "CH2 + H <=> CH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+18, 'cm^3/(mol*s)'), n=-1.56, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 71,
    label = "CH2 + O <=> CO + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 72,
    label = "CH2 + O <=> CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 73,
    label = "CH2 + OH <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 74,
    label = "CH2 + OH <=> CH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+07, 'cm^3/(mol*s)'), n=2, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 75,
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
    index = 76,
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
    index = 77,
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
    index = 78,
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
    index = 79,
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
    index = 80,
    label = "CH2 + CO2 <=> CO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 81,
    label = "CH2(S) + N2 <=> CH2 + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 82,
    label = "CH2(S) + H <=> CH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 83,
    label = "CH2(S) + H <=> CH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 84,
    label = "CH2(S) + O <=> CO + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 85,
    label = "CH2(S) + OH <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 86,
    label = "CH2(S) + O2 <=> CO + OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 87,
    label = "CH2(S) + H2O <=> CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 88,
    label = "CH2(S) + CO2 <=> CH2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 89,
    label = "CH + H <=> C(T) + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 90,
    label = "CH + O <=> CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 91,
    label = "CH + OH <=> HCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 92,
    label = "CH + OH <=> C(T) + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+07, 'cm^3/(mol*s)'), n=2, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 93,
    label = "CH + O2 <=> HCO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 94,
    label = "CH + H2O <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-755, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 95,
    label = "CH + CO2 <=> HCO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.8e+06, 'cm^3/(mol*s)'),
        n = 1.75,
        Ea = (-1040, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 96,
    label = "C(T) + OH <=> CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 97,
    label = "C(T) + O2 <=> CO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 98,
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
    index = 99,
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
    index = 100,
    label = "CH3OH + O <=> CH2OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(5305, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 101,
    label = "CH3OH + O <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(5305, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 102,
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
    index = 103,
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
    index = 104,
    label = "CH3OH + HO2 <=> CH2OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 105,
    label = "CH3OH + O2 <=> CH2OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(46600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 106,
    label = "CH3OH + O2 <=> CH3O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(54800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 107,
    label = "CH2OH + H <=> CH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 108,
    label = "CH2OH + H <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 109,
    label = "CH2OH + O <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(-693, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 110,
    label = "CH2OH + OH <=> CH2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 111,
    label = "CH2OH + HO2 <=> CH2O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 112,
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
    index = 114,
    label = "CH2OH + HCO <=> CH3OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 115,
    label = "CH2OH + HCO <=> CH2O + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 116,
    label = "CH2OH + CH2O <=> CH3OH + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5500, 'cm^3/(mol*s)'), n=2.81, Ea=(5862, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 117,
    label = "CH2OH + CH2OH <=> CH3OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 118,
    label = "CH2OH + CH3O <=> CH3OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 119,
    label = "CH2OH + CH4 <=> CH3OH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(22, 'cm^3/(mol*s)'), n=3.1, Ea=(16227, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 120,
    label = "CH3O + H <=> CH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(745, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 121,
    label = "CH3O + H <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(745, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 122,
    label = "CH3O + O <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 123,
    label = "CH3O + OH <=> CH2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 124,
    label = "CH3O + HO2 <=> CH2O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 125,
    label = "CH3O + O2 <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+10, 'cm^3/(mol*s)'), n=0, Ea=(1749, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 126,
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
    index = 127,
    label = "CH3O + CH3 <=> CH2O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 128,
    label = "CH3O + CH4 <=> CH3OH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+14, 'cm^3/(mol*s)'), n=0, Ea=(15073, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 129,
    label = "CH3O + CH2O <=> CH3OH + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(2981, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 130,
    label = "CH3O + CH3O <=> CH3OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 131,
    label = "CH3OOH <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+26, 's^-1'), n=-3.5, Ea=(46340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 132,
    label = "CH3OOH + H <=> CH2OOH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.4e+10, 'cm^3/(mol*s)'), n=0, Ea=(1860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 133,
    label = "CH3OOH + H <=> CH3OO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.4e+10, 'cm^3/(mol*s)'), n=0, Ea=(1860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 134,
    label = "CH3OOH + H <=> CH3O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+10, 'cm^3/(mol*s)'), n=0, Ea=(1860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 135,
    label = "CH3OOH + O <=> CH2OOH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 136,
    label = "CH3OOH + O <=> CH3OO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 137,
    label = "CH3OOH + OH <=> CH3OO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-437, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 138,
    label = "CH3OOH + OH <=> CH2OOH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-258, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 139,
    label = "CH3OOH + HO2 <=> CH3OO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 140,
    label = "CH3OO + H <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 141,
    label = "CH3OO + O <=> CH3O + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(-445, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 142,
    label = "CH3OO + OH <=> CH3OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+15, 'cm^3/(mol*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 143,
    label = "CH3OO + OH <=> CH3O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+11, 'cm^3/(mol*s)'), n=0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 144,
    label = "CH3OO + HO2 <=> CH3OOH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 145,
    label = "CH3OO + CH3 <=> CH3O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1411, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 146,
    label = "CH3OO + CH4 <=> CH3OOH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(47000, 'cm^3/(mol*s)'), n=2.5, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 147,
    label = "CH3OO + HCO <=> CH3O + H + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 148,
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
    index = 149,
    label = "CH3OO + CH2O <=> CH3OOH + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 150,
    label = "CH3OO + CH3O <=> CH2O + CH3OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 151,
    label = "CH3OO + CH3OH <=> CH3OOH + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(19400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 152,
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
    index = 154,
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
    index = 155,
    label = "CH3OO + C2H5 <=> CH3O + CH3CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1410, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 156,
    label = "CH3OO + C2H6 <=> CH3OOH + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(19, 'cm^3/(mol*s)'), n=3.64, Ea=(17100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 157,
    label = "CH2OOH => CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+14, 's^-1'), n=-1.064, Ea=(1744, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 158,
    label = "C2H6 + H <=> C2H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(9220, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 159,
    label = "C2H6 + O <=> C2H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e-07, 'cm^3/(mol*s)'), n=6.5, Ea=(274, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 160,
    label = "C2H6 + OH <=> C2H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(990, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 161,
    label = "C2H6 + HO2 <=> C2H5 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(110000, 'cm^3/(mol*s)'), n=2.5, Ea=(16850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 162,
    label = "C2H6 + O2 <=> C2H5 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(730000, 'cm^3/(mol*s)'), n=2.5, Ea=(49160, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 163,
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
    index = 165,
    label = "C2H6 + CH2(S) <=> C2H5 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 166,
    label = "C2H5 + O <=> CH3 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 167,
    label = "C2H5 + O <=> CH3CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 168,
    label = "C2H5 + O <=> C2H4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 169,
    label = "C2H5 + OH <=> C2H4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 170,
    label = "C2H5 + HO2 <=> CH3CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 171,
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
    index = 172,
    label = "C2H5 + CH2O <=> C2H6 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5500, 'cm^3/(mol*s)'), n=2.81, Ea=(5860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 173,
    label = "C2H5 + HCO <=> C2H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 174,
    label = "C2H5 + CH3 <=> C2H4 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 175,
    label = "C2H5 + C2H5 <=> C2H6 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 176,
    label = "C2H4 + H <=> C2H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(240, 'cm^3/(mol*s)'), n=3.62, Ea=(11266, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 177,
    label = "CH4 + CH <=> C2H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(-400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 178,
    label = "CH3 + CH2 <=> C2H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 179,
    label = "CH3 + CH2(S) <=> C2H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 180,
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
    index = 182,
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
    index = 184,
    label = "C2H4 + OH <=> C2H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.13, 'cm^3/(mol*s)'), n=4.2, Ea=(-860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 185,
    label = "C2H4 + OH <=> CH3 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+11, 'cm^3/(mol*s)'), n=0, Ea=(9079, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 186,
    label = "C2H4 + OH <=> CH3CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+33, 'cm^3/(mol*s)'),
        n = -6.114,
        Ea = (24907, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 187,
    label = "C2H4 + OH <=> CH2CHOH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(11527, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 188,
    label = "C2H4 + OH <=> CH2CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+20, 'cm^3/(mol*s)'),
        n = -2.399,
        Ea = (3294, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 189,
    label = "C2H4 + HO2 <=> cC2H4O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 190,
    label = "C2H4 + O2 <=> C2H3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(60010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 191,
    label = "C2H4 + CH3 <=> C2H3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+07, 'cm^3/(mol*s)'), n=1.56, Ea=(16630, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 192,
    label = "C2H3 + H <=> C2H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 193,
    label = "CH3 + CH <=> C2H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 194,
    label = "C2H3 + O <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 195,
    label = "C2H3 + OH <=> C2H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 196,
    label = "C2H3 + HO2 <=> CH2CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 197,
    label = "C2H3 + O2 <=> CH2CHOO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1680, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 198,
    label = "C2H3 + O2 <=> CH2O + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(3130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 199,
    label = "C2H3 + O2 <=> CH2CHO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(4800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 200,
    label = "C2H3 + O2 <=> C2H2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.6e+11, 'cm^3/(mol*s)'), n=0, Ea=(7930, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 201,
    label = "C2H3 + O2 <=> CH3O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(3130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 202,
    label = "C2H3 + O2 <=> CH3 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+10, 'cm^3/(mol*s)'), n=0, Ea=(3130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 203,
    label = "C2H3 + CH2O <=> C2H4 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5400, 'cm^3/(mol*s)'), n=2.81, Ea=(5860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 204,
    label = "C2H3 + HCO <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 205,
    label = "C2H3 + CH3 <=> C2H2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 206,
    label = "C2H3 + CH <=> CH2 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 207,
    label = "C2H3 + C2H3 <=> C2H4 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 208,
    label = "C2H3 + C2H <=> C2H2 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 209,
    label = "CH3 + C(T) <=> C2H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 210,
    label = "CH2 + CH <=> C2H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 211,
    label = "CH2 + CH2 <=> C2H2 + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 212,
    label = "C2H2 + O <=> HCCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+07, 'cm^3/(mol*s)'), n=2, Ea=(1900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 213,
    label = "C2H2 + O <=> CH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.1e+06, 'cm^3/(mol*s)'), n=2, Ea=(1900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 214,
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
    index = 215,
    label = "C2H2 + OH <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(830000, 'cm^3/(mol*s)'), n=1.77, Ea=(4697, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 216,
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
    index = 217,
    label = "C2H2 + OH <=> CHCHOH",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (6.2e+20, 'cm^3/(mol*s)'),
                n = -2.8,
                Ea = (2831, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.6e+29, 'cm^3/(mol*s)'),
                n = -4.91,
                Ea = (9734, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 219,
    label = "C2H2 + OH <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(15000, 'cm^3/(mol*s)'), n=2.45, Ea=(4477, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 220,
    label = "C2H2 + HO2 <=> CH2O + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 221,
    label = "C2H2 + HO2 <=> CH2CHO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 222,
    label = "C2H2 + O2 <=> HCO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+07, 'cm^3/(mol*s)'), n=1.8, Ea=(30600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 223,
    label = "C2H2 + CH2(S) <=> C2H2 + CH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 224,
    label = "H2CC <=> C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+07, 's^-1'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 225,
    label = "H2CC + H <=> C2H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 226,
    label = "H2CC + OH <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 227,
    label = "H2CC + O2 <=> CH2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 228,
    label = "C2 + H2 <=> C2H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(400000, 'cm^3/(mol*s)'), n=2.4, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 229,
    label = "CH2 + C(T) <=> C2H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 230,
    label = "C2H + O <=> CH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 231,
    label = "C2H + OH <=> HCCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 232,
    label = "C2H + OH <=> C2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+07, 'cm^3/(mol*s)'), n=2, Ea=(8000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 233,
    label = "C2H + H2 <=> C2H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(410000, 'cm^3/(mol*s)'), n=2.39, Ea=(864, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 234,
    label = "C2H + O2 <=> CO + CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.7e+13, 'cm^3/(mol*s)'), n=-0.16, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 235,
    label = "C2H + CH4 <=> CH3 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(976, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 236,
    label = "C2 <=> C(T) + C(T)",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.5e+16, 'cm^3/(mol*s)'), n=0, Ea=(142300, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

entry(
    index = 237,
    label = "C2 + O <=> C(T) + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 238,
    label = "C2 + OH <=> C2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 239,
    label = "C2 + O2 <=> CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(980, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 240,
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
    index = 241,
    label = "CH3CH2OH + H <=> CH2CH2OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+07, 'cm^3/(mol*s)'), n=1.8, Ea=(5098, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 242,
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
    index = 243,
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
    index = 244,
    label = "CH3CH2OH + O <=> CH2CH2OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.4e+07, 'cm^3/(mol*s)'), n=1.7, Ea=(5459, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 245,
    label = "CH3CH2OH + O <=> CH3CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+07, 'cm^3/(mol*s)'), n=2, Ea=(4448, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 246,
    label = "CH3CH2OH + OH <=> CH3CHOH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.6e+11, 'cm^3/(mol*s)'), n=0.15, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 247,
    label = "CH3CH2OH + OH <=> CH2CH2OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+11, 'cm^3/(mol*s)'), n=0.27, Ea=(600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 248,
    label = "CH3CH2OH + OH <=> CH3CH2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+11, 'cm^3/(mol*s)'), n=0.3, Ea=(1634, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 249,
    label = "CH3CH2OH + HO2 <=> CH3CHOH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8200, 'cm^3/(mol*s)'), n=2.55, Ea=(10750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 250,
    label = "CH3CH2OH + HO2 <=> CH2CH2OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(12000, 'cm^3/(mol*s)'), n=2.55, Ea=(15750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 251,
    label = "CH3CH2OH + HO2 <=> CH3CH2O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(24000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 252,
    label = "CH3CH2OH + CH3 <=> CH3CHOH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(730, 'cm^3/(mol*s)'), n=2.99, Ea=(7948, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 253,
    label = "CH3CH2OH + CH3 <=> CH2CH2OH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(220, 'cm^3/(mol*s)'), n=3.18, Ea=(9622, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 254,
    label = "CH3CH2OH + CH3 <=> CH3CH2O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(150, 'cm^3/(mol*s)'), n=2.99, Ea=(7649, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 255,
    label = "CH3CHOH <=> CH3CHO + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(25000, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

entry(
    index = 256,
    label = "CH3CHOH + O <=> CH3CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 257,
    label = "CH3CHOH + H <=> CH2OH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 258,
    label = "CH3CHOH + H <=> C2H4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 259,
    label = "CH3CHOH + OH <=> CH3CHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 260,
    label = "CH3CHOH + HO2 <=> CH3CHO + OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 261,
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
    index = 263,
    label = "CH2CH2OH <=> CH2CHOH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(220000, 's^-1'), n=2.84, Ea=(32920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 264,
    label = "CH3CH2O <=> CH2CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e-29, 's^-1'), n=11.9, Ea=(4450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 265,
    label = "CH2CH2OH + H <=> CH3 + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 266,
    label = "CH2CH2OH + O <=> CH2O + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 267,
    label = "CH2CH2OH + OH <=> CH2CHOH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 268,
    label = "CH2CH2OH + HO2 <=> CH3CH2OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 269,
    label = "CH2CH2OH + HO2 => CH2OH + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 270,
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
    index = 271,
    label = "CH3CH2O <=> CH3CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+13, 's^-1'), n=0, Ea=(20060, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 272,
    label = "CH3CH2O + H <=> CH3CHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 273,
    label = "CH3CH2O + OH <=> CH3CHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 274,
    label = "CH3CH2O + O2 <=> CH3CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(645, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 275,
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
    index = 276,
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
    index = 277,
    label = "CH3CHO + H <=> CH2CHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+12, 'cm^3/(mol*s)'), n=0.4, Ea=(5359, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 278,
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
    index = 279,
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
    index = 280,
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
    index = 281,
    label = "CH3CHO + OH <=> CH2CHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=-0.6, Ea=(800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 282,
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
    index = 283,
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
    index = 284,
    label = "CH3CHO + O2 <=> CH3CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(120000, 'cm^3/(mol*s)'), n=2.5, Ea=(37554, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 285,
    label = "CH3CHO + CH3 <=> CH3CO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.9e-07, 'cm^3/(mol*s)'), n=5.8, Ea=(2200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 286,
    label = "CH3CHO + CH3 <=> CH2CHO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(25, 'cm^3/(mol*s)'), n=3.15, Ea=(5727, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 287,
    label = "cC2H4O <=> CH2CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 's^-1'), n=0.2, Ea=(71780, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 288,
    label = "cC2H4O <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+13, 's^-1'), n=0.4, Ea=(61880, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 289,
    label = "cC2H4O <=> CH3CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 's^-1'), n=0.25, Ea=(65310, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 290,
    label = "cC2H4O <=> CH2CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+12, 's^-1'), n=-0.2, Ea=(63030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 291,
    label = "cC2H4O <=> CH3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 's^-1'), n=-0.75, Ea=(46424, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 292,
    label = "cC2H4O <=> C2H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.6e+12, 's^-1'), n=0.06, Ea=(69530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 293,
    label = "cC2H4O + H <=> cC2H3O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(8310, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 294,
    label = "cC2H4O + H <=> C2H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+09, 'cm^3/(mol*s)'), n=0, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 295,
    label = "cC2H4O + H <=> C2H4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 296,
    label = "cC2H4O + O <=> cC2H3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(5250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 297,
    label = "cC2H4O + OH <=> cC2H3O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(3610, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 298,
    label = "cC2H4O + HO2 <=> cC2H3O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 299,
    label = "cC2H4O + O2 <=> cC2H3O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(61500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 300,
    label = "cC2H4O + CH3 <=> cC2H3O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(11830, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 301,
    label = "CH2CHOH + H <=> CHCHOH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(240, 'cm^3/(mol*s)'), n=3.63, Ea=(11266, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 302,
    label = "CH2CHOH + H <=> CH2CHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+07, 'cm^3/(mol*s)'), n=1.7, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 303,
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
    index = 305,
    label = "CH2CHOH + O <=> CH2CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+07, 'cm^3/(mol*s)'), n=2, Ea=(4400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 306,
    label = "CH2CHOH + OH <=> CHCHOH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.13, 'cm^3/(mol*s)'), n=4.2, Ea=(-860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 307,
    label = "CH2CHOH + OH <=> CH2CHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+11, 'cm^3/(mol*s)'), n=0.3, Ea=(1600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 308,
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
    index = 309,
    label = "CHCHOH <=> HCCOH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+31, 's^-1'), n=-6.153, Ea=(51383, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 310,
    label = "CHCHOH + H <=> CH2CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 311,
    label = "CHCHOH + O <=> OCHCHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 312,
    label = "CHCHOH + O2 <=> HCCOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(140, 'cm^3/(mol*s)'), n=3.4, Ea=(3700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 313,
    label = "cC2H3O <=> CH2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.7e+31, 's^-1'), n=-6.9, Ea=(14994, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 314,
    label = "cC2H3O <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 's^-1'), n=0, Ea=(14863, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 315,
    label = "cC2H3O <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.1e+12, 's^-1'), n=0, Ea=(14280, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 316,
    label = "CH2CHO <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+36, 's^-1'), n=-6.48, Ea=(55171, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 317,
    label = "CH2CHO <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+33, 's^-1'), n=-5.97, Ea=(50448, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 318,
    label = "CH2CHO + H <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 319,
    label = "CH2CHO + H <=> CH3CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 320,
    label = "CH2CHO + H <=> CH2CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 321,
    label = "CH2CHO + O <=> CH2CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 322,
    label = "CH2CHO + OH <=> CH2CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 323,
    label = "CH2CHO + OH <=> CH2OH + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 324,
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
    index = 325,
    label = "CH2CHO + CH3 <=> C2H5 + CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.9e+14, 'cm^3/(mol*s)'), n=-0.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 326,
    label = "CH2CHO + HO2 <=> CH2O + HCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=-0.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 327,
    label = "CH2CHO + HO2 <=> CH3CHO + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=-0.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 328,
    label = "CH2CHO + CH2 <=> C2H4 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 329,
    label = "CH2CHO + CH <=> C2H3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 330,
    label = "CH3CO <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+20, 's^-1'), n=-2.32, Ea=(18012, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 331,
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
    index = 332,
    label = "CH3CO + H <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 333,
    label = "CH3CO + H <=> CH2CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 334,
    label = "CH3CO + O <=> CH3 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 335,
    label = "CH3CO + O <=> CH2CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 336,
    label = "CH3CO + OH <=> CH2CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 337,
    label = "CH3CO + CH3OO <=> CH3 + CO2 + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 338,
    label = "CH3CO + CH3 <=> C2H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 339,
    label = "CH3CO + CH3 <=> CH2CO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 340,
    label = "CH3CO + O2 <=> CH2O + CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 341,
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
    index = 342,
    label = "CH2CO + H <=> HCCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+07, 'cm^3/(mol*s)'), n=2, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 343,
    label = "CH + CH2O <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(-517, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 344,
    label = "CH2CO + O <=> CO2 + CH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(1350, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 345,
    label = "CH2CO + O <=> HCCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+07, 'cm^3/(mol*s)'), n=2, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 346,
    label = "CH2CO + OH <=> CH2OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1013, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 347,
    label = "CH2CO + OH <=> CH3 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.7e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1013, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 348,
    label = "CH2CO + OH <=> HCCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+07, 'cm^3/(mol*s)'), n=2, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 349,
    label = "CH2CO + CH2(S) <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 350,
    label = "HCCOH + H <=> HCCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+07, 'cm^3/(mol*s)'), n=2, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 351,
    label = "HCCOH + O <=> HCCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+07, 'cm^3/(mol*s)'), n=2, Ea=(1900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 352,
    label = "HCCOH + OH <=> HCCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+07, 'cm^3/(mol*s)'), n=2, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 353,
    label = "HCCO + H <=> CH2(S) + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 354,
    label = "HCCO + O <=> CO + CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 355,
    label = "HCCO + OH <=> HCO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 356,
    label = "HCCO + OH <=> C2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 357,
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
    index = 358,
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
    index = 359,
    label = "HCCO + O2 <=> HCO + CO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(220, 'cm^3/(mol*s)'), n=2.69, Ea=(3540, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 360,
    label = "HCCO + CH2 <=> C2H3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 361,
    label = "HCCO + CH <=> C2H2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 362,
    label = "HCCO + HCCO <=> C2H2 + CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 363,
    label = "C2O <=> C(T) + CO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2e+15, 'cm^3/(mol*s)'), n=0, Ea=(44200, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

entry(
    index = 364,
    label = "C2O + H <=> CH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 365,
    label = "C2O + O <=> CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 366,
    label = "C2O + OH <=> CO + CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 367,
    label = "C2O + O2 <=> CO + CO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(2600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 368,
    label = "C2O + O2 <=> CO + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(2600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 369,
    label = "C2O + C(T) <=> CO + C2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 370,
    label = "CH3CH2OOH <=> CH3CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+35, 's^-1'), n=-6.7, Ea=(47450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 371,
    label = "CH3CH2OOH + H <=> CH3CHOOH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(1860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 372,
    label = "CH3CH2OOH + H <=> CH3CH2OO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.3e+10, 'cm^3/(mol*s)'), n=0, Ea=(1860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 373,
    label = "CH3CH2OOH + H <=> CH3CH2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+10, 'cm^3/(mol*s)'), n=0, Ea=(1860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 374,
    label = "CH3CH2OOH + O <=> CH3CHOOH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 375,
    label = "CH3CH2OOH + O <=> CH3CH2OO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 376,
    label = "CH3CH2OOH + OH <=> CH3CHOOH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-258, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 377,
    label = "CH3CH2OOH + OH <=> CH3CH2OO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-437, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 378,
    label = "CH3CH2OOH + HO2 <=> CH3CH2OO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 379,
    label = "CH3CH2OO + H <=> CH3CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 380,
    label = "CH3CH2OO + O <=> CH3CH2O + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(-145, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 381,
    label = "CH3CH2OO + OH <=> CH3CH2OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+15, 'cm^3/(mol*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 382,
    label = "CH3CH2OO + OH <=> CH3CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+11, 'cm^3/(mol*s)'), n=0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 383,
    label = "CH3CH2OO + HO2 <=> CH3CH2OOH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1391, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 384,
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
    index = 385,
    label = "CH3CH2OO + CH3 <=> CH3CH2O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1411, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 386,
    label = "CH3CH2OO + CH4 <=> CH3CH2OOH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(47000, 'cm^3/(mol*s)'), n=2.5, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 387,
    label = "CH3CH2OO + CH3OH <=> CH3CH2OOH + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(19400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 388,
    label = "CH3CH2OO + CH2O <=> CH3CH2OOH + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 389,
    label = "CH3CH2OO + C2H5 <=> CH3CH2O + CH3CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1411, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 390,
    label = "CH3CH2OO + C2H6 <=> CH3CH2OOH + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.6, 'cm^3/(mol*s)'), n=3.76, Ea=(17200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 391,
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
    index = 392,
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
    index = 393,
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
    index = 394,
    label = "CH3CH2OO + CH3CH2OO <=> CH3CHO + CH3CH2OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.3e+09, 'cm^3/(mol*s)'), n=0, Ea=(-850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 395,
    label = "CH3CHOOH <=> CH3CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.5e+12, 's^-1'), n=-0.947, Ea=(979, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 396,
    label = "CH2CH2OOH <=> cC2H4O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+10, 's^-1'), n=0.72, Ea=(15380, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 397,
    label = "CH2CH2OOH <=> CH3CH2OO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+07, 's^-1'), n=1.04, Ea=(17980, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 398,
    label = "CH2CH2OOH <=> C2H4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+11, 's^-1'), n=0.52, Ea=(16150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 399,
    label = "CH2CHOOH <=> CH2CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+35, 's^-1'), n=-6.7, Ea=(47450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 400,
    label = "CH2CHOOH + H <=> CH2CHOO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.3e+10, 'cm^3/(mol*s)'), n=0, Ea=(1860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 401,
    label = "CH2CHOOH + H <=> CH2CHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+10, 'cm^3/(mol*s)'), n=0, Ea=(1860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 402,
    label = "CH2CHOOH + O <=> CH2CHOO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 403,
    label = "CH2CHOOH + OH <=> CH2CHOO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-437, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 404,
    label = "CH2CHOOH + HO2 <=> CH2CHOO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 405,
    label = "CH2CHOO <=> C2H2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+48, 's^-1'), n=-8.868, Ea=(110591, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 406,
    label = "CH2CHOO <=> CH2O + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.1e+47, 's^-1'), n=-8.701, Ea=(111046, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 407,
    label = "CH2CHOO <=> CYCOOC",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.9e+09, 's^-1'), n=0, Ea=(22250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 408,
    label = "CH2CHOO + H <=> CH2CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 409,
    label = "CH2CHOO + O <=> CH2CHO + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(-145, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 410,
    label = "CH2CHOO + OH <=> CH2CHOH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+15, 'cm^3/(mol*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 411,
    label = "CH2CHOO + OH <=> CH2CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+11, 'cm^3/(mol*s)'), n=0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 412,
    label = "CH2CHOO + HO2 <=> CH2CHOOH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1391, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 413,
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
    index = 414,
    label = "CH2CHOO + CH3 <=> CH2CHO + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1411, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 415,
    label = "CH2CHOO + CH4 <=> CH2CHOOH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(47000, 'cm^3/(mol*s)'), n=2.5, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 416,
    label = "CH2CHOO + CH3OH <=> CH2CHOOH + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(19400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 417,
    label = "CH2CHOO + CH2O <=> CH2CHOOH + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 418,
    label = "CH2CHOO + C2H6 <=> CH2CHOOH + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.6, 'cm^3/(mol*s)'), n=3.76, Ea=(17200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 419,
    label = "CYCOOC <=> CH2O + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.1e+10, 's^-1'), n=0, Ea=(914, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 420,
    label = "CYCOOC <=> OCHCHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 's^-1'), n=-1.093, Ea=(3159, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 421,
    label = "OCHCHO + H <=> CH2O + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 422,
    label = "OCHCHO + OH <=> HCO + CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 423,
    label = "HOCH2CH2OO <=> CH2O + CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.4e+08, 's^-1'), n=0.994, Ea=(22250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 424,
    label = "HOCH2CH2OO + HO2 => CH2OOH + CH2OH + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 425,
    label = "HOCH2CH2OO + CH2O => CH2OOH + CH2OH + HCO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 426,
    label = "HOCH2CH2OO + C2H4 => CH2O + CH2OH + CH3CHO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 427,
    label = "C2H5 + HCO <=> C2H5CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 428,
    label = "CH2CHO + CH3 <=> C2H5CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 429,
    label = "C2H5CHO + H <=> C2H5CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 430,
    label = "C2H5CHO + O <=> C2H5CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(1730, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 431,
    label = "C2H5CHO + OH <=> C2H5CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 432,
    label = "C2H5 + CO <=> C2H5CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(4800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 433,
    label = "C3H6 <=> C2H2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.5e+12, 's^-1'), n=0, Ea=(70000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 434,
    label = "C3H6 <=> H2CCCH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 's^-1'), n=0, Ea=(80000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 435,
    label = "CH3CHCH + H <=> C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 436,
    label = "CH3CCH2 + H <=> C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 437,
    label = "C3H6 + H <=> C2H4 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(1302, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 438,
    label = "C3H6 + H <=> CH2CHCH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(170000, 'cm^3/(mol*s)'), n=2.5, Ea=(2492, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 439,
    label = "C3H6 + H <=> CH3CCH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(410000, 'cm^3/(mol*s)'), n=2.5, Ea=(9794, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 440,
    label = "C3H6 + H <=> CH3CHCH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(800000, 'cm^3/(mol*s)'), n=2.5, Ea=(12284, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 441,
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
    index = 442,
    label = "C3H6 + O <=> CH2CHCH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.2e+11, 'cm^3/(mol*s)'), n=0.7, Ea=(5884, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 443,
    label = "C3H6 + O <=> CH3CHCH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0.7, Ea=(8959, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 444,
    label = "C3H6 + O <=> CH3CCH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+10, 'cm^3/(mol*s)'), n=0.7, Ea=(7632, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 445,
    label = "C3H6 + O <=> CH3CHCO + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+07, 'cm^3/(mol*s)'), n=1.76, Ea=(76, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 446,
    label = "C3H6 + OH <=> CH2CHCH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.1e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 447,
    label = "C3H6 + OH <=> CH3CCH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+06, 'cm^3/(mol*s)'), n=2, Ea=(1451, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 448,
    label = "C3H6 + OH <=> CH3CHCH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1e+06, 'cm^3/(mol*s)'), n=2, Ea=(2778, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 449,
    label = "C3H6 + HO2 <=> CH2CHCH2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9600, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 450,
    label = "CH3CHCH + HO2 <=> C3H6 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 451,
    label = "CH2CHCH2 + HO2 <=> C3H6 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 452,
    label = "CH3CCH2 + HO2 <=> C3H6 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 453,
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
    index = 454,
    label = "C3H6 + CH3 <=> CH2CHCH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 455,
    label = "C3H6 + CH3 <=> CH3CCH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.84, 'cm^3/(mol*s)'), n=3.5, Ea=(11656, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 456,
    label = "C3H6 + CH3 <=> CH3CHCH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4, 'cm^3/(mol*s)'), n=3.5, Ea=(12848, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 457,
    label = "CH2CHCH2 + CH2CHCH2 <=> C3H6 + H2CCCH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 458,
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
    index = 459,
    label = "CH3CHCH + H <=> CH2CHCH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 460,
    label = "CH3CHCH + H <=> H3CCCH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 461,
    label = "CH3CHCH + O <=> CH3CHCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 462,
    label = "CH3CHCH + OH <=> H3CCCH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 463,
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
    index = 464,
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
    index = 465,
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
    index = 466,
    label = "CH3CCH2 + H <=> CH2CHCH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 467,
    label = "CH3CCH2 + H <=> H3CCCH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 468,
    label = "CH3CCH2 + O <=> CH2CO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 469,
    label = "CH3CCH2 + OH <=> H3CCCH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 470,
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
    index = 471,
    label = "CH3CCH2 + CH3 <=> H3CCCH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 472,
    label = "C2H4 + CH2(S) <=> CH2CHCH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 473,
    label = "C2H3 + CH3 <=> CH2CHCH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(470, 'cm^3/(mol*s)'), n=3.7, Ea=(5677, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 474,
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
    index = 475,
    label = "CH2CHCH2 + H <=> H2CCCH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 476,
    label = "CH2CHCH2 + O <=> CH2CHCHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 477,
    label = "CH2CHCH2 + OH <=> H2CCCH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 478,
    label = "CH2CHCH2 + HO2 <=> CH2CHCHO + H + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 479,
    label = "CH2CHCH2 + O2 <=> H2CCCH2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+15, 'cm^3/(mol*s)'), n=-1.4, Ea=(22428, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 480,
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
    index = 481,
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
    index = 482,
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
    index = 483,
    label = "CH2CHCH2 + CH3 <=> H2CCCH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=-0.3, Ea=(-131, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 484,
    label = "C2H3 + CH2 <=> H2CCCH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 485,
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
    index = 486,
    label = "H2CCCH2 <=> H3CCCH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+14, 's^-1'), n=0, Ea=(68100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 487,
    label = "H2CCCH2 + H <=> H3CCCH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 488,
    label = "H2CCCH2 + H <=> H2CCCH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+07, 'cm^3/(mol*s)'), n=2, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 489,
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
    index = 490,
    label = "H2CCCH2 + H <=> CH3CCH2",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (9.2e+38, 'cm^3/(mol*s)'),
        n = -8.65,
        Ea = (7000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 491,
    label = "H2CCCH2 + H <=> CH2CHCH2",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (9.6e+61, 'cm^3/(mol*s)'),
        n = -14.67,
        Ea = (26000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 492,
    label = "H2CCCH2 + O <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+07, 'cm^3/(mol*s)'), n=1.8, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 493,
    label = "H2CCCH2 + OH <=> H2CCCH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+07, 'cm^3/(mol*s)'), n=2, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 494,
    label = "H2CCCH2 + CH3 <=> H2CCCH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 495,
    label = "H2CCCH2 + C2H <=> C2H2 + H2CCCH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 496,
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
    index = 497,
    label = "H3CCCH + H <=> H2CCCH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+07, 'cm^3/(mol*s)'), n=2, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 498,
    label = "H3CCCH + O <=> HCCO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(2250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 499,
    label = "H3CCCH + O <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(2250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 500,
    label = "H3CCCH + OH <=> H2CCCH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+07, 'cm^3/(mol*s)'), n=2, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 501,
    label = "H3CCCH + O2 => CH3 + HCO + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(4e+14, 'cm^3/(mol*s)'), n=0, Ea=(41900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 502,
    label = "H3CCCH + CH3 <=> H2CCCH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 503,
    label = "H3CCCH + C2H <=> C2H2 + H2CCCH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 504,
    label = "cC3H4 <=> H2CCCH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+14, 's^-1'), n=0, Ea=(50450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 505,
    label = "cC3H4 <=> H3CCCH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+15, 's^-1'), n=0, Ea=(43730, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 506,
    label = "C2H2 + CH2 <=> H2CCCH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(6621, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 507,
    label = "C2H2 + CH2(S) <=> H2CCCH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 508,
    label = "C2H2 + HCCO <=> H2CCCH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 509,
    label = "C2H3 + C2H3 <=> H2CCCH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 510,
    label = "H2CCCH <=> C3H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.2e+12, 's^-1'), n=0, Ea=(78447, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 511,
    label = "H2CCCH + H <=> C3H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 512,
    label = "H2CCCH + O <=> CH2O + C2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 513,
    label = "H2CCCH + OH <=> C3H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 514,
    label = "H2CCCH + OH <=> CH2O + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 515,
    label = "H2CCCH + OH <=> C2H3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 516,
    label = "H2CCCH + HO2 <=> H2CCCH2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 517,
    label = "H2CCCH + HO2 <=> H3CCCH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 518,
    label = "H2CCCH + O2 <=> CH2CO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(170000, 'cm^3/(mol*s)'), n=1.7, Ea=(1500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 519,
    label = "H2CCCH + HCO <=> H2CCCH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 520,
    label = "H2CCCH + HCO <=> H3CCCH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 521,
    label = "C3H2 + H <=> C3H + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 522,
    label = "C2H2 + CH <=> C3H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(-121, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 523,
    label = "C3H2 + O <=> C2H2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 524,
    label = "C3H2 + OH <=> C2H2 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 525,
    label = "C3H2 + O2 <=> HCCO + CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 526,
    label = "C3H + O <=> C2H + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 527,
    label = "C3H + O2 <=> HCCO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 528,
    label = "CH2CHCHO + H <=> C2H4 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(3500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 529,
    label = "CH2CHCHO + H <=> CH2CHCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(4200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 530,
    label = "CH2CHCHO + O <=> CH2CHCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(1970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 531,
    label = "CH2CHCHO + O <=> CH2CO + HCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+07, 'cm^3/(mol*s)'), n=1.76, Ea=(76, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 532,
    label = "CH2CHCHO + OH <=> CH2CHCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 533,
    label = "CH2CHCHO + O2 <=> CH2CHCO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(36000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 534,
    label = "CH2CHCO <=> C2H3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(34000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 535,
    label = "CH2CHCO + O <=> C2H3 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 536,
    label = "CH2CHCO + O2 <=> CH2CHO + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.4e+20, 'cm^3/(mol*s)'),
        n = -2.72,
        Ea = (7000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 537,
    label = "HNO + H <=> NO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.4e+11, 'cm^3/(mol*s)'), n=0.72, Ea=(650, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 538,
    label = "HNO + O <=> NO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 539,
    label = "HNO + OH <=> NO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 540,
    label = "HNO + O2 <=> HO2 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 541,
    label = "HNO + HNO <=> N2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+08, 'cm^3/(mol*s)'), n=0, Ea=(3100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 542,
    label = "HNO + NO2 <=> HONO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(44000, 'cm^3/(mol*s)'), n=2.64, Ea=(4040, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 543,
    label = "NO + HO2 <=> NO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-497, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 544,
    label = "NO2 + H <=> NO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+14, 'cm^3/(mol*s)'), n=0, Ea=(362, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 545,
    label = "NO2 + O <=> NO + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+14, 'cm^3/(mol*s)'), n=-0.52, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 546,
    label = "NO2 + HO2 <=> HONO + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9, 'cm^3/(mol*s)'), n=3.32, Ea=(3044, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 547,
    label = "NO2 + HO2 <=> HNO2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(19, 'cm^3/(mol*s)'), n=3.26, Ea=(4983, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 548,
    label = "NO2 + H2 <=> HONO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(13000, 'cm^3/(mol*s)'), n=2.76, Ea=(29770, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 549,
    label = "NO2 + H2 <=> HNO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4, 'cm^3/(mol*s)'), n=3.73, Ea=(32400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 550,
    label = "NO2 + NO2 <=> NO + NO + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(27599, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 551,
    label = "NO2 + NO2 <=> NO3 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+09, 'cm^3/(mol*s)'),
        n = 0.73,
        Ea = (20900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 552,
    label = "HONO + H <=> HNO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.6e+10, 'cm^3/(mol*s)'),
        n = 0.86,
        Ea = (5000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 553,
    label = "HONO + H <=> NO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.1e+06, 'cm^3/(mol*s)'),
        n = 1.89,
        Ea = (3850, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 554,
    label = "HONO + O <=> NO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(5960, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 555,
    label = "HONO + OH <=> NO2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-520, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 556,
    label = "HONO + NO2 <=> HONO2 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(32700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 557,
    label = "HONO + HONO <=> NO + NO2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.35, 'cm^3/(mol*s)'), n=3.64, Ea=(12140, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 558,
    label = "HNO2 + O <=> NO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 559,
    label = "HNO2 + OH <=> NO2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 560,
    label = "NO3 + H <=> NO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 561,
    label = "NO3 + O <=> NO2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 562,
    label = "NO3 + OH <=> NO2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 563,
    label = "NO3 + HO2 <=> NO2 + O2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 564,
    label = "NO3 + NO2 <=> NO + NO2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(2940, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 565,
    label = "HONO2 + H <=> H2 + NO3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.6e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (16400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 566,
    label = "HONO2 + H <=> H2O + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(61, 'cm^3/(mol*s)'), n=3.3, Ea=(6285, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 567,
    label = "HONO2 + H <=> OH + HONO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(380000, 'cm^3/(mol*s)'), n=2.3, Ea=(6976, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 568,
    label = "HONO2 + OH <=> H2O + NO3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+10, 'cm^3/(mol*s)'), n=0, Ea=(-1240, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 569,
    label = "N2O + H <=> N2 + OH",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(3.3e+10, 'cm^3/(mol*s)'), n=0, Ea=(4729, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.4e+14, 'cm^3/(mol*s)'), n=0, Ea=(19254, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 571,
    label = "N2O + O <=> NO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(27679, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 572,
    label = "N2O + O <=> N2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(15936, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 573,
    label = "N2O + OH <=> N2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.013, 'cm^3/(mol*s)'), n=4.72, Ea=(36560, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 574,
    label = "N2O + OH <=> HNO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00012, 'cm^3/(mol*s)'),
        n = 4.33,
        Ea = (25080, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 575,
    label = "N2O + NO <=> NO2 + N2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (530000, 'cm^3/(mol*s)'),
        n = 2.23,
        Ea = (46280, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 576,
    label = "NH3 <=> NH2 + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.2e+16, 'cm^3/(mol*s)'), n=0, Ea=(93470, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

entry(
    index = 577,
    label = "NH3 + H <=> NH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (640000, 'cm^3/(mol*s)'),
        n = 2.39,
        Ea = (10171, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 578,
    label = "NH3 + O <=> NH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.4e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (6460, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 579,
    label = "NH3 + OH <=> NH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+06, 'cm^3/(mol*s)'), n=2.04, Ea=(566, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 580,
    label = "NH3 + HO2 <=> NH2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 581,
    label = "NH2 + H <=> NH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(720000, 'cm^3/(mol*s)'), n=2.32, Ea=(799, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 582,
    label = "NH2 + O <=> HNO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.6e+14, 'cm^3/(mol*s)'), n=-0.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 583,
    label = "NH2 + O <=> NH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 584,
    label = "NH2 + OH <=> NH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+06, 'cm^3/(mol*s)'), n=2, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 585,
    label = "NH2 + HO2 <=> H2NO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 586,
    label = "NH2 + HO2 <=> NH3 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 587,
    label = "NH2 + O2 <=> H2NO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.48,
        Ea = (29586, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 588,
    label = "NH2 + O2 <=> HNO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.2e+07, 'cm^3/(mol*s)'),
        n = 1.23,
        Ea = (35100, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 589,
    label = "NH2 + NH2 <=> NH3 + NH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 590,
    label = "NH2 + NH <=> N2H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 591,
    label = "NH2 + NH <=> NH3 + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(920000, 'cm^3/(mol*s)'), n=1.94, Ea=(2444, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 592,
    label = "NH2 + N <=> N2 + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 593,
    label = "NH2 + HNO <=> NH3 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.6e+06, 'cm^3/(mol*s)'),
        n = 1.63,
        Ea = (-1250, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 594,
    label = "NH2 + NO <=> N2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+20, 'cm^3/(mol*s)'),
        n = -2.654,
        Ea = (1258, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 595,
    label = "NH2 + NO <=> NNH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+10, 'cm^3/(mol*s)'),
        n = 0.425,
        Ea = (-814, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 596,
    label = "NH2 + HONO <=> NH3 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(71, 'cm^3/(mol*s)'), n=3.02, Ea=(-4940, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 597,
    label = "NH2 + NO2 <=> N2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+16, 'cm^3/(mol*s)'),
        n = -1.44,
        Ea = (268, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 598,
    label = "NH2 + NO2 <=> H2NO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.5e+16, 'cm^3/(mol*s)'),
        n = -1.44,
        Ea = (268, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 599,
    label = "NH + H <=> N + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 600,
    label = "NH + O <=> NO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 601,
    label = "NH + OH <=> HNO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 602,
    label = "NH + OH <=> N + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+11, 'cm^3/(mol*s)'), n=0.5, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 603,
    label = "NH + O2 <=> HNO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(460000, 'cm^3/(mol*s)'), n=2, Ea=(6500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 604,
    label = "NH + O2 <=> NO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+06, 'cm^3/(mol*s)'), n=1.5, Ea=(100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 605,
    label = "NH + NH <=> N2 + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 606,
    label = "NH + N <=> N2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 607,
    label = "NH + NO <=> N2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+14, 'cm^3/(mol*s)'), n=-0.4, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 608,
    label = "NH + NO <=> N2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+13, 'cm^3/(mol*s)'), n=-0.23, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 609,
    label = "NH + HONO <=> NH2 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 610,
    label = "NH + NO2 <=> N2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 611,
    label = "N + OH <=> NO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 612,
    label = "N + O2 <=> NO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.4e+09, 'cm^3/(mol*s)'), n=1, Ea=(6280, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 613,
    label = "N + NO <=> N2 + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+12, 'cm^3/(mol*s)'), n=0.3, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 614,
    label = "NNH <=> N2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.5e+07, 's^-1'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 615,
    label = "NNH + H <=> N2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 616,
    label = "NNH + O <=> N2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 617,
    label = "NNH + O <=> N2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 618,
    label = "NNH + O <=> NH + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 619,
    label = "NNH + OH <=> N2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 620,
    label = "NNH + O2 <=> N2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 621,
    label = "NNH + O2 <=> N2 + H + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 622,
    label = "NNH + NH <=> N2 + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 623,
    label = "NNH + NH2 <=> N2 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 624,
    label = "NNH + NO <=> N2 + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 625,
    label = "NH2 + NH2 <=> N2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.6e+48, 'cm^3/(mol*s)'),
        n = -11.3,
        Ea = (11882, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 626,
    label = "N2H4 + H <=> N2H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(2500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 627,
    label = "N2H4 + O <=> N2H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.4e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1270, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 628,
    label = "N2H4 + O <=> N2H3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.7e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(2851, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 629,
    label = "N2H4 + OH <=> N2H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 630,
    label = "N2H4 + NH2 <=> N2H3 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(1500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 631,
    label = "N2H3 <=> N2H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+47, 's^-1'), n=-10.38, Ea=(69009, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 632,
    label = "NH2 + NH2 <=> N2H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+12, 'cm^3/(mol*s)'),
        n = -0.03,
        Ea = (10084, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 633,
    label = "N2H3 + H <=> N2H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-10, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 634,
    label = "N2H3 + O <=> N2H2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-646, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 635,
    label = "N2H3 + O <=> NH2 + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 636,
    label = "N2H3 + O => NH2 + NO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 637,
    label = "N2H3 + OH <=> N2H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 638,
    label = "N2H3 + OH <=> H2NN + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 639,
    label = "N2H3 + OH <=> NH3 + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 640,
    label = "N2H3 + HO2 <=> N2H2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14000, 'cm^3/(mol*s)'), n=2.69, Ea=(-1600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 641,
    label = "N2H3 + HO2 <=> N2H4 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(920000, 'cm^3/(mol*s)'), n=1.94, Ea=(2126, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 642,
    label = "N2H3 + NH2 <=> N2H2 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 643,
    label = "N2H3 + NH2 <=> H2NN + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 644,
    label = "N2H3 + NH <=> N2H2 + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 645,
    label = "N2H2 + H <=> NNH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(85000, 'cm^3/(mol*s)'), n=2.63, Ea=(230, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 646,
    label = "N2H2 + O <=> NNH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(497, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 647,
    label = "N2H2 + O <=> NH2 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 648,
    label = "N2H2 + OH <=> NNH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(59, 'cm^3/(mol*s)'), n=3.4, Ea=(1360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 649,
    label = "N2H2 + NH2 <=> NNH + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.088, 'cm^3/(mol*s)'), n=4.05, Ea=(1610, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 650,
    label = "N2H2 + NH <=> NNH + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 651,
    label = "N2H2 + NO <=> N2O + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(11922, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 652,
    label = "NH2 + NH2 <=> H2NN + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+21, 'cm^3/(mol*s)'),
        n = -3.08,
        Ea = (3368, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 653,
    label = "H2NN <=> NNH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.4e+26, 's^-1'), n=-4.83, Ea=(46228, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 654,
    label = "H2NN + H <=> NNH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 655,
    label = "H2NN + H <=> N2H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 656,
    label = "H2NN + O <=> NNH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 657,
    label = "H2NN + O <=> NH2 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 658,
    label = "H2NN + OH <=> NNH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 659,
    label = "H2NN + OH => NH2 + NO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 660,
    label = "H2NN + HO2 => NH2 + NO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 661,
    label = "H2NN + HO2 <=> NNH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(29000, 'cm^3/(mol*s)'), n=2.69, Ea=(-1600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 662,
    label = "H2NN + O2 <=> NH2 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(5961, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 663,
    label = "H2NN + NH2 <=> NNH + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 664,
    label = "H2NO + H <=> HNO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+07, 'cm^3/(mol*s)'), n=2, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 665,
    label = "H2NO + H <=> NH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 666,
    label = "H2NO + O <=> HNO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+07, 'cm^3/(mol*s)'), n=2, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 667,
    label = "H2NO + OH <=> HNO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+07, 'cm^3/(mol*s)'), n=2, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 668,
    label = "H2NO + HO2 <=> HNO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(29000, 'cm^3/(mol*s)'), n=2.69, Ea=(-1600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 669,
    label = "H2NO + O2 <=> HNO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(25000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 670,
    label = "H2NO + NH2 <=> HNO + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 671,
    label = "H2NO + NO <=> HNO + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(20000, 'cm^3/(mol*s)'), n=2, Ea=(13000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 672,
    label = "H2NO + NO2 <=> HONO + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 'cm^3/(mol*s)'), n=0, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 673,
    label = "HNOH + H <=> NH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 674,
    label = "HNOH + H <=> HNO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(378, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 675,
    label = "HNOH + O <=> HNO + OH",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.3e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-358, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 677,
    label = "HNOH + OH <=> HNO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 678,
    label = "HNOH + HO2 <=> HNO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(29000, 'cm^3/(mol*s)'), n=2.69, Ea=(-1600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 679,
    label = "HNOH + O2 <=> HNO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(25000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 680,
    label = "HNOH + NH2 <=> N2H3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(10, 'cm^3/(mol*s)'), n=3.46, Ea=(-467, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 681,
    label = "HNOH + NH2 <=> H2NN + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.8e+16, 'cm^3/(mol*s)'),
        n = -1.08,
        Ea = (1113, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 682,
    label = "HNOH + NH2 <=> NH3 + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 683,
    label = "HNOH + NO2 <=> HONO + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 'cm^3/(mol*s)'), n=0, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 684,
    label = "HCN + N2 <=> H + CN + N2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.6e+26, 'cm^3/(mol*s)'),
        n = -2.6,
        Ea = (124890, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 685,
    label = "CN + H2 <=> HCN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(110000, 'cm^3/(mol*s)'), n=2.6, Ea=(1908, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 686,
    label = "HCN + O <=> NCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14000, 'cm^3/(mol*s)'), n=2.64, Ea=(4980, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 687,
    label = "HCN + O <=> CN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+10, 'cm^3/(mol*s)'),
        n = 0.4,
        Ea = (20665, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 688,
    label = "HCN + O <=> NH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3500, 'cm^3/(mol*s)'), n=2.64, Ea=(4980, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 689,
    label = "HCN + OH <=> CN + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.9e+06, 'cm^3/(mol*s)'),
        n = 1.83,
        Ea = (10300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 690,
    label = "HCN + OH <=> HOCN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(59000, 'cm^3/(mol*s)'), n=2.4, Ea=(12500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 691,
    label = "HCN + OH <=> HNCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.002, 'cm^3/(mol*s)'), n=4, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 692,
    label = "HCN + OH <=> NH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00078, 'cm^3/(mol*s)'), n=4, Ea=(4000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 693,
    label = "HCN + O2 <=> CN + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(75100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 694,
    label = "HCN + CN <=> NCCN + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+07, 'cm^3/(mol*s)'),
        n = 1.71,
        Ea = (1530, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 695,
    label = "HNC + H <=> HCN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(3600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 696,
    label = "HNC + O <=> NH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(2200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 697,
    label = "HNC + OH <=> HNCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(3700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 698,
    label = "HNC + CN <=> NCCN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 699,
    label = "CN + O <=> CO + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+12, 'cm^3/(mol*s)'), n=0.46, Ea=(723, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 700,
    label = "CN + OH <=> NCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+15, 'cm^3/(mol*s)'), n=-0.437, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 701,
    label = "CN + O2 <=> NCO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(-417, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 702,
    label = "CN + O2 <=> NO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+17, 'cm^3/(mol*s)'), n=-2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 703,
    label = "CN + NO <=> NCO + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(42100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 704,
    label = "CN + NO2 <=> NCO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.3e+15, 'cm^3/(mol*s)'),
        n = -0.752,
        Ea = (344, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 705,
    label = "CN + NO2 <=> CO + N2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.9e+14, 'cm^3/(mol*s)'),
        n = -0.752,
        Ea = (344, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 706,
    label = "CN + NO2 <=> N2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+14, 'cm^3/(mol*s)'),
        n = -0.752,
        Ea = (344, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 707,
    label = "CN + HNO <=> HCN + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 708,
    label = "CN + HONO <=> HCN + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 709,
    label = "CN + N2O <=> NCN + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3800, 'cm^3/(mol*s)'), n=2.6, Ea=(3700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 710,
    label = "CN + HNCO <=> HCN + NCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 711,
    label = "CN + NCO <=> NCN + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 712,
    label = "HNCO + H <=> NH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(36000, 'cm^3/(mol*s)'), n=2.49, Ea=(2345, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 713,
    label = "HNCO + H <=> NCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+07, 'cm^3/(mol*s)'), n=1.66, Ea=(13900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 714,
    label = "HNCO + O <=> NCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+06, 'cm^3/(mol*s)'),
        n = 2.11,
        Ea = (11430, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 715,
    label = "HNCO + O <=> NH + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+07, 'cm^3/(mol*s)'),
        n = 1.41,
        Ea = (8520, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 716,
    label = "HNCO + O <=> HNO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+08, 'cm^3/(mol*s)'),
        n = 1.57,
        Ea = (44012, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 717,
    label = "HNCO + OH <=> NCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+07, 'cm^3/(mol*s)'), n=1.5, Ea=(3600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 718,
    label = "HNCO + HO2 <=> NCO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 719,
    label = "HNCO + O2 <=> HNO + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(35000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 720,
    label = "HNCO + NH <=> NH2 + NCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(23700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 721,
    label = "HOCN + H <=> HNCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+08, 'cm^3/(mol*s)'),
        n = 0.84,
        Ea = (1917, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 722,
    label = "HOCN + H <=> NH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+08, 'cm^3/(mol*s)'),
        n = 0.61,
        Ea = (2076, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 723,
    label = "HOCN + H <=> H2 + NCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(6617, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 724,
    label = "HOCN + O <=> OH + NCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(4133, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 725,
    label = "HOCN + OH <=> H2O + NCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(-248, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 726,
    label = "HOCN + NH2 <=> NCO + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(920000, 'cm^3/(mol*s)'), n=1.94, Ea=(3646, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 727,
    label = "HCNO <=> HCN + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.2e+31, 's^-1'), n=-6.12, Ea=(61210, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 728,
    label = "HCNO + H <=> HCN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.2e+10, 'cm^3/(mol*s)'),
        n = 0.841,
        Ea = (8612, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 729,
    label = "HCNO + O <=> HCO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 730,
    label = "HCNO + OH <=> CH2O + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 731,
    label = "HCNO + O <=> NCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 732,
    label = "HCNO + OH <=> NO + CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 733,
    label = "HCNO + OH <=> NCO + H + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 734,
    label = "HCNO + OH <=> NCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 735,
    label = "HCNO + OH <=> HCO + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 736,
    label = "NCO + H <=> CO + NH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 737,
    label = "NCO + O <=> NO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+15, 'cm^3/(mol*s)'), n=-0.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 738,
    label = "NCO + OH <=> HON + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.3e+12, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (5126, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 739,
    label = "NCO + OH <=> H + CO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.3e+12, 'cm^3/(mol*s)'),
        n = -0.05,
        Ea = (18042, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 740,
    label = "NCO + HO2 <=> HNCO + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 741,
    label = "NCO + O2 <=> NO + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(20000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 742,
    label = "NCO + NO <=> N2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+19, 'cm^3/(mol*s)'), n=-2.19, Ea=(1743, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 743,
    label = "NCO + NO <=> N2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+21, 'cm^3/(mol*s)'),
        n = -2.74,
        Ea = (1824, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 744,
    label = "NCO + NO2 <=> CO + NO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(-707, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 745,
    label = "NCO + NO2 <=> CO2 + N2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(-707, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 746,
    label = "NCO + HNO <=> HNCO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 747,
    label = "NCO + HONO <=> HNCO + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 748,
    label = "NCO + N <=> N2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 749,
    label = "NCO + NH3 <=> HNCO + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(28000, 'cm^3/(mol*s)'), n=2.48, Ea=(980, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 750,
    label = "NCO + NCO <=> CO + CO + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 751,
    label = "H2CN <=> HCN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+28, 's^-1'), n=-6.03, Ea=(29897, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 752,
    label = "H2CN + H <=> HCN + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 753,
    label = "H2CN + O <=> HCN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 754,
    label = "H2CN + OH <=> HCN + H2O",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.5e+19, 'cm^3/(mol*s)'),
                n = -2.18,
                Ea = (2166, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(1.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 756,
    label = "H2CN + O2 <=> CH2O + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(5961, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 757,
    label = "H2CN + NH2 <=> HCN + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 758,
    label = "H2CN + N <=> CH2 + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 759,
    label = "HCNH <=> HCN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.1e+28, 's^-1'), n=-5.69, Ea=(24271, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 760,
    label = "HCNH + H <=> H2CN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 761,
    label = "HCNH + H <=> HCN + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 762,
    label = "HCNH + O <=> HNCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 763,
    label = "HCNH + O <=> HCN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 764,
    label = "HCNH + OH <=> HCN + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 765,
    label = "CO + NO2 <=> NO + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(33800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 766,
    label = "CO + N2O <=> N2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.7e+11, 'cm^3/(mol*s)'), n=0, Ea=(20237, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 767,
    label = "CH2O + NO2 <=> HONO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e-07, 'cm^3/(mol*s)'),
        n = 5.64,
        Ea = (9220, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 768,
    label = "CH2O + NO2 <=> HNO2 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.11, 'cm^3/(mol*s)'), n=4.22, Ea=(19850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 769,
    label = "HCO + NO <=> HNO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 770,
    label = "HCO + NO2 <=> NO + CO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 771,
    label = "HCO + NO2 <=> HONO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 772,
    label = "HCO + NO2 <=> NO + CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 773,
    label = "HCO + HNO <=> NO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.58, 'cm^3/(mol*s)'), n=3.84, Ea=(115, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 774,
    label = "CH4 + NO2 <=> HONO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.5e+14, 'cm^3/(mol*s)'), n=0, Ea=(45800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 775,
    label = "CH4 + NO2 <=> HNO2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+14, 'cm^3/(mol*s)'), n=0, Ea=(37600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 776,
    label = "CH3 + NO2 <=> CH3O + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 777,
    label = "CH3 + HNO <=> NO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+14, 'cm^3/(mol*s)'), n=0, Ea=(8400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 778,
    label = "CH3OH + NO2 <=> HONO + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(150, 'cm^3/(mol*s)'), n=3.32, Ea=(20035, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 779,
    label = "CH3OH + NO2 <=> HNO2 + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2400, 'cm^3/(mol*s)'), n=2.9, Ea=(27470, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 780,
    label = "CH3O + NO <=> HNO + CH2O",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(7.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(2017, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.5e+18, 'cm^3/(mol*s)'), n=-2.56, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 782,
    label = "CH3O + NO2 <=> HONO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(2285, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 783,
    label = "CH3O + HNO <=> NO + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 784,
    label = "CH2OH + NO <=> CH2O + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 785,
    label = "CH2OH + NO2 <=> HONO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 786,
    label = "CH2OH + HNO <=> NO + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 787,
    label = "CH3OO + NO <=> NO2 + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(-715, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 788,
    label = "C2H6 + NO2 <=> HONO + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.5e+14, 'cm^3/(mol*s)'), n=0, Ea=(41400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 789,
    label = "C2H6 + NO2 <=> HNO2 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+14, 'cm^3/(mol*s)'), n=0, Ea=(33200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 790,
    label = "C2H5 + NO2 <=> NO + CH3CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=-0.2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 791,
    label = "C2H4 + NO2 <=> HONO + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.5e+14, 'cm^3/(mol*s)'), n=0, Ea=(41400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 792,
    label = "C2H4 + NO2 <=> HNO2 + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+14, 'cm^3/(mol*s)'), n=0, Ea=(33200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 793,
    label = "C2H3 + NO <=> C2H2 + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 794,
    label = "C2H3 + NO2 <=> NO + CH2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.7e+14, 'cm^3/(mol*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 795,
    label = "CH3CH2OO + NO <=> NO2 + CH3CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(-755, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 796,
    label = "CH3CH2O + NO <=> HNO + CH3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 797,
    label = "CH3CH2O + NO2 <=> HONO + CH3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 798,
    label = "CH2CHO + NO2 <=> CH2CO + HONO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-159, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 799,
    label = "CH3CO + NO2 => CH3 + CO2 + NO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 800,
    label = "CH2CH2OH + NO2 => CH2O + CH2OH + NO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 801,
    label = "CH2CHOO + NO <=> NO2 + CH2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(-755, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 802,
    label = "HOCH2CH2OO + NO => CH2OH + CH2O + NO2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(-755, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 803,
    label = "CH3NO2 + H <=> HONO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(3730, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 804,
    label = "CH3NO2 + H <=> CH3NO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(3730, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 805,
    label = "CH3NO2 + H <=> CH2NO2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(540, 'cm^3/(mol*s)'), n=3.5, Ea=(5200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 806,
    label = "CH3NO2 + O <=> CH2NO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(5350, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 807,
    label = "CH3NO2 + O2 <=> CH2NO2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(57000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 808,
    label = "CH3NO2 + OH <=> CH3OH + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+10, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 809,
    label = "CH3NO2 + OH <=> CH2NO2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(500000, 'cm^3/(mol*s)'), n=2, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 810,
    label = "CH3NO2 + HO2 <=> CH2NO2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(23000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 811,
    label = "CH3NO2 + CH3 <=> CH2NO2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.55, 'cm^3/(mol*s)'), n=4, Ea=(8300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 812,
    label = "CH3NO2 + CH3O <=> CH2NO2 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 813,
    label = "CH3NO2 + NO2 <=> CH2NO2 + HONO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(32000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 814,
    label = "CH2NO2 <=> CH2O + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(36000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 815,
    label = "CH2NO2 + H <=> CH3 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 816,
    label = "CH2NO2 + O <=> CH2O + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 817,
    label = "CH2NO2 + OH <=> CH2OH + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 818,
    label = "CH2NO2 + OH <=> CH2O + HONO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 819,
    label = "CH3ONO + H <=> CH3OH + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(1900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 820,
    label = "CH3ONO + H <=> CH2O + H2 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+11, 'cm^3/(mol*s)'), n=0, Ea=(1900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 821,
    label = "CH3ONO + O <=> CH3O + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(5210, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 822,
    label = "CH3ONO + OH <=> CH3OH + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(3505, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 823,
    label = "CH3ONO2 + H <=> CH3O + HONO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 824,
    label = "CH3ONO2 + O <=> CH3O + NO3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(5260, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 825,
    label = "CH3ONO2 + OH <=> CH3O + HONO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.9e+11, 'cm^3/(mol*s)'), n=0, Ea=(2027, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 826,
    label = "C2H5NO2 + OH <=> CH3CH2OH + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+10, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 827,
    label = "CH3CH2ONO + OH <=> CH3CH2OH + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+14, 'cm^3/(mol*s)'), n=0, Ea=(3505, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 828,
    label = "CH3CH2ONO2 + OH <=> CH3CH2O + HONO2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(2.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(2140, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.2e+10, 'cm^3/(mol*s)'), n=0, Ea=(-250, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 830,
    label = "CO2 + CN <=> NCO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+06, 'cm^3/(mol*s)'),
        n = 2.16,
        Ea = (26900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 831,
    label = "CH2O + NCO <=> HNCO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 832,
    label = "HCO + NCO <=> HNCO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 833,
    label = "CH4 + NH2 <=> CH3 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(710000, 'cm^3/(mol*s)'), n=2, Ea=(9300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 834,
    label = "CH4 + NH <=> CH3 + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(20000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 835,
    label = "CH4 + CN <=> CH3 + HCN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(62000, 'cm^3/(mol*s)'), n=2.64, Ea=(-437, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 836,
    label = "CH4 + NCO <=> CH3 + HNCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(8120, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 837,
    label = "CH3 + N <=> H2CN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 838,
    label = "CH3 + NO <=> HCN + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.15, 'cm^3/(mol*s)'), n=3.52, Ea=(3950, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 839,
    label = "CH3 + NO <=> H2CN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.15, 'cm^3/(mol*s)'), n=3.52, Ea=(3950, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 840,
    label = "CH3 + CN <=> CH2CN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 841,
    label = "CH3 + HOCN <=> CH3CN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 842,
    label = "CH2 + N <=> HCN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 843,
    label = "CH2 + NO <=> HCNO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-378, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 844,
    label = "CH2 + NO <=> HCN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.9e+11, 'cm^3/(mol*s)'), n=0, Ea=(-378, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 845,
    label = "CH2 + NO2 <=> CH2O + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 846,
    label = "CH2 + N2 <=> HCN + NH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(74000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 847,
    label = "CH2(S) + NO <=> HCN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 848,
    label = "CH2(S) + NO <=> CH2 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 849,
    label = "CH2(S) + HCN <=> CH3 + CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 850,
    label = "CH + NH3 <=> H2CN + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(-630, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 851,
    label = "CH + N <=> CN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 852,
    label = "CH + NO <=> HCN + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 853,
    label = "CH + NO <=> HCO + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 854,
    label = "CH + NO <=> NCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 855,
    label = "CH + NO2 <=> HCO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 856,
    label = "CH + N2O <=> HCN + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+13, 'cm^3/(mol*s)'), n=0, Ea=(-511, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 857,
    label = "CH + N2 <=> NCN + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+07, 'cm^3/(mol*s)'),
        n = 1.42,
        Ea = (20723, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 858,
    label = "C(T) + NO <=> CN + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 859,
    label = "C(T) + NO <=> CO + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 860,
    label = "C(T) + N2O <=> CN + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 861,
    label = "C(T) + N2 <=> CN + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(46000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 862,
    label = "CH2OH + CN <=> CH2CN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 863,
    label = "C2H6 + NH2 <=> C2H5 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.1e+06, 'cm^3/(mol*s)'), n=1.8, Ea=(6300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 864,
    label = "C2H6 + CN <=> C2H5 + HCN",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000, 'cm^3/(mol*s)'),
        n = 2.77,
        Ea = (-1788, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 865,
    label = "C2H6 + NCO <=> C2H5 + HNCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e-09, 'cm^3/(mol*s)'),
        n = 6.89,
        Ea = (-2910, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 866,
    label = "C2H5 + N <=> C2H4 + NH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 867,
    label = "C2H5 + N <=> CH3 + H2CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 868,
    label = "C2H4 + NH2 <=> C2H3 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(3950, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 869,
    label = "C2H4 + CN <=> C2H3 + HCN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.9e+14, 'cm^3/(mol*s)'), n=-0.24, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 870,
    label = "C2H3 + NO <=> HCN + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+21, 'cm^3/(mol*s)'),
        n = -3.382,
        Ea = (1025, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 871,
    label = "C2H2 + NCO <=> HCCO + HCN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(1815, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 872,
    label = "C2H + NH3 <=> C2H2 + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(-735, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 873,
    label = "C2H + NO <=> HCN + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(570, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 874,
    label = "C2 + NO <=> CN + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 875,
    label = "C2 + N2 <=> CN + CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(41730, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 876,
    label = "HCCO + N <=> HCN + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 877,
    label = "HCCO + NO <=> HCNO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.9e+12, 'cm^3/(mol*s)'),
        n = 0.089,
        Ea = (-457, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 878,
    label = "HCCO + NO <=> HCN + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+14, 'cm^3/(mol*s)'),
        n = -0.75,
        Ea = (-90, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 879,
    label = "HCCO + NO2 <=> HCNO + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 880,
    label = "C2O + NO <=> CO + NCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 881,
    label = "NCN + H <=> HCN + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 882,
    label = "NCN + O <=> CN + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 883,
    label = "NCN + OH <=> HCN + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 884,
    label = "NCN + O2 <=> NO + NCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+09, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 885,
    label = "CH3CN + H <=> HCN + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+07, 'cm^3/(mol*s)'), n=2, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 886,
    label = "CH3CN + H <=> CH2CN + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+07, 'cm^3/(mol*s)'), n=2, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 887,
    label = "CH3CN + O <=> NCO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(15000, 'cm^3/(mol*s)'), n=2.64, Ea=(4980, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 888,
    label = "CH3CN + OH <=> CH2CN + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+07, 'cm^3/(mol*s)'), n=2, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 889,
    label = "CH2CN + O <=> CH2O + CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 890,
    label = "H + H <=> H2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(7e+17, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[H][H]': 0, 'O': 0, 'N#N': 0},
    ),
)

entry(
    index = 891,
    label = "H + O <=> OH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(6.2e+16, 'cm^6/(mol^2*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'O': 5},
    ),
)

entry(
    index = 892,
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
    index = 893,
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
    index = 894,
    label = "OH + H <=> H2O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.5e+22, 'cm^6/(mol^2*s)'), n=-2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[H][H]': 0.73, 'O': 12, '[Ar]': 0.38},
    ),
)

entry(
    index = 895,
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
    index = 896,
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
    index = 897,
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
        efficiencies = {},
    ),
)

entry(
    index = 898,
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
        efficiencies = {},
    ),
)

entry(
    index = 899,
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
    index = 900,
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
    index = 901,
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
        efficiencies = {},
    ),
)

entry(
    index = 902,
    label = "CH2(S) <=> CH2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[H]': 0, 'O': 0, 'N#N': 0, '[Ar]': 0},
    ),
)

entry(
    index = 903,
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
        efficiencies = {},
    ),
)

entry(
    index = 904,
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
    index = 905,
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
        efficiencies = {},
    ),
)

entry(
    index = 906,
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
        efficiencies = {},
    ),
)

entry(
    index = 907,
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
    index = 908,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.4e+09, 'cm^3/(mol*s)'),
            n = 1.463,
            Ea = (1355, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2e+39, 'cm^6/(mol^2*s)'),
            n = -6.642,
            Ea = (5769, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -0.569,
        T3 = (299, 'K'),
        T1 = (9147, 'K'),
        T2 = (152.4, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 909,
    label = "C2H5 + H <=> C2H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.2e+17, 'cm^3/(mol*s)'),
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
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, 'N#N': 1, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 910,
    label = "C2H5 + O2 <=> CH3CH2OO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2e+10, 'cm^3/(mol*s)'), n=0.98, Ea=(-64, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (8.486e+29, 'cm^6/(mol^2*s)'),
            n = -4.29,
            Ea = (220, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.897,
        T3 = (1e-30, 'K'),
        T1 = (601, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 911,
    label = "C2H3 + H <=> C2H4",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.9e+13, 'cm^3/(mol*s)'), n=0.2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2.1e+24, 'cm^6/(mol^2*s)'), n=-1.3, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.5,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 912,
    label = "C2H4 <=> H2CC + H2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8e+12, 's^-1'), n=0.44, Ea=(88800, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (7e+50, 'cm^3/(mol*s)'),
            n = -9.31,
            Ea = (99900, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.735,
        T3 = (180, 'K'),
        T1 = (1035, 'K'),
        T2 = (5417, 'K'),
        efficiencies = {'O': 6, '[Ar]': 0.7},
    ),
)

entry(
    index = 913,
    label = "C2H2 + H <=> C2H3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.7e+10, 'cm^3/(mol*s)'),
            n = 1.266,
            Ea = (2709, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.3e+31, 'cm^6/(mol^2*s)'),
            n = -4.664,
            Ea = (3780, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7878,
        T3 = (-10212, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'[H][H]': 2, '[C]=O': 2, 'O=C=O': 3, 'O': 5},
    ),
)

entry(
    index = 914,
    label = "C2H2 <=> C2H + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (9.1e+30, 'cm^3/(mol*s)'),
            n = -3.7,
            Ea = (127138, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[H][H]': 2, '[C]=O': 2, 'O=C=O': 3, 'O': 5},
    ),
)

entry(
    index = 915,
    label = "CH3CH2OH <=> CH2OH + CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.9e+23, 's^-1'), n=-1.68, Ea=(91163, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.88e+85, 'cm^3/(mol*s)'),
            n = -18.9,
            Ea = (109914, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (200, 'K'),
        T1 = (890, 'K'),
        T2 = (4600, 'K'),
        efficiencies = {'[H][H]': 2, '[C]=O': 2, 'O=C=O': 3, 'O': 5},
    ),
)

entry(
    index = 916,
    label = "CH3CH2OH <=> C2H5 + OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.3e+23, 's^-1'), n=-1.54, Ea=(96005, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.25e+85, 'cm^3/(mol*s)'),
            n = -18.81,
            Ea = (114930, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (300, 'K'),
        T1 = (900, 'K'),
        T2 = (5000, 'K'),
        efficiencies = {'[H][H]': 2, '[C]=O': 2, 'O=C=O': 3, 'O': 5},
    ),
)

entry(
    index = 917,
    label = "CH3CH2OH <=> C2H4 + H2O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.8e+13, 's^-1'), n=0.09, Ea=(66136, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.57e+83, 'cm^3/(mol*s)'),
            n = -18.85,
            Ea = (86452, 'cal/mol'),
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
    index = 918,
    label = "CH3CH2OH <=> CH3CHO + H2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(7.2e+11, 's^-1'), n=0.095, Ea=(91007, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.46e+87, 'cm^3/(mol*s)'),
            n = -19.42,
            Ea = (115586, 'cal/mol'),
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
    index = 919,
    label = "CH2CH2OH + H <=> CH3CH2OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.2e+17, 'cm^3/(mol*s)'),
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
        efficiencies = {},
    ),
)

entry(
    index = 920,
    label = "CH2CH2OH + O2 <=> HOCH2CH2OO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2e+10, 'cm^3/(mol*s)'), n=0.98, Ea=(-64, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (8.486e+29, 'cm^6/(mol^2*s)'),
            n = -4.29,
            Ea = (220, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.897,
        T3 = (1e-30, 'K'),
        T1 = (601, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 921,
    label = "CH3CH2O <=> CH3 + CH2O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.1e+13, 's^-1'), n=0, Ea=(16790, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2e+16, 'cm^3/(mol*s)'), n=0, Ea=(13970, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.78,
        T3 = (1e-30, 'K'),
        T1 = (1235, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 922,
    label = "CH3CHO <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.3e+22, 's^-1'), n=-1.88, Ea=(85480, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.22e+76, 'cm^3/(mol*s)'),
            n = -11.81,
            Ea = (95040, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.23,
        T3 = (80, 'K'),
        T1 = (7000, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 923,
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
        efficiencies = {'O': 6, 'N#N': 1, '[Ar]': 0.7},
    ),
)

entry(
    index = 924,
    label = "CH + CO <=> HCCO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.7e+28, 'cm^6/(mol^2*s)'),
            n = -3.74,
            Ea = (1936, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5757,
        T3 = (237, 'K'),
        T1 = (1652, 'K'),
        T2 = (5069, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, 'N#N': 1, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 925,
    label = "CH3CH2OO <=> C2H4 + HO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(71000, 's^-1'), n=2.32, Ea=(27955, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (8.311e+21, 'cm^3/(mol*s)'),
            n = -0.651,
            Ea = (22890, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (1e-30, 'K'),
        T1 = (106, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 926,
    label = "CH2CHCH2 + H <=> C3H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.3e+60, 'cm^6/(mol^2*s)'),
            n = -12,
            Ea = (5970, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.02,
        T3 = (1097, 'K'),
        T1 = (1097, 'K'),
        T2 = (6860, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 927,
    label = "C2H3 + CH3 <=> C3H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.3e+58, 'cm^6/(mol^2*s)'),
            n = -11.94,
            Ea = (9770, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.175,
        T3 = (1341, 'K'),
        T1 = (60000, 'K'),
        T2 = (10140, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, 'C=C': 3, 'C#C': 3, '[Ar]': 0.7},
    ),
)

entry(
    index = 928,
    label = "H2CCCH2 + H <=> CH3CCH2",
    degeneracy = 1,
    duplicate = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.1e+34, 'cm^6/(mol^2*s)'),
            n = -5,
            Ea = (4450, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7086,
        T3 = (134, 'K'),
        T1 = (1784, 'K'),
        T2 = (5740, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 929,
    label = "H3CCCH + H <=> CH3CCH2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (8.45e+39, 'cm^6/(mol^2*s)'),
            n = -7.27,
            Ea = (6577, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7086,
        T3 = (134, 'K'),
        T1 = (1784, 'K'),
        T2 = (5740, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 930,
    label = "H2CCCH2 + H <=> CH2CHCH2",
    degeneracy = 1,
    duplicate = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.2e+11, 'cm^3/(mol*s)'),
            n = 0.69,
            Ea = (3007, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (5.56e+33, 'cm^6/(mol^2*s)'),
            n = -5,
            Ea = (4448, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7086,
        T3 = (134, 'K'),
        T1 = (1784, 'K'),
        T2 = (5740, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 931,
    label = "H2CCCH + H <=> H2CCCH2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+17, 'cm^3/(mol*s)'), n=-0.82, Ea=(315, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.5e+55, 'cm^6/(mol^2*s)'),
            n = -4.88,
            Ea = (2225, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7086,
        T3 = (134, 'K'),
        T1 = (1784, 'K'),
        T2 = (5740, 'K'),
        efficiencies = {'[H][H]': 2, '[C]=O': 2, 'O=C=O': 3, 'O': 8.6},
    ),
)

entry(
    index = 932,
    label = "H2CCCH + H <=> H3CCCH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+17, 'cm^3/(mol*s)'), n=-0.82, Ea=(315, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.5e+55, 'cm^6/(mol^2*s)'),
            n = -4.88,
            Ea = (2225, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7086,
        T3 = (134, 'K'),
        T1 = (1784, 'K'),
        T2 = (5740, 'K'),
        efficiencies = {'[H][H]': 2, '[C]=O': 2, 'O=C=O': 3, 'O': 8.6},
    ),
)

entry(
    index = 933,
    label = "NO + H <=> HNO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.5e+15, 'cm^3/(mol*s)'), n=-0.41, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.4e+14, 'cm^6/(mol^2*s)'),
            n = 0.206,
            Ea = (-1550, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.82,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'N#N': 1.6},
    ),
)

entry(
    index = 934,
    label = "NO + O <=> NO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.3e+15, 'cm^3/(mol*s)'), n=-0.75, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.72e+24, 'cm^6/(mol^2*s)'),
            n = -2.87,
            Ea = (1550, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.82,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'[Ar]': 0},
    ),
)

entry(
    index = 935,
    label = "NO + OH <=> HONO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.1e+14, 'cm^3/(mol*s)'), n=-0.3, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.392e+23, 'cm^6/(mol^2*s)'),
            n = -2.5,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.75,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 936,
    label = "NO2 + O <=> NO3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.5e+12, 'cm^3/(mol*s)'), n=0.24, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2.5e+20, 'cm^6/(mol^2*s)'), n=-1.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.71,
        T3 = (1e-30, 'K'),
        T1 = (1700, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 937,
    label = "NO2 + OH <=> HONO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2.938e+25, 'cm^6/(mol^2*s)'), n=-3, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.4,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 938,
    label = "HNO2 <=> HONO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.5e+14, 's^-1'), n=0, Ea=(32300, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(3.1e+18, 'cm^3/(mol*s)'), n=0, Ea=(31500, 'cal/mol'), T0=(1, 'K')),
        alpha = 1.149,
        T3 = (1e-30, 'K'),
        T1 = (3125, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 939,
    label = "N2O <=> N2 + O",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1.3e+12, 's^-1'), n=0, Ea=(62570, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(4e+14, 'cm^3/(mol*s)'), n=0, Ea=(56600, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'O=C=O': 3, '[O][O]': 1.4, 'O': 12, 'N#N': 1.7},
    ),
)

entry(
    index = 940,
    label = "N2H2 <=> NNH + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.9e+27, 'cm^3/(mol*s)'),
            n = -3.05,
            Ea = (66107, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O': 7},
    ),
)

entry(
    index = 941,
    label = "H2NO <=> HNO + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (2.8e+24, 'cm^3/(mol*s)'),
            n = -2.83,
            Ea = (64915, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O': 10},
    ),
)

entry(
    index = 942,
    label = "H2NO <=> HNOH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.1e+29, 'cm^3/(mol*s)'), n=-4, Ea=(44000, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'O': 10},
    ),
)

entry(
    index = 943,
    label = "HNOH <=> HNO + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (2e+24, 'cm^3/(mol*s)'),
            n = -2.84,
            Ea = (58934, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O': 10},
    ),
)

entry(
    index = 944,
    label = "HCN <=> H + CN",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (3.4e+35, 'cm^3/(mol*s)'),
            n = -5.13,
            Ea = (133000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[O][O]': 1.5, 'O': 10, 'N#N': 0},
    ),
)

entry(
    index = 945,
    label = "HCN <=> HNC",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.6e+26, 'cm^3/(mol*s)'),
            n = -3.23,
            Ea = (54600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 2, 'O': 7, '[Ar]': 0.7},
    ),
)

entry(
    index = 946,
    label = "HNCO <=> CO + NH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.1e+16, 'cm^3/(mol*s)'), n=0, Ea=(86000, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'N#N': 1.5},
    ),
)

entry(
    index = 947,
    label = "NCO <=> N + CO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.2e+14, 'cm^3/(mol*s)'), n=0, Ea=(54050, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'N#N': 1.5},
    ),
)

entry(
    index = 948,
    label = "CH3 + NO <=> CH3NO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(192, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.5e+16, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (-2841, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 5,
        T3 = (1e-30, 'K'),
        T1 = (120, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 949,
    label = "CH3O + NO <=> CH3ONO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6e+14, 'cm^3/(mol*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (8.14e+25, 'cm^6/(mol^2*s)'),
            n = -2.8,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (1e-30, 'K'),
        T1 = (900, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 950,
    label = "CH3O + NO2 <=> CH3ONO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.2e+15, 'cm^3/(mol*s)'), n=-0.88, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.911e+23, 'cm^6/(mol^2*s)'),
            n = -1.74,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.6,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 951,
    label = "CH3CH2O + NO <=> CH3CH2ONO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(-143, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(9.43e+19, 'cm^6/(mol^2*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.6,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 952,
    label = "CH3CH2O + NO2 <=> CH3CH2ONO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.1e+15, 'cm^3/(mol*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(5.88e+30, 'cm^6/(mol^2*s)'), n=-4, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.6,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 953,
    label = "CH3NO2 <=> CH3 + NO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.8e+16, 's^-1'), n=0, Ea=(58500, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.259e+17, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (42000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.183,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 954,
    label = "C2H5NO2 <=> C2H5 + NO2",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(2e+15, 's^-1'), n=0, Ea=(54000, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(1e+18, 'cm^3/(mol*s)'), n=0, Ea=(36000, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

