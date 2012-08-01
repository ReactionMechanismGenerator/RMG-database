#!/usr/bin/env python
# encoding: utf-8

name = "H_Abstraction/PrIMe"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1101,
    label = "r00011842",
    reactant1 = 
"""
1 *3 O 1
""",
    reactant2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.7378e+06,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1330.32,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Hong, Zekai", "Cook, Robert D.", "Davidson, David F.", "Hanson, Ronald K."],
        title = u'A Shock Tube Study of OH + H2O2 -> H2O + HO2 and H2O2 + M -> 2OH + M using Laser Absorption of H2O and OH',
        journal = "The Journal of Physical Chemistry A",
        volume = "114",
        pages = """5718-5727""",
        year = "2010",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011842/rk00000044.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011842/rk00000044.xml
""",
    history = [
        ("Tue May 17 14:34:50 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011842/rk00000044.xml"""),
    ],
)

entry(
    index = 1102,
    label = "r00011842",
    reactant1 = 
"""
1 *3 O 1
""",
    reactant2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.5858e+07,"cm^3/(mol*s)"),
        n = 0,
        Ea = (30431,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Hong, Zekai", "Cook, Robert D.", "Davidson, David F.", "Hanson, Ronald K."],
        title = u'A Shock Tube Study of OH + H2O2 -> H2O + HO2 and H2O2 + M -> 2OH + M using Laser Absorption of H2O and OH',
        journal = "The Journal of Physical Chemistry A",
        volume = "114",
        pages = """5718-5727""",
        year = "2010",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011842/rk00000045.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011842/rk00000045.xml
""",
    history = [
        ("Tue May 17 14:34:50 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011842/rk00000045.xml"""),
    ],
)

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

