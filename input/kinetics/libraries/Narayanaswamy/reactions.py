#!/usr/bin/env python
# encoding: utf-8

name = "Narayanaswamy"
shortDesc = u""
longDesc = u"""
From: Narayanaswamy, K.; Blanquart, G.; Pitsch, H., 
A consistent chemical mechanism for oxidation of substituted aromatic species. Combust. Flame 2010, 157, 1879-1898. 
"""
entry(
    index = 1,
    label = "H + O2 <=> O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.64e+16, 'cm^3/(mol*s)'),
        n = -0.67,
        Ea = (17041.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2,
    label = "O + H2 <=> H + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (45900, 'cm^3/(mol*s)'),
        n = 2.7,
        Ea = (6259.56, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3,
    label = "OH + H2 <=> H + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e+08, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (3429.73, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 4,
    label = "OH + OH <=> O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (39700, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (-2110.42, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 5,
    label = "H + H <=> H2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.78e+18, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 0, 'CC': 3, 'O': 0, '[H][H]': 0, '[Ar]': 0.63},
    ),
)

entry(
    index = 6,
    label = "H + H + H2 <=> H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+16, 'cm^6/(mol^2*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "H + H + H2O <=> H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.62e+19, 'cm^6/(mol^2*s)'),
        n = -1.25,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 8,
    label = "H + H + CO2 <=> H2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.5e+20, 'cm^6/(mol^2*s)'), n=-2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 9,
    label = "H + OH <=> H2O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.4e+22, 'cm^6/(mol^2*s)'), n=-2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 6.3, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.38},
    ),
)

entry(
    index = 10,
    label = "H + O <=> OH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(9.43e+18, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 11,
    label = "O + O <=> O2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.2e+17, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 15.4, '[H][H]': 2.4, '[C-]#[O+]': 1.75, '[Ar]': 0.83},
    ),
)

entry(
    index = 12,
    label = "H + O2 <=> HO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.12e+12, 'cm^3/(mol*s)'), n=0.44, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.33e+19, 'cm^6/(mol^2*s)'),
            n = -1.4,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (0, 'K'),
        T1 = (1e+10, 'K'),
        efficiencies = {'O=C=O': 2.18, 'O': 11.89, '[H][H]': 0.75, '[O][O]': 0.85, '[C-]#[O+]': 1.09, '[Ar]': 0.4},
    ),
)

