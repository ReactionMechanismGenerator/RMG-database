#!/usr/bin/env python
# encoding: utf-8

name = "Silylene_to_Silene/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "H3SiSiH <=> Si2H4",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (7.9E12, '1/s'),
        n = 0,
        Ea = (5.3095, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    reference = Article(
        authors = ["Dollet, A.", "de Persis, S."],
        title = "Pressure-dependent rate coefficients of chemical reactions involving Si2H4 isomerization from QRRK calculations",
        journal = "J. Anal. Apply. Pyrolysis",
        pages = """460-470""",
        year = "2007",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2007DOL/DEP460-470:1",
    ),
    longDesc = 
u"""
QRRK calculations for the Si2H4 isomerization. This is the high P limit. Rate parameters are corroborated in J. Phys. Chem. 91, 5765 (1987).""",
)

entry(
    index = 2,
    label = "Si2H5SiH <=> SiH3Si2H4",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.0E12, '1/s'),
        n = 0,
        Ea = (8.1, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Adamczyk, A.J.", "Reyniers, M.", "Marin, G.B.", "Broadbelt, L.J."],
        title = "Exploring 1,2-hydrogen shift in silicon nanoparticles: Reaction kinetics from quantum chemical calculations and derivation of transition state group additivity database",
        journal = "J. Phys. Chem. A",
        pages = """10933-10946""",
        year = "2009",
    ),
    longDesc = 
u"""
Calculations were performed with G3//B3LYP and exhibit two barriers (a stable intermediate is formed). Rates assume the second step is rate limiting, after validation of three models (full, 1st step rate limiting, 2nd step rate limiting). This assumption is considered valid under 1385 K.""",
)

entry(
    index = 3,
    label = "iSi3H7SiH <=> iSi2H6Si2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.16E12, '1/s'),
        n = 0,
        Ea = (9.0, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Adamczyk, A.J.", "Reyniers, M.", "Marin, G.B.", "Broadbelt, L.J."],
        title = "Exploring 1,2-hydrogen shift in silicon nanoparticles: Reaction kinetics from quantum chemical calculations and derivation of transition state group additivity database",
        journal = "J. Phys. Chem. A",
        pages = """10933-10946""",
        year = "2009",
    ),
    longDesc = 
u"""
Calculations were performed with G3//B3LYP and exhibit two barriers (a stable intermediate is formed). Rates assume the second step is rate limiting, after validation of three models (full, 1st step rate limiting, 2nd step rate limiting). This assumption is considered valid under 1385 K.""",
)

entry(
    index = 4,
    label = "H3SiSiSiH3 <=> SiH3Si2H4",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (5.01E12, '1/s'),
        n = 0,
        Ea = (4.7, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Adamczyk, A.J.", "Reyniers, M.", "Marin, G.B.", "Broadbelt, L.J."],
        title = "Exploring 1,2-hydrogen shift in silicon nanoparticles: Reaction kinetics from quantum chemical calculations and derivation of transition state group additivity database",
        journal = "J. Phys. Chem. A",
        pages = """10933-10946""",
        year = "2009",
    ),
    longDesc = 
u"""
Calculations were performed with G3//B3LYP and exhibit two barriers (a stable intermediate is formed). Rates assume the second step is rate limiting, after validation of three models (full, 1st step rate limiting, 2nd step rate limiting). This assumption is considered valid under 1385 K.""",
)

entry(
    index = 5,
    label = "iSi3H7SiSiH3 <=> iSi2H6Si2HSiH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58E12, '1/s'),
        n = 0,
        Ea = (6.1, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Adamczyk, A.J.", "Reyniers, M.", "Marin, G.B.", "Broadbelt, L.J."],
        title = "Exploring 1,2-hydrogen shift in silicon nanoparticles: Reaction kinetics from quantum chemical calculations and derivation of transition state group additivity database",
        journal = "J. Phys. Chem. A",
        pages = """10933-10946""",
        year = "2009",
    ),
    longDesc = 
u"""
Calculations were performed with G3//B3LYP and exhibit two barriers (a stable intermediate is formed). Rates assume the second step is rate limiting, after validation of three models (full, 1st step rate limiting, 2nd step rate limiting). This assumption is considered valid under 1385 K.""",
)

