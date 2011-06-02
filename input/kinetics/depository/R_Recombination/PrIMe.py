name = "R_Recombination"
shortDesc = ""
longDesc = """

"""

entry(
    index = 1,
    label = "r00001337",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S}
2     O     0 {1,D}
3  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (364174,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Aronowitz, D.", "Naegeli, D.W.", "Glassman, I."], title=u'Kinetics of the pyrolysis of methanol', journal="J. Phys. Chem.", volume="81", pages="""2555""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:30 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 2,
    label = "r00001337",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S}
2     O     0 {1,D}
3  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (364174,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Aronowitz, D.", "Naegeli, D."], title=u'High-Temperature Pyrolysis of Dimethyl Ether', journal="Int. J. Chem. Kinet.", volume="9", pages="""471""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:30 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 3,
    label = "r00001337",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S}
2     O     0 {1,D}
3  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.12e+12,"s^-1"),
        n = 0,
        Ea = (300984,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsuboi, T.", "Katoh, M.", "Kikuchi, S.", "Hashimoto, K."], title=u'Thermal Decomposition of Methanol behind Shock Waves', journal="Jpn. J. Appl. Phys.", volume="20", pages="""985""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:30 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 4,
    label = "r00001337",
    reactant1 = 
"""
1  *  C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2     O     0 {1,D}
3  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.47e+24,"cm^3/(mol*s)"),
        n = -2.57,
        Ea = (425,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000015.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:30 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 5,
    label = "r00001337",
    reactant1 = 
"""
1  *  C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2     O     0 {1,D}
3  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.94e+24,"cm^3/(mol*s)"),
        n = -2.57,
        Ea = (425,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000016.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:30 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 6,
    label = "r00001337",
    reactant1 = 
"""
1  *  C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2     O     0 {1,D}
3  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.482e+25,"cm^3/(mol*s)"),
        n = -2.57,
        Ea = (425,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000017.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:30 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 7,
    label = "r00001337",
    reactant1 = 
"""
1  *  C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2     O     0 {1,D}
3  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.94e+24,"cm^3/(mol*s)"),
        n = -2.57,
        Ea = (425,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000018.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:30 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 8,
    label = "r00001337",
    reactant1 = 
"""
1  *  C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2     O     0 {1,D}
3  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.705e+24,"cm^3/(mol*s)"),
        n = -2.57,
        Ea = (425,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000019.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:30 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 9,
    label = "r00001337",
    reactant1 = 
"""
1  *  C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2     O     0 {1,D}
3  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.94e+24,"cm^3/(mol*s)"),
        n = -2.57,
        Ea = (425,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000020.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:30 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 10,
    label = "r00001337",
    reactant1 = 
"""
1  *  C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2     O     0 {1,D}
3  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.41e+24,"cm^3/(mol*s)"),
        n = -2.57,
        Ea = (425,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000021.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:30 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 11,
    label = "r00001337",
    reactant1 = 
"""
1  *  C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2     O     0 {1,D}
3  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.729e+24,"cm^3/(mol*s)"),
        n = -2.57,
        Ea = (425,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000022.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:30 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 12,
    label = "r00001337",
    reactant1 = 
"""
1  *  C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2     O     0 {1,D}
3  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.09e+12,"cm^3/(mol*s)"),
        n = 0.48,
        Ea = (-260,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000023.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:30 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 13,
    label = "r00001337",
    reactant1 = 
"""
1  *  C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2     O     0 {1,D}
3  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.68e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-18957,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsuboi, T.", "Katoh, M.", "Kikuchi, S.", "Hashimoto, K."], title=u'Thermal Decomposition of Methanol behind Shock Waves', journal="Jpn. J. Appl. Phys.", volume="20", pages="""985""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000025.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:30 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 14,
    label = "r00001558",
    reactant1 = 
"""
1  *1 C     0 {3,S} {5,S}
2     C     0 {4,S} {5,S}
3     C     0 {1,S}
4     C     0 {2,S}
5  *2 O     0 {1,S} {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3  *  O     1 {2,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.7e+12,"s^-1"),
        n = 0,
        Ea = (241120,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Laidler, K.J.", "McKenney, D.J."], title=u'Kinetics and mechanisms of the pyrolysis of diethyl ether. I. The uninhibited reaction', journal="Proc. R. Soc. London", volume="278", pages="""505-516""", year="1964", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 15,
    label = "r00001558",
    reactant1 = 
"""
1  *1 C     0 {3,S} {5,S}
2     C     0 {4,S} {5,S}
3     C     0 {1,S}
4     C     0 {2,S}
5  *2 O     0 {1,S} {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3  *  O     1 {2,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2e+14,"s^-1"),
        n = 0,
        Ea = (324264,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Seres, I.", "Huhn, P."], title=u'A dietil-eter termikus bomlasa, III.', journal="Magy. Kem. Foly.", volume="81", pages="""120-123""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 16,
    label = "r00001558",
    reactant1 = 
"""
1  *1 C     0 {3,S} {5,S}
2     C     0 {4,S} {5,S}
3     C     0 {1,S}
4     C     0 {2,S}
5  *2 O     0 {1,S} {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3  *  O     1 {2,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5e+15,"s^-1"),
        n = 0,
        Ea = (339230,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Seres, I.", "Labadi, I.", "Huhn, P."], title=u'A Dietil-Eter Termikus Bomlasa, IV. Az Acetaldehid Hatasa a Bomlasra, [The Thermal Decomposition of Diethyl Ether, IV. The Effect of Acetaldehyde]', journal="Magy. Kem. Foly.", volume="83", pages="""151""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 17,
    label = "r00001558",
    reactant1 = 
"""
1  *1 C     0 {3,S} {5,S}
2     C     0 {4,S} {5,S}
3     C     0 {1,S}
4     C     0 {2,S}
5  *2 O     0 {1,S} {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3  *  O     1 {2,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.51e+15,"s^-1"),
        n = 0,
        Ea = (320939,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Foucaut, J.-F.", "Martin, R."], title=u"No. 18. - Etude analytique et cinetique de la pyrolyse de l'ether ethylique vers 500 \xb0C et a faible avancement", journal="J. Chim. Phys.", volume="75", pages="""132""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 18,
    label = "r00001558",
    reactant1 = 
"""
1  *1 C     0 {3,S} {5,S}
2     C     0 {4,S} {5,S}
3     C     0 {1,S}
4     C     0 {2,S}
5  *2 O     0 {1,S} {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3  *  O     1 {2,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.58e+17,"s^-1"),
        n = 0,
        Ea = (345051,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Seres, I.", "Huhn, P."], title=u'Radical steps in diethyl ether decomposition', journal="Int. J. Chem. Kinet.", volume="18", pages="""829""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 19,
    label = "r00001660",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *2 H     0 {2,S}
""",
    product1 = 
"""
1  *  H     1
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.19e+07,"s^-1"),
        n = 2.39,
        Ea = (1645.81,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ing, W.C.", "Sheng, C.Y.", "Bozzelli, J.W."], title=u'Development of a detailed high-pressure reaction model for methane/mehanol mixtures under pyrolytic and oxidative conditions and comparison with experimental data', journal="Fuel Process. Technol.", volume="83", pages="""111-145""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 20,
    label = "r00001660",
    reactant1 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.66e+41,"cm^3/(mol*s)"),
        n = -7.44,
        Ea = (14080,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 21,
    label = "r00001660",
    reactant1 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.32e+41,"cm^3/(mol*s)"),
        n = -7.44,
        Ea = (14080,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 22,
    label = "r00001660",
    reactant1 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.796e+42,"cm^3/(mol*s)"),
        n = -7.44,
        Ea = (14080,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 23,
    label = "r00001660",
    reactant1 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.32e+41,"cm^3/(mol*s)"),
        n = -7.44,
        Ea = (14080,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 24,
    label = "r00001660",
    reactant1 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.99e+41,"cm^3/(mol*s)"),
        n = -7.44,
        Ea = (14080,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 25,
    label = "r00001660",
    reactant1 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.32e+41,"cm^3/(mol*s)"),
        n = -7.44,
        Ea = (14080,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 26,
    label = "r00001660",
    reactant1 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.398e+42,"cm^3/(mol*s)"),
        n = -7.44,
        Ea = (14080,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 27,
    label = "r00001660",
    reactant1 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.43e+12,"cm^3/(mol*s)"),
        n = 0.515,
        Ea = (50,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 28,
    label = "r00001661",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 O     0 {1,S}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+16,"s^-1"),
        n = 0,
        Ea = (380803,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Aronowitz, D.", "Naegeli, D.W.", "Glassman, I."], title=u'Kinetics of the pyrolysis of methanol', journal="J. Phys. Chem.", volume="81", pages="""2555""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 29,
    label = "r00001661",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 O     0 {1,S}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+18,"s^-1"),
        n = 0,
        Ea = (394937,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsuboi, T.", "Katoh, M.", "Kikuchi, S.", "Hashimoto, K."], title=u'Thermal Decomposition of Methanol behind Shock Waves', journal="Jpn. J. Appl. Phys.", volume="20", pages="""985""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 30,
    label = "r00001661",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 O     0 {1,S}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.4e+15,"s^-1"),
        n = 0,
        Ea = (375814,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Spindler, K.", "Wagner, H.Gg."], title=u'Zum thermischen unimolekularen Zerfall von Methanol', journal="Ber. Bunsenges. Phys. Chem.", volume="86", pages="""2""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 31,
    label = "r00001661",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 O     0 {1,S}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.4e+15,"s^-1"),
        n = 0,
        Ea = (375814,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 32,
    label = "r00001661",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 O     0 {1,S}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.9e+16,"s^-1"),
        n = 0,
        Ea = (384129,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part 2. Methanol', journal="J. Phys. Chem. Ref. Data", volume="16", pages="""471""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 33,
    label = "r00001661",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 O     0 {1,S}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.7e+16,"s^-1"),
        n = 0,
        Ea = (379971,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Frank, P.", "Hayman, G.", "Just, Th.", "Kerr, J.A.", "Murrells, T.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."], title=u'Evaluated kinetic data for combusion modelling. Supplement I', journal="J. Phys. Chem. Ref. Data", volume="23", pages="""847-1033""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000015.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 34,
    label = "r00001661",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 O     0 {1,S}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.26e+10,"s^-1"),
        n = 2.05,
        Ea = (1492.81,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ing, W.C.", "Sheng, C.Y.", "Bozzelli, J.W."], title=u'Development of a detailed high-pressure reaction model for methane/mehanol mixtures under pyrolytic and oxidative conditions and comparison with experimental data', journal="Fuel Process. Technol.", volume="83", pages="""111-145""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000017.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 35,
    label = "r00001661",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  O     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 O     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4e+36,"cm^3/(mol*s)"),
        n = -5.92,
        Ea = (3140,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000018.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 36,
    label = "r00001661",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  O     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 O     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8e+36,"cm^3/(mol*s)"),
        n = -5.92,
        Ea = (3140,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000019.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 37,
    label = "r00001661",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  O     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 O     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.4e+37,"cm^3/(mol*s)"),
        n = -5.92,
        Ea = (3140,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000020.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 38,
    label = "r00001661",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  O     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 O     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8e+36,"cm^3/(mol*s)"),
        n = -5.92,
        Ea = (3140,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000021.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 39,
    label = "r00001661",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  O     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 O     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6e+36,"cm^3/(mol*s)"),
        n = -5.92,
        Ea = (3140,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000022.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 40,
    label = "r00001661",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  O     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 O     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8e+36,"cm^3/(mol*s)"),
        n = -5.92,
        Ea = (3140,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000023.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 41,
    label = "r00001661",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  O     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 O     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.2e+37,"cm^3/(mol*s)"),
        n = -5.92,
        Ea = (3140,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000024.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 42,
    label = "r00001661",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  O     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 O     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.79e+18,"cm^3/(mol*s)"),
        n = -1.43,
        Ea = (1330,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000025.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 43,
    label = "r00001661",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  O     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 O     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.23497e+40,"cm^3/(mol*s)"),
        n = -8.2,
        Ea = (48806,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M.", "Westmoreland, P.R."], title=u'Bimolecular QRRK analyss of methyl radical reactions', journal="Int. J. Chem. Kinet.", volume="19", pages="""207""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000027.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 44,
    label = "r00001661",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  O     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 O     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.31e+06,"cm^3/(mol*s)"),
        n = 2.08,
        Ea = (-29.0797,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ing, W.C.", "Sheng, C.Y.", "Bozzelli, J.W."], title=u'Development of a detailed high-pressure reaction model for methane/mehanol mixtures under pyrolytic and oxidative conditions and comparison with experimental data', journal="Fuel Process. Technol.", volume="83", pages="""111-145""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000036.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 45,
    label = "r00001662",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2     O     0 {1,S}
3  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1.64e+07,"s^-1"),
        n = 2.55,
        Ea = (1519.25,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ing, W.C.", "Sheng, C.Y.", "Bozzelli, J.W."], title=u'Development of a detailed high-pressure reaction model for methane/mehanol mixtures under pyrolytic and oxidative conditions and comparison with experimental data', journal="Fuel Process. Technol.", volume="83", pages="""111-145""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 46,
    label = "r00001662",
    reactant1 = 
"""
1  *  C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2     O     0 {1,S}
3  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.36e+31,"cm^3/(mol*s)"),
        n = -4.65,
        Ea = (5080,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 47,
    label = "r00001662",
    reactant1 = 
"""
1  *  C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2     O     0 {1,S}
3  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.72e+31,"cm^3/(mol*s)"),
        n = -4.65,
        Ea = (5080,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 48,
    label = "r00001662",
    reactant1 = 
"""
1  *  C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2     O     0 {1,S}
3  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.616e+32,"cm^3/(mol*s)"),
        n = -4.65,
        Ea = (5080,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 49,
    label = "r00001662",
    reactant1 = 
"""
1  *  C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2     O     0 {1,S}
3  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.72e+31,"cm^3/(mol*s)"),
        n = -4.65,
        Ea = (5080,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 50,
    label = "r00001662",
    reactant1 = 
"""
1  *  C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2     O     0 {1,S}
3  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.49e+31,"cm^3/(mol*s)"),
        n = -4.65,
        Ea = (5080,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 51,
    label = "r00001662",
    reactant1 = 
"""
1  *  C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2     O     0 {1,S}
3  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.72e+31,"cm^3/(mol*s)"),
        n = -4.65,
        Ea = (5080,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 52,
    label = "r00001662",
    reactant1 = 
"""
1  *  C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2     O     0 {1,S}
3  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.308e+32,"cm^3/(mol*s)"),
        n = -4.65,
        Ea = (5080,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 53,
    label = "r00001662",
    reactant1 = 
"""
1  *  C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2     O     0 {1,S}
3  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.055e+12,"cm^3/(mol*s)"),
        n = 0.5,
        Ea = (86,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000013.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 54,
    label = "r00001742",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     O     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,S}
3     O     0 {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.16e+16,"s^-1"),
        n = 0,
        Ea = (341725,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal Stability of Alcohols', journal="Int. J. Chem. Kinet.", volume="8", pages="""173""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 55,
    label = "r00001742",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     O     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,S}
3     O     0 {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.6e+81,"s^-1"),
        n = -19.56,
        Ea = (464954,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bui, B.H.", "Zhu, R.S.", "Lin, M.C."], title=u'Thermal Decomposition of Iso-Propanol:  First-Principles Prediction of Total and Product-Branching Rate Constants', journal="J. Chem. Phys.", volume="117", pages="""11188-11195""", year="2002", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 56,
    label = "r00001742",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     O     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,S}
3     O     0 {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.3e+73,"s^-1"),
        n = -17.06,
        Ea = (459624,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bui, B.H.", "Zhu, R.S.", "Lin, M.C."], title=u'Thermal Decomposition of Iso-Propanol:  First-Principles Prediction of Total and Product-Branching Rate Constants', journal="J. Chem. Phys.", volume="117", pages="""11188-11195""", year="2002", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 57,
    label = "r00001742",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     O     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,S}
3     O     0 {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (8e+29,"s^-1"),
        n = -3.75,
        Ea = (381144,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bui, B.H.", "Zhu, R.S.", "Lin, M.C."], title=u'Thermal Decomposition of Iso-Propanol:  First-Principles Prediction of Total and Product-Branching Rate Constants', journal="J. Chem. Phys.", volume="117", pages="""11188-11195""", year="2002", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 58,
    label = "r00001836",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *2 C     0 {1,S}
4     O     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2  *  C     1 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.58e+16,"s^-1"),
        n = 0,
        Ea = (341725,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal Stability of Alcohols', journal="Int. J. Chem. Kinet.", volume="8", pages="""173""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:32 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 59,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+13,"s^-1"),
        n = 0,
        Ea = (263569,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kenwright, R.", "Robinson, P.L.", "Trenwith, A.B."], title=u'The kinetics of the oxidation of ethane by nitrous oxide', journal="J. Chem. Soc.", pages="""660-666""", year="1958", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 60,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (197000,"s^-1"),
        n = 0,
        Ea = (62691.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Skinner, G.B.", "Ball, W.E."], title=u'Shock tube experiments on the pyrolysis of ethane', journal="J. Phys. Chem.", volume="64", pages="""1025""", year="1960", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 61,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.07e+15,"s^-1"),
        n = 0,
        Ea = (305973,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Laidler, K.J.", "Wojciechowski, B.W."], title=u'Kinetics and mechanisms of the thermal decomposition of ethane. I. The uninhibited reaction', journal="Proc. R. Soc. London", volume="260", pages="""91-102""", year="1961", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 62,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.6e+12,"s^-1"),
        n = 0,
        Ea = (280198,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Towell, g.D.", "Martin, J.J."], title=u'Kinetic data from nonisothermal experiments: thermal decomposition of ethane, ethylene, and acetylene', journal="AIChE J.", volume="7", pages="""693-698""", year="1961", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 63,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (288512,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kozlov, G.I.", "Knorre, V.G."], title=u'Single-pulse shock tube studies on the kinetics of the thermal decomposition of methane', journal="Combust. Flame", volume="6", pages="""253""", year="1962", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 64,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.82e+17,"s^-1"),
        n = 0,
        Ea = (384129,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Quinn, C.P."], title=u'The thermal dissociation and pyrolysis of ethane', journal="Proc. R. Soc. London A", volume="275", pages="""190""", year="1963", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 65,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.34e+16,"s^-1"),
        n = 0,
        Ea = (368331,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dexter, R.W.", "Trenwith, A.B."], title=u'The dissociation of ethane', journal="J. Chem. Soc.", pages="""392""", year="1964", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 66,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3e+16,"s^-1"),
        n = 0,
        Ea = (368331,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lin, M.C.", "Back, M.H."], title=u'the thermal decomposition of ethane. Part II. The unimolecular decomposition of the ethane molecule and the ethyl radical', journal="Can. J. Chem.", volume="44", pages="""2357""", year="1966", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 67,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+16,"s^-1"),
        n = 0,
        Ea = (360017,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lin, M.C.", "Back, M.H."], title=u'The thermal decomposition of ethane. Part I. Initiation and termination steps', journal="Can. J. Chem.", volume="44", pages="""505-514""", year="1966", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 68,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+16,"s^-1"),
        n = 0,
        Ea = (368331,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Trenwith, A.B."], title=u'Dissociation and kinetics of thermal decomposition of ethane', journal="J. Chem. Soc. Faraday Trans.", volume="62", pages="""1538""", year="1966", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000014.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 69,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+18,"s^-1"),
        n = 0,
        Ea = (379140,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Waage, E.V.", "Rabinovitch, B.S."], title=u'Some aspects of theory and experiment in the ethane-methyl radical system', journal="Int. J. Chem. Kinet.", volume="3", pages="""105-125""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000016.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 70,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+16,"s^-1"),
        n = 0,
        Ea = (369994,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Pacey, P.D.", "Purnell, J.H."], title=u'Arrhenius Parameters of the Reaction CH_3^. + C_2H_6 \u2192 CH_4 + C_2H_5^.', journal="J. Chem. Soc. Faraday Trans. 1", volume="68", pages="""1462""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000017.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 71,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+16,"s^-1"),
        n = 0,
        Ea = (374151,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Burcat, A.", "Skinner, G.B.", "Crossley, R.W.", "Scheller, K."], title=u'High Temperature Decomposition of Ethane', journal="Int. J. Chem. Kinet.", volume="5", pages="""345""", year="1973", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000018.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 72,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.35e+16,"s^-1"),
        n = 0,
        Ea = (362511,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Clark, J.A.", "Quinn, C.P."], title=u'Kinetic Isotope Effect in the Thermal Dissociation of Ethane', journal="J. Chem. Soc. Faraday Trans. 1", volume="72", pages="""706""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000020.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 73,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.08e+16,"s^-1"),
        n = 0,
        Ea = (377477,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Olson, D.B.", "Gardiner, W.C., Jr."], title=u'Thermal Dissociation Rate of Ethane at the High Pressure Limit from 250 to 2500 K', journal="J. Phys. Chem.", volume="83", pages="""922""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000021.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 74,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.04e+16,"s^-1"),
        n = 0,
        Ea = (367500,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Olson, D.B.", "Gardiner, W.C., Jr."], title=u'Thermal Dissociation Rate of Ethane at the High Pressure Limit from 250 to 2500 K', journal="J. Phys. Chem.", volume="83", pages="""922""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000022.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 75,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+15,"s^-1"),
        n = 0,
        Ea = (326759,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Pratt, G.", "Rogers, D."], title=u'Wall-less Reactor Studies. Part 1. - Ethane Pyrolysis', journal="J. Chem. Soc. Faraday Trans. 1", volume="75", pages="""1089""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000023.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 76,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+15,"s^-1"),
        n = 0,
        Ea = (349208,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Roth, P.", "Just, T.H."], title=u'Measurements of Some Elementary Hydrocarbon Reactions at High Temperatures', journal="NBS Spec. Publ. (U.S.)", volume="10", pages="""1339""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000024.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 77,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+15,"s^-1"),
        n = 0,
        Ea = (349208,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Roth, P.", "Just, Th."], title=u'Messungen zur Hochtemperaturpyroyse von Aethan', journal="Ber. Bunsenges. Phys. Chem.", volume="83", pages="""577""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000025.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 78,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.25e+16,"s^-1"),
        n = 0,
        Ea = (371657,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Trenwith, A.B."], title=u'Re-examination of the Thermal Dissociation of Ethane', journal="J. Chem. Soc. Faraday Trans. 1", volume="75", pages="""614""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000026.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 79,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+16,"s^-1"),
        n = 0,
        Ea = (372488,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Trenwith, A.B."], title=u'Re-examination of the Thermal Dissociation of Ethane', journal="J. Chem. Soc. Faraday Trans. 1", volume="75", pages="""614""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000027.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 80,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.4e+16,"s^-1"),
        n = 0,
        Ea = (365837,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Duxbury, J."], title=u'Ethane Decomposition and the Reference Rate Constant for Methyl Radical Recombination', journal="Combust. Flame", volume="37", pages="""313""", year="1980", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000028.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 81,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8e+12,"s^-1"),
        n = 0,
        Ea = (294332,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bhaskaran, K.A.", "Frank, P.", "Just, Th."], title=u'High Temperature Methyl Radical Reactions with Atomic and Molecular Oxygen', journal="Proc. Int. Symp. Shock Tubes Waves", volume="12", pages="""503""", year="1980", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000029.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 82,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.8e+15,"s^-1"),
        n = 0,
        Ea = (352534,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Chiang, C.C.", "Skinner, G.B."], title=u'Resonance Absorption Measurements of Atom Concentrations in Reacting Gas Mixtures. 7. Pyrolysis of C_2H_6 and C_2D_6 behind Shock Waves', journal="J. Phys. Chem.", volume="85", pages="""3126""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000031.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 83,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.58e+17,"s^-1"),
        n = 0,
        Ea = (380803,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Skinner, G.B.", "Rogers, D.", "Patel, K.B."], title=u'Consistency of theory and experiment in the ethane-methyl radical system', journal="Int. J. Chem. Kinet.", volume="13", pages="""481""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000033.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 84,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.31e+16,"s^-1"),
        n = 0,
        Ea = (367500,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kanan, K.", "Purnell, H.", "Sepherad, A."], title=u'Induced heterogeneity, a novel technique for the study of gas-phase reactions. 2. Direct study of C-C bond scission in ethane', journal="Int. J. Chem. Kinet.", volume="15", pages="""845""", year="1983", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000034.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 85,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.27e+16,"s^-1"),
        n = 0,
        Ea = (369994,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kanan, K.", "Purnell, H.", "Sepherad, A."], title=u'Induced heterogeneity, a novel technique for the study of gas-phase reactions. 2. Direct study of C-C bond scission in ethane', journal="Int. J. Chem. Kinet.", volume="15", pages="""845""", year="1983", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000035.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 86,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.4e+16,"s^-1"),
        n = 0,
        Ea = (365837,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000038.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 87,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+16,"s^-1"),
        n = 0,
        Ea = (374151,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000040.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 88,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7e+14,"s^-1"),
        n = 0,
        Ea = (335073,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hidaka, Y.", "Shiba, S.", "Takuma, H.", "Suga, M."], title=u'Thermal decomposition of ethane in shock waves', journal="Int. J. Chem. Kinet.", volume="17", pages="""441""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000041.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 89,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.18e+18,"s^-1"),
        n = -1.79,
        Ea = (380803,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W.", "Hampson, R.F."], title=u'Chemical kinetic data base for combustion chemistry. Part I. Methane and related compounds', journal="J. Phys. Chem. Ref. Data", volume="15", pages="""1087""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000043.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 90,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.31e+19,"s^-1"),
        n = -2.79,
        Ea = (389949,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Stewart, P.H.", "Larson, C.W.", "Golden, D.M."], title=u'Pressure and temperature dependence of reactions proceeding via a bound complex. 2. Application to 2CH\u2083 \u2192 C\u2082H\u2085 + H', journal="Combust. Flame", volume="75", pages="""25-31""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000044.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 91,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.12e+18,"s^-1"),
        n = -1.79,
        Ea = (380803,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Rate constants for the decomposition and formation of simple alkanes over extended temperature and pressure ranges', journal="Combust. Flame", volume="78", pages="""71-86""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000045.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 92,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.54e+18,"s^-1"),
        n = -1.24,
        Ea = (379971,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."], title=u'Evaluated kinetic data for combustion modelling', journal="J. Phys. Chem. Ref. Data", volume="21", pages="""411-429""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000046.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 93,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.38e+32,"s^-1"),
        n = -17.6,
        Ea = (488891,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Davidson, D.F.", "DiRosa, M.D.", "Hanson, R.K.", "Bowman, C.T."], title=u'A study of ethane decomposition in a shock tube using laser absorption of CH_3', journal="Int. J. Chem. Kinet.", volume="25", pages="""969-982""", year="1993", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000049.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 94,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.54e+18,"s^-1"),
        n = -1.24,
        Ea = (379971,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Frank, P.", "Hayman, G.", "Just, Th.", "Kerr, J.A.", "Murrells, T.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."], title=u'Evaluated kinetic data for combusion modelling. Supplement I', journal="J. Phys. Chem. Ref. Data", volume="23", pages="""847-1033""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000050.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 95,
    label = "r00002085",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+11,"s^-1"),
        n = 0,
        Ea = (251929,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Davidson, D.F.", "Hanson, R.K.", "Bowman, C.T."], title=u'Communication: revised values for the rate coefficients of ethane and methane decomposition', journal="Int. J. Chem. Kinet.", volume="27", pages="""305-308""", year="1995", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000054.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 96,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+41,"cm^3/(mol*s)"),
        n = -7.03,
        Ea = (2762,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000055.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 97,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.8e+41,"cm^3/(mol*s)"),
        n = -7.03,
        Ea = (2762,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000056.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 98,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.04e+42,"cm^3/(mol*s)"),
        n = -7.03,
        Ea = (2762,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000057.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 99,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.8e+41,"cm^3/(mol*s)"),
        n = -7.03,
        Ea = (2762,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000058.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 100,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.1e+41,"cm^3/(mol*s)"),
        n = -7.03,
        Ea = (2762,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000059.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 101,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.8e+41,"cm^3/(mol*s)"),
        n = -7.03,
        Ea = (2762,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000060.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 102,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+42,"cm^3/(mol*s)"),
        n = -7.03,
        Ea = (2762,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000061.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 103,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.38e+41,"cm^3/(mol*s)"),
        n = -7.03,
        Ea = (2762,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000062.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 104,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.77e+16,"cm^3/(mol*s)"),
        n = -1.18,
        Ea = (654,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000063.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 105,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.39e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-6343.94,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ingold, K.U.", "Lossing, F.P."], title=u'Free radicals by mass spectrometry. IV. The rate of combination of methyl radicals', journal="J. Chem. Phys.", volume="21", pages="""1135-1144""", year="1953", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000067.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 106,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.52058e+10,"cm^3/(mol*s)"),
        n = 0.5,
        Ea = (-9062.77,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ingold, K.U.", "Lossing, F.P."], title=u'The rate of combination of methyl radicals', journal="J. Chem. Phys.", volume="21", pages="""368""", year="1953", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000068.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 107,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.41e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (5903.28,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Waage, E.V.", "Rabinovitch, B.S."], title=u'Some aspects of theory and experiment in the ethane-methyl radical system', journal="Int. J. Chem. Kinet.", volume="3", pages="""105-125""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000081.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 108,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.62e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1795.93,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Teng, L.", "Jones, W.E."], title=u'Kinetics of the Reactions of Hydrogen Atoms with Ethylene and Vinyl Fluoride', journal="J. Chem. Soc. Faraday Trans. 1", volume="68", pages="""1267""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000082.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 109,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.67e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1280.43,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["MacPherson, M.T.", "Pilling, M.J.", "Smith, M.J.C."], title=u'The pressure and temperature dependence of the rate constant for methyl radical recombination over the temperature range 296-577 K', journal="Chem. Phys. Lett.", volume="94", pages="""430""", year="1983", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000105.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 110,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.39e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (448.981,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Cobos, C.J.", "Troe, J."], title=u'Theory of thermal unimolecular reactions at high pressures. II. Analysis of experimental results', journal="J. Chem. Phys.", volume="83", pages="""1010-1015""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000109.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 111,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.47e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1139.08,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Macpherson, M.T.", "Pilling, M.J.", "Smith, M.J.C."], title=u'Determination of the absorption cross section for CH_3 at 216.36 nm and the absolute rate constant for methyl radical recombination over the temperature range 296-577 K', journal="J. Phys. Chem.", volume="89", pages="""2268""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000110.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 112,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-29932.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Moller, W.", "Mozzhukhin, E.", "Wagner, H.Gg."], title=u'High temperature reactions of CH_3. 1. The reactions CH_3 + H_2 ? CH_4 + H', journal="Ber. Bunsenges. Phys. Chem.", volume="90", pages="""854""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000114.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 113,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.05736e+16,"cm^3/(mol*s)"),
        n = -1.18,
        Ea = (2735.46,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Slagle, I.R.", "Gutman, D.", "Davies, J.W.", "Pilling, M.J."], title=u'Study of the recombination reaction CH_3 + CH_3 \u2192 C_2H_6. 1. Experiment', journal="J. Phys. Chem.", volume="92", pages="""2455""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000118.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 114,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.05736e+16,"cm^3/(mol*s)"),
        n = -1.18,
        Ea = (2735.46,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Wagner, A.F.", "Wardlaw, D.M."], title=u'Study of the recombination reaction CH_3 + CH_3 ? C_2H_6. 2. Theory', journal="J. Phys. Chem.", volume="92", pages="""2462""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000119.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 115,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.68827e+16,"cm^3/(mol*s)"),
        n = -1.11,
        Ea = (2452.77,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Forst, W."], title=u'Microcanonical variational theory of radical recombination by inversion of interpolated partition function, with examples: CH_3 + H, CH_3 + CH_3', journal="J. Phys. Chem.", volume="95", pages="""3612-3620""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000122.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 116,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.37326e+16,"cm^3/(mol*s)"),
        n = -1.1,
        Ea = (2660.63,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hwang, S.M.", "Wagner, H.GG.", "Wolff, Th."], title=u'Recombination of CH_3 radicals at elevated pressures and temperatures', journal="Symp. Int. Combust. Proc.", volume="23", pages="""99-105""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000123.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 117,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.02674e+16,"cm^3/(mol*s)"),
        n = -1.17,
        Ea = (2660.63,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Walter, D.", "Grotheer, H-H."], title=u'Experimental and theoretical study of the recombination reaction CH_3 + CH_3 \u2192 C_2H_6', journal="Symp. Int. Combust. Proc.", volume="23", pages="""107-114""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000124.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 118,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.25556e+16,"cm^3/(mol*s)"),
        n = -1.1,
        Ea = (1330.32,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Robertson, S.H.", "Pilling, M.J.", "Baulch, D.L.", "Green, N.J.B."], title=u'Fitting of pressure-dependent kinetic rate data by master equation/inverse laplace transform analysis', journal="J. Phys. Chem.", volume="99", pages="""13452-13460""", year="1995", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000128.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 119,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.06092e+16,"cm^3/(mol*s)"),
        n = -1.2,
        Ea = (2452.77,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Du, H.", "Hessler, J.P.", "Ogren, P.J."], title=u'Recombination of methyl radicals. 1. New data between 1175 and 1750 K in the falloff region', journal="J. Phys. Chem.", volume="100", pages="""974-983""", year="1996", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000129.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 120,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.26459e+17,"cm^3/(mol*s)"),
        n = -1.4,
        Ea = (4173.86,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Pesa, M.", "Pilling, M.J.", "Robertson, S.H.", "Wardlaw, D.M."], title=u'Application of the canonical flexible transition state theory to CH_3, CF_3, and CCl_3', journal="J. Phys. Chem. A", volume="102", pages="""8526-8536""", year="1998", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000131.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 121,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.78106e-09,"cm^3/(mol*s)"),
        n = -0.69,
        Ea = (731.674,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Wang, B.S.", "Hou, H.", "Yoder, L.M.", "Muckerman, J.T.", "Fockenberg, C."], title=u'Experimental and theoretical investigations on the methyl-methyl recombination reaction', journal="J. Phys. Chem. A:", volume="107", pages="""11414-11426""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000159.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 122,
    label = "r00002085",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.22074e-16,"cm^3/(mol*s)"),
        n = -3.75,
        Ea = (4107.35,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Wang, B.S.", "Hou, H.", "Yoder, L.M.", "Muckerman, J.T.", "Fockenberg, C."], title=u'Experimental and theoretical investigations on the methyl-methyl recombination reaction', journal="J. Phys. Chem. A:", volume="107", pages="""11414-11426""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000160.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 123,
    label = "r00002086",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1.26e+16,"s^-1"),
        n = 0,
        Ea = (409903,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 124,
    label = "r00002086",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (8.11e+17,"s^-1"),
        n = -1.23,
        Ea = (427364,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Stewart, P.H.", "Larson, C.W.", "Golden, D.M."], title=u'Pressure and temperature dependence of reactions proceeding via a bound complex. 2. Application to 2CH\u2083 \u2192 C\u2082H\u2085 + H', journal="Combust. Flame", volume="75", pages="""25-31""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 125,
    label = "r00002086",
    reactant1 = 
"""
1  *  H     1
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,S}
3  *1 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.99e+41,"cm^3/(mol*s)"),
        n = -7.08,
        Ea = (6685,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 126,
    label = "r00002086",
    reactant1 = 
"""
1  *  H     1
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,S}
3  *1 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+41,"cm^3/(mol*s)"),
        n = -7.08,
        Ea = (6685,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 127,
    label = "r00002086",
    reactant1 = 
"""
1  *  H     1
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,S}
3  *1 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.194e+42,"cm^3/(mol*s)"),
        n = -7.08,
        Ea = (6685,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 128,
    label = "r00002086",
    reactant1 = 
"""
1  *  H     1
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,S}
3  *1 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+41,"cm^3/(mol*s)"),
        n = -7.08,
        Ea = (6685,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 129,
    label = "r00002086",
    reactant1 = 
"""
1  *  H     1
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,S}
3  *1 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.985e+41,"cm^3/(mol*s)"),
        n = -7.08,
        Ea = (6685,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 130,
    label = "r00002086",
    reactant1 = 
"""
1  *  H     1
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,S}
3  *1 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+41,"cm^3/(mol*s)"),
        n = -7.08,
        Ea = (6685,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 131,
    label = "r00002086",
    reactant1 = 
"""
1  *  H     1
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,S}
3  *1 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.97e+41,"cm^3/(mol*s)"),
        n = -7.08,
        Ea = (6685,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 132,
    label = "r00002086",
    reactant1 = 
"""
1  *  H     1
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,S}
3  *1 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.393e+41,"cm^3/(mol*s)"),
        n = -7.08,
        Ea = (6685,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 133,
    label = "r00002086",
    reactant1 = 
"""
1  *  H     1
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,S}
3  *1 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.21e+17,"cm^3/(mol*s)"),
        n = -0.99,
        Ea = (1580,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 134,
    label = "r00002163",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2e+16,"s^-1"),
        n = 0,
        Ea = (460622,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 135,
    label = "r00002163",
    reactant1 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,D}
2  *1 C     0 {1,D} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.4e+30,"cm^3/(mol*s)"),
        n = -3.86,
        Ea = (3320,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 136,
    label = "r00002163",
    reactant1 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,D}
2  *1 C     0 {1,D} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.8e+30,"cm^3/(mol*s)"),
        n = -3.86,
        Ea = (3320,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 137,
    label = "r00002163",
    reactant1 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,D}
2  *1 C     0 {1,D} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.4e+30,"cm^3/(mol*s)"),
        n = -3.86,
        Ea = (3320,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 138,
    label = "r00002163",
    reactant1 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,D}
2  *1 C     0 {1,D} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.8e+30,"cm^3/(mol*s)"),
        n = -3.86,
        Ea = (3320,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 139,
    label = "r00002163",
    reactant1 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,D}
2  *1 C     0 {1,D} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.1e+30,"cm^3/(mol*s)"),
        n = -3.86,
        Ea = (3320,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000013.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 140,
    label = "r00002163",
    reactant1 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,D}
2  *1 C     0 {1,D} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.8e+30,"cm^3/(mol*s)"),
        n = -3.86,
        Ea = (3320,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000014.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 141,
    label = "r00002163",
    reactant1 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,D}
2  *1 C     0 {1,D} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.2e+30,"cm^3/(mol*s)"),
        n = -3.86,
        Ea = (3320,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000015.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 142,
    label = "r00002163",
    reactant1 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,D}
2  *1 C     0 {1,D} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.8e+29,"cm^3/(mol*s)"),
        n = -3.86,
        Ea = (3320,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000016.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 143,
    label = "r00002163",
    reactant1 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,D}
2  *1 C     0 {1,D} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.08e+12,"cm^3/(mol*s)"),
        n = 0.27,
        Ea = (280,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000017.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 144,
    label = "r00002163",
    reactant1 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,D}
2  *1 C     0 {1,D} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.36e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (4107.35,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Duran, R.P.", "Amorebieta, V.T.", "Colussi, A.J."], title=u'Is the homogeneous thermal dimerization of acetylene a free-radical chain reaction? Kinetic and thermochemical analysis', journal="J. Phys. Chem.", volume="92", pages="""636""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000019.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 145,
    label = "r00002385",
    reactant1 = 
"""
1  *1 C     0 {2,T} {3,S}
2     C     0 {1,T}
3  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,T}
2  *  C     1 {1,T}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (460622,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Al'tshuler, B.N."], title=u'Investigation of the High Temperature Pyrolysis of Acetylene', journal="Kinet. Catal.", volume="15", pages="""835""", year="1974", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 146,
    label = "r00002385",
    reactant1 = 
"""
1  *1 C     0 {2,T} {3,S}
2     C     0 {1,T}
3  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,T}
2  *  C     1 {1,T}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.63e+15,"s^-1"),
        n = 0,
        Ea = (518823,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W.", "Hampson, R.F."], title=u'Chemical kinetic data base for combustion chemistry. Part I. Methane and related compounds', journal="J. Phys. Chem. Ref. Data", volume="15", pages="""1087""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 147,
    label = "r00002385",
    reactant1 = 
"""
1     C     0 {2,T}
2  *  C     1 {1,T}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,T}
2  *1 C     0 {1,T} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.75e+33,"cm^3/(mol*s)"),
        n = -4.8,
        Ea = (1900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 148,
    label = "r00002385",
    reactant1 = 
"""
1     C     0 {2,T}
2  *  C     1 {1,T}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,T}
2  *1 C     0 {1,T} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.5e+33,"cm^3/(mol*s)"),
        n = -4.8,
        Ea = (1900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 149,
    label = "r00002385",
    reactant1 = 
"""
1     C     0 {2,T}
2  *  C     1 {1,T}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,T}
2  *1 C     0 {1,T} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.25e+34,"cm^3/(mol*s)"),
        n = -4.8,
        Ea = (1900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000013.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 150,
    label = "r00002385",
    reactant1 = 
"""
1     C     0 {2,T}
2  *  C     1 {1,T}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,T}
2  *1 C     0 {1,T} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.5e+33,"cm^3/(mol*s)"),
        n = -4.8,
        Ea = (1900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000014.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 151,
    label = "r00002385",
    reactant1 = 
"""
1     C     0 {2,T}
2  *  C     1 {1,T}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,T}
2  *1 C     0 {1,T} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.625e+33,"cm^3/(mol*s)"),
        n = -4.8,
        Ea = (1900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000015.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 152,
    label = "r00002385",
    reactant1 = 
"""
1     C     0 {2,T}
2  *  C     1 {1,T}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,T}
2  *1 C     0 {1,T} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.5e+33,"cm^3/(mol*s)"),
        n = -4.8,
        Ea = (1900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000016.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 153,
    label = "r00002385",
    reactant1 = 
"""
1     C     0 {2,T}
2  *  C     1 {1,T}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,T}
2  *1 C     0 {1,T} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.125e+34,"cm^3/(mol*s)"),
        n = -4.8,
        Ea = (1900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000017.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 154,
    label = "r00002385",
    reactant1 = 
"""
1     C     0 {2,T}
2  *  C     1 {1,T}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,T}
2  *1 C     0 {1,T} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.625e+33,"cm^3/(mol*s)"),
        n = -4.8,
        Ea = (1900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000018.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 155,
    label = "r00002385",
    reactant1 = 
"""
1     C     0 {2,T}
2  *  C     1 {1,T}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1     C     0 {2,T}
2  *1 C     0 {1,T} {3,S}
3  *2 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+17,"cm^3/(mol*s)"),
        n = -1,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000019.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 156,
    label = "r00002698",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.31e+15,"s^-1"),
        n = 0,
        Ea = (396600,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 157,
    label = "r00002699",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *2 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1.58e+16,"s^-1"),
        n = 0,
        Ea = (408241,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 158,
    label = "r00002700",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.16e+16,"s^-1"),
        n = 0,
        Ea = (335073,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Blackmore, D.R.", "Hinshelwood, C."], title=u'Derivation of rate constants for steps in the free-radical chain decomposition of paraffins', journal="Proc. R. Soc. London A", volume="268", pages="""36""", year="1962", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 159,
    label = "r00002700",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.58e+14,"s^-1"),
        n = 0,
        Ea = (281029,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Laidler, K.J.", "Sagert, N.H.", "Wojciechowski, B.W."], title=u'Kinetics and mechanisms of the thermal decomposition of propane. I. The uninhibited reaction', journal="Proc. R. Soc. London A", volume="270", pages="""242""", year="1962", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 160,
    label = "r00002700",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.74e+14,"s^-1"),
        n = 0,
        Ea = (300152,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kao, W.", "Yeh, C."], title=u'The role of the termination reaction H + CH_3 \u2192 CH_4 in the pyrolysis of propane in the temperature range 1100-1300 K', journal="J. Chem. Phys.", volume="81", pages="""2304-2306""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 161,
    label = "r00002700",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5.01e+16,"s^-1"),
        n = 0,
        Ea = (355028,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Jezequel, J-Y.", "Baronnet, F.", "Niclause, M."], title=u'Modelisation de la pyrolyse du propane', journal="J. Chim. Phys.", volume="75", pages="""991-993""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 162,
    label = "r00002700",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.5e+16,"s^-1"),
        n = 0,
        Ea = (365837,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Chiang, C.", "Skinner, G.B."], title=u'Resonance absorption measurements of atom concentrations in reacting gas mixtures. 5. Pyrolysis of propane and propane-D_8 behind shock waves', journal="Report by Wright State University, Dept. of Chemistry, Dayton, OH 45435", pages="""1-18""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 163,
    label = "r00002700",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.5e+16,"s^-1"),
        n = 0,
        Ea = (365837,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Chiang, C.-C.", "Skinner, G.B."], title=u'Resonance Absorption Measurements of Atom Concentrations in Reacting Gas Mixtures 5. Pyrolysis of C_3H_8 and C_3D_8 Behind Shock Waves', journal="Symp. Int. Combust. Proc.", volume="18", pages="""915""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 164,
    label = "r00002700",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.7e+16,"s^-1"),
        n = 0,
        Ea = (377477,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Chiang, C.-C.", "Skinner, G.B."], title=u'Resonance Absorption Measurements of Atom Concentrations in Reacting Gas Mixtures 5. Pyrolysis of C_3H_8 and C_3D_8 Behind Shock Waves', journal="Symp. Int. Combust. Proc.", volume="18", pages="""915""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 165,
    label = "r00002700",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.47e+16,"s^-1"),
        n = 0,
        Ea = (354197,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Juste, C.", "Scacchi, G.", "Niclause, M."], title=u'Minor Products and Initiation Rate in the Chain Pyrolysis of Propane', journal="Int. J. Chem. Kinet.", volume="13", pages="""855""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 166,
    label = "r00002700",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.48e+17,"s^-1"),
        n = 0,
        Ea = (361680,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Al-Alami, M.Z.", "Kiefer, J.H."], title=u'Shock-tube study of propane pyrolysis. Rate of initial dissociation from 1400 to 2300 K', journal="J. Phys. Chem.", volume="87", pages="""499""", year="1983", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 167,
    label = "r00002700",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.74e+11,"s^-1"),
        n = 0,
        Ea = (232805,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Al-Alami, M.Z.", "Kiefer, J.H."], title=u'Shock-tube study of propane pyrolysis. Rate of initial dissociation from 1400 to 2300 K', journal="J. Phys. Chem.", volume="87", pages="""499""", year="1983", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 168,
    label = "r00002700",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5.13e+16,"s^-1"),
        n = 0,
        Ea = (349208,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kanan, K.", "Purnell, H.", "Smith, E."], title=u'Induced heterogeneity, a novel technique for the study of gas-phase reactions. Part I. Determination of the Arrhenius parameters for C-C bond scission in propane', journal="Int. J. Chem. Kinet.", volume="15", pages="""63""", year="1983", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000014.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 169,
    label = "r00002700",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5e+15,"s^-1"),
        n = 0,
        Ea = (350039,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000015.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 170,
    label = "r00002700",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.94e+16,"s^-1"),
        n = 0,
        Ea = (357522,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000016.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 171,
    label = "r00002700",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.12e+17,"s^-1"),
        n = 0,
        Ea = (355859,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dombi, A.", "Horvath, I.", "Huhn, P."], title=u'Effects of olefins on the thermal decomposition of propane. Part III. Some remarks on the kinetics of decomposition', journal="Int. J. Chem. Kinet.", volume="18", pages="""255""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000017.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 172,
    label = "r00002700",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.78e+18,"s^-1"),
        n = -1.8,
        Ea = (370825,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part 3. Propane', journal="J. Phys. Chem. Ref. Data", volume="17", pages="""887""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000018.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 173,
    label = "r00002700",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.1e+16,"s^-1"),
        n = 0,
        Ea = (351702,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hidaka, Y.", "Oki, T.", "Kawano, H."], title=u'Thermal decomposition of propane in shock waves', journal="Int. J. Chem. Kinet.", volume="21", pages="""689""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000019.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 174,
    label = "r00002700",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.94e+18,"s^-1"),
        n = -1.79,
        Ea = (370825,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Rate constants for the decomposition and formation of simple alkanes over extended temperature and pressure ranges', journal="Combust. Flame", volume="78", pages="""71-86""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000020.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 175,
    label = "r00002700",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.1e+17,"s^-1"),
        n = 0,
        Ea = (353365,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Frank, P.", "Hayman, G.", "Just, Th.", "Kerr, J.A.", "Murrells, T.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."], title=u'Evaluated kinetic data for combusion modelling. Supplement I', journal="J. Phys. Chem. Ref. Data", volume="23", pages="""847-1033""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000021.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 176,
    label = "r00002700",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.86e+17,"s^-1"),
        n = 0,
        Ea = (364174,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Belmeliani, A.", "Perrin, D.", "Martin, R."], title=u"Etude cinetique de l'ethane forme dans la pyrolyse homogene du propane et mesure de la constante de vitesse d'amorcage", journal="J. Chim. Phys.", volume="91", pages="""313-328""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000023.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 177,
    label = "r00002700",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.1e+17,"s^-1"),
        n = 0,
        Ea = (6098.48,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Mousavipour, S.H.", "Homayoon, Z."], title=u'A Theoretical Study on the Kinetics of Disproportionation Versus Association Reaction of CH_3 + C_2H_5', journal="J. Phys. Chem. A", volume="107", pages="""8566-8574""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000025.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 178,
    label = "r00002700",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *1 C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.71e+74,"cm^3/(mol*s)"),
        n = -16.82,
        Ea = (13065,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000026.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 179,
    label = "r00002700",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *1 C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.42e+74,"cm^3/(mol*s)"),
        n = -16.82,
        Ea = (13065,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000027.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 180,
    label = "r00002700",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *1 C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.626e+75,"cm^3/(mol*s)"),
        n = -16.82,
        Ea = (13065,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000028.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 181,
    label = "r00002700",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *1 C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.42e+74,"cm^3/(mol*s)"),
        n = -16.82,
        Ea = (13065,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000029.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 182,
    label = "r00002700",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *1 C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.065e+74,"cm^3/(mol*s)"),
        n = -16.82,
        Ea = (13065,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000030.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 183,
    label = "r00002700",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *1 C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.42e+74,"cm^3/(mol*s)"),
        n = -16.82,
        Ea = (13065,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000031.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 184,
    label = "r00002700",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *1 C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.13e+74,"cm^3/(mol*s)"),
        n = -16.82,
        Ea = (13065,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000032.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 185,
    label = "r00002700",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *1 C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.897e+74,"cm^3/(mol*s)"),
        n = -16.82,
        Ea = (13065,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000033.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 186,
    label = "r00002700",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *1 C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.43e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000034.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 187,
    label = "r00002700",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *1 C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1671.21,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Teng, L.", "Jones, W.E."], title=u'Kinetics of the Reactions of Hydrogen Atoms with Ethylene and Vinyl Fluoride', journal="J. Chem. Soc. Faraday Trans. 1", volume="68", pages="""1267""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000038.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 188,
    label = "r00002700",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *1 C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-47392.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Simmie, J.M.", "Gardiner, W.C., Jr.", "Eubank, C.S."], title=u'Falloff Behavior in Propane Thermal Decomposition at High Temperature', journal="J. Phys. Chem.", volume="86", pages="""799""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000042.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 189,
    label = "r00002700",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *1 C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.91e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-7108.87,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kanan, K.", "Purnell, H.", "Smith, E."], title=u'Induced heterogeneity, a novel technique for the study of gas-phase reactions. Part I. Determination of the Arrhenius parameters for C-C bond scission in propane', journal="Int. J. Chem. Kinet.", volume="15", pages="""63""", year="1983", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000044.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 190,
    label = "r00002700",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *1 C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.5e+14,"cm^3/(mol*s)"),
        n = -0.56,
        Ea = (-8.75696,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Mousavipour, S.H.", "Homayoon, Z."], title=u'A Theoretical Study on the Kinetics of Disproportionation Versus Association Reaction of CH_3 + C_2H_5', journal="J. Phys. Chem. A", volume="107", pages="""8566-8574""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000051.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 191,
    label = "r00003550",
    reactant1 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {4,S}
3  *1 C     0 {1,S} {5,S}
4     O     0 {1,S} {2,S}
5  *2 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {4,S}
3  *  C     1 {1,S}
4     O     0 {1,S} {2,S}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (8e+15,"s^-1"),
        n = 0,
        Ea = (384960,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lifshitz, A.", "Tamburu, C."], title=u'Isomerization and decomposition of propylene oxide. Studies with a single-pulse shock tube', journal="J. Phys. Chem.", volume="98", pages="""1161-1170""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:37 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 192,
    label = "r00003588",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     O     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S} {4,S}
4     O     0 {3,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (6.31e+16,"s^-1"),
        n = 0,
        Ea = (340062,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal Stability of Alcohols', journal="Int. J. Chem. Kinet.", volume="8", pages="""173""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:37 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 193,
    label = "r00003751",
    reactant1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *1 O     0 {1,S} {6,S}
6  *2 O     0 {5,S}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+13,"s^-1"),
        n = 0,
        Ea = (157975,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kirk, A.D.", "Knox, J.H."], title=u'The pyrolysis of alkyl hydroperoxides in the gas phase', journal="Trans. Faraday Soc.", volume="56", pages="""1296-1303""", year="1960", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:37 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 194,
    label = "r00003751",
    reactant1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *1 O     0 {1,S} {6,S}
6  *2 O     0 {5,S}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+15,"s^-1"),
        n = 0,
        Ea = (176267,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Benson, S.W.", "Spokes, G.N."], title=u'Very low pressure pyrolysis. III. t-Butyl hydroperoxide in fused silica and stainless steel reactors', journal="J. Phys. Chem.", volume="72", pages="""1182-1186""", year="1968", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:37 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 195,
    label = "r00003751",
    reactant1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *1 O     0 {1,S} {6,S}
6  *2 O     0 {5,S}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+15,"s^-1"),
        n = 0,
        Ea = (172941,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Mulder, P.", "Louw, R."], title=u'Gas-phase thermolysis of tert-butyl hydroperoxide in a nitrogen atmosphere. The effect of added toluene', journal="Recl. Trav. Chim. Pays-Bas", volume="103", pages="""148-152""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:37 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 196,
    label = "r00003751",
    reactant1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *1 O     0 {1,S} {6,S}
6  *2 O     0 {5,S}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+15,"s^-1"),
        n = 0,
        Ea = (177930,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Sahetchian, K.A.", "Rigny, R.", "Tardieu de Maleissye, J.", "Batt, L.", "Anwar Khan, M.", "Mathews, S."], title=u'The pyrolysis of organic hydroperoxides (ROOH)', journal="Symp. Int. Combust. Proc.", volume="24", pages="""637-643""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:37 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 197,
    label = "r00004010",
    reactant1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {5,D}
3  *1 O     0 {2,S} {4,S}
4  *2 O     0 {3,S}
5     O     0 {2,D}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {4,D}
3  *  O     1 {2,S}
4     O     0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+14,"s^-1"),
        n = 0,
        Ea = (167952,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Sahetchian, K.A.", "Rigny, R.", "Tardieu de Maleissye, J.", "Batt, L.", "Anwar Khan, M.", "Mathews, S."], title=u'The pyrolysis of organic hydroperoxides (ROOH)', journal="Symp. Int. Combust. Proc.", volume="24", pages="""637-643""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:38 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 198,
    label = "r00004033",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S} {6,S}
3  *2 C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {5,S}
5  *  C     1 {1,S} {4,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (3.98e+16,"s^-1"),
        n = 0,
        Ea = (339230,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal decomposition of 2,3-dimethylbutane in a single-pulse shock tube', journal="J. Chem. Phys.", volume="43", pages="""352-359""", year="1965", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:39 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 199,
    label = "r00004033",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S} {6,S}
3  *2 C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {5,S}
5  *  C     1 {1,S} {4,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (3.98e+16,"s^-1"),
        n = 0,
        Ea = (348376,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, R.R.", "Drewery, G.R.", "Walker, R.W."], title=u'Decomposition of 2,3-dimethylbutane in the presence of oxygen. Part 1.-Thermochemistry of the reaction (CH_3)_2CHCH(CH_3)_2 \u2192 2i-C_3H_7', journal="J. Chem. Soc. Faraday Trans. 1", volume="80", pages="""2827""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:39 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 200,
    label = "r00004187",
    reactant1 = 
"""
1  *1 C     0 {2,S} {9,S}
2     C     0 {1,S}
3     C     0 {4,B} {6,B} {9,S}
4     C     0 {3,B} {5,B} {10,S}
5     C     0 {4,B} {7,B}
6     C     0 {3,B} {8,B}
7     C     0 {5,B} {8,B}
8     C     0 {6,B} {7,B}
9  *2 O     0 {1,S} {3,S}
10    O     0 {4,S}
""",
    product1 = 
"""
1     C     0 {2,B} {3,B} {7,S}
2     C     0 {1,B} {4,B} {8,S}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6     C     0 {4,B} {5,B}
7     O     0 {1,S}
8  *  O     1 {2,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+15,"s^-1"),
        n = 0,
        Ea = (231142,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Suryan, M.M.", "Kafafi, S.A.", "Stein, S.E."], title=u'The thermal decomposition of hydroxy- and methoxy-substituted anisoles', journal="J. Am. Chem. Soc.", volume="111", pages="""1423""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:40 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 201,
    label = "r00004262",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {6,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S} {5,S}
5     C     0 {3,S} {4,S}
6  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S} {5,S}
5  *  C     1 {3,S} {4,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+12,"s^-1"),
        n = 0,
        Ea = (368331,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Brown, T.C.", "King, K.D."], title=u'Very low-pressure pyrolysis (VLPP) of methyl- and ethynyl- cyclopentanes and cyclohexanes', journal="Int. J. Chem. Kinet.", volume="21", pages="""251""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:40 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 202,
    label = "r00004286",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S} {6,B} {7,B}
6     C     0 {5,B} {9,B}
7     C     0 {5,B} {10,B}
8     C     0 {9,B} {10,B}
9     C     0 {6,B} {8,B}
10    C     0 {7,B} {8,B}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S} {4,S}
4     C     0 {3,S} {5,B} {6,B}
5     C     0 {4,B} {7,B}
6     C     0 {4,B} {9,B}
7     C     0 {5,B} {8,B}
8     C     0 {7,B} {9,B}
9     C     0 {6,B} {8,B}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (6.22e+13,"s^-1"),
        n = 0,
        Ea = (251929,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Leigh, C.H.", "Szwarc, M."], title=u'An investigation of the pyrolyses of cumene, t-butyl-benzene and p-cymene, and the relevant bond dissociation energies', journal="J. Chem. Phys.", volume="20", pages="""844-847""", year="1952", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 203,
    label = "r00004286",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S} {6,B} {7,B}
6     C     0 {5,B} {9,B}
7     C     0 {5,B} {10,B}
8     C     0 {9,B} {10,B}
9     C     0 {6,B} {8,B}
10    C     0 {7,B} {8,B}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S} {4,S}
4     C     0 {3,S} {5,B} {6,B}
5     C     0 {4,B} {7,B}
6     C     0 {4,B} {9,B}
7     C     0 {5,B} {8,B}
8     C     0 {7,B} {9,B}
9     C     0 {6,B} {8,B}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (7.94e+15,"s^-1"),
        n = 0,
        Ea = (289344,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Robaugh, D.A.", "Stein, S.E."], title=u'Very-low-pressure pyrolysis of ethylbenzene, isopropylbenzene, and tert-butylbenzene', journal="Int. J. Chem. Kinet.", volume="13", pages="""445""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 204,
    label = "r00004286",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S} {6,B} {7,B}
6     C     0 {5,B} {9,B}
7     C     0 {5,B} {10,B}
8     C     0 {9,B} {10,B}
9     C     0 {6,B} {8,B}
10    C     0 {7,B} {8,B}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S} {4,S}
4     C     0 {3,S} {5,B} {6,B}
5     C     0 {4,B} {7,B}
6     C     0 {4,B} {9,B}
7     C     0 {5,B} {8,B}
8     C     0 {7,B} {9,B}
9     C     0 {6,B} {8,B}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1.58e+16,"s^-1"),
        n = 0,
        Ea = (286018,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Brand, U.", "Hippler, H.", "Lindemann, L.", "Troe, J."], title=u'C-C and C-H bond splits of laser-excited aromatic molecules. 1. Specific and thermally averaged rate constants', journal="J. Phys. Chem.", volume="94", pages="""6305""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 205,
    label = "r00004286",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S} {4,S}
4     C     0 {3,S} {5,B} {6,B}
5     C     0 {4,B} {8,B}
6     C     0 {4,B} {9,B}
7     C     0 {8,B} {9,B}
8     C     0 {5,B} {7,B}
9     C     0 {6,B} {7,B}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {5,S}
2  *1 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S} {6,B} {7,B}
6     C     0 {5,B} {9,B}
7     C     0 {5,B} {10,B}
8     C     0 {9,B} {10,B}
9     C     0 {6,B} {8,B}
10    C     0 {7,B} {8,B}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.19e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (141.346,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Brand, U.", "Hippler, H.", "Lindemann, L.", "Troe, J."], title=u'C-C and C-H bond splits of laser-excited aromatic molecules. 1. Specific and thermally averaged rate constants', journal="J. Phys. Chem.", volume="94", pages="""6305""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 206,
    label = "r00004429",
    reactant1 = 
"""
1  *1 C     0 {8,S}
2     C     0 {3,B} {4,B} {8,S}
3     C     0 {2,B} {6,B}
4     C     0 {2,B} {7,B}
5     C     0 {6,B} {7,B}
6     C     0 {3,B} {5,B}
7     C     0 {4,B} {5,B}
8  *2 O     0 {1,S} {2,S}
""",
    product1 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B} {7,S}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6     C     0 {4,B} {5,B}
