#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_ROR/NIST"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "C2H6O <=> C2H4 + H2O",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (8.8e+25, 's^-1'),
        n = -3.68,
        Ea = (296.22, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1045, 'K'),
        Tmax = (1080, 'K'),
        Pmin = (172252, 'Pa'),
        Pmax = (303975, 'Pa'),
    ),
    reference = Article(
        authors = ["Li, J.", "Kazakov, A.", "Dryer, F.L."],
        title = u'Experimental and numerical studies of ethanol decomposition reactions',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """7671-7680""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004LI/KAZ7671-7680:4",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00001601
Pressure dependence: Rate constant is pressure dependent

The authors used a variable pressure flow reactor to study ethanol pyrolysis at 1.7-3.0 atm and 1045-1080 K in the presence of radical chain inhibitor. Rate constants were presented graphically but the numerical results from the experiments were NOT reported.

The authors used their data together with that from the literature to perform a master equation multi-channel RRKM analysis and derive the reported rate constants based on their model.
""",
)

entry(
    index = 2,
    label = "C2H6O <=> C2H4 + H2O",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (2.66e+09, 's^-1'),
        n = 1.25,
        Ea = (263.111, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1045, 'K'),
        Tmax = (1080, 'K'),
        Pmin = (172252, 'Pa'),
        Pmax = (303975, 'Pa'),
    ),
    reference = Article(
        authors = ["Li, J.", "Kazakov, A.", "Dryer, F.L."],
        title = u'Experimental and numerical studies of ethanol decomposition reactions',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """7671-7680""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004LI/KAZ7671-7680:6",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00001601
Pressure dependence: Rate constant is pressure dependent

The authors used a variable pressure flow reactor to study ethanol pyrolysis at 1.7-3.0 atm and 1045-1080 K in the presence of radical chain inhibitor. Rate constants were presented graphically but the numerical results from the experiments were NOT reported.

The authors used their data together with that from the literature to perform a master equation multi-channel RRKM analysis and derive the reported rate constants based on their model.
""",
)

entry(
    index = 3,
    label = "C2H6O <=> C2H4 + H2O",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (132000, 's^-1'),
        n = 2.52,
        Ea = (253.841, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1045, 'K'),
        Tmax = (1080, 'K'),
        Pmin = (172252, 'Pa'),
        Pmax = (303975, 'Pa'),
    ),
    reference = Article(
        authors = ["Li, J.", "Kazakov, A.", "Dryer, F.L."],
        title = u'Experimental and numerical studies of ethanol decomposition reactions',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """7671-7680""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004LI/KAZ7671-7680:7",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00001601
Pressure dependence: Rate constant is high pressure limit

The authors used a variable pressure flow reactor to study ethanol pyrolysis at 1.7-3.0 atm and 1045-1080 K in the presence of radical chain inhibitor. Rate constants were presented graphically but the numerical results from the experiments were NOT reported.

The authors used their data together with that from the literature to perform a master equation multi-channel RRKM analysis and derive the reported rate constants based on their model.
""",
)

entry(
    index = 4,
    label = "C2H6O <=> C2H4 + H2O",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1.41e+16, 's^-1'),
        n = -0.74,
        Ea = (277.055, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1045, 'K'),
        Tmax = (1080, 'K'),
        Pmin = (172252, 'Pa'),
        Pmax = (303975, 'Pa'),
    ),
    reference = Article(
        authors = ["Li, J.", "Kazakov, A.", "Dryer, F.L."],
        title = u'Experimental and numerical studies of ethanol decomposition reactions',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """7671-7680""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004LI/KAZ7671-7680:5",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00001601
Pressure dependence: Rate constant is pressure dependent

The authors used a variable pressure flow reactor to study ethanol pyrolysis at 1.7-3.0 atm and 1045-1080 K in the presence of radical chain inhibitor. Rate constants were presented graphically but the numerical results from the experiments were NOT reported.

The authors used their data together with that from the literature to perform a master equation multi-channel RRKM analysis and derive the reported rate constants based on their model.
""",
)

entry(
    index = 5,
    label = "C2H6O <=> C2H4 + H2O",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (3.77e+43, 's^-1'),
        n = -11.92,
        Ea = (262.13, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1045, 'K'),
        Tmax = (1080, 'K'),
        Pmin = (172252, 'Pa'),
        Pmax = (303975, 'Pa'),
    ),
    reference = Article(
        authors = ["Li, J.", "Kazakov, A.", "Dryer, F.L."],
        title = u'Experimental and numerical studies of ethanol decomposition reactions',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """7671-7680""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004LI/KAZ7671-7680:1",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00001601
Pressure dependence: Rate constant is pressure dependent

The authors used a variable pressure flow reactor to study ethanol pyrolysis at 1.7-3.0 atm and 1045-1080 K in the presence of radical chain inhibitor. Rate constants were presented graphically but the numerical results from the experiments were NOT reported.

The authors used their data together with that from the literature to perform a master equation multi-channel RRKM analysis and derive the reported rate constants based on their model.
""",
)

