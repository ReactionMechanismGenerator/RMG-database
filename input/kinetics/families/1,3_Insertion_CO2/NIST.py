#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_CO2/NIST"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    label = "2005SAI/SHI5352-5357:5",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,D} {4,S}
2 *1 O 0 {1,S} {5,S}
3    O 0 {1,D}
4 *4 H 0 {1,S}
5 *3 H 0 {2,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D} {3,D}
2 *1 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1 *3 H 0 {2,S}
2 *4 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.6e+08,"s^-1"),
        n = 0,
        Ea = (181.167,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (1350,"K"),
        Tmax = (1700,"K"),
        Pmin = (121590,"Pa"),
        Pmax = (243180,"Pa"),
    ),
    reference = Article(
        authors = ["Saito, K.", "Shiose, T.", "Takahashi, O.", "Hidaka, Y.", "Aiba, F.", "Tabayashi, F."],
        title = u'Unimolecular decomposition of formic acid in the gas phase - On the ratio of the competing reaction channels',
        journal = "J. Phys. Chem. A",
        volume = "109",
        pages = """5352-5357""",
        year = "2005",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2005SAI/SHI5352-5357:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00001636
Pressure dependence: Rate constant is pressure dependent
Experimental procedure: Shock tube
Excitation technique: Thermal
Time resolution: In both real time and by end product analysis
Analytical technique: Other (IR)

Formic acid was produced via thermal (shock induced) dissociation of the dimer. Reaction of the monomer was followed by monitoring CO formation in real time via IR emission at 4.63 um and CO2 formation at 4.23 um. CO2 formation was more difficult to follow as it was produced in only about 2 to 8% of the CO. CO, CO2, and H2products were also determined via GC analysis.

The precise temperature range is not reported in the paper. The listed values are approximate and were derived from the Arrhenius plots given in Figure 4 of the paper.
""",
    history = [
        ("Fri Jul 13 08:14:02 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2005SAI/SHI5352-5357:5"""),
        ("Wed Jul 18 12:58:00 2012","Sean Troiano <stroiano7@gmail.com>","action","""Fixed pressure range according to http://pubs.acs.org/doi/abs/10.1021/jp045072h"""),
    ],
)

entry(
    index = 2,
    label = "2005SAI/SHI5352-5357:4",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,D} {4,S}
2 *1 O 0 {1,S} {5,S}
3    O 0 {1,D}
4 *4 H 0 {1,S}
5 *3 H 0 {2,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D} {3,D}
2 *1 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1 *3 H 0 {2,S}
2 *4 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.02e+09,"s^-1"),
        n = 0,
        Ea = (203.342,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (1350,"K"),
        Tmax = (1600,"K"),
        Pmin = (121590,"Pa"),
        Pmax = (243180,"Pa"),
    ),
    reference = Article(
        authors = ["Saito, K.", "Shiose, T.", "Takahashi, O.", "Hidaka, Y.", "Aiba, F.", "Tabayashi, F."],
        title = u'Unimolecular decomposition of formic acid in the gas phase - On the ratio of the competing reaction channels',
        journal = "J. Phys. Chem. A",
        volume = "109",
        pages = """5352-5357""",
        year = "2005",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2005SAI/SHI5352-5357:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00001636
Pressure dependence: Rate constant is pressure dependent
Experimental procedure: Shock tube
Excitation technique: Thermal
Time resolution: In both real time and by end product analysis
Analytical technique: Other (IR)

Formic acid was produced via thermal (shock induced) dissociation of the dimer. Reaction of the monomer was followed by monitoring CO formation in real time via IR emission at 4.63 um and CO2 formation at 4.23 um. CO2 formation was more difficult to follow as it was produced in only about 2 to 8% of the CO. CO, CO2, and H2 products were also determined via GC analysis.

The precise temperature range is not reported in the paper. The listed values are approximate and were derived from the Arrhenius plots given in Figure 4 of the paper.
""",
    history = [
        ("Fri Jul 13 08:14:02 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2005SAI/SHI5352-5357:4"""),
        ("Wed Jul 18 12:58:00 2012","Sean Troiano <stroiano7@gmail.com>","action","""Fixed pressure range according to http://pubs.acs.org/doi/abs/10.1021/jp045072h"""),
    ],
)

entry(
    index = 3,
    label = "1971BLA/DAV1923:1",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,D} {4,S}
2 *1 O 0 {1,S} {5,S}
3    O 0 {1,D}
4 *4 H 0 {1,S}
5 *3 H 0 {2,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D} {3,D}
2 *1 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1 *3 H 0 {2,S}
2 *4 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.95e+09,"s^-1"),
        n = 0,
        Ea = (202.873,"kJ/mol","+|-",6.086),
        T0 = (1,"K"),
        Tmin = (730,"K"),
        Tmax = (1050,"K"),
        Pmin = (2666,"Pa"),
        Pmax = (40000,"Pa"),
    ),
    reference = Article(
        authors = ["Blake, P.G.", "Davies, H.H.", "Jackson, G.E."],
        title = u'Dehydration Mechanisms in the Thermal Decomposition of Gaseous Formic Acid',
        journal = "J. Chem. Soc. B",
        volume = "10",
        pages = """1923""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971BLA/DAV1923:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00001636
Bath gas: HCOOH
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 08:14:02 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1971BLA/DAV1923:1"""),
    ],
)

entry(
    index = 4,
    label = "1960BLA/HIN444-455:1",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,D} {4,S}
