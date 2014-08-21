#!/usr/bin/env python
# encoding: utf-8

name = "2+2_cycloaddition_Cd/NIST"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "C4H8 <=> C2H4 + C2H4",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (3.16e+16, 's^-1'),
        n = 0,
        Ea = (274.378, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (969, 'K'),
        Tmax = (1280, 'K'),
        Pmin = (26.66, 'Pa'),
        Pmax = (26.66, 'Pa'),
    ),
    reference = Article(
        authors = ["Beadle, P.C.", "Golden, D.M.", "King, K.D.", "Benson, S.W."],
        title = u'Pyrolysis of Cyclobutane',
        journal = "J. Am. Chem. Soc.",
        volume = "94",
        pages = """2943""",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972BEA/GOL2943:2",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00006456
Bath gas: Ar
""",
)

entry(
    index = 2,
    label = "C4H8 <=> C2H4 + C2H4",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (3.98e+15, 's^-1'),
        n = 0,
        Ea = (261.906, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (644, 'K'),
        Tmax = (1089, 'K'),
        Pmin = (2133, 'Pa'),
        Pmax = (307000, 'Pa'),
    ),
    reference = Article(
        authors = ["Lewis, D.K.", "Bergmann, J.", "Manjoney, R.", "Paddock, R.", "Kaira, B.L."],
        title = u'Rates of reactions of cyclopropane, cyclobutane, cyclopentene, and cyclohexene in the presence of boron trichloride',
        journal = "J. Phys. Chem.",
        volume = "88",
        pages = """4112""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984LEW/BER4112:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00006456
Bath gas: Cyclobutane
Pressure dependence: None reported
Experimental procedure: Other
Excitation technique: Thermal
Time resolution: By end product analysis
Analytical technique: Gas chromatography

Two experimental set-ups were used: experiments at 644-750 K and 16-25 torr were performed in a static reactor, while the shock tube methodology was used at 939-1089 K with shock pressures of about 2-3 atm. The rate parameters are from the literature but provide an excellent fit to the present data.
""",
)

entry(
    index = 3,
    label = "C4H8 <=> C2H4 + C2H4",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (1.52e+14, 's^-1'),
        n = 0,
        Ea = (229.479, 'kJ/mol', '+|-', 11.474),
        T0 = (1, 'K'),
        Tmin = (891, 'K'),
        Tmax = (1080, 'K'),
        Pmin = (18000, 'Pa'),
        Pmax = (110000, 'Pa'),
    ),
    reference = Article(
        authors = ["Barnard, J.A.", "Cocks, A.T.", "Lee, R.K.Y."],
        title = u'Kinetics of the Thermal Unimolecular Reactions of Cyclopropane and Cyclobutane behind Reflected Shock Waves',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "70",
        pages = """1782""",
        year = "1974",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1974BAR/COC1782:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00006456
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 4,
    label = "C4H8 <=> C2H4 + C2H4",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (2.63e+15, 's^-1'),
        n = 0,
        Ea = (259.412, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (969, 'K'),
        Tmax = (1280, 'K'),
        Pmin = (26.66, 'Pa'),
        Pmax = (26.66, 'Pa'),
    ),
    reference = Article(
        authors = ["Beadle, P.C.", "Golden, D.M.", "King, K.D.", "Benson, S.W."],
        title = u'Pyrolysis of Cyclobutane',
        journal = "J. Am. Chem. Soc.",
        volume = "94",
        pages = """2943""",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972BEA/GOL2943:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00006456
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 5,
    label = "C4H8 <=> C2H4 + C2H4",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (7.01e+15, 's^-1', '+|-', 7e+13),
        n = 0,
        Ea = (264.4, 'kJ/mol', '+|-', 1.255),
        T0 = (1, 'K'),
        Tmin = (683, 'K'),
        Tmax = (773, 'K'),
        Pmin = (13.33, 'Pa'),
        Pmax = (2666, 'Pa'),
    ),
    reference = Article(
        authors = ["Vreeland, R.W.", "Swinehart, D.F."],
        title = u'A mass spectometric investigation of the thermal decomposition of cyclobutane at low pressures',
        journal = "J. Am. Chem. Soc.",
        volume = "85",
        pages = """3349-3353""",
        year = "1963",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1963VRE/SWI3349-3353:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00006456
Bath gas: Cyclobutane
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 6,
    label = "C4H8 <=> C2H4 + C2H4",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (4.2e+15, 's^-1', '+|-', 8.4e+13),
        n = 0,
        Ea = (261.906, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (690, 'K'),
        Tmax = (733, 'K'),
        Pmin = (86700, 'Pa'),
        Pmax = (200000, 'Pa'),
    ),
    reference = Article(
        authors = ["Carr, R.W., Jr.", "Walters, W.D."],
        title = u'The thermal decomposition of cyclobutane',
        journal = "J. Phys. Chem.",
        volume = "67",
        pages = """1370-1372""",
        year = "1963",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1963CAR/WAL1370-1372:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00006456
Bath gas: Cyclobutane
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 7,
    label = "C4H8 <=> C2H4 + C2H4",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (2e+15, 's^-1', '*|/', 10),
        n = 0,
        Ea = (257.749, 'kJ/mol', '+|-', 10.31),
        T0 = (1, 'K'),
        Tmin = (671, 'K'),
        Tmax = (723, 'K'),
        Pmin = (13.33, 'Pa'),
        Pmax = (5733, 'Pa'),
    ),
    reference = Article(
        authors = ["Butler, J.N.", "Ogawa, R.B."],
        title = u'The thermal decomposition of cyclobutane at low pressures',
        journal = "J. Am. Chem. Soc.",
        volume = "85",
        pages = """3346-3349""",
        year = "1963",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1963BUT/OGA3346-3349:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00006456
Uncertainty: 10.0
Bath gas: Cyclobutane
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 8,
    label = "C4H8 <=> C2H4 + C2H4",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (4e+15, 's^-1'),
        n = 0,
        Ea = (261.906, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (693, 'K'),
        Tmax = (741, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (133000, 'Pa'),
    ),
    reference = Article(
        authors = ["Genaux, C.T.", "Kern, F.", "Walters, W.D."],
        title = u'The thermal decomposition of cyclobutane',
        journal = "J. Am. Chem. Soc.",
        volume = "75",
        pages = """6196-6199""",
        year = "1953",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1953GEN/KER6196-6199:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00006456
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00006456/rk00000001.xml
Bath gas: Cyclobutane
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 9,
    label = "C4H8 <=> C2H4 + C2H4",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (1.95e+20, 's^-1'),
        n = -1.26,
        Ea = (283.215, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Sirjean, B.", "Glaude, P.A.", "Ruiz-Lopez, M.F.", "Fournet, R."],
        title = u'Detailed kinetic study of the ring opening of cycloalkanes by CBS-QB3 calculations',
        journal = "J. Phys. Chem. A",
        volume = "110",
        pages = """12693-12704""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006SIR/GLA12693-12704:17",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00006456
Pressure dependence: None reported

Reaction potential energy surface was studied using quantum chemistry and rate constants were calculated using transition state theory. This is the rate expression for the "global" reaction proceeding via formation of a biradical intermediate.
""",
)

entry(
    index = 10,
    label = "C4H8 <=> C2H4 + C2H4",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (3.31e+21, 's^-1'),
        n = -1.61,
        Ea = (285.181, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Sirjean, B.", "Glaude, P.A.", "Ruiz-Lopez, M.F.", "Fournet, R."],
        title = u'Detailed kinetic study of the ring opening of cycloalkanes by CBS-QB3 calculations',
        journal = "J. Phys. Chem. A",
        volume = "110",
        pages = """12693-12704""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006SIR/GLA12693-12704:18",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00006456
Pressure dependence: None reported

Reaction potential energy surface was studied using quantum chemistry and rate constants were calculated using transition state theory. This is the rate expression for the "global" reaction proceeding via formation of a biradical intermediate.
""",
)

entry(
    index = 11,
    label = "C2H4 + C2H4 <=> C4H8",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (69200, 'm^3/(mol*s)'),
        n = 0,
        Ea = (182.918, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (723, 'K'),
        Tmax = (786, 'K'),
        Pmin = (40000, 'Pa'),
        Pmax = (173000, 'Pa'),
    ),
    reference = Article(
        authors = ["Quick, L.M.", "Knecht, D.A.", "Back, M.H."],
        title = u'Kinetics of the Formation of Cyclobutane from Ethylene',
        journal = "Int. J. Chem. Kinet.",
        volume = "4",
        pages = """61""",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972QUI/KNE61:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00006456
Bath gas: C2H4
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 12,
    label = "C3H6O <=> C2H4 + CH2O",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.63e+15, 's^-1', '*|/', 2.04),
        n = 0,
        Ea = (259.412, 'kJ/mol', '+|-', 2.594),
        T0 = (1, 'K'),
        Tmin = (668, 'K'),
        Tmax = (758, 'K'),
        Pmin = (99.99, 'Pa'),
        Pmax = (6999, 'Pa'),
    ),
    reference = Article(
        authors = ["Zalotai, L.", "Hunyadi-Zoltan, Zs.", "Berces, T.", "Marta, F."],
        title = u'Kinetics of gas phase decomposition of oxetan and oxetan-2,2-d2',
        journal = "Int. J. Chem. Kinet.",
        volume = "15",
        pages = """505""",
        year = "1983",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1983ZAL/HUN505:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00007176
Uncertainty: 2.04
Bath gas: Oxetane
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 13,
    label = "C3H6O <=> C2H4 + CH2O",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (5.13e+15, 's^-1', '*|/', 2.04),
        n = 0,
        Ea = (263.569, 'kJ/mol', '+|-', 2.636),
        T0 = (1, 'K'),
        Tmin = (693, 'K'),
        Tmax = (753, 'K'),
        Pmin = (53.33, 'Pa'),
        Pmax = (15600, 'Pa'),
    ),
    reference = Article(
        authors = ["Holbrook, K.A.", "Scott, R.A."],
        title = u'Gas-phase Thermal Unimolecular Decomposition of Oxetan',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "71",
        pages = """1849""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975HOL/SCO1849:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00007176
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007176/rk00000001.xml
Uncertainty: 2.04
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 14,
    label = "C5H10 <=> C3H6 + C2H4",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1.06e+16, 's^-1', '+|-', 9.5e+14),
        n = 0,
        Ea = (264.4, 'kJ/mol', '+|-', 1.255),
        T0 = (1, 'K'),
        Tmin = (683, 'K'),
        Tmax = (763, 'K'),
        Pmin = (1.33, 'Pa'),
        Pmax = (1333, 'Pa'),
    ),
    reference = Article(
        authors = ["Thomas, T.F.", "Conn, P.J.", "Swinehart, D.F."],
        title = u'Unimolecular reactions of methylcyclobutane at low pressures',
        journal = "J. Am. Chem. Soc.",
        volume = "91",
        pages = """7611-7616""",
        year = "1969",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1969THO/CON7611-7616:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00008107
Bath gas: Methylcyclobutane
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 15,
    label = "C5H10 <=> C3H6 + C2H4",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1.9e+15, 's^-1'),
        n = 0,
        Ea = (254.423, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (693, 'K'),
        Tmax = (703, 'K'),
        Pmin = (933, 'Pa'),
        Pmax = (55600, 'Pa'),
    ),
    reference = Article(
        authors = ["Pataracchia, A.F.", "Walters, W.D."],
        title = u'The thermal decomposition of methylcyclobutane at low pressures',
        journal = "J. Phys. Chem.",
        volume = "68",
        pages = """3894-3899""",
        year = "1964",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1964PAT/WAL3894-3899:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00008107
Bath gas: Methylcyclobutane
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 16,
    label = "C5H10 <=> C3H6 + C2H4",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (2.4e+15, 's^-1'),
        n = 0,
        Ea = (256.086, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (683, 'K'),
        Tmax = (723, 'K'),
        Pmin = (933, 'Pa'),
        Pmax = (55600, 'Pa'),
    ),
    reference = Article(
        authors = ["Das, M.N.", "Walters, W.D."],
        title = u'The thermal decomposition of methylcyclobutane',
        journal = "Z. Phys. Chem. (Neue Folge)",
        volume = "15",
        pages = """22-33""",
        year = "1958",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1958DAS/WAL22-33:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00008107
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008107/rk00000001.xml
Bath gas: Methylcyclobutane
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 17,
    label = "C4H6O <=> C2H4 + C2H2O",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (5e+14, 's^-1'),
        n = 0,
        Ea = (220.334, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (650, 'K'),
        Tmax = (1250, 'K'),
        Pmin = (440, 'Pa'),
        Pmax = (1307, 'Pa'),
    ),
    reference = Article(
        authors = ["Braun, W.", "McNesby, J.R.", "Scheer, M.D."],
        title = u'A comparative rate method for the study of unimolecular falloff behavior',
        journal = "J. Phys. Chem.",
        volume = "88",
        pages = """1846""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984BRA/MCN1846:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00009414
Bath gas: SF6
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 18,
    label = "C4H6O <=> C2H4 + C2H2O",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (3.6e+14, 's^-1'),
        n = 0,
        Ea = (217.008, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (633, 'K'),
        Tmax = (679, 'K'),
        Pmin = (200, 'Pa'),
        Pmax = (5066, 'Pa'),
    ),
    reference = Article(
        authors = ["McGee, T.H.", "Schleifer, A."],
        title = u'Thermal Decomposition of Cyclobutanone',
        journal = "J. Phys. Chem.",
        volume = "76",
        pages = """963""",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972MCG/SCH963:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009414
Bath gas: Cyclobutanone
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 19,
    label = "C4H6O <=> C2H4 + C2H2O",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (3.6e+14, 's^-1'),
        n = 0,
        Ea = (217.839, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (606, 'K'),
        Tmax = (646, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (11700, 'Pa'),
    ),
    reference = Article(
        authors = ["Das, M.N.", "Kern, F.", "Coyle, T.D.", "Walters, W.D."],
        title = u'The thermal decomposition of cyclobutanone',
        journal = "J. Am. Chem. Soc.",
        volume = "76",
        pages = """6271-6274""",
        year = "1954",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1954DAS/KER6271-6274:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009414
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009414/rk00000001.xml
Bath gas: Cyclobutanone
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 20,
    label = "C4H8O <=> C3H6 + CH2O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.39e+14, 's^-1', '*|/', 1.45),
        n = 0,
        Ea = (249.434, 'kJ/mol', '+|-', 2.494),
        T0 = (1, 'K'),
        Tmin = (659, 'K'),
        Tmax = (757, 'K'),
        Pmin = (1400, 'Pa'),
        Pmax = (1400, 'Pa'),
    ),
    reference = Article(
        authors = ["Zalotai, L.", "Berces, T.", "Marta, F."],
        title = u'Collisional energy transfer in the decomposition of 2-methyloxetane and 3-methyloxetane, I. Gas/gas collisions',
        journal = "React. Kinet. Catal. Lett.",
        volume = "42",
        pages = """79""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990ZAL/BER79:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010718
Uncertainty: 1.45
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 21,
    label = "C4H8O <=> C3H6 + CH2O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.39e+14, 's^-1', '*|/', 1.32),
        n = 0,
        Ea = (249.434, 'kJ/mol', '+|-', 2.494),
        T0 = (1, 'K'),
        Tmin = (660, 'K'),
        Tmax = (760, 'K'),
        Pmin = (1400, 'Pa'),
        Pmax = (3000, 'Pa'),
    ),
    reference = Article(
        authors = ["Zalotai, L.", "Berces, T.", "Marta, F."],
        title = u'Kinetics and energy transfer in the thermal decomposition of 2-methyloxetane and 3-methyloxetane',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "86",
        pages = """21""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990ZAL/BER21:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010718
Uncertainty: 1.3200001
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 22,
    label = "C4H8O <=> C3H6 + CH2O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.4e+14, 's^-1'),
        n = 0,
        Ea = (249.434, 'kJ/mol', '+|-', 4.997),
        T0 = (1, 'K'),
        Tmin = (730, 'K'),
        Tmax = (756, 'K'),
        Pmin = (800, 'Pa'),
        Pmax = (1893, 'Pa'),
    ),
    reference = Article(
        authors = ["Hammonds, P.", "Holbrook, K.A."],
        title = u'Thermolyses of 2-Methyloxetan and 2,2-Dimethyloxetan',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "78",
        pages = """2195""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982HAM/HOL2195:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010718
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010718/rk00000001.xml
Bath gas: Oxetane, 2-methyl-
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 23,
    label = "C4H8O <=> C2H4 + C2H4O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.68e+15, 's^-1', '*|/', 1.48),
        n = 0,
        Ea = (269.389, 'kJ/mol', '+|-', 2.702),
        T0 = (1, 'K'),
        Tmin = (659, 'K'),
        Tmax = (757, 'K'),
        Pmin = (1400, 'Pa'),
        Pmax = (1400, 'Pa'),
    ),
    reference = Article(
        authors = ["Zalotai, L.", "Berces, T.", "Marta, F."],
        title = u'Collisional energy transfer in the decomposition of 2-methyloxetane and 3-methyloxetane, I. Gas/gas collisions',
        journal = "React. Kinet. Catal. Lett.",
        volume = "42",
        pages = """79""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990ZAL/BER79:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010719
Uncertainty: 1.48
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 24,
    label = "C4H8O <=> C2H4 + C2H4O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.68e+15, 's^-1', '*|/', 1.48),
        n = 0,
        Ea = (269.389, 'kJ/mol', '+|-', 2.702),
        T0 = (1, 'K'),
        Tmin = (660, 'K'),
        Tmax = (760, 'K'),
        Pmin = (1400, 'Pa'),
        Pmax = (3000, 'Pa'),
    ),
    reference = Article(
        authors = ["Zalotai, L.", "Berces, T.", "Marta, F."],
        title = u'Kinetics and energy transfer in the thermal decomposition of 2-methyloxetane and 3-methyloxetane',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "86",
        pages = """21""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990ZAL/BER21:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010719
Uncertainty: 1.48
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 25,
    label = "C4H8O <=> C2H4 + C2H4O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.36e+14, 's^-1'),
        n = 0,
        Ea = (249.434, 'kJ/mol', '+|-', 4.997),
        T0 = (1, 'K'),
        Tmin = (703, 'K'),
        Tmax = (756, 'K'),
        Pmin = (800, 'Pa'),
        Pmax = (1893, 'Pa'),
    ),
    reference = Article(
        authors = ["Hammonds, P.", "Holbrook, K.A."],
        title = u'Thermolyses of 2-Methyloxetan and 2,2-Dimethyloxetan',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "78",
        pages = """2195""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982HAM/HOL2195:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010719
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010719/rk00000001.xml
Bath gas: Oxetane, 2-methyl-
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 26,
    label = "C4H8O-2 <=> C3H6 + CH2O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.4e+15, 's^-1', '*|/', 1.86),
        n = 0,
        Ea = (258.58, 'kJ/mol', '+|-', 2.586),
        T0 = (1, 'K'),
        Tmin = (660, 'K'),
        Tmax = (760, 'K'),
        Pmin = (2000, 'Pa'),
        Pmax = (3000, 'Pa'),
    ),
    reference = Article(
        authors = ["Zalotai, L.", "Berces, T.", "Marta, F."],
        title = u'Kinetics and energy transfer in the thermal decomposition of 2-methyloxetane and 3-methyloxetane',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "86",
        pages = """21""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990ZAL/BER21:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010716
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010716/rk00000001.xml
Uncertainty: 1.86
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 27,
    label = "C5H8O <=> C3H6 + C2H2O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.74e+14, 's^-1', '*|/', 1.12),
        n = 0,
        Ea = (200.379, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (552, 'K'),
        Tmax = (606, 'K'),
        Pmin = (120, 'Pa'),
        Pmax = (1880, 'Pa'),
    ),
    reference = Article(
        authors = ["Frey, H.M.", "Watts, H.P.", "Stevens, I.D.R."],
        title = u'The thermal unimolecular decomposition of 3-methylcyclobutanone',
        journal = "J. Chem. Soc. Faraday Trans. 2",
        volume = "83",
        pages = """601""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987FRE/WAT601:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009420
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009420/rk00000001.xml
Uncertainty: 1.12
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 28,
    label = "C6H10 <=> C4H6 + C2H4",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (3.16e+14, 's^-1'),
        n = 0,
        Ea = (208.693, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (839, 'K'),
        Tmax = (965, 'K'),
        Pmin = (14700, 'Pa'),
        Pmax = (26700, 'Pa'),
    ),
    reference = Article(
        authors = ["Lewis, D.K.", "Charney, D.J.", "Kalra, B.L.", "Plate, A-M.", "Woodard, M.H."],
        title = u'Kinetics of the thermal isomerizations of gaseous vinylcyclopropane and vinylcyclobutane',
        journal = "J. Phys. Chem. A",
        volume = "101",
        pages = """4097-4102""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997LEW/CHA4097-4102:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011373
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 29,
    label = "C6H10 <=> C4H6 + C2H4",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (7.41e+14, 's^-1', '*|/', 1.17),
        n = 0,
        Ea = (212.019, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (569, 'K'),
        Tmax = (639, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (1800, 'Pa'),
    ),
    reference = Article(
        authors = ["Frey, H.M.", "Pottinger, R."],
        title = u'Thermal unimolecular reactions of vinylcyclobutane and isopropenylcyclobutane',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "74",
        pages = """1827""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978FRE/POT1827:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011373
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011373/rk00000001.xml
Uncertainty: 1.17
Bath gas: Ethenylcyclobutane
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 30,
    label = "C5H10O <=> C3H6O-2 + C2H4",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1.51e+15, 's^-1', '*|/', 3.31),
        n = 0,
        Ea = (256.086, 'kJ/mol', '+|-', 7.683),
        T0 = (1, 'K'),
        Tmin = (692, 'K'),
        Tmax = (735, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (2133, 'Pa'),
    ),
    reference = Article(
        authors = ["Dirjal, N.K.", "Holbrook, K.A."],
        title = u'Thermal unimolecular decomposition of cyclobutanemethanol',
        journal = "J. Chem. Soc. Faraday Trans.",
        volume = "87",
        pages = """691-693""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991DIR/HOL691-693:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00012719
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012719/rk00000001.xml
Uncertainty: 3.3099999
Bath gas: Cyclobutanemethanol
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 31,
    label = "C6H12 <=> C4H8-2 + C2H4",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (3.6e+15, 's^-1'),
        n = 0,
        Ea = (259.412, 'kJ/mol', '+|-', 5.188),
        T0 = (1, 'K'),
        Tmin = (693, 'K'),
        Tmax = (733, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (26700, 'Pa'),
    ),
    reference = Article(
        authors = ["Wellman, R.E.", "Walters, W.D."],
        title = u'The thermal decomposition of ethylcyclobutane',
        journal = "J. Am. Chem. Soc.",
        volume = "79",
        pages = """1542-1546""",
        year = "1957",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1957WEL/WAL1542-1546:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00012797
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012797/rk00000001.xml
Bath gas: Cyclobutane, ethyl-
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 32,
    label = "C5H10O-2 <=> C4H8-3 + CH2O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.02e+13, 's^-1'),
        n = 0,
        Ea = (221.996, 'kJ/mol', '+|-', 2.22),
        T0 = (1, 'K'),
        Tmin = (675, 'K'),
        Tmax = (744, 'K'),
        Pmin = (960, 'Pa'),
        Pmax = (1227, 'Pa'),
    ),
    reference = Article(
        authors = ["Hammonds, P.", "Holbrook, K.A."],
        title = u'Thermolyses of 2-Methyloxetan and 2,2-Dimethyloxetan',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "78",
        pages = """2195""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982HAM/HOL2195:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00012962
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012962/rk00000001.xml
Bath gas: Oxetane, 2,2-dimethyl-
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 33,
    label = "C5H10O-2 <=> C2H4 + C3H6O-3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.63e+15, 's^-1'),
        n = 0,
        Ea = (270.22, 'kJ/mol', '+|-', 5.413),
        T0 = (1, 'K'),
        Tmin = (675, 'K'),
        Tmax = (744, 'K'),
        Pmin = (960, 'Pa'),
        Pmax = (1227, 'Pa'),
    ),
    reference = Article(
        authors = ["Hammonds, P.", "Holbrook, K.A."],
        title = u'Thermolyses of 2-Methyloxetan and 2,2-Dimethyloxetan',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "78",
        pages = """2195""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982HAM/HOL2195:7",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00012963
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012963/rk00000001.xml
Bath gas: Oxetane, 2,2-dimethyl-
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 34,
    label = "C5H10O-3 <=> C4H8-3 + CH2O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.8e+15, 's^-1', '+|-', 1.1e+14),
        n = 0,
        Ea = (253.591, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (673, 'K'),
        Tmax = (723, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (9733, 'Pa'),
    ),
    reference = Article(
        authors = ["Cohoe, G.F.", "Walters, W.D."],
        title = u'The kinetics of the thermal decomposition of 3,3-dimethyloxetane',
        journal = "J. Phys. Chem.",
        volume = "71",
        pages = """2326-2331""",
        year = "1967",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1967COH/WAL2326-2331:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00013035
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013035/rk00000001.xml
Bath gas: Oxetane, 3,3-dimethyl-
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 35,
    label = "C5H8O-2 <=> C3H4O + C2H4",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (2.7e+14, 's^-1', '+|-', 1.1e+13),
        n = 0,
        Ea = (222.828, 'kJ/mol', '+|-', 2.228),
        T0 = (1, 'K'),
        Tmin = (633, 'K'),
        Tmax = (673, 'K'),
        Pmin = (1200, 'Pa'),
        Pmax = (4666, 'Pa'),
    ),
    reference = Article(
        authors = ["Roquitte, B.C.", "Walters, W.D."],
        title = u'The thermal decomposition of cyclobutanecarboxaldehyde',
        journal = "J. Am. Chem. Soc.",
        volume = "84",
        pages = """4049-4052""",
        year = "1962",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1962ROQ/WAL4049-4052:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011611
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011611/rk00000001.xml
Bath gas: Cyclobutanecarboxaldehyde
Excitation technique: Thermal
Analytical technique: IR absorption
""",
)

entry(
    index = 36,
    label = "C6H12-2 <=> C2H4 + C4H8-4",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (3.7e+15, 's^-1'),
        n = 0,
        Ea = (263.569, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (653, 'K'),
        Tmax = (703, 'K'),
        Pmin = (773, 'Pa'),
        Pmax = (52400, 'Pa'),
    ),
    reference = Article(
        authors = ["Gerberich, H.R.", "Walters, W.D."],
        title = u'The thermal decomposition of cis-1,2-dimethylcyclobutane',
        journal = "J. Am. Chem. Soc.",
        volume = "83",
        pages = """3935-3939""",
        year = "1961",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1961GER/WAL3935-3939:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015648
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015648/rk00000001.xml
Bath gas: Cyclobutane, 1,2-dimethyl-, cis-
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 37,
    label = "C6H12-2 <=> C2H4 + C4H8-4",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.9e+15, 's^-1'),
        n = 0,
        Ea = (265.232, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (663, 'K'),
        Tmax = (713, 'K'),
        Pmin = (1733, 'Pa'),
        Pmax = (50000, 'Pa'),
    ),
    reference = Article(
        authors = ["Gerberich, H.R.", "Walters, W.D."],
        title = u'The thermal decomposition of trans-1,2-dimethylcyclobutane',
        journal = "J. Am. Chem. Soc.",
        volume = "83",
        pages = """4884-4888""",
        year = "1961",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1961GER/WAL4884-4888:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015651
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015651/rk00000001.xml
Bath gas: Cyclobutane, 1,2-dimethyl-, trans-
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 38,
    label = "C6H12-2 <=> C3H6 + C3H6",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3e+15, 's^-1'),
        n = 0,
        Ea = (252.76, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (653, 'K'),
        Tmax = (703, 'K'),
        Pmin = (773, 'Pa'),
        Pmax = (52400, 'Pa'),
    ),
    reference = Article(
        authors = ["Gerberich, H.R.", "Walters, W.D."],
        title = u'The thermal decomposition of cis-1,2-dimethylcyclobutane',
        journal = "J. Am. Chem. Soc.",
        volume = "83",
        pages = """3935-3939""",
        year = "1961",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1961GER/WAL3935-3939:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015649
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015649/rk00000001.xml
Bath gas: Cyclobutane, 1,2-dimethyl-, cis-
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 39,
    label = "C6H12-2 <=> C3H6 + C3H6",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.8e+15, 's^-1'),
        n = 0,
        Ea = (257.749, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (663, 'K'),
        Tmax = (713, 'K'),
        Pmin = (1733, 'Pa'),
        Pmax = (50000, 'Pa'),
    ),
    reference = Article(
        authors = ["Gerberich, H.R.", "Walters, W.D."],
        title = u'The thermal decomposition of trans-1,2-dimethylcyclobutane',
        journal = "J. Am. Chem. Soc.",
        volume = "83",
        pages = """4884-4888""",
        year = "1961",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1961GER/WAL4884-4888:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015652
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015652/rk00000001.xml
Bath gas: Cyclobutane, 1,2-dimethyl-, trans-
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 40,
    label = "C5H10O-4 <=> C4H8-4 + CH2O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.09e+15, 's^-1', '*|/', 1.82),
        n = 0,
        Ea = (266.063, 'kJ/mol', '+|-', 2.661),
        T0 = (1, 'K'),
        Tmin = (688, 'K'),
        Tmax = (756, 'K'),
        Pmin = (267, 'Pa'),
        Pmax = (4266, 'Pa'),
    ),
    reference = Article(
        authors = ["Holbrook, K.A.", "Scott, R.A."],
        title = u'Gas-phase Unimolecular Pyrolyses of cis- and trans-2,3-Dimethyloxetan',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "70",
        pages = """43""",
        year = "1974",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1974HOL/SCO43:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016231
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016231/rk00000001.xml
Uncertainty: 1.8200001
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 41,
    label = "C5H10O-4 <=> C4H8-4 + CH2O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.74e+15, 's^-1', '*|/', 1.78),
        n = 0,
        Ea = (261.074, 'kJ/mol', '+|-', 2.611),
        T0 = (1, 'K'),
        Tmin = (688, 'K'),
        Tmax = (756, 'K'),
        Pmin = (267, 'Pa'),
        Pmax = (4266, 'Pa'),
    ),
    reference = Article(
        authors = ["Holbrook, K.A.", "Scott, R.A."],
        title = u'Gas-phase Unimolecular Pyrolyses of cis- and trans-2,3-Dimethyloxetan',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "70",
        pages = """43""",
        year = "1974",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1974HOL/SCO43:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016297
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016297/rk00000001.xml
Uncertainty: 1.78
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 42,
    label = "C5H10O-4 <=> C3H6 + C2H4O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.13e+15, 's^-1', '*|/', 1.78),
        n = 0,
        Ea = (270.22, 'kJ/mol', '+|-', 2.702),
        T0 = (1, 'K'),
        Tmin = (688, 'K'),
        Tmax = (756, 'K'),
        Pmin = (267, 'Pa'),
        Pmax = (4266, 'Pa'),
    ),
    reference = Article(
        authors = ["Holbrook, K.A.", "Scott, R.A."],
        title = u'Gas-phase Unimolecular Pyrolyses of cis- and trans-2,3-Dimethyloxetan',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "70",
        pages = """43""",
        year = "1974",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1974HOL/SCO43:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016232
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016232/rk00000001.xml
Uncertainty: 1.78
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 43,
    label = "C5H10O-4 <=> C3H6 + C2H4O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+15, 's^-1', '*|/', 1.66),
        n = 0,
        Ea = (264.4, 'kJ/mol', '+|-', 2.644),
        T0 = (1, 'K'),
        Tmin = (688, 'K'),
        Tmax = (756, 'K'),
        Pmin = (267, 'Pa'),
        Pmax = (4266, 'Pa'),
    ),
    reference = Article(
        authors = ["Holbrook, K.A.", "Scott, R.A."],
        title = u'Gas-phase Unimolecular Pyrolyses of cis- and trans-2,3-Dimethyloxetan',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "70",
        pages = """43""",
        year = "1974",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1974HOL/SCO43:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016298
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016298/rk00000001.xml
Uncertainty: 1.66
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 44,
    label = "C7H12 <=> C2H4 + C5H8",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (6.92e+14, 's^-1'),
        n = 0,
        Ea = (254.423, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (699, 'K'),
        Tmax = (737, 'K'),
        Pmin = (267, 'Pa'),
        Pmax = (2666, 'Pa'),
    ),
    reference = Article(
        authors = ["Ellis, R.J.", "Frey, H.M."],
        title = u'The thermal unimolecular decomposition of bicyclo[3,2,0]-heptane',
        journal = "J. Chem. Soc.",
        pages = """4184-4187""",
        year = "1964",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1964ELL/FRE4184-4187:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00006431
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00006431/rk00000001.xml
Bath gas: Bicyclo[3.2.0]heptane
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 45,
    label = "C7H14 <=> C5H10-2 + C2H4",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (4.3e+15, 's^-1', '+|-', 8.6e+13),
        n = 0,
        Ea = (261.906, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (683, 'K'),
        Tmax = (1130, 'K'),
        Pmin = (1200, 'Pa'),
        Pmax = (7333, 'Pa'),
    ),
    reference = Article(
        authors = ["Zupan, M.", "Walters, W.D."],
        title = u'The kinetics of the thermal decomposition of isopropylcyclobutane',
        journal = "J. Phys. Chem.",
        volume = "67",
        pages = """1845-1848""",
        year = "1963",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1963ZUP/WAL1845-1848:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009049
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009049/rk00000001.xml
Bath gas: Isopropylcyclobutane
Excitation technique: Thermal
Analytical technique: Mass spectrometry
Note: Invalid activation energy uncertainty (8314.472) found and ignored
""",
)

entry(
    index = 46,
    label = "C6H10O <=> C4H8-3 + C2H2O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.74e+14, 's^-1', '*|/', 1.66),
        n = 0,
        Ea = (192.896, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (534, 'K'),
        Tmax = (586, 'K'),
        Pmin = (66.66, 'Pa'),
        Pmax = (1067, 'Pa'),
    ),
    reference = Article(
        authors = ["Frey, H.M.", "Smith, R.A."],
        title = u'Thermal decomposition of 3,3-dimethylcyclobutanone',
        journal = "J. Chem. Soc. Perkin Trans. 2",
        pages = """752""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977FRE/SMI752:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009421
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009421/rk00000001.xml
Uncertainty: 1.66
Bath gas: Cyclobutanone, 3,3-dimethyl-
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 47,
    label = "C5H8-2 + C2H4 <=> C7H12-2",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (132000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (123.886, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1180, 'K'),
        Pmin = (253000, 'Pa'),
        Pmax = (253000, 'Pa'),
    ),
    reference = Article(
        authors = ["Simmie, J.M."],
        title = u'Kinetic Study of a Retro Diels-Alder Reaction in a Single-Pulse Shock Tube: Decyclization of 1-Methylcyclohex-1-ene',
        journal = "Int. J. Chem. Kinet.",
        volume = "10",
        pages = """227""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978SIM227:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011630
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 48,
    label = "C6H10O-2 <=> C4H6O-2 + C2H4",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (3.4e+14, 's^-1'),
        n = 0,
        Ea = (227.817, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (633, 'K'),
        Tmax = (683, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (8666, 'Pa'),
    ),
    reference = Article(
        authors = ["Daignault, L.G.", "Walters, W.D."],
        title = u'The thermal decomposition of methyl cyclobutyl ketone',
        journal = "J. Am. Chem. Soc.",
        volume = "80",
        pages = """541-545""",
        year = "1958",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1958DAI/WAL541-545:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011632
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011632/rk00000001.xml
Bath gas: Ethanone, 1-cyclobutyl)-
Excitation technique: Thermal
Analytical technique: IR absorption
""",
)

entry(
    index = 49,
    label = "C7H14-2 <=> C5H10-3 + C2H4",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (3.4e+15, 's^-1'),
        n = 0,
        Ea = (257.749, 'kJ/mol', '+|-', 2.577),
        T0 = (1, 'K'),
        Tmin = (673, 'K'),
        Tmax = (729, 'K'),
        Pmin = (720, 'Pa'),
        Pmax = (66000, 'Pa'),
    ),
    reference = Article(
        authors = ["Kellner, S.M.E.", "Walters, W.D."],
        title = u'The thermal decomposition of n-propylcyclobutane',
        journal = "J. Phys. Chem.",
        volume = "65",
        pages = """466-469""",
        year = "1961",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1961KEL/WAL466-469:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00012798
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012798/rk00000001.xml
Bath gas: Cyclobutane, propyl-
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 50,
    label = "C7H10 <=> C2H4 + C5H6",
    degeneracy = 5,
    kinetics = Arrhenius(
        A = (7.94e+15, 's^-1', '*|/', 2.14),
        n = 0,
        Ea = (222.828, 'kJ/mol', '+|-', 4.465),
        T0 = (1, 'K'),
        Tmin = (580, 'K'),
        Tmax = (626, 'K'),
        Pmin = (5000, 'Pa'),
        Pmax = (5000, 'Pa'),
    ),
    reference = Article(
        authors = ["Cocks, A.T.", "Frey, H.M."],
        title = u'Thermal Unimolecular Reactions of Bicyclo[3.2.0]hept-2-ene',
        journal = "J. Chem. Soc. A",
        pages = """2564""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971COC/FRE2564:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00013054
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013054/rk00000001.xml
Uncertainty: 2.1400001
Bath gas: Bicyclo[3.2.0]hept-6-ene
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 51,
    label = "C7H14-3 <=> C2H4 + C5H10-4",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (8.51e+15, 's^-1', '*|/', 1.15),
        n = 0,
        Ea = (266.895, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (660, 'K'),
        Tmax = (728, 'K'),
        Pmin = (667, 'Pa'),
        Pmax = (1600, 'Pa'),
    ),
    reference = Article(
        authors = ["Cocks, A.T.", "Frey, H.M."],
        title = u'The Thermal Unimolecular Decomposition of 1,1,2-Trimethylcyclobutane',
        journal = "J. Phys. Chem.",
        volume = "75",
        pages = """1437""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971COC/FRE1437:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016299
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016299/rk00000001.xml
Uncertainty: 1.15
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 52,
    label = "C6H12O <=> C5H10-5 + CH2O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.28e+15, 's^-1', '*|/', 1.42),
        n = 0,
        Ea = (251.097, 'kJ/mol', '+|-', 2.511),
        T0 = (1, 'K'),
        Tmin = (680, 'K'),
        Tmax = (721, 'K'),
        Pmin = (960, 'Pa'),
        Pmax = (1667, 'Pa'),
    ),
    reference = Article(
        authors = ["Clements, A.D.", "Frey, H.M.", "Frey, J.G."],
        title = u'Thermal Decomposition of 3-Ethyl-3-methyloxetan and 3,3-Diethyloxetan',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "71",
        pages = """2485""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975CLE/FRE2485:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016368
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016368/rk00000001.xml
Uncertainty: 1.42
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 53,
    label = "C7H12-2 <=> C5H8-2 + C2H4",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (4.37e+14, 's^-1'),
        n = 0,
        Ea = (213.682, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (577, 'K'),
        Tmax = (621, 'K'),
    ),
    reference = Article(
        authors = ["Ellis, R.J.", "Frey, H.M."],
        title = u'Thermal unimolecular decomposition of isopropenylcyclobutane',
        journal = "Trans. Faraday Soc.",
        volume = "59",
        pages = """2076-2079""",
        year = "1963",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1963ELL/FRE2076-2079:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011630
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011630/rk00000001.xml
Bath gas: Cyclobutane,(1-methylethenyl)-
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 54,
    label = "C7H12-2 <=> C5H8-2 + C2H4",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1.66e+15, 's^-1', '*|/', 1.42),
        n = 0,
        Ea = (218.671, 'kJ/mol', '+|-', 2.187),
        T0 = (1, 'K'),
        Tmin = (574, 'K'),
        Tmax = (624, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (1800, 'Pa'),
    ),
    reference = Article(
        authors = ["Frey, H.M.", "Pottinger, R."],
        title = u'Thermal unimolecular reactions of vinylcyclobutane and isopropenylcyclobutane',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "74",
        pages = """1827""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978FRE/POT1827:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011630
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011630/rk00000002.xml
Uncertainty: 1.42
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 55,
    label = "C7H14-3 <=> C4H8-3 + C3H6",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5.62e+15, 's^-1', '*|/', 1.17),
        n = 0,
        Ea = (251.929, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (660, 'K'),
        Tmax = (728, 'K'),
        Pmin = (667, 'Pa'),
        Pmax = (1600, 'Pa'),
    ),
    reference = Article(
        authors = ["Cocks, A.T.", "Frey, H.M."],
        title = u'The Thermal Unimolecular Decomposition of 1,1,2-Trimethylcyclobutane',
        journal = "J. Phys. Chem.",
        volume = "75",
        pages = """1437""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971COC/FRE1437:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016300
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016300/rk00000001.xml
Uncertainty: 1.17
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 56,
    label = "C6H10O2 <=> C4H6O2 + C2H4",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (7e+14, 's^-1', '+|-', 7e+12),
        n = 0,
        Ea = (239.457, 'kJ/mol', '+|-', 2.395),
        T0 = (1, 'K'),
        Tmin = (653, 'K'),
        Tmax = (693, 'K'),
        Pmin = (840, 'Pa'),
        Pmax = (1520, 'Pa'),
    ),
    reference = Article(
        authors = ["Zupan, M.", "Walters, W.D."],
        title = u'The kinetics of the thermal decomposition of methyl cyclobutanecarboxylate',
        journal = "J. Am. Chem. Soc.",
        volume = "86",
        pages = """173-176""",
        year = "1964",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1964ZUP/WAL173-176:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00008915
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008915/rk00000001.xml
Bath gas: Cyclobutanecarboxylic acid methyl ester
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 57,
    label = "C7H12O <=> C5H8O-3 + C2H4",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (3.4e+14, 's^-1', '+|-', 1e+13),
        n = 0,
        Ea = (226.985, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (643, 'K'),
        Tmax = (683, 'K'),
        Pmin = (533, 'Pa'),
        Pmax = (2266, 'Pa'),
    ),
    reference = Article(
        authors = ["Roquitte, B.C.", "Walters, W.D."],
        title = u'The thermal decomposition of ethyl cyclobutyl ketone',
        journal = "J. Phys. Chem.",
        volume = "68",
        pages = """1606-1609""",
        year = "1964",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1964ROQ/WAL1606-1609:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00013004
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013004/rk00000001.xml
Bath gas: 1-Propanone, 1-cyclobutyl-
Excitation technique: Thermal
Analytical technique: IR absorption
""",
)

entry(
    index = 58,
    label = "C7H14O <=> C6H12-3 + CH2O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.98e+15, 's^-1', '*|/', 1.16),
        n = 0,
        Ea = (250.266, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (675, 'K'),
        Tmax = (736, 'K'),
        Pmin = (960, 'Pa'),
        Pmax = (1667, 'Pa'),
    ),
    reference = Article(
        authors = ["Clements, A.D.", "Frey, H.M.", "Frey, J.G."],
        title = u'Thermal Decomposition of 3-Ethyl-3-methyloxetan and 3,3-Diethyloxetan',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "71",
        pages = """2485""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975CLE/FRE2485:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00014886
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00014886/rk00000001.xml
Uncertainty: 1.16
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 59,
    label = "C7H8O <=> C5H6 + C2H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.45e+13, 's^-1', '*|/', 1.29),
        n = 0,
        Ea = (157.144, 'kJ/mol', '+|-', 1.571),
        T0 = (1, 'K'),
        Tmin = (471, 'K'),
        Tmax = (534, 'K'),
        Pmin = (2000, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Egger, K.W.", "Cocks, A.T."],
        title = u'Kinetics of the Four-centre Elimination of Keten from Bicyclo[3.2.0]hept-2-en-6-one in the Gas Phase',
        journal = "J. Chem. Soc. Perkin Trans. 2",
        pages = """211""",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972EGG/COC211:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015146
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015146/rk00000001.xml
Uncertainty: 1.29
Bath gas: CH3CH=CH2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 60,
    label = "C7H10O <=> C5H8 + C2H2O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.62e+14, 's^-1', '*|/', 1.26),
        n = 0,
        Ea = (202.873, 'kJ/mol', '+|-', 2.029),
        T0 = (1, 'K'),
        Tmin = (546, 'K'),
        Tmax = (652, 'K'),
        Pmin = (547, 'Pa'),
        Pmax = (5333, 'Pa'),
    ),
    reference = Article(
        authors = ["Cocks, A.T.", "Egger, K.W."],
        title = u'The Gas-Phase Thermal Unimolecular Elimination of Keten from Bicyclo-[3.2.0]heptan-6-one',
        journal = "J. Chem. Soc. Perkin Trans. 2",
        pages = """2014""",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972COC/EGG2014:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015261
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015261/rk00000001.xml
Uncertainty: 1.26
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 61,
    label = "C8H14 <=> C4H8-3 + C4H6",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.22e+15, 's^-1', '*|/', 2),
        n = 0,
        Ea = (199.547, 'kJ/mol', '+|-', 1.995),
        T0 = (1, 'K'),
        Tmin = (536, 'K'),
        Tmax = (574, 'K'),
        Pmin = (3306, 'Pa'),
        Pmax = (3306, 'Pa'),
    ),
    reference = Article(
        authors = ["Chickos, J.S.", "Frey, H.M."],
        title = u'The thermolysis of 2,2-dimethyl-1-vinylcyclobutane',
        journal = "J. Chem. Soc. Perkin Trans. 2",
        pages = """365""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987CHI/FRE365:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00017015
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00017015/rk00000001.xml
Uncertainty: 2.0
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 62,
    label = "C8H16 <=> C4H8-3 + C4H8-3",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.04e+16, 's^-1', '*|/', 1.12),
        n = 0,
        Ea = (272.715, 'kJ/mol', '+|-', 0.673),
        T0 = (1, 'K'),
        Tmin = (683, 'K'),
        Tmax = (6800, 'K'),
        Pmin = (933, 'Pa'),
        Pmax = (6666, 'Pa'),
    ),
    reference = Article(
        authors = ["Cocks, A.T.", "Frey, H.M."],
        title = u'Thermal unimolecular decomposition of 1,1,3,3-tetramethylcyclobutane',
        journal = "J. Chem. Soc. A",
        pages = """1671-1673""",
        year = "1969",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1969COC/FRE1671-1673:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016155
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016155/rk00000001.xml
Uncertainty: 1.12
Bath gas: Cyclobutane, 1,1,3,3-tetramethyl-
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 63,
    label = "C7H14O-2 <=> C5H10-4 + C2H4O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+14, 's^-1', '*|/', 2.24),
        n = 0,
        Ea = (236.962, 'kJ/mol', '+|-', 4.739),
        T0 = (1, 'K'),
        Tmin = (684, 'K'),
        Tmax = (750, 'K'),
        Pmin = (667, 'Pa'),
        Pmax = (1333, 'Pa'),
    ),
    reference = Article(
        authors = ["Hammonds, P.", "Holbrook, K.A.", "Carless, H.A.J."],
        title = u'Thermolyses of cis- and trans-2,2,3,4-tetramethyloxetane',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "80",
        pages = """691""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984HAM/HOL691:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016567
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016567/rk00000001.xml
Uncertainty: 2.24
Bath gas: Oxetane, 2,2,3,4-tetramethyl-,(E)-
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 64,
    label = "C7H14O-2 <=> C5H10-4 + C2H4O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+13, 's^-1', '*|/', 5),
        n = 0,
        Ea = (228.648, 'kJ/mol', '+|-', 9.146),
        T0 = (1, 'K'),
        Tmin = (682, 'K'),
        Tmax = (751, 'K'),
        Pmin = (667, 'Pa'),
        Pmax = (1333, 'Pa'),
    ),
    reference = Article(
        authors = ["Hammonds, P.", "Holbrook, K.A.", "Carless, H.A.J."],
        title = u'Thermolyses of cis- and trans-2,2,3,4-tetramethyloxetane',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "80",
        pages = """691""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984HAM/HOL691:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016568
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016568/rk00000001.xml
Uncertainty: 5.0
Bath gas: Oxetane, 2,2,3,4-tetramethyl-,(Z)-
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 65,
    label = "C7H12O-2 <=> C5H8-3 + C2H4O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.63e+13, 's^-1', '*|/', 5),
        n = 0,
        Ea = (200.379, 'kJ/mol', '+|-', 8.015),
        T0 = (1, 'K'),
        Tmin = (599, 'K'),
        Tmax = (657, 'K'),
        Pmin = (467, 'Pa'),
        Pmax = (4000, 'Pa'),
    ),
    reference = Article(
        authors = ["Carless, H.A.J.", "Maitra, A.K.", "Pottinger, R.", "Frey, H.M."],
        title = u'Thermal decomposition of cis-2,4-dimethyl-trans-3-vinyloxetan',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "76",
        pages = """1849""",
        year = "1980",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1980CAR/MAI1849:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016669
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016669/rk00000001.xml
Uncertainty: 5.0
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 66,
    label = "C8H14O <=> C4H8-3 + C4H6O-3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.23e+14, 's^-1', '*|/', 1.07),
        n = 0,
        Ea = (234.468, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (637, 'K'),
        Tmax = (700, 'K'),
        Pmin = (907, 'Pa'),
        Pmax = (907, 'Pa'),
    ),
    reference = Article(
        authors = ["Frey, H.M.", "Hopf, H."],
        title = u'The thermal unimolecular decomposition of 2,2,4,4-tetramethylcyclobutanone',
        journal = "J. Chem. Soc. Perkin Trans. 2",
        pages = """2016""",
        year = "1973",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1973FRE/HOP2016:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00012680
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012680/rk00000001.xml
Uncertainty: 1.0700001
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 67,
    label = "C9H12O <=> C5H6 + C4H6O-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+12, 's^-1', '*|/', 1.66),
        n = 0,
        Ea = (157.975, 'kJ/mol', '+|-', 1.58),
        T0 = (1, 'K'),
        Tmin = (470, 'K'),
        Tmax = (550, 'K'),
        Pmin = (987, 'Pa'),
        Pmax = (9333, 'Pa'),
    ),
    reference = Article(
        authors = ["Egger, K.W."],
        title = u'The Gas-Phase Thermal Unimolecular Elimination of 1,1-Dimethylketene from 7,7-Dimethylbicyclo[3.2.0]hept-2-en-6-one',
        journal = "Int. J. Chem. Kinet.",
        volume = "5",
        pages = """285""",
        year = "1973",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1973EGG285:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00008919
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008919/rk00000001.xml
Uncertainty: 1.66
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

