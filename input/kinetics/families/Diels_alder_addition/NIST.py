#!/usr/bin/env python
# encoding: utf-8

name = "Diels_alder_addition/NIST"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    label = "1973TSA651:1",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {7,S} {8,S}
2  *2 C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,S} {11,S} {12,S}
4  *6 C 0 {2,S} {6,S} {13,S} {14,S}
5  *4 C 0 {3,S} {6,D} {15,S}
6  *5 C 0 {4,S} {5,D} {16,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {6,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2 *2 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1  *5 C 0 {2,S} {3,D} {5,S}
2  *4 C 0 {1,S} {4,D} {6,S}
3  *6 C 0 {1,D} {7,S} {8,S}
4  *3 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.41e+15,"s^-1","*|/",3.16),
        n = 0,
        Ea = (278.535,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (1080,"K"),
        Tmax = (1150,"K"),
        Pmin = (55600,"Pa"),
        Pmax = (59300,"Pa"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Thermal Decomposition of 1,1,2,2-Tetramethylcyclopropane in a Single-Pulse Shock Tube',
        journal = "Int. J. Chem. Kinet.",
        volume = "5",
        pages = """651""",
        year = "1973",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1973TSA651:1",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00005509
Uncertainty: 3.1600001
Bath gas: Ar
""",
    history = [
        ("Fri Jul 13 07:33:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1973TSA651:1"""),
    ],
)

entry(
    index = 2,
    label = "1987KIE/SHA3024:1",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {7,S} {8,S}
2  *2 C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,S} {11,S} {12,S}
4  *6 C 0 {2,S} {6,S} {13,S} {14,S}
5  *4 C 0 {3,S} {6,D} {15,S}
6  *5 C 0 {4,S} {5,D} {16,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {6,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2 *2 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1  *5 C 0 {2,S} {3,D} {5,S}
2  *4 C 0 {1,S} {4,D} {6,S}
3  *6 C 0 {1,D} {7,S} {8,S}
4  *3 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (3.72e+15,"s^-1"),
        n = 0,
        Ea = (275.209,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (1200,"K"),
        Tmax = (1800,"K"),
        Pmin = (20000,"Pa"),
        Pmax = (46700,"Pa"),
    ),
    reference = Article(
        authors = ["Kiefer, J.H.", "Shah, J.N."],
        title = u'Unimolecular dissociation of cyclohexene at extremely high temperatures: Behavior of the energy-transfer collision efficiency',
        journal = "J. Phys. Chem.",
        volume = "91",
        pages = """3024""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987KIE/SHA3024:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00005509
Bath gas: Kr
""",
    history = [
        ("Fri Jul 13 07:33:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1987KIE/SHA3024:1"""),
    ],
)

entry(
    index = 3,
    label = "1987KIE/SHA3024:3",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {7,S} {8,S}
2  *2 C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,S} {11,S} {12,S}
4  *6 C 0 {2,S} {6,S} {13,S} {14,S}
5  *4 C 0 {3,S} {6,D} {15,S}
6  *5 C 0 {4,S} {5,D} {16,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {6,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2 *2 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1  *5 C 0 {2,S} {3,D} {5,S}
2  *4 C 0 {1,S} {4,D} {6,S}
3  *6 C 0 {1,D} {7,S} {8,S}
4  *3 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.34e+96,"s^-1"),
        n = -23.6,
        Ea = (465.61,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (1200,"K"),
        Tmax = (2000,"K"),
        Pmin = (48000,"Pa"),
        Pmax = (73300,"Pa"),
    ),
    reference = Article(
        authors = ["Kiefer, J.H.", "Shah, J.N."],
        title = u'Unimolecular dissociation of cyclohexene at extremely high temperatures: Behavior of the energy-transfer collision efficiency',
        journal = "J. Phys. Chem.",
        volume = "91",
        pages = """3024""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987KIE/SHA3024:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00005509
Bath gas: Kr
Excitation technique: Thermal
Analytical technique: Laser schlieren
""",
    history = [
        ("Fri Jul 13 07:33:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1987KIE/SHA3024:3"""),
    ],
)

entry(
    index = 4,
    label = "1987KIE/SHA3024:2",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {7,S} {8,S}
2  *2 C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,S} {11,S} {12,S}
4  *6 C 0 {2,S} {6,S} {13,S} {14,S}
5  *4 C 0 {3,S} {6,D} {15,S}
6  *5 C 0 {4,S} {5,D} {16,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {6,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2 *2 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1  *5 C 0 {2,S} {3,D} {5,S}
2  *4 C 0 {1,S} {4,D} {6,S}
3  *6 C 0 {1,D} {7,S} {8,S}
4  *3 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.82e+102,"s^-1"),
        n = -25.3,
        Ea = (483.071,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (1200,"K"),
        Tmax = (2000,"K"),
        Pmin = (14300,"Pa"),
        Pmax = (22700,"Pa"),
    ),
    reference = Article(
        authors = ["Kiefer, J.H.", "Shah, J.N."],
        title = u'Unimolecular dissociation of cyclohexene at extremely high temperatures: Behavior of the energy-transfer collision efficiency',
        journal = "J. Phys. Chem.",
        volume = "91",
        pages = """3024""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987KIE/SHA3024:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00005509
Bath gas: Kr
Excitation technique: Thermal
Analytical technique: Laser schlieren
""",
    history = [
        ("Fri Jul 13 07:33:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1987KIE/SHA3024:2"""),
    ],
)

entry(
    index = 5,
    label = "1984LEW/BER4112:2",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {7,S} {8,S}
2  *2 C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,S} {11,S} {12,S}
4  *6 C 0 {2,S} {6,S} {13,S} {14,S}
5  *4 C 0 {3,S} {6,D} {15,S}
6  *5 C 0 {4,S} {5,D} {16,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {6,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2 *2 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1  *5 C 0 {2,S} {3,D} {5,S}
2  *4 C 0 {1,S} {4,D} {6,S}
3  *6 C 0 {1,D} {7,S} {8,S}
4  *3 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.41e+15,"s^-1"),
        n = 0,
        Ea = (278.487,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (710,"K"),
        Tmax = (1190,"K"),
        Pmin = (4933,"Pa"),
        Pmax = (200000,"Pa"),
    ),
    reference = Article(
        authors = ["Lewis, D.K.", "Bergmann, J.", "Manjoney, R.", "Paddock, R.", "Kaira, B.L."],
        title = u'Rates of reactions of cyclopropane, cyclobutane, cyclopentene, and cyclohexene in the presence of boron trichloride',
        journal = "J. Phys. Chem.",
        volume = "88",
        pages = """4112""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984LEW/BER4112:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005509
Bath gas: Ar
Pressure dependence: None reported
Excitation technique: Thermal
Time resolution: By end product analysis
Analytical technique: Gas chromatography

Two experimental set-ups were used: experiments at 710-748 K and 37-53 torr were performed in a static reactor, while the shock tube methodology was used at 966-1190 K with shock pressures of about 2 atm. The rate parameters are from the literature but provide a reasonable fit to the present data.
""",
    history = [
        ("Fri Jul 13 07:33:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1984LEW/BER4112:2"""),
    ],
)

entry(
    index = 6,
    label = "1984HID/CHI181:1",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {7,S} {8,S}
2  *2 C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,S} {11,S} {12,S}
4  *6 C 0 {2,S} {6,S} {13,S} {14,S}
5  *4 C 0 {3,S} {6,D} {15,S}
6  *5 C 0 {4,S} {5,D} {16,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {6,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2 *2 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1  *5 C 0 {2,S} {3,D} {5,S}
2  *4 C 0 {1,S} {4,D} {6,S}
3  *6 C 0 {1,D} {7,S} {8,S}
4  *3 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.5e+15,"s^-1"),
        n = 0,
        Ea = (280.198,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (1120,"K"),
        Tmax = (1330,"K"),
        Pmin = (13300,"Pa"),
        Pmax = (13300,"Pa"),
    ),
    reference = Article(
        authors = ["Hidaka, Y.", "Chimori, T.", "Shiba, S.", "Suga, M."],
        title = u'Decyclization of cyclohexene in shock waves',
        journal = "Chem. Phys. Lett.",
        volume = "111",
        pages = """181""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984HID/CHI181:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005509
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
    history = [
        ("Fri Jul 13 07:33:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1984HID/CHI181:1"""),
    ],
)

entry(
    index = 7,
    label = "1981SKI/ROG481:2",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {7,S} {8,S}
2  *2 C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,S} {11,S} {12,S}
4  *6 C 0 {2,S} {6,S} {13,S} {14,S}
5  *4 C 0 {3,S} {6,D} {15,S}
6  *5 C 0 {4,S} {5,D} {16,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {6,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2 *2 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1  *5 C 0 {2,S} {3,D} {5,S}
2  *4 C 0 {1,S} {4,D} {6,S}
3  *6 C 0 {1,D} {7,S} {8,S}
4  *3 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.51e+15,"s^-1","*|/",3.16),
        n = 0,
        Ea = (280.198,"kJ/mol","+|-",11.225),
        T0 = (1,"K"),
        Tmin = (1000,"K"),
        Tmax = (1340,"K"),
        Pmin = (304000,"Pa"),
        Pmax = (912000,"Pa"),
    ),
    reference = Article(
        authors = ["Skinner, G.B.", "Rogers, D.", "Patel, K.B."],
        title = u'Consistency of theory and experiment in the ethane-methyl radical system',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """481""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981SKI/ROG481:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005509
Uncertainty: 3.1600001
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:33:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1981SKI/ROG481:2"""),
    ],
)

entry(
    index = 8,
    label = "1979NEW/ONE1167:2",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {7,S} {8,S}
2  *2 C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,S} {11,S} {12,S}
4  *6 C 0 {2,S} {6,S} {13,S} {14,S}
5  *4 C 0 {3,S} {6,D} {15,S}
6  *5 C 0 {4,S} {5,D} {16,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {6,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2 *2 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1  *5 C 0 {2,S} {3,D} {5,S}
2  *4 C 0 {1,S} {4,D} {6,S}
3  *6 C 0 {1,D} {7,S} {8,S}
4  *3 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.82e+15,"s^-1"),
        n = 0,
        Ea = (274.378,"kJ/mol","+|-",13.719),
        T0 = (1,"K"),
        Tmin = (1020,"K"),
        Tmax = (1200,"K"),
        Pmin = (520000,"Pa"),
        Pmax = (533000,"Pa"),
    ),
    reference = Article(
        authors = ["Newman, C.G.", "O'Neal, H.E.", "Ring, M.A.", "Leska, F.", "Shipley, N."],
        title = u'Kinetics and mechanism of the silane decomposition',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """1167""",
        year = "1979",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1979NEW/ONE1167:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00005509
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:33:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1979NEW/ONE1167:2"""),
    ],
)

entry(
    index = 9,
    label = "1976BAR/PAR2404:2",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {7,S} {8,S}
2  *2 C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,S} {11,S} {12,S}
4  *6 C 0 {2,S} {6,S} {13,S} {14,S}
5  *4 C 0 {3,S} {6,D} {15,S}
6  *5 C 0 {4,S} {5,D} {16,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {6,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2 *2 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1  *5 C 0 {2,S} {3,D} {5,S}
2  *4 C 0 {1,S} {4,D} {6,S}
3  *6 C 0 {1,D} {7,S} {8,S}
4  *3 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.45e+15,"s^-1"),
        n = 0,
        Ea = (274.378,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (1010,"K"),
        Tmax = (1190,"K"),
        Pmin = (169000,"Pa"),
        Pmax = (299000,"Pa"),
    ),
    reference = Article(
        authors = ["Barnard, J.A.", "Parrott, T.K."],
        title = u'Kinetics of the thermal unimolecular reactions of cyclohexene and 4-vinylcyclohexene behind reflected shock waves',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "72",
        pages = """2404""",
        year = "1976",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976BAR/PAR2404:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005509
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:33:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1976BAR/PAR2404:2"""),
    ],
)

entry(
    index = 10,
    label = "1970TSA311:2",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {7,S} {8,S}
2  *2 C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,S} {11,S} {12,S}
4  *6 C 0 {2,S} {6,S} {13,S} {14,S}
5  *4 C 0 {3,S} {6,D} {15,S}
6  *5 C 0 {4,S} {5,D} {16,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {6,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2 *2 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1  *5 C 0 {2,S} {3,D} {5,S}
2  *4 C 0 {1,S} {4,D} {6,S}
3  *6 C 0 {1,D} {7,S} {8,S}
4  *3 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2e+15,"s^-1"),
        n = 0,
        Ea = (280.198,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (950,"K"),
        Tmax = (1100,"K"),
        Pmin = (203000,"Pa"),
        Pmax = (608000,"Pa"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Comparative rate single-pulse shock tube studies on the thermal decomposition of cyclohexene, 2,2,3-trimethylbutane, isopropyl bromide, and ethylcyclobutane',
        journal = "Int. J. Chem. Kinet.",
        volume = "2",
        pages = """311""",
        year = "1970",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1970TSA311:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00005509
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:33:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1970TSA311:2"""),
    ],
)

entry(
    index = 11,
    label = "1965TSA1805-1809:2",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {7,S} {8,S}
2  *2 C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,S} {11,S} {12,S}
4  *6 C 0 {2,S} {6,S} {13,S} {14,S}
5  *4 C 0 {3,S} {6,D} {15,S}
6  *5 C 0 {4,S} {5,D} {16,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {6,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2 *2 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1  *5 C 0 {2,S} {3,D} {5,S}
2  *4 C 0 {1,S} {4,D} {6,S}
3  *6 C 0 {1,D} {7,S} {8,S}
4  *3 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.05e+15,"s^-1"),
        n = 0,
        Ea = (279.366,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (900,"K"),
        Tmax = (1150,"K"),
        Pmin = (52500,"Pa"),
        Pmax = (163000,"Pa"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Decyclization of cyclohexene, 4-methylcyclohexene, and 4-vinylcyclohexene in a single-pulse shock tube',
        journal = "J. Chem. Phys.",
        volume = "42",
        pages = """1805-1809""",
        year = "1965",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1965TSA1805-1809:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00005509
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:33:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1965TSA1805-1809:2"""),
    ],
)