entry(
    index = 6,
    label = "C2H6O <=> C2H4 + H2O",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1.61e+45, 's^-1'),
        n = -9.69,
        Ea = (325.919, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1045, 'K'),
        Tmax = (1080, 'K'),
        Pmin = (172252, 'Pa'),
        Pmax = (303975, 'Pa'),
    ),
    reference = Article(
        authors = ["Li, J.", "Kazakov, A.", "Dryer, F.L."],
        title = u'Experimental and numerical studies of ethanol decomposition reactions',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """7671-7680""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004LI/KAZ7671-7680:2",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00001601
Pressure dependence: Rate constant is pressure dependent

The authors used a variable pressure flow reactor to study ethanol pyrolysis at 1.7-3.0 atm and 1045-1080 K in the presence of radical chain inhibitor. Rate constants were presented graphically but the numerical results from the experiments were NOT reported.

The authors used their data together with that from the literature to perform a master equation multi-channel RRKM analysis and derive the reported rate constants based on their model.
""",
)

entry(
    index = 7,
    label = "C2H6O <=> C2H4 + H2O",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (4.27e+36, 's^-1'),
        n = -6.95,
        Ea = (314.744, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1045, 'K'),
        Tmax = (1080, 'K'),
        Pmin = (172252, 'Pa'),
        Pmax = (303975, 'Pa'),
    ),
    reference = Article(
        authors = ["Li, J.", "Kazakov, A.", "Dryer, F.L."],
        title = u'Experimental and numerical studies of ethanol decomposition reactions',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """7671-7680""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004LI/KAZ7671-7680:3",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00001601
Pressure dependence: Rate constant is pressure dependent

The authors used a variable pressure flow reactor to study ethanol pyrolysis at 1.7-3.0 atm and 1045-1080 K in the presence of radical chain inhibitor. Rate constants were presented graphically but the numerical results from the experiments were NOT reported.

The authors used their data together with that from the literature to perform a master equation multi-channel RRKM analysis and derive the reported rate constants based on their model.
""",
)

