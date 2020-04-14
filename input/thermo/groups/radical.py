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
    label = "CsJ-HNN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   N  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.8532,11.0458,6.19232,1.63176,-4.64424,-8.53536,-15.9829],'J/(mol*K)'),
        H298 = (438.663,'kJ/mol'),
        S298 = (7.12357,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 5,
    label = "CsJ-HNN3ds",
    group = 
"""
1 * Cs        u1 {2,S} {3,S} {4,S}
2   N         u0 {1,S}
3   [N3d,N3s] u0 {1,S}
4   H         u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.58597,-5.80395,-8.7662,-11.0768,-14.324,-16.3676,-18.708],'J/(mol*K)'),
        H298 = (393.258,'kJ/mol'),
        S298 = (0.575878,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 6,
    label = "CsJ-HN(N3dCd)",
    group = 
"""
1 * Cs       u1 {2,S} {3,S} {4,S}
2   N3d      u0 {1,S} {5,D}
3   N        u0 {1,S}
4   H        u0 {1,S}
5   [Cd,Cdd] u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.17364,0.526339,-1.56312,-4.04119,-8.28715,-11.0029,-15.4736],'J/(mol*K)'),
        H298 = (342.422,'kJ/mol'),
        S298 = (-4.66094,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 7,
    label = "CsJ-HN(N3dOd)",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   N3d u0 {1,S} {5,D}
3   N   u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.31137,-4.08151,-5.05929,-6.59864,-9.61356,-12.7552,-18.2312],'J/(mol*K)'),
        H298 = (303.519,'kJ/mol'),
        S298 = (-8.01983,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 8,
    label = "CsJ-HN(N3dN5dc)",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   N3d  u0 {1,S} {5,D}
3   N    u0 {1,S}
4   H    u0 {1,S}
5   N5dc u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.95318,3.13485,0.33421,-2.701,-7.67123,-10.5415,-15.8149],'J/(mol*K)'),
        H298 = (275.434,'kJ/mol'),
        S298 = (4.69758,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 9,
    label = "CsJ-HN5scN5sc",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   N5sc u0 {1,S}
3   N5sc u0 {1,S}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0538838,-1.876,-4.04855,-6.08546,-9.70524,-12.7382,-17.9892],'J/(mol*K)'),
        H298 = (436.377,'kJ/mol'),
        S298 = (7.19164,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 10,
    label = "CsJ-NNN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   N  u0 {1,S}
4   N  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.26669,-1.87614,-5.88538,-8.95583,-13.0988,-15.6997,-18.3991],'J/(mol*K)'),
        H298 = (388.334,'kJ/mol'),
        S298 = (-4.02418,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 11,
    label = "CsJ-HNO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O  u0 {1,S}
3   N  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.29692,-8.29409,-11.2699,-13.4031,-16.5816,-18.4631,-19.9014],'J/(mol*K)'),
        H298 = (371.563,'kJ/mol'),
        S298 = (2.01997,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 12,
    label = "CsJ-HON1sc",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   O    u0 {1,S}
3   N1sc u0 {1,S}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80826,-12.344,-15.0884,-16.9587,-18.722,-18.5848,-14.5979],'J/(mol*K)'),
        H298 = (273.333,'kJ/mol'),
        S298 = (-3.14275,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 13,
    label = "CsJ-NNO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O  u0 {1,S}
3   N  u0 {1,S}
4   N  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.60436,-6.81991,-9.0924,-11.5084,-13.7941,-14.5737,-13.827],'J/(mol*K)'),
        H298 = (311.145,'kJ/mol'),
        S298 = (4.53151,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 14,
    label = "CsJ-NOO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O  u0 {1,S}
3   O  u0 {1,S}
4   N  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.42994,-4.90751,-5.57809,-6.41818,-8.08512,-9.63419,-13.0091],'J/(mol*K)'),
        H298 = (324.92,'kJ/mol'),
        S298 = (-3.22872,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 15,
    label = "CsJ-CNN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   N  u0 {1,S}
4   N  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.80085,-5.80744,-7.57663,-9.14825,-11.7549,-13.7367,-16.6315],'J/(mol*K)'),
        H298 = (383.839,'kJ/mol'),
        S298 = (-5.21955,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 16,
    label = "CsJ-CNO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   O  u0 {1,S}
4   N  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.889156,-3.17426,-6.57797,-9.40356,-13.6201,-16.3703,-19.6483],'J/(mol*K)'),
        H298 = (390.332,'kJ/mol'),
        S298 = (4.50509,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 17,
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
    index = 18,
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
    index = 19,
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
    index = 20,
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
    index = 21,
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
    index = 22,
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
    index = 23,
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
    index = 24,
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
    index = 25,
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
    index = 26,
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
    index = 27,
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
    index = 28,
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
    index = 29,
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
    index = 30,
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
    index = 31,
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
    index = 32,
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
    index = 33,
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
    index = 34,
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
    index = 35,
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
    index = 36,
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
    index = 37,
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
    index = 38,
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
    index = 39,
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
    index = 40,
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
    index = 41,
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
    index = 42,
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
    index = 43,
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
    index = 44,
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
    index = 45,
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
    index = 46,
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
    index = 47,
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
    index = 48,
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
    index = 49,
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
    index = 50,
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
    index = 51,
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
    index = 52,
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
    index = 53,
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
    index = 54,
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
    index = 55,
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
    index = 56,
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
    index = 57,
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
    index = 58,
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
    index = 59,
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
    index = 60,
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
    index = 61,
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
    index = 62,
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
    index = 63,
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
    index = 64,
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
    index = 65,
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
    index = 66,
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
    index = 67,
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
    index = 68,
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
    index = 69,
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
    index = 70,
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
    index = 71,
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
    index = 72,
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
    index = 73,
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
    index = 74,
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
    index = 76,
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
    index = 76,
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
    index = 77,
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
    index = 78,
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
    index = 87,
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
    index = 88,
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
    index = 82,
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
    index = 83,
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
    index = 84,
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
    index = 85,
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
    index = 86,
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
    index = 87,
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
    index = 88,
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
    index = 89,
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
    index = 90,
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
    index = 91,
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
    index = 92,
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
    index = 93,
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
    index = 94,
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
    index = 95,
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
    index = 102,
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
    index = 98,
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
    index = 98,
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
    index = 99,
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
    index = 100,
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
    index = 101,
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
    index = 102,
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
    index = 103,
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
    index = 104,
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
    index = 105,
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
    index = 106,
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
    index = 107,
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
    index = 108,
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
    index = 109,
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
    index = 110,
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
    index = 111,
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
    index = 112,
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
    index = 113,
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
    index = 114,
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
    index = 115,
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
    index = 116,
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
    index = 117,
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
    index = 118,
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
    index = 119,
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
    index = 120,
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
    index = 121,
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
    index = 122,
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
    index = 123,
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
    index = 124,
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
    index = 125,
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
    index = 126,
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
    index = 127,
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
    index = 128,
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
    index = 129,
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
    index = 130,
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
    index = 131,
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
    index = 132,
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
    index = 133,
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
    index = 134,
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
    index = 135,
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
    index = 136,
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
    index = 137,
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
    index = 138,
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
    index = 139,
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
    index = 140,
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
    index = 141,
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
    index = 142,
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
    index = 143,
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
    index = 144,
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
    index = 145,
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
    index = 146,
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
    index = 147,
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
    index = 148,
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
    index = 149,
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
    index = 150,
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
    index = 151,
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
    index = 152,
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
    index = 153,
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
    index = 154,
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
    index = 155,
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
    index = 156,
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
    index = 157,
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
    index = 158,
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
    index = 159,
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
    index = 160,
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
    index = 161,
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
    index = 162,
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
    index = 163,
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
    index = 164,
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
    index = 165,
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
    index = 166,
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
    index = 167,
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
    index = 168,
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
    index = 169,
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
    index = 170,
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
    index = 171,
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
    index = 172,
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
    index = 173,
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
    index = 174,
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
    index = 175,
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
    index = 176,
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
    index = 177,
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
    index = 178,
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
    index = 179,
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
    index = 180,
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
    index = 181,
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
    index = 182,
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
    index = 183,
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
    index = 184,
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
    index = 185,
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
    index = 186,
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
    index = 187,
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
    index = 188,
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
    index = 189,
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
    index = 190,
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
    index = 191,
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
    index = 192,
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
    index = 193,
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
    index = 194,
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
    index = 195,
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
    index = 196,
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
    index = 197,
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
    index = 198,
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
    index = 199,
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
    index = 200,
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
    index = 201,
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
    index = 202,
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
    index = 203,
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
    index = 204,
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
    index = 205,
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
    index = 206,
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
    index = 207,
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
    index = 208,
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
    index = 209,
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
    index = 210,
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
    index = 211,
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
    index = 212,
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
    index = 213,
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
    index = 214,
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
    index = 215,
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
    index = 216,
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
    index = 217,
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
    index = 218,
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
    index = 219,
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
    index = 220,
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
    index = 221,
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
    index = 222,
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
    index = 223,
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
    index = 224,
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
    index = 225,
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
    index = 226,
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
    index = 227,
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
    index = 228,
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
    index = 229,
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
    index = 230,
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
    index = 231,
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
    index = 232,
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
    index = 233,
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
    index = 234,
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
    index = 235,
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
    index = 236,
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
    index = 237,
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
    index = 238,
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
    index = 239,
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
    index = 240,
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
    index = 241,
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
    index = 242,
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
    index = 243,
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
    index = 244,
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
    index = 245,
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
    index = 246,
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
    index = 247,
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
    index = 248,
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
    index = 249,
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
    index = 250,
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
    index = 251,
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
    index = 252,
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
    index = 257,
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
    index = 258,
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
    index = 259,
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
    index = 260,
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
    index = 261,
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
    index = 262,
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
    index = 263,
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
    index = 264,
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
    index = 265,
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
    index = 266,
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
    index = 267,
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
    index = 268,
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
    index = 269,
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
    index = 270,
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
    index = 271,
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
    index = 272,
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
    index = 273,
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
    index = 274,
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
    index = 275,
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
    index = 276,
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
    index = 277,
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
    index = 278,
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
    index = 279,
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
    index = 280,
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
    index = 281,
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
    index = 282,
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
    index = 283,
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
    index = 284,
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
    index = 285,
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
    index = 286,
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
    index = 287,
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
    index = 288,
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
    index = 289,
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
    index = 290,
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
    index = 291,
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
    index = 292,
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
    index = 293,
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
    index = 294,
    label = "CsJN3s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   N3s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.34639,0.0642418,-2.22164,-4.63062,-8.66372,-11.6685,-16.1145],'J/(mol*K)'),
        H298 = (388.92,'kJ/mol'),
        S298 = (-10.2036,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 295,
    label = "CsJN5sdtc",
    group = 
"""
1 * Cs                     u1 {2,S} {3,S} {4,S}
2   [N5sc,N5dc,N5ddc,N5tc] u0 {1,S}
3   H                      u0 {1,S}
4   H                      u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.81722,3.24544,2.72474,1.22104,-2.23308,-5.66919,-12.8356],'J/(mol*K)'),
        H298 = (404.243,'kJ/mol'),
        S298 = (-14.4918,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 296,
    label = "CsJN5sc",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   N5sc u0 {1,S}
3   H    u0 {1,S}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.491933,-0.720255,-2.86803,-5.09749,-8.94641,-12.0652,-17.2889],'J/(mol*K)'),
        H298 = (432.825,'kJ/mol'),
        S298 = (-2.63962,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 297,
    label = "CsJN5dcOdO0sc",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   N5dc u0 {1,S} {5,D} {6,S}
3   H    u0 {1,S}
4   H    u0 {1,S}
5   O2d  u0 {2,D}
6   O0sc u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.05016,0.29288,-2.17568,-4.97896,-10.1671,-14.393,-21.2966],'J/(mol*K)'),
        H298 = (424.73,'kJ/mol'),
        S298 = (-14.8665,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 298,
    label = "CsJN5dcN3dO0sc",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   N5dc u0 {1,S} {5,D} {6,S}
3   H    u0 {1,S}
4   H    u0 {1,S}
5   N3d  u0 {2,D}
6   O0sc u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.27482,3.34223,2.42357,0.716726,-3.09483,-6.83265,-14.3794],'J/(mol*K)'),
        H298 = (421.503,'kJ/mol'),
        S298 = (-9.69349,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 299,
    label = "CsJN3dCd",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   N3d u0 {1,S} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   Cd  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.334539,-0.181647,-0.845982,-1.98298,-4.81941,-7.87964,-14.2395],'J/(mol*K)'),
        H298 = (374.018,'kJ/mol'),
        S298 = (-11.1917,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 300,
    label = "CsJN3dCdd",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   N3d u0 {1,S} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.55707,4.38485,1.99807,-0.696803,-5.27072,-8.57746,-14.1022],'J/(mol*K)'),
        H298 = (389.255,'kJ/mol'),
        S298 = (-9.12797,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 301,
    label = "CsJN3dN5dc",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   N3d  u0 {1,S} {5,D}
3   H    u0 {1,S}
4   H    u0 {1,S}
5   N5dc u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.315332,0.568578,-0.652395,-2.70945,-6.57117,-9.32981,-14.8325],'J/(mol*K)'),
        H298 = (331.765,'kJ/mol'),
        S298 = (-9.5881,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 302,
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
    index = 303,
    label = "CdCsJN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   Cd u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.49236,-8.5813,-8.63032,-9.10002,-10.0385,-11.4238,-14.1214],'J/(mol*K)'),
        H298 = (329.078,'kJ/mol'),
        S298 = (-10.2951,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 304,
    label = "C2CsJN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.4665,-7.70578,-11.17,-13.75,-16.6445,-18.2536,-20.0442],'J/(mol*K)'),
        H298 = (392.461,'kJ/mol'),
        S298 = (-9.03706,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 305,
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
    index = 306,
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
    index = 307,
    label = "CdJ-NN",
    group = 
"""
1 * Cd u1 {2,S} {3,D}
2   N  u0 {1,S}
3   N  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.97657,-2.2041,-5.32888,-7.99133,-12.3333,-15.391,-19.6103],'J/(mol*K)'),
        H298 = (404.968,'kJ/mol'),
        S298 = (8.19458,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 308,
    label = "COJ-NOd",
    group = 
"""
1 * CO u1 {2,S} {3,D}
2   N  u0 {1,S}
3   O  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.499049,-2.566,-5.4926,-8.03919,-12.3239,-15.6108,-20.2366],'J/(mol*K)'),
        H298 = (352.267,'kJ/mol'),
        S298 = (5.58481,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 309,
    label = "CdJ-CdN",
    group = 
"""
1 * Cd u1 {2,S} {3,D}
2   N  u0 {1,S}
3   C  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.18369,-4.23173,-7.03311,-9.35183,-12.8111,-15.2187,-18.7271],'J/(mol*K)'),
        H298 = (445.085,'kJ/mol'),
        S298 = (5.80115,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 310,
    label = "CdJ-CddN",
    group = 
"""
1 * Cd  u1 {2,S} {3,D}
2   N   u0 {1,S}
3   Cdd u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.3921,-2.08105,-5.04651,-7.48487,-11.2668,-13.9403,-17.7653],'J/(mol*K)'),
        H298 = (371.87,'kJ/mol'),
        S298 = (2.60652,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 311,
    label = "CdJ-NdO",
    group = 
"""
1 * Cd u1 {2,S} {3,D}
2   O  u0 {1,S}
3   N  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.33945,-1.92324,-6.02047,-9.57875,-15.2601,-19.0789,-23.7518],'J/(mol*K)'),
        H298 = (437.007,'kJ/mol'),
        S298 = (7.57533,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 312,
    label = "CdJ-NdC",
    group = 
"""
1 * Cd u1 {2,S} {3,D}
2   C  u0 {1,S}
3   N  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.00763889,-2.36896,-5.21801,-7.8464,-11.991,-15.0452,-19.5882],'J/(mol*K)'),
        H298 = (431.362,'kJ/mol'),
        S298 = (4.60475,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 313,
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
    index = 314,
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
    index = 315,
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
    index = 316,
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
    index = 317,
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
    index = 318,
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
    index = 319,
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
    index = 320,
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
    index = 321,
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
    index = 322,
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
    index = 323,
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
    index = 324,
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
    index = 325,
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
    index = 326,
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
    index = 327,
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
    index = 328,
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
    index = 329,
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
    index = 330,
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
    index = 331,
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
    index = 332,
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
    index = 333,
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
    index = 334,
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
    index = 335,
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
    index = 336,
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
    index = 337,
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
    index = 338,
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
    index = 339,
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
    index = 340,
    label = "N=C=CJ",
    group = 
"""
1 * Cd  u1 {2,D} {3,S}
2   Cdd u0 {1,D} {4,D}
3   H   u0 {1,S}
4   N   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.92302,-3.87776,-5.86459,-7.91273,-11.031,-13.2669,-16.8954],'J/(mol*K)'),
        H298 = (369.234,'kJ/mol'),
        S298 = (-5.93117,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 341,
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
    index = 342,
    label = "N=C=CJC",
    group = 
"""
1 * Cd u1 {2,D} {3,S}
2   C  u0 {1,D} {4,D}
3   C  u0 {1,S}
4   N  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.07662,-4.81991,-7.34354,-9.45507,-12.8991,-15.5773,-19.5204],'J/(mol*K)'),
        H298 = (345.84,'kJ/mol'),
        S298 = (0.774208,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 343,
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
    index = 344,
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
    index = 345,
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
    index = 346,
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
    index = 347,
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
    index = 348,
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
    index = 349,
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
    index = 350,
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
    index = 351,
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
    index = 352,
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
    index = 353,
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
    index = 354,
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
    index = 355,
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
    index = 356,
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
    index = 357,
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
    index = 358,
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
    index = 359,
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
    index = 360,
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
    index = 361,
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
    index = 362,
    label = "CdJ-HN3d",
    group = 
"""
1 * Cd  u1 {2,S} {3,D}
2   H   u0 {1,S}
3   N3d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.535181,-3.60589,-6.39413,-8.86095,-12.7727,-15.5717,-19.8329],'J/(mol*K)'),
        H298 = (415.298,'kJ/mol'),
        S298 = (5.57767,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 363,
    label = "CdJ-H(N3dOs)",
    group = 
"""
1 * Cd  u1 {2,D} {3,S}
2   N3d u0 {1,D} {4,S}
3   H   u0 {1,S}
4   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.72438,-0.600728,-4.42251,-7.70232,-13.0613,-16.7127,-21.0715],'J/(mol*K)'),
        H298 = (440.68,'kJ/mol'),
        S298 = (7.40719,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 364,
    label = "CdJ-H(N3dCO)",
    group = 
"""
1   N3d u0 {2,D} {3,S}
2 * Cd  u1 {1,D} {4,S}
3   CO  u0 {1,S} {5,D}
4   H   u0 {2,S}
5   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.19479,-3.60166,-4.82249,-6.06327,-8.74387,-11.0941,-15.1265],'J/(mol*K)'),
        H298 = (411.286,'kJ/mol'),
        S298 = (-2.27887,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 365,
    label = "CdJ-H(N3dN3d)",
    group = 
"""
1 * Cd  u1 {2,D} {3,S}
2   N3d u0 {1,D} {4,S}
3   H   u0 {1,S}
4   N3d u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.175838,-2.38908,-4.71217,-6.73125,-10.4295,-13.5563,-18.2391],'J/(mol*K)'),
        H298 = (426.882,'kJ/mol'),
        S298 = (5.53135,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 366,
    label = "CdJ-H(N3dCd)",
    group = 
"""
1 * Cd       u1 {2,D} {3,S}
2   N3d      u0 {1,D} {4,S}
3   H        u0 {1,S}
4   [Cd,Cdd] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.23929,-2.28161,-6.55411,-9.87574,-14.8878,-18.2186,-21.9295],'J/(mol*K)'),
        H298 = (422.544,'kJ/mol'),
        S298 = (13.1379,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 367,
    label = "CdJ-HN5dc",
    group = 
"""
1 * Cd   u1 {2,S} {3,D}
2   H    u0 {1,S}
3   N5dc u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.58018,-0.431227,-3.62097,-6.67779,-11.585,-15.0896,-19.8118],'J/(mol*K)'),
        H298 = (490.037,'kJ/mol'),
        S298 = (7.65582,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 368,
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
    index = 369,
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
    index = 370,
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
    index = 371,
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
    index = 372,
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
    index = 373,
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
    index = 374,
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
    index = 375,
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
    index = 376,
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
    index = 377,
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
    index = 378,
    label = "O2sJ-N",
    group = 
"""
1 * O2s u1 {2,S}
2   N   u0 {1,S}
""",
    thermo = 'O2sJ-N3s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 379,
    label = "O2sJ-N3s",
    group = 
"""
1 * O2s u1 {2,S}
2   N3s u0 {1,S}
""",
    thermo = 'O2sJ-N3sC',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 380,
    label = "O2sJ-N3sC",
    group = 
"""
1   N3s u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.95666,-8.30392,-10.4418,-11.9018,-14.2655,-16.1736,-18.5966],'J/(mol*K)'),
        H298 = (327.882,'kJ/mol'),
        S298 = (3.22862,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 381,
    label = "O2sJ-N3sCO",
    group = 
"""
1   N3s u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3 * O2s u1 {1,S}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.80695,-9.17585,-11.1673,-12.1719,-13.6433,-14.6347,-16.2533],'J/(mol*K)'),
        H298 = (317.059,'kJ/mol'),
        S298 = (3.29589,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 382,
    label = "O2sJ-N3sO2s",
    group = 
"""
1   N3s u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.49247,-14.5591,-18.7597,-21.1308,-24.037,-25.4752,-25.7812],'J/(mol*K)'),
        H298 = (337.881,'kJ/mol'),
        S298 = (3.72329,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 383,
    label = "O2sJ-N3s(N5sdcO0sc)",
    group = 
"""
1   N3s         u0 {2,S} {3,S}
2   [N5sc,N5dc] u0 {1,S} {4,S}
3 * O2s         u1 {1,S}
4   O0sc        u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.50052,-2.35159,-6.76321,-10.6251,-17.0766,-21.9786,-28.6277],'J/(mol*K)'),
        H298 = (340.144,'kJ/mol'),
        S298 = (17.5768,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 384,
    label = "O2sJ-N5sdtc",
    group = 
"""
1 * O2s                    u1 {2,S}
2   [N5sc,N5dc,N5ddc,N5tc] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-12.452,-13.7444,-13.9339,-14.0699,-14.6564,-15.3839,-17.2753],'J/(mol*K)'),
        H298 = (431.96,'kJ/mol'),
        S298 = (-8.08566,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 385,
    label = "O2sJ-N5dcOd",
    group = 
"""
1   [N5dc,N5ddc] u0 {2,S} {3,D}
2 * O2s          u1 {1,S}
3   O2d          u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.39039,-6.26822,-9.33998,-11.4358,-14.5602,-16.8834,-20.3064],'J/(mol*K)'),
        H298 = (400.951,'kJ/mol'),
        S298 = (16.5987,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 386,
    label = "O2sJ-N5dcOdO0sc",
    group = 
"""
1   N5dc u0 {2,S} {3,D} {4,S}
2 * O2s  u1 {1,S}
3   O2d  u0 {1,D}
4   O0sc u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.87864,-2.55224,-5.6484,-7.7404,-10.9202,-13.2633,-16.6105],'J/(mol*K)'),
        H298 = (431.801,'kJ/mol'),
        S298 = (-4.97896,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 387,
    label = "O2sJ-N1sc",
    group = 
"""
1 * O2s  u1 {2,S}
2   N1sc u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.37293,-7.06222,-9.51612,-11.2729,-13.4699,-14.9722,-17.077],'J/(mol*K)'),
        H298 = (347.821,'kJ/mol'),
        S298 = (2.24576,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 388,
    label = "O2sJ-N3dN3d",
    group = 
"""
1   N3d u0 {2,S} {3,D}
2 * O2s u1 {1,S}
3   N3d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.29692,-10.2926,-12.6566,-14.1838,-16.3385,-17.5728,-18.6188],'J/(mol*K)'),
        H298 = (664.976,'kJ/mol'),
        S298 = (5.17262,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 389,
    label = "O2sJ-N3dCd",
    group = 
"""
1   N3d      u0 {2,S} {3,D}
2 * O2s      u1 {1,S}
3   [Cd,Cdd] u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.28771,-10.3803,-11.9598,-13.1984,-15.0803,-16.3293,-16.2292],'J/(mol*K)'),
        H298 = (355.56,'kJ/mol'),
        S298 = (-8.0332,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 390,
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
    index = 391,
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
    index = 392,
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
    index = 393,
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
    index = 394,
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
    index = 395,
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
    index = 396,
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
    index = 397,
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
    index = 398,
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
    index = 399,
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
    index = 400,
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
    index = 401,
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
    index = 402,
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
    index = 403,
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
    index = 404,
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
    index = 405,
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
    index = 406,
    label = "N=COJ",
    group = 
"""
1   Cd  u0 {2,S} {3,D}
2 * O2s u1 {1,S}
3   N   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.58496,-8.79662,-8.0527,-8.55566,-10.0922,-11.8503,-16.2634],'J/(mol*K)'),
        H298 = (158.992,'kJ/mol'),
        S298 = (-7.51805,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 407,
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
    index = 408,
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
    index = 409,
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
    index = 410,
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
    index = 411,
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
    index = 412,
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
    index = 413,
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
    index = 414,
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
    index = 415,
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
    index = 416,
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
    index = 417,
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
    index = 418,
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
    index = 419,
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
    index = 420,
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
    index = 421,
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
    index = 422,
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
    index = 423,
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
    index = 424,
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
    index = 425,
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
    index = 426,
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
    index = 427,
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
    index = 428,
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
    index = 429,
    label = "N5scJ-HNO",
    group = 
"""
1 * N5sc u1 {2,S} {3,S} {4,S}
2   O    u0 {1,S}
3   N    u0 {1,S}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.23096,2.78632,-0.890733,-4.71711,-11.537,-16.9037,-24.8648],'J/(mol*K)'),
        H298 = (244.093,'kJ/mol'),
        S298 = (9.44819,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 430,
    label = "N5scJ-NNO",
    group = 
"""
1 * N5sc u1 {2,S} {3,S} {4,S}
2   O    u0 {1,S}
3   N    u0 {1,S}
4   N    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.26078,-4.51709,-6.33547,-8.68178,-12.6875,-15.8402,-20.7728],'J/(mol*K)'),
        H298 = (243.145,'kJ/mol'),
        S298 = (6.887,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 431,
    label = "N5scJ-HOO",
    group = 
"""
1 * N5sc u1 {2,S} {3,S} {4,S}
2   O    u0 {1,S}
3   O    u0 {1,S}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.33189,-3.30638,-6.33549,-9.29979,-13.9065,-17.5137,-22.8214],'J/(mol*K)'),
        H298 = (249.25,'kJ/mol'),
        S298 = (-4.29011,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 432,
    label = "N5scJ-NOO",
    group = 
"""
1 * N5sc u1 {2,S} {3,S} {4,S}
2   O    u0 {1,S}
3   O    u0 {1,S}
4   N    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.490477,-4.77156,-9.06461,-12.6536,-18.0458,-21.5371,-25.0925],'J/(mol*K)'),
        H298 = (268.345,'kJ/mol'),
        S298 = (16.9494,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 433,
    label = "N5scJ-CHO",
    group = 
"""
1 * N5sc u1 {2,S} {3,S} {4,S}
2   C    u0 {1,S}
3   O    u0 {1,S}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.68916,-0.596662,-3.96519,-7.11111,-12.1745,-15.8829,-21.1153],'J/(mol*K)'),
        H298 = (221.895,'kJ/mol'),
        S298 = (9.67402,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 434,
    label = "N5scJ-CNO",
    group = 
"""
1 * N5sc u1 {2,S} {3,S} {4,S}
2   C    u0 {1,S}
3   O    u0 {1,S}
4   N    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.18288,-10.1337,-12.6351,-14.4515,-17.1056,-18.8129,-21.0934],'J/(mol*K)'),
        H298 = (242.269,'kJ/mol'),
        S298 = (21.4951,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 435,
    label = "N5scJ-COO",
    group = 
"""
1 * N5sc u1 {2,S} {3,S} {4,S}
2   C    u0 {1,S}
3   O    u0 {1,S}
4   O    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5935,-4.28154,-7.14307,-9.65718,-13.7651,-16.838,-21.2973],'J/(mol*K)'),
        H298 = (252.716,'kJ/mol'),
        S298 = (2.97211,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 436,
    label = "N5scJ-CCO",
    group = 
"""
1 * N5sc u1 {2,S} {3,S} {4,S}
2   C    u0 {1,S}
3   C    u0 {1,S}
4   O    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.68915,-13.5775,-15.5782,-17.0545,-19.0312,-20.0961,-21.1052],'J/(mol*K)'),
        H298 = (231.664,'kJ/mol'),
        S298 = (-4.55651,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 437,
    label = "N5dcJ-NOd",
    group = 
"""
1 * N5dc u1 {2,S} {3,D}
2   N    u0 {1,S}
3   O    u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.39198,-3.81228,-7.35331,-10.7644,-15.958,-19.1788,-22.8709],'J/(mol*K)'),
        H298 = (334.654,'kJ/mol'),
        S298 = (10.2785,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 438,
    label = "N5dcJ-NdO",
    group = 
"""
1 * N5dc u1 {2,S} {3,D}
2   O    u0 {1,S}
3   N    u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.499652,-2.21608,-5.07031,-7.71348,-12.0168,-14.9458,-19.6336],'J/(mol*K)'),
        H298 = (330.642,'kJ/mol'),
        S298 = (6.64296,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 439,
    label = "N5dcJ-CdO",
    group = 
"""
1 * N5dc u1 {2,S} {3,D}
2   O    u0 {1,S}
3   C    u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.630065,-3.07143,-5.60254,-7.95144,-11.7011,-14.4828,-19.0124],'J/(mol*K)'),
        H298 = (292.28,'kJ/mol'),
        S298 = (1.06787,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 440,
    label = "N3sJ-NN",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   N   u0 {1,S}
3   N   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.34071,-5.69699,-7.91406,-9.88987,-12.9386,-14.9969,-17.7496],'J/(mol*K)'),
        H298 = (312.632,'kJ/mol'),
        S298 = (-0.792667,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 441,
    label = "N3sJ-NO",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   O   u0 {1,S}
3   N   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.34109,-6.50259,-10.1593,-12.9651,-16.8921,-19.2488,-21.4789],'J/(mol*K)'),
        H298 = (324.57,'kJ/mol'),
        S298 = (5.85483,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 442,
    label = "N3sJ-OO",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   O   u0 {1,S}
3   O   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.13984,-7.76932,-11.2129,-13.2285,-15.9222,-17.5188,-19.276],'J/(mol*K)'),
        H298 = (311.479,'kJ/mol'),
        S298 = (2.11221,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 443,
    label = "N3sJ-CN",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   C   u0 {1,S}
3   N   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.80393,-7.37641,-9.47396,-11.2655,-13.9993,-15.8916,-18.271],'J/(mol*K)'),
        H298 = (351.185,'kJ/mol'),
        S298 = (-2.7415,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 444,
    label = "N3sJ-CO",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   C   u0 {1,S}
3   O   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.19861,-11.8128,-13.9282,-15.0709,-16.1492,-16.3336,-16.3143],'J/(mol*K)'),
        H298 = (332.252,'kJ/mol'),
        S298 = (-0.98057,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 445,
    label = "N3sJ-CtO",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   Ct  u0 {1,S}
3   O   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-26.6987,-32.4179,-35.63,-37.6419,-41.0509,-44.038,-47.8704],'J/(mol*K)'),
        H298 = (301.079,'kJ/mol'),
        S298 = (-75.7278,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 446,
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
    index = 447,
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
    index = 448,
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
    index = 449,
    label = "NHJ_Cd",
    group = 
"""
1 * N3s      u1 p1 {2,S} {3,S}
2   [Cd,Cdd] u0 p0 {1,S}
3   H        u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.36968,-7.21186,-7.55213,-8.1556,-9.51515,-10.9959,-14.5568],'J/(mol*K)'),
        H298 = (353.261,'kJ/mol'),
        S298 = (-3.90709,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 450,
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
    index = 451,
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
    index = 452,
    label = "NHJ_N3d",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   N3d u0 {1,S}
3   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.70038,-4.63454,-6.10735,-7.60395,-10.2929,-12.3802,-15.6322],'J/(mol*K)'),
        H298 = (339.161,'kJ/mol'),
        S298 = (1.25886,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 453,
    label = "NHJ_N5dc",
    group = 
"""
1 * N3s  u1 p1 {2,S} {3,S}
2   N5dc u0 {1,S}
3   H    u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.78518,1.52507,-3.04956,-6.60718,-12.0808,-15.9009,-20.6874],'J/(mol*K)'),
        H298 = (434.288,'kJ/mol'),
        S298 = (2.72516,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 454,
    label = "NJ_CC",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   C   u0 p0 {1,S}
3   C   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.88844,-7.02096,-9.05679,-10.9554,-13.6124,-15.7099,-19.2836],'J/(mol*K)'),
        H298 = (389.974,'kJ/mol'),
        S298 = (-10.0809,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 455,
    label = "NJ_CCd",
    group = 
"""
1 * N3s      u1 p1 {2,S} {3,S}
2   C        u0 p0 {1,S}
3   [Cd,Cdd] u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.94584,-1.87787,-2.86025,-4.58312,-8.42517,-11.1267,-15.6176],'J/(mol*K)'),
        H298 = (350.499,'kJ/mol'),
        S298 = (-11.7385,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 456,
    label = "NJ_CCO",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   CO  u0 p0 {1,S} {4,D}
3   C   u0 p0 {1,S}
4   O2d u0 p2 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.961761,-0.807363,-3.28705,-5.60897,-9.76264,-13.2901,-19.6482],'J/(mol*K)'),
        H298 = (450.927,'kJ/mol'),
        S298 = (3.87449,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 457,
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
    index = 458,
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
    index = 459,
    label = "N3dJ_Cdd",
    group = 
"""
1 * N3d u1 p1 {2,D}
2   Cdd u0 p0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.67103,-7.14899,-8.76464,-10.2906,-12.8917,-14.9076,-18.0576],'J/(mol*K)'),
        H298 = (257.412,'kJ/mol'),
        S298 = (-1.20388,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 460,
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
    index = 461,
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
    index = 462,
    label = "N3dJ_N5dc",
    group = 
"""
1 * N3d  u1 p1 {2,D}
2   N5dc u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0356123,-2.98703,-5.6088,-7.86526,-11.8936,-15.0898,-19.6396],'J/(mol*K)'),
        H298 = (413.171,'kJ/mol'),
        S298 = (2.89249,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 463,
    label = "N3dJ_N3d",
    group = 
"""
1 * N3d u1 p1 {2,D}
2   N3d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.05081,-2.13979,-6.00346,-9.14917,-13.5357,-16.2931,-19.6448],'J/(mol*K)'),
        H298 = (306.397,'kJ/mol'),
        S298 = (18.8295,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 464,
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
    index = 465,
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
    index = 466,
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
    index = 467,
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
    index = 468,
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
    index = 469,
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
    index = 470,
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
    index = 471,
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
    index = 472,
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
    index = 473,
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
    index = 474,
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
    index = 475,
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
    index = 476,
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
    index = 477,
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
    index = 478,
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
    index = 479,
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
    index = 480,
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
    index = 481,
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
    index = 482,
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
    index = 483,
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
    index = 484,
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
    index = 485,
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
    index = 486,
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
    index = 487,
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
    index = 488,
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
    index = 489,
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
    index = 490,
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
    index = 491,
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
    index = 492,
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
    index = 493,
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
    index = 494,
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
    index = 495,
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
    index = 496,
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
    index = 497,
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
    index = 498,
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
    index = 499,
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
    index = 500,
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
    index = 501,
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
    index = 502,
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
    index = 503,
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
    index = 504,
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
    index = 505,
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
    index = 506,
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
    index = 507,
    label = "NCdJ2_triplet",
    group = 
"""
1 * Cd  u2 {2,D}
2   N3d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.67688,-8.56951,-13.0936,-17.1322,-23.6155,-28.3134,-35.4124],'J/(mol*K)'),
        H298 = (587.145,'kJ/mol'),
        S298 = (22.0742,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 508,
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
    index = 509,
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
    index = 510,
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
    index = 511,
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
    index = 512,
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
    index = 513,
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
    index = 514,
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
    index = 515,
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
    index = 516,
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
    index = 517,
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
    index = 518,
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
    index = 519,
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
    index = 520,
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
    index = 521,
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
    index = 522,
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
                L5: CsJ-HNN
                    L6: CsJ-HNN3ds
                        L7: CsJ-HN(N3dCd)
                        L7: CsJ-HN(N3dOd)
                        L7: CsJ-HN(N3dN5dc)
                    L6: CsJ-HN5scN5sc
                L5: CsJ-NNN
                L5: CsJ-HNO
                    L6: CsJ-HON1sc
                L5: CsJ-NNO
                L5: CsJ-NOO
                L5: CsJ-CNN
                L5: CsJ-CNO
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
                    L6: Benzyl_P
                    L6: Allyl_P
                        L7: C=CC=CCJ
                        L7: CTCC=CCJ
                        L7: CJC=C=O
                    L6: Propargyl
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
                    L6: CCsJOO
                        L7: CCsJOOH
                        L7: CCsJOOC
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
                    L6: CsJN3s
                    L6: CsJN5sdtc
                        L7: CsJN5sc
                        L7: CsJN5dcOdO0sc
                        L7: CsJN5dcN3dO0sc
                    L6: CsJN3dCd
                    L6: CsJN3dCdd
                    L6: CsJN3dN5dc
                L5: CCsJN
                    L6: CdCsJN
                L5: C2CsJN
                L5: OCJO
            L4: CdsJ
                L5: CdJ-NN
                L5: COJ-NOd
                L5: CdJ-CdN
                    L6: CdJ-CddN
                L5: CdJ-NdO
                L5: CdJ-NdC
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
                        L7: C=CCJ=O
                        L7: OC=OCJ=O
                    L6: (O)CJO
                        L7: (O)CJOH
                        L7: (O)CJOC
                            L8: (O)CJOCH3
                            L8: (O)CJOCC
                            L8: (O)CJOCC2
                            L8: (O)CJOCC3
                    L6: SCJ=O
                L5: Cds_P
                    L6: C=C=CJ
                    L6: N=C=CJ
                L5: Cds_S
                    L6: N=C=CJC
                    L6: C=CJC=O
                    L6: C=CJC=C
                        L7: cyclobutadiene-C1
                            L8: bicyclo[2.2.0]hexa-1(4),2,5-triene-C2
                        L7: 1,3-cyclopentadiene-vinyl-2
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
                L5: S2s-CJ=C
                L5: C=CJO
                L5: CdJ-HN3d
                    L6: CdJ-H(N3dOs)
                    L6: CdJ-H(N3dCO)
                    L6: CdJ-H(N3dN3d)
                    L6: CdJ-H(N3dCd)
                L5: CdJ-HN5dc
            L4: CtJ
                L5: Acetyl
            L4: CbJ
            L4: C=SJ
                L5: C=SJ-S2s
                L5: C=SJ-H
                L5: C=SJ-C
                    L6: C=SJ-Cd
                    L6: C=SJ-Cs
        L3: OJ
            L4: O2sJ-N
                L5: O2sJ-N3s
                    L6: O2sJ-N3sC
                        L7: O2sJ-N3sCO
                    L6: O2sJ-N3sO2s
                    L6: O2sJ-N3s(N5sdcO0sc)
                L5: O2sJ-N5sdtc
                    L6: O2sJ-N5dcOd
                        L7: O2sJ-N5dcOdO0sc
                L5: O2sJ-N1sc
                L5: O2sJ-N3dN3d
                L5: O2sJ-N3dCd
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
                        L7: N=COJ
                    L6: OJC=O
                        L7: OC=OOJ
                L5: OCOJ
                L5: SCOJ
                L5: CsOJ
                    L6: H3COJ
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
        L3: NJ
            L4: N5scJ-HNO
            L4: N5scJ-NNO
            L4: N5scJ-HOO
            L4: N5scJ-NOO
            L4: N5scJ-CHO
            L4: N5scJ-CNO
            L4: N5scJ-COO
            L4: N5scJ-CCO
            L4: N5dcJ-NOd
            L4: N5dcJ-NdO
            L4: N5dcJ-CdO
            L4: N3sJ-NN
            L4: N3sJ-NO
            L4: N3sJ-OO
            L4: N3sJ-CN
            L4: N3sJ-CO
                L5: N3sJ-CtO
            L4: N3sJ
                L5: NH2J
                L5: NHJ_C
                    L6: NHJ_Cd
                L5: NHJ_O
                L5: NHJ_N
                    L6: NHJ_N3d
                    L6: NHJ_N5dc
                L5: NJ_CC
                    L6: NJ_CCd
                    L6: NJ_CCO
            L4: N3dJ
                L5: N3dJ_C
                    L6: N3dJ_Cdd
                L5: N3dJ_O
                L5: N3dJ_N
                    L6: N3dJ_N5dc
                    L6: N3dJ_N3d
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
                L5: NCdJ2_triplet
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