2 *1 O 0 {1,S} {5,S}
3    O 0 {1,D}
4 *4 H 0 {1,S}
5 *3 H 0 {2,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D} {3,D}
2 *1 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1 *3 H 0 {2,S}
2 *4 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (63100,"s^-1"),
        n = 0,
        Ea = (128.043,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (709,"K"),
        Tmax = (805,"K"),
        Pmin = (400,"Pa"),
        Pmax = (86700,"Pa"),
    ),
    reference = Article(
        authors = ["Blake, P.G.", "Hinshelwood, C."],
        title = u'The homogeneous decomposition reactions of gaseous formic acid',
        journal = "Proc. R. Soc. London A",
        volume = "255",
        pages = """444-455""",
        year = "1960",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1960BLA/HIN444-455:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00001636
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00001636/rk00000001.xml
Bath gas: HCOOH
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
    history = [
        ("Fri Jul 13 08:14:02 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1960BLA/HIN444-455:1"""),
    ],
)

entry(
    index = 5,
    label = "2007CHA/CHE6789-6797:3",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,D} {4,S}
2 *1 O 0 {1,S} {5,S}
3    O 0 {1,D}
4 *4 H 0 {1,S}
5 *3 H 0 {2,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D} {3,D}
2 *1 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1 *3 H 0 {2,S}
2 *4 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.46e+13,"s^-1"),
        n = 0,
        Ea = (285.516,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (500,"K"),
        Tmax = (2000,"K"),
    ),
    reference = Article(
        authors = ["Chang, J.G.", "Chen, H.T.", "Xu, S.C.", "Lin, M.C."],
        title = u'Computational study on the kinetics and mechanisms for the unimolecular decomposition of formic and oxalic Acids',
        journal = "J. Phys. Chem. A",
        volume = "111",
        pages = """6789-6797""",
        year = "2007",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2007CHA/CHE6789-6797:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00001636
Pressure dependence: Rate constant is high pressure limit

Reaction potential energy surface was studied using quantum chemistry and rate constants were calculated using RRKM .
""",
    history = [
        ("Fri Jul 13 08:14:02 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2007CHA/CHE6789-6797:3"""),
    ],
)

entry(
    index = 6,
    label = "1984MAC/DOO525:2",
    reactant1 = 
"""
1 *3 C 0 {2,S} {6,S} {7,S} {8,S}
2 *1 C 0 {1,S} {3,S} {4,D}
3 *2 O 0 {2,S} {5,S}
4    O 0 {2,D}
5 *4 H 0 {3,S}
6    H 0 {1,S}
7    H 0 {1,S}
8    H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,D}
2 *2 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1 *3 C 0 {2,S} {3,S} {4,S} {5,S}
2 *4 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.75e+12,"s^-1","*|/",1.86),
        n = 0,
        Ea = (295.164,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (1300,"K"),
        Tmax = (1950,"K"),
        Pmin = (101000,"Pa"),
        Pmax = (101000,"Pa"),
    ),
    reference = Article(
        authors = ["Mackie, J.C.", "Doolan, K.R."],
        title = u'High-temperature kinetics of thermal decomposition of acetic acid and its products',
        journal = "Int. J. Chem. Kinet.",
        volume = "16",
        pages = """525""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984MAC/DOO525:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00001645
Uncertainty: 1.86
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 08:14:07 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1984MAC/DOO525:2"""),
    ],
)

entry(
    index = 7,
    label = "1984MAC/DOO525:1",
    reactant1 = 
"""
1 *3 C 0 {2,S} {6,S} {7,S} {8,S}
2 *1 C 0 {1,S} {3,S} {4,D}
3 *2 O 0 {2,S} {5,S}
4    O 0 {2,D}
5 *4 H 0 {3,S}
6    H 0 {1,S}
7    H 0 {1,S}
8    H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,D}
2 *2 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1 *3 C 0 {2,S} {3,S} {4,S} {5,S}
2 *4 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.26e+13,"s^-1","*|/",2),
        n = 0,
        Ea = (304.31,"kJ/mol","+|-",15.215),
        T0 = (1,"K"),
        Tmin = (1300,"K"),
        Tmax = (1950,"K"),
        Pmin = (101000,"Pa"),
        Pmax = (101000,"Pa"),
    ),
    reference = Article(
        authors = ["Mackie, J.C.", "Doolan, K.R."],
        title = u'High-temperature kinetics of thermal decomposition of acetic acid and its products',
        journal = "Int. J. Chem. Kinet.",
        volume = "16",
        pages = """525""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984MAC/DOO525:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00001645
Uncertainty: 2.0
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 08:14:07 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1984MAC/DOO525:1"""),
    ],
)

entry(
    index = 8,
    label = "1969BLA/JAC94-96:1",
    reactant1 = 
"""
1 *3 C 0 {2,S} {6,S} {7,S} {8,S}
2 *1 C 0 {1,S} {3,S} {4,D}
3 *2 O 0 {2,S} {5,S}
4    O 0 {2,D}
5 *4 H 0 {3,S}
6    H 0 {1,S}
7    H 0 {1,S}
8    H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,D}
2 *2 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1 *3 C 0 {2,S} {3,S} {4,S} {5,S}
2 *4 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.89e+13,"s^-1","*|/",1.41),
        n = 0,
        Ea = (291.838,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (803,"K"),
        Tmax = (1040,"K"),
        Pmin = (933,"Pa"),
        Pmax = (21300,"Pa"),
    ),
    reference = Article(
        authors = ["Blake, P.G.", "Jackson, G.E."],
        title = u'High- and low-temperature mechanisms in the thermal decomposition of acetic acid',
        journal = "J. Chem. Soc. B",
        pages = """94-96""",
        year = "1969",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1969BLA/JAC94-96:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00001645
Uncertainty: 1.41
Bath gas: CH3C(O)OH
Excitation technique: Thermal
Analytical technique: Gas chromatography
Note: Invalid activation energy uncertainty (8314.472) found and ignored
""",
    history = [
        ("Fri Jul 13 08:14:07 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1969BLA/JAC94-96:1"""),
    ],
)

