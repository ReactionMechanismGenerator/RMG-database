#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination/NIST"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "H + H <=> H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (109000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (6.269, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (278, 'K'),
        Tmax = (372, 'K'),
    ),
    reference = Article(
        authors = ["Dingle, J.R.", "Le Roy, D.J."],
        title = u'Kinetics of the reaction of atomic hydrogen with acetylene',
        journal = "J. Chem. Phys.",
        volume = "18",
        pages = """1632-1637""",
        year = "1950",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1950DIN/LER1632-1637:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009454
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009454/rk00000026.xml
Bath gas: C2H2
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 2,
    label = "CH3 + H <=> CH4",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.59e+10, 'm^3/(mol*s)'),
        n = -0.6,
        Ea = (1.571, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = Article(
        authors = ["Forst, W."],
        title = u'Microcanonical variational theory of radical recombination by inversion of interpolated partition function, with examples: CH3 + H, CH3 + CH3',
        journal = "J. Phys. Chem.",
        volume = "95",
        pages = """3612-3620""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991FOR3612-3620:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010887
""",
)

entry(
    index = 3,
    label = "CH3 + H <=> CH4",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.17e+06, 'm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0.208, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972TEN/JON1267:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010887
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010887/rk00000004.xml
Uncertainty: 2.0
Bath gas: H2
Excitation technique: Electron beam
Analytical technique: Gas chromatography
""",
)

entry(
    index = 4,
    label = "CH3 + H <=> CH4",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.93e+08, 'm^3/(mol*s)'),
        n = 0,
        Ea = (1.147, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Takahashi, J.", "Momose, T.", "Shida, T."],
        title = u'Thermal rate constants for SiH4=SiH3+H and CH4=CH3+H by Canonical Variational Transition State Theory',
        journal = "Bull. Chem. Soc. Jpn.",
        volume = "67",
        pages = """74-85""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994TAK/MOM74-85:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00010887
""",
)

entry(
    index = 5,
    label = "CH3 + H <=> CH4",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2e+08, 'm^3/(mol*s)'),
        n = 0,
        Ea = (0.815, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = Article(
        authors = ["Hase, W.L.", "Mondro, S.L.", "Duchovic, R.J.", "Hirst, D.M."],
        title = u'Thermal rate constant for H + CH3 \u2192\x92 CH4 recombination. 3. Comparison of experiment and canonical variational transition state theory',
        journal = "J. Am. Chem. Soc.",
        volume = "109",
        pages = """2916-2922""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987HAS/MON2916-2922:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00010887
""",
)

entry(
    index = 6,
    label = "CH3 + H <=> CH4",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.7e+08, 'm^3/(mol*s)'),
        n = 0,
        Ea = (1.671, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2200, 'K'),
    ),
    reference = Article(
        authors = ["Cobos, C.J.", "Troe, J."],
        title = u'Theory of thermal unimolecular reactions at high pressures. II. Analysis of experimental results',
        journal = "J. Chem. Phys.",
        volume = "83",
        pages = """1010-1015""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985COB/TRO1010-1015:8",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00010887
Bath gas: Products
""",
)

entry(
    index = 7,
    label = "CH4 <=> CH3 + H",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (5.09e+19, 's^-1'),
        n = -0.86,
        Ea = (456.598, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1600, 'K'),
        Tmax = (4500, 'K'),
    ),
    reference = Article(
        authors = ["Sutherland, J.W.", "Su, M.-C.", "Michael, J.V."],
        title = u'Rate Constants for H + CH4, CH3 + H2, and CH4 Dissociation at High Temperature',
        journal = "Int J. Chem. Kinet.",
        volume = "33",
        pages = """669-684""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001SUT/SU669-684:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010887
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010887/rk00000048.xml
Pressure dependence: Rate constant is high pressure limit
Experimental procedure: Shock tube
Excitation technique: Flash photolysis (laser or conventional)
Time resolution: In real time
Analytical technique: Vis-UV absorption

Excimer laser photolysis-shock tube technique coupled with H-atom atomic resonance absorption spectromtry has been used. The real time H atom profiles were fit with a complex mechanism to derive the best fit rate constants for the reactions, H+CH4-> CH3+H2, CH3+H2->H+CH4, as well as the reaction CH4+Kr->CH3+H+Kr. The derived rate constants for the latter reaction were not sensitive to the H+CH4reaction within expermental error.

Results of this study and seven previous experimental studies have been evaluated. Results from theory are also discussed.
""",
)

entry(
    index = 8,
    label = "CH4 <=> CH3 + H",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (5.13e+14, 's^-1'),
        n = 0,
        Ea = (422.375, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1430, 'K'),
        Tmax = (1780, 'K'),
        Pmin = (507000, 'Pa'),
        Pmax = (507000, 'Pa'),
    ),
    reference = Article(
        authors = ["Skinner, G.B.", "Ruehrwein, R.A."],
        title = u'Shock tube studies on the pyrolysis and oxidation of methane',
        journal = "J. Phys. Chem.",
        volume = "63",
        pages = """1736""",
        year = "1959",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1959SKI/RUE1736:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010887
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010887/rk00000050.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 9,
    label = "CH4 <=> CH3 + H",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (3.8e+14, 's^-1'),
        n = 0,
        Ea = (430.69, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Palmer, H.B.", "Hirt, T.J."],
        title = u'The activation energy for the pyrolysis of methane',
        journal = "J. Phys. Chem.",
        volume = "67",
        pages = """709""",
        year = "1963",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1963PAL/HIR709:1",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00010887
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010887/rk00000051.xml
Bath gas: He
""",
)

entry(
    index = 10,
    label = "CH4 <=> CH3 + H",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.26e+14, 's^-1', '*|/', 1.5),
        n = 0,
        Ea = (422.375, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1160, 'K'),
        Tmax = (1350, 'K'),
    ),
    reference = Article(
        authors = ["Palmer, H.B.", "Hirt, T.J."],
        title = u'The activation energy for the pyrolysis of methane',
        journal = "J. Phys. Chem.",
        volume = "67",
        pages = """709""",
        year = "1963",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1963PAL/HIR709:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010887
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010887/rk00000052.xml
Uncertainty: 1.5
Bath gas: He
Excitation technique: Thermal
Analytical technique: Other
""",
)

entry(
    index = 11,
    label = "CH4 <=> CH3 + H",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1e+15, 's^-1'),
        n = 0,
        Ea = (430.69, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1590, 'K'),
        Tmax = (1750, 'K'),
        Pmin = (2.03e+06, 'Pa'),
        Pmax = (2.03e+06, 'Pa'),
    ),
    reference = Article(
        authors = ["Kondratiev, V.N."],
        title = u'Determination of the rate constant for thermal cracking of methane by means of adiabatic compression and expansion',
        journal = "Symp. Int. Combust. Proc.",
        volume = "10",
        pages = """319""",
        year = "1965",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1965KON319:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010887
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010887/rk00000053.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 12,
    label = "CH4 <=> CH3 + H",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.66e+16, 's^-1'),
        n = 0,
        Ea = (427.364, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (4000, 'K'),
    ),
    reference = Article(
        authors = ["Placzek, D.W.", "Rabinovitch, B.S.", "Whitten, G.Z."],
        title = u'Some comparisons of the classical RRK and the RRKM theoretical rate formulations',
        journal = "J. Chem. Phys.",
        volume = "43",
        pages = """4071-4080""",
        year = "1965",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1965PLA/RAB4071-4080:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010887
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010887/rk00000054.xml
""",
)

entry(
    index = 13,
    label = "CH4 <=> CH3 + H",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1e+15, 's^-1'),
        n = 0,
        Ea = (434.847, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1250, 'K'),
        Tmax = (1670, 'K'),
    ),
    reference = Article(
        authors = ["Palmer, H.B."],
        title = u'Discussion',
        journal = "Symp. Int. Combust. Proc.",
        volume = "12",
        pages = """588""",
        year = "1969",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1969PAL588:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010887
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010887/rk00000055.xml
Bath gas: He
""",
)

entry(
    index = 14,
    label = "CH4 <=> CH3 + H",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.26e+15, 's^-1'),
        n = 0,
        Ea = (434.847, 'kJ/mol', '+|-', 8.73),
        T0 = (1, 'K'),
        Tmin = (1850, 'K'),
        Tmax = (2500, 'K'),
        Pmin = (507000, 'Pa'),
        Pmax = (2.23e+07, 'Pa'),
    ),
    reference = Article(
        authors = ["Hartig, R.", "Troe, J.", "Wagner, H.GG."],
        title = u'Thermal Decomposition of Methane Behind Reflected Shock Waves',
        journal = "Symp. Int. Combust. Proc.",
        volume = "13",
        pages = """147""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971HAR/TRO147:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010887
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010887/rk00000056.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 15,
    label = "CH4 <=> CH3 + H",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.8e+16, 's^-1'),
        n = 0,
        Ea = (449.813, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (995, 'K'),
        Tmax = (1100, 'K'),
        Pmin = (3333, 'Pa'),
        Pmax = (93300, 'Pa'),
    ),
    reference = Article(
        authors = ["Chen, C.J.", "Back, M.H.", "Back, R.A."],
        title = u'The Thermal Decomposition of Methane. I.Kinetics of the Promary Decomposition to C2H6 + H2; Rate Constant for the Homogeneous Unimolecular Dissociation of Methane and its Pressure Dependence',
        journal = "Can. J. Chem.",
        volume = "53",
        pages = """3580""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975CHE/BAC3580:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010887
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010887/rk00000057.xml
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 16,
    label = "CH4 <=> CH3 + H",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1e+15, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (419.881, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (3000, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:11",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010887
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010887/rk00000058.xml
Uncertainty: 3.1600001
""",
)

entry(
    index = 17,
    label = "CH4 <=> CH3 + H",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1e+16, 's^-1'),
        n = 0,
        Ea = (439.004, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010887
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010887/rk00000059.xml
""",
)

entry(
    index = 18,
    label = "CH4 <=> CH3 + H",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (3.72e+15, 's^-1', '*|/', 1.5),
        n = 0,
        Ea = (434.015, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2700, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W.", "Hampson, R.F."],
        title = u'Chemical kinetic data base for combustion chemistry. Part I. Methane and related compounds',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "15",
        pages = """1087""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:14",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010887
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010887/rk00000060.xml
Uncertainty: 1.5
Bath gas: N2
""",
)

entry(
    index = 19,
    label = "CH4 <=> CH3 + H",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.75e+16, 's^-1', '+|-', 2.4e+15),
        n = 0,
        Ea = (440.667, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1070, 'K'),
        Tmax = (1150, 'K'),
        Pmin = (500000, 'Pa'),
        Pmax = (5e+06, 'Pa'),
    ),
    reference = Article(
        authors = ["Barnes, r.W.", "Pratt, G.L."],
        title = u'Pressure dependence of methane dissociation',
        journal = "J. Chem. Soc. Faraday Trans. 2",
        volume = "85",
        pages = """229-238""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989BAR/PRA229-238:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010887
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010887/rk00000061.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 20,
    label = "CH4 <=> CH3 + H",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.4e+16, 's^-1'),
        n = 0,
        Ea = (439.004, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (5000, 'K'),
    ),
    reference = Article(
        authors = ["Cobos, C.J.", "Troe, J."],
        title = u'The dissociation-recombination system CH4 + M = CH3 + H + M: reevaluated experiments from 300 to 3000 K',
        journal = "Z. Phys. Chem. (Neue Folge)",
        volume = "167",
        pages = """129-149""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990COB/TRO129-149:1",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00010887
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010887/rk00000063.xml
Bath gas: Ar
""",
)

entry(
    index = 21,
    label = "CH4 <=> CH3 + H",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (3.01e+12, 's^-1', '+|-', 9.9e+11),
        n = 0,
        Ea = (343.388, 'kJ/mol', '+|-', 10.31),
        T0 = (1, 'K'),
        Tmin = (1100, 'K'),
        Tmax = (1700, 'K'),
        Pmin = (14800, 'Pa'),
        Pmax = (93300, 'Pa'),
    ),
    reference = Article(
        authors = ["Arutyunov, V.S.", "Vedeneev, V.I.", "Moshkina, R.I.", "Ushakov, V.A."],
        title = u'Pyrolysis of methane under static conditions at 1100-1400 K',
        journal = "Kinet. Catal.",
        volume = "32",
        pages = """234-240""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991ARU/VED234-240:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010887
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010887/rk00000064.xml
Bath gas: CH4
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 22,
    label = "CH4 <=> CH3 + H",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.4e+16, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (439.004, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (3000, 'K'),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Frank, P.", "Hayman, G.", "Just, Th.", "Kerr, J.A.", "Murrells, T.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combusion modelling. Supplement I',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "23",
        pages = """847-1033""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994BAU/COB847-1033:12",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010887
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010887/rk00000065.xml
Uncertainty: 3.1600001
Bath gas: Ar
""",
)

entry(
    index = 23,
    label = "CH4 <=> CH3 + H",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.04e+18, 's^-1'),
        n = 0,
        Ea = (403.252, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1780, 'K'),
        Tmax = (2320, 'K'),
    ),
    reference = Article(
        authors = ["Davidson, D.F.", "Hanson, R.K.", "Bowman, C.T."],
        title = u'Communication: revised values for the rate coefficients of ethane and methane decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "27",
        pages = """305-308""",
        year = "1995",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1995DAV/HAN305-308:1",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00010887
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010887/rk00000069.xml
Bath gas: Ar
""",
)

entry(
    index = 24,
    label = "OH + H <=> H2O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.62e+08, 'm^3/(mol*s)'),
        n = 0,
        Ea = (0.624, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2100, 'K'),
    ),
    reference = Article(
        authors = ["Cobos, C.J.", "Troe, J."],
        title = u'Theory of thermal unimolecular reactions at high pressures. II. Analysis of experimental results',
        journal = "J. Chem. Phys.",
        volume = "83",
        pages = """1010-1015""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985COB/TRO1010-1015:15",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00013764
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013764/rk00000016.xml
Bath gas: Products
""",
)

