#!/usr/bin/env python
# encoding: utf-8

name = "FFCM1(-)"
shortDesc = u""
longDesc = u"""
Foundational Fuel Chemistry Model Version 1.0 (excited species removed)
http://web.stanford.edu/group/haiwanglab/FFCM1/pages/FFCM1.html

FFCM-1
H2/CO/C1 reaction model - Chemkin form - version v1.0c 
Release date: 05/31/3016.

G. P. Smith, Y. Tao, and H. Wang, Foundational Fuel Chemistry Model Version 1.0 (FFCM-1),
http://nanoenergy.stanford.edu/ffcm1, 2016.

The following reactions involve excited CH and OH species, which currently cannot be represented in RMG.
In order to compare RMG's predictions with experimental results of excited CH or OH,
it is advised to append the following reactions to the final Chemkin file.
Note that the model generation in RMG could have been somewhat different if these reactions were to integrated as a library.
See https://github.com/ReactionMechanismGenerator/RMG-database/issues/174 for more info.

CH+O2<=>CO+OH*                                     1.800E+11    0.000        0.00
C2H+O<=>CO+CH*                                     2.500E+12    0.000        0.00
C2H+O2<=>CO2+CH*                                   3.200E+11    0.000     1600.00
H+O+M=>OH*+M                                       5.450E+12    0.000        0.00
2OH+H=>OH*+H2O                                     1.450E+15    0.000        0.00
CH*=>CH                                            1.850E+06    0.000        0.00
CH*+N2<=>CH+N2                                     3.030E+02    3.400     -381.00
CH*+O2<=>CH+O2                                     2.400E+06    2.140    -1720.00
CH*+H2O<=>CH+H2O                                   5.300E+13    0.000        0.00
CH*+H2<=>CH+H2                                     1.470E+14    0.000     1361.00
CH*+CO2<=>CH+CO2                                   2.410E-01    4.300    -1694.00
CH*+CO<=>CH+CO                                     2.440E+12    0.500        0.00
CH*+CH4<=>CH+CH4                                   1.730E+13    0.000      167.00
CH*+Ar<=>CH+Ar                                     1.250E+10    0.500        0.00
CH*+He<=>CH+He                                     1.950E+09    0.500        0.00
OH*=>OH                                            1.450E+06    0.000        0.00
OH*+N2<=>OH+N2                                     1.080E+11    0.500    -1238.00
OH*+O2<=>OH+O2                                     2.100E+12    0.500     -482.00
OH*+H2O<=>OH+H2O                                   5.920E+12    0.500     -861.00
OH*+H2<=>OH+H2                                     2.950E+12    0.500     -444.00
OH*+CO2<=>OH+CO2                                   2.750E+12    0.500     -968.00
OH*+CO<=>OH+CO                                     3.230E+12    0.500     -787.00
OH*+CH4<=>OH+CH4                                   3.360E+12    0.500     -635.00
OH*+Ar<=>OH+Ar                                     1.250E+10    0.500        0.00
OH*+He<=>OH+He                                     1.950E+09    0.500        0.00
"""

entry(
    index = 107,
    label = "CH3 + CH3 <=> C2H6",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.844e+16, 'cm^3/(mol*s)'),
            n = -0.97,
            Ea = (620, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.77e+50, 'cm^6/(mol^2*s)'),
            n = -9.67,
            Ea = (6220, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5325,
        T3 = (151, 'K'),
        T1 = (1038, 'K'),
        T2 = (4970, 'K'),
        efficiencies = {'[Ar]': 0.69, '[He]': 0.70, '[O][O]': 1.00, 'O': 6.00, '[C-]#[O+]': 1.50, 'O=C=O': 2.00, 'C': 1.99, 'C=O': 2.50, 'CO': 3.00, 'CC': 3.00},
    ),
)

