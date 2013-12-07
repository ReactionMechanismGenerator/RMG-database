#!/usr/bin/env python
# encoding: utf-8

name = "HO2_Elimination_from_PeroxyRadical/NIST"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    label = "1990WAG/SLA1853-1868:1",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {6,S} {7,S}
2 *1 C 0 {1,S} {4,S} {8,S} {9,S}
3 *3 O 0 {1,S} {5,S}
4 *5 H 0 {2,S}
5 *4 O 1 {3,S}
6    H 0 {1,S}
7    H 0 {1,S}
8    H 0 {2,S}
9    H 0 {2,S}
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
1 *4 O 0 {2,S} {3,S}
2 *3 O 1 {1,S}
3 *5 H 0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (6.93e+14,"s^-1"),
        n = -0.63,
        Ea = (-132.2,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (1000,"K"),
        Pmin = (1013,"Pa"),
        Pmax = (1.01e+06,"Pa"),
    ),
    reference = Article(
        authors = ["Wagner, A.F.", "Slagle, I.R.", "Sarzynski, D.", "Gutman, D."],
        title = u'Experimental and theoretical studies of the C2H5 + O2 reaction kinetics',
        journal = "J. Phys. Chem.",
        volume = "94",
        pages = """1853-1868""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990WAG/SLA1853-1868:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00011720
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011720/rk00000001.xml
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Mass spectrometry
""",
    history = [
        ("Fri Jul 13 08:20:43 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1990WAG/SLA1853-1868:1"""),
    ],
)