7  *  O     1 {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+13,"s^-1"),
        n = 0,
        Ea = (242783,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Paul, S.", "Back, M.H."], title=u'A kinetic determination of the dissociation energy of the C-O bond in anisole', journal="Can. J. Chem.", volume="53", pages="""3330""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 207,
    label = "r00004429",
    reactant1 = 
"""
1  *1 C     0 {8,S}
2     C     0 {3,B} {4,B} {8,S}
3     C     0 {2,B} {6,B}
4     C     0 {2,B} {7,B}
5     C     0 {6,B} {7,B}
6     C     0 {3,B} {5,B}
7     C     0 {4,B} {5,B}
8  *2 O     0 {1,S} {2,S}
""",
    product1 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B} {7,S}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6     C     0 {4,B} {5,B}
7  *  O     1 {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.2e+16,"s^-1"),
        n = 0,
        Ea = (275209,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lin, C-Y.", "Lin, M.C."], title=u'Thermal decomposition of methyl phenyl ether in shock waves: The kinetics of phenoxy radical reactions', journal="J. Phys. Chem.", volume="90", pages="""425""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 208,
    label = "r00004429",
    reactant1 = 
"""
1  *1 C     0 {8,S}
2     C     0 {3,B} {4,B} {8,S}
3     C     0 {2,B} {6,B}
4     C     0 {2,B} {7,B}
5     C     0 {6,B} {7,B}
6     C     0 {3,B} {5,B}
7     C     0 {4,B} {5,B}
8  *2 O     0 {1,S} {2,S}
""",
    product1 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B} {7,S}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6     C     0 {4,B} {5,B}