entry(
    index = 9,
    label = "1968BLA/JAC1153-1155:1",
    reactant1 = 
"""
1 *3 C 0 {2,S} {6,S} {7,S} {8,S}
2 *1 C 0 {1,S} {3,S} {4,D}
3 *2 O 0 {2,S} {5,S}
4    O 0 {2,D}
5 *4 H 0 {3,S}
6    H 0 {1,S}
7    H 0 {1,S}
8    H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,D}
2 *2 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1 *3 C 0 {2,S} {3,S} {4,S} {5,S}
2 *4 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.32e+11,"s^-1"),
        n = 0,
        Ea = (244.445,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (733,"K"),
        Tmax = (868,"K"),
        Pmin = (1333,"Pa"),
        Pmax = (53300,"Pa"),
    ),
    reference = Article(
        authors = ["Blake, P.G.", "Jackson, G.E."],
        title = u'The thermal decomposition of acetic acid',
        journal = "J. Chem. Soc. B",
        pages = """1153-1155""",
        year = "1968",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1968BLA/JAC1153-1155:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00001645
Bath gas: CH3CH=CH2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 08:14:07 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1968BLA/JAC1153-1155:1"""),
    ],
)

entry(
    index = 10,
    label = "1949BAM/DEW2877-2882:1",
    reactant1 = 
"""
1 *3 C 0 {2,S} {6,S} {7,S} {8,S}
2 *1 C 0 {1,S} {3,S} {4,D}
3 *2 O 0 {2,S} {5,S}
4    O 0 {2,D}
5 *4 H 0 {3,S}
6    H 0 {1,S}
7    H 0 {1,S}
8    H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,D}
2 *2 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1 *3 C 0 {2,S} {3,S} {4,S} {5,S}
2 *4 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+11,"s^-1"),
        n = 0,
        Ea = (259.412,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (773,"K"),
        Tmax = (1170,"K"),
        Pmin = (1200,"Pa"),
        Pmax = (21100,"Pa"),
    ),
    reference = Article(
        authors = ["Bamford, C.H.", "Dewar, M.J.S."],
        title = u'608. The thermal decomposition of acetic acid',
        journal = "J. Chem. Soc.",
        pages = """2877-2882""",
        year = "1949",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1949BAM/DEW2877-2882:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00001645
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00001645/rk00000001.xml
Bath gas: CH3C(O)OH
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
    history = [
        ("Fri Jul 13 08:14:07 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1949BAM/DEW2877-2882:1"""),
    ],
)

entry(
    index = 11,
    label = "1995DUA/PAG5114-5119:1",
    reactant1 = 
"""
1 *3 C 0 {2,S} {6,S} {7,S} {8,S}
2 *1 C 0 {1,S} {3,S} {4,D}
3 *2 O 0 {2,S} {5,S}
4    O 0 {2,D}
5 *4 H 0 {3,S}
6    H 0 {1,S}
7    H 0 {1,S}
8    H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,D}
2 *2 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1 *3 C 0 {2,S} {3,S} {4,S} {5,S}
2 *4 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.08e+13,"s^-1"),
        n = 0,
        Ea = (311.793,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (990,"K"),
        Tmax = (1010,"K"),
    ),
    reference = Article(
        authors = ["Duan, X.", "Page, M."],
        title = u'Theoretical investigation of competing mechanisms in the thermal unimolecular decomposition of acetic acid and the hydration reaction of ketene',
        journal = "J. Am. Chem. Soc.",
        volume = "117",
        pages = """5114-5119""",
        year = "1995",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1995DUA/PAG5114-5119:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00001645
""",
    history = [
        ("Fri Jul 13 08:14:07 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1995DUA/PAG5114-5119:1"""),
    ],
)

entry(
    index = 12,
    label = "1966BLA/HOL577-579:1",
    reactant1 = 
"""
1  *3 C 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 {1,S} {9,S} {10,S} {11,S}
3  *1 C 0 {1,S} {4,S} {5,D}
4  *2 O 0 {3,S} {6,S}
5     O 0 {3,D}
6  *4 H 0 {4,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {2,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,D}
2 *2 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1 *3 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {6,S} {7,S} {8,S}
3 *4 H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {2,S}
7    H 0 {2,S}
8    H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+09,"s^-1"),
        n = 0,
        Ea = (206.199,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (769,"K"),
        Tmax = (854,"K"),
        Pmin = (3333,"Pa"),
        Pmax = (26700,"Pa"),
    ),
    reference = Article(
        authors = ["Blake, P.G.", "Hole, K.J."],
        title = u'The thermal decomposition of propionic acid',
        journal = "J. Chem. Soc. B",
        pages = """577-579""",
        year = "1966",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1966BLA/HOL577-579:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00003987
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00003987/rk00000001.xml
Bath gas: C2H5COOH
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 08:14:22 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1966BLA/HOL577-579:1"""),
    ],
)