entry(
    index = 8,
    label = "C2H6O <=> C2H4 + H2O",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (4.9e+09, 's^-1'),
        n = 1.36,
        Ea = (275.159, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (800, 'K'),
        Tmax = (1800, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Energy transfer effects during the multichannel decomposition of ethanol',
        journal = "Inter. J. Chem. Kinet.",
        volume = "36",
        pages = """456-465""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004TSA456-465:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00001601
Pressure dependence: Rate constant is high pressure limit

Results are based on a review and analysis of the literature data. The article discusses the multi-channel nature of ethanol decomposition and difficulties associated with expressing the rate constants in a convenient analytical form over extended temperature and pressure ranges.

Some analytical formats for intermediate pressures are also given in the paper but are too complex to reproduce here.
""",
)

entry(
    index = 9,
    label = "C2H6O <=> C2H4 + H2O",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (2.79e+13, 's^-1'),
        n = 0.09,
        Ea = (276.872, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (293, 'K'),
        Tmax = (750, 'K'),
    ),
    reference = Article(
        authors = ["Marinov, N.M."],
        title = u'A detailed chemical kinetic model for high temperature ethanol oxidation',
        journal = "Int. J. Chem. Kinet.",
        volume = "31",
        pages = """183-220""",
        year = "1999",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1999MAR183-220:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00001601
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00001601/rk00000001.xml
""",
)

entry(
    index = 10,
    label = "C2H6O <=> C2H4 + H2O",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (7.67e+14, 's^-1'),
        n = 0,
        Ea = (270.328, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1200, 'K'),
    ),
    reference = Article(
        authors = ["Rajakumar, B.", "Reddy, K.P.J.", "Arunan, E."],
        title = u'Thermal decomposition of 2-fluoroethanol:  Single pulse shock tube and ab initio studies',
        journal = "J. Phys. Chem. A",
        volume = "107",
        pages = """9782-9793""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003RAJ/RED9782-9793:7",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00001601

NOTE This is speculative reaction to explain formation of C2H4. Authors imply that C-OH bond fission channel (with identical rate expression) may be more likely.

Combined experimental and quantum chemical study of the thermal decomposition of 2-Fluoroethanol or CH2F-CH2OH. Measured decomposition of 2-Fluoroethanol in a shock tube at temperatures of 1000-1200 K and pressures of 13-23 atm. Typical concentrations of 500-1000 ppm 2-Fluoroethanol in Argon. Products detected with GC/FID. Quantum calculations using density functional theory (DFT) with B3LYP/6-311++G(d,p) method. Rate expressions from transition state using TST calculations.

Direct measurements from decomposition products of HF and H2O elimination. Possible C-OH bond fission channel measured indirectly by modeling formation of C2H4 from CH2FCH2OH -> CH2FCH2* + OH and CH2FCH2* -> C2H4 + F with the first step rate C-O bond fission rate determining and the second step C-F beta elimination fast. Also proposed another channel to explain C2H4 formation with HOF elimination or CH2FCH2OH -> C2H4 + HOF.  The authors seem to prefer the first C-O bond fission channel, the barrier of about 86 kcal/mol is very similar to the barrier for CH3OH -> CH3 + OH of about 90 kcal/mol. In addition, the authors could find no transition state for elimination of HOF using the quantum calculations.  Proposed HOF elimination channel is by analogy to known HOI elimination channel from CH2ICH2Cl. However, C-F bond is significantly stronger and thus HOF elimination is much less likely.

Good agreement (1 kcal/mol) between experimentally derived barriers for HF and H2O elimination and those from the quantum calculations. Also calculated CH3CH2OH -> C2H4 + H2O and compared with rate expression in literature. In this study, also the enthalpy of formation of 2- Fluoroethanol, not available elsewhere, was predicted using MP2/6-311++G(d,p) energies.

Note that initial CH2=CH2(OH) product from HF elimination channel quickly isomerizes to CH3-CHO.
""",
)

entry(
    index = 11,
    label = "C2H4O2 <=> C2H2O + H2O",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (5.25e+12, 's^-1'),
        n = 0,
        Ea = (295.164, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1300, 'K'),
        Tmax = (1950, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Mackie, J.C.", "Doolan, K.R."],
        title = u'High-temperature kinetics of thermal decomposition of acetic acid and its products',
        journal = "Int. J. Chem. Kinet.",
        volume = "16",
        pages = """525""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984MAC/DOO525:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00001646
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 12,
    label = "C2H4O2 <=> C2H2O + H2O",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.26e+13, 's^-1', '*|/', 2),
        n = 0,
        Ea = (304.31, 'kJ/mol', '+|-', 15.215),
        T0 = (1, 'K'),
        Tmin = (1300, 'K'),
        Tmax = (1950, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Mackie, J.C.", "Doolan, K.R."],
        title = u'High-temperature kinetics of thermal decomposition of acetic acid and its products',
        journal = "Int. J. Chem. Kinet.",
        volume = "16",
        pages = """525""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984MAC/DOO525:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00001646
Uncertainty: 2.0
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 13,
    label = "C2H4O2 <=> C2H2O + H2O",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.82e+12, 's^-1', '*|/', 1.91),
        n = 0,
        Ea = (271.883, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (873, 'K'),
        Tmax = (1040, 'K'),
        Pmin = (933, 'Pa'),
        Pmax = (21300, 'Pa'),
    ),
    reference = Article(
        authors = ["Blake, P.G.", "Jackson, G.E."],
        title = u'High- and low-temperature mechanisms in the thermal decomposition of acetic acid',
        journal = "J. Chem. Soc. B",
        pages = """94-96""",
        year = "1969",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1969BLA/JAC94-96:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00001646
Uncertainty: 1.91
Bath gas: CH3C(O)OH
Excitation technique: Thermal
Analytical technique: Gas chromatography
Note: Invalid activation energy uncertainty (8314.472) found and ignored
""",
)

entry(
    index = 14,
    label = "C2H4O2 <=> C2H2O + H2O",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (8.99e+12, 's^-1'),
        n = 0,
        Ea = (282.692, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (773, 'K'),
        Tmax = (1170, 'K'),
        Pmin = (1200, 'Pa'),
        Pmax = (21100, 'Pa'),
    ),
    reference = Article(
        authors = ["Bamford, C.H.", "Dewar, M.J.S."],
        title = u'608. The thermal decomposition of acetic acid',
        journal = "J. Chem. Soc.",
        pages = """2877-2882""",
        year = "1949",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1949BAM/DEW2877-2882:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00001646
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00001646/rk00000001.xml
Bath gas: CH3C(O)OH
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 15,
    label = "C2H4O2 <=> C2H2O + H2O",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (4.47e+14, 's^-1'),
        n = 0,
        Ea = (334.242, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (990, 'K'),
        Tmax = (1010, 'K'),
    ),
    reference = Article(
        authors = ["Duan, X.", "Page, M."],
        title = u'Theoretical investigation of competing mechanisms in the thermal unimolecular decomposition of acetic acid and the hydration reaction of ketene',
        journal = "J. Am. Chem. Soc.",
        volume = "117",
        pages = """5114-5119""",
        year = "1995",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1995DUA/PAG5114-5119:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00001646
""",
)

entry(
    index = 16,
    label = "C3H8O <=> C3H6 + H2O",
    degeneracy = 24,
    kinetics = Arrhenius(
        A = (1.26e+13, 's^-1', '*|/', 5),
        n = 0,
        Ea = (243.614, 'kJ/mol', '+|-', 14.633),
        T0 = (1, 'K'),
        Tmin = (721, 'K'),
        Tmax = (801, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (13300, 'Pa'),
    ),
    reference = Article(
        authors = ["Trenwith, A.B."],
        title = u'Thermal Decomposition of Isopropanol',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "71",
        pages = """2405""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975TRE2405:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00001741
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00001741/rk00000002.xml
Uncertainty: 5.0
Bath gas: iso-C3H7OH
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 17,
    label = "C3H8O <=> C3H6 + H2O",
    degeneracy = 24,
    kinetics = Arrhenius(
        A = (1.6e+51, 's^-1'),
        n = -11.46,
        Ea = (336.096, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2500, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (6666, 'Pa'),
    ),
    reference = Article(
        authors = ["Bui, B.H.", "Zhu, R.S.", "Lin, M.C."],
        title = u'Thermal Decomposition of Iso-Propanol:  First-Principles Prediction of Total and Product-Branching Rate Constants',
        journal = "J. Chem. Phys.",
        volume = "117",
        pages = """11188-11195""",
        year = "2002",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2002BUI/ZHU11188-11195:6",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00001741
Bath gas: Ar
Pressure dependence: Rate constant is pressure dependent

The authors studied the unimolecular decomposition of iso-C3H7OH with a modified GAUSSIAN-2 method. Six low-lying product channels were identified. Elimination of water via a four-member transition state is dominant below 760 Torr over the temperature range 500?500 K. At higher pressures and over 1200 K, the cleavage of a C-C bond is predicted to be dominant. Rates of C-C bond fission were in reasonable accord with experiments while the water elimination channel was somewhat lower than experiment.

Calculated structures, energetics, and molecular properties of reactant, products, and transition states are provided.
""",
)

entry(
    index = 18,
    label = "C3H8O <=> C3H6 + H2O",
    degeneracy = 24,
    kinetics = Arrhenius(
        A = (6.1e+43, 's^-1'),
        n = -9.13,
        Ea = (325.811, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2500, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Bui, B.H.", "Zhu, R.S.", "Lin, M.C."],
        title = u'Thermal Decomposition of Iso-Propanol:  First-Principles Prediction of Total and Product-Branching Rate Constants',
        journal = "J. Chem. Phys.",
        volume = "117",
        pages = """11188-11195""",
        year = "2002",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2002BUI/ZHU11188-11195:7",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00001741
Bath gas: Ar
Pressure dependence: Rate constant is pressure dependent

The authors studied the unimolecular decomposition of iso-C3H7OH with a modified GAUSSIAN-2 method. Six low-lying product channels were identified. Elimination of water via a four-member transition state is dominant below 760 Torr over the temperature range 500?500 K. At higher pressures and over 1200 K, the cleavage of a C-C bond is predicted to be dominant. Rates of C-C bond fission were in reasonable accord with experiments while the water elimination channel was somewhat lower than experiment.

Calculated structures, energetics, and molecular properties of reactant, products, and transition states are provided.
""",
)

entry(
    index = 19,
    label = "C3H8O <=> C3H6 + H2O",
    degeneracy = 24,
    kinetics = Arrhenius(
        A = (2e+06, 's^-1'),
        n = 2.12,
        Ea = (254.98, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Bui, B.H.", "Zhu, R.S.", "Lin, M.C."],
        title = u'Thermal Decomposition of Iso-Propanol:  First-Principles Prediction of Total and Product-Branching Rate Constants',
        journal = "J. Chem. Phys.",
        volume = "117",
        pages = """11188-11195""",
        year = "2002",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2002BUI/ZHU11188-11195:8",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00001741
Bath gas: Ar
Pressure dependence: Rate constant is high pressure limit

The authors studied the unimolecular decomposition of iso-C3H7OH with a modified GAUSSIAN-2 method. Six low-lying product channels were identified. Elimination of water via a four-member transition state is dominant below 760 Torr over the temperature range 500?500 K. At higher pressures and over 1200 K, the cleavage of a C-C bond is predicted to be dominant. Rates of C-C bond fission were in reasonable accord with experiments while the water elimination channel was somewhat lower than experiment.

Calculated structures, energetics, and molecular properties of reactant, products, and transition states are provided.
""",
)

entry(
    index = 20,
    label = "C4H10O <=> C2H4 + C2H6O-2",
    degeneracy = 24,
    kinetics = Arrhenius(
        A = (1e+13, 's^-1'),
        n = 0,
        Ea = (260.243, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978FOU/MAR132:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00001557
Bath gas: (C2H5)2O
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 21,
    label = "C4H10O <=> C2H4 + C2H6O-2",
    degeneracy = 24,
    kinetics = Arrhenius(
        A = (7.94e+13, 's^-1'),
        n = 0,
        Ea = (276.04, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (783, 'K'),
        Tmax = (823, 'K'),
        Pmin = (13300, 'Pa'),
        Pmax = (40000, 'Pa'),
    ),
    reference = Article(
        authors = ["Seres, I.", "Huhn, P."],
        title = u'A dietil-eter termikus bomlasa, III.',
        journal = "Magy. Kem. Foly.",
        volume = "81",
        pages = """120-123""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975SER/HUH120-123:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00001557
Bath gas: (C2H5)2O
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 22,
    label = "C4H10O <=> C2H4 + C2H6O-2",
    degeneracy = 24,
    kinetics = Arrhenius(
        A = (2.75e+18, 's^-1'),
        n = 0,
        Ea = (350.871, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (833, 'K'),
        Tmax = (913, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (48000, 'Pa'),
    ),
    reference = Article(
        authors = ["Laidler, K.J.", "McKenney, D.J."],
        title = u'Kinetics and mechanisms of the pyrolysis of diethyl ether. II. The reaction inhibited by nitric oxide',
        journal = "Proc. R. Soc. London",
        volume = "278",
        pages = """517-526""",
        year = "1964",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1964LAI/MCK517-526:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00001557
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00001557/rk00000001.xml
Bath gas: (C2H5)2O
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 23,
    label = "C4H10O-2 <=> C4H8 + H2O",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (7.76e+14, 's^-1'),
        n = 0,
        Ea = (275.209, 'kJ/mol', '+|-', 13.802),
        T0 = (1, 'K'),
        Tmin = (1020, 'K'),
        Tmax = (1200, 'K'),
        Pmin = (520000, 'Pa'),
        Pmax = (533000, 'Pa'),
    ),
    reference = Article(
        authors = ["Newman, C.G.", "O'Neal, H.E.", "Ring, M.A.", "Leska, F.", "Shipley, N."],
        title = u'Kinetics and mechanism of the silane decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """1167""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979NEW/ONE1167:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00003587
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 24,
    label = "C4H10O-2 <=> C4H8 + H2O",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (3.98e+14, 's^-1'),
        n = 0,
        Ea = (276.872, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (920, 'K'),
        Tmax = (1180, 'K'),
        Pmin = (49300, 'Pa'),
        Pmax = (208000, 'Pa'),
    ),
    reference = Article(
        authors = ["Lewis, D.", "Keil, M.", "Sarr, M."],
        title = u'Gas Phase Thermal Decomposition of tert-Butyl Alcohol',
        journal = "J. Am. Chem. Soc.",
        volume = "96",
        pages = """4398""",
        year = "1974",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1974LEW/KEI4398:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00003587
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 25,
    label = "C4H10O-2 <=> C4H8 + H2O",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (250000, 's^-1'),
        n = 0,
        Ea = (125.549, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (753, 'K'),
        Tmax = (833, 'K'),
    ),
    reference = Article(
        authors = ["Gonzalez, M.G.", "Lew, L.", "Cunningham, R.E."],
        title = u'Determinacion de la Cinetica de Descomposicion Termica de Alcoholes e Hidrocarburos Mediante un Reactor Pulso',
        journal = "Lab. Ensayo Mater. Invest. Tecnol. Prov. Buenos Aires Publ. Ser. 2",
        pages = """103-123""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971GON/LEW103-123:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00003587
Bath gas: tert-C4H9OH
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 26,
    label = "C4H10O-2 <=> C4H8 + H2O",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (2.24e+13, 's^-1', '*|/', 1.58),
        n = 0,
        Ea = (252.76, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (935, 'K'),
        Tmax = (1400, 'K'),
        Pmin = (13700, 'Pa'),
        Pmax = (34500, 'Pa'),
    ),
    reference = Article(
        authors = ["Dorko, E.A.", "McGhee, D.B.", "Painter, C.E.", "Caponecchi, A.J.", "Crossley, R.W."],
        title = u'Shock Tube Isomerization of Cyclopropane',
        journal = "J. Phys. Chem.",
        volume = "75",
        pages = """2526""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971DOR/MCG2526:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00003587
Uncertainty: 1.58
Bath gas: He
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 27,
    label = "C4H10O-2 <=> C4H8 + H2O",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (2.51e+13, 's^-1'),
        n = 0,
        Ea = (257.749, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1050, 'K'),
        Tmax = (1300, 'K'),
        Pmin = (10700, 'Pa'),
        Pmax = (46700, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Thermal decomposition of some tert-butyl compounds at elevated temperatures',
        journal = "J. Chem. Phys.",
        volume = "40",
        pages = """1498-1505""",
        year = "1964",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1964TSA1498-1505:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00003587
Bath gas: He
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 28,
    label = "C4H10O-2 <=> C4H8 + H2O",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (3.24e+11, 's^-1', '*|/', 2.82),
        n = 0,
        Ea = (227.817, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (760, 'K'),
        Tmax = (893, 'K'),
        Pmin = (5866, 'Pa'),
        Pmax = (41100, 'Pa'),
    ),
    reference = Article(
        authors = ["Barnard, J.A."],
        title = u'The pyrolysis of tert-butanol',
        journal = "Trans. Faraday Soc.",
        volume = "55",
        pages = """947-951""",
        year = "1959",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1959BAR947-951:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00003587
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00003587/rk00000002.xml
Uncertainty: 2.8199999
Bath gas: tert-C4H9OH
Excitation technique: Thermal
Analytical technique: Pressure measurement
Note: Invalid activation energy uncertainty (8314.472) found and ignored
""",
)

entry(
    index = 29,
    label = "C4H8O <=> C4H6 + H2O",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (7.94e+12, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (232.805, 'kJ/mol', '+|-', 6.992),
        T0 = (1, 'K'),
        Tmin = (773, 'K'),
        Tmax = (834, 'K'),
        Pmin = (667, 'Pa'),
        Pmax = (13300, 'Pa'),
    ),
    reference = Article(
        authors = ["Trenwith, A.B."],
        title = u'Dissociation of 3-Hydroxybut-1-ene and the Resonance Energy of the Hydroxyallyl Radical',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "69",
        pages = """1737""",
        year = "1973",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1973TRE1737:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00008094
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008094/rk00000001.xml
Uncertainty: 3.1600001
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 30,
    label = "C4H8O2 <=> C4H6O + H2O",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.24e+12, 's^-1', '*|/', 3.39),
        n = 0,
        Ea = (155.481, 'kJ/mol', '+|-', 4.673),
        T0 = (1, 'K'),
        Tmin = (493, 'K'),
        Tmax = (530, 'K'),
        Pmin = (2800, 'Pa'),
        Pmax = (20300, 'Pa'),
    ),
    reference = Article(
        authors = ["Rotinov, A.", "Chuchani, G.", "Machado, R.A.", "Rivas, C."],
        title = u'The retro-aldol mechanism in the pyrolysis kinetics of primary, secondary, and tertiary \u03b2-hydroxy ketones in the gas phase',
        journal = "Int. J. Chem. Kinet.",
        volume = "24",
        pages = """909-915""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992ROT/CHU909-915:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00007803
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007803/rk00000001.xml
Uncertainty: 3.3900001
Bath gas: Toluene
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 31,
    label = "C5H12O <=> C4H8 + CH4O",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (7.94e+13, 's^-1'),
        n = 0,
        Ea = (246.94, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (761, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (20000, 'Pa'),
    ),
    reference = Article(
        authors = ["Brocard, J.C.", "Baronnet, F."],
        title = u'Effets de parois dans la pyrolyse du methyl tert-butyl ether (MTBE)',
        journal = "J. Chim. Phys. Phys. Chim. Biol.",
        volume = "84",
        pages = """19""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987BRO/BAR19:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009888
Bath gas: tert-C4H9OCH3
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 32,
    label = "C5H12O <=> C4H8 + CH4O",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (1e+14, 's^-1'),
        n = 0,
        Ea = (249.434, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (623, 'K'),
        Tmax = (763, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (26700, 'Pa'),
    ),
    reference = Article(
        authors = ["Brocard, J.C.", "Baronnet, F."],
        title = u'Pyrolysis of methyl tert-butyl ether',
        journal = "Oxid. Commun.",
        volume = "1",
        pages = """321""",
        year = "1980",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1980BRO/BAR321:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009888
Bath gas: tert-C4H9OCH3
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 33,
    label = "C5H12O <=> C4H8 + CH4O",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (7.94e+13, 's^-1'),
        n = 0,
        Ea = (246.94, 'kJ/mol', '+|-', 4.939),
        T0 = (1, 'K'),
        Tmin = (888, 'K'),
        Tmax = (1160, 'K'),
    ),
    reference = Article(
        authors = ["Choo, K-Y.", "Golden, D.M.", "Benson, S.W."],
        title = u'Very Low-Pressure Pyrolysis (VLPP) of t-Butylmethyl Ether',
        journal = "Int. J. Chem. Kinet.",
        volume = "6",
        pages = """631""",
        year = "1974",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1974CHO/GOL631:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009888
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 34,
    label = "C5H12O <=> C4H8 + CH4O",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (2.23e+14, 's^-1'),
        n = 0,
        Ea = (255.254, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (706, 'K'),
        Tmax = (768, 'K'),
    ),
    reference = Article(
        authors = ["Daly, N.J.", "Wentrup, C."],
        title = u'The thermal decomposition of t-butyl methyl ether',
        journal = "Aust. J. Chem.",
        volume = "21",
        pages = """2711-2716""",
        year = "1968",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1968DAL/WEN2711-2716:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009888
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009888/rk00000002.xml
Bath gas: He
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 35,
    label = "C6H14O <=> C3H6 + C3H8O-2",
    degeneracy = 48,
    kinetics = Arrhenius(
        A = (4.17e+14, 's^-1'),
        n = 0,
        Ea = (266.063, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (696, 'K'),
        Tmax = (760, 'K'),
        Pmin = (30800, 'Pa'),
        Pmax = (52300, 'Pa'),
    ),
    reference = Article(
        authors = ["Daly, N.J.", "Stimson, V.R."],
        title = u'The thermal decomposition of diisopropyl ether',
        journal = "Aust. J. Chem.",
        volume = "19",
        pages = """239-250""",
        year = "1966",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1966DAL/STI239-250:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005036
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00005036/rk00000001.xml
Bath gas: (iso-C3H7)2O
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 36,
    label = "C5H12O2 <=> C2H4 + C3H8O2",
    degeneracy = 24,
    kinetics = Arrhenius(
        A = (1.17e+15, 's^-1', '*|/', 2.82),
        n = 0,
        Ea = (286.849, 'kJ/mol', '+|-', 8.647),
        T0 = (1, 'K'),
        Tmin = (1150, 'K'),
        Tmax = (1260, 'K'),
        Pmin = (200000, 'Pa'),
        Pmax = (400000, 'Pa'),
    ),
    reference = Article(
        authors = ["Herzler, J.", "Manion, J.A.", "Tsang, W."],
        title = u'Single-pulse shock tube studies of the decomposition of ethoxy compounds',
        journal = "J. Phys. Chem. A",
        volume = "101",
        pages = """5494-5499""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997HER/MAN5494-5499:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00006952
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00006952/rk00000001.xml
Uncertainty: 2.8199999
Bath gas: CH2(OC2H5)2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 37,
    label = "C6H14O-2 <=> C6H12 + H2O",
    degeneracy = 24,
    kinetics = Arrhenius(
        A = (1.48e+14, 's^-1'),
        n = 0,
        Ea = (268.557, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1080, 'K'),
        Tmax = (1160, 'K'),
        Pmin = (53300, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Thermal Stability of Alcohols',
        journal = "Int. J. Chem. Kinet.",
        volume = "8",
        pages = """173""",
        year = "1976",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976TSA173:9",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00008052
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008052/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 38,
    label = "C6H14O-3 <=> C6H12-2 + H2O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.57e+13, 's^-1'),
        n = 0,
        Ea = (271.883, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1080, 'K'),
        Tmax = (1160, 'K'),
        Pmin = (53300, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Thermal Stability of Alcohols',
        journal = "Int. J. Chem. Kinet.",
        volume = "8",
        pages = """173""",
        year = "1976",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976TSA173:10",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00008053
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008053/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 39,
    label = "C6H14O-4 <=> C4H8 + C2H6O-2",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (1.7e+14, 's^-1'),
        n = 0,
        Ea = (254, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1500, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (912000, 'Pa'),
    ),
    reference = Article(
        authors = ["Yasunaga, K.", "Kuraguchi, Y.", "Hidaka, Y.", "Takahashi, O.", "Yamada, H.", "Koike, T."],
        title = u'Kinetic and modeling studies on ETBE pyrolysis behind reflected shock waves',
        journal = "Chem. Phys. Lett.",
        volume = "451",
        pages = """192-197""",
        year = "2008",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2008YAS/KUR192-197:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00008622
Pressure dependence: Rate constant is high pressure limit
Experimental procedure: Shock tube
Time resolution: In real time
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 40,
    label = "C6H14O-4 <=> C4H8 + C2H6O-2",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (1.15e+14, 's^-1', '*|/', 1.4),
        n = 0,
        Ea = (248.603, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (706, 'K'),
        Tmax = (757, 'K'),
    ),
    reference = Article(
        authors = ["Daly, N.J.", "Wentrup, C."],
        title = u'The thermal decomposition of t-butyl ethyl ether',
        journal = "Aust. J. Chem.",
        volume = "21",
        pages = """1535""",
        year = "1968",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1968DAL/WEN1535:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00008622
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008622/rk00000003.xml
Uncertainty: 1.4
Bath gas: tert-C4H9OC2H5
Excitation technique: Thermal
Analytical technique: Pressure measurement
Note: Invalid activation energy uncertainty (8314.472) found and ignored
""",
)

entry(
    index = 41,
    label = "C6H14O-5 <=> C6H12-3 + H2O",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1e+14, 's^-1'),
        n = 0,
        Ea = (284.355, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1080, 'K'),
        Tmax = (1160, 'K'),
        Pmin = (53300, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Thermal Stability of Alcohols',
        journal = "Int. J. Chem. Kinet.",
        volume = "8",
        pages = """173""",
        year = "1976",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976TSA173:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00007088
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007088/rk00000001.xml
Rate constant is an upper limit.
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 42,
    label = "C7H16O <=> C4H8 + C3H8O-2",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (2.34e+13, 's^-1'),
        n = 0,
        Ea = (231.974, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (683, 'K'),
        Tmax = (748, 'K'),
        Pmin = (2440, 'Pa'),
        Pmax = (3133, 'Pa'),
    ),
    reference = Article(
        authors = ["Daly, N.J.", "Ziolkowski, F.J."],
        title = u'The thermal decomposition of t-butyl isopropyl ether',
        journal = "Aust. J. Chem.",
        volume = "23",
        pages = """541""",
        year = "1970",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1970DAL/ZIO541:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015783
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015783/rk00000001.xml
Bath gas: He
Excitation technique: Thermal
Analytical technique: Gas chromatography
Note: Invalid activation energy uncertainty (8314.472) found and ignored
""",
)

entry(
    index = 43,
    label = "C7H16O-2 <=> C3H6 + C4H10O-3",
    degeneracy = 24,
    kinetics = Arrhenius(
        A = (9.12e+12, 's^-1'),
        n = 0,
        Ea = (236.131, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (683, 'K'),
        Tmax = (748, 'K'),
        Pmin = (2440, 'Pa'),
        Pmax = (3133, 'Pa'),
    ),
    reference = Article(
        authors = ["Daly, N.J.", "Ziolkowski, F.J."],
        title = u'The thermal decomposition of t-butyl isopropyl ether',
        journal = "Aust. J. Chem.",
        volume = "23",
        pages = """541""",
        year = "1970",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1970DAL/ZIO541:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015784
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015784/rk00000001.xml
Bath gas: He
Excitation technique: Thermal
Analytical technique: Gas chromatography
Note: Invalid activation energy uncertainty (8314.472) found and ignored
""",
)

entry(
    index = 44,
    label = "C5H10O3 <=> C3H6 + C2H4O3",
    degeneracy = 24,
    kinetics = Arrhenius(
        A = (1.12e+12, 's^-1', '*|/', 2.29),
        n = 0,
        Ea = (195.39, 'kJ/mol', '+|-', 3.908),
        T0 = (1, 'K'),
        Tmin = (350, 'K'),
        Tmax = (400, 'K'),
        Pmin = (7599, 'Pa'),
        Pmax = (34900, 'Pa'),
    ),
    reference = Article(
        authors = ["Chuchani, G.", "Rotinov, A.", "Dominguez, R.M."],
        title = u'Elimination kinetics and mechanisms for several 2-alkoxyacetic acids in the gas phase',
        journal = "J. Phys. Org. Chem.",
        volume = "9",
        pages = """787-794""",
        year = "1996",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996CHU/ROT787-794:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016319
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016319/rk00000001.xml
Uncertainty: 2.29
Bath gas: Cyclohexene
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 45,
    label = "C8H10O <=> C8H8 + H2O",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.5e+12, 's^-1'),
        n = 0,
        Ea = (229.2, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (722, 'K'),
        Tmax = (764, 'K'),
    ),
    reference = Article(
        authors = ["Chuchani, G.", "Rotinov, A.", "Dominguez, R.M."],
        title = u'The kinetics and mechanisms of gas phase elimination of primary, secondary, and tertiary 2-hydroxyalkylbenzenes',
        journal = "Int. J. Chem. Kinet.",
        volume = "31",
        pages = """401-407""",
        year = "1999",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1999CHU/ROT401-407:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00001556
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00001556/rk00000001.xml
Pressure dependence: None reported
Experimental procedure: Static or low flow - Data taken vs time
Excitation technique: Thermal
Time resolution: By end product analysis
Analytical technique: Gas chromatography

Reactor surface seasoned with allyl bromide.No effect of change in surface to volume by factor of 6.
""",
)