entry(
    index = 25,
    label = "CHO + H <=> CH2O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (46800, 'm^3/(mol*s)'),
        n = 0,
        Ea = (-18.957, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981TSU/KAT985:8",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00001337
Bath gas: Ar
""",
)

entry(
    index = 26,
    label = "CH4O <=> H + CH3O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.19e+07, 's^-1'),
        n = 2.39,
        Ea = (416.768, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Ing, W.C.", "Sheng, C.Y.", "Bozzelli, J.W."],
        title = u'Development of a detailed high-pressure reaction model for methane/mehanol mixtures under pyrolytic and oxidative conditions and comparison with experimental data',
        journal = "Fuel Process. Technol.",
        volume = "83",
        pages = """111-145""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003ING/SHE111-145:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00001660
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00001660/rk00000001.xml
Pressure dependence: Rate constant is high pressure limit

Combined experimental, ab initio, and modeling study. Rate constants abstracted here are based on ab initio calculations.  CBS-Q//B3LYP/6-31G(d,p) and CBS-APNO ab initio methods were used. Rate constants for reactions with barrier were determined from the ab initio transition states using TST. For barrierless reactions variational TST was used.  Rate constants listed here are for high pressure limit. Pressure dependent rate expressions and full detailed chemical kinetic model can be obtained from the authors.
""",
)

entry(
    index = 27,
    label = "H + CH3O <=> CH4O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.45e+07, 'm^3/(mol*s)'),
        n = 0.24,
        Ea = (-0.217, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Jasper, A.W.", "Klippenstein, S.J.", "Harding, L.B.", "Ruscic, B."],
        title = u'Kinetics of the reaction of methyl radical with hydroxyl radical and methanol decomposition',
        journal = "J. Phys. Chem. A",
        volume = "111",
        pages = """3932-3950""",
        year = "2007",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2007JAS/KLI3932-3950:7",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00001660
Pressure dependence: Rate constant is high pressure limit

Reaction potential energy surface was studied using quantum chemistry and rate constants were calculated using variational transition state theory.
""",
)

entry(
    index = 28,
    label = "OH + CH3 <=> CH4O-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.23e+34, 'm^3/(mol*s)'),
        n = -8.2,
        Ea = (48.806, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987DEA/WES207:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00001661
Bath gas: N2
""",
)

entry(
    index = 29,
    label = "OH + CH3 <=> CH4O-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.2e+07, 'm^3/(mol*s)'),
        n = -0.02,
        Ea = (-0.139, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Jasper, A.W.", "Klippenstein, S.J.", "Harding, L.B.", "Ruscic, B."],
        title = u'Kinetics of the reaction of methyl radical with hydroxyl radical and methanol decomposition',
        journal = "J. Phys. Chem. A",
        volume = "111",
        pages = """3932-3950""",
        year = "2007",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2007JAS/KLI3932-3950:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00001661
Pressure dependence: Rate constant is high pressure limit

Reaction potential energy surface was studied using quantum chemistry and rate constants were calculated using variational transition state theory.
""",
)

entry(
    index = 30,
    label = "OH + CH3 <=> CH4O-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.31, 'm^3/(mol*s)'),
        n = 2.08,
        Ea = (-7.364, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Ing, W.C.", "Sheng, C.Y.", "Bozzelli, J.W."],
        title = u'Development of a detailed high-pressure reaction model for methane/mehanol mixtures under pyrolytic and oxidative conditions and comparison with experimental data',
        journal = "Fuel Process. Technol.",
        volume = "83",
        pages = """111-145""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003ING/SHE111-145:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00001661
Pressure dependence: Rate constant is high pressure limit

Combined experimental, ab initio, and modeling study. Rate constants abstracted here are based on ab initio calculations.  CBS-Q//B3LYP/6-31G(d,p) and CBS-APNO ab initio methods were used. Rate constants for reactions with barrier were determined from the ab initio transition states using TST. For barrierless reactions variational TST was used.  Rate constants listed here are for high pressure limit. Pressure dependent rate expressions and full detailed chemical kinetic model can be obtained from the authors.
""",
)

entry(
    index = 31,
    label = "CH4O-3 <=> CH3O-2 + H",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (0.0079, 's^-1'),
        n = 5.04,
        Ea = (353.448, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (3000, 'K'),
    ),
    reference = Article(
        authors = ["Jasper, A.W.", "Klippenstein, S.J.", "Harding, L.B.", "Ruscic, B."],
        title = u'Kinetics of the reaction of methyl radical with hydroxyl radical and methanol decomposition',
        journal = "J. Phys. Chem. A",
        volume = "111",
        pages = """3932-3950""",
        year = "2007",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2007JAS/KLI3932-3950:31",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00001662
Pressure dependence: Rate constant is high pressure limit

Reaction potential energy surface was studied using quantum chemistry and rate constants were calculated using variational transition state theory.
""",
)

entry(
    index = 32,
    label = "CH4O-3 <=> CH3O-2 + H",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1.64e+07, 's^-1'),
        n = 2.55,
        Ea = (384.719, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Ing, W.C.", "Sheng, C.Y.", "Bozzelli, J.W."],
        title = u'Development of a detailed high-pressure reaction model for methane/mehanol mixtures under pyrolytic and oxidative conditions and comparison with experimental data',
        journal = "Fuel Process. Technol.",
        volume = "83",
        pages = """111-145""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003ING/SHE111-145:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00001662
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00001662/rk00000005.xml
Pressure dependence: Rate constant is high pressure limit

Combined experimental, ab initio, and modeling study. Rate constants abstracted here are based on ab initio calculations.  CBS-Q//B3LYP/6-31G(d,p) and CBS-APNO ab initio methods were used. Rate constants for reactions with barrier were determined from the ab initio transition states using TST. For barrierless reactions variational TST was used.  Rate constants listed here are for high pressure limit. Pressure dependent rate expressions and full detailed chemical kinetic model can be obtained from the authors.
""",
)

entry(
    index = 33,
    label = "C2H6 <=> C2H5 + H",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (8.96e+20, 's^-1'),
        n = -1.23,
        Ea = (427.364, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Stewart, P.H.", "Larson, C.W.", "Golden, D.M."],
        title = u'Pressure and temperature dependence of reactions proceeding via a bound complex. 2. Application to 2CH3 \u2192\x92 C2H5 + H',
        journal = "Combust. Flame",
        volume = "75",
        pages = """25-31""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989STE/LAR25-31:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002086
Bath gas: Ar
""",
)

entry(
    index = 34,
    label = "C2H6 <=> C2H5 + H",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1.26e+16, 's^-1'),
        n = 0,
        Ea = (409.903, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002086
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002086/rk00000001.xml
""",
)

entry(
    index = 35,
    label = "C2H4 <=> C2H3 + H",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2e+16, 's^-1'),
        n = 0,
        Ea = (460.622, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002163
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002163/rk00000007.xml
""",
)

entry(
    index = 36,
    label = "C2H3 + H <=> C2H4",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (5.36e+08, 'm^3/(mol*s)'),
        n = 0,
        Ea = (4.107, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (1300, 'K'),
        Pmin = (10100, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Duran, R.P.", "Amorebieta, V.T.", "Colussi, A.J."],
        title = u'Is the homogeneous thermal dimerization of acetylene a free-radical chain reaction? Kinetic and thermochemical analysis',
        journal = "J. Phys. Chem.",
        volume = "92",
        pages = """636""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988DUR/AMO636:10",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00002163
""",
)

entry(
    index = 37,
    label = "C2H2 <=> C2H + H",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.63e+15, 's^-1'),
        n = 0,
        Ea = (518.823, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W.", "Hampson, R.F."],
        title = u'Chemical kinetic data base for combustion chemistry. Part I. Methane and related compounds',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "15",
        pages = """1087""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:61",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002385
Bath gas: N2
""",
)

entry(
    index = 38,
    label = "C2H2 <=> C2H + H",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1e+15, 's^-1'),
        n = 0,
        Ea = (460.622, 'kJ/mol', '+|-', 41.406),
        T0 = (1, 'K'),
        Tmin = (1700, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Al'tshuler, B.N."],
        title = u'Investigation of the High Temperature Pyrolysis of Acetylene',
        journal = "Kinet. Catal.",
        volume = "15",
        pages = """835""",
        year = "1974",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1974ALT835:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002385
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Other
""",
)

entry(
    index = 39,
    label = "CH2O <=> CHO + H",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1e+14, 's^-1'),
        n = 0,
        Ea = (364.174, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1060, 'K'),
        Tmax = (1220, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Aronowitz, D.", "Naegeli, D."],
        title = u'High-Temperature Pyrolysis of Dimethyl Ether',
        journal = "Int. J. Chem. Kinet.",
        volume = "9",
        pages = """471""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977ARO/NAE471:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00001337
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00001337/rk00000003.xml
Bath gas: N2
""",
)

entry(
    index = 40,
    label = "CH4O-2 <=> OH + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+16, 's^-1'),
        n = 0,
        Ea = (380.803, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1070, 'K'),
        Tmax = (1220, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Aronowitz, D.", "Naegeli, D.W.", "Glassman, I."],
        title = u'Kinetics of the pyrolysis of methanol',
        journal = "J. Phys. Chem.",
        volume = "81",
        pages = """2555""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977ARO/NAE2555:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00001661
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00001661/rk00000002.xml
Bath gas: N2
""",
)

entry(
    index = 41,
    label = "CH4O-2 <=> OH + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+18, 's^-1'),
        n = 0,
        Ea = (394.937, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981TSU/KAT985:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00001661
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00001661/rk00000005.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 42,
    label = "CH4O-2 <=> OH + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.4e+15, 's^-1'),
        n = 0,
        Ea = (375.814, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1600, 'K'),
        Tmax = (2100, 'K'),
        Pmin = (2800, 'Pa'),
        Pmax = (92900, 'Pa'),
    ),
    reference = Article(
        authors = ["Spindler, K.", "Wagner, H.Gg."],
        title = u'Zum thermischen unimolekularen Zerfall von Methanol',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "86",
        pages = """2""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982SPI/WAG2:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00001661
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00001661/rk00000007.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 43,
    label = "CH4O-2 <=> OH + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.4e+15, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (375.814, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:6",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00001661
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00001661/rk00000009.xml
Uncertainty: 3.1600001
""",
)

entry(
    index = 44,
    label = "CH4O-2 <=> OH + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.9e+16, 's^-1', '*|/', 2),
        n = 0,
        Ea = (384.129, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987TSA471:2",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00001661
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00001661/rk00000011.xml
Uncertainty: 2.0
""",
)

entry(
    index = 45,
    label = "CH4O-2 <=> OH + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.7e+16, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (379.971, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Frank, P.", "Hayman, G.", "Just, Th.", "Kerr, J.A.", "Murrells, T.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combusion modelling. Supplement I',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "23",
        pages = """847-1033""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994BAU/COB847-1033:8",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00001661
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00001661/rk00000015.xml
Uncertainty: 3.1600001
""",
)

entry(
    index = 46,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+13, 's^-1'),
        n = 0,
        Ea = (263.569, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (803, 'K'),
        Tmax = (943, 'K'),
        Pmin = (3333, 'Pa'),
        Pmax = (33300, 'Pa'),
    ),
    reference = Article(
        authors = ["Kenwright, R.", "Robinson, P.L.", "Trenwith, A.B."],
        title = u'The kinetics of the oxidation of ethane by nitrous oxide',
        journal = "J. Chem. Soc.",
        pages = """660-666""",
        year = "1958",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1958KEN/ROB660-666:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000001.xml
Bath gas: C2H6
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 47,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.012e+14, 's^-1'),
        n = 0,
        Ea = (79.3, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (1057, 'K'),
        Tmax = (1418, 'K'),
    ),
    reference = Article(
        authors = ["Skinner, G.B.", "Ball, W.E."],
        title = u'Shock tube experiments on the pyrolysis of ethane',
        journal = "J. Phys. Chem.",
        volume = "64",
        pages = """1025""",
        year = "1960",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1960SKI/BAL1025:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000003.xml
Bath gas: C2H6
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 48,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.07e+15, 's^-1'),
        n = 0,
        Ea = (305.973, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (823, 'K'),
        Tmax = (903, 'K'),
        Pmin = (4266, 'Pa'),
        Pmax = (84000, 'Pa'),
    ),
    reference = Article(
        authors = ["Laidler, K.J.", "Wojciechowski, B.W."],
        title = u'Kinetics and mechanisms of the thermal decomposition of ethane. I. The uninhibited reaction',
        journal = "Proc. R. Soc. London",
        volume = "260",
        pages = """91-102""",
        year = "1961",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1961LAI/WOJ91-102:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000004.xml
Bath gas: C2H6
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 49,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.6e+12, 's^-1'),
        n = 0,
        Ea = (280.198, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1040, 'K'),
        Tmax = (1340, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Towell, g.D.", "Martin, J.J."],
        title = u'Kinetic data from nonisothermal experiments: thermal decomposition of ethane, ethylene, and acetylene',
        journal = "AIChE J.",
        volume = "7",
        pages = """693-698""",
        year = "1961",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1961TOW/MAR693-698:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000005.xml
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 50,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+14, 's^-1'),
        n = 0,
        Ea = (288.512, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1160, 'K'),
        Tmax = (1580, 'K'),
        Pmin = (267, 'Pa'),
        Pmax = (800, 'Pa'),
    ),
    reference = Article(
        authors = ["Kozlov, G.I.", "Knorre, V.G."],
        title = u'Single-pulse shock tube studies on the kinetics of the thermal decomposition of methane',
        journal = "Combust. Flame",
        volume = "6",
        pages = """253""",
        year = "1962",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1962KOZ/KNO253:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000007.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 51,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.82e+17, 's^-1', '*|/', 10),
        n = 0,
        Ea = (384.129, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (837, 'K'),
        Tmax = (881, 'K'),
        Pmin = (8133, 'Pa'),
        Pmax = (26900, 'Pa'),
    ),
    reference = Article(
        authors = ["Quinn, C.P."],
        title = u'The thermal dissociation and pyrolysis of ethane',
        journal = "Proc. R. Soc. London A",
        volume = "275",
        pages = """190""",
        year = "1963",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1963QUI190:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000008.xml
Uncertainty: 10.0
Bath gas: C2H6
Excitation technique: Thermal
Analytical technique: Gas chromatography
Note: Invalid Ea value uncertainty (8314472.0) found and ignored
""",
)

entry(
    index = 52,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.34e+16, 's^-1'),
        n = 0,
        Ea = (368.331, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (830, 'K'),
        Tmax = (850, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (100000, 'Pa'),
    ),
    reference = Article(
        authors = ["Dexter, R.W.", "Trenwith, A.B."],
        title = u'The dissociation of ethane',
        journal = "J. Chem. Soc.",
        pages = """392""",
        year = "1964",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1964DEX/TRE392:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000009.xml
Bath gas: C2H6
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 53,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3e+16, 's^-1'),
        n = 0,
        Ea = (368.331, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (913, 'K'),
        Tmax = (999, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (26700, 'Pa'),
    ),
    reference = Article(
        authors = ["Lin, M.C.", "Back, M.H."],
        title = u'the thermal decomposition of ethane. Part II. The unimolecular decomposition of the ethane molecule and the ethyl radical',
        journal = "Can. J. Chem.",
        volume = "44",
        pages = """2357""",
        year = "1966",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1966LIN/BAC2357:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000010.xml
Bath gas: C2H6
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 54,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+16, 's^-1', '*|/', 1.16),
        n = 0,
        Ea = (360.017, 'kJ/mol', '+|-', 1.546),
        T0 = (1, 'K'),
        Tmin = (823, 'K'),
        Tmax = (893, 'K'),
        Pmin = (5333, 'Pa'),
        Pmax = (80000, 'Pa'),
    ),
    reference = Article(
        authors = ["Lin, M.C.", "Back, M.H."],
        title = u'The thermal decomposition of ethane. Part I. Initiation and termination steps',
        journal = "Can. J. Chem.",
        volume = "44",
        pages = """505-514""",
        year = "1966",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1966LIN/BAC505-514:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000012.xml
Uncertainty: 1.16
Bath gas: C2H6
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 55,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+16, 's^-1'),
        n = 0,
        Ea = (368.331, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (839, 'K'),
        Tmax = (873, 'K'),
        Pmin = (267, 'Pa'),
        Pmax = (1467, 'Pa'),
    ),
    reference = Article(
        authors = ["Trenwith, A.B."],
        title = u'Dissociation and kinetics of thermal decomposition of ethane',
        journal = "J. Chem. Soc. Faraday Trans.",
        volume = "62",
        pages = """1538""",
        year = "1966",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1966TRE1538:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000014.xml
Bath gas: C2H6
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 56,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+18, 's^-1'),
        n = 0,
        Ea = (379.14, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (860, 'K'),
        Tmax = (890, 'K'),
    ),
    reference = Article(
        authors = ["Waage, E.V.", "Rabinovitch, B.S."],
        title = u'Some aspects of theory and experiment in the ethane-methyl radical system',
        journal = "Int. J. Chem. Kinet.",
        volume = "3",
        pages = """105-125""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971WAA/RAB105-125:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000016.xml
""",
)

entry(
    index = 57,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+16, 's^-1'),
        n = 0,
        Ea = (369.994, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (920, 'K'),
        Tmax = (1040, 'K'),
        Pmin = (13.33, 'Pa'),
        Pmax = (26700, 'Pa'),
    ),
    reference = Article(
        authors = ["Pacey, P.D.", "Purnell, J.H."],
        title = u'Arrhenius Parameters of the Reaction CH3. + C2H6 \u2192\x92 CH4 + C2H5.',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "68",
        pages = """1462""",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972PAC/PUR1462:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000017.xml
Bath gas: C2H6
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 58,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+16, 's^-1'),
        n = 0,
        Ea = (374.151, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1500, 'K'),
        Pmin = (172000, 'Pa'),
        Pmax = (639000, 'Pa'),
    ),
    reference = Article(
        authors = ["Burcat, A.", "Skinner, G.B.", "Crossley, R.W.", "Scheller, K."],
        title = u'High Temperature Decomposition of Ethane',
        journal = "Int. J. Chem. Kinet.",
        volume = "5",
        pages = """345""",
        year = "1973",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1973BUR/SKI345:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000018.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 59,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.35e+16, 's^-1', '*|/', 1.21),
        n = 0,
        Ea = (362.511, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (778, 'K'),
        Tmax = (878, 'K'),
        Pmin = (1300, 'Pa'),
        Pmax = (215000, 'Pa'),
    ),
    reference = Article(
        authors = ["Clark, J.A.", "Quinn, C.P."],
        title = u'Kinetic Isotope Effect in the Thermal Dissociation of Ethane',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "72",
        pages = """706""",
        year = "1976",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976CLA/QUI706:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000020.xml
Uncertainty: 1.21
Bath gas: C2H6
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 60,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.08e+16, 's^-1'),
        n = 0,
        Ea = (377.477, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1330, 'K'),
        Tmax = (2500, 'K'),
        Pmin = (2720, 'Pa'),
        Pmax = (10900, 'Pa'),
    ),
    reference = Article(
        authors = ["Olson, D.B.", "Gardiner, W.C., Jr."],
        title = u'Thermal Dissociation Rate of Ethane at the High Pressure Limit from 250 to 2500 K',
        journal = "J. Phys. Chem.",
        volume = "83",
        pages = """922""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979OLS/GAR922:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000021.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Laser schlieren
""",
)

entry(
    index = 61,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.04e+16, 's^-1'),
        n = 0,
        Ea = (367.5, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (250, 'K'),
        Tmax = (2500, 'K'),
        Pmin = (2720, 'Pa'),
        Pmax = (10900, 'Pa'),
    ),
    reference = Article(
        authors = ["Olson, D.B.", "Gardiner, W.C., Jr."],
        title = u'Thermal Dissociation Rate of Ethane at the High Pressure Limit from 250 to 2500 K',
        journal = "J. Phys. Chem.",
        volume = "83",
        pages = """922""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979OLS/GAR922:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000022.xml
Bath gas: Ar
""",
)

entry(
    index = 62,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+15, 's^-1', '*|/', 2),
        n = 0,
        Ea = (326.759, 'kJ/mol', '+|-', 6.543),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979PRA/ROG1089:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000023.xml
Uncertainty: 2.0
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 63,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+15, 's^-1'),
        n = 0,
        Ea = (349.208, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1450, 'K'),
        Tmax = (2100, 'K'),
        Pmin = (175000, 'Pa'),
        Pmax = (185000, 'Pa'),
    ),
    reference = Article(
        authors = ["Roth, P.", "Just, T.H."],
        title = u'Measurements of Some Elementary Hydrocarbon Reactions at High Temperatures',
        journal = "NBS Spec. Publ. (U.S.)",
        volume = "10",
        pages = """1339""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979ROT/JUS1339:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000024.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 64,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.25e+16, 's^-1'),
        n = 0,
        Ea = (371.657, 'kJ/mol', '+|-', 3.717),
        T0 = (1, 'K'),
        Tmin = (840, 'K'),
        Tmax = (913, 'K'),
        Pmin = (87700, 'Pa'),
        Pmax = (92300, 'Pa'),
    ),
    reference = Article(
        authors = ["Trenwith, A.B."],
        title = u'Re-examination of the Thermal Dissociation of Ethane',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "75",
        pages = """614""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979TRE614:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000026.xml
Bath gas: C2H6
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 65,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+16, 's^-1'),
        n = 0,
        Ea = (372.488, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (840, 'K'),
        Tmax = (913, 'K'),
        Pmin = (87700, 'Pa'),
        Pmax = (92300, 'Pa'),
    ),
    reference = Article(
        authors = ["Trenwith, A.B."],
        title = u'Re-examination of the Thermal Dissociation of Ethane',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "75",
        pages = """614""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979TRE614:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000027.xml
Bath gas: C2H6
""",
)

entry(
    index = 66,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.4e+16, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (365.837, 'kJ/mol', '+|-', 25.609),
        T0 = (1, 'K'),
        Tmin = (750, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Duxbury, J."],
        title = u'Ethane Decomposition and the Reference Rate Constant for Methyl Radical Recombination',
        journal = "Combust. Flame",
        volume = "37",
        pages = """313""",
        year = "1980",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1980BAU/DUX313:1",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000028.xml
Uncertainty: 3.1600001
""",
)

entry(
    index = 67,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8e+12, 's^-1'),
        n = 0,
        Ea = (294.332, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1700, 'K'),
        Tmax = (2300, 'K'),
        Pmin = (157000, 'Pa'),
        Pmax = (177000, 'Pa'),
    ),
    reference = Article(
        authors = ["Bhaskaran, K.A.", "Frank, P.", "Just, Th."],
        title = u'High Temperature Methyl Radical Reactions with Atomic and Molecular Oxygen',
        journal = "Proc. Int. Symp. Shock Tubes Waves",
        volume = "12",
        pages = """503""",
        year = "1980",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1980BHA/FRA503:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000029.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 68,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.8e+15, 's^-1'),
        n = 0,
        Ea = (352.534, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1240, 'K'),
        Tmax = (1700, 'K'),
        Pmin = (203000, 'Pa'),
        Pmax = (304000, 'Pa'),
    ),
    reference = Article(
        authors = ["Chiang, C.C.", "Skinner, G.B."],
        title = u'Resonance Absorption Measurements of Atom Concentrations in Reacting Gas Mixtures. 7. Pyrolysis of C2H6 and C2D6 behind Shock Waves',
        journal = "J. Phys. Chem.",
        volume = "85",
        pages = """3126""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981CHI/SKI3126:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000031.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 69,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.58e+17, 's^-1'),
        n = 0,
        Ea = (380.803, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1300, 'K'),
        Pmin = (304000, 'Pa'),
        Pmax = (912000, 'Pa'),
    ),
    reference = Article(
        authors = ["Skinner, G.B.", "Rogers, D.", "Patel, K.B."],
        title = u'Consistency of theory and experiment in the ethane-methyl radical system',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """481""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981SKI/ROG481:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000033.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 70,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.31e+16, 's^-1', '*|/', 2.75),
        n = 0,
        Ea = (367.5, 'kJ/mol', '+|-', 7.358),
        T0 = (1, 'K'),
        Tmin = (841, 'K'),
        Tmax = (913, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (2666, 'Pa'),
    ),
    reference = Article(
        authors = ["Kanan, K.", "Purnell, H.", "Sepherad, A."],
        title = u'Induced heterogeneity, a novel technique for the study of gas-phase reactions. 2. Direct study of C-C bond scission in ethane',
        journal = "Int. J. Chem. Kinet.",
        volume = "15",
        pages = """845""",
        year = "1983",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1983KAN/PUR845:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000034.xml
Uncertainty: 2.75
Bath gas: C2H6
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 71,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.27e+16, 's^-1', '*|/', 1.51),
        n = 0,
        Ea = (369.994, 'kJ/mol', '+|-', 3.7),
        T0 = (1, 'K'),
        Tmin = (841, 'K'),
        Tmax = (913, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (2666, 'Pa'),
    ),
    reference = Article(
        authors = ["Kanan, K.", "Purnell, H.", "Sepherad, A."],
        title = u'Induced heterogeneity, a novel technique for the study of gas-phase reactions. 2. Direct study of C-C bond scission in ethane',
        journal = "Int. J. Chem. Kinet.",
        volume = "15",
        pages = """845""",
        year = "1983",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1983KAN/PUR845:2",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000035.xml
Uncertainty: 1.51
Bath gas: C2H6
""",
)

entry(
    index = 72,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.4e+16, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (365.837, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (750, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:16",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000038.xml
Uncertainty: 3.1600001
""",
)

entry(
    index = 73,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+16, 's^-1'),
        n = 0,
        Ea = (374.151, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000040.xml
""",
)

entry(
    index = 74,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7e+14, 's^-1'),
        n = 0,
        Ea = (335.073, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985HID/SHI441:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000041.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 75,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.17e+22, 's^-1', '*|/', 2),
        n = -1.79,
        Ea = (380.803, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:28",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000043.xml
Uncertainty: 2.0
Bath gas: Ar
""",
)

entry(
    index = 76,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.05e+26, 's^-1'),
        n = -2.79,
        Ea = (389.949, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Stewart, P.H.", "Larson, C.W.", "Golden, D.M."],
        title = u'Pressure and temperature dependence of reactions proceeding via a bound complex. 2. Application to 2CH3 \u2192\x92 C2H5 + H',
        journal = "Combust. Flame",
        volume = "75",
        pages = """25-31""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989STE/LAR25-31:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000044.xml
Bath gas: Ar
""",
)

entry(
    index = 77,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.01e+22, 's^-1'),
        n = -1.79,
        Ea = (380.803, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (843, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Rate constants for the decomposition and formation of simple alkanes over extended temperature and pressure ranges',
        journal = "Combust. Flame",
        volume = "78",
        pages = """71-86""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989TSA71-86:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000045.xml
Bath gas: Ar
""",
)

entry(
    index = 78,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.8e+21, 's^-1', '*|/', 2),
        n = -1.24,
        Ea = (379.971, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combustion modelling',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """411-429""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992BAU/COB411-429:32",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000046.xml
Uncertainty: 2.0
""",
)

entry(
    index = 79,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.85e+75, 's^-1', '*|/', 1.25),
        n = -17.6,
        Ea = (488.891, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1350, 'K'),
        Tmax = (2110, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Davidson, D.F.", "DiRosa, M.D.", "Hanson, R.K.", "Bowman, C.T."],
        title = u'A study of ethane decomposition in a shock tube using laser absorption of CH3',
        journal = "Int. J. Chem. Kinet.",
        volume = "25",
        pages = """969-982""",
        year = "1993",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1993DAV/DIR969-982:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000049.xml
Uncertainty: 1.25
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 80,
    label = "C2H6-2 <=> CH3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+11, 's^-1'),
        n = 0,
        Ea = (251.929, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1450, 'K'),
        Tmax = (1940, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Davidson, D.F.", "Hanson, R.K.", "Bowman, C.T."],
        title = u'Communication: revised values for the rate coefficients of ethane and methane decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "27",
        pages = """305-308""",
        year = "1995",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1995DAV/HAN305-308:2",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000054.xml
Bath gas: Ar
""",
)

entry(
    index = 81,
    label = "CH3 + CH3 <=> C2H6-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.39e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (-6.344, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (434, 'K'),
        Tmax = (1090, 'K'),
        Pmin = (640, 'Pa'),
        Pmax = (2466, 'Pa'),
    ),
    reference = Article(
        authors = ["Ingold, K.U.", "Lossing, F.P."],
        title = u'Free radicals by mass spectrometry. IV. The rate of combination of methyl radicals',
        journal = "J. Chem. Phys.",
        volume = "21",
        pages = """1135-1144""",
        year = "1953",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1953ING/LOS1135-1144:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000067.xml
Bath gas: (CH3)2Hg
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 82,
    label = "CH3 + CH3 <=> C2H6-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (55200, 'm^3/(mol*s)'),
        n = 0.5,
        Ea = (-9.063, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (434, 'K'),
        Tmax = (1090, 'K'),
        Pmin = (640, 'Pa'),
        Pmax = (2466, 'Pa'),
    ),
    reference = Article(
        authors = ["Ingold, K.U.", "Lossing, F.P."],
        title = u'The rate of combination of methyl radicals',
        journal = "J. Chem. Phys.",
        volume = "21",
        pages = """368""",
        year = "1953",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1953ING/LOS368:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000068.xml
Bath gas: He
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 83,
    label = "CH3 + CH3 <=> C2H6-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.41e+08, 'm^3/(mol*s)'),
        n = 0,
        Ea = (5.903, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (900, 'K'),
    ),
    reference = Article(
        authors = ["Waage, E.V.", "Rabinovitch, B.S."],
        title = u'Some aspects of theory and experiment in the ethane-methyl radical system',
        journal = "Int. J. Chem. Kinet.",
        volume = "3",
        pages = """105-125""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971WAA/RAB105-125:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000081.xml
""",
)

entry(
    index = 84,
    label = "CH3 + CH3 <=> C2H6-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.62e+07, 'm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (1.796, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972TEN/JON1267:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000082.xml
Uncertainty: 2.0
Bath gas: H2
Excitation technique: Electron beam
Analytical technique: Gas chromatography
""",
)

entry(
    index = 85,
    label = "CH3 + CH3 <=> C2H6-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.67e+07, 'm^3/(mol*s)', '+|-', 1e+06),
        n = 0,
        Ea = (-1.28, 'kJ/mol', '+|-', 0.18),
        T0 = (1, 'K'),
        Tmin = (296, 'K'),
        Tmax = (577, 'K'),
        Pmin = (667, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["MacPherson, M.T.", "Pilling, M.J.", "Smith, M.J.C."],
        title = u'The pressure and temperature dependence of the rate constant for methyl radical recombination over the temperature range 296-577 K',
        journal = "Chem. Phys. Lett.",
        volume = "94",
        pages = """430""",
        year = "1983",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1983MAC/PIL430:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000105.xml
Uncertainty: 1.3
Bath gas: Ar
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 86,
    label = "CH3 + CH3 <=> C2H6-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.39e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (0.449, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1300, 'K'),
    ),
    reference = Article(
        authors = ["Cobos, C.J.", "Troe, J."],
        title = u'Theory of thermal unimolecular reactions at high pressures. II. Analysis of experimental results',
        journal = "J. Chem. Phys.",
        volume = "83",
        pages = """1010-1015""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985COB/TRO1010-1015:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000109.xml
Bath gas: Products
""",
)

entry(
    index = 87,
    label = "CH3 + CH3 <=> C2H6-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.47e+07, 'm^3/(mol*s)', '+|-', 2.2e+06),
        n = 0,
        Ea = (-1.139, 'kJ/mol', '+|-', 0.274),
        T0 = (1, 'K'),
        Tmin = (296, 'K'),
        Tmax = (577, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (6666, 'Pa'),
    ),
    reference = Article(
        authors = ["Macpherson, M.T.", "Pilling, M.J.", "Smith, M.J.C."],
        title = u'Determination of the absorption cross section for CH3 at 216.36 nm and the absolute rate constant for methyl radical recombination over the temperature range 296-577 K',
        journal = "J. Phys. Chem.",
        volume = "89",
        pages = """2268-2274""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985MAC/PIL2268-2274:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000110.xml
Bath gas: Ar
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Gas chromatography
""",
)

entry(
    index = 88,
    label = "CH3 + CH3 <=> C2H6-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (200000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (-29.932, 'kJ/mol', '+|-', 5.687),
        T0 = (1, 'K'),
        Tmin = (1270, 'K'),
        Tmax = (2210, 'K'),
        Pmin = (72000, 'Pa'),
        Pmax = (72000, 'Pa'),
    ),
    reference = Article(
        authors = ["Moller, W.", "Mozzhukhin, E.", "Wagner, H.Gg."],
        title = u'High temperature reactions of CH3. 1. The reactions CH3 + H2 \u2192\x92 CH4 + H',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "90",
        pages = """854""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986MOL/MOZ854:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000114.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 89,
    label = "CH3 + CH3 <=> C2H6-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.06e+10, 'm^3/(mol*s)'),
        n = -1.18,
        Ea = (2.735, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (296, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (60000, 'Pa'),
    ),
    reference = Article(
        authors = ["Wagner, A.F.", "Wardlaw, D.M."],
        title = u'Study of the recombination reaction CH3 + CH3 \u2192\x92 C2H6. 2. Theory',
        journal = "J. Phys. Chem.",
        volume = "92",
        pages = """2462-2471""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988WAG/WAR2462-2471:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000119.xml
Bath gas: Ar
""",
)

entry(
    index = 90,
    label = "CH3 + CH3 <=> C2H6-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.69e+10, 'm^3/(mol*s)'),
        n = -1.11,
        Ea = (2.453, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Forst, W."],
        title = u'Microcanonical variational theory of radical recombination by inversion of interpolated partition function, with examples: CH3 + H, CH3 + CH3',
        journal = "J. Phys. Chem.",
        volume = "95",
        pages = """3612-3620""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991FOR3612-3620:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000122.xml
""",
)

entry(
    index = 91,
    label = "CH3 + CH3 <=> C2H6-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.37e+10, 'm^3/(mol*s)'),
        n = -1.1,
        Ea = (2.661, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1200, 'K'),
        Tmax = (1600, 'K'),
        Pmin = (1.01e+06, 'Pa'),
        Pmax = (2.43e+07, 'Pa'),
    ),
    reference = Article(
        authors = ["Hwang, S.M.", "Wagner, H.GG.", "Wolff, Th."],
        title = u'Recombination of CH3 radicals at elevated pressures and temperatures',
        journal = "Symp. Int. Combust. Proc.",
        volume = "23",
        pages = """99-105""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991HWA/WAG99-105:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000123.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 92,
    label = "CH3 + CH3 <=> C2H6-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.03e+10, 'm^3/(mol*s)'),
        n = -1.17,
        Ea = (2.661, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Walter, D.", "Grotheer, H-H."],
        title = u'Experimental and theoretical study of the recombination reaction CH3 + CH3 \u2192\x92 C2H6',
        journal = "Symp. Int. Combust. Proc.",
        volume = "23",
        pages = """107-114""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991WAL/GRO107-114:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000124.xml
Bath gas: Ar
""",
)

entry(
    index = 93,
    label = "CH3 + CH3 <=> C2H6-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.26e+10, 'm^3/(mol*s)'),
        n = -1.1,
        Ea = (1.33, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (296, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Robertson, S.H.", "Pilling, M.J.", "Baulch, D.L.", "Green, N.J.B."],
        title = u'Fitting of pressure-dependent kinetic rate data by master equation/inverse laplace transform analysis',
        journal = "J. Phys. Chem.",
        volume = "99",
        pages = """13452-13460""",
        year = "1995",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1995ROB/PIL13452-13460:1",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000128.xml
Bath gas: Ar
""",
)

entry(
    index = 94,
    label = "CH3 + CH3 <=> C2H6-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.06e+10, 'm^3/(mol*s)'),
        n = -1.2,
        Ea = (2.453, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (296, 'K'),
        Tmax = (1800, 'K'),
        Pmin = (122000, 'Pa'),
        Pmax = (122000, 'Pa'),
    ),
    reference = Article(
        authors = ["Du, H.", "Hessler, J.P.", "Ogren, P.J."],
        title = u'Recombination of methyl radicals. 1. New data between 1175 and 1750 K in the falloff region',
        journal = "J. Phys. Chem.",
        volume = "100",
        pages = """974-983""",
        year = "1996",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996DU/HES974-983:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000129.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 95,
    label = "CH3 + CH3 <=> C2H6-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.7e+11, 'm^3/(mol*s)'),
        n = -1.41,
        Ea = (4.177, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Pesa, M.", "Pilling, M.J.", "Robertson, S.H.", "Wardlaw, D.M."],
        title = u'Application of the canonical flexible transition state theory to CH3, CF3, and CCl3',
        journal = "J. Phys. Chem. A",
        volume = "102",
        pages = """8526-8536""",
        year = "1998",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1998PES/PIL8526-8536:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000131.xml
Pressure dependence: Rate constant is high pressure limit
""",
)

entry(
    index = 96,
    label = "CH3 + CH3 <=> C2H6-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.28e+09, 'm^3/(mol*s)'),
        n = -0.69,
        Ea = (0.732, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (1350, 'K'),
    ),
    reference = Article(
        authors = ["Wang, B.S.", "Hou, H.", "Yoder, L.M.", "Muckerman, J.T.", "Fockenberg, C."],
        title = u'Experimental and theoretical investigations on the methyl-methyl recombination reaction',
        journal = "J. Phys. Chem. A:",
        volume = "107",
        pages = """11414-11426""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003WAN/HOU11414-11426:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002085
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002085/rk00000159.xml
Pressure dependence: Rate constant is high pressure limit
Experimental procedure: Static or low flow - Data taken vs time
Excitation technique: Flash photolysis (laser or conventional)
Time resolution: In real time
Analytical technique: Mass spectrometry

Rate expressions given here are NOT the exact experimental values, but from TST calculations consistent with experimental measurements.  Derived Fcent(T) = exp(-T/570K)

This work is a combined experimental, TST, and ab initio study of recombination of CH3 radicals. Methyl radicals produced by 193 nm photolysis of acetone. Temperature range 300-700 K. Total pressure 0.6-10 torr He. Detected CH3 with time resolved mass spec. Calculated potential energy surface using ab initio MRCISD+Q/aug-cc-pVTZ method. Used variational transition state theory (Variflex program) to derive high pressure and low pressure limits (and falloff parameter Fcent) for this reaction that are consistent with the experimental measurements.
""",
)

entry(
    index = 97,
    label = "O2 + H <=> HO2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (-5.438, 'kJ/mol', '+|-', 2.07),
        T0 = (1, 'K'),
        Tmin = (733, 'K'),
        Tmax = (803, 'K'),
    ),
    reference = Article(
        authors = ["Baldwin, R.R.", "Jackson, D.", "Walker, R.W.", "Webster, S.J."],
        title = u'Interpretation of the slow reaction and second limit of hydrogen oxygen mixtures by computer methods',
        journal = "Trans. Faraday Soc.",
        volume = "63",
        pages = """1676-1686""",
        year = "1967",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1967BAL/JAC1676-1686:10",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00011821
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011821/rk00000017.xml
Bath gas: H2
""",
)

entry(
    index = 98,
    label = "O2 + H <=> HO2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (87900, 'm^3/(mol*s)'),
        n = 1,
        Ea = (1.862, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    reference = Article(
        authors = ["Duchovic, R.J.", "Pettigrew, J.D.", "Welling, B.", "Shipchandler, T."],
        title = u'Conventional transition state theory/Rice-Ramsperger-Kassel-Marcus theory calculations of thermal termolecular rate coefficients for H(D)+O2+M',
        journal = "J. Chem. Phys.",
        volume = "105",
        pages = """10367-10379""",
        year = "1996",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996DUC/PET10367-10379:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011821
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011821/rk00000022.xml
Bath gas: Ar
""",
)

entry(
    index = 99,
    label = "O2 + H <=> HO2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.63e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (3.184, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = Article(
        authors = ["Cobos, C.J.", "Troe, J."],
        title = u'Theory of thermal unimolecular reactions at high pressures. II. Analysis of experimental results',
        journal = "J. Chem. Phys.",
        volume = "83",
        pages = """1010-1015""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985COB/TRO1010-1015:17",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00011821
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011821/rk00000020.xml
Bath gas: Products
""",
)

entry(
    index = 100,
    label = "H2O2 <=> OH + OH",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.41e+11, 's^-1'),
        n = 0,
        Ea = (165.458, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (740, 'K'),
        Tmax = (794, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["McLane, C.K."],
        title = u'Hydrogen peroxide in the thermal hydrogen oxygen reaction. I. Thermal decomposition of hydrogen peroxide',
        journal = "J. Chem. Phys.",
        volume = "17",
        pages = """379-385""",
        year = "1949",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1949MCL379-385:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00013690
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013690/rk00000001.xml
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 101,
    label = "H2O2 <=> OH + OH",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.14e+10, 's^-1'),
        n = 0,
        Ea = (167.952, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (762, 'K'),
        Tmax = (815, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["McLane, C.K."],
        title = u'Hydrogen peroxide in the thermal hydrogen oxygen reaction. I. Thermal decomposition of hydrogen peroxide',
        journal = "J. Chem. Phys.",
        volume = "17",
        pages = """379-385""",
        year = "1949",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1949MCL379-385:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00013690
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013690/rk00000002.xml
Bath gas: O2
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 102,
    label = "H2O2 <=> OH + OH",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+13, 's^-1'),
        n = 0,
        Ea = (201.21, 'kJ/mol', '+|-', 12.056),
        T0 = (1, 'K'),
        Tmin = (673, 'K'),
        Tmax = (773, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (2666, 'Pa'),
    ),
    reference = Article(
        authors = ["Giguere, P.A.", "Liu, I.D."],
        title = u'Kinetics of the thermal decomposition of hydrogen peroxide vapor',
        journal = "Can. J. Chem.",
        volume = "35",
        pages = """283-293""",
        year = "1957",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1957GIG/LIU283-293:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00013690
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013690/rk00000003.xml
Bath gas: H2O2
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 103,
    label = "H2O2 <=> OH + OH",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.95e+14, 's^-1'),
        n = 0,
        Ea = (202.873, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = Article(
        authors = ["Brouwer, L.", "Cobos, C.J.", "Troe, J.", "Dubal, H.-R.", "Crim, F.F."],
        title = u'Specific rate constants k(E,J) and product state distributions in simple bond fission reactions. II. Application to HOOH \u2192\x92 OH + OH',
        journal = "J. Chem. Phys.",
        volume = "86",
        pages = """6171""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987BRO/COB6171:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Other theoretical""",
    longDesc = 
u"""
PrIMe Reaction: r00013690
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013690/rk00000018.xml
""",
)

entry(
    index = 104,
    label = "C3H8 <=> C3H7 + H",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.31e+15, 's^-1'),
        n = 0,
        Ea = (396.6, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002698
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002698/rk00000001.xml
""",
)

entry(
    index = 105,
    label = "C3H8-2 <=> C3H7-2 + H",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1.58e+16, 's^-1'),
        n = 0,
        Ea = (408.241, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002699
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002699/rk00000001.xml
""",
)

entry(
    index = 106,
    label = "C3H8-3 <=> C2H5 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.1e+17, 's^-1', '*|/', 2),
        n = 0,
        Ea = (353.365, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Frank, P.", "Hayman, G.", "Just, Th.", "Kerr, J.A.", "Murrells, T.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combusion modelling. Supplement I',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "23",
        pages = """847-1033""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994BAU/COB847-1033:34",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Uncertainty: 2.0
""",
)

entry(
    index = 107,
    label = "C3H8-3 <=> C2H5 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.9e+22, 's^-1', '*|/', 1.5),
        n = -1.8,
        Ea = (370.825, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988TSA887:15",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Uncertainty: 1.5
""",
)

entry(
    index = 108,
    label = "C3H8-3 <=> C2H5 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5e+15, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (350.039, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (800, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:41",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Uncertainty: 3.1600001
""",
)

entry(
    index = 109,
    label = "C3H8-3 <=> C2H5 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.5e+16, 's^-1', '*|/', 2),
        n = 0,
        Ea = (365.837, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1200, 'K'),
        Tmax = (1450, 'K'),
        Pmin = (203000, 'Pa'),
        Pmax = (304000, 'Pa'),
    ),
    reference = Article(
        authors = ["Chiang, C.-C.", "Skinner, G.B."],
        title = u'Resonance Absorption Measurements of Atom Concentrations in Reacting Gas Mixtures 5. Pyrolysis of C3H8 and C3D8 Behind Shock Waves',
        journal = "Symp. Int. Combust. Proc.",
        volume = "18",
        pages = """915""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981CHI/SKI915:1",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Uncertainty: 2.0
Bath gas: Ar
""",
)

entry(
    index = 110,
    label = "C3H8-3 <=> C2H5 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.29e+37, 's^-1'),
        n = -5.84,
        Ea = (407.492, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (1653, 'K'),
        Pmin = (13200, 'Pa'),
        Pmax = (851000, 'Pa'),
    ),
    reference = Article(
        authors = ["Oehlschlaeger, M.A.", "Davidson, D.F.", "Hanson, R.K."],
        title = u'High-temperature ethane and propane decomposition',
        journal = "Proc. Combust. Inst.",
        volume = "30",
        pages = """1119-1127""",
        year = "2005",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2005OEH/DAV1119-1127:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Pressure dependence: Rate constant is high pressure limit
Experimental procedure: Shock tube
Excitation technique: Thermal
Time resolution: In real time
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 111,
    label = "C3H8-3 <=> C2H5 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.5e+16, 's^-1', '*|/', 2.5),
        n = 0,
        Ea = (338, 'kJ/mol', '+|-', 19),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1100, 'K'),
        Pmin = (500, 'Pa'),
        Pmax = (500, 'Pa'),
    ),
    reference = Article(
        authors = ["Gladky, A.Yu.", "Ermolaev, V.K.", "Parmon, V.N."],
        title = u'Temperature Dependence of Chain Initiation in Pyrolysis of Propane Studied by Direct Mass-Spectrometric Detection of Methyl Radicals',
        journal = "React. Kinet. Catal. Lett.",
        volume = "67",
        pages = """183-189""",
        year = "1999",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1999GLA/ERM183-189:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Uncertainty: 2.5
Experimental procedure: Flow tube - Data taken vs distance
Excitation technique: Thermal
Time resolution: In real time
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 112,
    label = "C3H8-3 <=> C2H5 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.86e+17, 's^-1', '*|/', 10),
        n = 0,
        Ea = (364.174, 'kJ/mol', '+|-', 14.55),
        T0 = (1, 'K'),
        Tmin = (743, 'K'),
        Tmax = (803, 'K'),
        Pmin = (2666, 'Pa'),
        Pmax = (10700, 'Pa'),
    ),
    reference = Article(
        authors = ["Belmeliani, A.", "Perrin, D.", "Martin, R."],
        title = u"Etude cinetique de l'ethane forme dans la pyrolyse homogene du propane et mesure de la constante de vitesse d'amorcage",
        journal = "J. Chim. Phys.",
        volume = "91",
        pages = """313-328""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994BEL/PER313-328:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Uncertainty: 10.0
Bath gas: C3H8
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 113,
    label = "C3H8-3 <=> C2H5 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.89e+22, 's^-1'),
        n = -1.79,
        Ea = (370.825, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (773, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Rate constants for the decomposition and formation of simple alkanes over extended temperature and pressure ranges',
        journal = "Combust. Flame",
        volume = "78",
        pages = """71-86""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989TSA71-86:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Bath gas: Ar
""",
)

entry(
    index = 114,
    label = "C3H8-3 <=> C2H5 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.1e+16, 's^-1'),
        n = 0,
        Ea = (351.702, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1100, 'K'),
        Tmax = (1450, 'K'),
        Pmin = (152000, 'Pa'),
        Pmax = (264000, 'Pa'),
    ),
    reference = Article(
        authors = ["Hidaka, Y.", "Oki, T.", "Kawano, H."],
        title = u'Thermal decomposition of propane in shock waves',
        journal = "Int. J. Chem. Kinet.",
        volume = "21",
        pages = """689-701""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989HID/OKI689-701:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 115,
    label = "C3H8-3 <=> C2H5 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.12e+17, 's^-1', '*|/', 5),
        n = 0,
        Ea = (355.859, 'kJ/mol', '+|-', 10.643),
        T0 = (1, 'K'),
        Tmin = (760, 'K'),
        Tmax = (830, 'K'),
        Pmin = (2000, 'Pa'),
        Pmax = (4933, 'Pa'),
    ),
    reference = Article(
        authors = ["Dombi, A.", "Horvath, I.", "Huhn, P."],
        title = u'Effects of olefins on the thermal decomposition of propane. Part III. Some remarks on the kinetics of decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "18",
        pages = """255""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986DOM/HOR255:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Uncertainty: 5.0
Bath gas: CO2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 116,
    label = "C3H8-3 <=> C2H5 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.94e+16, 's^-1'),
        n = 0,
        Ea = (357.522, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:7",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
""",
)

entry(
    index = 117,
    label = "C3H8-3 <=> C2H5 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5.13e+16, 's^-1', '*|/', 5),
        n = 0,
        Ea = (349.208, 'kJ/mol', '+|-', 6.976),
        T0 = (1, 'K'),
        Tmin = (773, 'K'),
        Tmax = (973, 'K'),
        Pmin = (26700, 'Pa'),
        Pmax = (33300, 'Pa'),
    ),
    reference = Article(
        authors = ["Kanan, K.", "Purnell, H.", "Smith, E."],
        title = u'Induced heterogeneity, a novel technique for the study of gas-phase reactions. Part I. Determination of the Arrhenius parameters for C-C bond scission in propane',
        journal = "Int. J. Chem. Kinet.",
        volume = "15",
        pages = """63""",
        year = "1983",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1983KAN/PUR63:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Uncertainty: 5.0
Bath gas: C3H8
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 118,
    label = "C3H8-3 <=> C2H5 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.74e+11, 's^-1', '+|-', 1.5e+11),
        n = 0,
        Ea = (232.805, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1400, 'K'),
        Tmax = (1800, 'K'),
        Pmin = (13300, 'Pa'),
        Pmax = (69300, 'Pa'),
    ),
    reference = Article(
        authors = ["Al-Alami, M.Z.", "Kiefer, J.H."],
        title = u'Shock-tube study of propane pyrolysis. Rate of initial dissociation from 1400 to 2300 K',
        journal = "J. Phys. Chem.",
        volume = "87",
        pages = """499""",
        year = "1983",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1983ALA/KIE499:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Bath gas: Kr
Excitation technique: Thermal
Analytical technique: Laser schlieren
""",
)

entry(
    index = 119,
    label = "C3H8-3 <=> C2H5 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.48e+17, 's^-1'),
        n = 0,
        Ea = (361.68, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1400, 'K'),
        Tmax = (1700, 'K'),
        Pmin = (13300, 'Pa'),
        Pmax = (69300, 'Pa'),
    ),
    reference = Article(
        authors = ["Al-Alami, M.Z.", "Kiefer, J.H."],
        title = u'Shock-tube study of propane pyrolysis. Rate of initial dissociation from 1400 to 2300 K',
        journal = "J. Phys. Chem.",
        volume = "87",
        pages = """499""",
        year = "1983",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1983ALA/KIE499:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Bath gas: Kr
Excitation technique: Thermal
Analytical technique: Laser schlieren
""",
)

entry(
    index = 120,
    label = "C3H8-3 <=> C2H5 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.47e+16, 's^-1'),
        n = 0,
        Ea = (354.197, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (873, 'K'),
        Tmax = (1050, 'K'),
        Pmin = (26700, 'Pa'),
        Pmax = (26700, 'Pa'),
    ),
    reference = Article(
        authors = ["Juste, C.", "Scacchi, G.", "Niclause, M."],
        title = u'Minor Products and Initiation Rate in the Chain Pyrolysis of Propane',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """855""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981JUS/SCA855:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 121,
    label = "C3H8-3 <=> C2H5 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.7e+16, 's^-1'),
        n = 0,
        Ea = (377.477, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1200, 'K'),
        Tmax = (1450, 'K'),
        Pmin = (203000, 'Pa'),
        Pmax = (304000, 'Pa'),
    ),
    reference = Article(
        authors = ["Chiang, C.-C.", "Skinner, G.B."],
        title = u'Resonance Absorption Measurements of Atom Concentrations in Reacting Gas Mixtures 5. Pyrolysis of C3H8 and C3D8 Behind Shock Waves',
        journal = "Symp. Int. Combust. Proc.",
        volume = "18",
        pages = """915""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981CHI/SKI915:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 122,
    label = "C3H8-3 <=> C2H5 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.5e+16, 's^-1', '*|/', 1.41),
        n = 0,
        Ea = (365.837, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1200, 'K'),
        Tmax = (1450, 'K'),
        Pmin = (203000, 'Pa'),
        Pmax = (304000, 'Pa'),
    ),
    reference = Article(
        authors = ["Chiang, C.", "Skinner, G.B."],
        title = u'Resonance absorption measurements of atom concentrations in reacting gas mixtures. 5. Pyrolysis of propane and propane-D8 behind shock waves',
        journal = "Report by Wright State University, Dept. of Chemistry, Dayton, OH 45435",
        pages = """1-18""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979CHI/SKI1-18:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Uncertainty: 1.41
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 123,
    label = "C3H8-3 <=> C2H5 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.58e+14, 's^-1'),
        n = 0,
        Ea = (281.029, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (803, 'K'),
        Tmax = (943, 'K'),
        Pmin = (2000, 'Pa'),
        Pmax = (80000, 'Pa'),
    ),
    reference = Article(
        authors = ["Laidler, K.J.", "Sagert, N.H.", "Wojciechowski, B.W."],
        title = u'Kinetics and mechanisms of the thermal decomposition of propane. I. The uninhibited reaction',
        journal = "Proc. R. Soc. London A",
        volume = "270",
        pages = """242""",
        year = "1962",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1962LAI/SAG242:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Bath gas: C3H8
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 124,
    label = "C3H8-3 <=> C2H5 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (8.89e+22, 's^-1'),
        n = -1.67,
        Ea = (382.773, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
    ),
    reference = Article(
        authors = ["Zhu, R.S.", "Xu, Z.F.", "Lin, M.C."],
        title = u'Ab initio studies of alkyl radical reactions: Combination and disproportionation reactions of CH3 with C2H5, and the decomposition of chemically activated C3H8',
        journal = "J. Chem. Phys.",
        volume = "120",
        pages = """6566-6573""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004ZHU/XU6566-6573:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Pressure dependence: Rate constant is high pressure limit

The CH3 + C2H5 reaction was investigated by the modified Gaussian-2 method with variational transition state or Rice-Ramsperger-Kassel-Marcus calculations. Vibrational frequencies and moments of inertia of all species used in RRKM calculations were computed at the B3LYP/6-311G(3df,2p) level and are reported.

The results suggest the combination process dominates below 600 K and is pressure independent under typical experimental conditions. The disproportionation process producing CH4 and C2H4 is suggested to occur via a loose hydrogen-bonded precursor, H3C---HC2H4 , which fragments with a small ~1.9 kcal/mol! barrier giving rise to the products. The disproportionation and combination reactions are concluded to occur with entirely different transition states. Calculated rate constants are in ggod agreement with experimental values.
""",
)

entry(
    index = 125,
    label = "C3H8-3 <=> C2H5 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.1e+17, 's^-1'),
        n = 0,
        Ea = (369.1, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Mousavipour, S.H.", "Homayoon, Z."],
        title = u'A Theoretical Study on the Kinetics of Disproportionation Versus Association Reaction of CH3 + C2H5',
        journal = "J. Phys. Chem. A",
        volume = "107",
        pages = """8566-8574""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MOU/HOM8566-8574:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Pressure dependence: Rate constant is high pressure limit

The authors studied the CH3 + C2H5 system using theoretical methods. Potential energy surfaces were explored by UMP2, CAS, QCISD, and DFT methods. Stationary point energies were calculated by CASMP2, B3LYP, MP4SDTQ, and QCISD methods. Canonical variational transition-state theory and microcanonical variational RRKM calculations were used to locate the position of bottleneck for the association reaction of methyl and ethyl radicals. The pressure dependency of the rate constants for dissociation of propane and association of methyl and ethyl radicals was examined using RRKM methods. Conventional transition-state theory was used to calculate the rate constant for CH3 + C2H5 = CH4 + C2H4 in the temperature range of 200-2500 K.
""",
)

entry(
    index = 126,
    label = "C3H8-3 <=> C2H5 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5.01e+16, 's^-1'),
        n = 0,
        Ea = (355.028, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (760, 'K'),
        Tmax = (766, 'K'),
        Pmin = (13300, 'Pa'),
        Pmax = (13300, 'Pa'),
    ),
    reference = Article(
        authors = ["Jezequel, J-Y.", "Baronnet, F.", "Niclause, M."],
        title = u'Modelisation de la pyrolyse du propane',
        journal = "J. Chim. Phys.",
        volume = "75",
        pages = """991-993""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978JEZ/BAR991-993:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Bath gas: C3H8
""",
)

entry(
    index = 127,
    label = "C3H8-3 <=> C2H5 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.74e+14, 's^-1'),
        n = 0,
        Ea = (300.152, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1130, 'K'),
        Tmax = (1250, 'K'),
        Pmin = (40000, 'Pa'),
        Pmax = (133000, 'Pa'),
    ),
    reference = Article(
        authors = ["Kao, W.", "Yeh, C."],
        title = u'The role of the termination reaction H + CH3 \u2192\x92 CH4 in the pyrolysis of propane in the temperature range 1100-1300 K',
        journal = "J. Chem. Phys.",
        volume = "81",
        pages = """2304-2306""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977KAO/YEH2304-2306:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
""",
)

entry(
    index = 128,
    label = "C3H8-3 <=> C2H5 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.16e+16, 's^-1'),
        n = 0,
        Ea = (335.073, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1962BLA/HIN36:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002700/rk00000001.xml
""",
)

entry(
    index = 129,
    label = "C2H5 + CH3 <=> C3H8-3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (8.91e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (-7.109, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (773, 'K'),
        Tmax = (793, 'K'),
        Pmin = (26700, 'Pa'),
        Pmax = (26700, 'Pa'),
    ),
    reference = Article(
        authors = ["Kanan, K.", "Purnell, H.", "Smith, E."],
        title = u'Induced heterogeneity, a novel technique for the study of gas-phase reactions. Part I. Determination of the Arrhenius parameters for C-C bond scission in propane',
        journal = "Int. J. Chem. Kinet.",
        volume = "15",
        pages = """63""",
        year = "1983",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1983KAN/PUR63:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from detailed balance/reverse rate""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Bath gas: C3H8
""",
)

entry(
    index = 130,
    label = "C2H5 + CH3 <=> C3H8-3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (80000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (-47.392, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1300, 'K'),
        Tmax = (1700, 'K'),
        Pmin = (37200, 'Pa'),
        Pmax = (37200, 'Pa'),
    ),
    reference = Article(
        authors = ["Simmie, J.M.", "Gardiner, W.C., Jr.", "Eubank, C.S."],
        title = u'Falloff Behavior in Propane Thermal Decomposition at High Temperature',
        journal = "J. Phys. Chem.",
        volume = "86",
        pages = """799""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982SIM/GAR799:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: IR absorption
""",
)

entry(
    index = 131,
    label = "C2H5 + CH3 <=> C3H8-3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.51e+07, 'm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (1.671, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972TEN/JON1267:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Uncertainty: 2.0
Bath gas: H2
Excitation technique: Electron beam
Analytical technique: Gas chromatography
""",
)

entry(
    index = 132,
    label = "C2H5 + CH3 <=> C3H8-3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.45e+08, 'm^3/(mol*s)'),
        n = -0.34,
        Ea = (-2.153, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
    ),
    reference = Article(
        authors = ["Zhu, R.S.", "Xu, Z.F.", "Lin, M.C."],
        title = u'Ab initio studies of alkyl radical reactions: Combination and disproportionation reactions of CH3 with C2H5, and the decomposition of chemically activated C3H8',
        journal = "J. Chem. Phys.",
        volume = "120",
        pages = """6566-6573""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004ZHU/XU6566-6573:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Pressure dependence: Rate constant is high pressure limit

The CH3 + C2H5 reaction was investigated by the modified Gaussian-2 method with variational transition state or Rice-Ramsperger-Kassel-Marcus calculations. Vibrational frequencies and moments of inertia of all species used in RRKM calculations were computed at the B3LYP/6-311G(3df,2p) level and are reported.

The results suggest the combination process dominates below 600 K and is pressure independent under typical experimental conditions. The disproportionation process producing CH4 and C2H4 is suggested to occur via a loose hydrogen-bonded precursor, H3C---HC2H4 , which fragments with a small ~1.9 kcal/mol! barrier giving rise to the products. The disproportionation and combination reactions are concluded to occur with entirely different transition states. Calculated rate constants are in ggod agreement with experimental values.
""",
)

entry(
    index = 133,
    label = "C2H5 + CH3 <=> C3H8-3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5.5e+08, 'm^3/(mol*s)'),
        n = -0.56,
        Ea = (-0.53, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Mousavipour, S.H.", "Homayoon, Z."],
        title = u'A Theoretical Study on the Kinetics of Disproportionation Versus Association Reaction of CH3 + C2H5',
        journal = "J. Phys. Chem. A",
        volume = "107",
        pages = """8566-8574""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MOU/HOM8566-8574:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00002700
Pressure dependence: Rate constant is high pressure limit

The authors studied the CH3 + C2H5 system using theoretical methods. Potential energy surfaces were explored by UMP2, CAS, QCISD, and DFT methods. Stationary point energies were calculated by CASMP2, B3LYP, MP4SDTQ, and QCISD methods. Canonical variational transition-state theory and microcanonical variational RRKM calculations were used to locate the position of bottleneck for the association reaction of methyl and ethyl radicals. The pressure dependency of the rate constants for dissociation of propane and association of methyl and ethyl radicals was examined using RRKM methods. Conventional transition-state theory was used to calculate the rate constant for CH3 + C2H5 = CH4 + C2H4 in the temperature range of 200-2500 K.
""",
)

entry(
    index = 134,
    label = "C3H6 <=> C3H5 + H",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.5e+15, 's^-1', '*|/', 3),
        n = 0,
        Ea = (362.511, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:17",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00005623
Uncertainty: 3.0
Bath gas: Products
""",
)

entry(
    index = 135,
    label = "C3H6 <=> C3H5 + H",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (5.01e+12, 's^-1'),
        n = 0,
        Ea = (296.827, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996BAR/MAR829-847:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005623
Bath gas: CH3CH=CH2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 136,
    label = "C3H6 <=> C3H5 + H",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (4.57e+14, 's^-1'),
        n = 0,
        Ea = (371.657, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986NAR/NIE281:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00005623
""",
)

entry(
    index = 137,
    label = "C3H6 <=> C3H5 + H",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1.1e+11, 's^-1'),
        n = 0,
        Ea = (300.984, 'kJ/mol', '+|-', 12.056),
        T0 = (1, 'K'),
        Tmin = (953, 'K'),
        Tmax = (1140, 'K'),
        Pmin = (267, 'Pa'),
        Pmax = (1867, 'Pa'),
    ),
    reference = Article(
        authors = ["Szwarc, M."],
        title = u'The kinetics of the thermal decomposition of propylene',
        journal = "J. Chem. Phys.",
        volume = "17",
        pages = """284-291""",
        year = "1949",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1949SZW284-291:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005623
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00005623/rk00000001.xml
Bath gas: CH3CH=CH2
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 138,
    label = "C3H6 <=> C3H5 + H",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (5e+13, 's^-1'),
        n = 0,
        Ea = (335.073, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1200, 'K'),
        Tmax = (1800, 'K'),
    ),
    reference = Article(
        authors = ["Hidaka, Y.", "Nakamura, T.", "Tanaka, H.", "Jinno, A.", "Kawano, H."],
        title = u'Shock tube and modeling study of propene pyrolysis',
        journal = "Int. J. Chem. Kinet.",
        volume = "24",
        pages = """761-780""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992HID/NAK761-780:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00005623
""",
)

entry(
    index = 139,
    label = "C3H5 + H <=> C3H6",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (5.83e+07, 'm^3/(mol*s)'),
        n = 0.18,
        Ea = (-0.524, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Harding, L.B.", "Klippenstein, S.J.", "Georgievskii, Y."],
        title = u'On the combination reactions of hydrogen atoms with resonance-stabilized hydrocarbon radicals',
        journal = "J. Phys. Chem. A",
        volume = "111",
        pages = """3789-3801""",
        year = "2007",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2007HAR/KLI3789-3801:5",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00005623
""",
)

entry(
    index = 140,
    label = "C2H6O <=> CH3O + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.28e+35, 's^-1'),
        n = -5.89,
        Ea = (375.347, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (1350, 'K'),
        Pmin = (1.01e+06, 'Pa'),
        Pmax = (1.01e+06, 'Pa'),
    ),
    reference = Article(
        authors = ["Zhao, Z.", "Chaos, M.", "Kazakov, A.", "Dryer, F.L."],
        title = u'Thermal decomposition reaction and a comprehensive kinetic model of dimethyl ether',
        journal = "Int. J. Chem. Kinet.",
        volume = "40",
        pages = """1-18""",
        year = "2008",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2008ZHA/CHA1-18:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00010572
Experimental procedure: Stirred flow reactor(PSR etc.)
Time resolution: In real time
Analytical technique: Fourier transform (FTIR)
""",
)

entry(
    index = 141,
    label = "C2H6O <=> CH3O + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.7e+42, 's^-1'),
        n = -7.95,
        Ea = (384.133, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (1350, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Zhao, Z.", "Chaos, M.", "Kazakov, A.", "Dryer, F.L."],
        title = u'Thermal decomposition reaction and a comprehensive kinetic model of dimethyl ether',
        journal = "Int. J. Chem. Kinet.",
        volume = "40",
        pages = """1-18""",
        year = "2008",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2008ZHA/CHA1-18:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00010572
Experimental procedure: Stirred flow reactor(PSR etc.)
Time resolution: In real time
Analytical technique: Fourier transform (FTIR)
""",
)

entry(
    index = 142,
    label = "C2H6O <=> CH3O + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.5e+14, 's^-1'),
        n = 0,
        Ea = (313.8, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (900, 'K'),
        Tmax = (1900, 'K'),
        Pmin = (84100, 'Pa'),
        Pmax = (294000, 'Pa'),
    ),
    reference = Article(
        authors = ["Hidaka, Y.", "Sato, K.", "Yamane, M."],
        title = u'High-temperature pyrolysis of dimethyl ether in shock waves',
        journal = "Combust. Flame",
        volume = "123",
        pages = """1-22""",
        year = "2000",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2000HID/SAT1-22:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010572
Experimental procedure: Shock tube
Time resolution: In real time
Analytical technique: Vis-UV absorption

The high-temperature pyrolysis of dimethyl ether (DME) was studied behind reflected shock waves using single-pulse (reaction time between 1.3 and 2.9 ms), time-resolved IR absorption (3.39 mm), IR emission (4.24mm), and UV absorption (216 nm) methods. The studies were done using DME-Ar, DME-H2-Ar, DME-CO-Ar and DME-CH2O-Ar mixtures. From a computer simulation, a 94-reaction mechanism that could explain all exp. data was constructed.
""",
)

entry(
    index = 143,
    label = "C2H6O <=> CH3O + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.16e+16, 's^-1'),
        n = 0,
        Ea = (347.545, 'kJ/mol', '+|-', 6.943),
        T0 = (1, 'K'),
        Tmin = (680, 'K'),
        Tmax = (850, 'K'),
        Pmin = (53300, 'Pa'),
        Pmax = (107000, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L.", "Alvarado-Salinas, G.", "Reid, I.A.B.", "Robinson, C.", "Smith, D.B."],
        title = u'The Pyrolysis of Dimethyl Ether and Formaldehyde',
        journal = "Symp. Int. Combust. Proc.",
        volume = "19",
        pages = """81""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982BAT/ALV81:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010572
Bath gas: CH4
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 144,
    label = "C2H6O <=> CH3O + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.16e+15, 's^-1', '*|/', 2.51),
        n = 0,
        Ea = (320.107, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1060, 'K'),
        Tmax = (1220, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Aronowitz, D.", "Naegeli, D."],
        title = u'High-Temperature Pyrolysis of Dimethyl Ether',
        journal = "Int. J. Chem. Kinet.",
        volume = "9",
        pages = """471""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977ARO/NAE471:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010572
Uncertainty: 2.51
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 145,
    label = "C2H6O <=> CH3O + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1e+15, 's^-1', '*|/', 2.51),
        n = 0,
        Ea = (317.613, 'kJ/mol', '+|-', 9.562),
        T0 = (1, 'K'),
        Tmin = (782, 'K'),
        Tmax = (936, 'K'),
        Pmin = (3333, 'Pa'),
        Pmax = (52700, 'Pa'),
    ),
    reference = Article(
        authors = ["Pacey, P.D."],
        title = u'The Initial Stages of the Pyrolysis of Dimethyl Ether',
        journal = "Can. J. Chem.",
        volume = "53",
        pages = """2742""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975PAC2742:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010572
Uncertainty: 2.51
Bath gas: (CH3)2O
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 146,
    label = "C2H6O <=> CH3O + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.26e+18, 's^-1'),
        n = 0,
        Ea = (339.23, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (750, 'K'),
        Tmax = (820, 'K'),
        Pmin = (4666, 'Pa'),
        Pmax = (53300, 'Pa'),
    ),
    reference = Article(
        authors = ["Benson, S.W.", "Jain, D.V.S."],
        title = u'Further studies of the pyrolysis of dimethyl ether',
        journal = "J. Chem. Phys.",
        volume = "31",
        pages = """1008""",
        year = "1959",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1959BEN/JAI1008:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010572
Bath gas: (CH3)2O
""",
)

entry(
    index = 147,
    label = "C2H6O <=> CH3O + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.1e+16, 's^-1'),
        n = 0,
        Ea = (339.23, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (770, 'K'),
        Tmax = (785, 'K'),
        Pmin = (10400, 'Pa'),
        Pmax = (67900, 'Pa'),
    ),
    reference = Article(
        authors = ["Benson, S.W."],
        title = u'Pyrolysis of dimethyl ether',
        journal = "J. Chem. Phys.",
        volume = "25",
        pages = """27-31""",
        year = "1956",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1956BEN27-31:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010572
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010572/rk00000003.xml
Bath gas: (CH3)2O
""",
)

entry(
    index = 148,
    label = "C2H6O-2 <=> CH3O-2 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.39e+42, 's^-1'),
        n = -7.71,
        Ea = (410.128, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004LI/KAZ7671-7680:12",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00010768
Pressure dependence: Rate constant is pressure dependent

The authors used a variable pressure flow reactor to study ethanol pyrolysis at 1.7-3.0 atm and 1045-1080 K in the presence of radical chain inhibitor. Rate constants were presented graphically but the numerical results from the experiments were NOT reported.

The authors used their data together with that from the literature to perform a master equation multi-channel RRKM analysis and derive the reported rate constants based on their model.
""",
)

entry(
    index = 149,
    label = "C2H6O-2 <=> CH3O-2 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.07e+32, 's^-1'),
        n = -4.63,
        Ea = (391.795, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004LI/KAZ7671-7680:13",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00010768
Pressure dependence: Rate constant is pressure dependent

The authors used a variable pressure flow reactor to study ethanol pyrolysis at 1.7-3.0 atm and 1045-1080 K in the presence of radical chain inhibitor. Rate constants were presented graphically but the numerical results from the experiments were NOT reported.

The authors used their data together with that from the literature to perform a master equation multi-channel RRKM analysis and derive the reported rate constants based on their model.
""",
)

entry(
    index = 150,
    label = "C2H6O-2 <=> CH3O-2 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.2e+22, 's^-1'),
        n = -1.93,
        Ea = (373.237, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Li, J.", "Kazakov, A.", "Dryer, F.L."],
        title = u'Experimental and numerical studies of ethanol decomposition reactions',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """7671-7680""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004LI/KAZ7671-7680:14",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00010768
Pressure dependence: Rate constant is high pressure limit

The authors used a variable pressure flow reactor to study ethanol pyrolysis at 1.7-3.0 atm and 1045-1080 K in the presence of radical chain inhibitor. Rate constants were presented graphically but the numerical results from the experiments were NOT reported.

The authors used their data together with that from the literature to perform a master equation multi-channel RRKM analysis and derive the reported rate constants based on their model.
""",
)

entry(
    index = 151,
    label = "C2H6O-2 <=> CH3O-2 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.58e+50, 's^-1'),
        n = -11.45,
        Ea = (412.531, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004LI/KAZ7671-7680:9",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00010768
Pressure dependence: Rate constant is pressure dependent

The authors used a variable pressure flow reactor to study ethanol pyrolysis at 1.7-3.0 atm and 1045-1080 K in the presence of radical chain inhibitor. Rate constants were presented graphically but the numerical results from the experiments were NOT reported.

The authors used their data together with that from the literature to perform a master equation multi-channel RRKM analysis and derive the reported rate constants based on their model.
""",
)

entry(
    index = 152,
    label = "C2H6O-2 <=> CH3O-2 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.59e+54, 's^-1'),
        n = -11.99,
        Ea = (420.513, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004LI/KAZ7671-7680:10",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00010768
Pressure dependence: Rate constant is pressure dependent

The authors used a variable pressure flow reactor to study ethanol pyrolysis at 1.7-3.0 atm and 1045-1080 K in the presence of radical chain inhibitor. Rate constants were presented graphically but the numerical results from the experiments were NOT reported.

The authors used their data together with that from the literature to perform a master equation multi-channel RRKM analysis and derive the reported rate constants based on their model.
""",
)

entry(
    index = 153,
    label = "C2H6O-2 <=> CH3O-2 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.41e+34, 's^-1'),
        n = -9.16,
        Ea = (538.37, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004LI/KAZ7671-7680:8",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00010768
Pressure dependence: Rate constant is pressure dependent

The authors used a variable pressure flow reactor to study ethanol pyrolysis at 1.7-3.0 atm and 1045-1080 K in the presence of radical chain inhibitor. Rate constants were presented graphically but the numerical results from the experiments were NOT reported.

The authors used their data together with that from the literature to perform a master equation multi-channel RRKM analysis and derive the reported rate constants based on their model.
""",
)

entry(
    index = 154,
    label = "C2H6O-2 <=> CH3O-2 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+51, 's^-1'),
        n = -10.59,
        Ea = (422.034, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004LI/KAZ7671-7680:11",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00010768
Pressure dependence: Rate constant is pressure dependent

The authors used a variable pressure flow reactor to study ethanol pyrolysis at 1.7-3.0 atm and 1045-1080 K in the presence of radical chain inhibitor. Rate constants were presented graphically but the numerical results from the experiments were NOT reported.

The authors used their data together with that from the literature to perform a master equation multi-channel RRKM analysis and derive the reported rate constants based on their model.
""",
)

entry(
    index = 155,
    label = "C2H6O-2 <=> CH3O-2 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.61e+23, 's^-1'),
        n = -2.16,
        Ea = (368.364, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004TSA456-465:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010768
Pressure dependence: Rate constant is high pressure limit

Results are based on a review and analysis of the literature data. The article discusses the multi-channel nature of ethanol decomposition and difficulties associated with expressing the rate constants in a convenient analytical form over extended temperature and pressure ranges.

Some analytical formats for intermediate pressures are also given in the paper but are too complex to reproduce here.
""",
)

entry(
    index = 156,
    label = "C2H6O-2 <=> CH3O-2 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.94e+23, 's^-1'),
        n = -1.68,
        Ea = (381.634, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1999MAR183-220:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010768
""",
)

entry(
    index = 157,
    label = "C2H6O-2 <=> CH3O-2 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+16, 's^-1'),
        n = 0,
        Ea = (353.365, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976TSA173:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010768
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010768/rk00000002.xml
Bath gas: Ar
""",
)

entry(
    index = 158,
    label = "C2H4O <=> CHO + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7e+15, 's^-1', '*|/', 2.5),
        n = 0,
        Ea = (341.725, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (750, 'K'),
        Tmax = (1200, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combustion modelling',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """411-429""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992BAU/COB411-429:67",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010771
Uncertainty: 2.5
Bath gas: Products
""",
)

entry(
    index = 159,
    label = "C2H4O <=> CHO + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+15, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (330.916, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:50",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010771
Uncertainty: 3.1600001
""",
)

entry(
    index = 160,
    label = "C2H4O <=> CHO + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6e+14, 's^-1'),
        n = 0,
        Ea = (330.954, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1700, 'K'),
        Pmin = (122000, 'Pa'),
        Pmax = (284000, 'Pa'),
    ),
    reference = Article(
        authors = ["Yasunaga, K.", "Kubo, S.", "Hoshikawa, H.", "Kamesawa, T.", "Hidaka, Y."],
        title = u'Shock-tube and modeling study of acetaldehyde pyrolysis and oxidation',
        journal = "Int. J. Chem. Kinet.",
        volume = "40",
        pages = """73-102""",
        year = "2008",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2008YAS/KUB73-102:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010771
Experimental procedure: Shock tube
Time resolution: In real time
Analytical technique: Other (Vis-UV)

The reacted mixture was analyzed by gaschromatographic, IR-laser absorption, UV absorption and IR-emission equipments.
""",
)

entry(
    index = 161,
    label = "C2H4O <=> CHO + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.9e+14, 's^-1'),
        n = 0,
        Ea = (316.948, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1250, 'K'),
        Tmax = (1650, 'K'),
        Pmin = (130000, 'Pa'),
        Pmax = (130000, 'Pa'),
    ),
    reference = Article(
        authors = ["Bentz, T.", "Striebel, F.", "Olzmann, M."],
        title = u'Shock-tube study of the thermal decomposition of CH3CHO and CH3CHO+H reaction',
        journal = "J. Phys. Chem. A",
        volume = "112",
        pages = """6120-6124""",
        year = "2008",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2008BEN/STR6120-6124:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010771
Pressure dependence: Rate constant is pressure dependent
Experimental procedure: Shock tube
Time resolution: In real time
Analytical technique: Other (direct)
""",
)

entry(
    index = 162,
    label = "C2H4O <=> CHO + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.8e+14, 's^-1'),
        n = 0,
        Ea = (309.049, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1250, 'K'),
        Tmax = (1650, 'K'),
        Pmin = (290000, 'Pa'),
        Pmax = (290000, 'Pa'),
    ),
    reference = Article(
        authors = ["Bentz, T.", "Striebel, F.", "Olzmann, M."],
        title = u'Shock-tube study of the thermal decomposition of CH3CHO and CH3CHO+H reaction',
        journal = "J. Phys. Chem. A",
        volume = "112",
        pages = """6120-6124""",
        year = "2008",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2008BEN/STR6120-6124:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010771
Pressure dependence: Rate constant is pressure dependent
Experimental procedure: Shock tube
Time resolution: In real time
Analytical technique: Other (direct)
""",
)

entry(
    index = 163,
    label = "C2H4O <=> CHO + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.1e+14, 's^-1'),
        n = 0,
        Ea = (292.254, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1250, 'K'),
        Tmax = (1650, 'K'),
        Pmin = (450000, 'Pa'),
        Pmax = (450000, 'Pa'),
    ),
    reference = Article(
        authors = ["Bentz, T.", "Striebel, F.", "Olzmann, M."],
        title = u'Shock-tube study of the thermal decomposition of CH3CHO and CH3CHO+H reaction',
        journal = "J. Phys. Chem. A",
        volume = "112",
        pages = """6120-6124""",
        year = "2008",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2008BEN/STR6120-6124:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010771
Pressure dependence: Rate constant is pressure dependent
Experimental procedure: Shock tube
Time resolution: In real time
Analytical technique: Other (direct)
""",
)

entry(
    index = 164,
    label = "C2H4O <=> CHO + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.2e+16, 's^-1'),
        n = 0,
        Ea = (341.725, 'kJ/mol', '+|-', 3.417),
        T0 = (1, 'K'),
        Tmin = (1350, 'K'),
        Tmax = (1650, 'K'),
        Pmin = (20300, 'Pa'),
        Pmax = (7.4e+06, 'Pa'),
    ),
    reference = Article(
        authors = ["Ernst, J.", "Spindler, K.", "Wagner, H.Gg."],
        title = u'Untersuchungen zum Thermischen Zerfall von Acetaldehyd und Aceton',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "80",
        pages = """645""",
        year = "1976",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976ERN/SPI645:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010771
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 165,
    label = "C2H4O <=> CHO + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.2e+16, 's^-1'),
        n = 0,
        Ea = (341.725, 'kJ/mol', '+|-', 3.417),
        T0 = (1, 'K'),
        Tmin = (1400, 'K'),
        Tmax = (1600, 'K'),
        Pmin = (22300, 'Pa'),
        Pmax = (7.4e+06, 'Pa'),
    ),
    reference = Article(
        authors = ["Ernst, J.", "Spindler, K."],
        title = u'Untersuchungen zum Thermischen Zerfall von Acetaldehyd und Aceton',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "79",
        pages = """1163""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975ERN/SPI1163:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010771
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 166,
    label = "C2H4O <=> CHO + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.08e+15, 's^-1', '*|/', 1.62),
        n = 0,
        Ea = (342.556, 'kJ/mol', '+|-', 3.426),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975COL/NAE223:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010771
Uncertainty: 1.62
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 167,
    label = "C2H4O <=> CHO + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.88e+16, 's^-1', '+|-', 2.9e+16),
        n = 0,
        Ea = (333.41, 'kJ/mol', '+|-', 6.668),
        T0 = (1, 'K'),
        Tmin = (768, 'K'),
        Tmax = (813, 'K'),
        Pmin = (3333, 'Pa'),
        Pmax = (26700, 'Pa'),
    ),
    reference = Article(
        authors = ["Bardi, I.", "Marta, F."],
        title = u'Investigation of the Thermal Decomposition of Acetaldehyde',
        journal = "Acta Phys. Chem.",
        volume = "19",
        pages = """227""",
        year = "1973",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1973BAR/MAR227:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010771
Bath gas: H2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 168,
    label = "C2H4O <=> CHO + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.87e+16, 's^-1', '+|-', 4.4e+16),
        n = 0,
        Ea = (340.893, 'kJ/mol', '+|-', 13.636),
        T0 = (1, 'K'),
        Tmin = (768, 'K'),
        Tmax = (813, 'K'),
        Pmin = (3333, 'Pa'),
        Pmax = (26700, 'Pa'),
    ),
    reference = Article(
        authors = ["Bardi, I.", "Marta, F."],
        title = u'Investigation of the Thermal Decomposition of Acetaldehyde',
        journal = "Acta Phys. Chem.",
        volume = "19",
        pages = """227""",
        year = "1973",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1973BAR/MAR227:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010771
Bath gas: H2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 169,
    label = "C2H4O <=> CHO + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+15, 's^-1'),
        n = 0,
        Ea = (309.298, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1968LIU/LAI479:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010771
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010771/rk00000009.xml
Bath gas: He
Excitation technique: Thermal
Analytical technique: Gas chromatography
Note: Invalid activation energy uncertainty (8314.472) found and ignored
""",
)

entry(
    index = 170,
    label = "C3H6-2 <=> C2H3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.1e+21, 's^-1', '*|/', 3),
        n = -1.2,
        Ea = (409.072, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:18",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010777
Uncertainty: 3.0
Bath gas: Products
""",
)

entry(
    index = 171,
    label = "C3H6-2 <=> C2H3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.51e+17, 's^-1'),
        n = 0,
        Ea = (384.96, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986NAR/NIE281:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010777
""",
)

entry(
    index = 172,
    label = "C3H6-2 <=> C2H3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+16, 's^-1'),
        n = 0,
        Ea = (416.555, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:19",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010777
""",
)

entry(
    index = 173,
    label = "C3H6-2 <=> C2H3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+13, 's^-1'),
        n = 0,
        Ea = (309.298, 'kJ/mol', '+|-', 3.093),
        T0 = (1, 'K'),
        Tmin = (1160, 'K'),
        Tmax = (1700, 'K'),
        Pmin = (5600, 'Pa'),
        Pmax = (31700, 'Pa'),
    ),
    reference = Article(
        authors = ["Burcat, A."],
        title = u'Cracking of Propylene in a Shock Tube',
        journal = "Fuel",
        volume = "54",
        pages = """87""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975BUR87:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010777
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 174,
    label = "C3H6-2 <=> C2H3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.17e+16, 's^-1', '*|/', 2.51),
        n = 0,
        Ea = (359.185, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1100, 'K'),
        Tmax = (1650, 'K'),
        Pmin = (1.32e+06, 'Pa'),
        Pmax = (1.32e+06, 'Pa'),
    ),
    reference = Article(
        authors = ["Chappell, G.A.", "Shaw, H."],
        title = u'A shock tube study of the pyrolysis of propylene. Kinetics of the vinyl-methyl bond rupture',
        journal = "J. Phys. Chem.",
        volume = "72",
        pages = """4672-4675""",
        year = "1968",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1968CHA/SHA4672-4675:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010777
Uncertainty: 2.51
Bath gas: CH3CH=CH2
Excitation technique: Thermal
Analytical technique: Gas chromatography
Note: Invalid activation energy uncertainty (8314.472) found and ignored
""",
)

entry(
    index = 175,
    label = "C3H6-2 <=> C2H3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+17, 's^-1'),
        n = 0,
        Ea = (393.275, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (773, 'K'),
        Tmax = (973, 'K'),
        Pmin = (933, 'Pa'),
        Pmax = (40000, 'Pa'),
    ),
    reference = Article(
        authors = ["Marshall, R.M.", "Purnell, J.H.", "Shurlock, B.C."],
        title = u'The initiation of propylene pyrolysis',
        journal = "Can. J. Chem.",
        volume = "44",
        pages = """2778-2780""",
        year = "1966",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1966MAR/PUR2778-2780:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010777
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010777/rk00000003.xml
Bath gas: CH3CH=CH2
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 176,
    label = "C3H6-2 <=> C2H3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8e+14, 's^-1'),
        n = 0,
        Ea = (368.331, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1200, 'K'),
        Tmax = (1800, 'K'),
    ),
    reference = Article(
        authors = ["Hidaka, Y.", "Nakamura, T.", "Tanaka, H.", "Jinno, A.", "Kawano, H."],
        title = u'Shock tube and modeling study of propene pyrolysis',
        journal = "Int. J. Chem. Kinet.",
        volume = "24",
        pages = """761-780""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992HID/NAK761-780:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010777
""",
)

entry(
    index = 177,
    label = "CH4O2 <=> OH + CH3O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6e+14, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (177.098, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (800, 'K'),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Frank, P.", "Hayman, G.", "Just, Th.", "Kerr, J.A.", "Murrells, T.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combusion modelling. Supplement I',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "23",
        pages = """847-1033""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994BAU/COB847-1033:80",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011636
Uncertainty: 3.1600001
""",
)

entry(
    index = 178,
    label = "CH4O2 <=> OH + CH3O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4e+15, 's^-1', '*|/', 10),
        n = 0,
        Ea = (179.593, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (400, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combustion modelling',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """411-429""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992BAU/COB411-429:161",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011636
Uncertainty: 10.0
Bath gas: Products
""",
)

entry(
    index = 179,
    label = "CH4O2 <=> OH + CH3O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+14, 's^-1'),
        n = 0,
        Ea = (177.098, 'kJ/mol', '+|-', 8.813),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (700, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Lightfoot, P.D.", "Roussel, P.", "Caralp, F.", "Lesclaux, R."],
        title = u'Flash photolysis study of the CH3O2 + CH3O2 and CH3O2 + HO2 reactions between 600 and 719 K: unimolecular decomposition of methylhydroperoxide',
        journal = "J. Chem. Soc. Faraday Trans.",
        volume = "87",
        pages = """3213-3220""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991LIG/ROU3213-3220:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011636
Bath gas: N2
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 180,
    label = "CH4O2 <=> OH + CH3O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+11, 's^-1', '*|/', 100),
        n = 0,
        Ea = (133.863, 'kJ/mol', '+|-', 21.451),
        T0 = (1, 'K'),
        Tmin = (565, 'K'),
        Tmax = (651, 'K'),
        Pmin = (2933, 'Pa'),
        Pmax = (6533, 'Pa'),
    ),
    reference = Article(
        authors = ["Kirk, A.D."],
        title = u'The thermal decomposition of methyl hydroperoxide',
        journal = "Can. J. Chem.",
        volume = "43",
        pages = """2236-2242""",
        year = "1965",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1965KIR2236-2242:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011636
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011636/rk00000001.xml
Uncertainty: 100.0
Bath gas: Toluene
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 181,
    label = "C3H6-3 <=> C3H5-2 + H",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.59e+14, 's^-1'),
        n = 0,
        Ea = (424.038, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986NAR/NIE281:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00005625
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00005625/rk00000001.xml
""",
)

entry(
    index = 182,
    label = "C3H6-4 <=> C3H5-3 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.45e+15, 's^-1'),
        n = 0,
        Ea = (409.903, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986NAR/NIE281:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00005626
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00005626/rk00000001.xml
""",
)

entry(
    index = 183,
    label = "CH3 + O2 <=> CH3O2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.88e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (2.661, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = Article(
        authors = ["Cobos, C.J.", "Troe, J."],
        title = u'Theory of thermal unimolecular reactions at high pressures. II. Analysis of experimental results',
        journal = "J. Chem. Phys.",
        volume = "83",
        pages = """1010-1015""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985COB/TRO1010-1015:6",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00010854
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010854/rk00000028.xml
Bath gas: Products
""",
)

entry(
    index = 184,
    label = "CH3 + O2 <=> CH3O2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (8.51e+52, 'm^3/(mol*s)', '*|/', 3),
        n = -15,
        Ea = (71.255, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W.", "Hampson, R.F."],
        title = u'Chemical kinetic data base for combustion chemistry. Part I. Methane and related compounds',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "15",
        pages = """1087""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986TSA/HAM1087:167",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010854
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010854/rk00000031.xml
Uncertainty: 3.0
""",
)

entry(
    index = 185,
    label = "CH3 + O2 <=> CH3O2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.6e+27, 'm^3/(mol*s)'),
        n = -7.13,
        Ea = (22.366, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987DEA/WES207:9",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010854
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010854/rk00000032.xml
Bath gas: N2
""",
)

entry(
    index = 186,
    label = "CH3 + O2 <=> CH3O2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (25300, 'm^3/(mol*s)'),
        n = 0,
        Ea = (-5.729, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (530, 'K'),
        Pmin = (16900, 'Pa'),
        Pmax = (16900, 'Pa'),
    ),
    reference = Article(
        authors = ["Keiffer, M.", "Miscampbell, A.J.", "Pilling, M.J."],
        title = u'A global technique for analysing multiple decay curves. Application to the CH3 + O2 system',
        journal = "J. Chem. Soc. Faraday Trans. 2",
        volume = "84",
        pages = """505""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988KEI/MIS505:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Other theoretical""",
    longDesc = 
u"""
PrIMe Reaction: r00010854
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010854/rk00000035.xml
Bath gas: O2
""",
)

entry(
    index = 187,
    label = "C3H8O <=> C2H5O + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.6e+81, 's^-1'),
        n = -19.56,
        Ea = (464.954, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2002BUI/ZHU11188-11195:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00001742
Bath gas: Ar
Pressure dependence: Rate constant is pressure dependent

The authors studied the unimolecular decomposition of iso-C3H7OH with a modified GAUSSIAN-2 method. Six low-lying product channels were identified. Elimination of water via a four-member transition state is dominant below 760 Torr over the temperature range 500?500 K. At higher pressures and over 1200 K, the cleavage of a C-C bond is predicted to be dominant. Rates of C-C bond fission were in reasonable accord with experiments while the water elimination channel was somewhat lower than experiment.

Calculated structures, energetics, and molecular properties of reactant, products, and transition states are provided.
""",
)

entry(
    index = 188,
    label = "C3H8O <=> C2H5O + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.3e+73, 's^-1'),
        n = -17.06,
        Ea = (459.624, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2002BUI/ZHU11188-11195:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00001742
Bath gas: Ar
Pressure dependence: Rate constant is pressure dependent

The authors studied the unimolecular decomposition of iso-C3H7OH with a modified GAUSSIAN-2 method. Six low-lying product channels were identified. Elimination of water via a four-member transition state is dominant below 760 Torr over the temperature range 500?500 K. At higher pressures and over 1200 K, the cleavage of a C-C bond is predicted to be dominant. Rates of C-C bond fission were in reasonable accord with experiments while the water elimination channel was somewhat lower than experiment.

Calculated structures, energetics, and molecular properties of reactant, products, and transition states are provided.
""",
)

entry(
    index = 189,
    label = "C3H8O <=> C2H5O + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (8e+29, 's^-1'),
        n = -3.75,
        Ea = (381.144, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2002BUI/ZHU11188-11195:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00001742
Bath gas: Ar
Pressure dependence: Rate constant is high pressure limit

The authors studied the unimolecular decomposition of iso-C3H7OH with a modified GAUSSIAN-2 method. Six low-lying product channels were identified. Elimination of water via a four-member transition state is dominant below 760 Torr over the temperature range 500?500 K. At higher pressures and over 1200 K, the cleavage of a C-C bond is predicted to be dominant. Rates of C-C bond fission were in reasonable accord with experiments while the water elimination channel was somewhat lower than experiment.

Calculated structures, energetics, and molecular properties of reactant, products, and transition states are provided.
""",
)

entry(
    index = 190,
    label = "C3H8O <=> C2H5O + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.16e+16, 's^-1'),
        n = 0,
        Ea = (341.725, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976TSA173:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00001742
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00001742/rk00000001.xml
Bath gas: Ar
""",
)

entry(
    index = 191,
    label = "C3H8O-2 <=> C2H5O-2 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.58e+16, 's^-1'),
        n = 0,
        Ea = (341.725, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976TSA173:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00001836
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00001836/rk00000001.xml
Bath gas: Ar
""",
)

entry(
    index = 192,
    label = "C3H6O <=> C3H5O + H",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (8e+15, 's^-1'),
        n = 0,
        Ea = (384.96, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (835, 'K'),
        Tmax = (1160, 'K'),
        Pmin = (203000, 'Pa'),
        Pmax = (203000, 'Pa'),
    ),
    reference = Article(
        authors = ["Lifshitz, A.", "Tamburu, C."],
        title = u'Isomerization and decomposition of propylene oxide. Studies with a single-pulse shock tube',
        journal = "J. Phys. Chem.",
        volume = "98",
        pages = """1161-1170""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994LIF/TAM1161-1170:10",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00003550
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00003550/rk00000001.xml
Bath gas: Ar
""",
)

entry(
    index = 193,
    label = "C4H10 <=> C4H9 + H",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1e+16, 's^-1'),
        n = 0,
        Ea = (397.432, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:9",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00004586
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004586/rk00000001.xml
""",
)

entry(
    index = 194,
    label = "C4H10-2 <=> C4H9-2 + H",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1.58e+16, 's^-1'),
        n = 0,
        Ea = (409.903, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:10",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00004587
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004587/rk00000001.xml
""",
)

entry(
    index = 195,
    label = "C4H6 <=> C4H5 + H",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.58e+16, 's^-1'),
        n = 0,
        Ea = (460.622, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:14",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00004730
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004730/rk00000001.xml
""",
)

entry(
    index = 196,
    label = "C4H6 <=> C4H5 + H",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (7e+14, 's^-1'),
        n = 0,
        Ea = (397.432, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1100, 'K'),
        Tmax = (1600, 'K'),
    ),
    reference = Article(
        authors = ["Hidaka, Y.", "Higashihara, T.", "Ninomiya, N.", "Oshita, H.", "Kawano, H."],
        title = u'Thermal isomerization and decomposition of 2-butyne in shock waves',
        journal = "J. Phys. Chem.",
        volume = "97",
        pages = """10977-10983""",
        year = "1993",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1993HID/HIG10977-10983:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00004730
Bath gas: Ar
""",
)

entry(
    index = 197,
    label = "C4H6-2 <=> C4H5-2 + H",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.7e+14, 's^-1'),
        n = 0,
        Ea = (367.774, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1100, 'K'),
        Tmax = (1600, 'K'),
        Pmin = (638000, 'Pa'),
        Pmax = (922000, 'Pa'),
    ),
    reference = Article(
        authors = ["Belmekki, N. Glaude, P.A.", "Da Costa, I.", "Fournet, R.", "Battin-Leclerc, F."],
        title = u'Experimental and Modeling Study of the Oxidation of 1-Butyne and 2-Butyne',
        journal = "Int J. Chem. Kinet.",
        volume = "34",
        pages = """172-183""",
        year = "2002",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2002BEL/DAC172-183:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00004807
""",
)

entry(
    index = 198,
    label = "C4H6-2 <=> C4H5-2 + H",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7e+14, 's^-1'),
        n = 0,
        Ea = (360.017, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1100, 'K'),
        Tmax = (1600, 'K'),
    ),
    reference = Article(
        authors = ["Hidaka, Y.", "Higashihara, T.", "Ninomiya, N.", "Oshita, H.", "Kawano, H."],
        title = u'Thermal isomerization and decomposition of 2-butyne in shock waves',
        journal = "J. Phys. Chem.",
        volume = "97",
        pages = """10977-10983""",
        year = "1993",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1993HID/HIG10977-10983:5",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00004807
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004807/rk00000001.xml
Bath gas: Ar
""",
)

entry(
    index = 199,
    label = "C4H5-2 + H <=> C4H6-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7e+06, 'm^3/(mol*s)'),
        n = 0.31,
        Ea = (-0.778, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Harding, L.B.", "Klippenstein, S.J.", "Georgievskii, Y."],
        title = u'On the combination reactions of hydrogen atoms with resonance-stabilized hydrocarbon radicals',
        journal = "J. Phys. Chem. A",
        volume = "111",
        pages = """3789-3801""",
        year = "2007",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2007HAR/KLI3789-3801:14",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00004807
""",
)

entry(
    index = 200,
    label = "C4H8 <=> C3H5-2 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.16e+17, 's^-1'),
        n = 0,
        Ea = (415.724, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:16",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00004825
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004825/rk00000001.xml
""",
)

entry(
    index = 201,
    label = "C4H8-2 <=> C4H7 + H",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1.54e+19, 's^-1'),
        n = -0.87,
        Ea = (365.418, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1600, 'K'),
        Tmax = (2300, 'K'),
        Pmin = (933, 'Pa'),
        Pmax = (53300, 'Pa'),
    ),
    reference = Article(
        authors = ["Santhanam, S.", "Kiefer, J.H.", "Tranter, R.S.", "Srinivasan, N.K."],
        title = u'A Shock Tube, Laser-Schlieren Study of the Pyrolysis of Isobutene: Relaxation, Incubation, and Dissociation Rates',
        journal = "Int. J",
        volume = "35",
        pages = """381-390""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003SAN/KIE381-390:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00005814
Bath gas: Kr
Pressure dependence: Rate constant is high pressure limit
Experimental procedure: Shock tube
Excitation technique: Thermal
Time resolution: In real time
Analytical technique: Laser schlieren

The primary reaction is suggested by the authors to be C-H bond fission iso-C4H8 = H2C=C(CH3)CH2+ H although other channels were considered. A restricted-rotor, Gorin-model RRKM model of the reaction was developed and was able to describe the measured rates using the known bond-energy as barrier and < Delta Edown> = 680 cm-1. The reaction was well into the fall-off region under the experimental conditions with rate constants 1 to 3 orders of maginitude under the high pressure limit derived from the RRKM extrapolation. Measured rate constants are shown graphically but individual values are unfortunately not reported in the paper. The analysis included the development of a 32-step mechanism to describe iso-butene pyrolysis and possible secondary chemistry in their system. The derived high pressure limiting rate constant for dissociation is in good agreement with previous lower temperature studies.

An unexpected feature of the study was the observation of vibrational relaxation, and at high temperatures, a consequent incubation delay in the unimolecular dissociation.
""",
)

entry(
    index = 202,
    label = "C4H8-2 <=> C4H7 + H",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (2e+15, 's^-1'),
        n = 0,
        Ea = (365.837, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994DOU/PER1597-1627:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005814
Bath gas: iso-C4H8
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 203,
    label = "C4H8-2 <=> C4H7 + H",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (5e+11, 's^-1'),
        n = 0,
        Ea = (67, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (933, 'K'),
        Tmax = (1080, 'K'),
        Pmin = (173, 'Pa'),
        Pmax = (2600, 'Pa'),
    ),
    reference = Article(
        authors = ["Szwarc, M."],
        title = u'The kinetics of the thermal decomposition of isobutene',
        journal = "J. Chem. Phys.",
        volume = "17",
        pages = """292-295""",
        year = "1949",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1949SZW292-295:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005814
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00005814/rk00000001.xml
Bath gas: iso-C4H8
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 204,
    label = "C4H2 <=> C4H + H",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.2e+14, 's^-1', '+|-', 5.9e+13),
        n = 0,
        Ea = (488.06, 'kJ/mol', '+|-', 4.881),
        T0 = (1, 'K'),
        Tmin = (1850, 'K'),
        Tmax = (2300, 'K'),
        Pmin = (149000, 'Pa'),
        Pmax = (400000, 'Pa'),
    ),
    reference = Article(
        authors = ["Frank, P.", "Just, Th."],
        title = u'High Temperature Thermal Decomposition of Acetylene and Diacetylene at Low Relative Concentrations',
        journal = "Combust. Flame",
        volume = "38",
        pages = """231""",
        year = "1980",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1980FRA/JUS231:5",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00006906
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00006906/rk00000002.xml
Uncertainty: 1.3
Bath gas: Ar
""",
)

entry(
    index = 205,
    label = "C4H6-3 <=> C3H3 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1e+17, 's^-1'),
        n = 0,
        Ea = (502.194, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1100, 'K'),
        Tmax = (1600, 'K'),
    ),
    reference = Article(
        authors = ["Hidaka, Y.", "Higashihara, T.", "Ninomiya, N.", "Oshita, H.", "Kawano, H."],
        title = u'Thermal isomerization and decomposition of 2-butyne in shock waves',
        journal = "J. Phys. Chem.",
        volume = "97",
        pages = """10977-10983""",
        year = "1993",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1993HID/HIG10977-10983:8",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00007144
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007144/rk00000001.xml
Bath gas: Ar
""",
)

entry(
    index = 206,
    label = "C4H6-4 <=> C4H5-3 + H",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (3.16e+15, 's^-1'),
        n = 0,
        Ea = (365.005, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:20",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00007145
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007145/rk00000001.xml
""",
)

entry(
    index = 207,
    label = "C4H5-3 + H <=> C4H6-4",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (2.83e+07, 'm^3/(mol*s)'),
        n = 0.2,
        Ea = (-0.476, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Harding, L.B.", "Klippenstein, S.J.", "Georgievskii, Y."],
        title = u'On the combination reactions of hydrogen atoms with resonance-stabilized hydrocarbon radicals',
        journal = "J. Phys. Chem. A",
        volume = "111",
        pages = """3789-3801""",
        year = "2007",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2007HAR/KLI3789-3801:16",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00007145
""",
)

entry(
    index = 208,
    label = "C4H6-5 <=> C4H5-4 + H",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2e+15, 's^-1'),
        n = 0,
        Ea = (359.185, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:21",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00007774
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007774/rk00000001.xml
""",
)

entry(
    index = 209,
    label = "C3H5 + CH3 <=> C4H8-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.02e+08, 'm^3/(mol*s)', '*|/', 1.5),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:92",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010111
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010111/rk00000001.xml
Uncertainty: 1.5
Bath gas: Products
""",
)

entry(
    index = 210,
    label = "C4H8-3 <=> C3H5 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+16, 's^-1'),
        n = 0,
        Ea = (305.141, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:12",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010111
""",
)

entry(
    index = 211,
    label = "C4H8-3 <=> C3H5 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+15, 's^-1', '*|/', 2),
        n = 0,
        Ea = (299.321, 'kJ/mol', '+|-', 2.993),
        T0 = (1, 'K'),
        Tmin = (689, 'K'),
        Tmax = (760, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (93300, 'Pa'),
    ),
    reference = Article(
        authors = ["Trenwith, A.B."],
        title = u'Dissociation of 1-butene, 3-methyl-1-butene, and of 3,3-dimethyl-1-butene and the resonance energy of the allyl, methyl allyl and dimethyl allyl radicals',
        journal = "Trans. Faraday Soc.",
        volume = "66",
        pages = """2805-2811""",
        year = "1970",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1970TRE2805-2811:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010111
Uncertainty: 2.0
Bath gas: 1-C4H8
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 212,
    label = "C4H8-3 <=> C3H5 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+13, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (291.007, 'kJ/mol', '+|-', 8.73),
        T0 = (1, 'K'),
        Tmin = (798, 'K'),
        Tmax = (924, 'K'),
    ),
    reference = Article(
        authors = ["Halstead, M.P.", "Quinn, C.P."],
        title = u'Pyrolysis of ethylene',
        journal = "Trans. Faraday Soc.",
        volume = "64",
        pages = """103""",
        year = "1968",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1968HAL/QUI103:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010111
Uncertainty: 3.1600001
Bath gas: H2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 213,
    label = "C4H8-3 <=> C3H5 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.13e+12, 's^-1'),
        n = 0,
        Ea = (246.94, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (900, 'K'),
        Tmax = (990, 'K'),
        Pmin = (1533, 'Pa'),
        Pmax = (1533, 'Pa'),
    ),
    reference = Article(
        authors = ["Kerr, J.A.", "Spencer, R.", "Trotman-Dickenson, A.F."],
        title = u'The pyrolysis of but-1-ene, and the resonance energy of the allyl radical',
        journal = "J. Chem. Soc.",
        pages = """6652-6654""",
        year = "1965",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1965KER/SPE6652-6654:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010111
Bath gas: aniline
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 214,
    label = "C4H8-3 <=> C3H5 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.5e+13, 's^-1'),
        n = 0,
        Ea = (263.569, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (926, 'K'),
        Tmax = (1050, 'K'),
        Pmin = (1067, 'Pa'),
        Pmax = (1333, 'Pa'),
    ),
    reference = Article(
        authors = ["Sehon, A.H.", "Szwarc, M."],
        title = u'The CH2:CH2-CH3 bond dissociation energy and the heat of formation of the allyl radical',
        journal = "Proc. R. Soc. London A",
        volume = "202",
        pages = """263-276""",
        year = "1950",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1950SEH/SZW263-276:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010111
Bath gas: Toluene
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 215,
    label = "C3H7 + CH3 <=> C4H10-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.21e+08, 'm^3/(mol*s)'),
        n = -0.47,
        Ea = (-0.812, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Klippenstein, S.J.", "Georgievskii, Y.", "Harding, L.B."],
        title = u'Predictive theory for the combination kinetics of two alkyl radicals',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "8",
        pages = """1133-1147""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006KLI/GEO1133-1147:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00010181
Pressure dependence: Rate constant is high pressure limit

Rate constants were calculated with an ab initio transition state theory employing direct evaluations of the orientation dependent interaction energies at the CASPT2/cc-pvdz level within variable reaction
coordinate transition state theory (VRC-TST). Results were compared with experiment for a series of alkyl radicals and the good quantitative agreement was found.

Each methyl substituent adjacent to a radical site was found to reduce the rate coefficient by about a factor of two. Rate constants are predicted to decrease substantially with increasing temperature, with the more sterically hindered reactants having a more rapid decrease. The geometric mean rule was found to be in good agreement with the detailed calculations.

The authors state the rate parameters are strictly applicable between 200-2000 K but that they should provide reasonable predictions up to about 2700 K.
""",
)

entry(
    index = 216,
    label = "C3H7 + CH3 <=> C4H10-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (2.503, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (713, 'K'),
        Tmax = (814, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (20000, 'Pa'),
    ),
    reference = Article(
        authors = ["Konar, R.S.", "Marshall, R.M.", "Purnell, J.H."],
        title = u'Initiation of isobutane pyrolysis',
        journal = "Trans. Faraday Soc.",
        volume = "64",
        pages = """405-413""",
        year = "1968",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1968KON/MAR405-413:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010181
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010181/rk00000001.xml
Bath gas: iso-C4H10
""",
)

entry(
    index = 217,
    label = "C4H10-4 <=> C2H5 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+16, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (340.062, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:62",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010242
Uncertainty: 3.1600001
""",
)

entry(
    index = 218,
    label = "C4H10-4 <=> C2H5 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+17, 's^-1'),
        n = 0,
        Ea = (364.174, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1100, 'K'),
        Pmin = (66700, 'Pa'),
        Pmax = (160000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Evidence for Strongly Temperature-Dependent A Factors in Alkane Decomposition and High Heats of Formation for Alkyl Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "10",
        pages = """821""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978TSA821:4",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00010242
Bath gas: Ar
""",
)

entry(
    index = 219,
    label = "C4H10-4 <=> C2H5 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.72e+15, 's^-1'),
        n = 0,
        Ea = (316.366, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1320, 'K'),
        Tmax = (1600, 'K'),
    ),
    reference = Article(
        authors = ["Oehlschlaeger, M.A.", "Davidson, D.F.", "Hanson, R.K."],
        title = u'High-temperature thermal decomposition of isobutane and n-butane behind shock waves',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """4247-4253""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004OEH/DAV4247-4253:8",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010242
Pressure dependence: Rate constant is high pressure limit

RRKM-Master Equation model created on the basis of experimental data obtained in shock tube experiments in the same work.
""",
)

entry(
    index = 220,
    label = "C4H10-4 <=> C2H5 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+16, 's^-1'),
        n = 0,
        Ea = (335.905, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:11",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010242
""",
)

entry(
    index = 221,
    label = "C4H10-4 <=> C2H5 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e+16, 's^-1'),
        n = 0,
        Ea = (343.388, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1200, 'K'),
        Pmin = (66700, 'Pa'),
        Pmax = (160000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Evidence for Strongly Temperature-Dependent A Factors in Alkane Decomposition and High Heats of Formation for Alkyl Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "10",
        pages = """821""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978TSA821:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010242
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 222,
    label = "C4H10-4 <=> C2H5 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+15, 's^-1'),
        n = 0,
        Ea = (322.602, 'kJ/mol', '+|-', 16.13),
        T0 = (1, 'K'),
        Tmin = (895, 'K'),
        Tmax = (981, 'K'),
        Pmin = (3200, 'Pa'),
        Pmax = (3200, 'Pa'),
    ),
    reference = Article(
        authors = ["Hughes, D.G.", "Marshall, R.M.", "Purnell, J.H."],
        title = u'Rate Constants for the Initiation of n-Butane Pyrolysis and for the Recombination of Ethyl Radicals',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "70",
        pages = """594""",
        year = "1974",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1974HUG/MAR594:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010242
Bath gas: n-C4H10
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 223,
    label = "C4H10-4 <=> C2H5 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e+16, 's^-1'),
        n = 0,
        Ea = (338.399, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1100, 'K'),
        Tmax = (1250, 'K'),
    ),
    reference = Article(
        authors = ["Golden, D.M.", "Alfassi, Z.B.", "Beadle, P.C."],
        title = u"Very Low-Pressure Pyrolysis (VLPP) of Alkanes: n-Butane, 2,3-Dimethylbutane, 2,2',3,3'-Tetramethylbutane, and Isobutane",
        journal = "Int. J. Chem. Kinet.",
        volume = "6",
        pages = """359""",
        year = "1974",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1974GOL/ALF359:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010242
Bath gas: n-C4H10
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 224,
    label = "C4H10-4 <=> C2H5 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+17, 's^-1'),
        n = 0,
        Ea = (335.073, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1966LIN/BAC2369:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010242
Bath gas: C2H6
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 225,
    label = "C4H10-4 <=> C2H5 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.03e+24, 's^-1'),
        n = -2.17,
        Ea = (365.005, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1200, 'K'),
    ),
    reference = Article(
        authors = ["Forst, W."],
        title = u'Temperature-dependent A factor in thermal unimolecular reactions',
        journal = "J. Phys. Chem.",
        volume = "83",
        pages = """100-108""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979FOR100-108:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00010242
""",
)

entry(
    index = 226,
    label = "C4H10-4 <=> C2H5 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.77e+18, 's^-1'),
        n = 0,
        Ea = (360.848, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1962PUR/QUI267:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010242
Bath gas: n-C4H10
""",
)

entry(
    index = 227,
    label = "C4H10-5 <=> C3H7-2 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2e+16, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (340.062, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:61",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010516
Uncertainty: 3.1600001
""",
)

entry(
    index = 228,
    label = "C4H10-5 <=> C3H7-2 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.28e+14, 's^-1'),
        n = 0,
        Ea = (292.503, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1320, 'K'),
        Tmax = (1600, 'K'),
    ),
    reference = Article(
        authors = ["Oehlschlaeger, M.A.", "Davidson, D.F.", "Hanson, R.K."],
        title = u'High-temperature thermal decomposition of isobutane and n-butane behind shock waves',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """4247-4253""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004OEH/DAV4247-4253:7",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010516
Pressure dependence: Rate constant is high pressure limit

RRKM-Master Equation model created on the basis of experimental data obtained in shock tube experiments in the same work.
""",
)

entry(
    index = 229,
    label = "C4H10-5 <=> C3H7-2 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1e+17, 's^-1'),
        n = 0,
        Ea = (354.197, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:8",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010516
""",
)

entry(
    index = 230,
    label = "C4H10-5 <=> C3H7-2 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (8.89e+13, 's^-1'),
        n = 0,
        Ea = (300.984, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1290, 'K'),
        Tmax = (1610, 'K'),
        Pmin = (2666, 'Pa'),
        Pmax = (2666, 'Pa'),
    ),
    reference = Article(
        authors = ["Koike, T.", "Morinaga, K."],
        title = u'UV Absorption Studies of the Pyrolysis of Butane in Shock Waves',
        journal = "Bull. Chem. Soc. Jpn.",
        volume = "54",
        pages = """2439""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981KOI/MOR2439:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010516
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 231,
    label = "C4H10-5 <=> C3H7-2 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.77e+18, 's^-1'),
        n = 0,
        Ea = (360.848, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1962PUR/QUI267:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010516
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010516/rk00000003.xml
Bath gas: n-C4H10
""",
)

entry(
    index = 232,
    label = "C2H6O2 <=> CH3O + CH3O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+16, 's^-1', '*|/', 1.58),
        n = 0,
        Ea = (161.301, 'kJ/mol', '+|-', 3.218),
        T0 = (1, 'K'),
        Tmin = (383, 'K'),
        Tmax = (433, 'K'),
        Pmin = (68000, 'Pa'),
        Pmax = (68000, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L.", "Rattray, G.N."],
        title = u'The Reaction of Methoxy Radicals with Nitric Oxide and Nitrogen Dioxide',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """1183""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979BAT/RAT1183:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010569
Uncertainty: 1.58
Bath gas: CF4
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 233,
    label = "C2H6O2 <=> CH3O + CH3O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+15, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (155.481, 'kJ/mol', '+|-', 3.101),
        T0 = (1, 'K'),
        Tmin = (391, 'K'),
        Tmax = (432, 'K'),
        Pmin = (9866, 'Pa'),
        Pmax = (9866, 'Pa'),
    ),
    reference = Article(
        authors = ["Barker, J.R.", "Benson, S.W.", "Golden, D.M."],
        title = u'The Decomposition of Dimethyl Peroxide and the Rate Constant for CH3O + O2 \u2192\x92 CH2O +HO2',
        journal = "Int. J. Chem. Kinet.",
        volume = "9",
        pages = """31""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977BAR/BEN31:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010569
Uncertainty: 3.1600001
Bath gas: (CH3O)2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 234,
    label = "C2H6O2 <=> CH3O + CH3O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+15, 's^-1', '*|/', 5),
        n = 0,
        Ea = (154.649, 'kJ/mol', '+|-', 1.546),
        T0 = (1, 'K'),
        Tmin = (383, 'K'),
        Tmax = (413, 'K'),
        Pmin = (91200, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L.", "McCulloch, R.D."],
        title = u'Pyrolysis of Dimethyl Peroxide',
        journal = "Int. J. Chem. Kinet.",
        volume = "8",
        pages = """491""",
        year = "1976",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976BAT/MCC491:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010569
Uncertainty: 5.0
Bath gas: iso-C4H10
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 235,
    label = "C2H6O2 <=> CH3O + CH3O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.6e+15, 's^-1'),
        n = 0,
        Ea = (147.998, 'kJ/mol', '+|-', 10.31),
        T0 = (1, 'K'),
        Tmin = (386, 'K'),
        Tmax = (416, 'K'),
    ),
    reference = Article(
        authors = ["Hanst, P.L.", "Calvert, J.G."],
        title = u'The thermal decomposition of dimethyl peroxide: the oxygen-oxygen bond strength of dialkyl peroxides',
        journal = "J. Phys. Chem.",
        volume = "63",
        pages = """104-106""",
        year = "1959",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1959HAN/CAL104-106:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010569
Bath gas: (CH3O)2
Excitation technique: Thermal
Analytical technique: IR absorption
""",
)

entry(
    index = 236,
    label = "C2H6O2 <=> CH3O + CH3O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.1e+15, 's^-1'),
        n = 0,
        Ea = (154.649, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (428, 'K'),
        Tmax = (454, 'K'),
        Pmin = (1467, 'Pa'),
        Pmax = (6799, 'Pa'),
    ),
    reference = Article(
        authors = ["Takezaki, Y.", "Takeuchi, C."],
        title = u'Decomposition of methanol induced by methoxy radicals',
        journal = "J. Chem. Phys.",
        volume = "22",
        pages = """1527""",
        year = "1954",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1954TAK/TAK1527:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010569
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010569/rk00000003.xml
Bath gas: (CH3O)2
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 237,
    label = "C4H6-6 <=> C3H3-2 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+15, 's^-1'),
        n = 0,
        Ea = (316.781, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:15",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010783
""",
)

entry(
    index = 238,
    label = "C4H6-6 <=> C3H3-2 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.58e+17, 's^-1', '*|/', 5),
        n = 0,
        Ea = (312.624, 'kJ/mol', '+|-', 9.395),
        T0 = (1, 'K'),
        Tmin = (652, 'K'),
        Tmax = (731, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (160000, 'Pa'),
    ),
    reference = Article(
        authors = ["Trenwith, A.B.", "Wrigley, S.P."],
        title = u'Pyrolysis of But-1-yne and the Resonance Energy of the Propargyl and 3-Methylpropargyl Radicals',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "78",
        pages = """2337""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982TRE/WRI2337:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010783
Uncertainty: 5.0
Bath gas: C2H5CCH
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 239,
    label = "C4H6-6 <=> C3H3-2 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+15, 's^-1', '*|/', 2),
        n = 0,
        Ea = (310.13, 'kJ/mol', '+|-', 9.312),
        T0 = (1, 'K'),
        Tmin = (1050, 'K'),
        Tmax = (1150, 'K'),
    ),
    reference = Article(
        authors = ["King, K.D."],
        title = u'Very Low-Pressure Pyrolysis (VLPP) of But-1-yne. The Heat of Formation and Stabilization Energy of the Propargyl Radical',
        journal = "Int. J. Chem. Kinet.",
        volume = "10",
        pages = """545""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978KIN545:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010783
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010783/rk00000002.xml
Uncertainty: 2.0
Bath gas: C2H5CCH
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 240,
    label = "C4H6-6 <=> C3H3-2 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3e+15, 's^-1'),
        n = 0,
        Ea = (316.781, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1100, 'K'),
        Tmax = (1600, 'K'),
        Pmin = (125000, 'Pa'),
        Pmax = (233000, 'Pa'),
    ),
    reference = Article(
        authors = ["Hidaka, Y.", "Higashihara, T.", "Oki, T.", "Kawano, H."],
        title = u'Thermal decomposition of 1-butyne in shock waves',
        journal = "Int. J. Chem. Kinet.",
        volume = "27",
        pages = """321-330""",
        year = "1995",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1995HID/HIG321-330:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010783
Bath gas: Ar
""",
)

entry(
    index = 241,
    label = "C4H6-6 <=> C3H3-2 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3e+15, 's^-1'),
        n = 0,
        Ea = (320.939, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1100, 'K'),
        Tmax = (1600, 'K'),
    ),
    reference = Article(
        authors = ["Hidaka, Y.", "Higashihara, T.", "Ninomiya, N.", "Oshita, H.", "Kawano, H."],
        title = u'Thermal isomerization and decomposition of 2-butyne in shock waves',
        journal = "J. Phys. Chem.",
        volume = "97",
        pages = """10977-10983""",
        year = "1993",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1993HID/HIG10977-10983:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010783
Bath gas: Ar
""",
)

entry(
    index = 242,
    label = "C3H6O-2 <=> C2H3O + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.13e+16, 's^-1'),
        n = 0,
        Ea = (341.833, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1050, 'K'),
        Tmax = (1650, 'K'),
        Pmin = (122000, 'Pa'),
        Pmax = (324000, 'Pa'),
    ),
    reference = Article(
        authors = ["Sato, K.", "Hidaka, Y."],
        title = u'Shock-tube and modeling study of acetone pyrolysis and oxidation',
        journal = "Combust. Flame",
        volume = "122",
        pages = """291-311""",
        year = "2000",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2000SAT/HID291-311:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010789
Experimental procedure: Shock tube
Time resolution: In real time
Analytical technique: IR absorption
""",
)

entry(
    index = 243,
    label = "C3H6O-2 <=> C2H3O + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.94e+17, 's^-1', '*|/', 10),
        n = 0,
        Ea = (353.365, 'kJ/mol', '+|-', 14.135),
        T0 = (1, 'K'),
        Tmin = (825, 'K'),
        Tmax = (940, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (24000, 'Pa'),
    ),
    reference = Article(
        authors = ["Mousavipour, S.H.", "Pacey, P.D."],
        title = u'Initiation and abstraction reactions in the pyrolysis of acetone',
        journal = "J. Phys. Chem.",
        volume = "100",
        pages = """3573-3579""",
        year = "1996",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996MOU/PAC3573-3579:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010789
Uncertainty: 10.0
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 244,
    label = "C3H6O-2 <=> C2H3O + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.7e+16, 's^-1'),
        n = 0,
        Ea = (341.725, 'kJ/mol', '+|-', 13.719),
        T0 = (1, 'K'),
        Tmin = (1350, 'K'),
        Tmax = (1650, 'K'),
        Pmin = (20300, 'Pa'),
        Pmax = (7.4e+06, 'Pa'),
    ),
    reference = Article(
        authors = ["Ernst, J.", "Spindler, K.", "Wagner, H.Gg."],
        title = u'Untersuchungen zum Thermischen Zerfall von Acetaldehyd und Aceton',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "80",
        pages = """645""",
        year = "1976",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976ERN/SPI645:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010789
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 245,
    label = "C3H6O-2 <=> C2H3O + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2e+16, 's^-1'),
        n = 0,
        Ea = (338.399, 'kJ/mol', '+|-', 13.553),
        T0 = (1, 'K'),
        Tmin = (1400, 'K'),
        Tmax = (1600, 'K'),
        Pmin = (22300, 'Pa'),
        Pmax = (7.4e+06, 'Pa'),
    ),
    reference = Article(
        authors = ["Ernst, J.", "Spindler, K."],
        title = u'Untersuchungen zum Thermischen Zerfall von Acetaldehyd und Aceton',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "79",
        pages = """1163""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975ERN/SPI1163:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010789
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 246,
    label = "C3H6O-2 <=> C2H3O + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.4e+14, 's^-1'),
        n = 0,
        Ea = (296.827, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1110, 'K'),
        Pmin = (1733, 'Pa'),
        Pmax = (1733, 'Pa'),
    ),
    reference = Article(
        authors = ["Clark, D.", "Pritchard, H.O."],
        title = u'Arrhenius parameters of some reactions involving multiplicity changes',
        journal = "J. Chem. Soc. London",
        pages = """2136-2140""",
        year = "1956",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1956CLA/PRI2136-2140:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010789
Bath gas: Toluene
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 247,
    label = "C3H6O-2 <=> C2H3O + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.4e+14, 's^-1'),
        n = 0,
        Ea = (300.984, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (993, 'K'),
        Tmax = (1100, 'K'),
        Pmin = (693, 'Pa'),
        Pmax = (2800, 'Pa'),
    ),
    reference = Article(
        authors = ["Szwarc, M.", "Taylor, J.W."],
        title = u'Pyrolysis of acetone and the heat of formation of acetyl radicals',
        journal = "J. Chem. Phys.",
        volume = "23",
        pages = """2310-2314""",
        year = "1955",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1955SZW/TAY2310-2314:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010789
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010789/rk00000008.xml
Bath gas: Toluene
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 248,
    label = "C2H6O2-2 <=> OH + C2H5O-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4e+15, 's^-1', '*|/', 2),
        n = 0,
        Ea = (179.593, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (400, 'K'),
        Tmax = (800, 'K'),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Frank, P.", "Hayman, G.", "Just, Th.", "Kerr, J.A.", "Murrells, T.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combusion modelling. Supplement I',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "23",
        pages = """847-1033""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994BAU/COB847-1033:82",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011653
Uncertainty: 2.0
""",
)

entry(
    index = 249,
    label = "C2H6O2-2 <=> OH + C2H5O-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4e+15, 's^-1', '*|/', 10),
        n = 0,
        Ea = (179.593, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (400, 'K'),
        Tmax = (1000, 'K'),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combustion modelling',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """411-429""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992BAU/COB411-429:165",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00011653
Uncertainty: 10.0
""",
)

entry(
    index = 250,
    label = "C2H6O2-2 <=> OH + C2H5O-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+13, 's^-1', '*|/', 2),
        n = 0,
        Ea = (157.975, 'kJ/mol', '+|-', 3.151),
        T0 = (1, 'K'),
        Tmin = (561, 'K'),
        Tmax = (653, 'K'),
    ),
    reference = Article(
        authors = ["Kirk, A.D.", "Knox, J.H."],
        title = u'The pyrolysis of alkyl hydroperoxides in the gas phase',
        journal = "Trans. Faraday Soc.",
        volume = "56",
        pages = """1296-1303""",
        year = "1960",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1960KIR/KNO1296-1303:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011653
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011653/rk00000001.xml
Uncertainty: 2.0
Bath gas: Benzene
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 251,
    label = "O2 + C2H5 <=> C2H5O2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (22100, 'm^3/(mol*s)'),
        n = 0.77,
        Ea = (-2.386, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (1013, 'Pa'),
        Pmax = (1.01e+06, 'Pa'),
    ),
    reference = Article(
        authors = ["Wagner, A.F.", "Slagle, I.R.", "Sarzynski, D.", "Gutman, D."],
        title = u'Experimental and theoretical studies of the C2H5 + O2 reaction kinetics',
        journal = "J. Phys. Chem.",
        volume = "94",
        pages = """1853-1868""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990WAG/SLA1853-1868:7",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00013875
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 252,
    label = "O2 + C2H5 <=> C2H5O2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2e+36, 'm^3/(mol*s)'),
        n = -10.3,
        Ea = (25.442, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990BOZ/DEA3313-3317:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00013875
Bath gas: N2
""",
)

entry(
    index = 253,
    label = "O2 + C2H5 <=> C2H5O2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (794000, 'm^3/(mol*s)', '*|/', 1.1),
        n = 0,
        Ea = (-3.517, 'kJ/mol', '+|-', 0.281),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (400, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Munk, J.", "Pagsberg, P.", "Ratajczak, E.", "Sillesen, A."],
        title = u'Spectrokinetic studies of ethyl and ethylperoxy radicals',
        journal = "J. Phys. Chem.",
        volume = "90",
        pages = """2752""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986MUN/PAG2752:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00013875
Uncertainty: 1.1
Bath gas: H2
Excitation technique: Chemical activation
Analytical technique: Vis-UV emission
""",
)

entry(
    index = 254,
    label = "O2 + C2H5 <=> C2H5O2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.72e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (14.301, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (308, 'K'),
        Tmax = (423, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (3733, 'Pa'),
    ),
    reference = Article(
        authors = ["Jolley, J.E."],
        title = u'The photooxidation of diethyl ketone',
        journal = "J. Am. Chem. Soc.",
        volume = "79",
        pages = """1537""",
        year = "1957",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1957JOL1537:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00013875
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013875/rk00000001.xml
Bath gas: O2
Excitation technique: Direct photolysis
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 255,
    label = "O2 + C2H5 <=> C2H5O2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.62e+32, 'm^3/(mol*s)'),
        n = -9.22,
        Ea = (21.867, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003DES/KLI4415-4427:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00013875
Bath gas: He

Rate constants are based in part on master equation simulations employing transition states from quantum calculations. This work is a combined experimental, theory, and modeling study. Compared OH profiles with those from modeling. Model describes HO2 profiles well, but is not as good for OH profiles.

Static cell (low flow), 296-700 K, He buffer typically 3.65E17 cm-3 (10-20 torr), O2 typically 6.3E15 cm-3. Radicals produced by RH + Cl -> R + HCl, where Cl produced by 193 nm excimer laser photolysis of CCl3F. OH detected using LIF at 281.996 nm.

Employed earlier quantum calculations (see references below) combined with master equation modeling to provide rate expressions for many reactions in this system. Only a few rate expressions are abstracted here.

Miller and Klippenstein, IJCK 33, 654 (2001)
DeSain et al, Farad. Disc. 119, 101 (2001)
""",
)

entry(
    index = 256,
    label = "O2 + C2H5 <=> C2H5O2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (20200, 'm^3/(mol*s)'),
        n = 0.98,
        Ea = (-0.266, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (133000, 'Pa'),
    ),
    reference = Article(
        authors = ["Miller, J.A.", "Klippenstein, S.J."],
        title = u'The Reaction Between Ethyl and Molecular Oxygen II. Further Analysis',
        journal = "Int J. Chem. Kinet.",
        volume = "33",
        pages = """654-668""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001MIL/KLI654-668:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00013875
Pressure dependence: Rate constant is pressure dependent

Potential energy digrams for various product chennels have been computed.Three different regimes of the reaction (low-temperature, transition, and high-temepature) have been discussed in terms of eigenvectors and eigenvalues of the transition matrix of the master equation.Low pressure rate constant; k(0) = 2.34E-18 T(-4.29) exp(-220/RT) cm^6 / molecule^2 s wit F(cent)=0.897exp(-T/601).
""",
)

entry(
    index = 257,
    label = "C2H5O2 <=> O2 + C2H5",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.17e+17, 's^-1'),
        n = -0.83,
        Ea = (143.009, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (1013, 'Pa'),
        Pmax = (1.01e+06, 'Pa'),
    ),
    reference = Article(
        authors = ["Wagner, A.F.", "Slagle, I.R.", "Sarzynski, D.", "Gutman, D."],
        title = u'Experimental and theoretical studies of the C2H5 + O2 reaction kinetics',
        journal = "J. Phys. Chem.",
        volume = "94",
        pages = """1853-1868""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990WAG/SLA1853-1868:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00013875
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 258,
    label = "C2H5O2 <=> O2 + C2H5",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.46e+18, 's^-1'),
        n = -1.07,
        Ea = (147.779, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (250, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Sheng, C.Y.", "Bozzelli, J.W.", "Dean, A.M.", "Chang, A.Y."],
        title = u'Detailed Kinetics and Thermochemistry of C2H5 + O2:  Reaction Kinetics of the Chemically-Activated and Stabilized CH3CH2OO. Adduct',
        journal = "J. Phys. Chem. A",
        volume = "106",
        pages = """7276-7293""",
        year = "2002",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2002SHE/BOZ7276-7293:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00013875
Pressure dependence: Rate constant is high pressure limit
""",
)

entry(
    index = 259,
    label = "C4H8-4 <=> C4H7-2 + H",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.26e+15, 's^-1'),
        n = 0,
        Ea = (345.051, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:13",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00004651
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004651/rk00000001.xml
""",
)

entry(
    index = 260,
    label = "C4H8-5 <=> C4H7-3 + H",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (3.98e+15, 's^-1'),
        n = 0,
        Ea = (355.859, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:17",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00004826
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004826/rk00000001.xml
""",
)

entry(
    index = 261,
    label = "C4H4 <=> C4H3 + H",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.58e+15, 's^-1'),
        n = 0,
        Ea = (414.061, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988GHI/COL5839:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00008727
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008727/rk00000001.xml
""",
)

entry(
    index = 262,
    label = "H + C4H3 <=> C4H4-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.15e+08, 'm^3/(mol*s)'),
        n = 0,
        Ea = (3.367, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (1300, 'K'),
        Pmin = (10100, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Duran, R.P.", "Amorebieta, V.T.", "Colussi, A.J."],
        title = u'Is the homogeneous thermal dimerization of acetylene a free-radical chain reaction? Kinetic and thermochemical analysis',
        journal = "J. Phys. Chem.",
        volume = "92",
        pages = """636""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988DUR/AMO636:11",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00008727
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008727/rk00000002.xml
""",
)

entry(
    index = 263,
    label = "C4H4-3 <=> H + C4H3-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.1e+13, 's^-1'),
        n = 0,
        Ea = (335.073, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1200, 'K'),
        Tmax = (1750, 'K'),
        Pmin = (30400, 'Pa'),
        Pmax = (60800, 'Pa'),
    ),
    reference = Article(
        authors = ["Hidaka, Y.", "Tanaka, K.", "Suga, M."],
        title = u'Thermal decomposition of vinylacetylene in shock waves. Rate constant of initiation reaction',
        journal = "Chem. Phys. Lett.",
        volume = "130",
        pages = """195""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986HID/TAN195:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00008728
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008728/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 264,
    label = "C4H4-3 <=> H + C4H3-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.3e+13, 's^-1'),
        n = 0,
        Ea = (364.174, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1170, 'K'),
        Tmax = (1690, 'K'),
        Pmin = (132000, 'Pa'),
        Pmax = (233000, 'Pa'),
    ),
    reference = Article(
        authors = ["Hidaka, Y.", "Masaoka, H.", "Oshita, H.", "Nakamura, T.", "Tanaka, K.", "Kawano, H."],
        title = u'Thermal decomposition of vinylacetylene in shock waves',
        journal = "Int. J. Chem. Kinet.",
        volume = "24",
        pages = """871-885""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992HID/MAS871-885:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00008728
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008728/rk00000002.xml
Bath gas: He
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 265,
    label = "C4H10-3 <=> C3H7 + CH3",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (7.94e+18, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (335.073, 'kJ/mol', '+|-', 10.061),
        T0 = (1, 'K'),
        Tmin = (823, 'K'),
        Tmax = (853, 'K'),
        Pmin = (2.03e+06, 'Pa'),
        Pmax = (7.09e+06, 'Pa'),
    ),
    reference = Article(
        authors = ["Brooks, C.T."],
        title = u'Gas-phase high-pressure decomposition of isobutane in the presence of hydrogen',
        journal = "Trans. Faraday Soc.",
        volume = "62",
        pages = """935-944""",
        year = "1966",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1966BRO935-944:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010181
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010181/rk00000005.xml
Uncertainty: 3.1600001
Bath gas: iso-C4H10
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 266,
    label = "C4H10-3 <=> C3H7 + CH3",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (6.31e+17, 's^-1'),
        n = 0,
        Ea = (345.051, 'kJ/mol', '+|-', 13.802),
        T0 = (1, 'K'),
        Tmin = (713, 'K'),
        Tmax = (814, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (20000, 'Pa'),
    ),
    reference = Article(
        authors = ["Konar, R.S.", "Marshall, R.M.", "Purnell, J.H."],
        title = u'Initiation of isobutane pyrolysis',
        journal = "Trans. Faraday Soc.",
        volume = "64",
        pages = """405-413""",
        year = "1968",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1968KON/MAR405-413:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010181
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010181/rk00000008.xml
Bath gas: iso-C4H10
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 267,
    label = "C4H10-3 <=> C3H7 + CH3",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (8.71e+09, 's^-1'),
        n = 0,
        Ea = (202.042, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1200, 'K'),
        Tmax = (1500, 'K'),
        Pmin = (65100, 'Pa'),
        Pmax = (90000, 'Pa'),
    ),
    reference = Article(
        authors = ["Bradley, J.N."],
        title = u'A general mechanism for the high-temperature pyrolysis of alkanes. The pyrolysis of isobutane',
        journal = "Proc. R. Soc. London A",
        volume = "337",
        pages = """199""",
        year = "1974",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1974BRA199:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010181
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010181/rk00000009.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 268,
    label = "C4H10-3 <=> C3H7 + CH3",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.51e+16, 's^-1'),
        n = 0,
        Ea = (346.713, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1100, 'K'),
        Tmax = (1280, 'K'),
    ),
    reference = Article(
        authors = ["Golden, D.M.", "Alfassi, Z.B.", "Beadle, P.C."],
        title = u"Very Low-Pressure Pyrolysis (VLPP) of Alkanes: n-Butane, 2,3-Dimethylbutane, 2,2',3,3'-Tetramethylbutane, and Isobutane",
        journal = "Int. J. Chem. Kinet.",
        volume = "6",
        pages = """359""",
        year = "1974",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1974GOL/ALF359:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010181
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010181/rk00000010.xml
Bath gas: iso-C4H10
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 269,
    label = "C4H10-3 <=> C3H7 + CH3",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (8.39e+15, 's^-1'),
        n = 0,
        Ea = (357.522, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (970, 'K'),
        Tmax = (1030, 'K'),
        Pmin = (80000, 'Pa'),
        Pmax = (80000, 'Pa'),
    ),
    reference = Article(
        authors = ["Pratt, G.L.", "Rogers, D."],
        title = u'Wall-less Reactor Studies. Part 4. - Isobutane Pyrolysis',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "76",
        pages = """1694""",
        year = "1980",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1980PRA/ROG1694:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010181
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010181/rk00000011.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 270,
    label = "C4H10-3 <=> C3H7 + CH3",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1.66e+11, 's^-1', '*|/', 3.08),
        n = 0,
        Ea = (202.042, 'kJ/mol', '+|-', 10.144),
        T0 = (1, 'K'),
        Tmin = (973, 'K'),
        Tmax = (1120, 'K'),
        Pmin = (13300, 'Pa'),
        Pmax = (13300, 'Pa'),
    ),
    reference = Article(
        authors = ["Shevel'kova, L.V.", "Ivanvuk, A.V.", "Nametkin, N.S."],
        title = u'Comparative Study of the Pyrolysis of n-Butane and Isobutane',
        journal = "Neftekhimiya",
        volume = "20",
        pages = """837""",
        year = "1980",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1980SHE/IVA837:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010181
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010181/rk00000012.xml
Uncertainty: 3.0799999
Bath gas: H2
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 271,
    label = "C4H10-3 <=> C3H7 + CH3",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (6.31e+12, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (254.423, 'kJ/mol', '+|-', 20.37),
        T0 = (1, 'K'),
        Tmin = (1300, 'K'),
        Tmax = (1800, 'K'),
        Pmin = (50700, 'Pa'),
        Pmax = (50700, 'Pa'),
    ),
    reference = Article(
        authors = ["Koike, T.", "Morinaga, K."],
        title = u'UV Absorption Studies of the Pyrolysis of Isobutane in Shock Waves',
        journal = "Bull. Chem. Soc. Jpn.",
        volume = "55",
        pages = """690""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982KOI/MOR690:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010181
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010181/rk00000013.xml
Uncertainty: 3.1600001
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 272,
    label = "C4H10-3 <=> C3H7 + CH3",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (4e+16, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (346.713, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Book(
        authors = ["Warnatz, J."],
        title = u'Rate coefficients in the C/H/O system',
        publisher = "ed. W.C. Gardiner,Jr., pub. Springer-Verlag,NY",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984WAR197C:55",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010181
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010181/rk00000014.xml
Uncertainty: 3.1600001
""",
)

entry(
    index = 273,
    label = "C4H10-3 <=> C3H7 + CH3",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (4.5e+16, 's^-1', '*|/', 1.5),
        n = 0,
        Ea = (339.23, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1560, 'K'),
        Pmin = (132000, 'Pa'),
        Pmax = (293000, 'Pa'),
    ),
    reference = Article(
        authors = ["Hidaka, Y.", "Fujiwara, M.", "Oki, T.", "Kawano, H."],
        title = u'Thermal decomposition of isobutane in shock waves. Rate constant of initiation reaction',
        journal = "Chem. Phys. Lett.",
        volume = "144",
        pages = """570""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988HID/FUJ570:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010181
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010181/rk00000015.xml
Uncertainty: 1.5
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 274,
    label = "C4H10-3 <=> C3H7 + CH3",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1.1e+26, 's^-1', '*|/', 2),
        n = -2.61,
        Ea = (378.308, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:20",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010181
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010181/rk00000016.xml
Uncertainty: 2.0
""",
)

entry(
    index = 275,
    label = "C2H5 + C2H5 <=> C4H10-4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.59e+08, 'm^3/(mol*s)'),
        n = 0,
        Ea = (11.391, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (323, 'K'),
        Tmax = (423, 'K'),
        Pmin = (1107, 'Pa'),
        Pmax = (6066, 'Pa'),
    ),
    reference = Article(
        authors = ["Shepp, A.", "Kutschke, K.O."],
        title = u'Rate of recombination of radicals. III. Rate of recombination of ethyl radicals',
        journal = "J. Chem. Phys.",
        volume = "26",
        pages = """1020-1028""",
        year = "1957",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1957SHE/KUT1020-1028:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010242
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010242/rk00000002.xml
Bath gas: (C2H5)2CO
Excitation technique: Direct photolysis
Analytical technique: Pressure measurement
""",
)

entry(
    index = 276,
    label = "C2H5 + C2H5 <=> C4H10-4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.59e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (0.798, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972TEN/JON1267:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010242
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010242/rk00000009.xml
Bath gas: H2
Excitation technique: Electron beam
Analytical technique: Gas chromatography
""",
)

entry(
    index = 277,
    label = "C4H6-7 <=> C3H3-3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+12, 's^-1'),
        n = 0,
        Ea = (248.603, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1300, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (20300, 'Pa'),
        Pmax = (55700, 'Pa'),
    ),
    reference = Article(
        authors = ["Kern, R.D.", "Singh, H.J.", "Wu, C.H."],
        title = u'Thermal decomposition of 1,2 butadiene',
        journal = "Int. J. Chem. Kinet.",
        volume = "20",
        pages = """731""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988KER/SIN731:7",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from detailed balance/reverse rate""",
    longDesc = 
u"""
PrIMe Reaction: r00010784
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010784/rk00000003.xml
Bath gas: Ne
""",
)

entry(
    index = 278,
    label = "C4H6-7 <=> C3H3-3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+15, 's^-1'),
        n = 0,
        Ea = (313.456, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1100, 'K'),
        Tmax = (1600, 'K'),
    ),
    reference = Article(
        authors = ["Hidaka, Y.", "Higashihara, T.", "Ninomiya, N.", "Oshita, H.", "Kawano, H."],
        title = u'Thermal isomerization and decomposition of 2-butyne in shock waves',
        journal = "J. Phys. Chem.",
        volume = "97",
        pages = """10977-10983""",
        year = "1993",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1993HID/HIG10977-10983:10",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010784
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010784/rk00000004.xml
Bath gas: Ar
""",
)

entry(
    index = 279,
    label = "C4H6-8 <=> C2H3 + C2H3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.1e+16, 's^-1'),
        n = 0,
        Ea = (390.78, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1600, 'K'),
        Tmax = (1900, 'K'),
        Pmin = (14700, 'Pa'),
        Pmax = (78000, 'Pa'),
    ),
    reference = Article(
        authors = ["Kiefer, J.H.", "Wei, H.C.", "Kern, R.D.", "Wu, C.H."],
        title = u'The high temperature pyrolysis of 1,3-butadiene: Heat of formation and rate of dissociation of vinyl radical',
        journal = "Int. J. Chem. Kinet.",
        volume = "17",
        pages = """225-253""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985KIE/WEI225-253:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011415
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011415/rk00000009.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Laser schlieren
""",
)

entry(
    index = 280,
    label = "C4H6-8 <=> C2H3 + C2H3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.07e+12, 's^-1'),
        n = 0,
        Ea = (278.535, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1300, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (20300, 'Pa'),
        Pmax = (55700, 'Pa'),
    ),
    reference = Article(
        authors = ["Kern, R.D.", "Singh, H.J.", "Wu, C.H."],
        title = u'Thermal decomposition of 1,2 butadiene',
        journal = "Int. J. Chem. Kinet.",
        volume = "20",
        pages = """731""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988KER/SIN731:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from detailed balance/reverse rate""",
    longDesc = 
u"""
PrIMe Reaction: r00011415
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011415/rk00000010.xml
Bath gas: Ne
""",
)

entry(
    index = 281,
    label = "C4H6-8 <=> C2H3 + C2H3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.07e+17, 's^-1', '*|/', 2),
        n = 0,
        Ea = (393.275, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1660, 'K'),
        Tmax = (2220, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (93300, 'Pa'),
    ),
    reference = Article(
        authors = ["Kiefer, J.H.", "Mitchell, K.I.", "Wei, H.C."],
        title = u'The high temperature pyrolysis of 1,3-butadiene II: Pulsed laser flash absorption rate constants, and consideration of possible molecular dissociation pathways',
        journal = "Int. J. Chem. Kinet.",
        volume = "20",
        pages = """787""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988KIE/MIT787:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011415
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011415/rk00000011.xml
Uncertainty: 2.0
Bath gas: Ar
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 282,
    label = "C4H6-8 <=> C2H3 + C2H3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.8e+13, 's^-1'),
        n = 0,
        Ea = (355.859, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1560, 'K'),
        Tmax = (2210, 'K'),
        Pmin = (273000, 'Pa'),
        Pmax = (273000, 'Pa'),
    ),
    reference = Article(
        authors = ["Rao, V.S.", "Takeda, K.", "Skinner, G.B."],
        title = u'Formation of H and D atoms in pyrolysis of 1,3-butadiene and 1,3 butadiene-1,1,4,4,-d4 behind shock waves',
        journal = "Int. J. Chem. Kinet.",
        volume = "20",
        pages = """153""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988RAO/TAK153:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011415
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011415/rk00000012.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 283,
    label = "C4H10O <=> C2H5O-3 + C2H5",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.58e+17, 's^-1', '*|/', 5),
        n = 0,
        Ea = (345.051, 'kJ/mol', '+|-', 6.893),
        T0 = (1, 'K'),
        Tmin = (697, 'K'),
        Tmax = (761, 'K'),
        Pmin = (4400, 'Pa'),
        Pmax = (21700, 'Pa'),
    ),
    reference = Article(
        authors = ["Seres, I.", "Huhn, P."],
        title = u'Radical steps in diethyl ether decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "18",
        pages = """829""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986SER/HUH829:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00001558
Uncertainty: 5.0
Bath gas: (C2H5)2O
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 284,
    label = "C4H10O <=> C2H5O-3 + C2H5",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.51e+15, 's^-1'),
        n = 0,
        Ea = (320.939, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978FOU/MAR132:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00001558
Bath gas: (C2H5)2O
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 285,
    label = "C4H10O <=> C2H5O-3 + C2H5",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5e+15, 's^-1'),
        n = 0,
        Ea = (339.23, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (763, 'K'),
        Tmax = (823, 'K'),
        Pmin = (3333, 'Pa'),
        Pmax = (53300, 'Pa'),
    ),
    reference = Article(
        authors = ["Seres, I.", "Labadi, I.", "Huhn, P."],
        title = u'A Dietil-Eter Termikus Bomlasa, IV. Az Acetaldehid Hatasa a Bomlasra, [The Thermal Decomposition of Diethyl Ether, IV. The Effect of Acetaldehyde]',
        journal = "Magy. Kem. Foly.",
        volume = "83",
        pages = """151""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977SER/LAB151:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00001558
Bath gas: (C2H5)2O
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 286,
    label = "C4H10O <=> C2H5O-3 + C2H5",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2e+14, 's^-1'),
        n = 0,
        Ea = (324.264, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975SER/HUH120-123:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00001558
Bath gas: (C2H5)2O
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 287,
    label = "C4H10O <=> C2H5O-3 + C2H5",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2e+14, 's^-1'),
        n = 0,
        Ea = (324.264, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (790, 'K'),
        Tmax = (810, 'K'),
        Pmin = (26700, 'Pa'),
        Pmax = (26700, 'Pa'),
    ),
    reference = Article(
        authors = ["Seres, I.", "Huhn, P."],
        title = u'A dietil-eter termikus bomlasa, III.',
        journal = "Magy. Kem. Foly.",
        volume = "81",
        pages = """120-123""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975SER/HUH120-123:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00001558
Bath gas: (C2H5)2O
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 288,
    label = "C4H10O <=> C2H5O-3 + C2H5",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.7e+12, 's^-1'),
        n = 0,
        Ea = (241.12, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (833, 'K'),
        Tmax = (893, 'K'),
        Pmin = (2000, 'Pa'),
        Pmax = (42700, 'Pa'),
    ),
    reference = Article(
        authors = ["Laidler, K.J.", "McKenney, D.J."],
        title = u'Kinetics and mechanisms of the pyrolysis of diethyl ether. I. The uninhibited reaction',
        journal = "Proc. R. Soc. London",
        volume = "278",
        pages = """505-516""",
        year = "1964",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1964LAI/MCK505-516:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00001558
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00001558/rk00000001.xml
Bath gas: (C2H5)2O
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 289,
    label = "C4H10O-2 <=> C3H7O + CH3",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (6.31e+16, 's^-1'),
        n = 0,
        Ea = (340.062, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976TSA173:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00003588
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00003588/rk00000001.xml
Bath gas: Ar
""",
)

entry(
    index = 290,
    label = "C2H4O3 <=> OH + C2H3O2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+14, 's^-1', '*|/', 2.51),
        n = 0,
        Ea = (167.952, 'kJ/mol', '+|-', 3.359),
        T0 = (1, 'K'),
        Tmin = (533, 'K'),
        Tmax = (720, 'K'),
        Pmin = (30400, 'Pa'),
        Pmax = (203000, 'Pa'),
    ),
    reference = Article(
        authors = ["Sahetchian, K.A.", "Rigny, R.", "Tardieu de Maleissye, J.", "Batt, L.", "Anwar Khan, M.", "Mathews, S."],
        title = u'The pyrolysis of organic hydroperoxides (ROOH)',
        journal = "Symp. Int. Combust. Proc.",
        volume = "24",
        pages = """637-643""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992SAH/RIG637-643:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00004010
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004010/rk00000001.xml
Uncertainty: 2.51
Bath gas: H2
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 291,
    label = "C5H10 <=> C3H5 + C2H5",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+16, 's^-1', '*|/', 2),
        n = 0,
        Ea = (295.995, 'kJ/mol', '+|-', 8.896),
        T0 = (1, 'K'),
        Tmin = (900, 'K'),
        Tmax = (1220, 'K'),
    ),
    reference = Article(
        authors = ["Brown, T.C.", "King, K.D.", "Nguyen, T.T."],
        title = u'Kinetics of primary processes in the pyrolysis of cyclopentanes and cyclohexanes',
        journal = "J. Phys. Chem.",
        volume = "90",
        pages = """419""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986BRO/KIN419:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from detailed balance/reverse rate""",
    longDesc = 
u"""
PrIMe Reaction: r00005303
Uncertainty: 2.0
""",
)

entry(
    index = 292,
    label = "C5H10 <=> C3H5 + C2H5",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+16, 's^-1', '*|/', 1.1),
        n = 0,
        Ea = (298.49, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1200, 'K'),
        Pmin = (172000, 'Pa'),
        Pmax = (172000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Thermal Decomposition of Cyclopentane and Related Compounds',
        journal = "Int. J. Chem. Kinet.",
        volume = "10",
        pages = """599""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978TSA599:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00005303
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00005303/rk00000001.xml
Uncertainty: 1.1
Bath gas: Ar
""",
)

entry(
    index = 293,
    label = "C4H8O <=> C2H3O-2 + C2H5",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+15, 's^-1'),
        n = 0,
        Ea = (275.209, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Rosenfeld, R.N.", "Brauman, J.I.", "Barker, J.R.", "Golden, D.M."],
        title = u'Infrared photodecomposition of ethyl vinyl ether. A chemical probe of multiphoton dynamics',
        journal = "J. Am. Chem. Soc.",
        volume = "99",
        pages = """8063-8064""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977ROS/BRA8063-8064:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00005356
Bath gas: CH2=CHOC2H5
""",
)

entry(
    index = 294,
    label = "C4H8O <=> C2H3O-2 + C2H5",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8e+15, 's^-1'),
        n = 0,
        Ea = (292.669, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (812, 'K'),
        Tmax = (840, 'K'),
        Pmin = (2666, 'Pa'),
        Pmax = (2666, 'Pa'),
    ),
    reference = Article(
        authors = ["Blades, A.T.", "Murphy, G.W."],
        title = u'Kinetics of the thermal decomposition of vinyl ethyl ether',
        journal = "J. Am. Chem. Soc.",
        volume = "74",
        pages = """1039-1041""",
        year = "1952",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1952BLA/MUR1039-1041:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005356
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00005356/rk00000001.xml
Bath gas: Toluene
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 295,
    label = "C5H8 <=> C4H5-2 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2e+16, 's^-1', '*|/', 2),
        n = 0,
        Ea = (299.321, 'kJ/mol', '+|-', 2.993),
        T0 = (1, 'K'),
        Tmin = (940, 'K'),
        Tmax = (1220, 'K'),
    ),
    reference = Article(
        authors = ["Nguyen, T.T.", "King, K.D."],
        title = u'Kinetics of Decomposition and Interconversion of 3-Methylbut-1-yne and 3-Methylbuta-1,2-diene. Resonance Stabilization Energies of Propargylic Radicals',
        journal = "J. Phys. Chem.",
        volume = "85",
        pages = """3130""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981NGU/KIN3130:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00008082
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008082/rk00000001.xml
Uncertainty: 2.0
Bath gas: (CH3)2CHCCH
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 296,
    label = "C4H8O-2 <=> C3H5O-2 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.82e+16, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (289.344, 'kJ/mol', '+|-', 2.893),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1973TRE1737:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00008095
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008095/rk00000001.xml
Uncertainty: 3.1600001
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 297,
    label = "C5H8-2 <=> C4H5-3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+16, 's^-1', '*|/', 2),
        n = 0,
        Ea = (303.478, 'kJ/mol', '+|-', 9.146),
        T0 = (1, 'K'),
        Tmin = (1050, 'K'),
        Tmax = (1150, 'K'),
    ),
    reference = Article(
        authors = ["Nguyen, T.T.", "King, K.D."],
        title = u'Very Low-Pressure Pyrolysis (VLPP ) of Pentynes. III. Pent-2-yne. Heat of Formation and Resonance Stabilization Energy of the 3-Methylpropargyl Radical',
        journal = "Int. J. Chem. Kinet.",
        volume = "14",
        pages = """613""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982NGU/KIN613:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00008396
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008396/rk00000001.xml
Uncertainty: 2.0
Bath gas: C2H5CCCH3
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 298,
    label = "C4H9-3 + CH3 <=> C5H12",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.63e+07, 'm^3/(mol*s)', '*|/', 2),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990TSA1-68:74",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00009801
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009801/rk00000001.xml
Uncertainty: 2.0
""",
)

entry(
    index = 299,
    label = "C4H9-3 + CH3 <=> C5H12",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.99e+08, 'm^3/(mol*s)'),
        n = -0.67,
        Ea = (-0.614, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Klippenstein, S.J.", "Georgievskii, Y.", "Harding, L.B."],
        title = u'Predictive theory for the combination kinetics of two alkyl radicals',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "8",
        pages = """1133-1147""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006KLI/GEO1133-1147:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00009801
Pressure dependence: Rate constant is high pressure limit

Rate constants were calculated with an ab initio transition state theory employing direct evaluations of the orientation dependent interaction energies at the CASPT2/cc-pvdz level within variable reaction
coordinate transition state theory (VRC-TST). Results were compared with experiment for a series of alkyl radicals and the good quantitative agreement was found.

Each methyl substituent adjacent to a radical site was found to reduce the rate coefficient by about a factor of two. Rate constants are predicted to decrease substantially with increasing temperature, with the more sterically hindered reactants having a more rapid decrease. The geometric mean rule was found to be in good agreement with the detailed calculations.

The authors state the rate parameters are strictly applicable between 200-2000 K but that they should provide reasonable predictions up to about 2700 K.
""",
)

entry(
    index = 300,
    label = "C5H12 <=> C4H9-3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.1e+13, 's^-1'),
        n = 0,
        Ea = (259.412, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1230, 'K'),
        Tmax = (1460, 'K'),
        Pmin = (35500, 'Pa'),
        Pmax = (35500, 'Pa'),
    ),
    reference = Article(
        authors = ["Rao, V.S.", "Skinner, G.B."],
        title = u'Further experiments on pyrolysis of 2,2-dimethylpropane behind shock waves',
        journal = "Int. J. Chem. Kinet.",
        volume = "20",
        pages = """165""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988RAO/SKI165:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009801
Bath gas: He
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 301,
    label = "C5H12 <=> C4H9-3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.7e+17, 's^-1', '*|/', 2),
        n = 0,
        Ea = (351.702, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1140, 'K'),
        Tmax = (1300, 'K'),
        Pmin = (203000, 'Pa'),
        Pmax = (304000, 'Pa'),
    ),
    reference = Article(
        authors = ["Bernfeld, D.", "Skinner, G.B."],
        title = u'Formation of hydrogen atoms in pyrolysis of 2,2-dimethylpropane behind shock waves',
        journal = "J. Phys. Chem.",
        volume = "87",
        pages = """3732""",
        year = "1983",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1983BER/SKI3732:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00009801
Uncertainty: 2.0
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 302,
    label = "C5H12 <=> C4H9-3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+17, 's^-1'),
        n = 0,
        Ea = (338.399, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1260, 'K'),
    ),
    reference = Article(
        authors = ["Baldwin, A.C.", "Lewis, K.E.", "Golden, D.M."],
        title = u'Very-Low-Pressure Pyrolysis (VLPP) of Group IV(A) Tetramethyls: Neopentane and Tetramethyltin',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """529""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979BAL/LEW529:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009801
Bath gas: neo-C5H12
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 303,
    label = "C5H12 <=> C4H9-3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+17, 's^-1'),
        n = 0,
        Ea = (351.702, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (703, 'K'),
        Tmax = (743, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (6666, 'Pa'),
    ),
    reference = Article(
        authors = ["Marquaire, P.M.", "Come, G.M."],
        title = u'Non Quasi-Stationary State Pyrolysis. Kinetic Parameters of Neopentane Pyrolysis Mechanism',
        journal = "React. Kinet. Catal. Lett.",
        volume = "9",
        pages = """171""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978MAR/COM171:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009801
Bath gas: neo-C5H12
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 304,
    label = "C5H12 <=> C4H9-3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+16, 's^-1', '*|/', 5),
        n = 0,
        Ea = (330.085, 'kJ/mol', '+|-', 16.463),
        T0 = (1, 'K'),
        Tmin = (756, 'K'),
        Tmax = (845, 'K'),
        Pmin = (13300, 'Pa'),
        Pmax = (26700, 'Pa'),
    ),
    reference = Article(
        authors = ["Marshall, R.M.", "Purnell, H.", "Storey, P.D."],
        title = u'Chain Initiation of Neopentane Pyrolysis and a Suggested Reconciliation of the Thermochemically Calculated and Measured Rate Constants for the Recombination of t-Butyl Radicals',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "72",
        pages = """85""",
        year = "1976",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976MAR/PUR85:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009801
Uncertainty: 5.0
Bath gas: neo-C5H12
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 305,
    label = "C5H12 <=> C4H9-3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.3e+16, 's^-1'),
        n = 0,
        Ea = (335.905, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976BRA/WES8:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00009801
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 306,
    label = "C5H12 <=> C4H9-3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+17, 's^-1', '*|/', 2),
        n = 0,
        Ea = (355.859, 'kJ/mol', '+|-', 7.117),
        T0 = (1, 'K'),
        Tmin = (793, 'K'),
        Tmax = (953, 'K'),
        Pmin = (2666, 'Pa'),
        Pmax = (53300, 'Pa'),
    ),
    reference = Article(
        authors = ["Pacey, P.D."],
        title = u'The Reaction of Methyl Radicals with Neopentane',
        journal = "Can. J. Chem.",
        volume = "51",
        pages = """2415""",
        year = "1973",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1973PAC2415:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009801
Uncertainty: 2.0
Bath gas: neo-C5H12
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 307,
    label = "C5H12 <=> C4H9-3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+16, 's^-1'),
        n = 0,
        Ea = (343.388, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (723, 'K'),
        Tmax = (803, 'K'),
        Pmin = (3333, 'Pa'),
        Pmax = (26700, 'Pa'),
    ),
    reference = Article(
        authors = ["Baronnet, F.", "Dzierzynski, M.", "Come, G.M.", "Martin, R.", "Niclause, M."],
        title = u'The Pyrolysis of Neopentane at Small Extents of Reaction',
        journal = "Int. J. Chem. Kinet.",
        volume = "3",
        pages = """197""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971BAR/DZI197:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009801
Bath gas: neo-C5H12
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 308,
    label = "C5H12 <=> C4H9-3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+16, 's^-1'),
        n = 0,
        Ea = (336.736, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (923, 'K'),
        Tmax = (1070, 'K'),
    ),
    reference = Article(
        authors = ["Taylor, J.E.", "Hutchings, D.A.", "Frech, K.J."],
        title = u'Homogeneous gas-phase pyrolyses using a wall-less reactor. I. Neopentane',
        journal = "J. Am. Chem. Soc.",
        volume = "91",
        pages = """2215-2219""",
        year = "1969",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1969TAY/HUT2215-2219:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009801
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 309,
    label = "C5H12 <=> C4H9-3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.12e+18, 's^-1', '*|/', 5),
        n = 0,
        Ea = (359.185, 'kJ/mol', '+|-', 10.809),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (833, 'K'),
        Pmin = (2666, 'Pa'),
        Pmax = (73300, 'Pa'),
    ),
    reference = Article(
        authors = ["Halstead, M.P.", "Konar, R.S.", "Leathard, D.A.", "Marshall, R.M.", "Purnell, J.H."],
        title = u'The self-inhibited pyrolysis of neopentane at small extents of reaction',
        journal = "Proc. R. Soc. London A",
        volume = "310",
        pages = """525""",
        year = "1969",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1969HAL/KON525:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009801
Uncertainty: 5.0
Bath gas: neo-C5H12
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 310,
    label = "C5H12 <=> C4H9-3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+16, 's^-1'),
        n = 0,
        Ea = (327.59, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1100, 'K'),
        Pmin = (304000, 'Pa'),
        Pmax = (304000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Thermal decomposition of hexamethylethane, 2,2,3-trimethylbutane, and neopentane in a single-pulse shock tube',
        journal = "J. Chem. Phys.",
        volume = "44",
        pages = """4283-4295""",
        year = "1966",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1966TSA4283-4295:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00009801
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 311,
    label = "C5H12 <=> C4H9-3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.47e+16, 's^-1'),
        n = 0,
        Ea = (343.388, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (800, 'K'),
    ),
    reference = Article(
        authors = ["Mitchell, T.J.", "Benson, S.W."],
        title = u'Modelling of the homogeneously catalyzed and uncatalyzed pyrolysis of neopentane: thermochemistry of the neopentyl radical',
        journal = "Int. J. Chem. Kinet.",
        volume = "25",
        pages = """931-955""",
        year = "1993",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1993MIT/BEN931-955:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00009801
""",
)

entry(
    index = 312,
    label = "C5H12 <=> C4H9-3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.38e+15, 's^-1', '*|/', 1.23),
        n = 0,
        Ea = (333.41, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (945, 'K'),
        Tmax = (1020, 'K'),
        Pmin = (80000, 'Pa'),
        Pmax = (80000, 'Pa'),
    ),
    reference = Article(
        authors = ["Pratt, G.L.", "Rogers, D."],
        title = u'Wall-less Studies. Part 5. - Neopentane Pyrolysis',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "77",
        pages = """2751""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981PRA/ROG2751:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00009801
Uncertainty: 1.23
Bath gas: Ar
""",
)

entry(
    index = 313,
    label = "C3H7 + O2 <=> C3H7O2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.84e+39, 'm^3/(mol*s)'),
        n = -11.1,
        Ea = (27.355, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003DES/KLI4415-4427:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00010210
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010210/rk00000007.xml
Bath gas: He

Rate constants are based in part on master equation simulations employing transition states from quantum calculations. This work is a combined experimental, theory, and modeling study. Compared OH profiles with those from modeling. Model describes HO2 profiles well, but is not as good for OH profiles.

Static cell (low flow), 296-700 K, He buffer typically 3.65E17 cm-3 (10-20 torr), O2 typically 6.3E15 cm-3. Radicals produced by RH + Cl -> R + HCl, where Cl produced by 193 nm excimer laser photolysis of CCl3F. OH detected using LIF at 281.996 nm.

Employed earlier quantum calculations (see references below) combined with master equation modeling to provide rate expressions for many reactions in this system. Only a few rate expressions are abstracted here.

Miller and Klippenstein, IJCK 33, 654 (2001)
DeSain et al, Farad. Disc. 119, 101 (2001)
""",
)

entry(
    index = 314,
    label = "C5H6 <=> C5H5 + H",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.7e+14, 's^-1'),
        n = 0,
        Ea = (312.042, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1200, 'K'),
        Tmax = (1600, 'K'),
        Pmin = (200000, 'Pa'),
        Pmax = (200000, 'Pa'),
    ),
    reference = Article(
        authors = ["Roy, K.", "Braun-Unkhoff, M.", "Frank, P.", "Just, Th."],
        title = u'Kinetics of the Cyclopentadiene Decay and the Recombination of Cyclopentadienyl Radicals with H-Atoms: Enthalpy of Formation of the Cyclopentadienyl Radical',
        journal = "Int. J. Chem. Kinet.",
        volume = "33",
        pages = """821-833""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001ROY/BRA821-833:2",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010419

1) No formal statistical deviation presented.
2) The data are used in a 3rd law derivation of the heat of formation for cyclopentadienyl radical of Delta Hf,0=65.4 kJ/mole and Delta Hf,298=62.4 kJ/mole.
3) Extensive discussion of the fall-off behavior is given.
""",
)

entry(
    index = 315,
    label = "C5H6 <=> C5H5 + H",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5e+15, 's^-1'),
        n = 0,
        Ea = (329.253, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1080, 'K'),
        Tmax = (1550, 'K'),
        Pmin = (172000, 'Pa'),
        Pmax = (973000, 'Pa'),
    ),
    reference = Article(
        authors = ["Burcat, A.", "Dvinyaninov, M."],
        title = u'Detailed kinetics of cyclopentadiene decomposition studied in a shock tube',
        journal = "Int. J. Chem. Kinet.",
        volume = "29",
        pages = """505-514""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997BUR/DVI505-514:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010419
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010419/rk00000004.xml
Bath gas: Ar
Excitation technique: Thermal
Time resolution: In real time
Analytical technique: Gas chromatography
""",
)

entry(
    index = 316,
    label = "C5H6 <=> C5H5 + H",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.55e+18, 's^-1'),
        n = -0.8,
        Ea = (351.702, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Tokmakov, I.V.", "Moskaleva, L.V.", "Lin, M.C."],
        title = u'Quantum chemical/vRRKM study on the thermal decomposition of cyclopentadiene',
        journal = "Inter. J. Chem. Kinet.",
        volume = "36",
        pages = """139-151""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004TOK/MOS139-151:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00010419
Pressure dependence: Rate constant is high pressure limit

Reaction PES was studied using quantum chemistry. Rate constants were calculated as functions of temperature and pressure using variational transition state theory, RRKM, and master equation analysis of falloff effects.
""",
)

entry(
    index = 317,
    label = "C5H6 <=> C5H5 + H",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.5e+15, 's^-1'),
        n = 0,
        Ea = (343.088, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1476, 'K'),
        Tmax = (1618, 'K'),
    ),
    reference = Article(
        authors = ["Bacskay, G.B.", "Mackie, J.C."],
        title = u'The Pyrolysis of Cyclopentadiene: Quantum Chemical and Kinetic Modelling Studies of the Acetylene Plus Propyne/Allene Decomposition Channels',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "3",
        pages = """2467-2473""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001BAC/MAC2467-2473:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00010419
Pressure dependence: Rate constant is high pressure limit
""",
)

entry(
    index = 318,
    label = "C5H5 + H <=> C5H6",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.67e+08, 'm^3/(mol*s)'),
        n = 0,
        Ea = (2.037, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Tokmakov, I.V.", "Moskaleva, L.V.", "Lin, M.C."],
        title = u'Quantum chemical/vRRKM study on the thermal decomposition of cyclopentadiene',
        journal = "Inter. J. Chem. Kinet.",
        volume = "36",
        pages = """139-151""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004TOK/MOS139-151:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00010419
Pressure dependence: Rate constant is high pressure limit

Reaction PES was studied using quantum chemistry. Rate constants were calculated as functions of temperature and pressure using variational transition state theory, RRKM, and master equation analysis of falloff effects.
""",
)

entry(
    index = 319,
    label = "C3H7-2 + O2 <=> C3H7O2-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.82e+30, 'm^3/(mol*s)'),
        n = -8.23,
        Ea = (21.618, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003DES/KLI4415-4427:7",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00010545
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010545/rk00000009.xml
Bath gas: He
Pressure dependence: Rate constant is pressure dependent

Rate constants are based in part on master equation simulations employing transition states from quantum calculations. This work is a combined experimental, theory, and modeling study. Compared OH profiles with those from modeling. Model describes HO2 profiles well, but is not as good for OH profiles.

Static cell (low flow), 296-700 K, He buffer typically 3.65E17 cm-3 (10-20 torr), O2 typically 6.3E15 cm-3. Radicals produced by RH + Cl -> R + HCl, where Cl produced by 193 nm excimer laser photolysis of CCl3F. OH detected using LIF at 281.996 nm.

Employed earlier quantum calculations (see references below) combined with master equation modeling to provide rate expressions for many reactions in this system. Only a few rate expressions are abstracted here.

Miller and Klippenstein, IJCK 33, 654 (2001)
DeSain et al, Farad. Disc. 119, 101 (2001)
""",
)

entry(
    index = 320,
    label = "C5H12-2 <=> C4H9-2 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.16e+16, 's^-1'),
        n = 0,
        Ea = (330.916, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (803, 'K'),
        Tmax = (823, 'K'),
    ),
    reference = Article(
        authors = ["Blackmore, D.R.", "Hinshelwood, C."],
        title = u'Derivation of rate constants for steps in the free-radical chain decomposition of paraffins',
        journal = "Proc. R. Soc. London A",
        volume = "268",
        pages = """36""",
        year = "1962",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1962BLA/HIN36:5",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00010765
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010765/rk00000002.xml
""",
)

entry(
    index = 321,
    label = "C5H10-2 <=> C4H7 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+16, 's^-1', '*|/', 2.51),
        n = 0,
        Ea = (296.827, 'kJ/mol', '+|-', 2.968),
        T0 = (1, 'K'),
        Tmin = (671, 'K'),
        Tmax = (722, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Trenwith, A.B.", "Wrigley, S.P."],
        title = u'Dissociation of 2-Methylbut-1-ene and the Resonance Energy of the 2-Methyl allyl Radical',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "73",
        pages = """817""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977TRE/WRI817:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010916
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010916/rk00000002.xml
Uncertainty: 2.51
Bath gas: C2H5C(CH3)=CH2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 322,
    label = "C3H8O2 <=> OH + C3H7O-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.58e+15, 's^-1', '*|/', 2),
        n = 0,
        Ea = (167.121, 'kJ/mol', '+|-', 3.351),
        T0 = (1, 'K'),
        Tmin = (553, 'K'),
        Tmax = (653, 'K'),
    ),
    reference = Article(
        authors = ["Kirk, A.D.", "Knox, J.H."],
        title = u'The pyrolysis of alkyl hydroperoxides in the gas phase',
        journal = "Trans. Faraday Soc.",
        volume = "56",
        pages = """1296-1303""",
        year = "1960",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1960KIR/KNO1296-1303:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011657
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011657/rk00000001.xml
Uncertainty: 2.0
Bath gas: Benzene
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 323,
    label = "C4H8O-3 <=> C2H3O + C2H5",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.27e+14, 's^-1'),
        n = 0,
        Ea = (105.594, 'kJ/mol', '+|-', 17.959),
        T0 = (1, 'K'),
        Tmin = (291, 'K'),
        Tmax = (346, 'K'),
        Pmin = (53300, 'Pa'),
        Pmax = (53300, 'Pa'),
    ),
    reference = Article(
        authors = ["Abuin, E.", "Lissi, E.A."],
        title = u'Arrhenius Parameters for the Photocleavage of Butan-2-one Triplets',
        journal = "J. Photochem.",
        volume = "5",
        pages = """65""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975ABU/LIS65:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011751
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011751/rk00000002.xml
Bath gas: C3H8
Excitation technique: Thermal
Analytical technique: Chemiluminescence
""",
)

entry(
    index = 324,
    label = "C3H5O2 <=> O2 + C3H5",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.6e+10, 's^-1', '+|-', 8e+09),
        n = 0,
        Ea = (53.296, 'kJ/mol', '+|-', 1.596),
        T0 = (1, 'K'),
        Tmin = (382, 'K'),
        Tmax = (453, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (6666, 'Pa'),
    ),
    reference = Article(
        authors = ["Morgan, C.A.", "Pilling, M.J.", "Tulloch, J.M.", "Ruiz, R.P.", "Bayes, K.D."],
        title = u'Direct determination of the equilibrium constant and thermodynamic parameters for the reaction C3H5 + O2 = C3H5O2',
        journal = "J. Chem. Soc. Faraday Trans. 2",
        volume = "78",
        pages = """1323""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982MOR/PIL1323:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00012760
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012760/rk00000002.xml
Bath gas: Ar
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 325,
    label = "O2 + C2H5O-4 <=> C2H5O3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.44e+06, 'm^3/(mol*s)', '+|-', 450000),
        n = 0,
        Ea = (-0.382, 'kJ/mol', '+|-', 0.225),
        T0 = (1, 'K'),
        Tmin = (296, 'K'),
        Tmax = (473, 'K'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997SEH/SEH627-636:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00013961
Bath gas: SF6
Pressure dependence: Rate constant is high pressure limit
Excitation technique: Flash photolysis (laser or conventional)
Time resolution: In real time
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 326,
    label = "O2 + C2H5O-4 <=> C2H5O3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.87e+06, 'm^3/(mol*s)', '+|-', 600000),
        n = 0,
        Ea = (-2.711, 'kJ/mol', '+|-', 0.678),
        T0 = (1, 'K'),
        Tmin = (220, 'K'),
        Tmax = (355, 'K'),
        Pmin = (16000, 'Pa'),
        Pmax = (16000, 'Pa'),
    ),
    reference = Article(
        authors = ["Maricq, M.M.", "Szente, J.J.", "Hybl, J.D."],
        title = u'Kinetic studies of the oxidation of dimethyl ether and its chain reaction with Cl2',
        journal = "J. Phys. Chem. A",
        volume = "101",
        pages = """5155-5167""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997MAR/SZE5155-5167:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00013961
Excitation technique: Flash photolysis (laser or conventional)
Time resolution: In real time
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 327,
    label = "O2 + C2H5O-4 <=> C2H5O3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (339000, 'm^3/(mol*s)', '+|-', 91000),
        n = 0,
        Ea = (-7.109, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (302, 'K'),
        Tmax = (473, 'K'),
        Pmin = (99.99, 'Pa'),
        Pmax = (500, 'Pa'),
    ),
    reference = Article(
        authors = ["Hoyermann, K.", "Nacke, F."],
        title = u'Elementary reactions of the methoxymethyl radical in the gas phase: CH3OCH3 + F, CH2OCH3 + CH2OCH3, CH2OCH3 + O2 and CH2OCH3 + O',
        journal = "Symp. Int. Combust. Proc.",
        volume = "26",
        pages = """505-512""",
        year = "1996",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996HOY/NAC505-512:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00013961
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013961/rk00000002.xml
Bath gas: He
Excitation technique: Electron beam
Analytical technique: Mass spectrometry
Note: Invalid activation energy uncertainty (102.268) found and ignored
""",
)

entry(
    index = 328,
    label = "C5H10-3 <=> C4H7-2 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.94e+15, 's^-1', '*|/', 2),
        n = 0,
        Ea = (287.681, 'kJ/mol', '+|-', 2.877),
        T0 = (1, 'K'),
        Tmin = (685, 'K'),
        Tmax = (740, 'K'),
        Pmin = (2666, 'Pa'),
        Pmax = (46700, 'Pa'),
    ),
    reference = Article(
        authors = ["Trenwith, A.B."],
        title = u'Dissociation of 1-butene, 3-methyl-1-butene, and of 3,3-dimethyl-1-butene and the resonance energy of the allyl, methyl allyl and dimethyl allyl radicals',
        journal = "Trans. Faraday Soc.",
        volume = "66",
        pages = """2805-2811""",
        year = "1970",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1970TRE2805-2811:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00007566
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007566/rk00000001.xml
Uncertainty: 2.0
Bath gas: (CH3)2CHCH=CH2
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 329,
    label = "C5H8-3 <=> C4H5-5 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2e+16, 's^-1', '*|/', 2),
        n = 0,
        Ea = (315.118, 'kJ/mol', '+|-', 3.151),
        T0 = (1, 'K'),
        Tmin = (940, 'K'),
        Tmax = (1220, 'K'),
    ),
    reference = Article(
        authors = ["Nguyen, T.T.", "King, K.D."],
        title = u'Kinetics of Decomposition and Interconversion of 3-Methylbut-1-yne and 3-Methylbuta-1,2-diene. Resonance Stabilization Energies of Propargylic Radicals',
        journal = "J. Phys. Chem.",
        volume = "85",
        pages = """3130""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981NGU/KIN3130:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00008084
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008084/rk00000001.xml
Uncertainty: 2.0
Bath gas: CH2=C=C(CH3)2
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 330,
    label = "C4H10O2 <=> OH + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.5e+15, 's^-1', '*|/', 1.25),
        n = 0,
        Ea = (179.925, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (900, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (201000, 'Pa'),
        Pmax = (286000, 'Pa'),
    ),
    reference = Article(
        authors = ["Vasudevan, V.", "Davidson, D.F.", "Hanson, R.K."],
        title = u'Atoms Regeneration from Hydroperoxyl Radicals in the Reaction between Fluorine and Hydrogen Inhibited with Oxygen',
        journal = "Inter. J. Chem. Kinet.",
        volume = "37",
        pages = """98-109""",
        year = "2005",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2005VAS/DAV98-109:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00003751
Uncertainty: 1.25
Pressure dependence: None reported
Experimental procedure: Shock tube
Excitation technique: Thermal
Time resolution: In real time
Analytical technique: Vis-UV absorption

Rate constant was derived by fitting the early OH formation profiles.
""",
)

entry(
    index = 331,
    label = "C4H10O2 <=> OH + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+15, 's^-1', '*|/', 3.2),
        n = 0,
        Ea = (177.93, 'kJ/mol', '+|-', 3.559),
        T0 = (1, 'K'),
        Tmin = (443, 'K'),
        Tmax = (473, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Sahetchian, K.A.", "Rigny, R.", "Tardieu de Maleissye, J.", "Batt, L.", "Anwar Khan, M.", "Mathews, S."],
        title = u'The pyrolysis of organic hydroperoxides (ROOH)',
        journal = "Symp. Int. Combust. Proc.",
        volume = "24",
        pages = """637-643""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992SAH/RIG637-643:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00003751
Uncertainty: 3.2
Bath gas: iso-C4H10
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 332,
    label = "C4H10O2 <=> OH + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+15, 's^-1'),
        n = 0,
        Ea = (172.941, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (473, 'K'),
        Tmax = (573, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Mulder, P.", "Louw, R."],
        title = u'Gas-phase thermolysis of tert-butyl hydroperoxide in a nitrogen atmosphere. The effect of added toluene',
        journal = "Recl. Trav. Chim. Pays-Bas",
        volume = "103",
        pages = """148-152""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984MUL/LOU148-152:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00003751
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 333,
    label = "C4H10O2 <=> OH + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+15, 's^-1'),
        n = 0,
        Ea = (176.267, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (570, 'K'),
        Tmax = (973, 'K'),
    ),
    reference = Article(
        authors = ["Benson, S.W.", "Spokes, G.N."],
        title = u'Very low pressure pyrolysis. III. t-Butyl hydroperoxide in fused silica and stainless steel reactors',
        journal = "J. Phys. Chem.",
        volume = "72",
        pages = """1182-1186""",
        year = "1968",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1968BEN/SPO1182-1186:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00003751
Bath gas: tert-C4H9OOH
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 334,
    label = "C4H10O2 <=> OH + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+13, 's^-1', '*|/', 2),
        n = 0,
        Ea = (157.975, 'kJ/mol', '+|-', 3.159),
        T0 = (1, 'K'),
        Tmin = (574, 'K'),
        Tmax = (754, 'K'),
    ),
    reference = Article(
        authors = ["Kirk, A.D.", "Knox, J.H."],
        title = u'The pyrolysis of alkyl hydroperoxides in the gas phase',
        journal = "Trans. Faraday Soc.",
        volume = "56",
        pages = """1296-1303""",
        year = "1960",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1960KIR/KNO1296-1303:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00003751
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00003751/rk00000001.xml
Uncertainty: 2.0
Bath gas: Benzene
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 335,
    label = "C6H14 <=> C5H11 + CH3",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (3.98e+16, 's^-1'),
        n = 0,
        Ea = (348.376, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (753, 'K'),
        Tmax = (773, 'K'),
        Pmin = (13.33, 'Pa'),
        Pmax = (2000, 'Pa'),
    ),
    reference = Article(
        authors = ["Baldwin, R.R.", "Drewery, G.R.", "Walker, R.W."],
        title = u'Decomposition of 2,3-dimethylbutane in the presence of oxygen. Part 1.-Thermochemistry of the reaction (CH3)2CHCH(CH3)2 \u2192\x92 2i-C3H7',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "80",
        pages = """2827""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984BAL/DRE2827:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00004033
Bath gas: O2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 336,
    label = "C6H14 <=> C5H11 + CH3",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (3.98e+16, 's^-1'),
        n = 0,
        Ea = (339.23, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1200, 'K'),
        Pmin = (66700, 'Pa'),
        Pmax = (160000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Thermal decomposition of 2,3-dimethylbutane in a single-pulse shock tube',
        journal = "J. Chem. Phys.",
        volume = "43",
        pages = """352-359""",
        year = "1965",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1965TSA352-359:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00004033
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004033/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 337,
    label = "C6H12 <=> CH3 + C5H9",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+12, 's^-1', '*|/', 2),
        n = 0,
        Ea = (368.331, 'kJ/mol', '+|-', 11.058),
        T0 = (1, 'K'),
        Tmin = (1020, 'K'),
        Tmax = (1220, 'K'),
    ),
    reference = Article(
        authors = ["Brown, T.C.", "King, K.D."],
        title = u'Very low-pressure pyrolysis (VLPP) of methyl- and ethynyl- cyclopentanes and cyclohexanes',
        journal = "Int. J. Chem. Kinet.",
        volume = "21",
        pages = """251-266""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989BRO/KIN251-266:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00004262
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004262/rk00000001.xml
Uncertainty: 2.0
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 338,
    label = "C6H10 <=> C6H9 + H",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (5.01e+15, 's^-1'),
        n = 0,
        Ea = (341.725, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:18",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00005511
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00005511/rk00000001.xml
""",
)

entry(
    index = 339,
    label = "C2H3O + C2H3O <=> C4H6O2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.35e+06, 'm^3/(mol*s)', '+|-', 1.4e+06),
        n = 0,
        Ea = (-3.742, 'kJ/mol', '+|-', 1.014),
        T0 = (1, 'K'),
        Tmin = (214, 'K'),
        Tmax = (357, 'K'),
        Pmin = (13300, 'Pa'),
        Pmax = (13300, 'Pa'),
    ),
    reference = Article(
        authors = ["Maricq, M.M.", "Szente, J.J."],
        title = u'The UV spectrum of acetyl and the kinetics of the chain reaction between acetaldehyde and chlorine',
        journal = "Chem. Phys. Lett.",
        volume = "253",
        pages = """333-339""",
        year = "1996",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996MAR/SZE333-339:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00006863
Bath gas: N2
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 340,
    label = "C6H12-2 <=> C5H9-2 + CH3",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (7.94e+16, 's^-1', '*|/', 2),
        n = 0,
        Ea = (286.849, 'kJ/mol', '+|-', 2.868),
        T0 = (1, 'K'),
        Tmin = (657, 'K'),
        Tmax = (710, 'K'),
        Pmin = (5333, 'Pa'),
        Pmax = (46700, 'Pa'),
    ),
    reference = Article(
        authors = ["Trenwith, A.B."],
        title = u'Dissociation of 1-butene, 3-methyl-1-butene, and of 3,3-dimethyl-1-butene and the resonance energy of the allyl, methyl allyl and dimethyl allyl radicals',
        journal = "Trans. Faraday Soc.",
        volume = "66",
        pages = """2805-2811""",
        year = "1970",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1970TRE2805-2811:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00007547
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007547/rk00000001.xml
Uncertainty: 2.0
Bath gas: (CH3)3CCH=CH2
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 341,
    label = "C6H12-2 <=> C5H9-2 + CH3",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1.58e+16, 's^-1'),
        n = 0,
        Ea = (295.164, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976TSA173:7",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00007547
Bath gas: Ar
""",
)

entry(
    index = 342,
    label = "C6H12-3 <=> C5H9-3 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1e+16, 's^-1'),
        n = 0,
        Ea = (296.827, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976TSA173:8",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00007602
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007602/rk00000001.xml
Bath gas: Ar
""",
)

entry(
    index = 343,
    label = "C6H8 <=> C6H7 + H",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (5.01e+15, 's^-1'),
        n = 0,
        Ea = (303.478, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:24",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00007897
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007897/rk00000001.xml
""",
)

entry(
    index = 344,
    label = "C6H6 <=> C6H5 + H",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2e+15, 's^-1'),
        n = 0,
        Ea = (345.882, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:26",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00008426
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008426/rk00000001.xml
""",
)

entry(
    index = 345,
    label = "C4H10O2-2 <=> C2H5O-3 + C2H5O-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+16, 's^-1', '*|/', 10),
        n = 0,
        Ea = (156.312, 'kJ/mol', '+|-', 4.681),
        T0 = (1, 'K'),
        Tmin = (407, 'K'),
        Tmax = (441, 'K'),
        Pmin = (2666, 'Pa'),
        Pmax = (5333, 'Pa'),
    ),
    reference = Article(
        authors = ["Leggett, C.", "Thynne, J.C.J."],
        title = u'Thermal decomposition of dialkyl peroxides and heats of formation of the ethoxyl and isopropoxyl radicals',
        journal = "Trans. Faraday Soc.",
        volume = "63",
        pages = """2504-2509""",
        year = "1967",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1967LEG/THY2504-2509:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00008431
Uncertainty: 10.0
Bath gas: (C2H5O)2
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 346,
    label = "C4H10O2-2 <=> C2H5O-3 + C2H5O-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.1e+13, 's^-1'),
        n = 0,
        Ea = (133.032, 'kJ/mol', '+|-', 3.983),
        T0 = (1, 'K'),
        Tmin = (473, 'K'),
        Tmax = (518, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (1733, 'Pa'),
    ),
    reference = Article(
        authors = ["Rebbert, R.E.", "Laidler, K.J."],
        title = u'Kinetics of the decomposition of diethyl peroxide',
        journal = "J. Chem. Phys.",
        volume = "20",
        pages = """574-577""",
        year = "1952",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1952REB/LAI574-577:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00008431
Bath gas: Toluene
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 347,
    label = "C4H10O2-2 <=> C2H5O-3 + C2H5O-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.51e+12, 's^-1'),
        n = 0,
        Ea = (132.2, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (413, 'K'),
        Tmax = (458, 'K'),
        Pmin = (2666, 'Pa'),
        Pmax = (40000, 'Pa'),
    ),
    reference = Article(
        authors = ["Harris, E.J.", "Egerton, A.C."],
        title = u'The decomposition and ignition of peroxides. I. Diethylperoxide',
        journal = "Proc. R. Soc. London A",
        volume = "168",
        pages = """1-18""",
        year = "1938",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1938HAR/EGE1-18:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00008431
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008431/rk00000001.xml
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 348,
    label = "C6H10-2 <=> C3H3-2 + C3H7-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+15, 's^-1'),
        n = 0,
        Ea = (295.995, 'kJ/mol', '+|-', 8.896),
        T0 = (1, 'K'),
        Tmin = (903, 'K'),
        Tmax = (1150, 'K'),
    ),
    reference = Article(
        authors = ["King, K.D."],
        title = u'Kinetics of Competitive Pathways in the Thermal Unimolecular Decomposition of Hex-1-yne',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """273""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981KIN273:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00008770
Bath gas: C4H9CCH
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 349,
    label = "C6H10-2 <=> C3H3-2 + C3H7-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+15, 's^-1'),
        n = 0,
        Ea = (301.815, 'kJ/mol', '+|-', 3.018),
        T0 = (1, 'K'),
        Tmin = (990, 'K'),
        Tmax = (1200, 'K'),
        Pmin = (203000, 'Pa'),
        Pmax = (608000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Thermal Stability of Intermediate Sized Acetylenic Compounds and the Heats of Formation of Propargyl Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "10",
        pages = """687""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978TSA687:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00008770
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008770/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 350,
    label = "C6H10-3 <=> C5H7 + CH3",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (6.31e+15, 's^-1', '*|/', 2),
        n = 0,
        Ea = (295.995, 'kJ/mol', '+|-', 5.928),
        T0 = (1, 'K'),
        Tmin = (933, 'K'),
        Tmax = (1180, 'K'),
    ),
    reference = Article(
        authors = ["King, K.D."],
        title = u'Very Low-Pressure Pyrolysis (VLPP) of 3,3-Dimethylbut-1-yne (tert-Butyl Acetylene). The Heat of Formation and Stabilization Energy of the Dimethylpropargyl Radical',
        journal = "Int. J. Chem. Kinet.",
        volume = "9",
        pages = """907""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977KIN907:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009062
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009062/rk00000001.xml
Uncertainty: 2.0
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 351,
    label = "C6H14-2 <=> C4H9-3 + C2H5",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+16, 's^-1', '*|/', 1.26),
        n = 0,
        Ea = (320.107, 'kJ/mol', '+|-', 3.201),
        T0 = (1, 'K'),
        Tmin = (723, 'K'),
        Tmax = (985, 'K'),
        Pmin = (133000, 'Pa'),
        Pmax = (133000, 'Pa'),
    ),
    reference = Article(
        authors = ["Davidson, I.M.T.", "Barton, T.J.", "Hughes, K.J.", "Ijadi-Maghsoodi, S.", "Revis, A.", "Paul, G.C."],
        title = u'Kinetics of radical-forming homolyses in alkenyl- and tert-butyisilanes. The stability of \u03b1- and \u03b2-silicon-substituted alkyl radicals',
        journal = "Organometallics",
        volume = "6",
        pages = """644""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987DAV/BAR644:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009789
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009789/rk00000002.xml
Uncertainty: 1.26
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 352,
    label = "C4H9-3 + C2H5 <=> C6H14-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.68e+09, 'm^3/(mol*s)'),
        n = -0.89,
        Ea = (-0.608, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Klippenstein, S.J.", "Georgievskii, Y.", "Harding, L.B."],
        title = u'Predictive theory for the combination kinetics of two alkyl radicals',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "8",
        pages = """1133-1147""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006KLI/GEO1133-1147:7",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00009789
Pressure dependence: Rate constant is high pressure limit

Rate constants were calculated with an ab initio transition state theory employing direct evaluations of the orientation dependent interaction energies at the CASPT2/cc-pvdz level within variable reaction
coordinate transition state theory (VRC-TST). Results were compared with experiment for a series of alkyl radicals and good quantitative agreement was found.

Each methyl substituent adjacent to a radical site was found to reduce the rate coefficient by about a factor of two. Rate constants are predicted to decrease substantially with increasing temperature, with the more sterically hindered reactants having a more rapid decrease. The geometric mean rule was found to be in good agreement with the detailed calculations.

The authors state the rate parameters are strictly applicable between 200-2000 K but that they should provide reasonable predictions up to about 2700 K.
""",
)

entry(
    index = 353,
    label = "C4H9-3 + O2 <=> C4H9O2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.09e+06, 'm^3/(mol*s)', '+|-', 1.1e+06),
        n = 0,
        Ea = (-2.395, 'kJ/mol', '+|-', 0.694),
        T0 = (1, 'K'),
        Tmin = (241, 'K'),
        Tmax = (462, 'K'),
        Pmin = (152000, 'Pa'),
        Pmax = (152000, 'Pa'),
    ),
    reference = Article(
        authors = ["Dilger, H.", "Stolmar, M.", "Tregenna-Piggott, P.L.W.", "Roduner, E."],
        title = u'Gas phase addition kinetics of the tert-butyl radical to oxygen',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "101",
        pages = """956-960""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997DIL/STO956-960:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009827
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009827/rk00000004.xml
Bath gas: N2
Excitation technique: Thermal
Time resolution: In real time
Analytical technique: Other (direct)
""",
)

entry(
    index = 354,
    label = "C4H9O2 <=> C4H9-3 + O2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.83e+15, 's^-1'),
        n = 0,
        Ea = (140.164, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1999CHE/BOZ9731-9769:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00009827
Pressure dependence: Rate constant is high pressure limit
""",
)

entry(
    index = 355,
    label = "C3H5 + C3H5 <=> C6H10-4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+07, 'm^3/(mol*s)', '*|/', 2),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:79",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010093
Uncertainty: 2.0
""",
)

entry(
    index = 356,
    label = "C3H5 + C3H5 <=> C6H10-4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+07, 'm^3/(mol*s)', '+|-', 200000),
        n = 0,
        Ea = (-1.098, 'kJ/mol', '+|-', 0.09894),
        T0 = (1, 'K'),
        Tmin = (293, 'K'),
        Tmax = (571, 'K'),
        Pmin = (7066, 'Pa'),
        Pmax = (7066, 'Pa'),
    ),
    reference = Article(
        authors = ["Tulloch, J.M.", "Macpherson, M.T.", "Morgan, C.A.", "Pilling, M.J."],
        title = u'Flash Photolysis Studies of Free-Radical Reactions: C3H5 + C3H5 (293-691 K) and C3H5 + NO (295-400 K)',
        journal = "J. Phys. Chem.",
        volume = "86",
        pages = """3812-3819""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982TUL/MAC3812-3819:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010093
Bath gas: Ar
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Gas chromatography
""",
)

entry(
    index = 357,
    label = "C3H5 + C3H5 <=> C6H10-4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (460000, 'm^3/(mol*s)'),
        n = 0,
        Ea = (-21.119, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (913, 'K'),
        Tmax = (1060, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Golden, D.M.", "Gac, N.A.", "Benson, S.W."],
        title = u'Equilibrium constant for allyl radical recombination. Direct measurement of "allyl resonance energy"',
        journal = "J. Am. Chem. Soc.",
        pages = """2136""",
        year = "1969",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1969GOL/GAC2136:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010093
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010093/rk00000002.xml
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 358,
    label = "C6H10-4 <=> C3H5 + C3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e+13, 's^-1', '*|/', 2.51),
        n = 0,
        Ea = (101.437, 'kJ/mol', '+|-', 3.051),
        T0 = (1, 'K'),
        Tmin = (850, 'K'),
        Tmax = (950, 'K'),
    ),
    reference = Article(
        authors = ["Throssell, J.J."],
        title = u'Rates of reaction of allyl radicals: A reassessment',
        journal = "Int. J. Chem. Kinet.",
        volume = "4",
        pages = """273""",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972THR273:2",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00010093
Uncertainty: 2.51
Bath gas: CH2=C=CHCH(CH3)CCH
""",
)

entry(
    index = 359,
    label = "C6H10-4 <=> C3H5 + C3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.17e+14, 's^-1', '+|-', 2.1e+14),
        n = 0,
        Ea = (241.12, 'kJ/mol', '+|-', 2.411),
        T0 = (1, 'K'),
        Tmin = (681, 'K'),
        Tmax = (794, 'K'),
    ),
    reference = Article(
        authors = ["Roth, W.R.", "Bauer, F.", "Beitat, A.", "Ebbrecht, T.", "Wustefeld, M."],
        title = u'Die bildungsenthalpie des allyl- und methallyl-radikals',
        journal = "Chem. Ber.",
        volume = "124",
        pages = """1453-1460""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991ROT/BAU1453-1460:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010093
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 360,
    label = "C6H10-4 <=> C3H5 + C3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+15, 's^-1'),
        n = 0,
        Ea = (237.794, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:23",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010093
""",
)

entry(
    index = 361,
    label = "C6H10-4 <=> C3H5 + C3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+12, 's^-1'),
        n = 0,
        Ea = (230.311, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (773, 'K'),
        Tmax = (893, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Sakai, T.", "Nohara, D.", "Kunugi, T.", "Nohara, D."],
        title = u'A Kinetic Study on the Formation of Aromatics During Pyrolysis of Petroleum Hydrocarbons',
        journal = "Am. Chem. Soc. Symp. Ser.",
        volume = "22",
        pages = """152""",
        year = "1976",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976SAK/NOH152:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010093
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 362,
    label = "C6H10-4 <=> C3H5 + C3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.07e+12, 's^-1', '*|/', 1.82),
        n = 0,
        Ea = (213.682, 'kJ/mol', '+|-', 4.265),
        T0 = (1, 'K'),
        Tmin = (660, 'K'),
        Tmax = (710, 'K'),
    ),
    reference = Article(
        authors = ["Doering, W.v.E.", "Toscano, V.G.", "Beasley, G.H."],
        title = u'Kinetics of the Cope Rearrangement of 1,1-Dideuteriohexa-1,5-Diene',
        journal = "Tetrahedron",
        volume = "27",
        pages = """5299""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971DOE/TOS5299:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010093
Uncertainty: 1.8200001
Bath gas: He
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 363,
    label = "C6H10-4 <=> C3H5 + C3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.67e+15, 's^-1'),
        n = 0,
        Ea = (261.074, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (913, 'K'),
        Tmax = (1060, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Golden, D.M.", "Gac, N.A.", "Benson, S.W."],
        title = u'Equilibrium constant for allyl radical recombination. Direct measurement of "allyl resonance energy"',
        journal = "J. Am. Chem. Soc.",
        pages = """2136""",
        year = "1969",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1969GOL/GAC2136:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010093
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010093/rk00000002.xml
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 364,
    label = "C6H10-4 <=> C3H5 + C3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e+13, 's^-1'),
        n = 0,
        Ea = (234.468, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (866, 'K'),
        Tmax = (959, 'K'),
        Pmin = (1560, 'Pa'),
        Pmax = (2426, 'Pa'),
    ),
    reference = Article(
        authors = ["Akers, R.J.", "Throssell, J.J."],
        title = u'Kinetic studies on allyl radicals. Part 1.-Toluene-carrier pyrolysis of 4-phenyl-but-l-ene and hexa-1, 5-diene and the heat of formation of the allyl radical',
        journal = "Trans. Faraday Soc.",
        volume = "63",
        pages = """124""",
        year = "1967",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1967AKE/THR124:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010093
Bath gas: CH2=CHCH2CH2CH=CH2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 365,
    label = "C6H10-4 <=> C3H5 + C3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.01e+13, 's^-1'),
        n = 0,
        Ea = (184.581, 'kJ/mol', '+|-', 5.537),
        T0 = (1, 'K'),
        Tmin = (977, 'K'),
        Tmax = (1070, 'K'),
        Pmin = (933, 'Pa'),
        Pmax = (6799, 'Pa'),
    ),
    reference = Article(
        authors = ["Homer, J.B.", "Lossing, F.P."],
        title = u'Free radicals by mass spectrometry. XXXV. The heat of formation of allyl radical from biallyl pyrolysis',
        journal = "Can. J. Chem.",
        volume = "44",
        pages = """2211-2217""",
        year = "1966",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1966HOM/LOS2211-2217:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010093
Bath gas: He
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 366,
    label = "C6H10-4 <=> C3H5 + C3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+07, 's^-1'),
        n = 0,
        Ea = (131.369, 'kJ/mol', '+|-', 3.933),
        T0 = (1, 'K'),
        Tmin = (733, 'K'),
        Tmax = (794, 'K'),
        Pmin = (9333, 'Pa'),
        Pmax = (9333, 'Pa'),
    ),
    reference = Article(
        authors = ["Ruzicka, D.J.", "Bryce, W.A."],
        title = u'The pyrolysis of diallyl (1,5-hexadiene)',
        journal = "Can. J. Chem.",
        volume = "38",
        pages = """827-834""",
        year = "1960",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1960RUZ/BRY827-834:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010093
Bath gas: CH2=CHCH2CH2CH=CH2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 367,
    label = "C3H5 + C3H7 <=> C6H12-4",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.15e+08, 'm^3/(mol*s)', '*|/', 1.5),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:82",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010096
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010096/rk00000001.xml
Uncertainty: 1.5
""",
)

entry(
    index = 368,
    label = "C6H12-4 <=> C3H5 + C3H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5e+09, 's^-1'),
        n = 0,
        Ea = (184.581, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (743, 'K'),
        Tmax = (803, 'K'),
        Pmin = (3333, 'Pa'),
        Pmax = (26700, 'Pa'),
    ),
    reference = Article(
        authors = ["Taniewski, M."],
        title = u'Kinetics and mechanism of the thermal decomposition of 4-methylpent-1-ene',
        journal = "J. Chem. Soc.",
        pages = """7436""",
        year = "1965",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1965TAN7436:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010096
Bath gas: (CH3)2CHCH2CH=CH2
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 369,
    label = "C3H5 + C3H7-2 <=> C6H12-5",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.05e+07, 'm^3/(mol*s)', '*|/', 2),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:89",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010107
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010107/rk00000001.xml
Uncertainty: 2.0
""",
)

entry(
    index = 370,
    label = "C6H12-5 <=> C3H5 + C3H7-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+15, 's^-1', '*|/', 1.58),
        n = 0,
        Ea = (295.995, 'kJ/mol', '+|-', 2.96),
        T0 = (1, 'K'),
        Tmin = (915, 'K'),
        Tmax = (1150, 'K'),
    ),
    reference = Article(
        authors = ["King, K.D."],
        title = u'Very Low-Pressure Pyrolysis (VLPP) of Hex-1-ene. Kinetics of the Retro-ene Decomposition of a Mono-Olefin',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """1071""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979KIN1071:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010107
Uncertainty: 1.58
Bath gas: 1-C6H12
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 371,
    label = "C6H12-5 <=> C3H5 + C3H7-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+15, 's^-1'),
        n = 0,
        Ea = (295.995, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (990, 'K'),
        Tmax = (1100, 'K'),
        Pmin = (183000, 'Pa'),
        Pmax = (183000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Thermal Stability of Cyclohexane and 1-Hexene',
        journal = "Int. J. Chem. Kinet.",
        volume = "10",
        pages = """1119""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978TSA1119:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010107
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 372,
    label = "C6H12-5 <=> C3H5 + C3H7-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.8e+15, 's^-1'),
        n = 0,
        Ea = (75.05, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (1400, 'K'),
        Tmax = (1400, 'K'),
    ),
    reference = Article(
        authors = ["Yahyaoui, M.", "Djebaili-Chaumeix, N.", "Paillard, C.E.", "Touchard, S.", "Fournet, R.", "Glaude, P.A.", "Battin-Leclerc, F."],
        title = u'Experimental and modeling study of 1-hexene oxidation behind reflected shock waves',
        journal = "Proc. Combust. Inst.",
        volume = "30",
        pages = """1137-1145""",
        year = "2005",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2005YAH/DJE1137-1145:0",
    ),
    longDesc = 
u"""
PrIMe Reaction: r00010107
""",
)

entry(
    index = 373,
    label = "C3H7 + C3H7 <=> C6H14-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.43e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (1.339, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978ARR/KIR3016:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010169
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010169/rk00000009.xml
Bath gas: N2
Excitation technique: Direct photolysis
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 374,
    label = "C3H7 + C3H7 <=> C6H14-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.9e+08, 'm^3/(mol*s)'),
        n = -0.86,
        Ea = (-1.098, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Klippenstein, S.J.", "Georgievskii, Y.", "Harding, L.B."],
        title = u'Predictive theory for the combination kinetics of two alkyl radicals',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "8",
        pages = """1133-1147""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006KLI/GEO1133-1147:8",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00010169
Pressure dependence: Rate constant is high pressure limit

Rate constants were calculated with an ab initio transition state theory employing direct evaluations of the orientation dependent interaction energies at the CASPT2/cc-pvdz level within variable reaction
coordinate transition state theory (VRC-TST). Results were compared with experiment for a series of alkyl radicals and good quantitative agreement was found.

Each methyl substituent adjacent to a radical site was found to reduce the rate coefficient by about a factor of two. Rate constants are predicted to decrease substantially with increasing temperature, with the more sterically hindered reactants having a more rapid decrease. The geometric mean rule was found to be in good agreement with the detailed calculations.

The authors state the rate parameters are strictly applicable between 200-2000 K but that they should provide reasonable predictions up to about 2700 K.
""",
)

entry(
    index = 375,
    label = "C6H14-3 <=> C3H7 + C3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.63e+16, 's^-1'),
        n = 0,
        Ea = (319.276, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (760, 'K'),
        Tmax = (1200, 'K'),
        Pmin = (13.33, 'Pa'),
        Pmax = (2000, 'Pa'),
    ),
    reference = Article(
        authors = ["Baldwin, R.R.", "Drewery, G.R.", "Walker, R.W."],
        title = u'Decomposition of 2,3-dimethylbutane in the presence of oxygen. Part 1.-Thermochemistry of the reaction (CH3)2CHCH(CH3)2 \u2192\x92 2i-C3H7',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "80",
        pages = """2827""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984BAL/DRE2827:2",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00010169
""",
)

entry(
    index = 376,
    label = "C6H14-3 <=> C3H7 + C3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.82e+17, 's^-1'),
        n = 0,
        Ea = (339.23, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1100, 'K'),
        Pmin = (66700, 'Pa'),
        Pmax = (160000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Evidence for Strongly Temperature-Dependent A Factors in Alkane Decomposition and High Heats of Formation for Alkyl Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "10",
        pages = """821""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978TSA821:2",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00010169
Bath gas: Ar
""",
)

entry(
    index = 377,
    label = "C6H14-3 <=> C3H7 + C3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.16e+15, 's^-1', '*|/', 1.26),
        n = 0,
        Ea = (305.141, 'kJ/mol', '+|-', 15.215),
        T0 = (1, 'K'),
        Tmin = (753, 'K'),
        Tmax = (813, 'K'),
        Pmin = (13.33, 'Pa'),
        Pmax = (2000, 'Pa'),
    ),
    reference = Article(
        authors = ["Baldwin, R.R.", "Drewery, G.R.", "Walker, R.W."],
        title = u'Decomposition of 2,3-dimethylbutane in the presence of oxygen. Part 1.-Thermochemistry of the reaction (CH3)2CHCH(CH3)2 \u2192\x92 2i-C3H7',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "80",
        pages = """2827""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984BAL/DRE2827:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010169
Uncertainty: 1.26
Bath gas: O2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 378,
    label = "C6H14-3 <=> C3H7 + C3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+16, 's^-1'),
        n = 0,
        Ea = (316.781, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1200, 'K'),
        Pmin = (66700, 'Pa'),
        Pmax = (160000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Evidence for Strongly Temperature-Dependent A Factors in Alkane Decomposition and High Heats of Formation for Alkyl Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "10",
        pages = """821""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978TSA821:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010169
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 379,
    label = "C6H14-3 <=> C3H7 + C3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e+16, 's^-1'),
        n = 0,
        Ea = (311.793, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (990, 'K'),
        Tmax = (1250, 'K'),
    ),
    reference = Article(
        authors = ["Golden, D.M.", "Alfassi, Z.B.", "Beadle, P.C."],
        title = u"Very Low-Pressure Pyrolysis (VLPP) of Alkanes: n-Butane, 2,3-Dimethylbutane, 2,2',3,3'-Tetramethylbutane, and Isobutane",
        journal = "Int. J. Chem. Kinet.",
        volume = "6",
        pages = """359""",
        year = "1974",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1974GOL/ALF359:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00010169
Bath gas: (CH3)2CHCH(CH3)2
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 380,
    label = "C6H14-3 <=> C3H7 + C3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.26e+16, 's^-1'),
        n = 0,
        Ea = (317.613, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1200, 'K'),
        Pmin = (66700, 'Pa'),
        Pmax = (160000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Thermal decomposition of 2,3-dimethylbutane in a single-pulse shock tube',
        journal = "J. Chem. Phys.",
        volume = "43",
        pages = """352-359""",
        year = "1965",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1965TSA352-359:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010169
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 381,
    label = "C6H14-3 <=> C3H7 + C3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.76e+30, 's^-1'),
        n = -4.1,
        Ea = (354.197, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1200, 'K'),
    ),
    reference = Article(
        authors = ["Forst, W."],
        title = u'Temperature-dependent A factor in thermal unimolecular reactions',
        journal = "J. Phys. Chem.",
        volume = "83",
        pages = """100-108""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979FOR100-108:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00010169
""",
)

entry(
    index = 382,
    label = "C6H6-2 <=> C6H5-2 + H",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (2e+17, 's^-1'),
        n = 0,
        Ea = (493.88, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1810, 'K'),
        Tmax = (2450, 'K'),
        Pmin = (20000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Kiefer, J.H.", "Mizerka, L.J.", "Patel, M.R.", "Wei, H.-C."],
        title = u'A shock tube investigation of major pathways in the high-temperature pyrolysis of benzene',
        journal = "J. Phys. Chem.",
        volume = "89",
        pages = """2013-2019""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985KIE/MIZ2013-2019:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011174
Bath gas: Kr
Excitation technique: Thermal
Analytical technique: Laser schlieren
""",
)

entry(
    index = 383,
    label = "C6H6-2 <=> C6H5-2 + H",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (4.57e+13, 's^-1'),
        n = 0,
        Ea = (372.488, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1520, 'K'),
        Tmax = (2500, 'K'),
        Pmin = (20300, 'Pa'),
        Pmax = (304000, 'Pa'),
    ),
    reference = Article(
        authors = ["Kern, R.D.", "Wu, C.H.", "Skinner, G.B.", "Rao, V.S.", "Kiefer, J.H.", "Towers, J.A.", "Mizerka, L.J."],
        title = u'Collaborative shock tube studies of benzene pyrolysis',
        journal = "Symp. Int. Combust. Proc.",
        volume = "20",
        pages = """89""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985KER/WU789:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011174
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 384,
    label = "C6H6-2 <=> C6H5-2 + H",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (5.75e+16, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (484.734, 'kJ/mol', '+|-', 19.373),
        T0 = (1, 'K'),
        Tmin = (1600, 'K'),
        Tmax = (2300, 'K'),
        Pmin = (192000, 'Pa'),
        Pmax = (273000, 'Pa'),
    ),
    reference = Article(
        authors = ["Hsu, D.S.Y.", "Lin, C.Y.", "Lin, M.C."],
        title = u'CO formation in early stage high temperature benzene oxidation under fuel lean conditions: Kinetics of the initiation reaction, C6H6 \u2192\x92 C6H5 \u2192\x92 H',
        journal = "Symp. Int. Combust. Proc.",
        volume = "20",
        pages = """623""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985HSU/LIN623:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011174
Uncertainty: 3.1600001
Bath gas: Ar
""",
)

entry(
    index = 385,
    label = "C6H6-2 <=> C6H5-2 + H",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (5.01e+15, 's^-1', '*|/', 3.31),
        n = 0,
        Ea = (451.476, 'kJ/mol', '+|-', 18.042),
        T0 = (1, 'K'),
        Tmin = (1600, 'K'),
        Tmax = (2300, 'K'),
        Pmin = (192000, 'Pa'),
        Pmax = (273000, 'Pa'),
    ),
    reference = Article(
        authors = ["Hsu, D.S.Y.", "Lin, C.Y.", "Lin, M.C."],
        title = u'CO formation in early stage high temperature benzene oxidation under fuel lean conditions: Kinetics of the initiation reaction, C6H6 \u2192\x92 C6H5 \u2192\x92 H',
        journal = "Symp. Int. Combust. Proc.",
        volume = "20",
        pages = """623""",
        year = "1985",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985HSU/LIN623:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011174
Uncertainty: 3.3099999
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 386,
    label = "C6H6-2 <=> C6H5-2 + H",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (2e+17, 's^-1'),
        n = 0,
        Ea = (460.24, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1200, 'K'),
        Tmax = (1800, 'K'),
    ),
    reference = Article(
        authors = ["Sivaramakrishnan, R.", "Brezinsky, K.", "Vasudevan, H.", "Tranter, R.S."],
        title = u'A shock-tube study of the high-pressure thermal decomposition of benzene',
        journal = "Combust. Sci. Technol.",
        volume = "178",
        pages = """285-305""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006SIV/BRE285-305:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011174
""",
)

entry(
    index = 387,
    label = "C6H6-2 <=> C6H5-2 + H",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (9.29e+14, 's^-1'),
        n = 0,
        Ea = (443.161, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1500, 'K'),
        Tmax = (1900, 'K'),
        Pmin = (40500, 'Pa'),
        Pmax = (40500, 'Pa'),
    ),
    reference = Article(
        authors = ["Rao, V.S.", "Skinner, G.B."],
        title = u'Formation of H and D atoms in pyrolysis of benzene-d6, chlorobenzene, bromobenzene, and iodobenzene behind shock waves',
        journal = "J. Phys. Chem.",
        volume = "92",
        pages = """2442""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988RAO/SKI2442:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011174
Bath gas: Ar
""",
)

entry(
    index = 388,
    label = "C6H6-2 <=> C6H5-2 + H",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (7.08e+14, 's^-1'),
        n = 0,
        Ea = (443.161, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1200, 'K'),
        Tmax = (1700, 'K'),
        Pmin = (203000, 'Pa'),
        Pmax = (811000, 'Pa'),
    ),
    reference = Article(
        authors = ["Asaba, T.", "Fujii, N."],
        title = u'High temperature oxidation of benzene',
        journal = "Proc. Int. Symp. Shock Tubes Waves",
        volume = "8",
        pages = """1-12""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971ASA/FUJ1-12:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011174
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011174/rk00000006.xml
Bath gas: Ar
""",
)

entry(
    index = 389,
    label = "C6H6-3 <=> C3H3-2 + C3H3-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+14, 's^-1'),
        n = 0,
        Ea = (258.58, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:25",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011580
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011580/rk00000002.xml
""",
)

entry(
    index = 390,
    label = "C3H6O3 <=> OH + C3H5O2-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+15, 's^-1', '*|/', 10),
        n = 0,
        Ea = (167.952, 'kJ/mol', '+|-', 6.718),
        T0 = (1, 'K'),
        Tmin = (533, 'K'),
        Tmax = (573, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Sahetchian, K.A.", "Rigny, R.", "Tardieu de Maleissye, J.", "Batt, L.", "Anwar Khan, M.", "Mathews, S."],
        title = u'The pyrolysis of organic hydroperoxides (ROOH)',
        journal = "Symp. Int. Combust. Proc.",
        volume = "24",
        pages = """637-643""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992SAH/RIG637-643:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00012661
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012661/rk00000001.xml
Uncertainty: 10.0
Bath gas: H2
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 391,
    label = "C6H10-5 <=> C3H3-2 + C3H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.63e+15, 's^-1'),
        n = 0,
        Ea = (290.175, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1160, 'K'),
        Pmin = (55300, 'Pa'),
        Pmax = (169000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Rate and mechanism of thermal decomposition of 4-methyl-1-pentyne in a single-pulse shock tube',
        journal = "Int. J. Chem. Kinet.",
        volume = "2",
        pages = """23""",
        year = "1970",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1970TSA23:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00013061
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013061/rk00000001.xml
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 392,
    label = "C6H8-2 <=> C5H5-2 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+16, 's^-1', '*|/', 2),
        n = 0,
        Ea = (300.152, 'kJ/mol', '+|-', 12.056),
        T0 = (1, 'K'),
        Tmin = (949, 'K'),
        Tmax = (1230, 'K'),
    ),
    reference = Article(
        authors = ["Staker, W.S.", "King, K.D.", "Nguyen, T.T."],
        title = u'Kinetics of the thermal unimolecular decomposition of hex-1-ene-3-yne. Heat of formation and resonance stabilization energy of the 3-ethenylpropargyl radical',
        journal = "Int. J. Chem. Kinet.",
        volume = "24",
        pages = """781-790""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992STA/KIN781-790:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015258
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015258/rk00000001.xml
Uncertainty: 2.0
Bath gas: C2H5CCCH=CH2
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 393,
    label = "C6H8-3 <=> C3H3-2 + C3H5",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+15, 's^-1'),
        n = 0,
        Ea = (248.603, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1985DEA4600-4608:39",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00015452
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015452/rk00000001.xml
""",
)

entry(
    index = 394,
    label = "C2H5O-4 + C2H5O-4 <=> C4H10O2-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+07, 'm^3/(mol*s)', '+|-', 3.6e+06),
        n = 0,
        Ea = (-1.663, 'kJ/mol', '+|-', 0.831),
        T0 = (1, 'K'),
        Tmin = (220, 'K'),
        Tmax = (357, 'K'),
        Pmin = (3333, 'Pa'),
        Pmax = (60100, 'Pa'),
    ),
    reference = Article(
        authors = ["Maricq, M.M.", "Szente, J.J.", "Hybl, J.D."],
        title = u'Kinetic studies of the oxidation of dimethyl ether and its chain reaction with Cl2',
        journal = "J. Phys. Chem. A",
        volume = "101",
        pages = """5155-5167""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997MAR/SZE5155-5167:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015717
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015717/rk00000002.xml
Bath gas: N2
Excitation technique: Flash photolysis (laser or conventional)
Time resolution: In real time
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 395,
    label = "C4H10O2-3 <=> C2H5O-4 + C2H5O-4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+15, 's^-1'),
        n = 0,
        Ea = (298.49, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (738, 'K'),
        Tmax = (783, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (2666, 'Pa'),
    ),
    reference = Article(
        authors = ["Loucks, L.F.", "Laidler, K.J."],
        title = u'Thermochemistry of the methoxymethyl radical',
        journal = "Can. J. Chem.",
        volume = "45",
        pages = """2785-2793""",
        year = "1967",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1967LOU/LAI2785-2793:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015717
Bath gas: CH3OCH2CH2OCH3
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 396,
    label = "C6H10-6 <=> C5H7-2 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.58e+16, 's^-1', '*|/', 2),
        n = 0,
        Ea = (310.961, 'kJ/mol', '+|-', 6.228),
        T0 = (1, 'K'),
        Tmin = (903, 'K'),
        Tmax = (1250, 'K'),
    ),
    reference = Article(
        authors = ["King, K.D.", "Nguyen, T.T."],
        title = u'Very Low-Pressure Pyrolysis (VLPP) of Pentynes. II. 4-Methylpent-2-yne and 4,4-Dimethyl-pent-2-yne. Heats of Formation and Resonance Stabilization Energies of Methyl-Substituted Propargyl Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """255""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981KIN/NGU255:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016015
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016015/rk00000001.xml
Uncertainty: 2.0
Bath gas: (CH3)2CHCCCH3
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 397,
    label = "C4H6O2 <=> C2H3O + C2H3O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+10, 's^-1'),
        n = 0,
        Ea = (281.029, 'kJ/mol', '+|-', 14.051),
        T0 = (1, 'K'),
        Tmin = (677, 'K'),
        Tmax = (776, 'K'),
        Pmin = (79.99, 'Pa'),
        Pmax = (5999, 'Pa'),
    ),
    reference = Article(
        authors = ["Hole, K.J.", "Mulcahy, M.F.R."],
        title = u'The pyrolysis of biacetyl and the third-body effect on the combination of methyl radicals',
        journal = "J. Phys. Chem.",
        volume = "73",
        pages = """177""",
        year = "1969",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1969HOL/MUL177:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00006863
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00006863/rk00000001.xml
Bath gas: (CH3CO)2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 398,
    label = "C4H6O2 <=> C2H3O + C2H3O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+16, 's^-1', '*|/', 5),
        n = 0,
        Ea = (283.523, 'kJ/mol', '+|-', 16.962),
        T0 = (1, 'K'),
        Tmin = (240, 'K'),
        Tmax = (550, 'K'),
        Pmin = (4133, 'Pa'),
        Pmax = (24400, 'Pa'),
    ),
    reference = Article(
        authors = ["Knoll, H.", "Scherzer, K.", "Geiseler, G."],
        title = u'The Thermal Decomposition of Biacetyl',
        journal = "Int. J. Chem. Kinet.",
        volume = "5",
        pages = """271""",
        year = "1973",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1973KNO/SCH271:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00006863
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00006863/rk00000003.xml
Uncertainty: 5.0
Bath gas: (CH3CO)2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 399,
    label = "C4H6O2 <=> C2H3O + C2H3O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+15, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (279.366, 'kJ/mol', '+|-', 8.398),
        T0 = (1, 'K'),
        Tmin = (822, 'K'),
        Tmax = (905, 'K'),
        Pmin = (79.99, 'Pa'),
        Pmax = (57300, 'Pa'),
    ),
    reference = Article(
        authors = ["Scherzer, K.", "Plarre, D."],
        title = u'Der Thermische Zerfall von Diacetyl. II. Mitteilung: Untersuchungen bei hohen Temperaturen',
        journal = "Z. Phys. Chem. (Leipzig)",
        volume = "256",
        pages = """660""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975SCH/PLA660:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00006863
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00006863/rk00000004.xml
Uncertainty: 3.1600001
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 400,
    label = "C6H10-7 <=> C5H7-3 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.32e+15, 's^-1', '*|/', 1.48),
        n = 0,
        Ea = (277.703, 'kJ/mol', '+|-', 2.777),
        T0 = (1, 'K'),
        Tmin = (694, 'K'),
        Tmax = (759, 'K'),
        Pmin = (3333, 'Pa'),
        Pmax = (26700, 'Pa'),
    ),
    reference = Article(
        authors = ["Trenwith, A.B."],
        title = u'Dissociation of 1,3-Hexadiene and the Resonance Energy of the Pentadienyl Radical',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "76",
        pages = """266""",
        year = "1980",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1980TRE266:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00007893
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007893/rk00000001.xml
Uncertainty: 1.48
Bath gas: C2H5CH=CHCH=CH2
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 401,
    label = "C6H10-8 <=> C5H7-4 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.29e+15, 's^-1', '*|/', 1.26),
        n = 0,
        Ea = (271.883, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (653, 'K'),
        Tmax = (716, 'K'),
        Pmin = (2000, 'Pa'),
        Pmax = (26700, 'Pa'),
    ),
    reference = Article(
        authors = ["Trenwith, A.B."],
        title = u'Dissociation of 3-Methylpenta-1,4-diene and the Resonance Energy of the Pentadienyl Radical',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "78",
        pages = """3131""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982TRE3131:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009347
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009347/rk00000001.xml
Uncertainty: 1.26
Bath gas: CH2=CHCH(CH3)CH=CH2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 402,
    label = "C2H3 + C4H5 <=> C6H8-4",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.5e+07, 'm^3/(mol*s)'),
        n = -0.08,
        Ea = (0.416, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989WES/DEA8171-8180:20",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011454
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011454/rk00000001.xml
Bath gas: N2
""",
)

entry(
    index = 403,
    label = "C5H8O2 <=> C3H5O-3 + C2H3O",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.12e+17, 's^-1', '*|/', 1.91),
        n = 0,
        Ea = (311.793, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1120, 'K'),
        Tmax = (1660, 'K'),
        Pmin = (51700, 'Pa'),
        Pmax = (72900, 'Pa'),
    ),
    reference = Article(
        authors = ["Choudhury, T.K.", "Lin, M.C."],
        title = u'Homogeneous pyrolysis of acetylacetone at high temperatures in shock waves',
        journal = "Int. J. Chem. Kinet.",
        volume = "20",
        pages = """491-504""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990CHO/LIN491-504:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00006092
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00006092/rk00000001.xml
Uncertainty: 1.91
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
Note: Invalid activation energy uncertainty (8314.472) found and ignored
""",
)

entry(
    index = 404,
    label = "C5H12O2 <=> C3H7O2-3 + C2H5",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.09e+16, 's^-1', '*|/', 2.82),
        n = 0,
        Ea = (317.613, 'kJ/mol', '+|-', 9.562),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997HER/MAN5494-5499:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00006950
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00006950/rk00000001.xml
Uncertainty: 2.8199999
Bath gas: CH2(OC2H5)2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 405,
    label = "C7H16 <=> C4H9-3 + C3H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.88e+16, 's^-1', '*|/', 1.32),
        n = 0,
        Ea = (305.141, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (753, 'K'),
        Tmax = (1200, 'K'),
        Pmin = (7999, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Baldwin, R.R.", "Walker, R.W.", "Walker, R.W."],
        title = u'Decomposition of 2,2,3-Trimethylbutane in the Presence of Oxygen',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "76",
        pages = """825""",
        year = "1980",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1980BAL/WAL825:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00007080
Uncertainty: 1.3200001
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 406,
    label = "C7H16 <=> C4H9-3 + C3H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+16, 's^-1'),
        n = 0,
        Ea = (305.973, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1100, 'K'),
        Pmin = (203000, 'Pa'),
        Pmax = (608000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Comparative rate single-pulse shock tube studies on the thermal decomposition of cyclohexene, 2,2,3-trimethylbutane, isopropyl bromide, and ethylcyclobutane',
        journal = "Int. J. Chem. Kinet.",
        volume = "2",
        pages = """311""",
        year = "1970",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1970TSA311:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00007080
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 407,
    label = "C7H16 <=> C4H9-3 + C3H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.58e+16, 's^-1'),
        n = 0,
        Ea = (305.141, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1070, 'K'),
        Tmax = (1200, 'K'),
        Pmin = (405000, 'Pa'),
        Pmax = (405000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Thermal decomposition of hexamethylethane, 2,2,3-trimethylbutane, and neopentane in a single-pulse shock tube',
        journal = "J. Chem. Phys.",
        volume = "44",
        pages = """4283-4295""",
        year = "1966",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1966TSA4283-4295:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00007080
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007080/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 408,
    label = "C4H9-3 + C3H7 <=> C7H16",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.82e+09, 'm^3/(mol*s)'),
        n = -1.17,
        Ea = (-0.54, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Klippenstein, S.J.", "Georgievskii, Y.", "Harding, L.B."],
        title = u'Predictive theory for the combination kinetics of two alkyl radicals',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "8",
        pages = """1133-1147""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006KLI/GEO1133-1147:9",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00007080
Pressure dependence: Rate constant is high pressure limit

Rate constants were calculated with an ab initio transition state theory employing direct evaluations of the orientation dependent interaction energies at the CASPT2/cc-pvdz level within variable reaction
coordinate transition state theory (VRC-TST). Results were compared with experiment for a series of alkyl radicals and good quantitative agreement was found.

Each methyl substituent adjacent to a radical site was found to reduce the rate coefficient by about a factor of two. Rate constants are predicted to decrease substantially with increasing temperature, with the more sterically hindered reactants having a more rapid decrease. The geometric mean rule was found to be in good agreement with the detailed calculations.

The authors state the rate parameters are strictly applicable between 200-2000 K but that they should provide reasonable predictions up to about 2700 K.
""",
)

entry(
    index = 409,
    label = "C6H14O <=> C2H5O + C4H9-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.14e+16, 's^-1'),
        n = 0,
        Ea = (311.793, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976TSA173:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00007090
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007090/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 410,
    label = "C7H16-2 <=> C5H11-2 + C2H5",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.72e+16, 's^-1'),
        n = 0,
        Ea = (322.602, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1070, 'K'),
        Tmax = (1230, 'K'),
        Pmin = (57100, 'Pa'),
        Pmax = (164000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Thermal decomposition of 3,4-dimethylpentene-1,2,3,3-trimethylpentane, 3,3-dimethylpentane, and isobutylbenzene in a single pulse shock tube',
        journal = "Int. J. Chem. Kinet.",
        volume = "1",
        pages = """245""",
        year = "1969",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1969TSA245:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00007564
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007564/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 411,
    label = "C6H12O <=> C2H3O + C4H9",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+16, 's^-1', '*|/', 1.7),
        n = 0,
        Ea = (318.444, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (960, 'K'),
        Tmax = (1170, 'K'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Single pulse shock tube study on the thermal stability of ketones',
        journal = "Int. J. Chem. Kinet.",
        volume = "16",
        pages = """1543""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984TSA1543:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00007657
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007657/rk00000001.xml
Uncertainty: 1.7
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 412,
    label = "C6H14O-2 <=> C3H7O + C3H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.74e+16, 's^-1'),
        n = 0,
        Ea = (310.961, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976TSA173:11",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00008054
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008054/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 413,
    label = "C5H8O2-2 <=> C3H5O-4 + C2H3O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.91e+16, 's^-1'),
        n = 0,
        Ea = (283.523, 'kJ/mol', '+|-', 11.308),
        T0 = (1, 'K'),
        Tmin = (362, 'K'),
        Tmax = (398, 'K'),
        Pmin = (8666, 'Pa'),
        Pmax = (30700, 'Pa'),
    ),
    reference = Article(
        authors = ["Scherzer, K.", "Knoll, H.", "Geiseler, G."],
        title = u'Thermische und durch Methylradikale initiierte Spaltung von Pentandion-(2,3) bei geringen Umsaetzen',
        journal = "J. Prakt. Chem.",
        volume = "316",
        pages = """415""",
        year = "1974",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1974SCH/KNO415:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00008118
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008118/rk00000001.xml
Bath gas: CH3C(O)C(O)C2H5
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 414,
    label = "C7H14 <=> C6H11 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1e+16, 's^-1'),
        n = 0,
        Ea = (291.007, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1080, 'K'),
        Tmax = (1150, 'K'),
        Pmin = (57300, 'Pa'),
        Pmax = (60700, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Thermal Decomposition of 1,1,2,2-Tetramethylcyclopropane in a Single-Pulse Shock Tube',
        journal = "Int. J. Chem. Kinet.",
        volume = "5",
        pages = """651""",
        year = "1973",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1973TSA651:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00008332
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008332/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 415,
    label = "C7H12 <=> C6H9-2 + CH3",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.51e+16, 's^-1', '*|/', 2),
        n = 0,
        Ea = (298.49, 'kJ/mol', '+|-', 5.978),
        T0 = (1, 'K'),
        Tmin = (903, 'K'),
        Tmax = (1250, 'K'),
    ),
    reference = Article(
        authors = ["King, K.D.", "Nguyen, T.T."],
        title = u'Very Low-Pressure Pyrolysis (VLPP) of Pentynes. II. 4-Methylpent-2-yne and 4,4-Dimethyl-pent-2-yne. Heats of Formation and Resonance Stabilization Energies of Methyl-Substituted Propargyl Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """255""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981KIN/NGU255:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009241
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009241/rk00000001.xml
Uncertainty: 2.0
Bath gas: (tert-C4H9)CCCH3
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 416,
    label = "C4H9-3 + C3H5 <=> C7H14-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.24e+08, 'm^3/(mol*s)', '*|/', 1.5),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:76",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00009783
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009783/rk00000001.xml
Uncertainty: 1.5
""",
)

entry(
    index = 417,
    label = "C3H5 + C4H9-4 <=> C7H14-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.05e+07, 'm^3/(mol*s)', '*|/', 3),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991TSA221-273:105",
    ),
    referenceType = "review",
    shortDesc = u"""Extensive literature review""",
    longDesc = 
u"""
PrIMe Reaction: r00010126
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010126/rk00000001.xml
Uncertainty: 3.0
""",
)

entry(
    index = 418,
    label = "C6H6O <=> H + C6H5O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.01e+71, 's^-1'),
        n = -15.92,
        Ea = (522.149, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (800, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Xu, Z.F.", "Lin, M.C."],
        title = u'Ab initio kinetics for the unimolecular reaction C6H5OH -&gt; CO+C5H6',
        journal = "J. Phys. Chem. A",
        volume = "110",
        pages = """1672-1677""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006XU/LIN1672-1677:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00010358
Pressure dependence: Rate constant is pressure dependent

Reaction potential energy surface was studied using quantum chemistry and rate constants were calculated using RRKM / master equation analysis. Rate constants were calculated for wide ranges of temperatures and pressures
""",
)

entry(
    index = 419,
    label = "C6H6O <=> H + C6H5O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.33e+17, 's^-1'),
        n = -0.51,
        Ea = (383.297, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (800, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Xu, Z.F.", "Lin, M.C."],
        title = u'Ab initio kinetics for the unimolecular reaction C6H5OH -&gt; CO+C5H6',
        journal = "J. Phys. Chem. A",
        volume = "110",
        pages = """1672-1677""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006XU/LIN1672-1677:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00010358
Pressure dependence: Rate constant is high pressure limit

Reaction potential energy surface was studied using quantum chemistry and rate constants were calculated using RRKM / master equation analysis. Rate constants were calculated for wide ranges of temperatures and pressures
""",
)

entry(
    index = 420,
    label = "C6H6O <=> H + C6H5O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.63e+14, 's^-1'),
        n = 0,
        Ea = (363.59, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Zhu, L.", "Bozzelli, J.W."],
        title = u'Kinetics and Thermochemistry for the Gas-Phase Keto-Enol Tautomerism of Phenol &lt;-&gt; 2,4-Cyclohexadienone',
        journal = "J. Phys. Chem. A",
        volume = "107",
        pages = """3696-3703""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003ZHU/BOZ3696-3703:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00010358
Pressure dependence: Rate constant is high pressure limit

Extensive thermochemical data for reactants, products, and transition states are presented.
""",
)

entry(
    index = 421,
    label = "C6H6O <=> H + C6H5O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.25e+67, 's^-1'),
        n = -14.82,
        Ea = (512.958, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (2400, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Zhu, L.", "Bozzelli, J.W."],
        title = u'Kinetics and Thermochemistry for the Gas-Phase Keto-Enol Tautomerism of Phenol &lt;-&gt; 2,4-Cyclohexadienone',
        journal = "J. Phys. Chem. A",
        volume = "107",
        pages = """3696-3703""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003ZHU/BOZ3696-3703:7",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00010358

Extensive thermochemical data for reactants, products, and transition states are presented.
""",
)

entry(
    index = 422,
    label = "C6H6O <=> H + C6H5O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.67e+16, 's^-1'),
        n = 0,
        Ea = (371.657, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1070, 'K'),
        Tmax = (1160, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Lovell, A.B.", "Brezinsky, K.", "Glassman, I."],
        title = u'The gas phase pyrolysis of phenol',
        journal = "Int. J. Chem. Kinet.",
        volume = "21",
        pages = """547-560""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989LOV/BRE547-560:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010358
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010358/rk00000004.xml
""",
)

entry(
    index = 423,
    label = "C7H12-2 <=> C3H3-2 + C4H9-4",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+16, 's^-1'),
        n = 0,
        Ea = (305.141, 'kJ/mol', '+|-', 3.051),
        T0 = (1, 'K'),
        Tmin = (990, 'K'),
        Tmax = (1200, 'K'),
        Pmin = (203000, 'Pa'),
        Pmax = (608000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Thermal Stability of Intermediate Sized Acetylenic Compounds and the Heats of Formation of Propargyl Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "10",
        pages = """687""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978TSA687:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010729
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010729/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 424,
    label = "CH3 + C6H5-2 <=> C7H8",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.38e+07, 'm^3/(mol*s)', '+|-', 8e-08),
        n = 0,
        Ea = (0.191, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (980, 'K'),
        Pmin = (400, 'Pa'),
        Pmax = (400, 'Pa'),
    ),
    reference = Article(
        authors = ["Tokmakov, I.V.", "Park, J.", "Gheyas, S.", "Lin, M.C."],
        title = u'Experimental and theoretical studies of the reaction of the phenyl radical with methane',
        journal = "J. Phys. Chem. A",
        volume = "103",
        pages = """3636-3645""",
        year = "1999",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1999TOK/PAR3636-3645:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from detailed balance/reverse rate""",
    longDesc = 
u"""
PrIMe Reaction: r00010761
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010761/rk00000001.xml
Note: Invalid activation energy uncertainty (0.299) found and ignored
""",
)

entry(
    index = 425,
    label = "C7H8 <=> CH3 + C6H5-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5e+16, 's^-1'),
        n = 0,
        Ea = (410.032, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1040, 'K'),
        Tmax = (1270, 'K'),
    ),
    reference = Article(
        authors = ["Lifshitz, A.", "Suslensky, A.", "Tamburu, C."],
        title = u'Thermal reactions of 2,3-dihydrobenzofuran: Experimental results and computer modeling',
        journal = "Proc. Combust. Inst.",
        volume = "28",
        pages = """1733-1739""",
        year = "2000",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2000LIF/SUS1733-1739:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010761
Experimental procedure: Shock tube
Time resolution: In real time
Analytical technique: GC-MS
""",
)

entry(
    index = 426,
    label = "C7H8 <=> CH3 + C6H5-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.91e+12, 's^-1'),
        n = 0,
        Ea = (303.478, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1600, 'K'),
        Tmax = (2100, 'K'),
        Pmin = (50700, 'Pa'),
        Pmax = (50700, 'Pa'),
    ),
    reference = Article(
        authors = ["Pamidimukkala, K.M.", "Kern, R.D.", "Patel, M.R.", "Wei, H.C.", "Kiefer, J.H."],
        title = u'High-temperature pyrolysis of toluene',
        journal = "J. Phys. Chem.",
        volume = "91",
        pages = """2148""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987PAM/KER2148:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010761
Bath gas: Ne
Excitation technique: Thermal
Analytical technique: Laser schlieren
""",
)

entry(
    index = 427,
    label = "C7H8 <=> CH3 + C6H5-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.3e+22, 's^-1'),
        n = -1.73,
        Ea = (435.973, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Cavallotti, C.", "Mancarella, S.", "Rota, R.", "Carra, S."],
        title = u'Conversion of C5 into C6 cyclic species through the formation of C7 intermediates',
        journal = "J. Phys. Chem. A",
        volume = "111",
        pages = """3959-3969""",
        year = "2007",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2007CAV/MAN3959-3969:8",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00010761
""",
)

entry(
    index = 428,
    label = "C7H8 <=> CH3 + C6H5-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.62e+25, 's^-1'),
        n = -2.53,
        Ea = (437.228, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1027, 'K'),
        Tmax = (1897, 'K'),
    ),
    reference = Article(
        authors = ["Sivaramakrishnan, R.", "Tranter, R.S.", "Brezinsky, K."],
        title = u'High pressure pyrolysis of toluene. 1. Experiments and modeling of toluene decomposition',
        journal = "J. Phys. Chem. A",
        volume = "110",
        pages = """9388-9399""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006SIV/TRA9388-9399:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Derived from detailed balance/reverse rate""",
    longDesc = 
u"""
PrIMe Reaction: r00010761
Pressure dependence: Rate constant is high pressure limit

Rate constant values were determined from combinig theoretical rate constanst for the reverse reaction and critically evaluated value of reaction enthalpy.
""",
)

entry(
    index = 429,
    label = "C7H8 <=> CH3 + C6H5-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.07e+16, 's^-1'),
        n = 0,
        Ea = (408.555, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1027, 'K'),
        Tmax = (1897, 'K'),
    ),
    reference = Article(
        authors = ["Sivaramakrishnan, R.", "Tranter, R.S.", "Brezinsky, K."],
        title = u'High pressure pyrolysis of toluene. 1. Experiments and modeling of toluene decomposition',
        journal = "J. Phys. Chem. A",
        volume = "110",
        pages = """9388-9399""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006SIV/TRA9388-9399:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Derived from detailed balance/reverse rate""",
    longDesc = 
u"""
PrIMe Reaction: r00010761
Pressure dependence: Rate constant is high pressure limit

Rate constant values were determined from combinig theoretical rate constanst for the reverse reaction and critically evaluated value of reaction enthalpy.
""",
)

entry(
    index = 430,
    label = "C7H14-4 <=> CH3 + C6H11-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+16, 's^-1', '*|/', 2),
        n = 0,
        Ea = (368.331, 'kJ/mol', '+|-', 11.058),
        T0 = (1, 'K'),
        Tmin = (1010, 'K'),
        Tmax = (1210, 'K'),
    ),
    reference = Article(
        authors = ["Brown, T.C.", "King, K.D."],
        title = u'Very low-pressure pyrolysis (VLPP) of methyl- and ethynyl- cyclopentanes and cyclohexanes',
        journal = "Int. J. Chem. Kinet.",
        volume = "21",
        pages = """251-266""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989BRO/KIN251-266:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00010787
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010787/rk00000002.xml
Uncertainty: 2.0
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 431,
    label = "C7H12-3 <=> C4H7 + C3H5",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.7e+14, 's^-1', '+|-', 5.9e+13),
        n = 0,
        Ea = (235.3, 'kJ/mol', '+|-', 2.353),
        T0 = (1, 'K'),
        Tmin = (686, 'K'),
        Tmax = (801, 'K'),
    ),
    reference = Article(
        authors = ["Roth, W.R.", "Bauer, F.", "Beitat, A.", "Ebbrecht, T.", "Wustefeld, M."],
        title = u'Die bildungsenthalpie des allyl- und methallyl-radikals',
        journal = "Chem. Ber.",
        volume = "124",
        pages = """1453-1460""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991ROT/BAU1453-1460:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00012588
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012588/rk00000001.xml
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 432,
    label = "C5H11-3 + O2 <=> C5H11O2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.84e+16, 'm^3/(mol*s)'),
        n = -3.82,
        Ea = (5.979, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004SUN/BOZ1694-1711:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00016216
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016216/rk00000003.xml

Quantum calculations of energetics of pathways related to reaction between neopentyl radical and O2 (and subsequent reaction pathways). This includes primary reaction pathways as well as subsequent secondary reactions. Used ab initio CBS-Q method, as well as B3LYP/6-31G(d,p) for some molecules. Many reaction channels are discussed in paper, for some, rate expressions are provided at low pressure limit, high pressure limit, and a number of intermediate pressures. For some reaction channels, no rate expressions are given in paper, but are provided in auxillary information associated with the article in JPC.

Rate expressions reported are derived from ab initio transition states using QRRK analysis of the chemically activated reaction pathways. We have only abstracted rate expressions from the paper for 1 atm and 300-900 K. For other pressures and at higher temperatures see paper.
""",
)

entry(
    index = 433,
    label = "C7H12-4 <=> C3H3-2 + C4H9",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+15, 's^-1'),
        n = 0,
        Ea = (291.007, 'kJ/mol', '+|-', 2.91),
        T0 = (1, 'K'),
        Tmin = (990, 'K'),
        Tmax = (1200, 'K'),
        Pmin = (203000, 'Pa'),
        Pmax = (608000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Thermal Stability of Intermediate Sized Acetylenic Compounds and the Heats of Formation of Propargyl Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "10",
        pages = """687""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978TSA687:8",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00016546
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016546/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 434,
    label = "C7H14-5 <=> C4H7-2 + C3H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+15, 's^-1'),
        n = 0,
        Ea = (270.22, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1030, 'K'),
        Tmax = (1090, 'K'),
        Pmin = (69300, 'Pa'),
        Pmax = (167000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Thermal decomposition of 3,4-dimethylpentene-1,2,3,3-trimethylpentane, 3,3-dimethylpentane, and isobutylbenzene in a single pulse shock tube',
        journal = "Int. J. Chem. Kinet.",
        volume = "1",
        pages = """245""",
        year = "1969",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1969TSA245:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00013101
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013101/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 435,
    label = "C7H8O <=> C6H5O + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+14, 's^-1', '*|/', 1.58),
        n = 0,
        Ea = (255.254, 'kJ/mol', '+|-', 7.658),
        T0 = (1, 'K'),
        Tmin = (720, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (2026, 'Pa'),
        Pmax = (12200, 'Pa'),
    ),
    reference = Article(
        authors = ["Back, M.H."],
        title = u'Comment on the thermal decomposition of anisole and the heat of formation of the phenoxy radical',
        journal = "J. Phys. Chem.",
        volume = "93",
        pages = """6880-6881""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989BAC6880-6881:1",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00004429
Uncertainty: 1.58
Bath gas: Ar
""",
)

entry(
    index = 436,
    label = "C7H8O <=> C6H5O + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+15, 's^-1', '*|/', 1.58),
        n = 0,
        Ea = (266.063, 'kJ/mol', '+|-', 2.661),
        T0 = (1, 'K'),
        Tmin = (793, 'K'),
        Tmax = (1020, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Arends, I.W.C.E.", "Louw, R.", "Mulder, P."],
        title = u'Kinetic study of the thermolysis of anisole in a hydrogen atmosphere',
        journal = "J. Phys. Chem.",
        volume = "97",
        pages = """7914-7925""",
        year = "1993",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1993ARE/LOU7914-7925:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00004429
Uncertainty: 1.58
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 437,
    label = "C7H8O <=> C6H5O + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+15, 's^-1'),
        n = 0,
        Ea = (266.063, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (720, 'K'),
        Tmax = (795, 'K'),
    ),
    reference = Article(
        authors = ["Suryan, M.M.", "Kafafi, S.A.", "Stein, S.E."],
        title = u'The thermal decomposition of hydroxy- and methoxy-substituted anisoles',
        journal = "J. Am. Chem. Soc.",
        volume = "111",
        pages = """1423-1429""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989SUR/KAF1423-1429:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00004429
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 438,
    label = "C7H8O <=> C6H5O + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.9e+15, 's^-1', '+|-', 9.9e+14),
        n = 0,
        Ea = (267.726, 'kJ/mol', '+|-', 2.677),
        T0 = (1, 'K'),
        Tmin = (850, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (2026, 'Pa'),
        Pmax = (12200, 'Pa'),
    ),
    reference = Article(
        authors = ["Mackie, J.C.", "Doolan, K.R.", "Nelson, P.F."],
        title = u'Kinetics of the thermal decomposition of methoxybenzene (anisole)',
        journal = "J. Phys. Chem.",
        volume = "93",
        pages = """664-670""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989MAC/DOO664-670:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00004429
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 439,
    label = "C7H8O <=> C6H5O + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.61e+15, 's^-1'),
        n = 0,
        Ea = (262.737, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (800, 'K'),
        Tmax = (900, 'K'),
        Pmin = (1200, 'Pa'),
        Pmax = (1200, 'Pa'),
    ),
    reference = Article(
        authors = ["Bruinsma, O.S.L.", "Geertsman, R.S.", "Bank, P.", "Moulijn, J.A."],
        title = u'Gas phase pyrolysis of coal-related aromatic compounds in a coiled tube flow reactor. 1. Benzene and derivatives',
        journal = "Fuel",
        volume = "67",
        pages = """327-333""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988BRU/GEE327-333:10",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00004429
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 440,
    label = "C7H8O <=> C6H5O + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.2e+16, 's^-1', '+|-', 3e+15),
        n = 0,
        Ea = (275.209, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1580, 'K'),
        Pmin = (40500, 'Pa'),
        Pmax = (91200, 'Pa'),
    ),
    reference = Article(
        authors = ["Lin, C-Y.", "Lin, M.C."],
        title = u'Thermal decomposition of methyl phenyl ether in shock waves: The kinetics of phenoxy radical reactions',
        journal = "J. Phys. Chem.",
        volume = "90",
        pages = """425""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986LIN/LIN425:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00004429
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: IR absorption
""",
)

entry(
    index = 441,
    label = "C7H8O <=> C6H5O + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+13, 's^-1', '*|/', 2),
        n = 0,
        Ea = (242.783, 'kJ/mol', '+|-', 7.283),
        T0 = (1, 'K'),
        Tmin = (720, 'K'),
        Tmax = (795, 'K'),
        Pmin = (533, 'Pa'),
        Pmax = (2133, 'Pa'),
    ),
    reference = Article(
        authors = ["Paul, S.", "Back, M.H."],
        title = u'A kinetic determination of the dissociation energy of the C-O bond in anisole',
        journal = "Can. J. Chem.",
        volume = "53",
        pages = """3330""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975PAU/BAC3330:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00004429
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004429/rk00000001.xml
Uncertainty: 2.0
Bath gas: Methoxybenzene
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 442,
    label = "C7H14O <=> C3H5O-3 + C4H9-4",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+16, 's^-1'),
        n = 0,
        Ea = (337.568, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (960, 'K'),
        Tmax = (1180, 'K'),
        Pmin = (152000, 'Pa'),
        Pmax = (608000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Single pulse shock tube study on the thermal stability of ketones',
        journal = "Int. J. Chem. Kinet.",
        volume = "16",
        pages = """1543""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984TSA1543:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005417
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00005417/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 443,
    label = "C8H18 <=> C7H15 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2e+15, 's^-1'),
        n = 0,
        Ea = (325.096, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1100, 'K'),
        Tmax = (1400, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (800, 'Pa'),
    ),
    reference = Article(
        authors = ["Doolan, K>R.", "Mackie, J.C."],
        title = u'Kinetics of pyrolysis of octane in argon-hydrogen mixtures',
        journal = "Combust. Flame",
        volume = "50",
        pages = """29""",
        year = "1983",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1983DOO/MAC29:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00005574
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 444,
    label = "C8H18 <=> C7H15 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.16e+16, 's^-1'),
        n = 0,
        Ea = (316.781, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (763, 'K'),
        Tmax = (783, 'K'),
    ),
    reference = Article(
        authors = ["Blackmore, D.R.", "Hinshelwood, C."],
        title = u'Derivation of rate constants for steps in the free-radical chain decomposition of paraffins',
        journal = "Proc. R. Soc. London A",
        volume = "268",
        pages = """36""",
        year = "1962",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1962BLA/HIN36:7",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00005574
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00005574/rk00000001.xml
""",
)

entry(
    index = 445,
    label = "C8H18-2 <=> C5H11-2 + C3H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.41e+16, 's^-1'),
        n = 0,
        Ea = (298.49, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1030, 'K'),
        Tmax = (1170, 'K'),
        Pmin = (66900, 'Pa'),
        Pmax = (161000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Thermal decomposition of 3,4-dimethylpentene-1,2,3,3-trimethylpentane, 3,3-dimethylpentane, and isobutylbenzene in a single pulse shock tube',
        journal = "Int. J. Chem. Kinet.",
        volume = "1",
        pages = """245""",
        year = "1969",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1969TSA245:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00007562
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007562/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 446,
    label = "C8H18-3 <=> C4H9-3 + C4H9",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+16, 's^-1', '*|/', 1.17),
        n = 0,
        Ea = (302.647, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1040, 'K'),
        Tmax = (1180, 'K'),
        Pmin = (54700, 'Pa'),
        Pmax = (167000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Thermal Decomposition of 3,4-Dimethylhexane, 2,2,3-Trimethylpentane, tert-Butylcyclohexane, and Related Hydrocarbons',
        journal = "J. Phys. Chem.",
        volume = "76",
        pages = """143""",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972TSA143:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00007656
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007656/rk00000001.xml
Uncertainty: 1.17
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 447,
    label = "C8H18-4 <=> C4H9 + C4H9",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.19e+16, 's^-1', '*|/', 1.2),
        n = 0,
        Ea = (315.118, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1040, 'K'),
        Tmax = (1180, 'K'),
        Pmin = (54700, 'Pa'),
        Pmax = (167000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Thermal Decomposition of 3,4-Dimethylhexane, 2,2,3-Trimethylpentane, tert-Butylcyclohexane, and Related Hydrocarbons',
        journal = "J. Phys. Chem.",
        volume = "76",
        pages = """143""",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972TSA143:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00007681
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007681/rk00000001.xml
Uncertainty: 1.2
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 448,
    label = "C8H18-5 <=> C4H9-3 + C4H9-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+17, 's^-1'),
        n = 0,
        Ea = (304.31, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1100, 'K'),
        Pmin = (66700, 'Pa'),
        Pmax = (168000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Evidence for Strongly Temperature-Dependent A Factors in Alkane Decomposition and High Heats of Formation for Alkyl Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "10",
        pages = """821""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978TSA821:5",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00009780
Bath gas: Ar
""",
)

entry(
    index = 449,
    label = "C8H18-5 <=> C4H9-3 + C4H9-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.03e+16, 's^-1'),
        n = 0,
        Ea = (290.175, 'kJ/mol', '+|-', 2.902),
        T0 = (1, 'K'),
        Tmin = (713, 'K'),
        Tmax = (813, 'K'),
        Pmin = (7999, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Atri, G.M.", "Baldwin, R.R.", "Evans, G.A.", "Walker, R.W."],
        title = u'Decomposition of 2,2,3,3-Tetramethylbutane in the Presence of Oxygen',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "74",
        pages = """366""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978ATR/BAL366:1",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00009780
Bath gas: N2
""",
)

entry(
    index = 450,
    label = "C8H18-5 <=> C4H9-3 + C4H9-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.04e+17, 's^-1'),
        n = 0,
        Ea = (294.332, 'kJ/mol', '+|-', 2.943),
        T0 = (1, 'K'),
        Tmin = (673, 'K'),
        Tmax = (815, 'K'),
        Pmin = (7999, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Baldwin, R.R.", "Hisham, M.W.M.", "Keen, A.", "Walker, R.W."],
        title = u'The Decomposition of 2,2,3,3-Tetramethylbutane in KCl- and B2O3-coateed Vessels in the Presence of Oxygen',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "78",
        pages = """1165""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982BAL/HIS1165:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009780
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 451,
    label = "C8H18-5 <=> C4H9-3 + C4H9-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+17, 's^-1'),
        n = 0,
        Ea = (299.321, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (900, 'K'),
        Pmin = (152000, 'Pa'),
        Pmax = (152000, 'Pa'),
    ),
    reference = Article(
        authors = ["Walker, J.A.", "Tsang, W."],
        title = u'Thermal Decomposition of Hexamethylethane in a Flow System',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """867""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979WAL/TSA867:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00009780
Bath gas: He
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 452,
    label = "C8H18-5 <=> C4H9-3 + C4H9-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+16, 's^-1'),
        n = 0,
        Ea = (286.018, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (990, 'K'),
        Tmax = (1100, 'K'),
        Pmin = (66700, 'Pa'),
        Pmax = (168000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Evidence for Strongly Temperature-Dependent A Factors in Alkane Decomposition and High Heats of Formation for Alkyl Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "10",
        pages = """821""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978TSA821:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009780
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 453,
    label = "C8H18-5 <=> C4H9-3 + C4H9-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+10, 's^-1'),
        n = 0,
        Ea = (180.424, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (750, 'K'),
        Tmax = (950, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Taylor, J.E.", "Milazzo, T.S."],
        title = u'Gas-Phase Pyrolysis of 2,2,3,3-Tetramethylbutane using a Wall-less Reactor',
        journal = "Int. J. Chem. Kinet.",
        volume = "10",
        pages = """1245""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978TAY/MIL1245:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009780
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 454,
    label = "C8H18-5 <=> C4H9-3 + C4H9-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+16, 's^-1'),
        n = 0,
        Ea = (284.355, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (850, 'K'),
        Tmax = (1150, 'K'),
    ),
    reference = Article(
        authors = ["Golden, D.M.", "Alfassi, Z.B.", "Beadle, P.C."],
        title = u"Very Low-Pressure Pyrolysis (VLPP) of Alkanes: n-Butane, 2,3-Dimethylbutane, 2,2',3,3'-Tetramethylbutane, and Isobutane",
        journal = "Int. J. Chem. Kinet.",
        volume = "6",
        pages = """359""",
        year = "1974",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1974GOL/ALF359:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00009780
Bath gas: (CH3)3CC(CH3)3
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 455,
    label = "C8H18-5 <=> C4H9-3 + C4H9-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+16, 's^-1'),
        n = 0,
        Ea = (286.849, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (985, 'K'),
        Tmax = (1140, 'K'),
        Pmin = (304000, 'Pa'),
        Pmax = (304000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Thermal decomposition of hexamethylethane, 2,2,3-trimethylbutane, and neopentane in a single-pulse shock tube',
        journal = "J. Chem. Phys.",
        volume = "44",
        pages = """4283-4295""",
        year = "1966",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1966TSA4283-4295:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00009780
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009780/rk00000020.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 456,
    label = "C4H9-3 + C4H9-3 <=> C8H18-5",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.37e+08, 'm^3/(mol*s)'),
        n = -0.92,
        Ea = (-2.91, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Klippenstein, S.J.", "Georgievskii, Y.", "Harding, L.B."],
        title = u'Predictive theory for the combination kinetics of two alkyl radicals',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "8",
        pages = """1133-1147""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006KLI/GEO1133-1147:10",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00009780
Pressure dependence: Rate constant is high pressure limit

Rate constants were calculated with an ab initio transition state theory employing direct evaluations of the orientation dependent interaction energies at the CASPT2/cc-pvdz level within variable reaction
coordinate transition state theory (VRC-TST). Results were compared with experiment for a series of alkyl radicals and good quantitative agreement was found.

Each methyl substituent adjacent to a radical site was found to reduce the rate coefficient by about a factor of two. Rate constants are predicted to decrease substantially with increasing temperature, with the more sterically hindered reactants having a more rapid decrease. The geometric mean rule was found to be in good agreement with the detailed calculations.

The authors state the rate parameters are strictly applicable between 200-2000 K but that they should provide reasonable predictions up to about 2700 K.
""",
)

entry(
    index = 457,
    label = "C6H5O2 <=> C6H5-2 + O2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.36e+19, 's^-1'),
        n = -1.37,
        Ea = (203.928, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["da Silva, G.", "Bozzelli, J.W."],
        title = u'Variational analysis of the phenyl + O2 and phenoxy plus O reactions',
        journal = "J. Phys. Chem. A",
        volume = "112",
        pages = """3566-3575""",
        year = "2008",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2008DAS/BOZ3566-3575:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00011168
Pressure dependence: Rate constant is high pressure limit
""",
)

entry(
    index = 458,
    label = "C7H6O <=> H + C7H5O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+15, 's^-1'),
        n = 0,
        Ea = (350.039, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1170, 'K'),
        Tmax = (1240, 'K'),
    ),
    reference = Article(
        authors = ["Grela, M.A.", "Colussi, A.J."],
        title = u'Kinetics and mechanism of the thermal decomposition of unsaturated aldehydes: Benzaldehyde, 2-butenal, and 2-furaldehyde',
        journal = "J. Phys. Chem.",
        volume = "90",
        pages = """434""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986GRE/COL434:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011400
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011400/rk00000003.xml
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 459,
    label = "C8H14 <=> C5H9-4 + C3H5",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.2e+16, 's^-1', '+|-', 8e+15),
        n = 0,
        Ea = (296.827, 'kJ/mol', '+|-', 2.968),
        T0 = (1, 'K'),
        Tmin = (1040, 'K'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992TSA/WAL8378-8384:8",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00012437
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012437/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 460,
    label = "C8H14-2 <=> C4H7 + C4H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6e+14, 's^-1', '+|-', 1.6e+14),
        n = 0,
        Ea = (238.625, 'kJ/mol', '+|-', 2.386),
        T0 = (1, 'K'),
        Tmin = (690, 'K'),
        Tmax = (794, 'K'),
    ),
    reference = Article(
        authors = ["Roth, W.R.", "Bauer, F.", "Beitat, A.", "Ebbrecht, T.", "Wustefeld, M."],
        title = u'Die bildungsenthalpie des allyl- und methallyl-radikals',
        journal = "Chem. Ber.",
        volume = "124",
        pages = """1453-1460""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991ROT/BAU1453-1460:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015596
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015596/rk00000004.xml
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 461,
    label = "C6H14O2 <=> C3H7O-3 + C3H7O-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+13, 's^-1'),
        n = 0,
        Ea = (146.335, 'kJ/mol', '+|-', 1.463),
        T0 = (1, 'K'),
        Tmin = (373, 'K'),
        Tmax = (403, 'K'),
        Pmin = (3013, 'Pa'),
        Pmax = (7773, 'Pa'),
    ),
    reference = Article(
        authors = ["East, R.L.", "Phillips, L."],
        title = u'Kinetics of disproportionation-combination reactions between the n-propoxyl radical and nitric oxide, and of the pyrolysis of the O-O bond in di-n-propyl peroxide in the gas phase',
        journal = "J. Chem. Soc. A",
        pages = """331""",
        year = "1970",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1970EAS/PHI331:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00015703
Bath gas: NO
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 462,
    label = "C6H14O2 <=> C3H7O-3 + C3H7O-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.42e+15, 's^-1'),
        n = 0,
        Ea = (150.492, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (420, 'K'),
        Tmax = (448, 'K'),
        Pmin = (26.66, 'Pa'),
        Pmax = (400, 'Pa'),
    ),
    reference = Article(
        authors = ["Harris, E.J."],
        title = u'The decomposition of alkyl peroxides: dipropyl peroxide, ethyl hydrogen peroxide and propyl hydrogen peroxide',
        journal = "Proc. R. Soc. London A",
        volume = "173",
        pages = """126-146""",
        year = "1939",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1939HAR126-146:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015703
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015703/rk00000002.xml
Bath gas: (n-C3H7)-O-O-(n-C3H7)
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 463,
    label = "C6H14O2-2 <=> C3H7O-2 + C3H7O-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+16, 's^-1', '*|/', 50),
        n = 0,
        Ea = (163.795, 'kJ/mol', '+|-', 13.137),
        T0 = (1, 'K'),
        Tmin = (395, 'K'),
        Tmax = (432, 'K'),
    ),
    reference = Article(
        authors = ["Yee Quee, M.J.", "Thynne, J.C.J."],
        title = u'Reactions of isopropoxyl radicals',
        journal = "J. Chem. Soc. Faraday Trans.",
        volume = "64",
        pages = """1296""",
        year = "1968",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1968YEE/THY1296:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015740
Uncertainty: 50.0
Bath gas: NO
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 464,
    label = "C6H14O2-2 <=> C3H7O-2 + C3H7O-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.5e+15, 's^-1', '*|/', 2.51),
        n = 0,
        Ea = (155.481, 'kJ/mol', '+|-', 3.101),
        T0 = (1, 'K'),
        Tmin = (421, 'K'),
        Tmax = (458, 'K'),
        Pmin = (2000, 'Pa'),
        Pmax = (3333, 'Pa'),
    ),
    reference = Article(
        authors = ["Leggett, C.", "Thynne, J.C.J."],
        title = u'Thermal decomposition of dialkyl peroxides and heats of formation of the ethoxyl and isopropoxyl radicals',
        journal = "Trans. Faraday Soc.",
        volume = "63",
        pages = """2504-2509""",
        year = "1967",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1967LEG/THY2504-2509:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015740
Uncertainty: 2.51
Bath gas: (iso-C3H7O)2
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 465,
    label = "C6H14O2-2 <=> C3H7O-2 + C3H7O-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.4e+15, 's^-1'),
        n = 0,
        Ea = (153.818, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (378, 'K'),
        Tmax = (423, 'K'),
        Pmin = (4400, 'Pa'),
        Pmax = (14800, 'Pa'),
    ),
    reference = Article(
        authors = ["Hughes, G.A.", "Phillips, L."],
        title = u'The kinetics of disproportionation-combination reactions between the isopropoxyl radical and nitric oxide, and of the pyrolysis of the O-O bond in di-isopropyl peroxide',
        journal = "J. Chem. Soc. A",
        pages = """894-897""",
        year = "1967",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1967HUG/PHI894-897:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015740
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015740/rk00000001.xml
Bath gas: NO
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 466,
    label = "C8H16 <=> C4H7 + C4H9",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.27e+15, 's^-1', '*|/', 1.17),
        n = 0,
        Ea = (276.04, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1973TSA929:7",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00015745
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015745/rk00000001.xml
Uncertainty: 1.17
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 467,
    label = "C8H14-3 <=> C4H5-3 + C4H9-4",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.58e+16, 's^-1'),
        n = 0,
        Ea = (305.973, 'kJ/mol', '+|-', 3.06),
        T0 = (1, 'K'),
        Tmin = (990, 'K'),
        Tmax = (1200, 'K'),
        Pmin = (203000, 'Pa'),
        Pmax = (608000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Thermal Stability of Intermediate Sized Acetylenic Compounds and the Heats of Formation of Propargyl Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "10",
        pages = """687""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978TSA687:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00016525
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016525/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 468,
    label = "C6H5-2 + O2 <=> C6H5O2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.03e+06, 'm^3/(mol*s)', '*|/', 1.2),
        n = 0,
        Ea = (1.339, 'kJ/mol', '+|-', 0.549),
        T0 = (1, 'K'),
        Tmin = (297, 'K'),
        Tmax = (473, 'K'),
        Pmin = (2666, 'Pa'),
        Pmax = (10700, 'Pa'),
    ),
    reference = Article(
        authors = ["Yu, T.", "Lin, M.C."],
        title = u'Kinetics of the C6H5 + O2 reaction at low temperatures',
        journal = "J. Am. Chem. Soc.",
        volume = "116",
        pages = """9571-9576""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994YU/LIN9571-9576:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011168
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011168/rk00000002.xml
Uncertainty: 1.2
Bath gas: Ar
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 469,
    label = "C8H10O <=> C6H5O + C2H5",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+15, 's^-1'),
        n = 0,
        Ea = (259.412, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (720, 'K'),
        Tmax = (795, 'K'),
    ),
    reference = Article(
        authors = ["Suryan, M.M.", "Kafafi, S.A.", "Stein, S.E."],
        title = u'The thermal decomposition of hydroxy- and methoxy-substituted anisoles',
        journal = "J. Am. Chem. Soc.",
        volume = "111",
        pages = """1423-1429""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989SUR/KAF1423-1429:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00004476
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 470,
    label = "C8H10O <=> C6H5O + C2H5",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+15, 's^-1'),
        n = 0,
        Ea = (252.76, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (946, 'K'),
        Tmax = (1220, 'K'),
    ),
    reference = Article(
        authors = ["Colussi, A.J.", "Zabel, F.", "Benson, S.W."],
        title = u'The very low-pressure pyrolysis of phenyl ethyl ether, phenyl allyl ether, and benzyl methyl ether and the enthalpy of formation of the phenoxy radical',
        journal = "Int. J. Chem. Kinet.",
        volume = "9",
        pages = """161""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977COL/ZAB161:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00004476
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004476/rk00000001.xml
Bath gas: Ethoxybenzene
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 471,
    label = "C8H18O <=> C4H9O-2 + C4H9-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.1e+13, 's^-1'),
        n = 0,
        Ea = (214.513, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (523, 'K'),
        Tmax = (573, 'K'),
        Pmin = (1.33, 'Pa'),
        Pmax = (2.03e+07, 'Pa'),
    ),
    reference = Article(
        authors = ["Enguehard, F.", "Kressmann, S.", "Domine, F."],
        title = u'Kinetics of dibutylether pyrolysis at high pressure: Experimental study',
        journal = "Adv. Org. Geochem.",
        volume = "16",
        pages = """155-160""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990ENG/KRE155-160:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00006343
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00006343/rk00000001.xml
Bath gas: (n-C4H9)2O
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 472,
    label = "O2 + C6H7O <=> C6H7O3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.14e+09, 'm^3/(mol*s)'),
        n = -2.05,
        Ea = (19.622, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (400, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Lay, T.H.", "Bozzelli, J.W.", "Seinfeld, J.H."],
        title = u'Atmospheric photochemical oxidation of benzene: benzene + OH and the benzene-OH adduct (hydroxyl-2,4-cyclohexadienyl) + O2',
        journal = "J. Phys. Chem.",
        volume = "100",
        pages = """6543-6554""",
        year = "1996",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996LAY/BOZ6543-6554:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00013891
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013891/rk00000002.xml
Bath gas: N2
""",
)

entry(
    index = 473,
    label = "O2 + C6H7O <=> C6H7O3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.56e+30, 'm^3/(mol*s)'),
        n = -8.86,
        Ea = (15.881, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (400, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Lay, T.H.", "Bozzelli, J.W.", "Seinfeld, J.H."],
        title = u'Atmospheric photochemical oxidation of benzene: benzene + OH and the benzene-OH adduct (hydroxyl-2,4-cyclohexadienyl) + O2',
        journal = "J. Phys. Chem.",
        volume = "100",
        pages = """6543-6554""",
        year = "1996",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996LAY/BOZ6543-6554:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00013891
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013891/rk00000003.xml
Bath gas: N2
""",
)

entry(
    index = 474,
    label = "C8H10O2 <=> C6H5O2-2 + C2H5",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+15, 's^-1'),
        n = 0,
        Ea = (231.142, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (720, 'K'),
        Tmax = (795, 'K'),
    ),
    reference = Article(
        authors = ["Suryan, M.M.", "Kafafi, S.A.", "Stein, S.E."],
        title = u'The thermal decomposition of hydroxy- and methoxy-substituted anisoles',
        journal = "J. Am. Chem. Soc.",
        volume = "111",
        pages = """1423-1429""",
        year = "1989",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1989SUR/KAF1423-1429:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00004187
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004187/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 475,
    label = "C10H14 <=> C9H11 + CH3",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1.58e+16, 's^-1'),
        n = 0,
        Ea = (286.018, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (900, 'K'),
        Tmax = (1700, 'K'),
    ),
    reference = Article(
        authors = ["Brand, U.", "Hippler, H.", "Lindemann, L.", "Troe, J."],
        title = u'C-C and C-H bond splits of laser-excited aromatic molecules. 1. Specific and thermally averaged rate constants',
        journal = "J. Phys. Chem.",
        volume = "94",
        pages = """6305-6316""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990BRA/HIP6305-6316:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00004286
Bath gas: N2
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 476,
    label = "C10H14 <=> C9H11 + CH3",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (7.94e+15, 's^-1'),
        n = 0,
        Ea = (289.344, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (929, 'K'),
        Tmax = (1160, 'K'),
    ),
    reference = Article(
        authors = ["Robaugh, D.A.", "Stein, S.E."],
        title = u'Very-low-pressure pyrolysis of ethylbenzene, isopropylbenzene, and tert-butylbenzene',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """445""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981ROB/STE445:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00004286
Bath gas: t-Butylbenzene
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 477,
    label = "C10H14 <=> C9H11 + CH3",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (6.22e+13, 's^-1'),
        n = 0,
        Ea = (251.929, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (885, 'K'),
        Tmax = (940, 'K'),
        Pmin = (1600, 'Pa'),
        Pmax = (1733, 'Pa'),
    ),
    reference = Article(
        authors = ["Leigh, C.H.", "Szwarc, M."],
        title = u'An investigation of the pyrolyses of cumene, t-butyl-benzene and p-cymene, and the relevant bond dissociation energies',
        journal = "J. Chem. Phys.",
        volume = "20",
        pages = """844-847""",
        year = "1952",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1952LEI/SZW844-847:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00004286
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004286/rk00000001.xml
Bath gas: Toluene
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 478,
    label = "C9H11 + CH3 <=> C10H14",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (7.19e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (0.141, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1700, 'K'),
    ),
    reference = Article(
        authors = ["Brand, U.", "Hippler, H.", "Lindemann, L.", "Troe, J."],
        title = u'C-C and C-H bond splits of laser-excited aromatic molecules. 1. Specific and thermally averaged rate constants',
        journal = "J. Phys. Chem.",
        volume = "94",
        pages = """6305-6316""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990BRA/HIP6305-6316:12",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00004286
Bath gas: N2
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 479,
    label = "C10H14-2 <=> C8H9 + C2H5",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+14, 's^-1'),
        n = 0,
        Ea = (281.029, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (864, 'K'),
        Tmax = (1010, 'K'),
        Pmin = (1187, 'Pa'),
        Pmax = (1880, 'Pa'),
    ),
    reference = Article(
        authors = ["Esteban, G.L.", "Kerr, J.A.", "Trotman-Dickenson, A.F."],
        title = u'Pyrolysis of ethyl-, n-propyl-, and n-butyl-benzene and the heats of formation of the benzyl and n-propyl radicals',
        journal = "J. Chem. Soc.",
        pages = """3873""",
        year = "1963",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1963EST/KER3873:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00004483
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004483/rk00000001.xml
Bath gas: aniline
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 480,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.9e+12, 's^-1'),
        n = 0,
        Ea = (147.21, 'kJ/mol', '+|-', 0.418),
        T0 = (1, 'K'),
        Tmin = (513, 'K'),
        Tmax = (573, 'K'),
    ),
    reference = Article(
        authors = ["Cafferata, L.F.R.", "Jorge, N.L."],
        title = u'Determinacion Directa de  Parametros de Activacion de Reacciones Unimoleculares por Cromatografia Gaseosa',
        journal = "An. Asoc. Quim. Argent.",
        volume = "87",
        pages = """37-42""",
        year = "1999",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1999CAF/JOR37-42:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
Experimental procedure: Stirred flow reactor(PSR etc.)
Excitation technique: Thermal
Time resolution: In real time
Analytical technique: Gas chromatography

Consistent with previous data, but slightly lower rate.
""",
)

entry(
    index = 481,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+15, 's^-1', '*|/', 2),
        n = 0,
        Ea = (152.155, 'kJ/mol', '+|-', 4.556),
        T0 = (1, 'K'),
        Tmin = (389, 'K'),
        Tmax = (451, 'K'),
        Pmin = (10300, 'Pa'),
        Pmax = (12100, 'Pa'),
    ),
    reference = Article(
        authors = ["Kortvelyesi, T.", "Seres, L."],
        title = u'Thermal reaction of (CH3)2C=C(CH3)2 in the presence of di-tert-butyl peroxide; reactions of the radicals .CH3, (CH3)3C.C(CH3)2 and (CH3)2 C=C(CH3).CH2',
        journal = "J. Chim. Phys.",
        volume = "93",
        pages = """253-273""",
        year = "1996",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1996KOR/SER253-273:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
Uncertainty: 2.0
Bath gas: CO2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 482,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.72e+15, 's^-1', '*|/', 1.7),
        n = 0,
        Ea = (156.312, 'kJ/mol', '+|-', 1.563),
        T0 = (1, 'K'),
        Tmin = (391, 'K'),
        Tmax = (444, 'K'),
    ),
    reference = Article(
        authors = ["Seres, L.", "Nacsa, A.", "Arthur, N.L."],
        title = u'Thermal decomposition of di-t-butyl peroxide in the presence of (CH3)2C=CH2: reactions of CH3, (CH3)2CCH2CH3, and (CH3)2CCH2C(CH3)2CH2CH3 radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "26",
        pages = """227-246""",
        year = "1994",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1994SER/NAC227-246:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
Uncertainty: 1.7
Bath gas: (tert-C4H9O)2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 483,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.04e+15, 's^-1', '*|/', 2),
        n = 0,
        Ea = (156.312, 'kJ/mol', '+|-', 1.563),
        T0 = (1, 'K'),
        Tmin = (399, 'K'),
        Tmax = (434, 'K'),
        Pmin = (66700, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Sway, M.I."],
        title = u'Kinetics of abstraction reactions of tert-butoxyl radicals with cyclohexane and methyl-substituted cyclohexanes in the gas phase',
        journal = "J. Chem. Soc. Faraday Trans.",
        volume = "87",
        pages = """2157-2159""",
        year = "1991",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1991SWA2157-2159:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
Uncertainty: 2.0
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 484,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.24e+15, 's^-1', '*|/', 3.39),
        n = 0,
        Ea = (154.649, 'kJ/mol', '+|-', 4.648),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987BAT/ROB391:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
Uncertainty: 3.3900001
Bath gas: CF4
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 485,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+15, 's^-1', '*|/', 3.39),
        n = 0,
        Ea = (154.649, 'kJ/mol', '+|-', 4.648),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982BAT/ROB172:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
Uncertainty: 3.3900001
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 486,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+15, 's^-1', '*|/', 2),
        n = 0,
        Ea = (159.638, 'kJ/mol', '+|-', 3.201),
        T0 = (1, 'K'),
        Tmin = (399, 'K'),
        Tmax = (434, 'K'),
        Pmin = (2666, 'Pa'),
        Pmax = (26700, 'Pa'),
    ),
    reference = Article(
        authors = ["Al Akeel, N.Y.", "Selby, K.", "Waddington, D.J."],
        title = u'Reactions of Oxygenated Radicals in the Gas Phase. Part 8. Reactions of Alkoxyl Radicals with Aldehydes and Ketones',
        journal = "J. Chem. Soc. Perkin Trans. 2",
        pages = """1036""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981ALA/SEL1036:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
Uncertainty: 2.0
Bath gas: (tert-C4H9O)2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 487,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.61e+15, 's^-1'),
        n = 0,
        Ea = (157.975, 'kJ/mol', '+|-', 6.311),
        T0 = (1, 'K'),
        Tmin = (390, 'K'),
        Tmax = (440, 'K'),
        Pmin = (13300, 'Pa'),
        Pmax = (13300, 'Pa'),
    ),
    reference = Article(
        authors = ["Loucks, L.F.", "Liu, M.T.H.", "Hooper, D.G."],
        title = u'Pyrolysis of trifluoroacetaldehyde, initiated by di-tertiary-butyl peroxide decomposition',
        journal = "Can. J. Chem.",
        volume = "57",
        pages = """2201""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979LOU/LIU2201:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
Bath gas: CF3CHO
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 488,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.14e+15, 's^-1', '*|/', 3.16),
        n = 0,
        Ea = (152.155, 'kJ/mol', '+|-', 6.095),
        T0 = (1, 'K'),
        Tmin = (528, 'K'),
        Tmax = (677, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Lewis, D.K."],
        title = u'Di-tert-butyl peroxide decomposition behind shock waves',
        journal = "Can. J. Chem.",
        volume = "54",
        pages = """581-585""",
        year = "1976",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976LEW581-585:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
Uncertainty: 3.1600001
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 489,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+15, 's^-1', '*|/', 5),
        n = 0,
        Ea = (156.312, 'kJ/mol', '+|-', 4.698),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (660, 'K'),
        Pmin = (13.33, 'Pa'),
        Pmax = (13.33, 'Pa'),
    ),
    reference = Article(
        authors = ["Perona, M.J.", "Golden, D.M."],
        title = u'Very Low-Pressure Pyrolysis. VIII. The Decomposition of Di-t-Amyl Peroxide',
        journal = "Int. J. Chem. Kinet.",
        volume = "5",
        pages = """55""",
        year = "1973",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1973PER/GOL55:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
Uncertainty: 5.0
Bath gas: (tert-C4H9O)2
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 490,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+14, 's^-1', '*|/', 5),
        n = 0,
        Ea = (148.829, 'kJ/mol', '+|-', 7.45),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971CAD/TRO2296:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
Uncertainty: 5.0
Bath gas: C3H8
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 491,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.02e+16, 's^-1', '*|/', 1.05),
        n = 0,
        Ea = (162.964, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (503, 'K'),
        Tmax = (528, 'K'),
    ),
    reference = Article(
        authors = ["Retzloff, D.G.", "Coull, B.M.", "Coull, J."],
        title = u'A microchemical study of gas-phase kinetics for three irreversible reactions',
        journal = "J. Phys. Chem.",
        volume = "74",
        pages = """2455""",
        year = "1970",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1970RET/COU2455:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
Uncertainty: 1.05
Bath gas: (tert-C4H9O)2
Excitation technique: Thermal
Analytical technique: Gas chromatography
Note: Invalid activation energy uncertainty (335.073) found and ignored
""",
)

entry(
    index = 492,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.61e+15, 's^-1', '*|/', 1.51),
        n = 0,
        Ea = (157.975, 'kJ/mol', '+|-', 1.58),
        T0 = (1, 'K'),
        Tmin = (363, 'K'),
        Tmax = (403, 'K'),
        Pmin = (5066, 'Pa'),
        Pmax = (1.52e+06, 'Pa'),
    ),
    reference = Article(
        authors = ["Shaw, D.H.", "Pritchard, H.O."],
        title = u'Thermal decomposition of di-tert-buyl peroxide at high pressure',
        journal = "Can. J. Chem.",
        volume = "46",
        pages = """2721""",
        year = "1968",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1968SHA/PRI2721:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
Uncertainty: 1.51
Bath gas: CO2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 493,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.61e+12, 's^-1'),
        n = 0,
        Ea = (130.537, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (403, 'K'),
        Tmax = (423, 'K'),
        Pmin = (10300, 'Pa'),
        Pmax = (14900, 'Pa'),
    ),
    reference = Article(
        authors = ["Baker, G.", "Shaw, R."],
        title = u'Reactions of methoxyl, ethoxyl, and t-butoxyl with nitric oxide and with nitrogen dioxide',
        journal = "J. Chem. Soc.",
        pages = """6965""",
        year = "1965",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1965BAK/SHA6965:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
Bath gas: (tert-C4H9O)2
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 494,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+15, 's^-1'),
        n = 0,
        Ea = (156.312, 'kJ/mol', '+|-', 1.563),
        T0 = (1, 'K'),
        Tmin = (403, 'K'),
        Tmax = (433, 'K'),
        Pmin = (3600, 'Pa'),
        Pmax = (17300, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L.", "Benson, S.W."],
        title = u'Pyrolysis of di-tertiary butyl peroxide: temperature gradients and chain contribution to the rate',
        journal = "J. Chem. Phys.",
        volume = "36",
        pages = """895""",
        year = "1962",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1962BAT/BEN895:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
Bath gas: (tert-C4H9O)2
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 495,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.2e+16, 's^-1', '*|/', 1.1),
        n = 0,
        Ea = (160.469, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (430, 'K'),
        Tmax = (550, 'K'),
        Pmin = (1067, 'Pa'),
        Pmax = (3600, 'Pa'),
    ),
    reference = Article(
        authors = ["Mulcahy, M.F.R.", "Williams, D.J."],
        title = u'A stirred-flow reactor for investigating the kinetics of gaseous reactions: application to the decomposition of di-t-butyl peroxide',
        journal = "Aust. J. Chem.",
        volume = "14",
        pages = """534-544""",
        year = "1961",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1961MUL/WIL534-544:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
Uncertainty: 1.1
Bath gas: CO2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 496,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.5e+16, 's^-1'),
        n = 0,
        Ea = (162.132, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (376, 'K'),
        Tmax = (418, 'K'),
        Pmin = (1347, 'Pa'),
        Pmax = (2466, 'Pa'),
    ),
    reference = Article(
        authors = ["Blake, A.R.", "Kutschke, K.O."],
        title = u'The reaction of methyl radicals with formaldehyde',
        journal = "Can. J. Chem.",
        volume = "37",
        pages = """1462""",
        year = "1959",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1959BLA/KUT1462:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
Bath gas: (tert-C4H9O)2
Excitation technique: Thermal
Analytical technique: Laser schlieren
""",
)

entry(
    index = 497,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.5e+16, 's^-1'),
        n = 0,
        Ea = (162.132, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (376, 'K'),
        Tmax = (418, 'K'),
        Pmin = (1347, 'Pa'),
        Pmax = (2466, 'Pa'),
    ),
    reference = Article(
        authors = ["Blake, A.R.", "Kutschke, K.O."],
        title = u'The reaction of methyl radicals with formaldehyde',
        journal = "Can. J. Chem.",
        volume = "37",
        pages = """1462""",
        year = "1957",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1957BLA/KUT1462:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
Bath gas: (tert-C4H9O)2
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 498,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.95e+17, 's^-1'),
        n = 0,
        Ea = (159.638, 'kJ/mol'),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1957BIR/DAN154-164:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
Bath gas: (tert-C4H9O)2
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 499,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4e+16, 's^-1'),
        n = 0,
        Ea = (162.964, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (403, 'K'),
        Tmax = (428, 'K'),
    ),
    reference = Article(
        authors = ["Pritchard, G.O.", "Pritchard, H.O.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of methyl radicals with acetone, diethyl ketone, and di-tert.-butyl peroxide',
        journal = "J. Chem. Soc.",
        pages = """1425""",
        year = "1954",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1954PRI/PRI1425:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
Bath gas: (tert-C4H9O)2
Excitation technique: Thermal
Analytical technique: Other (direct)
Note: Invalid activation energy uncertainty (8314.472) found and ignored
""",
)

entry(
    index = 500,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7e+15, 's^-1'),
        n = 0,
        Ea = (158.806, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (553, 'K'),
        Tmax = (623, 'K'),
        Pmin = (733, 'Pa'),
        Pmax = (1667, 'Pa'),
    ),
    reference = Article(
        authors = ["Lossing, F.P.", "Tickner, A.W."],
        title = u'Free radicals by mass spectrometry. I. The measurement of methyl radical concentrations',
        journal = "J. Chem. Phys.",
        volume = "20",
        pages = """907-914""",
        year = "1952",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1952LOS/TIC907-914:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
Bath gas: He
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 501,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.87e+16, 's^-1'),
        n = 0,
        Ea = (157.975, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (399, 'K'),
        Tmax = (448, 'K'),
        Pmin = (13300, 'Pa'),
        Pmax = (40000, 'Pa'),
    ),
    reference = Article(
        authors = ["Jaquiss, M.T.", "Robert, J.S.", "Szwarc, M."],
        title = u'The reactions of methyl radicals with acetone',
        journal = "J. Am. Chem. Soc.",
        volume = "74",
        pages = """6005""",
        year = "1952",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1952JAQ/ROB6005:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
Bath gas: (tert-C4H9O)2
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 502,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.56e+15, 's^-1', '*|/', 10),
        n = 0,
        Ea = (157.144, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (402, 'K'),
        Tmax = (439, 'K'),
        Pmin = (2080, 'Pa'),
        Pmax = (3653, 'Pa'),
    ),
    reference = Article(
        authors = ["Brinton, R.K.", "Volman, D.H."],
        title = u'Decomposition of di-t-butyl peroxide and kinetics of the gas phase reaction of t-butoxy radicals in the presence of ethylenimine',
        journal = "J. Chem. Phys.",
        volume = "20",
        pages = """25""",
        year = "1952",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1952BRI/VOL25:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
Uncertainty: 10.0
Bath gas: (tert-C4H9O)2
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 503,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.5e+14, 's^-1', '+|-', 1.5e+14),
        n = 0,
        Ea = (150.492, 'kJ/mol', '+|-', 4.515),
        T0 = (1, 'K'),
        Tmin = (393, 'K'),
        Tmax = (553, 'K'),
        Pmin = (13300, 'Pa'),
        Pmax = (40000, 'Pa'),
    ),
    reference = Article(
        authors = ["Murawski, J.", "Roberts, J.S.", "Szwarc, M."],
        title = u'Kinetics of the thermal decomposition of di-t-butyl peroxide',
        journal = "J. Chem. Phys.",
        volume = "19",
        pages = """698""",
        year = "1951",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1951MUR/ROB698:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
Bath gas: Toluene
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 504,
    label = "C8H18O2 <=> C4H9O + C4H9O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.2e+16, 's^-1'),
        n = 0,
        Ea = (163.795, 'kJ/mol', '+|-', 1.638),
        T0 = (1, 'K'),
        Tmin = (413, 'K'),
        Tmax = (433, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (50700, 'Pa'),
    ),
    reference = Article(
        authors = ["Raley, J.H.", "Rust, F.F.", "Vaughan, W.E."],
        title = u'Decompositions of Di-t-alkyl peroxides. I. Kinetics',
        journal = "J. Am. Chem. Soc.",
        volume = "70",
        pages = """88-94""",
        year = "1948",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1948RAL/RUS88-94:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005412
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00005412/rk00000001.xml
Bath gas: (tert-C4H9O)2
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 505,
    label = "C10H10 <=> C9H7 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+16, 's^-1'),
        n = 0,
        Ea = (292.669, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1030, 'K'),
        Tmax = (1170, 'K'),
    ),
    reference = Article(
        authors = ["Robaugh, D.A.", "Stein, S.E."],
        title = u'Stabilities of highly conjugated radicals from bond homolysis rates',
        journal = "J. Am. Chem. Soc.",
        volume = "108",
        pages = """3224-3229""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986ROB/STE3224-3229:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00008918
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008918/rk00000001.xml
Bath gas: 1-Methylindene
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 506,
    label = "C10H20 <=> C4H9-3 + C6H11-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.04e+16, 's^-1', '*|/', 1.26),
        n = 0,
        Ea = (310.13, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1040, 'K'),
        Tmax = (1180, 'K'),
        Pmin = (54700, 'Pa'),
        Pmax = (167000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Thermal Decomposition of 3,4-Dimethylhexane, 2,2,3-Trimethylpentane, tert-Butylcyclohexane, and Related Hydrocarbons',
        journal = "J. Phys. Chem.",
        volume = "76",
        pages = """143""",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972TSA143:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011946
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011946/rk00000001.xml
Uncertainty: 1.26
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 507,
    label = "C6H10O4 <=> C3H5O2-2 + C3H5O2-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.5e+14, 's^-1'),
        n = 0,
        Ea = (125.549, 'kJ/mol', '+|-', 2.511),
        T0 = (1, 'K'),
        Tmin = (373, 'K'),
        Tmax = (464, 'K'),
        Pmin = (1013, 'Pa'),
        Pmax = (2973, 'Pa'),
    ),
    reference = Article(
        authors = ["Rembaum, A.", "Szwarc, M."],
        title = u'O-O bond dissociation energies in propionyl and butyryl peroxides',
        journal = "J. Chem. Phys.",
        volume = "23",
        pages = """909-913""",
        year = "1955",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1955REM/SZW909-913:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011959
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011959/rk00000001.xml
Bath gas: Toluene
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 508,
    label = "C8H18O2-2 <=> C4H9O-2 + C4H9O-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.05e+16, 's^-1', '*|/', 3.1),
        n = 0,
        Ea = (160.469, 'kJ/mol', '+|-', 11.225),
        T0 = (1, 'K'),
        Tmin = (473, 'K'),
        Tmax = (513, 'K'),
        Pmin = (40000, 'Pa'),
        Pmax = (40000, 'Pa'),
    ),
    reference = Article(
        authors = ["Sahetchian, K.A.", "Rigny, R.", "Blin, N.", "Heiss, A."],
        title = u'Homogeneous decomposition of dialkylperoxides in oxygen',
        journal = "J. Chem. Soc. Faraday Trans. 2",
        volume = "83",
        pages = """2035""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987SAH/RIG2035:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00012502
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012502/rk00000001.xml
Uncertainty: 3.0999999
Bath gas: O2
Excitation technique: Thermal
Analytical technique: Electron spin resonance (ESR or EPR)
""",
)

entry(
    index = 509,
    label = "C8H18O2-3 <=> C4H9O-3 + C4H9O-3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.8e+15, 's^-1'),
        n = 0,
        Ea = (152.155, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (373, 'K'),
        Tmax = (413, 'K'),
    ),
    reference = Article(
        authors = ["Walker, R.F.", "Phillips, L."],
        title = u'The kinetics of disproportionation-combination reactions between the s-butoxy-radical and nitric oxide, and of the pyrolysis of the O-O bond in di-s-butyl peroxide in the gas phase',
        journal = "J. Chem. Soc. London A",
        pages = """2103-2106""",
        year = "1968",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1968WAL/PHI2103-2106:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016191
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016191/rk00000002.xml
Bath gas: Peroxide, bis(1-methylpropyl)
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 510,
    label = "C10H14O <=> C6H5O + C4H9-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+16, 's^-1'),
        n = 0,
        Ea = (274.378, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (940, 'K'),
        Tmax = (1100, 'K'),
        Pmin = (203000, 'Pa'),
        Pmax = (304000, 'Pa'),
    ),
    reference = Article(
        authors = ["Walker, J.A.", "Tsang, W."],
        title = u'Single-pulse shock tube studies on the thermal decomposition of n-butyl phenyl ether, n-pentylbenzene, and phenotole and the heat of formation of phenoxy and benzyl radicals',
        journal = "J. Phys. Chem.",
        volume = "94",
        pages = """3324""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990WAL/TSA3324:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00009389
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009389/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 511,
    label = "C8H14O4 <=> C4H7O2 + C4H7O2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.9e+14, 's^-1'),
        n = 0,
        Ea = (123.886, 'kJ/mol', '+|-', 2.478),
        T0 = (1, 'K'),
        Tmin = (370, 'K'),
        Tmax = (452, 'K'),
        Pmin = (1053, 'Pa'),
        Pmax = (2786, 'Pa'),
    ),
    reference = Article(
        authors = ["Rembaum, A.", "Szwarc, M."],
        title = u'O-O bond dissociation energies in propionyl and butyryl peroxides',
        journal = "J. Chem. Phys.",
        volume = "23",
        pages = """909-913""",
        year = "1955",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1955REM/SZW909-913:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011505
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011505/rk00000001.xml
Bath gas: Benzene
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 512,
    label = "C6H5-2 + C6H5-2 <=> C12H10",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.39e+07, 'm^3/(mol*s)', '+|-', 1.1e+06),
        n = 0,
        Ea = (0.466, 'kJ/mol', '+|-', 0.298),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (500, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (6666, 'Pa'),
    ),
    reference = Article(
        authors = ["Park, J.", "Lin, M.C."],
        title = u'Kinetics for the recombination of phenyl radicals',
        journal = "J. Phys. Chem. A",
        volume = "101",
        pages = """14-18""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997PAR/LIN14-18:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011156
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011156/rk00000002.xml
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 513,
    label = "C10H22O2 <=> C5H11O + C5H11O",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+15, 's^-1', '*|/', 5),
        n = 0,
        Ea = (152.155, 'kJ/mol', '+|-', 4.573),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (650, 'K'),
    ),
    reference = Article(
        authors = ["Perona, M.J.", "Golden, D.M."],
        title = u'Very Low-Pressure Pyrolysis. VIII. The Decomposition of Di-t-Amyl Peroxide',
        journal = "Int. J. Chem. Kinet.",
        volume = "5",
        pages = """55""",
        year = "1973",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1973PER/GOL55:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00014912
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00014912/rk00000001.xml
Uncertainty: 5.0
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 514,
    label = "C13H12 <=> C13H11 + H",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2e+15, 's^-1'),
        n = 0,
        Ea = (340.893, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1250, 'K'),
    ),
    reference = Article(
        authors = ["Rossi, M.J.", "McMillen, D.F.", "Golden, D.M."],
        title = u'Aliphatic C-H bond scission processes in diphenylmethane and 2-benzyl- and 4-benzylpyridine. The head of formation of the diphenylmethyl and \u03b1-phenylethyl radical in the gas phase',
        journal = "J. Phys. Chem.",
        volume = "88",
        pages = """5031""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984ROS/MCM5031:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00004452
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004452/rk00000001.xml
Bath gas: Diphenylmethane
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 515,
    label = "C12H10O <=> C6H5O + C6H5-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.16e+15, 's^-1'),
        n = 0,
        Ea = (316.781, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1050, 'K'),
        Tmax = (1200, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["van Scheppingen, W.", "Dorrestijn, E.", "Arends, I.", "Mulder, P.", "Korth, H-G."],
        title = u'Carbon-oxygen bond strength in diphenyl ether and phenyl vinyl ether: an experimental and computational study',
        journal = "J. Phys. Chem. A",
        volume = "101",
        pages = """5404-5411""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997VAN/DOR5404-5411:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00004456
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004456/rk00000001.xml
Bath gas: H2
Excitation technique: Thermal
Time resolution: In real time
Analytical technique: Gas chromatography
""",
)

entry(
    index = 516,
    label = "C13H10O <=> C7H5O + C6H5-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.6e+16, 's^-1'),
        n = 0,
        Ea = (365.837, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1080, 'K'),
        Tmax = (1150, 'K'),
        Pmin = (1733, 'Pa'),
        Pmax = (1733, 'Pa'),
    ),
    reference = Article(
        authors = ["Clark, D.", "Pritchard, H.O."],
        title = u'Arrhenius parameters of some reactions involving multiplicity changes',
        journal = "J. Chem. Soc. London",
        pages = """2136-2140""",
        year = "1956",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1956CLA/PRI2136-2140:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005988
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00005988/rk00000001.xml
Bath gas: Toluene
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

entry(
    index = 517,
    label = "C14H14 <=> C13H11 + CH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+15, 's^-1'),
        n = 0,
        Ea = (282.692, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1070, 'K'),
    ),
    reference = Article(
        authors = ["Robaugh, D.A.", "Stein, S.E."],
        title = u'Stabilities of highly conjugated radicals from bond homolysis rates',
        journal = "J. Am. Chem. Soc.",
        volume = "108",
        pages = """3224-3229""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986ROB/STE3224-3229:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00008133
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008133/rk00000001.xml
Bath gas: 2,2'-Diphenylpropane
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 518,
    label = "C15H16 <=> C14H13 + CH3",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5.01e+15, 's^-1'),
        n = 0,
        Ea = (275.209, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (950, 'K'),
        Tmax = (1050, 'K'),
    ),
    reference = Article(
        authors = ["Robaugh, D.A.", "Stein, S.E."],
        title = u'Stabilities of highly conjugated radicals from bond homolysis rates',
        journal = "J. Am. Chem. Soc.",
        volume = "108",
        pages = """3224-3229""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986ROB/STE3224-3229:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00008930
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008930/rk00000001.xml
Bath gas: 1,1'-Diphenylethane
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
)

entry(
    index = 519,
    label = "C20H30 <=> C10H15 + C10H15",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.48e+13, 's^-1', '*|/', 5),
        n = 0,
        Ea = (116.403, 'kJ/mol', '+|-', 3.5),
        T0 = (1, 'K'),
        Tmin = (70, 'K'),
        Tmax = (102, 'K'),
        Pmin = (133, 'Pa'),
        Pmax = (7999, 'Pa'),
    ),
    reference = Article(
        authors = ["Roth, W.R.", "Hunold, F."],
        title = u'Bildungsenthalpie und Stabilisierungsenergie des Pentamethylcyclopentadienyl-Radikals',
        journal = "Liebigs Ann.",
        pages = """1119-1122""",
        year = "1995",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1995ROT/HUN1119-1122:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016760
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016760/rk00000001.xml
Uncertainty: 5.0
Bath gas: O2
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
)