7  *  O     1 {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.61e+15,"s^-1"),
        n = 0,
        Ea = (262737,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bruinsma, O.S.L.", "Geertsman, R.S.", "Bank, P.", "Moulijn, J.A."], title=u'Gas phase pyrolysis of coal-related aromatic compounds in a coiled tube flow reactor. 1. Benzene and derivatives', journal="Fuel", volume="67", pages="""327""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 209,
    label = "r00004429",
    reactant1 = 
"""
1  *1 C     0 {8,S}
2     C     0 {3,B} {4,B} {8,S}
3     C     0 {2,B} {6,B}
4     C     0 {2,B} {7,B}
5     C     0 {6,B} {7,B}
6     C     0 {3,B} {5,B}
7     C     0 {4,B} {5,B}
8  *2 O     0 {1,S} {2,S}
""",
    product1 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B} {7,S}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6     C     0 {4,B} {5,B}
7  *  O     1 {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+14,"s^-1"),
        n = 0,
        Ea = (255254,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Back, M.H."], title=u'Comment on the thermal decomposition of anisole and the heat of formation of the phenoxy radical', journal="J. Phys. Chem.", volume="93", pages="""6880""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 210,
    label = "r00004429",
    reactant1 = 
"""
1  *1 C     0 {8,S}
2     C     0 {3,B} {4,B} {8,S}
3     C     0 {2,B} {6,B}
4     C     0 {2,B} {7,B}
5     C     0 {6,B} {7,B}
6     C     0 {3,B} {5,B}
7     C     0 {4,B} {5,B}
8  *2 O     0 {1,S} {2,S}
""",
    product1 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B} {7,S}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6     C     0 {4,B} {5,B}
7  *  O     1 {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.9e+15,"s^-1"),
        n = 0,
        Ea = (267726,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Mackie, J.C.", "Doolan, K.R.", "Nelson, P.F."], title=u'Kinetics of the thermal decomposition of methoxybenzene (anisole)', journal="J. Phys. Chem.", volume="93", pages="""664""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 211,
    label = "r00004429",
    reactant1 = 
"""
1  *1 C     0 {8,S}
2     C     0 {3,B} {4,B} {8,S}
3     C     0 {2,B} {6,B}
4     C     0 {2,B} {7,B}
5     C     0 {6,B} {7,B}
6     C     0 {3,B} {5,B}
7     C     0 {4,B} {5,B}
8  *2 O     0 {1,S} {2,S}
""",
    product1 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B} {7,S}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6     C     0 {4,B} {5,B}
7  *  O     1 {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+15,"s^-1"),
        n = 0,
        Ea = (266063,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Suryan, M.M.", "Kafafi, S.A.", "Stein, S.E."], title=u'The thermal decomposition of hydroxy- and methoxy-substituted anisoles', journal="J. Am. Chem. Soc.", volume="111", pages="""1423""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 212,
    label = "r00004429",
    reactant1 = 
"""
1  *1 C     0 {8,S}
2     C     0 {3,B} {4,B} {8,S}
3     C     0 {2,B} {6,B}
4     C     0 {2,B} {7,B}
5     C     0 {6,B} {7,B}
6     C     0 {3,B} {5,B}
7     C     0 {4,B} {5,B}
8  *2 O     0 {1,S} {2,S}
""",
    product1 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B} {7,S}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6     C     0 {4,B} {5,B}
7  *  O     1 {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+15,"s^-1"),
        n = 0,
        Ea = (266063,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Arends, I.W.C.E.", "Louw, R.", "Mulder, P."], title=u'Kinetic study of the thermolysis of anisole in a hydrogen atmosphere', journal="J. Phys. Chem.", volume="97", pages="""7914-7925""", year="1993", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 213,
    label = "r00004452",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {14,S}
2     C     0 {1,S} {4,B} {5,B}
3     C     0 {1,S} {6,B} {7,B}
4     C     0 {2,B} {10,B}
5     C     0 {2,B} {11,B}
6     C     0 {3,B} {12,B}
7     C     0 {3,B} {13,B}
8     C     0 {10,B} {11,B}
9     C     0 {12,B} {13,B}
10    C     0 {4,B} {8,B}
11    C     0 {5,B} {8,B}
12    C     0 {6,B} {9,B}
13    C     0 {7,B} {9,B}
14 *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S} {4,B} {5,B}
2     C     0 {3,S} {6,B} {7,B}
3  *  C     1 {1,S} {2,S}
4     C     0 {1,B} {8,B}
5     C     0 {1,B} {10,B}
6     C     0 {2,B} {11,B}
7     C     0 {2,B} {12,B}
8     C     0 {4,B} {9,B}
9     C     0 {8,B} {10,B}
10    C     0 {5,B} {9,B}
11    C     0 {6,B} {13,B}
12    C     0 {7,B} {13,B}
13    C     0 {11,B} {12,B}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2e+15,"s^-1"),
        n = 0,
        Ea = (340893,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rossi, M.J.", "McMillen, D.F.", "Golden, D.M."], title=u'Aliphatic C-H bond scission processes in diphenylmethane and 2-benzyl- and 4-benzylpyridine. The head of formation of the diphenylmethyl and \u03b1-phenylethyl radical in the gas phase', journal="J. Phys. Chem.", volume="88", pages="""5031""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 214,
    label = "r00004456",
    reactant1 = 
"""
1  *1 C     0 {3,B} {4,B} {13,S}
2     C     0 {5,B} {6,B} {13,S}
3     C     0 {1,B} {9,B}
4     C     0 {1,B} {10,B}
5     C     0 {2,B} {11,B}
6     C     0 {2,B} {12,B}
7     C     0 {9,B} {10,B}
8     C     0 {11,B} {12,B}
9     C     0 {3,B} {7,B}
10    C     0 {4,B} {7,B}
11    C     0 {5,B} {8,B}
12    C     0 {6,B} {8,B}
13 *2 O     0 {1,S} {2,S}
""",
    product1 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B} {7,S}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6     C     0 {4,B} {5,B}
