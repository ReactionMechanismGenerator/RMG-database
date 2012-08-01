#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/PrIMe"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 104,
    label = "r00013871",
    reactant1 = 
"""
1 *2 C 0 {2,D}
2 *3 C 0 {1,D}
""",
    reactant2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 C 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.67e-20,"cm^3/(mol*s)"),
        n = -0.772,
        Ea = (38.4976,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Clifford, E.P.", "Farrell, J.T.", "DeSain, J.D.", "Taatjes, C.A."],
        title = u'Infrared Frequency-Modulation Probing of Product Formation in Alkyl + O_2 Reactions: I. The Reaction of C_2H_5 with O_2 between 295 and 698 K',
        journal = "J. Phys. Chem. A",
        volume = "104",
        pages = """11549-11560""",
        year = "2000",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013871/rk00000032.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013871/rk00000032.xml
""",
    history = [
        ("Tue May 17 14:35:14 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013871/rk00000032.xml"""),
    ],
)