entry(
    index = 12,
    label = "1964UCH/TOM1878:1",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {7,S} {8,S}
2  *2 C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,S} {11,S} {12,S}
4  *6 C 0 {2,S} {6,S} {13,S} {14,S}
5  *4 C 0 {3,S} {6,D} {15,S}
6  *5 C 0 {4,S} {5,D} {16,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {6,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2 *2 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1  *5 C 0 {2,S} {3,D} {5,S}
2  *4 C 0 {1,S} {4,D} {6,S}
3  *6 C 0 {1,D} {7,S} {8,S}
4  *3 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.45e+15,"s^-1"),
        n = 0,
        Ea = (276.872,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (814,"K"),
        Tmax = (902,"K"),
        Pmin = (3333,"Pa"),
        Pmax = (3333,"Pa"),
    ),
    reference = Article(
        authors = ["Uchiyama, M.", "Tomioka, T.", "Amano, A."],
        title = u'Thermal decomposition of cyclohexene',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "68",
        pages = """1878""",
        year = "1964",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1964UCH/TOM1878:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005509
Bath gas: He
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:33:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1964UCH/TOM1878:1"""),
    ],
)

entry(
    index = 13,
    label = "1961SMI/GOR1124:2",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {7,S} {8,S}
2  *2 C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,S} {11,S} {12,S}
4  *6 C 0 {2,S} {6,S} {13,S} {14,S}
5  *4 C 0 {3,S} {6,D} {15,S}
6  *5 C 0 {4,S} {5,D} {16,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {6,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2 *2 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1  *5 C 0 {2,S} {3,D} {5,S}
2  *4 C 0 {1,S} {4,D} {6,S}
3  *6 C 0 {1,D} {7,S} {8,S}
4  *3 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.4e+17,"s^-1"),
        n = 0,
        Ea = (304.31,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (698,"K"),
        Tmax = (808,"K"),
        Pmin = (30300,"Pa"),
        Pmax = (344000,"Pa"),
    ),
    reference = Article(
        authors = ["Smith, S.R.", "Gordon, A.S."],
        title = u'A study of the pyrolysis of cyclohexene',
        journal = "J. Phys. Chem.",
        volume = "65",
        pages = """1124""",
        year = "1961",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1961SMI/GOR1124:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005509
Bath gas: Cyclohexene
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:33:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1961SMI/GOR1124:2"""),
    ],
)