entry(
    index = 13,
    label = "1982BIG/CLA1:1",
    reactant1 = 
"""
1  *3 C 0 {2,S} {3,S} {8,S} {9,S}
2     C 0 {1,S} {4,D} {10,S}
3  *1 C 0 {1,S} {5,S} {6,D}
4     C 0 {2,D} {11,S} {12,S}
5  *2 O 0 {3,S} {7,S}
6     O 0 {3,D}
7  *4 H 0 {5,S}
8     H 0 {1,S}
9     H 0 {1,S}
10    H 0 {2,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,D}
2 *2 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1 *3 C 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 {1,S} {3,D} {7,S}
3    C 0 {2,D} {8,S} {9,S}
4 *4 H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
8    H 0 {3,S}
9    H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.12e+13,"s^-1"),
        n = 0,
        Ea = (190.401,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (636,"K"),
        Tmax = (651,"K"),
        Pmin = (6266,"Pa"),
        Pmax = (51200,"Pa"),
    ),
    reference = Article(
        authors = ["Bigley, D.B.", "Clarke, M.J."],
        title = u'Studies in Decarboxylation. Part 14. The Gas-phase Decarboxylation of But-3-enoic Acid and the Intermediacy of Isocrotonic (cis-But-2-enoic) Acid in its Isomerization to Crotonic (trans-But-2-enoic) Acid',
        journal = "J. Chem. Soc. Perkin Trans. 2",
        pages = """1""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982BIG/CLA1:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00008316
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
    history = [
        ("Fri Jul 13 08:14:31 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1982BIG/CLA1:1"""),
    ],
)

entry(
    index = 14,
    label = "1977BIG/WEA745:1",
    reactant1 = 
"""
1  *3 C 0 {2,S} {3,S} {8,S} {9,S}
2     C 0 {1,S} {4,D} {10,S}
3  *1 C 0 {1,S} {5,S} {6,D}
4     C 0 {2,D} {11,S} {12,S}
5  *2 O 0 {3,S} {7,S}
6     O 0 {3,D}
7  *4 H 0 {5,S}
8     H 0 {1,S}
9     H 0 {1,S}
10    H 0 {2,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,D}
2 *2 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1 *3 C 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 {1,S} {3,D} {7,S}
3    C 0 {2,D} {8,S} {9,S}
4 *4 H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
8    H 0 {3,S}
9    H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.97e+11,"s^-1"),
        n = 0,
        Ea = (167.952,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (456,"K"),
        Tmax = (500,"K"),
        Pmin = (6666,"Pa"),
        Pmax = (66700,"Pa"),
    ),
    reference = Article(
        authors = ["Bigley, D.B.", "Weatherhead, R.H.", "May, R.W."],
        title = u'Studies in Decarboxylation. Part 10. Effect of \u03b2-Substituents on the Rate of Gas-phase Decarboxylation of \u03b2\u03b2\u03b2\u03b2\u03c0\u03b2-Unsaturated Acids',
        journal = "J. Chem. Soc. Perkin Trans. 2",
        pages = """745""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977BIG/WEA745:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00008316
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
    history = [
        ("Fri Jul 13 08:14:31 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1977BIG/WEA745:1"""),
    ],
)

entry(
    index = 15,
    label = "1964SMI/BLA1231-1234:1",
    reactant1 = 
"""
1  *3 C 0 {2,S} {3,S} {8,S} {9,S}
2     C 0 {1,S} {4,D} {10,S}
3  *1 C 0 {1,S} {5,S} {6,D}
4     C 0 {2,D} {11,S} {12,S}
5  *2 O 0 {3,S} {7,S}
6     O 0 {3,D}
7  *4 H 0 {5,S}
8     H 0 {1,S}
9     H 0 {1,S}
10    H 0 {2,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,D}
2 *2 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1 *3 C 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 {1,S} {3,D} {7,S}
3    C 0 {2,D} {8,S} {9,S}
4 *4 H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
8    H 0 {3,S}
9    H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.54e+11,"s^-1"),
        n = 0,
        Ea = (162.132,"kJ/mol","+|-",6.494),
        T0 = (1,"K"),
        Tmin = (608,"K"),
        Tmax = (651,"K"),
    ),
    reference = Article(
        authors = ["Smith, G.G.", "Blau, S.E."],
        title = u'Decarboxylation. I. Kinetic study of the vapor phase thermal decarboxylation of 3-butenoic acid',
        journal = "J. Phys. Chem.",
        volume = "68",
        pages = """1231-1234""",
        year = "1964",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1964SMI/BLA1231-1234:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00008316
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008316/rk00000001.xml
Bath gas: CH2=CHCH2COOH
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 08:14:31 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1964SMI/BLA1231-1234:1"""),
    ],
)