entry(
    index = 13,
    label = "H2 + O2 <=> HO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (592000, 'cm^3/(mol*s)'),
        n = 2.43,
        Ea = (53501.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 14,
    label = "OH + OH <=> H2O2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.11e+14, 'cm^3/(mol*s)'), n=-0.37, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.01e+17, 'cm^6/(mol^2*s)'),
            n = -0.58,
            Ea = (-2292.07, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7346,
        T3 = (94, 'K'),
        T1 = (1756, 'K'),
        T2 = (5182, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 15,
    label = "HO2 + H <=> O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.97e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (671.61, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 16,
    label = "HO2 + H <=> OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.49e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (635.76, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 17,
    label = "HO2 + O <=> OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 18,
    label = "HO2 + OH <=> H2O + O2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (2.38e+13, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (-499.52, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(1e+16, 'cm^3/(mol*s)'), n=0, Ea=(17330.3, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 19,
    label = "HO2 + HO2 <=> O2 + H2O2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.3e+11, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (-1630.02, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.66e+14, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (12000.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 20,
    label = "H2O2 + H <=> HO2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.05e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (5200.76, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 21,
    label = "H2O2 + H <=> H2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3969.89, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 22,
    label = "H2O2 + O <=> HO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.63e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (3969.89, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 23,
    label = "H2O2 + OH <=> HO2 + H2O",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(427.82, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (2.67e+41, 'cm^3/(mol*s)'),
                n = -7,
                Ea = (37600.4, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 24,
    label = "CO + O <=> CO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.36e+10, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (2385.28, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.17e+24, 'cm^6/(mol^2*s)'),
            n = -2.79,
            Ea = (4192.16, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (1, 'K'),
        T1 = (1e+07, 'K'),
        T2 = (1e+07, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 25,
    label = "CO + OH <=> CO2 + H",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (8e+11, 'cm^3/(mol*s)'),
                n = 0.14,
                Ea = (7351.82, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.78e+10, 'cm^3/(mol*s)'),
                n = 0.03,
                Ea = (-16.73, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 26,
    label = "CO + O2 <=> CO2 + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.12e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47700.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 27,
    label = "CO + HO2 <=> CO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (22999.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 28,
    label = "HCO + H <=> CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 29,
    label = "HCO + O <=> CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 30,
    label = "HCO + O <=> CO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 31,
    label = "HCO + OH <=> CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.02e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 32,
    label = "HCO <=> CO + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.87e+17, 'cm^3/(mol*s)'),
            n = -1,
            Ea = (17000.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 0, '[H][H]': 2, '[C-]#[O+]': 1.75},
    ),
)

entry(
    index = 33,
    label = "HCO + H2O <=> CO + H + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.24e+18, 'cm^3/(mol*s)'),
        n = -1,
        Ea = (17000.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 34,
    label = "HCO + O2 <=> CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+10, 'cm^3/(mol*s)'),
        n = 0.81,
        Ea = (-726.58, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 35,
    label = "C + OH <=> CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 36,
    label = "C + O2 <=> CO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(576, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 37,
    label = "CH + H <=> C + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.65e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 38,
    label = "CH + O <=> CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 39,
    label = "CH + OH <=> HCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 40,
    label = "CH + H2 <=> T-CH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3109.46, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 41,
    label = "CH + H2 <=> CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.97e+12, 'cm^3/(mol*s)'),
            n = 0.43,
            Ea = (-370.46, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.82e+25, 'cm^6/(mol^2*s)'),
            n = -2.8,
            Ea = (590.34, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.578,
        T3 = (122, 'K'),
        T1 = (2535, 'K'),
        T2 = (9365, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 42,
    label = "CH + H2O <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.71e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-755.26, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 43,
    label = "CH + O2 <=> HCO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.71e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 44,
    label = "CH + CO <=> HCCO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.69e+28, 'cm^6/(mol^2*s)'),
            n = -3.74,
            Ea = (1935.95, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5757,
        T3 = (237, 'K'),
        T1 = (1652, 'K'),
        T2 = (5069, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 45,
    label = "CH + CO2 <=> HCO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.9e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15791.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 46,
    label = "CO + H2 <=> CH2O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4.3e+07, 'cm^3/(mol*s)'),
            n = 1.5,
            Ea = (79600.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (5.07e+27, 'cm^6/(mol^2*s)'),
            n = -3.42,
            Ea = (84349.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.932,
        T3 = (197, 'K'),
        T1 = (1540, 'K'),
        T2 = (10300, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 47,
    label = "HCO + H <=> CH2O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.09e+12, 'cm^3/(mol*s)'),
            n = 0.48,
            Ea = (-260.52, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.47e+24, 'cm^6/(mol^2*s)'),
            n = -2.57,
            Ea = (425.43, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7824,
        T3 = (271, 'K'),
        T1 = (2755, 'K'),
        T2 = (6570, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 48,
    label = "T-CH2 + H <=> CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.04e+26, 'cm^6/(mol^2*s)'),
            n = -2.76,
            Ea = (1598.95, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.562,
        T3 = (91, 'K'),
        T1 = (5836, 'K'),
        T2 = (8552, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 49,
    label = "T-CH2 + O <=> HCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 50,
    label = "T-CH2 + OH <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 51,
    label = "T-CH2 + OH <=> CH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.13e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (2999.52, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 52,
    label = "T-CH2 + H2 <=> H + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(500000, 'cm^3/(mol*s)'), n=2, Ea=(7229.92, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 53,
    label = "T-CH2 + O2 => CO2 + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1500.96, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 54,
    label = "T-CH2 + O2 <=> CH2O + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1500.96, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 55,
    label = "T-CH2 + O2 => OH + H + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(1500.96, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 56,
    label = "T-CH2 + HO2 <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 57,
    label = "T-CH2 + C <=> C2H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 58,
    label = "T-CH2 + CO <=> CH2CO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (8.1e+11, 'cm^3/(mol*s)'),
            n = 0.5,
            Ea = (4510.04, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.69e+33, 'cm^6/(mol^2*s)'),
            n = -5.11,
            Ea = (7096.08, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5907,
        T3 = (275, 'K'),
        T1 = (1226, 'K'),
        T2 = (5185, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 59,
    label = "T-CH2 + CH <=> C2H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 60,
    label = "T-CH2 + T-CH2 <=> C2H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+15, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11943.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 61,
    label = "T-CH2 + T-CH2 => C2H2 + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(10989.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 62,
    label = "S-CH2 + N2 <=> T-CH2 + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(599.9, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 63,
    label = "S-CH2 + AR <=> T-CH2 + AR",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(599.9, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 64,
    label = "S-CH2 + H <=> CH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 65,
    label = "S-CH2 + O <=> CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 66,
    label = "S-CH2 + O <=> HCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 67,
    label = "S-CH2 + OH <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 68,
    label = "S-CH2 + H2 <=> CH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 69,
    label = "S-CH2 + O2 <=> H + OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 70,
    label = "S-CH2 + O2 <=> CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 71,
    label = "S-CH2 + H2O <=> CH3OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4.82e+17, 'cm^3/(mol*s)'),
            n = -1.16,
            Ea = (1144.84, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.88e+38, 'cm^6/(mol^2*s)'),
            n = -6.36,
            Ea = (5040.63, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.6027,
        T3 = (208, 'K'),
        T1 = (3922, 'K'),
        T2 = (10180, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 72,
    label = "S-CH2 + H2O <=> T-CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 73,
    label = "S-CH2 + H2O => H2 + CH2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (6.82e+10, 'cm^3/(mol*s)'),
        n = 0.25,
        Ea = (-934.51, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 74,
    label = "S-CH2 + CO <=> T-CH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 75,
    label = "S-CH2 + CO2 <=> T-CH2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 76,
    label = "S-CH2 + CO2 <=> CH2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 77,
    label = "CH2O + H <=> CH2OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.4e+11, 'cm^3/(mol*s)'),
            n = 0.45,
            Ea = (3599.43, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.27e+32, 'cm^6/(mol^2*s)'),
            n = -4.82,
            Ea = (6529.64, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7187,
        T3 = (103, 'K'),
        T1 = (1291, 'K'),
        T2 = (4160, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 78,
    label = "CH2O + H <=> CH3O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.4e+11, 'cm^3/(mol*s)'),
            n = 0.45,
            Ea = (2600.38, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.2e+30, 'cm^6/(mol^2*s)'),
            n = -4.8,
            Ea = (5559.27, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.758,
        T3 = (94, 'K'),
        T1 = (1555, 'K'),
        T2 = (4200, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 79,
    label = "CH2O + H <=> HCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.74e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (2741.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 80,
    label = "CH2O + O <=> HCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3539.67, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 81,
    label = "CH2O + OH <=> HCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.43e+09, 'cm^3/(mol*s)'),
        n = 1.18,
        Ea = (-446.94, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 82,
    label = "CH2O + O2 <=> HCO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(40000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 83,
    label = "CH2O + HO2 <=> HCO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.6e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (12000.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 84,
    label = "CH2O + CH <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.46e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-516.25, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 85,
    label = "CH3 + H <=> CH4",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.92e+13, 'cm^3/(mol*s)'), n=0.18, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.47e+38, 'cm^6/(mol^2*s)'),
            n = -6.3,
            Ea = (5074.09, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.783,
        T3 = (74, 'K'),
        T1 = (2941, 'K'),
        T2 = (6964, 'K'),
        efficiencies = {'C': 3, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 86,
    label = "CH3 + O <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.06e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 87,
    label = "CH3 + O => H + H2 + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.37e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 88,
    label = "CH3 + OH <=> CH3OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2.79e+18, 'cm^3/(mol*s)'),
            n = -1.43,
            Ea = (1331.26, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4e+36, 'cm^6/(mol^2*s)'),
            n = -5.92,
            Ea = (3140.54, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.412,
        T3 = (195, 'K'),
        T1 = (5900, 'K'),
        T2 = (6394, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 89,
    label = "CH3 + OH <=> T-CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.6e+07, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (5420.65, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 90,
    label = "CH3 + OH => H2 + CH2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8e+09, 'cm^3/(mol*s)'), n=0, Ea=(-1754.3, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 91,
    label = "CH3 + OH <=> S-CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.44e+17, 'cm^3/(mol*s)'),
        n = -1.34,
        Ea = (1417.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 92,
    label = "CH3 + O2 <=> CH3O + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.38e+13, 'cm^3/(mol*s)'), n=0, Ea=(30521, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 93,
    label = "CH3 + O2 <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.87e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13840.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 94,
    label = "CH3 + O2 <=> CH3O2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.01e+08, 'cm^3/(mol*s)'), n=1.63, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.82e+31, 'cm^6/(mol^2*s)'),
            n = -4.89,
            Ea = (3432.12, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.045,
        T3 = (880.1, 'K'),
        T1 = (2.5e+09, 'K'),
        T2 = (1.786e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 95,
    label = "CH3O2 + CH3 <=> CH3O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(-1199.81, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 96,
    label = "CH3O2 + CH3O2 => CH3O + CH3O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1859.46, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 97,
    label = "CH3O2 + HO2 => CH3O + OH + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.47e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1570.27, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 98,
    label = "CH3O2 + CH2O => CH3O + OH + HCO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.99e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11670.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 99,
    label = "CH3 + HO2 <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 100,
    label = "CH3 + HO2 <=> CH4 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.61e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 101,
    label = "CH3 + H2O2 <=> CH4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24500, 'cm^3/(mol*s)'),
        n = 2.47,
        Ea = (5179.25, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 102,
    label = "CH3 + C <=> C2H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 103,
    label = "CH3 + CH <=> C2H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 104,
    label = "CH3 + HCO <=> CH4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.65e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 105,
    label = "CH3 + CH2O <=> CH4 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3320, 'cm^3/(mol*s)'),
        n = 2.81,
        Ea = (5860.42, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 106,
    label = "CH3 + T-CH2 <=> C2H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 107,
    label = "CH3 + S-CH2 <=> C2H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-571.22, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 108,
    label = "CH3 + CH3 <=> C2H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.84e+12, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (10599.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 109,
    label = "CH3O + H <=> CH3OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2.43e+12, 'cm^3/(mol*s)'),
            n = 0.52,
            Ea = (50.19, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.66e+41, 'cm^6/(mol^2*s)'),
            n = -7.44,
            Ea = (14079.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7,
        T3 = (100, 'K'),
        T1 = (90000, 'K'),
        T2 = (10000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 110,
    label = "CH3O + H <=> CH2OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.15e+07, 'cm^3/(mol*s)'),
        n = 1.63,
        Ea = (1924, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 111,
    label = "CH3O + H <=> CH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 112,
    label = "CH3O + H <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+12, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (-109.94, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 113,
    label = "CH3O + H <=> S-CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.62e+14, 'cm^3/(mol*s)'),
        n = -0.23,
        Ea = (1070.75, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 114,
    label = "CH3O + O <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 115,
    label = "CH3O + OH <=> CH2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 116,
    label = "CH3O + O2 <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.28e-13, 'cm^3/(mol*s)'),
        n = 7.6,
        Ea = (-3530.11, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 117,
    label = "CH2OH + H <=> CH3OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.06e+12, 'cm^3/(mol*s)'),
            n = 0.5,
            Ea = (86.04, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.36e+31, 'cm^6/(mol^2*s)'),
            n = -4.65,
            Ea = (5081.26, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.6,
        T3 = (100, 'K'),
        T1 = (9000, 'K'),
        T2 = (10000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 118,
    label = "CH2OH + H <=> CH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 119,
    label = "CH2OH + H <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.65e+11, 'cm^3/(mol*s)'),
        n = 0.65,
        Ea = (-284.42, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 120,
    label = "CH2OH + H <=> S-CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.28e+13, 'cm^3/(mol*s)'),
        n = -0.09,
        Ea = (609.46, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 121,
    label = "CH2OH + O <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 122,
    label = "CH2OH + OH <=> CH2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 123,
    label = "CH2OH + O2 <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(901.05, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 124,
    label = "CH4 + H <=> CH3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.6e+08, 'cm^3/(mol*s)'),
        n = 1.62,
        Ea = (10841.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 125,
    label = "CH4 + O <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (8599.43, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 126,
    label = "CH4 + OH <=> CH3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+08, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (3119.02, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 127,
    label = "CH4 + CH <=> C2H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 128,
    label = "CH4 + T-CH2 <=> CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.46e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (8269.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 129,
    label = "CH4 + S-CH2 <=> CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-571.22, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 130,
    label = "CH3OH + H <=> CH2OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+07, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (4870.94, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 131,
    label = "CH3OH + H <=> CH3O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+06, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (4870.94, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 132,
    label = "CH3OH + O <=> CH2OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (388000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (3099.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 133,
    label = "CH3OH + O <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(130000, 'cm^3/(mol*s)'), n=2.5, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 134,
    label = "CH3OH + OH <=> CH2OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.44e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-841.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 135,
    label = "CH3OH + OH <=> CH3O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1500.96, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 136,
    label = "CH3OH + CH3 <=> CH2OH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+07, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (9940.25, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 137,
    label = "CH3OH + CH3 <=> CH3O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+07, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (9940.25, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 138,
    label = "C2H + H <=> C2H2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+17, 'cm^3/(mol*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.6e+33, 'cm^6/(mol^2*s)'),
            n = -4.8,
            Ea = (1900.1, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.6464,
        T3 = (132, 'K'),
        T1 = (1315, 'K'),
        T2 = (5566, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 139,
    label = "C2H + O <=> CH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 140,
    label = "C2H + OH <=> H + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 141,
    label = "C2H + O2 <=> HCO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(-755.26, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 142,
    label = "C2H + H2 <=> C2H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.31e+06, 'cm^3/(mol*s)'),
        n = 2.26,
        Ea = (901.05, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 143,
    label = "HCCO + H <=> S-CH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 144,
    label = "HCCO + O <=> H + CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 145,
    label = "HCCO + O2 <=> OH + CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.2e+10, 'cm^3/(mol*s)'), n=0, Ea=(853.25, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 146,
    label = "HCCO + CH <=> C2H2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 147,
    label = "HCCO + T-CH2 <=> C2H3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 148,
    label = "HCCO + HCCO <=> C2H2 + CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 149,
    label = "C2H2 + H <=> C2H3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.71e+10, 'cm^3/(mol*s)'),
            n = 1.27,
            Ea = (2707.93, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.34e+31, 'cm^6/(mol^2*s)'),
            n = -4.66,
            Ea = (3781.07, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.2122,
        T3 = (1, 'K'),
        T1 = (-10212, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 150,
    label = "C2H2 + O <=> HCCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.1e+06, 'cm^3/(mol*s)'), n=2, Ea=(1900.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 151,
    label = "C2H2 + O <=> T-CH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.25e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1900.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 152,
    label = "C2H + OH <=> C2H2 + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 153,
    label = "C2H2 + OH <=> C2H + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.63e+06, 'cm^3/(mol*s)'),
        n = 2.14,
        Ea = (17060.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 154,
    label = "C2H2 + OH <=> HCCOH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (12712.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 155,
    label = "C2H2 + OH <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.53e+06, 'cm^3/(mol*s)'),
        n = 1.55,
        Ea = (2105.64, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 156,
    label = "C2H2 + OH <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.28e+09, 'cm^3/(mol*s)'),
        n = 0.73,
        Ea = (2578.87, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 157,
    label = "CH2CO + H <=> HCCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(7999.52, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 158,
    label = "CH2CO + H <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+09, 'cm^3/(mol*s)'),
        n = 1.38,
        Ea = (614.24, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 159,
    label = "CH2CO + O <=> HCCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(7999.52, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 160,
    label = "CH2CO + O <=> T-CH2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1350.38, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 161,
    label = "CH2CO + OH <=> HCCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2000.48, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 162,
    label = "HCCOH + H <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 163,
    label = "C2H3 + H <=> C2H4",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (6.08e+12, 'cm^3/(mol*s)'),
            n = 0.27,
            Ea = (279.64, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.4e+30, 'cm^6/(mol^2*s)'),
            n = -3.86,
            Ea = (3319.79, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.782,
        T3 = (207.5, 'K'),
        T1 = (2663, 'K'),
        T2 = (6095, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 164,
    label = "C2H3 + H <=> C2H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 165,
    label = "C2H3 + O <=> CH2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.03e+13, 'cm^3/(mol*s)'),
        n = 0.21,
        Ea = (-427.82, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 166,
    label = "C2H3 + OH <=> C2H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 167,
    label = "C2H3 + O2 <=> C2H2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.34e+06, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-384.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 168,
    label = "C2H3 + O2 <=> CH2CHO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.03e+11, 'cm^3/(mol*s)'),
        n = 0.29,
        Ea = (11.95, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 169,
    label = "C2H3 + O2 <=> HCO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.58e+16, 'cm^3/(mol*s)'),
        n = -1.39,
        Ea = (1015.77, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 170,
    label = "CH2CHO <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.32e+34, 's^-1'), n=-6.57, Ea=(49457.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 171,
    label = "CH2CHO <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.51e+34, 's^-1'), n=-6.87, Ea=(47194.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 172,
    label = "CH2CHO + O <=> CH2O + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.17e+13, 'cm^3/(mol*s)'),
        n = 0.03,
        Ea = (-394.36, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 173,
    label = "CH2CHO + O2 => OH + CO + CH2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.81e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 174,
    label = "CH2CHO + O2 => OH + HCO + HCO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.35e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 175,
    label = "CH2CHO + H <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 176,
    label = "CH2CHO + H <=> CH2CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 177,
    label = "CH2CHO + OH <=> H2O + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 178,
    label = "CH2CHO + OH <=> HCO + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 179,
    label = "CH3 + HCO <=> CH3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 180,
    label = "CH3CHO + O <=> CH2CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1809.27, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 181,
    label = "CH3CHO + H <=> CH2CHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.05e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2404.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 182,
    label = "CH3CHO + H => CH3 + CO + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.05e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2404.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 183,
    label = "CH3CHO + O => CH3 + CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.92e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1809.27, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 184,
    label = "CH3CHO + O2 => CH3 + CO + HO2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (39149.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 185,
    label = "CH3CHO + OH => CH3 + CO + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.34e+10, 'cm^3/(mol*s)'),
        n = 0.73,
        Ea = (-1113.77, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 186,
    label = "CH3CHO + HO2 => CH3 + CO + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11924, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 187,
    label = "CH3CHO + CH3 => CH3 + CO + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.72e+06, 'cm^3/(mol*s)'),
        n = 1.77,
        Ea = (5920.17, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 188,
    label = "C2H4 <=> H2C2 + H2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8e+12, 's^-1'), n=0.44, Ea=(88800.2, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (7e+50, 'cm^3/(mol*s)'),
            n = -9.31,
            Ea = (99899.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.735,
        T3 = (180, 'K'),
        T1 = (1035, 'K'),
        T2 = (5417, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 189,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.37e+09, 'cm^3/(mol*s)'),
            n = 1.46,
            Ea = (1355.16, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.03e+39, 'cm^6/(mol^2*s)'),
            n = -6.64,
            Ea = (5769.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -0.569,
        T3 = (299, 'K'),
        T1 = (-9147, 'K'),
        T2 = (152.4, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 190,
    label = "C2H4 + H <=> C2H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (127000, 'cm^3/(mol*s)'),
        n = 2.75,
        Ea = (11649.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 191,
    label = "C2H4 + O <=> CH2CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.66e+09, 'cm^3/(mol*s)'),
        n = 0.88,
        Ea = (1140.06, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 192,
    label = "C2H4 + O <=> T-CH2 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (71500, 'cm^3/(mol*s)'),
        n = 2.47,
        Ea = (929.73, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 193,
    label = "C2H4 + O <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.89e+08, 'cm^3/(mol*s)'),
        n = 1.36,
        Ea = (886.71, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 194,
    label = "C2H4 + OH <=> C2H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.131, 'cm^3/(mol*s)'),
        n = 4.2,
        Ea = (-860.42, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 195,
    label = "C2H4 + OH <=> C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.75e+36, 'cm^3/(mol*s)'),
        n = -7.8,
        Ea = (7060.23, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 196,
    label = "C2H4 + CH3 <=> C2H3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(227000, 'cm^3/(mol*s)'), n=2, Ea=(9199.33, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 197,
    label = "C2H4 + CH3 <=> N-C3H7",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2.55e+06, 'cm^3/(mol*s)'),
            n = 1.6,
            Ea = (5700.29, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3e+63, 'cm^6/(mol^2*s)'),
            n = -14.6,
            Ea = (18169.2, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.1894,
        T3 = (277, 'K'),
        T1 = (8748, 'K'),
        T2 = (7891, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 198,
    label = "C2H5 + H <=> C2H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.21e+17, 'cm^3/(mol*s)'),
            n = -0.99,
            Ea = (1579.83, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.99e+41, 'cm^6/(mol^2*s)'),
            n = -7.08,
            Ea = (6684.99, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.8422,
        T3 = (125, 'K'),
        T1 = (2219, 'K'),
        T2 = (6882, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 199,
    label = "C2H5 + H <=> C2H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 200,
    label = "C2H5 + CH3 <=> C2H4 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11800, 'cm^3/(mol*s)'),
        n = 2.45,
        Ea = (2920.65, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 201,
    label = "C2H5 + O <=> C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.17e+13, 'cm^3/(mol*s)'),
        n = 0.03,
        Ea = (-394.36, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 202,
    label = "C2H5O <=> CH3 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.32e+20, 's^-1'), n=-2.02, Ea=(20750.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 203,
    label = "C2H5O <=> CH3CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.45e+15, 's^-1'), n=-0.69, Ea=(22229.9, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 204,
    label = "C2H5O + O2 <=> CH3CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.29e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (874.76, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 205,
    label = "C2H5 + O2 <=> C2H4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.92e+07, 'cm^3/(mol*s)'),
        n = 1.02,
        Ea = (-2033.94, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 206,
    label = "C3H8 <=> C2H5 + CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.29e+37, 's^-1'), n=-5.84, Ea=(97387.7, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.64e+74, 'cm^3/(mol*s)'),
            n = -15.74,
            Ea = (98718.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.31,
        T3 = (50, 'K'),
        T1 = (3000, 'K'),
        T2 = (9000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 207,
    label = "C2H6 <=> CH3 + CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.88e+50, 's^-1'), n=-9.72, Ea=(107342, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.72e+65, 'cm^3/(mol*s)'),
            n = -13.14,
            Ea = (101580, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.39,
        T3 = (100, 'K'),
        T1 = (1900, 'K'),
        T2 = (6000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 208,
    label = "C2H6 + H <=> C2H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (170000, 'cm^3/(mol*s)'),
        n = 2.7,
        Ea = (5740.92, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 209,
    label = "C2H6 + O <=> C2H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(31.7, 'cm^3/(mol*s)'), n=3.8, Ea=(3130.98, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 210,
    label = "C2H6 + OH <=> C2H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.61e+06, 'cm^3/(mol*s)'),
        n = 2.22,
        Ea = (740.92, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 211,
    label = "C2H6 + S-CH2 <=> C2H5 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(-549.71, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 212,
    label = "C2H6 + CH3 <=> C2H5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.43e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (22256.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 213,
    label = "N-C3H7 + O <=> C2H5 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.17e+13, 'cm^3/(mol*s)'),
        n = 0.03,
        Ea = (-394.36, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 214,
    label = "N-C3H7 + H <=> C3H8",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.61e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.42e+61, 'cm^6/(mol^2*s)'),
            n = -13.55,
            Ea = (11357.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.315,
        T3 = (369, 'K'),
        T1 = (3285, 'K'),
        T2 = (6667, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 215,
    label = "N-C3H7 + OH <=> C3H6 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 216,
    label = "N-C3H7 + CH3 <=> C3H6 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.31e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-769.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 217,
    label = "C3H6 + H <=> N-C3H7",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (3.06e+14, 'cm^3/(mol*s)'),
            n = -0.37,
            Ea = (4032.03, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.26e+38, 'cm^6/(mol^2*s)'),
            n = -6.66,
            Ea = (7000.48, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (1000, 'K'),
        T1 = (1310, 'K'),
        T2 = (48097, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 218,
    label = "N-C3H7 + O2 <=> C3H6 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+16, 'cm^3/(mol*s)'),
        n = -1.63,
        Ea = (3417.78, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 219,
    label = "C3H8 + H <=> N-C3H7 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.058, 'cm^3/(mol*s)'),
        n = 4.71,
        Ea = (6211.76, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 220,
    label = "C3H8 + O <=> N-C3H7 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35, 'cm^3/(mol*s)'),
        n = 4.09,
        Ea = (2545.41, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 221,
    label = "C3H8 + OH <=> N-C3H7 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.36e+06, 'cm^3/(mol*s)'),
        n = 2.01,
        Ea = (365.68, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 222,
    label = "C3H8 + CH3 <=> N-C3H7 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.903, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7153.44, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 223,
    label = "C3H8 + HO2 <=> N-C3H7 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9640, 'cm^3/(mol*s)'), n=2.6, Ea=(13910.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 224,
    label = "C2H2 <=> H2C2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (2.45e+15, 'cm^3/(mol*s)'),
            n = -0.64,
            Ea = (49698.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 225,
    label = "H2C2 + O2 <=> T-CH2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 226,
    label = "H2C2 + O2 <=> HCO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 227,
    label = "C2H2 + S-CH2 <=> C3H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 228,
    label = "P-C3H4 + H <=> C2H2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.46e+12, 'cm^3/(mol*s)'),
        n = 0.44,
        Ea = (5463.67, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 229,
    label = "A-C3H4 + H <=> C2H2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.95e+13, 'cm^3/(mol*s)'),
        n = -0.02,
        Ea = (11250, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 230,
    label = "C2H2 + CH3 <=> S-C3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.45e+43, 'cm^3/(mol*s)'),
        n = -10.13,
        Ea = (18522.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 231,
    label = "C2H2 + C2H <=> N-C4H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 232,
    label = "C2H2 + HCCO <=> C3H3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(2999.52, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 233,
    label = "C2H3 + H2O2 <=> C2H4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-595.12, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 234,
    label = "C2H3 + HCO <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 235,
    label = "C2H3 + HCO <=> C2H3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 236,
    label = "C2H3 + CH3 <=> C2H2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.03e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-764.82, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 237,
    label = "C3H6 <=> C2H3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.04e+42, 's^-1'), n=-7.67, Ea=(111831, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 238,
    label = "C2H3 + CH3 <=> A-C3H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.93e+18, 'cm^3/(mol*s)'),
        n = -1.25,
        Ea = (7669.69, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 239,
    label = "A-C3H5 + H <=> C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.93e+54, 'cm^3/(mol*s)'),
        n = -11.76,
        Ea = (23549.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 240,
    label = "C2H + CH3 <=> C3H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 241,
    label = "C2O + H <=> CH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 242,
    label = "C2O + O <=> CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 243,
    label = "C2O + OH <=> H + CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 244,
    label = "C2O + O2 <=> O + CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 245,
    label = "HCCO + CH3 <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 246,
    label = "HCCO + OH <=> C2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 247,
    label = "HCCO + OH <=> HCO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 248,
    label = "CH2CO + OH <=> CH2OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 249,
    label = "CH2CO + T-CH2 <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 250,
    label = "CH2CO + T-CH2 <=> HCCO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(10999, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 251,
    label = "CH2CO + CH3 <=> C2H5 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 252,
    label = "CH2CO + CH3 <=> HCCO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12999.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 253,
    label = "CH2CHO + CH3 <=> C2H5 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.9e+14, 'cm^3/(mol*s)'), n=-0.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 254,
    label = "C2H4 + C2H <=> C4H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 255,
    label = "C2H4 + O2 <=> C2H3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.22e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (62100.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 256,
    label = "C2H4 + O2 => CH3 + CO2 + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.9e+12, 'cm^3/(mol*s)'),
        n = 0.42,
        Ea = (75800.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 257,
    label = "C2H5 + HCO <=> C2H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 258,
    label = "C2H5 + HO2 <=> C2H6 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 259,
    label = "C2H5 + HO2 <=> C2H4 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 260,
    label = "C2H5 + HO2 <=> C2H5O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 261,
    label = "C2H6 + HO2 <=> C2H5 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(261, 'cm^3/(mol*s)'), n=3.37, Ea=(15913, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 262,
    label = "C3H2 + O <=> C3H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.36e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 263,
    label = "C3H2 + OH <=> C2H2 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 264,
    label = "C3H2 + O2 <=> HCCO + CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.25e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (999.04, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 265,
    label = "C3H2 + CH <=> C4H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 266,
    label = "C3H2 + T-CH2 <=> N-C4H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 267,
    label = "C3H2 + CH3 <=> C4H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 268,
    label = "C3H2 + HCCO <=> N-C4H3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 269,
    label = "C2H + HCO <=> C3H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 270,
    label = "C3H2O + H <=> C2H2 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.46e+12, 'cm^3/(mol*s)'),
        n = 0.44,
        Ea = (5463.67, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 271,
    label = "C3H2O + H => C2H + CO + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.05e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2404.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 272,
    label = "C3H2O + O => C2H + CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.92e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1809.27, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 273,
    label = "C3H2O + O2 => C2H + CO + HO2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (39149.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 274,
    label = "C3H2O + OH => C2H + CO + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.34e+10, 'cm^3/(mol*s)'),
        n = 0.73,
        Ea = (-1113.77, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 275,
    label = "C3H2O + HO2 => C2H + CO + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11924, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 276,
    label = "C3H2O + CH3 => C2H + CO + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.72e+06, 'cm^3/(mol*s)'),
        n = 1.77,
        Ea = (5920.17, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 277,
    label = "C3H2 + H <=> C3H3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.02e+13, 'cm^3/(mol*s)'),
            n = 0.27,
            Ea = (279.64, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.8e+30, 'cm^6/(mol^2*s)'),
            n = -3.86,
            Ea = (3319.79, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.782,
        T3 = (207.5, 'K'),
        T1 = (2663, 'K'),
        T2 = (6095, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 278,
    label = "C3H3 + H <=> C3H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+10, 'cm^3/(mol*s)'),
        n = 1.13,
        Ea = (13929.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 279,
    label = "C3H3 + H <=> P-C3H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+29, 'cm^3/(mol*s)'),
        n = -5.06,
        Ea = (4861.38, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 280,
    label = "C3H3 + H <=> A-C3H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.16e+29, 'cm^3/(mol*s)'),
        n = -5,
        Ea = (4710.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 281,
    label = "C3H3 + OH <=> C2H3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.53e+06, 'cm^3/(mol*s)'),
        n = 1.55,
        Ea = (2105.64, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 282,
    label = "C3H3 + OH <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.28e+09, 'cm^3/(mol*s)'),
        n = 0.73,
        Ea = (2578.87, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 283,
    label = "C3H3 + OH <=> C3H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (113000, 'cm^3/(mol*s)'),
        n = 2.28,
        Ea = (2466.54, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 284,
    label = "C3H3 + OH <=> CH2O + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+36, 'cm^3/(mol*s)'),
        n = -7.8,
        Ea = (7060.23, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 285,
    label = "C3H3 + O <=> C3H2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.38e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 286,
    label = "C3H3 + O2 <=> CH2CO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (170000, 'cm^3/(mol*s)'),
        n = 1.7,
        Ea = (1500.96, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 287,
    label = "C3H3 + HO2 <=> OH + CO + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 288,
    label = "C3H3 + HO2 <=> A-C3H4 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 289,
    label = "C3H3 + HO2 <=> P-C3H4 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 290,
    label = "P-C3H4 + O2 <=> CH3 + HCO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+14, 'cm^3/(mol*s)'), n=0, Ea=(41928.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 291,
    label = "C3H3 + HCO <=> A-C3H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 292,
    label = "C3H3 + HCO <=> P-C3H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 293,
    label = "C3H3 + CH <=> I-C4H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 294,
    label = "C3H3 + T-CH2 <=> C4H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 295,
    label = "A-C3H4 <=> P-C3H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.76e+39, 's^-1'), n=-7.8, Ea=(78446.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 296,
    label = "A-C3H4 + H <=> P-C3H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.47e+15, 'cm^3/(mol*s)'),
        n = -0.33,
        Ea = (6436.42, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 297,
    label = "A-C3H4 + H <=> A-C3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.01e+49, 'cm^3/(mol*s)'),
        n = -10.77,
        Ea = (19622.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 298,
    label = "A-C3H4 + H <=> T-C3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.7e+42, 'cm^3/(mol*s)'),
        n = -12.46,
        Ea = (16359.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 299,
    label = "P-C3H4 + H <=> T-C3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.83e+52, 'cm^3/(mol*s)'),
        n = -12.36,
        Ea = (16446, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 300,
    label = "P-C3H4 + H <=> S-C3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.53e+49, 'cm^3/(mol*s)'),
        n = -11.97,
        Ea = (14144.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 301,
    label = "P-C3H4 + H <=> C3H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (85000, 'cm^3/(mol*s)'),
        n = 2.7,
        Ea = (5740.92, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 302,
    label = "P-C3H4 + O <=> C3H3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.49e+07, 'cm^3/(mol*s)'),
        n = 1.92,
        Ea = (5690.73, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 303,
    label = "P-C3H4 + OH <=> C3H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (805000, 'cm^3/(mol*s)'),
        n = 2.22,
        Ea = (740.92, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 304,
    label = "P-C3H4 + CH3 <=> C3H3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.22e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (22256.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 305,
    label = "P-C3H4 + HO2 <=> C3H3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(130, 'cm^3/(mol*s)'), n=3.37, Ea=(15913, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 306,
    label = "A-C3H4 + H <=> C3H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.33e+06, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (12239.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 307,
    label = "A-C3H4 + OH <=> C3H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.131, 'cm^3/(mol*s)'),
        n = 4.2,
        Ea = (-860.42, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 308,
    label = "A-C3H4 + CH3 <=> C3H3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(227000, 'cm^3/(mol*s)'), n=2, Ea=(9199.33, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 309,
    label = "A-C3H4 + HO2 <=> C3H3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.76e+10, 'cm^3/(mol*s)'),
        n = 0.12,
        Ea = (23370, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 310,
    label = "A-C3H4 + O <=> CH2CO + T-CH2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.63e+06, 'cm^3/(mol*s)'),
        n = 2.05,
        Ea = (179.25, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 311,
    label = "P-C3H4 + O <=> HCCO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.05e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1900.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 312,
    label = "P-C3H4 + O <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.25e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1900.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 313,
    label = "A-C3H4 + C2H <=> C2H2 + C3H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 314,
    label = "P-C3H4 + C2H <=> C2H2 + C3H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 315,
    label = "P-C3H4 + OH <=> HCCOH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (12712.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 316,
    label = "P-C3H4 + OH <=> CH2CO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.53e+06, 'cm^3/(mol*s)'),
        n = 1.55,
        Ea = (2105.64, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 317,
    label = "P-C3H4 + OH <=> C2H5 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.28e+09, 'cm^3/(mol*s)'),
        n = 0.73,
        Ea = (2578.87, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 318,
    label = "C2H3CHO + H => C2H3 + CO + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.09e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2404.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 319,
    label = "C2H3CHO + O => C2H3 + CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5.84e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1809.27, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 320,
    label = "C2H3CHO + OH => C2H3 + CO + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.89e+08, 'cm^3/(mol*s)'),
        n = 1.35,
        Ea = (-1572.66, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 321,
    label = "C2H3CHO + HO2 => C2H3 + CO + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (40900, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (10203.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 322,
    label = "C2H3CHO + CH3 => C2H3 + CO + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.49e-08, 'cm^3/(mol*s)'),
        n = 6.21,
        Ea = (1630.02, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 323,
    label = "A-C3H5 <=> T-C3H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.06e+56, 's^-1'), n=-14.08, Ea=(75867.6, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 324,
    label = "A-C3H5 <=> S-C3H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+51, 's^-1'), n=-13.02, Ea=(73300.7, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 325,
    label = "T-C3H5 <=> S-C3H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+48, 's^-1'), n=-12.71, Ea=(53900.6, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 326,
    label = "A-C3H5 + H <=> A-C3H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9560, 'cm^3/(mol*s)'), n=2.8, Ea=(3291.11, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 327,
    label = "A-C3H5 + OH <=> A-C3H4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 328,
    label = "A-C3H5 + CH3 <=> A-C3H4 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.86e+11, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (-131.45, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 329,
    label = "A-C3H5 + C2H3 <=> A-C3H4 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 330,
    label = "A-C3H5 + C2H5 <=> A-C3H4 + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-131.45, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 331,
    label = "A-C3H5 + A-C3H5 <=> A-C3H4 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 332,
    label = "A-C3H5 + O2 <=> A-C3H4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20600, 'cm^3/(mol*s)'),
        n = 2.19,
        Ea = (17590.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 333,
    label = "A-C3H5 + O2 <=> C2H3CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (336000, 'cm^3/(mol*s)'),
        n = 1.81,
        Ea = (19189.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 334,
    label = "A-C3H5 + O2 => C2H2 + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (9.71e+20, 'cm^3/(mol*s)'),
        n = -2.7,
        Ea = (24980.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 335,
    label = "A-C3H5 + O2 <=> CH2CHO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.08e+09, 'cm^3/(mol*s)'),
        n = 0.37,
        Ea = (16909.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 336,
    label = "A-C3H5 + O <=> C3H5O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.17e+13, 'cm^3/(mol*s)'),
        n = 0.03,
        Ea = (-394.36, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 337,
    label = "A-C3H5 + OH <=> C2H3CHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+32, 'cm^3/(mol*s)'),
        n = -5.16,
        Ea = (30126.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 338,
    label = "A-C3H5 + HCO <=> C3H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 339,
    label = "A-C3H5 + HO2 <=> C3H6 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.66e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 340,
    label = "A-C3H5 + HO2 <=> C3H5O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.06e+16, 'cm^3/(mol*s)'),
        n = -0.94,
        Ea = (2523.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 341,
    label = "A-C3H5 + CH3O2 <=> C3H5O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-999.04, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 342,
    label = "T-C3H5 + H <=> P-C3H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.34e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 343,
    label = "T-C3H5 + O <=> CH3 + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 344,
    label = "T-C3H5 + OH => CH3 + CH2CO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 345,
    label = "T-C3H5 + HO2 <=> CH3 + CH2CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 346,
    label = "T-C3H5 + HCO <=> C3H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 347,
    label = "T-C3H5 + CH3 <=> P-C3H4 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 348,
    label = "S-C3H5 + H <=> P-C3H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.34e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 349,
    label = "S-C3H5 + O <=> C2H4 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 350,
    label = "S-C3H5 + OH => C2H4 + HCO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 351,
    label = "S-C3H5 + HO2 <=> C2H4 + HCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 352,
    label = "S-C3H5 + HCO <=> C3H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 353,
    label = "S-C3H5 + CH3 <=> P-C3H4 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 354,
    label = "T-C3H5 + O2 <=> P-C3H4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.34e+06, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-384.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 355,
    label = "S-C3H5 + O2 <=> P-C3H4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (670000, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-384.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 356,
    label = "T-C3H5 + O2 => CH2CO + CH3 + O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.03e+11, 'cm^3/(mol*s)'),
        n = 0.29,
        Ea = (11.95, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 357,
    label = "S-C3H5 + O2 => C2H3CHO + H + O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.03e+11, 'cm^3/(mol*s)'),
        n = 0.29,
        Ea = (11.95, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 358,
    label = "T-C3H5 + O2 => CH3 + CO + CH2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.58e+16, 'cm^3/(mol*s)'),
        n = -1.39,
        Ea = (1015.77, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 359,
    label = "S-C3H5 + O2 <=> CH3CHO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.58e+16, 'cm^3/(mol*s)'),
        n = -1.39,
        Ea = (1015.77, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 360,
    label = "T-C3H5 + O2 <=> A-C3H4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.92e+07, 'cm^3/(mol*s)'),
        n = 1.02,
        Ea = (-2033.94, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 361,
    label = "C3H5O + O2 => C2H3CHO + HO2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(5999.04, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 362,
    label = "C3H5O <=> C2H3CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(29099, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 363,
    label = "C3H5O => C2H3 + CH2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.03e+12, 's^-1'), n=0.09, Ea=(23561.2, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 364,
    label = "C3H6 + H <=> C2H4 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+21, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 365,
    label = "C3H6 + O <=> CH2CHO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+08, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (327.44, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 366,
    label = "C3H6 + O <=> C2H5 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.5e+07, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (-972.75, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 367,
    label = "C3H6 + H <=> A-C3H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (660000, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756.69, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 368,
    label = "C3H6 + O <=> A-C3H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (96500, 'cm^3/(mol*s)'),
        n = 2.68,
        Ea = (3716.54, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 369,
    label = "C3H6 + OH <=> A-C3H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+08, 'cm^3/(mol*s)'),
        n = 1.46,
        Ea = (537.76, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 370,
    label = "C3H6 + HO2 <=> A-C3H5 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9600, 'cm^3/(mol*s)'), n=2.6, Ea=(13910.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 371,
    label = "C3H6 + CH3 <=> A-C3H5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.452, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7153.44, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 372,
    label = "C3H6 + H <=> T-C3H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (400000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (9789.67, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 373,
    label = "C3H6 + O <=> T-C3H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+10, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (7629.06, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 374,
    label = "C3H6 + OH <=> T-C3H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1450.76, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 375,
    label = "C3H6 + CH3 <=> T-C3H5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.84, 'cm^3/(mol*s)'), n=3.5, Ea=(11661.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 376,
    label = "C3H6 + H <=> S-C3H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (665000, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (12239.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 377,
    label = "C3H6 + O <=> S-C3H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (8960.33, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 378,
    label = "C3H6 + OH <=> S-C3H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0655, 'cm^3/(mol*s)'),
        n = 4.2,
        Ea = (-860.42, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 379,
    label = "C3H6 + CH3 <=> S-C3H5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(114000, 'cm^3/(mol*s)'), n=2, Ea=(9199.33, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 380,
    label = "C4H + O2 <=> C2H + CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(-755.26, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 381,
    label = "C4H + H <=> C4H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 382,
    label = "C4H2 + H <=> C4H + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+09, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (30107.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 383,
    label = "C4H2 + H2 <=> C4H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+14, 'cm^3/(mol*s)'), n=0, Ea=(53900.6, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 384,
    label = "C4H2 + C4H2 => C8H2 + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.51e+14, 'cm^3/(mol*s)'), n=0, Ea=(55999, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 385,
    label = "C4H2 + C4H2 <=> C8H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (42700.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 386,
    label = "C4H2 + O2 <=> HCCO + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.56e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (31099.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 387,
    label = "C4H2 + O <=> C3H2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.06e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1900.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 388,
    label = "C4H2 + H <=> I-C4H3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4.31e+10, 'cm^3/(mol*s)'),
            n = 1.16,
            Ea = (1751.91, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.3e+45, 'cm^6/(mol^2*s)'),
            n = -8.1,
            Ea = (2507.17, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.0748,
        T3 = (1, 'K'),
        T1 = (-4216, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 389,
    label = "C4H2 + H <=> N-C4H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+39, 'cm^3/(mol*s)'),
        n = -7.87,
        Ea = (15442.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 390,
    label = "C4H2 + OH <=> C4H + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.15e+09, 'cm^3/(mol*s)'),
        n = 1.03,
        Ea = (21747.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 391,
    label = "C4H2 + OH <=> C3H3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+12, 'cm^3/(mol*s)'),
        n = -0.25,
        Ea = (2375.72, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 392,
    label = "N-C4H3 <=> I-C4H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.1e+43, 's^-1'), n=-9.5, Ea=(52999.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 393,
    label = "N-C4H3 + H <=> I-C4H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+20, 'cm^3/(mol*s)'),
        n = -1.67,
        Ea = (10800.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 394,
    label = "N-C4H3 + H <=> C4H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+47, 'cm^3/(mol*s)'),
        n = -10.26,
        Ea = (13068.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 395,
    label = "I-C4H3 + H <=> C4H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+43, 'cm^3/(mol*s)'),
        n = -9.01,
        Ea = (12120, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 396,
    label = "N-C4H3 + H <=> C2H2 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+25, 'cm^3/(mol*s)'),
        n = -3.34,
        Ea = (10009.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 397,
    label = "I-C4H3 + H <=> C2H2 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+23, 'cm^3/(mol*s)'),
        n = -2.55,
        Ea = (10779.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 398,
    label = "N-C4H3 + H <=> C4H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 399,
    label = "I-C4H3 + H <=> C4H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 400,
    label = "N-C4H3 + OH <=> C4H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 401,
    label = "I-C4H3 + OH <=> C4H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 402,
    label = "N-C4H3 + O2 <=> C4H2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (670000, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-384.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 403,
    label = "I-C4H3 + O2 <=> C4H2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.34e+06, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-384.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 404,
    label = "I-C4H3 + O <=> CH2CO + C2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 405,
    label = "I-C4H3 + O2 <=> HCCO + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.63e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1799.71, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 406,
    label = "I-C4H3 + O2 <=> HCO + C2H2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (170000, 'cm^3/(mol*s)'),
        n = 1.7,
        Ea = (1500.96, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 407,
    label = "C4H4 + H <=> N-C4H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (127000, 'cm^3/(mol*s)'),
        n = 2.75,
        Ea = (11649.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 408,
    label = "C4H4 + H <=> I-C4H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (63500, 'cm^3/(mol*s)'),
        n = 2.75,
        Ea = (11649.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 409,
    label = "C4H4 + OH <=> N-C4H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0655, 'cm^3/(mol*s)'),
        n = 4.2,
        Ea = (-860.42, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 410,
    label = "C4H4 + OH <=> I-C4H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0328, 'cm^3/(mol*s)'),
        n = 4.2,
        Ea = (-860.42, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 411,
    label = "C4H4 + CH3 <=> N-C4H3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(114000, 'cm^3/(mol*s)'), n=2, Ea=(9199.33, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 412,
    label = "C4H4 + CH3 <=> I-C4H3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(56800, 'cm^3/(mol*s)'), n=2, Ea=(9199.33, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 413,
    label = "C4H4 + O <=> A-C3H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.25e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1900.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 414,
    label = "C4H4 + O <=> C3H2 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (35800, 'cm^3/(mol*s)'),
        n = 2.47,
        Ea = (929.73, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 415,
    label = "C4H4 + O <=> C3H3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.95e+08, 'cm^3/(mol*s)'),
        n = 1.36,
        Ea = (886.71, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 416,
    label = "C4H2 + C2H <=> C6H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 417,
    label = "C2H2 + C4H <=> C6H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 418,
    label = "C6H2 + C2H <=> C8H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 419,
    label = "C4H2 + C4H <=> C8H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 420,
    label = "H2C2 + C2H4 <=> C4H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 421,
    label = "H2C2 + C2H2 <=> C4H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 422,
    label = "C2H3 + C2H2 <=> N-C4H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.32e+12, 'cm^3/(mol*s)'),
        n = 0.16,
        Ea = (8312.62, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 423,
    label = "C2H3 + C2H3 <=> C4H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.43e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 424,
    label = "C2H3 + C2H3 <=> I-C4H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+22, 'cm^3/(mol*s)'),
        n = -2.44,
        Ea = (13654.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 425,
    label = "C2H3 + C2H3 <=> N-C4H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+20, 'cm^3/(mol*s)'),
        n = -2.04,
        Ea = (15363.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 426,
    label = "C2H3 + C2H3 <=> C2H2 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 427,
    label = "C3H3 + CH3 <=> C4H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.6e+57, 'cm^6/(mol^2*s)'),
            n = -11.94,
            Ea = (9772.94, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.175,
        T3 = (1340.6, 'K'),
        T1 = (60000, 'K'),
        T2 = (9769.8, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 428,
    label = "C3H6 + C2H3 <=> C4H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.23e+11, 'cm^3/(mol*s)'), n=0, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 429,
    label = "C4H6 <=> I-C4H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.7e+36, 's^-1'), n=-6.27, Ea=(112354, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 430,
    label = "C4H6 <=> N-C4H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+44, 's^-1'), n=-8.62, Ea=(123609, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 431,
    label = "C4H6 <=> C4H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+15, 's^-1'), n=0, Ea=(94698.9, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 432,
    label = "P-C3H4 + CH3 <=> C4H6 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.94e+07, 'cm^3/(mol*s)'),
        n = 1.14,
        Ea = (12380.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 433,
    label = "A-C3H4 + CH3 <=> C4H6 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.83e+08, 'cm^3/(mol*s)'),
        n = 1.06,
        Ea = (11161.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 434,
    label = "C4H6 + H <=> N-C4H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.33e+06, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (12239.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 435,
    label = "C4H6 + H <=> I-C4H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (665000, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (9239.96, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 436,
    label = "N-C4H5 + OH <=> C4H6 + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 437,
    label = "C4H6 + O <=> I-C4H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.5e+06, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (3740.44, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 438,
    label = "C4H6 + OH <=> N-C4H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (3429.73, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 439,
    label = "C4H6 + OH <=> I-C4H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.1e+06, 'cm^3/(mol*s)'), n=2, Ea=(430.21, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 440,
    label = "C4H6 + CH3 <=> N-C4H5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(22834.6, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 441,
    label = "C4H6 + CH3 <=> I-C4H5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(19799.2, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 442,
    label = "C4H6 + C2H3 <=> N-C4H5 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(22834.6, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 443,
    label = "C4H6 + C2H3 <=> I-C4H5 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (19799.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 444,
    label = "C4H6 + O => A-C3H5 + CO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (7.66e+09, 'cm^3/(mol*s)'),
        n = 0.88,
        Ea = (1140.06, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 445,
    label = "C4H6 + O <=> P-C3H4 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (71500, 'cm^3/(mol*s)'),
        n = 2.47,
        Ea = (929.73, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 446,
    label = "C4H6 + O <=> A-C3H5 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.89e+08, 'cm^3/(mol*s)'),
        n = 1.36,
        Ea = (886.71, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 447,
    label = "C4H6 + OH <=> A-C3H5 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.75e+36, 'cm^3/(mol*s)'),
        n = -7.8,
        Ea = (7060.23, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 448,
    label = "C4H4 + H <=> N-C4H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+51, 'cm^3/(mol*s)'),
        n = -11.92,
        Ea = (16501, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 449,
    label = "C4H4 + H <=> I-C4H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.9e+51, 'cm^3/(mol*s)'),
        n = -11.92,
        Ea = (17700.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 450,
    label = "N-C4H5 <=> I-C4H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+67, 's^-1'), n=-16.89, Ea=(59106.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 451,
    label = "N-C4H5 + H <=> I-C4H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+26, 'cm^3/(mol*s)'),
        n = -3.35,
        Ea = (17423.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 452,
    label = "N-C4H5 + H <=> C4H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 453,
    label = "N-C4H5 + OH <=> C4H4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 454,
    label = "N-C4H5 + HCO <=> C4H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 455,
    label = "N-C4H5 + H2O2 <=> C4H6 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-595.12, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 456,
    label = "N-C4H5 + HO2 <=> C4H6 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 457,
    label = "N-C4H5 + O <=> A-C3H5 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.03e+13, 'cm^3/(mol*s)'),
        n = 0.21,
        Ea = (-427.82, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 458,
    label = "N-C4H5 + O2 <=> C4H4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.34e+06, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-384.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 459,
    label = "N-C4H5 + O2 => A-C3H5 + CO + O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.03e+11, 'cm^3/(mol*s)'),
        n = 0.29,
        Ea = (11.95, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 460,
    label = "N-C4H5 + O2 <=> HCO + C2H3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.58e+16, 'cm^3/(mol*s)'),
        n = -1.39,
        Ea = (1015.77, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 461,
    label = "I-C4H5 + H <=> C4H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 462,
    label = "I-C4H5 + H <=> C3H3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(2000.48, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 463,
    label = "I-C4H5 + OH <=> C4H4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 464,
    label = "I-C4H5 + HCO <=> C4H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 465,
    label = "I-C4H5 + HO2 <=> C4H6 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 466,
    label = "I-C4H5 + H2O2 <=> C4H6 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-595.12, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 467,
    label = "I-C4H5 + O2 <=> CH2CO + CH2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.16e+10, 'cm^3/(mol*s)'), n=0, Ea=(2500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 468,
    label = "I-C4H5 + O <=> C3H3 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.17e+13, 'cm^3/(mol*s)'),
        n = 0.03,
        Ea = (-394.36, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 469,
    label = "N-C4H5 + C2H3 <=> A1 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.84e-13, 'cm^3/(mol*s)'),
        n = 7.07,
        Ea = (-3611.38, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 470,
    label = "N-C7H16 => C5H11 + C2H5",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8.1e+77, 's^-1'), n=-17.62, Ea=(120399, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 471,
    label = "N-C7H16 => P-C4H9 + N-C3H7",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.42e+78, 's^-1'), n=-17.71, Ea=(120700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 472,
    label = "N-C7H16 + H => C7H15 + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.75e+06, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (4361.85, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 473,
    label = "N-C7H16 + O => C7H15 + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (172000, 'cm^3/(mol*s)'),
        n = 2.81,
        Ea = (2260.99, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 474,
    label = "N-C7H16 + OH => C7H15 + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (7.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (258.13, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 475,
    label = "N-C7H16 + O2 => C7H15 + HO2",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.89e+13, 'cm^3/(mol*s)'),
        n = 0.2,
        Ea = (50109.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 476,
    label = "N-C7H16 + HO2 => C7H15 + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (7.57e+12, 'cm^3/(mol*s)'),
        n = 0.21,
        Ea = (17633.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 477,
    label = "C7H15 + H => N-C7H16",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.21e+81, 'cm^3/(mol*s)'),
        n = -19.78,
        Ea = (39022.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 478,
    label = "C7H15 + HO2 => N-C7H16 + O2",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.16e+08, 'cm^3/(mol*s)'),
        n = 0.98,
        Ea = (-1529.64, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 479,
    label = "C7H15 => C5H11 + C2H4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.89e+12, 's^-1'), n=0.02, Ea=(27784.4, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 480,
    label = "C7H15 => P-C4H9 + C3H6",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.73e+18, 's^-1'), n=-1.75, Ea=(31974.2, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 481,
    label = "C7H15 => N-C3H7 + P-C4H8",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.53e+18, 's^-1'), n=-1.65, Ea=(31682.6, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 482,
    label = "C7H15 => C2H5 + C5H10",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.49e+16, 's^-1'), n=-1.18, Ea=(29517.2, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 483,
    label = "C7H15 => C7H14 + H",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(1.41e+15, 's^-1'), n=-0.53, Ea=(37409.2, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 484,
    label = "C7H14 + H => C7H15",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(
        A = (6.66e+11, 'cm^3/(mol*s)'),
        n = 0.45,
        Ea = (2014.82, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 485,
    label = "C7H15 + HO2 => C7H15O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-999.04, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 486,
    label = "C7H15 + CH3O2 => C7H15O + CH3O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-999.04, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 487,
    label = "C7H15O => C3H7CHO + N-C3H7",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6.18e+16, 's^-1'), n=-1.36, Ea=(18518.2, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 488,
    label = "C7H15O => C2H5 + HCO + P-C4H9",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.23e+15, 's^-1'), n=-0.7, Ea=(18606.6, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 489,
    label = "C7H15O => CH3CHO + C5H11",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8.92e+19, 's^-1'), n=-2.03, Ea=(21003.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 490,
    label = "C7H14 => C4H7 + N-C3H7",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.19e+22, 's^-1'), n=-1.87, Ea=(73616.2, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 491,
    label = "C7H14 => P-C4H9 + A-C3H5",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1080, 's^-1'), n=3.77, Ea=(66546.4, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 492,
    label = "C7H14 + H <=> C7H13 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3900.57, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 493,
    label = "C7H14 + OH => C7H13 + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(1230.88, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 494,
    label = "C7H14 + OH => CH3CHO + C5H11",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (9.87e+22, 'cm^3/(mol*s)'),
        n = -3.62,
        Ea = (2903.92, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 495,
    label = "C7H14 + OH => C2H5 + HCO + P-C4H9",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.07e+16, 'cm^3/(mol*s)'),
        n = -1.65,
        Ea = (-1823.61, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 496,
    label = "C7H13 => A-C3H5 + P-C4H8",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+13, 's^-1'), n=0, Ea=(45000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 497,
    label = "C7H13 => C4H7 + C3H6",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+13, 's^-1'), n=0, Ea=(45000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 498,
    label = "C5H11 => C2H4 + N-C3H7",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.46e+21, 's^-1'), n=-2.61, Ea=(32026.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 499,
    label = "C5H11 => H + C5H10",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(8.46e+14, 's^-1'), n=-0.47, Ea=(37617.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 500,
    label = "C5H10 + H => C5H11",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(
        A = (7.1e+12, 'cm^3/(mol*s)'),
        n = 0.12,
        Ea = (1460.33, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 501,
    label = "C5H11 => C3H6 + C2H5",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.15e-19, 's^-1'), n=8.84, Ea=(7105.64, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 502,
    label = "C5H10 => C2H5 + A-C3H5",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(9.17e+20, 's^-1'), n=-1.63, Ea=(73989, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 503,
    label = "C5H10 + H => C5H9 + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4000.96, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 504,
    label = "C5H10 + O => C5H9 + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (254000, 'cm^3/(mol*s)'),
        n = 2.56,
        Ea = (-1130.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 505,
    label = "C5H10 + OH => C5H9 + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5.12e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-298.76, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 506,
    label = "C5H9 => A-C3H5 + C2H4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+13, 's^-1'), n=0, Ea=(45000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 507,
    label = "C5H9 => C4H6 + CH3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.34e+15, 's^-1'), n=-0.52, Ea=(38319.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 508,
    label = "P-C4H9 => P-C4H8 + H",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(8.61e+17, 's^-1'), n=-1.4, Ea=(38910.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 509,
    label = "P-C4H8 + H => P-C4H9",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(
        A = (7.68e+12, 'cm^3/(mol*s)'),
        n = 0.11,
        Ea = (1479.45, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 510,
    label = "P-C4H9 => C2H5 + C2H4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8.39e+14, 's^-1'), n=-0.64, Ea=(26904.9, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 511,
    label = "P-C4H9 => C3H6 + CH3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+31, 's^-1'), n=-5.43, Ea=(42507.2, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 512,
    label = "P-C4H8 => A-C3H5 + CH3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+15, 's^-1'), n=0, Ea=(70999, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 513,
    label = "P-C4H8 + H => C4H7 + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(3900.57, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 514,
    label = "P-C4H8 + OH => C4H7 + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.25e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2217.97, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 515,
    label = "P-C4H8 + O2 => C4H7 + HO2",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.7e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (33200.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 516,
    label = "P-C4H8 + HO2 => C4H7 + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14899.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 517,
    label = "P-C4H8 + CH3 => C4H7 + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(7299.24, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 518,
    label = "C4H7 + H => P-C4H8",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 519,
    label = "C4H7 + HO2 => P-C4H8 + O2",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 520,
    label = "P-C4H8 + O => CH3CHO + C2H4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(850.86, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 521,
    label = "P-C4H8 + O => C2H5 + CH3 + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(850.86, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 522,
    label = "P-C4H8 + O => C3H6 + CH2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (723000, 'cm^3/(mol*s)'),
        n = 2.34,
        Ea = (-1049.24, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 523,
    label = "P-C4H8 + O => C2H5 + HCO + T-CH2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(850.86, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 524,
    label = "P-C4H8 + OH => N-C3H7 + CH2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 525,
    label = "P-C4H8 + OH => C2H6 + CH3 + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 526,
    label = "P-C4H8 + OH => C2H5 + CH3 + HCO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 527,
    label = "P-C4H8 + OH => C2H5 + CH3CHO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 528,
    label = "C3H7CHO + H => N-C3H7 + CO + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(4199.33, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 529,
    label = "C3H7CHO + OH => N-C3H7 + CO + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.69e+10, 'cm^3/(mol*s)'),
        n = 0.76,
        Ea = (-339.39, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 530,
    label = "C3H7CHO + O2 => N-C3H7 + CO + HO2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (42201.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 531,
    label = "C3H7CHO + CH3 => N-C3H7 + CO + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.7e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8439.29, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 532,
    label = "C3H7CHO + HO2 => N-C3H7 + CO + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13599.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 533,
    label = "C4H7 <=> C4H6 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+31, 's^-1'), n=-5.9, Ea=(38788.2, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 534,
    label = "C2H4 + C2H3 <=> C4H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+06, 'cm^3/(mol*s)'),
        n = 1.84,
        Ea = (3059.27, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 535,
    label = "C4H7 + H => C4H6 + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.16e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 536,
    label = "C4H7 + O2 => C4H6 + HO2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+09, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 537,
    label = "C4H7 + CH3 => C4H6 + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 538,
    label = "C4H7 + C2H5 => C4H6 + C2H6",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.98e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 539,
    label = "C4H7 + A-C3H5 => C4H6 + C3H6",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6.31e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 540,
    label = "C4H7 + HO2 => C4H7O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-999.04, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 541,
    label = "C4H7 + CH3O2 => C4H7O + CH3O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-999.04, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 542,
    label = "C4H7O => CH3CHO + C2H3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.94e+14, 's^-1'), n=0, Ea=(19001, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 543,
    label = "C4H7O => C2H3CHO + CH3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.94e+14, 's^-1'), n=0, Ea=(19001, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 544,
    label = "N-C3H7 + HO2 => N-C3H7O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-999.04, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 545,
    label = "N-C3H7 + CH3O2 => N-C3H7O + CH3O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-999.04, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 546,
    label = "N-C3H7O => C2H5 + CH2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.39e+16, 's^-1'), n=-0.87, Ea=(19770.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 547,
    label = "N-C3H7O => C2H5 + HCO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.51e+14, 's^-1'), n=0, Ea=(23401, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 548,
    label = "C4H6 + O => C2H4 + CH2CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 549,
    label = "C4H6 + OH => C2H5 + CH2CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 550,
    label = "C4H6 + OH => C2H3 + CH3CHO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 551,
    label = "I-C8H18 => Y-C7H15 + CH3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.02e+49, 's^-1'), n=-9.38, Ea=(96582.2, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 552,
    label = "I-C8H18 => I-C4H8 + I-C3H7 + CH3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5.75e+49, 's^-1'), n=-9.66, Ea=(98040.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 553,
    label = "I-C8H18 => T-C4H9 + T-C4H9",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.94e+57, 's^-1'), n=-11.84, Ea=(98979.4, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 554,
    label = "I-C8H18 + H => C-C8H17 + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(51.5, 'cm^3/(mol*s)'), n=3.92, Ea=(2428.3, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 555,
    label = "I-C8H18 + O => C-C8H17 + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (12500, 'cm^3/(mol*s)'),
        n = 3.07,
        Ea = (1391.01, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 556,
    label = "I-C8H18 + OH => C-C8H17 + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.03e+07, 'cm^3/(mol*s)'),
        n = 1.99,
        Ea = (-284.42, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 557,
    label = "I-C8H18 + O2 => C-C8H17 + HO2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.03e+11, 'cm^3/(mol*s)'),
        n = 0.84,
        Ea = (46914.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 558,
    label = "I-C8H18 + CH3 => C-C8H17 + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.14e-18, 'cm^3/(mol*s)'),
        n = 9.25,
        Ea = (-2124.76, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 559,
    label = "I-C8H18 + HO2 => C-C8H17 + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (9.85e+10, 'cm^3/(mol*s)'),
        n = 0.73,
        Ea = (16943.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 560,
    label = "I-C8H18 + CH3O2 => C-C8H17 + CH3O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.93e+10, 'cm^3/(mol*s)'),
        n = 0.73,
        Ea = (16943.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 561,
    label = "C-C8H17 => I-C4H8 + T-C4H9",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(4.28e+22, 's^-1'), n=-2.81, Ea=(30521, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 562,
    label = "C-C8H17 => Y-C7H14 + CH3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.55e+39, 's^-1'), n=-7.47, Ea=(45286.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 563,
    label = "C-C8H17 => I-C4H8 + CH3 + C3H6",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(4.22e+24, 's^-1'), n=-3.34, Ea=(37920.7, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 564,
    label = "C-C8H17 + HO2 => D-C8H17O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-999.04, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 565,
    label = "C-C8H17 + CH3O2 => D-C8H17O + CH3O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-999.04, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 566,
    label = "D-C8H17O => I-C4H8 + CH3 + CH3COCH3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.33e+23, 's^-1'), n=-2.98, Ea=(15401.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 567,
    label = "D-C8H17O => T-C4H9 + I-C3H7 + HCO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.95e+33, 's^-1'), n=-6, Ea=(23319.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 568,
    label = "D-C8H17O => Y-C7H15 + CH2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.69e+20, 's^-1'), n=-2.08, Ea=(15055, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 569,
    label = "Y-C7H14 + H => Y-C7H15",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(
        A = (7.92e+16, 'cm^3/(mol*s)'),
        n = -1.01,
        Ea = (3819.31, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 570,
    label = "Y-C7H15 => Y-C7H14 + H",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(1.83e+17, 's^-1'), n=-0.9, Ea=(39605.6, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 571,
    label = "Y-C7H15 => I-C4H8 + I-C3H7",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.94e+18, 's^-1'), n=-1.49, Ea=(32688.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 572,
    label = "Y-C7H15 => T-C4H9 + C3H6",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.12e-44, 's^-1'), n=15.73, Ea=(-15676.4, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 573,
    label = "Y-C7H14 => I-C4H7 + I-C3H7",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6.53e+59, 's^-1'), n=-12.99, Ea=(94333.2, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 574,
    label = "Y-C7H14 => T-C4H9 + A-C3H5",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.09e+65, 's^-1'), n=-14.94, Ea=(91902.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 575,
    label = "Y-C7H14 + H => X-C7H13 + H2",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.38e-13, 'cm^3/(mol*s)'),
        n = 7.67,
        Ea = (-11388.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 576,
    label = "X-C7H13 + H2 => Y-C7H14 + H",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.93e+06, 'cm^3/(mol*s)'),
        n = 2.36,
        Ea = (22057.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 577,
    label = "Y-C7H14 + OH => X-C7H13 + H2O",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(
        A = (7.76e-09, 'cm^3/(mol*s)'),
        n = 6.18,
        Ea = (-9878.11, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 578,
    label = "X-C7H13 + H2O => Y-C7H14 + OH",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(
        A = (192000, 'cm^3/(mol*s)'),
        n = 2.76,
        Ea = (38080.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 579,
    label = "X-C7H13 + HO2 => I-C3H5CHO + I-C3H7 + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 580,
    label = "T-C4H9O => I-C3H7 + HCO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.78e+39, 's^-1'), n=-7.3, Ea=(37296.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 581,
    label = "T-C4H9O => CH2O + I-C3H7",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.25e+39, 's^-1'), n=-7.59, Ea=(33468, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 582,
    label = "T-C4H9O => CH3COCH3 + CH3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.09e+13, 's^-1'), n=0.03, Ea=(14070.3, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 583,
    label = "T-C4H9 => C3H6 + CH3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.34e+71, 's^-1'), n=-17.29, Ea=(62915.9, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 584,
    label = "T-C4H9 => H + I-C4H8",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(7.84e+45, 's^-1'), n=-9.64, Ea=(54115.7, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 585,
    label = "I-C4H8 + H => T-C4H9",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.14e+41, 'cm^3/(mol*s)'),
        n = -8.43,
        Ea = (14469.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 586,
    label = "T-C4H9 + HO2 => T-C4H9O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-999.04, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 587,
    label = "T-C4H9 + CH3O2 => T-C4H9O + CH3O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-999.04, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 588,
    label = "I-C4H8 => T-C3H5 + CH3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.92e+66, 's^-1'), n=-14.22, Ea=(128100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 589,
    label = "I-C4H8 <=> I-C4H7 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.07e+55, 's^-1'), n=-11.49, Ea=(114300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 590,
    label = "I-C4H8 + H => C3H6 + CH3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5.68e+33, 'cm^3/(mol*s)'),
        n = -5.72,
        Ea = (20000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 591,
    label = "I-C4H8 + H <=> I-C4H7 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (340000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (2492.83, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 592,
    label = "I-C4H8 + O => I-C4H7 + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.21e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (7633.84, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 593,
    label = "I-C4H8 + OH => I-C4H7 + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5.2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-298.76, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 594,
    label = "I-C4H8 + CH3 => I-C4H7 + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(4.42, 'cm^3/(mol*s)'), n=3.5, Ea=(5674, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 595,
    label = "I-C4H8 + HO2 => I-C4H7 + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (19300, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 596,
    label = "I-C4H8 + CH3O2 => I-C4H7 + CH3O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (19300, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 597,
    label = "I-C4H8 + O => I-C3H7 + HCO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.58e+07, 'cm^3/(mol*s)'),
        n = 1.76,
        Ea = (-1216.54, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 598,
    label = "I-C4H8 + O => CH2CO + CH3 + CH3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.33e+07, 'cm^3/(mol*s)'),
        n = 1.76,
        Ea = (76.48, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 599,
    label = "I-C4H7O => T-C3H5 + CH2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.01e+18, 's^-1'), n=-1.45, Ea=(30841.3, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 600,
    label = "I-C4H7O => I-C3H5CHO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+13, 's^-1'), n=0, Ea=(29099, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 601,
    label = "I-C4H7O + O2 => I-C3H5CHO + HO2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3e+10, 'cm^3/(mol*s)'), n=0, Ea=(1649.14, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 602,
    label = "I-C4H7 => A-C3H4 + CH3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.23e+47, 's^-1'), n=-9.74, Ea=(74259.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 603,
    label = "I-C4H7 + HO2 => I-C4H7O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 604,
    label = "I-C4H7 + O => I-C4H7O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 605,
    label = "I-C4H7 + O2 => I-C3H5CHO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.47e+13, 'cm^3/(mol*s)'),
        n = -0.45,
        Ea = (23021, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 606,
    label = "I-C4H7 + O2 => CH2CO + CH2O + CH3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (7.14e+15, 'cm^3/(mol*s)'),
        n = -1.21,
        Ea = (21049.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 607,
    label = "I-C4H7 + O2 => A-C3H4 + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (7.29e+29, 'cm^3/(mol*s)'),
        n = -5.71,
        Ea = (21450.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 608,
    label = "I-C4H7 + CH3O2 => I-C4H7O + CH3O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-999.04, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 609,
    label = "I-C3H5CHO + H => T-C3H5 + CO + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2600.38, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 610,
    label = "I-C3H5CHO + O => T-C3H5 + CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (7.18e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1388.62, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 611,
    label = "I-C3H5CHO + OH => T-C3H5 + CO + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.69e+10, 'cm^3/(mol*s)'),
        n = 0.76,
        Ea = (-339.39, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 612,
    label = "I-C3H5CHO + HO2 => T-C3H5 + CO + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(11919.2, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 613,
    label = "I-C3H5CHO + CH3 => T-C3H5 + CO + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.98e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8699.81, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 614,
    label = "I-C3H7 => C2H4 + CH3",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(9.77e-09, 's^-1'), n=5.36, Ea=(17029.2, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 615,
    label = "I-C3H7 => C3H6 + H",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(9.88e+18, 's^-1'), n=-1.59, Ea=(40348.9, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 616,
    label = "C3H6 + H => I-C3H7",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.73e+13, 'cm^3/(mol*s)'),
        n = 0.03,
        Ea = (1797.32, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 617,
    label = "C2H4 + CH3 => I-C3H7",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7203.63, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 618,
    label = "I-C3H7 + O2 => C3H6 + HO2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (7.65e+11, 'cm^3/(mol*s)'),
        n = -0.06,
        Ea = (5145.79, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 619,
    label = "CH3COCH3 + H => CH2CO + CH3 + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5.63e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (7700.76, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 620,
    label = "CH3COCH3 + O => CH2CO + CH3 + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.13e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7848.95, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 621,
    label = "CH3COCH3 + OH => CH2CO + CH3 + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.05e+10, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (1587, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 622,
    label = "CH3COCH3 + HO2 => CH2CO + CH3 + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.7e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20461.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 623,
    label = "C5H4CH2 + H <=> A1 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+12, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (2000.48, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 624,
    label = "N-C4H5 + C2H2 <=> C5H4CH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.62e+15, 'cm^3/(mol*s)'),
        n = -0.89,
        Ea = (9141.97, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 625,
    label = "I-C4H5 + C2H2 <=> C5H4CH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.8e+24, 'cm^3/(mol*s)'),
        n = -3.45,
        Ea = (20337, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 626,
    label = "C5H4CH2 <=> A1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.45e+45, 's^-1'), n=-8.9, Ea=(97002.9, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 627,
    label = "C5H4CH2 <=> A1- + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.24e+68, 's^-1'), n=-14.65, Ea=(142576, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 628,
    label = "N-C4H3 + C2H2 <=> A1-",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+70, 'cm^3/(mol*s)'),
        n = -17.77,
        Ea = (31300.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 629,
    label = "N-C4H5 + C2H2 <=> A1 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.38e+16, 'cm^3/(mol*s)'),
        n = -1,
        Ea = (8900.57, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 630,
    label = "I-C4H5 + C2H2 <=> A1 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.67e+23, 'cm^3/(mol*s)'),
        n = -3.3,
        Ea = (24959.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 631,
    label = "A-C3H5 + C3H3 => C5H4CH2 + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.16e+39, 'cm^3/(mol*s)'),
        n = -7.74,
        Ea = (23852.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 632,
    label = "C3H3 + C3H3 <=> C5H4CH2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.25e+46, 'cm^3/(mol*s)'),
        n = -10.1,
        Ea = (16959.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 633,
    label = "C3H3 + C3H3 <=> A1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.07e+45, 'cm^3/(mol*s)'),
        n = -9.57,
        Ea = (17014.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 634,
    label = "C3H3 + C3H3 <=> A1- + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.77e+37, 'cm^3/(mol*s)'),
        n = -7,
        Ea = (31505.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 635,
    label = "A1- + C2H2 <=> A1C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.29e+06, 'cm^3/(mol*s)'),
        n = 2.05,
        Ea = (3162.05, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 636,
    label = "A1- + C2H3 <=> A1C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 637,
    label = "A1 + C2H3 <=> A1C2H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.87e+07, 'cm^3/(mol*s)'),
        n = 1.47,
        Ea = (5532.98, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 638,
    label = "A1- + C2H4 <=> A1 + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00945, 'cm^3/(mol*s)'),
        n = 4.47,
        Ea = (4471.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 639,
    label = "A1C2H <=> A1C2H* + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.3e+60, 's^-1'), n=-12.48, Ea=(148086, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 640,
    label = "A1C2H + H <=> A1C2H* + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.29e+08, 'cm^3/(mol*s)'),
        n = 1.89,
        Ea = (17578.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 641,
    label = "A1C2H + OH <=> A1C2H* + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7800, 'cm^3/(mol*s)'), n=2.68, Ea=(733.75, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 642,
    label = "A1C2H2 <=> A1C2H3*",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.9e+10, 's^-1'), n=0.54, Ea=(27566.9, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 643,
    label = "A1C2H2 <=> A1C2H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.18e+10, 's^-1'), n=1.02, Ea=(38673.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 644,
    label = "A1C2H2 + H <=> A1C2H + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.65e+11, 'cm^3/(mol*s)'),
        n = 0.49,
        Ea = (10631, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 645,
    label = "A1C2H2 + OH <=> A1C2H + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 646,
    label = "A1C2H3 <=> A1C2H3* + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.3e+60, 's^-1'), n=-12.48, Ea=(148086, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 647,
    label = "A1C2H3 + H <=> A1C2H3* + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.23e+06, 'cm^3/(mol*s)'),
        n = 2.36,
        Ea = (16916.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 648,
    label = "A1C2H3 + OH <=> A1C2H3* + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(134, 'cm^3/(mol*s)'), n=3.33, Ea=(1455.54, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 649,
    label = "A1C2H3 <=> A1C2H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+14, 's^-1'), n=0.34, Ea=(111255, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 650,
    label = "A1C2H3 + H <=> A1C2H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (63500, 'cm^3/(mol*s)'),
        n = 2.75,
        Ea = (11649.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 651,
    label = "A1C2H3 + OH <=> A1C2H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0655, 'cm^3/(mol*s)'),
        n = 4.2,
        Ea = (-860.42, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 652,
    label = "A1C2H* + C2H2 <=> A2-",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (13400, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (1283.46, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 653,
    label = "A1C2H3* + C2H2 <=> A2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3020, 'cm^3/(mol*s)'),
        n = 2.55,
        Ea = (3181.17, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 654,
    label = "A1C2H2 + C2H2 <=> A2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+07, 'cm^3/(mol*s)'),
        n = 1.62,
        Ea = (4438.34, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 655,
    label = "A1C2H + C2H3 <=> A2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.6e+17, 'cm^3/(mol*s)'),
        n = -1.44,
        Ea = (15757.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 656,
    label = "A1C2H* + C2H4 <=> A2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+28, 'cm^3/(mol*s)'),
        n = -4.24,
        Ea = (23864.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 657,
    label = "A1- + C4H4 <=> A2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12600, 'cm^3/(mol*s)'),
        n = 2.61,
        Ea = (1434.03, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 658,
    label = "A2 <=> A2- + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.6e+60, 's^-1'), n=-12.48, Ea=(148076, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 659,
    label = "A2 + H <=> A2- + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.65e+08, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (17096.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 660,
    label = "A2 + OH <=> A2- + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(963, 'cm^3/(mol*s)'), n=3.02, Ea=(4373.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 661,
    label = "A2 <=> A2* + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.6e+60, 's^-1'), n=-12.48, Ea=(148076, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 662,
    label = "A2 + H <=> A2* + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.65e+08, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (17096.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 663,
    label = "A2 + OH <=> A2* + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(963, 'cm^3/(mol*s)'), n=3.02, Ea=(4373.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 664,
    label = "A2- + C2H2 <=> A2C2H2A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.28e+06, 'cm^3/(mol*s)'),
        n = 2.05,
        Ea = (1931.17, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 665,
    label = "A2* + C2H2 <=> A2C2H2B",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.29e+06, 'cm^3/(mol*s)'),
        n = 2.05,
        Ea = (3162.05, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 666,
    label = "A2- + C2H3 <=> A2C2H2A + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 667,
    label = "A2* + C2H3 <=> A2C2H2B + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 668,
    label = "A2 + C2H3 <=> A2C2H2A + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.2e+17, 'cm^3/(mol*s)'),
        n = -1.44,
        Ea = (15757.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 669,
    label = "A2 + C2H3 <=> A2C2H2B + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.2e+17, 'cm^3/(mol*s)'),
        n = -1.44,
        Ea = (15757.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 670,
    label = "A2- + C2H4 <=> A2C2H2A + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+28, 'cm^3/(mol*s)'),
        n = -4.24,
        Ea = (23864.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 671,
    label = "A2* + C2H4 <=> A2C2H2B + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+28, 'cm^3/(mol*s)'),
        n = -4.24,
        Ea = (23864.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 672,
    label = "A2C2H2A <=> A2C2HA + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.18e+10, 's^-1'), n=1.02, Ea=(38673.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 673,
    label = "A2C2H2A + H <=> A2C2HA + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.65e+11, 'cm^3/(mol*s)'),
        n = 0.49,
        Ea = (10631, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 674,
    label = "A2C2H2A + OH <=> A2C2HA + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 675,
    label = "A2C2H2B <=> A2C2HB + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.18e+10, 's^-1'), n=1.02, Ea=(38673.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 676,
    label = "A2C2H2B + H <=> A2C2HB + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.65e+11, 'cm^3/(mol*s)'),
        n = 0.49,
        Ea = (10631, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 677,
    label = "A2C2H2B + OH <=> A2C2HB + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 678,
    label = "A2C2HA <=> A2C2HA* + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.15e+60, 's^-1'), n=-12.48, Ea=(148076, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 679,
    label = "A2C2HA + H <=> A2C2HA* + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.32e+08, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (16821.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 680,
    label = "A2C2HA + OH <=> A2C2HA* + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (67.2, 'cm^3/(mol*s)'),
        n = 3.33,
        Ea = (1455.54, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 681,
    label = "A2C2HB <=> A2C2HB* + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.15e+60, 's^-1'), n=-12.48, Ea=(148076, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 682,
    label = "A2C2HB + H <=> A2C2HB* + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.32e+08, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (16821.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 683,
    label = "A2C2HB + OH <=> A2C2HB* + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (67.2, 'cm^3/(mol*s)'),
        n = 3.33,
        Ea = (1455.54, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 684,
    label = "A2C2H2A <=> A2R5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.88e+11, 's^-1'), n=0.23, Ea=(17026.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 685,
    label = "A2C2HA + H <=> A2R5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.52e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13360.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 686,
    label = "A2R5 <=> A2R5- + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.6e+60, 's^-1'), n=-12.48, Ea=(148076, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 687,
    label = "A2R5 + H <=> A2R5- + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.65e+08, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (17096.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 688,
    label = "A2R5 + OH <=> A2R5- + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(963, 'cm^3/(mol*s)'), n=3.02, Ea=(4373.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 689,
    label = "A2R5- + C2H2 <=> A2R5C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.29e+06, 'cm^3/(mol*s)'),
        n = 2.05,
        Ea = (3162.05, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 690,
    label = "A2R5- + C2H3 <=> A2R5C2H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 691,
    label = "A2R5 + C2H3 <=> A2R5C2H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.6e+17, 'cm^3/(mol*s)'),
        n = -1.44,
        Ea = (15757.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 692,
    label = "A2R5- + C2H4 <=> A2R5C2H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+28, 'cm^3/(mol*s)'),
        n = -4.24,
        Ea = (23864.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 693,
    label = "A2R5C2H <=> A2R5C2H* + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.15e+60, 's^-1'), n=-12.48, Ea=(148076, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 694,
    label = "A2R5C2H + H <=> A2R5C2H* + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.32e+08, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (16821.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 695,
    label = "A2R5C2H + OH <=> A2R5C2H* + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (67.2, 'cm^3/(mol*s)'),
        n = 3.33,
        Ea = (1455.54, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 696,
    label = "A2R5C2H2 <=> A2R5C2H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.18e+10, 's^-1'), n=1.02, Ea=(38673.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 697,
    label = "A2R5C2H2 + H <=> A2R5C2H + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.65e+11, 'cm^3/(mol*s)'),
        n = 0.49,
        Ea = (10631, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 698,
    label = "A2R5C2H2 + OH <=> A2R5C2H + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 699,
    label = "A1 + A1- <=> P2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.55e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2167.78, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 700,
    label = "A1- + A1- <=> P2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.39e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (112.33, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 701,
    label = "P2 <=> P2- + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.6e+60, 's^-1'), n=-12.48, Ea=(148076, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 702,
    label = "P2 + H <=> P2- + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.01e+08, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (16352.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 703,
    label = "P2 + OH <=> P2- + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(269, 'cm^3/(mol*s)'), n=3.33, Ea=(1455.54, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 704,
    label = "A2C2HA* + C2H2 <=> A3-",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (13400, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (1283.46, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 705,
    label = "A2C2HB* + C2H2 <=> A3-",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (13400, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (1283.46, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 706,
    label = "A2C2H2A + C2H2 <=> A3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+07, 'cm^3/(mol*s)'),
        n = 1.62,
        Ea = (4438.34, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 707,
    label = "A2C2H2B + C2H2 <=> A3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+07, 'cm^3/(mol*s)'),
        n = 1.62,
        Ea = (4438.34, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 708,
    label = "P2- + C2H2 <=> A3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.29e+06, 'cm^3/(mol*s)'),
        n = 2.05,
        Ea = (3162.05, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 709,
    label = "A2C2HA* + C2H3 <=> A3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 710,
    label = "A2C2HB* + C2H3 <=> A3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 711,
    label = "A2C2HA + C2H3 <=> A3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+17, 'cm^3/(mol*s)'),
        n = -1.44,
        Ea = (15757.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 712,
    label = "A2C2HB + C2H3 <=> A3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+17, 'cm^3/(mol*s)'),
        n = -1.44,
        Ea = (15757.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 713,
    label = "A2C2HA* + C2H4 <=> A3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+28, 'cm^3/(mol*s)'),
        n = -4.24,
        Ea = (23864.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 714,
    label = "A2C2HB* + C2H4 <=> A3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+28, 'cm^3/(mol*s)'),
        n = -4.24,
        Ea = (23864.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 715,
    label = "A2- + C4H4 <=> A3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12600, 'cm^3/(mol*s)'),
        n = 2.61,
        Ea = (1434.03, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 716,
    label = "A2* + C4H4 <=> A3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12600, 'cm^3/(mol*s)'),
        n = 2.61,
        Ea = (1434.03, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 717,
    label = "A1C2H + A1- <=> A3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.18e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2167.78, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 718,
    label = "A1C2H* + A1 <=> A3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.39e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2167.78, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 719,
    label = "A1C2H* + A1- <=> A3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.39e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (112.33, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 720,
    label = "A3 <=> A3- + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.3e+60, 's^-1'), n=-12.48, Ea=(148076, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 721,
    label = "A3 + H <=> A3- + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+08, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (16352.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 722,
    label = "A3 + OH <=> A3- + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(134, 'cm^3/(mol*s)'), n=3.33, Ea=(1455.54, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 723,
    label = "A3 <=> A3* + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.3e+60, 's^-1'), n=-12.48, Ea=(148076, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 724,
    label = "A3 + H <=> A3* + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.65e+08, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (17096.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 725,
    label = "A3 + OH <=> A3* + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(963, 'cm^3/(mol*s)'), n=3.02, Ea=(4373.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 726,
    label = "A3- <=> A2R5- + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+11, 's^-1'), n=1.08, Ea=(70399.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 727,
    label = "A2R5C2H* + C2H2 <=> A3R5-",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (13400, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (1283.46, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 728,
    label = "A2R5C2H2 + C2H2 <=> A3R5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+07, 'cm^3/(mol*s)'),
        n = 1.62,
        Ea = (4438.34, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 729,
    label = "A3* + C2H2 <=> A3R5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.28e+06, 'cm^3/(mol*s)'),
        n = 2.05,
        Ea = (1931.17, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 730,
    label = "A3* + C2H3 <=> A3R5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 731,
    label = "A2R5- + C4H4 <=> A3R5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12600, 'cm^3/(mol*s)'),
        n = 2.61,
        Ea = (1434.03, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 732,
    label = "A3R5 <=> A3R5- + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.15e+60, 's^-1'), n=-12.48, Ea=(148076, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 733,
    label = "A3R5 + H <=> A3R5- + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.65e+08, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (17096.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 734,
    label = "A3R5 + OH <=> A3R5- + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(963, 'cm^3/(mol*s)'), n=3.02, Ea=(4373.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 735,
    label = "A3- + C2H2 <=> A4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.28e+06, 'cm^3/(mol*s)'),
        n = 2.05,
        Ea = (1931.17, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 736,
    label = "A4 <=> A4- + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.72e+60, 's^-1'), n=-12.48, Ea=(148076, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 737,
    label = "A4 + H <=> A4- + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.3e+08, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (17096.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 738,
    label = "A4 + OH <=> A4- + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1930, 'cm^3/(mol*s)'), n=3.02, Ea=(4373.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 739,
    label = "A4- + C2H2 <=> A4R5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.28e+06, 'cm^3/(mol*s)'),
        n = 2.05,
        Ea = (1931.17, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 740,
    label = "A3R5- + C2H2 <=> A4R5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.28e+06, 'cm^3/(mol*s)'),
        n = 2.05,
        Ea = (1931.17, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 741,
    label = "A2 + A1- => FLTN + H + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (6.37e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2167.78, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 742,
    label = "A2- + A1 => FLTN + H + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (9.55e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2167.78, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 743,
    label = "A2- + A1- => FLTN + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.39e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (112.33, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 744,
    label = "C5H6 <=> C5H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.73e+68, 's^-1'), n=-15.16, Ea=(116372, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 745,
    label = "C5H6 + H <=> C5H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(2258.6, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 746,
    label = "C5H6 + H <=> A-C3H5 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12344.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 747,
    label = "C5H6 + H => S-C3H5 + C2H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.3e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12344.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 748,
    label = "C5H6 + O <=> C5H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47700, 'cm^3/(mol*s)'),
        n = 2.71,
        Ea = (1106.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 749,
    label = "C5H6 + OH <=> C5H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.08e+06, 'cm^3/(mol*s)'), n=2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 750,
    label = "C5H6 + O2 <=> C5H5 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(37151.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 751,
    label = "C5H6 + HO2 <=> C5H5 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (12899.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 752,
    label = "C5H6 + CH3 <=> C5H5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.18, 'cm^3/(mol*s)'), n=4, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 753,
    label = "C5H6 + C2H3 <=> C5H5 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 754,
    label = "C5H6 + N-C4H5 <=> C5H5 + C4H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 755,
    label = "C5H6 + O <=> T-C5H5O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.66e+09, 'cm^3/(mol*s)'),
        n = 0.88,
        Ea = (1140.06, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 756,
    label = "C5H6 + O => C2H4 + C2H2 + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.89e+08, 'cm^3/(mol*s)'),
        n = 1.36,
        Ea = (886.71, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 757,
    label = "C5H6 + OH => C4H6 + HCO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.75e+36, 'cm^3/(mol*s)'),
        n = -7.8,
        Ea = (7060.23, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 758,
    label = "C5H6 + OH => C2H4 + C2H2 + HCO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.75e+36, 'cm^3/(mol*s)'),
        n = -7.8,
        Ea = (7060.23, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 759,
    label = "C3H3 + C2H2 <=> C5H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.87e+55, 'cm^3/(mol*s)'),
        n = -12.5,
        Ea = (42065, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 760,
    label = "C5H5 + C5H5 => A2 + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (6.39e+29, 'cm^3/(mol*s)'),
        n = -4.03,
        Ea = (35205.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 761,
    label = "C5H5 + CH3 => C5H4CH2 + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.91e+31, 'cm^3/(mol*s)'),
        n = -4.85,
        Ea = (24772.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 762,
    label = "C5H5 + O <=> C5H4O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 763,
    label = "C5H5 + O2 <=> C5H4O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.34e+07, 'cm^3/(mol*s)'),
        n = 1.3,
        Ea = (17667.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 764,
    label = "C5H5 + HO2 <=> S-C5H5O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 765,
    label = "C5H5 + OH => S-C5H5O + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.02e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 766,
    label = "S-C5H5O <=> C5H4O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 's^-1'), n=0, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 767,
    label = "T-C5H5O => N-C4H5 + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+12, 's^-1'), n=0, Ea=(35999, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 768,
    label = "S-C5H5O + H => C5H4O + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6.67e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 769,
    label = "S-C5H5O + O => C5H4O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.33e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 770,
    label = "S-C5H5O + OH => C5H4O + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.67e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 771,
    label = "S-C5H5O + O2 => C5H4O + HO2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.43e-13, 'cm^3/(mol*s)'),
        n = 7.6,
        Ea = (-3530.11, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 772,
    label = "T-C5H5O + H => C5H4O + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.33e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 773,
    label = "T-C5H5O + O2 => C5H4O + HO2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.28e+07, 'cm^3/(mol*s)'),
        n = 1.02,
        Ea = (-2033.94, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 774,
    label = "C5H4O => C2H2 + C2H2 + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.37e+44, 's^-1'), n=-8, Ea=(108676, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 775,
    label = "C5H4O + H <=> T-C5H5O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.74e+09, 'cm^3/(mol*s)'),
        n = 1.46,
        Ea = (1355.16, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 776,
    label = "C5H4O + O <=> C4H4 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(2000.48, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 777,
    label = "C5H5 + C5H6 => C9H8 + CH3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (0.786, 'cm^3/(mol*s)'),
        n = 3.07,
        Ea = (5728.97, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 778,
    label = "A1- + C3H3 <=> C9H8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 779,
    label = "C9H8 <=> C9H7 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.73e+68, 's^-1'), n=-15.16, Ea=(116372, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 780,
    label = "C9H8 + H <=> C9H7 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(2258.6, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 781,
    label = "A1CH2 + C2H2 <=> C9H8 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (31600, 'cm^3/(mol*s)'),
        n = 2.48,
        Ea = (11061.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 782,
    label = "C9H8 + O <=> C9H7 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47700, 'cm^3/(mol*s)'),
        n = 2.71,
        Ea = (1106.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 783,
    label = "C9H8 + OH <=> C9H7 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.08e+06, 'cm^3/(mol*s)'), n=2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 784,
    label = "C9H8 + O2 <=> C9H7 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(37151.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 785,
    label = "C9H8 + HO2 <=> C9H7 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (12899.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 786,
    label = "C9H8 + CH3 <=> C9H7 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.18, 'cm^3/(mol*s)'), n=4, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 787,
    label = "C9H8 + O => C9H6O + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.83e+09, 'cm^3/(mol*s)'),
        n = 0.88,
        Ea = (1140.06, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 788,
    label = "C9H8 + OH => O-C6H4 + C2H4 + HCO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.88e+36, 'cm^3/(mol*s)'),
        n = -7.8,
        Ea = (7060.23, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 789,
    label = "C9H7 + C5H5 => A3 + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.56e+29, 'cm^3/(mol*s)'),
        n = -4.03,
        Ea = (35205.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 790,
    label = "C9H7 + CH3 => A2 + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.96e+31, 'cm^3/(mol*s)'),
        n = -4.85,
        Ea = (24772.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 791,
    label = "C9H7 + O <=> C9H6O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 792,
    label = "C9H7 + O2 <=> C9H6O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.74e+07, 'cm^3/(mol*s)'),
        n = 1.3,
        Ea = (17667.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 793,
    label = "C9H7 + HO2 => C9H6O + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.24e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 794,
    label = "C9H7 + OH => C9H6O + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(4.08e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 795,
    label = "C9H7 + C3H3 => A2R5 + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.32e+39, 'cm^3/(mol*s)'),
        n = -7.74,
        Ea = (23852.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 796,
    label = "C9H6O => O-C6H4 + C2H2 + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.37e+44, 's^-1'), n=-8, Ea=(108676, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 797,
    label = "C9H6O + H => A1C2H3* + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.37e+09, 'cm^3/(mol*s)'),
        n = 1.46,
        Ea = (1355.16, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 798,
    label = "A1CH3 + H <=> A1 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.31e+06, 'cm^3/(mol*s)'),
        n = 2.17,
        Ea = (4163.48, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 799,
    label = "A1CH3 <=> A1CH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.56e+13, 's^-1'), n=0.68, Ea=(89206.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 800,
    label = "A1CH3 <=> A1- + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.35e+22, 's^-1'), n=-1.73, Ea=(104209, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 801,
    label = "A1CH2 + H <=> A1- + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.83e+67, 'cm^3/(mol*s)'),
        n = -14.15,
        Ea = (68329.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 802,
    label = "A1CH2 <=> C5H5 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.2e+14, 's^-1'), n=0, Ea=(80676.4, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 803,
    label = "A1CH3 + O2 <=> A1CH2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.18e+07, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (46044.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 804,
    label = "A1CH3 + H <=> A1CH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.47, 'cm^3/(mol*s)'),
        n = 3.98,
        Ea = (3384.32, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 805,
    label = "A1CH3 + OH <=> A1CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (177000, 'cm^3/(mol*s)'),
        n = 2.39,
        Ea = (-602.29, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 806,
    label = "A1CH3 + OH <=> A1OH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(783, 'cm^3/(mol*s)'), n=2.88, Ea=(3221.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 807,
    label = "A1CH3 + OH <=> HOA1CH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (31.4, 'cm^3/(mol*s)'),
        n = 3.37,
        Ea = (4720.36, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 808,
    label = "A1CH3 + O <=> A1CH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.18, 'cm^3/(mol*s)'),
        n = 4.09,
        Ea = (2545.41, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 809,
    label = "A1CH3 + O <=> HOA1CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.69e+12, 'cm^3/(mol*s)'),
        n = 0.3,
        Ea = (4402.49, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 810,
    label = "A1CH3 + O <=> OA1CH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.66e+07, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (3974.67, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 811,
    label = "A1CH3 + CH3 <=> A1CH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.22e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (22256.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 812,
    label = "A1CH3 + HO2 <=> A1CH2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (93300, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (14684.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 813,
    label = "A1CH3 + A1- <=> A1CH2 + A1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11950.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 814,
    label = "A1CH2 + O <=> A1CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.28e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 815,
    label = "A1CH2 + OH <=> A1CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 816,
    label = "A1CH2 + HO2 <=> A1CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.19e+09, 'cm^3/(mol*s)'),
        n = 1.03,
        Ea = (-2249.04, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 817,
    label = "A1CH2 + C3H3 => A2 + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.32e+39, 'cm^3/(mol*s)'),
        n = -7.74,
        Ea = (23852.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 818,
    label = "A1CH2 + O2 <=> A1CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.76e+15, 'cm^3/(mol*s)'),
        n = -1.55,
        Ea = (11321.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 819,
    label = "A1CH2 + O2 <=> A1O + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.26e+37, 'cm^3/(mol*s)'),
        n = -8.86,
        Ea = (16582.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 820,
    label = "A1CH2O + H <=> A1CH2OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2.43e+12, 'cm^3/(mol*s)'),
            n = 0.52,
            Ea = (50.19, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.66e+41, 'cm^6/(mol^2*s)'),
            n = -7.44,
            Ea = (14079.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7,
        T3 = (100, 'K'),
        T1 = (90000, 'K'),
        T2 = (10000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 821,
    label = "A1CH2OH + H <=> A1CH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+06, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (4870.94, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 822,
    label = "A1CH2OH + O <=> A1CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(130000, 'cm^3/(mol*s)'), n=2.5, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 823,
    label = "A1CH2OH + OH <=> A1CH2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1500.96, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 824,
    label = "A1CH2OH + CH3 <=> A1CH2O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+07, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (9940.25, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 825,
    label = "A1- + CH2O <=> A1 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(85500, 'cm^3/(mol*s)'), n=2.19, Ea=(38.24, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 826,
    label = "A1CH2O <=> A1CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.26e+28, 's^-1'), n=-5.08, Ea=(22249, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 827,
    label = "A1CH2O <=> A1- + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.21e+33, 's^-1'), n=-6.21, Ea=(36849.9, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 828,
    label = "A1CH2O <=> A1 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.37e+32, 's^-1'), n=-6.1, Ea=(28809.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 829,
    label = "A1CH2O + H <=> A1CHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.33e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 830,
    label = "A1CH2O + O <=> A1CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.67e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 831,
    label = "A1CH2O + OH <=> A1CHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.33e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 832,
    label = "A1CH2O + O2 <=> A1CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.85e-13, 'cm^3/(mol*s)'),
        n = 7.6,
        Ea = (-3530.11, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 833,
    label = "A1CHO => A1- + CO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.1e+16, 's^-1'), n=0, Ea=(81740, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 834,
    label = "A1CHO + H => A1- + CO + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.09e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2404.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 835,
    label = "A1CHO + O => A1- + CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5.84e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1809.27, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 836,
    label = "A1CHO + OH => A1- + CO + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.89e+08, 'cm^3/(mol*s)'),
        n = 1.35,
        Ea = (-1572.66, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 837,
    label = "A1CHO + O2 => A1- + CO + HO2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(120000, 'cm^3/(mol*s)'), n=2.5, Ea=(37555, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 838,
    label = "A1CHO + HO2 => A1- + CO + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (40900, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (10203.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 839,
    label = "A1CHO + CH3 => A1- + CO + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.49e-08, 'cm^3/(mol*s)'),
        n = 6.21,
        Ea = (1630.02, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 840,
    label = "HOA1CH3 <=> OA1CH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.01e+71, 's^-1'), n=-15.92, Ea=(124790, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 841,
    label = "HOA1CH3 + H <=> OA1CH3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12397.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 842,
    label = "HOA1CH3 + O <=> OA1CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.81e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7351.82, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 843,
    label = "HOA1CH3 + OH <=> OA1CH3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.95e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1312.14, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 844,
    label = "OA1CH3 => C5H4CH2 + CO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.9e+10, 's^-1'), n=0, Ea=(36424.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 845,
    label = "A1CH3 <=> A1CH3* + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.39e+60, 's^-1'), n=-12.48, Ea=(148086, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 846,
    label = "A1CH3 + H <=> A1CH3* + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.91e+08, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (16352.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 847,
    label = "A1CH3 + O <=> A1CH3* + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14698.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 848,
    label = "A1CH3 + OH <=> A1CH3* + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (13600, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (619.02, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 849,
    label = "A1CH3 + CH3 <=> A1CH3* + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0179, 'cm^3/(mol*s)'),
        n = 4.46,
        Ea = (13637.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 850,
    label = "A1CH3* + O <=> OA1CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 851,
    label = "A1CH3* + OH <=> OA1CH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 852,
    label = "A1CH3* + HO2 <=> OA1CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 853,
    label = "A1CH3* + O2 <=> OA1CH3 + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.57e+20, 'cm^3/(mol*s)'),
        n = -2.27,
        Ea = (7189.29, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 854,
    label = "A1CH3* + O2 => C5H4CH2 + CO2 + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.55e+13, 'cm^3/(mol*s)'),
        n = -0.44,
        Ea = (-1649.14, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 855,
    label = "A1C2H4 + H <=> A1C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.61e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Commented out by Zach Buras because 4 products not compatible with RMG library\nA1CH3*+O2 => P-C3H4+C2H3+2CO            2.550e+13   -0.440  -1649.14',
    ),
    longDesc = 
u"""
Commented out by Zach Buras because 4 products not compatible with RMG library
A1CH3*+O2 => P-C3H4+C2H3+2CO            2.550e+13   -0.440  -1649.14
""",
)

entry(
    index = 856,
    label = "A1CH2 + CH3 <=> A1C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 857,
    label = "A1- + C2H5 <=> A1C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 858,
    label = "A1C2H5 + H <=> A1 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.31e+06, 'cm^3/(mol*s)'),
        n = 2.17,
        Ea = (4163.48, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 859,
    label = "A1C2H5 + OH <=> A1OH + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(783, 'cm^3/(mol*s)'), n=2.88, Ea=(3221.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 860,
    label = "A1C2H5 + H <=> A1C2H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0483, 'cm^3/(mol*s)'),
        n = 4.71,
        Ea = (6211.76, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 861,
    label = "A1C2H5 + O <=> A1C2H4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.96, 'cm^3/(mol*s)'),
        n = 4.09,
        Ea = (2545.41, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 862,
    label = "A1C2H5 + OH <=> A1C2H4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.47e+06, 'cm^3/(mol*s)'),
        n = 2.01,
        Ea = (365.68, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 863,
    label = "A1C2H5 + HO2 <=> A1C2H4 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8030, 'cm^3/(mol*s)'), n=2.6, Ea=(13910.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 864,
    label = "A1C2H5 + CH3 <=> A1C2H4 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.753, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7153.44, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 865,
    label = "A1C2H4 <=> A1- + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.72e+11, 's^-1'), n=0.78, Ea=(38704.6, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 866,
    label = "A1C2H4 <=> A1C2H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.79e+06, 's^-1'), n=2.08, Ea=(32105.6, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 867,
    label = "A1C2H4 + H <=> A1C2H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.67e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 868,
    label = "A1C2H4 + OH <=> A1C2H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 869,
    label = "A1C2H4 + CH3 <=> A1C2H3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.31e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-769.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 870,
    label = "A1C2H4 + O2 <=> A1C2H3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+16, 'cm^3/(mol*s)'),
        n = -1.63,
        Ea = (3417.78, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 871,
    label = "A1C2H4 + O <=> A1CH2 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.17e+13, 'cm^3/(mol*s)'),
        n = 0.03,
        Ea = (-394.36, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 872,
    label = "A1C2H4 + O <=> A1CHO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.17e+13, 'cm^3/(mol*s)'),
        n = 0.03,
        Ea = (-394.36, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 873,
    label = "A1C2H4 + HO2 => A1CH2 + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-999.04, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 874,
    label = "A1C2H4 + O2 => C8H9O2",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.82e+36, 'cm^3/(mol*s)'),
        n = -8.23,
        Ea = (5167.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 875,
    label = "A1C2H4 + O2 => A1CH2 + HCO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (38800, 'cm^3/(mol*s)'),
        n = 1.84,
        Ea = (-578.39, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 876,
    label = "C8H9O2 => A1C2H4 + O2",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(1.21e+45, 's^-1'), n=-10.15, Ea=(40815, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 877,
    label = "C8H9O2 => A1C2H3 + HO2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.45e+25, 's^-1'), n=-4.48, Ea=(32607.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 878,
    label = "C8H9O2 => A1CH2 + HCO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.23e+13, 's^-1'), n=-1.12, Ea=(27014.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 879,
    label = "C8H9O2 => C8H8OOH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(0.0545, 's^-1'), n=3.57, Ea=(16097, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 880,
    label = "C8H8OOH + O2 => OC8H7OOH + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 881,
    label = "A1C2H3 => A1 + H2C2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.4e+14, 's^-1'),
        n = 0,
        Ea = (78131, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Commented out by Zach Buras because 4 products not compatible with RMG library\nOC8H7OOH => A1-+CH2O+CO+OH              6.300e+14    0.000  43044.93',
    ),
    longDesc = 
u"""
Commented out by Zach Buras because 4 products not compatible with RMG library
OC8H7OOH => A1-+CH2O+CO+OH              6.300e+14    0.000  43044.93
""",
)

entry(
    index = 882,
    label = "A1C2H3 + O <=> A1CH2 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.1e+07, 'cm^3/(mol*s)'),
        n = 1.66,
        Ea = (657.27, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 883,
    label = "A1C2H3 + CH3 <=> A1C2H2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(114000, 'cm^3/(mol*s)'), n=2, Ea=(9199.33, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 884,
    label = "A1C2H3 + OH <=> A1CHO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+36, 'cm^3/(mol*s)'),
        n = -7.8,
        Ea = (7060.23, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 885,
    label = "A1C2H3 + OH <=> A1CH2 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+36, 'cm^3/(mol*s)'),
        n = -7.8,
        Ea = (7060.23, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 886,
    label = "A1C2H3 + OH <=> C2H3 + A1OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(783, 'cm^3/(mol*s)'), n=2.88, Ea=(3221.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 887,
    label = "A1C2H3 + O <=> A1C2H3* + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.33e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14698.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 888,
    label = "A1C2H2 + O <=> A1CH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.03e+13, 'cm^3/(mol*s)'),
        n = 0.21,
        Ea = (-427.82, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 889,
    label = "A1C2H2 + O2 <=> A1C2H + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (670000, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-384.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 890,
    label = "A1C2H2 + O2 => A1CH2 + CO + O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.03e+11, 'cm^3/(mol*s)'),
        n = 0.29,
        Ea = (11.95, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 891,
    label = "A1C2H2 + O2 <=> A1CHO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.58e+16, 'cm^3/(mol*s)'),
        n = -1.39,
        Ea = (1015.77, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 892,
    label = "A1C2H + OH <=> A1 + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 893,
    label = "A1CH3CH3 <=> A1CH3CH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+18, 's^-1'), n=-0.6, Ea=(94787.3, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 894,
    label = "A1CH3CH3 <=> A1CH3* + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.32e+29, 's^-1'), n=-3.58, Ea=(110165, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 895,
    label = "A1CH3CH3 + H <=> A1CH3CH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12.9, 'cm^3/(mol*s)'),
        n = 3.98,
        Ea = (3384.32, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 896,
    label = "A1CH3CH3 + O <=> A1CH3CH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.36, 'cm^3/(mol*s)'),
        n = 4.09,
        Ea = (2545.41, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 897,
    label = "A1CH3CH3 + OH <=> A1CH3CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (354000, 'cm^3/(mol*s)'),
        n = 2.39,
        Ea = (-602.29, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 898,
    label = "A1CH3CH3 + O2 <=> A1CH3CH2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.36e+07, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (46044.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 899,
    label = "A1CH3CH3 + HO2 <=> A1CH3CH2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (187000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (14684.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 900,
    label = "A1CH3CH3 + CH3 <=> A1CH3CH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.44e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (22256.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 901,
    label = "A1CH3CH3 + H <=> A1CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.62e+06, 'cm^3/(mol*s)'),
        n = 2.17,
        Ea = (4163.48, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 902,
    label = "A1CH3CH3 + OH <=> HOA1CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1570, 'cm^3/(mol*s)'), n=2.88, Ea=(3221.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 903,
    label = "A1CH3CH2 => A1 + H + C2H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (8.2e+14, 's^-1'),
        n = 0,
        Ea = (80676.4, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Commented out by Zach Buras because 4 products not compatible with RMG library\nA1CH3CH3+O => A1CH3+CO+2H               1.820e+08    1.550   3090.34',
    ),
    longDesc = 
u"""
Commented out by Zach Buras because 4 products not compatible with RMG library
A1CH3CH3+O => A1CH3+CO+2H               1.820e+08    1.550   3090.34
""",
)

entry(
    index = 904,
    label = "A1CH3CH2 + H <=> A1CH3* + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.83e+67, 'cm^3/(mol*s)'),
        n = -14.15,
        Ea = (68329.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 905,
    label = "A1CH3CH2 + O <=> A1CH3CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.37e+18, 'cm^3/(mol*s)'),
        n = -1.34,
        Ea = (1591.78, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 906,
    label = "A1CH3CH2 + O <=> A1CH3* + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.99e+23, 'cm^3/(mol*s)'),
        n = -2.47,
        Ea = (16192.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 907,
    label = "A1CH3CH2 + O <=> A1CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.97e+22, 'cm^3/(mol*s)'),
        n = -2.36,
        Ea = (8152.49, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 908,
    label = "A1CH3CH2 + OH => A1CH3CHO + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 909,
    label = "A1CH3CH2 + O2 <=> A1CH3CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(138, 'cm^3/(mol*s)'), n=2.42, Ea=(7440.25, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 910,
    label = "A1CH3CH2 + O2 <=> OA1CH3 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6570, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (5002.39, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 911,
    label = "A1CH3CH2 + HO2 => A1CH3CHO + H + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.28e+13, 'cm^3/(mol*s)'),
        n = -0.31,
        Ea = (-657.27, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 912,
    label = "A1CH3CH2 + HO2 => A1CH3* + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.13e+18, 'cm^3/(mol*s)'),
        n = -1.44,
        Ea = (13943.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 913,
    label = "A1CH3CH2 + HO2 => A1CH3 + HCO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.03e+17, 'cm^3/(mol*s)'),
        n = -1.33,
        Ea = (5903.44, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 914,
    label = "A1CH3CH2 + C3H3 => A2CH3 + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.32e+39, 'cm^3/(mol*s)'),
        n = -7.74,
        Ea = (23852.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 915,
    label = "A1CH3CHO <=> A1CHOCH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+18, 's^-1'), n=-0.6, Ea=(94787.3, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 916,
    label = "A1CH3CHO => A1- + CO + CH3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.16e+29, 's^-1'), n=-3.58, Ea=(110165, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 917,
    label = "A1CH3CHO => A1CH3* + CO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.1e+16, 's^-1'), n=0, Ea=(81740, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 918,
    label = "A1CH3CHO + H <=> A1CHOCH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.47, 'cm^3/(mol*s)'),
        n = 3.98,
        Ea = (3384.32, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 919,
    label = "A1CH3CHO + O <=> A1CHOCH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.18, 'cm^3/(mol*s)'),
        n = 4.09,
        Ea = (2545.41, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 920,
    label = "A1CH3CHO + OH <=> A1CHOCH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (177000, 'cm^3/(mol*s)'),
        n = 2.39,
        Ea = (-602.29, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 921,
    label = "A1CH3CHO + O2 <=> A1CHOCH2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.18e+07, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (46044.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 922,
    label = "A1CH3CHO + HO2 <=> A1CHOCH2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (93300, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (14684.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 923,
    label = "A1CH3CHO + CH3 <=> A1CHOCH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.22e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (22256.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 924,
    label = "A1CH3CHO + H => A1CH3* + CO + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.09e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2404.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 925,
    label = "A1CH3CHO + O => A1CH3* + CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5.84e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1809.27, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 926,
    label = "A1CH3CHO + OH => A1CH3* + CO + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.89e+08, 'cm^3/(mol*s)'),
        n = 1.35,
        Ea = (-1572.66, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 927,
    label = "A1CH3CHO + O2 => A1CH3* + CO + HO2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(120000, 'cm^3/(mol*s)'), n=2.5, Ea=(37555, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 928,
    label = "A1CH3CHO + HO2 => A1CH3* + CO + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (40900, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (10203.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 929,
    label = "A1CH3CHO + CH3 => A1CH3* + CO + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.49e-08, 'cm^3/(mol*s)'),
        n = 6.21,
        Ea = (1630.02, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 930,
    label = "A1CH3CHO + H <=> A1CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.31e+06, 'cm^3/(mol*s)'),
        n = 2.17,
        Ea = (4163.48, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 931,
    label = "A1CH3CHO + H <=> A1CHO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.31e+06, 'cm^3/(mol*s)'),
        n = 2.17,
        Ea = (4163.48, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 932,
    label = "A1CH3CHO + OH <=> HOA1CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(783, 'cm^3/(mol*s)'), n=2.88, Ea=(3221.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 933,
    label = "A1CHOCH2 + O <=> A1CHOCHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.37e+18, 'cm^3/(mol*s)'),
        n = -1.34,
        Ea = (1591.78, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Commented out by Zach Buras because 4 products not compatible with RMG library\nA1CH3CHO+OH => A1O+H+CO+CH3             7.830e+02    2.880   3221.80',
    ),
    longDesc = 
u"""
Commented out by Zach Buras because 4 products not compatible with RMG library
A1CH3CHO+OH => A1O+H+CO+CH3             7.830e+02    2.880   3221.80
""",
)

entry(
    index = 934,
    label = "A1CHOCH2 + O => A1- + CO + CH2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5.99e+23, 'cm^3/(mol*s)'),
        n = -2.47,
        Ea = (16192.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 935,
    label = "A1CHOCH2 + O <=> A1CHO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.97e+22, 'cm^3/(mol*s)'),
        n = -2.36,
        Ea = (8152.49, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 936,
    label = "A1CHOCH2 + OH => A1CHOCHO + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 937,
    label = "A1CHOCH2 + O2 <=> A1CHOCHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(138, 'cm^3/(mol*s)'), n=2.42, Ea=(7643.4, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 938,
    label = "A1CHOCH2 + HO2 => A1CHOCHO + OH + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.19e+09, 'cm^3/(mol*s)'),
        n = 1.03,
        Ea = (-2249.04, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 939,
    label = "A1CHOCHO + H => A1CHO + CO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (8.18e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2404.4, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Commented out by Zach Buras because 4 products not compatible with RMG library\nA1CHOCHO => A1-+2CO+H                   4.200e+16    0.000  81739.96',
    ),
    longDesc = 
u"""
Commented out by Zach Buras because 4 products not compatible with RMG library
A1CHOCHO => A1-+2CO+H                   4.200e+16    0.000  81739.96
""",
)

entry(
    index = 940,
    label = "A1CHOCHO + O => A1CHO + CO + O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.17e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1809.27, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 941,
    label = "A1CHOCHO + OH => A1CHO + CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5.78e+08, 'cm^3/(mol*s)'),
        n = 1.35,
        Ea = (-1572.66, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 942,
    label = "A1CHOCHO + O2 => A1CHO + CO + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(240000, 'cm^3/(mol*s)'), n=2.5, Ea=(37555, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 943,
    label = "A1CHOCHO + HO2 => A1CHO + CO + HO2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (81800, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (10203.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 944,
    label = "A1CHOCHO + CH3 => A1CHO + CO + CH3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (6.98e-08, 'cm^3/(mol*s)'),
        n = 6.21,
        Ea = (1630.02, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 945,
    label = "A1CHOCHO + H <=> A1CHO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.62e+06, 'cm^3/(mol*s)'),
        n = 2.17,
        Ea = (4163.48, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 946,
    label = "A2CH3 + H <=> A2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.31e+06, 'cm^3/(mol*s)'),
        n = 2.17,
        Ea = (4163.48, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Commented out by Zach Buras because 4 products not compatible with RMG library\nA1CHOCHO+OH => A1O+H+CO+HCO             1.570e+03    2.880   3221.80',
    ),
    longDesc = 
u"""
Commented out by Zach Buras because 4 products not compatible with RMG library
A1CHOCHO+OH => A1O+H+CO+HCO             1.570e+03    2.880   3221.80
""",
)

entry(
    index = 947,
    label = "A2CH3 + OH <=> A2OH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(783, 'cm^3/(mol*s)'), n=2.88, Ea=(3221.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 948,
    label = "A2CH3 <=> A2CH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+18, 's^-1'), n=-0.6, Ea=(94787.3, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 949,
    label = "A2CH3 <=> A2- + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+34, 's^-1'), n=-5.02, Ea=(114252, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 950,
    label = "A2CH2 + H <=> A2- + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.83e+67, 'cm^3/(mol*s)'),
        n = -14.15,
        Ea = (68329.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 951,
    label = "A2CH2 <=> C9H7 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.2e+14, 's^-1'), n=0, Ea=(80676.4, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 952,
    label = "A2CH3 + H <=> A2CH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.47, 'cm^3/(mol*s)'),
        n = 3.98,
        Ea = (3384.32, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 953,
    label = "A2CH3 + O <=> A2CH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.18, 'cm^3/(mol*s)'),
        n = 4.09,
        Ea = (2545.41, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 954,
    label = "A2CH3 + OH <=> A2CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (177000, 'cm^3/(mol*s)'),
        n = 2.39,
        Ea = (-602.29, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 955,
    label = "A2CH3 + O2 <=> A2CH2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.18e+07, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (46044.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 956,
    label = "A2CH3 + CH3 <=> A2CH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.22e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (22256.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 957,
    label = "A2CH3 + HO2 <=> A2CH2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (93300, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (14684.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 958,
    label = "A2CH3 + O => C9H7 + CH3 + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.47e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4531.55, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Commented out by Zach Buras because 4 products not compatible with RMG library\nA2CH3+O => A2+CO+2H                     1.100e+13    0.000   4531.55',
    ),
    longDesc = 
u"""
Commented out by Zach Buras because 4 products not compatible with RMG library
A2CH3+O => A2+CO+2H                     1.100e+13    0.000   4531.55
""",
)

entry(
    index = 959,
    label = "A2CH2 + O <=> A2CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.28e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 960,
    label = "A2CH2 + OH => A2CH2O + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 961,
    label = "A2CH2 + HO2 <=> A2CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.19e+09, 'cm^3/(mol*s)'),
        n = 1.03,
        Ea = (-2249.04, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 962,
    label = "A2CH2 + C3H3 => A3 + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.32e+39, 'cm^3/(mol*s)'),
        n = -7.74,
        Ea = (23852.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 963,
    label = "A2CH2 + O2 <=> A2CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.76e+15, 'cm^3/(mol*s)'),
        n = -1.55,
        Ea = (11321.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 964,
    label = "A2CH2 + O2 <=> A2O + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.08e+09, 'cm^3/(mol*s)'),
        n = 0.37,
        Ea = (16909.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 965,
    label = "A2CH2O <=> A2CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.26e+28, 's^-1'), n=-5.08, Ea=(22249, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 966,
    label = "A2CH2O <=> A2- + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.21e+33, 's^-1'), n=-6.21, Ea=(36849.9, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 967,
    label = "A2CH2O + H <=> A2CHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.33e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 968,
    label = "A2CH2O + O <=> A2CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.67e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 969,
    label = "A2CH2O + OH <=> A2CHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.33e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 970,
    label = "A2CH2O + O2 <=> A2CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.85e-13, 'cm^3/(mol*s)'),
        n = 7.6,
        Ea = (-3530.11, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 971,
    label = "A2CHO => A2- + CO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.1e+16, 's^-1'), n=0, Ea=(81740, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 972,
    label = "A2CHO + H => A2- + CO + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.09e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2404.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 973,
    label = "A2CHO + O => A2- + CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5.84e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1809.27, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 974,
    label = "A2CHO + OH => A2- + CO + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.89e+08, 'cm^3/(mol*s)'),
        n = 1.35,
        Ea = (-1572.66, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 975,
    label = "A2CHO + O2 => A2- + CO + HO2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(120000, 'cm^3/(mol*s)'), n=2.5, Ea=(37555, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 976,
    label = "A2CHO + HO2 => A2- + CO + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (40900, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (10203.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 977,
    label = "A2CHO + CH3 => A2- + CO + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.49e-08, 'cm^3/(mol*s)'),
        n = 6.21,
        Ea = (1630.02, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 978,
    label = "A1 <=> A1- + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.29e+61, 's^-1'), n=-12.48, Ea=(148086, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 979,
    label = "A1- <=> O-C6H4 + H",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.3e+12, 's^-1'), n=0.62, Ea=(77301.6, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1e+84, 'cm^3/(mol*s)'),
            n = -18.87,
            Ea = (90100.4, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.902,
        T3 = (696, 'K'),
        T1 = (358, 'K'),
        T2 = (3856, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[C-]#[O+]': 1.75, '[Ar]': 0.7},
    ),
)

entry(
    index = 980,
    label = "C4H2 + C2H2 <=> O-C6H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+78, 'cm^3/(mol*s)'),
        n = -19.31,
        Ea = (67920.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 981,
    label = "A1 + H <=> A1- + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+08, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (16352.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 982,
    label = "A1 + OH <=> A1- + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (23400, 'cm^3/(mol*s)'),
        n = 2.68,
        Ea = (733.75, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 983,
    label = "A1 + OH <=> A1OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(132, 'cm^3/(mol*s)'), n=3.25, Ea=(5590.34, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 984,
    label = "A1 + O2 <=> A1- + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.34e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (64292.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 985,
    label = "A1 + O <=> A1O + H",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (2.74e+08, 'cm^3/(mol*s)'),
                n = 1.55,
                Ea = (3090.34, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.99e+07, 'cm^3/(mol*s)'),
                n = 1.8,
                Ea = (3974.67, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 986,
    label = "A1 + O <=> A1OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.03e+12, 'cm^3/(mol*s)'),
        n = 0.3,
        Ea = (4402.49, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 987,
    label = "A1 + O <=> C5H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.8e+16, 'cm^3/(mol*s)'),
        n = -0.77,
        Ea = (15291.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 988,
    label = "A1 + O <=> A1- + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(14698.9, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 989,
    label = "A1- + O2 <=> A1O + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.57e+20, 'cm^3/(mol*s)'),
        n = -2.27,
        Ea = (7189.29, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 990,
    label = "A1- + O2 <=> OC6H4O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(8981.84, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 991,
    label = "A1- + O <=> A1O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 992,
    label = "A1- + OH <=> A1O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 993,
    label = "A1- + HO2 <=> A1O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 994,
    label = "A1- + CH4 <=> A1 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00389, 'cm^3/(mol*s)'),
        n = 4.57,
        Ea = (5258.13, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 995,
    label = "A1OH <=> C5H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.59e+15, 's^-1'), n=-0.61, Ea=(74118.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 996,
    label = "A1OH <=> A1O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.01e+71, 's^-1'), n=-15.92, Ea=(124790, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 997,
    label = "A1OH + H <=> A1O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(68.3, 'cm^3/(mol*s)'), n=3.4, Ea=(7232.31, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 998,
    label = "A1OH + OH <=> A1O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17.3, 'cm^3/(mol*s)'),
        n = 3.4,
        Ea = (-1142.45, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 999,
    label = "A1OH + CH3 <=> A1O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00037, 'cm^3/(mol*s)'),
        n = 4.7,
        Ea = (4827.92, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1000,
    label = "A1OH + O2 <=> A1O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.32e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (41400.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1001,
    label = "A1O <=> CO + C5H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+10, 's^-1'), n=0, Ea=(36424.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1002,
    label = "A1O + O <=> OC6H4O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.34e+13, 'cm^3/(mol*s)'),
        n = 0.03,
        Ea = (-394.36, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1003,
    label = "A1O + O2 <=> OC6H4O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.51e+07, 'cm^3/(mol*s)'),
        n = 1.3,
        Ea = (17667.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1004,
    label = "OC6H4O <=> C5H4O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.4e+11, 's^-1'), n=0, Ea=(59001, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1005,
    label = "OC6H4O + H <=> T-C5H5O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.3e+09, 'cm^3/(mol*s)'),
        n = 1.45,
        Ea = (3867.11, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1006,
    label = "A2 + O <=> A2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.83e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4529.16, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Commented out by Zach Buras because 4 products not compatible with RMG library\nOC6H4O+O => CH2CO+C2H2+2CO              3.000e+13    0.000   5000.00',
    ),
    longDesc = 
u"""
Commented out by Zach Buras because 4 products not compatible with RMG library
OC6H4O+O => CH2CO+C2H2+2CO              3.000e+13    0.000   5000.00
""",
)

entry(
    index = 1007,
    label = "A2 + O <=> A2OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.83e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4529.16, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1008,
    label = "A2 + OH <=> A2OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(220, 'cm^3/(mol*s)'), n=3.25, Ea=(5590.34, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1009,
    label = "A2- + O2 <=> A2O + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.57e+20, 'cm^3/(mol*s)'),
        n = -2.27,
        Ea = (7189.29, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1010,
    label = "A2* + O2 <=> A2O + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.57e+20, 'cm^3/(mol*s)'),
        n = -2.27,
        Ea = (7189.29, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1011,
    label = "A2- + O2 => C9H6O + CO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(8981.84, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1012,
    label = "A2* + O2 => C9H6O + CO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(8981.84, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1013,
    label = "A2- + O <=> A2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1014,
    label = "A2* + O <=> A2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1015,
    label = "A2- + OH <=> A2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1016,
    label = "A2* + OH <=> A2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1017,
    label = "A2OH <=> C9H8 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.62e+15, 's^-1'), n=-0.61, Ea=(74118.1, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1018,
    label = "A2OH <=> A2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.01e+71, 's^-1'), n=-15.92, Ea=(124790, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1019,
    label = "A2OH + H <=> A2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(68.3, 'cm^3/(mol*s)'), n=3.4, Ea=(7232.31, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1020,
    label = "A2OH + OH <=> A2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17.3, 'cm^3/(mol*s)'),
        n = 3.4,
        Ea = (-1142.45, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1021,
    label = "A2OH + CH3 <=> A2O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00037, 'cm^3/(mol*s)'),
        n = 4.7,
        Ea = (4827.92, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1022,
    label = "A2O <=> C9H7 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+10, 's^-1'), n=0, Ea=(36424.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1023,
    label = "A2O + O => C9H6O + CO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.68e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1024,
    label = "A2O + O2 => C9H6O + CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (6.51e+07, 'cm^3/(mol*s)'),
        n = 1.3,
        Ea = (17667.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1025,
    label = "A3- + O2 => A2C2H2B + CO + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (8.57e+20, 'cm^3/(mol*s)'),
        n = -2.27,
        Ea = (7189.29, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1026,
    label = "A3* + O2 => A2C2H2A + CO + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (8.57e+20, 'cm^3/(mol*s)'),
        n = -2.27,
        Ea = (7189.29, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1027,
    label = "A4- + O2 => A3- + CO + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (8.57e+20, 'cm^3/(mol*s)'),
        n = -2.27,
        Ea = (7189.29, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1028,
    label = "A2R5- + O2 => A2- + CO + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (8.57e+20, 'cm^3/(mol*s)'),
        n = -2.27,
        Ea = (7189.29, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1029,
    label = "A3R5- + O2 => A3- + CO + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (8.57e+20, 'cm^3/(mol*s)'),
        n = -2.27,
        Ea = (7189.29, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1030,
    label = "A3 + OH => A2C2HA + CH3 + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(110, 'cm^3/(mol*s)'), n=3.25, Ea=(5590.34, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1031,
    label = "A3 + OH => A2C2HB + CH3 + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(110, 'cm^3/(mol*s)'), n=3.25, Ea=(5590.34, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1032,
    label = "A4 + OH => A3 + HCCO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(220, 'cm^3/(mol*s)'), n=3.25, Ea=(5590.34, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1033,
    label = "A2R5 + OH => A2 + HCCO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(176, 'cm^3/(mol*s)'), n=3.25, Ea=(5590.34, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1034,
    label = "A3R5 + OH => A3 + HCCO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(220, 'cm^3/(mol*s)'), n=3.25, Ea=(5590.34, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1035,
    label = "A4R5 + OH => A4 + HCCO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(220, 'cm^3/(mol*s)'), n=3.25, Ea=(5590.34, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1036,
    label = "FLTN + OH => A3 + HCCO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(220, 'cm^3/(mol*s)'), n=3.25, Ea=(5590.34, 'cal/mol'), T0=(1, 'K')),
)