entry(
    index = 14,
    label = "1957KRA/VAV484:1",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {7,S} {8,S}
2  *2 C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,S} {11,S} {12,S}
4  *6 C 0 {2,S} {6,S} {13,S} {14,S}
5  *4 C 0 {3,S} {6,D} {15,S}
6  *5 C 0 {4,S} {5,D} {16,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {6,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2 *2 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1  *5 C 0 {2,S} {3,D} {5,S}
2  *4 C 0 {1,S} {4,D} {6,S}
3  *6 C 0 {1,D} {7,S} {8,S}
4  *3 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.22e+12,"s^-1"),
        n = 0,
        Ea = (230.311,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (937,"K"),
        Tmax = (1020,"K"),
        Pmin = (933,"Pa"),
        Pmax = (9333,"Pa"),
    ),
    reference = Article(
        authors = ["Kraus, M.", "Vavruska, M.", "Bazant, V."],
        title = u'Diene durch pyrolyse von cyclischen verbindungen. III. Die kinetik der spaltung von cyclohexen und cyclohexylacetat',
        journal = "Collect. Czech. Chem. Commun.",
        volume = "22",
        pages = """484""",
        year = "1957",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1957KRA/VAV484:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005509
Bath gas: H2O
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
    history = [
        ("Fri Jul 13 07:33:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1957KRA/VAV484:1"""),
    ],
)

entry(
    index = 15,
    label = "1939KUC874:3",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {7,S} {8,S}
2  *2 C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,S} {11,S} {12,S}
4  *6 C 0 {2,S} {6,S} {13,S} {14,S}
5  *4 C 0 {3,S} {6,D} {15,S}
6  *5 C 0 {4,S} {5,D} {16,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {6,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2 *2 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1  *5 C 0 {2,S} {3,D} {5,S}
2  *4 C 0 {1,S} {4,D} {6,S}
3  *6 C 0 {1,D} {7,S} {8,S}
4  *3 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (8.89e+12,"s^-1"),
        n = 0,
        Ea = (240.288,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (758,"K"),
        Tmax = (838,"K"),
        Pmin = (1333,"Pa"),
        Pmax = (26700,"Pa"),
    ),
    reference = Article(
        authors = ["Kuchler, L."],
        title = u'Homogenous thermal decomposition of some cyclic hydrocarbons',
        journal = "J. Chem. Soc. Faraday Trans.",
        volume = "35",
        pages = """874""",
        year = "1939",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1939KUC874:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00005509
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00005509/rk00000001.xml
Bath gas: Cyclohexene
Excitation technique: Thermal
Analytical technique: Other
""",
    history = [
        ("Fri Jul 13 07:33:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1939KUC874:3"""),
    ],
)

entry(
    index = 16,
    label = "1986TSA414-418:2",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {5,S} {8,S}
2  *2 C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {7,S} {11,S} {12,S}
4  *6 C 0 {2,S} {6,S} {13,S} {14,S}
5     C 0 {1,S} {15,S} {16,S} {17,S}
6  *5 C 0 {4,S} {7,D} {18,S}
7  *4 C 0 {3,S} {6,D} {19,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {5,S}
17    H 0 {5,S}
18    H 0 {6,S}
19    H 0 {7,S}
""",
    product1 = 
"""
1    C 0 {2,S} {4,S} {5,S} {6,S}
2 *1 C 0 {1,S} {3,D} {7,S}
3 *2 C 0 {2,D} {8,S} {9,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
8    H 0 {3,S}
9    H 0 {3,S}
""",
    product2 = 
"""
1  *4 C 0 {2,S} {3,D} {5,S}
2  *5 C 0 {1,S} {4,D} {6,S}
3  *3 C 0 {1,D} {7,S} {8,S}
4  *6 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2e+15,"s^-1"),
        n = 0,
        Ea = (277.703,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (950,"K"),
        Tmax = (1100,"K"),
        Pmin = (253000,"Pa"),
        Pmax = (811000,"Pa"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Single-pulse shock tube study on the stability of perfluorobromomethane',
        journal = "J. Phys. Chem.",
        volume = "90",
        pages = """414-418""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986TSA414-418:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00007814
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:34:09 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1986TSA414-418:2"""),
    ],
)

entry(
    index = 17,
    label = "1965TSA1805-1809:3",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {5,S} {8,S}
2  *2 C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {7,S} {11,S} {12,S}
4  *6 C 0 {2,S} {6,S} {13,S} {14,S}
5     C 0 {1,S} {15,S} {16,S} {17,S}
6  *5 C 0 {4,S} {7,D} {18,S}
7  *4 C 0 {3,S} {6,D} {19,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {5,S}
17    H 0 {5,S}
18    H 0 {6,S}
19    H 0 {7,S}
""",
    product1 = 
"""
1    C 0 {2,S} {4,S} {5,S} {6,S}
2 *1 C 0 {1,S} {3,D} {7,S}
3 *2 C 0 {2,D} {8,S} {9,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
8    H 0 {3,S}
9    H 0 {3,S}
""",
    product2 = 
"""
1  *4 C 0 {2,S} {3,D} {5,S}
2  *5 C 0 {1,S} {4,D} {6,S}
3  *3 C 0 {1,D} {7,S} {8,S}
4  *6 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.35e+15,"s^-1"),
        n = 0,
        Ea = (278.535,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (900,"K"),
        Tmax = (1150,"K"),
        Pmin = (52500,"Pa"),
        Pmax = (163000,"Pa"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Decyclization of cyclohexene, 4-methylcyclohexene, and 4-vinylcyclohexene in a single-pulse shock tube',
        journal = "J. Chem. Phys.",
        volume = "42",
        pages = """1805-1809""",
        year = "1965",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1965TSA1805-1809:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00007814
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007814/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:34:09 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1965TSA1805-1809:3"""),
    ],
)

entry(
    index = 18,
    label = "1978SIM227:2",
    reactant1 = 
"""
1  *2 C 0 {2,S} {4,S} {8,S} {9,S}
2  *1 C 0 {1,S} {3,S} {10,S} {11,S}
3  *3 C 0 {2,S} {6,S} {12,S} {13,S}
4  *6 C 0 {1,S} {7,S} {14,S} {15,S}
5     C 0 {6,S} {16,S} {17,S} {18,S}
6  *4 C 0 {3,S} {5,S} {7,D}
7  *5 C 0 {4,S} {6,D} {19,S}
8     H 0 {1,S}
9     H 0 {1,S}
10    H 0 {2,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {5,S}
18    H 0 {5,S}
19    H 0 {7,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2 *1 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2  *4 C 0 {1,S} {3,S} {4,D}
3  *5 C 0 {2,S} {5,D} {9,S}
4  *3 C 0 {2,D} {10,S} {11,S}
5  *6 C 0 {3,D} {12,S} {13,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {3,S}
10    H 0 {4,S}
11    H 0 {4,S}
12    H 0 {5,S}
13    H 0 {5,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (3.72e+15,"s^-1"),
        n = 0,
        Ea = (291.007,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (1000,"K"),
        Tmax = (1180,"K"),
        Pmin = (253000,"Pa"),
        Pmax = (253000,"Pa"),
    ),
    reference = Article(
        authors = ["Simmie, J.M."],
        title = u'Kinetic Study of a Retro Diels-Alder Reaction in a Single-Pulse Shock Tube: Decyclization of 1-Methylcyclohex-1-ene',
        journal = "Int. J. Chem. Kinet.",
        volume = "10",
        pages = """227""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978SIM227:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00007816
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007816/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:34:15 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1978SIM227:2"""),
    ],
)

entry(
    index = 19,
    label = "1978SIM227:1",
    reactant1 = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2 *1 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    reactant2 = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2  *4 C 0 {1,S} {3,S} {4,D}
3  *5 C 0 {2,S} {5,D} {9,S}
4  *3 C 0 {2,D} {10,S} {11,S}
5  *6 C 0 {3,D} {12,S} {13,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {3,S}
10    H 0 {4,S}
11    H 0 {4,S}
12    H 0 {5,S}
13    H 0 {5,S}
""",
    product1 = 
"""
1  *2 C 0 {2,S} {4,S} {8,S} {9,S}
2  *1 C 0 {1,S} {3,S} {10,S} {11,S}
3  *3 C 0 {2,S} {6,S} {12,S} {13,S}
4  *6 C 0 {1,S} {7,S} {14,S} {15,S}
5     C 0 {6,S} {16,S} {17,S} {18,S}
6  *4 C 0 {3,S} {5,S} {7,D}
7  *5 C 0 {4,S} {6,D} {19,S}
8     H 0 {1,S}
9     H 0 {1,S}
10    H 0 {2,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {5,S}
18    H 0 {5,S}
19    H 0 {7,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (132000,"m^3/(mol*s)"),
        n = 0,
        Ea = (123.886,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (1000,"K"),
        Tmax = (1180,"K"),
        Pmin = (253000,"Pa"),
        Pmax = (253000,"Pa"),
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
PrIMe Reaction: r00007816
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007816/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:34:15 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1978SIM227:1"""),
    ],
)

entry(
    index = 20,
    label = "1980HUY/RIG253:1",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2 *2 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    reactant2 = 
"""
1     C 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,D} {11,S}
4  *6 C 0 {2,S} {6,D} {12,S}
5  *4 C 0 {3,D} {6,S} {13,S}
6  *5 C 0 {4,D} {5,S} {14,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
""",
    product1 = 
"""
1  *3 C 0 {3,S} {5,S} {7,S} {9,S}
2  *6 C 0 {4,S} {6,S} {8,S} {10,S}
3  *1 C 0 {1,S} {4,S} {11,S} {12,S}
4  *2 C 0 {2,S} {3,S} {13,S} {14,S}
5     C 0 {1,S} {6,S} {15,S} {16,S}
6     C 0 {2,S} {5,S} {17,S} {18,S}
7  *4 C 0 {1,S} {8,D} {19,S}
8  *5 C 0 {2,S} {7,D} {20,S}
9     H 0 {1,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {5,S}
17    H 0 {6,S}
18    H 0 {6,S}
19    H 0 {7,S}
20    H 0 {8,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4570,"m^3/(mol*s)","*|/",1.05),
        n = 0,
        Ea = (108.92,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (466,"K"),
        Tmax = (591,"K"),
        Pmin = (4933,"Pa"),
        Pmax = (25700,"Pa"),
    ),
    reference = Article(
        authors = ["Huybrechts, G.", "Rigaux, D.", "Vankeerberghen, J.", "Van Mele, B."],
        title = u'Kinetics of the Diels-Alder Addition of Ethene to Cyclohexa-1,3-Diene and Its Reverse Reaction in the Gas Phase',
        journal = "Int. J. Chem. Kinet.",
        volume = "12",
        pages = """253""",
        year = "1980",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1980HUY/RIG253:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002185
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002185/rk00000001.xml
Uncertainty: 1.05
Bath gas: C2H4
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:32:35 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1980HUY/RIG253:1"""),
    ],
)

entry(
    index = 21,
    label = "1980HUY/RIG253:2",
    reactant1 = 
"""
1  *3 C 0 {3,S} {5,S} {7,S} {9,S}
2  *6 C 0 {4,S} {6,S} {8,S} {10,S}
3  *1 C 0 {1,S} {4,S} {11,S} {12,S}
4  *2 C 0 {2,S} {3,S} {13,S} {14,S}
5     C 0 {1,S} {6,S} {15,S} {16,S}
6     C 0 {2,S} {5,S} {17,S} {18,S}
7  *4 C 0 {1,S} {8,D} {19,S}
8  *5 C 0 {2,S} {7,D} {20,S}
9     H 0 {1,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {5,S}
17    H 0 {6,S}
18    H 0 {6,S}
19    H 0 {7,S}
20    H 0 {8,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2 *2 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1     C 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,D} {11,S}
4  *6 C 0 {2,S} {6,D} {12,S}
5  *4 C 0 {3,D} {6,S} {13,S}
6  *5 C 0 {4,D} {5,S} {14,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.32e+15,"s^-1","*|/",1.1),
        n = 0,
        Ea = (239.457,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (548,"K"),
        Tmax = (632,"K"),
        Pmin = (533,"Pa"),
        Pmax = (2800,"Pa"),
    ),
    reference = Article(
        authors = ["Huybrechts, G.", "Rigaux, D.", "Vankeerberghen, J.", "Van Mele, B."],
        title = u'Kinetics of the Diels-Alder Addition of Ethene to Cyclohexa-1,3-Diene and Its Reverse Reaction in the Gas Phase',
        journal = "Int. J. Chem. Kinet.",
        volume = "12",
        pages = """253""",
        year = "1980",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1980HUY/RIG253:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002185
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00002185/rk00000001.xml
Uncertainty: 1.1
Bath gas: C2H4
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:32:35 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1980HUY/RIG253:2"""),
    ],
)

entry(
    index = 22,
    label = "1971COC/FRE1661:1",
    reactant1 = 
"""
1  *3 C 0 {3,S} {5,S} {7,S} {9,S}
2  *6 C 0 {4,S} {6,S} {8,S} {10,S}
3  *1 C 0 {1,S} {4,S} {11,S} {12,S}
4  *2 C 0 {2,S} {3,S} {13,S} {14,S}
5     C 0 {1,S} {6,S} {15,S} {16,S}
6     C 0 {2,S} {5,S} {17,S} {18,S}
7  *4 C 0 {1,S} {8,D} {19,S}
8  *5 C 0 {2,S} {7,D} {20,S}
9     H 0 {1,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {5,S}
17    H 0 {6,S}
18    H 0 {6,S}
19    H 0 {7,S}
20    H 0 {8,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2 *2 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1     C 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,D} {11,S}
4  *6 C 0 {2,S} {6,D} {12,S}
5  *4 C 0 {3,D} {6,S} {13,S}
6  *5 C 0 {4,D} {5,S} {14,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.88e+15,"s^-1","*|/",1.12),
        n = 0,
        Ea = (244.445,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (649,"K"),
        Tmax = (718,"K"),
        Pmin = (500,"Pa"),
        Pmax = (2506,"Pa"),
    ),
    reference = Article(
        authors = ["Cocks, A.T.", "Frey, H.M."],
        title = u'Thermal Unimolecular Decomposition of Bicyclo[2.2.2]oct-2-ene',
        journal = "J. Chem. Soc. A",
        pages = """1661""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971COC/FRE1661:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00002185
Uncertainty: 1.12
Bath gas: Bicyclo[2.2.2]oct-2-ene
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:32:35 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1971COC/FRE1661:1"""),
    ],
)

entry(
    index = 23,
    label = "1977HUY/LUY283:3",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,D} {5,S}
2     C 0 {1,S} {4,D} {6,S}
3  *2 C 0 {1,D} {7,S} {8,S}
4     C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    reactant2 = 
"""
1  *4 C 0 {2,S} {3,D} {5,S}
2  *5 C 0 {1,S} {4,D} {6,S}
3  *3 C 0 {1,D} {7,S} {8,S}
4  *6 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    product1 = 
"""
1  *1 C 0 {2,S} {3,S} {5,S} {9,S}
2  *2 C 0 {1,S} {4,S} {10,S} {11,S}
3  *3 C 0 {1,S} {6,S} {12,S} {13,S}
4  *6 C 0 {2,S} {7,S} {14,S} {15,S}
5     C 0 {1,S} {8,D} {16,S}
6  *4 C 0 {3,S} {7,D} {17,S}
7  *5 C 0 {4,S} {6,D} {18,S}
8     C 0 {5,D} {19,S} {20,S}
9     H 0 {1,S}
10    H 0 {2,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {6,S}
18    H 0 {7,S}
19    H 0 {8,S}
20    H 0 {8,S}
""",
    degeneracy = 32,
    kinetics = Arrhenius(
        A = (8910,"m^3/(mol*s)"),
        n = 0,
        Ea = (102.268,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (464,"K"),
        Tmax = (557,"K"),
        Pmin = (6533,"Pa"),
        Pmax = (60000,"Pa"),
    ),
    reference = Article(
        authors = ["Huybrechts, G.", "Luyckx, L.", "Vandenboom, Th.", "Van Mele, B."],
        title = u'Thermal Dimerization of 1,3-Butadiene: Kinetics of the Formation of cis, cis-Cycloocta-1,5-diene',
        journal = "Int. J. Chem. Kinet.",
        volume = "9",
        pages = """283""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977HUY/LUY283:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00004731
Bath gas: 1,3-Butadiene
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:32:47 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1977HUY/LUY283:3"""),
    ],
)

entry(
    index = 24,
    label = "1951ROW/STE198-213:1",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,D} {5,S}
2     C 0 {1,S} {4,D} {6,S}
3  *2 C 0 {1,D} {7,S} {8,S}
4     C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    reactant2 = 
"""
1  *4 C 0 {2,S} {3,D} {5,S}
2  *5 C 0 {1,S} {4,D} {6,S}
3  *3 C 0 {1,D} {7,S} {8,S}
4  *6 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    product1 = 
"""
1  *1 C 0 {2,S} {3,S} {5,S} {9,S}
2  *2 C 0 {1,S} {4,S} {10,S} {11,S}
3  *3 C 0 {1,S} {6,S} {12,S} {13,S}
4  *6 C 0 {2,S} {7,S} {14,S} {15,S}
5     C 0 {1,S} {8,D} {16,S}
6  *4 C 0 {3,S} {7,D} {17,S}
7  *5 C 0 {4,S} {6,D} {18,S}
8     C 0 {5,D} {19,S} {20,S}
9     H 0 {1,S}
10    H 0 {2,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {6,S}
18    H 0 {7,S}
19    H 0 {8,S}
20    H 0 {8,S}
""",
    degeneracy = 32,
    kinetics = Arrhenius(
        A = (138000,"m^3/(mol*s)"),
        n = 0,
        Ea = (112.245,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (673,"K"),
        Tmax = (873,"K"),
        Pmin = (14500,"Pa"),
        Pmax = (101000,"Pa"),
    ),
    reference = Article(
        authors = ["Rowley, D.", "Steiner, H."],
        title = u'Kinetics of diene reactions at high temperatures',
        journal = "Discuss. Faraday Soc.",
        volume = "10",
        pages = """198-213""",
        year = "1951",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1951ROW/STE198-213:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00004731
Bath gas: 1,3-Butadiene
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
    history = [
        ("Fri Jul 13 07:32:47 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1951ROW/STE198-213:1"""),
    ],
)

entry(
    index = 25,
    label = "1932VAU3863-3876:1",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,D} {5,S}
2     C 0 {1,S} {4,D} {6,S}
3  *2 C 0 {1,D} {7,S} {8,S}
4     C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    reactant2 = 
"""
1  *4 C 0 {2,S} {3,D} {5,S}
2  *5 C 0 {1,S} {4,D} {6,S}
3  *3 C 0 {1,D} {7,S} {8,S}
4  *6 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    product1 = 
"""
1  *1 C 0 {2,S} {3,S} {5,S} {9,S}
2  *2 C 0 {1,S} {4,S} {10,S} {11,S}
3  *3 C 0 {1,S} {6,S} {12,S} {13,S}
4  *6 C 0 {2,S} {7,S} {14,S} {15,S}
5     C 0 {1,S} {8,D} {16,S}
6  *4 C 0 {3,S} {7,D} {17,S}
7  *5 C 0 {4,S} {6,D} {18,S}
8     C 0 {5,D} {19,S} {20,S}
9     H 0 {1,S}
10    H 0 {2,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {6,S}
18    H 0 {7,S}
19    H 0 {8,S}
20    H 0 {8,S}
""",
    degeneracy = 32,
    kinetics = Arrhenius(
        A = (47100,"m^3/(mol*s)"),
        n = 0,
        Ea = (108.92,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (653,"K"),
        Tmax = (709,"K"),
        Pmin = (200,"Pa"),
        Pmax = (96000,"Pa"),
    ),
    reference = Article(
        authors = ["Vaughan, W.E."],
        title = u'The homogeneous thermal polymerization of 1,3-butadiene',
        journal = "J. Am. Chem. Soc.",
        volume = "54",
        pages = """3863-3876""",
        year = "1932",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1932VAU3863-3876:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00004731
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004731/rk00000001.xml
Bath gas: 1,3-Butadiene
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
    history = [
        ("Fri Jul 13 07:32:47 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1932VAU3863-3876:1"""),
    ],
)

entry(
    index = 26,
    label = "1977HUY/LUY283:1",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {5,S} {9,S}
2  *2 C 0 {1,S} {4,S} {10,S} {11,S}
3  *3 C 0 {1,S} {6,S} {12,S} {13,S}
4  *6 C 0 {2,S} {7,S} {14,S} {15,S}
5     C 0 {1,S} {8,D} {16,S}
6  *4 C 0 {3,S} {7,D} {17,S}
7  *5 C 0 {4,S} {6,D} {18,S}
8     C 0 {5,D} {19,S} {20,S}
9     H 0 {1,S}
10    H 0 {2,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {6,S}
18    H 0 {7,S}
19    H 0 {8,S}
20    H 0 {8,S}
""",
    product1 = 
"""
1  *1 C 0 {2,S} {3,D} {5,S}
2     C 0 {1,S} {4,D} {6,S}
3  *2 C 0 {1,D} {7,S} {8,S}
4     C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    product2 = 
"""
1  *4 C 0 {2,S} {3,D} {5,S}
2  *5 C 0 {1,S} {4,D} {6,S}
3  *3 C 0 {1,D} {7,S} {8,S}
4  *6 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    degeneracy = 32,
    kinetics = Arrhenius(
        A = (2.51e+14,"s^-1","*|/",3.16),
        n = 0,
        Ea = (251.929,"kJ/mol","+|-",2.519),
        T0 = (1,"K"),
        Tmin = (464,"K"),
        Tmax = (557,"K"),
        Pmin = (6533,"Pa"),
        Pmax = (60000,"Pa"),
    ),
    reference = Article(
        authors = ["Huybrechts, G.", "Luyckx, L.", "Vandenboom, Th.", "Van Mele, B."],
        title = u'Thermal Dimerization of 1,3-Butadiene: Kinetics of the Formation of cis, cis-Cycloocta-1,5-diene',
        journal = "Int. J. Chem. Kinet.",
        volume = "9",
        pages = """283""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977HUY/LUY283:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from detailed balance/reverse rate""",
    longDesc = 
u"""
PrIMe Reaction: r00004731
Uncertainty: 3.1600001
""",
    history = [
        ("Fri Jul 13 07:32:47 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1977HUY/LUY283:1"""),
    ],
)

entry(
    index = 27,
    label = "1976BAR/PAR2404:1",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {5,S} {9,S}
2  *2 C 0 {1,S} {4,S} {10,S} {11,S}
3  *3 C 0 {1,S} {6,S} {12,S} {13,S}
4  *6 C 0 {2,S} {7,S} {14,S} {15,S}
5     C 0 {1,S} {8,D} {16,S}
6  *4 C 0 {3,S} {7,D} {17,S}
7  *5 C 0 {4,S} {6,D} {18,S}
8     C 0 {5,D} {19,S} {20,S}
9     H 0 {1,S}
10    H 0 {2,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {6,S}
18    H 0 {7,S}
19    H 0 {8,S}
20    H 0 {8,S}
""",
    product1 = 
"""
1  *1 C 0 {2,S} {3,D} {5,S}
2     C 0 {1,S} {4,D} {6,S}
3  *2 C 0 {1,D} {7,S} {8,S}
4     C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    product2 = 
"""
1  *4 C 0 {2,S} {3,D} {5,S}
2  *5 C 0 {1,S} {4,D} {6,S}
3  *3 C 0 {1,D} {7,S} {8,S}
4  *6 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    degeneracy = 32,
    kinetics = Arrhenius(
        A = (6.17e+15,"s^-1","*|/",1.55),
        n = 0,
        Ea = (261.906,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (927,"K"),
        Tmax = (1050,"K"),
        Pmin = (193000,"Pa"),
        Pmax = (247000,"Pa"),
    ),
    reference = Article(
        authors = ["Barnard, J.A.", "Parrott, T.K."],
        title = u'Kinetics of the thermal unimolecular reactions of cyclohexene and 4-vinylcyclohexene behind reflected shock waves',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "72",
        pages = """2404""",
        year = "1976",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976BAR/PAR2404:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00004731
Uncertainty: 1.55
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:32:47 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1976BAR/PAR2404:1"""),
    ],
)

entry(
    index = 28,
    label = "1965TSA1805-1809:1",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {5,S} {9,S}
2  *2 C 0 {1,S} {4,S} {10,S} {11,S}
3  *3 C 0 {1,S} {6,S} {12,S} {13,S}
4  *6 C 0 {2,S} {7,S} {14,S} {15,S}
5     C 0 {1,S} {8,D} {16,S}
6  *4 C 0 {3,S} {7,D} {17,S}
7  *5 C 0 {4,S} {6,D} {18,S}
8     C 0 {5,D} {19,S} {20,S}
9     H 0 {1,S}
10    H 0 {2,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {6,S}
18    H 0 {7,S}
19    H 0 {8,S}
20    H 0 {8,S}
""",
    product1 = 
"""
1  *1 C 0 {2,S} {3,D} {5,S}
2     C 0 {1,S} {4,D} {6,S}
3  *2 C 0 {1,D} {7,S} {8,S}
4     C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    product2 = 
"""
1  *4 C 0 {2,S} {3,D} {5,S}
2  *5 C 0 {1,S} {4,D} {6,S}
3  *3 C 0 {1,D} {7,S} {8,S}
4  *6 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    degeneracy = 32,
    kinetics = Arrhenius(
        A = (1.58e+15,"s^-1"),
        n = 0,
        Ea = (259.412,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (900,"K"),
        Tmax = (1050,"K"),
        Pmin = (52500,"Pa"),
        Pmax = (163000,"Pa"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Decyclization of cyclohexene, 4-methylcyclohexene, and 4-vinylcyclohexene in a single-pulse shock tube',
        journal = "J. Chem. Phys.",
        volume = "42",
        pages = """1805-1809""",
        year = "1965",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1965TSA1805-1809:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00004731
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:32:47 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1965TSA1805-1809:1"""),
    ],
)

entry(
    index = 29,
    label = "1952DUN/JAN1644-1645:1",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {5,S} {9,S}
2  *2 C 0 {1,S} {4,S} {10,S} {11,S}
3  *3 C 0 {1,S} {6,S} {12,S} {13,S}
4  *6 C 0 {2,S} {7,S} {14,S} {15,S}
5     C 0 {1,S} {8,D} {16,S}
6  *4 C 0 {3,S} {7,D} {17,S}
7  *5 C 0 {4,S} {6,D} {18,S}
8     C 0 {5,D} {19,S} {20,S}
9     H 0 {1,S}
10    H 0 {2,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {6,S}
18    H 0 {7,S}
19    H 0 {8,S}
20    H 0 {8,S}
""",
    product1 = 
"""
1  *1 C 0 {2,S} {3,D} {5,S}
2     C 0 {1,S} {4,D} {6,S}
3  *2 C 0 {1,D} {7,S} {8,S}
4     C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    product2 = 
"""
1  *4 C 0 {2,S} {3,D} {5,S}
2  *5 C 0 {1,S} {4,D} {6,S}
3  *3 C 0 {1,D} {7,S} {8,S}
4  *6 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    degeneracy = 32,
    kinetics = Arrhenius(
        A = (5.02e+15,"s^-1"),
        n = 0,
        Ea = (258.58,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (600,"K"),
        Tmax = (1000,"K"),
    ),
    reference = Article(
        authors = ["Duncan, N.E.", "Janz, G.J."],
        title = u'The thermal dimerization of butadiene, and the equilibrium between butadiene and vinylcyclohexene',
        journal = "J. Chem. Phys.",
        volume = "20",
        pages = """1644-1645""",
        year = "1952",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1952DUN/JAN1644-1645:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from detailed balance/reverse rate""",
    longDesc = 
u"""
PrIMe Reaction: r00004731
Bath gas: 4-Vinylcyclohexene
""",
    history = [
        ("Fri Jul 13 07:32:47 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1952DUN/JAN1644-1645:1"""),
    ],
)

entry(
    index = 30,
    label = "1936KIS/LAC123-133:2",
    reactant1 = 
"""
1  *4 C 0 {2,S} {3,D} {5,S}
2  *5 C 0 {1,S} {4,D} {6,S}
3  *3 C 0 {1,D} {7,S} {8,S}
4  *6 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    reactant2 = 
"""
1 *1 C 0 {2,D} {3,S} {5,S}
2 *2 C 0 {1,D} {6,S} {7,S}
3    C 0 {1,S} {4,D} {8,S}
4    O 0 {3,D}
5    H 0 {1,S}
6    H 0 {2,S}
7    H 0 {2,S}
8    H 0 {3,S}
""",
    product1 = 
"""
1  *1 C 0 {2,S} {3,S} {7,S} {9,S}
2  *2 C 0 {1,S} {4,S} {10,S} {11,S}
3  *3 C 0 {1,S} {5,S} {12,S} {13,S}
4  *6 C 0 {2,S} {6,S} {14,S} {15,S}
5  *4 C 0 {3,S} {6,D} {16,S}
6  *5 C 0 {4,S} {5,D} {17,S}
7     C 0 {1,S} {8,D} {18,S}
8     O 0 {7,D}
9     H 0 {1,S}
10    H 0 {2,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {6,S}
18    H 0 {7,S}
""",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (1460,"m^3/(mol*s)"),
        n = 0,
        Ea = (82.396,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (428,"K"),
        Tmax = (605,"K"),
        Pmin = (31600,"Pa"),
        Pmax = (87700,"Pa"),
    ),
    reference = Article(
        authors = ["Kistiakowsky, G.B.", "Lacher, J.R."],
        title = u'The kinetics of some gaseous diels-alder reactions',
        journal = "J. Am. Chem. Soc.",
        volume = "58",
        pages = """123-133""",
        year = "1936",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1936KIS/LAC123-133:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00004734
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004734/rk00000001.xml
Bath gas: CH2=CHCHO
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
    history = [
        ("Fri Jul 13 07:33:04 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1936KIS/LAC123-133:2"""),
    ],
)

entry(
    index = 31,
    label = "1986ROB/TSA5363-5367:4",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {9,S} {10,S}
2  *2 C 0 {1,S} {4,S} {11,S} {12,S}
3  *3 C 0 {1,S} {7,S} {13,S} {14,S}
4  *6 C 0 {2,S} {8,S} {15,S} {16,S}
5     C 0 {7,S} {17,S} {18,S} {19,S}
6     C 0 {8,S} {20,S} {21,S} {22,S}
7  *4 C 0 {3,S} {5,S} {8,D}
8  *5 C 0 {4,S} {6,S} {7,D}
9     H 0 {1,S}
10    H 0 {1,S}
11    H 0 {2,S}
12    H 0 {2,S}
13    H 0 {3,S}
14    H 0 {3,S}
15    H 0 {4,S}
16    H 0 {4,S}
17    H 0 {5,S}
18    H 0 {5,S}
19    H 0 {5,S}
20    H 0 {6,S}
21    H 0 {6,S}
22    H 0 {6,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2 *2 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1     C 0 {3,S} {7,S} {8,S} {9,S}
2     C 0 {4,S} {10,S} {11,S} {12,S}
3  *5 C 0 {1,S} {4,S} {5,D}
4  *4 C 0 {2,S} {3,S} {6,D}
5  *6 C 0 {3,D} {13,S} {14,S}
6  *3 C 0 {4,D} {15,S} {16,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {1,S}
10    H 0 {2,S}
11    H 0 {2,S}
12    H 0 {2,S}
13    H 0 {5,S}
14    H 0 {5,S}
15    H 0 {6,S}
16    H 0 {6,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (3.2e+15,"s^-1"),
        n = 0,
        Ea = (292.669,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (1050,"K"),
        Tmax = (1200,"K"),
        Pmin = (203000,"Pa"),
        Pmax = (608000,"Pa"),
    ),
    reference = Article(
        authors = ["Robaugh, D.", "Tsang, W."],
        title = u'Thermal decomposition of phenyl iodide and o-iodotoluene',
        journal = "J. Phys. Chem.",
        volume = "90",
        pages = """5363-5367""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986ROB/TSA5363-5367:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00009910
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009910/rk00000001.xml
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:34:30 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1986ROB/TSA5363-5367:4"""),
    ],
)

entry(
    index = 32,
    label = "1986VAN/BOO537:1",
    reactant1 = 
"""
1     C 0 {2,S} {4,S} {7,S} {10,S}
2  *3 C 0 {1,S} {6,S} {9,S} {11,S}
3  *6 C 0 {4,S} {5,S} {8,S} {12,S}
4     C 0 {1,S} {3,S} {13,S} {14,S}
5  *2 C 0 {3,S} {6,S} {15,S} {16,S}
6  *1 C 0 {2,S} {5,S} {17,S} {18,S}
7     C 0 {1,S} {19,S} {20,S} {21,S}
8  *5 C 0 {3,S} {9,D} {22,S}
9  *4 C 0 {2,S} {8,D} {23,S}
10    H 0 {1,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {5,S}
17    H 0 {6,S}
18    H 0 {6,S}
19    H 0 {7,S}
20    H 0 {7,S}
21    H 0 {7,S}
22    H 0 {8,S}
23    H 0 {9,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2 *1 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1     C 0 {2,S} {3,S} {4,S} {8,S}
2     C 0 {1,S} {5,S} {9,S} {10,S}
3     C 0 {1,S} {11,S} {12,S} {13,S}
4  *3 C 0 {1,S} {6,D} {14,S}
5  *6 C 0 {2,S} {7,D} {15,S}
6  *4 C 0 {4,D} {7,S} {16,S}
7  *5 C 0 {5,D} {6,S} {17,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {6,S}
17    H 0 {7,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.17e+14,"s^-1","*|/",1.05),
        n = 0,
        Ea = (241.951,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (567,"K"),
        Tmax = (670,"K"),
        Pmin = (400,"Pa"),
        Pmax = (1067,"Pa"),
    ),
    reference = Article(
        authors = ["van Mele, B.", "Boon, G.", "Huybrechts, G."],
        title = u'Gas phase kinetic and thermochemical data for endo- and exo-5-monosubstituted bicyclo[2.2.2]oct-2-enes',
        journal = "Int. J. Chem. Kinet.",
        volume = "18",
        pages = """537""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986VAN/BOO537:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015550
Uncertainty: 1.05
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:34:33 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1986VAN/BOO537:1"""),
    ],
)

entry(
    index = 33,
    label = "1975HUY/NGO775:1",
    reactant1 = 
"""
1     C 0 {2,S} {4,S} {7,S} {10,S}
2  *3 C 0 {1,S} {6,S} {9,S} {11,S}
3  *6 C 0 {4,S} {5,S} {8,S} {12,S}
4     C 0 {1,S} {3,S} {13,S} {14,S}
5  *2 C 0 {3,S} {6,S} {15,S} {16,S}
6  *1 C 0 {2,S} {5,S} {17,S} {18,S}
7     C 0 {1,S} {19,S} {20,S} {21,S}
8  *5 C 0 {3,S} {9,D} {22,S}
9  *4 C 0 {2,S} {8,D} {23,S}
10    H 0 {1,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {5,S}
17    H 0 {6,S}
18    H 0 {6,S}
19    H 0 {7,S}
20    H 0 {7,S}
21    H 0 {7,S}
22    H 0 {8,S}
23    H 0 {9,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2 *1 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1     C 0 {2,S} {3,S} {4,S} {8,S}
2     C 0 {1,S} {5,S} {9,S} {10,S}
3     C 0 {1,S} {11,S} {12,S} {13,S}
4  *3 C 0 {1,S} {6,D} {14,S}
5  *6 C 0 {2,S} {7,D} {15,S}
6  *4 C 0 {4,D} {7,S} {16,S}
7  *5 C 0 {5,D} {6,S} {17,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {6,S}
17    H 0 {7,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.2e+14,"s^-1","*|/",1.07),
        n = 0,
        Ea = (233.637,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (608,"K"),
        Tmax = (679,"K"),
        Pmin = (933,"Pa"),
        Pmax = (4933,"Pa"),
    ),
    reference = Article(
        authors = ["Huybrechts, G.", "Ngoy, G."],
        title = u'Kinetics of the Pyrolysis of Endo- and Exo-5-Methylbicyclo[2.2.2]oct-2-ene in the Gas Phase',
        journal = "Int. J. Chem. Kinet.",
        volume = "8",
        pages = """775""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975HUY/NGO775:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015550
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015550/rk00000001.xml
Uncertainty: 1.0700001
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:34:33 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1975HUY/NGO775:1"""),
    ],
)

entry(
    index = 34,
    label = "1986VAN/BOO537:2",
    reactant1 = 
"""
1  *1 C 0 {2,S} {4,S} {7,S} {10,S}
2  *3 C 0 {1,S} {6,S} {9,S} {11,S}
3  *6 C 0 {4,S} {5,S} {8,S} {12,S}
4  *2 C 0 {1,S} {3,S} {13,S} {14,S}
5     C 0 {3,S} {6,S} {15,S} {16,S}
6     C 0 {2,S} {5,S} {17,S} {18,S}
7     C 0 {1,S} {19,S} {20,S} {21,S}
8  *5 C 0 {3,S} {9,D} {22,S}
9  *4 C 0 {2,S} {8,D} {23,S}
10    H 0 {1,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {5,S}
17    H 0 {6,S}
18    H 0 {6,S}
19    H 0 {7,S}
20    H 0 {7,S}
21    H 0 {7,S}
22    H 0 {8,S}
23    H 0 {9,S}
""",
    product1 = 
"""
1    C 0 {2,S} {4,S} {5,S} {6,S}
2 *1 C 0 {1,S} {3,D} {7,S}
3 *2 C 0 {2,D} {8,S} {9,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
8    H 0 {3,S}
9    H 0 {3,S}
""",
    product2 = 
"""
1     C 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,D} {11,S}
4  *6 C 0 {2,S} {6,D} {12,S}
5  *4 C 0 {3,D} {6,S} {13,S}
6  *5 C 0 {4,D} {5,S} {14,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.15e+15,"s^-1","*|/",1.05),
        n = 0,
        Ea = (243.614,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (567,"K"),
        Tmax = (670,"K"),
        Pmin = (400,"Pa"),
        Pmax = (1067,"Pa"),
    ),
    reference = Article(
        authors = ["van Mele, B.", "Boon, G.", "Huybrechts, G."],
        title = u'Gas phase kinetic and thermochemical data for endo- and exo-5-monosubstituted bicyclo[2.2.2]oct-2-enes',
        journal = "Int. J. Chem. Kinet.",
        volume = "18",
        pages = """537""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986VAN/BOO537:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015551
Uncertainty: 1.05
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:34:38 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1986VAN/BOO537:2"""),
    ],
)

entry(
    index = 35,
    label = "1975HUY/NGO775:2",
    reactant1 = 
"""
1  *1 C 0 {2,S} {4,S} {7,S} {10,S}
2  *3 C 0 {1,S} {6,S} {9,S} {11,S}
3  *6 C 0 {4,S} {5,S} {8,S} {12,S}
4  *2 C 0 {1,S} {3,S} {13,S} {14,S}
5     C 0 {3,S} {6,S} {15,S} {16,S}
6     C 0 {2,S} {5,S} {17,S} {18,S}
7     C 0 {1,S} {19,S} {20,S} {21,S}
8  *5 C 0 {3,S} {9,D} {22,S}
9  *4 C 0 {2,S} {8,D} {23,S}
10    H 0 {1,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {5,S}
17    H 0 {6,S}
18    H 0 {6,S}
19    H 0 {7,S}
20    H 0 {7,S}
21    H 0 {7,S}
22    H 0 {8,S}
23    H 0 {9,S}
""",
    product1 = 
"""
1    C 0 {2,S} {4,S} {5,S} {6,S}
2 *1 C 0 {1,S} {3,D} {7,S}
3 *2 C 0 {2,D} {8,S} {9,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
8    H 0 {3,S}
9    H 0 {3,S}
""",
    product2 = 
"""
1     C 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,D} {11,S}
4  *6 C 0 {2,S} {6,D} {12,S}
5  *4 C 0 {3,D} {6,S} {13,S}
6  *5 C 0 {4,D} {5,S} {14,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.74e+14,"s^-1","*|/",1.05),
        n = 0,
        Ea = (234.468,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (608,"K"),
        Tmax = (679,"K"),
        Pmin = (933,"Pa"),
        Pmax = (4933,"Pa"),
    ),
    reference = Article(
        authors = ["Huybrechts, G.", "Ngoy, G."],
        title = u'Kinetics of the Pyrolysis of Endo- and Exo-5-Methylbicyclo[2.2.2]oct-2-ene in the Gas Phase',
        journal = "Int. J. Chem. Kinet.",
        volume = "8",
        pages = """775""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975HUY/NGO775:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015551
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015551/rk00000001.xml
Uncertainty: 1.05
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:34:38 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1975HUY/NGO775:2"""),
    ],
)

entry(
    index = 36,
    label = "1984HUY/POP93:3",
    reactant1 = 
"""
1    C 0 {2,S} {4,S} {5,S} {6,S}
2 *1 C 0 {1,S} {3,D} {7,S}
3 *2 C 0 {2,D} {8,S} {9,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
8    H 0 {3,S}
9    H 0 {3,S}
""",
    reactant2 = 
"""
1     C 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,D} {11,S}
4  *6 C 0 {2,S} {6,D} {12,S}
5  *4 C 0 {3,D} {6,S} {13,S}
6  *5 C 0 {4,D} {5,S} {14,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
""",
    product1 = 
"""
1  *1 C 0 {2,S} {4,S} {7,S} {10,S}
2  *3 C 0 {1,S} {6,S} {9,S} {11,S}
3  *6 C 0 {4,S} {5,S} {8,S} {12,S}
4  *2 C 0 {1,S} {3,S} {13,S} {14,S}
5     C 0 {3,S} {6,S} {15,S} {16,S}
6     C 0 {2,S} {5,S} {17,S} {18,S}
7     C 0 {1,S} {19,S} {20,S} {21,S}
8  *5 C 0 {3,S} {9,D} {22,S}
9  *4 C 0 {2,S} {8,D} {23,S}
10    H 0 {1,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {5,S}
17    H 0 {6,S}
18    H 0 {6,S}
19    H 0 {7,S}
20    H 0 {7,S}
21    H 0 {7,S}
22    H 0 {8,S}
23    H 0 {9,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1120,"m^3/(mol*s)"),
        n = 0,
        Ea = (111.414,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (488,"K"),
        Tmax = (606,"K"),
        Pmin = (7599,"Pa"),
        Pmax = (83300,"Pa"),
    ),
    reference = Article(
        authors = ["Huybrechts, G.", "Poppelsdorf, H.", "Maesschalck, L.", "Van Mele, B."],
        title = u'Kinetics, mechanism, and endo selectivity of diels-alder reactions of alkylmonosubstituted ethenes with cyclohexa-1,3-diene in the gas phase',
        journal = "Int. J. Chem. Kinet.",
        volume = "16",
        pages = """93""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984HUY/POP93:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015551
Bath gas: 1,3-Cyclohexadiene
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:34:39 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1984HUY/POP93:3"""),
    ],
)

entry(
    index = 37,
    label = "1974DEB/HUY545:1",
    reactant1 = 
"""
1    C 0 {2,S} {4,S} {5,S} {6,S}
2 *1 C 0 {1,S} {3,D} {7,S}
3 *2 C 0 {2,D} {8,S} {9,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
8    H 0 {3,S}
9    H 0 {3,S}
""",
    reactant2 = 
"""
1     C 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,D} {11,S}
4  *6 C 0 {2,S} {6,D} {12,S}
5  *4 C 0 {3,D} {6,S} {13,S}
6  *5 C 0 {4,D} {5,S} {14,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
""",
    product1 = 
"""
1  *1 C 0 {2,S} {4,S} {7,S} {10,S}
2  *3 C 0 {1,S} {6,S} {9,S} {11,S}
3  *6 C 0 {4,S} {5,S} {8,S} {12,S}
4  *2 C 0 {1,S} {3,S} {13,S} {14,S}
5     C 0 {3,S} {6,S} {15,S} {16,S}
6     C 0 {2,S} {5,S} {17,S} {18,S}
7     C 0 {1,S} {19,S} {20,S} {21,S}
8  *5 C 0 {3,S} {9,D} {22,S}
9  *4 C 0 {2,S} {8,D} {23,S}
10    H 0 {1,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {5,S}
17    H 0 {6,S}
18    H 0 {6,S}
19    H 0 {7,S}
20    H 0 {7,S}
21    H 0 {7,S}
22    H 0 {8,S}
23    H 0 {9,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (550,"m^3/(mol*s)","*|/",1.07),
        n = 0,
        Ea = (108.92,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (512,"K"),
        Tmax = (638,"K"),
        Pmin = (9333,"Pa"),
        Pmax = (85300,"Pa"),
    ),
    reference = Article(
        authors = ["Debande, G.", "Huybrechts, G."],
        title = u'Kinetics of the Addition of Propene to Cyclohexa-1,3-Diene in the Gas Phase',
        journal = "Int. J. Chem. Kinet.",
        volume = "6",
        pages = """545""",
        year = "1974",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1974DEB/HUY545:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00015551
Uncertainty: 1.0700001
Bath gas: CH3CH=CH2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:34:39 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1974DEB/HUY545:1"""),
    ],
)

entry(
    index = 38,
    label = "1936KIS/LAC123-133:1",
    reactant1 = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2  *4 C 0 {1,S} {3,S} {4,D}
3  *5 C 0 {2,S} {5,D} {9,S}
4  *3 C 0 {2,D} {10,S} {11,S}
5  *6 C 0 {3,D} {12,S} {13,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {3,S}
10    H 0 {4,S}
11    H 0 {4,S}
12    H 0 {5,S}
13    H 0 {5,S}
""",
    reactant2 = 
"""
1 *2 C 0 {2,D} {3,S} {5,S}
2 *1 C 0 {1,D} {6,S} {7,S}
3    C 0 {1,S} {4,D} {8,S}
4    O 0 {3,D}
5    H 0 {1,S}
6    H 0 {2,S}
7    H 0 {2,S}
8    H 0 {3,S}
""",
    product1 = 
"""
1  *2 C 0 {2,S} {4,S} {8,S} {10,S}
2  *1 C 0 {1,S} {3,S} {11,S} {12,S}
3  *3 C 0 {2,S} {6,S} {13,S} {14,S}
4  *6 C 0 {1,S} {7,S} {15,S} {16,S}
5     C 0 {6,S} {17,S} {18,S} {19,S}
6  *4 C 0 {3,S} {5,S} {7,D}
7  *5 C 0 {4,S} {6,D} {20,S}
8     C 0 {1,S} {9,D} {21,S}
9     O 0 {8,D}
10    H 0 {1,S}
11    H 0 {2,S}
12    H 0 {2,S}
13    H 0 {3,S}
14    H 0 {3,S}
15    H 0 {4,S}
16    H 0 {4,S}
17    H 0 {5,S}
18    H 0 {5,S}
19    H 0 {5,S}
20    H 0 {7,S}
21    H 0 {8,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1020,"m^3/(mol*s)"),
        n = 0,
        Ea = (78.239,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (492,"K"),
        Tmax = (606,"K"),
        Pmin = (20400,"Pa"),
        Pmax = (82700,"Pa"),
    ),
    reference = Article(
        authors = ["Kistiakowsky, G.B.", "Lacher, J.R."],
        title = u'The kinetics of some gaseous diels-alder reactions',
        journal = "J. Am. Chem. Soc.",
        volume = "58",
        pages = """123-133""",
        year = "1936",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1936KIS/LAC123-133:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00003841
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00003841/rk00000001.xml
Bath gas: CH2=CHCHO
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
    history = [
        ("Tue Jul 24 15:41:23 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1936KIS/LAC123-133:1"""),
    ],
)

entry(
    index = 39,
    label = "1936KIS/LAC123-133:3",
    reactant1 = 
"""
1  *4 C 0 {2,S} {3,D} {5,S}
2  *5 C 0 {1,S} {4,D} {6,S}
3  *3 C 0 {1,D} {7,S} {8,S}
4  *6 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    reactant2 = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2  *1 C 0 {1,S} {3,D} {9,S}
3  *2 C 0 {2,D} {4,S} {10,S}
4     C 0 {3,S} {5,D} {11,S}
5     O 0 {4,D}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
""",
    product1 = 
"""
1  *1 C 0 {2,S} {3,S} {5,S} {10,S}
2  *2 C 0 {1,S} {4,S} {8,S} {11,S}
3  *3 C 0 {1,S} {6,S} {12,S} {13,S}
4  *6 C 0 {2,S} {7,S} {14,S} {15,S}
5     C 0 {1,S} {16,S} {17,S} {18,S}
6  *4 C 0 {3,S} {7,D} {19,S}
7  *5 C 0 {4,S} {6,D} {20,S}
8     C 0 {2,S} {9,D} {21,S}
9     O 0 {8,D}
10    H 0 {1,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {5,S}
18    H 0 {5,S}
19    H 0 {6,S}
20    H 0 {7,S}
21    H 0 {8,S}
""",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (899,"m^3/(mol*s)"),
        n = 0,
        Ea = (92.291,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (515,"K"),
        Tmax = (572,"K"),
        Pmin = (64500,"Pa"),
        Pmax = (78900,"Pa"),
    ),
    reference = Article(
        authors = ["Kistiakowsky, G.B.", "Lacher, J.R."],
        title = u'The kinetics of some gaseous diels-alder reactions',
        journal = "J. Am. Chem. Soc.",
        volume = "58",
        pages = """123-133""",
        year = "1936",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1936KIS/LAC123-133:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00004794
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004794/rk00000001.xml
Bath gas: (Z)-CH3CH=CHCHO
Excitation technique: Thermal
Analytical technique: Other (direct)
""",
    history = [
        ("Tue Jul 24 15:52:38 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1936KIS/LAC123-133:3"""),
    ],
)

entry(
    index = 40,
    label = "1976HUY/PAT641:3",
    reactant1 = 
"""
1  *3 C 0 {2,S} {5,S} {7,S} {11,S}
2  *1 C 0 {1,S} {4,S} {9,S} {12,S}
3  *6 C 0 {4,S} {6,S} {8,S} {13,S}
4  *2 C 0 {2,S} {3,S} {14,S} {15,S}
5     C 0 {1,S} {6,S} {16,S} {17,S}
6     C 0 {3,S} {5,S} {18,S} {19,S}
7  *4 C 0 {1,S} {8,D} {20,S}
8  *5 C 0 {3,S} {7,D} {21,S}
9     C 0 {2,S} {10,D} {22,S}
10    O 0 {9,D}
11    H 0 {1,S}
12    H 0 {2,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {5,S}
18    H 0 {6,S}
19    H 0 {6,S}
20    H 0 {7,S}
21    H 0 {8,S}
22    H 0 {9,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S} {5,S}
2 *2 C 0 {1,D} {6,S} {7,S}
3    C 0 {1,S} {4,D} {8,S}
4    O 0 {3,D}
5    H 0 {1,S}
6    H 0 {2,S}
7    H 0 {2,S}
8    H 0 {3,S}
""",
    product2 = 
"""
1     C 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,D} {11,S}
4  *6 C 0 {2,S} {6,D} {12,S}
5  *4 C 0 {3,D} {6,S} {13,S}
6  *5 C 0 {4,D} {5,S} {14,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (9.55e+12,"s^-1","*|/",1.1),
        n = 0,
        Ea = (193.727,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (565,"K"),
        Tmax = (638,"K"),
        Pmin = (800,"Pa"),
        Pmax = (5066,"Pa"),
    ),
    reference = Article(
        authors = ["Huybrechts, G.", "Paternoster, G.", "Baetens, P."],
        title = u'Kinetics of the Diels-Alder Addition of Acrolein to Cyclohexa-1,3-diene and Its Reverse Reaction in the Gas Phase',
        journal = "Int. J. Chem. Kinet.",
        volume = "8",
        pages = """641""",
        year = "1976",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1976HUY/PAT641:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00004843
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004843/rk00000001.xml
Uncertainty: 1.1
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
    history = [
        ("Fri Jul 13 07:33:20 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1976HUY/PAT641:3"""),
    ],
)

entry(
    index = 41,
    label = "1990OND/ZIM547-550:1",
    reactant1 = 
"""
1  *1 C 0 {2,S} {5,S} {11,S} {12,S}
2  *2 C 0 {1,S} {6,S} {13,S} {14,S}
3     C 0 {4,S} {7,S} {15,S} {16,S}
4     C 0 {3,S} {8,S} {17,S} {18,S}
5  *3 C 0 {1,S} {9,S} {19,S} {20,S}
6  *6 C 0 {2,S} {10,S} {21,S} {22,S}
7     C 0 {3,S} {9,S} {23,S} {24,S}
8     C 0 {4,S} {10,S} {25,S} {26,S}
9  *4 C 0 {5,S} {7,S} {10,D}
10 *5 C 0 {6,S} {8,S} {9,D}
11    H 0 {1,S}
12    H 0 {1,S}
13    H 0 {2,S}
14    H 0 {2,S}
15    H 0 {3,S}
16    H 0 {3,S}
17    H 0 {4,S}
18    H 0 {4,S}
19    H 0 {5,S}
20    H 0 {5,S}
21    H 0 {6,S}
22    H 0 {6,S}
23    H 0 {7,S}
24    H 0 {7,S}
25    H 0 {8,S}
26    H 0 {8,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2 *2 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1     C 0 {2,S} {3,S} {9,S} {10,S}
2     C 0 {1,S} {4,S} {11,S} {12,S}
3     C 0 {1,S} {5,S} {13,S} {14,S}
4     C 0 {2,S} {6,S} {15,S} {16,S}
5  *5 C 0 {3,S} {6,S} {7,D}
6  *4 C 0 {4,S} {5,S} {8,D}
7  *6 C 0 {5,D} {17,S} {18,S}
8  *3 C 0 {6,D} {19,S} {20,S}
9     H 0 {1,S}
10    H 0 {1,S}
11    H 0 {2,S}
12    H 0 {2,S}
13    H 0 {3,S}
14    H 0 {3,S}
15    H 0 {4,S}
16    H 0 {4,S}
17    H 0 {7,S}
18    H 0 {7,S}
19    H 0 {8,S}
20    H 0 {8,S}
""",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (5.13e+14,"s^-1","*|/",50),
        n = 0,
        Ea = (260.243,"kJ/mol","+|-",5.197),
        T0 = (1,"K"),
        Tmin = (773,"K"),
        Tmax = (998,"K"),
        Pmin = (101000,"Pa"),
        Pmax = (101000,"Pa"),
    ),
    reference = Article(
        authors = ["Ondruschka, B.", "Zimmermann, G."],
        title = u'Pyrolysis kinetics of octalins',
        journal = "J. Prakt. Chem.",
        volume = "332",
        pages = """547-550""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990OND/ZIM547-550:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00007108
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007108/rk00000001.xml
Uncertainty: 50.0
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:34:07 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1990OND/ZIM547-550:1"""),
    ],
)

entry(
    index = 42,
    label = "1990OND/ZIM547-550:2",
    reactant1 = 
"""
1  *6 C 0 {2,S} {3,S} {9,S} {11,S}
2  *2 C 0 {1,S} {5,S} {12,S} {13,S}
3     C 0 {1,S} {4,S} {14,S} {15,S}
4     C 0 {3,S} {6,S} {16,S} {17,S}
5  *1 C 0 {2,S} {8,S} {18,S} {19,S}
6     C 0 {4,S} {7,S} {20,S} {21,S}
7     C 0 {6,S} {9,S} {22,S} {23,S}
8  *3 C 0 {5,S} {10,S} {24,S} {25,S}
9  *5 C 0 {1,S} {7,S} {10,D}
10 *4 C 0 {8,S} {9,D} {26,S}
11    H 0 {1,S}
12    H 0 {2,S}
13    H 0 {2,S}
14    H 0 {3,S}
15    H 0 {3,S}
16    H 0 {4,S}
17    H 0 {4,S}
18    H 0 {5,S}
19    H 0 {5,S}
20    H 0 {6,S}
21    H 0 {6,S}
22    H 0 {7,S}
23    H 0 {7,S}
24    H 0 {8,S}
25    H 0 {8,S}
26    H 0 {10,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2 *1 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1     C 0 {2,S} {3,S} {9,S} {10,S}
2     C 0 {1,S} {4,S} {11,S} {12,S}
3     C 0 {1,S} {5,S} {13,S} {14,S}
4     C 0 {2,S} {6,S} {15,S} {16,S}
5  *5 C 0 {3,S} {6,D} {7,S}
6  *6 C 0 {4,S} {5,D} {17,S}
7  *4 C 0 {5,S} {8,D} {18,S}
8  *3 C 0 {7,D} {19,S} {20,S}
9     H 0 {1,S}
10    H 0 {1,S}
11    H 0 {2,S}
12    H 0 {2,S}
13    H 0 {3,S}
14    H 0 {3,S}
15    H 0 {4,S}
16    H 0 {4,S}
17    H 0 {6,S}
18    H 0 {7,S}
19    H 0 {8,S}
20    H 0 {8,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.17e+13,"s^-1","*|/",10),
        n = 0,
        Ea = (239.457,"kJ/mol","+|-",35.835),
        T0 = (1,"K"),
        Tmin = (773,"K"),
        Tmax = (998,"K"),
        Pmin = (101000,"Pa"),
        Pmax = (101000,"Pa"),
    ),
    reference = Article(
        authors = ["Ondruschka, B.", "Zimmermann, G."],
        title = u'Pyrolysis kinetics of octalins',
        journal = "J. Prakt. Chem.",
        volume = "332",
        pages = """547-550""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990OND/ZIM547-550:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009426
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009426/rk00000001.xml
Uncertainty: 10.0
Bath gas: Ar
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:34:28 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1990OND/ZIM547-550:2"""),
    ],
)

entry(
    index = 43,
    label = "1982HUY/HUB251:1",
    reactant1 = 
"""
1  *1 C 0 {2,S} {4,S} {9,S} {11,S}
2  *3 C 0 {1,S} {6,S} {8,S} {12,S}
3  *6 C 0 {4,S} {5,S} {7,S} {13,S}
4  *2 C 0 {1,S} {3,S} {14,S} {15,S}
5     C 0 {3,S} {6,S} {16,S} {17,S}
6     C 0 {2,S} {5,S} {18,S} {19,S}
7  *5 C 0 {3,S} {8,D} {20,S}
8  *4 C 0 {2,S} {7,D} {21,S}
9     C 0 {1,S} {10,D} {22,S}
10    C 0 {9,D} {23,S} {24,S}
11    H 0 {1,S}
12    H 0 {2,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {5,S}
18    H 0 {6,S}
19    H 0 {6,S}
20    H 0 {7,S}
21    H 0 {8,S}
22    H 0 {9,S}
23    H 0 {10,S}
24    H 0 {10,S}
""",
    product1 = 
"""
1     C 0 {2,S} {3,D} {5,S}
2  *1 C 0 {1,S} {4,D} {6,S}
3     C 0 {1,D} {7,S} {8,S}
4  *2 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    product2 = 
"""
1     C 0 {2,S} {4,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {9,S} {10,S}
3  *3 C 0 {2,S} {6,D} {11,S}
4  *6 C 0 {1,S} {5,D} {12,S}
5  *5 C 0 {4,D} {6,S} {13,S}
6  *4 C 0 {3,D} {5,S} {14,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.88e+14,"s^-1","*|/",1.2),
        n = 0,
        Ea = (215.345,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (476,"K"),
        Tmax = (563,"K"),
        Pmin = (267,"Pa"),
        Pmax = (5333,"Pa"),
    ),
    reference = Article(
        authors = ["Huybrechts, G.", "Hubin, Y.", "Narmon, M.", "Van Mele, B."],
        title = u'Kinetics of the Thermal Reactions of Bicyclo[4.2.2]deca-3,7-diene and endo- and exo-5-Vinylbicyclo[2.2.2]oct-2-ene in the Gas Phase',
        journal = "Int. J. Chem. Kinet.",
        volume = "14",
        pages = """251""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982HUY/HUB251:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016017
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016017/rk00000001.xml
Uncertainty: 1.2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:35:06 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1982HUY/HUB251:1"""),
    ],
)

entry(
    index = 44,
    label = "1982HUY/HUB259:1",
    reactant1 = 
"""
1     C 0 {2,S} {3,D} {5,S}
2  *1 C 0 {1,S} {4,D} {6,S}
3     C 0 {1,D} {7,S} {8,S}
4  *2 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    reactant2 = 
"""
1     C 0 {2,S} {4,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {9,S} {10,S}
3  *3 C 0 {2,S} {6,D} {11,S}
4  *6 C 0 {1,S} {5,D} {12,S}
5  *5 C 0 {4,D} {6,S} {13,S}
6  *4 C 0 {3,D} {5,S} {14,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
""",
    product1 = 
"""
1  *1 C 0 {2,S} {4,S} {9,S} {11,S}
2  *3 C 0 {1,S} {6,S} {8,S} {12,S}
3  *6 C 0 {4,S} {5,S} {7,S} {13,S}
4  *2 C 0 {1,S} {3,S} {14,S} {15,S}
5     C 0 {3,S} {6,S} {16,S} {17,S}
6     C 0 {2,S} {5,S} {18,S} {19,S}
7  *5 C 0 {3,S} {8,D} {20,S}
8  *4 C 0 {2,S} {7,D} {21,S}
9     C 0 {1,S} {10,D} {22,S}
10    C 0 {9,D} {23,S} {24,S}
11    H 0 {1,S}
12    H 0 {2,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {5,S}
18    H 0 {6,S}
19    H 0 {6,S}
20    H 0 {7,S}
21    H 0 {8,S}
22    H 0 {9,S}
23    H 0 {10,S}
24    H 0 {10,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3800,"m^3/(mol*s)","*|/",1.05),
        n = 0,
        Ea = (103.931,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (437,"K"),
        Tmax = (526,"K"),
        Pmin = (14800,"Pa"),
        Pmax = (65300,"Pa"),
    ),
    reference = Article(
        authors = ["Huybrechts, G.", "Hubin, Y.", "Narmon, M.", "Van Mele, B."],
        title = u'Kinetics and Mechanism of the Addition of 1,3-Butadiene to Cyclohexa-1,3-diene in the Gas Phase',
        journal = "Int. J. Chem. Kinet.",
        volume = "14",
        pages = """259""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982HUY/HUB259:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016017
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016017/rk00000001.xml
Uncertainty: 1.05
Bath gas: 1,3-Butadiene
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:35:07 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1982HUY/HUB259:1"""),
    ],
)

entry(
    index = 45,
    label = "1986VAN/BOO537:7",
    reactant1 = 
"""
1     C 0 {2,S} {4,S} {7,S} {11,S}
2  *3 C 0 {1,S} {6,S} {10,S} {12,S}
3  *6 C 0 {4,S} {5,S} {9,S} {13,S}
4     C 0 {1,S} {3,S} {14,S} {15,S}
5  *2 C 0 {3,S} {6,S} {16,S} {17,S}
6  *1 C 0 {2,S} {5,S} {18,S} {19,S}
7     C 0 {1,S} {8,S} {20,S} {21,S}
8     C 0 {7,S} {22,S} {23,S} {24,S}
9  *5 C 0 {3,S} {10,D} {25,S}
10 *4 C 0 {2,S} {9,D} {26,S}
11    H 0 {1,S}
12    H 0 {2,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {5,S}
18    H 0 {6,S}
19    H 0 {6,S}
20    H 0 {7,S}
21    H 0 {7,S}
22    H 0 {8,S}
23    H 0 {8,S}
24    H 0 {8,S}
25    H 0 {9,S}
26    H 0 {10,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2 *1 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1     C 0 {2,S} {3,S} {5,S} {9,S}
2     C 0 {1,S} {4,S} {10,S} {11,S}
3     C 0 {1,S} {6,S} {12,S} {13,S}
4     C 0 {2,S} {14,S} {15,S} {16,S}
5  *3 C 0 {1,S} {7,D} {17,S}
6  *6 C 0 {3,S} {8,D} {18,S}
7  *4 C 0 {5,D} {8,S} {19,S}
8  *5 C 0 {6,D} {7,S} {20,S}
9     H 0 {1,S}
10    H 0 {2,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {4,S}
17    H 0 {5,S}
18    H 0 {6,S}
19    H 0 {7,S}
20    H 0 {8,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.71e+14,"s^-1","*|/",1.15),
        n = 0,
        Ea = (241.12,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (567,"K"),
        Tmax = (670,"K"),
        Pmin = (400,"Pa"),
        Pmax = (1067,"Pa"),
    ),
    reference = Article(
        authors = ["van Mele, B.", "Boon, G.", "Huybrechts, G."],
        title = u'Gas phase kinetic and thermochemical data for endo- and exo-5-monosubstituted bicyclo[2.2.2]oct-2-enes',
        journal = "Int. J. Chem. Kinet.",
        volume = "18",
        pages = """537""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986VAN/BOO537:7",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016994
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016994/rk00000001.xml
Uncertainty: 1.15
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:35:42 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1986VAN/BOO537:7"""),
    ],
)

entry(
    index = 46,
    label = "1986VAN/BOO537:8",
    reactant1 = 
"""
1  *1 C 0 {2,S} {4,S} {7,S} {11,S}
2  *3 C 0 {1,S} {6,S} {10,S} {12,S}
3  *6 C 0 {4,S} {5,S} {9,S} {13,S}
4  *2 C 0 {1,S} {3,S} {14,S} {15,S}
5     C 0 {3,S} {6,S} {16,S} {17,S}
6     C 0 {2,S} {5,S} {18,S} {19,S}
7     C 0 {1,S} {8,S} {20,S} {21,S}
8     C 0 {7,S} {22,S} {23,S} {24,S}
9  *5 C 0 {3,S} {10,D} {25,S}
10 *4 C 0 {2,S} {9,D} {26,S}
11    H 0 {1,S}
12    H 0 {2,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {5,S}
18    H 0 {6,S}
19    H 0 {6,S}
20    H 0 {7,S}
21    H 0 {7,S}
22    H 0 {8,S}
23    H 0 {8,S}
24    H 0 {8,S}
25    H 0 {9,S}
26    H 0 {10,S}
""",
    product1 = 
"""
1     C 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 {1,S} {7,S} {8,S} {9,S}
3  *1 C 0 {1,S} {4,D} {10,S}
4  *2 C 0 {3,D} {11,S} {12,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    product2 = 
"""
1     C 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,D} {11,S}
4  *6 C 0 {2,S} {6,D} {12,S}
5  *4 C 0 {3,D} {6,S} {13,S}
6  *5 C 0 {4,D} {5,S} {14,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.66e+15,"s^-1","*|/",1.1),
        n = 0,
        Ea = (244.445,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (567,"K"),
        Tmax = (670,"K"),
        Pmin = (400,"Pa"),
        Pmax = (1067,"Pa"),
    ),
    reference = Article(
        authors = ["van Mele, B.", "Boon, G.", "Huybrechts, G."],
        title = u'Gas phase kinetic and thermochemical data for endo- and exo-5-monosubstituted bicyclo[2.2.2]oct-2-enes',
        journal = "Int. J. Chem. Kinet.",
        volume = "18",
        pages = """537""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986VAN/BOO537:8",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016995
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016995/rk00000001.xml
Uncertainty: 1.1
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:35:46 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1986VAN/BOO537:8"""),
    ],
)

entry(
    index = 47,
    label = "1984HUY/POP93:1",
    reactant1 = 
"""
1     C 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 {1,S} {7,S} {8,S} {9,S}
3  *1 C 0 {1,S} {4,D} {10,S}
4  *2 C 0 {3,D} {11,S} {12,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    reactant2 = 
"""
1     C 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,D} {11,S}
4  *6 C 0 {2,S} {6,D} {12,S}
5  *4 C 0 {3,D} {6,S} {13,S}
6  *5 C 0 {4,D} {5,S} {14,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
""",
    product1 = 
"""
1  *1 C 0 {2,S} {4,S} {7,S} {11,S}
2  *3 C 0 {1,S} {6,S} {10,S} {12,S}
3  *6 C 0 {4,S} {5,S} {9,S} {13,S}
4  *2 C 0 {1,S} {3,S} {14,S} {15,S}
5     C 0 {3,S} {6,S} {16,S} {17,S}
6     C 0 {2,S} {5,S} {18,S} {19,S}
7     C 0 {1,S} {8,S} {20,S} {21,S}
8     C 0 {7,S} {22,S} {23,S} {24,S}
9  *5 C 0 {3,S} {10,D} {25,S}
10 *4 C 0 {2,S} {9,D} {26,S}
11    H 0 {1,S}
12    H 0 {2,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {5,S}
18    H 0 {6,S}
19    H 0 {6,S}
20    H 0 {7,S}
21    H 0 {7,S}
22    H 0 {8,S}
23    H 0 {8,S}
24    H 0 {8,S}
25    H 0 {9,S}
26    H 0 {10,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (708,"m^3/(mol*s)","*|/",1.12),
        n = 0,
        Ea = (109.751,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (488,"K"),
        Tmax = (606,"K"),
        Pmin = (7599,"Pa"),
        Pmax = (83300,"Pa"),
    ),
    reference = Article(
        authors = ["Huybrechts, G.", "Poppelsdorf, H.", "Maesschalck, L.", "Van Mele, B."],
        title = u'Kinetics, mechanism, and endo selectivity of diels-alder reactions of alkylmonosubstituted ethenes with cyclohexa-1,3-diene in the gas phase',
        journal = "Int. J. Chem. Kinet.",
        volume = "16",
        pages = """93""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984HUY/POP93:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016995
Uncertainty: 1.12
Bath gas: 1,3-Cyclohexadiene
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:35:47 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1984HUY/POP93:1"""),
    ],
)

entry(
    index = 48,
    label = "1982HUY/HUB259:3",
    reactant1 = 
"""
1  *4 C 0 {2,S} {3,D} {5,S}
2  *5 C 0 {1,S} {4,D} {6,S}
3  *3 C 0 {1,D} {7,S} {8,S}
4  *6 C 0 {2,D} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    reactant2 = 
"""
1     C 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 {1,S} {4,S} {9,S} {10,S}
3  *1 C 0 {1,S} {5,D} {11,S}
4     C 0 {2,S} {6,D} {12,S}
5  *2 C 0 {3,D} {6,S} {13,S}
6     C 0 {4,D} {5,S} {14,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
""",
    product1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {11,S}
2  *2 C 0 {1,S} {5,S} {7,S} {12,S}
3     C 0 {1,S} {6,S} {13,S} {14,S}
4  *3 C 0 {1,S} {8,S} {15,S} {16,S}
5  *6 C 0 {2,S} {9,S} {17,S} {18,S}
6     C 0 {3,S} {10,S} {19,S} {20,S}
7     C 0 {2,S} {10,D} {21,S}
8  *4 C 0 {4,S} {9,D} {22,S}
9  *5 C 0 {5,S} {8,D} {23,S}
10    C 0 {6,S} {7,D} {24,S}
11    H 0 {1,S}
12    H 0 {2,S}
13    H 0 {3,S}
14    H 0 {3,S}
15    H 0 {4,S}
16    H 0 {4,S}
17    H 0 {5,S}
18    H 0 {5,S}
19    H 0 {6,S}
20    H 0 {6,S}
21    H 0 {7,S}
22    H 0 {8,S}
23    H 0 {9,S}
24    H 0 {10,S}
""",
    degeneracy = 32,
    kinetics = Arrhenius(
        A = (10500,"m^3/(mol*s)","*|/",1.07),
        n = 0,
        Ea = (106.425,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (437,"K"),
        Tmax = (526,"K"),
        Pmin = (14800,"Pa"),
        Pmax = (65300,"Pa"),
    ),
    reference = Article(
        authors = ["Huybrechts, G.", "Hubin, Y.", "Narmon, M.", "Van Mele, B."],
        title = u'Kinetics and Mechanism of the Addition of 1,3-Butadiene to Cyclohexa-1,3-diene in the Gas Phase',
        journal = "Int. J. Chem. Kinet.",
        volume = "14",
        pages = """259""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982HUY/HUB259:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00004737
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004737/rk00000001.xml
Uncertainty: 1.0700001
Bath gas: 1,3-Butadiene
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Tue Jul 24 15:48:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1982HUY/HUB259:3"""),
    ],
)

entry(
    index = 49,
    label = "1987VAN/TYB1063:2",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S} {5,S}
2 *2 C 0 {1,D} {6,S} {7,S}
3    C 0 {1,S} {4,D} {8,S}
4    O 0 {3,D}
5    H 0 {1,S}
6    H 0 {2,S}
7    H 0 {2,S}
8    H 0 {3,S}
""",
    reactant2 = 
"""
1     C 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,D} {11,S}
4  *6 C 0 {2,S} {6,D} {12,S}
5  *4 C 0 {3,D} {6,S} {13,S}
6  *5 C 0 {4,D} {5,S} {14,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
""",
    product1 = 
"""
1  *3 C 0 {2,S} {5,S} {7,S} {11,S}
2  *1 C 0 {1,S} {4,S} {9,S} {12,S}
3  *6 C 0 {4,S} {6,S} {8,S} {13,S}
4  *2 C 0 {2,S} {3,S} {14,S} {15,S}
5     C 0 {1,S} {6,S} {16,S} {17,S}
6     C 0 {3,S} {5,S} {18,S} {19,S}
7  *4 C 0 {1,S} {8,D} {20,S}
8  *5 C 0 {3,S} {7,D} {21,S}
9     C 0 {2,S} {10,D} {22,S}
10    O 0 {9,D}
11    H 0 {1,S}
12    H 0 {2,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {5,S}
18    H 0 {6,S}
19    H 0 {6,S}
20    H 0 {7,S}
21    H 0 {8,S}
22    H 0 {9,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1020,"m^3/(mol*s)","*|/",1.07),
        n = 0,
        Ea = (83.976,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (379,"K"),
        Tmax = (581,"K"),
        Pmin = (6266,"Pa"),
        Pmax = (26900,"Pa"),
    ),
    reference = Article(
        authors = ["Van Mele, B.", "Tybaert, C.", "Huybrechts, G."],
        title = u'Kinetics, mechanism, and stereochemistry of Diels-Alder reactions of carbonyl-substituted ethenes with cyclohexa-1,3-diene in the gas phase',
        journal = "Int. J. Chem. Kinet.",
        volume = "19",
        pages = """1063""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987VAN/TYB1063:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00004843
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00004843/rk00000002.xml
Uncertainty: 1.0700001
Bath gas: 1,3-Cyclohexadiene
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Tue Jul 24 16:03:55 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1987VAN/TYB1063:2"""),
    ],
)

entry(
    index = 50,
    label = "1987VAN/TYB1063:1",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S} {5,S}
2 *2 C 0 {1,D} {6,S} {7,S}
3    C 0 {1,S} {4,D} {8,S}
4    O 0 {3,D}
5    H 0 {1,S}
6    H 0 {2,S}
7    H 0 {2,S}
8    H 0 {3,S}
""",
    reactant2 = 
"""
1     C 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,D} {11,S}
4  *6 C 0 {2,S} {6,D} {12,S}
5  *4 C 0 {3,D} {6,S} {13,S}
6  *5 C 0 {4,D} {5,S} {14,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
""",
    product1 = 
"""
1  *3 C 0 {2,S} {5,S} {7,S} {11,S}
2  *1 C 0 {1,S} {4,S} {9,S} {12,S}
3  *6 C 0 {4,S} {6,S} {8,S} {13,S}
4  *2 C 0 {2,S} {3,S} {14,S} {15,S}
5     C 0 {1,S} {6,S} {16,S} {17,S}
6     C 0 {3,S} {5,S} {18,S} {19,S}
7  *4 C 0 {1,S} {8,D} {20,S}
8  *5 C 0 {3,S} {7,D} {21,S}
9     C 0 {2,S} {10,D} {22,S}
10    O 0 {9,D}
11    H 0 {1,S}
12    H 0 {2,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {5,S}
18    H 0 {6,S}
19    H 0 {6,S}
20    H 0 {7,S}
21    H 0 {8,S}
22    H 0 {9,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (603,"m^3/(mol*s)","*|/",1.07),
        n = 0,
        Ea = (87.302,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (379,"K"),
        Tmax = (581,"K"),
        Pmin = (5733,"Pa"),
        Pmax = (26900,"Pa"),
    ),
    reference = Article(
        authors = ["Van Mele, B.", "Tybaert, C.", "Huybrechts, G."],
        title = u'Kinetics, mechanism, and stereochemistry of Diels-Alder reactions of carbonyl-substituted ethenes with cyclohexa-1,3-diene in the gas phase',
        journal = "Int. J. Chem. Kinet.",
        volume = "19",
        pages = """1063""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987VAN/TYB1063:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016478
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016478/rk00000003.xml
Uncertainty: 1.0700001
Bath gas: 1,3-Cyclohexadiene
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Tue Jul 24 16:21:05 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1987VAN/TYB1063:1"""),
    ],
)

entry(
    index = 51,
    label = "1986VAN/BOO537:5",
    reactant1 = 
"""
1     C 0 {2,S} {3,S} {5,S} {12,S}
2     C 0 {1,S} {8,S} {9,S} {13,S}
3  *3 C 0 {1,S} {7,S} {11,S} {14,S}
4  *6 C 0 {5,S} {6,S} {10,S} {15,S}
5     C 0 {1,S} {4,S} {16,S} {17,S}
6  *2 C 0 {4,S} {7,S} {18,S} {19,S}
7  *1 C 0 {3,S} {6,S} {20,S} {21,S}
8     C 0 {2,S} {22,S} {23,S} {24,S}
9     C 0 {2,S} {25,S} {26,S} {27,S}
10 *5 C 0 {4,S} {11,D} {28,S}
11 *4 C 0 {3,S} {10,D} {29,S}
12    H 0 {1,S}
13    H 0 {2,S}
14    H 0 {3,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {5,S}
18    H 0 {6,S}
19    H 0 {6,S}
20    H 0 {7,S}
21    H 0 {7,S}
22    H 0 {8,S}
23    H 0 {8,S}
24    H 0 {8,S}
25    H 0 {9,S}
26    H 0 {9,S}
27    H 0 {9,S}
28    H 0 {10,S}
29    H 0 {11,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2 *1 C 0 {1,D} {5,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    product2 = 
"""
1     C 0 {2,S} {4,S} {5,S} {10,S}
2     C 0 {1,S} {3,S} {6,S} {11,S}
3     C 0 {2,S} {7,S} {12,S} {13,S}
4     C 0 {1,S} {14,S} {15,S} {16,S}
5     C 0 {1,S} {17,S} {18,S} {19,S}
6  *3 C 0 {2,S} {8,D} {20,S}
7  *6 C 0 {3,S} {9,D} {21,S}
8  *4 C 0 {6,D} {9,S} {22,S}
9  *5 C 0 {7,D} {8,S} {23,S}
10    H 0 {1,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {4,S}
17    H 0 {5,S}
18    H 0 {5,S}
19    H 0 {5,S}
20    H 0 {6,S}
21    H 0 {7,S}
22    H 0 {8,S}
23    H 0 {9,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.35e+15,"s^-1","*|/",1.1),
        n = 0,
        Ea = (241.951,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (567,"K"),
        Tmax = (670,"K"),
        Pmin = (400,"Pa"),
        Pmax = (1067,"Pa"),
    ),
    reference = Article(
        authors = ["van Mele, B.", "Boon, G.", "Huybrechts, G."],
        title = u'Gas phase kinetic and thermochemical data for endo- and exo-5-monosubstituted bicyclo[2.2.2]oct-2-enes',
        journal = "Int. J. Chem. Kinet.",
        volume = "18",
        pages = """537""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986VAN/BOO537:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016991
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016991/rk00000001.xml
Uncertainty: 1.1
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:35:32 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1986VAN/BOO537:5"""),
    ],
)

entry(
    index = 52,
    label = "1986VAN/BOO537:6",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {5,S} {12,S}
2     C 0 {1,S} {8,S} {9,S} {13,S}
3  *3 C 0 {1,S} {7,S} {11,S} {14,S}
4  *6 C 0 {5,S} {6,S} {10,S} {15,S}
5  *2 C 0 {1,S} {4,S} {16,S} {17,S}
6     C 0 {4,S} {7,S} {18,S} {19,S}
7     C 0 {3,S} {6,S} {20,S} {21,S}
8     C 0 {2,S} {22,S} {23,S} {24,S}
9     C 0 {2,S} {25,S} {26,S} {27,S}
10 *5 C 0 {4,S} {11,D} {28,S}
11 *4 C 0 {3,S} {10,D} {29,S}
12    H 0 {1,S}
13    H 0 {2,S}
14    H 0 {3,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {5,S}
18    H 0 {6,S}
19    H 0 {6,S}
20    H 0 {7,S}
21    H 0 {7,S}
22    H 0 {8,S}
23    H 0 {8,S}
24    H 0 {8,S}
25    H 0 {9,S}
26    H 0 {9,S}
27    H 0 {9,S}
28    H 0 {10,S}
29    H 0 {11,S}
""",
    product1 = 
"""
1     C 0 {2,S} {3,S} {4,S} {6,S}
2     C 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 {1,S} {10,S} {11,S} {12,S}
4  *1 C 0 {1,S} {5,D} {13,S}
5  *2 C 0 {4,D} {14,S} {15,S}
6     H 0 {1,S}
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
    product2 = 
"""
1     C 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,D} {11,S}
4  *6 C 0 {2,S} {6,D} {12,S}
5  *4 C 0 {3,D} {6,S} {13,S}
6  *5 C 0 {4,D} {5,S} {14,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.1e+15,"s^-1","*|/",1.1),
        n = 0,
        Ea = (240.288,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (567,"K"),
        Tmax = (670,"K"),
        Pmin = (400,"Pa"),
        Pmax = (1067,"Pa"),
    ),
    reference = Article(
        authors = ["van Mele, B.", "Boon, G.", "Huybrechts, G."],
        title = u'Gas phase kinetic and thermochemical data for endo- and exo-5-monosubstituted bicyclo[2.2.2]oct-2-enes',
        journal = "Int. J. Chem. Kinet.",
        volume = "18",
        pages = """537""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986VAN/BOO537:6",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016992
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016992/rk00000001.xml
Uncertainty: 1.1
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:35:36 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1986VAN/BOO537:6"""),
    ],
)

entry(
    index = 53,
    label = "1984HUY/POP93:7",
    reactant1 = 
"""
1     C 0 {2,S} {3,S} {4,S} {6,S}
2     C 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 {1,S} {10,S} {11,S} {12,S}
4  *1 C 0 {1,S} {5,D} {13,S}
5  *2 C 0 {4,D} {14,S} {15,S}
6     H 0 {1,S}
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
    reactant2 = 
"""
1     C 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,D} {11,S}
4  *6 C 0 {2,S} {6,D} {12,S}
5  *4 C 0 {3,D} {6,S} {13,S}
6  *5 C 0 {4,D} {5,S} {14,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
""",
    product1 = 
"""
1  *1 C 0 {2,S} {3,S} {5,S} {12,S}
2     C 0 {1,S} {8,S} {9,S} {13,S}
3  *3 C 0 {1,S} {7,S} {11,S} {14,S}
4  *6 C 0 {5,S} {6,S} {10,S} {15,S}
5  *2 C 0 {1,S} {4,S} {16,S} {17,S}
6     C 0 {4,S} {7,S} {18,S} {19,S}
7     C 0 {3,S} {6,S} {20,S} {21,S}
8     C 0 {2,S} {22,S} {23,S} {24,S}
9     C 0 {2,S} {25,S} {26,S} {27,S}
10 *5 C 0 {4,S} {11,D} {28,S}
11 *4 C 0 {3,S} {10,D} {29,S}
12    H 0 {1,S}
13    H 0 {2,S}
14    H 0 {3,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {5,S}
18    H 0 {6,S}
19    H 0 {6,S}
20    H 0 {7,S}
21    H 0 {7,S}
22    H 0 {8,S}
23    H 0 {8,S}
24    H 0 {8,S}
25    H 0 {9,S}
26    H 0 {9,S}
27    H 0 {9,S}
28    H 0 {10,S}
29    H 0 {11,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (372,"m^3/(mol*s)","*|/",1.07),
        n = 0,
        Ea = (111.414,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (488,"K"),
        Tmax = (606,"K"),
        Pmin = (7599,"Pa"),
        Pmax = (83300,"Pa"),
    ),
    reference = Article(
        authors = ["Huybrechts, G.", "Poppelsdorf, H.", "Maesschalck, L.", "Van Mele, B."],
        title = u'Kinetics, mechanism, and endo selectivity of diels-alder reactions of alkylmonosubstituted ethenes with cyclohexa-1,3-diene in the gas phase',
        journal = "Int. J. Chem. Kinet.",
        volume = "16",
        pages = """93""",
        year = "1984",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1984HUY/POP93:7",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016992
Uncertainty: 1.0700001
Bath gas: 1,3-Cyclohexadiene
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 07:35:36 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1984HUY/POP93:7"""),
    ],
)

entry(
    index = 54,
    label = "1971DEM/HUY1397:3",
    reactant1 = 
"""
1     C 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 {1,S} {4,S} {9,S} {10,S}
3  *1 C 0 {1,S} {5,D} {11,S}
4     C 0 {2,S} {6,D} {12,S}
5  *2 C 0 {3,D} {6,S} {13,S}
6     C 0 {4,D} {5,S} {14,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
""",
    reactant2 = 
"""
1     C 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,D} {11,S}
4  *6 C 0 {2,S} {6,D} {12,S}
5  *4 C 0 {3,D} {6,S} {13,S}
6  *5 C 0 {4,D} {5,S} {14,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
""",
    product1 = 
"""
1  *1 C 0 {2,S} {3,S} {5,S} {13,S}
2  *2 C 0 {1,S} {4,S} {9,S} {14,S}
3  *3 C 0 {1,S} {6,S} {10,S} {15,S}
4  *6 C 0 {2,S} {7,S} {11,S} {16,S}
5     C 0 {1,S} {8,S} {17,S} {18,S}
6     C 0 {3,S} {7,S} {19,S} {20,S}
7     C 0 {4,S} {6,S} {21,S} {22,S}
8     C 0 {5,S} {12,S} {23,S} {24,S}
9     C 0 {2,S} {12,D} {25,S}
10 *4 C 0 {3,S} {11,D} {26,S}
11 *5 C 0 {4,S} {10,D} {27,S}
12    C 0 {8,S} {9,D} {28,S}
13    H 0 {1,S}
14    H 0 {2,S}
15    H 0 {3,S}
16    H 0 {4,S}
17    H 0 {5,S}
18    H 0 {5,S}
19    H 0 {6,S}
20    H 0 {6,S}
21    H 0 {7,S}
22    H 0 {7,S}
23    H 0 {8,S}
24    H 0 {8,S}
25    H 0 {9,S}
26    H 0 {10,S}
27    H 0 {11,S}
28    H 0 {12,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (933,"m^3/(mol*s)","*|/",1.78),
        n = 0,
        Ea = (104.762,"kJ/mol","+|-",2.104),
        T0 = (1,"K"),
        Tmin = (471,"K"),
        Tmax = (639,"K"),
        Pmin = (3333,"Pa"),
        Pmax = (84000,"Pa"),
    ),
    reference = Article(
        authors = ["De Mare, G.R.", "Huybrechts, G.", "Toth, M.", "Goldfinger, P."],
        title = u'Thermal Dimerization of 1,3-Cyclohexadiene in the Gas Phase',
        journal = "Trans. Faraday Soc.",
        volume = "67",
        pages = """1397""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971DEM/HUY1397:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00007902
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007902/rk00000001.xml
Uncertainty: 1.78
Bath gas: 1,3-Cyclohexadiene
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Tue Jul 24 16:10:24 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1971DEM/HUY1397:3"""),
    ],
)

entry(
    index = 55,
    label = "1971DEM/HUY1397:4",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {5,S} {13,S}
2  *2 C 0 {1,S} {4,S} {9,S} {14,S}
3  *3 C 0 {1,S} {7,S} {11,S} {15,S}
4  *6 C 0 {2,S} {6,S} {10,S} {16,S}
5     C 0 {1,S} {8,S} {17,S} {18,S}
6     C 0 {4,S} {7,S} {19,S} {20,S}
7     C 0 {3,S} {6,S} {21,S} {22,S}
8     C 0 {5,S} {12,S} {23,S} {24,S}
9     C 0 {2,S} {12,D} {25,S}
10 *5 C 0 {4,S} {11,D} {26,S}
11 *4 C 0 {3,S} {10,D} {27,S}
12    C 0 {8,S} {9,D} {28,S}
13    H 0 {1,S}
14    H 0 {2,S}
15    H 0 {3,S}
16    H 0 {4,S}
17    H 0 {5,S}
18    H 0 {5,S}
19    H 0 {6,S}
20    H 0 {6,S}
21    H 0 {7,S}
22    H 0 {7,S}
23    H 0 {8,S}
24    H 0 {8,S}
25    H 0 {9,S}
26    H 0 {10,S}
27    H 0 {11,S}
28    H 0 {12,S}
""",
    product1 = 
"""
1     C 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 {1,S} {4,S} {9,S} {10,S}
3  *1 C 0 {1,S} {5,D} {11,S}
4     C 0 {2,S} {6,D} {12,S}
5  *2 C 0 {3,D} {6,S} {13,S}
6     C 0 {4,D} {5,S} {14,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
""",
    product2 = 
"""
1     C 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,D} {11,S}
4  *6 C 0 {2,S} {6,D} {12,S}
5  *4 C 0 {3,D} {6,S} {13,S}
6  *5 C 0 {4,D} {5,S} {14,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+14,"s^-1","*|/",5),
        n = 0,
        Ea = (217.839,"kJ/mol","+|-",8.73),
        T0 = (1,"K"),
        Tmin = (554,"K"),
        Tmax = (631,"K"),
        Pmin = (533,"Pa"),
        Pmax = (2666,"Pa"),
    ),
    reference = Article(
        authors = ["De Mare, G.R.", "Huybrechts, G.", "Toth, M.", "Goldfinger, P."],
        title = u'Thermal Dimerization of 1,3-Cyclohexadiene in the Gas Phase',
        journal = "Trans. Faraday Soc.",
        volume = "67",
        pages = """1397""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971DEM/HUY1397:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00008812
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008812/rk00000001.xml
Uncertainty: 5.0
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Tue Jul 24 16:13:48 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1971DEM/HUY1397:4"""),
    ],
)

entry(
    index = 56,
    label = "1971DEM/HUY1397:2",
    reactant1 = 
"""
1     C 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 {1,S} {4,S} {9,S} {10,S}
3  *1 C 0 {1,S} {5,D} {11,S}
4     C 0 {2,S} {6,D} {12,S}
5  *2 C 0 {3,D} {6,S} {13,S}
6     C 0 {4,D} {5,S} {14,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
""",
    reactant2 = 
"""
1     C 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 {1,S} {4,S} {9,S} {10,S}
3  *3 C 0 {1,S} {5,D} {11,S}
4  *6 C 0 {2,S} {6,D} {12,S}
5  *4 C 0 {3,D} {6,S} {13,S}
6  *5 C 0 {4,D} {5,S} {14,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {6,S}
""",
    product1 = 
"""
1  *1 C 0 {2,S} {3,S} {5,S} {13,S}
2  *2 C 0 {1,S} {4,S} {9,S} {14,S}
3  *3 C 0 {1,S} {6,S} {10,S} {15,S}
4  *6 C 0 {2,S} {7,S} {11,S} {16,S}
5     C 0 {1,S} {8,S} {17,S} {18,S}
6     C 0 {3,S} {7,S} {19,S} {20,S}
7     C 0 {4,S} {6,S} {21,S} {22,S}
8     C 0 {5,S} {12,S} {23,S} {24,S}
9     C 0 {2,S} {12,D} {25,S}
10 *4 C 0 {3,S} {11,D} {26,S}
11 *5 C 0 {4,S} {10,D} {27,S}
12    C 0 {8,S} {9,D} {28,S}
13    H 0 {1,S}
14    H 0 {2,S}
15    H 0 {3,S}
16    H 0 {4,S}
17    H 0 {5,S}
18    H 0 {5,S}
19    H 0 {6,S}
20    H 0 {6,S}
21    H 0 {7,S}
22    H 0 {7,S}
23    H 0 {8,S}
24    H 0 {8,S}
25    H 0 {9,S}
26    H 0 {10,S}
27    H 0 {11,S}
28    H 0 {12,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1200,"m^3/(mol*s)","*|/",1.78),
        n = 0,
        Ea = (101.437,"kJ/mol","+|-",2.037),
        T0 = (1,"K"),
        Tmin = (471,"K"),
        Tmax = (639,"K"),
        Pmin = (3333,"Pa"),
        Pmax = (84000,"Pa"),
    ),
    reference = Article(
        authors = ["De Mare, G.R.", "Huybrechts, G.", "Toth, M.", "Goldfinger, P."],
        title = u'Thermal Dimerization of 1,3-Cyclohexadiene in the Gas Phase',
        journal = "Trans. Faraday Soc.",
        volume = "67",
        pages = """1397""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971DEM/HUY1397:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00008812
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00008812/rk00000002.xml
Uncertainty: 1.78
Bath gas: 1,3-Cyclohexadiene
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Tue Jul 24 16:17:01 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1971DEM/HUY1397:2"""),
    ],
)