entry(
    index = 16,
    label = "1986CAO/BAC967:1",
    reactant1 = 
"""
1  *3 C 0 {2,S} {3,S} {9,S} {10,S}
2  *1 C 0 {1,S} {4,S} {6,D}
3     C 0 {1,S} {5,S} {7,D}
4  *2 O 0 {2,S} {8,S}
5     O 0 {3,S} {11,S}
6     O 0 {2,D}
7     O 0 {3,D}
8  *4 H 0 {4,S}
9     H 0 {1,S}
10    H 0 {1,S}
11    H 0 {5,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,D}
2 *2 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1 *3 C 0 {2,S} {4,S} {6,S} {7,S}
2    C 0 {1,S} {3,S} {5,D}
3    O 0 {2,S} {8,S}
4 *4 H 0 {1,S}
5    O 0 {2,D}
6    H 0 {1,S}
7    H 0 {1,S}
8    H 0 {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.86e+13,"s^-1"),
        n = 0,
        Ea = (129.706,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (365,"K"),
        Tmax = (424,"K"),
        Pmin = (13.33,"Pa"),
        Pmax = (13.33,"Pa"),
    ),
    reference = Article(
        authors = ["Cao, J.-R.", "Back, R.A."],
        title = u'The thermolysis and photolysis of malonic acid in the gas phase',
        journal = "Can. J. Chem.",
        volume = "64",
        pages = """967""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986CAO/BAC967:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00006301
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00006301/rk00000001.xml
Bath gas: CH2(COOH)2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 08:14:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1986CAO/BAC967:1"""),
    ],
)

entry(
    index = 17,
    label = "1976BIG/WEA592:2",
    reactant1 = 
"""
1  *3 C 0 {3,S} {5,S} {9,S} {10,S}
2     C 0 {4,S} {11,S} {12,S} {13,S}
3     C 0 {1,S} {4,D} {14,S}
4     C 0 {2,S} {3,D} {15,S}
5  *1 C 0 {1,S} {6,S} {7,D}
6  *2 O 0 {5,S} {8,S}
7     O 0 {5,D}
8  *4 H 0 {6,S}
9     H 0 {1,S}
10    H 0 {1,S}
11    H 0 {2,S}
12    H 0 {2,S}
13    H 0 {2,S}
14    H 0 {3,S}
15    H 0 {4,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,D}
2 *2 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1  *3 C 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 {1,S} {4,D} {11,S}
4     C 0 {2,S} {3,D} {12,S}
5  *4 H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.34e+11,"s^-1"),
        n = 0,
        Ea = (172.941,"kJ/mol","+|-",6.918),
        T0 = (1,"K"),
        Tmin = (680,"K"),
        Tmax = (720,"K"),
        Pmin = (6666,"Pa"),
        Pmax = (66700,"Pa"),
    ),
    reference = Article(
        authors = ["Bigley, D.B.", "Weatherhead, R.H."],
        title = u'Studies in Decarboxylation. Part VIII. The Gas-phase Pyrolysis of \u03b2\u03c0-Acetylenic Acids',
        journal = "J. Chem. Soc. Perkin Trans. 2",
        pages = """592""",
        year = "1976",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976BIG/WEA592:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00012860
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012860/rk00000001.xml
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 08:14:46 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1976BIG/WEA592:2"""),
    ],
)

entry(
    index = 18,
    label = "1982ALB/BIG15:2",
    reactant1 = 
"""
1  *3 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {10,S} {11,S} {12,S}
3     C 0 {1,S} {13,S} {14,S} {15,S}
4     C 0 {1,S} {6,D} {16,S}
5  *1 C 0 {1,S} {7,S} {8,D}
6     C 0 {4,D} {17,S} {18,S}
7  *2 O 0 {5,S} {9,S}
8     O 0 {5,D}
9  *4 H 0 {7,S}
10    H 0 {2,S}
11    H 0 {2,S}
12    H 0 {2,S}
13    H 0 {3,S}
14    H 0 {3,S}
15    H 0 {3,S}
16    H 0 {4,S}
17    H 0 {6,S}
18    H 0 {6,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,D}
2 *2 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1  *3 C 0 {2,S} {3,S} {4,S} {6,S}
2     C 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 {1,S} {10,S} {11,S} {12,S}
4     C 0 {1,S} {5,D} {13,S}
5     C 0 {4,D} {14,S} {15,S}
6  *4 H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {5,S}
15    H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.03e+11,"s^-1"),
        n = 0,
        Ea = (154.649,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (550,"K"),
        Tmax = (600,"K"),
        Pmin = (6666,"Pa"),
        Pmax = (66700,"Pa"),
    ),
    reference = Article(
        authors = ["Al-Borno, A.", "Bigley, D.B."],
        title = u'Studies in Decarboxylation. Par t 15. The Effects of 3-Substitution on the Rate of Decarboxylation of \u03b2\u03b2\u03c0\u03b2-Unsaturated Acids',
        journal = "J. Chem. Soc. Perkin Trans. 2",
        pages = """15""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982ALB/BIG15:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00014891
Bath gas: He
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
    history = [
        ("Fri Jul 13 08:14:48 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1982ALB/BIG15:2"""),
    ],
)

entry(
    index = 19,
    label = "1967BIG/MAY557-559:3",
    reactant1 = 
"""
1  *3 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {10,S} {11,S} {12,S}
3     C 0 {1,S} {13,S} {14,S} {15,S}
4     C 0 {1,S} {6,D} {16,S}
5  *1 C 0 {1,S} {7,S} {8,D}
6     C 0 {4,D} {17,S} {18,S}
7  *2 O 0 {5,S} {9,S}
8     O 0 {5,D}
9  *4 H 0 {7,S}
10    H 0 {2,S}
11    H 0 {2,S}
12    H 0 {2,S}
13    H 0 {3,S}
14    H 0 {3,S}
15    H 0 {3,S}
16    H 0 {4,S}
17    H 0 {6,S}
18    H 0 {6,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,D}
2 *2 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1  *3 C 0 {2,S} {3,S} {4,S} {6,S}
2     C 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 {1,S} {10,S} {11,S} {12,S}
4     C 0 {1,S} {5,D} {13,S}
5     C 0 {4,D} {14,S} {15,S}
6  *4 H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {5,S}
15    H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.65e+10,"s^-1"),
        n = 0,
        Ea = (148.829,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (500,"K"),
        Tmax = (548,"K"),
    ),
    reference = Article(
        authors = ["Bigley, D.B.", "May, R.W."],
        title = u'Studies in decarboxylation. Part IV. The effect of alkyl substituents on the rate of gas-phase decarboxylation of some \u03b2\u03b3-unsaturated acids',
        journal = "J. Chem. Soc. B",
        pages = """557-559""",
        year = "1967",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1967BIG/MAY557-559:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00014891
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00014891/rk00000001.xml
Bath gas: CH2=CHC(CH3)2COOH
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 08:14:48 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1967BIG/MAY557-559:3"""),
    ],
)

