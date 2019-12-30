#!/usr/bin/env python
# encoding: utf-8

name = "Radical Corrections"
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "Radical",
    group = "OR{RJ, RJ2_triplet, RJ3}",
    thermo = 'RJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1,
    label = "RJ",
    group = 
"""
1 * R u1
""",
    thermo = 'CJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2,
    label = "CJ",
    group = 
"""
1 * C u1
""",
    thermo = 'CsJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 3,
    label = "CsJ",
    group = 
"""
1 * Cs u1
""",
    thermo = 'Cs_P',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 4,
    label = "CH3",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   H  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.71,0.34,-0.33,-1.07,-2.43,-3.54,-5.43],'cal/(mol*K)'),
        H298 = (104.81,'kcal/mol','+|-',0.1),
        S298 = (0.52,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated in relation to methane from NIST values""",
    longDesc = 
"""

""",
)

entry(
    index = 5,
    label = "Cs_P",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.77,-1.36,-1.91,-2.4,-3.16,-3.74,-4.66],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol'),
        S298 = (2.61,'cal/(mol*K)'),
    ),
    shortDesc = """Generic primary radical. (CHEN & BOZZELLI) #""",
    longDesc = 
"""

""",
)

entry(
    index = 6,
    label = "CJCO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S} {5,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.8,-1.5,-4.1,-6.7,-11.1,-14.3,-19.2],'J/(mol*K)'),
        H298 = (430,'kJ/mol'),
        S298 = (6.1,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 7,
    label = "C=C(O)CJ",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,S} {6,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2s u0 {2,S}
6   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.7,-2.3,-4.6,-7.1,-11,-13.5,-16.6],'J/(mol*K)'),
        H298 = (376.8,'kJ/mol'),
        S298 = (-3.9,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 8,
    label = "CJCOOH",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   Cs  u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2s u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.25,-0.76,-1.34,-1.91,-2.87,-3.6,-4.69],'cal/(mol*K)'),
        H298 = (103.26,'kcal/mol'),
        S298 = (3.54,'cal/(mol*K)'),
    ),
    shortDesc = """WIJAYA et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 9,
    label = "CJC(C)OC",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S}
2 * Cs  u1 {1,S} {5,S} {6,S}
3   O2s u0 {1,S} {7,S}
4   C   u0 {1,S}
5   H   u0 {2,S}
6   H   u0 {2,S}
7   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.5,1.8,-2,-5.5,-11,-14.7,-19.8],'J/(mol*K)'),
        H298 = (429.9,'kJ/mol'),
        S298 = (7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 10,
    label = "CJC(C)2O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2s u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.1,1.1,-2.1,-5.1,-9.7,-13.1,-18.5],'J/(mol*K)'),
        H298 = (431.1,'kJ/mol'),
        S298 = (5.1,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 11,
    label = "C=CC(C)(O)CJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   Cd  u0 {1,S} {8,D}
4   O2s u0 {1,S}
5   C   u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.5,-2.7,-5.5,-7.9,-11.8,-14.6,-19],'J/(mol*K)'),
        H298 = (431.9,'kJ/mol'),
        S298 = (9,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 12,
    label = "C=CC(O)(C=O)CJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   CO  u0 {1,S} {9,D}
4   Cd  u0 {1,S} {8,D}
5   O2s u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   C   u0 {4,D}
9   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4,0.9,-2.4,-5.2,-9.7,-13,-18.1],'J/(mol*K)'),
        H298 = (432.3,'kJ/mol'),
        S298 = (6.9,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 13,
    label = "CJC(C)(C=O)O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   CO  u0 {1,S} {8,D}
4   C   u0 {1,S}
5   O2s u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.6,5.1,2.3,-0.9,-6.8,-11.3,-17.8],'J/(mol*K)'),
        H298 = (430.9,'kJ/mol'),
        S298 = (3.7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 14,
    label = "CJC(O)2C",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   C   u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.4,-1.5,-5,-7.4,-10.8,-13.6,-18.2],'J/(mol*K)'),
        H298 = (435.3,'kJ/mol'),
        S298 = (8.1,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 15,
    label = "C=CC(O)2CJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   Cd  u0 {1,S} {8,D}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1,-0.2,-2,-4,-8.1,-11.6,-17.2],'J/(mol*K)'),
        H298 = (431.8,'kJ/mol'),
        S298 = (6.7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 16,
    label = "CJCC=O",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   C   u0 {1,S} {3,S}
3   CO  u0 {2,S} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.8,-1.5,-4.1,-6.7,-11.1,-14.3,-19.2],'J/(mol*K)'),
        H298 = (430,'kJ/mol'),
        S298 = (6.1,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 17,
    label = "CJC(C)2C=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   CO  u0 {1,S} {8,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.9,2.5,-1.1,-4.4,-9.7,-13.6,-19],'J/(mol*K)'),
        H298 = (429.5,'kJ/mol'),
        S298 = (7.9,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 18,
    label = "CJC(C=O)2C",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   CO  u0 {1,S} {8,D}
4   CO  u0 {1,S} {9,D}
5   C   u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   O2d u0 {3,D}
9   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.8,2.5,0.6,-1.9,-6.9,-10.9,-17.1],'J/(mol*K)'),
        H298 = (427,'kJ/mol'),
        S298 = (8.8,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 19,
    label = "C=CC(C=O)2CJ",
    group = 
"""
1    Cs  u0 {2,S} {3,S} {4,S} {5,S}
2  * Cs  u1 {1,S} {6,S} {7,S}
3    CO  u0 {1,S} {9,D}
4    CO  u0 {1,S} {10,D}
5    Cd  u0 {1,S} {8,D}
6    H   u0 {2,S}
7    H   u0 {2,S}
8    C   u0 {5,D}
9    O2d u0 {3,D}
10   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.7,2.4,-0.6,-3.5,-8.4,-12.1,-17.6],'J/(mol*K)'),
        H298 = (429.8,'kJ/mol'),
        S298 = (5.5,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 20,
    label = "C=CC(C)(C=O)CJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   CO  u0 {1,S} {9,D}
4   Cd  u0 {1,S} {8,D}
5   C   u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   C   u0 {4,D}
9   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.8,0.6,-2.7,-5.8,-10.8,-14.4,-19.3],'J/(mol*K)'),
        H298 = (430.6,'kJ/mol'),
        S298 = (9.8,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 21,
    label = "CJC(C)C=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S}
2 * Cs  u1 {1,S} {5,S} {6,S}
3   CO  u0 {1,S} {7,D}
4   C   u0 {1,S}
5   H   u0 {2,S}
6   H   u0 {2,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.6,0.2,-3,-5.8,-10.5,-14.1,-19.3],'J/(mol*K)'),
        H298 = (429.5,'kJ/mol'),
        S298 = (8.7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 22,
    label = "C=C(C=O)CJ",
    group = 
"""
1   Cd  u0 {2,S} {3,S} {4,D}
2 * Cs  u1 {1,S} {5,S} {6,S}
3   CO  u0 {1,S} {7,D}
4   C   u0 {1,D}
5   H   u0 {2,S}
6   H   u0 {2,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.8,-1.2,-2.4,-4.4,-8.2,-11.3,-15.9],'J/(mol*K)'),
        H298 = (374,'kJ/mol'),
        S298 = (-16.5,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 23,
    label = "CJCC=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {5,S} {6,S}
2   C   u0 {1,S} {3,S}
3   Cd  u0 {2,S} {4,D}
4   Cdd u0 {3,D} {7,D}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.3,-5.8,-8.1,-10.1,-13.4,-15.9,-19.9],'J/(mol*K)'),
        H298 = (420.3,'kJ/mol'),
        S298 = (16.4,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 24,
    label = "CJC(C)C=C=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   Cd  u0 {1,S} {4,D}
4   Cdd u0 {3,D} {8,D}
5   C   u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.2,-0.5,-4.1,-7.2,-11.8,-15,-19.5],'J/(mol*K)'),
        H298 = (430.1,'kJ/mol'),
        S298 = (9.7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 25,
    label = "C=C(CJ)C=C=O",
    group = 
"""
1   Cd  u0 {2,S} {3,S} {5,D}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   Cd  u0 {1,S} {4,D}
4   Cdd u0 {3,D} {8,D}
5   C   u0 {1,D}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.2,-5.6,-5.7,-6.4,-8.2,-10,-12.8],'J/(mol*K)'),
        H298 = (374.9,'kJ/mol'),
        S298 = (-8.1,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 26,
    label = "CsCsJ",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = 'Cs_P',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 27,
    label = "CCJ",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.65,-1.21,-1.75,-2.24,-3.02,-3.63,-3.63],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol','+|-',0.2),
        S298 = (2.61,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 28,
    label = "RCCJ",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.77,-1.36,-1.91,-2.4,-3.16,-3.74,-4.66],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol','+|-',0.2),
        S298 = (2.61,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 29,
    label = "Neopentyl",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.59,-1.32,-2.05,-2.65,-3.5,-4.06,-4.87],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol'),
        S298 = (3.03,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 30,
    label = "Isobutyl",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.54,-1.26,-1.92,-2.46,-3.27,-3.84,-3.84],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol'),
        S298 = (2.91,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 31,
    label = "CsJ-CsHH-HHN3s_513",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 p0 c0 {1,S} {6,S} {7,S}
3   N3s u0 p1 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.42827,1.35674,-1.51855,-4.31377,-8.85824,-12.4054,-18.1043],'J/(mol*K)'),
        H298 = (424.727,'kJ/mol'),
        S298 = (2.29234,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 32,
    label = "CsJ-CsHH-HHN3d_537",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 p0 c0 {1,S} {6,S} {7,S}
3   N3d u0 p1 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.08684,1.80834,-1.18257,-4.14603,-9.18584,-12.6059,-18.0041],'J/(mol*K)'),
        H298 = (400.011,'kJ/mol'),
        S298 = (24.9489,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 33,
    label = "Benzyl_P",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.492,0.642,0.109,-0.656,-1.606,-2.293,-4.101],'cal/(mol*K)'),
        H298 = (90.788,'kcal/mol','+|-',2.4),
        S298 = (-5.163,'cal/(mol*K)'),
    ),
    shortDesc = """Fitted From  Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 7/2017, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
[CH2]C1C=CC=CC=1
""",
)

entry(
    index = 34,
    label = "Allyl_P",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.62,-0.56,-0.78,-1.12,-1.84,-2.46,-3.49],'cal/(mol*K)'),
        H298 = (88.2,'kcal/mol'),
        S298 = (-2.56,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 35,
    label = "C=CC=CCJ",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {6,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.83,-1.86,-1.98,-1.99,-2.3,-2.5,-2.5],'cal/(mol*K)'),
        H298 = (80,'kcal/mol'),
        S298 = (-1.55,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 36,
    label = "CTCC=CCJ",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {6,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Ct u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.09,-1.62,-2.01,-2.63,-3.07,-3.48,-3.48],'cal/(mol*K)'),
        H298 = (81,'kcal/mol'),
        S298 = (-3.55,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 37,
    label = "CJC=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.2,-0.7,-2.6,-4.5,-8.1,-11,-15.6],'J/(mol*K)'),
        H298 = (373.5,'kJ/mol'),
        S298 = (-1.3,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 38,
    label = "CsJ-CdHH-HN3d_582",
    group = 
"""
1   Cd  u0 p0 c0 {2,S} {5,D} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {4,S}
3   H   u0 p0 c0 {2,S}
4   H   u0 p0 c0 {2,S}
5   N3d u0 p1 c0 {1,D}
6   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.13699,-3.51607,-4.78497,-6.71508,-10.4295,-13.4403,-18.7501],'J/(mol*K)'),
        H298 = (372.176,'kJ/mol'),
        S298 = (-9.46955,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 39,
    label = "CsJ-CdHH-HN5dc_693",
    group = 
"""
1   Cd   u0 p0 c0 {2,S} {5,D} {6,S}
2 * Cs   u1 p0 c0 {1,S} {3,S} {4,S}
3   H    u0 p0 c0 {2,S}
4   H    u0 p0 c0 {2,S}
5   N5dc u0 p0 c+1 {1,D}
6   H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.49161,-2.55893,-4.24251,-6.8092,-11.4862,-14.2808,-19.3847],'J/(mol*K)'),
        H298 = (320.191,'kJ/mol'),
        S298 = (-15.6421,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 40,
    label = "Propargyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Ct u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.84,-1.17,-1.56,-1.95,-2.7,-3.31,-5.31],'cal/(mol*K)'),
        H298 = (89.4,'kcal/mol'),
        S298 = (-0.51,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 41,
    label = "CsJ-CtHH-N3t_522",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   Ct  u0 p0 c0 {1,S} {5,T}
3   H   u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   N3t u0 p1 c0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.273584,-1.32013,-3.51813,-5.78322,-9.74623,-12.9862,-18.3394],'J/(mol*K)'),
        H298 = (404.751,'kJ/mol'),
        S298 = (-3.52414,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 42,
    label = "CJC=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.5,1.1,-0.4,-2.3,-6.1,-9.2,-14.4],'J/(mol*K)'),
        H298 = (402.4,'kJ/mol'),
        S298 = (-7.8,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 43,
    label = "C2JC=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D} {6,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.32,0.19,-0.15,-0.57,-1.43,-2.22,-3.67],'cal/(mol*K)'),
        H298 = (94.4,'kcal/mol'),
        S298 = (-1.16,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI""",
    longDesc = 
"""

""",
)

entry(
    index = 44,
    label = "Cs_S",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5,-2.33,-3.1,-3.39,-3.75,-4.45,-5.2],'cal/(mol*K)'),
        H298 = (98.45,'kcal/mol'),
        S298 = (4.44,'cal/(mol*K)'),
    ),
    shortDesc = """Generic secondary radical. (CHEN & BOZZELLI) #""",
    longDesc = 
"""

""",
)

entry(
    index = 45,
    label = "CCJCO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S} {5,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.9,-8.3,-10,-11.6,-14.5,-16.8,-20.3],'J/(mol*K)'),
        H298 = (416.9,'kJ/mol'),
        S298 = (13.8,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 46,
    label = "C=CCJCO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S} {5,S}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   O2s u0 {2,S}
6   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3,3.2,2.4,1,-1.8,-4.5,-9.8],'J/(mol*K)'),
        H298 = (335.4,'kJ/mol'),
        S298 = (-19.9,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 47,
    label = "C=CCJC(O)C=C",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {5,S}
2   Cs  u0 {1,S} {4,S} {6,S}
3   Cd  u0 {1,S} {8,D}
4   Cd  u0 {2,S} {7,D}
5   H   u0 {1,S}
6   O2s u0 {2,S}
7   C   u0 {4,D}
8   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.3,-4.5,-3,-2.8,-3.9,-5.6,-10.2],'J/(mol*K)'),
        H298 = (286.3,'kJ/mol'),
        S298 = (-9.6,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 48,
    label = "CCJCOOH",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   Cs  u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   O2s u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.65,-1.4,-2,-2.5,-3.27,-3.84,-4.73],'cal/(mol*K)'),
        H298 = (99.98,'kcal/mol'),
        S298 = (4.79,'cal/(mol*K)'),
    ),
    shortDesc = """WIJAYA et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 49,
    label = "CCJCC=O",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   C   u0 {1,S} {3,S}
3   CO  u0 {2,S} {6,D}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.9,-8.3,-10,-11.6,-14.5,-16.8,-20.3],'J/(mol*K)'),
        H298 = (416.9,'kJ/mol'),
        S298 = (13.8,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 50,
    label = "CCJC(C)=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {5,S}
2   Cd  u0 {1,S} {4,D}
3   C   u0 {1,S} {6,S}
4   Cdd u0 {2,D} {7,D}
5   H   u0 {1,S}
6   C   u0 {3,S}
7   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-4,-6.2,-7.9,-10.8,-12.9,-16.9],'J/(mol*K)'),
        H298 = (365.4,'kJ/mol'),
        S298 = (8.3,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 51,
    label = "(Cs)2CsJ",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = 'Cs_S',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 52,
    label = "cyclopentene-4",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {2,S} {4,D}
6   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Allyl_S""",
    longDesc = 
"""

""",
)

entry(
    index = 53,
    label = "bicyclo[2.1.1]hex-2-ene-C5",
    group = 
"""
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {7,S}
4   C  u0 {1,S} {2,S}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (104.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 54,
    label = "tricyclo[2.1.1.0(1,4)]hex-2-ene-C5",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {7,S}
4   C  u0 {1,S} {2,S}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (105.2,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 55,
    label = "bicyclo[2.1.0]pent-2-ene-C5",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {6,S}
4   Cd u0 {2,S} {5,D}
5   Cd u0 {1,S} {4,D}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (106.9,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 56,
    label = "bicyclo[1.1.1]pentane-C2",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {6,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (106.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 57,
    label = "tricyclo[1.1.1.0(1,3)]pentane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {6,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (111.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 58,
    label = "bicyclo[2.1.1]hexane-C5",
    group = 
"""
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {7,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {6,S}
6   C  u0 {1,S} {5,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (105.4,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 59,
    label = "tricyclo[2.1.1.0(1,4)]hexane-C5",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {7,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {6,S}
6   C  u0 {1,S} {5,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (103.4,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 60,
    label = "cyclopropane",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (106,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """D.F. McMillen, D.M. Golden, HYDROCARBON BOND-DISSOCIATION ENERGIES, Annual Review of Physical Chemistry, 33 (1982) 493-532.. S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 61,
    label = "spiro[2.2]pentane-secondary",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {3,S} {6,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {1,S} {4,S}
6   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (107.3,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 62,
    label = "tricyclo[2.2.1.0(1,4)]heptane-C7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S} {7,S}
2   Cs u0 {1,S} {3,S} {4,S} {6,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {2,S} {5,S}
5   C  u0 {1,S} {4,S}
6   C  u0 {2,S} {7,S}
7   C  u0 {1,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (106.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 63,
    label = "bicyclo[2.1.0]pentane-secondary-C3",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {6,S}
4   Cs u0 {2,S} {5,S}
5   Cs u0 {1,S} {4,S}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (105.9,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 64,
    label = "tricyclo[3.1.1.0(1,5)]heptane-C6",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   C  u0 {1,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 65,
    label = "bicyclo[1.1.0]butane-secondary",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {5,S}
4   Cs u0 {1,S} {2,S}
5   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 66,
    label = "bicyclo[3.1.0]hexane-C3",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {7,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {4,S} {5,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (108.3,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 68,
    label = "bicyclo[4.1.0]heptane-C3-7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {2,S} {6,S}
5   C  u0 {1,S} {7,S}
6   C  u0 {4,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (108.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 68,
    label = "bicyclo[4.1.0]heptane-C3-7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {2,S} {6,S}
5   C  u0 {1,S} {7,S}
6   C  u0 {4,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (108.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 69,
    label = "tricyclo[2.1.1.0(1,4)]hexane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {4,S} {5,S} {6,S}
3 * Cs u1 {1,S} {6,S} {7,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   Cs u0 {2,S} {3,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 70,
    label = "bicyclo[3.1.1]heptane-C6",
    group = 
"""
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   C  u0 {1,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (103,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 79,
    label = "tricyclo[2.2.1.0(1,4)]heptane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S} {7,S}
3 * Cs u1 {1,S} {5,S} {8,S}
4   C  u0 {1,S} {2,S}
5   Cs u0 {2,S} {3,S}
6   C  u0 {1,S} {7,S}
7   C  u0 {2,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 80,
    label = "bicyclo[4.2.0]octane-C4-7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {1,S} {4,S} {9,S}
4   Cs u0 {2,S} {3,S}
5   C  u0 {1,S} {8,S}
6   C  u0 {2,S} {7,S}
7   C  u0 {6,S} {8,S}
8   C  u0 {5,S} {7,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 73,
    label = "bicyclo[2.2.2]octane-C2",
    group = 
"""
1   Cs u0 {3,S} {5,S} {6,S}
2   Cs u0 {4,S} {7,S} {8,S}
3 * Cs u1 {1,S} {4,S} {9,S}
4   Cs u0 {2,S} {3,S}
5   C  u0 {1,S} {7,S}
6   C  u0 {1,S} {8,S}
7   C  u0 {2,S} {5,S}
8   C  u0 {2,S} {6,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 74,
    label = "tricyclo[2.2.2.0(1,4)]octane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S} {6,S}
2   Cs u0 {1,S} {4,S} {7,S} {8,S}
3 * Cs u1 {1,S} {4,S} {9,S}
4   Cs u0 {2,S} {3,S}
5   C  u0 {1,S} {7,S}
6   C  u0 {1,S} {8,S}
7   C  u0 {2,S} {5,S}
8   C  u0 {2,S} {6,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99.3,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 75,
    label = "cyclobutane",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.9,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Tian, Z.; Fattahi, A.; Lis, L.; Kass, S. R., "Cycloalkane and Cycloalkene C-H Bond Dissociation Energies," J. Am. Chem. Soc. 2006, 128, 17087-17092, DOI: 10.1021/ja065348u. S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 76,
    label = "bicyclo[2.1.0]pentane-secondary-C4",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cs u1 {1,S} {5,S} {6,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {2,S} {3,S}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 77,
    label = "bicyclo[2.2.0]hexane-secondary",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {1,S} {4,S} {7,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {2,S} {5,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 78,
    label = "bicyclo[3.2.0]heptane-C5-6",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {1,S} {4,S} {8,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 79,
    label = "tricyclo[2.2.1.0(1,4)]heptane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S} {7,S}
3 * Cs u1 {1,S} {5,S} {8,S}
4   C  u0 {1,S} {2,S}
5   Cs u0 {2,S} {3,S}
6   C  u0 {1,S} {7,S}
7   C  u0 {2,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 80,
    label = "bicyclo[4.2.0]octane-C4-7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {1,S} {4,S} {9,S}
4   Cs u0 {2,S} {3,S}
5   C  u0 {1,S} {8,S}
6   C  u0 {2,S} {7,S}
7   C  u0 {6,S} {8,S}
8   C  u0 {5,S} {7,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 81,
    label = "bicyclo[3.1.1]heptane-C2",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S}
2   Cs u0 {4,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   C  u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 82,
    label = "tricyclo[3.1.1.0(1,5)]heptane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {4,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   C  u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 83,
    label = "bicyclo[3.1.0]hexane-C5-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cs u1 {1,S} {6,S} {7,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {2,S} {6,S}
6   Cs u0 {3,S} {5,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (93.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 84,
    label = "bicyclo[3.1.0]hexane-C5-3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S} {7,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {5,S} {6,S} {8,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {1,S} {3,S}
6   Cs u0 {2,S} {3,S}
7   H  u0 {1,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (94.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 85,
    label = "bicyclo[2.1.1]hexane-C2",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S}
2   Cs u0 {4,S} {5,S} {6,S}
3 * Cs u1 {1,S} {6,S} {7,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   Cs u0 {2,S} {3,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 86,
    label = "7-norbornyl",
    group = 
"""
1   Cs u0 {3,S} {4,S} {7,S}
2   Cs u0 {3,S} {5,S} {6,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {2,S} {4,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {1,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """P.M. Nunes, S.G. Estacio, G.T. Lopes, B.J. Costa Cabral, R.M. Borges dos Santos, J.A. Martinho Simoes, CH Bond Dissociation Enthalpies in Norbornane. An Experimental and Computational Study, Organic Letters, 10 (2008) 1613-1616. S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 87,
    label = "2-norbornyl",
    group = 
"""
1   Cs u0 {2,S} {4,S} {6,S} {8,S}
2 * Cs u1 {1,S} {5,S} {9,S}
3   Cs u0 {4,S} {5,S} {7,S}
4   Cs u0 {1,S} {3,S}
5   Cs u0 {2,S} {3,S}
6   Cs u0 {1,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {1,S}
9   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (105.02,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """P.M. Nunes, S.G. Estacio, G.T. Lopes, B.J. Costa Cabral, R.M. Borges dos Santos, J.A. Martinho Simoes, CH Bond Dissociation Enthalpies in Norbornane. An Experimental and Computational Study, Organic Letters, 10 (2008) 1613-1616. S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 94,
    label = "bicyclo[4.1.0]heptane-C6-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cs u1 {1,S} {6,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   Cs u0 {3,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (94.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 90,
    label = "bicyclo[4.1.0]heptane-C6-3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {5,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   Cs u0 {1,S} {3,S}
6   C  u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 90,
    label = "bicyclo[4.1.0]heptane-C6-3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {5,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   Cs u0 {1,S} {3,S}
6   C  u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 91,
    label = "cycloheptane",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {8,S}
2   Cs u0 {1,S} {4,S}
3   Cs u0 {1,S} {5,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {3,S} {7,S}
6   Cs u0 {4,S} {7,S}
7   Cs u0 {5,S} {6,S}
8   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (92.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 92,
    label = "bicyclo[3.2.0]heptane-C5-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {8,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {2,S} {4,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.9,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 93,
    label = "bicyclo[3.2.0]heptane-C5-3",
    group = 
"""
1   Cs u0 {2,S} {5,S} {6,S}
2   Cs u0 {1,S} {4,S} {7,S}
3 * Cs u1 {4,S} {5,S} {8,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {1,S} {3,S}
6   Cs u0 {1,S} {7,S}
7   Cs u0 {2,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 94,
    label = "bicyclo[4.1.0]heptane-C6-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cs u1 {1,S} {6,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   Cs u0 {3,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (94.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 95,
    label = "bicyclo[3.1.1]heptane-C3",
    group = 
"""
1   Cs u0 {4,S} {5,S} {7,S}
2   Cs u0 {4,S} {5,S} {6,S}
3 * Cs u1 {6,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   Cs u0 {2,S} {3,S}
7   Cs u0 {1,S} {3,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.3,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 96,
    label = "tricyclo[3.1.1.0(1,5)]heptane-C3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S} {7,S}
2   Cs u0 {1,S} {4,S} {5,S} {6,S}
3 * Cs u1 {6,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   Cs u0 {2,S} {3,S}
7   Cs u0 {1,S} {3,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 97,
    label = "octahydro-pentalene-C5-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {9,S}
4   C  u0 {1,S} {8,S}
5   C  u0 {2,S} {7,S}
6   C  u0 {2,S} {8,S}
7   Cs u0 {3,S} {5,S}
8   C  u0 {4,S} {6,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 98,
    label = "octahydro-pentalene-C5-3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {6,S}
2   Cs u0 {1,S} {5,S} {7,S}
3 * Cs u1 {4,S} {5,S} {9,S}
4   Cs u0 {1,S} {3,S}
5   Cs u0 {2,S} {3,S}
6   C  u0 {1,S} {8,S}
7   C  u0 {2,S} {8,S}
8   C  u0 {6,S} {7,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 99,
    label = "bicyclo[4.2.0]octane-C6-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {9,S}
4   C  u0 {1,S} {5,S}
5   C  u0 {2,S} {4,S}
6   C  u0 {2,S} {8,S}
7   Cs u0 {3,S} {8,S}
8   C  u0 {6,S} {7,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 100,
    label = "bicyclo[4.2.0]octane-C6-3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {6,S}
2   Cs u0 {1,S} {5,S} {7,S}
3 * Cs u1 {4,S} {8,S} {9,S}
4   Cs u0 {1,S} {3,S}
5   C  u0 {2,S} {6,S}
6   C  u0 {1,S} {5,S}
7   C  u0 {2,S} {8,S}
8   Cs u0 {3,S} {7,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 101,
    label = "CCJC",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cs u0 {3,S} {7,S} {8,S} {9,S}
3  * Cs u1 {1,S} {2,S} {10,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    H  u0 {2,S}
9    H  u0 {2,S}
10   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.45,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 102,
    label = "RCCJC",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cs u0 {3,S} {7,S} {8,S} {9,S}
3  * Cs u1 {1,S} {2,S} {10,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    H  u0 {2,S}
9    H  u0 {2,S}
10   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-2.77,-3.49,-3.9,-4.35,-4.64,-4.64],'cal/(mol*K)'),
        H298 = (98.45,'kcal/mol'),
        S298 = (5.13,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 103,
    label = "RCCJCC",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cs u0 {3,S} {7,S} {8,S} {9,S}
3  * Cs u1 {1,S} {2,S} {10,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    C  u0 {2,S}
8    H  u0 {2,S}
9    H  u0 {2,S}
10   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71,-3.14,-3.92,-4.33,-4.71,-4.92,-4.92],'cal/(mol*K)'),
        H298 = (98.45,'kcal/mol'),
        S298 = (4.9,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 104,
    label = "cyclopentane",
    group = 
"""
1    Cs u0 {3,S} {4,S} {6,S} {7,S}
2    Cs u0 {3,S} {5,S} {8,S} {9,S}
3  * Cs u1 {1,S} {2,S} {10,S}
4    C  u0 {1,S} {5,S}
5    C  u0 {2,S} {4,S}
6    H  u0 {1,S}
7    H  u0 {1,S}
8    H  u0 {2,S}
9    H  u0 {2,S}
10   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71,-3.14,-3.92,-4.33,-4.71,-4.92,-4.92],'cal/(mol*K)'),
        H298 = (96.4,'kcal/mol'),
        S298 = (4.9,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from RCCJCC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 105,
    label = "cyclohexane",
    group = 
"""
1    Cs u0 {3,S} {4,S} {7,S} {8,S}
2    Cs u0 {3,S} {5,S} {9,S} {10,S}
3  * Cs u1 {1,S} {2,S} {11,S}
4    C  u0 {1,S} {6,S}
5    C  u0 {2,S} {6,S}
6    C  u0 {4,S} {5,S}
7    H  u0 {1,S}
8    H  u0 {1,S}
9    H  u0 {2,S}
10   H  u0 {2,S}
11   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71,-3.14,-3.92,-4.33,-4.71,-4.92,-4.92],'cal/(mol*K)'),
        H298 = (95.5,'kcal/mol'),
        S298 = (4.9,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from RCCJCC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 106,
    label = "Benzyl_S",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0448,-1.3002,-2.199,-2.5546,-2.5872,-2.8074,-5.6336],'cal/(mol*K)'),
        H298 = (88.064,'kcal/mol','+|-',2.4),
        S298 = (-4.8554,'cal/(mol*K)'),
    ),
    shortDesc = """Fitted From Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 7/2017, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C[CH]C1C=CC=CC=1
CC[CH]C1C=CC=CC=1
CCC[CH]C1C=CC=CC=1
CCCC[CH]C1C=CC=CC=1
CCCCC[CH]C1C=CC=CC=1
""",
)

entry(
    index = 107,
    label = "Indenyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cb u0 {1,S} {4,B}
3   Cd u0 {1,S} {5,D}
4   Cb u0 {2,B} {5,S}
5   Cd u0 {3,D} {4,S}
6   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.36,-0.72,-1.23,-1.77,-2.7,-3.43,-4.54],'cal/(mol*K)'),
        H298 = (81.62,'kcal/mol'),
        S298 = (0.69,'cal/(mol*K)'),
    ),
    shortDesc = """A.G. Vandeputte CBS-QB3""",
    longDesc = 
"""

""",
)

entry(
    index = 108,
    label = "Benzyl_S_Fused5",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cb u0 {1,S} {4,B}
3   C  u0 {1,S} {5,[S,D,T]}
4   Cb u0 {2,B} {5,S}
5   C  u0 {3,[S,D,T]} {4,S}
6   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.054016,-0.57486,-1.16181,-1.58687,-2.40332,-3.15038,-4.41676],'cal/(mol*K)','+|-',[0.20119,0.20119,0.20119,0.20119,0.20119,0.20119,0.20119]),
        H298 = (88.5038,'kcal/mol','+|-',0.737851),
        S298 = (3.11253,'cal/(mol*K)','+|-',0.434935),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C1=CC=C2CC[CH]C2=C1
CC1C[CH]C2=CC=CC=C21
CCC1C[CH]C2=CC=CC=C21
CCCC1C[CH]C2=CC=CC=C21
""",
)

entry(
    index = 109,
    label = "Benzyl_S_Fused6",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cb u0 {1,S} {4,B}
3   C  u0 {1,S} {5,[S,D,T,B]}
4   Cb u0 {2,B} {6,S}
5   C  u0 {3,[S,D,T,B]} {6,[S,D,T,B]}
6   C  u0 {4,S} {5,[S,D,T,B]}
7   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.881557,-1.19162,-1.64981,-2.00346,-2.50574,-3.09492,-4.34126],'cal/(mol*K)','+|-',[0.318445,0.318445,0.318445,0.318445,0.318445,0.318445,0.318445]),
        H298 = (86.3797,'kcal/mol','+|-',1.14843),
        S298 = (1.33063,'cal/(mol*K)','+|-',0.744626),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C1=CC=C2CCC[CH]C2=C1
CC1CC[CH]C2=CC=CC=C21
CCC1CC[CH]C2=CC=CC=C21
""",
)

entry(
    index = 110,
    label = "Benzyl_S_dihydronaphthalene",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cb u0 {1,S} {4,B}
3   C  u0 {1,S} {5,[S,D,B]}
4   Cb u0 {2,B} {6,S}
5   Cd u0 {3,[S,D,B]} {6,D}
6   Cd u0 {4,S} {5,D}
7   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.762975,-1.09193,-1.45447,-1.90836,-2.74844,-3.44654,-4.57653],'cal/(mol*K)','+|-',[0.226952,0.226952,0.226952,0.226952,0.226952,0.226952,0.226952]),
        H298 = (83.6682,'kcal/mol','+|-',0.869131),
        S298 = (1.4331,'cal/(mol*K)','+|-',0.350884),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 07/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2C=CC[CH]C2=C1
CC1=CC[CH]C2=CC=CC=C12
CCC1=CC[CH]C2=CC=CC=C12

Modified 10/2019 by Max Liu. Added enthalpy of H atom so that GAV predicted
enthalpy for C1=CC=C2C=CC[CH]C2=C1 matches calculated value.
""",
)

entry(
    index = 111,
    label = "Benzyl_S_Fused7",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {8,S}
2   Cb u0 {1,S} {4,B}
3   C  u0 {1,S} {5,[S,D,T,B]}
4   Cb u0 {2,B} {6,S}
5   C  u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
6   C  u0 {4,S} {7,[S,D,T,B]}
7   C  u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
8   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.42,-1.64,-1.86,-2.18,-2.74,-3.34,-4.5],'cal/(mol*K)','+|-',[1.4792,1.4792,1.4792,1.4792,1.4792,1.4792,1.4792]),
        H298 = (92.1,'kcal/mol','+|-',5.4578),
        S298 = (4.72,'cal/(mol*K)','+|-',4.205),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 04/2019, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds include:
C1=CC=C2CCCC[CH]C2=C1
""",
)

entry(
    index = 112,
    label = "Allyl_S",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (85.6,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 113,
    label = "Aromatic_pi_S_1_3",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cd u0 {1,S} {4,D}
3   Cs u0 {1,S} {5,S}
4   Cd u0 {2,D} {6,S}
5   Cd u0 {3,S} {6,D}
6   Cd u0 {4,S} {5,D}
7   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.013276,-1.28931,-2.31258,-2.92159,-3.39846,-3.6762,-4.8642],'cal/(mol*K)','+|-',[0.023461,0.023461,0.023461,0.023461,0.023461,0.023461,0.023461]),
        H298 = (75.4692,'kcal/mol','+|-',0.139824),
        S298 = (1.48461,'cal/(mol*K)','+|-',0.036353),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CC1=CC=C[CH]C1
CC1[CH]CC=CC=1
CC1C=CC[CH]C=1
CC1[CH]C=CC=C1
""",
)

entry(
    index = 114,
    label = "Aromatic_pi_S_(CH3_CH3_Ortho)_1_3",
    group = 
"""
1   Cs u0 {2,S} {3,S} {7,S}
2 * Cs u1 {1,S} {4,S} {8,S}
3   Cd u0 {1,S} {5,D} {9,S}
4   Cd u0 {2,S} {6,D}
5   Cd u0 {3,D} {6,S}
6   Cd u0 {4,D} {5,S}
7   C  u0 {1,S}
8   H  u0 {2,S}
9   C  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.104911,-1.14065,-2.32405,-3.03895,-3.75201,-4.05481,-5.14193],'cal/(mol*K)','+|-',[0.061305,0.061305,0.061305,0.061305,0.061305,0.061305,0.061305]),
        H298 = (75.5447,'kcal/mol','+|-',0.399656),
        S298 = (2.79083,'cal/(mol*K)','+|-',0.079011),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CC1=CC=C[CH]C1C
CC1[CH]C(C)C=CC=1
CC1C=CC(C)[CH]C=1
CC1(C)[CH]C=CC=C1
""",
)

entry(
    index = 115,
    label = "Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3",
    group = 
"""
1    Cs u0 {2,S} {3,S} {7,S}
2  * Cs u1 {1,S} {4,S} {8,S}
3    Cd u0 {1,S} {5,D} {9,S}
4    Cd u0 {2,S} {6,D}
5    Cd u0 {3,D} {6,S}
6    Cd u0 {4,D} {5,S}
7    C  u0 {1,S} {10,S}
8    H  u0 {2,S}
9    C  u0 {3,S}
10   C  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.453462,-1.20244,-2.43607,-2.95615,-3.47107,-3.9488,-5.03407],'cal/(mol*K)','+|-',[0.068504,0.068504,0.068504,0.068504,0.068504,0.068504,0.068504]),
        H298 = (74.982,'kcal/mol','+|-',0.417781),
        S298 = (1.24362,'cal/(mol*K)','+|-',0.106961),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CCC1[CH]C=CC=C1C
CCC1[CH]C(C)=CC=C1
CCC1[CH]C=C(C)C=C1
CCC1(C)[CH]C=CC=C1
""",
)

entry(
    index = 116,
    label = "Aromatic_pi_S_(fused5)_1_3",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D} {6,S}
3  * Cs u1 {1,S} {7,S} {10,S}
4    C  u0 {1,S} {9,S}
5    Cd u0 {2,D} {8,S}
6    C  u0 {2,S} {9,S}
7    Cd u0 {3,S} {8,D}
8    Cd u0 {5,S} {7,D}
9    C  u0 {4,S} {6,S}
10   H  u0 {3,S}
""",
    thermo = 'Aromatic_pi_S_(fused5)_1_4',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCC2[CH]1
CC1CCC2=CC=C[CH]C21
CCC1CCC2=CC=C[CH]C21
CCCC1CCC2=CC=C[CH]C21
C1=CC=C2CCCCC2[CH]1
CC1CCCC2=CC=C[CH]C21
CCC1CCCC2=CC=C[CH]C21
""",
)

entry(
    index = 117,
    label = "Aromatic_pi_S_(fused6)_1_3",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D} {6,S}
3  * Cs u1 {1,S} {7,S} {11,S}
4    C  u0 {1,S} {9,S}
5    Cd u0 {2,D} {8,S}
6    C  u0 {2,S} {10,S}
7    Cd u0 {3,S} {8,D}
8    Cd u0 {5,S} {7,D}
9    C  u0 {4,S} {10,S}
10   C  u0 {6,S} {9,S}
11   H  u0 {3,S}
""",
    thermo = 'Aromatic_pi_S_(fused5)_1_4',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCC2[CH]1
CC1CCC2=CC=C[CH]C21
CCC1CCC2=CC=C[CH]C21
CCCC1CCC2=CC=C[CH]C21
C1=CC=C2CCCCC2[CH]1
CC1CCCC2=CC=C[CH]C21
CCC1CCCC2=CC=C[CH]C21
""",
)

entry(
    index = 118,
    label = "Aromatic_pi_S_(fused7)_1_3",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D} {6,S}
3  * Cs u1 {1,S} {7,S} {12,S}
4    C  u0 {1,S} {9,S}
5    Cd u0 {2,D} {8,S}
6    C  u0 {2,S} {10,S}
7    Cd u0 {3,S} {8,D}
8    Cd u0 {5,S} {7,D}
9    C  u0 {4,S} {11,S}
10   C  u0 {6,S} {11,S}
11   C  u0 {9,S} {10,S}
12   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.084287,-0.439484,-1.00984,-1.6168,-2.48415,-3.29208,-4.57923],'cal/(mol*K)','+|-',[1.08001,1.08001,1.08001,1.08001,1.08001,1.08001,1.08001]),
        H298 = (76.4252,'kcal/mol','+|-',4.19016),
        S298 = (0.527688,'cal/(mol*K)','+|-',2.02975),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 04/2019, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds include:
C1=CC=C2CCCCCC2[CH]1
C1=CC=C2CCCCC(C)C2[CH]1
""",
)

entry(
    index = 119,
    label = "Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3",
    group = 
"""
1    Cs u0 {2,S} {3,S} {5,S}
2  * Cs u1 {1,S} {6,S} {14,S}
3    Cd u0 {1,S} {7,D} {15,S}
4    Cb u0 {5,S} {8,B} {9,B}
5    C  u0 {1,S} {4,S}
6    Cd u0 {2,S} {10,D}
7    Cd u0 {3,D} {10,S}
8    Cb u0 {4,B} {11,B}
9    Cb u0 {4,B} {12,B}
10   Cd u0 {6,D} {7,S}
11   Cb u0 {8,B} {13,B}
12   Cb u0 {9,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   H  u0 {2,S}
15   C  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.831072,-0.828879,-1.89888,-2.14323,-2.47359,-2.80572,-3.59479],'cal/(mol*K)','+|-',[0.208059,0.208059,0.208059,0.208059,0.208059,0.208059,0.208059]),
        H298 = (74.1331,'kcal/mol','+|-',0.742606),
        S298 = (-0.854817,'cal/(mol*K)','+|-',0.322012),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
""",
)

entry(
    index = 120,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S}
2    Cs u0 {1,S} {3,S} {14,S}
3    Cb u0 {2,S} {6,B} {7,B}
4  * Cs u1 {1,S} {8,S} {15,S}
5    Cd u0 {1,S} {9,D} {16,S}
6    Cb u0 {3,B} {11,B}
7    Cb u0 {3,B} {12,B}
8    Cd u0 {4,S} {10,D}
9    Cd u0 {5,D} {10,S}
10   Cd u0 {8,D} {9,S}
11   Cb u0 {6,B} {13,B}
12   Cb u0 {7,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {2,S}
15   H  u0 {4,S}
16   C  u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.67718,-0.360591,-1.61836,-2.06586,-2.45313,-2.74791,-3.50658],'cal/(mol*K)','+|-',[0.245046,0.245046,0.245046,0.245046,0.245046,0.245046,0.245046]),
        H298 = (74.3294,'kcal/mol','+|-',0.850906),
        S298 = (-3.58784,'cal/(mol*K)','+|-',0.338262),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
""",
)

entry(
    index = 121,
    label = "Aromatic_pi_S_(CH3_CH3_Meta)_1_3_1",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cd u0 {1,S} {4,D} {8,S}
3   Cs u0 {1,S} {5,S} {9,S}
4   Cd u0 {2,D} {6,S}
5   Cd u0 {3,S} {6,D}
6   Cd u0 {4,S} {5,D}
7   H  u0 {1,S}
8   C  u0 {2,S}
9   C  u0 {3,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 122,
    label = "Aromatic_pi_S_(CH3_C2H5_Meta)_1_3_1",
    group = 
"""
1  * Cs u1 {2,S} {3,S} {8,S}
2    Cs u0 {1,S} {4,S} {7,S}
3    Cd u0 {1,S} {5,D} {9,S}
4    Cd u0 {2,S} {6,D}
5    Cd u0 {3,D} {6,S}
6    Cd u0 {4,D} {5,S}
7    C  u0 {2,S} {10,S}
8    H  u0 {1,S}
9    C  u0 {3,S}
10   C  u0 {7,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 123,
    label = "Aromatic_pi_S_(CH3_Benzyl_Meta)_1_3_1",
    group = 
"""
1    Cs u0 {2,S} {5,S} {6,S}
2  * Cs u1 {1,S} {4,S} {14,S}
3    Cb u0 {5,S} {8,B} {9,B}
4    Cd u0 {2,S} {7,D} {15,S}
5    C  u0 {1,S} {3,S}
6    Cd u0 {1,S} {10,D}
7    Cd u0 {4,D} {10,S}
8    Cb u0 {3,B} {11,B}
9    Cb u0 {3,B} {12,B}
10   Cd u0 {6,D} {7,S}
11   Cb u0 {8,B} {13,B}
12   Cb u0 {9,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   H  u0 {2,S}
15   C  u0 {4,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 124,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_3_1",
    group = 
"""
1    Cs u0 {2,S} {3,S} {6,S}
2    Cs u0 {1,S} {4,S} {15,S}
3  * Cs u1 {1,S} {5,S} {14,S}
4    Cb u0 {2,S} {7,B} {8,B}
5    Cd u0 {3,S} {9,D} {16,S}
6    Cd u0 {1,S} {10,D}
7    Cb u0 {4,B} {11,B}
8    Cb u0 {4,B} {12,B}
9    Cd u0 {5,D} {10,S}
10   Cd u0 {6,D} {9,S}
11   Cb u0 {7,B} {13,B}
12   Cb u0 {8,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   H  u0 {3,S}
15   C  u0 {2,S}
16   C  u0 {5,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 125,
    label = "Aromatic_pi_S_(CH3_CH3_Meta)_1_3_2",
    group = 
"""
1   Cs u0 {2,S} {4,S} {8,S}
2 * Cs u1 {1,S} {5,S} {7,S}
3   Cd u0 {4,D} {6,S} {9,S}
4   Cd u0 {1,S} {3,D}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {3,S} {5,D}
7   H  u0 {2,S}
8   C  u0 {1,S}
9   C  u0 {3,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 126,
    label = "Aromatic_pi_S_(CH3_C2H5_Meta)_1_3_2",
    group = 
"""
1    Cs u0 {2,S} {4,S} {7,S}
2  * Cs u1 {1,S} {5,S} {8,S}
3    Cd u0 {4,D} {6,S} {9,S}
4    Cd u0 {1,S} {3,D}
5    Cd u0 {2,S} {6,D}
6    Cd u0 {3,S} {5,D}
7    C  u0 {1,S} {10,S}
8    H  u0 {2,S}
9    C  u0 {3,S}
10   C  u0 {7,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 127,
    label = "Aromatic_pi_S_(CH3_Benzyl_Meta)_1_3_2",
    group = 
"""
1    Cs u0 {3,S} {5,S} {6,S}
2    Cb u0 {5,S} {9,B} {10,B}
3  * Cs u1 {1,S} {7,S} {14,S}
4    Cd u0 {6,D} {8,S} {15,S}
5    C  u0 {1,S} {2,S}
6    Cd u0 {1,S} {4,D}
7    Cd u0 {3,S} {8,D}
8    Cd u0 {4,S} {7,D}
9    Cb u0 {2,B} {11,B}
10   Cb u0 {2,B} {12,B}
11   Cb u0 {9,B} {13,B}
12   Cb u0 {10,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   H  u0 {3,S}
15   C  u0 {4,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 128,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_3_2",
    group = 
"""
1    Cs u0 {2,S} {4,S} {6,S}
2    Cs u0 {1,S} {3,S} {14,S}
3    Cb u0 {2,S} {8,B} {9,B}
4  * Cs u1 {1,S} {7,S} {15,S}
5    Cd u0 {6,D} {10,S} {16,S}
6    Cd u0 {1,S} {5,D}
7    Cd u0 {4,S} {10,D}
8    Cb u0 {3,B} {11,B}
9    Cb u0 {3,B} {12,B}
10   Cd u0 {5,S} {7,D}
11   Cb u0 {8,B} {13,B}
12   Cb u0 {9,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {2,S}
15   H  u0 {4,S}
16   C  u0 {5,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 129,
    label = "Aromatic_pi_S_(CH3_CH3_Para)_1_3",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {7,S}
2   Cs u0 {1,S} {5,S} {8,S}
3   Cd u0 {4,D} {6,S} {9,S}
4   Cd u0 {1,S} {3,D}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {3,S} {5,D}
7   H  u0 {1,S}
8   C  u0 {2,S}
9   C  u0 {3,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 130,
    label = "Aromatic_pi_S_(CH3_C2H5_Para)_1_3",
    group = 
"""
1    Cs u0 {2,S} {5,S} {7,S}
2  * Cs u1 {1,S} {4,S} {8,S}
3    Cd u0 {4,D} {6,S} {9,S}
4    Cd u0 {2,S} {3,D}
5    Cd u0 {1,S} {6,D}
6    Cd u0 {3,S} {5,D}
7    C  u0 {1,S} {10,S}
8    H  u0 {2,S}
9    C  u0 {3,S}
10   C  u0 {7,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 131,
    label = "Aromatic_pi_S_(CH3_Benzyl_Para)_1_3",
    group = 
"""
1    Cs u0 {2,S} {5,S} {7,S}
2  * Cs u1 {1,S} {6,S} {14,S}
3    Cb u0 {5,S} {9,B} {10,B}
4    Cd u0 {6,D} {8,S} {15,S}
5    C  u0 {1,S} {3,S}
6    Cd u0 {2,S} {4,D}
7    Cd u0 {1,S} {8,D}
8    Cd u0 {4,S} {7,D}
9    Cb u0 {3,B} {11,B}
10   Cb u0 {3,B} {12,B}
11   Cb u0 {9,B} {13,B}
12   Cb u0 {10,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   H  u0 {2,S}
15   C  u0 {4,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 132,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Para)_1_3",
    group = 
"""
1    Cs u0 {2,S} {4,S} {7,S}
2    Cs u0 {1,S} {3,S} {14,S}
3    Cb u0 {2,S} {8,B} {9,B}
4  * Cs u1 {1,S} {6,S} {15,S}
5    Cd u0 {6,D} {10,S} {16,S}
6    Cd u0 {4,S} {5,D}
7    Cd u0 {1,S} {10,D}
8    Cb u0 {3,B} {11,B}
9    Cb u0 {3,B} {12,B}
10   Cd u0 {5,S} {7,D}
11   Cb u0 {8,B} {13,B}
12   Cb u0 {9,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {2,S}
15   H  u0 {4,S}
16   C  u0 {5,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 133,
    label = "Aromatic_pi_S_(CH3_CH3_Sub)_1_3",
    group = 
"""
1   Cs u0 {2,S} {3,S} {7,S} {8,S}
2 * Cs u1 {1,S} {4,S} {9,S}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {2,S} {6,D}
5   Cd u0 {3,D} {6,S}
6   Cd u0 {4,D} {5,S}
7   C  u0 {1,S}
8   C  u0 {1,S}
9   H  u0 {2,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 134,
    label = "Aromatic_pi_S_(s1_3_6_diene_1_4)_1_3",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {9,S}
3   C  u0 {1,S} {4,S}
4   C  u0 {1,S} {3,S}
5   Cd u0 {1,S} {7,D}
6   Cd u0 {2,S} {8,D}
7   Cd u0 {5,D} {8,S}
8   Cd u0 {6,D} {7,S}
9   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.48192,0.127981,-0.882314,-1.47156,-2.2164,-3.23195,-4.40182],'cal/(mol*K)','+|-',[0.7049,0.7049,0.7049,0.7049,0.7049,0.7049,0.7049]),
        H298 = (70.66,'kcal/mol','+|-',4.28202),
        S298 = (-1.77936,'cal/(mol*K)','+|-',1.91485),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CCCCC1CC12C=C[CH]C=C2
""",
)

entry(
    index = 135,
    label = "Aromatic_pi_S_(CH3_C2H5_Sub)_1_3",
    group = 
"""
1    Cs u0 {2,S} {3,S} {5,S} {8,S}
2  * Cs u1 {1,S} {4,S} {9,S}
3    Cd u0 {1,S} {6,D}
4    Cd u0 {2,S} {7,D}
5    C  u0 {1,S} {10,S}
6    Cd u0 {3,D} {7,S}
7    Cd u0 {4,D} {6,S}
8    C  u0 {1,S}
9    H  u0 {2,S}
10   C  u0 {5,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 136,
    label = "Aromatic_pi_S_(s1_4_6_diene_1_4)_1_3",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2  * Cs u1 {1,S} {6,S} {10,S}
3    Cd u0 {1,S} {8,D}
4    C  u0 {1,S} {7,S}
5    C  u0 {1,S} {7,S}
6    Cd u0 {2,S} {9,D}
7    C  u0 {4,S} {5,S}
8    Cd u0 {3,D} {9,S}
9    Cd u0 {6,D} {8,S}
10   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.85011,2.02306,1.41734,0.955199,-0.252841,-1.61161,-3.21428],'cal/(mol*K)','+|-',[0.733897,0.733897,0.733897,0.733897,0.733897,0.733897,0.733897]),
        H298 = (72.4956,'kcal/mol','+|-',4.45566),
        S298 = (2.72,'cal/(mol*K)','+|-',2.01098),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CCCC1CCC12C=C[CH]C=C2
""",
)

entry(
    index = 137,
    label = "Aromatic_pi_S_(s1_5_6_diene_1_4)_1_3",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2  * Cs u1 {1,S} {6,S} {11,S}
3    Cd u0 {1,S} {7,D}
4    C  u0 {1,S} {9,S}
5    C  u0 {1,S} {8,S}
6    Cd u0 {2,S} {10,D}
7    Cd u0 {3,D} {10,S}
8    C  u0 {5,S} {9,S}
9    C  u0 {4,S} {8,S}
10   Cd u0 {6,D} {7,S}
11   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.344733,-0.12429,-0.432103,-0.924571,-2.30122,-3.16695,-4.31502],'cal/(mol*K)','+|-',[0.781339,0.781339,0.781339,0.781339,0.781339,0.781339,0.781339]),
        H298 = (73.496,'kcal/mol','+|-',4.73954),
        S298 = (-3.2868,'cal/(mol*K)','+|-',2.17587),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CCC1CCCC12C=C[CH]C=C2
""",
)

entry(
    index = 138,
    label = "Aromatic_pi_S_(s1_6_6_diene_1_4)_1_3",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2  * Cs u1 {1,S} {6,S} {12,S}
3    Cd u0 {1,S} {7,D}
4    C  u0 {1,S} {9,S}
5    C  u0 {1,S} {8,S}
6    Cd u0 {2,S} {10,D}
7    Cd u0 {3,D} {10,S}
8    C  u0 {5,S} {11,S}
9    C  u0 {4,S} {11,S}
10   Cd u0 {6,D} {7,S}
11   C  u0 {8,S} {9,S}
12   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.226242,-0.404788,-1.08177,-1.65237,-2.56959,-3.27321,-4.6477],'cal/(mol*K)','+|-',[0.872202,0.872202,0.872202,0.872202,0.872202,0.872202,0.872202]),
        H298 = (74.0097,'kcal/mol','+|-',5.28577),
        S298 = (-1.20585,'cal/(mol*K)','+|-',2.5221),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CC1CCCCC12C=C[CH]C=C2
""",
)

entry(
    index = 139,
    label = "Aromatic_pi_S_(CH3_Benzyl_Sub)_1_3",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {14,S}
2  * Cs u1 {1,S} {6,S} {15,S}
3    Cb u0 {4,S} {7,B} {8,B}
4    C  u0 {1,S} {3,S}
5    Cd u0 {1,S} {9,D}
6    Cd u0 {2,S} {10,D}
7    Cb u0 {3,B} {11,B}
8    Cb u0 {3,B} {12,B}
9    Cd u0 {5,D} {10,S}
10   Cd u0 {6,D} {9,S}
11   Cb u0 {7,B} {13,B}
12   Cb u0 {8,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {1,S}
15   H  u0 {2,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 140,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Sub)_1_3",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {14,S}
2    Cs u0 {1,S} {3,S} {15,S}
3    Cb u0 {2,S} {7,B} {8,B}
4  * Cs u1 {1,S} {6,S} {16,S}
5    Cd u0 {1,S} {9,D}
6    Cd u0 {4,S} {10,D}
7    Cb u0 {3,B} {11,B}
8    Cb u0 {3,B} {12,B}
9    Cd u0 {5,D} {10,S}
10   Cd u0 {6,D} {9,S}
11   Cb u0 {7,B} {13,B}
12   Cb u0 {8,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {1,S}
15   C  u0 {2,S}
16   H  u0 {4,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 141,
    label = "CJ-Cd-Benzene",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cd u0 {1,S} {4,D}
3   Cs u0 {1,S} {5,S}
4   Cd u0 {2,D} {6,S}
5   Cb u0 {3,S} {6,B}
6   Cb u0 {4,S} {5,B}
7   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.038694,-0.486795,-1.26614,-1.94355,-2.84643,-3.50953,-4.60995],'cal/(mol*K)','+|-',[0.244001,0.244001,0.244001,0.244001,0.244001,0.244001,0.244001]),
        H298 = (80.0557,'kcal/mol','+|-',0.913362),
        S298 = (1.93251,'cal/(mol*K)','+|-',0.367823),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C1=CC=C2C=C[CH]CC2=C1
CC1[CH]C=CC2=CC=CC=C12
CC1=C[CH]CC2=CC=CC=C12
CCC1[CH]C=CC2=CC=CC=C12
CCC1=C[CH]CC2=CC=CC=C12
""",
)

entry(
    index = 142,
    label = "CJ-Cd-Benzene7",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {8,S}
2   Cd u0 {1,S} {4,D}
3   Cs u0 {1,S} {5,S}
4   Cd u0 {2,D} {6,S}
5   Cs u0 {3,S} {7,S}
6   Cb u0 {4,S} {7,B}
7   Cb u0 {5,S} {6,B}
8   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.3,-0.5,-1,-1.5,-2.5,-3.3,-4.5],'cal/(mol*K)','+|-',[2.4642,2.4642,2.4642,2.4642,2.4642,2.4642,2.4642]),
        H298 = (80.7,'kcal/mol','+|-',7.3256),
        S298 = (1,'cal/(mol*K)','+|-',3.8642),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 04/2019, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds include:
C1=CC=C2CC[CH]C=CC2=C1
""",
)

entry(
    index = 143,
    label = "cyclobutene-allyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S}
3   Cd u0 {1,S} {4,D}
4   Cd u0 {2,S} {3,D}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (91.2,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = """Tian, Z.; Fattahi, A.; Lis, L.; Kass, S. R., "Cycloalkane and Cycloalkene C-H Bond Dissociation Energies," J. Am. Chem. Soc. 2006, 128, 17087-17092, DOI: 10.1021/ja065348u S, Cp copied from Allyl_S""",
    longDesc = 
"""

""",
)

entry(
    index = 144,
    label = "cyclopentene-allyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S}
3   Cd u0 {1,S} {5,D}
4   C  u0 {2,S} {5,S}
5   Cd u0 {3,D} {4,S}
6   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (82.3,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = """Furuyama, S.; Golden, D. M.; Benson, S. W., "Kinetic Study of the Gas-Phase Reaction c-C5H8+I2 c-C5H6+2HI. Heat of Formation and the Stabilization Energy of the Cyclopentenyl Radical,"Int. J. Chem. Kinet. 1970, 2, 93-99. S, Cp copied from Allyl_S""",
    longDesc = 
"""

""",
)

entry(
    index = 145,
    label = "cyclohexene-allyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cs u0 {1,S} {4,S}
3   Cd u0 {1,S} {5,D}
4   C  u0 {2,S} {6,S}
5   Cd u0 {3,D} {6,S}
6   C  u0 {4,S} {5,S}
7   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (85,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = """Alfassi, Z. B.; Feldman, L., "The Kinetics of Radiation-Induced Hydrogen Abstraction by Trichloromethyl Radicals in the Liquid Phase: Cyclohexene," Int. J. Chem. Kinet. 1981, 13, 771-783. S, Cp copied from Allyl_S""",
    longDesc = 
"""

""",
)

entry(
    index = 146,
    label = "CsJ-CdCsH-HHHHN3d_560",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {7,S}
3   Cd  u0 p0 c0 {2,S} {8,D} {9,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   N3d u0 p1 c0 {3,D}
9   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.09582,-1.52603,-3.63043,-6.39284,-11.086,-13.6133,-18.498],'J/(mol*K)'),
        H298 = (364.794,'kJ/mol'),
        S298 = (-8.28063,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 147,
    label = "CsJ-CdCsH-HHHHN5dc_636",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cs   u1 p0 c0 {1,S} {3,S} {7,S}
3   Cd   u0 p0 c0 {2,S} {8,D} {9,S}
4   H    u0 p0 c0 {1,S}
5   H    u0 p0 c0 {1,S}
6   H    u0 p0 c0 {1,S}
7   H    u0 p0 c0 {2,S}
8   N5dc u0 p0 c+1 {3,D}
9   H    u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.43294,-0.613202,-3.84431,-7.12548,-11.595,-14.0599,-18.8614],'J/(mol*K)'),
        H298 = (309.07,'kJ/mol'),
        S298 = (-5.33705,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 148,
    label = "C=CCJC=C",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S}
3   Cd u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.13,-1.96,-1.88,-1.89,-2.2,-2.6,-2.6],'cal/(mol*K)'),
        H298 = (76,'kcal/mol'),
        S298 = (-4.05,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 149,
    label = "Aromatic_pi_S_1_4",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cd u0 {1,S} {4,D}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {2,D} {6,S}
5   Cd u0 {3,D} {6,S}
6   Cs u0 {4,S} {5,S}
7   H  u0 {1,S}
""",
    thermo = 'Aromatic_pi_S_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_1_3
""",
)

entry(
    index = 150,
    label = "Aromatic_pi_S_(CH3_CH3_Ortho)_1_4",
    group = 
"""
1   Cd u0 {2,S} {4,D} {7,S}
2   Cs u0 {1,S} {5,S} {8,S}
3 * Cs u1 {4,S} {6,S} {9,S}
4   Cd u0 {1,D} {3,S}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {3,S} {5,D}
7   C  u0 {1,S}
8   C  u0 {2,S}
9   H  u0 {3,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 151,
    label = "Aromatic_pi_S_(CH3_C2H5_Ortho)_1_4",
    group = 
"""
1    Cs u0 {2,S} {5,S} {7,S}
2    Cd u0 {1,S} {4,D} {8,S}
3  * Cs u1 {4,S} {6,S} {9,S}
4    Cd u0 {2,D} {3,S}
5    Cd u0 {1,S} {6,D}
6    Cd u0 {3,S} {5,D}
7    C  u0 {1,S} {10,S}
8    C  u0 {2,S}
9    H  u0 {3,S}
10   C  u0 {7,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 152,
    label = "Aromatic_pi_S_(fused5)_1_4",
    group = 
"""
1    Cd u0 {2,S} {4,D} {6,S}
2    Cs u0 {1,S} {5,S} {7,S}
3  * Cs u1 {4,S} {8,S} {10,S}
4    Cd u0 {1,D} {3,S}
5    Cd u0 {2,S} {8,D}
6    C  u0 {1,S} {9,S}
7    C  u0 {2,S} {9,S}
8    Cd u0 {3,S} {5,D}
9    C  u0 {6,S} {7,S}
10   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.748775,0.045256,-0.710099,-1.36165,-2.51235,-3.30599,-4.5709],'cal/(mol*K)','+|-',[0.098378,0.098378,0.098378,0.098378,0.098378,0.098378,0.098378]),
        H298 = (74.4829,'kcal/mol','+|-',1.11628),
        S298 = (0.780097,'cal/(mol*K)','+|-',0.163349),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCC2[CH]1
CC1CCC2=CC=C[CH]C21
CCC1CCC2=CC=C[CH]C21
CCCC1CCC2=CC=C[CH]C21
""",
)

entry(
    index = 153,
    label = "Aromatic_pi_S_(fused6)_1_4",
    group = 
"""
1    Cd u0 {2,S} {4,D} {6,S}
2    Cs u0 {1,S} {5,S} {7,S}
3  * Cs u1 {4,S} {8,S} {11,S}
4    Cd u0 {1,D} {3,S}
5    Cd u0 {2,S} {8,D}
6    C  u0 {1,S} {10,S}
7    C  u0 {2,S} {9,S}
8    Cd u0 {3,S} {5,D}
9    C  u0 {7,S} {10,S}
10   C  u0 {6,S} {9,S}
11   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.01284,-0.508381,-1.05994,-1.55009,-2.56531,-3.36004,-4.58598],'cal/(mol*K)','+|-',[0.129371,0.129371,0.129371,0.129371,0.129371,0.129371,0.129371]),
        H298 = (73.7347,'kcal/mol','+|-',1.66562),
        S298 = (0.399676,'cal/(mol*K)','+|-',0.285184),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCCC2[CH]1
CC1CCCC2=CC=C[CH]C21
CCC1CCCC2=CC=C[CH]C21
""",
)

entry(
    index = 154,
    label = "Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_4",
    group = 
"""
1    Cs u0 {2,S} {5,S} {7,S}
2    Cd u0 {1,S} {6,D} {14,S}
3    Cb u0 {5,S} {9,B} {10,B}
4  * Cs u1 {6,S} {8,S} {15,S}
5    C  u0 {1,S} {3,S}
6    Cd u0 {2,D} {4,S}
7    Cd u0 {1,S} {8,D}
8    Cd u0 {4,S} {7,D}
9    Cb u0 {3,B} {11,B}
10   Cb u0 {3,B} {12,B}
11   Cb u0 {9,B} {13,B}
12   Cb u0 {10,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {2,S}
15   H  u0 {4,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 155,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_4",
    group = 
"""
1    Cs u0 {2,S} {4,S} {7,S}
2    Cs u0 {1,S} {3,S} {14,S}
3    Cb u0 {2,S} {8,B} {9,B}
4    Cd u0 {1,S} {6,D} {15,S}
5  * Cs u1 {6,S} {10,S} {16,S}
6    Cd u0 {4,D} {5,S}
7    Cd u0 {1,S} {10,D}
8    Cb u0 {3,B} {11,B}
9    Cb u0 {3,B} {12,B}
10   Cd u0 {5,S} {7,D}
11   Cb u0 {8,B} {13,B}
12   Cb u0 {9,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {2,S}
15   C  u0 {4,S}
16   H  u0 {5,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 156,
    label = "Aromatic_pi_S_(CH3_CH3_Meta)_1_4",
    group = 
"""
1   Cd u0 {2,S} {4,D} {8,S}
2 * Cs u1 {1,S} {5,S} {7,S}
3   Cs u0 {4,S} {6,S} {9,S}
4   Cd u0 {1,D} {3,S}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {3,S} {5,D}
7   H  u0 {2,S}
8   C  u0 {1,S}
9   C  u0 {3,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 157,
    label = "Aromatic_pi_S_(CH3_C2H5_Meta)_1_4",
    group = 
"""
1    Cd u0 {3,S} {4,D} {9,S}
2    Cs u0 {4,S} {5,S} {7,S}
3  * Cs u1 {1,S} {6,S} {8,S}
4    Cd u0 {1,D} {2,S}
5    Cd u0 {2,S} {6,D}
6    Cd u0 {3,S} {5,D}
7    C  u0 {2,S} {10,S}
8    H  u0 {3,S}
9    C  u0 {1,S}
10   C  u0 {7,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 158,
    label = "Aromatic_pi_S_(CH3_Benzyl_Meta)_1_4",
    group = 
"""
1    Cs u0 {5,S} {6,S} {7,S}
2    Cb u0 {6,S} {9,B} {10,B}
3    Cd u0 {4,S} {5,D} {15,S}
4  * Cs u1 {3,S} {8,S} {14,S}
5    Cd u0 {1,S} {3,D}
6    C  u0 {1,S} {2,S}
7    Cd u0 {1,S} {8,D}
8    Cd u0 {4,S} {7,D}
9    Cb u0 {2,B} {11,B}
10   Cb u0 {2,B} {12,B}
11   Cb u0 {9,B} {13,B}
12   Cb u0 {10,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   H  u0 {4,S}
15   C  u0 {3,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 159,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_4",
    group = 
"""
1    Cs u0 {2,S} {6,S} {7,S}
2    Cs u0 {1,S} {3,S} {14,S}
3    Cb u0 {2,S} {9,B} {10,B}
4    Cd u0 {5,S} {6,D} {16,S}
5  * Cs u1 {4,S} {8,S} {15,S}
6    Cd u0 {1,S} {4,D}
7    Cd u0 {1,S} {8,D}
8    Cd u0 {5,S} {7,D}
9    Cb u0 {3,B} {11,B}
10   Cb u0 {3,B} {12,B}
11   Cb u0 {9,B} {13,B}
12   Cb u0 {10,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {2,S}
15   H  u0 {5,S}
16   C  u0 {4,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 160,
    label = "Aromatic_pi_S_(CH3_CH3_Sub)_1_4",
    group = 
"""
1   Cs u0 {3,S} {4,S} {7,S} {8,S}
2 * Cs u1 {5,S} {6,S} {9,S}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {1,S} {6,D}
5   Cd u0 {2,S} {3,D}
6   Cd u0 {2,S} {4,D}
7   C  u0 {1,S}
8   C  u0 {1,S}
9   H  u0 {2,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 161,
    label = "Aromatic_pi_S_(s1_3_6_diene_1_4)_1_4",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S} {6,S}
2 * Cs u1 {7,S} {8,S} {9,S}
3   C  u0 {1,S} {4,S}
4   C  u0 {1,S} {3,S}
5   Cd u0 {1,S} {7,D}
6   Cd u0 {1,S} {8,D}
7   Cd u0 {2,S} {5,D}
8   Cd u0 {2,S} {6,D}
9   H  u0 {2,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(s1_3_6_diene_1_4)_1_3
""",
)

entry(
    index = 162,
    label = "Aromatic_pi_S_(CH3_C2H5_Sub)_1_4",
    group = 
"""
1    Cs u0 {3,S} {4,S} {7,S} {8,S}
2  * Cs u1 {5,S} {6,S} {9,S}
3    Cd u0 {1,S} {5,D}
4    Cd u0 {1,S} {6,D}
5    Cd u0 {2,S} {3,D}
6    Cd u0 {2,S} {4,D}
7    C  u0 {1,S} {10,S}
8    C  u0 {1,S}
9    H  u0 {2,S}
10   C  u0 {7,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 163,
    label = "Aromatic_pi_S_(s1_4_6_diene_1_4)_1_4",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2  * Cs u1 {7,S} {8,S} {10,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    C  u0 {1,S} {9,S}
6    C  u0 {1,S} {9,S}
7    Cd u0 {2,S} {3,D}
8    Cd u0 {2,S} {4,D}
9    C  u0 {5,S} {6,S}
10   H  u0 {2,S}
""",
    thermo = 'Aromatic_pi_S_(s1_4_6_diene_1_4)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(s1_4_6_diene_1_4)_1_3
""",
)

entry(
    index = 164,
    label = "Aromatic_pi_S_(s1_5_6_diene_1_4)_1_4",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2  * Cs u1 {7,S} {8,S} {11,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    C  u0 {1,S} {10,S}
6    C  u0 {1,S} {9,S}
7    Cd u0 {2,S} {3,D}
8    Cd u0 {2,S} {4,D}
9    C  u0 {6,S} {10,S}
10   C  u0 {5,S} {9,S}
11   H  u0 {2,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(s1_5_6_diene_1_4)_1_3
""",
)

entry(
    index = 165,
    label = "Aromatic_pi_S_(s1_6_6_diene_1_4)_1_4",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2  * Cs u1 {7,S} {8,S} {12,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    C  u0 {1,S} {10,S}
6    C  u0 {1,S} {9,S}
7    Cd u0 {2,S} {3,D}
8    Cd u0 {2,S} {4,D}
9    C  u0 {6,S} {11,S}
10   C  u0 {5,S} {11,S}
11   C  u0 {9,S} {10,S}
12   H  u0 {2,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(s1_6_6_diene_1_4)_1_3
""",
)

entry(
    index = 166,
    label = "Aromatic_pi_S_(CH3_Benzyl_Sub)_1_4",
    group = 
"""
1    Cs u0 {4,S} {5,S} {6,S} {14,S}
2    Cb u0 {4,S} {9,B} {10,B}
3  * Cs u1 {7,S} {8,S} {15,S}
4    C  u0 {1,S} {2,S}
5    Cd u0 {1,S} {7,D}
6    Cd u0 {1,S} {8,D}
7    Cd u0 {3,S} {5,D}
8    Cd u0 {3,S} {6,D}
9    Cb u0 {2,B} {11,B}
10   Cb u0 {2,B} {12,B}
11   Cb u0 {9,B} {13,B}
12   Cb u0 {10,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {1,S}
15   H  u0 {3,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 167,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Sub)_1_4",
    group = 
"""
1    Cs u0 {2,S} {5,S} {6,S} {14,S}
2    Cs u0 {1,S} {3,S} {15,S}
3    Cb u0 {2,S} {9,B} {10,B}
4  * Cs u1 {7,S} {8,S} {16,S}
5    Cd u0 {1,S} {7,D}
6    Cd u0 {1,S} {8,D}
7    Cd u0 {4,S} {5,D}
8    Cd u0 {4,S} {6,D}
9    Cb u0 {3,B} {11,B}
10   Cb u0 {3,B} {12,B}
11   Cb u0 {9,B} {13,B}
12   Cb u0 {10,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {1,S}
15   C  u0 {2,S}
16   H  u0 {4,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 168,
    label = "cyclopropenyl-allyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {1,S} {2,D}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.13,-1.96,-1.88,-1.89,-2.2,-2.6,-2.6],'cal/(mol*K)'),
        H298 = (90.6,'kcal/mol'),
        S298 = (-4.05,'cal/(mol*K)'),
    ),
    shortDesc = """DeFrees, D. J.; McIver, R. T., Jr.; Hehre, W. J., "Heats of Formation of Gaseous Free Radicals via Ion Cyclotron Double Resonance Spectroscopy," J. Am. Chem. Soc. 1980, 102, 3334-3338, DOI: 10.1021/ja00530a005 S, Cp copied from C=CCJC=C""",
    longDesc = 
"""

""",
)

entry(
    index = 169,
    label = "1,3-cyclopentadiene-allyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cd u0 {1,S} {4,D}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {2,D} {5,S}
5   Cd u0 {3,D} {4,S}
6   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.157,0.892,-0.937,-2.776,-4.931,-3.793,-4.855],'cal/(mol*K)'),
        H298 = (84.912,'kcal/mol'),
        S298 = (-2.047,'cal/(mol*K)'),
    ),
    shortDesc = """Combined experimental and theoretical results of Tranter for 1,2-CPD'yl""",
    longDesc = 
"""
Absolute Enthalpy of formation at 298 K from experiment (1998 Kern and Tranter).
All other  values from theory (2001 Kiefer and Tranter).
""",
)

entry(
    index = 170,
    label = "C=CCJC=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.5,-3.8,-3.7,-4.3,-6.1,-8.1,-11.5],'J/(mol*K)'),
        H298 = (318,'kJ/mol'),
        S298 = (-22,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 171,
    label = "Sec_Propargyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.59,-1.2,-1.75,-2.19,-2.91,-3.49,-3.49],'cal/(mol*K)'),
        H298 = (87,'kcal/mol'),
        S298 = (-0.45,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 172,
    label = "CsJ-CsCtH-HHHN3t_538",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {7,S}
3   Ct  u0 p0 c0 {2,S} {8,T}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   N3t u0 p1 c0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0793835,-2.60364,-4.69222,-6.51468,-10.1661,-13.4041,-18.3476],'J/(mol*K)'),
        H298 = (388.052,'kJ/mol'),
        S298 = (1.75313,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 173,
    label = "CCJC=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   C   u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.9,-3.4,-3.4,-4.2,-6.7,-9.2,-13.9],'J/(mol*K)'),
        H298 = (379.1,'kJ/mol'),
        S298 = (-5.7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 174,
    label = "CCJCHO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D} {6,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.36,-1.57,-1.73,-1.89,-2.66,-3.11,-3.5],'cal/(mol*K)'),
        H298 = (91.9,'kcal/mol'),
        S298 = (-2.37,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 175,
    label = "C=OCJC=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   CO  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.9,1.5,0.9,0,-2.5,-5.1,-10.2],'J/(mol*K)'),
        H298 = (382.7,'kJ/mol'),
        S298 = (-13,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 176,
    label = "Cs_T",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = 'Tertalkyl',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 177,
    label = "CCJ(C)CO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S} {5,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.8,-9.3,-10.3,-11,-12.4,-13.7,-16.1],'J/(mol*K)'),
        H298 = (369.4,'kJ/mol'),
        S298 = (-0.8,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 178,
    label = "C2CJCOOH",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   Cs  u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   O2s u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.54,-4.16,-4.44,-4.58,-4.74,-4.88,-5.23],'cal/(mol*K)'),
        H298 = (97.2,'kcal/mol'),
        S298 = (7.31,'cal/(mol*K)'),
    ),
    shortDesc = """WIJAYA et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 179,
    label = "Tertalkyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (96.5,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 180,
    label = "bicyclo[1.1.0]butane-tertiary",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2 * Cs u1 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (113.8,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 181,
    label = "bicyclo[2.1.0]pentane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {5,S}
5   Cs u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (110.2,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 182,
    label = "bicyclo[1.1.1]pentane-C1",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {5,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (106.2,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 183,
    label = "bicyclo[3.1.0]hexane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (108.6,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 184,
    label = "bicyclo[2.2.0]hexane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {2,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (104,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 185,
    label = "bicyclo[2.1.1]hexane-C1",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   C  u0 {2,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (108.9,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 186,
    label = "bridgehead_norbornyl",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {7,S}
2   Cs u0 {3,S} {5,S} {6,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {2,S} {4,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (107.42,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """P.M. Nunes, S.G. Estacio, G.T. Lopes, B.J. Costa Cabral, R.M. Borges dos Santos, J.A. Martinho Simoes, CH Bond Dissociation Enthalpies in Norbornane. An Experimental and Computational Study, Organic Letters, 10 (2008) 1613-1616. S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 187,
    label = "bicyclo[3.2.0]heptane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {2,S} {7,S}
6   Cs u0 {1,S} {7,S}
7   Cs u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (102.6,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 188,
    label = "bicyclo[4.1.0]heptane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {4,S} {7,S}
7   Cs u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (105.4,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 189,
    label = "bicyclo[3.1.1]heptane-C1",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   Cs u0 {1,S} {7,S}
7   C  u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (103.6,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 190,
    label = "octahydro-pentalene-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {5,S} {6,S}
3   Cs u0 {1,S} {8,S}
4   Cs u0 {1,S} {7,S}
5   C  u0 {2,S} {7,S}
6   C  u0 {2,S} {8,S}
7   C  u0 {4,S} {5,S}
8   C  u0 {3,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (95.7,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 191,
    label = "bicyclo[4.2.0]octane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   C  u0 {2,S} {3,S}
5   C  u0 {2,S} {7,S}
6   Cs u0 {1,S} {8,S}
7   C  u0 {5,S} {8,S}
8   C  u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (97,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 192,
    label = "bicyclo[2.2.2]octane-C1",
    group = 
"""
1 * Cs u1 {3,S} {6,S} {8,S}
2   Cs u0 {4,S} {5,S} {7,S}
3   Cs u0 {1,S} {4,S}
4   C  u0 {2,S} {3,S}
5   C  u0 {2,S} {6,S}
6   Cs u0 {1,S} {5,S}
7   C  u0 {2,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (101.9,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 193,
    label = "Benzyl_T",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.27,-0.78,-1.54,-2.06,-2.74,-3.19,-3.19],'cal/(mol*K)'),
        H298 = (83.8,'kcal/mol'),
        S298 = (-5.34,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 194,
    label = "Benzyl_T_Fused5",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cb u0 {1,S} {4,B}
3   C  u0 {1,S} {5,[S,B,T]}
4   Cb u0 {2,B} {5,S}
5   C  u0 {3,[S,B,T]} {4,S}
6   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.457289,-1.56269,-2.22771,-2.42903,-2.80968,-3.48772,-4.25286],'cal/(mol*K)','+|-',[0.282803,0.282803,0.282803,0.282803,0.282803,0.282803,0.282803]),
        H298 = (85.4498,'kcal/mol','+|-',1.02262),
        S298 = (4.37066,'cal/(mol*K)','+|-',0.608769),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
CC1C[CH]C2=CC=CC=C21
CCC1C[CH]C2=CC=CC=C21
CCCC1C[CH]C2=CC=CC=C21
""",
)

entry(
    index = 195,
    label = "Benzyl_T_Fused6",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cb u0 {1,S} {4,B}
3   C  u0 {1,S} {5,[S,D,T,B]}
4   Cb u0 {2,B} {6,S}
5   C  u0 {3,[S,D,T,B]} {6,[S,D,T,B]}
6   C  u0 {4,S} {5,[S,D,T,B]}
7   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.148032,-0.974235,-1.84864,-2.42284,-3.01207,-3.46526,-4.43708],'cal/(mol*K)','+|-',[0.514226,0.514226,0.514226,0.514226,0.514226,0.514226,0.514226]),
        H298 = (84.72,'kcal/mol','+|-',1.82377),
        S298 = (1.70208,'cal/(mol*K)','+|-',1.17522),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C[C]1CCCC2=CC=CC=C21
CC[C]1CCCC2=CC=CC=C21
""",
)

entry(
    index = 196,
    label = "Benzyl_T_dihydronaphthalene",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cb u0 {1,S} {4,B}
3   C  u0 {1,S} {5,[S,D,T,B]}
4   Cb u0 {2,B} {6,S}
5   Cd u0 {3,[S,D,T,B]} {6,D}
6   Cd u0 {4,S} {5,D}
7   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.264274,-0.237466,-0.864612,-1.639,-2.84087,-3.59047,-4.6789],'cal/(mol*K)','+|-',[0.546927,0.546927,0.546927,0.546927,0.546927,0.546927,0.546927]),
        H298 = (83.3368,'kcal/mol','+|-',2.01563),
        S298 = (2.12045,'cal/(mol*K)','+|-',0.802466),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 07/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C[C]1CC=CC2=CC=CC=C12
CC[C]1CC=CC2=CC=CC=C12
""",
)

entry(
    index = 197,
    label = "CCJ(C)C=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.1,-10,-11.8,-12.9,-14.1,-15.1,-16.9],'J/(mol*K)'),
        H298 = (361.8,'kJ/mol'),
        S298 = (3.5,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 198,
    label = "C=CCJ(C)C=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   C   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.8,-8.2,-8.9,-9.3,-10.1,-11,-12.9],'J/(mol*K)'),
        H298 = (313.4,'kJ/mol'),
        S298 = (0.5,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 199,
    label = "C=CCJ(C=C=O)C=C",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   C   u0 {3,D}
7   C   u0 {4,D}
8   O2d u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.7,-9.3,-8.1,-7.2,-6.8,-7.2,-8.8],'J/(mol*K)'),
        H298 = (287.1,'kJ/mol'),
        S298 = (-27.5,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 200,
    label = "Allyl_T",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.79,-2.38,-2.74,-2.97,-3.28,-3.55,-3.55],'cal/(mol*K)'),
        H298 = (83.4,'kcal/mol'),
        S298 = (-3.69,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 201,
    label = "Aromatic_pi_T_1_3",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cd u0 {1,S} {5,D}
3   Cs u0 {1,S} {4,S}
4   Cd u0 {3,S} {6,D}
5   Cd u0 {2,D} {6,S}
6   Cd u0 {4,D} {5,S}
7   C  u0 {1,S}
""",
    thermo = 'Aromatic_pi_S_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_1_3
""",
)

entry(
    index = 202,
    label = "Aromatic_pi_T_(CH3_CH3_Ortho)_1_3",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cs u0 {1,S} {4,S} {8,S}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {2,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cd u0 {3,D} {5,S}
7   C  u0 {1,S}
8   C  u0 {2,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 203,
    label = "Aromatic_pi_T_(CH3_C2H5_Ortho)_1_3",
    group = 
"""
1   Cs u0 {2,S} {3,S} {7,S}
2 * Cs u1 {1,S} {4,S} {8,S}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {2,S} {6,D}
5   Cd u0 {3,D} {6,S}
6   Cd u0 {4,D} {5,S}
7   C  u0 {1,S} {9,S}
8   C  u0 {2,S}
9   C  u0 {7,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 204,
    label = "Aromatic_pi_T_(fused5)_1_3",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3   Cd u0 {1,S} {8,D}
4   Cd u0 {2,S} {9,D}
5   C  u0 {1,S} {7,S}
6   C  u0 {2,S} {7,S}
7   C  u0 {5,S} {6,S}
8   Cd u0 {3,D} {9,S}
9   Cd u0 {4,D} {8,S}
""",
    thermo = 'Aromatic_pi_S_(fused5)_1_4',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCC2[CH]1
CC1CCC2=CC=C[CH]C21
CCC1CCC2=CC=C[CH]C21
CCCC1CCC2=CC=C[CH]C21
C1=CC=C2CCCCC2[CH]1
CC1CCCC2=CC=C[CH]C21
CCC1CCCC2=CC=C[CH]C21
""",
)

entry(
    index = 205,
    label = "Aromatic_pi_T_(fused6)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {3,S} {5,S}
2    Cs u0 {1,S} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    C  u0 {1,S} {10,S}
6    C  u0 {2,S} {9,S}
7    Cd u0 {3,D} {8,S}
8    Cd u0 {4,D} {7,S}
9    C  u0 {6,S} {10,S}
10   C  u0 {5,S} {9,S}
""",
    thermo = 'Aromatic_pi_S_(fused5)_1_4',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCC2[CH]1
CC1CCC2=CC=C[CH]C21
CCC1CCC2=CC=C[CH]C21
CCCC1CCC2=CC=C[CH]C21
C1=CC=C2CCCCC2[CH]1
CC1CCCC2=CC=C[CH]C21
CCC1CCCC2=CC=C[CH]C21
""",
)

entry(
    index = 206,
    label = "Aromatic_pi_T_(CH3_Benzyl_Ortho)_1_3",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S}
2    Cb u0 {4,S} {7,B} {8,B}
3  * Cs u1 {1,S} {6,S} {14,S}
4    C  u0 {1,S} {2,S}
5    Cd u0 {1,S} {9,D}
6    Cd u0 {3,S} {10,D}
7    Cb u0 {2,B} {11,B}
8    Cb u0 {2,B} {12,B}
9    Cd u0 {5,D} {10,S}
10   Cd u0 {6,D} {9,S}
11   Cb u0 {7,B} {13,B}
12   Cb u0 {8,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {3,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 207,
    label = "Aromatic_pi_T_(CH3_EBenzyl_Ortho)_1_3",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S}
2    Cs u0 {1,S} {3,S} {14,S}
3    Cb u0 {2,S} {6,B} {7,B}
4  * Cs u1 {1,S} {8,S} {15,S}
5    Cd u0 {1,S} {9,D}
6    Cb u0 {3,B} {11,B}
7    Cb u0 {3,B} {12,B}
8    Cd u0 {4,S} {10,D}
9    Cd u0 {5,D} {10,S}
10   Cd u0 {8,D} {9,S}
11   Cb u0 {6,B} {13,B}
12   Cb u0 {7,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {2,S}
15   C  u0 {4,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 208,
    label = "Aromatic_pi_T_1_4",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,S} {4,D}
4   Cd u0 {3,D} {6,S}
5   Cd u0 {2,D} {6,S}
6   Cs u0 {4,S} {5,S}
7   C  u0 {1,S}
""",
    thermo = 'Aromatic_pi_S_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_1_3
""",
)

entry(
    index = 209,
    label = "Aromatic_pi_T_(CH3_CH3_Para)_1_4",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cd u0 {1,S} {4,D} {8,S}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {2,D} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cd u0 {3,D} {5,S}
7   C  u0 {1,S}
8   C  u0 {2,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 210,
    label = "Aromatic_pi_T_(CH3_C2H5_Para)_1_4",
    group = 
"""
1   Cd u0 {2,S} {3,D} {7,S}
2 * Cs u1 {1,S} {4,S} {8,S}
3   Cd u0 {1,D} {5,S}
4   Cd u0 {2,S} {6,D}
5   Cs u0 {3,S} {6,S}
6   Cd u0 {4,D} {5,S}
7   C  u0 {1,S} {9,S}
8   C  u0 {2,S}
9   C  u0 {7,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 211,
    label = "Aromatic_pi_T_(CH3_Benzyl_Para)_1_4",
    group = 
"""
1    Cd u0 {3,S} {4,S} {5,D}
2    Cb u0 {4,S} {7,B} {8,B}
3  * Cs u1 {1,S} {6,S} {14,S}
4    C  u0 {1,S} {2,S}
5    Cd u0 {1,D} {9,S}
6    Cd u0 {3,S} {10,D}
7    Cb u0 {2,B} {11,B}
8    Cb u0 {2,B} {12,B}
9    Cs u0 {5,S} {10,S}
10   Cd u0 {6,D} {9,S}
11   Cb u0 {7,B} {13,B}
12   Cb u0 {8,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {3,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 212,
    label = "Aromatic_pi_T_(CH3_EBenzyl_Para)_1_4",
    group = 
"""
1    Cd u0 {2,S} {4,S} {5,D}
2    Cs u0 {1,S} {3,S} {14,S}
3    Cb u0 {2,S} {6,B} {7,B}
4  * Cs u1 {1,S} {8,S} {15,S}
5    Cd u0 {1,D} {9,S}
6    Cb u0 {3,B} {11,B}
7    Cb u0 {3,B} {12,B}
8    Cd u0 {4,S} {10,D}
9    Cs u0 {5,S} {10,S}
10   Cd u0 {8,D} {9,S}
11   Cb u0 {6,B} {13,B}
12   Cb u0 {7,B} {13,B}
13   Cb u0 {11,B} {12,B}
14   C  u0 {2,S}
15   C  u0 {4,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 213,
    label = "bicyclo[2.1.0]pent-2-ene-C1",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cd u0 {2,S} {5,D}
5   Cd u0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (112.1,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 214,
    label = "bicyclo[2.1.1]hex-2-ene-C1",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (110.1,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 215,
    label = "bicyclo[2.2.0]hexa-2,5-diene-C1",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cd u0 {1,S} {4,D}
4   Cd u0 {2,S} {3,D}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (102.8,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 216,
    label = "C=CCJ(C)C=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {6,D}
4   C   u0 {1,S}
5   C   u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-12.2,-10.5,-9.4,-9,-9.1,-9.7,-11.5],'J/(mol*K)'),
        H298 = (335.4,'kJ/mol'),
        S298 = (-17.3,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 217,
    label = "C=CCJ(C=O)C=C",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {6,D}
5   C   u0 {2,D}
6   C   u0 {4,D}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10,-7.5,-6.1,-5.5,-5.6,-6.4,-8.5],'J/(mol*K)'),
        H298 = (307.4,'kJ/mol'),
        S298 = (-27.9,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 218,
    label = "Tert_Propargyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.04,-1.01,-1.74,-2.41,-3.19,-3.65,-3.65],'cal/(mol*K)'),
        H298 = (84.5,'kcal/mol'),
        S298 = (1.48,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 219,
    label = "C2CJCO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D} {6,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
6   R   u0 {2,S}
""",
    thermo = 'C2CJCHO',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 220,
    label = "C2CJCHO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D} {6,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
6   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.62,-0.2,-1.23,-1.82,-2.87,-3.47,-3.47],'cal/(mol*K)'),
        H298 = (89.8,'kcal/mol'),
        S298 = (-1.71,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI #. Value for Cp1500 taken as equal to Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 221,
    label = "CsJO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.9,3.7,1.6,-0.9,-5.9,-10.3,-17.5],'J/(mol*K)'),
        H298 = (413.3,'kJ/mol'),
        S298 = (1.2,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 222,
    label = "CsJOH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.25,0.18,-0.26,-0.83,-1.95,-2.85,-4.22],'cal/(mol*K)'),
        H298 = (96.51,'kcal/mol'),
        S298 = (0.09,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 223,
    label = "CsJOC",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,S}
""",
    thermo = 'CsJOCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 224,
    label = "CsJOCs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   Cs  u0 {2,S}
""",
    thermo = 'CsJOCH3',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 225,
    label = "CsJOCH3",
    group = 
"""
1   Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 * Cs  u1 {3,S} {7,S} {8,S}
3   O2s u0 {1,S} {2,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   H   u0 {2,S}
8   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.16,-0.4,-0.82,-1.33,-2.32,-3.13,-4.37],'cal/(mol*K)'),
        H298 = (97,'kcal/mol'),
        S298 = (0.78,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN #""",
    longDesc = 
"""

""",
)

entry(
    index = 226,
    label = "CsJOCC",
    group = 
"""
1   Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 * Cs  u1 {3,S} {7,S} {8,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   H   u0 {2,S}
8   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01,-1.22,-1.4,-1.71,-3.5,-3.24,-4.42],'cal/(mol*K)'),
        H298 = (96.83,'kcal/mol'),
        S298 = (1.41,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated from data in SUMATHI & GREEN. Values might have large error bars.""",
    longDesc = 
"""

""",
)

entry(
    index = 227,
    label = "CsJOCC2",
    group = 
"""
1   Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 * Cs  u1 {3,S} {7,S} {8,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   H   u0 {1,S}
7   H   u0 {2,S}
8   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.95,0.75,0.23,-0.43,-1.71,-2.72,-4.19],'cal/(mol*K)'),
        H298 = (96.16,'kcal/mol'),
        S298 = (-0.59,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 228,
    label = "CsJOCC3",
    group = 
"""
1   Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 * Cs  u1 {3,S} {7,S} {8,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   C   u0 {1,S}
7   H   u0 {2,S}
8   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.08,-0.09,-0.52,-1.06,-2.11,-2.96,-4.27],'cal/(mol*K)'),
        H298 = (95.75,'kcal/mol'),
        S298 = (0.27,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 229,
    label = "CsJOCds",
    group = 
"""
1 * Cs      u1 {2,S} {3,S} {4,S}
2   O2s     u0 {1,S} {5,S}
3   H       u0 {1,S}
4   H       u0 {1,S}
5   [Cd,CO] u0 {2,S}
""",
    thermo = 'CsJOC(O)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 230,
    label = "CsJOC(O)",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   CO  u0 {2,S} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.91,0.89,0.42,-0.21,-1.5,-2.62,-4.43],'cal/(mol*K)'),
        H298 = (100.7,'kcal/mol'),
        S298 = (-0.18,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 231,
    label = "CsJOC(O)H",
    group = 
"""
1 * Cs  u1 {3,S} {4,S} {5,S}
2   CO  u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
7   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.95,0.97,0.53,-0.12,-1.54,-2.76,-4.53],'cal/(mol*K)'),
        H298 = (100.88,'kcal/mol'),
        S298 = (-0.18,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 232,
    label = "CsJOC(O)C",
    group = 
"""
1 * Cs  u1 {3,S} {4,S} {5,S}
2   CO  u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
7   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.88,0.81,0.31,-0.3,-1.45,-2.47,-4.33],'cal/(mol*K)'),
        H298 = (100.48,'kcal/mol'),
        S298 = (-0.17,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 233,
    label = "C=COCJ",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   Cd  u0 {2,S} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.9,-7.2,-8.9,-10.6,-13.6,-15.9,-19.7],'J/(mol*K)'),
        H298 = (409.4,'kJ/mol'),
        S298 = (13.7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 234,
    label = "CsJOO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.18,-0.42,-0.79,-1.2,-1.99,-2.63,-3.65],'cal/(mol*K)'),
        H298 = (98.5,'kcal/mol'),
        S298 = (-1.57,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 235,
    label = "CsJOOH",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.06,-0.35,-0.76,-1.19,-1.99,-2.64,-3.68],'cal/(mol*K)'),
        H298 = (98.91,'kcal/mol'),
        S298 = (-1.52,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 236,
    label = "CsJOOC",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.31,-0.48,-0.82,-1.22,-1.99,-2.62,-3.63],'cal/(mol*K)'),
        H298 = (98.34,'kcal/mol'),
        S298 = (-1.62,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 237,
    label = "CsJ-HHO2s-N3s_518",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   O2s u0 p2 c0 {1,S} {5,S}
3   H   u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   N3s u0 p1 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.07379,-0.0636699,-2.67407,-5.40344,-10.057,-13.3943,-18.7624],'J/(mol*K)'),
        H298 = (399.133,'kJ/mol'),
        S298 = (-4.91081,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 238,
    label = "CsJ-HHO2s-N3d_535",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   O2s u0 p2 c0 {1,S} {5,S}
3   H   u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   N3d u0 p1 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.72365,1.63954,-1.1501,-4.029,-9.08416,-12.6843,-18.4558],'J/(mol*K)'),
        H298 = (409.974,'kJ/mol'),
        S298 = (-5.6404,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 239,
    label = "CsJ-HHO2s-N1sc_594",
    group = 
"""
1 * Cs   u1 p0 c0 {2,S} {3,S} {4,S}
2   O2s  u0 p2 c0 {1,S} {5,S}
3   H    u0 p0 c0 {1,S}
4   H    u0 p0 c0 {1,S}
5   N1sc u0 p2 c-1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.85167,1.57632,-1.03665,-3.94086,-9.17243,-12.6195,-18.2165],'J/(mol*K)'),
        H298 = (412.26,'kJ/mol'),
        S298 = (-2.54073,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 240,
    label = "CCsJO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.2,0.4,-1.5,-3.9,-8.6,-12.5,-18.7],'J/(mol*K)'),
        H298 = (402,'kJ/mol'),
        S298 = (3.9,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 241,
    label = "CCsJOC",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,S}
""",
    thermo = 'CCsJOCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 242,
    label = "C=CCJ(O)C",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2s u0 {1,S} {6,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
6   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.7,-8.4,-10,-11,-12.1,-13.1,-15.5],'J/(mol*K)'),
        H298 = (328.3,'kJ/mol'),
        S298 = (4.5,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 243,
    label = "CCsJOCs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
5   Cs  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.82,0.53,-0.11,-0.86,-2.2,-3.18,-4.51],'cal/(mol*K)'),
        H298 = (95.41,'kcal/mol'),
        S298 = (0.33,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 244,
    label = "CCsJOCds",
    group = 
"""
1 * Cs      u1 {2,S} {3,S} {4,S}
2   O2s     u0 {1,S} {5,S}
3   C       u0 {1,S}
4   H       u0 {1,S}
5   [CO,Cd] u0 {2,S}
""",
    thermo = 'CCsJOC(O)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 245,
    label = "CCsJOC(O)",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   CO  u0 {2,S} {6,D}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.16,0.78,0.05,-0.73,-2.13,-3.24,-4.9],'cal/(mol*K)'),
        H298 = (98.7,'kcal/mol'),
        S298 = (0.98,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 246,
    label = "CCsJOC(O)H",
    group = 
"""
1 * Cs  u1 {3,S} {4,S} {5,S}
2   CO  u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
7   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.2,0.88,0.16,-0.67,-2.22,-3.43,-5],'cal/(mol*K)'),
        H298 = (98.87,'kcal/mol'),
        S298 = (0.98,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 247,
    label = "CCsJOC(O)C",
    group = 
"""
1 * Cs  u1 {3,S} {4,S} {5,S}
2   CO  u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
7   C   u0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 248,
    label = "C=CCJO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6,-3.9,-3,-3.2,-5.7,-8.6,-13.8],'J/(mol*K)'),
        H298 = (333.9,'kJ/mol'),
        S298 = (-7.4,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 249,
    label = "OCJC=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-3.3,-5.6,-7.4,-9.8,-11.2,-14],'J/(mol*K)'),
        H298 = (356.6,'kJ/mol'),
        S298 = (0.2,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 250,
    label = "CCsJOH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.65,-0.01,-0.75,-1.43,-2.52,-3.31,-4.47],'cal/(mol*K)'),
        H298 = (95.39,'kcal/mol'),
        S298 = (0.92,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 251,
    label = "CsJ-CdHO2s-HHN5dc_608",
    group = 
"""
1 * Cs   u1 p0 c0 {2,S} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,S} {5,D} {6,S}
3   O2s  u0 p2 c0 {1,S} {7,S}
4   H    u0 p0 c0 {1,S}
5   N5dc u0 p0 c+1 {2,D}
6   H    u0 p0 c0 {2,S}
7   H    u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.49254,-5.39057,-6.96828,-9.24536,-12.3762,-14.5685,-19.3777],'J/(mol*K)'),
        H298 = (262.542,'kJ/mol'),
        S298 = (-16.2263,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 252,
    label = "CsJ-CsHO2s-HHHN3s_629",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {7,S}
3   O2s u0 p2 c0 {2,S} {8,S}
4   N3s u0 p1 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.35669,-3.01979,-5.13556,-7.23424,-10.8848,-13.8582,-18.7765],'J/(mol*K)'),
        H298 = (391.254,'kJ/mol'),
        S298 = (3.30391,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 253,
    label = "CCsJOO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.48,-1.15,-1.68,-2.11,-2.77,-3.26,-4.02],'cal/(mol*K)'),
        H298 = (96.9,'kcal/mol'),
        S298 = (0.76,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 254,
    label = "CCsJOOH",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.39,-1.08,-1.64,-2.08,-2.75,-3.26,-4.03],'cal/(mol*K)'),
        H298 = (97.19,'kcal/mol'),
        S298 = (0.77,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 255,
    label = "CCsJOOC",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.58,-1.21,-1.73,-2.15,-2.8,-3.27,-4.01],'cal/(mol*K)'),
        H298 = (96.64,'kcal/mol'),
        S298 = (0.74,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 256,
    label = "CsJ-CsHO2s-HHHN3s_722",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {7,S}
3   O2s u0 p2 c0 {2,S} {8,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   N3s u0 p1 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.797589,-1.63379,-4.31769,-6.67411,-10.6158,-13.6789,-18.5238],'J/(mol*K)'),
        H298 = (399.473,'kJ/mol'),
        S298 = (-2.02552,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 257,
    label = "C2CsJO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2,-7.1,-10.7,-13.4,-16.6,-18.5,-21.2],'J/(mol*K)'),
        H298 = (398.4,'kJ/mol'),
        S298 = (14.4,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 258,
    label = "C2CsJOH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.31,-0.66,-1.54,-2.23,-3.17,-3.8,-4.72],'cal/(mol*K)'),
        H298 = (94.5,'kcal/mol'),
        S298 = (2.17,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 259,
    label = "C2CsJOC",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   C   u0 {2,S}
""",
    thermo = 'C2CsJOCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 260,
    label = "C2CsJOCs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   Cs  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.09,-1.37,-2.49,-3.26,-4.15,-4.63,-5.23],'cal/(mol*K)'),
        H298 = (95.5,'kcal/mol'),
        S298 = (3.71,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 261,
    label = "C2CsJOCds",
    group = 
"""
1 * Cs      u1 {2,S} {3,S} {4,S}
2   O2s     u0 {1,S} {5,S}
3   C       u0 {1,S}
4   C       u0 {1,S}
5   [Cd,CO] u0 {2,S}
""",
    thermo = 'C2CsJOC(O)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 262,
    label = "C2CsJOC(O)",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   CO  u0 {2,S} {6,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.04,-1.34,-2.3,-2.99,-3.99,-4.77,-5.98],'cal/(mol*K)'),
        H298 = (100.1,'kcal/mol'),
        S298 = (4.77,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 263,
    label = "C2CsJOC(O)H",
    group = 
"""
1 * Cs  u1 {3,S} {4,S} {5,S}
2   CO  u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {2,D}
7   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.03,-1.28,-2.28,-3.1,-4.35,-5.19,-6.06],'cal/(mol*K)'),
        H298 = (99.97,'kcal/mol'),
        S298 = (4.88,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 264,
    label = "C2CsJOC(O)C",
    group = 
"""
1 * Cs  u1 {3,S} {4,S} {5,S}
2   CO  u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {2,D}
7   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.04,-1.4,-2.32,-2.89,-3.62,-4.36,-5.9],'cal/(mol*K)'),
        H298 = (100.25,'kcal/mol'),
        S298 = (4.66,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 265,
    label = "C2CsJOO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.89,-2.09,-2.81,-3.24,-3.69,-3.97,-4.43],'cal/(mol*K)'),
        H298 = (96.7,'kcal/mol'),
        S298 = (2.22,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 266,
    label = "C2CsJOOH",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   H   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01,-2.17,-2.87,-3.3,-3.77,-4.05,-4.49],'cal/(mol*K)'),
        H298 = (96.74,'kcal/mol'),
        S298 = (2.37,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 267,
    label = "C2CsJOOC",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.02,-2.75,-3.18,-3.62,-3.88,-4.37],'cal/(mol*K)'),
        H298 = (96.58,'kcal/mol'),
        S298 = (2.08,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 268,
    label = "CsJ-S",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   S  ux {1,S}
3   R  ux {1,S}
4   R  ux {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 269,
    label = "CsJ-SsHH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   S2s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.07,-0.32,-0.73,-1.22,-2.18,-2.99,-4.27],'cal/(mol*K)'),
        H298 = (95.34,'kcal/mol'),
        S298 = (1.18,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 270,
    label = "CsJ-CSH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 271,
    label = "CsJ-CsSsH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.25,-0.79,-1.36,-1.9,-2.82,-3.53,-4.64],'cal/(mol*K)'),
        H298 = (92.87,'kcal/mol'),
        S298 = (1.91,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 272,
    label = "CsJ-CtSsH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Ct  u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.26,-0.02,-0.47,-0.97,-1.95,-2.77,-4.12],'cal/(mol*K)'),
        H298 = (83.48,'kcal/mol'),
        S298 = (-0.16,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 273,
    label = "CsJ-CbSsH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.32,-0.38,-0.65,-1.01,-1.75,-2.4,-3.57],'cal/(mol*K)'),
        H298 = (84.88,'kcal/mol'),
        S298 = (-0.98,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 274,
    label = "CsJ-CdSsH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.21,-2.77,-2.39,-2.24,-2.39,-2.74,-3.56],'cal/(mol*K)'),
        H298 = (81.92,'kcal/mol'),
        S298 = (0.66,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 275,
    label = "CsJ-C=SSsH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CS  u0 {1,S} {5,D}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.75,-2.93,-2.07,-1.54,-1.2,-1.31,-2.01],'cal/(mol*K)'),
        H298 = (71.51,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 276,
    label = "CsJ-CCS",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 277,
    label = "CsJ-CsCsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.72,-2.04,-2.88,-3.4,-3.99,-4.36,-4.96],'cal/(mol*K)'),
        H298 = (92.32,'kcal/mol'),
        S298 = (3.87,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 278,
    label = "CsJ-CsCtSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Ct  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.99,-1.64,-2.18,-2.62,-3.3,-3.82,-4.65],'cal/(mol*K)'),
        H298 = (81.17,'kcal/mol'),
        S298 = (3.05,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 279,
    label = "CsJ-CsCbSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cb  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.99,-2.26,-2.53,-2.75,-3.12,-3.49,-4.43],'cal/(mol*K)'),
        H298 = (84.1,'kcal/mol'),
        S298 = (0.96,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 280,
    label = "CsJ-CsCdSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4,-4.74,-4.81,-4.59,-4.17,-3.99,-4.12],'cal/(mol*K)'),
        H298 = (80.07,'kcal/mol'),
        S298 = (2.53,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 281,
    label = "CsJ-CsC=SSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CS  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.86,-3.83,-3.41,-2.93,-2.28,-2.07,-2.36],'cal/(mol*K)'),
        H298 = (69.17,'kcal/mol'),
        S298 = (-1.97,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 282,
    label = "CsJ-SS",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   S2s u0 {1,S}
3   S2s u0 {1,S}
4   R   u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 283,
    label = "CsJ-SsSsH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   S2s u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.52,-4,-3.64,-3.53,-3.68,-4,-4.72],'cal/(mol*K)'),
        H298 = (90.16,'kcal/mol'),
        S298 = (1.31,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 284,
    label = "CsJ-CSS",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 285,
    label = "CsJ-CsSsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.36,-4,-4.17,-4.24,-4.37,-4.55,-5],'cal/(mol*K)'),
        H298 = (89.98,'kcal/mol'),
        S298 = (5.5,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 286,
    label = "CsJ-CtSsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Ct  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 287,
    label = "CsJ-CbSsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 288,
    label = "CsJ-CdSsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 289,
    label = "CsJ-C=SSsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CS  u0 {1,S} {5,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 290,
    label = "CsJ-SsSsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   S2s u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 291,
    label = "CCsJOS",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   O2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = 'CCsJOHSH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 292,
    label = "CCsJOHSH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   S2s u0 {1,S} {6,S}
4   C   u0 {1,S}
5   H   u0 {2,S}
6   H   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.21,-2.38,-2.47,-2.55,-2.89,-3.33,-4.54],'cal/(mol*K)'),
        H298 = (92.6,'kcal/mol'),
        S298 = (1.67,'cal/(mol*K)'),
    ),
    shortDesc = """CAC CBS-QB3 1d-hr""",
    longDesc = 
"""

""",
)

entry(
    index = 293,
    label = "CsJ-SsOsH",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   S  ux {1,S}
3   O  ux {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.95,-2.6,-2.88,-2.9,-2.72,-2.63,-3.06],'cal/(mol*K)'),
        H298 = (96.64,'kcal/mol'),
        S298 = (-0.74,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 294,
    label = "CsJN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = 'CCsJN',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 295,
    label = "CsJ-HHN3s-CdH_443",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {4,S}
3   H   u0 p0 c0 {2,S}
4   H   u0 p0 c0 {2,S}
5   Cd  u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.60111,1.72239,-1.20739,-4.21782,-9.12676,-12.6404,-18.7562],'J/(mol*K)'),
        H298 = (383.969,'kJ/mol'),
        S298 = (1.90813,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 296,
    label = "CsJ-HHN3d-Cd_447",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   N3d u0 p1 c0 {1,S} {5,D}
3   H   u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   Cd  u0 p0 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.213172,-0.521763,-2.40507,-4.73399,-9.08987,-12.5051,-18.3327],'J/(mol*K)'),
        H298 = (374.999,'kJ/mol'),
        S298 = (-6.06448,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 297,
    label = "CsJ-HHN3s-HO2s_449",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {4,S}
3   H   u0 p0 c0 {2,S}
4   H   u0 p0 c0 {2,S}
5   O2s u0 p2 c0 {1,S}
6   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.676804,-0.768338,-3.01952,-5.48805,-9.98096,-13.3448,-18.5822],'J/(mol*K)'),
        H298 = (369.261,'kJ/mol'),
        S298 = (-0.828503,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 298,
    label = "CsJ-HHN3s-HN3s_471",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {4,S}
3   H   u0 p0 c0 {2,S}
4   H   u0 p0 c0 {2,S}
5   N3s u0 p1 c0 {1,S}
6   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.587399,-0.369921,-2.77219,-5.30159,-9.1303,-12.3045,-17.1924],'J/(mol*K)'),
        H298 = (377.522,'kJ/mol'),
        S298 = (-14.0602,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 299,
    label = "CsJ-HHN3s-CtH_501",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {4,S}
3   H   u0 p0 c0 {2,S}
4   H   u0 p0 c0 {2,S}
5   Ct  u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.4846,1.2993,-1.72623,-4.54861,-9.32371,-13.0441,-18.734],'J/(mol*K)'),
        H298 = (395.957,'kJ/mol'),
        S298 = (0.178289,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 300,
    label = "CsJ-HHN3s-CsH_571",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {4,S}
3   H   u0 p0 c0 {2,S}
4   H   u0 p0 c0 {2,S}
5   Cs  u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.12301,-0.323264,-3.0302,-5.71542,-10.0424,-13.4574,-19.0212],'J/(mol*K)'),
        H298 = (384.739,'kJ/mol'),
        S298 = (-4.94229,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 301,
    label = "CsJ-HHN3s-HN3d_578",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {4,S}
3   H   u0 p0 c0 {2,S}
4   H   u0 p0 c0 {2,S}
5   N3d u0 p1 c0 {1,S}
6   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.19864,1.55467,-1.01753,-4.01962,-8.954,-12.6293,-18.6901],'J/(mol*K)'),
        H298 = (373.647,'kJ/mol'),
        S298 = (-3.7728,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 302,
    label = "CsJ-HHN3d-Cdd_597",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   N3d u0 p1 c0 {1,S} {5,D}
3   H   u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   Cdd u0 p0 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.82314,0.832024,-1.86625,-4.6256,-9.29816,-12.7375,-18.3266],'J/(mol*K)'),
        H298 = (390.719,'kJ/mol'),
        S298 = (-6.27782,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 303,
    label = "CsJ-HHN3s-HH_649",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {4,S}
3   H   u0 p0 c0 {2,S}
4   H   u0 p0 c0 {2,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.14471,0.310182,-2.06152,-4.8614,-9.6649,-13.1279,-18.7464],'J/(mol*K)'),
        H298 = (389.64,'kJ/mol'),
        S298 = (-3.68234,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 304,
    label = "CsJ-HHN3d-N5dc_680",
    group = 
"""
1 * Cs   u1 p0 c0 {2,S} {3,S} {4,S}
2   N3d  u0 p1 c0 {1,S} {5,D}
3   H    u0 p0 c0 {1,S}
4   H    u0 p0 c0 {1,S}
5   N5dc u0 p0 c+1 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0474744,-1.33251,-3.26675,-5.4796,-9.55814,-13.0471,-18.9606],'J/(mol*K)'),
        H298 = (333.546,'kJ/mol'),
        S298 = (-4.38053,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 305,
    label = "CCsJN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.2,-0.7,-1.4,-1.9,-2.8,-3.4,-4.5],'cal/(mol*K)'),
        H298 = (92.1,'kcal/mol'),
        S298 = (2.5,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 306,
    label = "CsJ-CsHN3s-HHHHH_486",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {7,S}
3   N3s u0 p1 c0 {2,S} {8,S} {9,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {3,S}
9   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.71234,-0.222063,-3.0628,-5.8137,-10.2581,-13.6048,-18.5794],'J/(mol*K)'),
        H298 = (384.262,'kJ/mol'),
        S298 = (-2.37496,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 307,
    label = "CsJ-CdHN3s-HHHN3d_585",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   N3s u0 p1 c0 {1,S} {5,S} {6,S}
3   Cd  u0 p0 c0 {1,S} {7,D} {8,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   N3d u0 p1 c0 {3,D}
8   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.31627,-1.51975,-3.42586,-6.10338,-10.3102,-13.568,-19.5662],'J/(mol*K)'),
        H298 = (316.194,'kJ/mol'),
        S298 = (-4.80556,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 308,
    label = "CsJ-CdHN3s-HHHN5dc_620",
    group = 
"""
1 * Cs   u1 p0 c0 {2,S} {3,S} {4,S}
2   N3s  u0 p1 c0 {1,S} {5,S} {6,S}
3   Cd   u0 p0 c0 {1,S} {7,D} {8,S}
4   H    u0 p0 c0 {1,S}
5   H    u0 p0 c0 {2,S}
6   H    u0 p0 c0 {2,S}
7   N5dc u0 p0 c+1 {3,D}
8   H    u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.03918,0.268657,-2.19117,-5.12963,-10.0564,-13.8413,-19.3914],'J/(mol*K)'),
        H298 = (274.549,'kJ/mol'),
        S298 = (0.778429,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 309,
    label = "CsJ-CdHN3s-CdHHH_668",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   N3s u0 p1 c0 {1,S} {5,S} {6,S}
3   Cd  u0 p0 c0 {1,S} {7,D} {8,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   Cd  u0 p0 c0 {3,D}
8   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.56491,0.238888,-2.15318,-4.91908,-9.62944,-13.3199,-19.006],'J/(mol*K)'),
        H298 = (323.711,'kJ/mol'),
        S298 = (4.17507,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 310,
    label = "CsJ-CsHN3s-HHHHO2s_705",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {7,S}
3   N3s u0 p1 c0 {2,S} {8,S} {9,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   O2s u0 p2 c0 {3,S}
9   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.38522,0.414761,-2.684,-5.42349,-9.89194,-13.2464,-18.3071],'J/(mol*K)'),
        H298 = (395.623,'kJ/mol'),
        S298 = (2.96723,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 311,
    label = "CsJ-CsHN3s-HHHHN3s_716",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {7,S}
3   N3s u0 p1 c0 {2,S} {8,S} {9,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   N3s u0 p1 c0 {3,S}
9   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.88752,-0.430371,-3.38906,-6.29779,-10.563,-13.6787,-18.6529],'J/(mol*K)'),
        H298 = (384.331,'kJ/mol'),
        S298 = (0.420533,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 312,
    label = "CsJ-CsHN3s-HHHHN3s_721",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {7,S}
3   N3s u0 p1 c0 {2,S} {8,S} {9,S}
4   N3s u0 p1 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {3,S}
9   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.31648,-1.13225,-3.61336,-6.01426,-10.1996,-13.5927,-18.9903],'J/(mol*K)'),
        H298 = (379.142,'kJ/mol'),
        S298 = (4.00986,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 313,
    label = "CsJ-CsHN3s-HHHHO2s_726",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cs  u1 p0 c0 {1,S} {3,S} {7,S}
3   N3s u0 p1 c0 {2,S} {8,S} {9,S}
4   O2s u0 p2 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {3,S}
9   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.64335,0.703285,-2.2537,-5.08179,-9.77064,-13.3548,-18.7733],'J/(mol*K)'),
        H298 = (386.299,'kJ/mol'),
        S298 = (8.34916,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 314,
    label = "CsJ-CsHN3d-HHHN5dc_728",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cs   u1 p0 c0 {1,S} {3,S} {7,S}
3   N3d  u0 p1 c0 {2,S} {8,D}
4   H    u0 p0 c0 {1,S}
5   H    u0 p0 c0 {1,S}
6   H    u0 p0 c0 {1,S}
7   H    u0 p0 c0 {2,S}
8   N5dc u0 p0 c+1 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.3583,1.43232,-1.77925,-5.27421,-10.746,-13.5259,-18.5479],'J/(mol*K)'),
        H298 = (316.589,'kJ/mol'),
        S298 = (-4.18939,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 315,
    label = "C2CsJN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = 'CCsJN',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 316,
    label = "OCJO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1,-8.2,-14.4,-17.5,-19.4,-20.1,-21.5],'J/(mol*K)'),
        H298 = (408.4,'kJ/mol'),
        S298 = (15.1,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 317,
    label = "CsJ-HO2sO2s-HN3s_466",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   O2s u0 p2 c0 {1,S} {5,S}
3   O2s u0 p2 c0 {1,S} {6,S}
4   H   u0 p0 c0 {1,S}
5   N3s u0 p1 c0 {2,S}
6   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.64187,-2.77678,-4.93896,-7.10102,-10.8662,-13.9283,-18.9165],'J/(mol*K)'),
        H298 = (401.883,'kJ/mol'),
        S298 = (1.90338,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 318,
    label = "CsJ-HN3sN3s_455",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   N3s u0 p1 c0 {1,S}
3   N3s u0 p1 c0 {1,S}
4   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.51465,-0.933882,-3.76965,-6.36862,-10.5537,-13.7131,-18.5315],'J/(mol*K)'),
        H298 = (386.157,'kJ/mol','+|-',7.82537),
        S298 = (6.10835,'J/(mol*K)','+|-',7.96288),
    ),
    shortDesc = """Average from child nodes: CsJ-HN3sN3s-HHHN3s_454 CsJ-HN3sN3s-CsHHH_489 CsJ-HN3sN3s-HHHH_598 CsJ-HN3sN3s-HHHO2s_695""",
    longDesc = 
"""

""",
)

entry(
    index = 319,
    label = "CsJ-HN3sN3s-HHHN3s_454",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   N3s u0 p1 c0 {1,S} {5,S} {6,S}
3   N3s u0 p1 c0 {1,S} {7,S} {8,S}
4   H   u0 p0 c0 {1,S}
5   N3s u0 p1 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {3,S}
8   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.239569,-1.46342,-4.02805,-6.53191,-10.681,-13.8602,-18.7603],'J/(mol*K)'),
        H298 = (385.368,'kJ/mol'),
        S298 = (6.17669,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 320,
    label = "CsJ-HN3sN3s-CsHHH_489",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   N3s u0 p1 c0 {1,S} {5,S} {6,S}
3   N3s u0 p1 c0 {1,S} {7,S} {8,S}
4   H   u0 p0 c0 {1,S}
5   Cs  u0 p0 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {3,S}
8   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.86237,-0.952883,-3.93044,-6.54985,-10.583,-13.6553,-18.4204],'J/(mol*K)'),
        H298 = (380.965,'kJ/mol'),
        S298 = (0.466465,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 321,
    label = "CsJ-HN3sN3s-HHHH_598",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   N3s u0 p1 c0 {1,S} {5,S} {6,S}
3   N3s u0 p1 c0 {1,S} {7,S} {8,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {3,S}
8   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.94022,-1.35855,-4.33085,-6.89396,-10.9796,-13.9594,-18.3791],'J/(mol*K)'),
        H298 = (389.629,'kJ/mol'),
        S298 = (8.58854,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 322,
    label = "CsJ-HN3sN3s-HHHO2s_695",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   N3s u0 p1 c0 {1,S} {5,S} {6,S}
3   N3s u0 p1 c0 {1,S} {7,S} {8,S}
4   H   u0 p0 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {3,S}
8   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.01646,0.0393208,-2.78925,-5.49874,-9.97103,-13.3774,-18.5664],'J/(mol*K)'),
        H298 = (388.665,'kJ/mol'),
        S298 = (9.20169,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 323,
    label = "CsJ-HN3sO2s_457",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   O2s u0 p2 c0 {1,S}
3   N3s u0 p1 c0 {1,S}
4   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.173559,-1.9079,-4.31708,-6.74341,-10.7288,-13.75,-18.6531],'J/(mol*K)'),
        H298 = (363.112,'kJ/mol','+|-',176.315),
        S298 = (4.648,'J/(mol*K)','+|-',12.9493),
    ),
    shortDesc = """Average from child nodes: CsJ-HN3sO2s-HHN3s_456 CsJ-HN3sO2s-HHN3s_467 CsJ-HN3sO2s-CsHH_488 CsJ-HN3sO2s-CsHH_493 CsJ-HN3sO2s-HHO2s_563 CsJ-HN3sO2s-HHH_601 CsJ-HN3sO2s-HHO2s_732""",
    longDesc = 
"""

""",
)

entry(
    index = 324,
    label = "CsJ-HN3sO2s-HHN3s_456",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   N3s u0 p1 c0 {1,S} {5,S} {6,S}
3   O2s u0 p2 c0 {1,S} {7,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   N3s u0 p1 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.344681,-2.0617,-4.37102,-6.51703,-10.3183,-13.4746,-18.7559],'J/(mol*K)'),
        H298 = (403.735,'kJ/mol'),
        S298 = (6.78581,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 325,
    label = "CsJ-HN3sO2s-HHN3s_467",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   N3s u0 p1 c0 {1,S} {5,S} {6,S}
3   O2s u0 p2 c0 {1,S} {7,S}
4   H   u0 p0 c0 {1,S}
5   N3s u0 p1 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.17633,-4.12263,-5.71186,-7.70474,-11.189,-14.0163,-18.7037],'J/(mol*K)'),
        H298 = (393.612,'kJ/mol'),
        S298 = (0.369926,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 326,
    label = "CsJ-HN3sO2s-CsHH_488",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   N3s u0 p1 c0 {1,S} {5,S} {6,S}
3   O2s u0 p2 c0 {1,S} {7,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   Cs  u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0850709,-2.1545,-4.69727,-7.19385,-11.2541,-13.9528,-18.7773],'J/(mol*K)'),
        H298 = (388.439,'kJ/mol'),
        S298 = (-1.61468,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 327,
    label = "CsJ-HN3sO2s-CsHH_493",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   N3s u0 p1 c0 {1,S} {5,S} {6,S}
3   O2s u0 p2 c0 {1,S} {7,S}
4   H   u0 p0 c0 {1,S}
5   Cs  u0 p0 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.681721,-1.60911,-4.41197,-7.13675,-11.0447,-13.8811,-18.7413],'J/(mol*K)'),
        H298 = (394.296,'kJ/mol'),
        S298 = (-0.90845,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 328,
    label = "CsJ-HN3sO2s-HHO2s_563",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   N3s u0 p1 c0 {1,S} {5,S} {6,S}
3   O2s u0 p2 c0 {1,S} {7,S}
4   H   u0 p0 c0 {1,S}
5   O2s u0 p2 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.721007,-2.06398,-4.00088,-6.36137,-10.4129,-13.5991,-18.6421],'J/(mol*K)'),
        H298 = (401.498,'kJ/mol'),
        S298 = (4.51512,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 329,
    label = "CsJ-HN3sO2s-HHH_601",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   N3s u0 p1 c0 {1,S} {5,S} {6,S}
3   O2s u0 p2 c0 {1,S} {7,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.234934,-1.5628,-4.06903,-6.56484,-10.6851,-13.8251,-18.6395],'J/(mol*K)'),
        H298 = (396.677,'kJ/mol'),
        S298 = (6.25148,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 330,
    label = "CsJ-HN3sO2s-HHO2s_732",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   N3s u0 p1 c0 {1,S} {5,S} {6,S}
3   O2s u0 p2 c0 {1,S} {7,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   O2s u0 p2 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.76584,0.219423,-2.9575,-5.72529,-10.1973,-13.5012,-18.3116],'J/(mol*K)'),
        H298 = (163.523,'kJ/mol'),
        S298 = (17.1368,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 331,
    label = "CsJ-HN3dN3s_465",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   N3s u0 p1 c0 {1,S}
3   N3d u0 p1 c0 {1,S}
4   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.50497,1.84254,-1.26365,-4.23559,-9.15437,-12.9057,-18.5674],'J/(mol*K)'),
        H298 = (300.196,'kJ/mol','+|-',57.8487),
        S298 = (11.7974,'J/(mol*K)','+|-',16.5017),
    ),
    shortDesc = """Average from child nodes: CsJ-HN3dN3s-CdHH_464 CsJ-HN3dN3s-HHN5dc_474""",
    longDesc = 
"""

""",
)

entry(
    index = 332,
    label = "CsJ-HN3dN3s-CdHH_464",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   N3s u0 p1 c0 {1,S} {5,S} {6,S}
3   N3d u0 p1 c0 {1,S} {7,D}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6   H   u0 p0 c0 {2,S}
7   Cd  u0 p0 c0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.44714,1.80259,-1.10759,-4.12231,-9.09651,-12.8697,-18.4926],'J/(mol*K)'),
        H298 = (320.648,'kJ/mol'),
        S298 = (5.9632,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 333,
    label = "CsJ-HN3dN3s-HHN5dc_474",
    group = 
"""
1 * Cs   u1 p0 c0 {2,S} {3,S} {4,S}
2   N3s  u0 p1 c0 {1,S} {5,S} {6,S}
3   N3d  u0 p1 c0 {1,S} {7,D}
4   H    u0 p0 c0 {1,S}
5   H    u0 p0 c0 {2,S}
6   H    u0 p0 c0 {2,S}
7   N5dc u0 p0 c+1 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.5628,1.88249,-1.41971,-4.34888,-9.21223,-12.9418,-18.6422],'J/(mol*K)'),
        H298 = (279.743,'kJ/mol'),
        S298 = (17.6317,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 334,
    label = "CsJ-HN3dO2s_589",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   O2s u0 p2 c0 {1,S}
3   N3d u0 p1 c0 {1,S}
4   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.06529,-4.33893,-6.92768,-9.36645,-13.2754,-16.1267,-20.1929],'J/(mol*K)'),
        H298 = (293.425,'kJ/mol'),
        S298 = (4.50766,'J/(mol*K)'),
    ),
    shortDesc = """Average from child nodes: CsJ-HN3dO2s-HO2d_588""",
    longDesc = 
"""

""",
)

entry(
    index = 335,
    label = "CsJ-HN3dO2s-HO2d_588",
    group = 
"""
1 * Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2   O2s u0 p2 c0 {1,S} {5,S}
3   N3d u0 p1 c0 {1,S} {6,D}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
6   O2d u0 p2 c0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.06529,-4.33893,-6.92768,-9.36645,-13.2754,-16.1267,-20.1929],'J/(mol*K)'),
        H298 = (293.425,'kJ/mol'),
        S298 = (4.50766,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 336,
    label = "CsJ-HN1scO2s_664",
    group = 
"""
1 * Cs   u1 p0 c0 {2,S} {3,S} {4,S}
2   O2s  u0 p2 c0 {1,S}
3   N1sc u0 p2 c-1 {1,S}
4   H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.21588,-2.94812,-5.17585,-7.51233,-11.3506,-14.2515,-18.6713],'J/(mol*K)'),
        H298 = (276.236,'kJ/mol'),
        S298 = (3.59311,'J/(mol*K)'),
    ),
    shortDesc = """Average from child nodes: CsJ-HN1scO2s-HN5dc_663""",
    longDesc = 
"""

""",
)

entry(
    index = 337,
    label = "CsJ-HN1scO2s-HN5dc_663",
    group = 
"""
1 * Cs   u1 p0 c0 {2,S} {3,S} {4,S}
2   O2s  u0 p2 c0 {1,S} {5,S}
3   N1sc u0 p2 c-1 {1,S} {6,S}
4   H    u0 p0 c0 {1,S}
5   H    u0 p0 c0 {2,S}
6   N5dc u0 p0 c+1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.21588,-2.94812,-5.17585,-7.51233,-11.3506,-14.2515,-18.6713],'J/(mol*K)'),
        H298 = (276.236,'kJ/mol'),
        S298 = (3.59311,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 338,
    label = "CdsJ",
    group = 
"""
1 * [Cd,CO] u1
""",
    thermo = 'Cds_P',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 339,
    label = "CdsJO",
    group = 
"""
1 * CO  u1 {2,D}
2   O2d u0 {1,D}
""",
    thermo = 'CCJ=O',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 340,
    label = "HCdsJO",
    group = 
"""
1 * CO  u1 {2,D} {3,S}
2   O2d u0 {1,D}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.19,-0.65,-1.19,-1.73,-2.63,-3.32,-4.42],'cal/(mol*K)'),
        H298 = (88.45,'kcal/mol'),
        S298 = (-0.01,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated in relation to formaldehyde from NIST values""",
    longDesc = 
"""

""",
)

entry(
    index = 341,
    label = "CCJ=O",
    group = 
"""
1 * CO  u1 {2,D} {3,S}
2   O2d u0 {1,D}
3   C   u0 {1,S}
""",
    thermo = 'CsCJ=O',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 342,
    label = "CC(C)CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S}
2 * CO  u1 {1,S} {5,D}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.1,-5.8,-7.9,-9.9,-13.5,-16.2,-20.3],'J/(mol*K)'),
        H298 = (376.2,'kJ/mol'),
        S298 = (6.7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 343,
    label = "CC(C)2CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 {1,S} {6,D}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.7,-5,-7.4,-9.6,-13.1,-15.6,-19.9],'J/(mol*K)'),
        H298 = (373.3,'kJ/mol'),
        S298 = (7.5,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 344,
    label = "CC(C)(C=O)CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.7,-4,-5.4,-7.2,-10.9,-13.9,-18.6],'J/(mol*K)'),
        H298 = (375.2,'kJ/mol'),
        S298 = (10.4,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 345,
    label = "C=CC(C)(C=O)CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   C   u0 {1,S}
6   C   u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.5,2.6,-2.4,-6.5,-12,-15.3,-19.7],'J/(mol*K)'),
        H298 = (373.6,'kJ/mol'),
        S298 = (1.2,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 346,
    label = "C=CC(C)2CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5,-4.2,-7,-9.3,-12.8,-15.4,-19.4],'J/(mol*K)'),
        H298 = (371.9,'kJ/mol'),
        S298 = (10.6,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 347,
    label = "CC(C)(O)CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 {1,S} {6,D}
3   C   u0 {1,S}
4   O2s u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.9,-2.6,-5.6,-8.1,-12,-14.9,-19.6],'J/(mol*K)'),
        H298 = (374.9,'kJ/mol'),
        S298 = (6.8,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 348,
    label = "C=CC(C)(O)CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   O2s u0 {1,S}
5   C   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1,-4.5,-7.4,-9.7,-12.7,-15.1,-19.5],'J/(mol*K)'),
        H298 = (375.3,'kJ/mol'),
        S298 = (8.7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 349,
    label = "CCCJ=O",
    group = 
"""
1 * CO  u1 {2,S} {4,D}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S}
4   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.7,-3.9,-7,-9.9,-14.5,-17.5,-21.4],'J/(mol*K)'),
        H298 = (378,'kJ/mol'),
        S298 = (8.3,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 350,
    label = "C=OCCJ=O",
    group = 
"""
1   C   u0 {2,S} {3,S}
2 * CO  u1 {1,S} {4,D}
3   CO  u0 {1,S} {5,D}
4   O2d u0 {2,D}
5   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.2,1.4,-2.8,-6.4,-12,-15.8,-20.4],'J/(mol*K)'),
        H298 = (379.4,'kJ/mol'),
        S298 = (0.8,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 351,
    label = "C=OC=OCJ=O",
    group = 
"""
1   CO  u0 {2,S} {3,S} {4,D}
2 * CO  u1 {1,S} {5,D}
3   CO  u0 {1,S} {6,D}
4   O2d u0 {1,D}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.2,-4.6,-4.4,-4.5,-4.9,-5.7,-7.8],'J/(mol*K)'),
        H298 = (330.2,'kJ/mol'),
        S298 = (-19.6,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 352,
    label = "C=C(C)CJ=O",
    group = 
"""
1   Cd  u0 {2,S} {3,S} {4,D}
2 * CO  u1 {1,S} {5,D}
3   C   u0 {1,S}
4   C   u0 {1,D}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-3.8,-6.4,-8.8,-12.5,-15.3,-19.5],'J/(mol*K)'),
        H298 = (381.7,'kJ/mol'),
        S298 = (6.7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 353,
    label = "CsCJ=O",
    group = 
"""
1 * CO  u1 {2,D} {3,S}
2   O2d u0 {1,D}
3   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.83,-1.43,-1.96,-2.42,-3.16,-3.73,-4.64],'cal/(mol*K)'),
        H298 = (89,'kcal/mol'),
        S298 = (1.12,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 354,
    label = "COJ-CsO2d-HHN3s_684",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 p0 c0 {1,S} {6,D}
3   N3s u0 p1 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   O2d u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.48117,-3.14277,-5.60868,-8.30264,-12.813,-15.3964,-19.5699],'J/(mol*K)'),
        H298 = (370.516,'kJ/mol'),
        S298 = (2.92551,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 355,
    label = "C=CCJ=O",
    group = 
"""
1 * CO  u1 {2,S} {3,D}
2   Cd  u0 {1,S} {4,D}
3   O2d u0 {1,D}
4   Cd  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.3,2.5,-1.1,-4.5,-9.9,-13.7,-18.9],'J/(mol*K)'),
        H298 = (379.9,'kJ/mol'),
        S298 = (7.2,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 356,
    label = "OC=OCJ=O",
    group = 
"""
1   CO  u0 {2,S} {3,S} {4,D}
2 * CO  u1 {1,S} {5,D}
3   O2s u0 {1,S}
4   O2d u0 {1,D}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3,-4.7,-7,-9.5,-14,-17.2,-21.1],'J/(mol*K)'),
        H298 = (376.2,'kJ/mol'),
        S298 = (4.6,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 357,
    label = "COJ-CdO2d-HN3d_500",
    group = 
"""
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2 * CO  u1 p0 c0 {1,S} {5,D}
3   N3d u0 p1 c0 {1,D}
4   H   u0 p0 c0 {1,S}
5   O2d u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.192035,-1.83612,-4.24772,-6.71145,-10.8895,-14.1732,-19.2774],'J/(mol*K)'),
        H298 = (382.213,'kJ/mol'),
        S298 = (3.3685,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 358,
    label = "COJ-CdO2d-HN5dc_678",
    group = 
"""
1   Cd   u0 p0 c0 {2,S} {3,D} {4,S}
2 * CO   u1 p0 c0 {1,S} {5,D}
3   N5dc u0 p0 c+1 {1,D}
4   H    u0 p0 c0 {1,S}
5   O2d  u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.83531,3.43194,-0.462495,-3.86978,-9.39746,-13.4795,-19.2177],'J/(mol*K)'),
        H298 = (361.089,'kJ/mol'),
        S298 = (23.1185,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 359,
    label = "(O)CJO",
    group = 
"""
1 * CO  u1 {2,D} {3,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
""",
    thermo = '(O)CJOC',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 360,
    label = "(O)CJOH",
    group = 
"""
1 * CO  u1 {2,S} {3,D}
2   O2s u0 {1,S} {4,S}
3   O2d u0 {1,D}
4   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.02,-0.66,-1.4,-2.12,-3.41,-4.44,-5.79],'cal/(mol*K)'),
        H298 = (100.75,'kcal/mol'),
        S298 = (0.78,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN #""",
    longDesc = 
"""

""",
)

entry(
    index = 361,
    label = "(O)CJOC",
    group = 
"""
1 * CO  u1 {2,S} {3,D}
2   O2s u0 {1,S} {4,S}
3   O2d u0 {1,D}
4   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.2,-0.2,-3.5,-6.5,-10.9,-13.6,-17],'J/(mol*K)'),
        H298 = (415.2,'kJ/mol'),
        S298 = (-4.3,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 362,
    label = "(O)CJOCH3",
    group = 
"""
1   Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   O2s u0 {1,S} {3,S}
3 * CO  u1 {2,S} {7,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.51,-0.11,-0.94,-1.8,-3.34,-4.48,-5.79],'cal/(mol*K)'),
        H298 = (100.1,'kcal/mol'),
        S298 = (0.72,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 363,
    label = "(O)CJOCC",
    group = 
"""
1   Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   O2s u0 {1,S} {3,S}
3 * CO  u1 {2,S} {7,D}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.45,-0.13,-0.98,-1.86,-3.43,-4.56,-5.79],'cal/(mol*K)'),
        H298 = (99.49,'kcal/mol'),
        S298 = (0.55,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN (values from (O)CJOCH2CH3)""",
    longDesc = 
"""

""",
)

entry(
    index = 364,
    label = "(O)CJOCC2",
    group = 
"""
1   Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   O2s u0 {1,S} {3,S}
3 * CO  u1 {2,S} {7,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.74,-0.06,-1.04,-2.01,-3.6,-4.66,-5.77],'cal/(mol*K)'),
        H298 = (98.99,'kcal/mol'),
        S298 = (0.82,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN (values from (O)CJOCH(CH3)2)""",
    longDesc = 
"""

""",
)

entry(
    index = 365,
    label = "(O)CJOCC3",
    group = 
"""
1   Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   O2s u0 {1,S} {3,S}
3 * CO  u1 {2,S} {7,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   C   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.11,-0.79,-1.8,-2.73,-4.17,-5.06,-5.87],'cal/(mol*K)'),
        H298 = (97.98,'kcal/mol'),
        S298 = (0.76,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN (values from (O)CJOC(CH3)3)""",
    longDesc = 
"""

""",
)

entry(
    index = 366,
    label = "COJ-O2dO2s-N3s_703",
    group = 
"""
1   O2s u0 p2 c0 {2,S} {4,S}
2 * CO  u1 p0 c0 {1,S} {3,D}
3   O2d u0 p2 c0 {2,D}
4   N3s u0 p1 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.848739,-2.08671,-4.72616,-7.05181,-11.0136,-14.2311,-18.7569],'J/(mol*K)'),
        H298 = (416.584,'kJ/mol'),
        S298 = (14.144,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 367,
    label = "SCJ=O",
    group = 
"""
1 * CO  u1 {2,D} {3,S}
2   O2d u0 {1,D}
3   S   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.3,-0.86,-1.5,-2.06,-2.99,-3.68,-4.7],'cal/(mol*K)'),
        H298 = (86.68,'kcal/mol'),
        S298 = (-1.02,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 368,
    label = "COJ-N1scO2d_623",
    group = 
"""
1 * CO   u1 p0 c0 {2,D} {3,S}
2   O2d  u0 p2 c0 {1,D}
3   N1sc u0 p2 c-1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.77774,-0.0905579,-3.23213,-6.03472,-10.718,-14.3234,-19.7244],'J/(mol*K)'),
        H298 = (312.7,'kJ/mol'),
        S298 = (11.6047,'J/(mol*K)'),
    ),
    shortDesc = """Average from child nodes: COJ-N1scO2d-N5dc_622""",
    longDesc = 
"""

""",
)

entry(
    index = 369,
    label = "COJ-N1scO2d-N5dc_622",
    group = 
"""
1   N1sc u0 p2 c-1 {2,S} {4,S}
2 * CO   u1 p0 c0 {1,S} {3,D}
3   O2d  u0 p2 c0 {2,D}
4   N5dc u0 p0 c+1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.77774,-0.0905579,-3.23213,-6.03472,-10.718,-14.3234,-19.7244],'J/(mol*K)'),
        H298 = (312.7,'kJ/mol'),
        S298 = (11.6047,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 370,
    label = "COJ-N3dO2d_626",
    group = 
"""
1 * CO  u1 p0 c0 {2,D} {3,S}
2   O2d u0 p2 c0 {1,D}
3   N3d u0 p1 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.17041,2.28588,-1.42566,-5.09635,-10.9899,-14.4708,-19.5119],'J/(mol*K)'),
        H298 = (315.527,'kJ/mol'),
        S298 = (3.28939,'J/(mol*K)'),
    ),
    shortDesc = """Average from child nodes: COJ-N3dO2d-Cd_625""",
    longDesc = 
"""

""",
)

entry(
    index = 371,
    label = "COJ-N3dO2d-Cd_625",
    group = 
"""
1   N3d u0 p1 c0 {2,S} {4,D}
2 * CO  u1 p0 c0 {1,S} {3,D}
3   O2d u0 p2 c0 {2,D}
4   Cd  u0 p0 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.17041,2.28588,-1.42566,-5.09635,-10.9899,-14.4708,-19.5119],'J/(mol*K)'),
        H298 = (315.527,'kJ/mol'),
        S298 = (3.28939,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 372,
    label = "COJ-N3sO2d_646",
    group = 
"""
1 * CO  u1 p0 c0 {2,D} {3,S}
2   O2d u0 p2 c0 {1,D}
3   N3s u0 p1 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.802773,-3.27007,-5.66483,-7.99595,-12.1524,-15.0459,-19.1834],'J/(mol*K)'),
        H298 = (395.157,'kJ/mol','+|-',6.5918),
        S298 = (4.06196,'J/(mol*K)','+|-',19.3418),
    ),
    shortDesc = """Average from child nodes: COJ-N3sO2d-HO2s_645 COJ-N3sO2d-CsH_715""",
    longDesc = 
"""

""",
)

entry(
    index = 373,
    label = "COJ-N3sO2d-HO2s_645",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {3,S} {4,S}
2 * CO  u1 p0 c0 {1,S} {5,D}
3   O2s u0 p2 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   O2d u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.29969,-2.11693,-5.20579,-7.65912,-11.6639,-14.6757,-19.2352],'J/(mol*K)'),
        H298 = (397.487,'kJ/mol'),
        S298 = (10.9003,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 374,
    label = "COJ-N3sO2d-CsH_715",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {3,S} {4,S}
2 * CO  u1 p0 c0 {1,S} {5,D}
3   Cs  u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   O2d u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.90524,-4.4232,-6.12387,-8.33278,-12.6409,-15.4162,-19.1315],'J/(mol*K)'),
        H298 = (392.826,'kJ/mol'),
        S298 = (-2.77639,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 375,
    label = "Cds_P",
    group = 
"""
1 * Cd u1 {2,D} {3,S}
2   C  u0 {1,D}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.19,-0.75,-1.36,-1.92,-2.82,-3.49,-4.53],'cal/(mol*K)'),
        H298 = (111.2,'kcal/mol'),
        S298 = (1.39,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 376,
    label = "C=C=CJ",
    group = 
"""
1 * Cd  u1 {2,D} {3,S}
2   Cdd u0 {1,D} {4,D}
3   H   u0 {1,S}
4   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.45,-1.05,-1.64,-2.15,-2.98,-3.6,-3.6],'cal/(mol*K)'),
        H298 = (89,'kcal/mol'),
        S298 = (1.29,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 377,
    label = "CdJ-CdH-HN3d_468",
    group = 
"""
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2 * Cd  u1 p0 c0 {1,D} {5,S}
3   N3d u0 p1 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.522639,-2.45963,-4.90407,-7.18967,-11.0001,-13.9474,-18.5753],'J/(mol*K)'),
        H298 = (479.135,'kJ/mol'),
        S298 = (5.81025,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 378,
    label = "CdJ-CddH-N3d_485",
    group = 
"""
1   Cdd u0 p0 c0 {2,D} {4,D}
2 * Cd  u1 p0 c0 {1,D} {3,S}
3   H   u0 p0 c0 {2,S}
4   N3d u0 p1 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.58163,-0.833069,-3.74531,-6.4892,-10.9068,-14.152,-18.8342],'J/(mol*K)'),
        H298 = (409.932,'kJ/mol'),
        S298 = (2.51553,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 379,
    label = "CdJ-CdH-HN3s_542",
    group = 
"""
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2 * Cd  u1 p0 c0 {1,D} {5,S}
3   N3s u0 p1 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0342899,-2.32653,-4.73631,-7.04933,-10.8991,-13.8558,-18.4485],'J/(mol*K)'),
        H298 = (470.731,'kJ/mol'),
        S298 = (4.11829,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 380,
    label = "CdJ-CdH-HN1sc_613",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 * Cd   u1 p0 c0 {1,D} {5,S}
3   N1sc u0 p2 c-1 {1,S}
4   H    u0 p0 c0 {1,S}
5   H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.91217,-3.19904,-4.94245,-7.10913,-10.8473,-13.8101,-18.5802],'J/(mol*K)'),
        H298 = (467.778,'kJ/mol'),
        S298 = (0.174907,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 381,
    label = "CdJ-CddH-N5dc_671",
    group = 
"""
1   Cdd  u0 p0 c0 {2,D} {4,D}
2 * Cd   u1 p0 c0 {1,D} {3,S}
3   H    u0 p0 c0 {2,S}
4   N5dc u0 p0 c+1 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.981745,-0.264815,-3.44602,-6.76682,-11.5616,-14.8812,-20.0773],'J/(mol*K)'),
        H298 = (306.071,'kJ/mol'),
        S298 = (-0.645425,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 382,
    label = "Cds_S",
    group = 
"""
1 * Cd u1 {2,D} {3,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (109,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 383,
    label = "C=CJC=O",
    group = 
"""
1 * Cd  u1 {2,S} {3,D}
2   CO  u0 {1,S} {4,D}
3   C   u0 {1,D}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.4,-2.2,-4.8,-7.2,-11.6,-15.5,-22],'J/(mol*K)'),
        H298 = (462.3,'kJ/mol'),
        S298 = (9.6,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 384,
    label = "C=CJC=C",
    group = 
"""
1 * Cd      u1 {2,D} {3,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.19,-0.76,-1.51,-2.01,-2.7,-3.17,-3.17],'cal/(mol*K)'),
        H298 = (99.8,'kcal/mol'),
        S298 = (0.71,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 385,
    label = "cyclobutadiene-C1",
    group = 
"""
1 * Cd u1 {2,D} {4,S}
2   Cd u0 {1,D} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {1,S} {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (104.6,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 386,
    label = "bicyclo[2.2.0]hexa-1(4),2,5-triene-C2",
    group = 
"""
1   Cd u0 {2,D} {3,S} {6,S}
2   Cd u0 {1,D} {4,S} {5,S}
3 * Cd u1 {1,S} {4,D}
4   Cd u0 {2,S} {3,D}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (102.9,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 387,
    label = "1,3-cyclopentadiene-vinyl-2",
    group = 
"""
1   C  u0 {2,S} {3,S}
2   Cd u0 {1,S} {4,D}
3   Cd u0 {1,S} {5,D}
4 * Cd u1 {2,D} {5,S}
5   Cd u0 {3,D} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (116.2,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 388,
    label = "CdJ-CdCd-HHHN5dc_547",
    group = 
"""
1   Cd   u0 p0 c0 {3,S} {4,D} {5,S}
2   Cd   u0 p0 c0 {3,D} {6,S} {7,S}
3 * Cd   u1 p0 c0 {1,S} {2,D}
4   N5dc u0 p0 c+1 {1,D}
5   H    u0 p0 c0 {1,S}
6   H    u0 p0 c0 {2,S}
7   H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.52613,0.43184,-2.9806,-5.80051,-10.3339,-13.6663,-18.536],'J/(mol*K)'),
        H298 = (383.592,'kJ/mol'),
        S298 = (14.8761,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 389,
    label = "CdJ-CdCd-HHHN3d_606",
    group = 
"""
1   Cd  u0 p0 c0 {3,S} {4,D} {5,S}
2   Cd  u0 p0 c0 {3,D} {6,S} {7,S}
3 * Cd  u1 p0 c0 {1,S} {2,D}
4   N3d u0 p1 c0 {1,D}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.34223,-0.552576,-3.27959,-5.88753,-10.1586,-13.3797,-18.2485],'J/(mol*K)'),
        H298 = (441.053,'kJ/mol'),
        S298 = (8.24859,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 390,
    label = "cyclopropenyl-vinyl",
    group = 
"""
1   C  u0 {2,S} {3,S}
2 * Cd u1 {1,S} {3,D}
3   Cd u0 {1,S} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (106.7,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Fattahi, A.; McCarthy, R. E.; Ahmad, M. R.; Kass, S. R., "Why Does Cyclopropene Have the Acidity of an Acetylene but the Bond Energy of Methane?," J. Am. Chem. Soc. 2003, 125, 11746-11750, DOI: 10.1021/ja035725s. S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 391,
    label = "cyclobutene-vinyl",
    group = 
"""
1   C  u0 {2,S} {4,S}
2   C  u0 {1,S} {3,S}
3 * Cd u1 {2,S} {4,D}
4   Cd u0 {1,S} {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (112.5,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Tian, Z.; Fattahi, A.; Lis, L.; Kass, S. R., "Cycloalkane and Cycloalkene C-H Bond Dissociation Energies," J. Am. Chem. Soc. 2006, 128, 17087-17092, DOI: 10.1021/ja065348u S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 392,
    label = "bicyclo[2.1.0]pent-2-ene-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   C  u0 {1,S} {2,S}
4 * Cd u1 {2,S} {5,D}
5   Cd u0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (109.8,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 393,
    label = "tricyclo[2.1.1.0(1,4)]hex-2-ene-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {4,S} {5,S}
3   C  u0 {1,S} {2,S}
4   C  u0 {1,S} {2,S}
5 * Cd u1 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (108.6,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 394,
    label = "bicyclo[2.2.0]hexa-2,5-diene-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cd u1 {1,S} {4,D}
4   Cd u0 {2,S} {3,D}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (111.6,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 395,
    label = "cyclopentene-vinyl",
    group = 
"""
1   C  u0 {2,S} {3,S}
2   C  u0 {1,S} {5,S}
3   C  u0 {1,S} {4,S}
4 * Cd u1 {3,S} {5,D}
5   Cd u0 {2,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (113.7,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 396,
    label = "bicyclo[2.1.1]hex-2-ene-C2",
    group = 
"""
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   C  u0 {1,S} {2,S}
4   C  u0 {1,S} {2,S}
5 * Cd u1 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (115.9,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 397,
    label = "1,3-cyclopentadiene-vinyl-1",
    group = 
"""
1   C  u0 {2,S} {3,S}
2 * Cd u1 {1,S} {4,D}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {2,D} {5,S}
5   Cd u0 {3,D} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (116.9,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 398,
    label = "CCCJ=C=O",
    group = 
"""
1 * Cd  u1 {2,S} {3,D}
2   C   u0 {1,S} {4,S}
3   Cdd u0 {1,D} {5,D}
4   C   u0 {2,S}
5   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.6,-3,-4.9,-6.5,-9.4,-11.6,-15.1],'J/(mol*K)'),
        H298 = (420.2,'kJ/mol'),
        S298 = (-2.3,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 399,
    label = "CC(C)CJ=C=O",
    group = 
"""
1   Cs  u0 {2,S} {4,S} {5,S}
2 * Cd  u1 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.8,-3.6,-6,-7.8,-10.6,-12.6,-15.8],'J/(mol*K)'),
        H298 = (424,'kJ/mol'),
        S298 = (1.7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 400,
    label = "C=C(C)CJ=C=O",
    group = 
"""
1   Cd  u0 {2,S} {4,D} {5,S}
2 * Cd  u1 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   C   u0 {1,D}
5   C   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.5,-13.7,-14.6,-15,-15.7,-16.3,-17.8],'J/(mol*K)'),
        H298 = (404,'kJ/mol'),
        S298 = (5.6,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 401,
    label = "OC=CJCb",
    group = 
"""
1 * Cd  u1 {2,D} {3,S}
2   C   u0 {1,D} {4,S}
3   Cb  u0 {1,S}
4   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.047,0.607,0.374,-0.3,-1.28,-1.972,-3.196],'cal/(mol*K)'),
        H298 = (123.797,'kcal/mol'),
        S298 = (2.661,'cal/(mol*K)'),
    ),
    shortDesc = """Fit to CCSD(T)-F12/cc-pVDZ-F12//M06/vtz calculations""",
    longDesc = 
"""
Fit to CCSD(T)-F12/cc-pVDZ-F12//M06/vtz calculations for OC=[C]c1ccccc1
""",
)

entry(
    index = 402,
    label = "CdJ-CdCt-HHN3t_502",
    group = 
"""
1   Cd  u0 p0 c0 {2,D} {4,S} {5,S}
2 * Cd  u1 p0 c0 {1,D} {3,S}
3   Ct  u0 p0 c0 {2,S} {6,T}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   N3t u0 p1 c0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.85741,-1.07091,-4.09582,-6.61643,-10.6309,-13.563,-17.9737],'J/(mol*K)'),
        H298 = (456.818,'kJ/mol'),
        S298 = (22.4618,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 403,
    label = "CdJ-CdCs-HHHHN3s_545",
    group = 
"""
1   Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   Cd  u0 p0 c0 {3,D} {7,S} {8,S}
3 * Cd  u1 p0 c0 {1,S} {2,D}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   N3s u0 p1 c0 {2,S}
8   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.408743,-3.31837,-6.03496,-8.37432,-12.0838,-14.7628,-18.6363],'J/(mol*K)'),
        H298 = (457.025,'kJ/mol'),
        S298 = (-4.7331,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 404,
    label = "CdJ-CdCs-HHHHN3s_553",
    group = 
"""
1   Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   Cd  u0 p0 c0 {3,D} {7,S} {8,S}
3 * Cd  u1 p0 c0 {1,S} {2,D}
4   N3s u0 p1 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.685024,-2.21761,-5.00729,-7.42315,-11.3004,-14.1626,-18.5125],'J/(mol*K)'),
        H298 = (447.892,'kJ/mol'),
        S298 = (8.88189,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 405,
    label = "CdJ-CddCs-HHHN3d_630",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   Cdd u0 p0 c0 {2,D} {7,D}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   N3d u0 p1 c0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.13654,-2.30015,-5.25503,-7.74303,-11.692,-14.5467,-18.6732],'J/(mol*K)'),
        H298 = (405.888,'kJ/mol'),
        S298 = (16.7517,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 406,
    label = "CdJ-CddCs-HHHN5dc_718",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cd   u1 p0 c0 {1,S} {3,D}
3   Cdd  u0 p0 c0 {2,D} {7,D}
4   H    u0 p0 c0 {1,S}
5   H    u0 p0 c0 {1,S}
6   H    u0 p0 c0 {1,S}
7   N5dc u0 p0 c+1 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0657357,-2.83214,-5.50345,-8.20665,-12.9366,-15.9863,-19.6947],'J/(mol*K)'),
        H298 = (294.714,'kJ/mol'),
        S298 = (9.61761,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 407,
    label = "S2s-CJ=C",
    group = 
"""
1 * Cd  u1 {2,S} {3,D}
2   S2s u0 {1,S}
3   C   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.16,-0.48,-1.16,-1.76,-2.68,-3.35,-4.45],'cal/(mol*K)'),
        H298 = (104.73,'kcal/mol'),
        S298 = (0.37,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 408,
    label = "C=CJO",
    group = 
"""
1 * Cd  u1 {2,D} {3,S}
2   C   u0 {1,D}
3   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.1,-11.8,-15.2,-17.2,-19.2,-20.3,-22],'J/(mol*K)'),
        H298 = (457.4,'kJ/mol'),
        S298 = (26.7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 409,
    label = "CdJ-CdO2s-HHN3s_519",
    group = 
"""
1   Cd  u0 p0 c0 {2,D} {4,S} {5,S}
2 * Cd  u1 p0 c0 {1,D} {3,S}
3   O2s u0 p2 c0 {2,S} {6,S}
4   N3s u0 p1 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.615222,-1.49912,-4.35582,-7.11964,-11.4926,-14.6255,-19.0241],'J/(mol*K)'),
        H298 = (466.565,'kJ/mol'),
        S298 = (7.24484,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 410,
    label = "CdJ-CddO2s-HN5dc_527",
    group = 
"""
1 * Cd   u1 p0 c0 {2,S} {3,D}
2   O2s  u0 p2 c0 {1,S} {4,S}
3   Cdd  u0 p0 c0 {1,D} {5,D}
4   H    u0 p0 c0 {2,S}
5   N5dc u0 p0 c+1 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.84075,0.744894,-3.29994,-6.76145,-11.6725,-14.7908,-19.8794],'J/(mol*K)'),
        H298 = (339.151,'kJ/mol'),
        S298 = (5.46555,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 411,
    label = "CdJ-CddO2s-HN3d_536",
    group = 
"""
1 * Cd  u1 p0 c0 {2,S} {3,D}
2   O2s u0 p2 c0 {1,S} {4,S}
3   Cdd u0 p0 c0 {1,D} {5,D}
4   H   u0 p0 c0 {2,S}
5   N3d u0 p1 c0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.0998,-2.44203,-5.52969,-8.01469,-11.9826,-14.8701,-19.0288],'J/(mol*K)'),
        H298 = (412.892,'kJ/mol'),
        S298 = (6.56981,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 412,
    label = "CdJ-CdO2s-HHN3s_543",
    group = 
"""
1   Cd  u0 p0 c0 {2,D} {4,S} {5,S}
2 * Cd  u1 p0 c0 {1,D} {3,S}
3   O2s u0 p2 c0 {2,S} {6,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   N3s u0 p1 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.40164,-0.40794,-3.41037,-5.9988,-9.98598,-13.2118,-18.4725],'J/(mol*K)'),
        H298 = (463.815,'kJ/mol'),
        S298 = (6.7577,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 413,
    label = "CdJ-CdN3d_453",
    group = 
"""
1 * Cd  u1 p0 c0 {2,D} {3,S}
2   N3d u0 p1 c0 {1,D}
3   Cd  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.8851,2.39296,-0.47576,-3.62029,-8.79633,-12.6826,-18.3499],'J/(mol*K)'),
        H298 = (399.068,'kJ/mol'),
        S298 = (7.96614,'J/(mol*K)'),
    ),
    shortDesc = """Average from child nodes: CdJ-CdN3d-CdHH_452""",
    longDesc = 
"""

""",
)

entry(
    index = 414,
    label = "CdJ-CdN3d-CdHH_452",
    group = 
"""
1   Cd  u0 p0 c0 {2,S} {4,D} {5,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   N3d u0 p1 c0 {2,D} {6,S}
4   Cd  u0 p0 c0 {1,D}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.8851,2.39296,-0.47576,-3.62029,-8.79633,-12.6826,-18.3499],'J/(mol*K)'),
        H298 = (399.068,'kJ/mol'),
        S298 = (7.96614,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 415,
    label = "CdJ-HN3d_470",
    group = 
"""
1 * Cd  u1 p0 c0 {2,D} {3,S}
2   N3d u0 p1 c0 {1,D}
3   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.801589,-1.59506,-4.25595,-6.77732,-11.0067,-14.0539,-18.6467],'J/(mol*K)'),
        H298 = (423.674,'kJ/mol','+|-',26.4394),
        S298 = (4.98625,'J/(mol*K)','+|-',6.83272),
    ),
    shortDesc = """Average from child nodes: CdJ-HN3d-O2s_469 CdJ-HN3d-H_507 CdJ-HN3d-N3s_566 CdJ-HN3d-CO_570 CdJ-HN3d-Ct_617 CdJ-HN3d-N3d_624 CdJ-HN3d-Cd_642 CdJ-HN3d-Cs_700""",
    longDesc = 
"""

""",
)

entry(
    index = 416,
    label = "CdJ-HN3d-O2s_469",
    group = 
"""
1   N3d u0 p1 c0 {2,D} {4,S}
2 * Cd  u1 p0 c0 {1,D} {3,S}
3   H   u0 p0 c0 {2,S}
4   O2s u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.75122,-0.687657,-3.67529,-6.44601,-10.8266,-14.0249,-18.7904],'J/(mol*K)'),
        H298 = (441.536,'kJ/mol'),
        S298 = (3.73576,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 417,
    label = "CdJ-HN3d-H_507",
    group = 
"""
1   N3d u0 p1 c0 {2,D} {4,S}
2 * Cd  u1 p0 c0 {1,D} {3,S}
3   H   u0 p0 c0 {2,S}
4   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.306523,-1.60399,-3.61994,-6.05397,-10.482,-13.5737,-18.4167],'J/(mol*K)'),
        H298 = (402.187,'kJ/mol'),
        S298 = (1.42988,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 418,
    label = "CdJ-HN3d-N3s_566",
    group = 
"""
1   N3d u0 p1 c0 {2,D} {4,S}
2 * Cd  u1 p0 c0 {1,D} {3,S}
3   H   u0 p0 c0 {2,S}
4   N3s u0 p1 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.225408,-2.77878,-5.4703,-7.9327,-11.8453,-14.6814,-18.7848],'J/(mol*K)'),
        H298 = (426.878,'kJ/mol'),
        S298 = (5.43637,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 419,
    label = "CdJ-HN3d-CO_570",
    group = 
"""
1   N3d u0 p1 c0 {2,D} {4,S}
2 * Cd  u1 p0 c0 {1,D} {3,S}
3   H   u0 p0 c0 {2,S}
4   CO  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0530271,-1.8967,-4.28444,-6.8993,-11.5745,-14.3142,-18.5889],'J/(mol*K)'),
        H298 = (413.585,'kJ/mol'),
        S298 = (3.65393,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 420,
    label = "CdJ-HN3d-Ct_617",
    group = 
"""
1   N3d u0 p1 c0 {2,D} {4,S}
2 * Cd  u1 p0 c0 {1,D} {3,S}
3   H   u0 p0 c0 {2,S}
4   Ct  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.92364,-2.1828,-5.00109,-7.45398,-11.4147,-14.345,-18.6764],'J/(mol*K)'),
        H298 = (423.017,'kJ/mol'),
        S298 = (4.12544,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 421,
    label = "CdJ-HN3d-N3d_624",
    group = 
"""
1   N3d u0 p1 c0 {2,D} {4,S}
2 * Cd  u1 p0 c0 {1,D} {3,S}
3   H   u0 p0 c0 {2,S}
4   N3d u0 p1 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.45351,-2.15601,-4.73443,-7.11499,-11.0359,-14.0154,-18.6249],'J/(mol*K)'),
        H298 = (429.199,'kJ/mol'),
        S298 = (6.31867,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 422,
    label = "CdJ-HN3d-Cd_642",
    group = 
"""
1   N3d u0 p1 c0 {2,D} {4,S}
2 * Cd  u1 p0 c0 {1,D} {3,S}
3   H   u0 p0 c0 {2,S}
4   Cd  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.74052,1.31587,-1.96457,-4.87759,-9.63542,-13.1983,-18.4398],'J/(mol*K)'),
        H298 = (438.405,'kJ/mol'),
        S298 = (12.5641,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 423,
    label = "CdJ-HN3d-Cs_700",
    group = 
"""
1   N3d u0 p1 c0 {2,D} {4,S}
2 * Cd  u1 p0 c0 {1,D} {3,S}
3   H   u0 p0 c0 {2,S}
4   Cs  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.128776,-2.77041,-5.29757,-7.44005,-11.2394,-14.2781,-18.8513],'J/(mol*K)'),
        H298 = (414.586,'kJ/mol'),
        S298 = (2.62588,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 424,
    label = "CdJ-N3dN3s_473",
    group = 
"""
1 * Cd  u1 p0 c0 {2,S} {3,D}
2   N3s u0 p1 c0 {1,S}
3   N3d u0 p1 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.08418,-0.463191,-4.00068,-6.90519,-11.2504,-14.2245,-18.5406],'J/(mol*K)'),
        H298 = (424.782,'kJ/mol','+|-',36.2418),
        S298 = (10.5906,'J/(mol*K)','+|-',6.39284),
    ),
    shortDesc = """Average from child nodes: CdJ-N3dN3s-HHO2s_472 CdJ-N3dN3s-CsHH_562 CdJ-N3dN3s-HHN3s_586 CdJ-N3dN3s-HHO2s_640 CdJ-N3dN3s-HHH_665 CdJ-N3dN3s-HHN3s_696 CdJ-N3dN3s-CsHH_706""",
    longDesc = 
"""

""",
)

entry(
    index = 425,
    label = "CdJ-N3dN3s-HHO2s_472",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {4,S} {5,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   N3d u0 p1 c0 {2,D} {6,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   O2s u0 p2 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.12791,-1.72802,-5.44785,-7.98162,-11.8911,-14.6657,-18.6038],'J/(mol*K)'),
        H298 = (458.257,'kJ/mol'),
        S298 = (8.9607,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 426,
    label = "CdJ-N3dN3s-CsHH_562",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {4,S} {5,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   N3d u0 p1 c0 {2,D} {6,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   Cs  u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.6548,-2.19385,-5.39198,-8.03167,-12.0366,-14.8778,-19.3681],'J/(mol*K)'),
        H298 = (414.949,'kJ/mol'),
        S298 = (6.98942,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 427,
    label = "CdJ-N3dN3s-HHN3s_586",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {4,S} {5,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   N3d u0 p1 c0 {2,D} {6,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   N3s u0 p1 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.56056,-0.0699533,-3.83106,-6.71232,-11.1814,-14.3104,-18.5983],'J/(mol*K)'),
        H298 = (440.335,'kJ/mol'),
        S298 = (9.78772,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 428,
    label = "CdJ-N3dN3s-HHO2s_640",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {4,S} {5,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   N3d u0 p1 c0 {2,D} {6,S}
4   O2s u0 p2 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.14679,1.59337,-2.51766,-5.71862,-10.6505,-14.0965,-18.7669],'J/(mol*K)'),
        H298 = (421.745,'kJ/mol'),
        S298 = (15.9949,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 429,
    label = "CdJ-N3dN3s-HHH_665",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {4,S} {5,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   N3d u0 p1 c0 {2,D} {6,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.70001,1.20352,-3.06533,-6.70114,-11.0097,-13.7924,-17.1727],'J/(mol*K)'),
        H298 = (406.485,'kJ/mol'),
        S298 = (7.56637,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 430,
    label = "CdJ-N3dN3s-HHN3s_696",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {4,S} {5,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   N3d u0 p1 c0 {2,D} {6,S}
4   N3s u0 p1 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.74384,-0.712039,-3.75663,-6.41442,-10.7277,-13.9443,-18.7623],'J/(mol*K)'),
        H298 = (413.906,'kJ/mol'),
        S298 = (12.3635,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 431,
    label = "CdJ-N3dN3s-CsHH_706",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {4,S} {5,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   N3d u0 p1 c0 {2,D} {6,S}
4   Cs  u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.65536,-1.33536,-3.99424,-6.77658,-11.2559,-13.8845,-18.5122],'J/(mol*K)'),
        H298 = (417.799,'kJ/mol'),
        S298 = (12.4715,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 432,
    label = "CdJ-CsN3d_480",
    group = 
"""
1 * Cd  u1 p0 c0 {2,D} {3,S}
2   N3d u0 p1 c0 {1,D}
3   Cs  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.336014,-2.37874,-5.0871,-7.63526,-11.7433,-14.5843,-18.9743],'J/(mol*K)'),
        H298 = (410.172,'kJ/mol','+|-',34.6547),
        S298 = (0.0183624,'J/(mol*K)','+|-',9.41285),
    ),
    shortDesc = """Average from child nodes: CdJ-CsN3d-HHHN3s_479 CdJ-CsN3d-HHHO2s_504 CdJ-CsN3d-CsHHH_670 CdJ-CsN3d-CsHHH_677 CdJ-CsN3d-HHHN3s_682 CdJ-CsN3d-HHHH_709""",
    longDesc = 
"""

""",
)

entry(
    index = 433,
    label = "CdJ-CsN3d-HHHN3s_479",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   N3d u0 p1 c0 {2,D} {7,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   N3s u0 p1 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.36747,-3.2557,-6.33754,-8.90886,-12.7949,-15.4118,-18.92],'J/(mol*K)'),
        H298 = (418.477,'kJ/mol'),
        S298 = (-0.753499,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 434,
    label = "CdJ-CsN3d-HHHO2s_504",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   N3d u0 p1 c0 {2,D} {7,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   O2s u0 p2 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.23881,-1.07242,-3.9875,-6.54371,-10.7198,-13.8612,-18.6112],'J/(mol*K)'),
        H298 = (441.928,'kJ/mol'),
        S298 = (6.68326,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 435,
    label = "CdJ-CsN3d-CsHHH_670",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   N3d u0 p1 c0 {2,D} {7,S}
4   Cs  u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.348619,-2.27585,-4.61165,-7.06919,-11.4763,-14.3738,-18.7986],'J/(mol*K)'),
        H298 = (398.139,'kJ/mol'),
        S298 = (-1.53931,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 436,
    label = "CdJ-CsN3d-CsHHH_677",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   N3d u0 p1 c0 {2,D} {7,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   Cs  u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.42742,-3.71465,-6.12779,-8.52389,-12.6187,-15.1844,-19.469],'J/(mol*K)'),
        H298 = (404.195,'kJ/mol'),
        S298 = (-5.95045,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 437,
    label = "CdJ-CsN3d-HHHN3s_682",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   N3d u0 p1 c0 {2,D} {7,S}
4   N3s u0 p1 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0602834,-1.86141,-4.70211,-7.52306,-11.5375,-14.3034,-19.1219],'J/(mol*K)'),
        H298 = (398.845,'kJ/mol'),
        S298 = (4.46471,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 438,
    label = "CdJ-CsN3d-HHHH_709",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   N3d u0 p1 c0 {2,D} {7,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.125565,-2.09239,-4.75604,-7.24284,-11.313,-14.3708,-18.9252],'J/(mol*K)'),
        H298 = (399.451,'kJ/mol'),
        S298 = (-2.79453,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 439,
    label = "CdJ-N3dO2s_491",
    group = 
"""
1 * Cd  u1 p0 c0 {2,S} {3,D}
2   O2s u0 p2 c0 {1,S}
3   N3d u0 p1 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.27585,-0.195027,-3.48409,-6.25666,-10.8801,-14.1315,-18.7585],'J/(mol*K)'),
        H298 = (445.705,'kJ/mol','+|-',42.7484),
        S298 = (9.99194,'J/(mol*K)','+|-',15.4166),
    ),
    shortDesc = """Average from child nodes: CdJ-N3dO2s-HO2s_490 CdJ-N3dO2s-HN3s_572 CdJ-N3dO2s-HO2s_639 CdJ-N3dO2s-HN3s_694 CdJ-N3dO2s-CsH_707""",
    longDesc = 
"""

""",
)

entry(
    index = 440,
    label = "CdJ-N3dO2s-HO2s_490",
    group = 
"""
1 * Cd  u1 p0 c0 {2,S} {3,D}
2   O2s u0 p2 c0 {1,S} {4,S}
3   N3d u0 p1 c0 {1,D} {5,S}
4   H   u0 p0 c0 {2,S}
5   O2s u0 p2 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.3389,-1.52025,-5.21071,-7.81026,-11.8458,-14.7358,-18.8446],'J/(mol*K)'),
        H298 = (474.969,'kJ/mol'),
        S298 = (7.29153,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 441,
    label = "CdJ-N3dO2s-HN3s_572",
    group = 
"""
1 * Cd  u1 p0 c0 {2,S} {3,D}
2   O2s u0 p2 c0 {1,S} {4,S}
3   N3d u0 p1 c0 {1,D} {5,S}
4   H   u0 p0 c0 {2,S}
5   N3s u0 p1 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.18849,1.23219,-2.49987,-5.69109,-10.6958,-14.2333,-19.0487],'J/(mol*K)'),
        H298 = (456.246,'kJ/mol'),
        S298 = (9.21825,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 442,
    label = "CdJ-N3dO2s-HO2s_639",
    group = 
"""
1 * Cd  u1 p0 c0 {2,S} {3,D}
2   O2s u0 p2 c0 {1,S} {4,S}
3   N3d u0 p1 c0 {1,D} {5,S}
4   O2s u0 p2 c0 {2,S}
5   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.91908,2.05115,-2.15478,-5.3612,-10.2896,-13.7714,-18.597],'J/(mol*K)'),
        H298 = (447.309,'kJ/mol'),
        S298 = (20.7144,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 443,
    label = "CdJ-N3dO2s-HN3s_694",
    group = 
"""
1 * Cd  u1 p0 c0 {2,S} {3,D}
2   O2s u0 p2 c0 {1,S} {4,S}
3   N3d u0 p1 c0 {1,D} {5,S}
4   N3s u0 p1 c0 {2,S}
5   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.80137,-0.135537,-2.71742,-5.5455,-10.6638,-13.8198,-18.4479],'J/(mol*K)'),
        H298 = (425.213,'kJ/mol'),
        S298 = (13.0214,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 444,
    label = "CdJ-N3dO2s-CsH_707",
    group = 
"""
1 * Cd  u1 p0 c0 {2,S} {3,D}
2   O2s u0 p2 c0 {1,S} {4,S}
3   N3d u0 p1 c0 {1,D} {5,S}
4   Cs  u0 p0 c0 {2,S}
5   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.131394,-2.60269,-4.8377,-6.87525,-10.9056,-14.0973,-18.8545],'J/(mol*K)'),
        H298 = (424.79,'kJ/mol'),
        S298 = (-0.285822,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 445,
    label = "CdJ-CdN3s_506",
    group = 
"""
1 * Cd  u1 p0 c0 {2,S} {3,D}
2   N3s u0 p1 c0 {1,S}
3   Cd  u0 p0 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.989871,-2.21021,-5.17516,-7.62321,-11.4736,-14.3385,-18.5804],'J/(mol*K)'),
        H298 = (447.811,'kJ/mol','+|-',7.79323),
        S298 = (7.80832,'J/(mol*K)','+|-',16.556),
    ),
    shortDesc = """Average from child nodes: CdJ-CdN3s-HHHO2s_505 CdJ-CdN3s-CsHHH_523 CdJ-CdN3s-HHHN3s_532 CdJ-CdN3s-CsHHH_539 CdJ-CdN3s-HHHN3s_544 CdJ-CdN3s-HHHH_591 CdJ-CdN3s-HHHO2s_618""",
    longDesc = 
"""

""",
)

entry(
    index = 446,
    label = "CdJ-CdN3s-HHHO2s_505",
    group = 
"""
1   N3s u0 p1 c0 {3,S} {4,S} {5,S}
2   Cd  u0 p0 c0 {3,D} {6,S} {7,S}
3 * Cd  u1 p0 c0 {1,S} {2,D}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   O2s u0 p2 c0 {2,S}
7   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.760146,-2.59303,-5.81403,-8.33325,-12.2724,-15.0732,-19.0939],'J/(mol*K)'),
        H298 = (447.523,'kJ/mol'),
        S298 = (11.3939,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 447,
    label = "CdJ-CdN3s-CsHHH_523",
    group = 
"""
1   N3s u0 p1 c0 {3,S} {4,S} {5,S}
2   Cd  u0 p0 c0 {3,D} {6,S} {7,S}
3 * Cd  u1 p0 c0 {1,S} {2,D}
4   Cs  u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.32153,-2.75934,-5.69821,-7.83719,-11.0113,-13.8558,-18.5248],'J/(mol*K)'),
        H298 = (449.551,'kJ/mol'),
        S298 = (7.76253,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 448,
    label = "CdJ-CdN3s-HHHN3s_532",
    group = 
"""
1   N3s u0 p1 c0 {3,S} {4,S} {5,S}
2   Cd  u0 p0 c0 {3,D} {6,S} {7,S}
3 * Cd  u1 p0 c0 {1,S} {2,D}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   N3s u0 p1 c0 {2,S}
7   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.43341,-5.15311,-7.19342,-9.18711,-12.4958,-15.0408,-19.0236],'J/(mol*K)'),
        H298 = (443.745,'kJ/mol'),
        S298 = (-2.45328,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 449,
    label = "CdJ-CdN3s-CsHHH_539",
    group = 
"""
1   N3s u0 p1 c0 {3,S} {4,S} {5,S}
2   Cd  u0 p0 c0 {3,D} {6,S} {7,S}
3 * Cd  u1 p0 c0 {1,S} {2,D}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   Cs  u0 p0 c0 {2,S}
7   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.515138,-2.5914,-5.48707,-7.97536,-11.9069,-14.7271,-18.7335],'J/(mol*K)'),
        H298 = (442.611,'kJ/mol'),
        S298 = (-2.74195,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 450,
    label = "CdJ-CdN3s-HHHN3s_544",
    group = 
"""
1   N3s u0 p1 c0 {3,S} {4,S} {5,S}
2   Cd  u0 p0 c0 {3,D} {6,S} {7,S}
3 * Cd  u1 p0 c0 {1,S} {2,D}
4   N3s u0 p1 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.48679,-0.72289,-4.15524,-6.91578,-11.1195,-13.9958,-18.0263],'J/(mol*K)'),
        H298 = (452.987,'kJ/mol'),
        S298 = (20.6911,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 451,
    label = "CdJ-CdN3s-HHHH_591",
    group = 
"""
1   N3s u0 p1 c0 {3,S} {4,S} {5,S}
2   Cd  u0 p0 c0 {3,D} {6,S} {7,S}
3 * Cd  u1 p0 c0 {1,S} {2,D}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.786995,-2.37912,-5.09364,-7.48752,-11.3835,-14.288,-18.5578],'J/(mol*K)'),
        H298 = (446.473,'kJ/mol'),
        S298 = (8.25863,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 452,
    label = "CdJ-CdN3s-HHHO2s_618",
    group = 
"""
1   N3s u0 p1 c0 {3,S} {4,S} {5,S}
2   Cd  u0 p0 c0 {3,D} {6,S} {7,S}
3 * Cd  u1 p0 c0 {1,S} {2,D}
4   O2s u0 p2 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.49191,0.727397,-2.78452,-5.62624,-10.1261,-13.3891,-18.1031],'J/(mol*K)'),
        H298 = (451.79,'kJ/mol'),
        S298 = (11.7473,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 453,
    label = "CdJ-CddN3s_512",
    group = 
"""
1 * Cd  u1 p0 c0 {2,S} {3,D}
2   N3s u0 p1 c0 {1,S}
3   Cdd u0 p0 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.65335,-0.554872,-4.20389,-7.21444,-11.8114,-14.9997,-19.4637],'J/(mol*K)'),
        H298 = (354.98,'kJ/mol','+|-',62.0951),
        S298 = (6.60787,'J/(mol*K)','+|-',16.3618),
    ),
    shortDesc = """Average from child nodes: CdJ-CddN3s-HHN5dc_511 CdJ-CddN3s-CdHH_603 CdJ-CddN3s-HHN3d_657 CdJ-CddN3s-HHO2d_661""",
    longDesc = 
"""

""",
)

entry(
    index = 454,
    label = "CdJ-CddN3s-HHN5dc_511",
    group = 
"""
1   N3s  u0 p1 c0 {2,S} {4,S} {5,S}
2 * Cd   u1 p0 c0 {1,S} {3,D}
3   Cdd  u0 p0 c0 {2,D} {6,D}
4   H    u0 p0 c0 {1,S}
5   H    u0 p0 c0 {1,S}
6   N5dc u0 p0 c+1 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.30075,-0.472827,-4.16595,-7.33317,-11.8987,-14.9971,-20.031],'J/(mol*K)'),
        H298 = (310.981,'kJ/mol'),
        S298 = (3.12981,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 455,
    label = "CdJ-CddN3s-CdHH_603",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {4,S} {5,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   Cdd u0 p0 c0 {2,D} {6,D}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   Cd  u0 p0 c0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.24601,1.86939,-2.18149,-5.44718,-10.5405,-14.1086,-18.8851],'J/(mol*K)'),
        H298 = (374.734,'kJ/mol'),
        S298 = (15.596,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 456,
    label = "CdJ-CddN3s-HHN3d_657",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {4,S} {5,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   Cdd u0 p0 c0 {2,D} {6,D}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   N3d u0 p1 c0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.84044,0.576532,-3.35723,-6.47414,-11.3263,-14.7133,-19.2056],'J/(mol*K)'),
        H298 = (378.76,'kJ/mol'),
        S298 = (10.6616,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 457,
    label = "CdJ-CddN3s-HHO2d_661",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {4,S} {5,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   Cdd u0 p0 c0 {2,D} {6,D}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   O2d u0 p2 c0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.7738,-4.19258,-7.11087,-9.60326,-13.48,-16.1797,-19.7332],'J/(mol*K)'),
        H298 = (355.443,'kJ/mol'),
        S298 = (-2.95594,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 458,
    label = "CdJ-CsN5dc_531",
    group = 
"""
1 * Cd   u1 p0 c0 {2,D} {3,S}
2   N5dc u0 p0 c+1 {1,D}
3   Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.04921,-3.25612,-5.82026,-8.3178,-11.9099,-14.2453,-18.6405],'J/(mol*K)'),
        H298 = (476.28,'kJ/mol','+|-',18.693),
        S298 = (0.816782,'J/(mol*K)','+|-',15.4521),
    ),
    shortDesc = """Average from child nodes: CdJ-CsN5dc-HHHHO0sc_530 CdJ-CsN5dc-HHHN3sO0sc_596 CdJ-CsN5dc-HHHO0scO2s_602 CdJ-CsN5dc-CsHHHO0sc_660""",
    longDesc = 
"""

""",
)

entry(
    index = 459,
    label = "CdJ-CsN5dc-HHHHO0sc_530",
    group = 
"""
1   Cs   u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   N5dc u0 p0 c+1 {3,D} {7,S} {8,S}
3 * Cd   u1 p0 c0 {1,S} {2,D}
4   H    u0 p0 c0 {1,S}
5   H    u0 p0 c0 {1,S}
6   H    u0 p0 c0 {1,S}
7   O0sc u0 p3 c-1 {2,S}
8   H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.688023,-2.61068,-4.90445,-7.6006,-12.1186,-14.4574,-18.4818],'J/(mol*K)'),
        H298 = (484.309,'kJ/mol'),
        S298 = (2.47204,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 460,
    label = "CdJ-CsN5dc-HHHN3sO0sc_596",
    group = 
"""
1   Cs   u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   N5dc u0 p0 c+1 {3,D} {7,S} {8,S}
3 * Cd   u1 p0 c0 {1,S} {2,D}
4   N3s  u0 p1 c0 {1,S}
5   H    u0 p0 c0 {1,S}
6   H    u0 p0 c0 {1,S}
7   O0sc u0 p3 c-1 {2,S}
8   H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.216262,-3.01431,-5.59085,-7.85195,-11.5534,-14.3506,-18.6468],'J/(mol*K)'),
        H298 = (477.357,'kJ/mol'),
        S298 = (8.82883,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 461,
    label = "CdJ-CsN5dc-HHHO0scO2s_602",
    group = 
"""
1   Cs   u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   N5dc u0 p0 c+1 {3,D} {7,S} {8,S}
3 * Cd   u1 p0 c0 {1,S} {2,D}
4   O2s  u0 p2 c0 {1,S}
5   H    u0 p0 c0 {1,S}
6   H    u0 p0 c0 {1,S}
7   O0sc u0 p3 c-1 {2,S}
8   H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.99546,-4.85659,-7.00115,-9.35247,-12.3633,-14.3002,-18.6193],'J/(mol*K)'),
        H298 = (462.924,'kJ/mol'),
        S298 = (-9.73591,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 462,
    label = "CdJ-CsN5dc-CsHHHO0sc_660",
    group = 
"""
1   Cs   u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   N5dc u0 p0 c+1 {3,D} {7,S} {8,S}
3 * Cd   u1 p0 c0 {1,S} {2,D}
4   Cs   u0 p0 c0 {1,S}
5   H    u0 p0 c0 {1,S}
6   H    u0 p0 c0 {1,S}
7   O0sc u0 p3 c-1 {2,S}
8   H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.702923,-2.5429,-5.78458,-8.46619,-11.6041,-13.8731,-18.8141],'J/(mol*K)'),
        H298 = (480.532,'kJ/mol'),
        S298 = (1.70218,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 463,
    label = "CdJ-N3sN5dc_552",
    group = 
"""
1 * Cd   u1 p0 c0 {2,S} {3,D}
2   N3s  u0 p1 c0 {1,S}
3   N5dc u0 p0 c+1 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.90442,-5.07532,-7.09337,-9.07901,-12.4461,-14.928,-19.0015],'J/(mol*K)'),
        H298 = (400.908,'kJ/mol','+|-',39.6031),
        S298 = (1.4727,'J/(mol*K)','+|-',10.9847),
    ),
    shortDesc = """Average from child nodes: CdJ-N3sN5dc-HHO0scO2s_551 CdJ-N3sN5dc-HHN3sO0sc_554 CdJ-N3sN5dc-CsHHO0sc_681 CdJ-N3sN5dc-HHHO0sc_704""",
    longDesc = 
"""

""",
)

entry(
    index = 464,
    label = "CdJ-N3sN5dc-HHO0scO2s_551",
    group = 
"""
1   N3s  u0 p1 c0 {3,S} {4,S} {5,S}
2   N5dc u0 p0 c+1 {3,D} {6,S} {7,S}
3 * Cd   u1 p0 c0 {1,S} {2,D}
4   O2s  u0 p2 c0 {1,S}
5   H    u0 p0 c0 {1,S}
6   O0sc u0 p3 c-1 {2,S}
7   H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.87076,-5.52203,-7.17562,-9.0399,-12.3029,-14.9058,-19.1826],'J/(mol*K)'),
        H298 = (375.125,'kJ/mol'),
        S298 = (0.389768,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 465,
    label = "CdJ-N3sN5dc-HHN3sO0sc_554",
    group = 
"""
1   N3s  u0 p1 c0 {3,S} {4,S} {5,S}
2   N5dc u0 p0 c+1 {3,D} {6,S} {7,S}
3 * Cd   u1 p0 c0 {1,S} {2,D}
4   N3s  u0 p1 c0 {1,S}
5   H    u0 p0 c0 {1,S}
6   O0sc u0 p3 c-1 {2,S}
7   H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.72978,-4.99026,-7.20765,-9.09278,-12.2644,-14.7583,-18.8428],'J/(mol*K)'),
        H298 = (397.247,'kJ/mol'),
        S298 = (4.96521,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 466,
    label = "CdJ-N3sN5dc-CsHHO0sc_681",
    group = 
"""
1   N3s  u0 p1 c0 {3,S} {4,S} {5,S}
2   N5dc u0 p0 c+1 {3,D} {6,S} {7,S}
3 * Cd   u1 p0 c0 {1,S} {2,D}
4   Cs   u0 p0 c0 {1,S}
5   H    u0 p0 c0 {1,S}
6   O0sc u0 p3 c-1 {2,S}
7   H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.11273,-4.79053,-6.75902,-8.87257,-12.5603,-14.9201,-19.0924],'J/(mol*K)'),
        H298 = (421.316,'kJ/mol'),
        S298 = (-5.82407,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 467,
    label = "CdJ-N3sN5dc-HHHO0sc_704",
    group = 
"""
1   N3s  u0 p1 c0 {3,S} {4,S} {5,S}
2   N5dc u0 p0 c+1 {3,D} {6,S} {7,S}
3 * Cd   u1 p0 c0 {1,S} {2,D}
4   H    u0 p0 c0 {1,S}
5   H    u0 p0 c0 {1,S}
6   O0sc u0 p3 c-1 {2,S}
7   H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.90442,-4.99847,-7.23119,-9.31078,-12.6569,-15.1277,-18.8881],'J/(mol*K)'),
        H298 = (409.944,'kJ/mol'),
        S298 = (6.35987,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 468,
    label = "CdJ-HN5dc_577",
    group = 
"""
1 * Cd   u1 p0 c0 {2,D} {3,S}
2   N5dc u0 p0 c+1 {1,D}
3   H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.34221,-0.597309,-4.01019,-6.64199,-10.5522,-13.4802,-17.9919],'J/(mol*K)'),
        H298 = (498.304,'kJ/mol'),
        S298 = (22.8724,'J/(mol*K)'),
    ),
    shortDesc = """Average from child nodes: CdJ-HN5dc-HO0sc_576""",
    longDesc = 
"""

""",
)

entry(
    index = 469,
    label = "CdJ-HN5dc-HO0sc_576",
    group = 
"""
1   N5dc u0 p0 c+1 {2,D} {3,S} {4,S}
2 * Cd   u1 p0 c0 {1,D} {5,S}
3   O0sc u0 p3 c-1 {1,S}
4   H    u0 p0 c0 {1,S}
5   H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.34221,-0.597309,-4.01019,-6.64199,-10.5522,-13.4802,-17.9919],'J/(mol*K)'),
        H298 = (498.304,'kJ/mol'),
        S298 = (22.8724,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 470,
    label = "CdJ-N1scN3d_580",
    group = 
"""
1 * Cd   u1 p0 c0 {2,S} {3,D}
2   N1sc u0 p2 c-1 {1,S}
3   N3d  u0 p1 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.30772,4.41999,0.363214,-3.58117,-9.51127,-12.9966,-19.0256],'J/(mol*K)'),
        H298 = (341.839,'kJ/mol'),
        S298 = (6.18198,'J/(mol*K)'),
    ),
    shortDesc = """Average from child nodes: CdJ-N1scN3d-HN5dc_579""",
    longDesc = 
"""

""",
)

entry(
    index = 471,
    label = "CdJ-N1scN3d-HN5dc_579",
    group = 
"""
1 * Cd   u1 p0 c0 {2,S} {3,D}
2   N1sc u0 p2 c-1 {1,S} {4,S}
3   N3d  u0 p1 c0 {1,D} {5,S}
4   N5dc u0 p0 c+1 {2,S}
5   H    u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.30772,4.41999,0.363214,-3.58117,-9.51127,-12.9966,-19.0256],'J/(mol*K)'),
        H298 = (341.839,'kJ/mol'),
        S298 = (6.18198,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 472,
    label = "CdJ-CON3d_610",
    group = 
"""
1 * Cd  u1 p0 c0 {2,D} {3,S}
2   N3d u0 p1 c0 {1,D}
3   CO  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.963833,-1.39916,-3.95901,-6.29064,-10.307,-13.5377,-18.7854],'J/(mol*K)'),
        H298 = (401.158,'kJ/mol'),
        S298 = (6.48994,'J/(mol*K)'),
    ),
    shortDesc = """Average from child nodes: CdJ-CON3d-HHO2d_609""",
    longDesc = 
"""

""",
)

entry(
    index = 473,
    label = "CdJ-CON3d-HHO2d_609",
    group = 
"""
1   CO  u0 p0 c0 {2,S} {4,D} {5,S}
2 * Cd  u1 p0 c0 {1,S} {3,D}
3   N3d u0 p1 c0 {2,D} {6,S}
4   O2d u0 p2 c0 {1,D}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.963833,-1.39916,-3.95901,-6.29064,-10.307,-13.5377,-18.7854],'J/(mol*K)'),
        H298 = (401.158,'kJ/mol'),
        S298 = (6.48994,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 474,
    label = "CdJ-N5dcO2s_615",
    group = 
"""
1 * Cd   u1 p0 c0 {2,S} {3,D}
2   O2s  u0 p2 c0 {1,S}
3   N5dc u0 p0 c+1 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.185087,-2.70747,-5.3353,-7.68372,-11.4826,-14.1935,-18.7152],'J/(mol*K)'),
        H298 = (431.838,'kJ/mol','+|-',48.6621),
        S298 = (3.43189,'J/(mol*K)','+|-',12.8654),
    ),
    shortDesc = """Average from child nodes: CdJ-N5dcO2s-HN3sO0sc_614 CdJ-N5dcO2s-CsHO0sc_643 CdJ-N5dcO2s-HHO0sc_720""",
    longDesc = 
"""

""",
)

entry(
    index = 475,
    label = "CdJ-N5dcO2s-HN3sO0sc_614",
    group = 
"""
1   N5dc u0 p0 c+1 {2,D} {4,S} {5,S}
2 * Cd   u1 p0 c0 {1,D} {3,S}
3   O2s  u0 p2 c0 {2,S} {6,S}
4   O0sc u0 p3 c-1 {1,S}
5   H    u0 p0 c0 {1,S}
6   N3s  u0 p1 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.463274,-2.79935,-5.34957,-7.60633,-11.3447,-14.2102,-18.6535],'J/(mol*K)'),
        H298 = (420.769,'kJ/mol'),
        S298 = (7.58196,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 476,
    label = "CdJ-N5dcO2s-CsHO0sc_643",
    group = 
"""
1   N5dc u0 p0 c+1 {2,D} {4,S} {5,S}
2 * Cd   u1 p0 c0 {1,D} {3,S}
3   O2s  u0 p2 c0 {2,S} {6,S}
4   O0sc u0 p3 c-1 {1,S}
5   H    u0 p0 c0 {1,S}
6   Cs   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.206046,-2.62482,-5.31319,-7.87335,-11.7588,-14.063,-18.5248],'J/(mol*K)'),
        H298 = (415.01,'kJ/mol'),
        S298 = (-3.97813,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 477,
    label = "CdJ-N5dcO2s-HHO0sc_720",
    group = 
"""
1   N5dc u0 p0 c+1 {2,D} {4,S} {5,S}
2 * Cd   u1 p0 c0 {1,D} {3,S}
3   O2s  u0 p2 c0 {2,S} {6,S}
4   O0sc u0 p3 c-1 {1,S}
5   H    u0 p0 c0 {1,S}
6   H    u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.298033,-2.69824,-5.34313,-7.57147,-11.3444,-14.3073,-18.9674],'J/(mol*K)'),
        H298 = (459.736,'kJ/mol'),
        S298 = (6.69184,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 478,
    label = "CdJ-N3dN5dc_628",
    group = 
"""
1 * Cd   u1 p0 c0 {2,D} {3,S}
2   N5dc u0 p0 c+1 {1,D}
3   N3d  u0 p1 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.82583,-0.362927,-3.52635,-6.29135,-10.7993,-14.1656,-19.0865],'J/(mol*K)'),
        H298 = (425.092,'kJ/mol'),
        S298 = (12.9456,'J/(mol*K)'),
    ),
    shortDesc = """Average from child nodes: CdJ-N3dN5dc-HN3dO0sc_627""",
    longDesc = 
"""

""",
)

entry(
    index = 479,
    label = "CdJ-N3dN5dc-HN3dO0sc_627",
    group = 
"""
1   N5dc u0 p0 c+1 {2,D} {4,S} {5,S}
2 * Cd   u1 p0 c0 {1,D} {3,S}
3   N3d  u0 p1 c0 {2,S} {6,D}
4   O0sc u0 p3 c-1 {1,S}
5   H    u0 p0 c0 {1,S}
6   N3d  u0 p1 c0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.82583,-0.362927,-3.52635,-6.29135,-10.7993,-14.1656,-19.0865],'J/(mol*K)'),
        H298 = (425.092,'kJ/mol'),
        S298 = (12.9456,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 480,
    label = "CdJ-CdN1sc_673",
    group = 
"""
1 * Cd   u1 p0 c0 {2,S} {3,D}
2   N1sc u0 p2 c-1 {1,S}
3   Cd   u0 p0 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.85711,3.0575,-0.773589,-4.03122,-9.26492,-13.0903,-18.4974],'J/(mol*K)'),
        H298 = (386.113,'kJ/mol'),
        S298 = (12.91,'J/(mol*K)'),
    ),
    shortDesc = """Average from child nodes: CdJ-CdN1sc-HHN5dc_672""",
    longDesc = 
"""

""",
)

entry(
    index = 481,
    label = "CdJ-CdN1sc-HHN5dc_672",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 * Cd   u1 p0 c0 {1,D} {3,S}
3   N1sc u0 p2 c-1 {2,S} {6,S}
4   H    u0 p0 c0 {1,S}
5   H    u0 p0 c0 {1,S}
6   N5dc u0 p0 c+1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.85711,3.0575,-0.773589,-4.03122,-9.26492,-13.0903,-18.4974],'J/(mol*K)'),
        H298 = (386.113,'kJ/mol'),
        S298 = (12.91,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 482,
    label = "CdJ-CON5dc_713",
    group = 
"""
1 * Cd   u1 p0 c0 {2,D} {3,S}
2   N5dc u0 p0 c+1 {1,D}
3   CO   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.458096,-3.33991,-5.71682,-7.86087,-11.7812,-14.6796,-18.5269],'J/(mol*K)'),
        H298 = (513.011,'kJ/mol'),
        S298 = (10.6413,'J/(mol*K)'),
    ),
    shortDesc = """Average from child nodes: CdJ-CON5dc-HHO0scO2d_712""",
    longDesc = 
"""

""",
)

entry(
    index = 483,
    label = "CdJ-CON5dc-HHO0scO2d_712",
    group = 
"""
1   N5dc u0 p0 c+1 {3,D} {4,S} {5,S}
2   CO   u0 p0 c0 {3,S} {6,D} {7,S}
3 * Cd   u1 p0 c0 {1,D} {2,S}
4   O0sc u0 p3 c-1 {1,S}
5   H    u0 p0 c0 {1,S}
6   O2d  u0 p2 c0 {2,D}
7   H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.458096,-3.33991,-5.71682,-7.86087,-11.7812,-14.6796,-18.5269],'J/(mol*K)'),
        H298 = (513.011,'kJ/mol'),
        S298 = (10.6413,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 484,
    label = "CtJ",
    group = 
"""
1 * Ct u1 {2,T}
2   Ct u0 {1,T}
""",
    thermo = 'Acetyl',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 485,
    label = "Acetyl",
    group = 
"""
1   Ct u0 {2,T} {3,S}
2 * Ct u1 {1,T}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.51,-1.56,-2.27,-2.78,-3.47,-3.97,-3.97],'cal/(mol*K)'),
        H298 = (132.7,'kcal/mol'),
        S298 = (2.11,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 486,
    label = "CtJ-Ct-N3s_462",
    group = 
"""
1   Ct  u0 p0 c0 {2,T} {3,S}
2 * Ct  u1 p0 c0 {1,T}
3   N3s u0 p1 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.47851,-9.21476,-11.1898,-12.5087,-14.6232,-16.2179,-18.9399],'J/(mol*K)'),
        H298 = (484.745,'kJ/mol'),
        S298 = (5.3989,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 487,
    label = "CtJ-Ct-N3d_561",
    group = 
"""
1   Ct  u0 p0 c0 {2,T} {3,S}
2 * Ct  u1 p0 c0 {1,T}
3   N3d u0 p1 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.09521,-7.08229,-9.58566,-11.4115,-14.1737,-16.0659,-18.9065],'J/(mol*K)'),
        H298 = (482.404,'kJ/mol'),
        S298 = (4.99017,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 488,
    label = "CtJ-Ct-N1sc_711",
    group = 
"""
1   Ct   u0 p0 c0 {2,T} {3,S}
2 * Ct   u1 p0 c0 {1,T}
3   N1sc u0 p2 c-1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.39333,-6.73136,-9.07001,-10.5442,-12.9832,-14.893,-18.2116],'J/(mol*K)'),
        H298 = (553.861,'kJ/mol'),
        S298 = (13.7384,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 489,
    label = "CbJ",
    group = 
"""
1 * Cb u1 {2,B} {3,B}
2   C  u0 {1,B}
3   C  u0 {1,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.41,-1.18,-1.93,-2.69,-3.75,-4.48,-5.24],'cal/(mol*K)'),
        H298 = (113,'kcal/mol'),
        S298 = (1.48,'cal/(mol*K)'),
    ),
    shortDesc = """BDE from TSANG, S and Cp from THERM""",
    longDesc = 
"""

""",
)

entry(
    index = 490,
    label = "C=SJ",
    group = 
"""
1 * CS  u1 {2,D}
2   S2d u0 p2 {1,D}
""",
    thermo = 'C=SJ-H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 491,
    label = "C=SJ-S2s",
    group = 
"""
1 * CS  u1 {2,S} {3,D}
2   S2s u0 p2 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 492,
    label = "C=SJ-H",
    group = 
"""
1 * CS  u1 {2,S} {3,D}
2   H   u0 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.31,-0.88,-1.47,-1.99,-2.85,-3.49,-4.52],'cal/(mol*K)'),
        H298 = (92.39,'kcal/mol'),
        S298 = (-0.14,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 493,
    label = "C=SJ-C",
    group = 
"""
1 * CS  u1 {2,S} {3,D}
2   C   u0 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 494,
    label = "C=SJ-Cd",
    group = 
"""
1 * CS  u1 {2,S} {3,D}
2   Cd  u0 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.21,-1.76,-2.24,-2.65,-3.3,-3.81,-4.67],'cal/(mol*K)'),
        H298 = (77.87,'kcal/mol'),
        S298 = (0.48,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 495,
    label = "C=SJ-Cs",
    group = 
"""
1 * CS  u1 {2,S} {3,D}
2   Cs  u0 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.2,-1.8,-2.25,-2.63,-3.24,-3.74,-4.64],'cal/(mol*K)'),
        H298 = (91.94,'kcal/mol'),
        S298 = (0.65,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 496,
    label = "OJ",
    group = 
"""
1 * O u1
""",
    thermo = 'COJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 497,
    label = "HOJ",
    group = 
"""
1 * O2s u1 {2,S}
2   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.87,-1.1,-1.36,-1.62,-2.11,-2.53,-3.38],'cal/(mol*K)'),
        H298 = (119.22,'kcal/mol'),
        S298 = (-2.6,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated from NIST values for H2O, OH and H""",
    longDesc = 
"""

""",
)

entry(
    index = 498,
    label = "COJ",
    group = 
"""
1 * O2s u1 {2,S}
2   C   ux {1,S}
""",
    thermo = 'CsOJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 499,
    label = "CCOJ",
    group = 
"""
1   C   u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.1,-12.2,-14.4,-15.1,-14.7,-14.5,-15.6],'J/(mol*K)'),
        H298 = (442.9,'kJ/mol'),
        S298 = (3.8,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 500,
    label = "C=OCOJ",
    group = 
"""
1   C   u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3 * O2s u1 {1,S}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.6,-9.3,-11.5,-13.2,-15,-16,-17.5],'J/(mol*K)'),
        H298 = (461,'kJ/mol'),
        S298 = (2.6,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 501,
    label = "C=CC(C)(C=O)OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4 * O2s u1 {1,S}
5   C   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.5,-11.3,-14.6,-16.2,-17.2,-17.4,-18.4],'J/(mol*K)'),
        H298 = (462.1,'kJ/mol'),
        S298 = (10.4,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 502,
    label = "CC(C)(C=O)OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3 * O2s u1 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.6,-13.9,-16.3,-17.5,-18.4,-18.8,-19.1],'J/(mol*K)'),
        H298 = (459.1,'kJ/mol'),
        S298 = (16.3,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 503,
    label = "C=OC=OOJ",
    group = 
"""
1   CO  u0 {2,S} {3,S} {4,D}
2   CO  u0 {1,S} {5,D}
3 * O2s u1 {1,S}
4   O2d u0 {1,D}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.1,-6.8,-10.1,-13,-17.5,-20.9,-25.9],'J/(mol*K)'),
        H298 = (479.5,'kJ/mol'),
        S298 = (16,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 504,
    label = "CC(C)OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S}
2 * O2s u1 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.3,-6.3,-7.3,-8.3,-9.8,-11.2,-14.2],'J/(mol*K)'),
        H298 = (447.6,'kJ/mol'),
        S298 = (-6.8,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 505,
    label = "CC(C)2OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u1 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.2,-7.9,-9,-9.9,-10.7,-11.7,-14.6],'J/(mol*K)'),
        H298 = (446.1,'kJ/mol'),
        S298 = (-4.6,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 506,
    label = "C=CC(C)2OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3 * O2s u1 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.9,-12.1,-12.9,-12.9,-12.6,-12.9,-14.8],'J/(mol*K)'),
        H298 = (445.9,'kJ/mol'),
        S298 = (2.7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 507,
    label = "CC(C)(O)OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u1 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.8,-18.8,-22.1,-22.3,-19.5,-17.2,-16],'J/(mol*K)'),
        H298 = (449,'kJ/mol'),
        S298 = (8,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 508,
    label = "C=CC(C)(O)OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3 * O2s u1 {1,S}
4   C   u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.2,-12.5,-16.7,-19.1,-20.1,-19.4,-18.2],'J/(mol*K)'),
        H298 = (450.7,'kJ/mol'),
        S298 = (8.5,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 509,
    label = "C=C(C)OJ",
    group = 
"""
1   Cd  u0 {2,S} {3,D} {4,S}
2 * O2s u1 {1,S}
3   C   u0 {1,D}
4   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.2,-13.1,-15.6,-17,-17.7,-17.6,-17.6],'J/(mol*K)'),
        H298 = (354.8,'kJ/mol'),
        S298 = (7.4,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 510,
    label = "CdsOJ",
    group = 
"""
1 * O2s     u1 {2,S}
2   [Cd,CO] u0 {1,S}
""",
    thermo = 'RC=COJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 511,
    label = "RC=COJ",
    group = 
"""
1 * O2s u1 {2,S}
2   Cd  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34,-1.99,-2.48,-2.79,-3.13,-3.33,-3.79],'cal/(mol*K)'),
        H298 = (88,'kcal/mol'),
        S298 = (-1.11,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI""",
    longDesc = 
"""

""",
)

entry(
    index = 512,
    label = "C=COJ",
    group = 
"""
1   Cd  u0 {2,S} {3,D}
2 * O2s u1 {1,S}
3   C   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.1,-13.5,-14.6,-14.6,-14.3,-14.5,-16],'J/(mol*K)'),
        H298 = (358.1,'kJ/mol'),
        S298 = (3.3,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 513,
    label = "OJC=O",
    group = 
"""
1   CO  u0 {2,S} {3,D}
2 * O2s u1 {1,S}
3   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.31,-1.87,-2.32,-2.69,-3.28,-3.74,-4.56],'cal/(mol*K)'),
        H298 = (104,'kcal/mol'),
        S298 = (0.79,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI""",
    longDesc = 
"""

""",
)

entry(
    index = 514,
    label = "OC=OOJ",
    group = 
"""
1   CO  u0 {2,S} {3,S} {4,D}
2 * O2s u1 {1,S}
3   O2s u0 {1,S}
4   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.5,-13.1,-16.3,-18.3,-20.4,-21.2,-21.4],'J/(mol*K)'),
        H298 = (460.9,'kJ/mol'),
        S298 = (6,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 515,
    label = "OCOJ",
    group = 
"""
1   C   u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.9,-17.5,-19.8,-19.3,-16.2,-14.3,-14.3],'J/(mol*K)'),
        H298 = (444.4,'kJ/mol'),
        S298 = (0.8,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 516,
    label = "SCOJ",
    group = 
"""
1   C   ux {2,S} {3,S}
2 * O2s u1 {1,S}
3   S   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.09,-4.17,-4.38,-4.16,-3.24,-2.43,-1.96],'cal/(mol*K)'),
        H298 = (104.33,'kcal/mol'),
        S298 = (1.24,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 517,
    label = "CsOJ",
    group = 
"""
1 * O2s u1 {2,S}
2   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.98,-1.3,-1.61,-1.89,-2.38,-2.8,-3.59],'cal/(mol*K)'),
        H298 = (104.06,'kcal/mol'),
        S298 = (-1.46,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI(ROJ)""",
    longDesc = 
"""

""",
)

entry(
    index = 518,
    label = "H3COJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u1 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.11,-1.29,-1.62,-1.97,-2.59,-3.07,-3.84],'cal/(mol*K)'),
        H298 = (104.27,'kcal/mol'),
        S298 = (0.51,'cal/(mol*K)'),
    ),
    shortDesc = """Enthalpy HBI calculated from NIST values, entropy and Cp from B3LYP/6-31G* for CH3OH, CH3O and H""",
    longDesc = 
"""

""",
)

entry(
    index = 519,
    label = "O2sJ-Cs-HHN3d_595",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u1 p2 c0 {1,S}
3   N3d u0 p1 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.59651,-4.56893,-6.47423,-8.17569,-11.0476,-13.3349,-17.2929],'J/(mol*K)'),
        H298 = (436.724,'kJ/mol'),
        S298 = (7.50024,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 520,
    label = "O2sJ-Cs-HHN3s_674",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u1 p2 c0 {1,S}
3   N3s u0 p1 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.8392,-5.66249,-7.30843,-8.7478,-11.1111,-13.3058,-17.1795],'J/(mol*K)'),
        H298 = (452.391,'kJ/mol'),
        S298 = (2.08537,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 521,
    label = "O2sJ-Cs-HHN1sc_708",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s  u1 p2 c0 {1,S}
3   N1sc u0 p2 c-1 {1,S}
4   H    u0 p0 c0 {1,S}
5   H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.29285,-3.50401,-5.6835,-7.54634,-10.6221,-13.0001,-16.9722],'J/(mol*K)'),
        H298 = (446.883,'kJ/mol'),
        S298 = (10.3957,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 522,
    label = "CbOJ",
    group = 
"""
1 * O2s u1 {2,S}
2   Cb  u0 {1,S}
""",
    thermo = 'RC=COJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 523,
    label = "OOJ",
    group = 
"""
1 * O2s u1 {2,S}
2   O2s u0 {1,S}
""",
    thermo = 'ROOJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 524,
    label = "ROOJ",
    group = 
"""
1   O2s u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05,-2.84,-3.55,-4.09,-4.72,-4.97,-5.08],'cal/(mol*K)'),
        H298 = (88.2,'kcal/mol'),
        S298 = (0.22,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI""",
    longDesc = 
"""

""",
)

entry(
    index = 525,
    label = "C(=O)OOJ",
    group = 
"""
1   O2s u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3 * O2s u1 {1,S}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05,-2.84,-3.55,-4.09,-4.72,-4.97,-5.08],'cal/(mol*K)'),
        H298 = (98.33,'kcal/mol'),
        S298 = (0.22,'cal/(mol*K)'),
    ),
    shortDesc = """HBI for enthalpy from CHEN & BOZZELLI. Cp and S values taken from ROOJ""",
    longDesc = 
"""

""",
)

entry(
    index = 526,
    label = "C3COOJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S} {6,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6 * O2s u1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05,-2.84,-3.55,-4.09,-4.72,-4.97,-5.08],'cal/(mol*K)'),
        H298 = (85.3,'kcal/mol'),
        S298 = (0.22,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI""",
    longDesc = 
"""

""",
)

entry(
    index = 527,
    label = "SOOJ",
    group = 
"""
1   O2s u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   S   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.39,-2.62,-2.95,-3.22,-3.66,-3.98,-4.52],'cal/(mol*K)'),
        H298 = (91.79,'kcal/mol'),
        S298 = (1.36,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 528,
    label = "HOOJ",
    group = 
"""
1   O2s u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.99,-2.68,-3.07,-3.3,-3.55,-3.66,-3.9],'cal/(mol*K)'),
        H298 = (85.13,'kcal/mol'),
        S298 = (-0.92,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated from NIST values for H2O2, O2H and H""",
    longDesc = 
"""

""",
)

entry(
    index = 529,
    label = "SOJ",
    group = 
"""
1 * O u1 p2 c0 {2,S}
2   S ux c0 {1,S}
""",
    thermo = 'O2sJ-S2s',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 530,
    label = "O2sJ-S2s",
    group = 
"""
1 * O2s u1 p2 c0 {2,S}
2   S2s u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.53,-0.81,-0.99,-1.17,-1.56,-1.88,-2.49],'cal/(mol*K)'),
        H298 = (79.78,'kcal/mol'),
        S298 = (1.28,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 531,
    label = "O2sJ-S4d",
    group = 
"""
1 * O2s u1 p2 c0 {2,S}
2   S4d u0 p1 c0 {1,S}
""",
    thermo = 'O2sJ-(S4d-OdO)',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value of 52.103 kcal/mol, 4/2017, Ryan Gillis
""",
)

entry(
    index = 532,
    label = "O2sJ-(S4d-OdO)",
    group = 
"""
1   S4d u0 p1 c0 {2,S} {3,D} {4,S}
2 * O2s u1 p2 c0 {1,S}
3   O2d u0 p2 c0 {1,D}
4   O   u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.62,-0.07,-0.61,-0.93,-1.55,-2,-2.49],'cal/(mol*K)'),
        H298 = (28.13,'kcal/mol'),
        S298 = (2.64,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 533,
    label = "O2sJ-(S4d-OdC)",
    group = 
"""
1   S4d u0 p1 c0 {2,S} {3,D} {4,S}
2 * O2s u1 p2 c0 {1,S}
3   O   u0 p2 c0 {1,D}
4   C   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.33,-2.94,-3.19,-3.38,-3.72,-4.01,-4.59],'cal/(mol*K)'),
        H298 = (78.16,'kcal/mol'),
        S298 = (-0.19,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 534,
    label = "O2sJ-(S4d-OdH)",
    group = 
"""
1   S4d u0 p1 c0 {2,S} {3,D} {4,S}
2 * O2s u1 p2 c0 {1,S}
3   O   u0 p2 c0 {1,D}
4   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.69,-3.3,-3.74,-4.07,-4.4,-4.54,-4.927],'cal/(mol*K)'),
        H298 = (79.582,'kcal/mol'),
        S298 = (-1.49,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 535,
    label = "O2sJ-(S4d-CdC)",
    group = 
"""
1   S4d u0 p1 c0 {2,S} {3,D} {4,S}
2 * O2s u1 p2 c0 {1,S}
3   C   u0 p0 c0 {1,D}
4   C   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.13,-1.86,-2.28,-2.63,-3.2,-3.64,-4.39],'cal/(mol*K)'),
        H298 = (74.659,'kcal/mol'),
        S298 = (0.698,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 536,
    label = "O2sJ-S6d",
    group = 
"""
1 * O2s u1 p2 c0 {2,S}
2   S6d u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.68,-2.09,-2.45,-2.77,-3.3,-3.71,-4.41],'cal/(mol*K)'),
        H298 = (106.21,'kcal/mol'),
        S298 = (-1.07,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 537,
    label = "O2sJ-N3s_459",
    group = 
"""
1   N3s u0 p1 c0 {2,S}
2 * O2s u1 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.44493,-7.94622,-9.75359,-11.1811,-13.5576,-15.4224,-18.608],'J/(mol*K)'),
        H298 = (323.519,'kJ/mol','+|-',45.6625),
        S298 = (1.48757,'J/(mol*K)','+|-',8.81907),
    ),
    shortDesc = """Average from child nodes: O2sJ-N3s-HO2s_458 O2sJ-N3s-HN1sc_564 O2sJ-N3s-COH_590 O2sJ-N3s-CdH_653""",
    longDesc = 
"""

""",
)

entry(
    index = 538,
    label = "O2sJ-N3s-HO2s_458",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {3,S} {4,S}
2 * O2s u1 p2 c0 {1,S}
3   O2s u0 p2 c0 {1,S}
4   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5869,-8.66425,-11.0328,-12.218,-14.1065,-15.5842,-18.2929],'J/(mol*K)'),
        H298 = (351.987,'kJ/mol'),
        S298 = (7.83813,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 539,
    label = "O2sJ-N3s-HN1sc_564",
    group = 
"""
1   N3s  u0 p1 c0 {2,S} {3,S} {4,S}
2 * O2s  u1 p2 c0 {1,S}
3   N1sc u0 p2 c-1 {1,S}
4   H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.32774,-7.63705,-8.7637,-10.2663,-12.8795,-14.9731,-18.4969],'J/(mol*K)'),
        H298 = (314.256,'kJ/mol'),
        S298 = (-2.29606,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 540,
    label = "O2sJ-N3s-COH_590",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {3,S} {4,S}
2 * O2s u1 p2 c0 {1,S}
3   CO  u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.36228,-8.81545,-10.5685,-11.8677,-14.0238,-15.7134,-18.6556],'J/(mol*K)'),
        H298 = (329.46,'kJ/mol'),
        S298 = (0.646791,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 541,
    label = "O2sJ-N3s-CdH_653",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {3,S} {4,S}
2 * O2s u1 p2 c0 {1,S}
3   Cd  u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.50279,-6.66812,-8.64944,-10.3724,-13.2205,-15.4187,-18.9866],'J/(mol*K)'),
        H298 = (298.374,'kJ/mol'),
        S298 = (-0.238592,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 542,
    label = "O2sJ-N1sc_559",
    group = 
"""
1   N1sc u0 p2 c-1 {2,S}
2 * O2s  u1 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.24314,-1.19209,-4.53775,-7.00271,-10.8006,-13.6738,-18.0599],'J/(mol*K)'),
        H298 = (364.959,'kJ/mol'),
        S298 = (9.15896,'J/(mol*K)'),
    ),
    shortDesc = """Average from child nodes: O2sJ-N1sc-N5dc_558""",
    longDesc = 
"""

""",
)

entry(
    index = 543,
    label = "O2sJ-N1sc-N5dc_558",
    group = 
"""
1   N1sc u0 p2 c-1 {2,S} {3,S}
2 * O2s  u1 p2 c0 {1,S}
3   N5dc u0 p0 c+1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.24314,-1.19209,-4.53775,-7.00271,-10.8006,-13.6738,-18.0599],'J/(mol*K)'),
        H298 = (364.959,'kJ/mol'),
        S298 = (9.15896,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 544,
    label = "NJ",
    group = 
"""
1 * N u1
""",
    thermo = 'N3sJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 545,
    label = "N3sJ",
    group = 
"""
1 * N3s u1 p1
""",
    thermo = 'NHJ_C',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 546,
    label = "NH2J",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   H   u0 p0 {1,S}
3   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.43,-0.82,-1.27,-1.72,-2.48,-3.08,-4.1],'cal/(mol*K)'),
        H298 = (107.183,'kcal/mol'),
        S298 = (0.53,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated in relation to ammonia from thermo_DFT_CCSDTF12_BAC values""",
    longDesc = 
"""

""",
)

entry(
    index = 547,
    label = "NHJ_C",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   C   u0 p0 {1,S}
3   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.79,-1.23,-1.64,-2.02,-2.66,-3.2,-4.16],'cal/(mol*K)'),
        H298 = (99.653,'kcal/mol'),
        S298 = (0.92,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated in relation to CH3NH2 from thermo_DFT_CCSDTF12_BAC values""",
    longDesc = 
"""

""",
)

entry(
    index = 548,
    label = "N3sJ-CdH-HN3d_448",
    group = 
"""
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2 * N3s u1 p1 c0 {1,S} {5,S}
3   N3d u0 p1 c0 {1,D}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.55925,-7.44893,-8.88286,-10.1178,-12.1342,-14.0298,-17.3337],'J/(mol*K)'),
        H298 = (393.923,'kJ/mol'),
        S298 = (-0.982286,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 549,
    label = "N3sJ-COH-HO2d_487",
    group = 
"""
1   CO  u0 p0 c0 {2,S} {3,D} {4,S}
2 * N3s u1 p1 c0 {1,S} {5,S}
3   O2d u0 p2 c0 {1,D}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.76427,-6.0835,-7.14234,-8.56996,-11.1076,-13.3449,-17.5941],'J/(mol*K)'),
        H298 = (475.365,'kJ/mol'),
        S298 = (-4.26825,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 550,
    label = "N3sJ-CsH-CdHH_526",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * N3s u1 p1 c0 {1,S} {6,S}
3   Cd  u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.44291,-3.02796,-4.85211,-6.73601,-10.138,-12.7659,-17.284],'J/(mol*K)'),
        H298 = (417.441,'kJ/mol'),
        S298 = (5.91175,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 551,
    label = "N3sJ-CsH-CtHH_548",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * N3s u1 p1 c0 {1,S} {6,S}
3   Ct  u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.419213,-3.30311,-5.39601,-7.14344,-10.0922,-12.6634,-17.1586],'J/(mol*K)'),
        H298 = (427.451,'kJ/mol'),
        S298 = (15.0968,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 552,
    label = "N3sJ-CsH-HHO2s_568",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * N3s u1 p1 c0 {1,S} {6,S}
3   O2s u0 p2 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.06717,-4.15862,-5.63183,-7.23347,-10.3403,-12.7995,-17.1254],'J/(mol*K)'),
        H298 = (424.973,'kJ/mol'),
        S298 = (0.365571,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 553,
    label = "N3sJ-CsH-HHN3d_616",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * N3s u1 p1 c0 {1,S} {6,S}
3   N3d u0 p1 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.96659,-3.75641,-5.48523,-7.09868,-10.1966,-12.8588,-17.2172],'J/(mol*K)'),
        H298 = (423.469,'kJ/mol'),
        S298 = (5.69224,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 554,
    label = "N3sJ-CsH-CsHH_631",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * N3s u1 p1 c0 {1,S} {6,S}
3   Cs  u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.06633,-2.83162,-4.87642,-6.81525,-10.126,-12.8051,-17.3696],'J/(mol*K)'),
        H298 = (416.34,'kJ/mol'),
        S298 = (2.17061,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 555,
    label = "N3sJ-CsH-HHN3s_659",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * N3s u1 p1 c0 {1,S} {6,S}
3   N3s u0 p1 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.90609,-3.92623,-5.7647,-7.39114,-10.3444,-12.9051,-17.2482],'J/(mol*K)'),
        H298 = (422.641,'kJ/mol'),
        S298 = (2.69492,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 556,
    label = "N3sJ-CsH-HHH_710",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * N3s u1 p1 c0 {1,S} {6,S}
3   H   u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.08006,-2.76758,-4.80388,-6.9364,-10.4942,-12.9709,-17.2637],'J/(mol*K)'),
        H298 = (417.656,'kJ/mol'),
        S298 = (-4.5821,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 557,
    label = "N3sJ-CsH-COHH_717",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * N3s u1 p1 c0 {1,S} {6,S}
3   CO  u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.03144,-3.74173,-5.0217,-6.8655,-10.8694,-13.2696,-17.4415],'J/(mol*K)'),
        H298 = (420.798,'kJ/mol'),
        S298 = (-0.29843,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 558,
    label = "N3sJ-CdH-HN5dc_727",
    group = 
"""
1   Cd   u0 p0 c0 {2,S} {3,D} {4,S}
2 * N3s  u1 p1 c0 {1,S} {5,S}
3   N5dc u0 p0 c+1 {1,D}
4   H    u0 p0 c0 {1,S}
5   H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.30828,-7.7023,-9.76545,-11.3226,-13.7472,-15.5429,-18.4613],'J/(mol*K)'),
        H298 = (308.509,'kJ/mol'),
        S298 = (3.01058,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 559,
    label = "NHJ_O",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   O   u0 p2 {1,S}
3   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.26,-1.89,-2.4,-2.79,-3.17,-3.37,-3.65],'cal/(mol*K)'),
        H298 = (85.023,'kcal/mol'),
        S298 = (-0.27,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t NH2OH and [NH]OH, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 560,
    label = "N3sJ-HO2s-N3s_461",
    group = 
"""
1   O2s u0 p2 c0 {2,S} {4,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   H   u0 p0 c0 {2,S}
4   N3s u0 p1 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.77678,-6.66825,-8.25953,-9.69845,-12.31,-14.5426,-18.4182],'J/(mol*K)'),
        H298 = (351.111,'kJ/mol'),
        S298 = (0.951632,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 561,
    label = "N3sJ-HO2s-O2s_463",
    group = 
"""
1   O2s u0 p2 c0 {2,S} {4,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   H   u0 p0 c0 {2,S}
4   O2s u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.104177,-3.64733,-6.4228,-8.57073,-11.9448,-14.3872,-18.1505],'J/(mol*K)'),
        H298 = (337.39,'kJ/mol'),
        S298 = (12.7183,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 562,
    label = "N3sJ-HO2s-Cs_478",
    group = 
"""
1   O2s u0 p2 c0 {2,S} {4,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   H   u0 p0 c0 {2,S}
4   Cs  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.98744,-5.43806,-7.26203,-8.84523,-11.7903,-14.3197,-18.4065],'J/(mol*K)'),
        H298 = (360.027,'kJ/mol'),
        S298 = (-4.38015,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 563,
    label = "N3sJ-HO2s-Cd_521",
    group = 
"""
1   O2s u0 p2 c0 {2,S} {4,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   H   u0 p0 c0 {2,S}
4   Cd  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.64442,-4.38346,-6.17027,-8.19898,-11.607,-14.1466,-18.5708],'J/(mol*K)'),
        H298 = (364.218,'kJ/mol'),
        S298 = (-5.61898,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 564,
    label = "N3sJ-HO2s-Ct_581",
    group = 
"""
1   O2s u0 p2 c0 {2,S} {4,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   H   u0 p0 c0 {2,S}
4   Ct  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.97708,-6.03517,-7.30593,-9.03601,-12.0042,-14.3805,-18.3277],'J/(mol*K)'),
        H298 = (374.964,'kJ/mol'),
        S298 = (-6.59891,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 565,
    label = "N3sJ-HO2s-N3d_607",
    group = 
"""
1   O2s u0 p2 c0 {2,S} {4,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   H   u0 p0 c0 {2,S}
4   N3d u0 p1 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.78942,-4.99584,-6.8341,-8.66655,-11.7594,-14.1998,-18.2021],'J/(mol*K)'),
        H298 = (363.894,'kJ/mol'),
        S298 = (-0.124191,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 566,
    label = "N3sJ-HO2s-N1sc_650",
    group = 
"""
1   O2s  u0 p2 c0 {2,S} {4,S}
2 * N3s  u1 p1 c0 {1,S} {3,S}
3   H    u0 p0 c0 {2,S}
4   N1sc u0 p2 c-1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.26825,-3.72306,-6.01817,-7.7783,-10.6148,-13.1723,-17.9718],'J/(mol*K)'),
        H298 = (385.338,'kJ/mol'),
        S298 = (0.0497425,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 567,
    label = "N3sJ-HO2s-H_686",
    group = 
"""
1   O2s u0 p2 c0 {2,S} {4,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   H   u0 p0 c0 {2,S}
4   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.27548,-6.95525,-8.41518,-9.78068,-12.4004,-14.5666,-18.3558],'J/(mol*K)'),
        H298 = (356.289,'kJ/mol'),
        S298 = (-1.60382,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 568,
    label = "N3sJ-HO2s-CO_714",
    group = 
"""
1   O2s u0 p2 c0 {2,S} {4,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   H   u0 p0 c0 {2,S}
4   CO  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.11187,-3.74334,-5.85002,-7.8038,-11.1387,-13.8028,-18.1989],'J/(mol*K)'),
        H298 = (376.302,'kJ/mol'),
        S298 = (0.787139,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 569,
    label = "NHJ_N",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   N   u0 {1,S}
3   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.77,-2.62,-3.28,-3.79,-4.57,-5.11,-5.85],'cal/(mol*K)'),
        H298 = (82.283,'kcal/mol'),
        S298 = (-0.33,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t NH2NH2 and [NH]NH2, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 570,
    label = "N3sJ-HN3s-HH_460",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {3,S} {4,S}
2 * N3s u1 p1 c0 {1,S} {5,S}
3   H   u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.9682,-4.61787,-6.57686,-8.37874,-11.4753,-13.9784,-18.2268],'J/(mol*K)'),
        H298 = (346.228,'kJ/mol'),
        S298 = (0.540089,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 571,
    label = "N3sJ-HN3s-HO2s_475",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {3,S} {4,S}
2 * N3s u1 p1 c0 {1,S} {5,S}
3   O2s u0 p2 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.59292,-4.72759,-6.62917,-8.39193,-11.3919,-13.8422,-17.9946],'J/(mol*K)'),
        H298 = (365.933,'kJ/mol'),
        S298 = (2.1958,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 572,
    label = "N3sJ-HN3s-CsH_481",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {3,S} {4,S}
2 * N3s u1 p1 c0 {1,S} {5,S}
3   Cs  u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.85651,-4.67632,-6.73138,-8.67126,-11.8178,-14.2801,-18.4278],'J/(mol*K)'),
        H298 = (340.608,'kJ/mol'),
        S298 = (-0.448826,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 573,
    label = "N3sJ-HN3s-HN3d_508",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {3,S} {4,S}
2 * N3s u1 p1 c0 {1,S} {5,S}
3   N3d u0 p1 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.27578,-7.15247,-8.06061,-9.3821,-11.9372,-14.1944,-18.3846],'J/(mol*K)'),
        H298 = (350.708,'kJ/mol'),
        S298 = (-3.12537,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 574,
    label = "N3sJ-HN3s-HN3s_520",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {3,S} {4,S}
2 * N3s u1 p1 c0 {1,S} {5,S}
3   N3s u0 p1 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.85135,-5.70525,-7.42113,-9.12546,-12.0175,-14.3738,-18.4164],'J/(mol*K)'),
        H298 = (343.333,'kJ/mol'),
        S298 = (-0.293172,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 575,
    label = "N3sJ-HN3d-N5dc_529",
    group = 
"""
1   N3d  u0 p1 c0 {2,S} {4,D}
2 * N3s  u1 p1 c0 {1,S} {3,S}
3   H    u0 p0 c0 {2,S}
4   N5dc u0 p0 c+1 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.744704,-3.84656,-6.13732,-8.03903,-11.244,-13.7432,-17.7752],'J/(mol*K)'),
        H298 = (354.576,'kJ/mol'),
        S298 = (7.87504,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 576,
    label = "N3sJ-HN3s-COH_546",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {3,S} {4,S}
2 * N3s u1 p1 c0 {1,S} {5,S}
3   CO  u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.90858,-7.93857,-8.68078,-9.85453,-12.3386,-14.2456,-18.5414],'J/(mol*K)'),
        H298 = (352.954,'kJ/mol'),
        S298 = (-12.4113,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 577,
    label = "N3sJ-HN3s-CdH_567",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {3,S} {4,S}
2 * N3s u1 p1 c0 {1,S} {5,S}
3   Cd  u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.22544,-6.32152,-7.5666,-9.08335,-11.8198,-14.1554,-18.3481],'J/(mol*K)'),
        H298 = (340.696,'kJ/mol'),
        S298 = (-2.13744,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 578,
    label = "NJ_CC",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   C   u0 p0 {1,S}
3   C   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.46,3.7,3.86,3.95,3.73,3.16,1.98],'cal/(mol*K)'),
        H298 = (120.063,'kcal/mol'),
        S298 = (10.18,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t CH3NHCH3 and CH3[N]CH3, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 579,
    label = "N3sJ-CdCs-HHHHN3d_482",
    group = 
"""
1   Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   Cd  u0 p0 c0 {3,S} {7,D} {8,S}
3 * N3s u1 p1 c0 {1,S} {2,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   N3d u0 p1 c0 {2,D}
8   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.93944,-6.11391,-7.24264,-8.41128,-10.9283,-13.2572,-17.3492],'J/(mol*K)'),
        H298 = (407.481,'kJ/mol'),
        S298 = (-10.3783,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 580,
    label = "N3sJ-COCs-HHHHO2d_503",
    group = 
"""
1   Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   CO  u0 p0 c0 {3,S} {7,D} {8,S}
3 * N3s u1 p1 c0 {1,S} {2,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   O2d u0 p2 c0 {2,D}
8   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.79184,-4.29661,-5.37095,-7.10713,-10.8133,-13.3354,-17.2433],'J/(mol*K)'),
        H298 = (453.172,'kJ/mol'),
        S298 = (-4.61516,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 581,
    label = "N3sJ-CsCt-HHHN3t_592",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   Ct  u0 p0 c0 {2,S} {7,T}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   N3t u0 p1 c0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.55096,-7.10886,-8.19682,-9.29722,-11.4732,-13.5322,-17.7139],'J/(mol*K)'),
        H298 = (385.231,'kJ/mol'),
        S298 = (-1.25513,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 582,
    label = "N3sJ-CdCs-HHHHN5dc_647",
    group = 
"""
1   Cs   u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   Cd   u0 p0 c0 {3,S} {7,D} {8,S}
3 * N3s  u1 p1 c0 {1,S} {2,S}
4   H    u0 p0 c0 {1,S}
5   H    u0 p0 c0 {1,S}
6   H    u0 p0 c0 {1,S}
7   N5dc u0 p0 c+1 {2,D}
8   H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.07725,-5.21993,-7.75258,-10.1465,-13.2287,-14.9433,-18.4473],'J/(mol*K)'),
        H298 = (298.394,'kJ/mol'),
        S298 = (-9.13218,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 583,
    label = "N3sJ-CsCs-HHHHHH_667",
    group = 
"""
1   Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   Cs  u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3 * N3s u1 p1 c0 {1,S} {2,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {2,S}
9   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.38379,-3.57362,-5.08476,-6.77295,-9.88757,-12.6076,-17.62],'J/(mol*K)'),
        H298 = (394.457,'kJ/mol'),
        S298 = (-1.42036,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 584,
    label = "N3sJ-CsCs-HHHHHO2s_724",
    group = 
"""
1   Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   Cs  u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3 * N3s u1 p1 c0 {1,S} {2,S}
4   O2s u0 p2 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {2,S}
9   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.83038,-3.75508,-5.63303,-7.63791,-10.5243,-12.7808,-17.3613],'J/(mol*K)'),
        H298 = (409.852,'kJ/mol'),
        S298 = (6.59187,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 585,
    label = "N3sJ-CsCs-HHHHHN3s_725",
    group = 
"""
1   Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   Cs  u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3 * N3s u1 p1 c0 {1,S} {2,S}
4   N3s u0 p1 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {2,S}
9   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.08562,-3.76064,-5.73993,-7.61113,-10.5601,-12.9852,-17.3274],'J/(mol*K)'),
        H298 = (392.392,'kJ/mol'),
        S298 = (8.02189,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 586,
    label = "N3sJ-CdN3s_445",
    group = 
"""
1 * N3s u1 p1 c0 {2,S} {3,S}
2   N3s u0 p1 c0 {1,S}
3   Cd  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.03287,-5.02703,-6.42805,-8.25712,-11.4505,-14.0481,-18.4232],'J/(mol*K)'),
        H298 = (302.216,'kJ/mol','+|-',76.3491),
        S298 = (-1.52094,'J/(mol*K)','+|-',4.81668),
    ),
    shortDesc = """Average from child nodes: N3sJ-CdN3s-HHHN3d_444 N3sJ-CdN3s-HHHN5dc_611""",
    longDesc = 
"""

""",
)

entry(
    index = 587,
    label = "N3sJ-CdN3s-HHHN3d_444",
    group = 
"""
1   N3s u0 p1 c0 {3,S} {4,S} {5,S}
2   Cd  u0 p0 c0 {3,S} {6,D} {7,S}
3 * N3s u1 p1 c0 {1,S} {2,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   N3d u0 p1 c0 {2,D}
7   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.37252,-4.46504,-6.04102,-7.88882,-11.109,-13.7377,-18.2235],'J/(mol*K)'),
        H298 = (329.209,'kJ/mol'),
        S298 = (0.182016,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 588,
    label = "N3sJ-CdN3s-HHHN5dc_611",
    group = 
"""
1   N3s  u0 p1 c0 {3,S} {4,S} {5,S}
2   Cd   u0 p0 c0 {3,S} {6,D} {7,S}
3 * N3s  u1 p1 c0 {1,S} {2,S}
4   H    u0 p0 c0 {1,S}
5   H    u0 p0 c0 {1,S}
6   N5dc u0 p0 c+1 {2,D}
7   H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.69322,-5.58902,-6.81508,-8.62541,-11.792,-14.3584,-18.6228],'J/(mol*K)'),
        H298 = (275.222,'kJ/mol'),
        S298 = (-3.22389,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 589,
    label = "N3sJ-CON3s_477",
    group = 
"""
1 * N3s u1 p1 c0 {2,S} {3,S}
2   N3s u0 p1 c0 {1,S}
3   CO  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.61946,-4.63981,-6.2884,-8.1636,-11.561,-13.9136,-18.4053],'J/(mol*K)'),
        H298 = (344.732,'kJ/mol'),
        S298 = (-4.71045,'J/(mol*K)'),
    ),
    shortDesc = """Average from child nodes: N3sJ-CON3s-HHHO2d_476""",
    longDesc = 
"""

""",
)

entry(
    index = 590,
    label = "N3sJ-CON3s-HHHO2d_476",
    group = 
"""
1   N3s u0 p1 c0 {3,S} {4,S} {5,S}
2   CO  u0 p0 c0 {3,S} {6,D} {7,S}
3 * N3s u1 p1 c0 {1,S} {2,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   O2d u0 p2 c0 {2,D}
7   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.61946,-4.63981,-6.2884,-8.1636,-11.561,-13.9136,-18.4053],'J/(mol*K)'),
        H298 = (344.732,'kJ/mol'),
        S298 = (-4.71045,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 591,
    label = "N3sJ-N3dO2s_484",
    group = 
"""
1 * N3s u1 p1 c0 {2,S} {3,S}
2   O2s u0 p2 c0 {1,S}
3   N3d u0 p1 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.67209,-4.52809,-6.52516,-8.48225,-11.7337,-14.199,-18.1206],'J/(mol*K)'),
        H298 = (297.438,'kJ/mol'),
        S298 = (4.00099,'J/(mol*K)'),
    ),
    shortDesc = """Average from child nodes: N3sJ-N3dO2s-CdH_483""",
    longDesc = 
"""

""",
)

entry(
    index = 592,
    label = "N3sJ-N3dO2s-CdH_483",
    group = 
"""
1 * N3s u1 p1 c0 {2,S} {3,S}
2   O2s u0 p2 c0 {1,S} {4,S}
3   N3d u0 p1 c0 {1,S} {5,D}
4   H   u0 p0 c0 {2,S}
5   Cd  u0 p0 c0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.67209,-4.52809,-6.52516,-8.48225,-11.7337,-14.199,-18.1206],'J/(mol*K)'),
        H298 = (297.438,'kJ/mol'),
        S298 = (4.00099,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 593,
    label = "N3sJ-CsO2s_499",
    group = 
"""
1 * N3s u1 p1 c0 {2,S} {3,S}
2   O2s u0 p2 c0 {1,S}
3   Cs  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.96465,-5.52735,-7.41078,-9.11445,-12.1297,-14.4739,-18.2651],'J/(mol*K)'),
        H298 = (345.346,'kJ/mol','+|-',18.61),
        S298 = (0.661925,'J/(mol*K)','+|-',13.0243),
    ),
    shortDesc = """Average from child nodes: N3sJ-CsO2s-HHHN3s_498 N3sJ-CsO2s-HHHH_569 N3sJ-CsO2s-CsHHH_600 N3sJ-CsO2s-CsHHH_612 N3sJ-CsO2s-HHHO2s_654 N3sJ-CsO2s-HHHO2s_730 N3sJ-CsO2s-HHHN3s_731""",
    longDesc = 
"""

""",
)

entry(
    index = 594,
    label = "N3sJ-CsO2s-HHHN3s_498",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   O2s u0 p2 c0 {2,S} {7,S}
4   N3s u0 p1 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.65346,-5.61773,-7.71524,-9.44908,-12.2626,-14.4005,-18.0006],'J/(mol*K)'),
        H298 = (343.51,'kJ/mol'),
        S298 = (7.79536,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 595,
    label = "N3sJ-CsO2s-HHHH_569",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   O2s u0 p2 c0 {2,S} {7,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.58956,-5.49529,-7.34576,-9.02829,-11.9259,-14.2791,-18.3305],'J/(mol*K)'),
        H298 = (336.617,'kJ/mol'),
        S298 = (-4.98613,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 596,
    label = "N3sJ-CsO2s-CsHHH_600",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   O2s u0 p2 c0 {2,S} {7,S}
4   Cs  u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.328,-5.92853,-7.71397,-8.98559,-11.658,-14.4488,-18.2839],'J/(mol*K)'),
        H298 = (337.529,'kJ/mol'),
        S298 = (-1.874,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 597,
    label = "N3sJ-CsO2s-CsHHH_612",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   O2s u0 p2 c0 {2,S} {7,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   Cs  u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.23,-4.2951,-5.65012,-7.74655,-11.9057,-14.3493,-18.2387],'J/(mol*K)'),
        H298 = (352.403,'kJ/mol'),
        S298 = (-9.89107,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 598,
    label = "N3sJ-CsO2s-HHHO2s_654",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   O2s u0 p2 c0 {2,S} {7,S}
4   O2s u0 p2 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.59374,-5.59981,-7.67382,-9.32502,-12.1135,-14.3363,-18.1897],'J/(mol*K)'),
        H298 = (357.833,'kJ/mol'),
        S298 = (6.83082,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 599,
    label = "N3sJ-CsO2s-HHHO2s_730",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   O2s u0 p2 c0 {2,S} {7,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   O2s u0 p2 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.11541,-6.2529,-8.36684,-10.1549,-12.9915,-15.0667,-18.3236],'J/(mol*K)'),
        H298 = (354.051,'kJ/mol'),
        S298 = (2.65789,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 600,
    label = "N3sJ-CsO2s-HHHN3s_731",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   O2s u0 p2 c0 {2,S} {7,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   N3s u0 p1 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.24235,-5.50208,-7.40972,-9.11173,-12.0504,-14.4367,-18.4887],'J/(mol*K)'),
        H298 = (335.48,'kJ/mol'),
        S298 = (4.10061,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 601,
    label = "N3sJ-CsN3s_541",
    group = 
"""
1 * N3s u1 p1 c0 {2,S} {3,S}
2   N3s u0 p1 c0 {1,S}
3   Cs  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.40632,-4.4619,-6.4817,-8.31914,-11.124,-13.5049,-17.279],'J/(mol*K)'),
        H298 = (328.542,'kJ/mol','+|-',23.0656),
        S298 = (-7.83905,'J/(mol*K)','+|-',31.695),
    ),
    shortDesc = """Average from child nodes: N3sJ-CsN3s-CsHHHH_540 N3sJ-CsN3s-HHHHH_587 N3sJ-CsN3s-CsHHHH_599 N3sJ-CsN3s-HHHHO2s_655 N3sJ-CsN3s-HHHHN3s_662 N3sJ-CsN3s-HHHHN3s_698 N3sJ-CsN3s-HHHHO2s_699""",
    longDesc = 
"""

""",
)

entry(
    index = 602,
    label = "N3sJ-CsN3s-CsHHHH_540",
    group = 
"""
1   Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   N3s u0 p1 c0 {3,S} {7,S} {8,S}
3 * N3s u1 p1 c0 {1,S} {2,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   Cs  u0 p0 c0 {2,S}
8   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.97069,-4.40339,-6.24381,-7.89337,-8.76402,-9.74933,-10.7201],'J/(mol*K)'),
        H298 = (311.662,'kJ/mol'),
        S298 = (-43.2888,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 603,
    label = "N3sJ-CsN3s-HHHHH_587",
    group = 
"""
1   Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   N3s u0 p1 c0 {3,S} {7,S} {8,S}
3 * N3s u1 p1 c0 {1,S} {2,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.20906,-4.07823,-6.14554,-8.05566,-11.3037,-13.894,-18.218],'J/(mol*K)'),
        H298 = (329.544,'kJ/mol'),
        S298 = (-4.70587,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 604,
    label = "N3sJ-CsN3s-CsHHHH_599",
    group = 
"""
1   Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   N3s u0 p1 c0 {3,S} {7,S} {8,S}
3 * N3s u1 p1 c0 {1,S} {2,S}
4   Cs  u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.073,-4.0032,-5.96957,-7.81072,-11.0945,-13.8604,-18.2069],'J/(mol*K)'),
        H298 = (331.91,'kJ/mol'),
        S298 = (-2.60865,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 605,
    label = "N3sJ-CsN3s-HHHHO2s_655",
    group = 
"""
1   Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   N3s u0 p1 c0 {3,S} {7,S} {8,S}
3 * N3s u1 p1 c0 {1,S} {2,S}
4   O2s u0 p2 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.99733,-5.17266,-6.79559,-8.5734,-11.6427,-14.1342,-18.3607],'J/(mol*K)'),
        H298 = (341.477,'kJ/mol'),
        S298 = (-0.0104719,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 606,
    label = "N3sJ-CsN3s-HHHHN3s_662",
    group = 
"""
1   Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   N3s u0 p1 c0 {3,S} {7,S} {8,S}
3 * N3s u1 p1 c0 {1,S} {2,S}
4   N3s u0 p1 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   H   u0 p0 c0 {2,S}
8   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.40515,-5.03761,-6.8984,-8.6671,-11.7117,-14.1783,-18.3779],'J/(mol*K)'),
        H298 = (334.443,'kJ/mol'),
        S298 = (2.69008,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 607,
    label = "N3sJ-CsN3s-HHHHN3s_698",
    group = 
"""
1   Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   N3s u0 p1 c0 {3,S} {7,S} {8,S}
3 * N3s u1 p1 c0 {1,S} {2,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   N3s u0 p1 c0 {2,S}
8   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.26461,-5.07905,-7.53684,-9.3802,-12.0233,-14.672,-18.6318],'J/(mol*K)'),
        H298 = (313.577,'kJ/mol'),
        S298 = (-4.64893,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 608,
    label = "N3sJ-CsN3s-HHHHO2s_699",
    group = 
"""
1   Cs  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   N3s u0 p1 c0 {3,S} {7,S} {8,S}
3 * N3s u1 p1 c0 {1,S} {2,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {1,S}
7   O2s u0 p2 c0 {2,S}
8   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.924429,-3.45917,-5.78215,-7.85356,-11.3283,-14.0458,-18.4376],'J/(mol*K)'),
        H298 = (337.182,'kJ/mol'),
        S298 = (-2.30076,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 609,
    label = "N3sJ-CdO2s_550",
    group = 
"""
1 * N3s u1 p1 c0 {2,S} {3,S}
2   O2s u0 p2 c0 {1,S}
3   Cd  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.05718,-5.83324,-7.85329,-9.70684,-12.7559,-15.0423,-18.6924],'J/(mol*K)'),
        H298 = (296.002,'kJ/mol','+|-',112.959),
        S298 = (1.79378,'J/(mol*K)','+|-',6.94995),
    ),
    shortDesc = """Average from child nodes: N3sJ-CdO2s-HHN3d_549 N3sJ-CdO2s-HHN5dc_619""",
    longDesc = 
"""

""",
)

entry(
    index = 610,
    label = "N3sJ-CdO2s-HHN3d_549",
    group = 
"""
1   Cd  u0 p0 c0 {2,S} {4,D} {5,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   O2s u0 p2 c0 {2,S} {6,S}
4   N3d u0 p1 c0 {1,D}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.47188,-8.32386,-9.51017,-10.9614,-13.3801,-15.1755,-18.1995],'J/(mol*K)'),
        H298 = (335.939,'kJ/mol'),
        S298 = (-0.663395,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 611,
    label = "N3sJ-CdO2s-HHN5dc_619",
    group = 
"""
1   Cd   u0 p0 c0 {2,S} {4,D} {5,S}
2 * N3s  u1 p1 c0 {1,S} {3,S}
3   O2s  u0 p2 c0 {2,S} {6,S}
4   N5dc u0 p0 c+1 {1,D}
5   H    u0 p0 c0 {1,S}
6   H    u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.642468,-3.34261,-6.19642,-8.45226,-12.1316,-14.9091,-19.1853],'J/(mol*K)'),
        H298 = (256.065,'kJ/mol'),
        S298 = (4.25096,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 612,
    label = "N3sJ-COO2s_557",
    group = 
"""
1 * N3s u1 p1 c0 {2,S} {3,S}
2   O2s u0 p2 c0 {1,S}
3   CO  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.45956,-10.4996,-11.1874,-12.1293,-13.9022,-15.3998,-18.3377],'J/(mol*K)'),
        H298 = (358.123,'kJ/mol'),
        S298 = (-3.27653,'J/(mol*K)'),
    ),
    shortDesc = """Average from child nodes: N3sJ-COO2s-HHO2d_556""",
    longDesc = 
"""

""",
)

entry(
    index = 613,
    label = "N3sJ-COO2s-HHO2d_556",
    group = 
"""
1   CO  u0 p0 c0 {2,S} {4,D} {5,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   O2s u0 p2 c0 {2,S} {6,S}
4   O2d u0 p2 c0 {1,D}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.45956,-10.4996,-11.1874,-12.1293,-13.9022,-15.3998,-18.3377],'J/(mol*K)'),
        H298 = (358.123,'kJ/mol'),
        S298 = (-3.27653,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 614,
    label = "N3sJ-CsN3d_575",
    group = 
"""
1 * N3s u1 p1 c0 {2,S} {3,S}
2   N3d u0 p1 c0 {1,S}
3   Cs  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.55394,-1.2031,-4.33615,-7.00042,-10.3957,-12.9499,-17.5168],'J/(mol*K)'),
        H298 = (310.272,'kJ/mol'),
        S298 = (-2.57585,'J/(mol*K)'),
    ),
    shortDesc = """Average from child nodes: N3sJ-CsN3d-HHHN5dc_574""",
    longDesc = 
"""

""",
)

entry(
    index = 615,
    label = "N3sJ-CsN3d-HHHN5dc_574",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 * N3s  u1 p1 c0 {1,S} {3,S}
3   N3d  u0 p1 c0 {2,S} {7,D}
4   H    u0 p0 c0 {1,S}
5   H    u0 p0 c0 {1,S}
6   H    u0 p0 c0 {1,S}
7   N5dc u0 p0 c+1 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.55394,-1.2031,-4.33615,-7.00042,-10.3957,-12.9499,-17.5168],'J/(mol*K)'),
        H298 = (310.272,'kJ/mol'),
        S298 = (-2.57585,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 616,
    label = "N3sJ-N3sN3s_633",
    group = 
"""
1 * N3s u1 p1 c0 {2,S} {3,S}
2   N3s u0 p1 c0 {1,S}
3   N3s u0 p1 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.417,-4.37355,-6.13986,-7.99907,-11.283,-13.9627,-18.4517],'J/(mol*K)'),
        H298 = (316.36,'kJ/mol','+|-',27.1365),
        S298 = (2.17698,'J/(mol*K)','+|-',3.23024),
    ),
    shortDesc = """Average from child nodes: N3sJ-N3sN3s-HHHH_632 N3sJ-N3sN3s-HHHO2s_689""",
    longDesc = 
"""

""",
)

entry(
    index = 617,
    label = "N3sJ-N3sN3s-HHHH_632",
    group = 
"""
1   N3s u0 p1 c0 {3,S} {4,S} {5,S}
2   N3s u0 p1 c0 {3,S} {6,S} {7,S}
3 * N3s u1 p1 c0 {1,S} {2,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05084,-4.47159,-6.35424,-8.14698,-11.3216,-13.9618,-18.4459],'J/(mol*K)'),
        H298 = (306.766,'kJ/mol'),
        S298 = (3.31904,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 618,
    label = "N3sJ-N3sN3s-HHHO2s_689",
    group = 
"""
1   N3s u0 p1 c0 {3,S} {4,S} {5,S}
2   N3s u0 p1 c0 {3,S} {6,S} {7,S}
3 * N3s u1 p1 c0 {1,S} {2,S}
4   O2s u0 p2 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {2,S}
7   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.78317,-4.27551,-5.92547,-7.85117,-11.2445,-13.9636,-18.4576],'J/(mol*K)'),
        H298 = (325.954,'kJ/mol'),
        S298 = (1.03492,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 619,
    label = "N3sJ-N3sO2s_635",
    group = 
"""
1 * N3s u1 p1 c0 {2,S} {3,S}
2   O2s u0 p2 c0 {1,S}
3   N3s u0 p1 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.134804,-3.36803,-6.0009,-8.11659,-11.5126,-14.068,-18.2098],'J/(mol*K)'),
        H298 = (306,'kJ/mol','+|-',65.2848),
        S298 = (6.48406,'J/(mol*K)','+|-',13.992),
    ),
    shortDesc = """Average from child nodes: N3sJ-N3sO2s-HHO2s_634 N3sJ-N3sO2s-CsHH_648 N3sJ-N3sO2s-HHH_651 N3sJ-N3sO2s-CsHH_683 N3sJ-N3sO2s-HHO2s_690 N3sJ-N3sO2s-HHN3s_697 N3sJ-N3sO2s-HHN3s_733""",
    longDesc = 
"""

""",
)

entry(
    index = 620,
    label = "N3sJ-N3sO2s-HHO2s_634",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {4,S} {5,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   O2s u0 p2 c0 {2,S} {6,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   O2s u0 p2 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.70417,-1.80943,-4.43988,-6.28756,-9.45156,-12.019,-16.5561],'J/(mol*K)'),
        H298 = (236.542,'kJ/mol'),
        S298 = (16.7839,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 621,
    label = "N3sJ-N3sO2s-CsHH_648",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {4,S} {5,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   O2s u0 p2 c0 {2,S} {6,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   Cs  u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.711549,-3.38042,-6.10405,-8.4884,-11.7391,-14.0798,-18.6381],'J/(mol*K)'),
        H298 = (311.947,'kJ/mol'),
        S298 = (-3.99663,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 622,
    label = "N3sJ-N3sO2s-HHH_651",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {4,S} {5,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   O2s u0 p2 c0 {2,S} {6,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.9818,-3.85775,-6.01963,-8.17423,-11.6849,-14.3033,-18.3283],'J/(mol*K)'),
        H298 = (316.403,'kJ/mol'),
        S298 = (4.04755,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 623,
    label = "N3sJ-N3sO2s-CsHH_683",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {4,S} {5,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   O2s u0 p2 c0 {2,S} {6,S}
4   Cs  u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.0437,-4.05926,-6.41453,-8.46966,-12.1595,-14.9,-18.7912],'J/(mol*K)'),
        H298 = (297.446,'kJ/mol'),
        S298 = (0.106176,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 624,
    label = "N3sJ-N3sO2s-HHO2s_690",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {4,S} {5,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   O2s u0 p2 c0 {2,S} {6,S}
4   O2s u0 p2 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.681518,-2.05473,-5.31814,-7.79654,-11.5797,-14.3313,-18.4186],'J/(mol*K)'),
        H298 = (333.992,'kJ/mol'),
        S298 = (9.10515,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 625,
    label = "N3sJ-N3sO2s-HHN3s_697",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {4,S} {5,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   O2s u0 p2 c0 {2,S} {6,S}
4   N3s u0 p1 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.277044,-4.14773,-6.90448,-8.8684,-12.0707,-14.5046,-18.4273],'J/(mol*K)'),
        H298 = (321.97,'kJ/mol'),
        S298 = (8.26882,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 626,
    label = "N3sJ-N3sO2s-HHN3s_733",
    group = 
"""
1   N3s u0 p1 c0 {2,S} {4,S} {5,S}
2 * N3s u1 p1 c0 {1,S} {3,S}
3   O2s u0 p2 c0 {2,S} {6,S}
4   H   u0 p0 c0 {1,S}
5   H   u0 p0 c0 {1,S}
6   N3s u0 p1 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.31523,-4.26688,-6.80557,-8.73131,-11.9024,-14.3377,-18.3087],'J/(mol*K)'),
        H298 = (323.701,'kJ/mol'),
        S298 = (11.0735,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 627,
    label = "N3sJ-O2sO2s_638",
    group = 
"""
1 * N3s u1 p1 c0 {2,S} {3,S}
2   O2s u0 p2 c0 {1,S}
3   O2s u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.60673,-4.21026,-6.57934,-8.65497,-11.9161,-14.4376,-18.5013],'J/(mol*K)'),
        H298 = (306.032,'kJ/mol','+|-',10.1865),
        S298 = (2.4319,'J/(mol*K)','+|-',0.966786),
    ),
    shortDesc = """Average from child nodes: N3sJ-O2sO2s-CsH_637 N3sJ-O2sO2s-HH_692""",
    longDesc = 
"""

""",
)

entry(
    index = 628,
    label = "N3sJ-O2sO2s-CsH_637",
    group = 
"""
1 * N3s u1 p1 c0 {2,S} {3,S}
2   O2s u0 p2 c0 {1,S} {4,S}
3   O2s u0 p2 c0 {1,S} {5,S}
4   Cs  u0 p0 c0 {2,S}
5   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.434549,-3.63127,-6.23551,-8.41954,-11.7306,-14.3307,-18.5782],'J/(mol*K)'),
        H298 = (302.431,'kJ/mol'),
        S298 = (2.09009,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 629,
    label = "N3sJ-O2sO2s-HH_692",
    group = 
"""
1 * N3s u1 p1 c0 {2,S} {3,S}
2   O2s u0 p2 c0 {1,S} {4,S}
3   O2s u0 p2 c0 {1,S} {5,S}
4   H   u0 p0 c0 {2,S}
5   H   u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.77891,-4.78926,-6.92316,-8.8904,-12.1015,-14.5444,-18.4243],'J/(mol*K)'),
        H298 = (309.634,'kJ/mol'),
        S298 = (2.77371,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 630,
    label = "N3sJ-N3dN3s_676",
    group = 
"""
1 * N3s u1 p1 c0 {2,S} {3,S}
2   N3s u0 p1 c0 {1,S}
3   N3d u0 p1 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.570244,-1.12252,-3.69181,-6.1693,-10.2466,-13.3402,-18.0429],'J/(mol*K)'),
        H298 = (298.725,'kJ/mol'),
        S298 = (3.37343,'J/(mol*K)'),
    ),
    shortDesc = """Average from child nodes: N3sJ-N3dN3s-HHN5dc_675""",
    longDesc = 
"""

""",
)

entry(
    index = 631,
    label = "N3sJ-N3dN3s-HHN5dc_675",
    group = 
"""
1   N3s  u0 p1 c0 {2,S} {4,S} {5,S}
2 * N3s  u1 p1 c0 {1,S} {3,S}
3   N3d  u0 p1 c0 {2,S} {6,D}
4   H    u0 p0 c0 {1,S}
5   H    u0 p0 c0 {1,S}
6   N5dc u0 p0 c+1 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.570244,-1.12252,-3.69181,-6.1693,-10.2466,-13.3402,-18.0429],'J/(mol*K)'),
        H298 = (298.725,'kJ/mol'),
        S298 = (3.37343,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 632,
    label = "N3sJ-N1scO2s_688",
    group = 
"""
1 * N3s  u1 p1 c0 {2,S} {3,S}
2   O2s  u0 p2 c0 {1,S}
3   N1sc u0 p2 c-1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.24294,-2.98481,-5.20037,-7.43785,-11.1544,-14.013,-18.4632],'J/(mol*K)'),
        H298 = (292.19,'kJ/mol'),
        S298 = (3.04153,'J/(mol*K)'),
    ),
    shortDesc = """Average from child nodes: N3sJ-N1scO2s-HN5dc_687""",
    longDesc = 
"""

""",
)

entry(
    index = 633,
    label = "N3sJ-N1scO2s-HN5dc_687",
    group = 
"""
1 * N3s  u1 p1 c0 {2,S} {3,S}
2   O2s  u0 p2 c0 {1,S} {4,S}
3   N1sc u0 p2 c-1 {1,S} {5,S}
4   H    u0 p0 c0 {2,S}
5   N5dc u0 p0 c+1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.24294,-2.98481,-5.20037,-7.43785,-11.1544,-14.013,-18.4632],'J/(mol*K)'),
        H298 = (292.19,'kJ/mol'),
        S298 = (3.04153,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 634,
    label = "N3sJ-CtO2s_702",
    group = 
"""
1 * N3s u1 p1 c0 {2,S} {3,S}
2   O2s u0 p2 c0 {1,S}
3   Ct  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.47,-7.12847,-8.52379,-10.0027,-12.5861,-14.6952,-18.3928],'J/(mol*K)'),
        H298 = (314.633,'kJ/mol'),
        S298 = (-0.886968,'J/(mol*K)'),
    ),
    shortDesc = """Average from child nodes: N3sJ-CtO2s-CtH_701""",
    longDesc = 
"""

""",
)

entry(
    index = 635,
    label = "N3sJ-CtO2s-CtH_701",
    group = 
"""
1 * N3s u1 p1 c0 {2,S} {3,S}
2   O2s u0 p2 c0 {1,S} {4,S}
3   Ct  u0 p0 c0 {1,S} {5,T}
4   H   u0 p0 c0 {2,S}
5   Ct  u0 p0 c0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.47,-7.12847,-8.52379,-10.0027,-12.5861,-14.6952,-18.3928],'J/(mol*K)'),
        H298 = (314.633,'kJ/mol'),
        S298 = (-0.886968,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 636,
    label = "N3dJ",
    group = 
"""
1 * N3d u1 p1
""",
    thermo = 'N3dJ_C',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 637,
    label = "N3dJ_C",
    group = 
"""
1 * N3d u1 p1 {2,D}
2   C   u0 p0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.2,-0.6,-1.07,-1.56,-2.44,-3.15,-4.26],'cal/(mol*K)'),
        H298 = (88.343,'kcal/mol'),
        S298 = (-0.71,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t NH=CH2 and [N]=CH2, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 638,
    label = "N3dJ-Cdd-Cdd_446",
    group = 
"""
1   Cdd u0 p0 c0 {2,D} {3,D}
2 * N3d u1 p1 c0 {1,D}
3   Cdd u0 p0 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.69275,-7.08882,-9.08155,-10.8668,-13.9087,-16.2136,-19.4145],'J/(mol*K)'),
        H298 = (265.788,'kJ/mol'),
        S298 = (3.03183,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 639,
    label = "N3dJ-Cd-HH_492",
    group = 
"""
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2 * N3d u1 p1 c0 {1,D}
3   H   u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.83925,-2.55727,-4.53791,-6.57878,-10.3147,-13.2687,-17.9109],'J/(mol*K)'),
        H298 = (369.555,'kJ/mol'),
        S298 = (-2.97535,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 640,
    label = "N3dJ-Cd-CsH_510",
    group = 
"""
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2 * N3d u1 p1 c0 {1,D}
3   Cs  u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.41059,-3.30916,-5.62956,-7.91271,-11.5397,-14.1376,-18.421],'J/(mol*K)'),
        H298 = (375.581,'kJ/mol'),
        S298 = (-1.79086,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 641,
    label = "N3dJ-Cd-HO2s_516",
    group = 
"""
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2 * N3d u1 p1 c0 {1,D}
3   O2s u0 p2 c0 {1,S}
4   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.749627,-3.48351,-6.03694,-8.22289,-11.8865,-14.5059,-18.4558],'J/(mol*K)'),
        H298 = (420.697,'kJ/mol'),
        S298 = (3.27364,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 642,
    label = "N3dJ-Cd-HN3s_517",
    group = 
"""
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2 * N3d u1 p1 c0 {1,D}
3   N3s u0 p1 c0 {1,S}
4   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.53463,-4.045,-6.6003,-8.83063,-12.125,-14.3613,-17.9577],'J/(mol*K)'),
        H298 = (408.725,'kJ/mol'),
        S298 = (2.52553,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 643,
    label = "N3dJ-Cdd-N5dc_533",
    group = 
"""
1   Cdd  u0 p0 c0 {2,D} {3,D}
2 * N3d  u1 p1 c0 {1,D}
3   N5dc u0 p0 c+1 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.42145,-6.77701,-9.07633,-11.1196,-14.3685,-16.7134,-20.0205],'J/(mol*K)'),
        H298 = (198.991,'kJ/mol'),
        S298 = (0.702963,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 644,
    label = "N3dJ-Cd-CtH_534",
    group = 
"""
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2 * N3d u1 p1 c0 {1,D}
3   Ct  u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.60506,-3.66919,-5.94907,-8.06848,-11.6017,-14.1895,-18.277],'J/(mol*K)'),
        H298 = (392.745,'kJ/mol'),
        S298 = (4.32479,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 645,
    label = "N3dJ-Cdd-N3d_605",
    group = 
"""
1   Cdd u0 p0 c0 {2,D} {3,D}
2 * N3d u1 p1 c0 {1,D}
3   N3d u0 p1 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.26308,-8.22657,-9.83228,-11.3264,-13.8352,-15.8034,-19.0851],'J/(mol*K)'),
        H298 = (307.02,'kJ/mol'),
        S298 = (-0.191746,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 646,
    label = "N3dJ-Cdd-Cd_621",
    group = 
"""
1   Cdd u0 p0 c0 {2,D} {3,D}
2 * N3d u1 p1 c0 {1,D}
3   Cd  u0 p0 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.67657,-5.90416,-8.14283,-10.1688,-13.4449,-15.8735,-19.4779],'J/(mol*K)'),
        H298 = (239.725,'kJ/mol'),
        S298 = (1.40429,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 647,
    label = "N3dJ-Cd-HN3d_641",
    group = 
"""
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2 * N3d u1 p1 c0 {1,D}
3   N3d u0 p1 c0 {1,S}
4   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.781,-3.941,-6.15522,-8.14489,-11.5069,-14.1605,-18.4903],'J/(mol*K)'),
        H298 = (395.749,'kJ/mol'),
        S298 = (3.56318,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 648,
    label = "N3dJ-Cd-HN1sc_666",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 * N3d  u1 p1 c0 {1,D}
3   N1sc u0 p2 c-1 {1,S}
4   H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.0235,-3.93339,-6.22557,-8.66482,-12.2588,-14.1597,-18.4947],'J/(mol*K)'),
        H298 = (396.573,'kJ/mol'),
        S298 = (-4.08993,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 649,
    label = "N3dJ-Cd-COH_679",
    group = 
"""
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2 * N3d u1 p1 c0 {1,D}
3   CO  u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.69701,-3.88068,-5.81322,-7.75837,-11.2823,-14.0105,-18.3584],'J/(mol*K)'),
        H298 = (382.09,'kJ/mol'),
        S298 = (6.06044,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 650,
    label = "N3dJ-Cdd-O2d_719",
    group = 
"""
1   Cdd u0 p0 c0 {2,D} {3,D}
2 * N3d u1 p1 c0 {1,D}
3   O2d u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.16076,-7.17594,-8.15682,-9.04851,-10.6039,-11.9298,-14.5519],'J/(mol*K)'),
        H298 = (462.301,'kJ/mol'),
        S298 = (-12.2956,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 651,
    label = "N3dJ-Cd-CdH_723",
    group = 
"""
1   Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2 * N3d u1 p1 c0 {1,D}
3   Cd  u0 p0 c0 {1,S}
4   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.56495,-3.74955,-6.04967,-8.10046,-11.5093,-14.1448,-18.3552],'J/(mol*K)'),
        H298 = (383.091,'kJ/mol'),
        S298 = (5.3282,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 652,
    label = "N3dJ_O",
    group = 
"""
1 * N3d u1 p1 {2,D}
2   O   u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.12,-1.36,-1.67,-2,-2.62,-3.11,-3.89],'cal/(mol*K)'),
        H298 = (48.613,'kcal/mol'),
        S298 = (-3.69,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t HN=O and [N]=O, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 653,
    label = "N3dJ_N",
    group = 
"""
1 * N3d u1 p1 {2,D}
2   N   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.14,-0.51,-0.97,-1.46,-2.33,-3.02,-4.16],'cal/(mol*K)'),
        H298 = (64.083,'kcal/mol'),
        S298 = (1.49,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t HN=NH and [N]=NH, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 654,
    label = "N3dJ-N3d-Cd_509",
    group = 
"""
1   N3d u0 p1 c0 {2,D} {3,S}
2 * N3d u1 p1 c0 {1,D}
3   Cd  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.0548,-1.14716,-4.15633,-6.85971,-11.2475,-14.4103,-18.8629],'J/(mol*K)'),
        H298 = (301.206,'kJ/mol'),
        S298 = (11.2468,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 655,
    label = "N3dJ-N3d-CO_528",
    group = 
"""
1   N3d u0 p1 c0 {2,D} {3,S}
2 * N3d u1 p1 c0 {1,D}
3   CO  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.24972,-1.40812,-4.38713,-7.22779,-11.5383,-14.1769,-18.8222],'J/(mol*K)'),
        H298 = (279.24,'kJ/mol'),
        S298 = (-0.78999,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 656,
    label = "N3dJ-N3d-Ct_584",
    group = 
"""
1   N3d u0 p1 c0 {2,D} {3,S}
2 * N3d u1 p1 c0 {1,D}
3   Ct  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.781155,-1.7982,-4.84207,-7.76127,-12.1183,-14.8129,-18.3133],'J/(mol*K)'),
        H298 = (307.753,'kJ/mol'),
        S298 = (8.66171,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 657,
    label = "N3dJ-N3d-N3s_644",
    group = 
"""
1   N3d u0 p1 c0 {2,D} {3,S}
2 * N3d u1 p1 c0 {1,D}
3   N3s u0 p1 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.905972,-3.08001,-5.52543,-7.90585,-11.9081,-14.5315,-18.6409],'J/(mol*K)'),
        H298 = (316.02,'kJ/mol'),
        S298 = (-0.869194,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 658,
    label = "N3dJ-N3d-Cs_652",
    group = 
"""
1   N3d u0 p1 c0 {2,D} {3,S}
2 * N3d u1 p1 c0 {1,D}
3   Cs  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.01066,-1.15303,-4.68112,-7.74748,-12.6773,-16.117,-20.8539],'J/(mol*K)'),
        H298 = (249.456,'kJ/mol'),
        S298 = (16.2055,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 659,
    label = "N3dJ-N5dc-HO0sc_658",
    group = 
"""
1   N5dc u0 p0 c+1 {2,D} {3,S} {4,S}
2 * N3d  u1 p1 c0 {1,D}
3   O0sc u0 p3 c-1 {1,S}
4   H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.24671,-3.27841,-5.50322,-7.65082,-11.1182,-13.75,-18.0589],'J/(mol*K)'),
        H298 = (388.881,'kJ/mol'),
        S298 = (4.76187,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 660,
    label = "N5dcJ-CdO0sc_451",
    group = 
"""
1 * N5dc u1 p0 c+1 {2,S} {3,D}
2   O0sc u0 p3 c-1 {1,S}
3   Cd   u0 p0 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.06879,-3.74741,-6.31672,-8.48733,-11.9226,-14.5565,-18.7194],'J/(mol*K)'),
        H298 = (320.184,'kJ/mol','+|-',21.1806),
        S298 = (6.14787,'J/(mol*K)','+|-',5.17873),
    ),
    shortDesc = """Average from child nodes: N5dcJ-CdO0sc-CsH_450 N5dcJ-CdO0sc-HN3d_494 N5dcJ-CdO0sc-HN3s_497 N5dcJ-CdO0sc-CdH_565 N5dcJ-CdO0sc-HH_669 N5dcJ-CdO0sc-COH_691 N5dcJ-CdO0sc-HO2s_729""",
    longDesc = 
"""

""",
)

entry(
    index = 661,
    label = "N5dcJ-CdO0sc-CsH_450",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 * N5dc u1 p0 c+1 {1,D} {5,S}
3   Cs   u0 p0 c0 {1,S}
4   H    u0 p0 c0 {1,S}
5   O0sc u0 p3 c-1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.98705,-4.49609,-6.74256,-8.73681,-12.1074,-14.7806,-18.7852],'J/(mol*K)'),
        H298 = (313.191,'kJ/mol'),
        S298 = (3.95379,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 662,
    label = "N5dcJ-CdO0sc-HN3d_494",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 * N5dc u1 p0 c+1 {1,D} {5,S}
3   N3d  u0 p1 c0 {1,S}
4   H    u0 p0 c0 {1,S}
5   O0sc u0 p3 c-1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.85556,-4.66606,-6.72595,-8.73605,-12.0688,-14.6341,-18.7192],'J/(mol*K)'),
        H298 = (321.632,'kJ/mol'),
        S298 = (6.016,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 663,
    label = "N5dcJ-CdO0sc-HN3s_497",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 * N5dc u1 p0 c+1 {1,D} {5,S}
3   N3s  u0 p1 c0 {1,S}
4   H    u0 p0 c0 {1,S}
5   O0sc u0 p3 c-1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.55779,-4.14461,-6.83963,-9.01953,-12.0043,-14.2858,-18.4757],'J/(mol*K)'),
        H298 = (328.225,'kJ/mol'),
        S298 = (3.56515,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 664,
    label = "N5dcJ-CdO0sc-CdH_565",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 * N5dc u1 p0 c+1 {1,D} {5,S}
3   Cd   u0 p0 c0 {1,S}
4   H    u0 p0 c0 {1,S}
5   O0sc u0 p3 c-1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.174064,-3.13084,-5.85144,-8.07581,-11.6728,-14.3549,-18.4779],'J/(mol*K)'),
        H298 = (312.681,'kJ/mol'),
        S298 = (7.78877,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 665,
    label = "N5dcJ-CdO0sc-HH_669",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 * N5dc u1 p0 c+1 {1,D} {5,S}
3   H    u0 p0 c0 {1,S}
4   H    u0 p0 c0 {1,S}
5   O0sc u0 p3 c-1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.36471,-3.8355,-6.48192,-8.70804,-12.049,-14.6161,-18.6646],'J/(mol*K)'),
        H298 = (308.382,'kJ/mol'),
        S298 = (3.69546,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 666,
    label = "N5dcJ-CdO0sc-COH_691",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 * N5dc u1 p0 c+1 {1,D} {5,S}
3   CO   u0 p0 c0 {1,S}
4   H    u0 p0 c0 {1,S}
5   O0sc u0 p3 c-1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.07742,-3.60321,-5.89998,-7.96176,-11.4508,-14.2044,-18.6535],'J/(mol*K)'),
        H298 = (318.089,'kJ/mol'),
        S298 = (7.65521,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 667,
    label = "N5dcJ-CdO0sc-HO2s_729",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 * N5dc u1 p0 c+1 {1,D} {5,S}
3   O2s  u0 p2 c0 {1,S}
4   H    u0 p0 c0 {1,S}
5   O0sc u0 p3 c-1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.18693,-2.35557,-5.67555,-8.17332,-12.1055,-15.0195,-19.2595],'J/(mol*K)'),
        H298 = (339.086,'kJ/mol'),
        S298 = (10.3607,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 668,
    label = "N5dcJ-N1scO2d_496",
    group = 
"""
1 * N5dc u1 p0 c+1 {2,D} {3,S}
2   O2d  u0 p2 c0 {1,D}
3   N1sc u0 p2 c-1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.82557,-1.42948,-4.33205,-6.82767,-11.2157,-14.3717,-18.5315],'J/(mol*K)'),
        H298 = (335.778,'kJ/mol','+|-',27.0015),
        S298 = (11.5743,'J/(mol*K)','+|-',19.0228),
    ),
    shortDesc = """Average from child nodes: N5dcJ-N1scO2d-O2s_495 N5dcJ-N1scO2d-Cs_685""",
    longDesc = 
"""

""",
)

entry(
    index = 669,
    label = "N5dcJ-N1scO2d-O2s_495",
    group = 
"""
1   N1sc u0 p2 c-1 {2,S} {4,S}
2 * N5dc u1 p0 c+1 {1,S} {3,D}
3   O2d  u0 p2 c0 {2,D}
4   O2s  u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.95141,-0.909818,-4.01425,-6.69571,-11.0969,-14.0617,-18.5507],'J/(mol*K)'),
        H298 = (345.324,'kJ/mol'),
        S298 = (4.84874,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 670,
    label = "N5dcJ-N1scO2d-Cs_685",
    group = 
"""
1   N1sc u0 p2 c-1 {2,S} {4,S}
2 * N5dc u1 p0 c+1 {1,S} {3,D}
3   O2d  u0 p2 c0 {2,D}
4   Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.69973,-1.94915,-4.64985,-6.95963,-11.3345,-14.6817,-18.5122],'J/(mol*K)'),
        H298 = (326.231,'kJ/mol'),
        S298 = (18.2999,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 671,
    label = "N5dcJ-CddO0sc_515",
    group = 
"""
1 * N5dc u1 p0 c+1 {2,S} {3,D}
2   O0sc u0 p3 c-1 {1,S}
3   Cdd  u0 p0 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.169902,-3.3898,-6.21492,-8.65999,-12.5418,-15.2795,-19.1329],'J/(mol*K)'),
        H298 = (250.978,'kJ/mol','+|-',51.7559),
        S298 = (0.70915,'J/(mol*K)','+|-',10.8469),
    ),
    shortDesc = """Average from child nodes: N5dcJ-CddO0sc-Cdd_514 N5dcJ-CddO0sc-O2d_593 N5dcJ-CddO0sc-N3d_604 N5dcJ-CddO0sc-Cd_656""",
    longDesc = 
"""

""",
)

entry(
    index = 672,
    label = "N5dcJ-CddO0sc-Cdd_514",
    group = 
"""
1   Cdd  u0 p0 c0 {2,D} {4,D}
2 * N5dc u1 p0 c+1 {1,D} {3,S}
3   O0sc u0 p3 c-1 {2,S}
4   Cdd  u0 p0 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.53288,-1.60106,-4.87683,-7.55365,-11.7646,-14.7578,-18.8707],'J/(mol*K)'),
        H298 = (282.728,'kJ/mol'),
        S298 = (6.96811,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 673,
    label = "N5dcJ-CddO0sc-O2d_593",
    group = 
"""
1   Cdd  u0 p0 c0 {2,D} {4,D}
2 * N5dc u1 p0 c+1 {1,D} {3,S}
3   O0sc u0 p3 c-1 {2,S}
4   O2d  u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.99037,-7.96334,-9.73353,-11.3022,-13.8987,-15.9025,-19.1594],'J/(mol*K)'),
        H298 = (223.132,'kJ/mol'),
        S298 = (-5.16618,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 674,
    label = "N5dcJ-CddO0sc-N3d_604",
    group = 
"""
1   Cdd  u0 p0 c0 {2,D} {4,D}
2 * N5dc u1 p0 c+1 {1,D} {3,S}
3   O0sc u0 p3 c-1 {2,S}
4   N3d  u0 p1 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.895277,-3.17974,-6.23468,-8.72242,-12.635,-15.4156,-19.261],'J/(mol*K)'),
        H298 = (259.465,'kJ/mol'),
        S298 = (3.20743,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 675,
    label = "N5dcJ-CddO0sc-Cd_656",
    group = 
"""
1   Cdd  u0 p0 c0 {2,D} {4,D}
2 * N5dc u1 p0 c+1 {1,D} {3,S}
3   O0sc u0 p3 c-1 {2,S}
4   Cd   u0 p0 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.8826,-0.815083,-4.01463,-7.06168,-11.8689,-15.0421,-19.2406],'J/(mol*K)'),
        H298 = (238.589,'kJ/mol'),
        S298 = (-2.17276,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 676,
    label = "N5dcJ-N3dO0sc_525",
    group = 
"""
1 * N5dc u1 p0 c+1 {2,S} {3,D}
2   O0sc u0 p3 c-1 {1,S}
3   N3d  u0 p1 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.265394,-2.41798,-4.98104,-7.32942,-11.0368,-13.8784,-18.4003],'J/(mol*K)'),
        H298 = (317.726,'kJ/mol','+|-',51.9482),
        S298 = (5.59998,'J/(mol*K)','+|-',7.83286),
    ),
    shortDesc = """Average from child nodes: N5dcJ-N3dO0sc-Cs_524 N5dcJ-N3dO0sc-N3s_555 N5dcJ-N3dO0sc-H_583""",
    longDesc = 
"""

""",
)

entry(
    index = 677,
    label = "N5dcJ-N3dO0sc-Cs_524",
    group = 
"""
1   N3d  u0 p1 c0 {2,D} {4,S}
2 * N5dc u1 p0 c+1 {1,D} {3,S}
3   O0sc u0 p3 c-1 {2,S}
4   Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.180942,-3.03035,-5.61746,-7.94982,-11.7556,-14.5767,-18.7436],'J/(mol*K)'),
        H298 = (322.357,'kJ/mol'),
        S298 = (4.22869,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 678,
    label = "N5dcJ-N3dO0sc-N3s_555",
    group = 
"""
1   N3d  u0 p1 c0 {2,D} {4,S}
2 * N5dc u1 p0 c+1 {1,D} {3,S}
3   O0sc u0 p3 c-1 {2,S}
4   N3s  u0 p1 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.21685,-1.03748,-3.83744,-6.20365,-9.78629,-12.7259,-17.7422],'J/(mol*K)'),
        H298 = (341.073,'kJ/mol'),
        S298 = (10.0177,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 679,
    label = "N5dcJ-N3dO0sc-H_583",
    group = 
"""
1   N3d  u0 p1 c0 {2,D} {4,S}
2 * N5dc u1 p0 c+1 {1,D} {3,S}
3   O0sc u0 p3 c-1 {2,S}
4   H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.23972,-3.18611,-5.48824,-7.83479,-11.5685,-14.3326,-18.715],'J/(mol*K)'),
        H298 = (289.748,'kJ/mol'),
        S298 = (2.55359,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 680,
    label = "N5dcJ-O0scO2d_574",
    group = 
"""
1 * N5dc u1 p0 c+1 {2,S} {3,D}
2   O0sc u0 p3 c-1 {1,S}
3   O2d  u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.72545,-3.72637,-5.93536,-8.1239,-11.8542,-14.5654,-18.842],'J/(mol*K)'),
        H298 = (296.984,'kJ/mol'),
        S298 = (1.77574,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Nitrogen_G4 ThermoLibrary""",
    longDesc = 
"""

""",
)

entry(
    index = 681,
    label = "SiJ",
    group = 
"""
1 * Si u1
""",
    thermo = 'CJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 682,
    label = "SJ",
    group = 
"""
1 * S u1
""",
    thermo = 'S2J',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 683,
    label = "S2J",
    group = 
"""
1 * S2s u1 p2
""",
    thermo = 'S2J-C',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 684,
    label = "S2J-H",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.2,-1.52,-1.84,-2.17,-2.73,-3.2,-3.95],'cal/(mol*K)'),
        H298 = (91.82,'kcal/mol'),
        S298 = (-4.62,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 685,
    label = "S2J-C",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   C   u0 {1,S}
""",
    thermo = 'S2J-Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 686,
    label = "S2J-Cs",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Cs  u0 {1,S}
""",
    thermo = 'S2sJ-(CsHHH)',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 687,
    label = "S2sJ-(CsHHH)",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * S2s u1 p2 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.35,-1.58,-1.87,-2.16,-2.66,-3.11,-3.95],'cal/(mol*K)'),
        H298 = (87.08,'kcal/mol'),
        S298 = (-3.45,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 688,
    label = "S2J-(Cs-Cb)",
    group = 
"""
1   Cs  u0 {2,S} {3,S}
2 * S2s u1 p2 {1,S}
3   Cb  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.29,-3.84,-4.16,-4.58,-5.31,-5.9,-6.84],'cal/(mol*K)'),
        H298 = (86.83,'kcal/mol'),
        S298 = (-4.81,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 689,
    label = "S2J-Ct",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Ct  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.18,-2.05,-2.66,-3.12,-3.76,-4.24,-4.99],'cal/(mol*K)'),
        H298 = (77.56,'kcal/mol'),
        S298 = (-4.6,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 690,
    label = "S2J-Cb",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Cb  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.92,-2.1,-2.3,-2.51,-2.93,-3.32,-3.96],'cal/(mol*K)'),
        H298 = (81.36,'kcal/mol'),
        S298 = (-3.66,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 691,
    label = "S2J-Cd",
    group = 
"""
1   Cd  u0 {2,S} {3,D}
2 * S2s u1 p2 {1,S}
3   C   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.29,-2.56,-2.72,-2.87,-3.19,-3.52,-4.13],'cal/(mol*K)'),
        H298 = (79.29,'kcal/mol'),
        S298 = (-1.79,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 692,
    label = "S2J-C=S",
    group = 
"""
1   CS  u0 {2,S} {3,D}
2 * S2s u1 p2 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.93,-3.56,-3.88,-4.08,-4.41,-4.74,-5.25],'cal/(mol*K)'),
        H298 = (80.07,'kcal/mol'),
        S298 = (-0.7,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 693,
    label = "S2J-CO",
    group = 
"""
1   CO  u0 {2,S} {3,D}
2 * S2s u1 p2 {1,S}
3   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.26,-2.82,-3.17,-3.44,-3.89,-4.29,-4.95],'cal/(mol*K)'),
        H298 = (89.6,'kcal/mol'),
        S298 = (-0.42,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 CAC""",
    longDesc = 
"""

""",
)

entry(
    index = 694,
    label = "S2J-S2s",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   S2s u0 p2 {1,S}
""",
    thermo = 'S2J-S2s-H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 695,
    label = "S2J-S2s-H",
    group = 
"""
1   S2s u0 p2 {2,S} {3,S}
2 * S2s u1 p2 {1,S}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.93,-2.7,-3.26,-3.67,-4.24,-4.59,-5],'cal/(mol*K)'),
        H298 = (73.97,'kcal/mol'),
        S298 = (-2.53,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 696,
    label = "S2J-S2s-Cs",
    group = 
"""
1   S2s u0 p2 {2,S} {3,S}
2 * S2s u1 p2 {1,S}
3   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.95,-3.43,-3.78,-4.06,-4.47,-4.74,-5.03],'cal/(mol*K)'),
        H298 = (71.05,'kcal/mol'),
        S298 = (-1.7,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 697,
    label = "S2J-S2s-S2s",
    group = 
"""
1   S2s u0 p2 {2,S} {3,S}
2 * S2s u1 p2 {1,S}
3   S2s u0 p2 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.63,-4.32,-4.84,-5.26,-5.82,-6.07,-5.99],'cal/(mol*K)'),
        H298 = (72.74,'kcal/mol'),
        S298 = (0.6,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 698,
    label = "S2sJ-O",
    group = 
"""
1 * S2s u1 p2 c0 {2,S}
2   O2s u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.15904,-4.00975,-4.36187,-4.91092,-5.32059,-5.53025,-5.75797],'cal/(mol*K)'),
        H298 = (108.577,'kcal/mol'),
        S298 = (-7.47722,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 699,
    label = "S4sJ",
    group = 
"""
1 * S4s u1 p1
""",
    thermo = 'S4sJ-CCC',
    shortDesc = """Sulfur Oxygen Extension""",
    longDesc = 
"""
"
""",
)

entry(
    index = 700,
    label = "S4sJ-CCC",
    group = 
"""
1 * S4s u1 p1 c0 {2,S} {3,S} {4,S}
2   C   ux {1,S}
3   C   ux {1,S}
4   C   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.055,-3.801,-4.696,-5.408,-6.524,-7.325,-8.52],'cal/(mol*K)'),
        H298 = (63.249,'kcal/mol'),
        S298 = (12.849,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
Calculated at CBS-QB3
""",
)

entry(
    index = 701,
    label = "S4sJ-OCC",
    group = 
"""
1 * S4s u1 p1 c0 {2,S} {3,S} {4,S}
2   O   ux {1,S}
3   C   ux {1,S}
4   C   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.475,-0.55,-2.75,-4.66,-7.27,-9.325,-8.64],'cal/(mol*K)'),
        H298 = (21.67,'kcal/mol'),
        S298 = (15.449,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
Based on radical calculations at CBS-QB3
""",
)

entry(
    index = 702,
    label = "S4dJ",
    group = 
"""
1 * S4d u1 p1
""",
    thermo = 'S4dJ-OdO',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 703,
    label = "S4dJ-OdH",
    group = 
"""
1 * S4d u1 p1 c0 {2,D} {3,S}
2   O2d u0 p2 c0 {1,D}
3   H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.51,-1.2,-1.93,-2.59,-3.6,-4.27,-5.1],'cal/(mol*K)'),
        H298 = (58,'kcal/mol'),
        S298 = (0.54,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 704,
    label = "S4dJ-OdO",
    group = 
"""
1 * S4d u1 p1 c0 {2,D} {3,S}
2   O2d u0 p2 c0 {1,D}
3   O2s u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71,-2.41,-3.09,-3.65,-4.42,-4.89,-5.45],'cal/(mol*K)'),
        H298 = (58.9,'kcal/mol'),
        S298 = (0.14,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 705,
    label = "S6sJ",
    group = 
"""
1 * S6s u1 p0
""",
    thermo = 'S6sJ-CCCCC',
    shortDesc = """Calculated at CBS-QB3""",
    longDesc = 
"""
"
""",
)

entry(
    index = 706,
    label = "S6sJ-CCCCC",
    group = 
"""
1 * S6s u1 p0 c0 {2,S} {3,S} {4,S} {5,S} {6,S}
2   C   ux {1,S}
3   C   ux {1,S}
4   C   ux {1,S}
5   C   ux {1,S}
6   C   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.815,3.48,2.34,1.364,-0.161,-1.233,-2.644],'cal/(mol*K)'),
        H298 = (60.164,'kcal/mol'),
        S298 = (9.723,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 707,
    label = "S6dJ",
    group = 
"""
1 * S6d u1 p0
""",
    thermo = 'S6dJ-OdOCC',
    shortDesc = """Calculated at CBS-QB3""",
    longDesc = 
"""
"
""",
)

entry(
    index = 708,
    label = "S6dJ-OdOCC",
    group = 
"""
1 * S6d u1 p0 c0 {2,S} {3,S} {4,S} {5,D}
2   O   ux {1,S}
3   C   ux {1,S}
4   C   ux {1,S}
5   O   ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.35,1.6,-0.19,-0.45,-0.95,-1.42,-3.65],'cal/(mol*K)'),
        H298 = (56.531,'kcal/mol'),
        S298 = (3.34,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
Based on radical calculations at CBS-QB3
""",
)

entry(
    index = 709,
    label = "S6ddJ",
    group = 
"""
1 * S6dd u1 p0
""",
    thermo = 'S6ddJ-OdOdO',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 710,
    label = "S6ddJ-OdOdH",
    group = 
"""
1 * S6dd u1 p0 c0 {2,D} {3,D} {4,S}
2   O2d  u0 p2 c0 {1,D}
3   O2d  u0 p2 c0 {1,D}
4   H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.977,0.64,-0.027,-0.741,-1.913,-2.873,-4.269],'cal/(mol*K)'),
        H298 = (75.948,'kcal/mol'),
        S298 = (3.331,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 711,
    label = "S6ddJ-OdOdO",
    group = 
"""
1 * S6dd u1 p0 c0 {2,D} {3,D} {4,S}
2   O2d  u0 p2 c0 {1,D}
3   O2d  u0 p2 c0 {1,D}
4   O2s  u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.539,-1.537,-2.332,-2.933,-4.01,-4.785,-5.701],'cal/(mol*K)'),
        H298 = (86.194,'kcal/mol'),
        S298 = (4.146,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 712,
    label = "RJ2_triplet",
    group = 
"""
1 * R!H u2
""",
    thermo = 'CJ2_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 713,
    label = "CJ2_triplet",
    group = 
"""
1 * C u2
""",
    thermo = 'CsJ2_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 714,
    label = "OsCsJ2H_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   O  u0 p2 {1,S} {4,S}
3   H  u0 {1,S}
4   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.444,-1.111,-1.988,-2.889,-4.529,-5.915,-8.422],'cal/(mol*K)'),
        H298 = (205.773,'kcal/mol'),
        S298 = (-2.011,'cal/(mol*K)'),
    ),
    shortDesc = """Fittted to DFT_QCI_thermo library""",
    longDesc = 
"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 715,
    label = "CsJ2_triplet",
    group = 
"""
1 * Cs u2
""",
    thermo = 'CH2_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 716,
    label = "CH2_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   H  u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.27,-1.08,-2.14,-3.23,-5.18,-6.74,-9.47],'cal/(mol*K)'),
        H298 = (214.44,'kcal/mol'),
        S298 = (-1.73,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated for methylene in relation to methane from NIST values""",
    longDesc = 
"""

""",
)

entry(
    index = 717,
    label = "CsJ2_P_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   C  u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = 'CsCsJ2_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 718,
    label = "CsCsJ2_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   Cs u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = 'CCJ2_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 719,
    label = "CCJ2_triplet",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u2 {1,S} {6,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.81,-1.74,-2.69,-3.61,-5.18,-6.42,-8.36],'cal/(mol*K)'),
        H298 = (211.3,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """BDE and Cp calculated from data in KIM et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 720,
    label = "PhCH_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   Cb u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (195,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """BDE from PUTSMA et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 721,
    label = "AllylJ2_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   Cd u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (192.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """BDE from PUTSMA et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 722,
    label = "CsJ2_S_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
""",
    thermo = 'CsJ2_P_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 723,
    label = "CdJ2_triplet",
    group = 
"""
1 * [Cd,CO] u2
""",
    thermo = 'CCdJ2_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 724,
    label = "CCdJ2_triplet",
    group = 
"""
1 * Cd u2 {2,D}
2   C  u0 {1,D}
""",
    thermo = 'CdCdJ2_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 725,
    label = "CdCdJ2_triplet",
    group = 
"""
1   Cd u0 {2,D} {3,S} {4,S}
2 * Cd u2 {1,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.904,-2.152,-3.433,-4.583,-6.214,-7.197,-9.27],'cal/(mol*K)'),
        H298 = (237.632,'kcal/mol'),
        S298 = (1.79,'cal/(mol*K)'),
    ),
    shortDesc = """Fittted to DFT_QCI_thermo library""",
    longDesc = 
"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

    Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
    J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 726,
    label = "(CO)CdJ2_triplet",
    group = 
"""
1   Cdd u0 {2,D} {3,D}
2 * Cd  u2 {1,D}
3   O   u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.763,-2.732,-3.654,-4.473,-5.712,-6.563,-8.315],'cal/(mol*K)'),
        H298 = (206.595,'kcal/mol'),
        S298 = (-1.634,'cal/(mol*K)'),
    ),
    shortDesc = """Fittted to DFT_QCI_thermo library""",
    longDesc = 
"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

    Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
    J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 727,
    label = "CdJ2-Sd_triplet",
    group = 
"""
1 * CS  u2 {2,D}
2   S2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.42,-2.3,-3.22,-4.04,-5.42,-6.5,-8.29],'cal/(mol*K)'),
        H298 = (238.75,'kcal/mol'),
        S298 = (-3.31,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 728,
    label = "NJ2_triplet",
    group = 
"""
1 * N u2
""",
    thermo = 'NJ2_C',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 729,
    label = "N3sJ2",
    group = 
"""
1 * N3s u2 p1
""",
    thermo = 'NJ2_C',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 730,
    label = "NHJ2",
    group = 
"""
1 * N3s u2 p1 {2,S}
2   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-2.1,-2.78,-3.47,-4.75,-5.77,-7.61],'cal/(mol*K)'),
        H298 = (200.636,'kcal/mol'),
        S298 = (-2.72,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t NH3 and [N], both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 731,
    label = "NJ2_C",
    group = 
"""
1 * N3s u2 p1 {2,S}
2   C   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.36,-2.97,-3.51,-4,-5,-5.96,-7.75],'cal/(mol*K)'),
        H298 = (184.816,'kcal/mol'),
        S298 = (-3.04,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t NH2CH3 and [N]CH3, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 732,
    label = "NJ2_O",
    group = 
"""
1 * N3s u2 p1 {2,S}
2   O   u0 p2 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05,-3.22,-4.34,-5.36,-6.88,-7.91,-9.25],'cal/(mol*K)'),
        H298 = (166.156,'kcal/mol'),
        S298 = (-0.91,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t NH2OH and [N]OH, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 733,
    label = "Oa_triplet",
    group = 
"""
1 * O u2
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.8,-3.05,-3.33,-3.62,-4.24,-4.86,-6.28],'cal/(mol*K)'),
        H298 = (221.55,'kcal/mol'),
        S298 = (-8.02,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated for atomic oxygen in relation to water from NIST values""",
    longDesc = 
"""

""",
)

entry(
    index = 734,
    label = "SiJ2_triplet",
    group = 
"""
1 * Si u2
""",
    thermo = 'CJ2_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 735,
    label = "SJ2_triplet",
    group = 
"""
1 * S u2
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.19,-3.52,-3.89,-4.3,-5.12,-5.86,-7.14],'cal/(mol*K)'),
        H298 = (176.42,'kcal/mol'),
        S298 = (-12.02,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 736,
    label = "RJ3",
    group = 
"""
1 * R!H u3
""",
    thermo = 'CJ3',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 737,
    label = "CJ3",
    group = 
"""
1 * Cs u3
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.57,-2.73,-4.11,-5.5,-7.92,-9.85,-12.95],'cal/(mol*K)'),
        H298 = (316.19,'kcal/mol'),
        S298 = (-5.7,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated for methylidyene in relation to methane from NIST values""",
    longDesc = 
"""

""",
)

entry(
    index = 738,
    label = "SiJ3",
    group = 
"""
1 * Sis u3
""",
    thermo = 'CJ3',
    shortDesc = """""",
    longDesc = 
"""

""",
)

tree(
"""
L1: Radical
    L2: RJ
        L3: CJ
            L4: CsJ
                L5: CH3
                L5: Cs_P
                    L6: CJCO
                        L7: C=C(O)CJ
                        L7: CJCOOH
                        L7: CJC(C)OC
                        L7: CJC(C)2O
                            L8: C=CC(C)(O)CJ
                                L9: C=CC(O)(C=O)CJ
                            L8: CJC(C)(C=O)O
                        L7: CJC(O)2C
                            L8: C=CC(O)2CJ
                    L6: CJCC=O
                        L7: CJC(C)2C=O
                            L8: CJC(C=O)2C
                                L9: C=CC(C=O)2CJ
                            L8: C=CC(C)(C=O)CJ
                        L7: CJC(C)C=O
                        L7: C=C(C=O)CJ
                    L6: CJCC=C=O
                        L7: CJC(C)C=C=O
                        L7: C=C(CJ)C=C=O
                    L6: CsCsJ
                        L7: CCJ
                        L7: RCCJ
                        L7: Neopentyl
                        L7: Isobutyl
                        L7: CsJ-CsHH-HHN3s_513
                        L7: CsJ-CsHH-HHN3d_537
                    L6: Benzyl_P
                    L6: Allyl_P
                        L7: C=CC=CCJ
                        L7: CTCC=CCJ
                        L7: CJC=C=O
                        L7: CsJ-CdHH-HN3d_582
                        L7: CsJ-CdHH-HN5dc_693
                    L6: Propargyl
                        L7: CsJ-CtHH-N3t_522
                    L6: CJC=O
                        L7: C2JC=O
                L5: Cs_S
                    L6: CCJCO
                        L7: C=CCJCO
                            L8: C=CCJC(O)C=C
                        L7: CCJCOOH
                    L6: CCJCC=O
                    L6: CCJC(C)=C=O
                    L6: (Cs)2CsJ
                        L7: cyclopentene-4
                            L8: bicyclo[2.1.1]hex-2-ene-C5
                                L9: tricyclo[2.1.1.0(1,4)]hex-2-ene-C5
                            L8: bicyclo[2.1.0]pent-2-ene-C5
                        L7: bicyclo[1.1.1]pentane-C2
                            L8: tricyclo[1.1.1.0(1,3)]pentane-C2
                        L7: bicyclo[2.1.1]hexane-C5
                            L8: tricyclo[2.1.1.0(1,4)]hexane-C5
                        L7: cyclopropane
                            L8: spiro[2.2]pentane-secondary
                            L8: tricyclo[2.2.1.0(1,4)]heptane-C7
                            L8: bicyclo[2.1.0]pentane-secondary-C3
                            L8: tricyclo[3.1.1.0(1,5)]heptane-C6
                            L8: bicyclo[1.1.0]butane-secondary
                            L8: bicyclo[3.1.0]hexane-C3
                            L8: bicyclo[4.1.0]heptane-C3-7
                            L8: bicyclo[4.1.0]heptane-C3-7
                        L7: tricyclo[2.1.1.0(1,4)]hexane-C2
                        L7: bicyclo[3.1.1]heptane-C6
                        L7: tricyclo[2.2.1.0(1,4)]heptane-C2
                        L7: bicyclo[4.2.0]octane-C4-7
                        L7: bicyclo[2.2.2]octane-C2
                            L8: tricyclo[2.2.2.0(1,4)]octane-C2
                        L7: cyclobutane
                            L8: bicyclo[2.1.0]pentane-secondary-C4
                            L8: bicyclo[2.2.0]hexane-secondary
                            L8: bicyclo[3.2.0]heptane-C5-6
                            L8: tricyclo[2.2.1.0(1,4)]heptane-C2
                            L8: bicyclo[4.2.0]octane-C4-7
                        L7: bicyclo[3.1.1]heptane-C2
                            L8: tricyclo[3.1.1.0(1,5)]heptane-C2
                        L7: bicyclo[3.1.0]hexane-C5-2
                        L7: bicyclo[3.1.0]hexane-C5-3
                        L7: bicyclo[2.1.1]hexane-C2
                        L7: 7-norbornyl
                        L7: 2-norbornyl
                        L7: bicyclo[4.1.0]heptane-C6-2
                        L7: bicyclo[4.1.0]heptane-C6-3
                        L7: bicyclo[4.1.0]heptane-C6-3
                        L7: cycloheptane
                            L8: bicyclo[3.2.0]heptane-C5-2
                            L8: bicyclo[3.2.0]heptane-C5-3
                        L7: bicyclo[4.1.0]heptane-C6-2
                        L7: bicyclo[3.1.1]heptane-C3
                            L8: tricyclo[3.1.1.0(1,5)]heptane-C3
                        L7: octahydro-pentalene-C5-2
                        L7: octahydro-pentalene-C5-3
                        L7: bicyclo[4.2.0]octane-C6-2
                        L7: bicyclo[4.2.0]octane-C6-3
                        L7: CCJC
                        L7: RCCJC
                        L7: RCCJCC
                            L8: cyclopentane
                            L8: cyclohexane
                    L6: Benzyl_S
                        L7: Indenyl
                        L7: Benzyl_S_Fused5
                        L7: Benzyl_S_Fused6
                            L8: Benzyl_S_dihydronaphthalene
                        L7: Benzyl_S_Fused7
                    L6: Allyl_S
                        L7: Aromatic_pi_S_1_3
                            L8: Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
                                L9: Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
                                    L10: Aromatic_pi_S_(fused5)_1_3
                                    L10: Aromatic_pi_S_(fused6)_1_3
                                    L10: Aromatic_pi_S_(fused7)_1_3
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3
                            L8: Aromatic_pi_S_(CH3_CH3_Meta)_1_3_1
                                L9: Aromatic_pi_S_(CH3_C2H5_Meta)_1_3_1
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Meta)_1_3_1
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_3_1
                            L8: Aromatic_pi_S_(CH3_CH3_Meta)_1_3_2
                                L9: Aromatic_pi_S_(CH3_C2H5_Meta)_1_3_2
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Meta)_1_3_2
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_3_2
                            L8: Aromatic_pi_S_(CH3_CH3_Para)_1_3
                                L9: Aromatic_pi_S_(CH3_C2H5_Para)_1_3
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Para)_1_3
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Para)_1_3
                            L8: Aromatic_pi_S_(CH3_CH3_Sub)_1_3
                                L9: Aromatic_pi_S_(s1_3_6_diene_1_4)_1_3
                                L9: Aromatic_pi_S_(CH3_C2H5_Sub)_1_3
                                    L10: Aromatic_pi_S_(s1_4_6_diene_1_4)_1_3
                                    L10: Aromatic_pi_S_(s1_5_6_diene_1_4)_1_3
                                    L10: Aromatic_pi_S_(s1_6_6_diene_1_4)_1_3
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Sub)_1_3
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Sub)_1_3
                        L7: CJ-Cd-Benzene
                        L7: CJ-Cd-Benzene7
                        L7: cyclobutene-allyl
                        L7: cyclopentene-allyl
                        L7: cyclohexene-allyl
                        L7: CsJ-CdCsH-HHHHN3d_560
                        L7: CsJ-CdCsH-HHHHN5dc_636
                    L6: C=CCJC=C
                        L7: Aromatic_pi_S_1_4
                            L8: Aromatic_pi_S_(CH3_CH3_Ortho)_1_4
                                L9: Aromatic_pi_S_(CH3_C2H5_Ortho)_1_4
                                    L10: Aromatic_pi_S_(fused5)_1_4
                                    L10: Aromatic_pi_S_(fused6)_1_4
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_4
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_4
                            L8: Aromatic_pi_S_(CH3_CH3_Meta)_1_4
                                L9: Aromatic_pi_S_(CH3_C2H5_Meta)_1_4
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Meta)_1_4
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_4
                            L8: Aromatic_pi_S_(CH3_CH3_Sub)_1_4
                                L9: Aromatic_pi_S_(s1_3_6_diene_1_4)_1_4
                                L9: Aromatic_pi_S_(CH3_C2H5_Sub)_1_4
                                    L10: Aromatic_pi_S_(s1_4_6_diene_1_4)_1_4
                                    L10: Aromatic_pi_S_(s1_5_6_diene_1_4)_1_4
                                    L10: Aromatic_pi_S_(s1_6_6_diene_1_4)_1_4
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Sub)_1_4
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Sub)_1_4
                        L7: cyclopropenyl-allyl
                        L7: 1,3-cyclopentadiene-allyl
                        L7: C=CCJC=C=O
                    L6: Sec_Propargyl
                        L7: CsJ-CsCtH-HHHN3t_538
                    L6: CCJC=O
                        L7: CCJCHO
                        L7: C=OCJC=O
                L5: Cs_T
                    L6: CCJ(C)CO
                        L7: C2CJCOOH
                    L6: Tertalkyl
                        L7: bicyclo[1.1.0]butane-tertiary
                        L7: bicyclo[2.1.0]pentane-tertiary
                        L7: bicyclo[1.1.1]pentane-C1
                        L7: bicyclo[3.1.0]hexane-tertiary
                        L7: bicyclo[2.2.0]hexane-tertiary
                        L7: bicyclo[2.1.1]hexane-C1
                        L7: bridgehead_norbornyl
                        L7: bicyclo[3.2.0]heptane-tertiary
                        L7: bicyclo[4.1.0]heptane-tertiary
                        L7: bicyclo[3.1.1]heptane-C1
                        L7: octahydro-pentalene-tertiary
                        L7: bicyclo[4.2.0]octane-tertiary
                        L7: bicyclo[2.2.2]octane-C1
                    L6: Benzyl_T
                        L7: Benzyl_T_Fused5
                        L7: Benzyl_T_Fused6
                            L8: Benzyl_T_dihydronaphthalene
                    L6: CCJ(C)C=C=O
                        L7: C=CCJ(C)C=C=O
                            L8: C=CCJ(C=C=O)C=C
                    L6: Allyl_T
                        L7: Aromatic_pi_T_1_3
                            L8: Aromatic_pi_T_(CH3_CH3_Ortho)_1_3
                                L9: Aromatic_pi_T_(CH3_C2H5_Ortho)_1_3
                                    L10: Aromatic_pi_T_(fused5)_1_3
                                    L10: Aromatic_pi_T_(fused6)_1_3
                                    L10: Aromatic_pi_T_(CH3_Benzyl_Ortho)_1_3
                                        L11: Aromatic_pi_T_(CH3_EBenzyl_Ortho)_1_3
                        L7: Aromatic_pi_T_1_4
                            L8: Aromatic_pi_T_(CH3_CH3_Para)_1_4
                                L9: Aromatic_pi_T_(CH3_C2H5_Para)_1_4
                                    L10: Aromatic_pi_T_(CH3_Benzyl_Para)_1_4
                                        L11: Aromatic_pi_T_(CH3_EBenzyl_Para)_1_4
                        L7: bicyclo[2.1.0]pent-2-ene-C1
                        L7: bicyclo[2.1.1]hex-2-ene-C1
                        L7: bicyclo[2.2.0]hexa-2,5-diene-C1
                        L7: C=CCJ(C)C=O
                            L8: C=CCJ(C=O)C=C
                    L6: Tert_Propargyl
                    L6: C2CJCO
                        L7: C2CJCHO
                L5: CsJO
                    L6: CsJOH
                    L6: CsJOC
                        L7: CsJOCs
                            L8: CsJOCH3
                            L8: CsJOCC
                            L8: CsJOCC2
                            L8: CsJOCC3
                        L7: CsJOCds
                            L8: CsJOC(O)
                                L9: CsJOC(O)H
                                L9: CsJOC(O)C
                            L8: C=COCJ
                    L6: CsJOO
                        L7: CsJOOH
                        L7: CsJOOC
                    L6: CsJ-HHO2s-N3s_518
                    L6: CsJ-HHO2s-N3d_535
                    L6: CsJ-HHO2s-N1sc_594
                L5: CCsJO
                    L6: CCsJOC
                        L7: C=CCJ(O)C
                        L7: CCsJOCs
                        L7: CCsJOCds
                            L8: CCsJOC(O)
                                L9: CCsJOC(O)H
                                L9: CCsJOC(O)C
                    L6: C=CCJO
                    L6: OCJC=O
                    L6: CCsJOH
                        L7: CsJ-CdHO2s-HHN5dc_608
                        L7: CsJ-CsHO2s-HHHN3s_629
                    L6: CCsJOO
                        L7: CCsJOOH
                        L7: CCsJOOC
                    L6: CsJ-CsHO2s-HHHN3s_722
                L5: C2CsJO
                    L6: C2CsJOH
                    L6: C2CsJOC
                        L7: C2CsJOCs
                        L7: C2CsJOCds
                            L8: C2CsJOC(O)
                                L9: C2CsJOC(O)H
                                L9: C2CsJOC(O)C
                    L6: C2CsJOO
                        L7: C2CsJOOH
                        L7: C2CsJOOC
                L5: CsJ-S
                    L6: CsJ-SsHH
                    L6: CsJ-CSH
                        L7: CsJ-CsSsH
                        L7: CsJ-CtSsH
                        L7: CsJ-CbSsH
                        L7: CsJ-CdSsH
                        L7: CsJ-C=SSsH
                    L6: CsJ-CCS
                        L7: CsJ-CsCsSs
                        L7: CsJ-CsCtSs
                        L7: CsJ-CsCbSs
                        L7: CsJ-CsCdSs
                        L7: CsJ-CsC=SSs
                    L6: CsJ-SS
                        L7: CsJ-SsSsH
                        L7: CsJ-CSS
                            L8: CsJ-CsSsSs
                            L8: CsJ-CtSsSs
                            L8: CsJ-CbSsSs
                            L8: CsJ-CdSsSs
                            L8: CsJ-C=SSsSs
                        L7: CsJ-SsSsSs
                    L6: CCsJOS
                        L7: CCsJOHSH
                    L6: CsJ-SsOsH
                L5: CsJN
                    L6: CsJ-HHN3s-CdH_443
                    L6: CsJ-HHN3d-Cd_447
                    L6: CsJ-HHN3s-HO2s_449
                    L6: CsJ-HHN3s-HN3s_471
                    L6: CsJ-HHN3s-CtH_501
                    L6: CsJ-HHN3s-CsH_571
                    L6: CsJ-HHN3s-HN3d_578
                    L6: CsJ-HHN3d-Cdd_597
                    L6: CsJ-HHN3s-HH_649
                    L6: CsJ-HHN3d-N5dc_680
                L5: CCsJN
                    L6: CsJ-CsHN3s-HHHHH_486
                    L6: CsJ-CdHN3s-HHHN3d_585
                    L6: CsJ-CdHN3s-HHHN5dc_620
                    L6: CsJ-CdHN3s-CdHHH_668
                    L6: CsJ-CsHN3s-HHHHO2s_705
                    L6: CsJ-CsHN3s-HHHHN3s_716
                    L6: CsJ-CsHN3s-HHHHN3s_721
                    L6: CsJ-CsHN3s-HHHHO2s_726
                    L6: CsJ-CsHN3d-HHHN5dc_728
                L5: C2CsJN
                L5: OCJO
                    L6: CsJ-HO2sO2s-HN3s_466
                L5: CsJ-HN3sN3s_455
                    L6: CsJ-HN3sN3s-HHHN3s_454
                    L6: CsJ-HN3sN3s-CsHHH_489
                    L6: CsJ-HN3sN3s-HHHH_598
                    L6: CsJ-HN3sN3s-HHHO2s_695
                L5: CsJ-HN3sO2s_457
                    L6: CsJ-HN3sO2s-HHN3s_456
                    L6: CsJ-HN3sO2s-HHN3s_467
                    L6: CsJ-HN3sO2s-CsHH_488
                    L6: CsJ-HN3sO2s-CsHH_493
                    L6: CsJ-HN3sO2s-HHO2s_563
                    L6: CsJ-HN3sO2s-HHH_601
                    L6: CsJ-HN3sO2s-HHO2s_732
                L5: CsJ-HN3dN3s_465
                    L6: CsJ-HN3dN3s-CdHH_464
                    L6: CsJ-HN3dN3s-HHN5dc_474
                L5: CsJ-HN3dO2s_589
                    L6: CsJ-HN3dO2s-HO2d_588
                L5: CsJ-HN1scO2s_664
                    L6: CsJ-HN1scO2s-HN5dc_663
            L4: CdsJ
                L5: CdsJO
                    L6: HCdsJO
                    L6: CCJ=O
                        L7: CC(C)CJ=O
                            L8: CC(C)2CJ=O
                                L9: CC(C)(C=O)CJ=O
                                    L10: C=CC(C)(C=O)CJ=O
                                L9: C=CC(C)2CJ=O
                            L8: CC(C)(O)CJ=O
                                L9: C=CC(C)(O)CJ=O
                        L7: CCCJ=O
                            L8: C=OCCJ=O
                                L9: C=OC=OCJ=O
                            L8: C=C(C)CJ=O
                        L7: CsCJ=O
                            L8: COJ-CsO2d-HHN3s_684
                        L7: C=CCJ=O
                        L7: OC=OCJ=O
                        L7: COJ-CdO2d-HN3d_500
                        L7: COJ-CdO2d-HN5dc_678
                    L6: (O)CJO
                        L7: (O)CJOH
                        L7: (O)CJOC
                            L8: (O)CJOCH3
                            L8: (O)CJOCC
                            L8: (O)CJOCC2
                            L8: (O)CJOCC3
                        L7: COJ-O2dO2s-N3s_703
                    L6: SCJ=O
                    L6: COJ-N1scO2d_623
                        L7: COJ-N1scO2d-N5dc_622
                    L6: COJ-N3dO2d_626
                        L7: COJ-N3dO2d-Cd_625
                    L6: COJ-N3sO2d_646
                        L7: COJ-N3sO2d-HO2s_645
                        L7: COJ-N3sO2d-CsH_715
                L5: Cds_P
                    L6: C=C=CJ
                    L6: CdJ-CdH-HN3d_468
                    L6: CdJ-CddH-N3d_485
                    L6: CdJ-CdH-HN3s_542
                    L6: CdJ-CdH-HN1sc_613
                    L6: CdJ-CddH-N5dc_671
                L5: Cds_S
                    L6: C=CJC=O
                    L6: C=CJC=C
                        L7: cyclobutadiene-C1
                            L8: bicyclo[2.2.0]hexa-1(4),2,5-triene-C2
                        L7: 1,3-cyclopentadiene-vinyl-2
                        L7: CdJ-CdCd-HHHN5dc_547
                        L7: CdJ-CdCd-HHHN3d_606
                    L6: cyclopropenyl-vinyl
                    L6: cyclobutene-vinyl
                        L7: bicyclo[2.1.0]pent-2-ene-C2
                            L8: tricyclo[2.1.1.0(1,4)]hex-2-ene-C2
                        L7: bicyclo[2.2.0]hexa-2,5-diene-C2
                    L6: cyclopentene-vinyl
                        L7: bicyclo[2.1.1]hex-2-ene-C2
                    L6: 1,3-cyclopentadiene-vinyl-1
                    L6: CCCJ=C=O
                        L7: CC(C)CJ=C=O
                        L7: C=C(C)CJ=C=O
                    L6: OC=CJCb
                    L6: CdJ-CdCt-HHN3t_502
                    L6: CdJ-CdCs-HHHHN3s_545
                    L6: CdJ-CdCs-HHHHN3s_553
                    L6: CdJ-CddCs-HHHN3d_630
                    L6: CdJ-CddCs-HHHN5dc_718
                L5: S2s-CJ=C
                L5: C=CJO
                    L6: CdJ-CdO2s-HHN3s_519
                    L6: CdJ-CddO2s-HN5dc_527
                    L6: CdJ-CddO2s-HN3d_536
                    L6: CdJ-CdO2s-HHN3s_543
                L5: CdJ-CdN3d_453
                    L6: CdJ-CdN3d-CdHH_452
                L5: CdJ-HN3d_470
                    L6: CdJ-HN3d-O2s_469
                    L6: CdJ-HN3d-H_507
                    L6: CdJ-HN3d-N3s_566
                    L6: CdJ-HN3d-CO_570
                    L6: CdJ-HN3d-Ct_617
                    L6: CdJ-HN3d-N3d_624
                    L6: CdJ-HN3d-Cd_642
                    L6: CdJ-HN3d-Cs_700
                L5: CdJ-N3dN3s_473
                    L6: CdJ-N3dN3s-HHO2s_472
                    L6: CdJ-N3dN3s-CsHH_562
                    L6: CdJ-N3dN3s-HHN3s_586
                    L6: CdJ-N3dN3s-HHO2s_640
                    L6: CdJ-N3dN3s-HHH_665
                    L6: CdJ-N3dN3s-HHN3s_696
                    L6: CdJ-N3dN3s-CsHH_706
                L5: CdJ-CsN3d_480
                    L6: CdJ-CsN3d-HHHN3s_479
                    L6: CdJ-CsN3d-HHHO2s_504
                    L6: CdJ-CsN3d-CsHHH_670
                    L6: CdJ-CsN3d-CsHHH_677
                    L6: CdJ-CsN3d-HHHN3s_682
                    L6: CdJ-CsN3d-HHHH_709
                L5: CdJ-N3dO2s_491
                    L6: CdJ-N3dO2s-HO2s_490
                    L6: CdJ-N3dO2s-HN3s_572
                    L6: CdJ-N3dO2s-HO2s_639
                    L6: CdJ-N3dO2s-HN3s_694
                    L6: CdJ-N3dO2s-CsH_707
                L5: CdJ-CdN3s_506
                    L6: CdJ-CdN3s-HHHO2s_505
                    L6: CdJ-CdN3s-CsHHH_523
                    L6: CdJ-CdN3s-HHHN3s_532
                    L6: CdJ-CdN3s-CsHHH_539
                    L6: CdJ-CdN3s-HHHN3s_544
                    L6: CdJ-CdN3s-HHHH_591
                    L6: CdJ-CdN3s-HHHO2s_618
                L5: CdJ-CddN3s_512
                    L6: CdJ-CddN3s-HHN5dc_511
                    L6: CdJ-CddN3s-CdHH_603
                    L6: CdJ-CddN3s-HHN3d_657
                    L6: CdJ-CddN3s-HHO2d_661
                L5: CdJ-CsN5dc_531
                    L6: CdJ-CsN5dc-HHHHO0sc_530
                    L6: CdJ-CsN5dc-HHHN3sO0sc_596
                    L6: CdJ-CsN5dc-HHHO0scO2s_602
                    L6: CdJ-CsN5dc-CsHHHO0sc_660
                L5: CdJ-N3sN5dc_552
                    L6: CdJ-N3sN5dc-HHO0scO2s_551
                    L6: CdJ-N3sN5dc-HHN3sO0sc_554
                    L6: CdJ-N3sN5dc-CsHHO0sc_681
                    L6: CdJ-N3sN5dc-HHHO0sc_704
                L5: CdJ-HN5dc_577
                    L6: CdJ-HN5dc-HO0sc_576
                L5: CdJ-N1scN3d_580
                    L6: CdJ-N1scN3d-HN5dc_579
                L5: CdJ-CON3d_610
                    L6: CdJ-CON3d-HHO2d_609
                L5: CdJ-N5dcO2s_615
                    L6: CdJ-N5dcO2s-HN3sO0sc_614
                    L6: CdJ-N5dcO2s-CsHO0sc_643
                    L6: CdJ-N5dcO2s-HHO0sc_720
                L5: CdJ-N3dN5dc_628
                    L6: CdJ-N3dN5dc-HN3dO0sc_627
                L5: CdJ-CdN1sc_673
                    L6: CdJ-CdN1sc-HHN5dc_672
                L5: CdJ-CON5dc_713
                    L6: CdJ-CON5dc-HHO0scO2d_712
            L4: CtJ
                L5: Acetyl
                L5: CtJ-Ct-N3s_462
                L5: CtJ-Ct-N3d_561
                L5: CtJ-Ct-N1sc_711
            L4: CbJ
            L4: C=SJ
                L5: C=SJ-S2s
                L5: C=SJ-H
                L5: C=SJ-C
                    L6: C=SJ-Cd
                    L6: C=SJ-Cs
        L3: OJ
            L4: HOJ
            L4: COJ
                L5: CCOJ
                    L6: C=OCOJ
                        L7: C=CC(C)(C=O)OJ
                        L7: CC(C)(C=O)OJ
                        L7: C=OC=OOJ
                    L6: CC(C)OJ
                        L7: CC(C)2OJ
                            L8: C=CC(C)2OJ
                        L7: CC(C)(O)OJ
                            L8: C=CC(C)(O)OJ
                    L6: C=C(C)OJ
                L5: CdsOJ
                    L6: RC=COJ
                        L7: C=COJ
                    L6: OJC=O
                        L7: OC=OOJ
                L5: OCOJ
                L5: SCOJ
                L5: CsOJ
                    L6: H3COJ
                    L6: O2sJ-Cs-HHN3d_595
                    L6: O2sJ-Cs-HHN3s_674
                    L6: O2sJ-Cs-HHN1sc_708
                L5: CbOJ
            L4: OOJ
                L5: ROOJ
                    L6: C(=O)OOJ
                    L6: C3COOJ
                    L6: SOOJ
                L5: HOOJ
            L4: SOJ
                L5: O2sJ-S2s
                L5: O2sJ-S4d
                    L6: O2sJ-(S4d-OdO)
                    L6: O2sJ-(S4d-OdC)
                    L6: O2sJ-(S4d-OdH)
                    L6: O2sJ-(S4d-CdC)
                L5: O2sJ-S6d
            L4: O2sJ-N3s_459
                L5: O2sJ-N3s-HO2s_458
                L5: O2sJ-N3s-HN1sc_564
                L5: O2sJ-N3s-COH_590
                L5: O2sJ-N3s-CdH_653
            L4: O2sJ-N1sc_559
                L5: O2sJ-N1sc-N5dc_558
        L3: NJ
            L4: N3sJ
                L5: NH2J
                L5: NHJ_C
                    L6: N3sJ-CdH-HN3d_448
                    L6: N3sJ-COH-HO2d_487
                    L6: N3sJ-CsH-CdHH_526
                    L6: N3sJ-CsH-CtHH_548
                    L6: N3sJ-CsH-HHO2s_568
                    L6: N3sJ-CsH-HHN3d_616
                    L6: N3sJ-CsH-CsHH_631
                    L6: N3sJ-CsH-HHN3s_659
                    L6: N3sJ-CsH-HHH_710
                    L6: N3sJ-CsH-COHH_717
                    L6: N3sJ-CdH-HN5dc_727
                L5: NHJ_O
                    L6: N3sJ-HO2s-N3s_461
                    L6: N3sJ-HO2s-O2s_463
                    L6: N3sJ-HO2s-Cs_478
                    L6: N3sJ-HO2s-Cd_521
                    L6: N3sJ-HO2s-Ct_581
                    L6: N3sJ-HO2s-N3d_607
                    L6: N3sJ-HO2s-N1sc_650
                    L6: N3sJ-HO2s-H_686
                    L6: N3sJ-HO2s-CO_714
                L5: NHJ_N
                    L6: N3sJ-HN3s-HH_460
                    L6: N3sJ-HN3s-HO2s_475
                    L6: N3sJ-HN3s-CsH_481
                    L6: N3sJ-HN3s-HN3d_508
                    L6: N3sJ-HN3s-HN3s_520
                    L6: N3sJ-HN3d-N5dc_529
                    L6: N3sJ-HN3s-COH_546
                    L6: N3sJ-HN3s-CdH_567
                L5: NJ_CC
                    L6: N3sJ-CdCs-HHHHN3d_482
                    L6: N3sJ-COCs-HHHHO2d_503
                    L6: N3sJ-CsCt-HHHN3t_592
                    L6: N3sJ-CdCs-HHHHN5dc_647
                    L6: N3sJ-CsCs-HHHHHH_667
                    L6: N3sJ-CsCs-HHHHHO2s_724
                    L6: N3sJ-CsCs-HHHHHN3s_725
                L5: N3sJ-CdN3s_445
                    L6: N3sJ-CdN3s-HHHN3d_444
                    L6: N3sJ-CdN3s-HHHN5dc_611
                L5: N3sJ-CON3s_477
                    L6: N3sJ-CON3s-HHHO2d_476
                L5: N3sJ-N3dO2s_484
                    L6: N3sJ-N3dO2s-CdH_483
                L5: N3sJ-CsO2s_499
                    L6: N3sJ-CsO2s-HHHN3s_498
                    L6: N3sJ-CsO2s-HHHH_569
                    L6: N3sJ-CsO2s-CsHHH_600
                    L6: N3sJ-CsO2s-CsHHH_612
                    L6: N3sJ-CsO2s-HHHO2s_654
                    L6: N3sJ-CsO2s-HHHO2s_730
                    L6: N3sJ-CsO2s-HHHN3s_731
                L5: N3sJ-CsN3s_541
                    L6: N3sJ-CsN3s-CsHHHH_540
                    L6: N3sJ-CsN3s-HHHHH_587
                    L6: N3sJ-CsN3s-CsHHHH_599
                    L6: N3sJ-CsN3s-HHHHO2s_655
                    L6: N3sJ-CsN3s-HHHHN3s_662
                    L6: N3sJ-CsN3s-HHHHN3s_698
                    L6: N3sJ-CsN3s-HHHHO2s_699
                L5: N3sJ-CdO2s_550
                    L6: N3sJ-CdO2s-HHN3d_549
                    L6: N3sJ-CdO2s-HHN5dc_619
                L5: N3sJ-COO2s_557
                    L6: N3sJ-COO2s-HHO2d_556
                L5: N3sJ-CsN3d_575
                    L6: N3sJ-CsN3d-HHHN5dc_574
                L5: N3sJ-N3sN3s_633
                    L6: N3sJ-N3sN3s-HHHH_632
                    L6: N3sJ-N3sN3s-HHHO2s_689
                L5: N3sJ-N3sO2s_635
                    L6: N3sJ-N3sO2s-HHO2s_634
                    L6: N3sJ-N3sO2s-CsHH_648
                    L6: N3sJ-N3sO2s-HHH_651
                    L6: N3sJ-N3sO2s-CsHH_683
                    L6: N3sJ-N3sO2s-HHO2s_690
                    L6: N3sJ-N3sO2s-HHN3s_697
                    L6: N3sJ-N3sO2s-HHN3s_733
                L5: N3sJ-O2sO2s_638
                    L6: N3sJ-O2sO2s-CsH_637
                    L6: N3sJ-O2sO2s-HH_692
                L5: N3sJ-N3dN3s_676
                    L6: N3sJ-N3dN3s-HHN5dc_675
                L5: N3sJ-N1scO2s_688
                    L6: N3sJ-N1scO2s-HN5dc_687
                L5: N3sJ-CtO2s_702
                    L6: N3sJ-CtO2s-CtH_701
            L4: N3dJ
                L5: N3dJ_C
                    L6: N3dJ-Cdd-Cdd_446
                    L6: N3dJ-Cd-HH_492
                    L6: N3dJ-Cd-CsH_510
                    L6: N3dJ-Cd-HO2s_516
                    L6: N3dJ-Cd-HN3s_517
                    L6: N3dJ-Cdd-N5dc_533
                    L6: N3dJ-Cd-CtH_534
                    L6: N3dJ-Cdd-N3d_605
                    L6: N3dJ-Cdd-Cd_621
                    L6: N3dJ-Cd-HN3d_641
                    L6: N3dJ-Cd-HN1sc_666
                    L6: N3dJ-Cd-COH_679
                    L6: N3dJ-Cdd-O2d_719
                    L6: N3dJ-Cd-CdH_723
                L5: N3dJ_O
                L5: N3dJ_N
                    L6: N3dJ-N3d-Cd_509
                    L6: N3dJ-N3d-CO_528
                    L6: N3dJ-N3d-Ct_584
                    L6: N3dJ-N3d-N3s_644
                    L6: N3dJ-N3d-Cs_652
                    L6: N3dJ-N5dc-HO0sc_658
            L4: N5dcJ-CdO0sc_451
                L5: N5dcJ-CdO0sc-CsH_450
                L5: N5dcJ-CdO0sc-HN3d_494
                L5: N5dcJ-CdO0sc-HN3s_497
                L5: N5dcJ-CdO0sc-CdH_565
                L5: N5dcJ-CdO0sc-HH_669
                L5: N5dcJ-CdO0sc-COH_691
                L5: N5dcJ-CdO0sc-HO2s_729
            L4: N5dcJ-N1scO2d_496
                L5: N5dcJ-N1scO2d-O2s_495
                L5: N5dcJ-N1scO2d-Cs_685
            L4: N5dcJ-CddO0sc_515
                L5: N5dcJ-CddO0sc-Cdd_514
                L5: N5dcJ-CddO0sc-O2d_593
                L5: N5dcJ-CddO0sc-N3d_604
                L5: N5dcJ-CddO0sc-Cd_656
            L4: N5dcJ-N3dO0sc_525
                L5: N5dcJ-N3dO0sc-Cs_524
                L5: N5dcJ-N3dO0sc-N3s_555
                L5: N5dcJ-N3dO0sc-H_583
            L4: N5dcJ-O0scO2d_574
        L3: SiJ
        L3: SJ
            L4: S2J
                L5: S2J-H
                L5: S2J-C
                    L6: S2J-Cs
                        L7: S2sJ-(CsHHH)
                        L7: S2J-(Cs-Cb)
                    L6: S2J-Ct
                    L6: S2J-Cb
                    L6: S2J-Cd
                    L6: S2J-C=S
                    L6: S2J-CO
                L5: S2J-S2s
                    L6: S2J-S2s-H
                    L6: S2J-S2s-Cs
                    L6: S2J-S2s-S2s
                L5: S2sJ-O
            L4: S4sJ
                L5: S4sJ-CCC
                L5: S4sJ-OCC
            L4: S4dJ
                L5: S4dJ-OdH
                L5: S4dJ-OdO
            L4: S6sJ
                L5: S6sJ-CCCCC
            L4: S6dJ
                L5: S6dJ-OdOCC
            L4: S6ddJ
                L5: S6ddJ-OdOdH
                L5: S6ddJ-OdOdO
    L2: RJ2_triplet
        L3: CJ2_triplet
            L4: OsCsJ2H_triplet
            L4: CsJ2_triplet
                L5: CH2_triplet
                L5: CsJ2_P_triplet
                    L6: CsCsJ2_triplet
                        L7: CCJ2_triplet
                    L6: PhCH_triplet
                    L6: AllylJ2_triplet
                L5: CsJ2_S_triplet
            L4: CdJ2_triplet
                L5: CCdJ2_triplet
                    L6: CdCdJ2_triplet
                    L6: (CO)CdJ2_triplet
            L4: CdJ2-Sd_triplet
        L3: NJ2_triplet
            L4: N3sJ2
                L5: NHJ2
                L5: NJ2_C
                L5: NJ2_O
        L3: Oa_triplet
        L3: SiJ2_triplet
        L3: SJ2_triplet
    L2: RJ3
        L3: CJ3
        L3: SiJ3
"""
)

