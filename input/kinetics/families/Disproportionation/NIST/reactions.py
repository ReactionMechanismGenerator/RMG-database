#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/NIST"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "C2H4 + H2 <=> H + C2H5",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.02e+07, 'm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (285.186, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:46",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002190
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002190/rk00000001.xml
Uncertainty: 3.0
""",
)

entry(
    index = 2,
    label = "CH3O + H <=> H2 + CH2O",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (8.55e-15, 'm^3/(mol*s)'),
        n = -0.58,
        Ea = (7.111, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Li, Q.S.", "Zhang, Y.", "Zhang, S.W."],
        title = u'Direct ab initio dynamics study on the rate constants and kinetics isotope effects of CH3O + H -&gt; CH2O + H2 reaction',
        journal = "J. Chem. Phys.",
        volume = "121",
        pages = """9474-9480""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004LI/ZHA9474-9480:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00010601
Pressure dependence: Rate constant is pressure independent

The authors calculated the potential energy surface at several levels of theory, up to UQCISD(T)/aug-cc-pVTZ//UQCISD/cc-pVDZ, and then used canonical variational transition-state theory to calculate the rate constants. At the highest level of theory employed the rate constants are within a factor of about 2.5 of the experimental values, while deviations are much larger (ca 10x at low and high T) at lower levels of theory. The kinetic isotope effect is also calculated.
""",
)

entry(
    index = 3,
    label = "CH2O-2 + HO2 <=> O2 + CH3O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.39e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (79.985, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1200, 'K'),
        Tmax = (1800, 'K'),
        Pmin = (20300, 'Pa'),
        Pmax = (507000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsuboi, T.", "Hashimoto, K."],
        title = u'Shock Tube Study on Homogeneous Thermal Oxidation of Methanol',
        journal = "Combust. Flame",
        volume = "42",
        pages = """61""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981TSU/HAS61:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00001361
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00001361/rk00000001.xml
Bath gas: Ar
""",
)

entry(
    index = 4,
    label = "O2 + CH3O-2 <=> CH2O-2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.03e+09, 'm^3/(mol*s)', '+|-', 1.5e+09),
        n = 0,
        Ea = (14.301, 'kJ/mol', '+|-', 5.862),
        T0 = (1, 'K'),
        Tmin = (215, 'K'),
        Tmax = (250, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (133, 'Pa'),
    ),
    reference = Article(
        authors = ["Nesbitt, F.L.", "Payne, W.A.", "Stief, L.J."],
        title = u'Temperature dependence for the absolute rate constant for the reaction CH2OH + O2 \u2192\x92 HO2 + H2CO from 215 to 300 K',
        journal = "J. Phys. Chem.",
        volume = "92",
        pages = """4030""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988NES/PAY4030:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00001361
Bath gas: He
Excitation technique: Electron beam
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 5,
    label = "O2 + CH3O-2 <=> CH2O-2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.01e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (1.655, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (250, 'K'),
        Tmax = (300, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (133, 'Pa'),
    ),
    reference = Article(
        authors = ["Nesbitt, F.L.", "Payne, W.A.", "Stief, L.J."],
        title = u'Temperature dependence for the absolute rate constant for the reaction CH2OH + O2 \u2192\x92 HO2 + H2CO from 215 to 300 K',
        journal = "J. Phys. Chem.",
        volume = "92",
        pages = """4030""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988NES/PAY4030:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00001361
Bath gas: He
Excitation technique: Electron beam
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 6,
    label = "O2 + CH3O-2 <=> CH2O-2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e-12, 'm^3/(mol*s)'),
        n = 5.94,
        Ea = (-18.957, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (700, 'K'),
        Pmin = (131, 'Pa'),
        Pmax = (259, 'Pa'),
    ),
    reference = Article(
        authors = ["Grotheer, H.", "Riekert, G.", "Walter, D.", "Just, Th."],
        title = u'Non-arrhenius behavior of the reaction of hydroxymethyl radicals with molecular oxygen',
        journal = "J. Phys. Chem.",
        volume = "92",
        pages = """4028""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988GRO/RIE4028:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00001361
Bath gas: He
Excitation technique: Electron beam
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 7,
    label = "O2 + CH3O-2 <=> CH2O-2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+08, 'm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (20.952, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (5333, 'Pa'),
        Pmax = (5333, 'Pa'),
    ),
    reference = Article(
        authors = ["Vandooren, J.", "Van Tiggelen, P.J."],
        title = u'Experimental Investigation of Methanol Oxidation in Flames: Mechanism and Rate Constants of Elementary Steps',
        journal = "Symp. Int. Combust. Proc.",
        volume = "18",
        pages = """473""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981VAN/VAN473:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00001361
Uncertainty: 2.0
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 8,
    label = "O2 + CH3O-2 <=> CH2O-2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+08, 'm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (25.11, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (5333, 'Pa'),
        Pmax = (5333, 'Pa'),
    ),
    reference = Article(
        authors = ["Olsson, J.M.", "Olsson, I.B.M.", "Andersson, L.L."],
        title = u'Lean premixed laminar methanol flames: A computational study',
        journal = "J. Phys. Chem.",
        volume = "91",
        pages = """4160""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987OLS/OLS4160:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00001361
Uncertainty: 5.0
Bath gas: Ar
""",
)

entry(
    index = 9,
    label = "C3H5 + CH3 <=> CH4 + C3H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+06, 'm^3/(mol*s)', '*|/', 3),
        n = -0.32,
        Ea = (-0.549, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:91",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010110
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010110/rk00000001.xml
Uncertainty: 3.0
""",
)