entry(
    index = 20,
    label = "1967BIG/MAY557-559:4",
    reactant1 = 
"""
1  *3 C 0 {2,S} {3,S} {5,S} {7,S}
2     C 0 {1,S} {11,S} {12,S} {13,S}
3     C 0 {1,S} {14,S} {15,S} {16,S}
4     C 0 {6,S} {17,S} {18,S} {19,S}
5     C 0 {1,S} {6,D} {20,S}
6     C 0 {4,S} {5,D} {21,S}
7  *1 C 0 {1,S} {8,S} {9,D}
8  *2 O 0 {7,S} {10,S}
9     O 0 {7,D}
10 *4 H 0 {8,S}
11    H 0 {2,S}
12    H 0 {2,S}
13    H 0 {2,S}
14    H 0 {3,S}
15    H 0 {3,S}
16    H 0 {3,S}
17    H 0 {4,S}
18    H 0 {4,S}
19    H 0 {4,S}
20    H 0 {5,S}
21    H 0 {6,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,D}
2 *2 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1  *3 C 0 {2,S} {3,S} {5,S} {7,S}
2     C 0 {1,S} {8,S} {9,S} {10,S}
3     C 0 {1,S} {11,S} {12,S} {13,S}
4     C 0 {6,S} {14,S} {15,S} {16,S}
5     C 0 {1,S} {6,D} {17,S}
6     C 0 {4,S} {5,D} {18,S}
7  *4 H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {4,S}
17    H 0 {5,S}
18    H 0 {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.64e+11,"s^-1"),
        n = 0,
        Ea = (164.627,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (500,"K"),
        Tmax = (564,"K"),
    ),
    reference = Article(
        authors = ["Bigley, D.B.", "May, R.W."],
        title = u'Studies in decarboxylation. Part IV. The effect of alkyl substituents on the rate of gas-phase decarboxylation of some \u03b2\u03b3-unsaturated acids',
        journal = "J. Chem. Soc. B",
        pages = """557-559""",
        year = "1967",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1967BIG/MAY557-559:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015735
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015735/rk00000001.xml
Bath gas: 3-Pentenoic acid, 2,2-dimethyl-
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 08:14:53 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1967BIG/MAY557-559:4"""),
    ],
)

entry(
    index = 21,
    label = "1967BIG/MAY557-559:2",
    reactant1 = 
"""
1  *3 C 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 {1,S} {11,S} {12,S} {13,S}
3     C 0 {1,S} {14,S} {15,S} {16,S}
4     C 0 {5,S} {17,S} {18,S} {19,S}
5     C 0 {1,S} {4,S} {7,D}
6  *1 C 0 {1,S} {8,S} {9,D}
7     C 0 {5,D} {20,S} {21,S}
8  *2 O 0 {6,S} {10,S}
9     O 0 {6,D}
10 *4 H 0 {8,S}
11    H 0 {2,S}
12    H 0 {2,S}
13    H 0 {2,S}
14    H 0 {3,S}
15    H 0 {3,S}
16    H 0 {3,S}
17    H 0 {4,S}
18    H 0 {4,S}
19    H 0 {4,S}
20    H 0 {7,S}
21    H 0 {7,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,D}
2 *2 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1  *3 C 0 {2,S} {3,S} {5,S} {7,S}
2     C 0 {1,S} {8,S} {9,S} {10,S}
3     C 0 {1,S} {11,S} {12,S} {13,S}
4     C 0 {5,S} {14,S} {15,S} {16,S}
5     C 0 {1,S} {4,S} {6,D}
6     C 0 {5,D} {17,S} {18,S}
7  *4 H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {4,S}
17    H 0 {6,S}
18    H 0 {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.65e+10,"s^-1"),
        n = 0,
        Ea = (133.863,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (447,"K"),
        Tmax = (500,"K"),
    ),
    reference = Article(
        authors = ["Bigley, D.B.", "May, R.W."],
        title = u'Studies in decarboxylation. Part IV. The effect of alkyl substituents on the rate of gas-phase decarboxylation of some \u03b2\u03b3-unsaturated acids',
        journal = "J. Chem. Soc. B",
        pages = """557-559""",
        year = "1967",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1967BIG/MAY557-559:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00012640
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012640/rk00000001.xml
Bath gas: CH2=C(CH3)C(CH3)2COOH
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Tue Jul 24 14:32:51 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1967BIG/MAY557-559:2"""),
    ],
)

entry(
    index = 22,
    label = "1982ALB/BIG15:1",
    reactant1 = 
"""
1  *3 C 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 {1,S} {11,S} {12,S} {13,S}
3     C 0 {1,S} {14,S} {15,S} {16,S}
4     C 0 {5,S} {17,S} {18,S} {19,S}
5     C 0 {1,S} {4,S} {7,D}
6  *1 C 0 {1,S} {8,S} {9,D}
7     C 0 {5,D} {20,S} {21,S}
8  *2 O 0 {6,S} {10,S}
9     O 0 {6,D}
10 *4 H 0 {8,S}
11    H 0 {2,S}
12    H 0 {2,S}
13    H 0 {2,S}
14    H 0 {3,S}
15    H 0 {3,S}
16    H 0 {3,S}
17    H 0 {4,S}
18    H 0 {4,S}
19    H 0 {4,S}
20    H 0 {7,S}
21    H 0 {7,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,D}
2 *2 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1  *3 C 0 {2,S} {3,S} {5,S} {7,S}
2     C 0 {1,S} {8,S} {9,S} {10,S}
3     C 0 {1,S} {11,S} {12,S} {13,S}
4     C 0 {5,S} {14,S} {15,S} {16,S}
5     C 0 {1,S} {4,S} {6,D}
6     C 0 {5,D} {17,S} {18,S}
7  *4 H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {4,S}
17    H 0 {6,S}
18    H 0 {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.04e+11,"s^-1"),
        n = 0,
        Ea = (143.009,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (550,"K"),
        Tmax = (600,"K"),
        Pmin = (6666,"Pa"),
        Pmax = (66700,"Pa"),
    ),
    reference = Article(
        authors = ["Al-Borno, A.", "Bigley, D.B."],
        title = u'Studies in Decarboxylation. Par t 15. The Effects of 3-Substitution on the Rate of Decarboxylation of \u03b2\u03b2\u03c0\u03b2-Unsaturated Acids',
        journal = "J. Chem. Soc. Perkin Trans. 2",
        pages = """15""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982ALB/BIG15:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00012640
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012640/rk00000002.xml
Bath gas: He
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
    history = [
        ("Tue Jul 24 14:39:32 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1982ALB/BIG15:1"""),
    ],
)