entry(
    index = 33,
    label = "HCO + O <=> H + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.001e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 85,
    label = "CH2O + O2 <=> HO2 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (329700, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (36460, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 80,
    label = "HCO + H <=> CH2O",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.913e+14, 'cm^3/(mol*s)'),
            n = -0.033,
            Ea = (-142, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.19e+34, 'cm^6/(mol^2*s)'),
            n = -5.533,
            Ea = (6128, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.782,
        T3 = (271, 'K'),
        T1 = (2755, 'K'),
        T2 = (6570, 'K'),
        efficiencies = {'[Ar]': 0.79, '[He]': 0.70, 'O': 6.00, '[C-]#[O+]': 1.50, 'O=C=O': 2.00, 'C': 2.00, 'C=O': 2.84, 'CO': 3.00, 'CC': 3.00},
    ),
)

entry(
    index = 84,
    label = "CH2O + OH <=> HCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.338e+07, 'cm^3/(mol*s)'),
        n = 1.63,
        Ea = (-1055, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 82,
    label = "CH2O + H <=> HCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.149e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (2742, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 83,
    label = "CH2O + O <=> OH + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.244e+11, 'cm^3/(mol*s)'),
        n = 0.57,
        Ea = (2762, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 110,
    label = "CH3 + CH2O <=> HCO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(32.13, 'cm^3/(mol*s)'), n=3.36, Ea=(4310, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 86,
    label = "CH2O + HO2 <=> HCO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(71110, 'cm^3/(mol*s)'), n=2.5, Ea=(10210, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 111,
    label = "CH3O <=> H + CH2O",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.13e+10, 's^-1'), n=1.21, Ea=(24075, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.02e+16, 'cm^3/(mol*s)'),
            n = -0.547,
            Ea = (18024, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.341,
        T3 = (28, 'K'),
        T1 = (1000, 'K'),
        T2 = (2339, 'K'),
        efficiencies = {'[Ar]': 0.85, '[He]': 0.67, '[H][H]': 2.00, 'O': 6.00, '[C-]#[O+]': 1.50, 'O=C=O': 2.00, 'C': 2.00, 'C=O': 2.50, 'CO': 3.00},
    ),
)

entry(
    index = 119,
    label = "CH3O + O2 <=> HO2 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.32e+10, 'cm^3/(mol*s)'), n=0, Ea=(2603, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 154,
    label = "CH3OH + CH3 <=> CH3O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(21500, 'cm^3/(mol*s)'), n=2.27, Ea=(8710, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 139,
    label = "CH3OH + H <=> CH2OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.55e+06, 'cm^3/(mol*s)'),
        n = 2.351,
        Ea = (5912, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 122,
    label = "CH2OH <=> H + CH2O",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(7.37e+10, 's^-1'), n=0.811, Ea=(39580, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.01e+13, 'cm^3/(mol*s)'),
            n = 0.184,
            Ea = (17230, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.001,
        T3 = (50, 'K'),
        T1 = (600, 'K'),
        T2 = (2780, 'K'),
        efficiencies = {'[Ar]': 0.85, '[He]': 0.67, '[H][H]': 2.00, 'O': 5.97, '[C-]#[O+]': 1.50, 'O=C=O': 2.00, 'C': 2.00, 'C=O': 2.50, 'CO': 3.00},
    ),
)

entry(
    index = 129,
    label = "CH2OH + O2 <=> HO2 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.298e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3736, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 124,
    label = "CH2OH + H <=> H2 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.44e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 128,
    label = "CH2OH + OH <=> H2O + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 127,
    label = "CH2OH + O <=> OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 95,
    label = "CH3 + OH <=> CH3OH",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (6.21e+13, 'cm^3/(mol*s)'),
            n = -0.018,
            Ea = (-33, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (7.24e+36, 'cm^6/(mol^2*s)'),
            n = -6,
            Ea = (3226, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.1855,
        T3 = (156, 'K'),
        T1 = (1675, 'K'),
        T2 = (4530, 'K'),
        efficiencies = {'O': 6.00, '[C-]#[O+]': 1.50, 'O=C=O': 2.00, 'C': 2.00, 'C=O': 2.50, 'CO': 3.00, 'CC': 3.00},
    ),
)

entry(
    index = 123,
    label = "CH2OH + H <=> CH3OH",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.67e+10, 'cm^3/(mol*s)'), n=0.96, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.34e+41, 'cm^6/(mol^2*s)'),
            n = -7.38,
            Ea = (9177, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.684,
        T3 = (37050, 'K'),
        T1 = (41490, 'K'),
        T2 = (3980, 'K'),
        efficiencies = {'[Ar]': 0.70, '[He]': 0.70, 'O': 6.00, '[C-]#[O+]': 1.50, 'O=C=O': 2.00, 'C': 2.00, 'C=O': 2.50, 'CO': 3.00, 'CC': 3.00},
    ),
)

entry(
    index = 140,
    label = "CH3OH + H <=> CH3O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.49e+06, 'cm^3/(mol*s)'),
        n = 2.147,
        Ea = (11134, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 141,
    label = "CH3OH + O <=> OH + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.47e+13, 'cm^3/(mol*s)'), n=0, Ea=(5306, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 143,
    label = "CH3OH + OH <=> CH2OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (142000, 'cm^3/(mol*s)'),
        n = 2.37,
        Ea = (-965.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 144,
    label = "CH3OH + OH <=> CH3O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(16000, 'cm^3/(mol*s)'), n=2.7, Ea=(53.3, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 145,
    label = "CH3OH + O2 <=> CH2OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (358000, 'cm^3/(mol*s)'),
        n = 2.27,
        Ea = (42760, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 146,
    label = "CH3OH + HO2 <=> CH2OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.28e-05, 'cm^3/(mol*s)'),
        n = 5.06,
        Ea = (10213, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 153,
    label = "CH3OH + CH3 <=> CH2OH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(665, 'cm^3/(mol*s)'), n=3.03, Ea=(8720, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 92,
    label = "CH3 + H <=> CH4",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.801e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (7.93e+24, 'cm^6/(mol^2*s)'),
            n = -2.17,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.124,
        T3 = (1801, 'K'),
        T1 = (33.1, 'K'),
        T2 = (90000, 'K'),
        efficiencies = {'[Ar]': 0.36, '[He]': 0.42, 'N#N': 0.59, '[O][O]': 0.59, 'O': 3.42, '[C-]#[O+]': 0.89, 'O=C=O': 2.00, 'C': 2.00, 'C=O': 2.50, 'CO': 3.00, 'CC': 3.00},
    ),
)

entry(
    index = 131,
    label = "CH4 + H <=> CH3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(478100, 'cm^3/(mol*s)'), n=2.5, Ea=(9588, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 133,
    label = "CH4 + OH <=> CH3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (983900, 'cm^3/(mol*s)'),
        n = 2.182,
        Ea = (2446, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 132,
    label = "CH4 + O <=> OH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.786e+08, 'cm^3/(mol*s)'),
        n = 1.56,
        Ea = (8485, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 134,
    label = "CH4 + HO2 <=> CH3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(47780, 'cm^3/(mol*s)'), n=2.5, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 98,
    label = "CH3 + OH <=> H2 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.735e+09, 'cm^3/(mol*s)'),
        n = 0.734,
        Ea = (-2177, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 125,
    label = "CH2OH + H <=> OH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.006e+13, 'cm^3/(mol*s)'),
        n = 0.198,
        Ea = (-241, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 100,
    label = "CH3 + HO2 <=> OH + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.821e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-590, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 99,
    label = "CH3 + HO2 <=> O2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (126900, 'cm^3/(mol*s)'),
        n = 2.228,
        Ea = (-3022, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 93,
    label = "CH3 + O <=> H + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.722e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 101,
    label = "CH3 + O2 <=> O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.104e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (28297, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 102,
    label = "CH3 + O2 <=> OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(99.77, 'cm^3/(mol*s)'), n=2.86, Ea=(9768, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 243,
    label = "C2H5 + H <=> C2H6",
    degeneracy = 1,
    elementary_high_p = True,
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
        efficiencies = {'[Ar]': 0.70, '[He]': 0.70, 'O': 6.00, '[C-]#[O+]': 1.50, 'O=C=O': 2.00, 'C': 2.00, 'C=O': 2.50, 'CO': 3.00, 'CC': 3.00},
    ),
)

entry(
    index = 252,
    label = "C2H6 + H <=> C2H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.133e+08, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (7530, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 253,
    label = "C2H6 + O <=> OH + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(176300, 'cm^3/(mol*s)'), n=2.8, Ea=(5803, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 254,
    label = "C2H6 + OH <=> C2H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.463e+06, 'cm^3/(mol*s)'), n=2, Ea=(994, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 258,
    label = "C2H6 + O2 <=> C2H5 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (729000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (49160, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 257,
    label = "C2H6 + CH3 <=> C2H5 + CH4",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (5.6e+10, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (9420, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.299e+14, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (22260, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = u"""The multiArrhenius form is to capture both high and low temperature behavior""",
)

entry(
    index = 259,
    label = "C2H6 + HO2 <=> C2H5 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (110000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (16850, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 233,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.232e+09, 'cm^3/(mol*s)'),
            n = 1.463,
            Ea = (1355, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.9e+39, 'cm^6/(mol^2*s)'),
            n = -6.642,
            Ea = (5769, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1.569,
        T3 = (-9147, 'K'),
        T1 = (299, 'K'),
        T2 = (152.4, 'K'),
        efficiencies = {'[Ar]': 0.70, '[He]': 0.70, 'N#N': 0.86, 'O': 4.92, '[C-]#[O+]': 1.50, 'O=C=O': 2.00, 'C': 2.00, 'C=O': 2.50, 'CO': 3.00, 'CC': 3.00},
    ),
)

entry(
    index = 249,
    label = "C2H5 + CH3 <=> CH4 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 108,
    label = "CH3 + CH3 <=> H + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.621e+12, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (10600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 244,
    label = "C2H5 + H <=> H2 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 246,
    label = "C2H5 + O <=> H + CH3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.89e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 248,
    label = "C2H5 + O2 <=> HO2 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.355e+07, 'cm^3/(mol*s)'),
        n = 1.09,
        Ea = (-1975, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 223,
    label = "CH3CHO <=> CH3 + HCO",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(2.18e+22, 's^-1'), n=-1.74, Ea=(86364, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (9.15e+58, 'cm^3/(mol*s)'),
            n = -11.3,
            Ea = (95922, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[H][H]': 2.00, 'O': 6.00, '[C-]#[O+]': 1.50, 'O=C=O': 2.00, 'C': 2.00, 'C=O': 2.50, 'CO': 3.00, 'C#C': 3.00, 'C=C': 3.00, 'CC': 3.00},
        comment = 'Warning: SRI parameters from chemkin file ignored on import.',
    ),
    longDesc = 
u"""
Warning: SRI parameters from chemkin file ignored on import.
""",
)

entry(
    index = 224,
    label = "CH3CHO + H <=> CH2CHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.05e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2405, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 203,
    label = "CH2CHO <=> CH2CO + H",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.43e+15, 's^-1'), n=-0.15, Ea=(45606, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.44e+29, 'cm^3/(mol*s)'),
            n = -3.79,
            Ea = (43577, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.796,
        T3 = (100, 'K'),
        T1 = (50000, 'K'),
        T2 = (34204, 'K'),
        efficiencies = {'[H][H]': 2.00, 'O': 6.00, '[C-]#[O+]': 1.50, 'O=C=O': 2.00, 'C': 2.00, 'C=O': 2.50, 'CO': 3.00, 'C#C': 3.00, 'C=C': 3.00, 'CC': 3.00},
    ),
)

entry(
    index = 192,
    label = "C2H3 + H <=> C2H4",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.88e+13, 'cm^3/(mol*s)'), n=0.2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
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
        efficiencies = {'[Ar]': 0.70, '[He]': 0.70, 'O': 6.00, '[C-]#[O+]': 1.50, 'O=C=O': 2.00, 'C': 2.00, 'C=O': 2.50, 'CO': 3.00, 'CC': 3.00},
    ),
)

entry(
    index = 234,
    label = "C2H4 + H <=> C2H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (220.1, 'cm^3/(mol*s)'),
        n = 3.62,
        Ea = (11270, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 235,
    label = "C2H4 + O <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.355e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (183, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 236,
    label = "C2H4 + O <=> H + CH2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+09, 'cm^3/(mol*s)'),
        n = 0.907,
        Ea = (839, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 238,
    label = "C2H4 + OH <=> C2H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (21440, 'cm^3/(mol*s)'),
        n = 2.745,
        Ea = (2216, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 239,
    label = "C2H4 + OH <=> CH2O + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (178000, 'cm^3/(mol*s)'),
        n = 1.68,
        Ea = (2060, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 240,
    label = "C2H4 + OH <=> H + CH3CHO",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (0.0238, 'cm^3/(mol*s)'),
                n = 3.91,
                Ea = (1723, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.190e+5, 'cm^3/(mol*s)'),
                n = 2.190,
                Ea = (5256, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = u"""The multiArrhenius form is to capture both high and low temperature behavior""",
)

entry(
    index = 241,
    label = "C2H4 + CH3 <=> C2H3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+07, 'cm^3/(mol*s)'),
        n = 1.56,
        Ea = (16630, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 242,
    label = "C2H4 + O2 <=> HO2 + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(60010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 158,
    label = "CH3OH + C2H3 <=> C2H4 + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.5, 'cm^3/(mol*s)'), n=3.1, Ea=(6940, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 172,
    label = "C2H2 + H <=> C2H3",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.54e+08, 'cm^3/(mol*s)'),
            n = 1.64,
            Ea = (2096, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.63e+27, 'cm^6/(mol^2*s)'),
            n = -3.38,
            Ea = (847, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.215,
        T3 = (10.7, 'K'),
        T1 = (1043, 'K'),
        T2 = (2341, 'K'),
        efficiencies = {'[Ar]': 0.70, '[He]': 0.70, 'O': 6.00, '[C-]#[O+]': 1.50, 'O=C=O': 2.00, 'C': 2.00, 'C=O': 2.50, 'CO': 3.00, 'CC': 3.00},
    ),
)

entry(
    index = 199,
    label = "C2H3 + O2 <=> HCO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.936e+15, 'cm^3/(mol*s)'),
        n = -0.959,
        Ea = (580, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 200,
    label = "C2H3 + O2 <=> CH2CHO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.849e+09, 'cm^3/(mol*s)'),
        n = 0.923,
        Ea = (226, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 202,
    label = "C2H3 + CH3 <=> CH4 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-765, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 193,
    label = "C2H3 + H <=> H2 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 196,
    label = "C2H3 + OH <=> H2O + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 175,
    label = "C2H2 + OH <=> H + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.867, 'cm^3/(mol*s)'),
        n = 3.566,
        Ea = (-2370, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 14,
    label = "H + O2 <=> HO2",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4.565e+12, 'cm^3/(mol*s)'),
            n = 0.44,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.37e+20, 'cm^6/(mol^2*s)'),
            n = -1.72,
            Ea = (525, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (30, 'K'),
        T1 = (90000, 'K'),
        T2 = (90000, 'K'),
        efficiencies = {'[Ar]': 0.6, '[He]': 0.71, 'N#N': 0.96, '[H][H]': 1.87, '[O][O]': 0.75, 'O': 15.81, '[C-]#[O+]': 1.90, 'O=C=O': 3.45, 'C': 2.00, 'C=O': 2.50, 'CO': 3.00, 'CC': 3.00},
    ),
)

entry(
    index = 136,
    label = "CH4 + CH2(T) <=> CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.483e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (8270, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 137,
    label = "CH4 + CH2(S) <=> CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.867e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-497, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 96,
    label = "CH3 + OH <=> CH2(T) + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(44640, 'cm^3/(mol*s)'), n=2.57, Ea=(3998, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 97,
    label = "CH3 + OH <=> CH2(S) + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.81e+15, 'cm^3/(mol*s)'),
        n = -0.91,
        Ea = (546, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 50,
    label = "CH2(T) + H <=> CH3",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.13e+13, 'cm^3/(mol*s)'), n=0.32, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.39e+34, 'cm^6/(mol^2*s)'),
            n = -5.04,
            Ea = (7400, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.405,
        T3 = (258, 'K'),
        T1 = (2811, 'K'),
        T2 = (9908, 'K'),
        efficiencies = {'[Ar]': 0.70, '[He]': 0.70, 'O': 6.00, '[C-]#[O+]': 1.50, 'O=C=O': 2.00, 'C': 2.00, 'C=O': 2.50, 'CO': 3.00, 'CC': 3.00},
    ),
)

entry(
    index = 57,
    label = "CH2(T) + O2 <=> H + H + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.844e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 51,
    label = "CH2(T) + O <=> H + H + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 53,
    label = "CH2(T) + OH <=> CH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (863000, 'cm^3/(mol*s)'),
        n = 2.02,
        Ea = (6776, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 68,
    label = "CH2(S) + H <=> CH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 44,
    label = "CH + O2 <=> O + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.84e+08, 'cm^3/(mol*s)'),
        n = 1.43,
        Ea = (1200, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 38,
    label = "CH + H <=> C(T) + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.089e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)


entry(
    index = 39,
    label = "CH + O <=> H + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 40,
    label = "CH + OH <=> H + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 43,
    label = "CH + H2O <=> H + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.43e+12, 'cm^3/(mol*s)'), n=0, Ea=(-884, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 49,
    label = "CH + CO2 <=> HCO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.38e+07, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (-715, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 256,
    label = "C2H6 + CH2(S) <=> CH3 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(-660, 'cal/mol'), T0=(1, 'K')),
)


entry(
    index = 182,
    label = "CH2CO + H <=> HCCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (11850, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 185,
    label = "CH2CO + O <=> CH2(T) + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.08e+12, 'cm^3/(mol*s)'), n=0, Ea=(1351, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 184,
    label = "CH2CO + O <=> OH + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(10300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 130,
    label = "CH2OH + CH3 <=> CH4 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 135,
    label = "CH4 + CH <=> H + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(-397, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 105,
    label = "CH3 + CH2(T) <=> H + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.824e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 106,
    label = "CH3 + CH2(S) <=> H + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(-497, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 194,
    label = "C2H3 + H <=> H2CC + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.893e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 159,
    label = "C2H + H <=> C2H2",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.25e+13, 'cm^3/(mol*s)'), n=0.32, Ea=(0, 'cal/mol'), T0=(1, 'K')),
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
        efficiencies = {'[Ar]': 0.70, '[He]': 0.70, 'O': 6.00, '[C-]#[O+]': 1.50, 'O=C=O': 2.00, 'C': 2.00, 'C=O': 2.50, 'CO': 3.00, 'CC': 3.00},
    ),
)

entry(
    index = 160,
    label = "C2H + O <=> CH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 161,
    label = "C2H + OH <=> H + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 163,
    label = "C2H + O2 <=> HCO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.63e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 162,
    label = "C2H + H2 <=> H + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.11e+06, 'cm^3/(mol*s)'),
        n = 2.32,
        Ea = (882, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 171,
    label = "C2H2 <=> H2CC",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(8e+14, 's^-1'), n=-0.52, Ea=(50750, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.45e+15, 'cm^3/(mol*s)'),
            n = -0.64,
            Ea = (49700, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[Ar]': 0.69, '[He]': 0.70, 'O': 6.00, '[C-]#[O+]': 1.50, 'O=C=O': 2.00, 'C': 2.00, 'C=O': 2.50, 'CO': 3.00, 'CC': 3.00},
    ),
)

entry(
    index = 174,
    label = "C2H2 + O <=> CO + CH2(T)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.304e+08, 'cm^3/(mol*s)'),
        n = 1.4,
        Ea = (2206, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 173,
    label = "C2H2 + O <=> H + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.679e+08, 'cm^3/(mol*s)'),
        n = 1.4,
        Ea = (2206, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)


