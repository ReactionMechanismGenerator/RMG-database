#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 5,
    label = "NO + O2 <=> NO3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (117000, 'm^3/(mol*s)', '*|/', -1),
        n = 0,
        Ea = (13.386, 'kJ/mol', '+|-', -0.001),
        T0 = (1, 'K'),
        Tmin = (473, 'K'),
        Tmax = (703, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (33600, 'Pa'),
    ),
    reference = Article(
        authors = ['Ashmore, P.G.', 'Burnett, M.G.'],
        title = 'Concurrent molecular and free radical mechanisms in the thermal decomposition of nitrogen dioxide',
        journal = 'J. Chem. Soc. Faraday Trans. 2',
        volume = '58',
        pages = '253',
        year = '1962',
        url = 'http://kinetics.nist.gov/kinetics/Detail?id=1962ASH/BUR253:5',
    ),
    referenceType = "experiment",
    rank = 10,
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
Uncertainty: 3.0
Bath gas: NO2
Excitation technique: Thermal
Analytical technique: Pressure measurement

Bad `Group additivity` performance for NO and NO3 thermo. Thermo from `thermo_DFT_CCSDTF12_BAC` could help. 
""",
)

entry(
    index = 7,
    label = "C5H5 + C2H5 <=> C7H10",
    degeneracy = 5.0,
    kinetics = Arrhenius(
        A = (8.34e+15, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (-0.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: ethyl + CPDyl <=> ethylCPD

Thermo data for C5H5 diverges for `SABIC_aromatics`, `Group additivity`, `bio_oil`, `vinylCPD_H`. Thermo data for C7H10 from group additivity.
""",
)

entry(
    index = 12,
    label = "C5H5 + CH3 <=> C6H8",
    degeneracy = 5.0,
    kinetics = Arrhenius(
        A = (1.623e+17, 'cm^3/(mol*s)'),
        n = -1.07,
        Ea = (0.002, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Krasnoukhov, V. S.', 'Porfiriev, D. P.', 'Zavershinskiy, I. P.', 'Azyazov, V. N.', 'Mebel, A. M.'],
        title = 'Kinetics of the CH3 + C5H5 Reaction: A Theoretical Study',
        journal = 'The Journal of Physical Chemistry A',
        volume = '121 (48)',
        pages = '9191-9200',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc =
u"""
CCSD(T)-F12/cc-pVTZ-f12//B2PLYPD3/aug-cc-pVDZ

Thermo data for C5H5 diverges for `SABIC_aromatics`, `Group additivity`, `bio_oil`, `vinylCPD_H`. Thermo data for C6H8 from group additivity.
""",
)

entry(
    index = 20,
    label = "CN + NCN <=> NCNCN",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.01e+09, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-34691, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (2000, 'K'),
        Tmax = (4000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc =
u"""
See Table 1 on p. 2397 in L.V Moskaleva, M.C. Lin, Proceedings of the Combustion Institute, 2000, 28(2), 2393-2401, doi: 10.1016/S0082-0784(00)80652-9
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory

Bad `Group additivity` for CN, NCN, and only `Group additivity` available for NCNCN.
""",
)

entry(
    index = 32,
    label = "C10H9 <=> C10H8 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.89e+16, 's^-1'), n=-0.28, Ea=(68.378, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc =
u"""
Taken from entry: W111 <=> P114 + H

Backward reaction violates the collision limit using thermo data from the `SABIC_aromatics` library.
""",
)

entry(
    index = 50,
    label = "C4H5-2 + H <=> C4H6-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.25e+14, 'cm^3/(mol*s)'),
        n = -0.119,
        Ea = (-1.012, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['Huang, C.', 'Yang, B.', 'Zhang, F.'],
        title = 'Initiation mechanism of 1,3-butadiene combustion and its effect on soot precursors',
        journal = 'Combustion and Flame',
        volume = '184',
        pages = '167-175',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
CCSD(T)-F12/cc-pVTZ-F12//QCISD/6-311++G(2df,2p)

Diverging heat capacity profiles for C4H5-2 and C4H6-3 from library values and `Group additivity`.
""",
)

entry(
    index = 134,
    label = "C5H5 + H <=> C5H6",
    degeneracy = 5.0,
    kinetics = Arrhenius(
        A = (2.5e+15, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""From 2001 Roy IJCK high-P value""",
    longDesc =
u"""
Converted to training reaction from rate rule: C_rad_cyclopentadiene;H_rad

Thermo data for C5H5 diverges for `SABIC_aromatics`, `Group additivity`, `bio_oil`, `vinylCPD_H`.
""",
)

entry(
    index = 135,
    label = "C5H5 + CH3 <=> C6H8",
    degeneracy = 5.0,
    kinetics = Arrhenius(
        A = (4.17e+16, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (2.092, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Sharma J. Phys. Chem. A 113 8871 - 8882 (2009)""",
    longDesc =
u"""
Converted to training reaction from rate rule: C_rad_cyclopentadiene;C_methyl

Thermo data for C5H5 diverges for `SABIC_aromatics`, `Group additivity`, `bio_oil`, `vinylCPD_H`. `Group additivity` for C6H8.
""",
)

entry(
    index = 136,
    label = "C5H5 + C5H5 <=> C10H10-6",
    degeneracy = 12.5,
    kinetics = Arrhenius(
        A = (6.25e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 11,
    shortDesc = u"""A. G. Vandeputte estimated value""",
    longDesc =
u"""
Converted to training reaction from rate rule: C_rad_cyclopentadiene;C_rad_cyclopentadiene

Thermo data for C5H5 diverges for `SABIC_aromatics`, `Group additivity`, `bio_oil`, `vinylCPD_H`. 
""",
)

entry(
    index = 140,
    label = "H + SH <=> H2S-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.77e+15, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1.79912, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""GA Jonas x 3 for spinorbit""",
    longDesc = 
u"""
Converted to training reaction from rate rule: H_rad;SsJ-H

Bad `Group additivity` thermo for SH.
""",
)