entry(
    index = 23,
    label = "1992COL/AMO2125-2127:1",
    reactant1 = 
"""
1  *3 C 0 {2,S} {8,S} {12,S} {13,S}
2     C 0 {1,S} {3,B} {4,B}
3     C 0 {2,B} {6,B} {14,S}
4     C 0 {2,B} {7,B} {15,S}
5     C 0 {6,B} {7,B} {16,S}
6     C 0 {3,B} {5,B} {17,S}
7     C 0 {4,B} {5,B} {18,S}
8  *1 C 0 {1,S} {9,S} {10,D}
9  *2 O 0 {8,S} {11,S}
10    O 0 {8,D}
11 *4 H 0 {9,S}
12    H 0 {1,S}
13    H 0 {1,S}
14    H 0 {3,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {6,S}
18    H 0 {7,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,D}
2 *2 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1  *3 C 0 {2,S} {8,S} {9,S} {10,S}
2     C 0 {1,S} {3,B} {4,B}
3     C 0 {2,B} {5,B} {11,S}
4     C 0 {2,B} {6,B} {12,S}
5     C 0 {3,B} {7,B} {13,S}
6     C 0 {4,B} {7,B} {14,S}
7     C 0 {5,B} {6,B} {15,S}
8  *4 H 0 {1,S}
9     H 0 {1,S}
10    H 0 {1,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
15    H 0 {7,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"s^-1","*|/",2),
        n = 0,
        Ea = (101.437,"kJ/mol","+|-",4.057),
        T0 = (1,"K"),
        Tmin = (870,"K"),
        Tmax = (1020,"K"),
    ),
    reference = Article(
        authors = ["Colussi, A.J.", "Amorebieta, V.T.", "Grela, M.A."],
        title = u'Very low pressure pyrolysis of phenylacetic acid',
        journal = "J. Chem. Soc. Faraday Trans.",
        volume = "88",
        pages = """2125-2127""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992COL/AMO2125-2127:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00004480
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004480/rk00000001.xml
Uncertainty: 2.0
Bath gas: Benzeneacetic acid
Excitation technique: Thermal
Analytical technique: Mass spectrometry
""",
    history = [
        ("Fri Jul 13 08:14:24 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1992COL/AMO2125-2127:1"""),
    ],
)

entry(
    index = 24,
    label = "1967BIG/MAY557-559:6",
    reactant1 = 
"""
1  *3 C 0 {5,S} {6,S} {7,S} {9,S}
2     C 0 {3,S} {4,S} {13,S} {14,S}
3     C 0 {2,S} {7,S} {15,S} {16,S}
4     C 0 {2,S} {8,S} {17,S} {18,S}
5     C 0 {1,S} {19,S} {20,S} {21,S}
6     C 0 {1,S} {22,S} {23,S} {24,S}
7     C 0 {1,S} {3,S} {8,D}
8     C 0 {4,S} {7,D} {25,S}
9  *1 C 0 {1,S} {10,S} {11,D}
10 *2 O 0 {9,S} {12,S}
11    O 0 {9,D}
12 *4 H 0 {10,S}
13    H 0 {2,S}
14    H 0 {2,S}
15    H 0 {3,S}
16    H 0 {3,S}
17    H 0 {4,S}
18    H 0 {4,S}
19    H 0 {5,S}
20    H 0 {5,S}
21    H 0 {5,S}
22    H 0 {6,S}
23    H 0 {6,S}
24    H 0 {6,S}
25    H 0 {8,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,D}
2 *2 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1  *3 C 0 {5,S} {6,S} {7,S} {9,S}
2     C 0 {3,S} {4,S} {10,S} {11,S}
3     C 0 {2,S} {7,S} {12,S} {13,S}
4     C 0 {2,S} {8,S} {14,S} {15,S}
5     C 0 {1,S} {16,S} {17,S} {18,S}
6     C 0 {1,S} {19,S} {20,S} {21,S}
7     C 0 {1,S} {3,S} {8,D}
8     C 0 {4,S} {7,D} {22,S}
9  *4 H 0 {1,S}
10    H 0 {2,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {5,S}
18    H 0 {5,S}
19    H 0 {6,S}
20    H 0 {6,S}
21    H 0 {6,S}
22    H 0 {8,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.25e+08,"s^-1"),
        n = 0,
        Ea = (121.391,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (469,"K"),
        Tmax = (501,"K"),
    ),
    reference = Article(
        authors = ["Bigley, D.B.", "May, R.W."],
        title = u'Studies in decarboxylation. Part IV. The effect of alkyl substituents on the rate of gas-phase decarboxylation of some \u03b2\u03b3-unsaturated acids',
        journal = "J. Chem. Soc. B",
        pages = """557-559""",
        year = "1967",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1967BIG/MAY557-559:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015737
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015737/rk00000001.xml
Bath gas: 1-Cyclopentene-1-acetic acid, α,α-dimethyl-
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 08:15:01 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1967BIG/MAY557-559:6"""),
    ],
)