entry(
    index = 6,
    label = "SiH3SiSi2H5 <=> SiH3Si2H2SiH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.02E12, '1/s'),
        n = 0,
        Ea = (5.5, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Adamczyk, A.J.", "Reyniers, M.", "Marin, G.B.", "Broadbelt, L.J."],
        title = "Exploring 1,2-hydrogen shift in silicon nanoparticles: Reaction kinetics from quantum chemical calculations and derivation of transition state group additivity database",
        journal = "J. Phys. Chem. A",
        pages = """10933-10946""",
        year = "2009",
    ),
    longDesc = 
u"""
Calculations were performed with G3//B3LYP and exhibit two barriers (a stable intermediate is formed). Rates assume the second step is rate limiting, after validation of three models (full, 1st step rate limiting, 2nd step rate limiting). This assumption is considered valid under 1385 K.""",
)

entry(
    index = 7,
    label = "Si4H9SiH <=> Si3H7Si2H3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.0E14, '1/s'),
        n = 0,
        Ea = (8.0, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Adamczyk, A.J.", "Reyniers, M.", "Marin, G.B.", "Broadbelt, L.J."],
        title = "Exploring 1,2-hydrogen shift in silicon nanoparticles: Reaction kinetics from quantum chemical calculations and derivation of transition state group additivity database",
        journal = "J. Phys. Chem. A",
        pages = """10933-10946""",
        year = "2009",
    ),
    longDesc = 
u"""
Calculations were performed with G3//B3LYP and exhibit two barriers (a stable intermediate is formed). Rates assume the second step is rate limiting, after validation of three models (full, 1st step rate limiting, 2nd step rate limiting). This assumption is considered valid under 1385 K.""",
)

entry(
    index = 8,
    label = "Si3H7SiSiH3 <=> Si2H5Si2H2SiH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.58E15, '1/s'),
        n = 0,
        Ea = (5.4, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Adamczyk, A.J.", "Reyniers, M.", "Marin, G.B.", "Broadbelt, L.J."],
        title = "Exploring 1,2-hydrogen shift in silicon nanoparticles: Reaction kinetics from quantum chemical calculations and derivation of transition state group additivity database",
        journal = "J. Phys. Chem. A",
        pages = """10933-10946""",
        year = "2009",
    ),
    longDesc = 
u"""
Calculations were performed with G3//B3LYP and exhibit two barriers (a stable intermediate is formed). Rates assume the second step is rate limiting, after validation of three models (full, 1st step rate limiting, 2nd step rate limiting). This assumption is considered valid under 1385 K.""",
)

entry(
    index = 9,
    label = "iSi3H7SiSi2H5-1 <=> iSi2H6Si2HSi2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.0E7, '1/s'),
        n = 0,
        Ea = (7.3, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Adamczyk, A.J.", "Reyniers, M.", "Marin, G.B.", "Broadbelt, L.J."],
        title = "Exploring 1,2-hydrogen shift in silicon nanoparticles: Reaction kinetics from quantum chemical calculations and derivation of transition state group additivity database",
        journal = "J. Phys. Chem. A",
        pages = """10933-10946""",
        year = "2009",
    ),
    longDesc = 
u"""
Calculations were performed with G3//B3LYP and exhibit two barriers (a stable intermediate is formed). Rates assume the second step is rate limiting, after validation of three models (full, 1st step rate limiting, 2nd step rate limiting). This assumption is considered valid under 1385 K.""",
)

entry(
    index = 10,
    label = "iSi3H7SiSi2H5-2 <=> iSi3H7Si2H2SiH3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.58E7, '1/s'),
        n = 0,
        Ea = (7.2, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Adamczyk, A.J.", "Reyniers, M.", "Marin, G.B.", "Broadbelt, L.J."],
        title = "Exploring 1,2-hydrogen shift in silicon nanoparticles: Reaction kinetics from quantum chemical calculations and derivation of transition state group additivity database",
        journal = "J. Phys. Chem. A",
        pages = """10933-10946""",
        year = "2009",
    ),
    longDesc = 
u"""
Calculations were performed with G3//B3LYP and exhibit two barriers (a stable intermediate is formed). Rates assume the second step is rate limiting, after validation of three models (full, 1st step rate limiting, 2nd step rate limiting). This assumption is considered valid under 1385 K.""",
)