7  *  O     1 {2,S}
""",
    product2 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6  *  C     1 {4,B} {5,B}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.16e+15,"s^-1"),
        n = 0,
        Ea = (316781,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["van Scheppingen, W.", "Dorrestijn, E.", "Arends, I.", "Mulder, P.", "Korth, H-G."], title=u'Carbon-oxygen bond strength in diphenyl ether and phenyl vinyl ether: an experimental and computational study', journal="J. Phys. Chem. A", volume="101", pages="""5404-5411""", year="1997", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 215,
    label = "r00004476",
    reactant1 = 
"""
1  *1 C     0 {2,S} {9,S}
2     C     0 {1,S}
3     C     0 {4,B} {5,B} {9,S}
4     C     0 {3,B} {7,B}
5     C     0 {3,B} {8,B}
6     C     0 {7,B} {8,B}
7     C     0 {4,B} {6,B}
8     C     0 {5,B} {6,B}
9  *2 O     0 {1,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B} {7,S}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6     C     0 {4,B} {5,B}
7  *  O     1 {2,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+15,"s^-1"),
        n = 0,
        Ea = (252760,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Colussi, A.J.", "Zabel, F.", "Benson, S.W."], title=u'The very low-pressure pyrolysis of phenyl ethyl ether, phenyl allyl ether, and benzyl methyl ether and the enthalpy of formation of the phenoxy radical', journal="Int. J. Chem. Kinet.", volume="9", pages="""161""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:44 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 216,
    label = "r00004476",
    reactant1 = 
"""
1  *1 C     0 {2,S} {9,S}
2     C     0 {1,S}
3     C     0 {4,B} {5,B} {9,S}
4     C     0 {3,B} {7,B}
5     C     0 {3,B} {8,B}
6     C     0 {7,B} {8,B}
7     C     0 {4,B} {6,B}
8     C     0 {5,B} {6,B}
9  *2 O     0 {1,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B} {7,S}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6     C     0 {4,B} {5,B}
7  *  O     1 {2,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+15,"s^-1"),
        n = 0,
        Ea = (259412,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Suryan, M.M.", "Kafafi, S.A.", "Stein, S.E."], title=u'The thermal decomposition of hydroxy- and methoxy-substituted anisoles', journal="J. Am. Chem. Soc.", volume="111", pages="""1423""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:44 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 217,
    label = "r00004483",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5     C     0 {3,S} {6,B} {7,B}
6     C     0 {5,B} {9,B}
7     C     0 {5,B} {10,B}
8     C     0 {9,B} {10,B}
9     C     0 {6,B} {8,B}
10    C     0 {7,B} {8,B}
""",
    product1 = 
"""
1     C     0 {2,S} {8,S}
2     C     0 {1,S} {3,B} {4,B}
3     C     0 {2,B} {5,B}
4     C     0 {2,B} {7,B}
5     C     0 {3,B} {6,B}
6     C     0 {5,B} {7,B}
7     C     0 {4,B} {6,B}
8  *  C     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+14,"s^-1"),
        n = 0,
        Ea = (281029,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Esteban, G.L.", "Kerr, J.A.", "Trotman-Dickenson, A.F."], title=u'Pyrolysis of ethyl-, n-propyl-, and n-butyl-benzene and the heats of formation of the benzyl and n-propyl radicals', journal="J. Chem. Soc.", pages="""3873""", year="1963", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:44 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 218,
    label = "r00004586",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
5  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {3,S}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1e+16,"s^-1"),
        n = 0,
        Ea = (397432,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 219,
    label = "r00004587",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *1 C     0 {1,S} {5,S}
4     C     0 {2,S}
5  *2 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *  C     1 {2,S}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1.58e+16,"s^-1"),
        n = 0,
        Ea = (409903,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 220,
    label = "r00004651",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S} {4,D}
4     C     0 {3,D}
5  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,S}
3     C     0 {2,S} {4,D}
4     C     0 {3,D}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.26e+15,"s^-1"),
        n = 0,
        Ea = (345051,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 221,
    label = "r00004730",
    reactant1 = 
"""
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3  *1 C     0 {1,D} {5,S}
4     C     0 {2,D}
5  *2 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4  *  C     1 {2,D}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.58e+16,"s^-1"),
        n = 0,
        Ea = (460622,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 222,
    label = "r00004730",
    reactant1 = 
"""
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3  *1 C     0 {1,D} {5,S}
4     C     0 {2,D}
5  *2 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4  *  C     1 {2,D}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (7e+14,"s^-1"),
        n = 0,
        Ea = (397432,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hidaka, Y.", "Higashihara, T.", "Ninomiya, N.", "Oshita, H.", "Kawano, H."], title=u'Thermal isomerization and decomposition of 2-butyne in shock waves', journal="J. Phys. Chem.", volume="97", pages="""10977-10983""", year="1993", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 223,
    label = "r00004807",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S} {4,T}
4     C     0 {3,T}
5  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,S}
3     C     0 {2,S} {4,T}
4     C     0 {3,T}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7e+14,"s^-1"),
        n = 0,
        Ea = (360017,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hidaka, Y.", "Higashihara, T.", "Ninomiya, N.", "Oshita, H.", "Kawano, H."], title=u'Thermal isomerization and decomposition of 2-butyne in shock waves', journal="J. Phys. Chem.", volume="97", pages="""10977-10983""", year="1993", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:48 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 224,
    label = "r00004825",
    reactant1 = 
"""
1  *1 C     0 {3,S}
2     C     0 {4,S}
3  *2 C     0 {1,S} {4,D}
4     C     0 {2,S} {3,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,D}
3  *  C     1 {2,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.16e+17,"s^-1"),
        n = 0,
        Ea = (415724,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:48 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 225,
    label = "r00004826",
    reactant1 = 
"""
1  *1 C     0 {3,S} {5,S}
2     C     0 {4,S}
3     C     0 {1,S} {4,D}
4     C     0 {2,S} {3,D}
5  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D} {4,S}
4  *  C     1 {3,S}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (3.98e+15,"s^-1"),
        n = 0,
        Ea = (355859,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:48 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 226,
    label = "r00005303",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S} {5,D}
5     C     0 {4,D}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+16,"s^-1"),
        n = 0,
        Ea = (298490,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal Decomposition of Cyclopentane and Related Compounds', journal="Int. J. Chem. Kinet.", volume="10", pages="""599""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:51 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 227,
    label = "r00005303",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S} {5,D}
5     C     0 {4,D}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+16,"s^-1"),
        n = 0,
        Ea = (295995,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Brown, T.C.", "King, K.D.", "Nguyen, T.T."], title=u'Kinetics of primary processes in the pyrolysis of cyclopentanes and cyclohexanes', journal="J. Phys. Chem.", volume="90", pages="""419""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:51 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 228,
    label = "r00005356",
    reactant1 = 
"""
1  *1 C     0 {2,S} {5,S}
2     C     0 {1,S}
3     C     0 {4,D} {5,S}
4     C     0 {3,D}
5  *2 O     0 {1,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3  *  O     1 {2,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8e+15,"s^-1"),
        n = 0,
        Ea = (292669,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Blades, A.T.", "Murphy, G.W."], title=u'Kinetics of the thermal decomposition of vinyl ethyl ether', journal="J. Am. Chem. Soc.", volume="74", pages="""1039-1041""", year="1952", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:51 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 229,
    label = "r00005356",
    reactant1 = 
"""
1  *1 C     0 {2,S} {5,S}
2     C     0 {1,S}
3     C     0 {4,D} {5,S}
4     C     0 {3,D}
5  *2 O     0 {1,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3  *  O     1 {2,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (275209,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rosenfeld, R.N.", "Brauman, J.I.", "Barker, J.R.", "Golden, D.M."], title=u'Infrared photodecomposition of ethyl vinyl ether. A chemical probe of multiphoton dynamics', journal="J. Am. Chem. Soc.", volume="99", pages="""8063-8064""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:51 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 230,
    label = "r00005412",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {9,S}
2     C     0 {6,S} {7,S} {8,S} {10,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.2e+16,"s^-1"),
        n = 0,
        Ea = (163795,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Raley, J.H.", "Rust, F.F.", "Vaughan, W.E."], title=u'Decompositions of Di-t-alkyl peroxides. I. Kinetics', journal="J. Am. Chem. Soc.", volume="70", pages="""88-94""", year="1948", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 231,
    label = "r00005412",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {9,S}
2     C     0 {6,S} {7,S} {8,S} {10,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.5e+14,"s^-1"),
        n = 0,
        Ea = (150492,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Murawski, J.", "Roberts, J.S.", "Szwarc, M."], title=u'Kinetics of the thermal decomposition of di-t-butyl peroxide', journal="J. Chem. Phys.", volume="19", pages="""698""", year="1951", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 232,
    label = "r00005412",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {9,S}
2     C     0 {6,S} {7,S} {8,S} {10,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.56e+15,"s^-1"),
        n = 0,
        Ea = (157144,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Brinton, R.K.", "Volman, D.H."], title=u'Decomposition of di-t-butyl peroxide and kinetics of the gas phase reaction of t-butoxy radicals in the presence of ethylenimine', journal="J. Chem. Phys.", volume="20", pages="""25""", year="1952", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 233,
    label = "r00005412",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {9,S}
2     C     0 {6,S} {7,S} {8,S} {10,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.87e+16,"s^-1"),
        n = 0,
        Ea = (157975,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Jaquiss, M.T.", "Robert, J.S.", "Szwarc, M."], title=u'The reactions of methyl radicals with acetone', journal="J. Am. Chem. Soc.", volume="74", pages="""6005""", year="1952", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 234,
    label = "r00005412",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {9,S}
2     C     0 {6,S} {7,S} {8,S} {10,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7e+15,"s^-1"),
        n = 0,
        Ea = (158806,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lossing, F.P.", "Tickner, A.W."], title=u'Free radicals by mass spectrometry. I. The measurement of methyl radical concentrations', journal="J. Chem. Phys.", volume="20", pages="""907-914""", year="1952", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 235,
    label = "r00005412",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {9,S}
2     C     0 {6,S} {7,S} {8,S} {10,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4e+16,"s^-1"),
        n = 0,
        Ea = (162964,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Pritchard, G.O.", "Pritchard, H.O.", "Trotman-Dickenson, A.F."], title=u'The reactions of methyl radicals with acetone, diethyl ketone, and di-tert.-butyl peroxide', journal="J. Chem. Soc.", pages="""1425""", year="1954", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 236,
    label = "r00005412",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {9,S}
2     C     0 {6,S} {7,S} {8,S} {10,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.95e+17,"s^-1"),
        n = 0,
        Ea = (159638,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Birss, F.W.", "Danby, C.J.", "Hinshelwood, C."], title=u'The thermal dissociation of tertiary butyl peroxide in presence of nitric oxide', journal="Proc. R. Soc. London A", volume="239", pages="""154-164""", year="1957", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 237,
    label = "r00005412",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {9,S}
2     C     0 {6,S} {7,S} {8,S} {10,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.5e+16,"s^-1"),
        n = 0,
        Ea = (162132,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Blake, A.R.", "Kutschke, K.O."], title=u'The reaction of methyl radicals with formaldehyde', journal="Can. J. Chem.", volume="37", pages="""1462""", year="1957", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 238,
    label = "r00005412",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {9,S}
2     C     0 {6,S} {7,S} {8,S} {10,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.5e+16,"s^-1"),
        n = 0,
        Ea = (162132,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Blake, A.R.", "Kutschke, K.O."], title=u'The reaction of methyl radicals with formaldehyde', journal="Can. J. Chem.", volume="37", pages="""1462""", year="1959", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 239,
    label = "r00005412",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {9,S}
2     C     0 {6,S} {7,S} {8,S} {10,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.2e+16,"s^-1"),
        n = 0,
        Ea = (160469,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Mulcahy, M.F.R.", "Williams, D.J."], title=u'A stirred-flow reactor for investigating the kinetics of gaseous reactions: application to the decomposition of di-t-butyl peroxide', journal="Aust. J. Chem.", volume="14", pages="""534-544""", year="1961", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 240,
    label = "r00005412",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {9,S}
2     C     0 {6,S} {7,S} {8,S} {10,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+15,"s^-1"),
        n = 0,
        Ea = (156312,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L.", "Benson, S.W."], title=u'Pyrolysis of di-tertiary butyl peroxide: temperature gradients and chain contribution to the rate', journal="J. Chem. Phys.", volume="36", pages="""895""", year="1962", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 241,
    label = "r00005412",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {9,S}
2     C     0 {6,S} {7,S} {8,S} {10,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.61e+12,"s^-1"),
        n = 0,
        Ea = (130537,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baker, G.", "Shaw, R."], title=u'Reactions of methoxyl, ethoxyl, and t-butoxyl with nitric oxide and with nitrogen dioxide', journal="J. Chem. Soc.", pages="""6965""", year="1965", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 242,
    label = "r00005412",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {9,S}
2     C     0 {6,S} {7,S} {8,S} {10,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.61e+15,"s^-1"),
        n = 0,
        Ea = (157975,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Shaw, D.H.", "Pritchard, H.O."], title=u'Thermal decomposition of di-tert-buyl peroxide at high pressure', journal="Can. J. Chem.", volume="46", pages="""2721""", year="1968", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000013.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 243,
    label = "r00005412",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {9,S}
2     C     0 {6,S} {7,S} {8,S} {10,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.02e+16,"s^-1"),
        n = 0,
        Ea = (162964,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Retzloff, D.G.", "Coull, B.M.", "Coull, J."], title=u'A microchemical study of gas-phase kinetics for three irreversible reactions', journal="J. Phys. Chem.", volume="74", pages="""2455""", year="1970", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000014.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 244,
    label = "r00005412",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {9,S}
2     C     0 {6,S} {7,S} {8,S} {10,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+14,"s^-1"),
        n = 0,
        Ea = (148829,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Cadman, P.", "Trotman-Dickenson, A.F.", "White, A.J."], title=u'Kinetics and Pressure-Dependence of the t-Butoxyl Radical Decomposition', journal="J. Chem. Soc. A", pages="""2296""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000015.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 245,
    label = "r00005412",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {9,S}
2     C     0 {6,S} {7,S} {8,S} {10,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+15,"s^-1"),
        n = 0,
        Ea = (156312,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Perona, M.J.", "Golden, D.M."], title=u'Very Low-Pressure Pyrolysis. VIII. The Decomposition of Di-t-Amyl Peroxide', journal="Int. J. Chem. Kinet.", volume="5", pages="""55""", year="1973", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000016.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 246,
    label = "r00005412",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {9,S}
2     C     0 {6,S} {7,S} {8,S} {10,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.14e+15,"s^-1"),
        n = 0,
        Ea = (152155,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lewis, D.K."], title=u'Di-tert-butyl peroxide decomposition behind shock waves', journal="Can. J. Chem.", volume="54", pages="""581-585""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000017.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 247,
    label = "r00005412",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {9,S}
2     C     0 {6,S} {7,S} {8,S} {10,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.61e+15,"s^-1"),
        n = 0,
        Ea = (157975,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Loucks, L.F.", "Liu, M.T.H.", "Hooper, D.G."], title=u'Pyrolysis of trifluoroacetaldehyde, initiated by di-tertiary-butyl peroxide decomposition', journal="Can. J. Chem.", volume="57", pages="""2201""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000018.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 248,
    label = "r00005412",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {9,S}
2     C     0 {6,S} {7,S} {8,S} {10,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+15,"s^-1"),
        n = 0,
        Ea = (159638,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Al Akeel, N.Y.", "Selby, K.", "Waddington, D.J."], title=u'Reactions of Oxygenated Radicals in the Gas Phase. Part 8. Reactions of Alkoxyl Radicals with Aldehydes and Ketones', journal="J. Chem. Soc. Perkin Trans. 2", pages="""1036""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000020.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 249,
    label = "r00005412",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {9,S}
2     C     0 {6,S} {7,S} {8,S} {10,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+15,"s^-1"),
        n = 0,
        Ea = (154649,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L.", "Robinson, G.N."], title=u'Decomposition of the t-butoxy radical', journal="Phys. Chem. Behav. Atmos. Pollut. Proc. Eur. Symp.", pages="""172""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000021.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 250,
    label = "r00005412",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {9,S}
2     C     0 {6,S} {7,S} {8,S} {10,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.24e+15,"s^-1"),
        n = 0,
        Ea = (154649,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L.", "Robinson, G.N."], title=u'Decomposition of the t-Butoxy radical. I. Studies over the temperature range 402-443 K', journal="Int. J. Chem. Kinet.", volume="19", pages="""391""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000022.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 251,
    label = "r00005412",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {9,S}
2     C     0 {6,S} {7,S} {8,S} {10,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.04e+15,"s^-1"),
        n = 0,
        Ea = (156312,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Sway, M.I."], title=u'Kinetics of abstraction reactions of tert-butoxyl radicals with cyclohexane and methyl-substituted cyclohexanes in the gas phase', journal="J. Chem. Soc. Faraday Trans.", volume="87", pages="""2157-2159""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000024.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 252,
    label = "r00005412",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {9,S}
2     C     0 {6,S} {7,S} {8,S} {10,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.72e+15,"s^-1"),
        n = 0,
        Ea = (156312,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Seres, L.", "Nacsa, A.", "Arthur, N.L."], title=u'Thermal decomposition of di-t-butyl peroxide in the presence of (CH_3)_2C=CH_2: reactions of CH_3, (CH_3)_2CCH_2CH_3, and (CH_3)_2CCH_2C(CH_3)_2CH_2CH_3 radicals', journal="Int. J. Chem. Kinet.", volume="26", pages="""227-246""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000025.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 253,
    label = "r00005412",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {9,S}
2     C     0 {6,S} {7,S} {8,S} {10,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (152155,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kortvelyesi, T.", "Seres, L."], title=u'Thermal reaction of (CH_3)_2C=C(CH_3)_2 in the presence of di-tert-butyl peroxide; reactions of the radicals ^.CH_3, (CH_3)_3C^.C(CH_3)_2 and (CH_3)_2 C=C(CH_3)^.CH_2', journal="J. Chim. Phys.", volume="93", pages="""253-273""", year="1996", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000026.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 254,
    label = "r00005417",
    reactant1 = 
"""
1     C     0 {2,S} {4,S} {5,S}
2  *1 C     0 {1,S} {3,S}
3  *2 C     0 {2,S} {7,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {7,S}
7     C     0 {3,S} {6,S} {8,D}
8     O     0 {7,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {4,D}
3  *  C     1 {2,S}
4     O     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+16,"s^-1"),
        n = 0,
        Ea = (337568,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Single pulse shock tube study on the thermal stability of ketones', journal="Int. J. Chem. Kinet.", volume="16", pages="""1543""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 255,
    label = "r00005511",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *1 C     0 {1,S} {5,S} {7,S}
4     C     0 {2,S} {6,S}
5     C     0 {3,S} {6,D}
6     C     0 {4,S} {5,D}
7  *2 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S} {6,D}
5  *  C     1 {3,S} {6,S}
6     C     0 {4,D} {5,S}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (5.01e+15,"s^-1"),
        n = 0,
        Ea = (341725,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 256,
    label = "r00005574",
    reactant1 = 
"""
1     C     0 {3,S} {5,S}
2     C     0 {4,S} {6,S}
3     C     0 {1,S} {4,S}
4     C     0 {2,S} {3,S}
5  *1 C     0 {1,S} {7,S}
6     C     0 {2,S} {8,S}
7  *2 C     0 {5,S}
8     C     0 {6,S}
""",
    product1 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {5,S}
4     C     0 {1,S} {6,S}
5     C     0 {3,S} {7,S}
6     C     0 {4,S}
7  *  C     1 {5,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.16e+16,"s^-1"),
        n = 0,
        Ea = (316781,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Blackmore, D.R.", "Hinshelwood, C."], title=u'Derivation of rate constants for steps in the free-radical chain decomposition of paraffins', journal="Proc. R. Soc. London A", volume="268", pages="""36""", year="1962", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 257,
    label = "r00005574",
    reactant1 = 
"""
1     C     0 {3,S} {5,S}
2     C     0 {4,S} {6,S}
3     C     0 {1,S} {4,S}
4     C     0 {2,S} {3,S}
5  *1 C     0 {1,S} {7,S}
6     C     0 {2,S} {8,S}
7  *2 C     0 {5,S}
8     C     0 {6,S}
""",
    product1 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {5,S}
4     C     0 {1,S} {6,S}
5     C     0 {3,S} {7,S}
6     C     0 {4,S}
7  *  C     1 {5,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2e+15,"s^-1"),
        n = 0,
        Ea = (325096,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Doolan, K>R.", "Mackie, J.C."], title=u'Kinetics of pyrolysis of octane in argon-hydrogen mixtures', journal="Combust. Flame", volume="50", pages="""29""", year="1983", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 258,
    label = "r00005623",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1.1e+11,"s^-1"),
        n = 0,
        Ea = (300984,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Szwarc, M."], title=u'The kinetics of the thermal decomposition of propylene', journal="J. Chem. Phys.", volume="17", pages="""284-291""", year="1949", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:54 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 259,
    label = "r00005623",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (4.57e+14,"s^-1"),
        n = 0,
        Ea = (371657,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Naroznik, M.", "Niedzielski, J."], title=u'Propylene photolysis at 6.7 eV: Calculation of the quantum yields for the secondary processes', journal="J. Photochem.", volume="32", pages="""281""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:54 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 260,
    label = "r00005623",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.5e+15,"s^-1"),
        n = 0,
        Ea = (362511,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:54 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 261,
    label = "r00005623",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (5e+13,"s^-1"),
        n = 0,
        Ea = (335073,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hidaka, Y.", "Nakamura, T.", "Tanaka, H.", "Jinno, A.", "Kawano, H."], title=u'Shock tube and modeling study of propene pyrolysis', journal="Int. J. Chem. Kinet.", volume="24", pages="""761-780""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:54 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 262,
    label = "r00005623",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (5.01e+12,"s^-1"),
        n = 0,
        Ea = (296827,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Barbe, P.", "Martin, R.", "Perrin, D.", "Scacchi, G."], title=u'Kinetics and modeling of the thermal reaction of propene at 800 K. Part I. Pure propene', journal="Int. J. Chem. Kinet.", volume="28", pages="""829-847""", year="1996", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:54 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 263,
    label = "r00005625",
    reactant1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,D}
3  *1 C     0 {2,D} {4,S}
4  *2 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,D}
3  *  C     1 {2,D}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.59e+14,"s^-1"),
        n = 0,
        Ea = (424038,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Naroznik, M.", "Niedzielski, J."], title=u'Propylene photolysis at 6.7 eV: Calculation of the quantum yields for the secondary processes', journal="J. Photochem.", volume="32", pages="""281""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:54 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 264,
    label = "r00005626",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D} {4,S}
3     C     0 {2,D}
4  *2 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,D}
3  *  C     1 {1,S} {2,D}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.45e+15,"s^-1"),
        n = 0,
        Ea = (409903,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Naroznik, M.", "Niedzielski, J."], title=u'Propylene photolysis at 6.7 eV: Calculation of the quantum yields for the secondary processes', journal="J. Photochem.", volume="32", pages="""281""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:54 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 265,
    label = "r00005814",
    reactant1 = 
"""
1  *1 C     0 {3,S} {5,S}
2     C     0 {3,S}
3     C     0 {1,S} {2,S} {4,D}
4     C     0 {3,D}
5  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,D} {4,S}
3     C     0 {2,D}
4  *  C     1 {2,S}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (5e+12,"s^-1"),
        n = 0,
        Ea = (-280198,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Szwarc, M."], title=u'The kinetics of the thermal decomposition of isobutene', journal="J. Chem. Phys.", volume="17", pages="""292-295""", year="1949", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:55 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 266,
    label = "r00005814",
    reactant1 = 
"""
1  *1 C     0 {3,S} {5,S}
2     C     0 {3,S}
3     C     0 {1,S} {2,S} {4,D}
4     C     0 {3,D}
5  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,D} {4,S}
3     C     0 {2,D}
4  *  C     1 {2,S}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (2e+15,"s^-1"),
        n = 0,
        Ea = (365837,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Douhou, S.", "Perrin, D.", "Martin, R."], title=u"Etude cinetique et modelisaiton de la reaction thermique de l'isobutene vers 800 K. I. Isobutene pur", journal="J. Chim. Phys.", volume="91", pages="""1597-1627""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:55 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 267,
    label = "r00005814",
    reactant1 = 
"""
1  *1 C     0 {3,S} {5,S}
2     C     0 {3,S}
3     C     0 {1,S} {2,S} {4,D}
4     C     0 {3,D}
5  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,D} {4,S}
3     C     0 {2,D}
4  *  C     1 {2,S}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1.538e+19,"s^-1"),
        n = -0.865,
        Ea = (1443.03,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Santhanam, S.", "Kiefer, J.H.", "Tranter, R.S.", "Srinivasan, N.K."], title=u'A Shock Tube, Laser-Schlieren Study of the Pyrolysis of Isobutene: Relaxation, Incubation, and Dissociation Rates', journal="Int. J", volume="35", pages="""381-390""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:55 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 268,
    label = "r00005988",
    reactant1 = 
"""
1  *1 C     0 {3,S} {4,B} {5,B}
2     C     0 {3,S} {6,B} {7,B}
3  *2 C     0 {1,S} {2,S} {14,D}
4     C     0 {1,B} {10,B}
5     C     0 {1,B} {11,B}
6     C     0 {2,B} {12,B}
7     C     0 {2,B} {13,B}
8     C     0 {10,B} {11,B}
9     C     0 {12,B} {13,B}
10    C     0 {4,B} {8,B}
11    C     0 {5,B} {8,B}
12    C     0 {6,B} {9,B}
13    C     0 {7,B} {9,B}
14    O     0 {3,D}
""",
    product1 = 
"""
1     C     0 {2,B} {3,B} {7,S}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {6,B}
4     C     0 {2,B} {5,B}
5     C     0 {4,B} {6,B}
6     C     0 {3,B} {5,B}
7  *  C     1 {1,S} {8,D}
8     O     0 {7,D}
""",
    product2 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6  *  C     1 {4,B} {5,B}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.6e+16,"s^-1"),
        n = 0,
        Ea = (365837,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Clark, D.", "Pritchard, H.O."], title=u'Arrhenius parameters of some reactions involving multiplicity changes', journal="J. Chem. Soc. London", pages="""2136-2140""", year="1956", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:56 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 269,
    label = "r00006092",
    reactant1 = 
"""
1  *1 C     0 {4,S} {5,S}
2     C     0 {4,S}
3     C     0 {5,S}
4  *2 C     0 {1,S} {2,S} {6,D}
5     C     0 {1,S} {3,S} {7,D}
6     O     0 {4,D}
7     O     0 {5,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {4,D}
3  *  C     1 {2,S}
4     O     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,D}
3     O     0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.12e+17,"s^-1"),
        n = 0,
        Ea = (311793,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Choudhury, T.K.", "Lin, M.C."], title=u'Homogeneous pyrolysis of acetylacetone at high temperatures in shock waves', journal="Int. J. Chem. Kinet.", volume="20", pages="""491""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:57 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 270,
    label = "r00006343",
    reactant1 = 
"""
1     C     0 {3,S} {5,S}
2     C     0 {4,S} {6,S}
3     C     0 {1,S} {7,S}
4     C     0 {2,S} {8,S}
5  *1 C     0 {1,S} {9,S}
6     C     0 {2,S} {9,S}
7     C     0 {3,S}
8     C     0 {4,S}
9  *2 O     0 {5,S} {6,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S} {5,S}
5  *  O     1 {4,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *  C     1 {2,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.1e+13,"s^-1"),
        n = 0,
        Ea = (214513,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Enguehard, F.", "Kressmann, S.", "Domine, F."], title=u'Kinetics of dibutylether pyrolysis at high pressure: Experimental study', journal="Adv. Org. Geochem.", volume="16", pages="""155""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:58 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 271,
    label = "r00006863",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {4,S}
3  *1 C     0 {1,S} {4,S} {5,D}
4  *2 C     0 {2,S} {3,S} {6,D}
5     O     0 {3,D}
6     O     0 {4,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,D}
3     O     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,D}
3     O     0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+10,"s^-1"),
        n = 0,
        Ea = (281029,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hole, K.J.", "Mulcahy, M.F.R."], title=u'The pyrolysis of biacetyl and the third-body effect on the combination of methyl radicals', journal="J. Phys. Chem.", volume="73", pages="""177""", year="1969", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:01 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 272,
    label = "r00006863",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {4,S}
3  *1 C     0 {1,S} {4,S} {5,D}
4  *2 C     0 {2,S} {3,S} {6,D}
5     O     0 {3,D}
6     O     0 {4,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,D}
3     O     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,D}
3     O     0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+16,"s^-1"),
        n = 0,
        Ea = (283523,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Knoll, H.", "Scherzer, K.", "Geiseler, G."], title=u'The Thermal Decomposition of Biacetyl', journal="Int. J. Chem. Kinet.", volume="5", pages="""271""", year="1973", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:01 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 273,
    label = "r00006863",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {4,S}
3  *1 C     0 {1,S} {4,S} {5,D}
4  *2 C     0 {2,S} {3,S} {6,D}
5     O     0 {3,D}
6     O     0 {4,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,D}
3     O     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,D}
3     O     0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+15,"s^-1"),
        n = 0,
        Ea = (279366,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Scherzer, K.", "Plarre, D."], title=u'Der Thermische Zerfall von Diacetyl. II. Mitteilung: Untersuchungen bei hohen Temperaturen', journal="Z. Phys. Chem. (Leipzig)", volume="256", pages="""660""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:01 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 274,
    label = "r00006863",
    reactant1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,D}
3     O     0 {2,D}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {4,S}
3  *1 C     0 {1,S} {4,S} {5,D}
4  *2 C     0 {2,S} {3,S} {6,D}
5     O     0 {3,D}
6     O     0 {4,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-3741.51,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Maricq, M.M.", "Szente, J.J."], title=u'The UV spectrum of acetyl and the kinetics of the chain reaction between acetaldehyde and chlorine', journal="Chem. Phys. Lett.", volume="253", pages="""333-339""", year="1996", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000013.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:01 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 275,
    label = "r00006906",
    reactant1 = 
"""
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,T}
3  *1 C     0 {1,T} {5,S}
4     C     0 {2,T}
5  *2 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,T} {3,S}
2     C     0 {1,T}
3     C     0 {1,S} {4,T}
4  *  C     1 {3,T}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.2e+14,"s^-1"),
        n = 0,
        Ea = (488060,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Frank, P.", "Just, Th."], title=u'High Temperature Thermal Decomposition of Acetylene and Diacetylene at Low Relative Concentrations', journal="Combust. Flame", volume="38", pages="""231""", year="1980", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:01 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 276,
    label = "r00006950",
    reactant1 = 
"""
1  *1 C     0 {3,S} {6,S}
2     C     0 {4,S} {7,S}
3     C     0 {1,S}
4     C     0 {2,S}
5     C     0 {6,S} {7,S}
6  *2 O     0 {1,S} {5,S}
7     O     0 {2,S} {5,S}
""",
    product1 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3     C     0 {4,S} {5,S}
4     O     0 {1,S} {3,S}
5  *  O     1 {3,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.09e+16,"s^-1"),
        n = 0,
        Ea = (317613,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Herzler, J.", "Manion, J.A.", "Tsang, W."], title=u'Single-pulse shock tube studies of the decomposition of ethoxy compounds', journal="J. Phys. Chem. A", volume="101", pages="""5494-5499""", year="1997", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:01 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 277,
    label = "r00007080",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S} {6,S} {7,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.58e+16,"s^-1"),
        n = 0,
        Ea = (305141,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal decomposition of hexamethylethane, 2,2,3-trimethylbutane, and neopentane in a single-pulse shock tube', journal="J. Chem. Phys.", volume="44", pages="""4283-4295""", year="1966", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:02 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 278,
    label = "r00007080",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S} {6,S} {7,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+16,"s^-1"),
        n = 0,
        Ea = (305973,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Comparative rate single-pulse shock tube studies on the thermal decomposition of cyclohexene, 2,2,3-trimethylbutane, isopropyl bromide, and ethylcyclobutane', journal="Int. J. Chem. Kinet.", volume="2", pages="""311""", year="1970", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:02 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 279,
    label = "r00007080",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S} {6,S} {7,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.88e+16,"s^-1"),
        n = 0,
        Ea = (305141,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, R.R.", "Walker, R.W.", "Walker, R.W."], title=u'Decomposition of 2,2,3-Trimethylbutane in the Presence of Oxygen', journal="J. Chem. Soc. Faraday Trans. 1", volume="76", pages="""825""", year="1980", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:02 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 280,
    label = "r00007090",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S} {6,S} {7,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     O     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,S}
3     O     0 {2,S}
""",
    product2 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.14e+16,"s^-1"),
        n = 0,
        Ea = (311793,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal Stability of Alcohols', journal="Int. J. Chem. Kinet.", volume="8", pages="""173""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:02 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 281,
    label = "r00007144",
    reactant1 = 
"""
1  *1 C     0 {3,S}
2     C     0 {4,S}
3  *2 C     0 {1,S} {4,T}
4     C     0 {2,S} {3,T}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,T}
3  *  C     1 {2,T}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1e+17,"s^-1"),
        n = 0,
        Ea = (502194,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hidaka, Y.", "Higashihara, T.", "Ninomiya, N.", "Oshita, H.", "Kawano, H."], title=u'Thermal isomerization and decomposition of 2-butyne in shock waves', journal="J. Phys. Chem.", volume="97", pages="""10977-10983""", year="1993", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:03 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 282,
    label = "r00007145",
    reactant1 = 
"""
1  *1 C     0 {3,S} {5,S}
2     C     0 {4,S}
3     C     0 {1,S} {4,T}
4     C     0 {2,S} {3,T}
5  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2  *  C     1 {4,S}
3     C     0 {1,S} {4,T}
4     C     0 {2,S} {3,T}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (3.16e+15,"s^-1"),
        n = 0,
        Ea = (365005,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:03 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 283,
    label = "r00007547",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S} {6,D}
6     C     0 {5,D}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S} {4,S}
4     C     0 {3,S} {5,D}
5     C     0 {4,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (7.94e+16,"s^-1"),
        n = 0,
        Ea = (286849,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Trenwith, A.B."], title=u'Dissociation of 1-butene, 3-methyl-1-butene, and of 3,3-dimethyl-1-butene and the resonance energy of the allyl, methyl allyl and dimethyl allyl radicals', journal="Trans. Faraday Soc.", volume="66", pages="""2805-2811""", year="1970", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:08 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 284,
    label = "r00007547",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S} {6,D}
6     C     0 {5,D}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S} {4,S}
4     C     0 {3,S} {5,D}
5     C     0 {4,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1.58e+16,"s^-1"),
        n = 0,
        Ea = (295164,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal Stability of Alcohols', journal="Int. J. Chem. Kinet.", volume="8", pages="""173""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:08 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 285,
    label = "r00007562",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S} {6,S} {7,S}
3     C     0 {1,S} {8,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {5,S}
2     C     0 {1,S}
3     C     0 {5,S}
4     C     0 {5,S}
5  *  C     1 {1,S} {3,S} {4,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.41e+16,"s^-1"),
        n = 0,
        Ea = (298490,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal decomposition of 3,4-dimethylpentene-1,2,3,3-trimethylpentane, 3,3-dimethylpentane, and isobutylbenzene in a single pulse shock tube', journal="Int. J. Chem. Kinet.", volume="1", pages="""245""", year="1969", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:08 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 286,
    label = "r00007564",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S} {6,S}
3     C     0 {1,S} {7,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {5,S}
2     C     0 {1,S}
3     C     0 {5,S}
4     C     0 {5,S}
5  *  C     1 {1,S} {3,S} {4,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.72e+16,"s^-1"),
        n = 0,
        Ea = (322602,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal decomposition of 3,4-dimethylpentene-1,2,3,3-trimethylpentane, 3,3-dimethylpentane, and isobutylbenzene in a single pulse shock tube', journal="Int. J. Chem. Kinet.", volume="1", pages="""245""", year="1969", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:08 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 287,
    label = "r00007566",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S} {5,D}
5     C     0 {4,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,S}
3     C     0 {2,S} {4,D}
4     C     0 {3,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.94e+15,"s^-1"),
        n = 0,
        Ea = (287681,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Trenwith, A.B."], title=u'Dissociation of 1-butene, 3-methyl-1-butene, and of 3,3-dimethyl-1-butene and the resonance energy of the allyl, methyl allyl and dimethyl allyl radicals', journal="Trans. Faraday Soc.", volume="66", pages="""2805-2811""", year="1970", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:08 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 288,
    label = "r00007602",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {5,S}
5     C     0 {1,S} {4,S} {6,D}
6     C     0 {5,D}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {4,S}
3     C     0 {1,S} {4,S} {5,D}
4  *  C     1 {2,S} {3,S}
5     C     0 {3,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1e+16,"s^-1"),
        n = 0,
        Ea = (296827,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal Stability of Alcohols', journal="Int. J. Chem. Kinet.", volume="8", pages="""173""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:08 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 289,
    label = "r00007656",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S} {5,S} {6,S}
2  *2 C     0 {1,S} {3,S} {7,S}
3     C     0 {2,S} {8,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {1,S}
7     C     0 {2,S}
8     C     0 {3,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+16,"s^-1"),
        n = 0,
        Ea = (302647,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal Decomposition of 3,4-Dimethylhexane, 2,2,3-Trimethylpentane, tert-Butylcyclohexane, and Related Hydrocarbons', journal="J. Phys. Chem.", volume="76", pages="""143""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:09 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 290,
    label = "r00007657",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {6,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
5     C     0 {6,S}
6  *2 C     0 {1,S} {5,S} {7,D}
7     O     0 {6,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,D}
3     O     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+16,"s^-1"),
        n = 0,
        Ea = (318444,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Single pulse shock tube study on the thermal stability of ketones', journal="Int. J. Chem. Kinet.", volume="16", pages="""1543""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:09 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 291,
    label = "r00007681",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2  *2 C     0 {1,S} {4,S} {6,S}
3     C     0 {1,S} {7,S}
4     C     0 {2,S} {8,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {3,S}
8     C     0 {4,S}
""",
    product1 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {3,S}
""",
    product2 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.19e+16,"s^-1"),
        n = 0,
        Ea = (315118,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal Decomposition of 3,4-Dimethylhexane, 2,2,3-Trimethylpentane, tert-Butylcyclohexane, and Related Hydrocarbons', journal="J. Phys. Chem.", volume="76", pages="""143""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:09 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 292,
    label = "r00007774",
    reactant1 = 
"""
1  *1 C     0 {2,S} {5,S}
2     C     0 {1,S} {4,D}
3     C     0 {4,D}
4     C     0 {2,D} {3,D}
5  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S} {4,D}
2  *  C     1 {1,S}
3     C     0 {4,D}
4     C     0 {1,D} {3,D}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2e+15,"s^-1"),
        n = 0,
        Ea = (359185,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:10 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 293,
    label = "r00007893",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S} {4,D}
4     C     0 {3,D} {5,S}
5     C     0 {4,S} {6,D}
6     C     0 {5,D}
""",
    product1 = 
"""
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D} {5,S}
4     C     0 {2,D}
5  *  C     1 {3,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.32e+15,"s^-1"),
        n = 0,
        Ea = (277703,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Trenwith, A.B."], title=u'Dissociation of 1,3-Hexadiene and the Resonance Energy of the Pentadienyl Radical', journal="J. Chem. Soc. Faraday Trans. 1", volume="76", pages="""266""", year="1980", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:10 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 294,
    label = "r00007897",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {7,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S} {6,D}
5     C     0 {3,D} {6,S}
6     C     0 {4,D} {5,S}
7  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3  *  C     1 {1,S} {5,S}
4     C     0 {2,D} {6,S}
5     C     0 {3,S} {6,D}
6     C     0 {4,S} {5,D}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (5.01e+15,"s^-1"),
        n = 0,
        Ea = (303478,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:11 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 295,
    label = "r00008054",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {7,S}
2  *2 C     0 {1,S} {5,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {2,S}
7     O     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S} {4,S}
4     O     0 {3,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.74e+16,"s^-1"),
        n = 0,
        Ea = (310961,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal Stability of Alcohols', journal="Int. J. Chem. Kinet.", volume="8", pages="""173""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:11 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 296,
    label = "r00008082",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S} {5,T}
5     C     0 {4,T}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,S}
3     C     0 {2,S} {4,T}
4     C     0 {3,T}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2e+16,"s^-1"),
        n = 0,
        Ea = (299321,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Nguyen, T.T.", "King, K.D."], title=u'Kinetics of Decomposition and Interconversion of 3-Methylbut-1-yne and 3-Methylbuta-1,2-diene. Resonance Stabilization Energies of Propargylic Radicals', journal="J. Phys. Chem.", volume="85", pages="""3130""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:12 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 297,
    label = "r00008084",
    reactant1 = 
"""
1  *1 C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {5,D}
4     C     0 {5,D}
5     C     0 {3,D} {4,D}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {4,D}
3  *  C     1 {1,S} {4,D}
4     C     0 {2,D} {3,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2e+16,"s^-1"),
        n = 0,
        Ea = (315118,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Nguyen, T.T.", "King, K.D."], title=u'Kinetics of Decomposition and Interconversion of 3-Methylbut-1-yne and 3-Methylbuta-1,2-diene. Resonance Stabilization Energies of Propargylic Radicals', journal="J. Phys. Chem.", volume="85", pages="""3130""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:12 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 298,
    label = "r00008095",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S} {4,D}
4     C     0 {3,D}
5     O     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,D}
2  *  C     1 {1,S} {4,S}
3     C     0 {1,D}
4     O     0 {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.82e+16,"s^-1"),
        n = 0,
        Ea = (289344,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Trenwith, A.B."], title=u'Dissociation of 3-Hydroxybut-1-ene and the Resonance Energy of the Hydroxyallyl Radical', journal="J. Chem. Soc. Faraday Trans. 1", volume="69", pages="""1737""", year="1973", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:12 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 299,
    label = "r00008118",
    reactant1 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3     C     0 {5,S}
4  *1 C     0 {1,S} {5,S} {7,D}
5  *2 C     0 {3,S} {4,S} {6,D}
6     O     0 {5,D}
7     O     0 {4,D}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *  C     1 {1,S} {4,D}
4     O     0 {3,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,D}
3     O     0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.91e+16,"s^-1"),
        n = 0,
        Ea = (283523,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Scherzer, K.", "Knoll, H.", "Geiseler, G."], title=u'Thermische und durch Methylradikale initiierte Spaltung von Pentandion-(2,3) bei geringen Umsaetzen', journal="J. Prakt. Chem.", volume="316", pages="""415""", year="1974", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:12 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 300,
    label = "r00008133",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S}
3     C     0 {1,S} {5,B} {6,B}
4     C     0 {1,S} {7,B} {8,B}
5     C     0 {3,B} {11,B}
6     C     0 {3,B} {12,B}
7     C     0 {4,B} {13,B}
8     C     0 {4,B} {14,B}
9     C     0 {11,B} {12,B}
10    C     0 {13,B} {14,B}
11    C     0 {5,B} {9,B}
12    C     0 {6,B} {9,B}
13    C     0 {7,B} {10,B}
14    C     0 {8,B} {10,B}
""",
    product1 = 
"""
1     C     0 {3,S} {4,B} {5,B}
2     C     0 {3,S} {6,B} {7,B}
3  *  C     1 {1,S} {2,S}
4     C     0 {1,B} {8,B}
5     C     0 {1,B} {10,B}
6     C     0 {2,B} {11,B}
7     C     0 {2,B} {12,B}
8     C     0 {4,B} {9,B}
9     C     0 {8,B} {10,B}
10    C     0 {5,B} {9,B}
11    C     0 {6,B} {13,B}
12    C     0 {7,B} {13,B}
13    C     0 {11,B} {12,B}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+15,"s^-1"),
        n = 0,
        Ea = (282692,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Robaugh, D.A.", "Stein, S.E."], title=u'Stabilities of highly conjugated radicals from bond homolysis rates', journal="J. Am. Chem. Soc.", volume="108", pages="""3224-3229""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:12 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 301,
    label = "r00008332",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {7,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {6,S}
5     C     0 {6,S}
6     C     0 {4,S} {5,S} {7,D}
7     C     0 {1,S} {6,D}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {5,S}
4     C     0 {1,S} {2,S} {6,D}
5  *  C     1 {3,S} {6,S}
6     C     0 {4,D} {5,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1e+16,"s^-1"),
        n = 0,
        Ea = (291007,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal Decomposition of 1,1,2,2-Tetramethylcyclopropane in a Single-Pulse Shock Tube', journal="Int. J. Chem. Kinet.", volume="5", pages="""651""", year="1973", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:15 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 302,
    label = "r00008396",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *2 C     0 {1,S}
3     C     0 {5,S}
4     C     0 {1,S} {5,T}
5     C     0 {3,S} {4,T}
""",
    product1 = 
"""
1     C     0 {3,S}
2  *  C     1 {4,S}
3     C     0 {1,S} {4,T}
4     C     0 {2,S} {3,T}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+16,"s^-1"),
        n = 0,
        Ea = (303478,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Nguyen, T.T.", "King, K.D."], title=u'Very Low-Pressure Pyrolysis (VLPP ) of Pentynes. III. Pent-2-yne. Heat of Formation and Resonance Stabilization Energy of the 3-Methylpropargyl Radical', journal="Int. J. Chem. Kinet.", volume="14", pages="""613""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:15 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 303,
    label = "r00008426",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {7,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,T}
4     C     0 {2,S} {6,T}
5     C     0 {3,T}
6     C     0 {4,T}
7  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2  *  C     1 {1,S} {4,S}
3     C     0 {1,S} {5,T}
4     C     0 {2,S} {6,T}
5     C     0 {3,T}
6     C     0 {4,T}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2e+15,"s^-1"),
        n = 0,
        Ea = (345882,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:15 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 304,
    label = "r00008431",
    reactant1 = 
"""
1     C     0 {3,S} {5,S}
2     C     0 {4,S} {6,S}
3     C     0 {1,S}
4     C     0 {2,S}
5  *1 O     0 {1,S} {6,S}
6  *2 O     0 {2,S} {5,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3  *  O     1 {2,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.51e+12,"s^-1"),
        n = 0,
        Ea = (132200,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Harris, E.J.", "Egerton, A.C."], title=u'The decomposition and ignition of peroxides. I. Diethylperoxide', journal="Proc. R. Soc. London A", volume="168", pages="""1-18""", year="1938", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:15 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 305,
    label = "r00008431",
    reactant1 = 
"""
1     C     0 {3,S} {5,S}
2     C     0 {4,S} {6,S}
3     C     0 {1,S}
4     C     0 {2,S}
5  *1 O     0 {1,S} {6,S}
6  *2 O     0 {2,S} {5,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3  *  O     1 {2,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.1e+13,"s^-1"),
        n = 0,
        Ea = (133032,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rebbert, R.E.", "Laidler, K.J."], title=u'Kinetics of the decomposition of diethyl peroxide', journal="J. Chem. Phys.", volume="20", pages="""574-577""", year="1952", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:15 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 306,
    label = "r00008431",
    reactant1 = 
"""
1     C     0 {3,S} {5,S}
2     C     0 {4,S} {6,S}
3     C     0 {1,S}
4     C     0 {2,S}
5  *1 O     0 {1,S} {6,S}
6  *2 O     0 {2,S} {5,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3  *  O     1 {2,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+16,"s^-1"),
        n = 0,
        Ea = (156312,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Leggett, C.", "Thynne, J.C.J."], title=u'Thermal decomposition of dialkyl peroxides and heats of formation of the ethoxyl and isopropoxyl radicals', journal="Trans. Faraday Soc.", volume="63", pages="""2504-2509""", year="1967", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:15 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 307,
    label = "r00008727",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S} {5,S}
2     C     0 {1,D}
3     C     0 {1,S} {4,T}
4     C     0 {3,T}
5  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D} {3,S}
3     C     0 {2,S} {4,T}
4     C     0 {3,T}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.58e+15,"s^-1"),
        n = 0,
        Ea = (414061,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ghibaudi, E.", "Colussi, A.J."], title=u'Kinetics and thermochemistry of the equilibrium 2 (acetylene) = vinylacetylene. Direct evidence against a chain mechanism', journal="J. Phys. Chem.", volume="92", pages="""5839""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:17 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 308,
    label = "r00008727",
    reactant1 = 
"""
1  *  H     1
""",
    reactant2 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D} {3,S}
3     C     0 {2,S} {4,T}
4     C     0 {3,T}
""",
    product1 = 
"""
1  *2 C     0 {2,D} {3,S} {5,S}
2     C     0 {1,D}
3     C     0 {1,S} {4,T}
4     C     0 {3,T}
5  *1 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.15e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3367.36,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Duran, R.P.", "Amorebieta, V.T.", "Colussi, A.J."], title=u'Is the homogeneous thermal dimerization of acetylene a free-radical chain reaction? Kinetic and thermochemical analysis', journal="J. Phys. Chem.", volume="92", pages="""636""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:17 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 309,
    label = "r00008728",
    reactant1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S} {4,T}
4  *1 C     0 {3,T} {5,S}
5  *2 H     0 {4,S}
""",
    product1 = 
"""
1  *  H     1
""",
    product2 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S} {4,T}
4  *  C     1 {3,T}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.1e+13,"s^-1"),
        n = 0,
        Ea = (335073,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hidaka, Y.", "Tanaka, K.", "Suga, M."], title=u'Thermal decomposition of vinylacetylene in shock waves. Rate constant of initiation reaction', journal="Chem. Phys. Lett.", volume="130", pages="""195""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:17 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 310,
    label = "r00008728",
    reactant1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S} {4,T}
4  *1 C     0 {3,T} {5,S}
5  *2 H     0 {4,S}
""",
    product1 = 
"""
1  *  H     1
""",
    product2 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3     C     0 {1,S} {4,T}
4  *  C     1 {3,T}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.3e+13,"s^-1"),
        n = 0,
        Ea = (364174,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hidaka, Y.", "Masaoka, H.", "Oshita, H.", "Nakamura, T.", "Tanaka, K.", "Kawano, H."], title=u'Thermal decomposition of vinylacetylene in shock waves', journal="Int. J. Chem. Kinet.", volume="24", pages="""871-885""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:17 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 311,
    label = "r00008770",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {5,S}
4     C     0 {2,S}
5     C     0 {3,S} {6,T}
6     C     0 {5,T}
""",
    product1 = 
"""
1  *  C     1 {2,S}
2     C     0 {1,S} {3,T}
3     C     0 {2,T}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+15,"s^-1"),
        n = 0,
        Ea = (301815,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal Stability of Intermediate Sized Acetylenic Compounds and the Heats of Formation of Propargyl Radicals', journal="Int. J. Chem. Kinet.", volume="10", pages="""687""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:17 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 312,
    label = "r00008770",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {5,S}
4     C     0 {2,S}
5     C     0 {3,S} {6,T}
6     C     0 {5,T}
""",
    product1 = 
"""
1  *  C     1 {2,S}
2     C     0 {1,S} {3,T}
3     C     0 {2,T}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+15,"s^-1"),
        n = 0,
        Ea = (295995,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["King, K.D."], title=u'Kinetics of Competitive Pathways in the Thermal Unimolecular Decomposition of Hex-1-yne', journal="Int. J. Chem. Kinet.", volume="13", pages="""273""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:17 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 313,
    label = "r00008918",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S} {4,B} {6,B}
4     C     0 {3,B} {7,S} {8,B}
5     C     0 {1,S} {7,D}
6     C     0 {3,B} {10,B}
7     C     0 {4,S} {5,D}
8     C     0 {4,B} {9,B}
9     C     0 {8,B} {10,B}
10    C     0 {6,B} {9,B}
""",
    product1 = 
"""
1     C     0 {2,B} {3,S} {4,B}
2     C     0 {1,B} {5,S} {6,B}
3     C     0 {1,S} {7,D}
4     C     0 {1,B} {8,B}
5  *  C     1 {2,S} {7,S}
6     C     0 {2,B} {9,B}
7     C     0 {3,D} {5,S}
8     C     0 {4,B} {9,B}
9     C     0 {6,B} {8,B}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+16,"s^-1"),
        n = 0,
        Ea = (292669,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Robaugh, D.A.", "Stein, S.E."], title=u'Stabilities of highly conjugated radicals from bond homolysis rates', journal="J. Am. Chem. Soc.", volume="108", pages="""3224-3229""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:19 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 314,
    label = "r00008930",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S} {6,B} {7,B}
5     C     0 {1,S} {8,B} {9,B}
6     C     0 {4,B} {12,B}
7     C     0 {4,B} {13,B}
8     C     0 {5,B} {14,B}
9     C     0 {5,B} {15,B}
10    C     0 {12,B} {13,B}
11    C     0 {14,B} {15,B}
12    C     0 {6,B} {10,B}
13    C     0 {7,B} {10,B}
14    C     0 {8,B} {11,B}
15    C     0 {9,B} {11,B}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,S} {4,S}
3     C     0 {2,S} {5,B} {6,B}
4     C     0 {2,S} {7,B} {8,B}
5     C     0 {3,B} {9,B}
6     C     0 {3,B} {11,B}
7     C     0 {4,B} {12,B}
8     C     0 {4,B} {13,B}
9     C     0 {5,B} {10,B}
10    C     0 {9,B} {11,B}
11    C     0 {6,B} {10,B}
12    C     0 {7,B} {14,B}
13    C     0 {8,B} {14,B}
14    C     0 {12,B} {13,B}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5.01e+15,"s^-1"),
        n = 0,
        Ea = (275209,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Robaugh, D.A.", "Stein, S.E."], title=u'Stabilities of highly conjugated radicals from bond homolysis rates', journal="J. Am. Chem. Soc.", volume="108", pages="""3224-3229""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:19 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 315,
    label = "r00009062",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S} {6,T}
6     C     0 {5,T}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S} {4,S}
4     C     0 {3,S} {5,T}
5     C     0 {4,T}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (6.31e+15,"s^-1"),
        n = 0,
        Ea = (295995,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["King, K.D."], title=u'Very Low-Pressure Pyrolysis (VLPP) of 3,3-Dimethylbut-1-yne (tert-Butyl Acetylene). The Heat of Formation and Stabilization Energy of the Dimethylpropargyl Radical', journal="Int. J. Chem. Kinet.", volume="9", pages="""907""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:21 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 316,
    label = "r00009241",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {6,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {7,S}
6     C     0 {1,S} {7,T}
7     C     0 {5,S} {6,T}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {5,S}
4  *  C     1 {1,S} {2,S} {6,S}
5     C     0 {3,S} {6,T}
6     C     0 {4,S} {5,T}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.51e+16,"s^-1"),
        n = 0,
        Ea = (298490,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["King, K.D.", "Nguyen, T.T."], title=u'Very Low-Pressure Pyrolysis (VLPP) of Pentynes. II. 4-Methylpent-2-yne and 4,4-Dimethyl-pent-2-yne. Heats of Formation and Resonance Stabilization Energies of Methyl-Substituted Propargyl Radicals', journal="Int. J. Chem. Kinet.", volume="13", pages="""255""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:23 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 317,
    label = "r00009347",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S}
3     C     0 {1,S} {5,D}
4     C     0 {1,S} {6,D}
5     C     0 {3,D}
6     C     0 {4,D}
""",
    product1 = 
"""
1  *  C     1 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S} {5,D}
4     C     0 {2,D}
5     C     0 {3,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.29e+15,"s^-1"),
        n = 0,
        Ea = (271883,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Trenwith, A.B."], title=u'Dissociation of 3-Methylpenta-1,4-diene and the Resonance Energy of the Pentadienyl Radical', journal="J. Chem. Soc. Faraday Trans. 1", volume="78", pages="""3131""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:24 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 318,
    label = "r00009389",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *1 C     0 {1,S} {11,S}
4     C     0 {2,S}
5     C     0 {6,B} {7,B} {11,S}
6     C     0 {5,B} {9,B}
7     C     0 {5,B} {10,B}
8     C     0 {9,B} {10,B}
9     C     0 {6,B} {8,B}
10    C     0 {7,B} {8,B}
11 *2 O     0 {3,S} {5,S}
""",
    product1 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B} {7,S}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6     C     0 {4,B} {5,B}
7  *  O     1 {2,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *  C     1 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+16,"s^-1"),
        n = 0,
        Ea = (274378,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Walker, J.A.", "Tsang, W."], title=u'Single-pulse shock tube studies on the thermal decomposition of n-butyl phenyl ether, n-pentylbenzene, and phenotole and the heat of formation of phenoxy and benzyl radicals', journal="J. Phys. Chem.", volume="94", pages="""3324""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:25 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 319,
    label = "r00009454",
    reactant1 = 
"""
1  *  H     1
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 H     0 {2,S}
2  *2 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+18,"cm^3/(mol*s)"),
        n = -1,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000018.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:25 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 320,
    label = "r00009454",
    reactant1 = 
"""
1  *  H     1
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 H     0 {2,S}
2  *2 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+16,"cm^3/(mol*s)"),
        n = -0.6,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000019.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:25 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 321,
    label = "r00009454",
    reactant1 = 
"""
1  *  H     1
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 H     0 {2,S}
2  *2 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+19,"cm^3/(mol*s)"),
        n = -1.25,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000020.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:25 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 322,
    label = "r00009454",
    reactant1 = 
"""
1  *  H     1
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 H     0 {2,S}
2  *2 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.5e+20,"cm^3/(mol*s)"),
        n = -2,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000021.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:25 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 323,
    label = "r00009454",
    reactant1 = 
"""
1  *  H     1
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 H     0 {2,S}
2  *2 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+18,"cm^3/(mol*s)"),
        n = -1,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000022.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:25 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 324,
    label = "r00009454",
    reactant1 = 
"""
1  *  H     1
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 H     0 {2,S}
2  *2 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+17,"cm^3/(mol*s)"),
        n = -1,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000023.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:25 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 325,
    label = "r00009454",
    reactant1 = 
"""
1  *  H     1
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 H     0 {2,S}
2  *2 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+18,"cm^3/(mol*s)"),
        n = -1,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000024.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:25 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 326,
    label = "r00009454",
    reactant1 = 
"""
1  *  H     1
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 H     0 {2,S}
2  *2 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.09e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6269.11,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dingle, J.R.", "Le Roy, D.J."], title=u'Kinetics of the reaction of atomic hydrogen with acetylene', journal="J. Chem. Phys.", volume="18", pages="""1632-1637""", year="1950", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000026.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:25 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 327,
    label = "r00009780",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S} {6,S} {7,S} {8,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+16,"s^-1"),
        n = 0,
        Ea = (286849,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal decomposition of hexamethylethane, 2,2,3-trimethylbutane, and neopentane in a single-pulse shock tube', journal="J. Chem. Phys.", volume="44", pages="""4283-4295""", year="1966", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000020.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:27 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 328,
    label = "r00009780",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S} {6,S} {7,S} {8,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+16,"s^-1"),
        n = 0,
        Ea = (284355,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Golden, D.M.", "Alfassi, Z.B.", "Beadle, P.C."], title=u"Very Low-Pressure Pyrolysis (VLPP) of Alkanes: n-Butane, 2,3-Dimethylbutane, 2,2',3,3'-Tetramethylbutane, and Isobutane", journal="Int. J. Chem. Kinet.", volume="6", pages="""359""", year="1974", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000021.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:27 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 329,
    label = "r00009780",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S} {6,S} {7,S} {8,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.03e+16,"s^-1"),
        n = 0,
        Ea = (290175,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Atri, G.M.", "Baldwin, R.R.", "Evans, G.A.", "Walker, R.W."], title=u'Decomposition of 2,2,3,3-Tetramethylbutane in the Presence of Oxygen', journal="J. Chem. Soc. Faraday Trans. 1", volume="74", pages="""366""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000022.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:27 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 330,
    label = "r00009780",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S} {6,S} {7,S} {8,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+10,"s^-1"),
        n = 0,
        Ea = (180424,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Taylor, J.E.", "Milazzo, T.S."], title=u'Gas-Phase Pyrolysis of 2,2,3,3-Tetramethylbutane using a Wall-less Reactor', journal="Int. J. Chem. Kinet.", volume="10", pages="""1245""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000023.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:27 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 331,
    label = "r00009780",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S} {6,S} {7,S} {8,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+17,"s^-1"),
        n = 0,
        Ea = (304310,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Evidence for Strongly Temperature-Dependent A Factors in Alkane Decomposition and High Heats of Formation for Alkyl Radicals', journal="Int. J. Chem. Kinet.", volume="10", pages="""821""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000024.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:27 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 332,
    label = "r00009780",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S} {6,S} {7,S} {8,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+16,"s^-1"),
        n = 0,
        Ea = (286018,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Evidence for Strongly Temperature-Dependent A Factors in Alkane Decomposition and High Heats of Formation for Alkyl Radicals', journal="Int. J. Chem. Kinet.", volume="10", pages="""821""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000025.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:27 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 333,
    label = "r00009780",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S} {6,S} {7,S} {8,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+17,"s^-1"),
        n = 0,
        Ea = (299321,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Walker, J.A.", "Tsang, W."], title=u'Thermal Decomposition of Hexamethylethane in a Flow System', journal="Int. J. Chem. Kinet.", volume="11", pages="""867""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000026.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:27 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 334,
    label = "r00009780",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S} {6,S} {7,S} {8,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.04e+17,"s^-1"),
        n = 0,
        Ea = (294332,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, R.R.", "Hisham, M.W.M.", "Keen, A.", "Walker, R.W."], title=u'The Decomposition of 2,2,3,3-Tetramethylbutane in KCl- and B_2O_3-coateed Vessels in the Presence of Oxygen', journal="J. Chem. Soc. Faraday Trans. 1", volume="78", pages="""1165""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000027.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:27 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 335,
    label = "r00009783",
    reactant1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    reactant2 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S} {7,D}
7     C     0 {6,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.24409e+14,"cm^3/(mol*s)"),
        n = -0.75,
        Ea = (-548.755,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:27 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 336,
    label = "r00009789",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+16,"s^-1"),
        n = 0,
        Ea = (320107,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Davidson, I.M.T.", "Barton, T.J.", "Hughes, K.J.", "Ijadi-Maghsoodi, S.", "Revis, A.", "Paul, G.C."], title=u'Kinetics of radical-forming homolyses in alkenyl- and tert-butyisilanes. The stability of \u03b1- and \u03b2-silicon-substituted alkyl radicals', journal="Organometallics", volume="6", pages="""644""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:27 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 337,
    label = "r00009801",
    reactant1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 C     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.63e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-2494.34,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part 4. Isobutane', journal="J. Phys. Chem. Ref. Data", volume="19", pages="""1-68""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:28 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 338,
    label = "r00009801",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.26e+16,"s^-1"),
        n = 0,
        Ea = (327590,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal decomposition of hexamethylethane, 2,2,3-trimethylbutane, and neopentane in a single-pulse shock tube', journal="J. Chem. Phys.", volume="44", pages="""4283-4295""", year="1966", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:28 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 339,
    label = "r00009801",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.12e+18,"s^-1"),
        n = 0,
        Ea = (359185,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Halstead, M.P.", "Konar, R.S.", "Leathard, D.A.", "Marshall, R.M.", "Purnell, J.H."], title=u'The self-inhibited pyrolysis of neopentane at small extents of reaction', journal="Proc. R. Soc. London A", volume="310", pages="""525""", year="1969", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:28 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 340,
    label = "r00009801",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (7.94e+16,"s^-1"),
        n = 0,
        Ea = (336736,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Taylor, J.E.", "Hutchings, D.A.", "Frech, K.J."], title=u'Homogeneous gas-phase pyrolyses using a wall-less reactor. I. Neopentane', journal="J. Am. Chem. Soc.", volume="91", pages="""2215-2219""", year="1969", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:28 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 341,
    label = "r00009801",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (6.31e+16,"s^-1"),
        n = 0,
        Ea = (343388,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baronnet, F.", "Dzierzynski, M.", "Come, G.M.", "Martin, R.", "Niclause, M."], title=u'The Pyrolysis of Neopentane at Small Extents of Reaction', journal="Int. J. Chem. Kinet.", volume="3", pages="""197""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:28 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 342,
    label = "r00009801",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (5.01e+17,"s^-1"),
        n = 0,
        Ea = (355859,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Pacey, P.D."], title=u'The Reaction of Methyl Radicals with Neopentane', journal="Can. J. Chem.", volume="51", pages="""2415""", year="1973", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:28 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 343,
    label = "r00009801",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (3.3e+16,"s^-1"),
        n = 0,
        Ea = (335905,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bradley, J.N.", "West, K.O."], title=u'Single-pulse Shock Tube Studies of Hydrocarbon Pyrolysis. Part 5. Pyrolysis of Neopentane', journal="J. Chem. Soc. Faraday Trans. 1", volume="72", pages="""8""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:28 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 344,
    label = "r00009801",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.26e+16,"s^-1"),
        n = 0,
        Ea = (330085,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Marshall, R.M.", "Purnell, H.", "Storey, P.D."], title=u'Chain Initiation of Neopentane Pyrolysis and a Suggested Reconciliation of the Thermochemically Calculated and Measured Rate Constants for the Recombination of t-Butyl Radicals', journal="J. Chem. Soc. Faraday Trans. 1", volume="72", pages="""85""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:28 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 345,
    label = "r00009801",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (3.98e+17,"s^-1"),
        n = 0,
        Ea = (351702,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Marquaire, P.M.", "Come, G.M."], title=u'Non Quasi-Stationary State Pyrolysis. Kinetic Parameters of Neopentane Pyrolysis Mechanism', journal="React. Kinet. Catal. Lett.", volume="9", pages="""171""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:28 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 346,
    label = "r00009801",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2e+17,"s^-1"),
        n = 0,
        Ea = (338399,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, A.C.", "Lewis, K.E.", "Golden, D.M."], title=u'Very-Low-Pressure Pyrolysis (VLPP) of Group IV(A) Tetramethyls: Neopentane and Tetramethyltin', journal="Int. J. Chem. Kinet.", volume="11", pages="""529""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:28 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 347,
    label = "r00009801",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.38e+15,"s^-1"),
        n = 0,
        Ea = (333410,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Pratt, G.L.", "Rogers, D."], title=u'Wall-less Studies. Part 5. - Neopentane Pyrolysis', journal="J. Chem. Soc. Faraday Trans. 1", volume="77", pages="""2751""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000014.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:28 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 348,
    label = "r00009801",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.7e+17,"s^-1"),
        n = 0,
        Ea = (351702,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bernfeld, D.", "Skinner, G.B."], title=u'Formation of hydrogen atoms in pyrolysis of 2,2-dimethylpropane behind shock waves', journal="J. Phys. Chem.", volume="87", pages="""3732""", year="1983", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000015.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:28 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 349,
    label = "r00009801",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.1e+13,"s^-1"),
        n = 0,
        Ea = (259412,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rao, V.S.", "Skinner, G.B."], title=u'Further experiments on pyrolysis of 2,2-dimethylpropane behind shock waves', journal="Int. J. Chem. Kinet.", volume="20", pages="""165""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000016.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:28 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 350,
    label = "r00009801",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (4.47e+16,"s^-1"),
        n = 0,
        Ea = (343388,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Mitchell, T.J.", "Benson, S.W."], title=u'Modelling of the homogeneously catalyzed and uncatalyzed pyrolysis of neopentane: thermochemistry of the neopentyl radical', journal="Int. J. Chem. Kinet.", volume="25", pages="""931-955""", year="1993", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000017.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:28 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 351,
    label = "r00009827",
    reactant1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    reactant2 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 O     0 {1,S} {6,S}
6     O     1 {5,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.09e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-2394.57,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dilger, H.", "Stolmar, M.", "Tregenna-Piggott, P.L.W.", "Roduner, E."], title=u'Gas phase addition kinetics of the tert-butyl radical to oxygen', journal="Ber. Bunsenges. Phys. Chem.", volume="101", pages="""956-960""", year="1997", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:28 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 352,
    label = "r00010093",
    reactant1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S} {6,D}
5     C     0 {3,D}
6     C     0 {4,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-21118.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Golden, D.M.", "Gac, N.A.", "Benson, S.W."], title=u'Equilibrium constant for allyl radical recombination. Direct measurement of "allyl resonance energy"', journal="J. Am. Chem. Soc.", pages="""2136""", year="1969", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 353,
    label = "r00010093",
    reactant1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S} {6,D}
5     C     0 {3,D}
6     C     0 {4,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1097.51,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tulloch, J.M.", "Macpherson, M.T.", "Morgan, C.A.", "Pilling, M.J."], title=u'Flash Photolysis Studies of Free-Radical Reactions: C_3H_5 + C_3H_5 (293-691 K) and C_3H_5 + NO (295-400 K)', journal="J. Phys. Chem.", volume="86", pages="""3812""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 354,
    label = "r00010093",
    reactant1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S} {6,D}
5     C     0 {3,D}
6     C     0 {4,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1097.51,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 355,
    label = "r00010093",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S} {6,D}
5     C     0 {3,D}
6     C     0 {4,D}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,D}
2  *  C     1 {1,S}
3     C     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+07,"s^-1"),
        n = 0,
        Ea = (131369,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ruzicka, D.J.", "Bryce, W.A."], title=u'The pyrolysis of diallyl (1,5-hexadiene)', journal="Can. J. Chem.", volume="38", pages="""827-834""", year="1960", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000013.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 356,
    label = "r00010093",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S} {6,D}
5     C     0 {3,D}
6     C     0 {4,D}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,D}
2  *  C     1 {1,S}
3     C     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.01e+13,"s^-1"),
        n = 0,
        Ea = (184581,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Homer, J.B.", "Lossing, F.P."], title=u'Free radicals by mass spectrometry. XXXV. The heat of formation of allyl radical from biallyl pyrolysis', journal="Can. J. Chem.", volume="44", pages="""2211-2217""", year="1966", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000014.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 357,
    label = "r00010093",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S} {6,D}
5     C     0 {3,D}
6     C     0 {4,D}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,D}
2  *  C     1 {1,S}
3     C     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+13,"s^-1"),
        n = 0,
        Ea = (234468,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Akers, R.J.", "Throssell, J.J."], title=u'Kinetic studies on allyl radicals. Part 1.-Toluene-carrier pyrolysis of 4-phenyl-but-l-ene and hexa-1, 5-diene and the heat of formation of the allyl radical', journal="Trans. Faraday Soc.", volume="63", pages="""124""", year="1967", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000015.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 358,
    label = "r00010093",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S} {6,D}
5     C     0 {3,D}
6     C     0 {4,D}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,D}
2  *  C     1 {1,S}
3     C     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.67e+15,"s^-1"),
        n = 0,
        Ea = (261074,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Golden, D.M.", "Gac, N.A.", "Benson, S.W."], title=u'Equilibrium constant for allyl radical recombination. Direct measurement of "allyl resonance energy"', journal="J. Am. Chem. Soc.", pages="""2136""", year="1969", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000016.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 359,
    label = "r00010093",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S} {6,D}
5     C     0 {3,D}
6     C     0 {4,D}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,D}
2  *  C     1 {1,S}
3     C     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.07e+12,"s^-1"),
        n = 0,
        Ea = (213682,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Doering, W.v.E.", "Toscano, V.G.", "Beasley, G.H."], title=u'Kinetics of the Cope Rearrangement of 1,1-Dideuteriohexa-1,5-Diene', journal="Tetrahedron", volume="27", pages="""5299""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000017.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 360,
    label = "r00010093",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S} {6,D}
5     C     0 {3,D}
6     C     0 {4,D}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,D}
2  *  C     1 {1,S}
3     C     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+13,"s^-1"),
        n = 0,
        Ea = (101437,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Throssell, J.J."], title=u'Rates of reaction of allyl radicals: A reassessment', journal="Int. J. Chem. Kinet.", volume="4", pages="""273""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000018.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 361,
    label = "r00010093",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S} {6,D}
5     C     0 {3,D}
6     C     0 {4,D}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,D}
2  *  C     1 {1,S}
3     C     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+12,"s^-1"),
        n = 0,
        Ea = (230311,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Sakai, T.", "Nohara, D.", "Kunugi, T.", "Nohara, D."], title=u'A Kinetic Study on the Formation of Aromatics During Pyrolysis of Petroleum Hydrocarbons', journal="Am. Chem. Soc. Symp. Ser.", volume="22", pages="""152""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000019.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 362,
    label = "r00010093",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S} {6,D}
5     C     0 {3,D}
6     C     0 {4,D}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,D}
2  *  C     1 {1,S}
3     C     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+15,"s^-1"),
        n = 0,
        Ea = (237794,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000020.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 363,
    label = "r00010093",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S} {6,D}
5     C     0 {3,D}
6     C     0 {4,D}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,D}
2  *  C     1 {1,S}
3     C     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.17e+14,"s^-1"),
        n = 0,
        Ea = (241120,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Roth, W.R.", "Bauer, F.", "Beitat, A.", "Ebbrecht, T.", "Wustefeld, M."], title=u'Die bildungsenthalpie des allyl- und methallyl-radikals', journal="Chem. Ber.", volume="124", pages="""1453-1460""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000021.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 364,
    label = "r00010096",
    reactant1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S}
2  *1 C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S} {6,D}
6     C     0 {5,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.14578e+14,"cm^3/(mol*s)"),
        n = -0.35,
        Ea = (-548.755,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 365,
    label = "r00010096",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S} {6,D}
6     C     0 {5,D}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5e+09,"s^-1"),
        n = 0,
        Ea = (184581,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Taniewski, M."], title=u'Kinetics and mechanism of the thermal decomposition of 4-methylpent-1-ene', journal="J. Chem. Soc.", pages="""7436""", year="1965", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 366,
    label = "r00010107",
    reactant1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *  C     1 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *1 C     0 {1,S} {5,S}
4     C     0 {2,S}
5     C     0 {3,S} {6,D}
6     C     0 {5,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.05e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-548.755,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 367,
    label = "r00010107",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {5,S}
4     C     0 {2,S}
5     C     0 {3,S} {6,D}
6     C     0 {5,D}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+15,"s^-1"),
        n = 0,
        Ea = (295995,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal Stability of Cyclohexane and 1-Hexene', journal="Int. J. Chem. Kinet.", volume="10", pages="""1119""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 368,
    label = "r00010107",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {5,S}
4     C     0 {2,S}
5     C     0 {3,S} {6,D}
6     C     0 {5,D}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+15,"s^-1"),
        n = 0,
        Ea = (295995,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["King, K.D."], title=u'Very Low-Pressure Pyrolysis (VLPP) of Hex-1-ene. Kinetics of the Retro-ene Decomposition of a Mono-Olefin', journal="Int. J. Chem. Kinet.", volume="11", pages="""1071""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 369,
    label = "r00010111",
    reactant1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S} {4,D}
4     C     0 {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.0153e+14,"cm^3/(mol*s)"),
        n = -0.32,
        Ea = (-548.755,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 370,
    label = "r00010111",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S} {4,D}
4     C     0 {3,D}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.5e+13,"s^-1"),
        n = 0,
        Ea = (263569,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Sehon, A.H.", "Szwarc, M."], title=u'The CH_2:CH_2-CH_3 bond dissociation energy and the heat of formation of the allyl radical', journal="Proc. R. Soc. London A", volume="202", pages="""263-276""", year="1950", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 371,
    label = "r00010111",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S} {4,D}
4     C     0 {3,D}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.13e+12,"s^-1"),
        n = 0,
        Ea = (246940,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kerr, J.A.", "Spencer, R.", "Trotman-Dickenson, A.F."], title=u'The pyrolysis of but-1-ene, and the resonance energy of the allyl radical', journal="J. Chem. Soc.", pages="""6652-6654""", year="1965", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 372,
    label = "r00010111",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S} {4,D}
4     C     0 {3,D}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+13,"s^-1"),
        n = 0,
        Ea = (291007,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Halstead, M.P.", "Quinn, C.P."], title=u'Pyrolysis of ethylene', journal="Trans. Faraday Soc.", volume="64", pages="""103""", year="1968", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 373,
    label = "r00010111",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S} {4,D}
4     C     0 {3,D}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+15,"s^-1"),
        n = 0,
        Ea = (299321,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Trenwith, A.B."], title=u'Dissociation of 1-butene, 3-methyl-1-butene, and of 3,3-dimethyl-1-butene and the resonance energy of the allyl, methyl allyl and dimethyl allyl radicals', journal="Trans. Faraday Soc.", volume="66", pages="""2805-2811""", year="1970", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 374,
    label = "r00010111",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S} {4,D}
4     C     0 {3,D}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+16,"s^-1"),
        n = 0,
        Ea = (305141,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:32 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 375,
    label = "r00010126",
    reactant1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *  C     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *  C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S} {4,S} {5,S}
2  *2 C     0 {1,S} {3,S}
3  *1 C     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {3,S} {7,D}
7     C     0 {6,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.05e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-548.755,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:32 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 376,
    label = "r00010169",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    reactant2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S} {5,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.43e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1338.63,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Arrowsmith, P.", "Kirsch, L.J."], title=u'Mutual Reaction of Isopropyl Radicals', journal="J. Chem. Soc. Faraday Trans. 1", volume="74", pages="""3016""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 377,
    label = "r00010169",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S} {5,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+16,"s^-1"),
        n = 0,
        Ea = (317613,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal decomposition of 2,3-dimethylbutane in a single-pulse shock tube', journal="J. Chem. Phys.", volume="43", pages="""352-359""", year="1965", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000016.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 378,
    label = "r00010169",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S} {5,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+16,"s^-1"),
        n = 0,
        Ea = (311793,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Golden, D.M.", "Alfassi, Z.B.", "Beadle, P.C."], title=u"Very Low-Pressure Pyrolysis (VLPP) of Alkanes: n-Butane, 2,3-Dimethylbutane, 2,2',3,3'-Tetramethylbutane, and Isobutane", journal="Int. J. Chem. Kinet.", volume="6", pages="""359""", year="1974", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000017.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 379,
    label = "r00010169",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S} {5,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.58e+16,"s^-1"),
        n = 0,
        Ea = (316781,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Evidence for Strongly Temperature-Dependent A Factors in Alkane Decomposition and High Heats of Formation for Alkyl Radicals', journal="Int. J. Chem. Kinet.", volume="10", pages="""821""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000018.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 380,
    label = "r00010169",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S} {5,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.82e+17,"s^-1"),
        n = 0,
        Ea = (339230,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Evidence for Strongly Temperature-Dependent A Factors in Alkane Decomposition and High Heats of Formation for Alkyl Radicals', journal="Int. J. Chem. Kinet.", volume="10", pages="""821""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000019.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 381,
    label = "r00010169",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S} {5,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.98e+20,"s^-1"),
        n = -4.1,
        Ea = (354197,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Forst, W."], title=u'Temperature-dependent A factor in thermal unimolecular reactions', journal="J. Phys. Chem.", volume="83", pages="""100-108""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000020.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 382,
    label = "r00010169",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S} {5,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+15,"s^-1"),
        n = 0,
        Ea = (305141,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, R.R.", "Drewery, G.R.", "Walker, R.W."], title=u'Decomposition of 2,3-dimethylbutane in the presence of oxygen. Part 1.-Thermochemistry of the reaction (CH_3)_2CHCH(CH_3)_2 \u2192 2i-C_3H_7', journal="J. Chem. Soc. Faraday Trans. 1", volume="80", pages="""2827""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000021.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 383,
    label = "r00010169",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S} {5,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.63e+16,"s^-1"),
        n = 0,
        Ea = (319276,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, R.R.", "Drewery, G.R.", "Walker, R.W."], title=u'Decomposition of 2,3-dimethylbutane in the presence of oxygen. Part 1.-Thermochemistry of the reaction (CH_3)_2CHCH(CH_3)_2 \u2192 2i-C_3H_7', journal="J. Chem. Soc. Faraday Trans. 1", volume="80", pages="""2827""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000022.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 384,
    label = "r00010181",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    reactant2 = 
"""
1  *  C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *2 C     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (2502.66,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Konar, R.S.", "Marshall, R.M.", "Purnell, J.H."], title=u'Initiation of isobutane pyrolysis', journal="Trans. Faraday Soc.", volume="64", pages="""405-413""", year="1968", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 385,
    label = "r00010181",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (7.94e+18,"s^-1"),
        n = 0,
        Ea = (335073,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Brooks, C.T."], title=u'Gas-phase high-pressure decomposition of isobutane in the presence of hydrogen', journal="Trans. Faraday Soc.", volume="62", pages="""935-944""", year="1966", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 386,
    label = "r00010181",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (6.31e+07,"s^-1"),
        n = 0,
        Ea = (345051,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Konar, R.S.", "Marshall, R.M.", "Purnell, J.H."], title=u'Initiation of isobutane pyrolysis', journal="Trans. Faraday Soc.", volume="64", pages="""405-413""", year="1968", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 387,
    label = "r00010181",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (6.31e+16,"s^-1"),
        n = 0,
        Ea = (341725,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Konar, R.S.", "Marshall, R.M.", "Purnell, J.H."], title=u'The Self-Inhibited Pyrolysis of Isobutane', journal="Int. J. Chem. Kinet.", volume="5", pages="""1007""", year="1973", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 388,
    label = "r00010181",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (8.71e+09,"s^-1"),
        n = 0,
        Ea = (202042,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bradley, J.N."], title=u'A general mechanism for the high-temperature pyrolysis of alkanes. The pyrolysis of isobutane', journal="Proc. R. Soc. London A", volume="337", pages="""199""", year="1974", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 389,
    label = "r00010181",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.51e+16,"s^-1"),
        n = 0,
        Ea = (346713,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Golden, D.M.", "Alfassi, Z.B.", "Beadle, P.C."], title=u"Very Low-Pressure Pyrolysis (VLPP) of Alkanes: n-Butane, 2,3-Dimethylbutane, 2,2',3,3'-Tetramethylbutane, and Isobutane", journal="Int. J. Chem. Kinet.", volume="6", pages="""359""", year="1974", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 390,
    label = "r00010181",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (8.39e+15,"s^-1"),
        n = 0,
        Ea = (357522,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Pratt, G.L.", "Rogers, D."], title=u'Wall-less Reactor Studies. Part 4. - Isobutane Pyrolysis', journal="J. Chem. Soc. Faraday Trans. 1", volume="76", pages="""1694""", year="1980", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 391,
    label = "r00010181",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1.66e+11,"s^-1"),
        n = 0,
        Ea = (202042,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Shevel'kova, L.V.", "Ivanvuk, A.V.", "Nametkin, N.S."], title=u'Comparative Study of the Pyrolysis of n-Butane and Isobutane', journal="Neftekhimiya", volume="20", pages="""837""", year="1980", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 392,
    label = "r00010181",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (6.31e+12,"s^-1"),
        n = 0,
        Ea = (254423,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Koike, T.", "Morinaga, K."], title=u'UV Absorption Studies of the Pyrolysis of Isobutane in Shock Waves', journal="Bull. Chem. Soc. Jpn.", volume="55", pages="""690""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000013.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 393,
    label = "r00010181",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (4e+16,"s^-1"),
        n = 0,
        Ea = (346713,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000014.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 394,
    label = "r00010181",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (4.5e+16,"s^-1"),
        n = 0,
        Ea = (339230,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hidaka, Y.", "Fujiwara, M.", "Oki, T.", "Kawano, H."], title=u'Thermal decomposition of isobutane in shock waves. Rate constant of initiation reaction', journal="Chem. Phys. Lett.", volume="144", pages="""570""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000015.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 395,
    label = "r00010181",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (3.84e+19,"s^-1"),
        n = -2.61,
        Ea = (378308,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Rate constants for the decomposition and formation of simple alkanes over extended temperature and pressure ranges', journal="Combust. Flame", volume="78", pages="""71-86""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000016.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 396,
    label = "r00010181",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (3.84e+19,"s^-1"),
        n = -2.61,
        Ea = (378308,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part 4. Isobutane', journal="J. Phys. Chem. Ref. Data", volume="19", pages="""1-68""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000017.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 397,
    label = "r00010210",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    reactant2 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *2 O     0 {1,S} {5,S}
5     O     1 {4,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.05485e+21,"cm^3/(mol*s)"),
        n = -11.1,
        Ea = (27354.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["DeSain, J.D.", "Klippenstein, S.J.", "Miller, J.A.", "Taatjes, C.A."], title=u'Measurements, Theory, and Modeling of OH Formation in Ethyl + O_2 and Propyl + O_2 Reactions', journal="J. Phys. Chem. A", volume="107", pages="""4415-4427""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 398,
    label = "r00010242",
    reactant1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.59e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11390.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Shepp, A.", "Kutschke, K.O."], title=u'Rate of recombination of radicals. III. Rate of recombination of ethyl radicals', journal="J. Chem. Phys.", volume="26", pages="""1020-1028""", year="1957", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 399,
    label = "r00010242",
    reactant1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.59e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (798.189,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Teng, L.", "Jones, W.E."], title=u'Kinetics of the Reactions of Hydrogen Atoms with Ethylene and Vinyl Fluoride', journal="J. Chem. Soc. Faraday Trans. 1", volume="68", pages="""1267""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 400,
    label = "r00010242",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.77e+18,"s^-1"),
        n = 0,
        Ea = (360848,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Purnell, J.H.", "Quinn, C.P."], title=u'The pyrolysis of n-butane', journal="Proc. R. Soc. London A", volume="270", pages="""267""", year="1962", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000029.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 401,
    label = "r00010242",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.2e+17,"s^-1"),
        n = 0,
        Ea = (335073,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lin, M.C.", "Back, M.H."], title=u'The thermal decomposition of ethane. Part III. Secondary reactions', journal="Can. J. Chem.", volume="44", pages="""2369""", year="1966", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000030.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 402,
    label = "r00010242",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+16,"s^-1"),
        n = 0,
        Ea = (338399,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Golden, D.M.", "Alfassi, Z.B.", "Beadle, P.C."], title=u"Very Low-Pressure Pyrolysis (VLPP) of Alkanes: n-Butane, 2,3-Dimethylbutane, 2,2',3,3'-Tetramethylbutane, and Isobutane", journal="Int. J. Chem. Kinet.", volume="6", pages="""359""", year="1974", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000031.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 403,
    label = "r00010242",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+15,"s^-1"),
        n = 0,
        Ea = (322602,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hughes, D.G.", "Marshall, R.M.", "Purnell, J.H."], title=u'Rate Constants for the Initiation of n-Butane Pyrolysis and for the Recombination of Ethyl Radicals', journal="J. Chem. Soc. Faraday Trans. 1", volume="70", pages="""594""", year="1974", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000032.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 404,
    label = "r00010242",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+16,"s^-1"),
        n = 0,
        Ea = (343388,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Evidence for Strongly Temperature-Dependent A Factors in Alkane Decomposition and High Heats of Formation for Alkyl Radicals', journal="Int. J. Chem. Kinet.", volume="10", pages="""821""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000033.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 405,
    label = "r00010242",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.58e+17,"s^-1"),
        n = 0,
        Ea = (364174,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Evidence for Strongly Temperature-Dependent A Factors in Alkane Decomposition and High Heats of Formation for Alkyl Radicals', journal="Int. J. Chem. Kinet.", volume="10", pages="""821""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000034.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 406,
    label = "r00010242",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.41e+18,"s^-1"),
        n = -2.17,
        Ea = (365005,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Forst, W."], title=u'Temperature-dependent A factor in thermal unimolecular reactions', journal="J. Phys. Chem.", volume="83", pages="""100-108""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000035.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 407,
    label = "r00010242",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+16,"s^-1"),
        n = 0,
        Ea = (340062,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000037.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 408,
    label = "r00010242",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+16,"s^-1"),
        n = 0,
        Ea = (335905,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000038.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 409,
    label = "r00010358",
    reactant1 = 
"""
1     C     0 {2,B} {3,B} {7,S}
2     C     0 {1,B} {5,B}
3     C     0 {1,B} {6,B}
4     C     0 {5,B} {6,B}
5     C     0 {2,B} {4,B}
6     C     0 {3,B} {4,B}
7  *1 O     0 {1,S} {8,S}
8  *2 H     0 {7,S}
""",
    product1 = 
"""
1  *  H     1
""",
    product2 = 
"""
1     C     0 {2,B} {3,B} {7,S}
2     C     0 {1,B} {5,B}
3     C     0 {1,B} {6,B}
4     C     0 {5,B} {6,B}
5     C     0 {2,B} {4,B}
6     C     0 {3,B} {4,B}
7  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.67e+16,"s^-1"),
        n = 0,
        Ea = (371657,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lovell, A.B.", "Brezinsky, K.", "Glassman, I."], title=u'The gas phase pyrolysis of phenol', journal="Int. J. Chem. Kinet.", volume="21", pages="""547""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 410,
    label = "r00010419",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {6,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S} {5,D}
4     C     0 {2,D} {5,S}
5     C     0 {3,D} {4,S}
6  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,D}
4  *  C     1 {2,S} {5,S}
5     C     0 {3,D} {4,S}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5e+15,"s^-1"),
        n = 0,
        Ea = (329253,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Burcat, A.", "Dvinyaninov, M."], title=u'Detailed kinetics of cyclopentadiene decomposition studied in a shock tube', journal="Int. J. Chem. Kinet.", volume="29", pages="""505-514""", year="1997", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 411,
    label = "r00010419",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {6,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S} {5,D}
4     C     0 {2,D} {5,S}
5     C     0 {3,D} {4,S}
6  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,D}
4  *  C     1 {2,S} {5,S}
5     C     0 {3,D} {4,S}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.7e+14,"s^-1"),
        n = 0,
        Ea = (-312042,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Roy, K.", "Braun-Unkhoff, M.", "Frank, P.", "Just, Th."], title=u'Erratum: "Kinetics of the Cyclopentadiene Decay and the Recombination of Cyclopentadienyl Radicals with H-Atoms:  Enthalpy of Formation of the Cyclopentadienyl Radical:, Int. J. Chem. Kinet 2001, 33, 821', journal="Int J. Chem. Kinet.", volume="34", pages="""209-209""", year="2002", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 412,
    label = "r00010516",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *2 C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.77e+18,"s^-1"),
        n = 0,
        Ea = (360848,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Purnell, J.H.", "Quinn, C.P."], title=u'The pyrolysis of n-butane', journal="Proc. R. Soc. London A", volume="270", pages="""267""", year="1962", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 413,
    label = "r00010516",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *2 C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (8.89e+13,"s^-1"),
        n = 0,
        Ea = (300984,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Koike, T.", "Morinaga, K."], title=u'UV Absorption Studies of the Pyrolysis of Butane in Shock Waves', journal="Bull. Chem. Soc. Jpn.", volume="54", pages="""2439""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 414,
    label = "r00010516",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *2 C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2e+16,"s^-1"),
        n = 0,
        Ea = (340062,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 415,
    label = "r00010516",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *2 C     0 {1,S}
4     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *  C     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1e+17,"s^-1"),
        n = 0,
        Ea = (354197,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 416,
    label = "r00010545",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *  C     1 {1,S}
""",
    reactant2 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *2 O     0 {2,S} {5,S}
5     O     1 {4,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (8.00072e+12,"cm^3/(mol*s)"),
        n = -8.23,
        Ea = (21617.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["DeSain, J.D.", "Klippenstein, S.J.", "Miller, J.A.", "Taatjes, C.A."], title=u'Measurements, Theory, and Modeling of OH Formation in Ethyl + O_2 and Propyl + O_2 Reactions', journal="J. Phys. Chem. A", volume="107", pages="""4415-4427""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 417,
    label = "r00010569",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {4,S}
3  *1 O     0 {1,S} {4,S}
4  *2 O     0 {2,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.1e+15,"s^-1"),
        n = 0,
        Ea = (154649,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Takezaki, Y.", "Takeuchi, C."], title=u'Decomposition of methanol induced by methoxy radicals', journal="J. Chem. Phys.", volume="22", pages="""1527""", year="1954", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 418,
    label = "r00010569",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {4,S}
3  *1 O     0 {1,S} {4,S}
4  *2 O     0 {2,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.6e+15,"s^-1"),
        n = 0,
        Ea = (147998,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hanst, P.L.", "Calvert, J.G."], title=u'The thermal decomposition of dimethyl peroxide: the oxygen-oxygen bond strength of dialkyl peroxides', journal="J. Phys. Chem.", volume="63", pages="""104-106""", year="1959", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 419,
    label = "r00010569",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {4,S}
3  *1 O     0 {1,S} {4,S}
4  *2 O     0 {2,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+15,"s^-1"),
        n = 0,
        Ea = (154649,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L.", "McCulloch, R.D."], title=u'Pyrolysis of Dimethyl Peroxide', journal="Int. J. Chem. Kinet.", volume="8", pages="""491""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 420,
    label = "r00010569",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {4,S}
3  *1 O     0 {1,S} {4,S}
4  *2 O     0 {2,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+15,"s^-1"),
        n = 0,
        Ea = (155481,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Barker, J.R.", "Benson, S.W.", "Golden, D.M."], title=u'The Decomposition of Dimethyl Peroxide and the Rate Constant for CH_3O + O_2 \u2192 CH_2O +HO_2', journal="Int. J. Chem. Kinet.", volume="9", pages="""31""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 421,
    label = "r00010569",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {4,S}
3  *1 O     0 {1,S} {4,S}
4  *2 O     0 {2,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+16,"s^-1"),
        n = 0,
        Ea = (161301,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L.", "Rattray, G.N."], title=u'The Reaction of Methoxy Radicals with Nitric Oxide and Nitrogen Dioxide', journal="Int. J. Chem. Kinet.", volume="11", pages="""1183""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 422,
    label = "r00010572",
    reactant1 = 
"""
1  *1 C     0 {3,S}
2     C     0 {3,S}
3  *2 O     0 {1,S} {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.1e+16,"s^-1"),
        n = 0,
        Ea = (339230,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Benson, S.W."], title=u'Pyrolysis of dimethyl ether', journal="J. Chem. Phys.", volume="25", pages="""27-31""", year="1956", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 423,
    label = "r00010572",
    reactant1 = 
"""
1  *1 C     0 {3,S}
2     C     0 {3,S}
3  *2 O     0 {1,S} {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.26e+18,"s^-1"),
        n = 0,
        Ea = (339230,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Benson, S.W.", "Jain, D.V.S."], title=u'Further studies of the pyrolysis of dimethyl ether', journal="J. Chem. Phys.", volume="31", pages="""1008""", year="1959", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 424,
    label = "r00010572",
    reactant1 = 
"""
1  *1 C     0 {3,S}
2     C     0 {3,S}
3  *2 O     0 {1,S} {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (317613,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Pacey, P.D."], title=u'The Initial Stages of the Pyrolysis of Dimethyl Ether', journal="Can. J. Chem.", volume="53", pages="""2742""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 425,
    label = "r00010572",
    reactant1 = 
"""
1  *1 C     0 {3,S}
2     C     0 {3,S}
3  *2 O     0 {1,S} {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.16e+15,"s^-1"),
        n = 0,
        Ea = (320107,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Aronowitz, D.", "Naegeli, D."], title=u'High-Temperature Pyrolysis of Dimethyl Ether', journal="Int. J. Chem. Kinet.", volume="9", pages="""471""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 426,
    label = "r00010572",
    reactant1 = 
"""
1  *1 C     0 {3,S}
2     C     0 {3,S}
3  *2 O     0 {1,S} {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.16e+16,"s^-1"),
        n = 0,
        Ea = (347545,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L.", "Alvarado-Salinas, G.", "Reid, I.A.B.", "Robinson, C.", "Smith, D.B."], title=u'The Pyrolysis of Dimethyl Ether and Formaldehyde', journal="Symp. Int. Combust. Proc.", volume="19", pages="""81""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 427,
    label = "r00010729",
    reactant1 = 
"""
1     C     0 {2,S} {4,S} {5,S}
2  *1 C     0 {1,S} {3,S}
3  *2 C     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {3,S} {7,T}
7     C     0 {6,T}
""",
    product1 = 
"""
1  *  C     1 {2,S}
2     C     0 {1,S} {3,T}
3     C     0 {2,T}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+16,"s^-1"),
        n = 0,
        Ea = (305141,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal Stability of Intermediate Sized Acetylenic Compounds and the Heats of Formation of Propargyl Radicals', journal="Int. J. Chem. Kinet.", volume="10", pages="""687""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:40 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 428,
    label = "r00010761",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6  *  C     1 {4,B} {5,B}
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S} {3,B} {4,B}
3     C     0 {2,B} {6,B}
4     C     0 {2,B} {7,B}
5     C     0 {6,B} {7,B}
6     C     0 {3,B} {5,B}
7     C     0 {4,B} {5,B}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.38e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (191.233,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tokmakov, I.V.", "Park, J.", "Gheyas, S.", "Lin, M.C."], title=u'Experimental and theoretical studies of the reaction of the phenyl radical with methane', journal="J. Phys. Chem. A", volume="103", pages="""3636-3645""", year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:40 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 429,
    label = "r00010761",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6  *  C     1 {4,B} {5,B}
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S} {3,B} {4,B}
3     C     0 {2,B} {6,B}
4     C     0 {2,B} {7,B}
5     C     0 {6,B} {7,B}
6     C     0 {3,B} {5,B}
7     C     0 {4,B} {5,B}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.39e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (124.717,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Park, J.", "Gheyas, S.I.", "Lin, M.C."], title=u'Kinetics of C_6H_5 Radical Reactions with 2-Methylpropane, 2,3-Dimethylbutane and 2,3,4-Trimethylpentane', journal="Int J. Chem. Kinet.", volume="31", pages="""645-653""", year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:40 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 430,
    label = "r00010761",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S} {3,B} {4,B}
3     C     0 {2,B} {6,B}
4     C     0 {2,B} {7,B}
5     C     0 {6,B} {7,B}
6     C     0 {3,B} {5,B}
7     C     0 {4,B} {5,B}
""",
    product1 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6  *  C     1 {4,B} {5,B}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.91e+12,"s^-1"),
        n = 0,
        Ea = (303478,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Pamidimukkala, K.M.", "Kern, R.D.", "Patel, M.R.", "Wei, H.C.", "Kiefer, J.H."], title=u'High-temperature pyrolysis of toluene', journal="J. Phys. Chem.", volume="91", pages="""2148""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:40 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 431,
    label = "r00010765",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4  *2 C     0 {2,S}
5     C     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *  C     1 {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.16e+16,"s^-1"),
        n = 0,
        Ea = (330916,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Blackmore, D.R.", "Hinshelwood, C."], title=u'Derivation of rate constants for steps in the free-radical chain decomposition of paraffins', journal="Proc. R. Soc. London A", volume="268", pages="""36""", year="1962", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:40 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 432,
    label = "r00010768",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     O     0 {1,S}
""",
    product1 = 
"""
1  *  C     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+16,"s^-1"),
        n = 0,
        Ea = (353365,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal Stability of Alcohols', journal="Int. J. Chem. Kinet.", volume="8", pages="""173""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:40 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 433,
    label = "r00010768",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     O     0 {1,S}
""",
    product1 = 
"""
1  *  C     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.14e+19,"s^-1"),
        n = -1.68,
        Ea = (381634,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Marinov, N.M."], title=u'A detailed chemical kinetic model for high temperature ethanol oxidation', journal="Int. J. Chem. Kinet.", volume="31", pages="""183-220""", year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:40 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 434,
    label = "r00010771",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
1  *  C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+15,"s^-1"),
        n = 0,
        Ea = (309298,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Liu, M.T.H.", "Laidler, K.J."], title=u'Elementary processes in the acetaldehyde pyrolysis', journal="Can. J. Chem.", volume="46", pages="""479""", year="1968", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:40 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 435,
    label = "r00010771",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
1  *  C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.88e+16,"s^-1"),
        n = 0,
        Ea = (333410,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bardi, I.", "Marta, F."], title=u'Investigation of the Thermal Decomposition of Acetaldehyde', journal="Acta Phys. Chem.", volume="19", pages="""227""", year="1973", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:40 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 436,
    label = "r00010771",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
1  *  C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.87e+16,"s^-1"),
        n = 0,
        Ea = (340893,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bardi, I.", "Marta, F."], title=u'Investigation of the Thermal Decomposition of Acetaldehyde', journal="Acta Phys. Chem.", volume="19", pages="""227""", year="1973", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:40 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 437,
    label = "r00010771",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
1  *  C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.08e+15,"s^-1"),
        n = 0,
        Ea = (342556,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Colket, M.B., III", "Naegeli, D.W.", "Glassman, I."], title=u'High-Temperature Pyrolysis of Acetaldehyde', journal="Int. J. Chem. Kinet.", volume="7", pages="""223""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:40 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 438,
    label = "r00010771",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
1  *  C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.2e+16,"s^-1"),
        n = 0,
        Ea = (341725,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ernst, J.", "Spindler, K."], title=u'Untersuchungen zum Thermischen Zerfall von Acetaldehyd und Aceton', journal="Ber. Bunsenges. Phys. Chem.", volume="79", pages="""1163""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000013.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:40 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 439,
    label = "r00010771",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
1  *  C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.2e+16,"s^-1"),
        n = 0,
        Ea = (341725,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ernst, J.", "Spindler, K.", "Wagner, H.Gg."], title=u'Untersuchungen zum Thermischen Zerfall von Acetaldehyd und Aceton', journal="Ber. Bunsenges. Phys. Chem.", volume="80", pages="""645""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000014.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:40 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 440,
    label = "r00010771",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
1  *  C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+15,"s^-1"),
        n = 0,
        Ea = (330916,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000015.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:40 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 441,
    label = "r00010771",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
1  *  C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7e+15,"s^-1"),
        n = 0,
        Ea = (341725,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."], title=u'Evaluated kinetic data for combustion modelling', journal="J. Phys. Chem. Ref. Data", volume="21", pages="""411-429""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000016.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:40 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 442,
    label = "r00010777",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3     C     0 {2,D}
""",
    product1 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+17,"s^-1"),
        n = 0,
        Ea = (393275,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Marshall, R.M.", "Purnell, J.H.", "Shurlock, B.C."], title=u'The initiation of propylene pyrolysis', journal="Can. J. Chem.", volume="44", pages="""2778-2780""", year="1966", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 443,
    label = "r00010777",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3     C     0 {2,D}
""",
    product1 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.17e+16,"s^-1"),
        n = 0,
        Ea = (359185,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Chappell, G.A.", "Shaw, H."], title=u'A shock tube study of the pyrolysis of propylene. Kinetics of the vinyl-methyl bond rupture', journal="J. Phys. Chem.", volume="72", pages="""4672-4675""", year="1968", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 444,
    label = "r00010777",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3     C     0 {2,D}
""",
    product1 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+13,"s^-1"),
        n = 0,
        Ea = (309298,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Burcat, A."], title=u'Cracking of Propylene in a Shock Tube', journal="Fuel", volume="54", pages="""87""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 445,
    label = "r00010777",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3     C     0 {2,D}
""",
    product1 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+16,"s^-1"),
        n = 0,
        Ea = (416555,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 446,
    label = "r00010777",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3     C     0 {2,D}
""",
    product1 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.51e+17,"s^-1"),
        n = 0,
        Ea = (384960,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Naroznik, M.", "Niedzielski, J."], title=u'Propylene photolysis at 6.7 eV: Calculation of the quantum yields for the secondary processes', journal="J. Photochem.", volume="32", pages="""281""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 447,
    label = "r00010777",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3     C     0 {2,D}
""",
    product1 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.18e+18,"s^-1"),
        n = -1.2,
        Ea = (409072,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 448,
    label = "r00010777",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3     C     0 {2,D}
""",
    product1 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8e+14,"s^-1"),
        n = 0,
        Ea = (368331,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hidaka, Y.", "Nakamura, T.", "Tanaka, H.", "Jinno, A.", "Kawano, H."], title=u'Shock tube and modeling study of propene pyrolysis', journal="Int. J. Chem. Kinet.", volume="24", pages="""761-780""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 449,
    label = "r00010783",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S} {4,T}
4     C     0 {3,T}
""",
    product1 = 
"""
1  *  C     1 {2,S}
2     C     0 {1,S} {3,T}
3     C     0 {2,T}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+15,"s^-1"),
        n = 0,
        Ea = (310130,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["King, K.D."], title=u'Very Low-Pressure Pyrolysis (VLPP) of But-1-yne. The Heat of Formation and Stabilization Energy of the Propargyl Radical', journal="Int. J. Chem. Kinet.", volume="10", pages="""545""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 450,
    label = "r00010783",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S} {4,T}
4     C     0 {3,T}
""",
    product1 = 
"""
1  *  C     1 {2,S}
2     C     0 {1,S} {3,T}
3     C     0 {2,T}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.58e+17,"s^-1"),
        n = 0,
        Ea = (312624,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Trenwith, A.B.", "Wrigley, S.P."], title=u'Pyrolysis of But-1-yne and the Resonance Energy of the Propargyl and 3-Methylpropargyl Radicals', journal="J. Chem. Soc. Faraday Trans. 1", volume="78", pages="""2337""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 451,
    label = "r00010783",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S} {4,T}
4     C     0 {3,T}
""",
    product1 = 
"""
1  *  C     1 {2,S}
2     C     0 {1,S} {3,T}
3     C     0 {2,T}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+15,"s^-1"),
        n = 0,
        Ea = (316781,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 452,
    label = "r00010783",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S} {4,T}
4     C     0 {3,T}
""",
    product1 = 
"""
1  *  C     1 {2,S}
2     C     0 {1,S} {3,T}
3     C     0 {2,T}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3e+15,"s^-1"),
        n = 0,
        Ea = (320939,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hidaka, Y.", "Higashihara, T.", "Ninomiya, N.", "Oshita, H.", "Kawano, H."], title=u'Thermal isomerization and decomposition of 2-butyne in shock waves', journal="J. Phys. Chem.", volume="97", pages="""10977-10983""", year="1993", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 453,
    label = "r00010783",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S}
3     C     0 {1,S} {4,T}
4     C     0 {3,T}
""",
    product1 = 
"""
1  *  C     1 {2,S}
2     C     0 {1,S} {3,T}
3     C     0 {2,T}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3e+15,"s^-1"),
        n = 0,
        Ea = (316781,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hidaka, Y.", "Higashihara, T.", "Oki, T.", "Kawano, H."], title=u'Thermal decomposition of 1-butyne in shock waves', journal="Int. J. Chem. Kinet.", volume="27", pages="""321-330""", year="1995", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 454,
    label = "r00010784",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S} {4,D}
3     C     0 {4,D}
4     C     0 {2,D} {3,D}
""",
    product1 = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3  *  C     1 {2,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+12,"s^-1"),
        n = 0,
        Ea = (248603,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kern, R.D.", "Singh, H.J.", "Wu, C.H."], title=u'Thermal decomposition of 1,2 butadiene', journal="Int. J. Chem. Kinet.", volume="20", pages="""731""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 455,
    label = "r00010784",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S} {4,D}
3     C     0 {4,D}
4     C     0 {2,D} {3,D}
""",
    product1 = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3  *  C     1 {2,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+15,"s^-1"),
        n = 0,
        Ea = (313456,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hidaka, Y.", "Higashihara, T.", "Ninomiya, N.", "Oshita, H.", "Kawano, H."], title=u'Thermal isomerization and decomposition of 2-butyne in shock waves', journal="J. Phys. Chem.", volume="97", pages="""10977-10983""", year="1993", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 456,
    label = "r00010784",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 C     0 {1,S} {4,D}
3     C     0 {4,D}
4     C     0 {2,D} {3,D}
""",
    product1 = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3  *  C     1 {2,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+15,"s^-1"),
        n = 0,
        Ea = (313456,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hidaka, Y.", "Higashihara, T.", "Ninomiya, N.", "Oki, T.", "Kawano, H."], title=u'Thermal isomerization and decomposition of 1,2-butadiene in shock waves', journal="Int. J. Chem. Kinet.", volume="27", pages="""331-341""", year="1995", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 457,
    label = "r00010787",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {7,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S} {6,S}
4     C     0 {5,S} {6,S}
5     C     0 {2,S} {4,S}
6     C     0 {3,S} {4,S}
7  *2 C     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S} {6,S}
5     C     0 {3,S} {6,S}
6  *  C     1 {4,S} {5,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+16,"s^-1"),
        n = 0,
        Ea = (368331,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Brown, T.C.", "King, K.D."], title=u'Very low-pressure pyrolysis (VLPP) of methyl- and ethynyl- cyclopentanes and cyclohexanes', journal="Int. J. Chem. Kinet.", volume="21", pages="""251""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 458,
    label = "r00010789",
    reactant1 = 
"""
1  *1 C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4     O     0 {3,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,D}
3     O     0 {2,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.4e+14,"s^-1"),
        n = 0,
        Ea = (300984,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Szwarc, M.", "Taylor, J.W."], title=u'Pyrolysis of acetone and the heat of formation of acetyl radicals', journal="J. Chem. Phys.", volume="23", pages="""2310-2314""", year="1955", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 459,
    label = "r00010789",
    reactant1 = 
"""
1  *1 C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4     O     0 {3,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,D}
3     O     0 {2,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.4e+14,"s^-1"),
        n = 0,
        Ea = (296827,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Clark, D.", "Pritchard, H.O."], title=u'Arrhenius parameters of some reactions involving multiplicity changes', journal="J. Chem. Soc. London", pages="""2136-2140""", year="1956", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 460,
    label = "r00010789",
    reactant1 = 
"""
1  *1 C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4     O     0 {3,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,D}
3     O     0 {2,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2e+16,"s^-1"),
        n = 0,
        Ea = (338399,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ernst, J.", "Spindler, K."], title=u'Untersuchungen zum Thermischen Zerfall von Acetaldehyd und Aceton', journal="Ber. Bunsenges. Phys. Chem.", volume="79", pages="""1163""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 461,
    label = "r00010789",
    reactant1 = 
"""
1  *1 C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4     O     0 {3,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,D}
3     O     0 {2,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.7e+16,"s^-1"),
        n = 0,
        Ea = (341725,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ernst, J.", "Spindler, K.", "Wagner, H.Gg."], title=u'Untersuchungen zum Thermischen Zerfall von Acetaldehyd und Aceton', journal="Ber. Bunsenges. Phys. Chem.", volume="80", pages="""645""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 462,
    label = "r00010789",
    reactant1 = 
"""
1  *1 C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4     O     0 {3,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,D}
3     O     0 {2,D}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.94e+17,"s^-1"),
        n = 0,
        Ea = (353365,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Mousavipour, S.H.", "Pacey, P.D."], title=u'Initiation and abstraction reactions in the pyrolysis of acetone', journal="J. Phys. Chem.", volume="100", pages="""3573-3579""", year="1996", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 463,
    label = "r00010854",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 O     0 {1,S} {3,S}
3     O     1 {2,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.88e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (2660.63,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Cobos, C.J.", "Troe, J."], title=u'Theory of thermal unimolecular reactions at high pressures. II. Analysis of experimental results', journal="J. Chem. Phys.", volume="83", pages="""1010-1015""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000028.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 464,
    label = "r00010854",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 O     0 {1,S} {3,S}
3     O     1 {2,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (8.51428e+58,"cm^3/(mol*s)"),
        n = -15,
        Ea = (71255,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W.", "Hampson, R.F."], title=u'Chemical kinetic data base for combustion chemistry. Part I. Methane and related compounds', journal="J. Phys. Chem. Ref. Data", volume="15", pages="""1087""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000031.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 465,
    label = "r00010854",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 O     0 {1,S} {3,S}
3     O     1 {2,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.59985e+33,"cm^3/(mol*s)"),
        n = -7.13,
        Ea = (22365.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M.", "Westmoreland, P.R."], title=u'Bimolecular QRRK analyss of methyl radical reactions', journal="Int. J. Chem. Kinet.", volume="19", pages="""207""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000032.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 466,
    label = "r00010854",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 O     0 {1,S} {3,S}
3     O     1 {2,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.53e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-5728.67,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Keiffer, M.", "Miscampbell, A.J.", "Pilling, M.J."], title=u'A global technique for analysing multiple decay curves. Application to the CH_3 + O_2 system', journal="J. Chem. Soc. Faraday Trans. 2", volume="84", pages="""505""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000035.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 467,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.17e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (207.862,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Teng, L.", "Jones, W.E."], title=u'Kinetics of the Reactions of Hydrogen Atoms with Ethylene and Vinyl Fluoride', journal="J. Chem. Soc. Faraday Trans. 1", volume="68", pages="""1267""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 468,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.7e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1671.21,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Cobos, C.J.", "Troe, J."], title=u'Theory of thermal unimolecular reactions at high pressures. II. Analysis of experimental results', journal="J. Chem. Phys.", volume="83", pages="""1010-1015""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000018.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 469,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (814.818,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hase, W.L.", "Mondro, S.L.", "Duchovic, R.J.", "Hirst, D.M."], title=u'Thermal rate constant for H + CH_3 \u2192 CH_4 recombination. 3. Comparison of experiment and canonical variational transition state theory', journal="J. Am. Chem. Soc.", volume="109", pages="""2916-2922""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000020.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 470,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.58684e+16,"cm^3/(mol*s)"),
        n = -0.6,
        Ea = (1571.44,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Forst, W."], title=u'Microcanonical variational theory of radical recombination by inversion of interpolated partition function, with examples: CH_3 + H, CH_3 + CH_3', journal="J. Phys. Chem.", volume="95", pages="""3612-3620""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000027.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 471,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.93e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1147.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Takahashi, J.", "Momose, T.", "Shida, T."], title=u'Thermal rate constants for SiH_4=SiH_3+H and CH_4=CH_3+H by Canonical Variational Transition State Theory', journal="Bull. Chem. Soc. Jpn.", volume="67", pages="""74-85""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000037.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 472,
    label = "r00010887",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.62e+33,"cm^3/(mol*s)"),
        n = -4.76,
        Ea = (2440,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000038.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 473,
    label = "r00010887",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.24e+33,"cm^3/(mol*s)"),
        n = -4.76,
        Ea = (2440,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000039.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 474,
    label = "r00010887",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.572e+34,"cm^3/(mol*s)"),
        n = -4.76,
        Ea = (2440,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000040.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 475,
    label = "r00010887",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.86e+33,"cm^3/(mol*s)"),
        n = -4.76,
        Ea = (2440,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000041.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 476,
    label = "r00010887",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.93e+33,"cm^3/(mol*s)"),
        n = -4.76,
        Ea = (2440,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000042.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 477,
    label = "r00010887",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.24e+33,"cm^3/(mol*s)"),
        n = -4.76,
        Ea = (2440,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000043.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 478,
    label = "r00010887",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.86e+33,"cm^3/(mol*s)"),
        n = -4.76,
        Ea = (2440,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000044.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 479,
    label = "r00010887",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.834e+33,"cm^3/(mol*s)"),
        n = -4.76,
        Ea = (2440,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000045.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 480,
    label = "r00010887",
    reactant1 = 
"""
1  *  C     1
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.39e+16,"cm^3/(mol*s)"),
        n = -0.534,
        Ea = (536,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000046.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 481,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.08e-07,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-362619,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Sutherland, J.W.", "Su, M.-C.", "Michael, J.V."], title=u'Rate Constants for H + CH_4, CH_3 + H_2, and CH_4 Dissociation at High Temperature', journal="Int J. Chem. Kinet.", volume="33", pages="""669-684""", year="2001", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000048.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 482,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (5.13e+14,"s^-1"),
        n = 0,
        Ea = (422375,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Skinner, G.B.", "Ruehrwein, R.A."], title=u'Shock tube studies on the pyrolysis and oxidation of methane', journal="J. Phys. Chem.", volume="63", pages="""1736""", year="1959", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000050.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 483,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (3.8e+14,"s^-1"),
        n = 0,
        Ea = (430690,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Palmer, H.B.", "Hirt, T.J."], title=u'The activation energy for the pyrolysis of methane', journal="J. Phys. Chem.", volume="67", pages="""709""", year="1963", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000051.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 484,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.26e+14,"s^-1"),
        n = 0,
        Ea = (422375,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Palmer, H.B.", "Hirt, T.J."], title=u'The activation energy for the pyrolysis of methane', journal="J. Phys. Chem.", volume="67", pages="""709""", year="1963", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000052.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 485,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (430690,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kondratiev, V.N."], title=u'Determination of the rate constant for thermal cracking of methane by means of adiabatic compression and expansion', journal="Symp. Int. Combust. Proc.", volume="10", pages="""319""", year="1965", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000053.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 486,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.66e+16,"s^-1"),
        n = 0,
        Ea = (427364,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Placzek, D.W.", "Rabinovitch, B.S.", "Whitten, G.Z."], title=u'Some comparisons of the classical RRK and the RRKM theoretical rate formulations', journal="J. Chem. Phys.", volume="43", pages="""4071-4080""", year="1965", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000054.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 487,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (434847,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Palmer, H.B."], title=u'Discussion', journal="Symp. Int. Combust. Proc.", volume="12", pages="""588""", year="1969", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000055.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 488,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.26e+15,"s^-1"),
        n = 0,
        Ea = (434847,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hartig, R.", "Troe, J.", "Wagner, H.GG."], title=u'Thermal Decomposition of Methane Behind Reflected Shock Waves', journal="Symp. Int. Combust. Proc.", volume="13", pages="""147""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000056.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 489,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.8e+16,"s^-1"),
        n = 0,
        Ea = (449813,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Chen, C.J.", "Back, M.H.", "Back, R.A."], title=u'The Thermal Decomposition of Methane. I.Kinetics of the Promary Decomposition to C_2H_6 + H_2; Rate Constant for the Homogeneous Unimolecular Dissociation of Methane and its Pressure Dependence', journal="Can. J. Chem.", volume="53", pages="""3580""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000057.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 490,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (419881,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000058.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 491,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1e+16,"s^-1"),
        n = 0,
        Ea = (439004,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000059.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 492,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (3.72e+15,"s^-1"),
        n = 0,
        Ea = (434015,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W.", "Hampson, R.F."], title=u'Chemical kinetic data base for combustion chemistry. Part I. Methane and related compounds', journal="J. Phys. Chem. Ref. Data", volume="15", pages="""1087""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000060.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 493,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.75e+16,"s^-1"),
        n = 0,
        Ea = (440667,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Barnes, r.W.", "Pratt, G.L."], title=u'Pressure dependence of methane dissociation', journal="J. Chem. Soc. Faraday Trans. 2", volume="85", pages="""229""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000061.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 494,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (3.7e+15,"s^-1"),
        n = 0,
        Ea = (434015,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Rate constants for the decomposition and formation of simple alkanes over extended temperature and pressure ranges', journal="Combust. Flame", volume="78", pages="""71-86""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000062.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 495,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.4e+16,"s^-1"),
        n = 0,
        Ea = (439004,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Cobos, C.J.", "Troe, J."], title=u'The dissociation-recombination system CH_4 + M = CH_3 + H + M: reevaluated experiments from 300 to 3000 K', journal="Z. Phys. Chem. (Neue Folge)", volume="167", pages="""129-149""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000063.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 496,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (3.01e+12,"s^-1"),
        n = 0,
        Ea = (343388,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Arutyunov, V.S.", "Vedeneev, V.I.", "Moshkina, R.I.", "Ushakov, V.A."], title=u'Pyrolysis of methane under static conditions at 1100-1400 K', journal="Kinet. Catal.", volume="32", pages="""234-240""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000064.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 497,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.4e+16,"s^-1"),
        n = 0,
        Ea = (439004,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."], title=u'Evaluated kinetic data for combustion modelling', journal="J. Phys. Chem. Ref. Data", volume="21", pages="""411-429""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000065.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 498,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.4e+16,"s^-1"),
        n = 0,
        Ea = (439004,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Cobos, C.J.", "Troe, J."], title=u'The dissociation-recombination system CH_4 + M = CH_3 + H + M: II. Evaluation of experiments up to 5000 K and temperature dependence of <\u0394E>', journal="Z. Phys. Chem. (Munich)", volume="176", pages="""161-171""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000066.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 499,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.4e+16,"s^-1"),
        n = 0,
        Ea = (439004,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Frank, P.", "Hayman, G.", "Just, Th.", "Kerr, J.A.", "Murrells, T.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."], title=u'Evaluated kinetic data for combusion modelling. Supplement I', journal="J. Phys. Chem. Ref. Data", volume="23", pages="""847-1033""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000067.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 500,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.03e+16,"s^-1"),
        n = 0,
        Ea = (435678,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Takahashi, J.", "Momose, T.", "Shida, T."], title=u'Thermal rate constants for SiH_4=SiH_3+H and CH_4=CH_3+H by Canonical Variational Transition State Theory', journal="Bull. Chem. Soc. Jpn.", volume="67", pages="""74-85""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000068.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 501,
    label = "r00010887",
    reactant1 = 
"""
1  *1 C     0 {2,S}
2  *2 H     0 {1,S}
""",
    product1 = 
"""
1  *  C     1
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.04e+18,"s^-1"),
        n = 0,
        Ea = (403252,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Davidson, D.F.", "Hanson, R.K.", "Bowman, C.T."], title=u'Communication: revised values for the rate coefficients of ethane and methane decomposition', journal="Int. J. Chem. Kinet.", volume="27", pages="""305-308""", year="1995", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000069.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 502,
    label = "r00010916",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *2 C     0 {1,S}
3     C     0 {4,S}
4     C     0 {1,S} {3,S} {5,D}
5     C     0 {4,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,D} {4,S}
3     C     0 {2,D}
4  *  C     1 {2,S}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+16,"s^-1"),
        n = 0,
        Ea = (296827,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Trenwith, A.B.", "Wrigley, S.P."], title=u'Dissociation of 2-Methylbut-1-ene and the Resonance Energy of the 2-Methyl allyl Radical', journal="J. Chem. Soc. Faraday Trans. 1", volume="73", pages="""817""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:41 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 503,
    label = "r00011156",
    reactant1 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6  *  C     1 {4,B} {5,B}
""",
    reactant2 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6  *  C     1 {4,B} {5,B}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,B} {4,B}
2  *2 C     0 {1,S} {5,B} {6,B}
3     C     0 {1,B} {8,B}
4     C     0 {1,B} {9,B}
5     C     0 {2,B} {11,B}
6     C     0 {2,B} {12,B}
7     C     0 {8,B} {9,B}
8     C     0 {3,B} {7,B}
9     C     0 {4,B} {7,B}
10    C     0 {11,B} {12,B}
11    C     0 {5,B} {10,B}
12    C     0 {6,B} {10,B}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.39e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (465.61,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Park, J.", "Lin, M.C."], title=u'Kinetics for the recombination of phenyl radicals', journal="J. Phys. Chem. A", volume="101", pages="""14-18""", year="1997", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:45 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 504,
    label = "r00011168",
    reactant1 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6  *  C     1 {4,B} {5,B}
""",
    reactant2 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,B} {3,B} {7,S}
2     C     0 {1,B} {5,B}
3     C     0 {1,B} {6,B}
4     C     0 {5,B} {6,B}
5     C     0 {2,B} {4,B}
6     C     0 {3,B} {4,B}
7  *2 O     0 {1,S} {8,S}
8     O     1 {7,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.03e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1338.63,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Yu, T.", "Lin, M.C."], title=u'Kinetics of the C_6H_5 + O_2 reaction at low temperatures', journal="J. Am. Chem. Soc.", volume="116", pages="""9571-9576""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:45 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 505,
    label = "r00011174",
    reactant1 = 
"""
1  *1 C     0 {2,B} {3,B} {7,S}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6     C     0 {4,B} {5,B}
7  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6  *  C     1 {4,B} {5,B}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (7.08e+14,"s^-1"),
        n = 0,
        Ea = (443161,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Asaba, T.", "Fujii, N."], title=u'High temperature oxidation of benzene', journal="Proc. Int. Symp. Shock Tubes Waves", volume="8", pages="""1-12""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:45 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 506,
    label = "r00011174",
    reactant1 = 
"""
1  *1 C     0 {2,B} {3,B} {7,S}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6     C     0 {4,B} {5,B}
7  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6  *  C     1 {4,B} {5,B}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (5.01e+15,"s^-1"),
        n = 0,
        Ea = (451476,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hsu, D.S.Y.", "Lin, C.Y.", "Lin, M.C."], title=u'CO formation in early stage high temperature benzene oxidation under fuel lean conditions: Kinetics of the initiation reaction, C_6H_6 \u2192 C_6H_5 \u2192 H', journal="Symp. Int. Combust. Proc.", volume="20", pages="""623""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:45 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 507,
    label = "r00011174",
    reactant1 = 
"""
1  *1 C     0 {2,B} {3,B} {7,S}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6     C     0 {4,B} {5,B}
7  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6  *  C     1 {4,B} {5,B}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (5.75e+16,"s^-1"),
        n = 0,
        Ea = (484734,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hsu, D.S.Y.", "Lin, C.Y.", "Lin, M.C."], title=u'CO formation in early stage high temperature benzene oxidation under fuel lean conditions: Kinetics of the initiation reaction, C_6H_6 \u2192 C_6H_5 \u2192 H', journal="Symp. Int. Combust. Proc.", volume="20", pages="""623""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:45 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 508,
    label = "r00011174",
    reactant1 = 
"""
1  *1 C     0 {2,B} {3,B} {7,S}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6     C     0 {4,B} {5,B}
7  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6  *  C     1 {4,B} {5,B}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (4.57e+13,"s^-1"),
        n = 0,
        Ea = (372488,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kern, R.D.", "Wu, C.H.", "Skinner, G.B.", "Rao, V.S.", "Kiefer, J.H.", "Towers, J.A.", "Mizerka, L.J."], title=u'Collaborative shock tube studies of benzene pyrolysis', journal="Symp. Int. Combust. Proc.", volume="20", pages="""789""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:45 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 509,
    label = "r00011174",
    reactant1 = 
"""
1  *1 C     0 {2,B} {3,B} {7,S}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6     C     0 {4,B} {5,B}
7  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6  *  C     1 {4,B} {5,B}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (2e+17,"s^-1"),
        n = 0,
        Ea = (493880,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kiefer, J.H.", "Mizerka, L.J.", "Patel, M.R.", "Wei, H.-C."], title=u'A shock tube investigation of major pathways in the high-temperature pyrolysis of benzene', journal="J. Phys. Chem.", volume="89", pages="""2013""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:45 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 510,
    label = "r00011174",
    reactant1 = 
"""
1  *1 C     0 {2,B} {3,B} {7,S}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6     C     0 {4,B} {5,B}
7  *2 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6  *  C     1 {4,B} {5,B}
""",
    product2 = 
"""
1  *  H     1
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (9.29e+14,"s^-1"),
        n = 0,
        Ea = (443161,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rao, V.S.", "Skinner, G.B."], title=u'Formation of H and D atoms in pyrolysis of benzene-d_6, chlorobenzene, bromobenzene, and iodobenzene behind shock waves', journal="J. Phys. Chem.", volume="92", pages="""2442""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:45 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 511,
    label = "r00011400",
    reactant1 = 
"""
1     C     0 {2,B} {3,B} {7,S}
2     C     0 {1,B} {5,B}
3     C     0 {1,B} {6,B}
4     C     0 {5,B} {6,B}
5     C     0 {2,B} {4,B}
6     C     0 {3,B} {4,B}
7  *1 C     0 {1,S} {8,D} {9,S}
8     O     0 {7,D}
9  *2 H     0 {7,S}
""",
    product1 = 
"""
1  *  H     1
""",
    product2 = 
"""
1     C     0 {2,B} {3,B} {7,S}
2     C     0 {1,B} {5,B}
3     C     0 {1,B} {6,B}
4     C     0 {5,B} {6,B}
5     C     0 {2,B} {4,B}
6     C     0 {3,B} {4,B}
7  *  C     1 {1,S} {8,D}
8     O     0 {7,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+15,"s^-1"),
        n = 0,
        Ea = (350039,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Grela, M.A.", "Colussi, A.J."], title=u'Kinetics and mechanism of the thermal decomposition of unsaturated aldehydes: Benzaldehyde, 2-butenal, and 2-furaldehyde', journal="J. Phys. Chem.", volume="90", pages="""434""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 512,
    label = "r00011415",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,D}
2  *2 C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product1 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    product2 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.1e+16,"s^-1"),
        n = 0,
        Ea = (390780,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kiefer, J.H.", "Wei, H.C.", "Kern, R.D.", "Wu, C.H."], title=u'The high temperature pyrolysis of 1,3-butadiene: Heat of formation and rate of dissociation of vinyl radical', journal="Int. J. Chem. Kinet.", volume="17", pages="""225""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 513,
    label = "r00011415",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,D}
2  *2 C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product1 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    product2 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.07e+12,"s^-1"),
        n = 0,
        Ea = (278535,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kern, R.D.", "Singh, H.J.", "Wu, C.H."], title=u'Thermal decomposition of 1,2 butadiene', journal="Int. J. Chem. Kinet.", volume="20", pages="""731""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 514,
    label = "r00011415",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,D}
2  *2 C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product1 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    product2 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.07e+17,"s^-1"),
        n = 0,
        Ea = (393275,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kiefer, J.H.", "Mitchell, K.I.", "Wei, H.C."], title=u'The high temperature pyrolysis of 1,3-butadiene II: Pulsed laser flash absorption rate constants, and consideration of possible molecular dissociation pathways', journal="Int. J. Chem. Kinet.", volume="20", pages="""787""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 515,
    label = "r00011415",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,D}
2  *2 C     0 {1,S} {4,D}
3     C     0 {1,D}
4     C     0 {2,D}
""",
    product1 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    product2 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.8e+13,"s^-1"),
        n = 0,
        Ea = (355859,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rao, V.S.", "Takeda, K.", "Skinner, G.B."], title=u'Formation of H and D atoms in pyrolysis of 1,3-butadiene and 1,3 butadiene-1,1,4,4,-d_4 behind shock waves', journal="Int. J. Chem. Kinet.", volume="20", pages="""153""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 516,
    label = "r00011454",
    reactant1 = 
"""
1     C     0 {2,D}
2  *  C     1 {1,D}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4  *  C     1 {2,D}
""",
    product1 = 
"""
1     C     0 {2,D} {4,S}
2  *2 C     0 {1,D} {3,S}
3  *1 C     0 {2,S} {5,D}
4     C     0 {1,S} {6,D}
5     C     0 {3,D}
6     C     0 {4,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.49782e+13,"cm^3/(mol*s)"),
        n = -0.075,
        Ea = (415.724,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Westmoreland, P.R.", "Dean, A.M.", "Howard, J.B.", "Longwell, J.P."], title=u'Forming benzene in flames by chemically activated isomerization', journal="J. Phys. Chem.", volume="93", pages="""8171""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 517,
    label = "r00011505",
    reactant1 = 
"""
1     C     0 {3,S} {5,S}
2     C     0 {4,S} {6,S}
3     C     0 {1,S} {7,S}
4     C     0 {2,S} {8,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {3,S} {9,S} {11,D}
8     C     0 {4,S} {10,S} {12,D}
9  *1 O     0 {7,S} {10,S}
10 *2 O     0 {8,S} {9,S}
11    O     0 {7,D}
12    O     0 {8,D}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S} {5,D} {6,S}
5     O     0 {4,D}
6  *  O     1 {4,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S} {5,S} {6,D}
5  *  O     1 {4,S}
6     O     0 {4,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.9e+14,"s^-1"),
        n = 0,
        Ea = (123886,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rembaum, A.", "Szwarc, M."], title=u'O-O bond dissociation energies in propionyl and butyryl peroxides', journal="J. Chem. Phys.", volume="23", pages="""909-913""", year="1955", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:48 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 518,
    label = "r00011580",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3     C     0 {1,S} {5,T}
4     C     0 {2,S} {6,T}
5     C     0 {3,T}
6     C     0 {4,T}
""",
    product1 = 
"""
1  *  C     1 {2,S}
2     C     0 {1,S} {3,T}
3     C     0 {2,T}
""",
    product2 = 
"""
1  *  C     1 {2,S}
2     C     0 {1,S} {3,T}
3     C     0 {2,T}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+14,"s^-1"),
        n = 0,
        Ea = (258580,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:48 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 519,
    label = "r00011636",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *2 O     0 {2,S}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+11,"s^-1"),
        n = 0,
        Ea = (133863,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kirk, A.D."], title=u'The thermal decomposition of methyl hydroperoxide', journal="Can. J. Chem.", volume="43", pages="""2236-2242""", year="1965", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:49 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 520,
    label = "r00011636",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *2 O     0 {2,S}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+14,"s^-1"),
        n = 0,
        Ea = (177098,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lightfoot, P.D.", "Roussel, P.", "Caralp, F.", "Lesclaux, R."], title=u'Flash photolysis study of the CH_3O_2 + CH_3O_2 and CH_3O_2 + HO_2 reactions between 600 and 719 K: unimolecular decomposition of methylhydroperoxide', journal="J. Chem. Soc. Faraday Trans.", volume="87", pages="""3213-3220""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:49 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 521,
    label = "r00011636",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *2 O     0 {2,S}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4e+15,"s^-1"),
        n = 0,
        Ea = (179593,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."], title=u'Evaluated kinetic data for combustion modelling', journal="J. Phys. Chem. Ref. Data", volume="21", pages="""411-429""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:49 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 522,
    label = "r00011636",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *2 O     0 {2,S}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6e+14,"s^-1"),
        n = 0,
        Ea = (177098,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Frank, P.", "Hayman, G.", "Just, Th.", "Kerr, J.A.", "Murrells, T.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."], title=u'Evaluated kinetic data for combusion modelling. Supplement I', journal="J. Phys. Chem. Ref. Data", volume="23", pages="""847-1033""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:49 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 523,
    label = "r00011653",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 O     0 {1,S} {4,S}
4  *2 O     0 {3,S}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+13,"s^-1"),
        n = 0,
        Ea = (157975,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kirk, A.D.", "Knox, J.H."], title=u'The pyrolysis of alkyl hydroperoxides in the gas phase', journal="Trans. Faraday Soc.", volume="56", pages="""1296-1303""", year="1960", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:49 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 524,
    label = "r00011653",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 O     0 {1,S} {4,S}
4  *2 O     0 {3,S}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4e+15,"s^-1"),
        n = 0,
        Ea = (179593,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."], title=u'Evaluated kinetic data for combustion modelling', journal="J. Phys. Chem. Ref. Data", volume="21", pages="""411-429""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:49 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 525,
    label = "r00011653",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 O     0 {1,S} {4,S}
4  *2 O     0 {3,S}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4e+15,"s^-1"),
        n = 0,
        Ea = (179593,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Frank, P.", "Hayman, G.", "Just, Th.", "Kerr, J.A.", "Murrells, T.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."], title=u'Evaluated kinetic data for combusion modelling. Supplement I', journal="J. Phys. Chem. Ref. Data", volume="23", pages="""847-1033""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:49 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 526,
    label = "r00011657",
    reactant1 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *1 O     0 {1,S} {5,S}
5  *2 O     0 {4,S}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.58e+15,"s^-1"),
        n = 0,
        Ea = (167121,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kirk, A.D.", "Knox, J.H."], title=u'The pyrolysis of alkyl hydroperoxides in the gas phase', journal="Trans. Faraday Soc.", volume="56", pages="""1296-1303""", year="1960", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:49 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 527,
    label = "r00011751",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2     C     0 {1,S}
3     C     0 {4,S}
4  *2 C     0 {1,S} {3,S} {5,D}
5     O     0 {4,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,D}
3     O     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.27e+14,"s^-1"),
        n = 0,
        Ea = (105594,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Abuin, E.", "Lissi, E.A."], title=u'Arrhenius Parameters for the Photocleavage of Butan-2-one Triplets', journal="J. Photochem.", volume="5", pages="""65""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 528,
    label = "r00011821",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *2 H     0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.1e+18,"cm^3/(mol*s)"),
        n = -0.86,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 529,
    label = "r00011821",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *2 H     0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.2e+18,"cm^3/(mol*s)"),
        n = -0.86,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 530,
    label = "r00011821",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *2 H     0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.2e+18,"cm^3/(mol*s)"),
        n = -0.86,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 531,
    label = "r00011821",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *2 H     0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.08e+19,"cm^3/(mol*s)"),
        n = -1.24,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 532,
    label = "r00011821",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *2 H     0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.126e+19,"cm^3/(mol*s)"),
        n = -0.76,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 533,
    label = "r00011821",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *2 H     0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.6e+19,"cm^3/(mol*s)"),
        n = -1.24,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 534,
    label = "r00011821",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *2 H     0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7e+17,"cm^3/(mol*s)"),
        n = -0.8,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 535,
    label = "r00011821",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *2 H     0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.8e+18,"cm^3/(mol*s)"),
        n = -0.86,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000015.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 536,
    label = "r00011821",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *2 H     0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-5437.66,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, R.R.", "Jackson, D.", "Walker, R.W.", "Webster, S.J."], title=u'Interpretation of the slow reaction and second limit of hydrogen oxygen mixtures by computer methods', journal="Trans. Faraday Soc.", volume="63", pages="""1676-1686""", year="1967", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000017.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 537,
    label = "r00011821",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *2 H     0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.63e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3184.44,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Cobos, C.J.", "Troe, J."], title=u'Theory of thermal unimolecular reactions at high pressures. II. Analysis of experimental results', journal="J. Chem. Phys.", volume="83", pages="""1010-1015""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000020.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 538,
    label = "r00011821",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *2 H     0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (8.79195e+10,"cm^3/(mol*s)"),
        n = 1,
        Ea = (1862.44,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Duchovic, R.J.", "Pettigrew, J.D.", "Welling, B.", "Shipchandler, T."], title=u'Conventional transition state theory/Rice-Ramsperger-Kassel-Marcus theory calculations of thermal termolecular rate coefficients for H(D)+O_2+M', journal="J. Chem. Phys.", volume="105", pages="""10367-10379""", year="1996", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000022.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 539,
    label = "r00011821",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *2 H     0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.34e+19,"cm^3/(mol*s)"),
        n = -1.4,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Davis, S.G.", "Joshi, A.V.", "Wang, H.", "Egolfopoulos, F."], title=u'An optimized kinetic model of H2/CO Combustion', journal="Proc. Combust. Inst.", volume="30", pages="""1283-1292""", year="2005", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000026.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 540,
    label = "r00011821",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *2 H     0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.07e+19,"cm^3/(mol*s)"),
        n = -1.4,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Davis, S.G.", "Joshi, A.V.", "Wang, H.", "Egolfopoulos, F."], title=u'An optimized kinetic model of H2/CO Combustion', journal="Proc. Combust. Inst.", volume="30", pages="""1283-1292""", year="2005", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000027.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 541,
    label = "r00011821",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *2 H     0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.95e+20,"cm^3/(mol*s)"),
        n = -1.4,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Davis, S.G.", "Joshi, A.V.", "Wang, H.", "Egolfopoulos, F."], title=u'An optimized kinetic model of H2/CO Combustion', journal="Proc. Combust. Inst.", volume="30", pages="""1283-1292""", year="2005", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000028.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 542,
    label = "r00011946",
    reactant1 = 
"""
1  *1 C     0 {2,S} {8,S} {9,S} {10,S}
2  *2 C     0 {1,S} {3,S} {4,S}
3     C     0 {2,S} {6,S}
4     C     0 {2,S} {7,S}
5     C     0 {6,S} {7,S}
6     C     0 {3,S} {5,S}
7     C     0 {4,S} {5,S}
8     C     0 {1,S}
9     C     0 {1,S}
10    C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {2,S} {3,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S} {6,S}
5     C     0 {3,S} {6,S}
6  *  C     1 {4,S} {5,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.04e+16,"s^-1"),
        n = 0,
        Ea = (310130,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal Decomposition of 3,4-Dimethylhexane, 2,2,3-Trimethylpentane, tert-Butylcyclohexane, and Related Hydrocarbons', journal="J. Phys. Chem.", volume="76", pages="""143""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:51 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 543,
    label = "r00011959",
    reactant1 = 
"""
1     C     0 {3,S} {5,S}
2     C     0 {4,S} {6,S}
3     C     0 {1,S}
4     C     0 {2,S}
5     C     0 {1,S} {7,S} {9,D}
6     C     0 {2,S} {8,S} {10,D}
7  *1 O     0 {5,S} {8,S}
8  *2 O     0 {6,S} {7,S}
9     O     0 {5,D}
10    O     0 {6,D}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S} {4,D} {5,S}
4     O     0 {3,D}
5  *  O     1 {3,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S} {4,S} {5,D}
4  *  O     1 {3,S}
5     O     0 {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.5e+14,"s^-1"),
        n = 0,
        Ea = (125549,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rembaum, A.", "Szwarc, M."], title=u'O-O bond dissociation energies in propionyl and butyryl peroxides', journal="J. Chem. Phys.", volume="23", pages="""909-913""", year="1955", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:51 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 544,
    label = "r00012437",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {5,S}
4     C     0 {2,S} {6,S}
5     C     0 {3,S} {7,D}
6     C     0 {4,S} {8,D}
7     C     0 {5,D}
8     C     0 {6,D}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4  *  C     1 {2,S}
5     C     0 {3,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,D}
2  *  C     1 {1,S}
3     C     0 {1,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.2e+16,"s^-1"),
        n = 0,
        Ea = (296827,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W.", "Walker, J.A."], title=u'Pyrolysis of 1,7-octadiene and the kinetic and thermodynamic stability of allyl and 4-pentenyl radicals', journal="J. Phys. Chem.", volume="96", pages="""8378-8384""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 545,
    label = "r00012502",
    reactant1 = 
"""
1     C     0 {3,S} {5,S}
2     C     0 {4,S} {6,S}
3     C     0 {1,S} {7,S}
4     C     0 {2,S} {8,S}
5     C     0 {1,S} {9,S}
6     C     0 {2,S} {10,S}
7     C     0 {3,S}
8     C     0 {4,S}
9  *1 O     0 {5,S} {10,S}
10 *2 O     0 {6,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S} {5,S}
5  *  O     1 {4,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5  *  O     1 {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.05e+16,"s^-1"),
        n = 0,
        Ea = (160469,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Sahetchian, K.A.", "Rigny, R.", "Blin, N.", "Heiss, A."], title=u'Homogeneous decomposition of dialkylperoxides in oxygen', journal="J. Chem. Soc. Faraday Trans. 2", volume="83", pages="""2035""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:54 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 546,
    label = "r00012588",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *2 C     0 {1,S} {5,S}
3     C     0 {4,S}
4     C     0 {1,S} {3,S} {6,D}
5     C     0 {2,S} {7,D}
6     C     0 {4,D}
7     C     0 {5,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,D} {4,S}
3     C     0 {2,D}
4  *  C     1 {2,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,D}
2  *  C     1 {1,S}
3     C     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.7e+14,"s^-1"),
        n = 0,
        Ea = (235300,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Roth, W.R.", "Bauer, F.", "Beitat, A.", "Ebbrecht, T.", "Wustefeld, M."], title=u'Die bildungsenthalpie des allyl- und methallyl-radikals', journal="Chem. Ber.", volume="124", pages="""1453-1460""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:54 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 547,
    label = "r00012661",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S} {4,S} {6,D}
4  *1 O     0 {3,S} {5,S}
5  *2 O     0 {4,S}
6     O     0 {3,D}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S} {4,S} {5,D}
4  *  O     1 {3,S}
5     O     0 {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+15,"s^-1"),
        n = 0,
        Ea = (167952,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Sahetchian, K.A.", "Rigny, R.", "Tardieu de Maleissye, J.", "Batt, L.", "Anwar Khan, M.", "Mathews, S."], title=u'The pyrolysis of organic hydroperoxides (ROOH)', journal="Symp. Int. Combust. Proc.", volume="24", pages="""637-643""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:56 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 548,
    label = "r00012760",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *2 O     0 {1,S} {5,S}
5     O     1 {4,S}
""",
    product1 = 
"""
1     O     1 {2,S}
2  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,D}
2  *  C     1 {1,S}
3     C     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.6e+10,"s^-1"),
        n = 0,
        Ea = (53295.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Morgan, C.A.", "Pilling, M.J.", "Tulloch, J.M.", "Ruiz, R.P.", "Bayes, K.D."], title=u'Direct determination of the equilibrium constant and thermodynamic parameters for the reaction C_3H_5 + O_2 = C_3H_5O_2', journal="J. Chem. Soc. Faraday Trans. 2", volume="78", pages="""1323""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:57 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 549,
    label = "r00013061",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S} {6,T}
6     C     0 {5,T}
""",
    product1 = 
"""
1  *  C     1 {2,S}
2     C     0 {1,S} {3,T}
3     C     0 {2,T}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.63e+15,"s^-1"),
        n = 0,
        Ea = (290175,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Rate and mechanism of thermal decomposition of 4-methyl-1-pentyne in a single-pulse shock tube', journal="Int. J. Chem. Kinet.", volume="2", pages="""23""", year="1970", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:12 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 550,
    label = "r00013101",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S} {5,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {2,S} {7,D}
7     C     0 {6,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S} {3,S}
3     C     0 {2,S} {4,D}
4     C     0 {3,D}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *  C     1 {1,S} {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+15,"s^-1"),
        n = 0,
        Ea = (270220,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal decomposition of 3,4-dimethylpentene-1,2,3,3-trimethylpentane, 3,3-dimethylpentane, and isobutylbenzene in a single pulse shock tube', journal="Int. J. Chem. Kinet.", volume="1", pages="""245""", year="1969", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:12 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 551,
    label = "r00013690",
    reactant1 = 
"""
1  *1 O     0 {2,S}
2  *2 O     0 {1,S}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1  *  O     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.41e+11,"s^-1"),
        n = 0,
        Ea = (165458,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["McLane, C.K."], title=u'Hydrogen peroxide in the thermal hydrogen oxygen reaction. I. Thermal decomposition of hydrogen peroxide', journal="J. Chem. Phys.", volume="17", pages="""379-385""", year="1949", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:13 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 552,
    label = "r00013690",
    reactant1 = 
"""
1  *1 O     0 {2,S}
2  *2 O     0 {1,S}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1  *  O     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.14e+10,"s^-1"),
        n = 0,
        Ea = (167952,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["McLane, C.K."], title=u'Hydrogen peroxide in the thermal hydrogen oxygen reaction. I. Thermal decomposition of hydrogen peroxide', journal="J. Chem. Phys.", volume="17", pages="""379-385""", year="1949", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:13 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 553,
    label = "r00013690",
    reactant1 = 
"""
1  *1 O     0 {2,S}
2  *2 O     0 {1,S}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1  *  O     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+13,"s^-1"),
        n = 0,
        Ea = (201210,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Giguere, P.A.", "Liu, I.D."], title=u'Kinetics of the thermal decomposition of hydrogen peroxide vapor', journal="Can. J. Chem.", volume="35", pages="""283-293""", year="1957", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:13 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 554,
    label = "r00013690",
    reactant1 = 
"""
1  *1 O     0 {2,S}
2  *2 O     0 {1,S}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1  *  O     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.95e+14,"s^-1"),
        n = 0,
        Ea = (202873,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Brouwer, L.", "Cobos, C.J.", "Troe, J.", "Dubal, H.-R.", "Crim, F.F."], title=u'Specific rate constants k(E,J) and product state distributions in simple bond fission reactions. II. Application to HOOH \u2192 OH + OH', journal="J. Chem. Phys.", volume="86", pages="""6171""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000018.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:13 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 555,
    label = "r00013690",
    reactant1 = 
"""
1  *1 O     0 {2,S}
2  *2 O     0 {1,S}
""",
    product1 = 
"""
1  *  O     1
""",
    product2 = 
"""
1  *  O     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3e+14,"s^-1"),
        n = 0,
        Ea = (202873,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."], title=u'Evaluated kinetic data for combustion modelling', journal="J. Phys. Chem. Ref. Data", volume="21", pages="""411-429""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000019.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:13 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 556,
    label = "r00013690",
    reactant1 = 
"""
1  *  O     1
""",
    reactant2 = 
"""
1  *  O     1
""",
    product1 = 
"""
1  *1 O     0 {2,S}
2  *2 O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+18,"cm^3/(mol*s)"),
        n = -0.9,
        Ea = (-1700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000022.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:13 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 557,
    label = "r00013690",
    reactant1 = 
"""
1  *  O     1
""",
    reactant2 = 
"""
1  *  O     1
""",
    product1 = 
"""
1  *1 O     0 {2,S}
2  *2 O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6e+18,"cm^3/(mol*s)"),
        n = -0.9,
        Ea = (-1700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000023.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:13 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 558,
    label = "r00013690",
    reactant1 = 
"""
1  *  O     1
""",
    reactant2 = 
"""
1  *  O     1
""",
    product1 = 
"""
1  *1 O     0 {2,S}
2  *2 O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.38e+19,"cm^3/(mol*s)"),
        n = -0.9,
        Ea = (-1700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000024.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:13 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 559,
    label = "r00013690",
    reactant1 = 
"""
1  *  O     1
""",
    reactant2 = 
"""
1  *  O     1
""",
    product1 = 
"""
1  *1 O     0 {2,S}
2  *2 O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6e+18,"cm^3/(mol*s)"),
        n = -0.9,
        Ea = (-1700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000025.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:13 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 560,
    label = "r00013690",
    reactant1 = 
"""
1  *  O     1
""",
    reactant2 = 
"""
1  *  O     1
""",
    product1 = 
"""
1  *1 O     0 {2,S}
2  *2 O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.45e+18,"cm^3/(mol*s)"),
        n = -0.9,
        Ea = (-1700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000026.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:13 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 561,
    label = "r00013690",
    reactant1 = 
"""
1  *  O     1
""",
    reactant2 = 
"""
1  *  O     1
""",
    product1 = 
"""
1  *1 O     0 {2,S}
2  *2 O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6e+18,"cm^3/(mol*s)"),
        n = -0.9,
        Ea = (-1700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000027.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:13 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 562,
    label = "r00013690",
    reactant1 = 
"""
1  *  O     1
""",
    reactant2 = 
"""
1  *  O     1
""",
    product1 = 
"""
1  *1 O     0 {2,S}
2  *2 O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.9e+18,"cm^3/(mol*s)"),
        n = -0.9,
        Ea = (-1700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000028.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:13 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 563,
    label = "r00013690",
    reactant1 = 
"""
1  *  O     1
""",
    reactant2 = 
"""
1  *  O     1
""",
    product1 = 
"""
1  *1 O     0 {2,S}
2  *2 O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.61e+18,"cm^3/(mol*s)"),
        n = -0.9,
        Ea = (-1700,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000029.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:13 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 564,
    label = "r00013690",
    reactant1 = 
"""
1  *  O     1
""",
    reactant2 = 
"""
1  *  O     1
""",
    product1 = 
"""
1  *1 O     0 {2,S}
2  *2 O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.4e+13,"cm^3/(mol*s)"),
        n = -0.37,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000030.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:13 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 565,
    label = "r00013764",
    reactant1 = 
"""
1  *  O     1
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 O     0 {2,S}
2  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.2e+22,"cm^3/(mol*s)"),
        n = -2,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:13 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 566,
    label = "r00013764",
    reactant1 = 
"""
1  *  O     1
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 O     0 {2,S}
2  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.606e+22,"cm^3/(mol*s)"),
        n = -2,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:13 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 567,
    label = "r00013764",
    reactant1 = 
"""
1  *  O     1
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 O     0 {2,S}
2  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.03e+22,"cm^3/(mol*s)"),
        n = -2,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:13 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 568,
    label = "r00013764",
    reactant1 = 
"""
1  *  O     1
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 O     0 {2,S}
2  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.4e+22,"cm^3/(mol*s)"),
        n = -2,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:13 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 569,
    label = "r00013764",
    reactant1 = 
"""
1  *  O     1
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 O     0 {2,S}
2  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.6e+22,"cm^3/(mol*s)"),
        n = -2,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000013.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:13 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 570,
    label = "r00013764",
    reactant1 = 
"""
1  *  O     1
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 O     0 {2,S}
2  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.36e+21,"cm^3/(mol*s)"),
        n = -2,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000014.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:13 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 571,
    label = "r00013764",
    reactant1 = 
"""
1  *  O     1
""",
    reactant2 = 
"""
1  *  H     1
""",
    product1 = 
"""
1  *1 O     0 {2,S}
2  *2 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.62e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (623.585,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Cobos, C.J.", "Troe, J."], title=u'Theory of thermal unimolecular reactions at high pressures. II. Analysis of experimental results', journal="J. Chem. Phys.", volume="83", pages="""1010-1015""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000016.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:13 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 572,
    label = "r00013875",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 O     0 {1,S} {4,S}
4     O     1 {3,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.72e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14300.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Jolley, J.E."], title=u'The photooxidation of diethyl ketone', journal="J. Am. Chem. Soc.", volume="79", pages="""1537""", year="1957", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:14 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 573,
    label = "r00013875",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 O     0 {1,S} {4,S}
4     O     1 {3,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.94e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-3517.02,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Munk, J.", "Pagsberg, P.", "Ratajczak, E.", "Sillesen, A."], title=u'Spectrokinetic studies of ethyl and ethylperoxy radicals', journal="J. Phys. Chem.", volume="90", pages="""2752""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:14 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 574,
    label = "r00013875",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 O     0 {1,S} {4,S}
4     O     1 {3,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.99834e+42,"cm^3/(mol*s)"),
        n = -10.3,
        Ea = (25442.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bozzelli, J.W.", "Dean, A.M."], title=u'Chemical activation analysis of the reaction of C_2H_5 with O_2', journal="J. Phys. Chem.", volume="94", pages="""3313""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000013.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:14 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 575,
    label = "r00013875",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 O     0 {1,S} {4,S}
4     O     1 {3,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.214e+10,"cm^3/(mol*s)"),
        n = 0.772,
        Ea = (-2386.25,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Wagner, A.F.", "Slagle, I.R.", "Sarzynski, D.", "Gutman, D."], title=u'Experimental and theoretical studies of the C_2H_5 + O_2 reaction kinetics', journal="J. Phys. Chem.", volume="94", pages="""1853""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000017.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:14 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 576,
    label = "r00013875",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 O     0 {1,S} {4,S}
4     O     1 {3,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.36e-14,"cm^3/(mol*s)"),
        n = 0.98,
        Ea = (-1050.84,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Miller, J.A.", "Klippenstein, S.J."], title=u'The Reaction Between Ethyl and Molecular Oxygen II. Further Analysis', journal="Int J. Chem. Kinet.", volume="33", pages="""654-668""", year="2001", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000030.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:14 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 577,
    label = "r00013875",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 O     0 {1,S} {4,S}
4     O     1 {3,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.26564e+15,"cm^3/(mol*s)"),
        n = -9.22,
        Ea = (21867.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["DeSain, J.D.", "Klippenstein, S.J.", "Miller, J.A.", "Taatjes, C.A."], title=u'Measurements, Theory, and Modeling of OH Formation in Ethyl + O_2 and Propyl + O_2 Reactions', journal="J. Phys. Chem. A", volume="107", pages="""4415-4427""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000031.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:14 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 578,
    label = "r00013875",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *2 O     0 {1,S} {4,S}
4     O     1 {3,S}
""",
    product1 = 
"""
1     O     1 {2,S}
2  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.3e+15,"s^-1"),
        n = -0.835,
        Ea = (143009,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Wagner, A.F.", "Slagle, I.R.", "Sarzynski, D.", "Gutman, D."], title=u'Experimental and theoretical studies of the C_2H_5 + O_2 reaction kinetics', journal="J. Phys. Chem.", volume="94", pages="""1853""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000032.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:14 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 579,
    label = "r00013891",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S} {7,S}
2  *  C     1 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S} {6,D}
5     C     0 {3,D} {6,S}
6     C     0 {4,D} {5,S}
7     O     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {8,S}
2  *2 C     0 {1,S} {4,S} {7,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S} {6,D}
5     C     0 {3,D} {6,S}
6     C     0 {4,D} {5,S}
7  *1 O     0 {2,S} {9,S}
8     O     0 {1,S}
9     O     1 {7,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.13709e+15,"cm^3/(mol*s)"),
        n = -2.05,
        Ea = (19622.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lay, T.H.", "Bozzelli, J.W.", "Seinfeld, J.H."], title=u'Atmospheric photochemical oxidation of benzene: benzene + OH and the benzene-OH adduct (hydroxyl-2,4-cyclohexadienyl) + O_2', journal="J. Phys. Chem.", volume="100", pages="""6543-6554""", year="1996", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:14 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 580,
    label = "r00013891",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S} {7,S}
2  *  C     1 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S} {6,D}
5     C     0 {3,D} {6,S}
6     C     0 {4,D} {5,S}
7     O     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {8,S}
2  *2 C     0 {1,S} {4,S} {7,S}
3     C     0 {1,S} {5,D}
4     C     0 {2,S} {6,D}
5     C     0 {3,D} {6,S}
6     C     0 {4,D} {5,S}
7  *1 O     0 {2,S} {9,S}
8     O     0 {1,S}
9     O     1 {7,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.55603e+36,"cm^3/(mol*s)"),
        n = -8.86,
        Ea = (15880.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lay, T.H.", "Bozzelli, J.W.", "Seinfeld, J.H."], title=u'Atmospheric photochemical oxidation of benzene: benzene + OH and the benzene-OH adduct (hydroxyl-2,4-cyclohexadienyl) + O_2', journal="J. Phys. Chem.", volume="100", pages="""6543-6554""", year="1996", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:14 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 581,
    label = "r00013961",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {3,S}
2  *  C     1 {3,S}
3     O     0 {1,S} {2,S}
""",
    product1 = 
"""
1  *2 C     0 {3,S} {4,S}
2     C     0 {3,S}
3     O     0 {1,S} {2,S}
4  *1 O     0 {1,S} {5,S}
5     O     1 {4,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.39e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-7108.87,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hoyermann, K.", "Nacke, F."], title=u'Elementary reactions of the methoxymethyl radical in the gas phase: CH_3OCH_3 + F, CH_2OCH_3 + CH_2OCH_3, CH_2OCH_3 + O_2 and CH_2OCH_3 + O', journal="Symp. Int. Combust. Proc.", volume="26", pages="""505-512""", year="1996", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:14 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 582,
    label = "r00013961",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {3,S}
2  *  C     1 {3,S}
3     O     0 {1,S} {2,S}
""",
    product1 = 
"""
1  *2 C     0 {3,S} {4,S}
2     C     0 {3,S}
3     O     0 {1,S} {2,S}
4  *1 O     0 {1,S} {5,S}
5     O     1 {4,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.87e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-2710.52,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Maricq, M.M.", "Szente, J.J.", "Hybl, J.D."], title=u'Kinetic studies of the oxidation of dimethyl ether and its chain reaction with Cl_2', journal="J. Phys. Chem. A", volume="101", pages="""5155-5167""", year="1997", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:14 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 583,
    label = "r00013961",
    reactant1 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {3,S}
2  *  C     1 {3,S}
3     O     0 {1,S} {2,S}
""",
    product1 = 
"""
1  *2 C     0 {3,S} {4,S}
2     C     0 {3,S}
3     O     0 {1,S} {2,S}
4  *1 O     0 {1,S} {5,S}
5     O     1 {4,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.44e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-382.466,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Sehested, J.", "Sehested, K.", "Platz, J.", "Egsgaard, H.", "Nielsen, O.J."], title=u'Oxidation of dimethyl ether: absolute rate constants for the self reaction of CH_3OCH_2 radicals, the reaction of CH_3OCH_2 radicals with O_2, and the thermal decomposition of CH_3OCH_2 radicals', journal="Int. J. Chem. Kinet.", volume="29", pages="""627-636""", year="1997", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:14 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 584,
    label = "r00014912",
    reactant1 = 
"""
1     C     0 {3,S} {5,S} {6,S} {11,S}
2     C     0 {4,S} {7,S} {8,S} {12,S}
3     C     0 {1,S} {9,S}
4     C     0 {2,S} {10,S}
5     C     0 {1,S}
6     C     0 {1,S}
7     C     0 {2,S}
8     C     0 {2,S}
9     C     0 {3,S}
10    C     0 {4,S}
11 *1 O     0 {1,S} {12,S}
12 *2 O     0 {2,S} {11,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {6,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {6,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+15,"s^-1"),
        n = 0,
        Ea = (152155,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Perona, M.J.", "Golden, D.M."], title=u'Very Low-Pressure Pyrolysis. VIII. The Decomposition of Di-t-Amyl Peroxide', journal="Int. J. Chem. Kinet.", volume="5", pages="""55""", year="1973", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:17 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 585,
    label = "r00015258",
    reactant1 = 
"""
1  *1 C     0 {2,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {4,D} {6,S}
4     C     0 {3,D}
5     C     0 {1,S} {6,T}
6     C     0 {3,S} {5,T}
""",
    product1 = 
"""
1     C     0 {2,D} {4,S}
2     C     0 {1,D}
3  *  C     1 {5,S}
4     C     0 {1,S} {5,T}
5     C     0 {3,S} {4,T}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+16,"s^-1"),
        n = 0,
        Ea = (300152,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Staker, W.S.", "King, K.D.", "Nguyen, T.T."], title=u'Kinetics of the thermal unimolecular decomposition of hex-1-ene-3-yne. Heat of formation and resonance stabilization energy of the 3-ethenylpropargyl radical', journal="Int. J. Chem. Kinet.", volume="24", pages="""781-790""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:18 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 586,
    label = "r00015452",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {5,S}
3     C     0 {1,S} {4,D}
4     C     0 {3,D}
5     C     0 {2,S} {6,T}
6     C     0 {5,T}
""",
    product1 = 
"""
1  *  C     1 {2,S}
2     C     0 {1,S} {3,T}
3     C     0 {2,T}
""",
    product2 = 
"""
1     C     0 {2,S} {3,D}
2  *  C     1 {1,S}
3     C     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+15,"s^-1"),
        n = 0,
        Ea = (248603,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:23 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 587,
    label = "r00015596",
    reactant1 = 
"""
1  *1 C     0 {2,S} {5,S}
2  *2 C     0 {1,S} {6,S}
3     C     0 {5,S}
4     C     0 {6,S}
5     C     0 {1,S} {3,S} {7,D}
6     C     0 {2,S} {4,S} {8,D}
7     C     0 {5,D}
8     C     0 {6,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,D} {4,S}
3     C     0 {2,D}
4  *  C     1 {2,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {4,D}
3  *  C     1 {2,S}
4     C     0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6e+14,"s^-1"),
        n = 0,
        Ea = (238625,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Roth, W.R.", "Bauer, F.", "Beitat, A.", "Ebbrecht, T.", "Wustefeld, M."], title=u'Die bildungsenthalpie des allyl- und methallyl-radikals', journal="Chem. Ber.", volume="124", pages="""1453-1460""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:24 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 588,
    label = "r00015703",
    reactant1 = 
"""
1     C     0 {3,S} {5,S}
2     C     0 {4,S} {6,S}
3     C     0 {1,S} {7,S}
4     C     0 {2,S} {8,S}
5     C     0 {1,S}
6     C     0 {2,S}
7  *1 O     0 {3,S} {8,S}
8  *2 O     0 {4,S} {7,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S} {4,S}
4  *  O     1 {3,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *  O     1 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.42e+15,"s^-1"),
        n = 0,
        Ea = (150492,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Harris, E.J."], title=u'The decomposition of alkyl peroxides: dipropyl peroxide, ethyl hydrogen peroxide and propyl hydrogen peroxide', journal="Proc. R. Soc. London A", volume="173", pages="""126-146""", year="1939", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:26 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 589,
    label = "r00015703",
    reactant1 = 
"""
1     C     0 {3,S} {5,S}
2     C     0 {4,S} {6,S}
3     C     0 {1,S} {7,S}
4     C     0 {2,S} {8,S}
5     C     0 {1,S}
6     C     0 {2,S}
7  *1 O     0 {3,S} {8,S}
8  *2 O     0 {4,S} {7,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S} {4,S}
4  *  O     1 {3,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *  O     1 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+13,"s^-1"),
        n = 0,
        Ea = (146335,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["East, R.L.", "Phillips, L."], title=u'Kinetics of disproportionation-combination reactions between the n-propoxyl radical and nitric oxide, and of the pyrolysis of the O-O bond in di-n-propyl peroxide in the gas phase', journal="J. Chem. Soc. A", pages="""331""", year="1970", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:26 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 590,
    label = "r00015717",
    reactant1 = 
"""
1     C     0 {3,S}
2  *  C     1 {3,S}
3     O     0 {1,S} {2,S}
""",
    reactant2 = 
"""
1     C     0 {3,S}
2  *  C     1 {3,S}
3     O     0 {1,S} {2,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {5,S}
2  *2 C     0 {1,S} {6,S}
3     C     0 {5,S}
4     C     0 {6,S}
5     O     0 {1,S} {3,S}
6     O     0 {2,S} {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1662.89,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Maricq, M.M.", "Szente, J.J.", "Hybl, J.D."], title=u'Kinetic studies of the oxidation of dimethyl ether and its chain reaction with Cl_2', journal="J. Phys. Chem. A", volume="101", pages="""5155-5167""", year="1997", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:26 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 591,
    label = "r00015717",
    reactant1 = 
"""
1  *1 C     0 {2,S} {5,S}
2  *2 C     0 {1,S} {6,S}
3     C     0 {5,S}
4     C     0 {6,S}
5     O     0 {1,S} {3,S}
6     O     0 {2,S} {4,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2  *  C     1 {3,S}
3     O     0 {1,S} {2,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2  *  C     1 {3,S}
3     O     0 {1,S} {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.3e+15,"s^-1"),
        n = 0,
        Ea = (298490,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Loucks, L.F.", "Laidler, K.J."], title=u'Thermochemistry of the methoxymethyl radical', journal="Can. J. Chem.", volume="45", pages="""2785-2793""", year="1967", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:26 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 592,
    label = "r00015740",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {7,S}
2     C     0 {5,S} {6,S} {8,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {2,S}
7  *1 O     0 {1,S} {8,S}
8  *2 O     0 {2,S} {7,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.4e+15,"s^-1"),
        n = 0,
        Ea = (153818,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hughes, G.A.", "Phillips, L."], title=u'The kinetics of disproportionation-combination reactions between the isopropoxyl radical and nitric oxide, and of the pyrolysis of the O-O bond in di-isopropyl peroxide', journal="J. Chem. Soc. A", pages="""894-897""", year="1967", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:28 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 593,
    label = "r00015740",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {7,S}
2     C     0 {5,S} {6,S} {8,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {2,S}
7  *1 O     0 {1,S} {8,S}
8  *2 O     0 {2,S} {7,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.5e+15,"s^-1"),
        n = 0,
        Ea = (155481,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Leggett, C.", "Thynne, J.C.J."], title=u'Thermal decomposition of dialkyl peroxides and heats of formation of the ethoxyl and isopropoxyl radicals', journal="Trans. Faraday Soc.", volume="63", pages="""2504-2509""", year="1967", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:28 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 594,
    label = "r00015740",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {7,S}
2     C     0 {5,S} {6,S} {8,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {2,S}
7  *1 O     0 {1,S} {8,S}
8  *2 O     0 {2,S} {7,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+16,"s^-1"),
        n = 0,
        Ea = (163795,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Yee Quee, M.J.", "Thynne, J.C.J."], title=u'Reactions of isopropoxyl radicals', journal="J. Chem. Soc. Faraday Trans.", volume="64", pages="""1296""", year="1968", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:28 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 595,
    label = "r00015745",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3  *2 C     0 {1,S} {7,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {7,S}
7     C     0 {3,S} {6,S} {8,D}
8     C     0 {7,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,D} {4,S}
3     C     0 {2,D}
4  *  C     1 {2,S}
""",
    product2 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.27e+15,"s^-1"),
        n = 0,
        Ea = (276040,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Pyrolysis of 2,4-Dimethylhexene-1 and the Stability of Isobutenyl Radicals', journal="Int. J. Chem. Kinet.", volume="5", pages="""929""", year="1973", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:28 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 596,
    label = "r00016015",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2  *2 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {6,S}
5     C     0 {1,S} {6,T}
6     C     0 {4,S} {5,T}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {4,S}
3  *  C     1 {1,S} {5,S}
4     C     0 {2,S} {5,T}
5     C     0 {3,S} {4,T}
""",
    product2 = 
"""
1  *  C     1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.58e+16,"s^-1"),
        n = 0,
        Ea = (310961,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["King, K.D.", "Nguyen, T.T."], title=u'Very Low-Pressure Pyrolysis (VLPP) of Pentynes. II. 4-Methylpent-2-yne and 4,4-Dimethyl-pent-2-yne. Heats of Formation and Resonance Stabilization Energies of Methyl-Substituted Propargyl Radicals', journal="Int. J. Chem. Kinet.", volume="13", pages="""255""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 597,
    label = "r00016191",
    reactant1 = 
"""
1     C     0 {3,S} {5,S} {9,S}
2     C     0 {4,S} {6,S} {10,S}
3     C     0 {1,S} {7,S}
4     C     0 {2,S} {8,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {3,S}
8     C     0 {4,S}
9  *1 O     0 {1,S} {10,S}
10 *2 O     0 {2,S} {9,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
5  *  O     1 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
5  *  O     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.8e+15,"s^-1"),
        n = 0,
        Ea = (152155,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Walker, R.F.", "Phillips, L."], title=u'The kinetics of disproportionation-combination reactions between the s-butoxy-radical and nitric oxide, and of the pyrolysis of the O-O bond in di-s-butyl peroxide in the gas phase', journal="J. Chem. Soc. London A", pages="""2103-2106""", year="1968", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:39 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 598,
    label = "r00016216",
    reactant1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *  C     1 {1,S}
""",
    reactant2 = 
"""
1  *  O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2  *1 C     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6  *2 O     0 {2,S} {7,S}
7     O     1 {6,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.84e+22,"cm^3/(mol*s)"),
        n = -3.82,
        Ea = (23610.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Sun, H.", "Bozzelli, J.W."], title=u'Thermochemical and kinetic analysis on the reactions of neopentyl and hydroperoxy-neopentyl radicals with oxygen: Part I.  OH and initial stable HC product formation', journal="J. Phys. Chem. A", volume="108", pages="""1694-1711""", year="2004", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:39 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 599,
    label = "r00016525",
    reactant1 = 
"""
1     C     0 {2,S} {4,S} {5,S}
2  *1 C     0 {1,S} {3,S}
3  *2 C     0 {2,S} {7,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {8,S}
7     C     0 {3,S} {8,T}
8     C     0 {6,S} {7,T}
""",
    product1 = 
"""
1     C     0 {3,S}
2  *  C     1 {4,S}
3     C     0 {1,S} {4,T}
4     C     0 {2,S} {3,T}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *  C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.58e+16,"s^-1"),
        n = 0,
        Ea = (305973,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal Stability of Intermediate Sized Acetylenic Compounds and the Heats of Formation of Propargyl Radicals', journal="Int. J. Chem. Kinet.", volume="10", pages="""687""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:48 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 600,
    label = "r00016546",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3  *2 C     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {3,S} {7,T}
7     C     0 {6,T}
""",
    product1 = 
"""
1  *  C     1 {2,S}
2     C     0 {1,S} {3,T}
3     C     0 {2,T}
""",
    product2 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3     C     0 {4,S}
4  *  C     1 {1,S} {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+15,"s^-1"),
        n = 0,
        Ea = (291007,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal Stability of Intermediate Sized Acetylenic Compounds and the Heats of Formation of Propargyl Radicals', journal="Int. J. Chem. Kinet.", volume="10", pages="""687""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:48 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 601,
    label = "r00016760",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {13,S} {14,S}
2  *2 C     0 {1,S} {4,S} {15,S} {16,S}
3     C     0 {1,S}
4     C     0 {2,S}
5     C     0 {13,S}
6     C     0 {14,S}
7     C     0 {15,S}
8     C     0 {16,S}
9     C     0 {17,S}
10    C     0 {18,S}
11    C     0 {19,S}
12    C     0 {20,S}
13    C     0 {1,S} {5,S} {17,D}
14    C     0 {1,S} {6,S} {18,D}
15    C     0 {2,S} {7,S} {19,D}
16    C     0 {2,S} {8,S} {20,D}
17    C     0 {9,S} {13,D} {18,S}
18    C     0 {10,S} {14,D} {17,S}
19    C     0 {11,S} {15,D} {20,S}
20    C     0 {12,S} {16,D} {19,S}
""",
    product1 = 
"""
1     C     0 {6,S}
2     C     0 {7,S}
3     C     0 {8,S}
4     C     0 {9,S}
5     C     0 {10,S}
6     C     0 {1,S} {7,S} {8,D}
7  *  C     1 {2,S} {6,S} {9,S}
8     C     0 {3,S} {6,D} {10,S}
9     C     0 {4,S} {7,S} {10,D}
10    C     0 {5,S} {8,S} {9,D}
""",
    product2 = 
"""
1     C     0 {6,S}
2     C     0 {7,S}
3     C     0 {8,S}
4     C     0 {9,S}
5     C     0 {10,S}
6  *  C     1 {1,S} {7,S} {8,S}
7     C     0 {2,S} {6,S} {9,D}
8     C     0 {3,S} {6,S} {10,D}
9     C     0 {4,S} {7,D} {10,S}
10    C     0 {5,S} {8,D} {9,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.48e+13,"s^-1"),
        n = 0,
        Ea = (116403,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Roth, W.R.", "Hunold, F."], title=u'Bildungsenthalpie und Stabilisierungsenergie des Pentamethylcyclopentadienyl-Radikals', journal="Liebigs Ann.", pages="""1119-1122""", year="1995", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:57 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