entry(
    index = 10,
    label = "C2H5-2 + C2H5 <=> C2H6 + C2H4",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.65e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (3.342, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (248, 'K'),
        Tmax = (473, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (10700, 'Pa'),
    ),
    reference = Article(
        authors = ["Ivin, K.J.", "Steacie, E.W.R."],
        title = u'The disproportionation and combination of ethyl radicals: The photolysis of mercury diethyl',
        journal = "Proc. R. Soc. London A",
        volume = "208",
        pages = """25""",
        year = "1951",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1951IVI/STE25:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010240
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010240/rk00000001.xml
Bath gas: N2
Excitation technique: Direct photolysis
Analytical technique: Vis-UV absorption
Note: Invalid activation energy uncertainty (8314.472) found and ignored
""",
)

entry(
    index = 11,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47100, 'm^3/(mol*s)', '+|-', 22900),
        n = 0,
        Ea = (9.562, 'kJ/mol', '+|-', 1.58),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (610, 'K'),
    ),
    reference = Article(
        authors = ["Orlando, J.J.", "Tyndall, G.S.", "Wallington, T.J."],
        title = u'The atmospheric chemistry of alkoxy radicals',
        journal = "Chem. Rev.",
        volume = "103",
        pages = """4657-4689""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003ORL/TYN4657-4689:3",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
""",
)

entry(
    index = 12,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (43400, 'm^3/(mol*s)'),
        n = 0,
        Ea = (8.98, 'kJ/mol', '+|-', 2.494),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (610, 'K'),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Crowley, J.N.", "Hampson, R.F, Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."],
        title = u'Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry',
        journal = "Not in System",
        pages = """1-56""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001ATK/BAU1-56:129",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Pressure dependence: None reported
""",
)

entry(
    index = 13,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (23500, 'm^3/(mol*s)'),
        n = 0,
        Ea = (7.483, 'kJ/mol', '+|-', 2.469),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (300, 'K'),
    ),
    reference = Article(
        authors = ["DeMore, W.B.", "Sander, S.P.", "Golden, D.M.", "Hampson, R.F.", "Kurylo, M.J.", "Howard, C.J.", "Ravishankara, A.R.", "Kolb, C.E.", "Molina, M.J."],
        title = u'Chemical kinetics and photochemical data for use in stratospheric modeling. Evaluation number 12',
        journal = "JPL Publication 97-4",
        pages = """1-266""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997DEM/SAN1-266:269",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
""",
)

entry(
    index = 14,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (43400, 'm^3/(mol*s)'),
        n = 0,
        Ea = (8.98, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (610, 'K'),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Hampson, R.F., Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."],
        title = u'Evaluated kinetic, photochemical and heterogeneous data for atmospheric chemistry: supplement V, IUPAC subcommittee on gas kinetic data evaluation for atmospheric chemistry',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "26",
        pages = """521-1011""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997ATK/BAU521-1011:213",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
""",
)

entry(
    index = 15,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (43400, 'm^3/(mol*s)'),
        n = 0,
        Ea = (8.98, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (600, 'K'),
    ),
    reference = Article(
        authors = ["Atkinson, R."],
        title = u'Atmospheric reactions of alkoxy and \u03b2-hydroxyalkoxy radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "29",
        pages = """99-111""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997ATK99-111:1",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
""",
)

entry(
    index = 16,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (23500, 'm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (7.483, 'kJ/mol', '+|-', 2.469),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (300, 'K'),
    ),
    reference = Article(
        authors = ["DeMore, W.B.", "Sander, S.P.", "Golden, D.M.", "Hampson, R.F.", "Kurylo, M.J.", "Howard, C.J.", "Ravishankara, A.R.", "Kolb, C.J.", "Molina, M.J."],
        title = u'Chemical Kinetic and Photochemical Data for Use in Stratospheric Modeling: Evaluation No. 11 of the NASA Panel for Data Evaluation',
        journal = "JPL Publication 94-26",
        pages = """1-2""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994DEM/SAN:251",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Uncertainty: 1.5
""",
)

entry(
    index = 17,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (21700, 'm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (7.317, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Frank, P.", "Hayman, G.", "Just, Th.", "Kerr, J.A.", "Murrells, T.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combusion modelling. Supplement I',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "23",
        pages = """847-1033""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994BAU/COB847-1033:65",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Uncertainty: 2.0
""",
)

entry(
    index = 18,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (36100, 'm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (8.896, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combustion modelling',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """411-429""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992BAU/COB411-429:118",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Uncertainty: 2.0
""",
)

entry(
    index = 19,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (43400, 'm^3/(mol*s)'),
        n = 0,
        Ea = (8.98, 'kJ/mol', '+|-', 2.511),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (610, 'K'),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Hampson Jr., R.F.", "Kerr, J.A.", "Troe, J."],
        title = u'Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry. Supplement IV, IUPAC Subcommittee on Gas Kinetic Data Evaluation for Atmospheric Chemistry',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """1125-1568""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992ATK/BAU1125-1568:181",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
""",
)

entry(
    index = 20,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (43400, 'm^3/(mol*s)', '*|/', 1.58),
        n = 0,
        Ea = (8.98, 'kJ/mol', '+|-', 2.511),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (610, 'K'),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Hampson Jr., R.F.", "Kerr, J.A.", "Troe, J."],
        title = u'Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry: Supplement III',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "18",
        pages = """881-1097""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989ATK/BAU881-1097:108",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Uncertainty: 1.58
""",
)

entry(
    index = 21,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (51300, 'm^3/(mol*s)', '*|/', 1.35),
        n = 0,
        Ea = (10.726, 'kJ/mol', '+|-', 1.073),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (628, 'K'),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:5",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Uncertainty: 1.35
""",
)

entry(
    index = 22,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (66200, 'm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (10.892, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:151",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Uncertainty: 5.0
""",
)

entry(
    index = 23,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+07, 'm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (30.015, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:130",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Uncertainty: 5.0
""",
)

entry(
    index = 24,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (235000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (15.049, 'kJ/mol', '+|-', 4.515),
        T0 = (1, 'K'),
        Tmin = (384, 'K'),
        Tmax = (425, 'K'),
        Pmin = (267, 'Pa'),
        Pmax = (267, 'Pa'),
    ),
    reference = Article(
        authors = ["Ballod, A.P.", "Poroikova, A.I.", "Titarchuk, T.A.", "Khabarov, V.N.488"],
        title = u'Determination of the rate constant of the reaction of methoxyl radicals with molecular oxygen',
        journal = "Kinet. Catal.",
        volume = "30",
        pages = """483-488""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989BAL/POR483-488:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Bath gas: O2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 25,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (63000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (10.892, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (900, 'K'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988ZAS/MUK244:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Chemiluminescence
""",
)

entry(
    index = 26,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (33100, 'm^3/(mol*s)', '+|-', 12000),
        n = 0,
        Ea = (8.314, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (425, 'K'),
        Pmin = (9999, 'Pa'),
        Pmax = (9999, 'Pa'),
    ),
    reference = Article(
        authors = ["Zellner, R."],
        title = u'Recent advances in free radical kinetics of oxygenated hydrocarbon radicals',
        journal = "J. Chim. Phys.",
        volume = "84",
        pages = """403-407""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987ZEL403-407:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Laser induced fluorescence
""",
)

entry(
    index = 27,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.38e-25, 'm^3/(mol*s)', '+|-', 1.13e-25),
        n = (9.5, '', '+|-', 0.67),
        Ea = (-23.031, 'kJ/mol', '+|-', 2.76),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (973, 'K'),
        Pmin = (9999, 'Pa'),
        Pmax = (9999, 'Pa'),
    ),
    reference = Article(
        authors = ["Wantuck, P.J.", "Oldenborg, R.C.", "Baughcum, S.L.", "Winn, K.R."],
        title = u'Removal rate constant measurements for CH3O by O2 over the 298-973 K range',
        journal = "J. Phys. Chem.",
        volume = "91",
        pages = """4653""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987WAN/OLD4653:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Bath gas: Ar
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Laser induced fluorescence
""",
)

entry(
    index = 28,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (33100, 'm^3/(mol*s)', '+|-', 12000),
        n = 0,
        Ea = (8.314, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
        Pmin = (9999, 'Pa'),
        Pmax = (9999, 'Pa'),
    ),
    reference = Article(
        authors = ["Lorenz, K.", "Rhasa, D.", "Zellner, R.", "Fritz, B."],
        title = u'Laser photolysis - LIF kinetic studies of the reactions of CH3O and CH2CHO with O2 between 300 and 500 K',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "89",
        pages = """341""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985LOR/RHA341:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Laser induced fluorescence
""",
)

entry(
    index = 29,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (63000, 'm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (10.892, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (413, 'K'),
        Tmax = (628, 'K'),
        Pmin = (5333, 'Pa'),
        Pmax = (5333, 'Pa'),
    ),
    reference = Article(
        authors = ["Gutman, D.", "Sanders, N.", "Butler, J.E."],
        title = u'Kinetic of the Reactions of Methoxy and Ethoxy Radicals with Oxygen',
        journal = "J. Phys. Chem.",
        volume = "86",
        pages = """66""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982GUT/SAN66:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Uncertainty: 5.0
Bath gas: N2
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Laser induced fluorescence
""",
)

entry(
    index = 30,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (75900, 'm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (11.225, 'kJ/mol', '+|-', 2.81),
        T0 = (1, 'K'),
        Tmin = (296, 'K'),
        Tmax = (450, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Cox, R.A.", "Derwent, R.G.", "Kearsey, S.V.", "Batt, L.", "Partick, K.G."],
        title = u'Photolysis of Methyl Nitrite: Kinetics of the Reaction of the Methoxy Radical with O2',
        journal = "J. Photochem.",
        volume = "13",
        pages = """149""",
        year = "1980",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1980COX/DER149:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Uncertainty: 5.0
Bath gas: O2
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 31,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+06, 'm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (20.121, 'kJ/mol', '+|-', 4.623),
        T0 = (1, 'K'),
        Tmin = (383, 'K'),
        Tmax = (433, 'K'),
        Pmin = (66900, 'Pa'),
        Pmax = (67600, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L.", "Robinson, G.N."],
        title = u'Reaction of Methoxy Radicals with Oxygen. I. Using Dimethyl Peroxide as a Thermal Source of Methoxy Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """1045""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979BAT/ROB1045:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Uncertainty: 5.0
Bath gas: O2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 32,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+06, 'm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (18.791, 'kJ/mol', '+|-', 4.523),
        T0 = (1, 'K'),
        Tmin = (383, 'K'),
        Tmax = (433, 'K'),
        Pmin = (93300, 'Pa'),
        Pmax = (93300, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L.", "Rattray, G.N."],
        title = u'The Reaction of Methoxy Radicals with Nitric Oxide and Nitrogen Dioxide',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """1183""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979BAT/RAT1183:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Uncertainty: 5.0
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 33,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (316000, 'm^3/(mol*s)', '*|/', 3.16),
        n = 0,
        Ea = (16.712, 'kJ/mol', '+|-', 11.723),
        T0 = (1, 'K'),
        Tmin = (396, 'K'),
        Tmax = (442, 'K'),
        Pmin = (93600, 'Pa'),
        Pmax = (93600, 'Pa'),
    ),
    reference = Article(
        authors = ["Barker, J.R.", "Benson, S.W.", "Golden, D.M."],
        title = u'The Decomposition of Dimethyl Peroxide and the Rate Constant for CH3O + O2 \u2192\x92 CH2O +HO2',
        journal = "Int. J. Chem. Kinet.",
        volume = "9",
        pages = """31""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977BAR/BEN31:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010588/rk00000010.xml
Uncertainty: 3.1600001
Bath gas: O2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 34,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.06e+15, 'm^3/(mol*s)'),
        n = 0,
        Ea = (136.357, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (593, 'K'),
        Tmax = (626, 'K'),
        Pmin = (81200, 'Pa'),
        Pmax = (81200, 'Pa'),
    ),
    reference = Article(
        authors = ["Moshkina, R.I.", "Polyak, S.S.", "Sokolova, N.A.", "Masterovoi, I.F.", "Nalbandyan, A.B."],
        title = u'Study of the ethane oxidation reaction by the kinetic tracer method',
        journal = "Int. J. Chem. Kinet.",
        volume = "12",
        pages = """315""",
        year = "1980",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1980MOS/POL315:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010588
Bath gas: O2
""",
)

entry(
    index = 35,
    label = "C2H4-2 + C2H4 <=> C2H3 + C2H5",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (4.82e+08, 'm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (299.321, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:43",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011408
Uncertainty: 5.0
""",
)

entry(
    index = 36,
    label = "C2H4-2 + C2H4 <=> C2H3 + C2H5",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.86e+08, 'm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (268.557, 'kJ/mol', '+|-', 8.057),
        T0 = (1, 'K'),
        Tmin = (748, 'K'),
        Tmax = (819, 'K'),
        Pmin = (13300, 'Pa'),
        Pmax = (40000, 'Pa'),
    ),
    reference = Article(
        authors = ["Ayranci, G.", "Back, M.H."],
        title = u'Kinetics of the reaction: 2C2H4 \u2192\x92 C2H5 + C2H3. Heat of formation of the vinyl radical',
        journal = "Int. J. Chem. Kinet.",
        volume = "15",
        pages = """83-104""",
        year = "1983",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1983AYR/BAC83-104:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011408
Uncertainty: 5.0
Bath gas: C2H4
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 37,
    label = "C2H4-2 + C2H4 <=> C2H3 + C2H5",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.58e+10, 'm^3/(mol*s)'),
        n = 0,
        Ea = (280.198, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (773, 'K'),
        Pmin = (9999, 'Pa'),
        Pmax = (53300, 'Pa'),
    ),
    reference = Article(
        authors = ["Ayranci, G.", "Back, M.H."],
        title = u'Kinetics of the Bimolecular Initiation Process in the Thermal Reactions of Ethylene',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """897""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981AYR/BAC897:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011408
Bath gas: C2H4
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 38,
    label = "C2H4-2 + C2H4 <=> C2H3 + C2H5",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.82e+08, 'm^3/(mol*s)'),
        n = 0,
        Ea = (267.726, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (800, 'K'),
    ),
    reference = Article(
        authors = ["Back, M.H."],
        title = u'Mechanism of the bimolecular reactions of ethylene and propylene',
        journal = "Int. J. Chem. Kinet.",
        volume = "2",
        pages = """409-418""",
        year = "1970",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1970BAC409-418:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011408
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011408/rk00000003.xml
""",
)

entry(
    index = 39,
    label = "O2 + C2H5 <=> C2H4 + HO2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (102000, 'm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (-9.146, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (1200, 'K'),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combustion modelling',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """411-429""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992BAU/COB411-429:209",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00013871
Uncertainty: 2.0
""",
)

entry(
    index = 40,
    label = "O2 + C2H5 <=> C2H4 + HO2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (843000, 'm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (16.213, 'kJ/mol', '+|-', 5.03),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Hampson Jr., R.F.", "Kerr, J.A.", "Troe, J."],
        title = u'Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry: Supplement III',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "18",
        pages = """881-1097""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989ATK/BAU881-1097:221",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00013871
Uncertainty: 2.0
""",
)

entry(
    index = 41,
    label = "O2 + C2H5 <=> C2H4 + HO2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (843000, 'm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (16.213, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:249",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00013871
Uncertainty: 1.5
""",
)

entry(
    index = 42,
    label = "O2 + C2H5 <=> C2H4 + HO2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+06, 'm^3/(mol*s)', '*|/', 3.16),
        n = 0,
        Ea = (20.869, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:187",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00013871
Uncertainty: 3.1600001
""",
)

entry(
    index = 43,
    label = "O2 + C2H5 <=> C2H4 + HO2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.55, 'm^3/(mol*s)', '+|-', 2.3),
        n = 0,
        Ea = (-21.202, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (243, 'K'),
        Tmax = (368, 'K'),
    ),
    reference = Article(
        authors = ["Dobis, O.", "Benson, S.W."],
        title = u'Reaction of the ethyl radical with oxygen at millitorr pressures at 243-368 K and a study of the Cl + HO2, ethyl + HO2, and HO2 + HO2 reactions',
        journal = "J. Am. Chem. Soc.",
        volume = "115",
        pages = """8798-8809""",
        year = "1993",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1993DOB/BEN8798-8809:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00013871
Bath gas: He
Excitation technique: Electron beam
Analytical technique: Mass spectrometry
Note: Invalid activation energy uncertainty (8314.472) found and ignored
""",
)

entry(
    index = 44,
    label = "O2 + C2H5 <=> C2H4 + HO2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.56e+13, 'm^3/(mol*s)'),
        n = -2.77,
        Ea = (8.273, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990BOZ/DEA3313-3317:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00013871
Bath gas: N2
""",
)

entry(
    index = 45,
    label = "O2 + C2H5 <=> C2H4 + HO2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (11200, 'm^3/(mol*s)', '*|/', 1.51),
        n = 0,
        Ea = (-6.302, 'kJ/mol', '+|-', 3.525),
        T0 = (1, 'K'),
        Tmin = (593, 'K'),
        Tmax = (753, 'K'),
        Pmin = (7999, 'Pa'),
        Pmax = (7999, 'Pa'),
    ),
    reference = Article(
        authors = ["McAdam, K.G.", "Walker, R.W."],
        title = u'Arrhenius Parameters for the reaction C2H5 + O2 \u2192\x92 C2H4 + HO2',
        journal = "J. Chem. Soc. Faraday Trans. 2",
        volume = "83",
        pages = """1509""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987MCA/WAL1509:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00013871
Uncertainty: 1.51
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 46,
    label = "O2 + C2H5 <=> C2H4 + HO2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (217000, 'm^3/(mol*s)', '*|/', 1.38),
        n = 0,
        Ea = (5.77, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (713, 'K'),
        Tmax = (896, 'K'),
    ),
    reference = Article(
        authors = ["Baker, R.R.", "Baldwin, R.R.", "Walker, R.W."],
        title = u'The Use of the H2 + O2 Reaction in Determining the Velocity Constants of Elementary Reactions in Hydrocarbon Oxidation',
        journal = "Symp. Int. Combust. Proc.",
        volume = "13",
        pages = """291""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971BAK/BAL291:23",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from detailed balance/reverse rate""",
    longDesc = 
u"""
PrIMe Reaction: r00013871
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013871/rk00000007.xml
Uncertainty: 1.38
""",
)

entry(
    index = 47,
    label = "O2 + C2H5 <=> C2H4 + HO2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.11e+10, 'm^3/(mol*s)'),
        n = -1.87,
        Ea = (5.878, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (296, 'K'),
        Tmax = (700, 'K'),
    ),
    reference = Article(
        authors = ["DeSain, J.D.", "Klippenstein, S.J.", "Miller, J.A.", "Taatjes, C.A."],
        title = u'Measurements, Theory, and Modeling of OH Formation in Ethyl + O2 and Propyl + O2 Reactions',
        journal = "J. Phys. Chem. A",
        volume = "107",
        pages = """4415-4427""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003DES/KLI4415-4427:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00013871
Bath gas: He

Rate constants are based in part on master equation simulations employing transition states from quantum calculations. This work is a combined experimental, theory, and modeling study. Compared OH profiles with those from modeling. Model describes HO2 profiles well, but is not as good for OH profiles.

Static cell (low flow), 296-700 K, He buffer typically 3.65E17 cm-3 (10-20 torr), O2 typically 6.3E15 cm-3. Radicals produced by RH + Cl -> R + HCl, where Cl produced by 193 nm excimer laser photolysis of CCl3F. OH detected using LIF at 281.996 nm.

Employed earlier quantum calculations (see references below) combined with master equation modeling to provide rate expressions for many reactions in this system. Only a few rate expressions are abstracted here.

Miller and Klippenstein, IJCK 33, 654 (2001)
DeSain et al, Farad. Disc. 119, 101 (2001)
""",
)

entry(
    index = 48,
    label = "O2 + C2H5 <=> C2H4 + HO2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (851000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (16.213, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (673, 'K'),
        Tmax = (813, 'K'),
        Pmin = (7999, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Baldwin, R.R.", "Pickering, I.A.", "Walker, R.W."],
        title = u'Reactions of Ethyl Radicals with Oxygen over the Temperature Range 400-540oC',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "76",
        pages = """2374""",
        year = "1980",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1980BAL/PIC2374:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00013871
Bath gas: N2
""",
)

entry(
    index = 49,
    label = "O2 + C2H5 <=> C2H4 + HO2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (20.952, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1400, 'K'),
        Tmax = (1800, 'K'),
        Pmin = (26700, 'Pa'),
        Pmax = (40000, 'Pa'),
    ),
    reference = Article(
        authors = ["Cooke, D.F.", "Williams, A."],
        title = u'Shock-tube studies of the ignition and combustion of ethane and slightly rich methane mixtures with oxygen',
        journal = "Symp. Int. Combust. Proc.",
        volume = "13",
        pages = """757""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971COO/WIL757:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00013871
Bath gas: Ar
""",
)

entry(
    index = 50,
    label = "OH + C2H3O <=> H2O + C2H2O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.21e+07, 'm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (0, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:209",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00017303
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00017303/rk00000001.xml
Uncertainty: 3.0
""",
)

entry(
    index = 51,
    label = "C4H9 + CH3 <=> CH4 + C4H8",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (1.26e+07, 'm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (-2.494, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:73",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00009800
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009800/rk00000004.xml
Uncertainty: 2.0
""",
)

entry(
    index = 52,
    label = "C3H5 + C2H5-2 <=> C2H6 + C3H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (964000, 'm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (-0.549, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:111",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010098
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010098/rk00000003.xml
Uncertainty: 2.0
""",
)

entry(
    index = 53,
    label = "C2H6 + C3H4 <=> C3H5 + C2H5-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.35e+08, 'm^3/(mol*s)', '+|-', 3.7e+07),
        n = 0,
        Ea = (164.627, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1070, 'K'),
        Tmax = (1130, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Korzun, N.V.", "Trushkova, L.V."],
        title = u'Kinetic parameters of the reaction C2H6 + C3H4 \u2192\x92 C2H5 + C3H5',
        journal = "Kinet. Catal.",
        volume = "26",
        pages = """1068""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985KOR/TRU1068:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010098
Bath gas: He
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 54,
    label = "C3H5-2 + C2H5 <=> C3H6 + C2H4",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.59e+06, 'm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (-0.549, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:112",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010099
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010099/rk00000004.xml
Uncertainty: 2.0
""",
)

entry(
    index = 55,
    label = "C3H6 + C2H4 <=> C3H5-2 + C2H5",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (5.78e+07, 'm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (216.176, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:6",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010099
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010099/rk00000004.xml
Uncertainty: 3.0
""",
)

entry(
    index = 56,
    label = "C3H6 + C2H4 <=> C3H5-2 + C2H5",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1e+08, 'm^3/(mol*s)'),
        n = 0,
        Ea = (206.199, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (800, 'K'),
    ),
    reference = Article(
        authors = ["Back, M.H."],
        title = u'Mechanism of the bimolecular reactions of ethylene and propylene',
        journal = "Int. J. Chem. Kinet.",
        volume = "2",
        pages = """409-418""",
        year = "1970",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1970BAC409-418:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010099
""",
)

entry(
    index = 57,
    label = "C3H5 + O2 <=> HO2 + C3H4",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (0.0206, 'm^3/(mol*s)'),
        n = 2.19,
        Ea = (73.597, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Lee, J.", "Bozzelli, J.W."],
        title = u'Thermochemical and kinetic analysis of the allyl radical with O2 reaction system',
        journal = "Proc. Combust. Inst.",
        volume = "30",
        pages = """1015-1022""",
        year = "2005",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2005LEE/BOZ1015-1022:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00010133

Reaction potential energy surface was studied using quantum chemistry, product pathways were analyzed, and rate constants were calculated using QRRK / master equation method. Rate constants were calculated for a wide range of temperatures; Arrhenius expressions for the pressure of 1 atm are given in a table in the Supplementary Data (online).
""",
)

entry(
    index = 58,
    label = "C2H4-2 + C3H6-2 <=> C2H3 + C3H7",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.22e+09, 'm^3/(mol*s)', '*|/', 3),
        n = -0.65,
        Ea = (308.467, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:7",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010195
Uncertainty: 3.0
""",
)

entry(
    index = 59,
    label = "C2H4-2 + C3H6-2 <=> C2H3 + C3H7",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (9.12e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (264.4, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (800, 'K'),
    ),
    reference = Article(
        authors = ["Back, M.H."],
        title = u'Mechanism of the bimolecular reactions of ethylene and propylene',
        journal = "Int. J. Chem. Kinet.",
        volume = "2",
        pages = """409-418""",
        year = "1970",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1970BAC409-418:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010195
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010195/rk00000004.xml
""",
)

entry(
    index = 60,
    label = "C3H7 + O2 <=> HO2 + C3H6-2",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1e+06, 'm^3/(mol*s)', '*|/', 3.16),
        n = 0,
        Ea = (12.472, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:120",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010209
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010209/rk00000003.xml
Uncertainty: 3.1600001
""",
)

entry(
    index = 61,
    label = "C3H7 + O2 <=> HO2 + C3H6-2",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (27500, 'm^3/(mol*s)', '*|/', 1.78),
        n = 0,
        Ea = (-8.98, 'kJ/mol', '+|-', 5.039),
        T0 = (1, 'K'),
        Tmin = (653, 'K'),
        Tmax = (773, 'K'),
        Pmin = (4800, 'Pa'),
        Pmax = (5733, 'Pa'),
    ),
    reference = Article(
        authors = ["Gulati, S.K.", "Walker, R.W."],
        title = u'Arrhenius parameters for the reaction i-C3H7 + O2 \u2192\x92 C3H6 + HO2',
        journal = "J. Chem. Soc. Faraday Trans. 2",
        volume = "84",
        pages = """401""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988GUL/WAL401:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010209
Uncertainty: 1.78
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 62,
    label = "C3H7 + O2 <=> HO2 + C3H6-2",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (6.7e+14, 'm^3/(mol*s)'),
        n = -3.02,
        Ea = (10.476, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (296, 'K'),
        Tmax = (700, 'K'),
    ),
    reference = Article(
        authors = ["DeSain, J.D.", "Klippenstein, S.J.", "Miller, J.A.", "Taatjes, C.A."],
        title = u'Measurements, Theory, and Modeling of OH Formation in Ethyl + O2 and Propyl + O2 Reactions',
        journal = "J. Phys. Chem. A",
        volume = "107",
        pages = """4415-4427""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003DES/KLI4415-4427:5",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00010209
Bath gas: He

Rate constants are based in part on master equation simulations employing transition states from quantum calculations. This work is a combined experimental, theory, and modeling study. Compared OH profiles with those from modeling. Model describes HO2 profiles well, but is not as good for OH profiles.

Static cell (low flow), 296-700 K, He buffer typically 3.65E17 cm-3 (10-20 torr), O2 typically 6.3E15 cm-3. Radicals produced by RH + Cl -> R + HCl, where Cl produced by 193 nm excimer laser photolysis of CCl3F. OH detected using LIF at 281.996 nm.

Employed earlier quantum calculations (see references below) combined with master equation modeling to provide rate expressions for many reactions in this system. Only a few rate expressions are abstracted here.

Miller and Klippenstein, IJCK 33, 654 (2001)
DeSain et al, Farad. Disc. 119, 101 (2001)
""",
)

entry(
    index = 63,
    label = "C2H4-2 + C3H6-3 <=> C2H3 + C3H7-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.03e+07, 'm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (315.95, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:8",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010524
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010524/rk00000002.xml
Uncertainty: 3.0
""",
)

entry(
    index = 64,
    label = "C3H7-2 + O2 <=> HO2 + C3H6-3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1e+06, 'm^3/(mol*s)', '*|/', 3.16),
        n = 0,
        Ea = (21.036, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:127",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010543
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010543/rk00000007.xml
Uncertainty: 3.1600001
""",
)

entry(
    index = 65,
    label = "C3H7-2 + O2 <=> HO2 + C3H6-3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.7e+10, 'm^3/(mol*s)'),
        n = -1.63,
        Ea = (14.301, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (296, 'K'),
        Tmax = (700, 'K'),
    ),
    reference = Article(
        authors = ["DeSain, J.D.", "Klippenstein, S.J.", "Miller, J.A.", "Taatjes, C.A."],
        title = u'Measurements, Theory, and Modeling of OH Formation in Ethyl + O2 and Propyl + O2 Reactions',
        journal = "J. Phys. Chem. A",
        volume = "107",
        pages = """4415-4427""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003DES/KLI4415-4427:8",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00010543
Bath gas: He

Rate constants are based in part on master equation simulations employing transition states from quantum calculations. This work is a combined experimental, theory, and modeling study. Compared OH profiles with those from modeling. Model describes HO2 profiles well, but is not as good for OH profiles.

Static cell (low flow), 296-700 K, He buffer typically 3.65E17 cm-3 (10-20 torr), O2 typically 6.3E15 cm-3. Radicals produced by RH + Cl -> R + HCl, where Cl produced by 193 nm excimer laser photolysis of CCl3F. OH detected using LIF at 281.996 nm.

Employed earlier quantum calculations (see references below) combined with master equation modeling to provide rate expressions for many reactions in this system. Only a few rate expressions are abstracted here.

Miller and Klippenstein, IJCK 33, 654 (2001)
DeSain et al, Farad. Disc. 119, 101 (2001)
""",
)

entry(
    index = 66,
    label = "C2H5O + O2 <=> HO2 + C2H4O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (36100, 'm^3/(mol*s)'),
        n = 0,
        Ea = (4.573, 'kJ/mol', '+|-', 2.494),
        T0 = (1, 'K'),
        Tmin = (295, 'K'),
        Tmax = (425, 'K'),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Crowley, J.N.", "Hampson, R.F, Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."],
        title = u'Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry',
        journal = "Not in System",
        pages = """1-56""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001ATK/BAU1-56:130",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010641
Pressure dependence: None reported
""",
)

entry(
    index = 67,
    label = "C2H5O + O2 <=> HO2 + C2H4O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (37900, 'm^3/(mol*s)'),
        n = 0,
        Ea = (4.573, 'kJ/mol', '+|-', 1.646),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (300, 'K'),
    ),
    reference = Article(
        authors = ["DeMore, W.B.", "Sander, S.P.", "Golden, D.M.", "Hampson, R.F.", "Kurylo, M.J.", "Howard, C.J.", "Ravishankara, A.R.", "Kolb, C.E.", "Molina, M.J."],
        title = u'Chemical kinetics and photochemical data for use in stratospheric modeling. Evaluation number 12',
        journal = "JPL Publication 97-4",
        pages = """1-266""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997DEM/SAN1-266:275",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010641
""",
)

entry(
    index = 68,
    label = "C2H5O + O2 <=> HO2 + C2H4O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (36100, 'm^3/(mol*s)'),
        n = 0,
        Ea = (4.573, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (295, 'K'),
        Tmax = (425, 'K'),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Hampson, R.F., Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."],
        title = u'Evaluated kinetic, photochemical and heterogeneous data for atmospheric chemistry: supplement V, IUPAC subcommittee on gas kinetic data evaluation for atmospheric chemistry',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "26",
        pages = """521-1011""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997ATK/BAU521-1011:219",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010641
""",
)

entry(
    index = 69,
    label = "C2H5O + O2 <=> HO2 + C2H4O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (36100, 'm^3/(mol*s)'),
        n = 0,
        Ea = (4.573, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (600, 'K'),
    ),
    reference = Article(
        authors = ["Atkinson, R."],
        title = u'Atmospheric reactions of alkoxy and \u03b2-hydroxyalkoxy radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "29",
        pages = """99-111""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997ATK99-111:2",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010641
""",
)

entry(
    index = 70,
    label = "C2H5O + O2 <=> HO2 + C2H4O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (37900, 'm^3/(mol*s)', '*|/', 1.5),
        n = 0,
        Ea = (4.573, 'kJ/mol', '+|-', 1.646),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (300, 'K'),
    ),
    reference = Article(
        authors = ["DeMore, W.B.", "Sander, S.P.", "Golden, D.M.", "Hampson, R.F.", "Kurylo, M.J.", "Howard, C.J.", "Ravishankara, A.R.", "Kolb, C.J.", "Molina, M.J."],
        title = u'Chemical Kinetic and Photochemical Data for Use in Stratospheric Modeling: Evaluation No. 11 of the NASA Panel for Data Evaluation',
        journal = "JPL Publication 94-26",
        pages = """1-2""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994DEM/SAN:257",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010641
Uncertainty: 1.5
""",
)

entry(
    index = 71,
    label = "C2H5O + O2 <=> HO2 + C2H4O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (60300, 'm^3/(mol*s)', '*|/', 3.16),
        n = 0,
        Ea = (6.901, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combustion modelling',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """411-429""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992BAU/COB411-429:123",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010641
Uncertainty: 3.1600001
""",
)

entry(
    index = 72,
    label = "C2H5O + O2 <=> HO2 + C2H4O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (36100, 'm^3/(mol*s)'),
        n = 0,
        Ea = (4.573, 'kJ/mol', '+|-', 2.519),
        T0 = (1, 'K'),
        Tmin = (295, 'K'),
        Tmax = (425, 'K'),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Hampson Jr., R.F.", "Kerr, J.A.", "Troe, J."],
        title = u'Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry. Supplement IV, IUPAC Subcommittee on Gas Kinetic Data Evaluation for Atmospheric Chemistry',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """1125-1568""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992ATK/BAU1125-1568:187",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010641
""",
)

entry(
    index = 73,
    label = "C2H5O + O2 <=> HO2 + C2H4O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (97700, 'm^3/(mol*s)', '*|/', 1.55),
        n = 0,
        Ea = (6.652, 'kJ/mol', '+|-', 1.064),
        T0 = (1, 'K'),
        Tmin = (225, 'K'),
        Tmax = (425, 'K'),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:11",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010641
Uncertainty: 1.55
""",
)

entry(
    index = 74,
    label = "C2H5O + O2 <=> HO2 + C2H4O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (42800, 'm^3/(mol*s)', '+|-', 4300),
        n = 0,
        Ea = (4.59, 'kJ/mol', '+|-', 0.55),
        T0 = (1, 'K'),
        Tmin = (295, 'K'),
        Tmax = (411, 'K'),
        Pmin = (3453, 'Pa'),
        Pmax = (3453, 'Pa'),
    ),
    reference = Article(
        authors = ["Hartmann, D.", "Karthauser, J.", "Sawerysyn, J.P.", "Zellner, R."],
        title = u'Kinetics and HO2 product yield of the reaction C2H5O + O2 between 295 and 411 K',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "94",
        pages = """639-645""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990HAR/KAR639-645:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010641
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Laser induced fluorescence
""",
)

entry(
    index = 75,
    label = "C2H5O + O2 <=> HO2 + C2H4O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (181000, 'm^3/(mol*s)', '+|-', 60000),
        n = 0,
        Ea = (7.683, 'kJ/mol', '+|-', 0.768),
        T0 = (1, 'K'),
        Tmin = (225, 'K'),
        Tmax = (393, 'K'),
        Pmin = (533, 'Pa'),
        Pmax = (48100, 'Pa'),
    ),
    reference = Article(
        authors = ["Zabarnick, S.", "Heicklen, J."],
        title = u'Reactions of alkoxy radicals with O2. I. C2H5O radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "17",
        pages = """455""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985ZAB/HEI455:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010641
Bath gas: N2
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 76,
    label = "C2H5O + O2 <=> HO2 + C2H4O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (17200, 'm^3/(mol*s)'),
        n = 0,
        Ea = (3.143, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (296, 'K'),
        Tmax = (353, 'K'),
        Pmin = (5333, 'Pa'),
        Pmax = (5333, 'Pa'),
    ),
    reference = Article(
        authors = ["Gutman, D.", "Sanders, N.", "Butler, J.E."],
        title = u'Kinetic of the Reactions of Methoxy and Ethoxy Radicals with Oxygen',
        journal = "J. Phys. Chem.",
        volume = "86",
        pages = """66""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982GUT/SAN66:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010641
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010641/rk00000002.xml
Bath gas: N2
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Laser induced fluorescence
""",
)

entry(
    index = 77,
    label = "C2H5O-2 + O2 <=> HO2 + C2H4O-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (23.281, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1300, 'K'),
        Tmax = (1700, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (203000, 'Pa'),
    ),
    reference = Article(
        authors = ["Natarajan, K.", "Bhaskaran, K.A."],
        title = u'An Experimental and Analytical Investigation of High Temperature Ignition of Ethanol',
        journal = "Proc. Int. Symp. Shock Tubes Waves",
        volume = "13",
        pages = """834""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982NAT/BHA834:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011080
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011080/rk00000001.xml
Bath gas: Ar
""",
)

entry(
    index = 78,
    label = "C3H5 + O2 <=> HO2 + C3H4",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.21e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (56.705, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:108",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010133
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010133/rk00000002.xml
Rate constant is an upper limit.
""",
)

entry(
    index = 79,
    label = "C4H9 + O2 <=> HO2 + C4H8",
    degeneracy = 18,
    kinetics = Arrhenius(
        A = (800000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (9.063, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (713, 'K'),
        Tmax = (813, 'K'),
        Pmin = (66700, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Evans, G.A.", "Walker, R.W."],
        title = u'Reaction of t-Butyl Radicals with Hydrogen and with Oxygen',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "75",
        pages = """1458""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979EVA/WAL1458:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00009826
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009826/rk00000002.xml
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
Note: Invalid activation energy uncertainty (9.977) found and ignored
""",
)

entry(
    index = 80,
    label = "C3H5-2 + C3H5 <=> C3H6 + C3H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (84300, 'm^3/(mol*s)', '*|/', 2.5),
        n = 0,
        Ea = (-1.098, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:78",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010092
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010092/rk00000002.xml
Uncertainty: 2.5
""",
)

entry(
    index = 81,
    label = "C3H5-2 + C3H5 <=> C3H6 + C3H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (33900, 'm^3/(mol*s)'),
        n = 0,
        Ea = (39.327, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996BAR/MAR829-847:8",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010092
Bath gas: CH3CH=CH2
""",
)

entry(
    index = 82,
    label = "C3H5 + C3H7-3 <=> C3H8 + C3H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.58e+06, 'm^3/(mol*s)', '*|/', 3),
        n = -0.35,
        Ea = (-0.549, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:80",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010094
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010094/rk00000001.xml
Uncertainty: 3.0
""",
)

entry(
    index = 83,
    label = "C3H5-2 + C3H7 <=> C3H6 + C3H6-2",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.29e+07, 'm^3/(mol*s)', '*|/', 3),
        n = -0.35,
        Ea = (-0.549, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:81",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010095
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010095/rk00000002.xml
Uncertainty: 3.0
""",
)

entry(
    index = 84,
    label = "C3H5-2 + C3H7 <=> C3H6 + C3H6-2",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (501000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (19.622, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996BAR/MAR829-847:9",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010095
Bath gas: CH3CH=CH2
""",
)

entry(
    index = 85,
    label = "C3H6 + C3H6-2 <=> C3H5-2 + C3H7",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (4.88e+07, 'm^3/(mol*s)', '*|/', 2.5),
        n = 0,
        Ea = (218.671, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:21",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010095
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010095/rk00000002.xml
Uncertainty: 2.5
""",
)

entry(
    index = 86,
    label = "C3H6 + C3H6-2 <=> C3H5-2 + C3H7",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.51e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (182.087, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (743, 'K'),
        Tmax = (803, 'K'),
        Pmin = (667, 'Pa'),
        Pmax = (5333, 'Pa'),
    ),
    reference = Article(
        authors = ["Simon, M.", "Back, M.H."],
        title = u'The Kinetics of the Reaction 2C3H6 \u2192\x92 C3H5 + C3H7',
        journal = "Can. J. Chem.",
        volume = "51",
        pages = """2934""",
        year = "1973",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1973SIM/BAC2934:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010095
Bath gas: CH3CH=CH2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 87,
    label = "C3H6 + C3H6-2 <=> C3H5-2 + C3H7",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.57e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (236.962, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996BAR/MAR829-847:5",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010095
Bath gas: CH3CH=CH2
""",
)

entry(
    index = 88,
    label = "C3H6 + C3H6-2 <=> C3H5-2 + C3H7",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1.32e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (202.873, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (800, 'K'),
    ),
    reference = Article(
        authors = ["Back, M.H."],
        title = u'Mechanism of the bimolecular reactions of ethylene and propylene',
        journal = "Int. J. Chem. Kinet.",
        volume = "2",
        pages = """409-418""",
        year = "1970",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1970BAC409-418:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010095
""",
)

entry(
    index = 89,
    label = "C3H5 + C3H7-4 <=> C3H8-2 + C3H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (723000, 'm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (-0.549, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:87",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010105
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010105/rk00000001.xml
Uncertainty: 3.0
""",
)

entry(
    index = 90,
    label = "C3H5-2 + C3H7-2 <=> C3H6 + C3H6-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.45e+06, 'm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (-0.549, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:88",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010106
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010106/rk00000001.xml
Uncertainty: 3.0
""",
)

entry(
    index = 91,
    label = "C3H5-2 + C3H7-2 <=> C3H6 + C3H6-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (275000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (19.622, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996BAR/MAR829-847:10",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010106
Bath gas: CH3CH=CH2
""",
)

entry(
    index = 92,
    label = "C3H6 + C3H6-3 <=> C3H5-2 + C3H7-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.53e+08, 'm^3/(mol*s)', '*|/', 2.5),
        n = 0,
        Ea = (231.142, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:22",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010106
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010106/rk00000001.xml
Uncertainty: 2.5
""",
)

entry(
    index = 93,
    label = "C3H6 + C3H6-3 <=> C3H5-2 + C3H7-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.89e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (249.434, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996BAR/MAR829-847:6",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010106
Bath gas: CH3CH=CH2
""",
)

entry(
    index = 94,
    label = "C3H7O + O2 <=> HO2 + C3H6O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8430, 'm^3/(mol*s)'),
        n = 0,
        Ea = (1.746, 'kJ/mol', '+|-', 1.663),
        T0 = (1, 'K'),
        Tmin = (210, 'K'),
        Tmax = (390, 'K'),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Crowley, J.N.", "Hampson, R.F, Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."],
        title = u'Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry',
        journal = "Not in System",
        pages = """1-56""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001ATK/BAU1-56:132",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012573
Pressure dependence: None reported
""",
)

entry(
    index = 95,
    label = "C3H7O + O2 <=> HO2 + C3H6O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9040, 'm^3/(mol*s)'),
        n = 0,
        Ea = (1.663, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (290, 'K'),
        Tmax = (390, 'K'),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Hampson, R.F., Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."],
        title = u'Evaluated kinetic, photochemical and heterogeneous data for atmospheric chemistry: supplement V, IUPAC subcommittee on gas kinetic data evaluation for atmospheric chemistry',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "26",
        pages = """521-1011""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997ATK/BAU521-1011:289",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012573
""",
)

entry(
    index = 96,
    label = "C3H7O + O2 <=> HO2 + C3H6O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9040, 'm^3/(mol*s)'),
        n = 0,
        Ea = (1.663, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (600, 'K'),
    ),
    reference = Article(
        authors = ["Atkinson, R."],
        title = u'Atmospheric reactions of alkoxy and \u03b2-hydroxyalkoxy radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "29",
        pages = """99-111""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997ATK99-111:3",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012573
""",
)

entry(
    index = 97,
    label = "C3H7O + O2 <=> HO2 + C3H6O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9040, 'm^3/(mol*s)'),
        n = 0,
        Ea = (1.663, 'kJ/mol', '+|-', 1.663),
        T0 = (1, 'K'),
        Tmin = (290, 'K'),
        Tmax = (390, 'K'),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Hampson Jr., R.F.", "Kerr, J.A.", "Troe, J."],
        title = u'Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry. Supplement IV, IUPAC Subcommittee on Gas Kinetic Data Evaluation for Atmospheric Chemistry',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """1125-1568""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992ATK/BAU1125-1568:275",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012573
""",
)

entry(
    index = 98,
    label = "C3H7O + O2 <=> HO2 + C3H6O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9040, 'm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (1.663, 'kJ/mol', '+|-', 1.663),
        T0 = (1, 'K'),
        Tmin = (290, 'K'),
        Tmax = (390, 'K'),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Hampson Jr., R.F.", "Kerr, J.A.", "Troe, J."],
        title = u'Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry: Supplement III',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "18",
        pages = """881-1097""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989ATK/BAU881-1097:193",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012573
Uncertainty: 2.0
""",
)

entry(
    index = 99,
    label = "C3H7O + O2 <=> HO2 + C3H6O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (49000, 'm^3/(mol*s)', '*|/', 1.55),
        n = 0,
        Ea = (6.652, 'kJ/mol', '+|-', 1.064),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (383, 'K'),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:17",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00012573
Uncertainty: 1.55
""",
)

entry(
    index = 100,
    label = "C3H7O + O2 <=> HO2 + C3H6O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9100, 'm^3/(mol*s)', '+|-', 4200),
        n = 0,
        Ea = (1.63, 'kJ/mol', '+|-', 1.172),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (383, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (6666, 'Pa'),
    ),
    reference = Article(
        authors = ["Balla, R.J.", "Nelson, H.H.", "McDonald, J.R."],
        title = u'Kinetics of the reactions of isopropoxy radicals with NO, NO2, and O2',
        journal = "Chem. Phys.",
        volume = "99",
        pages = """323""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985BAL/NEL323:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00012573
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012573/rk00000001.xml
Bath gas: N2
Excitation technique: Direct photolysis
Analytical technique: Laser induced fluorescence
""",
)

entry(
    index = 101,
    label = "C4H9-2 + O2 <=> HO2 + C4H8-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.7e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (26.606, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (313, 'K'),
        Tmax = (753, 'K'),
        Pmin = (66700, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Baker, R.R.", "Baldwin, R.R.", "Walker, R.W."],
        title = u'Addition of i-Butane to Slowly Reacting Mixtures of Hydrogen and Oxygen at 480o C',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "74",
        pages = """2229""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978BAK/BAL2229:6",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00012779
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012779/rk00000003.xml
Bath gas: N2
""",
)

entry(
    index = 102,
    label = "O2 + C3H7O-2 <=> HO2 + C3H6O-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (8430, 'm^3/(mol*s)'),
        n = 0,
        Ea = (0.915, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (220, 'K'),
        Tmax = (310, 'K'),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Crowley, J.N.", "Hampson, R.F, Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."],
        title = u'Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry',
        journal = "Not in System",
        pages = """1-56""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001ATK/BAU1-56:131",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00013958
Pressure dependence: None reported
Note: Invalid activation energy uncertainty (4.157) found and ignored
""",
)

entry(
    index = 103,
    label = "O2 + C3H7O-2 <=> HO2 + C3H6O-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (195000, 'm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        Ea = (8.281, 'kJ/mol', '+|-', 0.745),
        T0 = (1, 'K'),
        Tmin = (250, 'K'),
        Tmax = (361, 'K'),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:19",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00013958
Uncertainty: 1.3
""",
)

entry(
    index = 104,
    label = "O2 + C3H7O-2 <=> HO2 + C3H6O-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (175000, 'm^3/(mol*s)', '+|-', 100000),
        n = 0,
        Ea = (7.308, 'kJ/mol', '+|-', 0.948),
        T0 = (1, 'K'),
        Tmin = (247, 'K'),
        Tmax = (361, 'K'),
        Pmin = (20000, 'Pa'),
        Pmax = (20000, 'Pa'),
    ),
    reference = Article(
        authors = ["Zabarnick, S.", "Heicklen, J."],
        title = u'The reactions of alkoxy radicals with O2. II. n-C3H7O radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "17",
        pages = """477""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985ZAB/HEI477:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00013958
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013958/rk00000001.xml
Bath gas: N2
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 105,
    label = "C3H7-3 + C3H7 <=> C3H8 + C3H6-2",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (3.01e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (-0.208, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (301, 'K'),
        Tmax = (424, 'K'),
    ),
    reference = Article(
        authors = ["Arrowsmith, P.", "Kirsch, L.J."],
        title = u'Mutual Reaction of Isopropyl Radicals',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "74",
        pages = """3016""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978ARR/KIR3016:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010168
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010168/rk00000013.xml
Bath gas: N2
Excitation technique: Direct photolysis
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 106,
    label = "C4H9-3 + C3H5 <=> C4H10 + C3H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.89e+07, 'm^3/(mol*s)', '*|/', 3),
        n = -0.75,
        Ea = (-0.549, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:74",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00009781
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009781/rk00000001.xml
Uncertainty: 3.0
""",
)

entry(
    index = 107,
    label = "C4H9 + C3H5-2 <=> C3H6 + C4H8",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (4.33e+08, 'm^3/(mol*s)', '*|/', 3),
        n = -0.75,
        Ea = (-0.549, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:75",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00009782
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009782/rk00000001.xml
Uncertainty: 3.0
""",
)

entry(
    index = 108,
    label = "C3H5 + C4H9-4 <=> C4H10-2 + C3H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (783000, 'm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (-0.549, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:103",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010124
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010124/rk00000001.xml
Uncertainty: 3.0
""",
)

entry(
    index = 109,
    label = "C3H5-2 + C4H9-2 <=> C3H6 + C4H8-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (783000, 'm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (-0.549, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:104",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010125
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010125/rk00000001.xml
Uncertainty: 2.0
""",
)

entry(
    index = 110,
    label = "O2 + C4H9O <=> HO2 + C4H8O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (36100, 'm^3/(mol*s)'),
        n = 0,
        Ea = (4.573, 'kJ/mol', '+|-', 4.157),
        T0 = (1, 'K'),
        Tmin = (290, 'K'),
        Tmax = (400, 'K'),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Crowley, J.N.", "Hampson, R.F, Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."],
        title = u'Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry',
        journal = "Not in System",
        pages = """1-56""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001ATK/BAU1-56:133",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00013972
Pressure dependence: None reported
""",
)

entry(
    index = 111,
    label = "O2 + C4H9O <=> HO2 + C4H8O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (195000, 'm^3/(mol*s)', '*|/', 1.32),
        n = 0,
        Ea = (8.281, 'kJ/mol', '+|-', 0.745),
        T0 = (1, 'K'),
        Tmin = (296, 'K'),
        Tmax = (361, 'K'),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:20",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00013972
Uncertainty: 1.3200001
""",
)

entry(
    index = 112,
    label = "O2 + C4H9O <=> HO2 + C4H8O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (450000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (9.811, 'kJ/mol', '+|-', 1.472),
        T0 = (1, 'K'),
        Tmin = (265, 'K'),
        Tmax = (393, 'K'),
        Pmin = (53300, 'Pa'),
        Pmax = (53300, 'Pa'),
    ),
    reference = Article(
        authors = ["Morabito, P.", "Heicklen, J."],
        title = u'The reactions of alkoxyl radicals with O2. IV. n-C4H9O radicals',
        journal = "Bull. Chem. Soc. Jpn.",
        volume = "60",
        pages = """2641""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987MOR/HEI2641:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00013972
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013972/rk00000001.xml
Bath gas: N2
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 113,
    label = "O2 + C4H9O-2 <=> HO2 + C4H8O-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (195000, 'm^3/(mol*s)', '*|/', 1.32),
        n = 0,
        Ea = (8.281, 'kJ/mol', '+|-', 0.745),
        T0 = (1, 'K'),
        Tmin = (265, 'K'),
        Tmax = (361, 'K'),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988HEI177:21",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00013994
Uncertainty: 1.3200001
""",
)

entry(
    index = 114,
    label = "O2 + C4H9O-2 <=> HO2 + C4H8O-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (193000, 'm^3/(mol*s)', '+|-', 120000),
        n = 0,
        Ea = (6.951, 'kJ/mol', '+|-', 1.322),
        T0 = (1, 'K'),
        Tmin = (265, 'K'),
        Tmax = (361, 'K'),
        Pmin = (20000, 'Pa'),
        Pmax = (20000, 'Pa'),
    ),
    reference = Article(
        authors = ["Zabarnick, S.", "Heicklen, J."],
        title = u'Reactions of alkoxy radicals with O2. III. i-C4H9O radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "17",
        pages = """503""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985ZAB/HEI503:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00013994
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013994/rk00000001.xml
Bath gas: N2
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 115,
    label = "C4H8-3 + C4H8 <=> C4H7 + C4H9",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (209.525, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (753, 'K'),
        Tmax = (813, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (13300, 'Pa'),
    ),
    reference = Article(
        authors = ["Douhou, S.", "Perrin, D.", "Martin, R."],
        title = u"Etude cinetique et modelisaiton de la reaction thermique de l'isobutene vers 800 K. I. Isobutene pur",
        journal = "J. Chim. Phys.",
        volume = "91",
        pages = """1597-1627""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994DOU/PER1597-1627:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005815
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00005815/rk00000001.xml
Bath gas: iso-C4H8
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 116,
    label = "C4H8-3 + C4H8-2 <=> C4H7 + C4H9-2",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (3.9e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (231.142, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (763, 'K'),
        Tmax = (813, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (13300, 'Pa'),
    ),
    reference = Article(
        authors = ["Douhou, S.", "Perrin, D.", "Martin, R."],
        title = u"Etude cinetique et modelisaiton de la reaction thermique de l'isobutene vers 800 K. I. Isobutene pur",
        journal = "J. Chim. Phys.",
        volume = "91",
        pages = """1597-1627""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994DOU/PER1597-1627:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005816
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00005816/rk00000001.xml
Bath gas: iso-C4H8
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 117,
    label = "C4H9-5 + C4H9-6 <=> C4H10-3 + C4H8-4",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+08, 'm^3/(mol*s)'),
        n = 0,
        Ea = (5.438, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (334, 'K'),
        Tmax = (502, 'K'),
        Pmin = (1600, 'Pa'),
        Pmax = (2800, 'Pa'),
    ),
    reference = Article(
        authors = ["Kerr, J.A.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part III. n-Butyl radicals from the photolysis of n-Valeraldehyde',
        journal = "J. Chem. Soc.",
        pages = """1602""",
        year = "1960",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1960KER/TRO1602:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011216
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011216/rk00000001.xml
Bath gas: n-C4H9CHO
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

