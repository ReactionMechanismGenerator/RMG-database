#!/usr/bin/env python
# encoding: utf-8

name = "Silylene_Insertion/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "SiH2 + H2 <=> SiH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.05E6, 'cm^3/(mol*s)'),
        n = 1.97,
        Ea = (-1.9, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (400, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    reference = Article(
        authors = ["Walch, S.P.", "Dateo, C.E."],
        title = "Thermal decomposition pathways and rates for silane, chlorosilane, dichlorosilane, and trichlorosilane",
        journal = "J. Phys. Chem. A",
        pages = """2015-2022""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001WAL/DAT2015-2022:2",
    ),
    longDesc = 
u"""
Calculations using CASSCF/cc-pVDZ for geometries and vibrational frequencies. Energies of reactats, products and TS computed with CCSD(T)/aug-cc-pVTZ extrapolated to complete basis set using MP2/aug-cc-pVnZ(n=2,3,4). Rate founded with conventional TST. Error in barrier at most 2 kcal/mol, likely about 1 kcal/mol.
""",
)

entry(
    index = 2,
    label = "SiH2 + SiH4 <=> Si2H6",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.80E10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-7.9, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Adamczyk, A.J.", "Reyniers, M.", "Marin, G.", "Broadbelt, L.J."],
        title = "Kinetics of substituted silylene addition and elimination in silicon nanocluster growth captured by group additivity",
        journal = "ChemPhysChem",
        pages = """1978-1994""",
        year = "2010",
    ),
    longDesc = 
u"""
Rates were calculated using G3//B3LYP and are corrected for internal rotations. The insertion of silylenes into silanes exhibits formation of a stable adduct. Calculations assume that the first step is equilibrated.
""",
)

entry(
    index = 3,
    label = "SiH2 + Si2H6 <=> Si3H8-1",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1.86E14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1.9, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (295, 'K'),
        Tmax = (595, 'K'),
	),
    reference = Article(
        authors = ["Becerra, R.", "Frey, H.M.", "Mason, B.P.", "Walsh, R."],
        title = "Time-resolved gas-phase kinetic studies of the reactions of silylene with disilane and trisilane",
        journal = "J. Organometal. Chem.",
        pages = """343-349""",
        year = "1996",
    ),
    rank = 1,
    longDesc = 
u"""
Laser flash photolysis was used to measure rates and fit to Arrhenius form. Error in logA +/- 0.04 and error in Ea +/- 0.3 kJ/mol. Authors note the Arrhenius plot is slightly curved.
""",
)

entry(
    index = 4,
    label = "SiH2 + Si3H8-1 <=> nSi4H10",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.24E14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-2.0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (295, 'K'),
        Tmax = (595, 'K'),
	),
    rank = 1,
    reference = Article(
        authors = ["Becerra, R.", "Frey, H.M.", "Mason, B.P.", "Walsh, R."],
        title = "Time-resolved gas-phase kinetic studies of the reactions of silylene with disilane and trisilane",
        journal = "J. Organometal. Chem.",
        pages = """343-349""",
        year = "1996",
    ),
    longDesc = 
u"""
Laser flash photolysis was used to measure rates and fit to Arrhenius form. Error in logA +/- 0.06 and error in Ea +/- 0.4 kJ/mol. Authors note the Arrhenius plot is slightly curved.
""",
)

entry(
    index = 5,
    label = "H3SiSiH + SiH4 <=> Si3H8-1",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.40E10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-9.1, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Adamczyk, A.J.", "Reyniers, M.", "Marin, G.", "Broadbelt, L.J."],
        title = "Kinetics of substituted silylene addition and elimination in silicon nanocluster growth captured by group additivity",
        journal = "ChemPhysChem",
        pages = """1978-1994""",
        year = "2010",
    ),
    longDesc = 
u"""
Rates were calculated using G3//B3LYP and are corrected for internal rotations. The insertion of silylenes into silanes exhibits formation of a stable adduct. Calculations assume that the first step is equilibrated.
""",
)

entry(
    index = 6,
    label = "SiH2 + Si3H8-2 <=> iSi4H10",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.90E11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-11.6, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Adamczyk, A.J.", "Reyniers, M.", "Marin, G.", "Broadbelt, L.J."],
        title = "Kinetics of substituted silylene addition and elimination in silicon nanocluster growth captured by group additivity",
        journal = "ChemPhysChem",
        pages = """1978-1994""",
        year = "2010",
    ),
    longDesc = 
u"""
Rates were calculated using G3//B3LYP and are corrected for internal rotations. The insertion of silylenes into silanes exhibits formation of a stable adduct. Calculations assume that the first step is equilibrated.
""",
)

entry(
    index = 7,
    label = "H3SiSiSiH3 + SiH4 <=> iSi4H10",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.90E10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-10.4, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Adamczyk, A.J.", "Reyniers, M.", "Marin, G.", "Broadbelt, L.J."],
        title = "Kinetics of substituted silylene addition and elimination in silicon nanocluster growth captured by group additivity",
        journal = "ChemPhysChem",
        pages = """1978-1994""",
        year = "2010",
    ),
    longDesc = 
u"""
Rates were calculated using G3//B3LYP and are corrected for internal rotations. The insertion of silylenes into silanes exhibits formation of a stable adduct. Calculations assume that the first step is equilibrated.
""",
)

entry(
    index = 8,
    label = "SiH2 + iSi4H10 <=> tSi5H12",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.40E11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-12.4, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Adamczyk, A.J.", "Reyniers, M.", "Marin, G.", "Broadbelt, L.J."],
        title = "Kinetics of substituted silylene addition and elimination in silicon nanocluster growth captured by group additivity",
        journal = "ChemPhysChem",
        pages = """1978-1994""",
        year = "2010",
    ),
    longDesc = 
u"""
Rates were calculated using G3//B3LYP and are corrected for internal rotations. The insertion of silylenes into silanes exhibits formation of a stable adduct. Calculations assume that the first step is equilibrated.
""",
)

entry(
    index = 9,
    label = "Si2H5SiH + SiH4 <=> nSi4H10",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.80E10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-8.5, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Adamczyk, A.J.", "Reyniers, M.", "Marin, G.", "Broadbelt, L.J."],
        title = "Kinetics of substituted silylene addition and elimination in silicon nanocluster growth captured by group additivity",
        journal = "ChemPhysChem",
        pages = """1978-1994""",
        year = "2010",
    ),
    longDesc = 
u"""
Rates were calculated using G3//B3LYP and are corrected for internal rotations. The insertion of silylenes into silanes exhibits formation of a stable adduct. Calculations assume that the first step is equilibrated.
""",
)

entry(
    index = 10,
    label = "Si4H9SiH + SiH4 <=> nSi6H14",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.80E10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-10.8, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Adamczyk, A.J.", "Reyniers, M.", "Marin, G.", "Broadbelt, L.J."],
        title = "Kinetics of substituted silylene addition and elimination in silicon nanocluster growth captured by group additivity",
        journal = "ChemPhysChem",
        pages = """1978-1994""",
        year = "2010",
    ),
    longDesc = 
u"""
Rates were calculated using G3//B3LYP and are corrected for internal rotations. The insertion of silylenes into silanes exhibits formation of a stable adduct. Calculations assume that the first step is equilibrated.
""",
)

entry(
    index = 11,
    label = "SiH2 + nSi5H12 <=> nSi6H14",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (3.02E11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-10.8, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Adamczyk, A.J.", "Reyniers, M.", "Marin, G.", "Broadbelt, L.J."],
        title = "Kinetics of substituted silylene addition and elimination in silicon nanocluster growth captured by group additivity",
        journal = "ChemPhysChem",
        pages = """1978-1994""",
        year = "2010",
    ),
    longDesc = 
u"""
Rates were calculated using G3//B3LYP and are corrected for internal rotations. The insertion of silylenes into silanes exhibits formation of a stable adduct. Calculations assume that the first step is equilibrated.
""",
)

entry(
    index = 12,
    label = "H3SiSiH + H2 <=> Si2H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.80E12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0.8, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Adamczyk, A.J.", "Reyniers, M.", "Marin, G.", "Broadbelt, L.J."],
        title = "Kinetic correlations for H2 addition and elimination reaction mechanisms during silicon hydride pyrolysis",
        journal = "Phys. Chem. Chem. Phys.",
        pages = """12676-12696""",
        year = "2010",
    ),
    longDesc = 
u"""
Rates were calculated using G3//B3LYP. In most cases, the insertion of silylenes into H2 exhibits formation of a stable adduct. Calculations assume that the first step is equilibrated.
""",
)

entry(
    index = 13,
    label = "Si2H5SiH + H2 <=> Si3H8-1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02E12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2.1, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Adamczyk, A.J.", "Reyniers, M.", "Marin, G.", "Broadbelt, L.J."],
        title = "Kinetic correlations for H2 addition and elimination reaction mechanisms during silicon hydride pyrolysis",
        journal = "Phys. Chem. Chem. Phys.",
        pages = """12676-12696""",
        year = "2010",
    ),
    longDesc = 
u"""
Rates were calculated using G3//B3LYP. In most cases, the insertion of silylenes into H2 exhibits formation of a stable adduct. Calculations assume that the first step is equilibrated.
""",
)

entry(
    index = 14,
    label = "H3SiSiSiH3 + H2 <=> Si3H8-1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.20E13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.5, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Adamczyk, A.J.", "Reyniers, M.", "Marin, G.", "Broadbelt, L.J."],
        title = "Kinetic correlations for H2 addition and elimination reaction mechanisms during silicon hydride pyrolysis",
        journal = "Phys. Chem. Chem. Phys.",
        pages = """12676-12696""",
        year = "2010",
    ),
    longDesc = 
u"""
Rates were calculated using G3//B3LYP. In most cases, the insertion of silylenes into H2 exhibits formation of a stable adduct. Calculations assume that the first step is equilibrated.
""",
)

entry(
    index = 15,
    label = "Si2H5SiSi2H5 + H2 <=> nSi5H12",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.54E12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1.5, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Adamczyk, A.J.", "Reyniers, M.", "Marin, G.", "Broadbelt, L.J."],
        title = "Kinetic correlations for H2 addition and elimination reaction mechanisms during silicon hydride pyrolysis",
        journal = "Phys. Chem. Chem. Phys.",
        pages = """12676-12696""",
        year = "2010",
    ),
    longDesc = 
u"""
Rates were calculated using G3//B3LYP. In most cases, the insertion of silylenes into H2 exhibits formation of a stable adduct. Calculations assume that the first step is equilibrated.
""",
)

entry(
    index = 16,
    label = "Si2H5SiSi2H5 + H2 <=> nSi5H12",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.54E12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1.5, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Adamczyk, A.J.", "Reyniers, M.", "Marin, G.", "Broadbelt, L.J."],
        title = "Kinetic correlations for H2 addition and elimination reaction mechanisms during silicon hydride pyrolysis",
        journal = "Phys. Chem. Chem. Phys.",
        pages = """12676-12696""",
        year = "2010",
    ),
    longDesc = 
u"""
Rates were calculated using G3//B3LYP. In most cases, the insertion of silylenes into H2 exhibits formation of a stable adduct. Calculations assume that the first step is equilibrated.
""",
)

entry(
    index = 17,
    label = "iSi3H7SiSiH3 + H2 <=> iSi5H12",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02E12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1.5, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Adamczyk, A.J.", "Reyniers, M.", "Marin, G.", "Broadbelt, L.J."],
        title = "Kinetic correlations for H2 addition and elimination reaction mechanisms during silicon hydride pyrolysis",
        journal = "Phys. Chem. Chem. Phys.",
        pages = """12676-12696""",
        year = "2010",
    ),
    longDesc = 
u"""
Rates were calculated using G3//B3LYP. In most cases, the insertion of silylenes into H2 exhibits formation of a stable adduct. Calculations assume that the first step is equilibrated.
""",
)

entry(
    index = 18,
    label = "Si4H9SiH + H2 <=> nSi5H12",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.20E13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2.0, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Adamczyk, A.J.", "Reyniers, M.", "Marin, G.", "Broadbelt, L.J."],
        title = "Kinetic correlations for H2 addition and elimination reaction mechanisms during silicon hydride pyrolysis",
        journal = "Phys. Chem. Chem. Phys.",
        pages = """12676-12696""",
        year = "2010",
    ),
    longDesc = 
u"""
Rates were calculated using G3//B3LYP. In most cases, the insertion of silylenes into H2 exhibits formation of a stable adduct. Calculations assume that the first step is equilibrated.
""",
)

