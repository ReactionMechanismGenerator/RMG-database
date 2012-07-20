#!/usr/bin/env python
# encoding: utf-8

name = "HO2_Elimination_from_PeroxyRadical/PrIMe"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 5,
    label = "r00012692",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S}
2 *1 C 0 {1,S} {5,S}
3    C 0 {1,S}
4 *3 O 0 {1,S} {6,S}
5 *5 H 0 {2,S}
6 *4 O 1 {4,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *1 C 0 {2,D}
""",
    product2 = 
"""
1 *4 O 0 {2,S} {3,S}
2 *3 O 1 {1,S}
3 *5 H 0 {1,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (9.38e+16,"s^-1"),
        n = -7.86,
        Ea = (153236,"J/mol"),
        T0 = (298,"K"),
    ),
    reference = Article(
        authors = ["DeSain, J.D.", "Klippenstein, S.J.", "Miller, J.A.", "Taatjes, C.A."],
        title = u'Measurements, Theory, and Modeling of OH Formation in Ethyl + O_2 and Propyl + O_2 Reactions',
        journal = "J. Phys. Chem. A",
        volume = "107",
        pages = """4415-4427""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00012692/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012692/rk00000001.xml
Referece T0 corrected from 1 to 298K according to NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2003DES/KLI4415-4427:6
""",
    history = [
        ("Tue May 17 14:34:57 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012692/rk00000001.xml"""),
        ("2011-08-05","Richard West <rwest@mit.edu>","action","""Corrected T0 from 1K to 298K according to NIST database"""),
    ],
)

