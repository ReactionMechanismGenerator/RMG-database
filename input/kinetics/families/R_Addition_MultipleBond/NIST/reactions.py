#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/NIST"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "C2H5 <=> C2H4 + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.06e+10, 's^-1'),
        n = 0.95,
        Ea = (154.557, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:14",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 2,
    label = "C2H5 <=> C2H4 + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (8.2e+13, 's^-1', '*|/', 2),
        n = 0,
        Ea = (167.121, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (1100, 'K'),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Frank, P.", "Hayman, G.", "Just, Th.", "Kerr, J.A.", "Murrells, T.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combusion modelling. Supplement I',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "23",
        pages = """847-1033""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994BAU/COB847-1033:117",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Uncertainty: 2.0
Bath gas: Ar
""",
)

entry(
    index = 3,
    label = "C2H5 <=> C2H4 + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.09e+10, 's^-1'),
        n = 1.04,
        Ea = (153.818, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (1100, 'K'),
        Pmin = (107, 'Pa'),
        Pmax = (1907, 'Pa'),
    ),
    reference = Article(
        authors = ["Feng, Y.", "Niiranen, J.T.", "Bencsura, A.", "Knyazev, V.D.", "Gutman, D.", "Tsang, W."],
        title = u'Weak collision effects in the reaction C2H5 = C2H4 + H',
        journal = "J. Phys. Chem.",
        volume = "97",
        pages = """871-880""",
        year = "1993",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1993FEN/NII871-880:1",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Bath gas: He
""",
)

entry(
    index = 4,
    label = "C2H5 <=> C2H4 + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (4.9e+09, 's^-1', '*|/', 2),
        n = 1.19,
        Ea = (155.481, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W.", "Hampson, R.F."],
        title = u'Chemical kinetic data base for combustion chemistry. Part I. Methane and related compounds',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "15",
        pages = """1087""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:258",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Uncertainty: 2.0
Bath gas: N2
""",
)

entry(
    index = 5,
    label = "C2H5 <=> C2H4 + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2e+13, 's^-1', '*|/', 2),
        n = 0,
        Ea = (166.289, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:195",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Uncertainty: 2.0
""",
)

entry(
    index = 6,
    label = "C2H5 <=> C2H4 + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.8e+43, 's^-1'),
        n = -9.54,
        Ea = (213.682, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (250, 'K'),
        Tmax = (1200, 'K'),
        Pmin = (93.33, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Bozzelli, J.W.", "Dean, A.M."],
        title = u'Chemical activation analysis of the reaction of C2H5 with O2',
        journal = "J. Phys. Chem.",
        volume = "94",
        pages = """3313-3317""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990BOZ/DEA3313-3317:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Bath gas: N2
""",
)

entry(
    index = 7,
    label = "C2H5 <=> C2H4 + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.58e+13, 's^-1'),
        n = 0,
        Ea = (158.806, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (793, 'K'),
        Tmax = (813, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (40000, 'Pa'),
    ),
    reference = Article(
        authors = ["Simon, Y.", "Foucaut, J.F.", "Scacchi, G."],
        title = u'Etude experimentale et modelisation theorique de la decomposition du radical ethyle',
        journal = "Can. J. Chem.",
        volume = "66",
        pages = """2142""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988SIM/FOU2142:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Bath gas: C2H6
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 8,
    label = "C2H5 <=> C2H4 + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (8.91e+12, 's^-1', '*|/', 1.58),
        n = 0,
        Ea = (158.806, 'kJ/mol', '+|-', 3.176),
        T0 = (1, 'K'),
        Tmin = (841, 'K'),
        Tmax = (931, 'K'),
        Pmin = (120, 'Pa'),
        Pmax = (124000, 'Pa'),
    ),
    reference = Article(
        authors = ["Trenwith, A.B."],
        title = u'The pyrolysis of ethane. A study of the dissociation reaction C2H5 \u2192\x92 C2H4 + H',
        journal = "J. Chem. Soc. Faraday Trans. 2",
        volume = "82",
        pages = """457""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986TRE457:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Uncertainty: 1.58
Bath gas: C2H6
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 9,
    label = "C2H5 <=> C2H4 + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.92e+11, 's^-1'),
        n = 0,
        Ea = (141.346, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (775, 'K'),
        Tmax = (825, 'K'),
        Pmin = (26700, 'Pa'),
        Pmax = (26700, 'Pa'),
    ),
    reference = Article(
        authors = ["Brouard, M.", "Lightfoot, P.D.", "Pilling, M.J."],
        title = u'Observation of equilibration in the system H + C2H4 = C2H5. The determination of the heat of formation of C2H5',
        journal = "J. Phys. Chem.",
        volume = "90",
        pages = """445-450""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986BRO/LIG445-450:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Resonance fluorescence
""",
)

entry(
    index = 10,
    label = "C2H5 <=> C2H4 + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.2e+12, 's^-1'),
        n = 0,
        Ea = (146.335, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1200, 'K'),
        Tmax = (1700, 'K'),
        Pmin = (172000, 'Pa'),
        Pmax = (253000, 'Pa'),
    ),
    reference = Article(
        authors = ["Hidaka, Y.", "Shiba, S.", "Takuma, H.", "Suga, M."],
        title = u'Thermal decomposition of ethane in shock waves',
        journal = "Int. J. Chem. Kinet.",
        volume = "17",
        pages = """441""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985HID/SHI441:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 11,
    label = "C2H5 <=> C2H4 + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (5.01e+13, 's^-1'),
        n = 0,
        Ea = (171.278, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Dean, A.M."],
        title = u'Predictions of pressure and temperature effects upon radical addition and recombination reactions',
        journal = "J. Phys. Chem.",
        volume = "89",
        pages = """4600-4608""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:40",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
""",
)

entry(
    index = 12,
    label = "C2H5 <=> C2H4 + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.16e+13, 's^-1'),
        n = 0,
        Ea = (174.604, 'kJ/mol', '+|-', 12.222),
        T0 = (1, 'K'),
        Tmin = (941, 'K'),
        Tmax = (1070, 'K'),
        Pmin = (80000, 'Pa'),
        Pmax = (80000, 'Pa'),
    ),
    reference = Article(
        authors = ["Pratt, G.", "Rogers, D."],
        title = u'Wall-less Reactor Studies. Part 1. - Ethane Pyrolysis',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "75",
        pages = """1089""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979PRA/ROG1089:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 13,
    label = "C2H5 <=> C2H4 + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1e+11, 's^-1'),
        n = 0,
        Ea = (126.38, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (669, 'K'),
        Tmax = (762, 'K'),
        Pmin = (1907, 'Pa'),
        Pmax = (2053, 'Pa'),
    ),
    reference = Article(
        authors = ["Koski, A.A.", "Price, S.J.W.", "Trudell, B.C."],
        title = u'Studies of the pyrolysis of diethylzinc by the toluene carrier method and of the reaction of ethyl radicals with toluene',
        journal = "Can. J. Chem.",
        volume = "54",
        pages = """482-487""",
        year = "1976",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976KOS/PRI482-487:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 14,
    label = "C2H5 <=> C2H4 + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.7e+14, 's^-1'),
        n = 0,
        Ea = (171.278, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (673, 'K'),
        Tmax = (773, 'K'),
        Pmin = (533, 'Pa'),
        Pmax = (86700, 'Pa'),
    ),
    reference = Article(
        authors = ["Loucks, L.F.", "Laidler, K.J."],
        title = u'Thermal decomposition of the ethyl radical',
        journal = "Can. J. Chem.",
        volume = "45",
        pages = """2795-2803""",
        year = "1967",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1967LOU/LAI2795-2803:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Bath gas: C2H6
Excitation technique: Sensitized photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 15,
    label = "C2H5 <=> C2H4 + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.8e+13, 's^-1'),
        n = 0,
        Ea = (158.806, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (823, 'K'),
        Tmax = (913, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (80000, 'Pa'),
    ),
    reference = Article(
        authors = ["Lin, M.C.", "Back, M.H."],
        title = u'the thermal decomposition of ethane. Part II. The unimolecular decomposition of the ethane molecule and the ethyl radical',
        journal = "Can. J. Chem.",
        volume = "44",
        pages = """2357""",
        year = "1966",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1966LIN/BAC2357:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Bath gas: C2H6
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 16,
    label = "C2H5 <=> C2H4 + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1e+13, 's^-1'),
        n = 0,
        Ea = (167.121, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (693, 'K'),
        Tmax = (803, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (20000, 'Pa'),
    ),
    reference = Article(
        authors = ["Purnell, J.H.", "Quinn, C.P."],
        title = u'The pyrolysis of n-butane',
        journal = "Proc. R. Soc. London A",
        volume = "270",
        pages = """267""",
        year = "1962",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1962PUR/QUI267:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Bath gas: n-C4H10
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 17,
    label = "C2H5 <=> C2H4 + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.58e+11, 's^-1'),
        n = 0,
        Ea = (129.706, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (633, 'K'),
        Tmax = (778, 'K'),
        Pmin = (1667, 'Pa'),
        Pmax = (1667, 'Pa'),
    ),
    reference = Article(
        authors = ["Kerr, J.A.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part V. Ethyl radicals from propionaldehyde',
        journal = "J. Chem. Soc.",
        pages = """1611""",
        year = "1960",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1960KER/TRO1611:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Bath gas: C2H5CHO
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 18,
    label = "C2H5 <=> C2H4 + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1e+10, 's^-1'),
        n = 0,
        Ea = (152.986, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1040, 'K'),
        Tmax = (1160, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Brodsky, A.M.", "Kalinenko, R.A.", "Lavrovsky, K.P."],
        title = u'The principles governing high-temperature ethane cracking',
        journal = "J. Chem. Soc.",
        pages = """4443""",
        year = "1960",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1960BRO/KAL4443:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010238/rk00000001.xml
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 19,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (17000, 'm^3/(mol*s)'),
        n = 1.07,
        Ea = (6.067, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:1",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 20,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (253, 'm^3/(mol*s)'),
        n = 1.75,
        Ea = (5.029, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Michael, J.V.", "Su, M.C.", "Sutherland, J.W.", "Harding, L.B.", "Wagner, A.F."],
        title = u'Rate constants for D+C2H4 -&gt; C2H3D+H at high temperature: implications to the high pressure rate constant for H+C2H4 -&gt; C2H5',
        journal = "Proc. Combust. Inst.",
        volume = "30",
        pages = """965-973""",
        year = "2005",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2005MIC/SU965-973:2",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Pressure dependence: Rate constant is high pressure limit
Experimental procedure: Shock tube
Excitation technique: Thermal
Time resolution: In real time
Analytical technique: Other (direct)

Rate constant was dervived from theory by the authors following an analysis of theoretical and experimental results from this paper and the literature.
""",
)

entry(
    index = 21,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3970, 'm^3/(mol*s)', '*|/', 2),
        n = 1.28,
        Ea = (5.404, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (1100, 'K'),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Frank, P.", "Hayman, G.", "Just, Th.", "Kerr, J.A.", "Murrells, T.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combusion modelling. Supplement I',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "23",
        pages = """847-1033""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994BAU/COB847-1033:23",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Uncertainty: 2.0
Bath gas: Ar
""",
)

entry(
    index = 22,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.64e+07, 'm^3/(mol*s)', '+|-', 3.4e+06),
        n = 0,
        Ea = (9.063, 'kJ/mol', '+|-', 0.271),
        T0 = (1, 'K'),
        Tmin = (285, 'K'),
        Tmax = (604, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (80000, 'Pa'),
    ),
    reference = Article(
        authors = ["Lightfoot, P.D.", "Pilling, M.J."],
        title = u'Temperature and pressure dependence of the rate constant for the addition of H to C2H4',
        journal = "J. Phys. Chem.",
        volume = "91",
        pages = """3373-3379""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987LIG/PIL3373-3379:1",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Bath gas: He
""",
)

entry(
    index = 23,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (842, 'm^3/(mol*s)', '*|/', 3),
        n = 1.49,
        Ea = (4.149, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W.", "Hampson, R.F."],
        title = u'Chemical kinetic data base for combustion chemistry. Part I. Methane and related compounds',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "15",
        pages = """1087""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:57",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Uncertainty: 3.0
Bath gas: N2
""",
)

entry(
    index = 24,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1e+07, 'm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (6.302, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:28",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Uncertainty: 2.0
""",
)

entry(
    index = 25,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (9.33e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (11.723, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (813, 'K'),
        Pmin = (667, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Book(
        authors = ["Kerr, J.A.", "Parsonage, M.J."],
        title = u'Evaluated Kinetic Data on Gas Phase Addition Reactions. Reactions of Atoms and Radicals with Alkenes, Alkynes and Aromatic Compounds',
        publisher = "London",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972KER/PARB:24",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Bath gas: He
""",
)

entry(
    index = 26,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.75e+07, 'm^3/(mol*s)', '+|-', 4.4e+06),
        n = 0,
        Ea = (9.395, 'kJ/mol', '+|-', 0.283),
        T0 = (1, 'K'),
        Tmin = (285, 'K'),
        Tmax = (604, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (80000, 'Pa'),
    ),
    reference = Article(
        authors = ["Lightfoot, P.D.", "Pilling, M.J."],
        title = u'Temperature and pressure dependence of the rate constant for the addition of H to C2H4',
        journal = "J. Phys. Chem.",
        volume = "91",
        pages = """3373-3379""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987LIG/PIL3373-3379:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Resonance fluorescence
""",
)

entry(
    index = 27,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (173000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (-15.548, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (775, 'K'),
        Tmax = (825, 'K'),
        Pmin = (26700, 'Pa'),
        Pmax = (26700, 'Pa'),
    ),
    reference = Article(
        authors = ["Brouard, M.", "Lightfoot, P.D.", "Pilling, M.J."],
        title = u'Observation of equilibration in the system H + C2H4 = C2H5. The determination of the heat of formation of C2H5',
        journal = "J. Phys. Chem.",
        volume = "90",
        pages = """445-450""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986BRO/LIG445-450:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Resonance fluorescence
""",
)

entry(
    index = 28,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.83e+07, 'm^3/(mol*s)', '+|-', 2.8e+06),
        n = 0,
        Ea = (9.146, 'kJ/mol', '+|-', 0.274),
        T0 = (1, 'K'),
        Tmin = (206, 'K'),
        Tmax = (461, 'K'),
        Pmin = (79300, 'Pa'),
        Pmax = (86700, 'Pa'),
    ),
    reference = Article(
        authors = ["Sugawara, K.", "Okazaki, K.", "Sato, S."],
        title = u'Temperature Dependence of the Rate Constants of H and D-Atom Additions to C2H4, C2H3D, C2D4, C2H2, and C2D2',
        journal = "Bull. Chem. Soc. Jpn.",
        volume = "54",
        pages = """2872""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981SUG/OKA2872:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Bath gas: H2
Excitation technique: Ultrasonics
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 29,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.77e+07, 'm^3/(mol*s)', '+|-', 1.9e+06),
        n = 0,
        Ea = (8.98, 'kJ/mol', '+|-', 0.0898),
        T0 = (1, 'K'),
        Tmin = (206, 'K'),
        Tmax = (461, 'K'),
        Pmin = (93300, 'Pa'),
        Pmax = (93300, 'Pa'),
    ),
    reference = Article(
        authors = ["Sugawara, K.", "Okazaki, K.", "Sato, S."],
        title = u'Kinetic Isotope Effects in the Reaction H + C2H4 \u2192\x92 C2H5',
        journal = "Chem. Phys. Lett.",
        volume = "78",
        pages = """259""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981SUG/OKA259:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Bath gas: H2
Excitation technique: Ultrasonics
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 30,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.98e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (19.456, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (523, 'K'),
        Tmax = (829, 'K'),
        Pmin = (13300, 'Pa'),
        Pmax = (13300, 'Pa'),
    ),
    reference = Article(
        authors = ["Billaud, F.", "Baronnet, F.", "Niclause, M."],
        title = u"Influence de l'Ethylene sur la Pyrolyse de l'Ethane vers 540oC",
        journal = "J. Chim. Phys.",
        volume = "77",
        pages = """357""",
        year = "1980",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1980BIL/BAR357:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Bath gas: C2H6
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 31,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.21e+07, 'm^3/(mol*s)', '+|-', 4e+06),
        n = 0,
        Ea = (8.647, 'kJ/mol', '+|-', 0.346),
        T0 = (1, 'K'),
        Tmin = (198, 'K'),
        Tmax = (320, 'K'),
        Pmin = (40000, 'Pa'),
        Pmax = (93300, 'Pa'),
    ),
    reference = Article(
        authors = ["Lee, J.H.", "Michael, J.V.", "Payne, W.A.", "Stief, L.J."],
        title = u'Absolute Rate of the Reaction of Atomic Hydrogen with Ethylene from 198 to 320 K at High Pressure',
        journal = "J. Chem. Phys.",
        volume = "68",
        pages = """1817""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978LEE/MIC1817:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Bath gas: Ar
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Resonance fluorescence
""",
)

entry(
    index = 32,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (789000, 'm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (3.051, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303, 'K'),
        Tmax = (603, 'K'),
        Pmin = (160, 'Pa'),
        Pmax = (267, 'Pa'),
    ),
    reference = Article(
        authors = ["Teng, L.", "Jones, W.E."],
        title = u'Kinetics of the Reactions of Hydrogen Atoms with Ethylene and Vinyl Fluoride',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "68",
        pages = """1267""",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972TEN/JON1267:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Uncertainty: 2.0
Bath gas: H2
Excitation technique: Electron beam
Analytical technique: Gas chromatography
""",
)

entry(
    index = 33,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.08e+06, 'm^3/(mol*s)'),
        n = 0.5,
        Ea = (6.693, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (293, 'K'),
        Tmax = (600, 'K'),
        Pmin = (400, 'Pa'),
        Pmax = (2000, 'Pa'),
    ),
    reference = Article(
        authors = ["Dodonov, A.F.", "Lavrovskaya, G.K.", "Talroze, V.L."],
        title = u'Mass-spectroscopic determination of rate constants for elementary reactions. III. The rections H + C2H4, H + C3H6, and H + n-C4H8',
        journal = "Kinet. Catal.",
        volume = "10",
        pages = """14""",
        year = "1969",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1969DOD/LAV14:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Bath gas: He
Excitation technique: Electron beam
Analytical technique: Mass spectrometry
Note: Invalid activation energy uncertainty (8314.472) found and ignored
""",
)

entry(
    index = 34,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (7.94e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (7.949, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (330, 'K'),
        Tmax = (490, 'K'),
    ),
    reference = Article(
        authors = ["Yang, K."],
        title = u'Free radical reactions initiated by ionizing radiations. I. Arrhenius parameters for the reactions of hydrogen atoms with propane, ethylene and propylene',
        journal = "J. Am. Chem. Soc.",
        volume = "84",
        pages = """719-721""",
        year = "1962",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1962YAN719-721:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010238
Bath gas: Ar
Excitation technique: Ultrasonics
Analytical technique: Gas chromatography
""",
)

entry(
    index = 35,
    label = "CH3O <=> CH2O + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.56e+15, 's^-1'),
        n = -0.39,
        Ea = (110.458, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:43",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010564
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 36,
    label = "CH3O <=> CH2O + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2e+14, 's^-1'),
        n = 0,
        Ea = (104.762, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:2",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010564
""",
)

entry(
    index = 37,
    label = "CH3O <=> CH2O + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.6e+14, 's^-1', '*|/', 5),
        n = 0,
        Ea = (104.762, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:128",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010564
Uncertainty: 5.0
""",
)

entry(
    index = 38,
    label = "CH3O <=> CH2O + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (6.8e+13, 's^-1', '*|/', 1.3),
        n = 0,
        Ea = (109.5, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (678, 'K'),
        Tmax = (808, 'K'),
    ),
    reference = Article(
        authors = ["Hippler, H.", "Striebel, F.", "Viskolcz, B."],
        title = u'A Detailed Experimental and Theoretical Study on the Decomposition of Methoxy Radicals',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "3",
        pages = """2450-2458""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001HIP/STR2450-2458:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010564
Uncertainty: 1.3
Pressure dependence: Rate constant is high pressure limit
Experimental procedure: Static or low flow - Data taken vs time
Excitation technique: Flash photolysis (laser or conventional)
Time resolution: In real time
Analytical technique: Laser induced fluorescence

The reaction was studied at pressures between 1 and 90 bar using helium as the bath gas. The rate constant increased by about an order of magnitude over this pressure range. At the highest pressures studied the reaction was a factor of 2 to 3 under the high pressure limit, which was obtained by an RRKM extrapolation.
""",
)

entry(
    index = 39,
    label = "CH3O <=> CH2O + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1e+15, 's^-1'),
        n = 0,
        Ea = (143.009, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (900, 'K'),
        Tmax = (1600, 'K'),
        Pmin = (13300, 'Pa'),
        Pmax = (45600, 'Pa'),
    ),
    reference = Article(
        authors = ["Zaslonko, I.S.", "Mukoseev, Yu.K.", "Tyurin, A.N."],
        title = u'Reactions of CH3O radicals in shock waves',
        journal = "Kinet. Catal.",
        volume = "29",
        pages = """244""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988ZAS/MUK244:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010564
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Chemiluminescence
""",
)

entry(
    index = 40,
    label = "CH3O <=> CH2O + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.16e+14, 's^-1'),
        n = 0,
        Ea = (108.088, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (950, 'K'),
        Tmax = (1050, 'K'),
    ),
    reference = Article(
        authors = ["Greenhill, P.G.", "O'Grady, B.V.", "Gilbert, R.G."],
        title = u'Theoretical prediction of CH3O and CH2OH gas phase decomposition rate coefficients',
        journal = "Aust. J. Chem.",
        volume = "39",
        pages = """1929""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986GRE/OGR1929:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010564
""",
)

entry(
    index = 41,
    label = "CH3O <=> CH2O + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.58e+14, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (114.74, 'kJ/mol', '+|-', 4.606),
        T0 = (1, 'K'),
        Tmin = (393, 'K'),
        Tmax = (433, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L."],
        title = u'The Gas-Phase Decomposition of Alkoxy Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """977""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979BAT977:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010564
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010564/rk00000001.xml
Uncertainty: 3.1600001
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 42,
    label = "CH3O <=> CH2O + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.61e+10, 's^-1'),
        n = 1.31,
        Ea = (131.298, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Huynh, L.K.", "Violi, A."],
        title = u'Thermal decomposition of methyl butanoate: Ab initio study of a biodiesel fuel surrogate',
        journal = "J. Org. Chem.",
        volume = "73",
        pages = """94-101""",
        year = "2008",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2008HUY/VIO94-101:15",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00010564

The authors presented the Arrhenius expressions for rate constant using erroneous units for activation energy [kcal/mol]
""",
)

entry(
    index = 43,
    label = "CH3O <=> CH2O + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.49e+37, 's^-1'),
        n = 0,
        Ea = (107.8, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (850, 'K'),
    ),
    reference = Article(
        authors = ["Hippler, H.", "Striebel, F.", "Viskolcz, B."],
        title = u'A Detailed Experimental and Theoretical Study on the Decomposition of Methoxy Radicals',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "3",
        pages = """2450-2458""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001HIP/STR2450-2458:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00010564
Pressure dependence: Rate constant is high pressure limit

This high pressure limiting rate constant derived from theory is in excellent agreement with the present experimental data (678 - 808 K) and literature data (297 - 605 K ) on the isotope exchange reaction
H2CO + D -> HDCO + H
which can be related to the high pressure rate of methoxy radical decomposition.
""",
)

entry(
    index = 44,
    label = "CH2O + H <=> CH3O",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.4e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (17.196, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:29",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010564
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 45,
    label = "CH2O + H <=> CH3O",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (199, 'm^3/(mol*s)'),
        n = 1.66,
        Ea = (7.188, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Huynh, L.K.", "Violi, A."],
        title = u'Thermal decomposition of methyl butanoate: Ab initio study of a biodiesel fuel surrogate',
        journal = "J. Org. Chem.",
        volume = "73",
        pages = """94-101""",
        year = "2008",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2008HUY/VIO94-101:16",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00010564

The authors presented the Arrhenius expressions for rate constant using erroneous units [cm3molecule-1s-1)] and activation energy [kcal/mol]
""",
)

entry(
    index = 46,
    label = "CH3O-2 <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+14, 's^-1'),
        n = 0,
        Ea = (123.886, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (950, 'K'),
        Tmax = (1050, 'K'),
    ),
    reference = Article(
        authors = ["Greenhill, P.G.", "O'Grady, B.V.", "Gilbert, R.G."],
        title = u'Theoretical prediction of CH3O and CH2OH gas phase decomposition rate coefficients',
        journal = "Aust. J. Chem.",
        volume = "39",
        pages = """1929""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986GRE/OGR1929:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011282
""",
)

entry(
    index = 47,
    label = "CH3O-2 <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+09, 's^-1'),
        n = 0,
        Ea = (121.391, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1540, 'K'),
        Tmax = (2180, 'K'),
        Pmin = (21300, 'Pa'),
        Pmax = (62000, 'Pa'),
    ),
    reference = Article(
        authors = ["Bowman, C.T."],
        title = u'A Shock-Tube Investigation of the High-Temperature Oxidation of Methanol',
        journal = "Combust. Flame",
        volume = "25",
        pages = """343""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975BOW343:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011282
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011282/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 48,
    label = "CH3O-2 <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.6e+10, 's^-1'),
        n = 0,
        Ea = (121.391, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1500, 'K'),
        Tmax = (1900, 'K'),
        Pmin = (933, 'Pa'),
        Pmax = (933, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsuboi, T.", "Katoh, M.", "Kikuchi, S.", "Hashimoto, K."],
        title = u'Thermal Decomposition of Methanol behind Shock Waves',
        journal = "Jpn. J. Appl. Phys.",
        volume = "20",
        pages = """985""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981TSU/KAT985:7",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011282
Bath gas: Ar
""",
)

entry(
    index = 49,
    label = "CH2O + H <=> CH3O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12600, 'm^3/(mol*s)'),
        n = 0,
        Ea = (4.997, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1500, 'K'),
        Tmax = (1900, 'K'),
        Pmin = (709000, 'Pa'),
        Pmax = (709000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsuboi, T.", "Katoh, M.", "Kikuchi, S.", "Hashimoto, K."],
        title = u'Thermal Decomposition of Methanol behind Shock Waves',
        journal = "Jpn. J. Appl. Phys.",
        volume = "20",
        pages = """985""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981TSU/KAT985:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011282
Bath gas: Ar
""",
)

entry(
    index = 50,
    label = "C2H3 <=> C2H2 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+14, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (166.289, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combustion modelling',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """411-429""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992BAU/COB411-429:156",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011402
Uncertainty: 3.1600001
""",
)

entry(
    index = 51,
    label = "C2H3 <=> C2H2 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.6e+14, 's^-1', '*|/', 5),
        n = 0,
        Ea = (158.806, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:154",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011402
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011402/rk00000004.xml
Uncertainty: 5.0
""",
)

entry(
    index = 52,
    label = "C2H3 <=> C2H2 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.87e+08, 's^-1'),
        n = 1.62,
        Ea = (154.649, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (879, 'K'),
        Tmax = (1060, 'K'),
        Pmin = (240, 'Pa'),
        Pmax = (2000, 'Pa'),
    ),
    reference = Article(
        authors = ["Knyazev, V.D.", "Slagle, I.R."],
        title = u'Experimental and theoretical study of the C2H3 = H + C2H2 reaction. Tunneling and the shape of falloff curves',
        journal = "J. Phys. Chem.",
        volume = "100",
        pages = """16899-16911""",
        year = "1996",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996KNY/SLA16899-16911:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011402
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 53,
    label = "C2H3 <=> C2H2 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.29e+13, 's^-1'),
        n = 0,
        Ea = (192.064, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (302, 'K'),
    ),
    reference = Article(
        authors = ["Naroznik, M.", "Niedzielski, J."],
        title = u'Propylene photolysis at 6.7 eV: Calculation of the quantum yields for the secondary processes',
        journal = "J. Photochem.",
        volume = "32",
        pages = """281""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986NAR/NIE281:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011402
""",
)

entry(
    index = 54,
    label = "C2H3 <=> C2H2 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+12, 's^-1'),
        n = 0,
        Ea = (160.469, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Dean, A.M."],
        title = u'Predictions of pressure and temperature effects upon radical addition and recombination reactions',
        journal = "J. Phys. Chem.",
        volume = "89",
        pages = """4600-4608""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:36",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011402
""",
)

entry(
    index = 55,
    label = "C2H3 <=> C2H2 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.93e+12, 's^-1'),
        n = 0,
        Ea = (186.244, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1200, 'K'),
        Tmax = (1900, 'K'),
        Pmin = (50700, 'Pa'),
        Pmax = (50700, 'Pa'),
    ),
    reference = Article(
        authors = ["Rao, V.S.", "Skinner, G.B."],
        title = u'Reactions of vinyl radicals at high temperatures: Pyrolysis of vinyl bromide and vinyl iodide and the reaction H + C2D2 \u2192\x92 D + C2HD',
        journal = "J. Phys. Chem.",
        volume = "92",
        pages = """6313""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988RAO/SKI6313:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011402
Bath gas: Ar
""",
)

entry(
    index = 56,
    label = "C2H3 <=> C2H2 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+13, 's^-1'),
        n = 0,
        Ea = (172.11, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (872, 'K'),
        Tmax = (1080, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Manion, J.A.", "Louw, R."],
        title = u'Gas-phase hydrogenolysis of chloroethene: Rates, products, and computer modelling',
        journal = "J. Chem. Soc. Perkin Trans. 2",
        pages = """1547-1555""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988MAN/LOU1547-1555:14",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011402
Bath gas: N2
""",
)

entry(
    index = 57,
    label = "C2H3 <=> C2H2 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+11, 's^-1'),
        n = 0,
        Ea = (168.784, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1260, 'K'),
        Tmax = (1310, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Weissman, M.", "Benson, S.W."],
        title = u'Pyrolysis of methyl chloride, a pathway in the chlorine-catalyzed polymerization of methane',
        journal = "Int. J. Chem. Kinet.",
        volume = "16",
        pages = """307-333""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WEI/BEN307-333:14",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011402
""",
)

entry(
    index = 58,
    label = "C2H2 + H <=> C2H3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.43e+06, 'm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (10.809, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (400, 'K'),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combustion modelling',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """411-429""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992BAU/COB411-429:59",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011402
Uncertainty: 2.0
Bath gas: He
""",
)

entry(
    index = 59,
    label = "C2H2 + H <=> C2H3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.5e+06, 'm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (10.144, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:36",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011402
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011402/rk00000004.xml
Uncertainty: 5.0
""",
)

entry(
    index = 60,
    label = "C2H2 + H <=> C2H3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (36400, 'm^3/(mol*s)'),
        n = 1.09,
        Ea = (11.058, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (879, 'K'),
        Tmax = (1060, 'K'),
        Pmin = (240, 'Pa'),
        Pmax = (2000, 'Pa'),
    ),
    reference = Article(
        authors = ["Knyazev, V.D.", "Slagle, I.R."],
        title = u'Experimental and theoretical study of the C2H3 = H + C2H2 reaction. Tunneling and the shape of falloff curves',
        journal = "J. Phys. Chem.",
        volume = "100",
        pages = """16899-16911""",
        year = "1996",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996KNY/SLA16899-16911:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011402
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 61,
    label = "C2H2 + H <=> C2H3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.29e+07, 'm^3/(mol*s)', '+|-', 1.1e+06),
        n = 0,
        Ea = (11.391, 'kJ/mol', '+|-', 0.114),
        T0 = (1, 'K'),
        Tmin = (206, 'K'),
        Tmax = (461, 'K'),
        Pmin = (79300, 'Pa'),
        Pmax = (86700, 'Pa'),
    ),
    reference = Article(
        authors = ["Sugawara, K.", "Okazaki, K.", "Sato, S."],
        title = u'Temperature Dependence of the Rate Constants of H and D-Atom Additions to C2H4, C2H3D, C2D4, C2H2, and C2D2',
        journal = "Bull. Chem. Soc. Jpn.",
        volume = "54",
        pages = """2872""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981SUG/OKA2872:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011402
Bath gas: H2
Excitation technique: Ultrasonics
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 62,
    label = "C2H2 + H <=> C2H3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.43e+06, 'm^3/(mol*s)', '+|-', 1.8e+06),
        n = 0,
        Ea = (11.308, 'kJ/mol', '+|-', 0.68),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (473, 'K'),
        Pmin = (100000, 'Pa'),
        Pmax = (100000, 'Pa'),
    ),
    reference = Article(
        authors = ["Ellul, R.", "Potzinger, P.", "Reimann, B.", "Camilleri, P."],
        title = u'Arrhenius parameters for the system (CH3)3Si + D2 = (CH3)3SiD + D. The (CH3)3Si-D bond dissociation energy',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "85",
        pages = """407""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981ELL/POT407:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011402
Bath gas: He
Excitation technique: Sensitized photolysis
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 63,
    label = "C2H2 + H <=> C2H3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.55e+06, 'm^3/(mol*s)', '+|-', 1.6e+06),
        n = 0,
        Ea = (10.061, 'kJ/mol', '+|-', 0.605),
        T0 = (1, 'K'),
        Tmin = (193, 'K'),
        Tmax = (400, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (93300, 'Pa'),
    ),
    reference = Article(
        authors = ["Payne, W.A.", "Stief, L.J."],
        title = u'Absolute Rate Constant for the Reaction of Atomic Hydrogen with Acetylene over an Extended Pressure and Temperature Range',
        journal = "J. Chem. Phys.",
        volume = "64",
        pages = """1150""",
        year = "1976",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976PAY/STI1150:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011402
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Resonance fluorescence
""",
)

entry(
    index = 64,
    label = "C2H2 + H <=> C2H3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.3e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (10.476, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (243, 'K'),
        Tmax = (463, 'K'),
        Pmin = (66.66, 'Pa'),
        Pmax = (4000, 'Pa'),
    ),
    reference = Article(
        authors = ["Hoyermann, K.", "Wagner, H.Gg.", "Wolfrum, J."],
        title = u'Die geschwindigkeit der reaktion von atomarem Wasserstoff mit azetylen',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "72",
        pages = """1004""",
        year = "1968",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1968HOY/WAG1004:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011402
Excitation technique: Electron beam
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 65,
    label = "CH3O <=> CH2O + H",
    degeneracy = 3,
    kinetics = Arrhenius(A=(5.5e+13, 's^-1'), n=0, Ea=(101.1, 'kJ/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003RAU/BOY431-442:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00010564
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010564/rk00000022.xml

Rate expression does not contain tunneling contributions.
""",
)

entry(
    index = 66,
    label = "C2H4 + CH3 <=> C3H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (0.0176, 'm^3/(mol*s)'),
        n = 2.48,
        Ea = (25.648, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:7",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002218
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 67,
    label = "C2H4 + CH3 <=> C3H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (211000, 'm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (30.764, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (600, 'K'),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combustion modelling',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """411-429""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992BAU/COB411-429:43",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002218
Uncertainty: 2.0
""",
)

entry(
    index = 68,
    label = "C2H4 + CH3 <=> C3H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (331000, 'm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (32.26, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W.", "Hampson, R.F."],
        title = u'Chemical kinetic data base for combustion chemistry. Part I. Methane and related compounds',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "15",
        pages = """1087""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:50",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002218
Uncertainty: 1.3
""",
)

entry(
    index = 69,
    label = "C2H4 + CH3 <=> C3H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (209000, 'm^3/(mol*s)', '*|/', 3.16),
        n = 0,
        Ea = (30.514, 'kJ/mol', '+|-', 4.274),
        T0 = (1, 'K'),
        Tmin = (350, 'K'),
        Tmax = (503, 'K'),
        Pmin = (73100, 'Pa'),
        Pmax = (86900, 'Pa'),
    ),
    reference = Article(
        authors = ["Holt, P.M.", "Kerr, J.A."],
        title = u'Kinetics of Gas-Phase Addition Reactions of Methyl Radicals. I. Addition to Ethylene, Acetylene, and Benzene',
        journal = "Int. J. Chem. Kinet.",
        volume = "9",
        pages = """185""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977HOL/KER185:3",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00002218
Uncertainty: 3.1600001
Bath gas: iso-C4H10
""",
)

entry(
    index = 70,
    label = "C2H4 + CH3 <=> C3H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (331000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (32.26, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (353, 'K'),
        Tmax = (503, 'K'),
        Pmin = (1733, 'Pa'),
        Pmax = (400000, 'Pa'),
    ),
    reference = Book(
        authors = ["Kerr, J.A.", "Parsonage, M.J."],
        title = u'Evaluated Kinetic Data on Gas Phase Addition Reactions. Reactions of Atoms and Radicals with Alkenes, Alkynes and Aromatic Compounds',
        publisher = "London",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972KER/PARB:7",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002218
""",
)

entry(
    index = 71,
    label = "C2H4 + CH3 <=> C3H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (31600, 'm^3/(mol*s)'),
        n = 0,
        Ea = (33.008, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (676, 'K'),
        Tmax = (813, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (3466, 'Pa'),
    ),
    reference = Article(
        authors = ["Camilleri, P.", "Marshall, R.M.", "Purnell, H."],
        title = u'Arrhenius Parameters for the Unimolecular Decompositions of Azomethane and n-Propyl and Isopropyl Radicals and for Methyl Radical Attack on Propane',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "71",
        pages = """1491""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975CAM/MAR1491:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002218
Bath gas: C3H8
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 72,
    label = "C2H4 + CH3 <=> C3H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (459000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (32.759, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (392, 'K'),
        Tmax = (434, 'K'),
    ),
    reference = Article(
        authors = ["Hogg, A.M.", "Kebarle, P."],
        title = u'Addition of methyl radicals to vinyl chloride and catalysis of di-t-butyl peroxide decomposition by chlorinated compounds',
        journal = "J. Am. Chem. Soc.",
        volume = "86",
        pages = """4558-4562""",
        year = "1964",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1964HOG/KEB4558-4562:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002218
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002218/rk00000001.xml
Bath gas: (tert-C4H9O)2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 73,
    label = "C3H7 <=> C2H4 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.24e+10, 's^-1'),
        n = 0.87,
        Ea = (127.445, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:17",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002218
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 74,
    label = "C3H7 <=> C2H4 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.23e+13, 's^-1'),
        n = -0.1,
        Ea = (126.38, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = Article(
        authors = ["Bencsura, A.", "Knyazev, V.D.", "Xing, S-B.", "Slagle, I.R.", "Gutman, D."],
        title = u'Kinetics of the thermal decomposition of the n-propyl radical',
        journal = "Symp. Int. Combust. Proc.",
        volume = "24",
        pages = """629-635""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992BEN/KNY629-635:1",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00002218
Bath gas: N2
""",
)

entry(
    index = 75,
    label = "C3H7 <=> C2H4 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.2e+13, 's^-1', '*|/', 1.2),
        n = 0,
        Ea = (126.38, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 3. Propane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "17",
        pages = """887""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:93",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002218
Uncertainty: 1.2
Bath gas: Products
""",
)

entry(
    index = 76,
    label = "C3H7 <=> C2H4 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3e+14, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (138.852, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:124",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002218
Uncertainty: 3.1600001
""",
)

entry(
    index = 77,
    label = "C3H7 <=> C2H4 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+13, 's^-1'),
        n = 0,
        Ea = (127.211, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (800, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'The stability of alkyl radicals',
        journal = "J. Am. Chem. Soc.",
        volume = "107",
        pages = """2872-2880""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985TSA2872-2880:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from detailed balance/reverse rate""",
    longDesc = 
u"""
PrIMe Reaction: r00002218
""",
)

entry(
    index = 78,
    label = "C3H7 <=> C2H4 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+13, 's^-1'),
        n = 0,
        Ea = (138.02, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Dean, A.M."],
        title = u'Predictions of pressure and temperature effects upon radical addition and recombination reactions',
        journal = "J. Phys. Chem.",
        volume = "89",
        pages = """4600-4608""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:29",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002218
""",
)

entry(
    index = 79,
    label = "C3H7 <=> C2H4 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.04e+12, 's^-1'),
        n = 0,
        Ea = (116.403, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (609, 'K'),
        Tmax = (648, 'K'),
        Pmin = (2533, 'Pa'),
        Pmax = (2533, 'Pa'),
    ),
    reference = Article(
        authors = ["Mintz, K.J.", "Le Roy, D.J."],
        title = u'Kinetics of radical reactions in sodium diffusion flames',
        journal = "Can. J. Chem.",
        volume = "56",
        pages = """941""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978MIN/LER941:7",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002218
Bath gas: He
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 80,
    label = "C3H7 <=> C2H4 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+12, 's^-1'),
        n = 0,
        Ea = (136.357, 'kJ/mol', '+|-', 8.156),
        T0 = (1, 'K'),
        Tmin = (676, 'K'),
        Tmax = (813, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (3466, 'Pa'),
    ),
    reference = Article(
        authors = ["Camilleri, P.", "Marshall, R.M.", "Purnell, H."],
        title = u'Arrhenius Parameters for the Unimolecular Decompositions of Azomethane and n-Propyl and Isopropyl Radicals and for Methyl Radical Attack on Propane',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "71",
        pages = """1491""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975CAM/MAR1491:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002218
Bath gas: C3H8
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 81,
    label = "C3H7 <=> C2H4 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.5e+14, 's^-1'),
        n = 0,
        Ea = (136.357, 'kJ/mol', '+|-', 2.727),
        T0 = (1, 'K'),
        Tmin = (525, 'K'),
        Tmax = (623, 'K'),
        Pmin = (667, 'Pa'),
        Pmax = (93300, 'Pa'),
    ),
    reference = Article(
        authors = ["Papic, M.M.", "Laidler, K.J."],
        title = u'Kinetics of the Mercury-Photosensitized Decomposition of Propane. Part II. Reactions of the Propyl Radicals',
        journal = "Can. J. Chem.",
        volume = "49",
        pages = """549""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971PAP/LAI549:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002218
Bath gas: C3H8
Excitation technique: Sensitized photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 82,
    label = "C3H7 <=> C2H4 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.47e+13, 's^-1'),
        n = 0,
        Ea = (131.369, 'kJ/mol', '+|-', 1.314),
        T0 = (1, 'K'),
        Tmin = (533, 'K'),
        Tmax = (573, 'K'),
        Pmin = (7333, 'Pa'),
        Pmax = (26100, 'Pa'),
    ),
    reference = Article(
        authors = ["Lin, M.C.", "Laidler, K.J."],
        title = u'Kinetics of the decompositions of ethane and propane sensitized by azomethane. The decomposition of the normal propyl radical',
        journal = "Can. J. Chem.",
        volume = "44",
        pages = """2927-2940""",
        year = "1966",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1966LIN/LAI2927-2940:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002218
Bath gas: C3H8
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 83,
    label = "C3H7 <=> C2H4 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.29e+15, 's^-1'),
        n = 0,
        Ea = (144.672, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (297, 'K'),
        Tmax = (564, 'K'),
        Pmin = (853, 'Pa'),
        Pmax = (2800, 'Pa'),
    ),
    reference = Article(
        authors = ["Kerr, J.A.", "Calvery, J.G."],
        title = u'The photolysis of azo-n-propane; the decomposition of the n-propyl radical',
        journal = "J. Am. Chem. Soc.",
        volume = "83",
        pages = """3391""",
        year = "1961",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1961KER/CAL3391:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002218
Bath gas: (n-C3H7)-N=N-(n-C3H7)
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 84,
    label = "C3H7 <=> C2H4 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5e+11, 's^-1'),
        n = 0,
        Ea = (105.594, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (543, 'K'),
        Tmax = (694, 'K'),
        Pmin = (1200, 'Pa'),
        Pmax = (4400, 'Pa'),
    ),
    reference = Article(
        authors = ["Kerr, J.A.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part 1.-n-Propyl radicals from the photolysis of n-butyraldehyde',
        journal = "Trans. Faraday Soc.",
        volume = "55",
        pages = """572""",
        year = "1959",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1959KER/TRO572:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002218
Bath gas: n-C3H7CHO
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 85,
    label = "C3H7 <=> C2H4 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.85e+15, 's^-1'),
        n = 0,
        Ea = (146.335, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (471, 'K'),
        Tmax = (560, 'K'),
        Pmin = (11200, 'Pa'),
        Pmax = (13600, 'Pa'),
    ),
    reference = Article(
        authors = ["Calvert, J.G.", "Sleppy, W.C."],
        title = u'A kinetic study of the n-propyl radical decomposition reaction',
        journal = "J. Am. Chem. Soc.",
        volume = "81",
        pages = """1544-1546""",
        year = "1959",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1959CAL/SLE1544-1546:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002218
Bath gas: (CH3N)2
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 86,
    label = "C3H7 <=> C2H4 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.7e+13, 's^-1'),
        n = 0,
        Ea = (125.693, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (680, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = Article(
        authors = ["Zheng, X.B.", "Blowers, P."],
        title = u'Kinetic modeling of the propyl radical beta-scission reaction: An application of composite energy methods',
        journal = "Ind. Eng. Chem. Res.",
        volume = "45",
        pages = """530-535""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006ZHE/BLO530-535:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00002218
Pressure dependence: Rate constant is high pressure limit

Reaction potential energy surface was studied using quantum chemistry and rate constants were calculated using RRKM theory. A simple parameterization of rate constants suitable for use in engineering applications is presented.
""",
)

entry(
    index = 87,
    label = "C3H7 <=> C2H4 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+16, 's^-1'),
        n = 0,
        Ea = (227.817, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (843, 'K'),
        Tmax = (863, 'K'),
    ),
    reference = Article(
        authors = ["Blackmore, D.R.", "Hinshelwood, C."],
        title = u'Derivation of rate constants for steps in the free-radical chain decomposition of paraffins',
        journal = "Proc. R. Soc. London A",
        volume = "268",
        pages = """36""",
        year = "1962",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1962BLA/HIN36:15",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00002218
""",
)

entry(
    index = 88,
    label = "C3H7 <=> C2H4 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+13, 's^-1'),
        n = 0,
        Ea = (129.706, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (573, 'K'),
        Tmax = (723, 'K'),
    ),
    reference = Article(
        authors = ["Jackson, W.M.", "McNesby, J.R."],
        title = u'Photolysis of acetone-d6 in the presence of propane-2,2-d2. Decomposition of the n-propyl radical',
        journal = "J. Am. Chem. Soc.",
        volume = "83",
        pages = """4891""",
        year = "1961",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1961JAC/MCN4891:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00002218
""",
)

entry(
    index = 89,
    label = "C3H4 + H <=> C3H5",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.2e+07, 'm^3/(mol*s)', '*|/', 2.51),
        n = 0,
        Ea = (8.813, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (500, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:86",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00006986
Uncertainty: 2.51
""",
)

entry(
    index = 90,
    label = "C3H4 + H <=> C3H5",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (120000, 'm^3/(mol*s)', '*|/', 2.5),
        n = 0.69,
        Ea = (12.555, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (350, 'K'),
        Tmax = (1200, 'K'),
        Pmin = (203000, 'Pa'),
        Pmax = (709000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W.", "Walker, J.A."],
        title = u'Pyrolysis of 1,7-octadiene and the kinetic and thermodynamic stability of allyl and 4-pentenyl radicals',
        journal = "J. Phys. Chem.",
        volume = "96",
        pages = """8378-8384""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992TSA/WAL8378-8384:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00006986
Uncertainty: 2.5
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 91,
    label = "C3H4 + H <=> C3H5",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4e+06, 'm^3/(mol*s)', '+|-', 2e+06),
        n = 0,
        Ea = (11.308, 'kJ/mol', '+|-', 1.696),
        T0 = (1, 'K'),
        Tmin = (273, 'K'),
        Tmax = (470, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (2666, 'Pa'),
    ),
    reference = Article(
        authors = ["Wagner, H.Gg.", "Zellner, R."],
        title = u'Reaktionen von Wasserstoffatomen mit ungesaettigten C3-Kohlenwasserstoffen. III. Die Reaktion von H-Atomen mit Allen',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "76",
        pages = """667""",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972WAG/ZEL667:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00006986
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00006986/rk00000001.xml
Bath gas: He
Excitation technique: Electron beam
Analytical technique: Gas chromatography
""",
)

entry(
    index = 92,
    label = "C3H5 <=> C3H4 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.4e+13, 's^-1', '*|/', 5),
        n = 0,
        Ea = (251.097, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:77",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00006986
Uncertainty: 5.0
""",
)

entry(
    index = 93,
    label = "C3H5 <=> C3H4 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.3e+79, 's^-1', '*|/', 0.3),
        n = -19.29,
        Ea = (398.9, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1600, 'K'),
        Pmin = (100000, 'Pa'),
        Pmax = (100000, 'Pa'),
    ),
    reference = Article(
        authors = ["Fernandes, R.X.", "Giri, B.R.", "Hippler, H.", "Kachiani, C.", "Striebel, F."],
        title = u'Shock wave study on the thermal unimolecular decomposition of allyl radicals',
        journal = "J. Phys. Chem. A",
        volume = "109",
        pages = """1063-1070""",
        year = "2005",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2005FER/GIR1063-1070:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00006986
Uncertainty: 0.30000001
Pressure dependence: Rate constant is pressure dependent

Master equation / RRKM modeling was performed. Model parameters were adjusted to reproduce experimental k(T) dependences in the 0.25 - 4.5 Bar pressure range and 1125 - 1570 K temperature range.
""",
)

entry(
    index = 94,
    label = "C3H5 <=> C3H4 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.3e+67, 's^-1', '*|/', 0.3),
        n = -15.61,
        Ea = (369.1, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1600, 'K'),
        Pmin = (100000, 'Pa'),
        Pmax = (100000, 'Pa'),
    ),
    reference = Article(
        authors = ["Fernandes, R.X.", "Giri, B.R.", "Hippler, H.", "Kachiani, C.", "Striebel, F."],
        title = u'Shock wave study on the thermal unimolecular decomposition of allyl radicals',
        journal = "J. Phys. Chem. A",
        volume = "109",
        pages = """1063-1070""",
        year = "2005",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2005FER/GIR1063-1070:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00006986
Uncertainty: 0.30000001
Pressure dependence: Rate constant is pressure dependent

Master equation / RRKM modeling was performed. Model parameters were adjusted to reproduce experimental k(T) dependences in the 0.25 - 4.5 Bar pressure range and 1125 - 1570 K temperature range.
""",
)

entry(
    index = 95,
    label = "C3H5 <=> C3H4 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.49e+11, 's^-1', '*|/', 10),
        n = 0.84,
        Ea = (250.266, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (350, 'K'),
        Tmax = (1200, 'K'),
        Pmin = (203000, 'Pa'),
        Pmax = (709000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W.", "Walker, J.A."],
        title = u'Pyrolysis of 1,7-octadiene and the kinetic and thermodynamic stability of allyl and 4-pentenyl radicals',
        journal = "J. Phys. Chem.",
        volume = "96",
        pages = """8378-8384""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992TSA/WAL8378-8384:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00006986
Uncertainty: 10.0
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 96,
    label = "C3H5 <=> C3H4 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.63e+13, 's^-1'),
        n = 0,
        Ea = (250.266, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (302, 'K'),
    ),
    reference = Article(
        authors = ["Naroznik, M.", "Niedzielski, J."],
        title = u'Propylene photolysis at 6.7 eV: Calculation of the quantum yields for the secondary processes',
        journal = "J. Photochem.",
        volume = "32",
        pages = """281""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986NAR/NIE281:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00006986
""",
)

entry(
    index = 97,
    label = "C3H5 <=> C3H4 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+13, 's^-1'),
        n = 0,
        Ea = (256.086, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Dean, A.M."],
        title = u'Predictions of pressure and temperature effects upon radical addition and recombination reactions',
        journal = "J. Phys. Chem.",
        volume = "89",
        pages = """4600-4608""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:27",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00006986
""",
)

entry(
    index = 98,
    label = "C3H5 <=> C3H4 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+15, 's^-1'),
        n = 0,
        Ea = (265.6, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1125, 'K'),
        Tmax = (1570, 'K'),
        Pmin = (25000, 'Pa'),
        Pmax = (450000, 'Pa'),
    ),
    reference = Article(
        authors = ["Fernandes, R.X.", "Giri, B.R.", "Hippler, H.", "Kachiani, C.", "Striebel, F."],
        title = u'Shock wave study on the thermal unimolecular decomposition of allyl radicals',
        journal = "J. Phys. Chem. A",
        volume = "109",
        pages = """1063-1070""",
        year = "2005",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2005FER/GIR1063-1070:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00006986
Pressure dependence: Rate constant is high pressure limit

Rate constants were calculated using a potential energy surface based on quantum chemical calculations published elsewhere.
""",
)

entry(
    index = 99,
    label = "C3H7-2 <=> C3H6 + H",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1.11e+12, 's^-1'),
        n = 0.48,
        Ea = (153.846, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:15",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010166
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 100,
    label = "C3H7-2 <=> C3H6 + H",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1.6e+13, 's^-1', '*|/', 2),
        n = 0,
        Ea = (149.66, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 3. Propane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "17",
        pages = """887""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:49",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010166
Uncertainty: 2.0
""",
)

entry(
    index = 101,
    label = "C3H7-2 <=> C3H6 + H",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2e+14, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (162.132, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:116",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010166
Uncertainty: 3.1600001
""",
)

entry(
    index = 102,
    label = "C3H7-2 <=> C3H6 + H",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (6.5e+07, 's^-1'),
        n = 1.83,
        Ea = (147.998, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (177, 'K'),
        Tmax = (910, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (1200, 'Pa'),
    ),
    reference = Article(
        authors = ["Seakins, P.W.", "Robertson, S.H.", "Pilling, M.J.", "Slagle, I.R.", "Gmurczyk, G.W.", "Bencsura, A.", "Gutman, D.", "Tsang, W."],
        title = u'Kinetics of the unimolecular decomposition of iso-C3H7: weak collision effects in helium, argon, and nitrogen',
        journal = "J. Phys. Chem.",
        volume = "97",
        pages = """4450-4458""",
        year = "1993",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1993SEA/ROB4450-4458:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010166
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 103,
    label = "C3H7-2 <=> C3H6 + H",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.19e+13, 's^-1'),
        n = 0,
        Ea = (155.481, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (800, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'The stability of alkyl radicals',
        journal = "J. Am. Chem. Soc.",
        volume = "107",
        pages = """2872-2880""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985TSA2872-2880:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from detailed balance/reverse rate""",
    longDesc = 
u"""
PrIMe Reaction: r00010166
""",
)

entry(
    index = 104,
    label = "C3H7-2 <=> C3H6 + H",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (3.98e+13, 's^-1'),
        n = 0,
        Ea = (165.458, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Dean, A.M."],
        title = u'Predictions of pressure and temperature effects upon radical addition and recombination reactions',
        journal = "J. Phys. Chem.",
        volume = "89",
        pages = """4600-4608""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:28",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010166
""",
)

entry(
    index = 105,
    label = "C3H7-2 <=> C3H6 + H",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.51e+13, 's^-1', '*|/', 5),
        n = 0,
        Ea = (171.278, 'kJ/mol', '+|-', 10.227),
        T0 = (1, 'K'),
        Tmin = (676, 'K'),
        Tmax = (813, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (3466, 'Pa'),
    ),
    reference = Article(
        authors = ["Camilleri, P.", "Marshall, R.M.", "Purnell, H."],
        title = u'Arrhenius Parameters for the Unimolecular Decompositions of Azomethane and n-Propyl and Isopropyl Radicals and for Methyl Radical Attack on Propane',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "71",
        pages = """1491""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975CAM/MAR1491:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010166
Uncertainty: 5.0
Bath gas: C3H8
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 106,
    label = "C3H7-2 <=> C3H6 + H",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2e+14, 's^-1'),
        n = 0,
        Ea = (162.132, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (525, 'K'),
        Tmax = (623, 'K'),
        Pmin = (667, 'Pa'),
        Pmax = (93300, 'Pa'),
    ),
    reference = Article(
        authors = ["Papic, M.M.", "Laidler, K.J."],
        title = u'Kinetics of the Mercury-Photosensitized Decomposition of Propane. Part II. Reactions of the Propyl Radicals',
        journal = "Can. J. Chem.",
        volume = "49",
        pages = """549""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971PAP/LAI549:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010166
Bath gas: C3H8
Excitation technique: Sensitized photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 107,
    label = "C3H7-2 <=> C3H6 + H",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1e+15, 's^-1'),
        n = 0,
        Ea = (175.435, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (714, 'K'),
        Tmax = (776, 'K'),
        Pmin = (10100, 'Pa'),
        Pmax = (55500, 'Pa'),
    ),
    reference = Article(
        authors = ["Leathard, D.A.", "Purnell, J.H."],
        title = u'Propyl radical isomerization and heterogeneous effects in the pyrolysis of propane below 500\xb0C',
        journal = "Proc. R. Soc. London A",
        volume = "306",
        pages = """553""",
        year = "1968",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1968LEA/PUR553:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010166
Bath gas: C3H8
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 108,
    label = "C3H7-2 <=> C3H6 + H",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (6.31e+13, 's^-1'),
        n = 0,
        Ea = (154.649, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (673, 'K'),
        Tmax = (773, 'K'),
        Pmin = (1200, 'Pa'),
        Pmax = (4400, 'Pa'),
    ),
    reference = Article(
        authors = ["Kerr, J.A.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part 2. s-Propyl radicals from the photolysis of isobutyraldehyde',
        journal = "Trans. Faraday Soc.",
        volume = "55",
        pages = """921""",
        year = "1959",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1959KER/TRO921:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010166
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010166/rk00000001.xml
Bath gas: (CH3)2CHCHO
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 109,
    label = "C3H6 + H <=> C3H7-2",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (424000, 'm^3/(mol*s)'),
        n = 0.51,
        Ea = (5.146, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:2",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010166
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 110,
    label = "C3H6 + H <=> C3H7-2",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1.3e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (6.527, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for hydrocarbon pyrolysis',
        journal = "Ind. Eng. Chem.",
        volume = "31",
        pages = """3-8""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992TSA3-8:4",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00010166
""",
)

entry(
    index = 111,
    label = "C3H6 + H <=> C3H7-2",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1.32e+07, 'm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (6.527, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:62",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010166
Uncertainty: 2.0
""",
)

entry(
    index = 112,
    label = "C3H6 + H <=> C3H7-2",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (4e+06, 'm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (3.999, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:75",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010166
Uncertainty: 2.0
""",
)

entry(
    index = 113,
    label = "C3H6 + H <=> C3H7-2",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (7.24e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (5.022, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (177, 'K'),
        Tmax = (473, 'K'),
        Pmin = (667, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Book(
        authors = ["Kerr, J.A.", "Parsonage, M.J."],
        title = u'Evaluated Kinetic Data on Gas Phase Addition Reactions. Reactions of Atoms and Radicals with Alkenes, Alkynes and Aromatic Compounds',
        publisher = "London",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972KER/PARB:124",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010166
Bath gas: He
""",
)

entry(
    index = 114,
    label = "C3H6 + H <=> C3H7-2",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (5700, 'm^3/(mol*s)'),
        n = 1.16,
        Ea = (3.658, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (177, 'K'),
        Tmax = (910, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (1200, 'Pa'),
    ),
    reference = Article(
        authors = ["Seakins, P.W.", "Robertson, S.H.", "Pilling, M.J.", "Slagle, I.R.", "Gmurczyk, G.W.", "Bencsura, A.", "Gutman, D.", "Tsang, W."],
        title = u'Kinetics of the unimolecular decomposition of iso-C3H7: weak collision effects in helium, argon, and nitrogen',
        journal = "J. Phys. Chem.",
        volume = "97",
        pages = """4450-4458""",
        year = "1993",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1993SEA/ROB4450-4458:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010166
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 115,
    label = "C3H6 + H <=> C3H7-2",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (5.4e+06, 'm^3/(mol*s)', '+|-', 590000),
        n = 0,
        Ea = (5.23, 'kJ/mol', '+|-', 0.418),
        T0 = (1, 'K'),
        Tmin = (195, 'K'),
        Tmax = (390, 'K'),
        Pmin = (213, 'Pa'),
        Pmax = (2666, 'Pa'),
    ),
    reference = Article(
        authors = ["Wagner, H.Gg.", "Zellner, R."],
        title = u'Reaktionen von Wasserstoffatomen mit ungesaettigten C3-Kohlenwasserstoffen. I. Die Reaktion von H-Atomen mit Propylen',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "76",
        pages = """440""",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972WAG/ZEL440:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010166
Bath gas: He
Excitation technique: Electron beam
Analytical technique: Gas chromatography
""",
)

entry(
    index = 116,
    label = "C3H6 + H <=> C3H7-2",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (6.14e+06, 'm^3/(mol*s)', '+|-', 180000),
        n = 0,
        Ea = (5.064, 'kJ/mol', '+|-', 0.05064),
        T0 = (1, 'K'),
        Tmin = (177, 'K'),
        Tmax = (298, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (6666, 'Pa'),
    ),
    reference = Article(
        authors = ["Kurylo, M.J.", "Peterson, N.C.", "Braun, W."],
        title = u'Temperature and Pressure Effects in the Addition of H Atoms to Propylene',
        journal = "J. Chem. Phys.",
        volume = "54",
        pages = """4662""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971KUR/PET4662:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010166
Bath gas: He
Excitation technique: Thermal
Analytical technique: Resonance fluorescence
""",
)

entry(
    index = 117,
    label = "C3H7 <=> C3H6 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.14e+12, 's^-1'),
        n = 0.17,
        Ea = (149.034, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:16",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010504
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 118,
    label = "C3H7 <=> C3H6 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+14, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (156.312, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:125",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010504
Uncertainty: 3.1600001
""",
)

entry(
    index = 119,
    label = "C3H7 <=> C3H6 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+13, 's^-1'),
        n = 0,
        Ea = (161.301, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Dean, A.M."],
        title = u'Predictions of pressure and temperature effects upon radical addition and recombination reactions',
        journal = "J. Phys. Chem.",
        volume = "89",
        pages = """4600-4608""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:30",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010504
""",
)

entry(
    index = 120,
    label = "C3H7 <=> C3H6 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.11e+11, 's^-1'),
        n = 0,
        Ea = (112.245, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (567, 'K'),
        Tmax = (609, 'K'),
        Pmin = (467, 'Pa'),
        Pmax = (2440, 'Pa'),
    ),
    reference = Article(
        authors = ["Mintz, K.J.", "Le Roy, D.J."],
        title = u'Kinetics of radical reactions in sodium diffusion flames',
        journal = "Can. J. Chem.",
        volume = "56",
        pages = """941""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978MIN/LER941:8",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010504
Bath gas: He
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 121,
    label = "C3H7 <=> C3H6 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+13, 's^-1'),
        n = 0,
        Ea = (146.335, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (620, 'K'),
        Tmax = (694, 'K'),
        Pmin = (1200, 'Pa'),
        Pmax = (4400, 'Pa'),
    ),
    reference = Article(
        authors = ["Kerr, J.A.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part 1.-n-Propyl radicals from the photolysis of n-butyraldehyde',
        journal = "Trans. Faraday Soc.",
        volume = "55",
        pages = """572""",
        year = "1959",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1959KER/TRO572:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010504
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010504/rk00000001.xml
Bath gas: n-C3H7CHO
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 122,
    label = "C3H7 <=> C3H6 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+13, 's^-1'),
        n = 0,
        Ea = (158.806, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1260, 'K'),
        Tmax = (1310, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Weissman, M.", "Benson, S.W."],
        title = u'Pyrolysis of methyl chloride, a pathway in the chlorine-catalyzed polymerization of methane',
        journal = "Int. J. Chem. Kinet.",
        volume = "16",
        pages = """307-333""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WEI/BEN307-333:11",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010504
""",
)

entry(
    index = 123,
    label = "C3H7 <=> C3H6 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+14, 's^-1'),
        n = 0,
        Ea = (154.649, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (573, 'K'),
        Tmax = (723, 'K'),
    ),
    reference = Article(
        authors = ["Jackson, W.M.", "McNesby, J.R."],
        title = u'Photolysis of acetone-d6 in the presence of propane-2,2-d2. Decomposition of the n-propyl radical',
        journal = "J. Am. Chem. Soc.",
        volume = "83",
        pages = """4891""",
        year = "1961",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1961JAC/MCN4891:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010504
""",
)

entry(
    index = 124,
    label = "C3H6 + H <=> C3H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (250000, 'm^3/(mol*s)'),
        n = 0.51,
        Ea = (10.962, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:3",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010504
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 125,
    label = "C3H6 + H <=> C3H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.3e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (13.636, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for hydrocarbon pyrolysis',
        journal = "Ind. Eng. Chem.",
        volume = "31",
        pages = """3-8""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992TSA3-8:5",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00010504
""",
)

entry(
    index = 126,
    label = "C3H6 + H <=> C3H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.32e+07, 'm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (13.636, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:63",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010504
Uncertainty: 1.5
""",
)

entry(
    index = 127,
    label = "C3H6 + H <=> C3H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4e+06, 'm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (10.975, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:76",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010504
Uncertainty: 2.0
""",
)

entry(
    index = 128,
    label = "C3H6 + H <=> C3H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.24e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (12.139, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (177, 'K'),
        Tmax = (473, 'K'),
        Pmin = (667, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Book(
        authors = ["Kerr, J.A.", "Parsonage, M.J."],
        title = u'Evaluated Kinetic Data on Gas Phase Addition Reactions. Reactions of Atoms and Radicals with Alkenes, Alkynes and Aromatic Compounds',
        publisher = "London",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972KER/PARB:125",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010504
Bath gas: He
""",
)

entry(
    index = 129,
    label = "C3H6 + H <=> C3H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.4e+06, 'm^3/(mol*s)', '+|-', 620000),
        n = 0,
        Ea = (11.474, 'kJ/mol', '+|-', 0.806),
        T0 = (1, 'K'),
        Tmin = (195, 'K'),
        Tmax = (390, 'K'),
        Pmin = (213, 'Pa'),
        Pmax = (2666, 'Pa'),
    ),
    reference = Article(
        authors = ["Wagner, H.Gg.", "Zellner, R."],
        title = u'Reaktionen von Wasserstoffatomen mit ungesaettigten C3-Kohlenwasserstoffen. I. Die Reaktion von H-Atomen mit Propylen',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "76",
        pages = """440""",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972WAG/ZEL440:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010504
Bath gas: He
Excitation technique: Electron beam
Analytical technique: Gas chromatography
""",
)

entry(
    index = 130,
    label = "CH2O + CH3 <=> C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (300000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (26.51, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:34",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010632
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 131,
    label = "CH2O + CH3 <=> C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.49e-12, 'm^3/(mol*s)'),
        n = 4.98,
        Ea = (4.686, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (333, 'K'),
        Tmax = (1333, 'K'),
    ),
    reference = Article(
        authors = ["Che, C.-b.", "Zhang, H.", "Zhang, X.", "Liu, Y.", "Liu, B."],
        title = u'Ab Initio and Kinetic Study on CH3 Radical Reaction with H2CO',
        journal = "J. Phys. Chem. A",
        volume = "107",
        pages = """2929-2933""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003CHE/ZHA2929-2933:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00010632
Pressure dependence: Rate constant is high pressure limit

Quantum calculations of reaction of CH3 with CH2O. Calculated geometries at B3LYP/6-311+G(d,p) and energies at CCSD(T)/6-311G(2df,p). Also calculated energetics at B3LYP and G2 levels. Use Truhlars Polyrate program to calculate rate expressions using CVT/SCT tunneling corrections.

Considered abstraction, carbon addition, and oxygen addition channels. Abstraction dominates over addition channels by factor of 10 over carbon addition and many orders of magnitude over oxygen addition channel.  Found carbon addition channel can contribute at lower temperatures. Agreement with experimental measurements is good (factor of 2 higher) with some and only fair with others (factor of 5-10 higher). Depends on temperature range and the specific measurement.

Calculated barriers are 40 kcal/mol for abstraction, 34 kcal/mol for C addition, and 69 kcal/mol for O addition channels. Although abstraction has higher barrier than C addition, it also has larger prefactor.

Fits given here in database are NIST fits to curves in Figure 3 in paper.  Rate expressions NOT given in paper.
""",
)

entry(
    index = 132,
    label = "C2H5O <=> C2H4O + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.43e+15, 's^-1'),
        n = -0.69,
        Ea = (93.01, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:44",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010633
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 133,
    label = "C2H5O <=> C2H4O + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+14, 's^-1'),
        n = 0,
        Ea = (97.279, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:10",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010633
""",
)

entry(
    index = 134,
    label = "C2H5O <=> C2H4O + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+14, 's^-1'),
        n = 0,
        Ea = (98.111, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (393, 'K'),
        Tmax = (433, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L."],
        title = u'The Gas-Phase Decomposition of Alkoxy Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """977""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979BAT977:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010633
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 135,
    label = "C2H5O <=> C2H4O + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.3e+09, 's^-1'),
        n = 1.42,
        Ea = (85.639, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Zhang, Y.", "Zhang, S.W.", "Li, Q.S."],
        title = u'A theoretical study on the beta-C-H fission of ethoxy radical',
        journal = "Chem. Phys.",
        volume = "296",
        pages = """79-86""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004ZHA/ZHA79-86:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00010633
Pressure dependence: Rate constant is high pressure limit

Variational transition state theory calculations based on quantum chemical calculations of the potential energy surface
""",
)

entry(
    index = 136,
    label = "C2H5O <=> C2H4O + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+13, 's^-1'),
        n = 0,
        Ea = (100.6, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (400, 'K'),
        Tmax = (400, 'K'),
    ),
    reference = Article(
        authors = ["Hoyermann, K.", "Olzmann, M.", "Seeba, J.", "Viskolcz, B."],
        title = u'Reactions of C2H5 Radicals with O, O3, and NO3: Decomposition Pathways of the Intermediate C2H5O Radical',
        journal = "J. Phys. Chem. A",
        volume = "103",
        pages = """5692-5698""",
        year = "1999",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1999HOY/OLZ5692-5698:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00010633
Pressure dependence: Rate constant is high pressure limit
""",
)

entry(
    index = 137,
    label = "C2H5O <=> C2H4O + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.62e+36, 's^-1', '*|/', 0.3),
        n = 0,
        Ea = (84, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (391, 'K'),
        Tmax = (471, 'K'),
        Pmin = (6e+06, 'Pa'),
        Pmax = (6e+06, 'Pa'),
    ),
    reference = Article(
        authors = ["Caralp, F.", "Devolder, P.", "Fittschen, C.", "Gomez, N.", "Hippler, H.", "Mereau, R.", "Rayez, M.T.", "Striebel, F.", "Viskolcz, B."],
        title = u'The Thermal Unimolecular Decomposition Rate Constants of Ethoxy Radicals',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "1",
        pages = """2935-2944""",
        year = "1999",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1999CAR/DEV2935-2944:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010633
Uncertainty: 0.30000001
Pressure dependence: Rate constant is high pressure limit
""",
)

entry(
    index = 138,
    label = "C2H5O <=> C2H4O + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+14, 's^-1'),
        n = 0,
        Ea = (81.149, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (435, 'K'),
        Tmax = (491, 'K'),
        Pmin = (91200, 'Pa'),
        Pmax = (91200, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L.", "Milne, R.T."],
        title = u'The Gas-Phase Pyrolysis of Alkyl Nitrites. IV. Ethyl Nitrite',
        journal = "Int. J. Chem. Kinet.",
        volume = "9",
        pages = """549""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977BAT/MIL549:5",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010633
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010633/rk00000001.xml
Bath gas: CF4
""",
)

entry(
    index = 139,
    label = "C2H4O + H <=> C2H5O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (26.778, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:30",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010633
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 140,
    label = "C2H3O <=> C2H2O + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.43e+15, 's^-1'),
        n = -0.15,
        Ea = (190.834, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Senosiain, J.P.", "Klippenstein, S.J.", "Miller, J.A."],
        title = u'Pathways and rate coefficients for the decomposition of vinoxy and acetyl radicals',
        journal = "J. Phys. Chem. A",
        volume = "110",
        pages = """5772-5781""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006SEN/KLI5772-5781:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00012710
Pressure dependence: Rate constant is high pressure limit

Reaction potential energy surface was studied using quantum chemistry and rate constants were calculated using RRKM theory. Rate constants were calculated for wide ranges of temperatures and pressures.
""",
)

entry(
    index = 141,
    label = "C2H3O <=> C2H2O + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.58e+13, 's^-1'),
        n = 0,
        Ea = (146.335, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (800, 'K'),
        Tmax = (1220, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Colket, M.B., III", "Naegeli, D.W.", "Glassman, I."],
        title = u'High-Temperature Pyrolysis of Acetaldehyde',
        journal = "Int. J. Chem. Kinet.",
        volume = "7",
        pages = """223""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975COL/NAE223:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00012710
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012710/rk00000001.xml
Bath gas: N2
""",
)

entry(
    index = 142,
    label = "C2H2O + H <=> C2H3O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1990, 'm^3/(mol*s)'),
        n = 1.43,
        Ea = (25.318, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Senosiain, J.P.", "Klippenstein, S.J.", "Miller, J.A."],
        title = u'Pathways and rate coefficients for the decomposition of vinoxy and acetyl radicals',
        journal = "J. Phys. Chem. A",
        volume = "110",
        pages = """5772-5781""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006SEN/KLI5772-5781:5",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00012710
Pressure dependence: Rate constant is high pressure limit

Reaction potential energy surface was studied using quantum chemistry and rate constants were calculated using RRKM theory.
""",
)

entry(
    index = 143,
    label = "C2H5O-2 <=> C2H4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.19e+11, 's^-1', '+|-', 9.9e+10),
        n = 0,
        Ea = (98.942, 'kJ/mol', '+|-', 2.968),
        T0 = (1, 'K'),
        Tmin = (544, 'K'),
        Tmax = (673, 'K'),
        Pmin = (37100, 'Pa'),
        Pmax = (82100, 'Pa'),
    ),
    reference = Article(
        authors = ["Diau, E.W-G.", "Lee, Y-P."],
        title = u'Detailed rate coefficients and the enthalpy change of the equilibrium reaction OH+C2H4(+M) = HOC2H4(+M) over the temperature range 544-673 K',
        journal = "J. Chem. Phys.",
        volume = "96",
        pages = """377-386""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992DIA/LEE377-386:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00012720
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012720/rk00000001.xml
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Laser induced fluorescence
""",
)

entry(
    index = 144,
    label = "C2H4 + OH <=> C2H5O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.02e+06, 'm^3/(mol*s)', '+|-', 120000),
        n = 0,
        Ea = (-1.231, 'kJ/mol', '+|-', 0.04157),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (400, 'K'),
    ),
    reference = Article(
        authors = ["Cleary, P.A.", "Romero, M.TB.", "Blitz, M.A.", "Heard, D.E.", "Pilling, M.J.", "Seakins, P.W.", "Wang, L."],
        title = u'Determination of the temperature and pressure dependence of the reaction OH + C2H4 from 200-400 K using experimental and master equation analyses',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "8",
        pages = """5633-5642""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CLE/ROM5633-5642:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00012720
Pressure dependence: Rate constant is high pressure limit

Reaction potential energy surface was studied using quantum chemistry and rate constants were calculated using master equation modeling. Model parameters were adjusted to reproduce a large body of experimental falloff and high-pressure-limit data. Rate constants were calculated for wide ranges of temperatures and pressures.
""",
)

entry(
    index = 145,
    label = "C2H4 + OH <=> C2H5O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.19e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (3.849, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (1200, 'K'),
    ),
    reference = Article(
        authors = ["Yamada, T.", "Bozzelli, J.W.", "Lay, T."],
        title = u'Kinetic and Thermodynamic Analysis on OH Addition to Ethylene: Adduct Formation, Isomerization, and Isomer Dissociations',
        journal = "J. Phys. Chem. A",
        volume = "103",
        pages = """7646-7655""",
        year = "1999",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1999YAM/BOZ7646-7655:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00012720
Pressure dependence: Rate constant is high pressure limit
""",
)

entry(
    index = 146,
    label = "C2H4 + OH <=> C2H5O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (-3.849, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (290, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Yamada, T.", "Bozzelli, J.W.", "Lay, T."],
        title = u'Kinetic and Thermodynamic Analysis on OH Addition to Ethylene: Adduct Formation, Isomerization, and Isomer Dissociations',
        journal = "J. Phys. Chem. A",
        volume = "103",
        pages = """7646-7655""",
        year = "1999",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1999YAM/BOZ7646-7655:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00012720
Pressure dependence: Rate constant is high pressure limit
""",
)

entry(
    index = 147,
    label = "C2H4 + OH <=> C2H5O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (241000, 'm^3/(mol*s)', '+|-', 180000),
        n = 0,
        Ea = (-9.977, 'kJ/mol', '+|-', 6.685),
        T0 = (1, 'K'),
        Tmin = (544, 'K'),
        Tmax = (590, 'K'),
        Pmin = (37100, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Diau, E.W-G.", "Lee, Y-P."],
        title = u'Detailed rate coefficients and the enthalpy change of the equilibrium reaction OH+C2H4(+M) = HOC2H4(+M) over the temperature range 544-673 K',
        journal = "J. Chem. Phys.",
        volume = "96",
        pages = """377-386""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992DIA/LEE377-386:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00012720
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012720/rk00000001.xml
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Laser induced fluorescence
""",
)

entry(
    index = 148,
    label = "C2H4 + OH <=> C2H5O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (993000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (-4.016, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (590, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Liu, A.", "Jonah, C.D.", "Mulac, W.A."],
        title = u'The gas-phase reactions of hydroxyl radicals with several unsaturated hydrocarbons at atmosphere pressure',
        journal = "Radiat. Phys. Chem.",
        volume = "34",
        pages = """687-691""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989LIU/JON687-691:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00012720
Bath gas: Ar
Excitation technique: Chemical activation
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 149,
    label = "C2H4 + OH <=> C2H5O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (993000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (-3.991, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (343, 'K'),
        Tmax = (563, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Liu, A.", "Mulac, W.A.", "Jonah, C.D."],
        title = u'Kinetic isotope effects in the gas-phase reaction of hydroxyl radicals with ethylene in the temperature range 343-1173 K and at 1-atm pressure',
        journal = "J. Phys. Chem.",
        volume = "92",
        pages = """3828""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988LIU/MUL3828:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00012720
Bath gas: Ar
Excitation technique: Chemical activation
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 150,
    label = "C2H4 + OH <=> C2H5O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (723000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (-4.889, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (343, 'K'),
        Tmax = (563, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Liu, A.-D.", "Mulac, W.A.", "Jonah, C.D."],
        title = u'Pulse radiolysis study of the reaction of OH radicals with C2H4 over the temperature range 343-1173 K',
        journal = "Int. J. Chem. Kinet.",
        volume = "19",
        pages = """25""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987LIU/MUL25:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00012720
Bath gas: Ar
Excitation technique: Chemical activation
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 151,
    label = "C2H4 + OH <=> C2H5O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.226, 'm^3/(mol*s)'),
        n = 2.28,
        Ea = (-10.318, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (3000, 'K'),
    ),
    reference = Article(
        authors = ["Zhu, R.S.", "Park, J.", "Lin, M.C."],
        title = u'Ab initio kinetic study on the low-energy paths of the HO+C2H4 reaction',
        journal = "Chem. Phys. Lett.",
        volume = "408",
        pages = """25-30""",
        year = "2005",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2005ZHU/PAR25-30:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00012720
Pressure dependence: Rate constant is high pressure limit

Reaction potential energy surface was studied using quantum chemistry and rate constants were calculated using variational transition state theory / RRKM.
""",
)

entry(
    index = 152,
    label = "C2H4 + OH <=> C2H5O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18100, 'm^3/(mol*s)'),
        n = 0.72,
        Ea = (-3.534, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (500, 'K'),
    ),
    reference = Article(
        authors = ["Zhu, R.S.", "Park, J.", "Lin, M.C."],
        title = u'Ab initio kinetic study on the low-energy paths of the HO+C2H4 reaction',
        journal = "Chem. Phys. Lett.",
        volume = "408",
        pages = """25-30""",
        year = "2005",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2005ZHU/PAR25-30:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00012720
Pressure dependence: Rate constant is high pressure limit

Reaction potential energy surface was studied using quantum chemistry and rate constants were calculated using variational transition state theory / RRKM.
""",
)

entry(
    index = 153,
    label = "C2H5O-3 <=> CH2O + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+13, 's^-1'),
        n = 0,
        Ea = (106.425, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (573, 'K'),
        Tmax = (666, 'K'),
        Pmin = (1.83e+06, 'Pa'),
        Pmax = (1.83e+06, 'Pa'),
    ),
    reference = Article(
        authors = ["Sehested, J.", "Sehested, K.", "Platz, J.", "Egsgaard, H.", "Nielsen, O.J."],
        title = u'Oxidation of dimethyl ether: absolute rate constants for the self reaction of CH3OCH2 radicals, the reaction of CH3OCH2 radicals with O2, and the thermal decomposition of CH3OCH2 radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "29",
        pages = """627-636""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997SEH/SEH627-636:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015716
Bath gas: SF6
Excitation technique: Flash photolysis (laser or conventional)
Time resolution: In real time
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 154,
    label = "C2H5O-3 <=> CH2O + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+13, 's^-1'),
        n = 0,
        Ea = (106.425, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (373, 'K'),
        Tmax = (473, 'K'),
        Pmin = (400, 'Pa'),
        Pmax = (80000, 'Pa'),
    ),
    reference = Article(
        authors = ["Loucks, L.F.", "Laidler, K.J."],
        title = u'Mercury-photosensitized decomposition of dimethyl ether. Part II. The thermal decomposition of the methoxymethyl radical',
        journal = "Can. J. Chem.",
        volume = "45",
        pages = """2767-2773""",
        year = "1967",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1967LOU/LAI2767-2773:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00015716
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015716/rk00000002.xml
Bath gas: (CH3)2O
Excitation technique: Sensitized photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 155,
    label = "C2H5O-3 <=> CH2O + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.45e+14, 's^-1'),
        n = -0.22,
        Ea = (113.908, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Li, Q.S.", "Zhang, Y.", "Zhang, S.W."],
        title = u'Dual level direct ab initio and density-functional theory dynamics study on the unimolecular decomposition of CH3OCH2 radical',
        journal = "J. Phys. Chem. A:",
        volume = "108",
        pages = """2014-2019""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004LI/ZHA2014-2019:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00015716

Ab initio and DFT study of the unimolecular decomposition of CH3OCH2. A variety of different ab initio and DFT methods were used.  The highest level was QCSID(T)/aug-cc-pVTZ energies using MP21K/6-31+G(d,p) geometries. Microcanonical variational transition state theory using the VKLab program was used to calculate rate expressions using transition state potential energy surface.  Agreement with experimental data was fair with the calculated rate constants about 1.5-2.0 higher than experimental values. See Sehested et al, IJCK 29, 627 (1997) and Loucks and Laidler, Can J Chem 45, 2767 (1967).
""",
)

entry(
    index = 156,
    label = "C2H3O-2 <=> C2H2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+12, 's^-1', '+|-', 4e+11),
        n = 0,
        Ea = (125.549, 'kJ/mol', '+|-', 5.022),
        T0 = (1, 'K'),
        Tmin = (627, 'K'),
        Tmax = (713, 'K'),
        Pmin = (55200, 'Pa'),
        Pmax = (115000, 'Pa'),
    ),
    reference = Article(
        authors = ["Lai, L-H.", "Hsu, Y-C.", "Lee, Y-P."],
        title = u'The enthalpy change and the detailed rate coefficients of the equilibrium reaction OH+C2H2 + M = HOC2H2 + M over the temperature range 627-713K',
        journal = "J. Chem. Phys.",
        volume = "97",
        pages = """3092-3099""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992LAI/HSU3092-3099:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00017010
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00017010/rk00000001.xml
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Laser induced fluorescence
""",
)

entry(
    index = 157,
    label = "C2H2 + OH <=> C2H3O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.4e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (5.3, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (210, 'K'),
        Tmax = (373, 'K'),
        Pmin = (667, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Mckee, K.W.", "Blitz, M.A.", "Cleary, P.A.", "Glowacki, D.R.", "Pilling, M.J.", "Seakins, P.W.", "Wang, L.M."],
        title = u'Experimental and master equation study of the kinetics of OH+C2H2: Temperature dependence of the limiting high pressure and pressure dependent rate coefficients',
        journal = "J. Phys. Chem. A",
        volume = "111",
        pages = """4043-4055""",
        year = "2007",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2007MCK/BLI4043-4055:1",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00017010
Pressure dependence: Rate constant is high pressure limit
Experimental procedure: Static or low flow - Data taken vs time
Excitation technique: Flash photolysis (laser or conventional)
Time resolution: In real time
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 158,
    label = "C2H2 + OH <=> C2H3O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+06, 'm^3/(mol*s)', '*|/', 10),
        n = 0,
        Ea = (1.912, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (1100, 'K'),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combustion modelling',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """411-429""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992BAU/COB411-429:56",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00017010
Uncertainty: 10.0
""",
)

entry(
    index = 159,
    label = "C2H2 + OH <=> C2H3O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.12e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (5.862, 'kJ/mol', '+|-', 0.234),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (500, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Liu, A.", "Mulac, W.A.", "Jonah, C.D."],
        title = u'Temperature dependence of the rate constants of the reactions of OH radicals with C2H2 and C2D2 at 1 atm in Ar and from 333 to 1273 K',
        journal = "J. Phys. Chem.",
        volume = "92",
        pages = """5942""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988LIU/MUL5942:2",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00017010
Bath gas: Ar
""",
)

entry(
    index = 160,
    label = "C2H2 + OH <=> C2H3O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.29e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (7.566, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (800, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (1.32e+07, 'Pa'),
    ),
    reference = Article(
        authors = ["Fulle, D.", "Hamann, H.F.", "Hippler, H.", "Jansch, C.P."],
        title = u'The high pressure range of the addition of OH to C2H2 and C2H4',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "101",
        pages = """1433-1442""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997FUL/HAM1433-1442:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00017010
Bath gas: N2O
Pressure dependence: Rate constant is high pressure limit
Excitation technique: Flash photolysis (laser or conventional)
Time resolution: In real time
Analytical technique: Laser induced fluorescence
""",
)

entry(
    index = 161,
    label = "C2H2 + OH <=> C2H3O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (723000, 'm^3/(mol*s)', '+|-', 120000),
        n = 0,
        Ea = (1.688, 'kJ/mol', '+|-', 0.338),
        T0 = (1, 'K'),
        Tmin = (294, 'K'),
        Tmax = (353, 'K'),
        Pmin = (12700, 'Pa'),
        Pmax = (12700, 'Pa'),
    ),
    reference = Article(
        authors = ["Siese, M.", "Zetzsch, C."],
        title = u'Addition of OH to acetylene and consecutive reactions of the adduct with O2',
        journal = "Z. Phys. Chem. (Munich)",
        volume = "188",
        pages = """75-89""",
        year = "1995",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1995SIE/ZET75-89:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00017010
Bath gas: Ar
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Resonance fluorescence
""",
)

entry(
    index = 162,
    label = "C2H2 + OH <=> C2H3O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (66200, 'm^3/(mol*s)', '+|-', 12000),
        n = 0,
        Ea = (-12.139, 'kJ/mol', '+|-', 4.124),
        T0 = (1, 'K'),
        Tmin = (627, 'K'),
        Tmax = (713, 'K'),
        Pmin = (55200, 'Pa'),
        Pmax = (115000, 'Pa'),
    ),
    reference = Article(
        authors = ["Lai, L-H.", "Hsu, Y-C.", "Lee, Y-P."],
        title = u'The enthalpy change and the detailed rate coefficients of the equilibrium reaction OH+C2H2 + M = HOC2H2 + M over the temperature range 627-713K',
        journal = "J. Chem. Phys.",
        volume = "97",
        pages = """3092-3099""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992LAI/HSU3092-3099:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00017010
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00017010/rk00000001.xml
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Laser induced fluorescence
""",
)

entry(
    index = 163,
    label = "C2H2 + OH <=> C2H3O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.12e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (5.853, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (393, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Liu, A.", "Jonah, C.D.", "Mulac, W.A."],
        title = u'The gas-phase reactions of hydroxyl radicals with several unsaturated hydrocarbons at atmosphere pressure',
        journal = "Radiat. Phys. Chem.",
        volume = "34",
        pages = """687-691""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989LIU/JON687-691:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00017010
Bath gas: Ar
Excitation technique: Chemical activation
Analytical technique: Vis-UV absorption
Note: Invalid activation energy uncertainty (8314.472) found and ignored
""",
)

entry(
    index = 164,
    label = "C2H2 + OH <=> C2H3O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (152, 'm^3/(mol*s)'),
        n = 1.7,
        Ea = (4.182, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (250, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Miller, J.A.", "Melius, C.F."],
        title = u'A theoretical analysis of the reaction between hydroxyl and acetylene',
        journal = "Symp. Int. Combust. Proc.",
        volume = "22",
        pages = """1031-1039""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989MIL/MEL1031-1039:5",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00017010
""",
)

entry(
    index = 165,
    label = "C3H4-2 + H <=> C3H5-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.79e+06, 'm^3/(mol*s)', '+|-', 1.2e+06),
        n = 0,
        Ea = (12.971, 'kJ/mol', '+|-', 1.039),
        T0 = (1, 'K'),
        Tmin = (195, 'K'),
        Tmax = (503, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (2400, 'Pa'),
    ),
    reference = Article(
        authors = ["Wagner, H.Gg.", "Zellner, R."],
        title = u'Reaktionen von Wasserstoffatomen mit ungesaettigten C3-Kohlenwasserstoffen. II. Die Reaktion von H-Atomen mit Methylacetylen',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "76",
        pages = """518""",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972WAG/ZEL518:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002857
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002857/rk00000001.xml
Bath gas: He
Excitation technique: Electron beam
Analytical technique: Gas chromatography
""",
)

entry(
    index = 166,
    label = "C3H5-2 <=> C3H4-2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+12, 's^-1'),
        n = 0,
        Ea = (152.986, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Dean, A.M."],
        title = u'Predictions of pressure and temperature effects upon radical addition and recombination reactions',
        journal = "J. Phys. Chem.",
        volume = "89",
        pages = """4600-4608""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:38",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002857
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002857/rk00000002.xml
""",
)

entry(
    index = 167,
    label = "C3H5-2 <=> C3H4-2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.24e+13, 's^-1'),
        n = 0,
        Ea = (182.087, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (302, 'K'),
    ),
    reference = Article(
        authors = ["Naroznik, M.", "Niedzielski, J."],
        title = u'Propylene photolysis at 6.7 eV: Calculation of the quantum yields for the secondary processes',
        journal = "J. Photochem.",
        volume = "32",
        pages = """281""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986NAR/NIE281:8",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002857
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002857/rk00000003.xml
""",
)

entry(
    index = 168,
    label = "C2H5O <=> CH2O + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+13, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (90.628, 'kJ/mol', '+|-', 4.523),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."],
        title = u'Photochemical smog. Rate parameter estimates and computer simulations',
        journal = "J. Phys. Chem.",
        volume = "81",
        pages = """2483""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977BAL/BAR2483:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010632
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010632/rk00000002.xml
Uncertainty: 3.1600001
Bath gas: N2
""",
)

entry(
    index = 169,
    label = "C2H5O <=> CH2O + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15, 's^-1'),
        n = 0,
        Ea = (90.628, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (435, 'K'),
        Tmax = (491, 'K'),
        Pmin = (91200, 'Pa'),
        Pmax = (91200, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L.", "Milne, R.T."],
        title = u'The Gas-Phase Pyrolysis of Alkyl Nitrites. IV. Ethyl Nitrite',
        journal = "Int. J. Chem. Kinet.",
        volume = "9",
        pages = """549""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977BAT/MIL549:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010632
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010632/rk00000003.xml
Bath gas: CF4
""",
)

entry(
    index = 170,
    label = "C2H5O <=> CH2O + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (90.628, 'kJ/mol', '+|-', 4.523),
        T0 = (1, 'K'),
        Tmin = (393, 'K'),
        Tmax = (433, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L."],
        title = u'The Gas-Phase Decomposition of Alkoxy Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """977""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979BAT977:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010632
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010632/rk00000004.xml
Uncertainty: 3.1600001
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 171,
    label = "C2H5O <=> CH2O + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+13, 's^-1'),
        n = 0,
        Ea = (83.976, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Choo, K.Y.", "Benson, S.W."],
        title = u'Arrhenius Parameters for the Alkoxy Radical Decomposition Reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """833""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981CHO/BEN833:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Other theoretical""",
    longDesc = 
u"""
PrIMe Reaction: r00010632
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010632/rk00000005.xml
""",
)

entry(
    index = 172,
    label = "C2H5O <=> CH2O + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15, 's^-1'),
        n = 0,
        Ea = (90.628, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:9",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010632
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010632/rk00000006.xml
""",
)

entry(
    index = 173,
    label = "C2H5O <=> CH2O + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 's^-1', '*|/', 10),
        n = 0,
        Ea = (89.796, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (600, 'K'),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combustion modelling',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """411-429""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992BAU/COB411-429:122",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010632
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010632/rk00000007.xml
Uncertainty: 10.0
""",
)

entry(
    index = 174,
    label = "C2H5O <=> CH2O + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.98e+13, 's^-1'), n=0, Ea=(70.4, 'kJ/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003RAU/BOY431-442:8",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00010632
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010632/rk00000010.xml

Rate expression does not contain tunneling contributions. Temperature range not specified but it does include 298.15 K.
""",
)

entry(
    index = 175,
    label = "C2H5O <=> C2H4O + H",
    degeneracy = 2,
    kinetics = Arrhenius(A=(2.46e+13, 's^-1'), n=0, Ea=(87.6, 'kJ/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003RAU/BOY431-442:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00010633
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010633/rk00000006.xml

Rate expression does not contain tunneling contributions. Temperature range not specified but it does include 298.15 K.
""",
)

entry(
    index = 176,
    label = "C3H5-2 <=> C2H2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.26e+13, 's^-1'),
        n = 0,
        Ea = (139.683, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Dean, A.M."],
        title = u'Predictions of pressure and temperature effects upon radical addition and recombination reactions',
        journal = "J. Phys. Chem.",
        volume = "89",
        pages = """4600-4608""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:37",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00012935
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000001.xml
""",
)

entry(
    index = 177,
    label = "C3H5-2 <=> C2H2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.77e+12, 's^-1'),
        n = 0,
        Ea = (180.424, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (302, 'K'),
    ),
    reference = Article(
        authors = ["Naroznik, M.", "Niedzielski, J."],
        title = u'Propylene photolysis at 6.7 eV: Calculation of the quantum yields for the secondary processes',
        journal = "J. Photochem.",
        volume = "32",
        pages = """281""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986NAR/NIE281:7",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00012935
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000002.xml
""",
)

entry(
    index = 178,
    label = "C2H2 + CH3 <=> C3H5-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (251000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (32.177, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (644, 'K'),
        Tmax = (752, 'K'),
        Pmin = (3200, 'Pa'),
        Pmax = (56500, 'Pa'),
    ),
    reference = Article(
        authors = ["Garcia Dominguez, J.A.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part IX. The addition of methyl, ethyl, isopropyl, and t-butyl radicals to acetylene and the isomerization of alkenyl radicals',
        journal = "J. Chem. Soc.",
        pages = """940-944""",
        year = "1962",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1962GAR/TRO940-944:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00012935
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000003.xml
Bath gas: C2H2
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 179,
    label = "C2H2 + CH3 <=> C3H5-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.61e+34, 'm^3/(mol*s)'),
        n = -8.58,
        Ea = (84.808, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2500, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Dean, A.M.", "Westmoreland, P.R."],
        title = u'Bimolecular QRRK analyss of methyl radical reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "19",
        pages = """207""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987DEA/WES207:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00012935
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000004.xml
Bath gas: N2
""",
)

entry(
    index = 180,
    label = "C2H2 + CH3 <=> C3H5-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (603000, 'm^3/(mol*s)', '*|/', 3.16),
        n = 0,
        Ea = (32.426, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (600, 'K'),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combustion modelling',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """411-429""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992BAU/COB411-429:53",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012935
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000005.xml
Uncertainty: 3.1600001
""",
)

entry(
    index = 181,
    label = "C2H2 + CH3 <=> C3H5-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.57e+50, 'm^3/(mol*s)'),
        n = -13.7,
        Ea = (116.403, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Diau, E.W.", "Lin, M.C."],
        title = u'A theoretical study of the CH3 + C2H2 reaction',
        journal = "J. Chem. Phys.",
        volume = "101",
        pages = """3923-3927""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994DIA/LIN3923-3927:5",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00012935
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000006.xml
Bath gas: Ar
""",
)

entry(
    index = 182,
    label = "C2H2 + CH3 <=> C3H5-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.29e+24, 'm^3/(mol*s)'),
        n = -5.98,
        Ea = (55.79, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Diau, E.W.", "Lin, M.C."],
        title = u'A theoretical study of the CH3 + C2H2 reaction',
        journal = "J. Chem. Phys.",
        volume = "101",
        pages = """3923-3927""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994DIA/LIN3923-3927:6",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00012935
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000007.xml
Bath gas: Ar
""",
)

entry(
    index = 183,
    label = "C2H2 + CH3 <=> C3H5-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (375000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (32.51, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (370, 'K'),
        Tmax = (478, 'K'),
    ),
    reference = Article(
        authors = ["Diau, E.W.", "Lin, M.C."],
        title = u'Kinetic modeling of the CH3 + C2H2 reaction data with sensitivity analyses',
        journal = "Int. J. Chem. Kinet.",
        volume = "27",
        pages = """855-866""",
        year = "1995",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1995DIA/LIN855-866:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00012935
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000008.xml
""",
)

entry(
    index = 184,
    label = "C2H5O <=> CH2O + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.41e+12, 's^-1', '*|/', 5),
        n = 0,
        Ea = (92.291, 'kJ/mol', '+|-', 7.4),
        T0 = (1, 'K'),
        Tmin = (422, 'K'),
        Tmax = (449, 'K'),
    ),
    reference = Article(
        authors = ["Leggett, C.", "Thynne, J.C.J."],
        title = u'Decomposition of ethoxyl radicals',
        journal = "J. Chem. Soc. A",
        pages = """1188""",
        year = "1970",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1970LEG/THY1188:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010632
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010632/rk00000001.xml
Uncertainty: 5.0
Excitation technique: Thermal
Analytical technique: Mass spectrometry
Reference reaction: CH3CH2O* + CH3CH2O* -> C2H5OH + CH3CHO
""",
)

entry(
    index = 185,
    label = "C3H5-3 <=> C3H4-2 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.55e+12, 's^-1'),
        n = 0,
        Ea = (192.896, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (302, 'K'),
    ),
    reference = Article(
        authors = ["Naroznik, M.", "Niedzielski, J."],
        title = u'Propylene photolysis at 6.7 eV: Calculation of the quantum yields for the secondary processes',
        journal = "J. Photochem.",
        volume = "32",
        pages = """281""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986NAR/NIE281:9",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00015628
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015628/rk00000001.xml
""",
)

entry(
    index = 186,
    label = "C3H4-2 + H <=> C3H5-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.5e+06, 'm^3/(mol*s)', '+|-', 1.2e+06),
        n = 0,
        Ea = (8.398, 'kJ/mol', '+|-', 0.84),
        T0 = (1, 'K'),
        Tmin = (195, 'K'),
        Tmax = (503, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (2400, 'Pa'),
    ),
    reference = Article(
        authors = ["Wagner, H.Gg.", "Zellner, R."],
        title = u'Reaktionen von Wasserstoffatomen mit ungesaettigten C3-Kohlenwasserstoffen. II. Die Reaktion von H-Atomen mit Methylacetylen',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "76",
        pages = """518""",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972WAG/ZEL518:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00015628
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015628/rk00000002.xml
Bath gas: He
Excitation technique: Electron beam
Analytical technique: Gas chromatography
""",
)

entry(
    index = 187,
    label = "C3H5-3 <=> C3H4 + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.32e+13, 's^-1'),
        n = 0,
        Ea = (199.547, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (302, 'K'),
    ),
    reference = Article(
        authors = ["Naroznik, M.", "Niedzielski, J."],
        title = u'Propylene photolysis at 6.7 eV: Calculation of the quantum yields for the secondary processes',
        journal = "J. Photochem.",
        volume = "32",
        pages = """281""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986NAR/NIE281:10",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00015629
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015629/rk00000001.xml
""",
)

entry(
    index = 188,
    label = "C3H4 + H <=> C3H5-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.49e+06, 'm^3/(mol*s)', '+|-', 2e+06),
        n = 0,
        Ea = (8.398, 'kJ/mol', '+|-', 0.84),
        T0 = (1, 'K'),
        Tmin = (273, 'K'),
        Tmax = (470, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (2666, 'Pa'),
    ),
    reference = Article(
        authors = ["Wagner, H.Gg.", "Zellner, R."],
        title = u'Reaktionen von Wasserstoffatomen mit ungesaettigten C3-Kohlenwasserstoffen. III. Die Reaktion von H-Atomen mit Allen',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "76",
        pages = """667""",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972WAG/ZEL667:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015629
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015629/rk00000002.xml
Bath gas: He
Excitation technique: Electron beam
Analytical technique: Gas chromatography
""",
)

entry(
    index = 189,
    label = "CHO2 <=> CO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.74e+12, 's^-1'),
        n = 0.31,
        Ea = (138.02, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2200, 'K'),
        Pmin = (13.33, 'Pa'),
        Pmax = (133000, 'Pa'),
    ),
    reference = Article(
        authors = ["Larson, c.W.", "Stewart, P.H.", "Golden, D.M."],
        title = u'Pressure and temperature dependence of reactions proceeding via a bound complex. An approach for combustion and atmospheric chemistry modelers. Application to HO + CO \u2192\x92 [HOCO] \u2192\x92 H + CO2',
        journal = "Int. J. Chem. Kinet.",
        volume = "20",
        pages = """27""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988LAR/STE27:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00015704
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015704/rk00000001.xml
Bath gas: N2
""",
)

entry(
    index = 190,
    label = "C2H4 + C2H3 <=> C4H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (200000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (8.398, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1260, 'K'),
        Tmax = (1310, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Weissman, M.", "Benson, S.W."],
        title = u'Pyrolysis of methyl chloride, a pathway in the chlorine-catalyzed polymerization of methane',
        journal = "Int. J. Chem. Kinet.",
        volume = "16",
        pages = """307-333""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WEI/BEN307-333:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00002230
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002230/rk00000001.xml
Activation energy is a lower limit.
""",
)

entry(
    index = 191,
    label = "C2H2 + C2H5 <=> C4H7-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (50100, 'm^3/(mol*s)'),
        n = 0,
        Ea = (29.267, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (373, 'K'),
        Tmax = (473, 'K'),
        Pmin = (2666, 'Pa'),
        Pmax = (20000, 'Pa'),
    ),
    reference = Book(
        authors = ["Kerr, J.A.", "Parsonage, M.J."],
        title = u'Evaluated Kinetic Data on Gas Phase Addition Reactions. Reactions of Atoms and Radicals with Alkenes, Alkynes and Aromatic Compounds',
        publisher = "London",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972KER/PARB:38",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002412
""",
)

entry(
    index = 192,
    label = "C2H2 + C2H5 <=> C4H7-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (100000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (29.267, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (373, 'K'),
        Tmax = (473, 'K'),
        Pmin = (1867, 'Pa'),
        Pmax = (5999, 'Pa'),
    ),
    reference = Article(
        authors = ["Garcia Dominguez, J.A.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part IX. The addition of methyl, ethyl, isopropyl, and t-butyl radicals to acetylene and the isomerization of alkenyl radicals',
        journal = "J. Chem. Soc.",
        pages = """940-944""",
        year = "1962",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1962GAR/TRO940-944:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002412
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002412/rk00000001.xml
Bath gas: C2H2
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 193,
    label = "C4H9 <=> C4H8 + H",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (5.66e+11, 's^-1'),
        n = 0.7,
        Ea = (153.009, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:18",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00009777
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 194,
    label = "C4H9 <=> C4H8 + H",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (8.3e+13, 's^-1', '*|/', 3),
        n = 0,
        Ea = (159.638, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 4. Isobutane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "19",
        pages = """1-68""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:59",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00009777
Uncertainty: 3.0
""",
)

entry(
    index = 195,
    label = "C4H9 <=> C4H8 + H",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (2.18e+09, 's^-1'),
        n = 1.48,
        Ea = (150.492, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (712, 'K'),
        Tmax = (779, 'K'),
        Pmin = (120, 'Pa'),
        Pmax = (933, 'Pa'),
    ),
    reference = Article(
        authors = ["Knyazev, V.D.", "Dubinsky, I.A.", "Slagle, I.R.", "Gutman, D."],
        title = u'Unimolecular decomposition of t-C4H9 radical',
        journal = "J. Phys. Chem.",
        volume = "98",
        pages = """5279-5289""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994KNY/DUB5279-5289:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00009777
Bath gas: He
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 196,
    label = "C4H9 <=> C4H8 + H",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (8.32e+13, 's^-1'),
        n = 0,
        Ea = (157.144, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (800, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'The stability of alkyl radicals',
        journal = "J. Am. Chem. Soc.",
        volume = "107",
        pages = """2872-2880""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985TSA2872-2880:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from detailed balance/reverse rate""",
    longDesc = 
u"""
PrIMe Reaction: r00009777
""",
)

entry(
    index = 197,
    label = "C4H9 <=> C4H8 + H",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (4.68e+14, 's^-1', '*|/', 1.29),
        n = 0,
        Ea = (164.627, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (584, 'K'),
        Tmax = (604, 'K'),
        Pmin = (6933, 'Pa'),
        Pmax = (36300, 'Pa'),
    ),
    reference = Article(
        authors = ["Canosa, C.E.", "Marshall, R.M."],
        title = u'The Rate Constant for t-C4H9 \u2192\x92 H + i-C4H8 and the Thermodynamic Parameters of t-C4H9',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """303""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981CAN/MAR303:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009777
Uncertainty: 1.29
Bath gas: N2
Excitation technique: Sensitized photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 198,
    label = "C4H9 <=> C4H8 + H",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (2e+16, 's^-1'),
        n = 0,
        Ea = (182.087, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (663, 'K'),
        Tmax = (763, 'K'),
    ),
    reference = Article(
        authors = ["Birrell, R.N.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part VII. t-butyl radicals from the photolysis of pivalaldehyde',
        journal = "J. Chem. Soc.",
        pages = """4218""",
        year = "1960",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1960BIR/TRO4218:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00009777
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009777/rk00000001.xml
Bath gas: 2,2-dimethylpropanal
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 199,
    label = "C4H8 + H <=> C4H9",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (1.06e+06, 'm^3/(mol*s)'),
        n = 0.51,
        Ea = (5.146, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:4",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00009777
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 200,
    label = "C4H8 + H <=> C4H9",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (3.09e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (6.277, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (285, 'K'),
        Tmax = (500, 'K'),
        Pmin = (267, 'Pa'),
        Pmax = (80000, 'Pa'),
    ),
    reference = Book(
        authors = ["Kerr, J.A.", "Parsonage, M.J."],
        title = u'Evaluated Kinetic Data on Gas Phase Addition Reactions. Reactions of Atoms and Radicals with Alkenes, Alkynes and Aromatic Compounds',
        publisher = "London",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972KER/PARB:135",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00009777
""",
)

entry(
    index = 201,
    label = "C4H8 + H <=> C4H9",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (2.75e+07, 'm^3/(mol*s)', '+|-', 7.95e+06),
        n = 0,
        Ea = (6.061, 'kJ/mol', '+|-', 0.765),
        T0 = (1, 'K'),
        Tmin = (299, 'K'),
        Tmax = (503, 'K'),
        Pmin = (128, 'Pa'),
        Pmax = (400, 'Pa'),
    ),
    reference = Article(
        authors = ["Bryukov, M.G.", "Slagle, I.R.", "Knyazev, V.D."],
        title = u'Kinetics of Reactions of H Atoms with Methane and Chlorinated Methanes',
        journal = "J. Phys. Chem. A",
        volume = "105",
        pages = """3107-3122""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001BRY/SLA3107-3122:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009777
Pressure dependence: None reported
Experimental procedure: Flow tube - Data taken vs distance
Excitation technique: Discharge
Analytical technique: Resonance fluorescence

Error limits are 2 sigma and reflect only statistical contributions.
""",
)

entry(
    index = 202,
    label = "C4H8 + H <=> C4H9",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (6.21e+06, 'm^3/(mol*s)'),
        n = 0.25,
        Ea = (6.128, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (712, 'K'),
        Tmax = (779, 'K'),
        Pmin = (120, 'Pa'),
        Pmax = (933, 'Pa'),
    ),
    reference = Article(
        authors = ["Knyazev, V.D.", "Dubinsky, I.A.", "Slagle, I.R.", "Gutman, D."],
        title = u'Unimolecular decomposition of t-C4H9 radical',
        journal = "J. Phys. Chem.",
        volume = "98",
        pages = """5279-5289""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994KNY/DUB5279-5289:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00009777
Bath gas: He
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 203,
    label = "C4H8 + H <=> C4H9",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (1.25e+07, 'm^3/(mol*s)', '+|-', 1e+06),
        n = 0,
        Ea = (3.6, 'kJ/mol', '+|-', 0.216),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (500, 'K'),
        Pmin = (80000, 'Pa'),
        Pmax = (80000, 'Pa'),
    ),
    reference = Article(
        authors = ["Kyogoku, T.", "Watanabe, T.", "Tsunashima, S.", "Sato, S."],
        title = u'Arrhenius parameters for the reactions of hydrogen and deuterium atoms with four butenes',
        journal = "Bull. Chem. Soc. Jpn.",
        volume = "56",
        pages = """19-21""",
        year = "1983",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1983KYO/WAT19-21:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009777
Bath gas: H2
Excitation technique: Chemical activation
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 204,
    label = "C4H8 + H <=> C4H9",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (3.89e+07, 'm^3/(mol*s)', '*|/', 1.29),
        n = 0,
        Ea = (7.491, 'kJ/mol', '+|-', 0.824),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (563, 'K'),
        Pmin = (933, 'Pa'),
        Pmax = (1067, 'Pa'),
    ),
    reference = Article(
        authors = ["Canosa, C.E.", "Marshall, R.M.", "Sheppard, A."],
        title = u'The Rate Constant for H + i-C4H8 \u2192\x92 t-C4H9 in the Range of 298-563 K',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """295""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981CAN/MAR295:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009777
Uncertainty: 1.29
Bath gas: He
Excitation technique: Electron beam
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 205,
    label = "C4H8 + H <=> C4H9",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (1.6e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (6.302, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1030, 'K'),
        Tmax = (1300, 'K'),
        Pmin = (300000, 'Pa'),
        Pmax = (400000, 'Pa'),
    ),
    reference = Article(
        authors = ["Bradley, J.N.", "West, K.O."],
        title = u'Single-pulse Shock Tube Studies of Hydrocarbon Pyrolysis. Part 5. Pyrolysis of Neopentane',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "72",
        pages = """8""",
        year = "1976",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976BRA/WES8:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00009777
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 206,
    label = "C4H8 + H <=> C4H9",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (3.63e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (5.937, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (285, 'K'),
        Tmax = (403, 'K'),
        Pmin = (267, 'Pa'),
        Pmax = (267, 'Pa'),
    ),
    reference = Article(
        authors = ["Dalgleish, D.G.", "Knox, J.H."],
        title = u'The reactions of hydrogen atoms with isobutane and isobutene',
        journal = "J. Chem. Soc. Chem. Commun.",
        pages = """917-918""",
        year = "1966",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1966DAL/KNO917-918:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009777
Bath gas: Ar
Excitation technique: Electron beam
Analytical technique: Gas chromatography
Note: Invalid activation energy uncertainty (8314.472) found and ignored
""",
)

entry(
    index = 207,
    label = "C4H7 <=> C4H6 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+13, 's^-1'),
        n = 0,
        Ea = (145.503, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1260, 'K'),
        Tmax = (1310, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Weissman, M.", "Benson, S.W."],
        title = u'Pyrolysis of methyl chloride, a pathway in the chlorine-catalyzed polymerization of methane',
        journal = "Int. J. Chem. Kinet.",
        volume = "16",
        pages = """307-333""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WEI/BEN307-333:12",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010706
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010706/rk00000001.xml
""",
)

entry(
    index = 208,
    label = "C4H9-2 <=> C4H8-2 + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.99e+11, 's^-1'),
        n = 0.59,
        Ea = (154.055, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:21",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011104
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 209,
    label = "C4H9-2 <=> C4H8-2 + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.29e+13, 's^-1'),
        n = 0,
        Ea = (152.155, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (800, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'The stability of alkyl radicals',
        journal = "J. Am. Chem. Soc.",
        volume = "107",
        pages = """2872-2880""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985TSA2872-2880:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from detailed balance/reverse rate""",
    longDesc = 
u"""
PrIMe Reaction: r00011104
""",
)

entry(
    index = 210,
    label = "C4H9-2 <=> C4H8-2 + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.58e+13, 's^-1'),
        n = 0,
        Ea = (165.458, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Dean, A.M."],
        title = u'Predictions of pressure and temperature effects upon radical addition and recombination reactions',
        journal = "J. Phys. Chem.",
        volume = "89",
        pages = """4600-4608""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:31",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011104
""",
)

entry(
    index = 211,
    label = "C4H9-2 <=> C4H8-2 + H",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (5e+12, 's^-1'),
        n = 0,
        Ea = (166.289, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (533, 'K'),
        Tmax = (613, 'K'),
        Pmin = (7866, 'Pa'),
        Pmax = (27200, 'Pa'),
    ),
    reference = Article(
        authors = ["Lin, M.C.", "Laidler, K.J."],
        title = u'Thermal decomposition of the sec-butl radical',
        journal = "Can. J. Chem.",
        volume = "45",
        pages = """1315""",
        year = "1967",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1967LIN/LAI1315:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011104
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011104/rk00000001.xml
Bath gas: n-C4H10
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 212,
    label = "C4H9-2 <=> C4H8-3 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.85e+11, 's^-1'),
        n = 0.34,
        Ea = (148.616, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:22",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011105
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 213,
    label = "C4H9-2 <=> C4H8-3 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+12, 's^-1'),
        n = 0,
        Ea = (154.649, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Dean, A.M."],
        title = u'Predictions of pressure and temperature effects upon radical addition and recombination reactions',
        journal = "J. Phys. Chem.",
        volume = "89",
        pages = """4600-4608""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:32",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011105
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011105/rk00000001.xml
""",
)

entry(
    index = 214,
    label = "C4H9-2 <=> C3H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.79e+10, 's^-1'),
        n = 1.04,
        Ea = (127.026, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:25",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011106
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 215,
    label = "C4H9-2 <=> C3H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+14, 's^-1', '*|/', 2),
        n = 0,
        Ea = (137.189, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:143",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011106
Uncertainty: 2.0
""",
)

entry(
    index = 216,
    label = "C4H9-2 <=> C3H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.67e+10, 's^-1'),
        n = 1.06,
        Ea = (129.706, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1200, 'K'),
        Pmin = (1.33, 'Pa'),
        Pmax = (1333, 'Pa'),
    ),
    reference = Article(
        authors = ["Gang, J.", "Pilling, M.J.", "Robertson, S.H."],
        title = u'Asymmetric internal rotation: application to the 2-C4H9=CH3 + C3H6 reaction',
        journal = "J. Chem. Soc. Faraday Trans.",
        volume = "93",
        pages = """1481-1491""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997GAN/PIL1481-1491:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011106
Bath gas: He
Pressure dependence: Rate constant is high pressure limit
""",
)

entry(
    index = 217,
    label = "C4H9-2 <=> C3H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.73e+10, 's^-1'),
        n = 1.11,
        Ea = (130.537, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (1500, 'K'),
        Pmin = (101, 'Pa'),
        Pmax = (1.01e+06, 'Pa'),
    ),
    reference = Article(
        authors = ["Knyazev, V.D.", "Dubinsky, I.A.", "Slagle, I.R.", "Gutman, D."],
        title = u'Experimental and theoretical study of the sec-C4H9 = CH3 + C3H6 reaction',
        journal = "J. Phys. Chem.",
        volume = "98",
        pages = """11099-11108""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994KNY/DUB11099-11108:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011106
Bath gas: Ar
Pressure dependence: Rate constant is high pressure limit
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 218,
    label = "C4H9-2 <=> C3H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.63e+13, 's^-1'),
        n = 0,
        Ea = (133.032, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (295, 'K'),
        Tmax = (305, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (120000, 'Pa'),
    ),
    reference = Article(
        authors = ["Gierczak, T.", "Gawlowski, J.", "Niedzielski, J."],
        title = u'Isomerization of chemically activated secondary butyl radical',
        journal = "React. Kinet. Catal. Lett.",
        volume = "36",
        pages = """435""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988GIE/GAW435:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011106
Bath gas: H2S
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 219,
    label = "C4H9-2 <=> C3H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.33e+12, 's^-1'),
        n = 0,
        Ea = (122.223, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (800, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'The stability of alkyl radicals',
        journal = "J. Am. Chem. Soc.",
        volume = "107",
        pages = """2872-2880""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985TSA2872-2880:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from detailed balance/reverse rate""",
    longDesc = 
u"""
PrIMe Reaction: r00011106
""",
)

entry(
    index = 220,
    label = "C4H9-2 <=> C3H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.31e+12, 's^-1'),
        n = 0,
        Ea = (135.526, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Dean, A.M."],
        title = u'Predictions of pressure and temperature effects upon radical addition and recombination reactions',
        journal = "J. Phys. Chem.",
        volume = "89",
        pages = """4600-4608""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:33",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011106
""",
)

entry(
    index = 221,
    label = "C4H9-2 <=> C3H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.1e+14, 's^-1'),
        n = 0,
        Ea = (136.357, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (533, 'K'),
        Tmax = (613, 'K'),
        Pmin = (7866, 'Pa'),
        Pmax = (27200, 'Pa'),
    ),
    reference = Article(
        authors = ["Lin, M.C.", "Laidler, K.J."],
        title = u'Thermal decomposition of the sec-butl radical',
        journal = "Can. J. Chem.",
        volume = "45",
        pages = """1315""",
        year = "1967",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1967LIN/LAI1315:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011106
Bath gas: n-C4H10
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 222,
    label = "C4H9-2 <=> C3H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.72e+14, 's^-1', '*|/', 2.14),
        n = 0,
        Ea = (138.02, 'kJ/mol', '+|-', 4.132),
        T0 = (1, 'K'),
        Tmin = (535, 'K'),
        Tmax = (613, 'K'),
    ),
    reference = Article(
        authors = ["Marshall, R.M."],
        title = u'The rate constant for the intramolecular isomerization of pentyl radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "22",
        pages = """935-950""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990MAR935-950:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011106
Uncertainty: 2.1400001
""",
)

entry(
    index = 223,
    label = "C3H6 + CH3 <=> C4H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0176, 'm^3/(mol*s)'),
        n = 2.48,
        Ea = (25.648, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:8",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011106
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 224,
    label = "C3H6 + CH3 <=> C4H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (169000, 'm^3/(mol*s)', '*|/', 1.4),
        n = 0,
        Ea = (31.013, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:40",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011106
Uncertainty: 1.4
""",
)

entry(
    index = 225,
    label = "C3H6 + CH3 <=> C4H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (178000, 'm^3/(mol*s)', '*|/', 1.78),
        n = 0,
        Ea = (29.516, 'kJ/mol', '+|-', 2.952),
        T0 = (1, 'K'),
        Tmin = (353, 'K'),
        Tmax = (753, 'K'),
        Pmin = (66700, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Baldwin, R.R.", "Keen, A.", "Walker, R.W."],
        title = u'Rate constants for the addition of methyl radicals to propene',
        journal = "J. Chem. Soc. Faraday Trans. 2",
        volume = "83",
        pages = """759""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987BAL/KEE759:3",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00011106
Uncertainty: 1.78
Bath gas: H2
""",
)

entry(
    index = 226,
    label = "C3H6 + CH3 <=> C4H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.128, 'm^3/(mol*s)'),
        n = 2.28,
        Ea = (27.604, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (1500, 'K'),
        Pmin = (101, 'Pa'),
        Pmax = (1.01e+06, 'Pa'),
    ),
    reference = Article(
        authors = ["Knyazev, V.D.", "Dubinsky, I.A.", "Slagle, I.R.", "Gutman, D."],
        title = u'Experimental and theoretical study of the sec-C4H9 = CH3 + C3H6 reaction',
        journal = "J. Phys. Chem.",
        volume = "98",
        pages = """11099-11108""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994KNY/DUB11099-11108:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011106
Bath gas: Ar
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 227,
    label = "C3H6 + CH3 <=> C4H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (79400, 'm^3/(mol*s)'),
        n = 0,
        Ea = (29.683, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (335, 'K'),
        Tmax = (424, 'K'),
    ),
    reference = Article(
        authors = ["Tedder, J.M.", "Walton, J.C.", "Winton, K.D.R."],
        title = u'Free Radical Addition to Olefins Part 9. Addition of Methyl Radicals to Fluoro-ethylenes',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "68",
        pages = """1866""",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972TED/WAL1866:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011106
Bath gas: CH3I
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 228,
    label = "C4H9-3 <=> C2H4 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.58e+12, 's^-1'),
        n = 0.46,
        Ea = (123.344, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:23",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011209
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 229,
    label = "C4H9-3 <=> C2H4 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+13, 's^-1', '*|/', 5),
        n = 0,
        Ea = (119.728, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (400, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:145",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011209
Uncertainty: 5.0
""",
)

entry(
    index = 230,
    label = "C4H9-3 <=> C2H4 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.06e+13, 's^-1'),
        n = 0,
        Ea = (116.403, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (900, 'K'),
        Pmin = (101, 'Pa'),
        Pmax = (1.01e+06, 'Pa'),
    ),
    reference = Article(
        authors = ["Knyazev, V.D.", "Slagle, I.R."],
        title = u'Unimolecular decomposition of n-C4H9 and iso-C4H9 radicals',
        journal = "J. Phys. Chem.",
        volume = "100",
        pages = """5318-5328""",
        year = "1996",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996KNY/SLA5318-5328:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011209
Bath gas: He
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 231,
    label = "C4H9-3 <=> C2H4 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.47e+13, 's^-1'),
        n = 0,
        Ea = (121.391, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (295, 'K'),
        Tmax = (305, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (120000, 'Pa'),
    ),
    reference = Article(
        authors = ["Gierczak, T.", "Gawlowski, J.", "Niedzielski, J."],
        title = u'Isomerization of chemically activated secondary butyl radical',
        journal = "React. Kinet. Catal. Lett.",
        volume = "36",
        pages = """435""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988GIE/GAW435:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011209
Bath gas: H2S
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 232,
    label = "C4H9-3 <=> C2H4 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+12, 's^-1'),
        n = 0,
        Ea = (116.403, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Dean, A.M."],
        title = u'Predictions of pressure and temperature effects upon radical addition and recombination reactions',
        journal = "J. Phys. Chem.",
        volume = "89",
        pages = """4600-4608""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:34",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011209
""",
)

entry(
    index = 233,
    label = "C4H9-3 <=> C2H4 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.73e+13, 's^-1'),
        n = 0,
        Ea = (119.728, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (430, 'K'),
        Tmax = (520, 'K'),
        Pmin = (555, 'Pa'),
        Pmax = (1653, 'Pa'),
    ),
    reference = Article(
        authors = ["Morganroth, W.E.", "Calvert, J.G."],
        title = u"The photolysis of 1,1'-azo-n-butane vapor. The reactions of the n-butyl free radical",
        journal = "J. Am. Chem. Soc.",
        volume = "88",
        pages = """5387""",
        year = "1966",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1966MOR/CAL5387:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011209
Bath gas: Di-n-butyldiazene
Excitation technique: Direct photolysis
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 234,
    label = "C4H9-3 <=> C2H4 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+11, 's^-1'),
        n = 0,
        Ea = (92.291, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (477, 'K'),
        Tmax = (689, 'K'),
        Pmin = (1560, 'Pa'),
        Pmax = (1560, 'Pa'),
    ),
    reference = Article(
        authors = ["Kerr, J.A.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part III. n-Butyl radicals from the photolysis of n-Valeraldehyde',
        journal = "J. Chem. Soc.",
        pages = """1602""",
        year = "1960",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1960KER/TRO1602:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011209
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011209/rk00000001.xml
Bath gas: n-C4H9CHO
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 235,
    label = "C4H9-3 <=> C2H4 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.68e+37, 's^-1'),
        n = 0,
        Ea = (125.845, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = Article(
        authors = ["Zheng, X.B.", "Blowers, P."],
        title = u'The application of composite energy methods to n-butyl radical beta-scission reaction kinetic estimations',
        journal = "Theor. Chem. Acct.",
        volume = "117",
        pages = """207-212""",
        year = "2007",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2007ZHE/BLO207-212:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00011209
Pressure dependence: Rate constant is pressure dependent

Ab initio study, using canonical transition state theory. (CTST)

Rate expressions calculated when P(pressure) is greater or equal to P0(switching pressure)

complete basis set (CBS) composite energies

when P0(switching pressure) is greater than or equal to P(pressure), the rate expression is:
2.04E9 x P^(.51) x e^(-9745.7/T).

CH2CH2CH2CH3 -> CH2CH2 + CH2CH3
Ea = 28.62kcal/mol
DrH = 21.57kcal/mol
no uncertainties reported.
""",
)

entry(
    index = 236,
    label = "C4H9-3 <=> C2H4 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.95e+13, 's^-1', '*|/', 5),
        n = 0,
        Ea = (119.728, 'kJ/mol', '+|-', 4.806),
        T0 = (1, 'K'),
        Tmin = (432, 'K'),
        Tmax = (520, 'K'),
    ),
    reference = Article(
        authors = ["Marshall, R.M."],
        title = u'The rate constant for the intramolecular isomerization of pentyl radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "22",
        pages = """935-950""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990MAR935-950:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011209
Uncertainty: 5.0
""",
)

entry(
    index = 237,
    label = "C2H4 + C2H5 <=> C4H9-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0132, 'm^3/(mol*s)'),
        n = 2.48,
        Ea = (25.648, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:13",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011209
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 238,
    label = "C2H4 + C2H5 <=> C4H9-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (158000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (30.514, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (348, 'K'),
        Tmax = (482, 'K'),
        Pmin = (800, 'Pa'),
        Pmax = (17300, 'Pa'),
    ),
    reference = Book(
        authors = ["Kerr, J.A.", "Parsonage, M.J."],
        title = u'Evaluated Kinetic Data on Gas Phase Addition Reactions. Reactions of Atoms and Radicals with Alkenes, Alkynes and Aromatic Compounds',
        publisher = "London",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972KER/PARB:25",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011209
""",
)

entry(
    index = 239,
    label = "C2H4 + C2H5 <=> C4H9-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.003976, 'm^3/(mol*s)'),
        n = 2.44,
        Ea = (22.449, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (1500, 'K'),
        Pmin = (101, 'Pa'),
        Pmax = (1.01e+06, 'Pa'),
    ),
    reference = Article(
        authors = ["Knyazev, V.D.", "Slagle, I.R."],
        title = u'Unimolecular decomposition of n-C4H9 and iso-C4H9 radicals',
        journal = "J. Phys. Chem.",
        volume = "100",
        pages = """5318-5328""",
        year = "1996",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996KNY/SLA5318-5328:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011209
Bath gas: He
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 240,
    label = "C2H4 + C2H5 <=> C4H9-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.48e+08, 'm^3/(mol*s)'),
        n = 0,
        Ea = (31.595, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (348, 'K'),
        Tmax = (405, 'K'),
    ),
    reference = Article(
        authors = ["Watkins, K.W.", "O'Deen, L.A."],
        title = u'Kinetics of the addition of ethyl, isopropyl, n-butyl, and isopentyl radicals to ethylene',
        journal = "J. Phys. Chem.",
        volume = "73",
        pages = """4094-4102""",
        year = "1969",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1969WAT/ODE4094-4102:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011209
Bath gas: (C2H5)2NN
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 241,
    label = "C2H4 + C2H5 <=> C4H9-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.12e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (36.002, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (417, 'K'),
        Tmax = (460, 'K'),
        Pmin = (1667, 'Pa'),
        Pmax = (8679, 'Pa'),
    ),
    reference = Article(
        authors = ["Kerr, J.A.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part V. Ethyl radicals from propionaldehyde',
        journal = "J. Chem. Soc.",
        pages = """1611""",
        year = "1960",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1960KER/TRO1611:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011209
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011209/rk00000001.xml
Bath gas: C2H5CHO
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 242,
    label = "C2H4 + C2H5 <=> C4H9-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (27.188, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (430, 'K'),
        Tmax = (520, 'K'),
        Pmin = (555, 'Pa'),
        Pmax = (1653, 'Pa'),
    ),
    reference = Article(
        authors = ["Morganroth, W.E.", "Calvert, J.G."],
        title = u"The photolysis of 1,1'-azo-n-butane vapor. The reactions of the n-butyl free radical",
        journal = "J. Am. Chem. Soc.",
        volume = "88",
        pages = """5387""",
        year = "1966",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1966MOR/CAL5387:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011209
Bath gas: Di-n-butyldiazene
""",
)

entry(
    index = 243,
    label = "C4H9-3 <=> C4H8-2 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.65e+12, 's^-1'),
        n = 0.25,
        Ea = (149.411, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:20",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011210
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 244,
    label = "C4H9-3 <=> C4H8-2 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+14, 's^-1'),
        n = 0,
        Ea = (160.469, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Dean, A.M."],
        title = u'Predictions of pressure and temperature effects upon radical addition and recombination reactions',
        journal = "J. Phys. Chem.",
        volume = "89",
        pages = """4600-4608""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:35",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011210
""",
)

entry(
    index = 245,
    label = "C4H9-3 <=> C4H8-2 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+14, 's^-1'),
        n = 0,
        Ea = (167.121, 'kJ/mol', '+|-', 16.712),
        T0 = (1, 'K'),
        Tmin = (823, 'K'),
        Tmax = (999, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (80000, 'Pa'),
    ),
    reference = Article(
        authors = ["Lin, M.C.", "Back, M.H."],
        title = u'The thermal decomposition of ethane. Part III. Secondary reactions',
        journal = "Can. J. Chem.",
        volume = "44",
        pages = """2369""",
        year = "1966",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1966LIN/BAC2369:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011210
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011210/rk00000001.xml
Bath gas: C2H6
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 246,
    label = "C4H9-3 <=> C4H8-2 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+13, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (148.829, 'kJ/mol', '+|-', 7.45),
        T0 = (1, 'K'),
        Tmin = (892, 'K'),
        Tmax = (905, 'K'),
        Pmin = (3066, 'Pa'),
        Pmax = (33300, 'Pa'),
    ),
    reference = Article(
        authors = ["MacKenzie, A.L.", "Pacey, P.D.", "Wimalasena, J.H."],
        title = u'Radical addition, decomposition, and isomerization reactions in the pyrolysis of ethane and ethylene',
        journal = "Can. J. Chem.",
        volume = "62",
        pages = """1325""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984MAC/PAC1325:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011210
Uncertainty: 3.1600001
Bath gas: C2H4
""",
)

entry(
    index = 247,
    label = "C4H8-2 + H <=> C4H9-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (250000, 'm^3/(mol*s)'),
        n = 0.51,
        Ea = (10.962, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:6",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011210
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 248,
    label = "C3H7O <=> C3H6O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.66e+14, 's^-1'),
        n = -0.48,
        Ea = (84.015, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:48",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012570
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 249,
    label = "C3H7O <=> C3H6O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+14, 's^-1'),
        n = 0,
        Ea = (89.796, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:15",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012570
""",
)

entry(
    index = 250,
    label = "C3H7O <=> C3H6O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+14, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (89.796, 'kJ/mol', '+|-', 1.796),
        T0 = (1, 'K'),
        Tmin = (393, 'K'),
        Tmax = (433, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L."],
        title = u'The Gas-Phase Decomposition of Alkoxy Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """977""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979BAT977:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00012570
Uncertainty: 3.1600001
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 251,
    label = "C3H7O <=> C3H6O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.7e+12, 's^-1'),
        n = 0,
        Ea = (79.902, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (753, 'K'),
        Tmax = (813, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (74700, 'Pa'),
    ),
    reference = Article(
        authors = ["Liu, M.T.H.", "Laidler, K.J."],
        title = u'Elementary processes in the acetaldehyde pyrolysis',
        journal = "Can. J. Chem.",
        volume = "46",
        pages = """479""",
        year = "1968",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1968LIU/LAI479:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00012570
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012570/rk00000001.xml
Bath gas: He
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 252,
    label = "C3H6O + H <=> C3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (30.418, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:33",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012570
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 253,
    label = "C3H7O <=> C2H4O + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.33e+19, 's^-1'),
        n = -1.7,
        Ea = (71.714, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:49",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012571
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 254,
    label = "C3H7O <=> C2H4O + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+15, 's^-1'),
        n = 0,
        Ea = (73.25, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:16",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012571
""",
)

entry(
    index = 255,
    label = "C3H7O <=> C2H4O + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+14, 's^-1'),
        n = 0,
        Ea = (72.003, 'kJ/mol', '+|-', 2.162),
        T0 = (1, 'K'),
        Tmin = (393, 'K'),
        Tmax = (433, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L."],
        title = u'The Gas-Phase Decomposition of Alkoxy Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """977""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979BAT977:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00012571
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 256,
    label = "C3H7O <=> C2H4O + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+14, 's^-1', '*|/', 2.51),
        n = 0,
        Ea = (71.504, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (393, 'K'),
        Tmax = (473, 'K'),
        Pmin = (91200, 'Pa'),
        Pmax = (91200, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L.", "McCulloch, R.D.", "Milne, R.T."],
        title = u'Thermochemical and Kinetic Studies of Alkyl Nitrites (RONO)-D(RO-NO), The Reactions between RO. and NO, and the Decomposition RO.',
        journal = "Proc. Symp. Chem. Kinet. Data Upper Lower Atmos. 1974",
        pages = """441""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975BAT/MCC441:13",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00012571
Uncertainty: 2.51
Bath gas: CF4
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 257,
    label = "C3H7O <=> C2H4O + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+12, 's^-1'),
        n = 0,
        Ea = (67.347, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (395, 'K'),
        Tmax = (428, 'K'),
    ),
    reference = Article(
        authors = ["Yee Quee, M.J.", "Thynne, J.C.J."],
        title = u'The pressure dependence of the decomposition of the isopropoxyl radical',
        journal = "J. Phys. Chem.",
        volume = "72",
        pages = """2824""",
        year = "1968",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1968YEE/THY2824:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00012571
Bath gas: (iso-C3H7O)2
Excitation technique: Direct photolysis
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 258,
    label = "C3H7O <=> C2H4O + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+11, 's^-1'),
        n = 0,
        Ea = (72.336, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (433, 'K'),
        Tmax = (473, 'K'),
        Pmin = (2666, 'Pa'),
        Pmax = (30700, 'Pa'),
    ),
    reference = Article(
        authors = ["Cox, D.L.", "Livermore, R.A.", "Phillips, L."],
        title = u'Reactions of the isopropoxyl radical. Part II. Pressure dependence and kinetics of pyrolysis at 160-200\xb0 in the gas phase',
        journal = "J. Chem. Soc. London B",
        pages = """245-249""",
        year = "1966",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1966COX/LIV245-249:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00012571
Bath gas: i-C3H7ONO
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 259,
    label = "C3H7O <=> C2H4O + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.5e+10, 's^-1'),
        n = 0,
        Ea = (66.931, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (448, 'K'),
        Tmax = (473, 'K'),
        Pmin = (4666, 'Pa'),
        Pmax = (4666, 'Pa'),
    ),
    reference = Article(
        authors = ["Ferguson, J.M.", "Phillips, L."],
        title = u'Reactions of the isopropoxyl radical. Part I. Pyrolysis of isopropyl nitrite in a static system at 175-200\xb0',
        journal = "J. Chem. Soc.",
        pages = """4416""",
        year = "1965",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1965FER/PHI4416:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00012571
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012571/rk00000001.xml
Bath gas: i-C3H7ONO
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 260,
    label = "C3H7O <=> C2H4O + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+13, 's^-1'),
        n = 0,
        Ea = (70.257, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Choo, K.Y.", "Benson, S.W."],
        title = u'Arrhenius Parameters for the Alkoxy Radical Decomposition Reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """833""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981CHO/BEN833:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Other theoretical""",
    longDesc = 
u"""
PrIMe Reaction: r00012571
""",
)

entry(
    index = 261,
    label = "C3H7O <=> C2H4O + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+14, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (74.498, 'kJ/mol', '+|-', 4.465),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."],
        title = u'Photochemical smog. Rate parameter estimates and computer simulations',
        journal = "J. Phys. Chem.",
        volume = "81",
        pages = """2483""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977BAL/BAR2483:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00012571
Uncertainty: 3.1600001
Bath gas: N2
""",
)

entry(
    index = 262,
    label = "C2H4O + CH3 <=> C3H7O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (100000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (38.727, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:39",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012571
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 263,
    label = "C4H9-4 <=> C3H6 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.59e+11, 's^-1'),
        n = 0.77,
        Ea = (128.491, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:24",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012768
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 264,
    label = "C4H9-4 <=> C3H6 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+13, 's^-1', '*|/', 5),
        n = 0,
        Ea = (125.549, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 4. Isobutane',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "19",
        pages = """1-68""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:122",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012768
Uncertainty: 5.0
""",
)

entry(
    index = 265,
    label = "C4H9-4 <=> C3H6 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7e+12, 's^-1', '*|/', 5),
        n = 0,
        Ea = (109.751, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:175",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012768
Uncertainty: 5.0
""",
)

entry(
    index = 266,
    label = "C4H9-4 <=> C3H6 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+12, 's^-1'),
        n = 0,
        Ea = (137.189, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (763, 'K'),
        Tmax = (813, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (13300, 'Pa'),
    ),
    reference = Article(
        authors = ["Douhou, S.", "Perrin, D.", "Martin, R."],
        title = u"Etude cinetique et modelisation de la reaction thermique de l'isobutene vers 800 K. II. Isobutene en presence d'hydrogene",
        journal = "J. Chim. Phys.",
        volume = "91",
        pages = """1628-1647""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994DOU/PER1628-1647:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00012768
Bath gas: iso-C4H8
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 267,
    label = "C4H9-4 <=> C3H6 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.4e+12, 's^-1'),
        n = 0,
        Ea = (129.706, 'kJ/mol', '+|-', 7.782),
        T0 = (1, 'K'),
        Tmin = (543, 'K'),
        Tmax = (598, 'K'),
        Pmin = (437, 'Pa'),
        Pmax = (2186, 'Pa'),
    ),
    reference = Article(
        authors = ["Slater, D.H.", "Collier, S.S.", "Calvert, J.G."],
        title = u"The photolysis of 1,1'-azoisobutane vapor at 3660 A. The reactions of the isobutyl free radical",
        journal = "J. Am. Chem. Soc.",
        volume = "90",
        pages = """268-273""",
        year = "1968",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1968SLA/COL268-273:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00012768
Bath gas: (CH3)2CHCH2N=NCH2CH(CH3)2
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 268,
    label = "C4H9-4 <=> C3H6 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.61e+12, 's^-1'),
        n = 0,
        Ea = (109.751, 'kJ/mol', '+|-', 1.098),
        T0 = (1, 'K'),
        Tmin = (552, 'K'),
        Tmax = (690, 'K'),
        Pmin = (2480, 'Pa'),
        Pmax = (4933, 'Pa'),
    ),
    reference = Article(
        authors = ["Metcalfe, E.L.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part VIII. Isobutyl radicals from the photolysis of isovaleraldehyde',
        journal = "J. Chem. Soc.",
        pages = """5072-5077""",
        year = "1960",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1960MET/TRO5072-5077:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00012768
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012768/rk00000001.xml
Bath gas: iso-C4H9CHO
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 269,
    label = "C4H9-4 <=> C3H6 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.14e+12, 's^-1'),
        n = 0.65,
        Ea = (129.115, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (1500, 'K'),
        Pmin = (101, 'Pa'),
        Pmax = (1.01e+06, 'Pa'),
    ),
    reference = Article(
        authors = ["Knyazev, V.D.", "Slagle, I.R."],
        title = u'Unimolecular decomposition of n-C4H9 and iso-C4H9 radicals',
        journal = "J. Phys. Chem.",
        volume = "100",
        pages = """5318-5328""",
        year = "1996",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996KNY/SLA5318-5328:7",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00012768

An analysis and exptrapolation of experimental literature data of Slater et al. and Trotman-Dickenson covering ca. 550- 690 K.
""",
)

entry(
    index = 270,
    label = "C3H6 + CH3 <=> C4H9-4",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (0.00189, 'm^3/(mol*s)'),
        n = 2.67,
        Ea = (28.66, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:11",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012768
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 271,
    label = "C3H6 + CH3 <=> C4H9-4",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (96400, 'm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (33.507, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:41",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012768
Uncertainty: 3.0
""",
)

entry(
    index = 272,
    label = "C3H6 + CH3 <=> C4H9-4",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (200000, 'm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (36.501, 'kJ/mol', '+|-', 5.113),
        T0 = (1, 'K'),
        Tmin = (353, 'K'),
        Tmax = (753, 'K'),
        Pmin = (66700, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Baldwin, R.R.", "Keen, A.", "Walker, R.W."],
        title = u'Rate constants for the addition of methyl radicals to propene',
        journal = "J. Chem. Soc. Faraday Trans. 2",
        volume = "83",
        pages = """759""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987BAL/KEE759:6",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00012768
Uncertainty: 2.0
Bath gas: H2
""",
)

entry(
    index = 273,
    label = "C3H6 + CH3 <=> C4H9-4",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (0.01, 'm^3/(mol*s)'),
        n = 2.57,
        Ea = (32.26, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (1500, 'K'),
        Pmin = (101, 'Pa'),
        Pmax = (1.01e+06, 'Pa'),
    ),
    reference = Article(
        authors = ["Knyazev, V.D.", "Slagle, I.R."],
        title = u'Unimolecular decomposition of n-C4H9 and iso-C4H9 radicals',
        journal = "J. Phys. Chem.",
        volume = "100",
        pages = """5318-5328""",
        year = "1996",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996KNY/SLA5318-5328:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00012768
Bath gas: He
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 274,
    label = "C4H9-4 <=> C4H8 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.71e+13, 's^-1'),
        n = 0.12,
        Ea = (140.917, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:19",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012769
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 275,
    label = "C4H9-4 <=> C4H8 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 's^-1'),
        n = 0,
        Ea = (128.043, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (302, 'K'),
        Tmax = (690, 'K'),
        Pmin = (2480, 'Pa'),
        Pmax = (4933, 'Pa'),
    ),
    reference = Article(
        authors = ["Metcalfe, E.L.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part VIII. Isobutyl radicals from the photolysis of isovaleraldehyde',
        journal = "J. Chem. Soc.",
        pages = """5072-5077""",
        year = "1960",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1960MET/TRO5072-5077:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00012769
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012769/rk00000001.xml
Bath gas: iso-C4H9CHO
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 276,
    label = "C4H9-4 <=> C4H8 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 's^-1'),
        n = 0,
        Ea = (152.155, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1260, 'K'),
        Tmax = (1310, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Weissman, M.", "Benson, S.W."],
        title = u'Pyrolysis of methyl chloride, a pathway in the chlorine-catalyzed polymerization of methane',
        journal = "Int. J. Chem. Kinet.",
        volume = "16",
        pages = """307-333""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WEI/BEN307-333:16",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00012769
""",
)

entry(
    index = 277,
    label = "C4H8 + H <=> C4H9-4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (625000, 'm^3/(mol*s)'),
        n = 0.51,
        Ea = (10.962, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:5",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012769
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 278,
    label = "C3H7O-2 <=> C3H6 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+12, 's^-1'),
        n = 0,
        Ea = (112.245, 'kJ/mol', '+|-', 6.751),
        T0 = (1, 'K'),
        Tmin = (504, 'K'),
        Tmax = (564, 'K'),
        Pmin = (100000, 'Pa'),
        Pmax = (100000, 'Pa'),
    ),
    reference = Article(
        authors = ["Dunlop, J.R.", "Tully, F.P."],
        title = u'Catalytic dehydration of alcohols by OH. 2-propanol: an intermediate case',
        journal = "J. Phys. Chem.",
        volume = "97",
        pages = """6457-6464""",
        year = "1993",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1993DUN/TUL6457-6464:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00013083
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013083/rk00000001.xml
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Laser induced fluorescence
Note: Invalid preexponential uncertainty (5.2e+12) found and ignored
""",
)

entry(
    index = 279,
    label = "C4H7-3 <=> C3H4 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 's^-1'),
        n = 0,
        Ea = (209.525, 'kJ/mol', '+|-', 4.19),
        T0 = (1, 'K'),
        Tmin = (996, 'K'),
        Tmax = (1180, 'K'),
        Pmin = (152000, 'Pa'),
        Pmax = (507000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Pyrolysis of 2,4-Dimethylhexene-1 and the Stability of Isobutenyl Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "5",
        pages = """929""",
        year = "1973",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1973TSA929:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00015595
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015595/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 280,
    label = "C4H7-3 <=> C3H4 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.1e+10, 's^-1'),
        n = 1.38,
        Ea = (235.81, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Zheng, X.L.", "Sun, H.Y.", "Law, C.K."],
        title = u'Thermochemical and kinetic analyses on oxidation of isobutenyl radical and 2-hydroperoxymethyl-2-propenyl radical',
        journal = "J. Phys. Chem. A",
        volume = "109",
        pages = """9044-9053""",
        year = "2005",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2005ZHE/SUN9044-9053:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00015595
Pressure dependence: Rate constant is high pressure limit

Reaction potential energy surface was studied using quantum chemistry and rate constants were calculated using transition state theory.
""",
)

entry(
    index = 281,
    label = "C3H4 + CH3 <=> C4H7-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (158000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (20.786, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (996, 'K'),
        Tmax = (1180, 'K'),
        Pmin = (152000, 'Pa'),
        Pmax = (507000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Pyrolysis of 2,4-Dimethylhexene-1 and the Stability of Isobutenyl Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "5",
        pages = """929""",
        year = "1973",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1973TSA929:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00015595
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015595/rk00000001.xml
Bath gas: Ar
""",
)

entry(
    index = 282,
    label = "C3H7O-3 <=> CH2O + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.72e+21, 's^-1'),
        n = -2.45,
        Ea = (71.002, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:47",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00015701
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 283,
    label = "C3H7O-3 <=> CH2O + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 's^-1'),
        n = 0,
        Ea = (56.3, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (190, 'K'),
        Tmax = (330, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Johnson, D.", "Cassanelli, P.", "Cox, R.A."],
        title = u'Correlation-type structure activity relationships for the kinetics of the decomposition of simple and beta-substituted alkoxyl radicals',
        journal = "Atmos. Environ.",
        volume = "38",
        pages = """1755-1765""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004JOH/CAS1755-1765:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00015701

The authors developed a structure activity relationship (SARs) for the estimation of rate data for the decomposition of RO to alkyl radical and carbonyl fragments. The SARs are based upon strong, non-linear, correlations between the logarithm of measured room temperature rate coefficients and the average measured ionisation potential (IP) of the reaction products,. The considered compounds include simple unsubstituted, beta-chlorinated and beta-hydroxylated alkoxylradicals. Chemical activation processes in the decomposition chemistry are briefly discussed.

The temperature range over which the estimates are intended to be useful is not given, but the results are derived for atmospheric chemistry occurring in the troposphere through lower stratosphere. This is assumed by us to approimately cover 190 K to 330 K.

For the 10 simple and 11 heteroatom-substituted RO: species used to construct the correlations, 18(85%) of the room temperature rate coefficients predicted using the present method are within a factor of two of their measured (or theoretically calculated) values, and 100% are within a factor of three. The average ratio of measured to calculated rate coefficients is 0.9.
""",
)

entry(
    index = 284,
    label = "C3H7O-3 <=> CH2O + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+13, 's^-1'),
        n = 0,
        Ea = (65.269, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Choo, K.Y.", "Benson, S.W."],
        title = u'Arrhenius Parameters for the Alkoxy Radical Decomposition Reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """833""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981CHO/BEN833:6",
    ),
    referenceType = "theory",
    shortDesc = u"""Other theoretical""",
    longDesc = 
u"""
PrIMe Reaction: r00015701
""",
)

entry(
    index = 285,
    label = "C3H7O-3 <=> CH2O + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.31e+13, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (81.565, 'kJ/mol', '+|-', 4.082),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."],
        title = u'Photochemical smog. Rate parameter estimates and computer simulations',
        journal = "J. Phys. Chem.",
        volume = "81",
        pages = """2483""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977BAL/BAR2483:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00015701
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015701/rk00000001.xml
Uncertainty: 3.1600001
Bath gas: N2
""",
)

entry(
    index = 286,
    label = "CH2O + C2H5 <=> C3H7O-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (14.627, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:35",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00015701
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 287,
    label = "C3H7O-3 <=> C3H6O-2 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.89e+10, 's^-1'),
        n = 0.75,
        Ea = (88.115, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:46",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00015702
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 288,
    label = "C3H6O-2 + H <=> C3H7O-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (26.192, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:31",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00015702
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 289,
    label = "C4H5 <=> C2H2 + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 's^-1'),
        n = 0,
        Ea = (183.75, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Dean, A.M."],
        title = u'Predictions of pressure and temperature effects upon radical addition and recombination reactions',
        journal = "J. Phys. Chem.",
        volume = "89",
        pages = """4600-4608""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:43",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00016900
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016900/rk00000001.xml
""",
)

entry(
    index = 290,
    label = "C2H2 + C2H3 <=> C4H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (31500, 'm^3/(mol*s)'),
        n = 0,
        Ea = (12.971, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (500, 'K'),
        Pmin = (13300, 'Pa'),
        Pmax = (80000, 'Pa'),
    ),
    reference = Article(
        authors = ["Callear, A.B.", "Smith, G.B."],
        title = u'Addition of atomic hydrogen to acetylene. Chain reactions of the vinyl radical',
        journal = "Chem. Phys. Lett.",
        volume = "105",
        pages = """119""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984CAL/SMI119:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00016900
Bath gas: H2
Excitation technique: Sensitized photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 291,
    label = "C2H2 + C2H3 <=> C4H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (316000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (25.11, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (1200, 'K'),
    ),
    reference = Article(
        authors = ["Benson, S.W."],
        title = u'The mechanism of the reversible reaction: 2C2H2 = vinyl acetylene and the pyrolysis of butadiene',
        journal = "Int. J. Chem. Kinet.",
        volume = "21",
        pages = """233-243""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989BEN233-243:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00016900
""",
)

entry(
    index = 292,
    label = "C2H2 + C2H3 <=> C4H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.251, 'm^3/(mol*s)'),
        n = 1.9,
        Ea = (8.813, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = Article(
        authors = ["Weissman, M.A.", "Benson, S.W."],
        title = u'Rate parameters for the reactions of C2H3 and C4H5 with H2 and C2H2',
        journal = "J. Phys. Chem.",
        volume = "92",
        pages = """4080""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988WEI/BEN4080:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00016900
""",
)

entry(
    index = 293,
    label = "C2H2 + C2H3 <=> C4H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (619000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (20.287, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (1300, 'K'),
        Pmin = (12200, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Duran, R.P.", "Amorebieta, V.T.", "Colussi, A.J."],
        title = u'Is the homogeneous thermal dimerization of acetylene a free-radical chain reaction? Kinetic and thermochemical analysis',
        journal = "J. Phys. Chem.",
        volume = "92",
        pages = """636""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988DUR/AMO636:5",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00016900
""",
)

entry(
    index = 294,
    label = "C2H2 + C2H3 <=> C4H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (631000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (19.622, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1260, 'K'),
        Tmax = (1310, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Weissman, M.", "Benson, S.W."],
        title = u'Pyrolysis of methyl chloride, a pathway in the chlorine-catalyzed polymerization of methane',
        journal = "Int. J. Chem. Kinet.",
        volume = "16",
        pages = """307-333""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WEI/BEN307-333:5",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00016900
""",
)

entry(
    index = 295,
    label = "C2H4 + CH3O-2 <=> C3H7O-4",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (48200, 'm^3/(mol*s)'),
        n = 0,
        Ea = (29.101, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part 2. Methanol',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "16",
        pages = """471""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987TSA471:25",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002226
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002226/rk00000001.xml
""",
)

entry(
    index = 296,
    label = "C3H4 + CH3 <=> C4H7-4",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (200000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (33.923, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (373, 'K'),
        Tmax = (483, 'K'),
    ),
    reference = Article(
        authors = ["Getty, R.R.", "Kerr, J.A.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part XII. The additions of methyl, ethyl, and isopropyl radicals to allene',
        journal = "J. Chem. Soc. A",
        pages = """979-982""",
        year = "1967",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1967GET/KER979-982:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00006972
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00006972/rk00000001.xml
Bath gas: H2
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 297,
    label = "C4H9-2 <=> C3H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.5e+11, 's^-1'),
        n = 0,
        Ea = (100.605, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (625, 'K'),
        Pmin = (2400, 'Pa'),
        Pmax = (3466, 'Pa'),
    ),
    reference = Article(
        authors = ["Gruver, J.T.", "Calvert, J.C."],
        title = u'The vapor phase photolysis of 2-methylbutanal at wave length 3130 A',
        journal = "J. Am. Chem. Soc.",
        volume = "78",
        pages = """5208""",
        year = "1956",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1956GRU/CAL5208:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011106
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011106/rk00000001.xml
Rate constant is an upper limit.
Bath gas: sec-C4H9CHO
""",
)

entry(
    index = 298,
    label = "C4H9-2 <=> C4H8-3 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.17e+12, 's^-1'),
        n = 0,
        Ea = (145.503, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (800, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'The stability of alkyl radicals',
        journal = "J. Am. Chem. Soc.",
        volume = "107",
        pages = """2872-2880""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985TSA2872-2880:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from detailed balance/reverse rate""",
    longDesc = 
u"""
PrIMe Reaction: r00011107
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011107/rk00000001.xml
""",
)

entry(
    index = 299,
    label = "C4H9-2 <=> C4H8-3 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.57e+12, 's^-1'),
        n = 0,
        Ea = (142.177, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (800, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'The stability of alkyl radicals',
        journal = "J. Am. Chem. Soc.",
        volume = "107",
        pages = """2872-2880""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985TSA2872-2880:7",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from detailed balance/reverse rate""",
    longDesc = 
u"""
PrIMe Reaction: r00011108
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011108/rk00000001.xml
""",
)

entry(
    index = 300,
    label = "C4H8-3 + H <=> C4H9-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.61e+07, 'm^3/(mol*s)', '+|-', 2.4e+06),
        n = 0,
        Ea = (8.023, 'kJ/mol', '+|-', 0.321),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (500, 'K'),
        Pmin = (80000, 'Pa'),
        Pmax = (80000, 'Pa'),
    ),
    reference = Article(
        authors = ["Kyogoku, T.", "Watanabe, T.", "Tsunashima, S.", "Sato, S."],
        title = u'Arrhenius parameters for the reactions of hydrogen and deuterium atoms with four butenes',
        journal = "Bull. Chem. Soc. Jpn.",
        volume = "56",
        pages = """19-21""",
        year = "1983",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1983KYO/WAT19-21:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011107
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011107/rk00000007.xml
Bath gas: H2
Excitation technique: Chemical activation
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 301,
    label = "C4H8-3 + H <=> C4H9-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.08e+07, 'm^3/(mol*s)', '+|-', 2.1e+06),
        n = 0,
        Ea = (8.647, 'kJ/mol', '+|-', 0.52),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (445, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (6666, 'Pa'),
    ),
    reference = Article(
        authors = ["Harris, G.W.", "Pitts, J.N., Jr."],
        title = u'Absolute Rate Constants and Temperature Dependences for the Gas Phase Reactions of H Atoms with Propene and the Butenes in the Temperature Range 298 to 445 K',
        journal = "J. Chem. Phys.",
        volume = "77",
        pages = """3994""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982HAR/PIT3994:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011108
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011108/rk00000013.xml
Bath gas: Ar
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Resonance fluorescence
""",
)

entry(
    index = 302,
    label = "C4H8-3 + H <=> C4H9-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.39e+07, 'm^3/(mol*s)', '+|-', 1.7e+06),
        n = 0,
        Ea = (8.813, 'kJ/mol', '+|-', 0.175),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (500, 'K'),
        Pmin = (80000, 'Pa'),
        Pmax = (80000, 'Pa'),
    ),
    reference = Article(
        authors = ["Kyogoku, T.", "Watanabe, T.", "Tsunashima, S.", "Sato, S."],
        title = u'Arrhenius parameters for the reactions of hydrogen and deuterium atoms with four butenes',
        journal = "Bull. Chem. Soc. Jpn.",
        volume = "56",
        pages = """19-21""",
        year = "1983",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1983KYO/WAT19-21:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011108
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011108/rk00000014.xml
Bath gas: H2
Excitation technique: Chemical activation
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 303,
    label = "C4H8-2 + H <=> C4H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.49e+07, 'm^3/(mol*s)', '+|-', 2.5e+06),
        n = 0,
        Ea = (6.244, 'kJ/mol', '+|-', 0.375),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (500, 'K'),
        Pmin = (80000, 'Pa'),
        Pmax = (80000, 'Pa'),
    ),
    reference = Article(
        authors = ["Kyogoku, T.", "Watanabe, T.", "Tsunashima, S.", "Sato, S."],
        title = u'Arrhenius parameters for the reactions of hydrogen and deuterium atoms with four butenes',
        journal = "Bull. Chem. Soc. Jpn.",
        volume = "56",
        pages = """19-21""",
        year = "1983",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1983KYO/WAT19-21:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011210
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011210/rk00000004.xml
Pressure dependence: None reported
Experimental procedure: Static or low flow - Data taken vs time
Excitation technique: Electron beam
Time resolution: In real time
Analytical technique: Vis-UV absorption

In agreement with the literature, the authors state that addition of H will preferentially occur at the terminal carbon to form 2-C4H9. Their experiment, however, provides no direct information on the branching ratio.
""",
)

entry(
    index = 304,
    label = "C4H3 <=> C4H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 's^-1'),
        n = 0,
        Ea = (167.121, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2400, 'K'),
    ),
    reference = Article(
        authors = ["Back, M.H."],
        title = u'Mechanism of the pyrolysis of acetylene',
        journal = "Can. J. Chem.",
        volume = "49",
        pages = """2199""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971BAC2199:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011527
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011527/rk00000001.xml
Note: Invalid activation energy uncertainty (8314472.0) found and ignored
""",
)

entry(
    index = 305,
    label = "C4H3 <=> C4H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 's^-1'),
        n = 0,
        Ea = (170.447, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1260, 'K'),
        Tmax = (1310, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Weissman, M.", "Benson, S.W."],
        title = u'Pyrolysis of methyl chloride, a pathway in the chlorine-catalyzed polymerization of methane',
        journal = "Int. J. Chem. Kinet.",
        volume = "16",
        pages = """307-333""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WEI/BEN307-333:15",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011527
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011527/rk00000003.xml
""",
)

entry(
    index = 306,
    label = "C4H3 <=> C4H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.15e+61, 's^-1'),
        n = -13.9,
        Ea = (256.917, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1380, 'K'),
        Tmax = (1700, 'K'),
        Pmin = (149000, 'Pa'),
        Pmax = (607000, 'Pa'),
    ),
    reference = Article(
        authors = ["Braun-Unkhoff, M.", "Frank, P.", "Just, Th."],
        title = u'A shock tube study on the thermal decomposition of toluene and of the phenyl radical at high temperatures',
        journal = "Symp. Int. Combust. Proc.",
        volume = "22",
        pages = """1053-1061""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989BRA/FRA1053-1061:9",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011527
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011527/rk00000005.xml
Bath gas: Toluene
""",
)

entry(
    index = 307,
    label = "C3H7O <=> C3H6O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.58e+13, 's^-1'), n=0, Ea=(76.6, 'kJ/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003RAU/BOY431-442:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00012570
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012570/rk00000004.xml

Rate expression does not contain tunneling contributions. Temperature range not specified but it does include 298.15 K.
""",
)

entry(
    index = 308,
    label = "C3H7O <=> C2H4O + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(A=(9.12e+13, 's^-1'), n=0, Ea=(60.1, 'kJ/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003RAU/BOY431-442:9",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00012571
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012571/rk00000015.xml

Rate expression does not contain tunneling contributions. Temperature range not specified but it does include 298.15 K.
""",
)

entry(
    index = 309,
    label = "C3H4 + CH3 <=> C4H7-4",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (57500, 'm^3/(mol*s)', '*|/', 1.58),
        n = 0,
        Ea = (28.602, 'kJ/mol', '+|-', 0.856),
        T0 = (1, 'K'),
        Tmin = (573, 'K'),
        Tmax = (595, 'K'),
        Pmin = (3800, 'Pa'),
        Pmax = (3800, 'Pa'),
    ),
    reference = Article(
        authors = ["Scherzer, K.", "Claus, P.", "Dabbagh, M."],
        title = u'Kinetische untersuchungen der reaktionen von methylradikalen mit allen',
        journal = "J. Prakt. Chem.",
        volume = "325",
        pages = """680""",
        year = "1983",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1983SCH/CLA680:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00006972
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00006972/rk00000003.xml
Uncertainty: 1.58
Bath gas: (E)-CH3N=NCH3
Excitation technique: Thermal
Analytical technique: Gas chromatography
Reference reaction: *CH3 + (E)-CH3N=NCH3 -> Other Products + CH4
""",
)

entry(
    index = 310,
    label = "C3H7O-3 <=> C3H6O-2 + H",
    degeneracy = 2,
    kinetics = Arrhenius(A=(1.7e+13, 's^-1'), n=0, Ea=(85.8, 'kJ/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003RAU/BOY431-442:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00015702
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015702/rk00000001.xml
""",
)

entry(
    index = 311,
    label = "C3H5O <=> CH2O + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.39e+14, 's^-1'), n=0, Ea=(94.8, 'kJ/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003RAU/BOY431-442:15",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00016184
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016184/rk00000001.xml

Rate expression does not contain tunneling contributions. Temperature range not specified but it does include 298.15 K.
""",
)

entry(
    index = 312,
    label = "C3H5O <=> C3H4O + H",
    degeneracy = 2,
    kinetics = Arrhenius(A=(1.1e+13, 's^-1'), n=0, Ea=(77.2, 'kJ/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003RAU/BOY431-442:6",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00016185
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016185/rk00000001.xml

Rate expression does not contain tunneling contributions. Temperature range not specified but it does include 298.15 K.
""",
)

entry(
    index = 313,
    label = "C4H3-2 <=> C4H2 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+14, 's^-1'),
        n = 0,
        Ea = (216.176, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1400, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = Article(
        authors = ["Ghibaudi, E.", "Colussi, A.J."],
        title = u'Kinetics and thermochemistry of the equilibrium 2 (acetylene) = vinylacetylene. Direct evidence against a chain mechanism',
        journal = "J. Phys. Chem.",
        volume = "92",
        pages = """5839""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988GHI/COL5839:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00016678
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016678/rk00000002.xml
""",
)

entry(
    index = 314,
    label = "C4H2 + H <=> C4H3-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.3e+24, 'm^3/(mol*s)'),
        n = -4.92,
        Ea = (45.189, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1150, 'K'),
        Tmax = (2130, 'K'),
        Pmin = (91200, 'Pa'),
        Pmax = (193000, 'Pa'),
    ),
    reference = Article(
        authors = ["Eiteneer, B.", "Frenklach, M."],
        title = u'Experimental and Modeling Study of Shock-Tube Oxidation of Acetylene',
        journal = "Int J. Chem. Kinet.",
        volume = "35",
        pages = """391-414""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003EIT/FRE391-414:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00016678
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016678/rk00000003.xml
Pressure dependence: None reported
Experimental procedure: Shock tube
Excitation technique: Thermal
Time resolution: In real time
Analytical technique: IR absorption

No direct measurements of rate constants. Rate constants reported are either from estimates or optimization fits. Enthalpies of formation were also allowed to be varied in fits. This paper is combined experimental and modeling. These measurements consist of shock tube oxidation of C2H2 at temperatures of 1150-2130 K, pressures of 0.9-1.9 atm in Argon, with lean to rich conditions (Phi = 0.06 to 1.7). CO produced was detected using CO laser absorption at 2077.1 cm-1
""",
)

entry(
    index = 315,
    label = "C4H7-5 <=> C3H4-2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+13, 's^-1'),
        n = 0,
        Ea = (131.369, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Dean, A.M."],
        title = u'Predictions of pressure and temperature effects upon radical addition and recombination reactions',
        journal = "J. Phys. Chem.",
        volume = "89",
        pages = """4600-4608""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:42",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00016804
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016804/rk00000001.xml
""",
)

entry(
    index = 316,
    label = "C3H4-2 + CH3 <=> C4H7-5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (501000, 'm^3/(mol*s)', '*|/', 1.26),
        n = 0,
        Ea = (36.833, 'kJ/mol', '+|-', 0.737),
        T0 = (1, 'K'),
        Tmin = (379, 'K'),
        Tmax = (465, 'K'),
    ),
    reference = Article(
        authors = ["Getty, R.R.", "Kerr, J.A.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part XIII. The additions of methyl, isopropyl, and t-butyl radicals to propyne and the isomerisation of alkenyl radicals',
        journal = "J. Chem. Soc. A",
        pages = """1360""",
        year = "1967",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1967GET/KER1360:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00016804
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016804/rk00000002.xml
Uncertainty: 1.26
Bath gas: CH3CHO
Excitation technique: Direct photolysis
Analytical technique: Other (direct)
""",
)

entry(
    index = 317,
    label = "C4H5 <=> C4H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 's^-1'),
        n = 0,
        Ea = (172.941, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1260, 'K'),
        Tmax = (1310, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Weissman, M.", "Benson, S.W."],
        title = u'Pyrolysis of methyl chloride, a pathway in the chlorine-catalyzed polymerization of methane',
        journal = "Int. J. Chem. Kinet.",
        volume = "16",
        pages = """307-333""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WEI/BEN307-333:19",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00016901
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016901/rk00000001.xml
""",
)

entry(
    index = 318,
    label = "C4H5 <=> C4H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+14, 's^-1'),
        n = 0,
        Ea = (172.941, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (900, 'K'),
        Tmax = (1100, 'K'),
    ),
    reference = Article(
        authors = ["Colket, M.B., III", "Seery, D.J.", "Palmer, H.B."],
        title = u'The pyrolysis of acetylene initiated by acetone',
        journal = "Combust. Flame",
        volume = "75",
        pages = """343-366""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989COL/SEE343-366:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00016901
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016901/rk00000002.xml
""",
)

entry(
    index = 319,
    label = "CH2O + C3H7 <=> C4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (14.464, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:36",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00001349
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 320,
    label = "CH2O + C3H7 <=> C4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (79400, 'm^3/(mol*s)'),
        n = 0,
        Ea = (28.02, 'kJ/mol', '+|-', 1.962),
        T0 = (1, 'K'),
        Tmin = (333, 'K'),
        Tmax = (363, 'K'),
        Pmin = (7733, 'Pa'),
        Pmax = (7733, 'Pa'),
    ),
    reference = Article(
        authors = ["Knoll, H.", "Nacsa, A.", "Foergeteg, S.", "Berces, T."],
        title = u'Free Radical Additions to the C=O Bond of Formaldehyde',
        journal = "React. Kinet. Catal. Lett.",
        volume = "15",
        pages = """481""",
        year = "1980",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1980KNO/NAC481:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00001349
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00001349/rk00000001.xml
Bath gas: (n-C3H7)-N=N-(n-C3H7)
Excitation technique: Direct photolysis
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 321,
    label = "C4H9O <=> CH2O + C3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.57e+21, 's^-1'),
        n = -2.44,
        Ea = (70.459, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:50",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00001349
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 322,
    label = "C4H9O <=> CH2O + C3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.5e+13, 's^-1'),
        n = 0,
        Ea = (67.189, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (1200, 'K'),
    ),
    reference = Article(
        authors = ["Somnitz, H."],
        title = u'The contribution of tunnelling to the 1,5 H-shift isomerisation reaction of alkoxyl radicals',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "10",
        pages = """965-973""",
        year = "2008",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2008SOM965-973:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00001349
Pressure dependence: Rate constant is high pressure limit
""",
)

entry(
    index = 326,
    label = "C4H9O <=> CH2O + C3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+13, 's^-1'),
        n = 0,
        Ea = (67.2, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = Article(
        authors = ["Somnitz, H.", "Zellner, R."],
        title = u'Kinetics and dynamics of multi-channel unimolecular reactions of alkoxyl radicals over an extended range of temperature and pressure. A combined quantum chemical/RRKM dynamical study',
        journal = "Z. Phys. Chem.",
        volume = "220",
        pages = """1029-1048""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006SOM/ZEL1029-1048:5",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00001349
Pressure dependence: Rate constant is high pressure limit

Reaction potential energy surface was studied using quantum chemistry and rate constants were calculated using transition RRKM and master equation analysis. Rate constants were calculated for wide ranges of temperatures and pressures.
""",
)

entry(
    index = 327,
    label = "C4H9O <=> CH2O + C3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 's^-1'),
        n = 0,
        Ea = (56.2, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (190, 'K'),
        Tmax = (330, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Johnson, D.", "Cassanelli, P.", "Cox, R.A."],
        title = u'Correlation-type structure activity relationships for the kinetics of the decomposition of simple and beta-substituted alkoxyl radicals',
        journal = "Atmos. Environ.",
        volume = "38",
        pages = """1755-1765""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004JOH/CAS1755-1765:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00001349

The authors developed a structure activity relationship (SARs) for the estimation of rate data for the decomposition of RO to alkyl radical and carbonyl fragments. The SARs are based upon strong, non-linear, correlations between the logarithm of measured room temperature rate coefficients and the average measured ionisation potential (IP) of the reaction products,. The considered compounds include simple unsubstituted, beta-chlorinated and beta-hydroxylated alkoxylradicals. Chemical activation processes in the decomposition chemistry are briefly discussed.

The temperature range over which the estimates are intended to be useful is not given, but the results are derived for atmospheric chemistry occurring in the troposphere through lower stratosphere. This is assumed by us to approimately cover 190 K to 330 K.

For the 10 simple and 11 heteroatom-substituted RO: species used to construct the correlations, 18(85%) of the room temperature rate coefficients predicted using the present method are within a factor of two of their measured (or theoretically calculated) values, and 100% are within a factor of three. The average ratio of measured to calculated rate coefficients is 0.9.
""",
)

entry(
    index = 328,
    label = "C4H9O <=> CH2O + C3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+13, 's^-1'),
        n = 0,
        Ea = (79.902, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (590, 'K'),
        Tmax = (750, 'K'),
    ),
    reference = Article(
        authors = ["Baldwin, A.C.", "Golden, D.M."],
        title = u'Alkoxy Radical Reactions: The Isomerization of n-Butoxy Radicals Generated from the Pyrolysis of n-Butyl Nitrite',
        journal = "Chem. Phys. Lett.",
        volume = "60",
        pages = """108""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978BAL/GOL108:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00001349
Bath gas: n-C4H9ONO
""",
)

entry(
    index = 329,
    label = "C4H9O <=> CH2O + C3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+13, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (79.902, 'kJ/mol', '+|-', 3.999),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."],
        title = u'Photochemical smog. Rate parameter estimates and computer simulations',
        journal = "J. Phys. Chem.",
        volume = "81",
        pages = """2483""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977BAL/BAR2483:5",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00001349
Uncertainty: 3.1600001
Bath gas: N2
""",
)

entry(
    index = 330,
    label = "C2H4 + C3H7-2 <=> C5H11",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (69200, 'm^3/(mol*s)'),
        n = 0,
        Ea = (28.851, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (340, 'K'),
        Tmax = (457, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (16000, 'Pa'),
    ),
    reference = Book(
        authors = ["Kerr, J.A.", "Parsonage, M.J."],
        title = u'Evaluated Kinetic Data on Gas Phase Addition Reactions. Reactions of Atoms and Radicals with Alkenes, Alkynes and Aromatic Compounds',
        publisher = "London",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972KER/PARB:5",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002199
""",
)

entry(
    index = 331,
    label = "C2H4 + C3H7-2 <=> C5H11",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.66e+08, 'm^3/(mol*s)'),
        n = 0,
        Ea = (29.018, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (340, 'K'),
        Tmax = (413, 'K'),
    ),
    reference = Article(
        authors = ["Watkins, K.W.", "O'Deen, L.A."],
        title = u'Kinetics of the addition of ethyl, isopropyl, n-butyl, and isopentyl radicals to ethylene',
        journal = "J. Phys. Chem.",
        volume = "73",
        pages = """4094-4102""",
        year = "1969",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1969WAT/ODE4094-4102:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002199
Bath gas: (iso-C3H7)-N=N-(iso-C3H7)
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 332,
    label = "C2H4 + C3H7-2 <=> C5H11",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (250000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (28.851, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (268, 'K'),
        Tmax = (468, 'K'),
        Pmin = (1200, 'Pa'),
        Pmax = (4400, 'Pa'),
    ),
    reference = Article(
        authors = ["Kerr, J.A.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part 2. s-Propyl radicals from the photolysis of isobutyraldehyde',
        journal = "Trans. Faraday Soc.",
        volume = "55",
        pages = """921""",
        year = "1959",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1959KER/TRO921:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002199
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002199/rk00000001.xml
Bath gas: (CH3)2CHCHO
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 333,
    label = "C2H4 + C3H7 <=> C5H11-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (19500, 'm^3/(mol*s)'),
        n = 0,
        Ea = (25.525, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (375, 'K'),
        Tmax = (503, 'K'),
        Pmin = (9333, 'Pa'),
        Pmax = (13300, 'Pa'),
    ),
    reference = Book(
        authors = ["Kerr, J.A.", "Parsonage, M.J."],
        title = u'Evaluated Kinetic Data on Gas Phase Addition Reactions. Reactions of Atoms and Radicals with Alkenes, Alkynes and Aromatic Compounds',
        publisher = "London",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972KER/PARB:6",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002210
""",
)

entry(
    index = 334,
    label = "C2H4 + C3H7 <=> C5H11-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (141000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (30.93, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (330, 'K'),
        Tmax = (373, 'K'),
        Pmin = (79.99, 'Pa'),
        Pmax = (36300, 'Pa'),
    ),
    reference = Article(
        authors = ["Watkins, K.W.", "Lawson, D.R."],
        title = u'Isomerization of Chemically Activated n-Pentyl Radicals',
        journal = "J. Phys. Chem.",
        volume = "75",
        pages = """1632""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971WAT/LAW1632:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002210
Bath gas: C2H4
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 335,
    label = "C2H4 + C3H7 <=> C5H11-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (79400, 'm^3/(mol*s)'),
        n = 0,
        Ea = (27.188, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (344, 'K'),
        Tmax = (434, 'K'),
        Pmin = (1200, 'Pa'),
        Pmax = (4400, 'Pa'),
    ),
    reference = Article(
        authors = ["Kerr, J.A.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part 1.-n-Propyl radicals from the photolysis of n-butyraldehyde',
        journal = "Trans. Faraday Soc.",
        volume = "55",
        pages = """572""",
        year = "1959",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1959KER/TRO572:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002210
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002210/rk00000001.xml
Bath gas: n-C3H7CHO
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 336,
    label = "C5H11-2 <=> C2H4 + C3H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.9e+14, 's^-1'),
        n = 0,
        Ea = (137.2, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (250, 'K'),
        Tmax = (2600, 'K'),
    ),
    reference = Article(
        authors = ["Jitariu, L.C.", "Wang, H.", "Hillier, I.H.", "Pilling, M.J."],
        title = u'Unimolecular Decomposition of the n-C3H7 Radical.  Direct Dynamics Calculation of the Thermal Rate Constant',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "3",
        pages = """2459-2466""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001JIT/WAN2459-2466:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00002210

Reaction potential energy surface was studied using quantum chemistry and rate constants were calculated using variational transition state theory with tunneling correction. The temperature interval for which the Arrhenius parameters are given is not specified but probably is the same as for the other eeaction studied in the same work, that of n-C3H7 decomposition.
""",
)

entry(
    index = 337,
    label = "C5H11-2 <=> C2H4 + C3H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.7e+13, 's^-1'),
        n = 0,
        Ea = (113.4, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (250, 'K'),
        Tmax = (2600, 'K'),
    ),
    reference = Article(
        authors = ["Jitariu, L.C.", "Wang, H.", "Hillier, I.H.", "Pilling, M.J."],
        title = u'Unimolecular Decomposition of the n-C3H7 Radical.  Direct Dynamics Calculation of the Thermal Rate Constant',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "3",
        pages = """2459-2466""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001JIT/WAN2459-2466:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00002210

Reaction potential energy surface was studied using quantum chemistry and rate constants were calculated using variational transition state theory with tunneling correction. The temperature interval for which the Arrhenius parameters are given is not specified but probably is the same as for the other eeaction studied in the same work, that of n-C3H7 decomposition.
""",
)

entry(
    index = 338,
    label = "C2H2 + C3H5 <=> C5H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (31900, 'm^3/(mol*s)', '*|/', 10),
        n = 0,
        Ea = (29.101, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:12",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002408
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002408/rk00000001.xml
Uncertainty: 10.0
""",
)

entry(
    index = 339,
    label = "C2H2 + C3H7-2 <=> C5H9",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (50100, 'm^3/(mol*s)'),
        n = 0,
        Ea = (28.851, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (363, 'K'),
        Tmax = (577, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (13300, 'Pa'),
    ),
    reference = Book(
        authors = ["Kerr, J.A.", "Parsonage, M.J."],
        title = u'Evaluated Kinetic Data on Gas Phase Addition Reactions. Reactions of Atoms and Radicals with Alkenes, Alkynes and Aromatic Compounds',
        publisher = "London",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972KER/PARB:31",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002410
""",
)

entry(
    index = 340,
    label = "C2H2 + C3H7-2 <=> C5H9",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (158000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (28.851, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (363, 'K'),
        Tmax = (477, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (13300, 'Pa'),
    ),
    reference = Article(
        authors = ["Garcia Dominguez, J.A.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part IX. The addition of methyl, ethyl, isopropyl, and t-butyl radicals to acetylene and the isomerization of alkenyl radicals',
        journal = "J. Chem. Soc.",
        pages = """940-944""",
        year = "1962",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1962GAR/TRO940-944:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002410
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002410/rk00000001.xml
Bath gas: C2H2
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 341,
    label = "C4H6 + CH3 <=> C5H9-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (81300, 'm^3/(mol*s)'),
        n = 0,
        Ea = (17.128, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (353, 'K'),
        Tmax = (453, 'K'),
        Pmin = (400000, 'Pa'),
        Pmax = (400000, 'Pa'),
    ),
    reference = Book(
        authors = ["Kerr, J.A.", "Parsonage, M.J."],
        title = u'Evaluated Kinetic Data on Gas Phase Addition Reactions. Reactions of Atoms and Radicals with Alkenes, Alkynes and Aromatic Compounds',
        publisher = "London",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972KER/PARB:87",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00004745
""",
)

entry(
    index = 342,
    label = "C5H9-2 <=> C4H6 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.75e+13, 's^-1'),
        n = 0.1,
        Ea = (150.2, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Mechanism and rate constants for the decomposition of 1-pentenyl radicals',
        journal = "J. Phys. Chem. A",
        volume = "110",
        pages = """8501-8509""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006TSA8501-8509:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00004745
Pressure dependence: Rate constant is high pressure limit

The log(k/k) values at various pressures were presented in four parameters form
""",
)

entry(
    index = 343,
    label = "C4H8 + CH3 <=> C5H11-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0176, 'm^3/(mol*s)'),
        n = 2.48,
        Ea = (25.648, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:9",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00005827
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 344,
    label = "C4H8 + CH3 <=> C5H11-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (251000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (28.02, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (391, 'K'),
        Tmax = (449, 'K'),
    ),
    reference = Article(
        authors = ["Seres, L.", "Nacsa, A.", "Arthur, N.L."],
        title = u'Thermal decomposition of di-t-butyl peroxide in the presence of (CH3)2C=CH2: reactions of CH3, (CH3)2CCH2CH3, and (CH3)2CCH2C(CH3)2CH2CH3 radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "26",
        pages = """227-246""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994SER/NAC227-246:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00005827
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00005827/rk00000001.xml
Bath gas: (tert-C4H9O)2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 345,
    label = "C5H11-3 <=> C4H8 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.65e+10, 's^-1'),
        n = 1.19,
        Ea = (126.566, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:27",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00005827
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 346,
    label = "C2H4O + C2H5 <=> C4H9O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (33300, 'm^3/(mol*s)'),
        n = 0,
        Ea = (26.765, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:40",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010737
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 347,
    label = "C4H9O-3 <=> C3H6O + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.59e+22, 's^-1'),
        n = -2.55,
        Ea = (70.459, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:53",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011689
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 348,
    label = "C4H9O-3 <=> C3H6O + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1e+15, 's^-1'),
        n = 0,
        Ea = (69.01, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:13",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011689
""",
)

entry(
    index = 349,
    label = "C4H9O-3 <=> C3H6O + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1e+14, 's^-1'),
        n = 0,
        Ea = (60.5, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (323, 'K'),
        Tmax = (383, 'K'),
        Pmin = (4000, 'Pa'),
        Pmax = (6e+06, 'Pa'),
    ),
    reference = Article(
        authors = ["Fittschen, C.", "Hippler, H.", "Viskolcz, B."],
        title = u'The beta C-C bond scission in alkoxy radicals: thermal unimolecular decomposition of t-butoxy radicals',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "2",
        pages = """1677-1683""",
        year = "2000",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2000FIT/HIP1677-1683:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011689
Pressure dependence: Rate constant is high pressure limit
Experimental procedure: Static or low flow - Data taken vs time
Excitation technique: Flash photolysis (laser or conventional)
Time resolution: In real time
Analytical technique: Laser induced fluorescence

Fc=0.87-T/870(K)
""",
)

entry(
    index = 350,
    label = "C4H9O-3 <=> C3H6O + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.1e+14, 's^-1', '*|/', 2.34),
        n = 0,
        Ea = (62.525, 'kJ/mol', '+|-', 0.625),
        T0 = (1, 'K'),
        Tmin = (303, 'K'),
        Tmax = (393, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (120000, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L.", "Hisham, M.W.M.", "Mackay, M."],
        title = u'Decomposition of the t-butoxy radical: II. Studies over the temperature range 303-393 K',
        journal = "Int. J. Chem. Kinet.",
        volume = "21",
        pages = """535-546""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989BAT/HIS535-546:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011689
Uncertainty: 2.3399999
Bath gas: CF4
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 351,
    label = "C4H9O-3 <=> C3H6O + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.98e+14, 's^-1', '*|/', 5),
        n = 0,
        Ea = (66.931, 'kJ/mol', '+|-', 5.355),
        T0 = (1, 'K'),
        Tmin = (402, 'K'),
        Tmax = (443, 'K'),
        Pmin = (4000, 'Pa'),
        Pmax = (133000, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L.", "Robinson, G.N."],
        title = u'Decomposition of the t-Butoxy radical. I. Studies over the temperature range 402-443 K',
        journal = "Int. J. Chem. Kinet.",
        volume = "19",
        pages = """391""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987BAT/ROB391:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011689
Uncertainty: 5.0
Bath gas: CF4
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 352,
    label = "C4H9O-3 <=> C3H6O + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.98e+14, 's^-1', '*|/', 5),
        n = 0,
        Ea = (66.516, 'kJ/mol', '+|-', 5.321),
        T0 = (1, 'K'),
        Tmin = (402, 'K'),
        Tmax = (443, 'K'),
        Pmin = (3333, 'Pa'),
        Pmax = (200000, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L.", "Robinson, G.N."],
        title = u'Decomposition of the t-butoxy radical',
        journal = "Phys. Chem. Behav. Atmos. Pollut. Proc. Eur. Symp.",
        pages = """172""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982BAT/ROB172:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011689
Uncertainty: 5.0
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 353,
    label = "C4H9O-3 <=> C3H6O + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (7.94e+14, 's^-1'),
        n = 0,
        Ea = (69.426, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (402, 'K'),
        Tmax = (443, 'K'),
        Pmin = (3333, 'Pa'),
        Pmax = (200000, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L.", "Robinson, G.N."],
        title = u'Decomposition of the t-butoxy radical',
        journal = "Phys. Chem. Behav. Atmos. Pollut. Proc. Eur. Symp.",
        pages = """172""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982BAT/ROB172:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011689
Bath gas: Ar
""",
)

entry(
    index = 354,
    label = "C4H9O-3 <=> C3H6O + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.98e+14, 's^-1', '*|/', 5),
        n = 0,
        Ea = (66.516, 'kJ/mol', '+|-', 5.321),
        T0 = (1, 'K'),
        Tmin = (403, 'K'),
        Tmax = (443, 'K'),
        Pmin = (3333, 'Pa'),
        Pmax = (200000, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L.", "Robinson, G.N."],
        title = u'Arrhenius Parameters for the Decomposition of the t-Butoxy Radical',
        journal = "Int. J. Chem. Kinet.",
        volume = "14",
        pages = """1053""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982BAT/ROB1053:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011689
Uncertainty: 5.0
Bath gas: CF4
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 355,
    label = "C4H9O-3 <=> C3H6O + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (7.94e+14, 's^-1'),
        n = 0,
        Ea = (69.426, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (403, 'K'),
        Tmax = (1500, 'K'),
        Pmin = (3333, 'Pa'),
        Pmax = (333000, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L.", "Robinson, G.N."],
        title = u'Arrhenius Parameters for the Decomposition of the t-Butoxy Radical',
        journal = "Int. J. Chem. Kinet.",
        volume = "14",
        pages = """1053""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982BAT/ROB1053:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011689
Bath gas: CF4
""",
)

entry(
    index = 356,
    label = "C4H9O-3 <=> C3H6O + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.16e+15, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (71.172, 'kJ/mol', '+|-', 4.265),
        T0 = (1, 'K'),
        Tmin = (393, 'K'),
        Tmax = (433, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L."],
        title = u'The Gas-Phase Decomposition of Alkoxy Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """977""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979BAT977:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011689
Uncertainty: 3.1600001
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 357,
    label = "C4H9O-3 <=> C3H6O + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (5.01e+15, 's^-1'),
        n = 0,
        Ea = (71.172, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (393, 'K'),
        Tmax = (433, 'K'),
        Pmin = (10100, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L.", "Milne, R.T."],
        title = u'The Gas Phase Pyrolysis of Alkyl Nitrites. I. t-Butyl Nitrite',
        journal = "Int. J. Chem. Kinet.",
        volume = "8",
        pages = """59""",
        year = "1976",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976BAT/MIL59:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011689
Bath gas: NO
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 358,
    label = "C4H9O-3 <=> C3H6O + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.98e+15, 's^-1', '*|/', 2.51),
        n = 0,
        Ea = (71.504, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (393, 'K'),
        Tmax = (473, 'K'),
        Pmin = (91200, 'Pa'),
        Pmax = (91200, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L.", "McCulloch, R.D.", "Milne, R.T."],
        title = u'Thermochemical and Kinetic Studies of Alkyl Nitrites (RONO)-D(RO-NO), The Reactions between RO. and NO, and the Decomposition RO.',
        journal = "Proc. Symp. Chem. Kinet. Data Upper Lower Atmos. 1974",
        pages = """441""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975BAT/MCC441:11",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011689
Uncertainty: 2.51
Bath gas: CF4
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 359,
    label = "C4H9O-3 <=> C3H6O + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.34e+13, 's^-1', '*|/', 5),
        n = 0,
        Ea = (70.174, 'kJ/mol', '+|-', 6.319),
        T0 = (1, 'K'),
        Tmin = (373, 'K'),
        Tmax = (423, 'K'),
        Pmin = (3106, 'Pa'),
        Pmax = (46400, 'Pa'),
    ),
    reference = Article(
        authors = ["Cadman, P.", "Trotman-Dickenson, A.F.", "White, A.J."],
        title = u'Kinetics and Pressure-Dependence of the t-Butoxyl Radical Decomposition',
        journal = "J. Chem. Soc. A",
        pages = """2296""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971CAD/TRO2296:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011689
Uncertainty: 5.0
Bath gas: C3H8
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 360,
    label = "C4H9O-3 <=> C3H6O + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (5.01e+14, 's^-1'),
        n = 0,
        Ea = (95.616, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (398, 'K'),
        Tmax = (436, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (7999, 'Pa'),
    ),
    reference = Article(
        authors = ["Yee Quee, M.J.", "Thynne, J.C.J."],
        title = u'Pressure-dependence of decomposition of tert-butoxyl radical',
        journal = "Trans. Faraday Soc.",
        volume = "63",
        pages = """2970-2974""",
        year = "1967",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1967YEE/THY2970-2974:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011689
Bath gas: NO
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 361,
    label = "C4H9O-3 <=> C3H6O + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (5.01e+14, 's^-1'),
        n = 0,
        Ea = (95.616, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (398, 'K'),
        Tmax = (436, 'K'),
        Pmin = (1013, 'Pa'),
        Pmax = (4533, 'Pa'),
    ),
    reference = Article(
        authors = ["Quee, M.J.Y.", "Thynne, J.C.J."],
        title = u'Pressure-dependence of decomposition of tert-butoxyl radical',
        journal = "J. Chem. Soc. Faraday Trans.",
        volume = "63",
        pages = """2970""",
        year = "1967",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1967QUE/THY2970:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011689
Bath gas: (tert-C4H9O)2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 362,
    label = "C4H9O-3 <=> C3H6O + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.3e+14, 's^-1'),
        n = 0,
        Ea = (62.6, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (700, 'K'),
    ),
    reference = Article(
        authors = ["Buback, M.", "Kling, M.", "Schmatz, S."],
        title = u'Decomposition of tertiary alkoxy radicals',
        journal = "Z. Phys. Chem.",
        volume = "219",
        pages = """1205-1222""",
        year = "2005",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2005BUB/KLI1205-1222:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00011689
Pressure dependence: Rate constant is high pressure limit

Reaction potential energy surface was studied using quantum chemistry and rate constants were calculated using transition state theory.
""",
)

entry(
    index = 363,
    label = "C4H9O-3 <=> C3H6O + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.26e+14, 's^-1'),
        n = 0,
        Ea = (64.021, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Choo, K.Y.", "Benson, S.W."],
        title = u'Arrhenius Parameters for the Alkoxy Radical Decomposition Reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """833""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981CHO/BEN833:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Other theoretical""",
    longDesc = 
u"""
PrIMe Reaction: r00011689
""",
)

entry(
    index = 364,
    label = "C4H9O-3 <=> C3H6O + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.58e+15, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (66.516, 'kJ/mol', '+|-', 3.991),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."],
        title = u'Photochemical smog. Rate parameter estimates and computer simulations',
        journal = "J. Phys. Chem.",
        volume = "81",
        pages = """2483""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977BAL/BAR2483:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011689
Uncertainty: 3.1600001
Bath gas: N2
""",
)

entry(
    index = 365,
    label = "C4H9O-3 <=> C3H6O + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1e+11, 's^-1'),
        n = 0,
        Ea = (46.062, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (297, 'K'),
        Tmax = (324, 'K'),
        Pmin = (2666, 'Pa'),
        Pmax = (2666, 'Pa'),
    ),
    reference = Article(
        authors = ["McMillan, G.R."],
        title = u'Photolysis of di-t-butyl peroxide-azomethane and ei-t-butyl peroxide-isobutane mixtures',
        journal = "J. Am. Chem. Soc.",
        volume = "82",
        pages = """2422""",
        year = "1960",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1960MCM2422:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011689
Bath gas: (tert-C4H9O)2
""",
)

entry(
    index = 366,
    label = "C4H9O-3 <=> C3H6O + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (5.01e+09, 's^-1'),
        n = 0,
        Ea = (55.208, 'kJ/mol', '+|-', 9.977),
        T0 = (1, 'K'),
        Tmin = (403, 'K'),
        Tmax = (443, 'K'),
    ),
    reference = Article(
        authors = ["Birss, F.W.", "Danby, C.J.", "Hinshelwood, C."],
        title = u'The thermal dissociation of tertiary butyl peroxide in presence of nitric oxide',
        journal = "Proc. R. Soc. London A",
        volume = "239",
        pages = """154-164""",
        year = "1957",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1957BIR/DAN154-164:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011689
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011689/rk00000001.xml
Bath gas: (tert-C4H9O)2
""",
)

entry(
    index = 367,
    label = "C3H6O + CH3 <=> C4H9O-3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (25000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (42.217, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:42",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011689
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 368,
    label = "C3H6O + CH3 <=> C4H9O-3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (31600, 'm^3/(mol*s)', '*|/', 2.51),
        n = 0,
        Ea = (48.141, 'kJ/mol', '+|-', 4.814),
        T0 = (1, 'K'),
        Tmin = (413, 'K'),
        Tmax = (563, 'K'),
        Pmin = (28300, 'Pa'),
        Pmax = (119000, 'Pa'),
    ),
    reference = Article(
        authors = ["Knoll, H.", "Richter, G.", "Schliebs, R."],
        title = u'On the Gas-Phase Free Radical Displacement Reaction CH3 + CD3COCD3 \u2192\x92 CD3 + CH3COCD3',
        journal = "Int. J. Chem. Kinet.",
        volume = "12",
        pages = """623""",
        year = "1980",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1980KNO/RIC623:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011689
Uncertainty: 2.51
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 369,
    label = "C3H6O + CH3 <=> C4H9O-3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1740, 'm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (56.289, 'kJ/mol', '+|-', 7.317),
        T0 = (1, 'K'),
        Tmin = (373, 'K'),
        Tmax = (423, 'K'),
        Pmin = (3120, 'Pa'),
        Pmax = (46400, 'Pa'),
    ),
    reference = Article(
        authors = ["Cadman, P.", "Trotman-Dickenson, A.F.", "White, A.J."],
        title = u'Kinetics and Pressure-Dependence of the t-Butoxyl Radical Decomposition',
        journal = "J. Chem. Soc. A",
        pages = """2296""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971CAD/TRO2296:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011689
Uncertainty: 5.0
Bath gas: C3H8
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 370,
    label = "C4H9O-4 <=> C2H4 + C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+11, 's^-1'),
        n = 0,
        Ea = (100.605, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (763, 'K'),
        Tmax = (798, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (13300, 'Pa'),
    ),
    reference = Article(
        authors = ["Foucaut, J.-F.", "Martin, R."],
        title = u"No. 18. - Etude analytique et cinetique de la pyrolyse de l'ether ethylique vers 500 \xb0C et a faible avancement",
        journal = "J. Chim. Phys.",
        volume = "75",
        pages = """132""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978FOU/MAR132:7",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011972
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011972/rk00000001.xml
Bath gas: (C2H5)2O
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 371,
    label = "C5H11-4 <=> C4H8 + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (4.25e+17, 's^-1'),
        n = -1.11,
        Ea = (137.863, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:26",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012477
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 372,
    label = "C5H11-4 <=> C4H8 + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (7.94e+13, 's^-1'),
        n = 0,
        Ea = (128.874, 'kJ/mol', '+|-', 3.875),
        T0 = (1, 'K'),
        Tmin = (560, 'K'),
        Tmax = (650, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (1200, 'Pa'),
    ),
    reference = Article(
        authors = ["Slagle, I.R.", "Batt, L.", "Gmurczyk, G.W.", "Gutman, D."],
        title = u'Unimolecular decomposition of the neopentyl radical',
        journal = "J. Phys. Chem.",
        volume = "95",
        pages = """7732-7739""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991SLA/BAT7732-7739:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00012477
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 373,
    label = "C5H11-4 <=> C4H8 + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.07e+13, 's^-1'),
        n = 0,
        Ea = (124.717, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (800, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'The stability of alkyl radicals',
        journal = "J. Am. Chem. Soc.",
        volume = "107",
        pages = """2872-2880""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985TSA2872-2880:8",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from detailed balance/reverse rate""",
    longDesc = 
u"""
PrIMe Reaction: r00012477
""",
)

entry(
    index = 374,
    label = "C5H11-4 <=> C4H8 + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (4.45e+13, 's^-1'),
        n = 0,
        Ea = (127.211, 'kJ/mol', '+|-', 6.377),
        T0 = (1, 'K'),
        Tmin = (653, 'K'),
        Tmax = (793, 'K'),
        Pmin = (66700, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Baldwin, R.R.", "Hisham, M.W.M.", "Walker, R.W."],
        title = u'Arrhenius parameters of elementary reactions involved in the oxidation of neopentane',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "78",
        pages = """1615""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982BAL/HIS1615:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00012477
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 375,
    label = "C5H11-4 <=> C4H8 + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.51e+13, 's^-1', '*|/', 5),
        n = 0,
        Ea = (123.886, 'kJ/mol', '+|-', 7.441),
        T0 = (1, 'K'),
        Tmin = (512, 'K'),
        Tmax = (571, 'K'),
        Pmin = (7466, 'Pa'),
        Pmax = (7466, 'Pa'),
    ),
    reference = Article(
        authors = ["Szirovicza, L.", "Marta, F."],
        title = u'Kinetics of the Decomposition of Neopentane Sensitized by Azoisopropane',
        journal = "Magy. Kem. Foly.",
        volume = "85",
        pages = """369""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979SZI/MAR369:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00012477
Uncertainty: 5.0
Bath gas: neo-C5H12
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 376,
    label = "C5H11-4 <=> C4H8 + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1e+13, 's^-1'),
        n = 0,
        Ea = (125.549, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (750, 'K'),
        Tmax = (755, 'K'),
        Pmin = (13300, 'Pa'),
        Pmax = (13300, 'Pa'),
    ),
    reference = Article(
        authors = ["Muller, J.", "Baronnet, F.", "Scacchi, G.", "Dzierzynski, M.", "Niclause, M."],
        title = u'Influences of ClH and BrH on the Pyrolyses of Neopentane and Ethane at Small Extents of Reaction',
        journal = "Int. J. Chem. Kinet.",
        volume = "9",
        pages = """425""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977MUL/BAR425:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00012477
Bath gas: neo-C5H12
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 377,
    label = "C5H11-4 <=> C4H8 + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2e+13, 's^-1'),
        n = 0,
        Ea = (124.717, 'kJ/mol', '+|-', 8.73),
        T0 = (1, 'K'),
        Tmin = (512, 'K'),
        Tmax = (571, 'K'),
        Pmin = (1600, 'Pa'),
        Pmax = (26300, 'Pa'),
    ),
    reference = Article(
        authors = ["Szirovicza, L.", "Marta, F."],
        title = u'Kinetics of the Decomposition of neo-Pentane Sensitized by Azoisopropane',
        journal = "React. Kinet. Catal. Lett.",
        volume = "3",
        pages = """9""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975SZI/MAR9:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00012477
Bath gas: neo-C5H12
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 378,
    label = "C5H11-4 <=> C4H8 + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.5e+13, 's^-1'),
        n = 0,
        Ea = (121.391, 'kJ/mol', '+|-', 2.428),
        T0 = (1, 'K'),
        Tmin = (529, 'K'),
        Tmax = (608, 'K'),
        Pmin = (3600, 'Pa'),
        Pmax = (30000, 'Pa'),
    ),
    reference = Article(
        authors = ["Furimsky, E.", "Laidler, K.J."],
        title = u'Kinetics of the Mercury- Photosensitized Decomposition of Neopentane. Part II. Reactions of the Methyl and Neopentyl Radicals',
        journal = "Can. J. Chem.",
        volume = "50",
        pages = """1123""",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972FUR/LAI1123:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00012477
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012477/rk00000002.xml
Bath gas: neo-C5H12
Excitation technique: Sensitized photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 379,
    label = "C5H11-4 <=> C4H8 + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.21e+10, 's^-1'),
        n = 1.08,
        Ea = (124.6, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Sun, H.", "Bozzelli, J.W."],
        title = u'Thermochemical and kinetic analysis on the reactions of neopentyl and hydroperoxy-neopentyl radicals with oxygen: Part I.  OH and initial stable HC product formation',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """1694-1711""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004SUN/BOZ1694-1711:31",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00012477
Pressure dependence: Rate constant is high pressure limit

Quantum calculations of energetics of pathways related to reaction between neopentyl radical and O2 (and subsequent reaction pathways). This includes primary reaction pathways as well as subsequent secondary reactions. Used ab initio CBS-Q method, as well as B3LYP/6-31G(d,p) for some molecules. Many reaction channels are discussed in paper, for some, rate expressions are provided at low pressure limit, high pressure limit, and a number of intermediate pressures. For some reaction channels, no rate expressions are given in paper, but are provided in auxillary information associated with the article in JPC.

Rate expressions reported are derived from ab initio transition states using QRRK analysis of the chemically activated reaction pathways. We have only abstracted rate expressions from the paper for 1 atm and 300-900 K. For other pressures and at higher temperatures see paper.
""",
)

entry(
    index = 380,
    label = "C4H8 + CH3 <=> C5H11-4",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (0.0013, 'm^3/(mol*s)'),
        n = 2.48,
        Ea = (35.648, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:10",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012477
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 381,
    label = "C4H8 + CH3 <=> C5H11-4",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (223000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (44.316, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (560, 'K'),
        Tmax = (650, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (1200, 'Pa'),
    ),
    reference = Article(
        authors = ["Slagle, I.R.", "Batt, L.", "Gmurczyk, G.W.", "Gutman, D."],
        title = u'Unimolecular decomposition of the neopentyl radical',
        journal = "J. Phys. Chem.",
        volume = "95",
        pages = """7732-7739""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991SLA/BAT7732-7739:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from detailed balance/reverse rate""",
    longDesc = 
u"""
PrIMe Reaction: r00012477
Bath gas: He
""",
)

entry(
    index = 382,
    label = "C4H9O-5 <=> CH2O + C3H7-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.34e+22, 's^-1'),
        n = -2.8,
        Ea = (63.764, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:54",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00016186
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 383,
    label = "C4H9O-5 <=> CH2O + C3H7-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 's^-1'),
        n = 0,
        Ea = (50.8, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (190, 'K'),
        Tmax = (330, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Johnson, D.", "Cassanelli, P.", "Cox, R.A."],
        title = u'Correlation-type structure activity relationships for the kinetics of the decomposition of simple and beta-substituted alkoxyl radicals',
        journal = "Atmos. Environ.",
        volume = "38",
        pages = """1755-1765""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004JOH/CAS1755-1765:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00016186

The authors developed a structure activity relationship (SARs) for the estimation of rate data for the decomposition of RO to alkyl radical and carbonyl fragments. The SARs are based upon strong, non-linear, correlations between the logarithm of measured room temperature rate coefficients and the average measured ionisation potential (IP) of the reaction products,. The considered compounds include simple unsubstituted, beta-chlorinated and beta-hydroxylated alkoxylradicals. Chemical activation processes in the decomposition chemistry are briefly discussed.

The temperature range over which the estimates are intended to be useful is not given, but the results are derived for atmospheric chemistry occurring in the troposphere through lower stratosphere. This is assumed by us to approimately cover 190 K to 330 K.

For the 10 simple and 11 heteroatom-substituted RO: species used to construct the correlations, 18(85%) of the room temperature rate coefficients predicted using the present method are within a factor of two of their measured (or theoretically calculated) values, and 100% are within a factor of three. The average ratio of measured to calculated rate coefficients is 0.9.
""",
)

entry(
    index = 384,
    label = "C4H9O-5 <=> CH2O + C3H7-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+13, 's^-1'),
        n = 0,
        Ea = (51.882, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Choo, K.Y.", "Benson, S.W."],
        title = u'Arrhenius Parameters for the Alkoxy Radical Decomposition Reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """833""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981CHO/BEN833:7",
    ),
    referenceType = "theory",
    shortDesc = u"""Other theoretical""",
    longDesc = 
u"""
PrIMe Reaction: r00016186
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016186/rk00000001.xml
""",
)

entry(
    index = 385,
    label = "CH2O + C3H7-2 <=> C4H9O-5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (9.749, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Curran, H.J."],
        title = u'Rate constant estimation for C-1 to C-4 alkyl and alkoxyl radical decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """250-275""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006CUR250-275:37",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00016186
Pressure dependence: Rate constant is high pressure limit

Rate coeficients for alkyl and alkoxy radical decomposition reactions, as well as the corresponding reverse adddition reactions, are recommended on the basis of review of large volume of literature and correlations between activation energies and reaction types. The temperature range of recommendations is uncertain. The range cited here (298 - 2000 K) is based on the largest temperature interval used by the author in an Arrhenius plot.
""",
)

entry(
    index = 386,
    label = "C3H7O2 <=> CH2O + C2H5O-4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+13, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (87.302, 'kJ/mol', '+|-', 4.373),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."],
        title = u'Photochemical smog. Rate parameter estimates and computer simulations',
        journal = "J. Phys. Chem.",
        volume = "81",
        pages = """2483""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977BAL/BAR2483:14",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00016688
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016688/rk00000001.xml
Uncertainty: 3.1600001
Bath gas: N2
""",
)

entry(
    index = 387,
    label = "C4H7O <=> C2H4O + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.74e+14, 's^-1'), n=0, Ea=(85.6, 'kJ/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003RAU/BOY431-442:16",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00000050
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00000050/rk00000001.xml

Rate expression does not contain tunneling contributions. Temperature range not specified but it does include 298.15 K.
""",
)

entry(
    index = 388,
    label = "C4H7O <=> C4H6O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.77e+12, 's^-1'), n=0, Ea=(72.2, 'kJ/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003RAU/BOY431-442:7",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00000051
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00000051/rk00000001.xml

Rate expression does not contain tunneling contributions. Temperature range not specified but it does include 298.15 K.
""",
)

entry(
    index = 389,
    label = "C4H7O <=> C3H4O + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.69e+13, 's^-1'), n=0, Ea=(50.7, 'kJ/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003RAU/BOY431-442:12",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00000052
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00000052/rk00000001.xml

Rate expression does not contain tunneling contributions. Temperature range not specified but it does include 298.15 K.
""",
)

entry(
    index = 390,
    label = "C4H6 + CH3 <=> C5H9-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (63100, 'm^3/(mol*s)'),
        n = 0,
        Ea = (31.346, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (743, 'K'),
        Tmax = (772, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (13300, 'Pa'),
    ),
    reference = Article(
        authors = ["Perrin, D.", "Richard, C.", "Martin, R."],
        title = u'H2S-promoted thermal isomerization of Cis-2-pentene to 1-pentene and trans-2-pentene around 800 K',
        journal = "Int. J. Chem. Kinet.",
        volume = "20",
        pages = """621""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988PER/RIC621:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00004745
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004745/rk00000001.xml
Bath gas: 2-(Z)-C5H10
""",
)

entry(
    index = 391,
    label = "C4H9O-2 <=> C2H4O + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+09, 's^-1', '*|/', 5),
        n = 0,
        Ea = (66.931, 'kJ/mol', '+|-', 8.032),
        T0 = (1, 'K'),
        Tmin = (357, 'K'),
        Tmax = (676, 'K'),
        Pmin = (4666, 'Pa'),
        Pmax = (280000, 'Pa'),
    ),
    reference = Article(
        authors = ["Hohlein, G.", "Freeman, G.R."],
        title = u'Radiation-sensitized pyrolysis of diethyl ether. Free-radical reaction rate parameters',
        journal = "J. Am. Chem. Soc.",
        volume = "92",
        pages = """6118""",
        year = "1970",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1970HOH/FRE6118:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010737
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010737/rk00000003.xml
Uncertainty: 5.0
Bath gas: (C2H5)2O
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 392,
    label = "C4H9O-3 <=> C3H6O + CH3",
    degeneracy = 3,
    kinetics = Arrhenius(A=(1.15e+14, 's^-1'), n=0, Ea=(56.9, 'kJ/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003RAU/BOY431-442:11",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00011689
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011689/rk00000023.xml

Rate expression does not contain tunneling contributions. Temperature range not specified but it does include 298.15 K.
""",
)

entry(
    index = 393,
    label = "C5H9-4 <=> C2H4 + C3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.31e+13, 's^-1'),
        n = 0,
        Ea = (93.954, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (290, 'K'),
        Tmax = (310, 'K'),
        Pmin = (1013, 'Pa'),
        Pmax = (4026, 'Pa'),
    ),
    reference = Article(
        authors = ["Gierczak, T.", "Gawlowski, J.", "Niedzielski, J."],
        title = u'Mutual isomerization of cyclopentyl and 1-penten-5-yl radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "18",
        pages = """623-637""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986GIE/GAW623-637:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00013096
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013096/rk00000001.xml
Bath gas: H2S
""",
)

entry(
    index = 394,
    label = "C5H9-2 <=> C4H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.26e+13, 's^-1'),
        n = 0,
        Ea = (159.638, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (743, 'K'),
        Tmax = (772, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (13300, 'Pa'),
    ),
    reference = Article(
        authors = ["Perrin, D.", "Richard, C.", "Martin, R."],
        title = u'H2S-promoted thermal isomerization of Cis-2-pentene to 1-pentene and trans-2-pentene around 800 K',
        journal = "Int. J. Chem. Kinet.",
        volume = "20",
        pages = """621""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988PER/RIC621:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00004745
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004745/rk00000004.xml
Bath gas: 2-(Z)-C5H10
Excitation technique: Thermal
Analytical technique: Gas chromatography
Reference reaction: H2S + CH2CH=CHCH2CH3 -> 2-(Z)-C5H10 + SH
""",
)

entry(
    index = 395,
    label = "C4H8-3 + CH3 <=> C5H11-5",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (45000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (29.267, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (399, 'K'),
        Tmax = (436, 'K'),
        Pmin = (5466, 'Pa'),
        Pmax = (8666, 'Pa'),
    ),
    reference = Article(
        authors = ["Yokoyama, N.", "Brinton, R.K."],
        title = u'Reaction of methyl radicals with cis-butene-2',
        journal = "Can. J. Chem.",
        volume = "47",
        pages = """2987""",
        year = "1969",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1969YOK/BRI2987:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00007721
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007721/rk00000002.xml
Bath gas: CH3CHO
Excitation technique: Thermal
Analytical technique: Gas chromatography
Reference reaction: *CH3 + *CH3 -> C2H6
""",
)

entry(
    index = 396,
    label = "C4H9O-2 <=> C2H4O + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+13, 's^-1'),
        n = 0,
        Ea = (73.25, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (423, 'K'),
        Tmax = (463, 'K'),
        Pmin = (1600, 'Pa'),
        Pmax = (26700, 'Pa'),
    ),
    reference = Article(
        authors = ["East, R.L.", "Phillips, L."],
        title = u'Pressure-dependence of the gas-phase pyrolysis of the s-butoxyl radical at 150-190\xb0',
        journal = "J. Chem. Soc. A",
        pages = """1939""",
        year = "1967",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1967EAS/PHI1939:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010737
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010737/rk00000001.xml
Bath gas: sec-C4H9NO2
Excitation technique: Thermal
Analytical technique: Gas chromatography
Reference reaction: 2-C4H9O + NO -> C2H5COCH3 + HNO
""",
)

entry(
    index = 397,
    label = "C4H9O-6 <=> C2H4O + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+16, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (73.25, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (393, 'K'),
        Tmax = (473, 'K'),
        Pmin = (91200, 'Pa'),
        Pmax = (91200, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L.", "McCulloch, R.D.", "Milne, R.T."],
        title = u'Thermochemical and Kinetic Studies of Alkyl Nitrites (RONO)-D(RO-NO), The Reactions between RO. and NO, and the Decomposition RO.',
        journal = "Proc. Symp. Chem. Kinet. Data Upper Lower Atmos. 1974",
        pages = """441""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975BAT/MCC441:18",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00016188
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000001.xml
Uncertainty: 3.1600001
Bath gas: CF4
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 398,
    label = "C4H9O-6 <=> C2H4O + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.31e+14, 's^-1'),
        n = 0,
        Ea = (64.021, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (433, 'K'),
        Tmax = (473, 'K'),
        Pmin = (10100, 'Pa'),
        Pmax = (91200, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L.", "McCulloch, R.D."],
        title = u'The Gas-Phase Pyrolysis of Alkyl Nitrites. II. s-Butyl Nitrite',
        journal = "Int. J. Chem. Kinet.",
        volume = "8",
        pages = """911""",
        year = "1976",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976BAT/MCC911:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00016188
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000002.xml
Bath gas: NO
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 399,
    label = "C4H9O-6 <=> C2H4O + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.76e+14, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (61.111, 'kJ/mol', '+|-', 4.274),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."],
        title = u'Photochemical smog. Rate parameter estimates and computer simulations',
        journal = "J. Phys. Chem.",
        volume = "81",
        pages = """2483""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977BAL/BAR2483:7",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00016188
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000003.xml
Uncertainty: 3.1600001
Bath gas: N2
""",
)

entry(
    index = 400,
    label = "C4H9O-6 <=> C2H4O + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+14, 's^-1'),
        n = 0,
        Ea = (64.021, 'kJ/mol', '+|-', 4.482),
        T0 = (1, 'K'),
        Tmin = (393, 'K'),
        Tmax = (433, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L."],
        title = u'The Gas-Phase Decomposition of Alkoxy Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """977""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979BAT977:8",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016188
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000004.xml
Bath gas: NO
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 401,
    label = "C4H9O-6 <=> C2H4O + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+13, 's^-1'),
        n = 0,
        Ea = (56.455, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Choo, K.Y.", "Benson, S.W."],
        title = u'Arrhenius Parameters for the Alkoxy Radical Decomposition Reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """833""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981CHO/BEN833:8",
    ),
    referenceType = "theory",
    shortDesc = u"""Other theoretical""",
    longDesc = 
u"""
PrIMe Reaction: r00016188
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000005.xml
""",
)

entry(
    index = 402,
    label = "C4H9O-6 <=> C2H4O + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15, 's^-1'),
        n = 0,
        Ea = (64.437, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:31",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00016188
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000007.xml
""",
)

entry(
    index = 403,
    label = "C4H9O-6 <=> C2H4O + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.35e+13, 's^-1', '+|-', 3.4e+13),
        n = 0,
        Ea = (62.774, 'kJ/mol', '+|-', 3.766),
        T0 = (1, 'K'),
        Tmin = (363, 'K'),
        Tmax = (503, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Heiss, A.", "Tardieu de Maleissye, J.", "Viossat, V.", "Sahetchian, K.A."],
        title = u'Reactions of primary and secondary butoxy radicals in oxygen at atmospheric pressure',
        journal = "Int. J. Chem. Kinet.",
        volume = "23",
        pages = """607-622""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991HEI/TAR607-622:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00016188
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000008.xml
Uncertainty: 2.0
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 404,
    label = "C4H9O-6 <=> C2H4O + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.25e+13, 's^-1'), n=0, Ea=(48.9, 'kJ/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003RAU/BOY431-442:14",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00016188
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000009.xml

Rate expression does not contain tunneling contributions. Temperature range not specified but it does include 298.15 K.
""",
)

entry(
    index = 405,
    label = "C4H9O-6 <=> C4H8O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.51e+13, 's^-1'), n=0, Ea=(75.6, 'kJ/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003RAU/BOY431-442:5",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00016189
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016189/rk00000001.xml

Rate expression does not contain tunneling contributions. Temperature range not specified but it does include 298.15 K.
""",
)

entry(
    index = 406,
    label = "C4H9O-6 <=> C3H6O-2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+14, 's^-1'),
        n = 0,
        Ea = (79.486, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (393, 'K'),
        Tmax = (433, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L."],
        title = u'The Gas-Phase Decomposition of Alkoxy Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """977""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979BAT977:9",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016190
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016190/rk00000001.xml
Bath gas: NO
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 407,
    label = "C4H9O-6 <=> C3H6O-2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15, 's^-1'),
        n = 0,
        Ea = (79.902, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:32",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00016190
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016190/rk00000002.xml
""",
)

entry(
    index = 408,
    label = "C4H9O-6 <=> C3H6O-2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.78e+13, 's^-1'), n=0, Ea=(62.3, 'kJ/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003RAU/BOY431-442:10",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00016190
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016190/rk00000003.xml

Rate expression does not contain tunneling contributions. Temperature range not specified but it does include 298.15 K.
""",
)

entry(
    index = 409,
    label = "C2H4 + C4H9-3 <=> C6H13",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (23400, 'm^3/(mol*s)'),
        n = 0,
        Ea = (28.02, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (352, 'K'),
        Tmax = (405, 'K'),
        Pmin = (800, 'Pa'),
        Pmax = (14700, 'Pa'),
    ),
    reference = Book(
        authors = ["Kerr, J.A.", "Parsonage, M.J."],
        title = u'Evaluated Kinetic Data on Gas Phase Addition Reactions. Reactions of Atoms and Radicals with Alkenes, Alkynes and Aromatic Compounds',
        publisher = "London",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972KER/PARB:10",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002224
""",
)

entry(
    index = 410,
    label = "C2H4 + C4H9-3 <=> C6H13",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.19e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (28.02, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (352, 'K'),
        Tmax = (405, 'K'),
    ),
    reference = Article(
        authors = ["Watkins, K.W.", "O'Deen, L.A."],
        title = u'Kinetics of the addition of ethyl, isopropyl, n-butyl, and isopentyl radicals to ethylene',
        journal = "J. Phys. Chem.",
        volume = "73",
        pages = """4094-4102""",
        year = "1969",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1969WAT/ODE4094-4102:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002224
Bath gas: (C2H5)2NN
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 411,
    label = "C2H4 + C4H9-3 <=> C6H13",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (126000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (30.514, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (350, 'K'),
        Tmax = (464, 'K'),
        Pmin = (11900, 'Pa'),
        Pmax = (11900, 'Pa'),
    ),
    reference = Article(
        authors = ["Kerr, J.A.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part III. n-Butyl radicals from the photolysis of n-Valeraldehyde',
        journal = "J. Chem. Soc.",
        pages = """1602""",
        year = "1960",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1960KER/TRO1602:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002224
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002224/rk00000001.xml
Bath gas: n-C4H9CHO
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 412,
    label = "C2H2 + C4H9 <=> C6H11",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (50100, 'm^3/(mol*s)'),
        n = 0,
        Ea = (22.2, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (373, 'K'),
        Tmax = (493, 'K'),
        Pmin = (920, 'Pa'),
        Pmax = (32500, 'Pa'),
    ),
    reference = Article(
        authors = ["Garcia Dominguez, J.A.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part IX. The addition of methyl, ethyl, isopropyl, and t-butyl radicals to acetylene and the isomerization of alkenyl radicals',
        journal = "J. Chem. Soc.",
        pages = """940-944""",
        year = "1962",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1962GAR/TRO940-944:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002406
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002406/rk00000001.xml
Bath gas: C2H2
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 413,
    label = "C3H6O-3 + C2H5 <=> C5H11O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (746000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (36.833, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (323, 'K'),
        Tmax = (415, 'K'),
    ),
    reference = Article(
        authors = ["Brown, A.C.R.", "James, D.G.L."],
        title = u'A kinetic study of the metathetical and addition reactions characteristic of allyl polymerization',
        journal = "Can. J. Chem.",
        volume = "40",
        pages = """796-803""",
        year = "1962",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1962BRO/JAM796-803:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00004930
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004930/rk00000001.xml
Bath gas: (C2H5)2CO
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 414,
    label = "C6H10 + H <=> C6H11-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.2e+07, 'm^3/(mol*s)', '+|-', 4.2e+06),
        n = 0,
        Ea = (10.476, 'kJ/mol', '+|-', 2.519),
        T0 = (1, 'K'),
        Tmin = (296, 'K'),
        Tmax = (493, 'K'),
        Pmin = (253, 'Pa'),
        Pmax = (1960, 'Pa'),
    ),
    reference = Article(
        authors = ["Hoyermann, K.", "Preuss, A.W.", "Wagner, H.G."],
        title = u'Die reaktionen von atomarem wasserstoff mit cyclohexen, cyclohexadien-1,3 und benzol',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "79",
        pages = """156""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975HOY/PRE156:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005528
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00005528/rk00000004.xml
Bath gas: He
Excitation technique: Electron beam
Analytical technique: Electron spin resonance (ESR or EPR)
""",
)

entry(
    index = 415,
    label = "C6H11-2 <=> C6H10 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.91e+13, 's^-1'),
        n = 0,
        Ea = (148.513, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (533, 'K'),
        Tmax = (780, 'K'),
    ),
    reference = Article(
        authors = ["Knepp, A.M.", "Meloni, G.", "Jusinski, L.E.", "Taatjes, C.A.", "Cavallotti, C.", "Klippenstein, S.J."],
        title = u'Theory, measurements, and modeling of OH and HO2 formation in the reaction of cyclohexyl radicals with O2',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "9",
        pages = """4315-4331""",
        year = "2007",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2007KNE/MEL4315-4331:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00005528

The detailed rate coefficients for all experimental conditions, carried out using the final adjusted stationary point energies, are given as electronic supplementary information.
""",
)

entry(
    index = 416,
    label = "C3H6 + C3H5 <=> C6H11-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (355000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (70.673, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (762, 'K'),
        Tmax = (811, 'K'),
        Pmin = (4000, 'Pa'),
        Pmax = (26700, 'Pa'),
    ),
    reference = Article(
        authors = ["Barbe, P.", "Martin, R.", "Perrin, D.", "Scacchi, G."],
        title = u'Kinetics and modeling of the thermal reaction of propene at 800 K. Part I. Pure propene',
        journal = "Int. J. Chem. Kinet.",
        volume = "28",
        pages = """829-847""",
        year = "1996",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996BAR/MAR829-847:7",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00005637
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00005637/rk00000001.xml
Bath gas: CH3CH=CH2
""",
)

entry(
    index = 417,
    label = "C6H13-2 <=> C3H6 + C3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+13, 's^-1'),
        n = 0,
        Ea = (108.92, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (823, 'K'),
        Tmax = (999, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (80000, 'Pa'),
    ),
    reference = Article(
        authors = ["Lin, M.C.", "Back, M.H."],
        title = u'The thermal decomposition of ethane. Part III. Secondary reactions',
        journal = "Can. J. Chem.",
        volume = "44",
        pages = """2369""",
        year = "1966",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1966LIN/BAC2369:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011228
Bath gas: C2H6
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 418,
    label = "C6H13-2 <=> C3H6 + C3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 's^-1'),
        n = 0,
        Ea = (125.549, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (723, 'K'),
        Tmax = (823, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (13300, 'Pa'),
    ),
    reference = Article(
        authors = ["Imbert, F.E.", "Marshall, R.M."],
        title = u'The mechanism and rate parameters for the pyrolysis of n-hexane in the range 723-823 K',
        journal = "Int. J. Chem. Kinet.",
        volume = "19",
        pages = """81""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987IMB/MAR81:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011228
Bath gas: N2
""",
)

entry(
    index = 419,
    label = "C6H13-2 <=> C3H6 + C3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 's^-1'),
        n = 0,
        Ea = (93.954, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (800, 'K'),
        Tmax = (900, 'K'),
        Pmin = (12300, 'Pa'),
        Pmax = (12300, 'Pa'),
    ),
    reference = Article(
        authors = ["Quinn, C.P."],
        title = u'Isomerization of primary n-alkyl radicals in the pyrolysis of ethane',
        journal = "J. Chem. Soc. Faraday Trans. 2",
        volume = "59",
        pages = """2543""",
        year = "1963",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1963QUI2543:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011228
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011228/rk00000001.xml
Bath gas: C2H6
""",
)

entry(
    index = 420,
    label = "C5H11O-2 <=> C3H6O + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+14, 's^-1'),
        n = 0,
        Ea = (45.7, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (700, 'K'),
    ),
    reference = Article(
        authors = ["Buback, M.", "Kling, M.", "Schmatz, S."],
        title = u'Decomposition of tertiary alkoxy radicals',
        journal = "Z. Phys. Chem.",
        volume = "219",
        pages = """1205-1222""",
        year = "2005",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2005BUB/KLI1205-1222:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00015135
Pressure dependence: Rate constant is high pressure limit

Reaction potential energy surface was studied using quantum chemistry and rate constants were calculated using transition state theory.
""",
)

entry(
    index = 421,
    label = "C5H11O-2 <=> C4H8O + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.3e+14, 's^-1'),
        n = 0,
        Ea = (60.4, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (700, 'K'),
    ),
    reference = Article(
        authors = ["Buback, M.", "Kling, M.", "Schmatz, S."],
        title = u'Decomposition of tertiary alkoxy radicals',
        journal = "Z. Phys. Chem.",
        volume = "219",
        pages = """1205-1222""",
        year = "2005",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2005BUB/KLI1205-1222:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00015136
Pressure dependence: Rate constant is high pressure limit

Reaction potential energy surface was studied using quantum chemistry and rate constants were calculated using transition state theory.
""",
)

entry(
    index = 422,
    label = "C6H11-4 <=> C2H4 + C4H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 's^-1'),
        n = 0,
        Ea = (124.717, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (1300, 'K'),
        Pmin = (23300, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Handford-Styring, S.M.", "Walker, R.W."],
        title = u'Addition of cyclopentane to slowly reacting mixtures of H2 + O2 between 673 and 783 K: reactions of H and OH with cyclopentane and of cyclopentyl radicals',
        journal = "J. Chem. Soc. Faraday Trans.",
        volume = "91",
        pages = """1431-1438""",
        year = "1995",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1995HAN/WAL1431-1438:11",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00015690
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015690/rk00000001.xml
Bath gas: O2
""",
)

entry(
    index = 423,
    label = "C6H13-3 <=> C5H10 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+13, 's^-1'),
        n = 0,
        Ea = (129.706, 'kJ/mol', '+|-', 6.477),
        T0 = (1, 'K'),
        Tmin = (773, 'K'),
        Tmax = (813, 'K'),
        Pmin = (733, 'Pa'),
        Pmax = (17300, 'Pa'),
    ),
    reference = Article(
        authors = ["Baldwin, R.R.", "Drewery, G.R.", "Walker, R.W."],
        title = u'Decomposition of 2,3-dimethylbutane in the presence of oxygen. Part 2.-Elementary reactions involved in the formation of products',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "80",
        pages = """3195""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984BAL/DRE3195:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00016149
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016149/rk00000001.xml
Bath gas: O2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 424,
    label = "C6H13-3 <=> C6H12 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.31e+13, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (148.829, 'kJ/mol', '+|-', 7.45),
        T0 = (1, 'K'),
        Tmin = (753, 'K'),
        Tmax = (813, 'K'),
        Pmin = (733, 'Pa'),
        Pmax = (17300, 'Pa'),
    ),
    reference = Article(
        authors = ["Baldwin, R.R.", "Drewery, G.R.", "Walker, R.W."],
        title = u'Decomposition of 2,3-dimethylbutane in the presence of oxygen. Part 2.-Elementary reactions involved in the formation of products',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "80",
        pages = """3195""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984BAL/DRE3195:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00016150
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016150/rk00000001.xml
Uncertainty: 3.1600001
Bath gas: O2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 425,
    label = "C5H11O-3 <=> C2H4O + C3H7-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 's^-1'),
        n = 0,
        Ea = (46.1, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (190, 'K'),
        Tmax = (330, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Johnson, D.", "Cassanelli, P.", "Cox, R.A."],
        title = u'Correlation-type structure activity relationships for the kinetics of the decomposition of simple and beta-substituted alkoxyl radicals',
        journal = "Atmos. Environ.",
        volume = "38",
        pages = """1755-1765""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004JOH/CAS1755-1765:11",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00016551

The authors developed a structure activity relationship (SARs) for the estimation of rate data for the decomposition of RO to alkyl radical and carbonyl fragments. The SARs are based upon strong, non-linear, correlations between the logarithm of measured room temperature rate coefficients and the average measured ionisation potential (IP) of the reaction products,. The considered compounds include simple unsubstituted, beta-chlorinated and beta-hydroxylated alkoxylradicals. Chemical activation processes in the decomposition chemistry are briefly discussed.

The temperature range over which the estimates are intended to be useful is not specifically given, but the results are derived for atmospheric chemistry occurring in the troposphere through lower stratosphere. This is assumed by us to approimately cover 190 K to 330 K.

For the 10 simple and 11 heteroatom-substituted RO: species used to construct the correlations, 18(85%) of the room temperature rate coefficients predicted using the present method are within a factor of two of their measured (or theoretically calculated) values, and 100% are within a factor ofthree. The average ratio of measured to calculated rate coefficients is 0.9.
""",
)

entry(
    index = 426,
    label = "C5H11O-3 <=> C2H4O + C3H7-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+13, 's^-1'),
        n = 0,
        Ea = (51.882, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Baldwin, R.R.", "Walker, R.W."],
        title = u'Elementary Reactions in the Oxidation of Alkenes',
        journal = "Symp. Int. Combust. Proc.",
        volume = "18",
        pages = """819""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981BAL/WAL819:10",
    ),
    referenceType = "theory",
    shortDesc = u"""Other theoretical""",
    longDesc = 
u"""
PrIMe Reaction: r00016551
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016551/rk00000001.xml
""",
)

entry(
    index = 427,
    label = "C4H7O2 <=> C2H4O + C2H3O-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 's^-1'),
        n = 0,
        Ea = (23.9, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (190, 'K'),
        Tmax = (330, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Johnson, D.", "Cassanelli, P.", "Cox, R.A."],
        title = u'Correlation-type structure activity relationships for the kinetics of the decomposition of simple and beta-substituted alkoxyl radicals',
        journal = "Atmos. Environ.",
        volume = "38",
        pages = """1755-1765""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004JOH/CAS1755-1765:17",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00016689

The authors developed a structure activity relationship (SARs) for the estimation of rate data for the decomposition of RO to alkyl radical and carbonyl fragments. The SARs are based upon strong, non-linear, correlations between the logarithm of measured room temperature rate coefficients and the average measured ionisation potential (IP) of the reaction products,. The considered compounds include simple unsubstituted, beta-chlorinated and beta-hydroxylated alkoxylradicals. Chemical activation processes in the decomposition chemistry are briefly discussed.

The temperature range over which the estimates are intended to be useful is not specifically given, but the results are derived for atmospheric chemistry occurring in the troposphere through lower stratosphere. This is assumed by us to approimately cover 190 K to 330 K.

For the 10 simple and 11 heteroatom-substituted RO: species used to construct the correlations, 18(85%) of the room temperature rate coefficients predicted using the present method are within a factor of two of their measured (or theoretically calculated) values, and 100% are within a factor ofthree. The average ratio of measured to calculated rate coefficients is 0.9.
""",
)

entry(
    index = 428,
    label = "C4H7O2 <=> C2H4O + C2H3O-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.16e+14, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (53.545, 'kJ/mol', '+|-', 4.282),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."],
        title = u'Photochemical smog. Rate parameter estimates and computer simulations',
        journal = "J. Phys. Chem.",
        volume = "81",
        pages = """2483""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977BAL/BAR2483:15",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00016689
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016689/rk00000001.xml
Uncertainty: 3.1600001
Bath gas: N2
""",
)

entry(
    index = 429,
    label = "C2H4 + C4H9 <=> C6H13-4",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (158000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (29.683, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (370, 'K'),
        Tmax = (455, 'K'),
    ),
    reference = Article(
        authors = ["Birrell, R.N.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part VII. t-butyl radicals from the photolysis of pivalaldehyde',
        journal = "J. Chem. Soc.",
        pages = """4218""",
        year = "1960",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1960BIR/TRO4218:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002194
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002194/rk00000001.xml
Bath gas: 2,2-dimethylpropanal
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 430,
    label = "C5H8 + OH <=> C5H9O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (578000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (23.871, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (500, 'K'),
    ),
    reference = Article(
        authors = ["Francisco-Marquez, M.", "Alvarez-Idaboy, J.R.", "Galano, A.", "Vivier-Bunge, A."],
        title = u'Theoretical study of the initial reaction between OH and isoprene in tropospheric conditions',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "5",
        pages = """1392-1399""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003FRA/ALV1392-1399:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00003845
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00003845/rk00000001.xml

A quantum chemical study of the reaction of OH with isoprene (2-Methyl-1,3-butadiene). Used ab initio MP2/cc-pVTZ and CCSD(T)/6-311+G(d,p) methods, also DFT BHandHLYP/6-311G(d,p) methods. Computed rate constants from transtion states using Truongs TST The Rate program. Found good agreement with experimental measurements for total and site specific rate constants. Addition to double bonds at terminal sites is barrierless, while addition to internal sites has a barrier of 10-20 kJ/mol using the DFT method. The CCSD(T)/6-311+G(d,p)//MP2/6-311G(d,p) barriers were significantly higher (9-11 kJ/mol for terminal addition and 27-35 kJ/mol for internal addition). Rate constants reported here are using the DFT energetics.
""",
)

entry(
    index = 431,
    label = "C5H8 + OH <=> C5H9O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.09e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (13.029, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (500, 'K'),
    ),
    reference = Article(
        authors = ["Francisco-Marquez, M.", "Alvarez-Idaboy, J.R.", "Galano, A.", "Vivier-Bunge, A."],
        title = u'Theoretical study of the initial reaction between OH and isoprene in tropospheric conditions',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "5",
        pages = """1392-1399""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003FRA/ALV1392-1399:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00003846
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00003846/rk00000001.xml

A quantum chemical study of the reaction of OH with isoprene (2-Methyl-1,3-butadiene). Used ab initio MP2/cc-pVTZ and CCSD(T)/6-311+G(d,p) methods, also DFT BHandHLYP/6-311G(d,p) methods. Computed rate constants from transtion states using Truongs TST The Rate program. Found good agreement with experimental measurements for total and site specific rate constants. Addition to double bonds at terminal sites is barrierless, while addition to internal sites has a barrier of 10-20 kJ/mol using the DFT method. The CCSD(T)/6-311+G(d,p)//MP2/6-311G(d,p) barriers were significantly higher (9-11 kJ/mol for terminal addition and 27-35 kJ/mol for internal addition). Rate constants reported here are using the DFT energetics.
""",
)

entry(
    index = 432,
    label = "C5H8 + OH <=> C5H9O-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.35e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (-2.104, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (500, 'K'),
    ),
    reference = Article(
        authors = ["Francisco-Marquez, M.", "Alvarez-Idaboy, J.R.", "Galano, A.", "Vivier-Bunge, A."],
        title = u'Theoretical study of the initial reaction between OH and isoprene in tropospheric conditions',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "5",
        pages = """1392-1399""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003FRA/ALV1392-1399:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00003847
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00003847/rk00000001.xml

A quantum chemical study of the reaction of OH with isoprene (2-Methyl-1,3-butadiene). Used ab initio MP2/cc-pVTZ and CCSD(T)/6-311+G(d,p) methods, also DFT BHandHLYP/6-311G(d,p) methods. Computed rate constants from transtion states using Truongs TST The Rate program. Found good agreement with experimental measurements for total and site specific rate constants. Addition to double bonds at terminal sites is barrierless, while addition to internal sites has a barrier of 10-20 kJ/mol using the DFT method. The CCSD(T)/6-311+G(d,p)//MP2/6-311G(d,p) barriers were significantly higher (9-11 kJ/mol for terminal addition and 27-35 kJ/mol for internal addition). Rate constants reported here are using the DFT energetics.

NOTE Main product channels (adding to terminal carbon) are resonance stabilized radicals. They can be drawn with several Lewis structures. The ones drawn here are with "radical" located on terminal carbon.
""",
)

entry(
    index = 433,
    label = "C5H8 + OH <=> C5H9O-4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.44e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (-5.621, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (500, 'K'),
    ),
    reference = Article(
        authors = ["Francisco-Marquez, M.", "Alvarez-Idaboy, J.R.", "Galano, A.", "Vivier-Bunge, A."],
        title = u'Theoretical study of the initial reaction between OH and isoprene in tropospheric conditions',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "5",
        pages = """1392-1399""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003FRA/ALV1392-1399:5",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00003848
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00003848/rk00000001.xml

A quantum chemical study of the reaction of OH with isoprene (2-Methyl-1,3-butadiene). Used ab initio MP2/cc-pVTZ and CCSD(T)/6-311+G(d,p) methods, also DFT BHandHLYP/6-311G(d,p) methods. Computed rate constants from transtion states using Truongs TST The Rate program. Found good agreement with experimental measurements for total and site specific rate constants. Addition to double bonds at terminal sites is barrierless, while addition to internal sites has a barrier of 10-20 kJ/mol using the DFT method. The CCSD(T)/6-311+G(d,p)//MP2/6-311G(d,p) barriers were significantly higher (9-11 kJ/mol for terminal addition and 27-35 kJ/mol for internal addition). Rate constants reported here are using the DFT energetics.

NOTE Main product channels (adding to terminal carbon) are resonance stabilized radicals. They can be drawn with several Lewis structures. The ones drawn here are with "radical" located on terminal carbon.
""",
)

entry(
    index = 434,
    label = "HO2 + C4H8 <=> C4H9O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0131, 'm^3/(mol*s)'),
        n = 2.1,
        Ea = (31.547, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Chen, C.-J.", "Bozzelli, J.W."],
        title = u'Analysis of Tertiary Butyl Radical + O2, Isobutene + HO2, Isobutene + OH, and Isobutene-OH Adducts + O2: A Detailed Tertiary Butyl Oxidation Mechanism',
        journal = "J. Phys. Chem. A",
        volume = "103",
        pages = """9731-9769""",
        year = "1999",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1999CHE/BOZ9731-9769:7",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00011862
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011862/rk00000001.xml
Pressure dependence: Rate constant is high pressure limit
""",
)

entry(
    index = 435,
    label = "C5H11O-2 <=> C3H6O + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+14, 's^-1', '*|/', 1.58),
        n = 0,
        Ea = (59.864, 'kJ/mol', '+|-', 4.19),
        T0 = (1, 'K'),
        Tmin = (433, 'K'),
        Tmax = (463, 'K'),
        Pmin = (267, 'Pa'),
        Pmax = (267, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L.", "Islam, T.S.A.", "Rattray, G.N."],
        title = u'The Gas-Phase Pyrolysis of Alkyl Nitrites. VI. t-Amyl Nitrite',
        journal = "Int. J. Chem. Kinet.",
        volume = "10",
        pages = """931""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978BAT/ISL931:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00015135
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015135/rk00000001.xml
Uncertainty: 1.58
Bath gas: NO
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 436,
    label = "C5H11O-2 <=> C3H6O + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.31e+14, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (57.702, 'kJ/mol', '+|-', 4.041),
        T0 = (1, 'K'),
        Tmin = (393, 'K'),
        Tmax = (473, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L."],
        title = u'The Gas-Phase Decomposition of Alkoxy Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """977""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979BAT977:7",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015135
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015135/rk00000003.xml
Uncertainty: 3.1600001
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 437,
    label = "C5H11O-2 <=> C3H6O + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+13, 's^-1'),
        n = 0,
        Ea = (51.882, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Choo, K.Y.", "Benson, S.W."],
        title = u'Arrhenius Parameters for the Alkoxy Radical Decomposition Reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """833""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981CHO/BEN833:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Other theoretical""",
    longDesc = 
u"""
PrIMe Reaction: r00015135
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015135/rk00000004.xml
""",
)

entry(
    index = 438,
    label = "C5H11O-2 <=> C3H6O + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15, 's^-1'),
        n = 0,
        Ea = (64.021, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:28",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00015135
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015135/rk00000005.xml
""",
)

entry(
    index = 439,
    label = "C5H11O-2 <=> C4H8O + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+13, 's^-1'),
        n = 0,
        Ea = (67.347, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Choo, K.Y.", "Benson, S.W."],
        title = u'Arrhenius Parameters for the Alkoxy Radical Decomposition Reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """833""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981CHO/BEN833:5",
    ),
    referenceType = "theory",
    shortDesc = u"""Other theoretical""",
    longDesc = 
u"""
PrIMe Reaction: r00015136
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015136/rk00000002.xml
""",
)

entry(
    index = 440,
    label = "C5H11O-2 <=> C4H8O + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+15, 's^-1'),
        n = 0,
        Ea = (78.239, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:29",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00015136
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015136/rk00000003.xml
""",
)

entry(
    index = 441,
    label = "C5H11O-2 <=> C4H8O + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+15, 's^-1'),
        n = 0,
        Ea = (78.239, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (433, 'K'),
        Tmax = (463, 'K'),
        Pmin = (267, 'Pa'),
        Pmax = (267, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L.", "Islam, T.S.A.", "Rattray, G.N."],
        title = u'The Gas-Phase Pyrolysis of Alkyl Nitrites. VI. t-Amyl Nitrite',
        journal = "Int. J. Chem. Kinet.",
        volume = "10",
        pages = """931""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978BAT/ISL931:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00015136
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015136/rk00000001.xml
Bath gas: NO
Excitation technique: Thermal
Analytical technique: Gas chromatography
Reference reaction: C2H5C(CH3)2O(*) -> (CH3)2CO + *C2H5
""",
)

entry(
    index = 442,
    label = "C5H11O-4 <=> C2H4O + C3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+14, 's^-1', '*|/', 2.51),
        n = 0,
        Ea = (57.702, 'kJ/mol', '+|-', 3.467),
        T0 = (1, 'K'),
        Tmin = (363, 'K'),
        Tmax = (413, 'K'),
    ),
    reference = Article(
        authors = ["Dobe, S.", "Berces, T.", "Marta, F."],
        title = u'Gas phase decomposition and isomerization reactions of 2-pentoxy radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "18",
        pages = """329""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986DOB/BER329:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00016656
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016656/rk00000001.xml
Uncertainty: 2.51
Bath gas: CO2
Excitation technique: Thermal
Analytical technique: Gas chromatography
Reference reaction: NO + CH3(CH2)2CH(CH3)O -> CH3(CH2)2CH(CH3)ONO
""",
)

entry(
    index = 443,
    label = "C5H11O-4 <=> C2H4O + C3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15, 's^-1'),
        n = 0,
        Ea = (64.437, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:33",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00016656
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016656/rk00000002.xml
""",
)

entry(
    index = 444,
    label = "C5H11O-4 <=> C4H8O-2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+14, 's^-1'),
        n = 0,
        Ea = (72.835, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (363, 'K'),
        Tmax = (413, 'K'),
    ),
    reference = Article(
        authors = ["Dobe, S.", "Berces, T.", "Marta, F."],
        title = u'Gas phase decomposition and isomerization reactions of 2-pentoxy radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "18",
        pages = """329""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986DOB/BER329:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00016657
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016657/rk00000001.xml
Bath gas: CO2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 445,
    label = "C4H9O2-2 <=> CH2O + C3H7O-4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (79.486, 'kJ/mol', '+|-', 3.974),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."],
        title = u'Photochemical smog. Rate parameter estimates and computer simulations',
        journal = "J. Phys. Chem.",
        volume = "81",
        pages = """2483""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977BAL/BAR2483:8",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00016682
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016682/rk00000001.xml
Uncertainty: 3.1600001
Bath gas: N2
""",
)

entry(
    index = 446,
    label = "C6H5 <=> C2H2 + C4H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.97e+62, 's^-1'),
        n = -14.7,
        Ea = (240.288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1380, 'K'),
        Tmax = (1700, 'K'),
        Pmin = (149000, 'Pa'),
        Pmax = (607000, 'Pa'),
    ),
    reference = Article(
        authors = ["Braun-Unkhoff, M.", "Frank, P.", "Just, Th."],
        title = u'A shock tube study on the thermal decomposition of toluene and of the phenyl radical at high temperatures',
        journal = "Symp. Int. Combust. Proc.",
        volume = "22",
        pages = """1053-1061""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989BRA/FRA1053-1061:12",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00017011
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00017011/rk00000001.xml
Bath gas: Toluene
""",
)

entry(
    index = 447,
    label = "C2H2 + C4H3 <=> C6H5",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.15e+09, 'm^3/(mol*s)'),
        n = -1.51,
        Ea = (20.204, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (400, 'K'),
        Tmax = (1600, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Westmoreland, P.R.", "Dean, A.M.", "Howard, J.B.", "Longwell, J.P."],
        title = u'Forming benzene in flames by chemically activated isomerization',
        journal = "J. Phys. Chem.",
        volume = "93",
        pages = """8171-8180""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989WES/DEA8171-8180:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00017011
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00017011/rk00000002.xml
Bath gas: N2
""",
)

entry(
    index = 448,
    label = "C6H5 <=> C6H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e+58, 's^-1'),
        n = -13.8,
        Ea = (208.693, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1380, 'K'),
        Tmax = (1700, 'K'),
        Pmin = (149000, 'Pa'),
        Pmax = (607000, 'Pa'),
    ),
    reference = Article(
        authors = ["Braun-Unkhoff, M.", "Frank, P.", "Just, Th."],
        title = u'A shock tube study on the thermal decomposition of toluene and of the phenyl radical at high temperatures',
        journal = "Symp. Int. Combust. Proc.",
        volume = "22",
        pages = """1053-1061""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989BRA/FRA1053-1061:13",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00017013
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00017013/rk00000001.xml
Bath gas: Toluene
""",
)

entry(
    index = 449,
    label = "C6H7 <=> C2H2 + C4H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.16e+13, 's^-1'),
        n = 0,
        Ea = (180.424, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Dean, A.M."],
        title = u'Predictions of pressure and temperature effects upon radical addition and recombination reactions',
        journal = "J. Phys. Chem.",
        volume = "89",
        pages = """4600-4608""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:44",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00017118
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00017118/rk00000001.xml
""",
)

entry(
    index = 450,
    label = "C2H2 + C4H5 <=> C6H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.24e+08, 'm^3/(mol*s)'),
        n = -1.38,
        Ea = (16.629, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (400, 'K'),
        Tmax = (1600, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Westmoreland, P.R.", "Dean, A.M.", "Howard, J.B.", "Longwell, J.P."],
        title = u'Forming benzene in flames by chemically activated isomerization',
        journal = "J. Phys. Chem.",
        volume = "93",
        pages = """8171-8180""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989WES/DEA8171-8180:10",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00017118
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00017118/rk00000002.xml
Bath gas: N2
""",
)

entry(
    index = 451,
    label = "C2H4 + C5H11 <=> C7H15",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (12300, 'm^3/(mol*s)'),
        n = 0,
        Ea = (26.939, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (340, 'K'),
        Tmax = (413, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (14700, 'Pa'),
    ),
    reference = Book(
        authors = ["Kerr, J.A.", "Parsonage, M.J."],
        title = u'Evaluated Kinetic Data on Gas Phase Addition Reactions. Reactions of Atoms and Radicals with Alkenes, Alkynes and Aromatic Compounds',
        publisher = "London",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972KER/PARB:9",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002223
""",
)

entry(
    index = 452,
    label = "C2H4 + C5H11 <=> C7H15",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (26.939, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (343, 'K'),
        Tmax = (413, 'K'),
    ),
    reference = Article(
        authors = ["Watkins, K.W.", "O'Deen, L.A."],
        title = u'Kinetics of the addition of ethyl, isopropyl, n-butyl, and isopentyl radicals to ethylene',
        journal = "J. Phys. Chem.",
        volume = "73",
        pages = """4094-4102""",
        year = "1969",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1969WAT/ODE4094-4102:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002223
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002223/rk00000001.xml
Bath gas: (iso-C3H7)-N=N-(iso-C3H7)
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 453,
    label = "C3H6 + C4H9 <=> C7H15-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3070, 'm^3/(mol*s)', '*|/', 10),
        n = 0,
        Ea = (24.611, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Chemical kinetic data base for combustion chemistry. Part V. Propene',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "20",
        pages = """221-273""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:24",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00005635
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00005635/rk00000001.xml
Uncertainty: 10.0
""",
)

entry(
    index = 454,
    label = "C7H15-2 <=> C3H6 + C4H9",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.31e+13, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (111.414, 'kJ/mol', '+|-', 6.66),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (800, 'K'),
        Pmin = (66700, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Baldwin, R.R.", "Walker, R.W.", "Walker, R.W."],
        title = u'Addition of 2,2,3-Trimethylbutane to Slowly Reacting Mixtures of Hydrogen and Oxygen at 480oC',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "77",
        pages = """2157""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981BAL/WAL2157:13",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00005635
Uncertainty: 3.1600001
Bath gas: N2
""",
)

entry(
    index = 455,
    label = "C7H15-3 <=> C6H12-2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.31e+13, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (129.706, 'kJ/mol', '+|-', 6.502),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (800, 'K'),
        Pmin = (66700, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Baldwin, R.R.", "Walker, R.W.", "Walker, R.W."],
        title = u'Addition of 2,2,3-Trimethylbutane to Slowly Reacting Mixtures of Hydrogen and Oxygen at 480oC',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "77",
        pages = """2157""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981BAL/WAL2157:14",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00016148
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016148/rk00000001.xml
Uncertainty: 3.1600001
Bath gas: N2
""",
)

entry(
    index = 456,
    label = "C6H13O <=> C3H6O + C3H7-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+13, 's^-1'),
        n = 0,
        Ea = (40.575, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Choo, K.Y.", "Benson, S.W."],
        title = u'Arrhenius Parameters for the Alkoxy Radical Decomposition Reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """833""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981CHO/BEN833:9",
    ),
    referenceType = "theory",
    shortDesc = u"""Other theoretical""",
    longDesc = 
u"""
PrIMe Reaction: r00016227
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016227/rk00000002.xml
""",
)

entry(
    index = 457,
    label = "C5H11O2 <=> C4H8 + CH3O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.5e+13, 's^-1'),
        n = 0,
        Ea = (116.403, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (653, 'K'),
        Tmax = (793, 'K'),
        Pmin = (66700, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Baldwin, R.R.", "Hisham, M.W.M.", "Walker, R.W."],
        title = u'Arrhenius parameters of elementary reactions involved in the oxidation of neopentane',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "78",
        pages = """1615""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982BAL/HIS1615:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00016870
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016870/rk00000001.xml
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 458,
    label = "C5H11O2 <=> C4H8O2 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.17e+45, 's^-1'),
        n = -11,
        Ea = (148.243, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (900, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Sun, H.", "Bozzelli, J.W."],
        title = u'Thermochemical and kinetic analysis on the reactions of neopentyl and hydroperoxy-neopentyl radicals with oxygen: Part I.  OH and initial stable HC product formation',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """1694-1711""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004SUN/BOZ1694-1711:27",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00016871
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016871/rk00000001.xml

Quantum calculations of energetics of pathways related to reaction between neopentyl radical and O2 (and subsequent reaction pathways). This includes primary reaction pathways as well as subsequent secondary reactions. Used ab initio CBS-Q method, as well as B3LYP/6-31G(d,p) for some molecules. Many reaction channels are discussed in paper, for some, rate expressions are provided at low pressure limit, high pressure limit, and a number of intermediate pressures. For some reaction channels, no rate expressions are given in paper, but are provided in auxillary information associated with the article in JPC.

Rate expressions reported are derived from ab initio transition states using QRRK analysis of the chemically activated reaction pathways. We have only abstracted rate expressions from the paper for 1 atm and 300-900 K. For other pressures and at higher temperatures see paper.
""",
)

entry(
    index = 459,
    label = "C5H11O2 <=> C4H8O2 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.72e+26, 's^-1'),
        n = -5.92,
        Ea = (82.467, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (900, 'K'),
        Tmax = (2500, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Sun, H.", "Bozzelli, J.W."],
        title = u'Thermochemical and kinetic analysis on the reactions of neopentyl and hydroperoxy-neopentyl radicals with oxygen: Part I.  OH and initial stable HC product formation',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """1694-1711""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004SUN/BOZ1694-1711:28",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00016871
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016871/rk00000001.xml

Quantum calculations of energetics of pathways related to reaction between neopentyl radical and O2 (and subsequent reaction pathways). This includes primary reaction pathways as well as subsequent secondary reactions. Used ab initio CBS-Q method, as well as B3LYP/6-31G(d,p) for some molecules. Many reaction channels are discussed in paper, for some, rate expressions are provided at low pressure limit, high pressure limit, and a number of intermediate pressures. For some reaction channels, no rate expressions are given in paper, but are provided in auxillary information associated with the article in JPC.

Rate expressions reported are derived from ab initio transition states using QRRK analysis of the chemically activated reaction pathways. We have only abstracted rate expressions from the paper for 1 atm and 300-900 K. For other pressures and at higher temperatures see paper.
""",
)

entry(
    index = 460,
    label = "C4H8-3 + C3H7-2 <=> C7H15-4",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (63100, 'm^3/(mol*s)', '*|/', 3.2),
        n = 0,
        Ea = (39.494, 'kJ/mol', '+|-', 5.138),
        T0 = (1, 'K'),
        Tmin = (489, 'K'),
        Tmax = (542, 'K'),
    ),
    reference = Article(
        authors = ["Seres, L.", "Fischer, R.", "Scherzer, K.", "Gorgenyl, M."],
        title = u'Thermal reaction of azoisopropane in the presence of (E)-CH3CH = CHCH3: reactions of the radical 2-C3H7',
        journal = "J. Chem. Soc. Faraday Trans.",
        volume = "91",
        pages = """1303-1312""",
        year = "1995",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1995SER/FIS1303-1312:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00008207
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008207/rk00000001.xml
Uncertainty: 3.2
Bath gas: (iso-C3H7)-N=N-(iso-C3H7)
Excitation technique: Thermal
Analytical technique: Gas chromatography
Reference reaction: iso-C3H7 + iso-C3H7 -> (CH3)2CHCH(CH3)2
""",
)

entry(
    index = 461,
    label = "C8H7 <=> C2H2 + C6H5-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.35e+14, 's^-1'),
        n = 0.34,
        Ea = (191.251, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (250, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tokmakov, I.V.", "Lin, M.C."],
        title = u'Reaction of phenyl radicals with acetylene: Quantum chemical investigation of the mechanism and master equation analysis of the kinetics',
        journal = "J. Am. Chem. Soc.",
        volume = "125",
        pages = """11397-11408""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003TOK/LIN11397-11408:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00016107
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016107/rk00000001.xml

Ab initio study of reaction pathways for C6H4 (phenyl) plus C2H2 (acetylene). Used G2M(CC5) method (see paper for details). Calculated many different reaction pathways and intermediates. Only a few of the more important ones are abstracted here. Rate expressions for different pressures for some of the channels are also given in the paper. See paper for further details. Used NIST ChemRate program to calculated rate expressions from ab initio transition states. In paper also provide DfHo heats of formation for many of the intermediates.
""",
)

entry(
    index = 462,
    label = "C8H7 <=> C8H6 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+11, 's^-1'),
        n = 0.82,
        Ea = (162.799, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (250, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tokmakov, I.V.", "Lin, M.C."],
        title = u'Reaction of phenyl radicals with acetylene: Quantum chemical investigation of the mechanism and master equation analysis of the kinetics',
        journal = "J. Am. Chem. Soc.",
        volume = "125",
        pages = """11397-11408""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003TOK/LIN11397-11408:13",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00016108
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016108/rk00000001.xml

Ab initio study of reaction pathways for C6H4 (phenyl) plus C2H2 (acetylene). Used G2M(CC5) method (see paper for details). Calculated many different reaction pathways and intermediates. Only a few of the more important ones are abstracted here. Rate expressions for different pressures for some of the channels are also given in the paper. See paper for further details. Used NIST ChemRate program to calculated rate expressions from ab initio transition states. In paper also provide DfHo heats of formation for many of the intermediates.
""",
)

entry(
    index = 463,
    label = "C7H7O <=> C7H6O + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.27e+14, 's^-1'),
        n = 0,
        Ea = (4.615, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1180, 'K'),
    ),
    reference = Article(
        authors = ["Brezinsky, K.", "Litzinger, T.A.", "Glassman, I."],
        title = u'The high temperature oxidation of the methyl side chain of toluene',
        journal = "Int. J. Chem. Kinet.",
        volume = "16",
        pages = """1053""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984BRE/LIT1053:5",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00016187
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016187/rk00000001.xml
Bath gas: N2
""",
)

entry(
    index = 464,
    label = "C4H8 + C5H11-3 <=> C9H19",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3980, 'm^3/(mol*s)'),
        n = 0,
        Ea = (24.361, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (391, 'K'),
        Tmax = (449, 'K'),
    ),
    reference = Article(
        authors = ["Seres, L.", "Nacsa, A.", "Arthur, N.L."],
        title = u'Thermal decomposition of di-t-butyl peroxide in the presence of (CH3)2C=CH2: reactions of CH3, (CH3)2CCH2CH3, and (CH3)2CCH2C(CH3)2CH2CH3 radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "26",
        pages = """227-246""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994SER/NAC227-246:8",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00005846
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00005846/rk00000001.xml
Bath gas: (tert-C4H9O)2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 465,
    label = "C7H14 + C2H5 <=> C9H19-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (193000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (33.424, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (453, 'K'),
    ),
    reference = Article(
        authors = ["James, D.G.L.", "Steacie, E.W.R."],
        title = u'Reactions of the ethyl radical. II. Addition to unsaturated hydrocarbons',
        journal = "Proc. R. Soc. London A",
        volume = "244",
        pages = """297-311""",
        year = "1958",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1958JAM/STE297-311:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00007920
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007920/rk00000001.xml
Bath gas: (C2H5)2CO
Excitation technique: Direct photolysis
Analytical technique: Mass spectrometry
Note: Invalid activation energy uncertainty (8314.472) found and ignored
""",
)

entry(
    index = 466,
    label = "C6H5-2 + C3H4-3 <=> C9H9",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (0.024, 'm^3/(mol*s)'),
        n = 2.57,
        Ea = (1.38, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Vereecken, L.", "Peeters, J."],
        title = u'Reactions of chemically activated C9H9 species II: The reaction of phenyl radicals with allene and cyclopropene, and of benzyl radicals with acetylene',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "5",
        pages = """2807-2817""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003VER/PEE2807-2817:5",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00011160
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011160/rk00000001.xml

Used quantum calculations to compute many, many possible pathways for reactions of Phenyl + Allene, Phenyl + Cyclopropene, and Benzyl + Acetylene. Used B3LYP/6-311+G(d,p) for geometries/frequencies/PES and CCSD(T) or QCISD(T)/6-311G(d,p) for critical energies. RRKM/Master equation methods to calculate rate expressions. Too complicated to abstract all reaction pathways. Article refers reader to companion article by Vereecken et al, JACS 124, 2781 (2002) for more details. Rate expressions for a number of the major reaction pathways are abstracted here from the paper and supplementary material. For more details, see article and companion article.
""",
)

entry(
    index = 467,
    label = "C3H4 + C6H5-2 <=> C9H9-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (0.0132, 'm^3/(mol*s)'),
        n = 2.64,
        Ea = (15.55, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Vereecken, L.", "Peeters, J."],
        title = u'Reactions of chemically activated C9H9 species II: The reaction of phenyl radicals with allene and cyclopropene, and of benzyl radicals with acetylene',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "5",
        pages = """2807-2817""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003VER/PEE2807-2817:10",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00006975
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00006975/rk00000001.xml

Used quantum calculations to compute many, many possible pathways for reactions of Phenyl + Allene, Phenyl + Cyclopropene, and Benzyl + Acetylene. Used B3LYP/6-311+G(d,p) for geometries/frequencies/PES and CCSD(T) or QCISD(T)/6-311G(d,p) for critical energies. RRKM/Master equation methods to calculate rate expressions. Too complicated to abstract all reaction pathways. Article refers reader to companion article by Vereecken et al, JACS 124, 2781 (2002) for more details. Rate expressions for a number of the major reaction pathways are abstracted here from the paper and supplementary material. For more details, see article and companion article.
""",
)

entry(
    index = 468,
    label = "C3H4 + C6H5-2 <=> C9H9-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (0.0179, 'm^3/(mol*s)'),
        n = 2.53,
        Ea = (11.92, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Vereecken, L.", "Peeters, J."],
        title = u'Reactions of chemically activated C9H9 species II: The reaction of phenyl radicals with allene and cyclopropene, and of benzyl radicals with acetylene',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "5",
        pages = """2807-2817""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003VER/PEE2807-2817:8",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00006976
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00006976/rk00000001.xml

Used quantum calculations to compute many, many possible pathways for reactions of Phenyl + Allene, Phenyl + Cyclopropene, and Benzyl + Acetylene. Used B3LYP/6-311+G(d,p) for geometries/frequencies/PES and CCSD(T) or QCISD(T)/6-311G(d,p) for critical energies. RRKM/Master equation methods to calculate rate expressions. Too complicated to abstract all reaction pathways. Article refers reader to companion article by Vereecken et al, JACS 124, 2781 (2002) for more details. Rate expressions for a number of the major reaction pathways are abstracted here from the paper and supplementary material. For more details, see article and companion article.
""",
)

entry(
    index = 469,
    label = "C10H11 <=> C9H8 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 's^-1'),
        n = 0,
        Ea = (131.796, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Fascella, S.", "Cavallotti, C.", "Rota, R.", "Carra, S."],
        title = u'Quantum chemistry investigation of key reactions involved in the formation of naphthalene and indene',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """3829-3843""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004FAS/CAV3829-3843:13",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00016835
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016835/rk00000001.xml
""",
)

entry(
    index = 470,
    label = "C10H11 <=> C9H8 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.45e+13, 's^-1'),
        n = 0,
        Ea = (117.278, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (1700, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Cavallotti, C.", "Fascella, S.", "Rota, R.", "Carra, S."],
        title = u'A quantum chemistry study of the formation of PAH and soot precursors through butadiene reactions',
        journal = "Combust. Sci. Technol.",
        volume = "176",
        pages = """705-720""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004CAV/FAS705-720:20",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00016835
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016835/rk00000001.xml
Pressure dependence: Rate constant is pressure dependent

Rate expressions derived from density functional theory (DFT) quantum calculations of transition states, and reactants and products. Transition state theory and QRRK methods were used to provide rate expressions bases on the calculated transition states. The geometries and energies of the molecules and transition states were calculated at the B3LYP/6-31G(d,p) level.
""",
)

entry(
    index = 471,
    label = "C9H8 + CH3 <=> C10H11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (200000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (50.626, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Fascella, S.", "Cavallotti, C.", "Rota, R.", "Carra, S."],
        title = u'Quantum chemistry investigation of key reactions involved in the formation of naphthalene and indene',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """3829-3843""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004FAS/CAV3829-3843:14",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00016835
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016835/rk00000001.xml
""",
)

entry(
    index = 472,
    label = "C6H5-2 + C4H6 <=> C10H11-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+40, 'm^3/(mol*s)'),
        n = -10.2,
        Ea = (69.069, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2500, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Fascella, S.", "Cavallotti, C.", "Rota, R.", "Carra, S."],
        title = u'Quantum chemistry investigation of key reactions involved in the formation of naphthalene and indene',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """3829-3843""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004FAS/CAV3829-3843:36",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00011148
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011148/rk00000001.xml

Assuming c10h11-c5, c10h11-c6, and c10h11-1 are STABILIZED products

Rate expressions based on ab inito transition states using G2MP2//B3LYP/6-31G(d,p) method. Also computed B3LYP/6-31G(d,p) energies (not as good). Rate expressions computed using conventional transition state theory or QRRK methods. Treated hindered rotors. All rate expressions abstracted from paper, including those using different assumptions for stabilization of C10H11 intermediates. See paper for more discussion.
""",
)

entry(
    index = 473,
    label = "C10H11-2 <=> C4H6 + C6H5-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.3e+17, 's^-1'),
        n = -1,
        Ea = (204.598, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Fascella, S.", "Cavallotti, C.", "Rota, R.", "Carra, S."],
        title = u'Quantum chemistry investigation of key reactions involved in the formation of naphthalene and indene',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """3829-3843""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004FAS/CAV3829-3843:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00011148
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011148/rk00000004.xml

Rate expressions based on ab inito transition states using G2MP2//B3LYP/6-31G(d,p) method. Also computed B3LYP/6-31G(d,p) energies (not as good). Rate expressions computed using conventional transition state theory or QRRK methods. Treated hindered rotors. All rate expressions abstracted from paper, including those using different assumptions for stabilization of C10H11 intermediates. See paper for more discussion.
""",
)

entry(
    index = 474,
    label = "C10H10 + H <=> C10H11-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.2e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (36.819, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Fascella, S.", "Cavallotti, C.", "Rota, R.", "Carra, S."],
        title = u'Quantum chemistry investigation of key reactions involved in the formation of naphthalene and indene',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """3829-3843""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004FAS/CAV3829-3843:10",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00015756
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015756/rk00000001.xml

Rate expressions based on ab inito transition states using G2MP2//B3LYP/6-31G(d,p) method. Also computed B3LYP/6-31G(d,p) energies (not as good). Rate expressions computed using conventional transition state theory or QRRK methods. Treated hindered rotors. All rate expressions abstracted from paper, including those using different assumptions for stabilization of C10H11 intermediates. See paper for more discussion.
""",
)

entry(
    index = 475,
    label = "C10H11-2 <=> C10H10 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.4e+12, 's^-1'),
        n = 0,
        Ea = (195.811, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Fascella, S.", "Cavallotti, C.", "Rota, R.", "Carra, S."],
        title = u'Quantum chemistry investigation of key reactions involved in the formation of naphthalene and indene',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """3829-3843""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004FAS/CAV3829-3843:9",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00015756
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015756/rk00000002.xml

Rate expressions based on ab inito transition states using G2MP2//B3LYP/6-31G(d,p) method. Also computed B3LYP/6-31G(d,p) energies (not as good). Rate expressions computed using conventional transition state theory or QRRK methods. Treated hindered rotors. All rate expressions abstracted from paper, including those using different assumptions for stabilization of C10H11 intermediates. See paper for more discussion.
""",
)