entry(
    index = 2,
    label = "2003DES/KLI4415-4427:3",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {6,S} {7,S}
2 *1 C 0 {1,S} {4,S} {8,S} {9,S}
3 *3 O 0 {1,S} {5,S}
4 *5 H 0 {2,S}
5 *4 O 1 {3,S}
6    H 0 {1,S}
7    H 0 {1,S}
8    H 0 {2,S}
9    H 0 {2,S}
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
1 *4 O 0 {2,S} {3,S}
2 *3 O 1 {1,S}
3 *5 H 0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (9.12e+31,"s^-1"),
        n = -6.88,
        Ea = (141.845,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (296,"K"),
        Tmax = (700,"K"),
    ),
    reference = Article(
        authors = ["DeSain, J.D.", "Klippenstein, S.J.", "Miller, J.A.", "Taatjes, C.A."],
        title = u'Measurements, Theory, and Modeling of OH Formation in Ethyl + O2 and Propyl + O2 Reactions',
        journal = "J. Phys. Chem. A",
        volume = "107",
        pages = """4415-4427""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003DES/KLI4415-4427:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00011720
Bath gas: He
Pressure dependence: Rate constant is pressure dependent

Rate constants are based in part on master equation simulations employing transition states from quantum calculations. This work is a combined experimental, theory, and modeling study. Compared OH profiles with those from modeling. Model describes HO2 profiles well, but is not as good for OH profiles.

Static cell (low flow), 296-700 K, He buffer typically 3.65E17 cm-3 (10-20 torr), O2 typically 6.3E15 cm-3. Radicals produced by RH + Cl -> R + HCl, where Cl produced by 193 nm excimer laser photolysis of CCl3F. OH detected using LIF at 281.996 nm.

Employed earlier quantum calculations (see references below) combined with master equation modeling to provide rate expressions for many reactions in this system. Only a few rate expressions are abstracted here.

Miller and Klippenstein, IJCK 33, 654 (2001)
DeSain et al, Farad. Disc. 119, 101 (2001)
""",
    history = [
        ("Fri Jul 13 08:20:43 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2003DES/KLI4415-4427:3"""),
        ("Wed Jul 18 13:27:00 2012","Sean Troiano <stroiano7@gmail.com>","action","""Removed invalid pressure range according to http://pubs.acs.org/doi/abs/10.1021/jp0221946"""),
    ],
)

entry(
    index = 3,
    label = "2001MIL/KLI654-668:3",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {6,S} {7,S}
2 *1 C 0 {1,S} {4,S} {8,S} {9,S}
3 *3 O 0 {1,S} {5,S}
4 *5 H 0 {2,S}
5 *4 O 1 {3,S}
6    H 0 {1,S}
7    H 0 {1,S}
8    H 0 {2,S}
9    H 0 {2,S}
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
1 *4 O 0 {2,S} {3,S}
2 *3 O 1 {1,S}
3 *5 H 0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (71400,"s^-1"),
        n = 2.32,
        Ea = (116.964,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (298,"K"),
        Tmax = (2000,"K"),
        Pmin = (133,"Pa"),
        Pmax = (133000,"Pa"),
    ),
    reference = Article(
        authors = ["Miller, J.A.", "Klippenstein, S.J."],
        title = u'The Reaction Between Ethyl and Molecular Oxygen II. Further Analysis',
        journal = "Int J. Chem. Kinet.",
        volume = "33",
        pages = """654-668""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001MIL/KLI654-668:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00011720
Pressure dependence: Rate constant is pressure dependent

Potential energy diagrams for various product channels have been computed.Three different regimes of the reaction (low-temperature, transition, and high-temperature) have been discussed in terms of eigenvectors and eigenvalues of the transition matrix of the master equation.Low pressure rate constant; k(0) = 1.38E-2 T^(-0.651) exp(-22890/RT) cm^3 / molecule s with F(cent)=exp (-T/106).
""",
    history = [
        ("Fri Jul 13 08:20:43 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2001MIL/KLI654-668:3"""),
    ],
)

entry(
    index = 4,
    label = "2003DES/KLI4415-4427:9",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {5,S} {7,S}
2  *2 C 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 {1,S} {10,S} {11,S} {12,S}
4  *3 O 0 {2,S} {6,S}
5  *5 H 0 {1,S}
6  *4 O 1 {4,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {3,S}
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
1 *4 O 0 {2,S} {3,S}
2 *3 O 1 {1,S}
3 *5 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.45e+25,"s^-1"),
        n = -4.48,
        Ea = (136.44,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (296,"K"),
        Tmax = (700,"K"),
    ),
    reference = Article(
        authors = ["DeSain, J.D.", "Klippenstein, S.J.", "Miller, J.A.", "Taatjes, C.A."],
        title = u'Measurements, Theory, and Modeling of OH Formation in Ethyl + O2 and Propyl + O2 Reactions',
        journal = "J. Phys. Chem. A",
        volume = "107",
        pages = """4415-4427""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003DES/KLI4415-4427:9",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00016504
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016504/rk00000001.xml
Bath gas: He
Pressure dependence: Rate constant is pressure dependent

Rate constants are based in part on master equation simulations employing transition states from quantum calculations. This work is a combined experimental, theory, and modeling study. Compared OH profiles with those from modeling. Model describes HO2 profiles well, but is not as good for OH profiles.

Static cell (low flow), 296-700 K, He buffer typically 3.65E17 cm-3 (10-20 torr), O2 typically 6.3E15 cm-3. Radicals produced by RH + Cl -> R + HCl, where Cl produced by 193 nm excimer laser photolysis of CCl3F. OH detected using LIF at 281.996 nm.

Employed earlier quantum calculations (see references below) combined with master equation modeling to provide rate expressions for many reactions in this system. Only a few rate expressions are abstracted here.

Miller and Klippenstein, IJCK 33, 654 (2001)
DeSain et al, Farad. Disc. 119, 101 (2001)
""",
    history = [
        ("Fri Jul 13 08:20:59 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2003DES/KLI4415-4427:9"""),
        ("Wed Jul 18 13:27:00 2012","Sean Troiano <stroiano7@gmail.com>","action","""Removed invalid pressure range according to http://pubs.acs.org/doi/abs/10.1021/jp0221946"""),
    ],
)

entry(
    index = 5,
    label = "2003DES/KLI4415-4427:6",
    reactant1 = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {7,S}
2  *1 C 0 {1,S} {5,S} {8,S} {9,S}
3     C 0 {1,S} {10,S} {11,S} {12,S}
4  *3 O 0 {1,S} {6,S}
5  *5 H 0 {2,S}
6  *4 O 1 {4,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {3,S}
""",
    product1 = 
"""
1    C 0 {2,S} {4,S} {5,S} {6,S}
2 *2 C 0 {1,S} {3,D} {7,S}
3 *1 C 0 {2,D} {8,S} {9,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
8    H 0 {3,S}
9    H 0 {3,S}
""",
    product2 = 
"""
1 *4 O 0 {2,S} {3,S}
2 *3 O 1 {1,S}
3 *5 H 0 {1,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.63e+36,"s^-1"),
        n = -7.86,
        Ea = (153.236,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (296,"K"),
        Tmax = (700,"K"),
    ),
    reference = Article(
        authors = ["DeSain, J.D.", "Klippenstein, S.J.", "Miller, J.A.", "Taatjes, C.A."],
        title = u'Measurements, Theory, and Modeling of OH Formation in Ethyl + O2 and Propyl + O2 Reactions',
        journal = "J. Phys. Chem. A",
        volume = "107",
        pages = """4415-4427""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003DES/KLI4415-4427:6",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00012692
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012692/rk00000001.xml
Bath gas: He

Rate constants are based in part on master equation simulations employing transition states from quantum calculations. This work is a combined experimental, theory, and modeling study. Compared OH profiles with those from modeling. Model describes HO2 profiles well, but is not as good for OH profiles.

Static cell (low flow), 296-700 K, He buffer typically 3.65E17 cm-3 (10-20 torr), O2 typically 6.3E15 cm-3. Radicals produced by RH + Cl -> R + HCl, where Cl produced by 193 nm excimer laser photolysis of CCl3F. OH detected using LIF at 281.996 nm.

Employed earlier quantum calculations (see references below) combined with master equation modeling to provide rate expressions for many reactions in this system. Only a few rate expressions are abstracted here.

Miller and Klippenstein, IJCK 33, 654 (2001)
DeSain et al, Farad. Disc. 119, 101 (2001)
""",
    history = [
        ("Tue Jul 24 16:31:45 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2003DES/KLI4415-4427:6"""),
    ],
)

entry(
    index = 6,
    label = "1999CHE/BOZ9731-9769:8",
    reactant1 = 
"""
1 *4 O 0 {2,S} {3,S}
2 *3 O 1 {1,S}
3 *5 H 0 {1,S}
""",
    reactant2 = 
"""
1     C 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 {3,S} {8,S} {9,S} {10,S}
3  *2 C 0 {1,S} {2,S} {4,D}
4  *1 C 0 {3,D} {11,S} {12,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    product1 = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {8,S} {9,S} {10,S}
3     C 0 {1,S} {11,S} {12,S} {13,S}
4  *1 C 0 {1,S} {6,S} {14,S} {15,S}
5  *3 O 0 {1,S} {7,S}
6  *5 H 0 {4,S}
7  *4 O 1 {5,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.01e-05,"m^3/(mol*s)"),
        n = 2.48,
        Ea = (82.006,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    reference = Article(
        authors = ["Chen, C.-J.", "Bozzelli, J.W."],
        title = u'Analysis of Tertiary Butyl Radical + O2, Isobutene + HO2, Isobutene + OH, and Isobutene-OH Adducts + O2: A Detailed Tertiary Butyl Oxidation Mechanism',
        journal = "J. Phys. Chem. A",
        volume = "103",
        pages = """9731-9769""",
        year = "1999",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1999CHE/BOZ9731-9769:8",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00011861
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011861/rk00000001.xml
Pressure dependence: Rate constant is high pressure limit
""",
    history = [
        ("Fri Jul 13 08:20:50 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1999CHE/BOZ9731-9769:8"""),
    ],
)

entry(
    index = 7,
    label = "1999CHE/BOZ9731-9769:2",
    reactant1 = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {8,S} {9,S} {10,S}
3     C 0 {1,S} {11,S} {12,S} {13,S}
4  *1 C 0 {1,S} {6,S} {14,S} {15,S}
5  *3 O 0 {1,S} {7,S}
6  *5 H 0 {4,S}
7  *4 O 1 {5,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {4,S}
15    H 0 {4,S}
""",
    product1 = 
"""
1 *4 O 0 {2,S} {3,S}
2 *3 O 1 {1,S}
3 *5 H 0 {1,S}
""",
    product2 = 
"""
1     C 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 {3,S} {8,S} {9,S} {10,S}
3  *2 C 0 {1,S} {2,S} {4,D}
4  *1 C 0 {3,D} {11,S} {12,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.04e+12,"s^-1"),
        n = 0.82,
        Ea = (114.767,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    reference = Article(
        authors = ["Chen, C.-J.", "Bozzelli, J.W."],
        title = u'Analysis of Tertiary Butyl Radical + O2, Isobutene + HO2, Isobutene + OH, and Isobutene-OH Adducts + O2: A Detailed Tertiary Butyl Oxidation Mechanism',
        journal = "J. Phys. Chem. A",
        volume = "103",
        pages = """9731-9769""",
        year = "1999",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1999CHE/BOZ9731-9769:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00011861
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011861/rk00000001.xml
Pressure dependence: Rate constant is high pressure limit
""",
    history = [
        ("Fri Jul 13 08:20:51 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1999CHE/BOZ9731-9769:2"""),
    ],
)