entry(
    index = 25,
    label = "1997CHU/MAR121-124:2",
    reactant1 = 
"""
1  *3 C 0 {2,S} {8,S} {9,S} {13,S}
2     C 0 {1,S} {3,B} {4,B}
3     C 0 {2,B} {6,B} {14,S}
4     C 0 {2,B} {7,B} {15,S}
5     C 0 {6,B} {7,B} {16,S}
6     C 0 {3,B} {5,B} {17,S}
7     C 0 {4,B} {5,B} {18,S}
8  *1 C 0 {1,S} {10,S} {11,D}
9     O 0 {1,S} {19,S}
10 *2 O 0 {8,S} {12,S}
11    O 0 {8,D}
12 *4 H 0 {10,S}
13    H 0 {1,S}
14    H 0 {3,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {6,S}
18    H 0 {7,S}
19    H 0 {9,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,D}
2 *2 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1  *3 C 0 {2,S} {8,S} {9,S} {10,S}
2     C 0 {1,S} {3,B} {4,B}
3     C 0 {2,B} {5,B} {11,S}
4     C 0 {2,B} {6,B} {12,S}
5     C 0 {3,B} {7,B} {13,S}
6     C 0 {4,B} {7,B} {14,S}
7     C 0 {5,B} {6,B} {15,S}
8     O 0 {1,S} {16,S}
9  *4 H 0 {1,S}
10    H 0 {1,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
15    H 0 {7,S}
16    H 0 {8,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.41e+14,"s^-1","+|-",1.15e+14),
        n = 0,
        Ea = (202.7,"kJ/mol","+|-",4.6),
        T0 = (1,"K"),
        Tmin = (583,"K"),
        Tmax = (613,"K"),
        Pmin = (2026,"Pa"),
        Pmax = (6946,"Pa"),
    ),
    reference = Article(
        authors = ["Chuchani, G.", "Martin, I."],
        title = u'ELIMINATION KINETICS OF DL-MANDELIC ACID IN THE GAS PHASE',
        journal = "J. Phys. Org. Chem.",
        volume = "10",
        pages = """121-124""",
        year = "1997",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1997CHU/MAR121-124:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00008130
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008130/rk00000001.xml
Pressure dependence: None reported
Experimental procedure: Static or low flow - Data taken vs time
Excitation technique: Thermal
Time resolution: By end product analysis
Analytical technique: Pressure measurement

The A-factor given in the paper (1.41E13 s-1) is one order of magnitude smaller than required to reproduce the reported rate constants, apparently due to a typographical error. The value listed here closely reproduces the actual rate data listed by the authors and our least squares analysis of their reported rate data.

Kinetics were determined by following pressure vs. time. Products were determined by GC product analysis.

Uncertainties are precision only and are at the 90% confidence level.
""",
    history = [
        ("Fri Jul 20 17:40:53 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1997CHU/MAR121-124:2"""),
    ],
)

entry(
    index = 26,
    label = "1967BIG/MAY557-559:5",
    reactant1 = 
"""
1  *3 C 0 {3,S} {4,S} {7,S} {9,S}
2     C 0 {5,S} {7,S} {13,S} {14,S}
3     C 0 {1,S} {15,S} {16,S} {17,S}
4     C 0 {1,S} {18,S} {19,S} {20,S}
5     C 0 {2,S} {21,S} {22,S} {23,S}
6     C 0 {8,S} {24,S} {25,S} {26,S}
7     C 0 {1,S} {2,S} {8,D}
8     C 0 {6,S} {7,D} {27,S}
9  *1 C 0 {1,S} {10,S} {11,D}
10 *2 O 0 {9,S} {12,S}
11    O 0 {9,D}
12 *4 H 0 {10,S}
13    H 0 {2,S}
14    H 0 {2,S}
15    H 0 {3,S}
16    H 0 {3,S}
17    H 0 {3,S}
18    H 0 {4,S}
19    H 0 {4,S}
20    H 0 {4,S}
21    H 0 {5,S}
22    H 0 {5,S}
23    H 0 {5,S}
24    H 0 {6,S}
25    H 0 {6,S}
26    H 0 {6,S}
27    H 0 {8,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,D}
2 *2 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1  *3 C 0 {3,S} {4,S} {7,S} {9,S}
2     C 0 {5,S} {7,S} {10,S} {11,S}
3     C 0 {1,S} {12,S} {13,S} {14,S}
4     C 0 {1,S} {15,S} {16,S} {17,S}
5     C 0 {2,S} {18,S} {19,S} {20,S}
6     C 0 {8,S} {21,S} {22,S} {23,S}
7     C 0 {1,S} {2,S} {8,D}
8     C 0 {6,S} {7,D} {24,S}
9  *4 H 0 {1,S}
10    H 0 {2,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {3,S}
15    H 0 {4,S}
16    H 0 {4,S}
17    H 0 {4,S}
18    H 0 {5,S}
19    H 0 {5,S}
20    H 0 {5,S}
21    H 0 {6,S}
22    H 0 {6,S}
23    H 0 {6,S}
24    H 0 {8,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.07e+11,"s^-1"),
        n = 0,
        Ea = (146.335,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (467,"K"),
        Tmax = (502,"K"),
    ),
    reference = Article(
        authors = ["Bigley, D.B.", "May, R.W."],
        title = u'Studies in decarboxylation. Part IV. The effect of alkyl substituents on the rate of gas-phase decarboxylation of some \u03b2\u03b3-unsaturated acids',
        journal = "J. Chem. Soc. B",
        pages = """557-559""",
        year = "1967",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1967BIG/MAY557-559:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015736
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015736/rk00000001.xml
Bath gas: CH3CH=C(C2H5)C(CH3)2COOH
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Tue Jul 24 15:01:52 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1967BIG/MAY557-559:5"""),
    ],
)

