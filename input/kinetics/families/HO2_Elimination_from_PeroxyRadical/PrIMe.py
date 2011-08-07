#!/usr/bin/env python
# encoding: utf-8

name = "HO2_Elimination_from_PeroxyRadical/PrIMe"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    label = "r00011720",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S}
3  *3 O     0 {1,S} {5,S}
4  *5 H     0 {2,S}
5  *4 O     1 {3,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S} {3,S}
2  *3 O     1 {1,S}
3  *5 H     0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.87e+13,"s^-1"),
        n = -0.634,
        Ea = (-132200,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Wagner, A.F.", "Slagle, I.R.", "Sarzynski, D.", "Gutman, D."], title=u'Experimental and theoretical studies of the C_2H_5 + O_2 reaction kinetics', journal="J. Phys. Chem.", volume="94", pages="""1853""", year="1990", url="http://warehouse.primekinetics.org/depository/reactions/data/r00011720/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011720/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:34:50 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011720/rk00000001.xml"""),
    ],
)

entry(
    index = 2,
    label = "r00011720",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S}
3  *3 O     0 {1,S} {5,S}
4  *5 H     0 {2,S}
5  *4 O     1 {3,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S} {3,S}
2  *3 O     1 {1,S}
3  *5 H     0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (71400,"s^-1"),
        n = 2.32,
        Ea = (27955,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Miller, J.A.", "Klippenstein, S.J."], title=u'The Reaction Between Ethyl and Molecular Oxygen II. Further Analysis', journal="Int J. Chem. Kinet.", volume="33", pages="""654-668""", year="2001", doi="10.1002/kin.1063", url="http://warehouse.primekinetics.org/depository/reactions/data/r00011720/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011720/rk00000003.xml
PrIMe had an error: Corrected the activation energy according to the $k_{p \infty}$ on page 665 of doi:10.1002/kin.1063
See text on page 663 for clue to the units being cal/mol.
""",
    history = [
        ("Tue May 17 14:34:50 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011720/rk00000003.xml"""),
        ("2011-06-20","Richard West <rwest@mit.edu>","action","""Corrected the activation energy according to the $k_{p \infty}$ on page 665 of doi:10.1002/kin.1063"""),
    ],
)

entry(
    index = 3,
    label = "r00011720",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S}
3  *3 O     0 {1,S} {5,S}
4  *5 H     0 {2,S}
5  *4 O     1 {3,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S} {3,S}
2  *3 O     1 {1,S}
3  *5 H     0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (8.66e+14,"s^-1"),
        n = -6.88,
        Ea = (141845,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["DeSain, J.D.", "Klippenstein, S.J.", "Miller, J.A.", "Taatjes, C.A."], title=u'Measurements, Theory, and Modeling of OH Formation in Ethyl + O_2 and Propyl + O_2 Reactions', journal="J. Phys. Chem. A", volume="107", pages="""4415-4427""", year="2003", url="http://warehouse.primekinetics.org/depository/reactions/data/r00011720/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011720/rk00000004.xml
""",
    history = [
        ("Tue May 17 14:34:50 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011720/rk00000004.xml"""),
    ],
)

entry(
    index = 4,
    label = "r00011861",
    reactant1 = 
"""
1  *4 O     0 {2,S} {3,S}
2  *3 O     1 {1,S}
3  *5 H     0 {1,S}
""",
    reactant2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *1 C     0 {3,D}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *1 C     0 {1,S} {6,S}
5  *3 O     0 {1,S} {7,S}
6  *5 H     0 {4,S}
7  *4 O     1 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20.1,"cm^3/(mol*s)"),
        n = 2.48142,
        Ea = (19.6,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Chen, C.-J.", "Bozzelli, J.W."], title=u'Analysis of Tertiary Butyl Radical + O_2, Isobutene + HO_2, Isobutene + OH, and Isobutene-OH Adducts + O_2: A Detailed Tertiary Butyl Oxidation Mechanism', journal="J. Phys. Chem. A", volume="103", pages="""9731-9769""", year="1999", url="http://warehouse.primekinetics.org/depository/reactions/data/r00011861/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011861/rk00000001.xml
Values corrected according to current NIST database and original publication at http://dx.doi.org/10.1021/jp991227n Table 9.
The PrIMe data had assumed T0=298K (hence the incorrect A) but I cannot explain the discrepancy in the Ea.
""",
    history = [
        ("Tue May 17 14:34:50 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011861/rk00000001.xml"""),
        ("2011-08-07","Richard West <rwest@mit.edu>","action","""Corrected values based on NIST database and original publication. T0 was wrong, and Ea."""),
    ],
)

entry(
    index = 5,
    label = "r00012692",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S}
2  *1 C     0 {1,S} {5,S}
3     C     0 {1,S}
4  *3 O     0 {1,S} {6,S}
5  *5 H     0 {2,S}
6  *4 O     1 {4,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S} {3,S}
2  *3 O     1 {1,S}
3  *5 H     0 {1,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (9.38e+16,"s^-1"),
        n = -7.86,
        Ea = (153236,"J/mol"),
        T0 = (298,"K"),
    ),
    reference = Article(authors=["DeSain, J.D.", "Klippenstein, S.J.", "Miller, J.A.", "Taatjes, C.A."], title=u'Measurements, Theory, and Modeling of OH Formation in Ethyl + O_2 and Propyl + O_2 Reactions', journal="J. Phys. Chem. A", volume="107", pages="""4415-4427""", year="2003", url="http://warehouse.primekinetics.org/depository/reactions/data/r00012692/rk00000001.xml"),
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

entry(
    index = 6,
    label = "r00016504",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *3 O     0 {2,S} {6,S}
5  *5 H     0 {1,S}
6  *4 O     1 {4,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S} {3,S}
2  *3 O     1 {1,S}
3  *5 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.02e+14,"s^-1"),
        n = -4.48,
        Ea = (136440,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["DeSain, J.D.", "Klippenstein, S.J.", "Miller, J.A.", "Taatjes, C.A."], title=u'Measurements, Theory, and Modeling of OH Formation in Ethyl + O_2 and Propyl + O_2 Reactions', journal="J. Phys. Chem. A", volume="107", pages="""4415-4427""", year="2003", url="http://warehouse.primekinetics.org/depository/reactions/data/r00016504/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016504/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:48 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016504/rk00000001.xml"""),
    ],
)

