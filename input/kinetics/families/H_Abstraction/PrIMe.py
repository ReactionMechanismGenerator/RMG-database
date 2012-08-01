#!/usr/bin/env python
# encoding: utf-8

name = "H_Abstraction/PrIMe"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1145,
    label = "r00013765",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (4.78e+06,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8563.91,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Clarke, J.S.", "Kroll, J.H.", "Donahue, N.M.", "Anderson, J.G."],
        title = u'Testing frontier orbital control: kinetics of OH with ethane, propane, and cyclopropane from 180 to 360K',
        journal = "J. Phys. Chem. A",
        volume = "102",
        pages = """9847-9857""",
        year = "1998",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013765/rk00000004.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013765/rk00000004.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013765/rk00000004.xml"""),
    ],
)

