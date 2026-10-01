#!/usr/bin/env python
# encoding: utf-8

name = "P_0"
shortDesc = ""
longDesc = """
ARC v1.1.0
Levels of theory used:
Conformer optimization:       wb97xd/def2svp, software: gaussian
Composite method: cbs-qb3, software: gaussian (using a fine grid)
Frequencies:      b3lyp/cbsb7, software: gaussian
Rotor scans:      b3lyp/cbsb7, software: gaussian
Using p-type bond additivity corrections for thermo
Using the following ESS settings: {'gaussian': ['local']}
"""

entry(
    index = 0,
    label = "S0",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 C u0 p0 c0 {3,S} {4,D} {6,S}
3 C u0 p0 c0 {2,S} {5,T}
4 C u0 p0 c0 {1,D} {2,D}
5 C u0 p0 c0 {3,T} {7,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89406,0.00684459,9.03088e-05,-2.20544e-07,1.55689e-10,23232.1,8.98482], Tmin=(10,'K'), Tmax=(498.309,'K')),
            NASAPolynomial(coeffs=[4.99266,0.0195567,-1.27681e-05,4.06608e-09,-4.98888e-13,22855.3,1.76768], Tmin=(498.309,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (193.137,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C#C': 1, 'C-C': 1, 'C=C': 1, 'C=O': 1, 'C-H': 2}

External symmetry: 1, optical isomers: 1

Geometry:
C       1.86809800    0.11611400   -0.45905000
C       0.73145700   -0.13766300   -0.15302000
C      -0.59576700   -0.46760300    0.21184700
C      -1.57038200    0.42798200    0.22505400
O      -2.43489200    1.19608500    0.24265900
H       2.86946300    0.34363200   -0.72954000
H      -0.86797700   -1.47854700    0.49784100
""",
)

entry(
    index = 1,
    label = "S1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {8,S} {24,S}
2  C u0 p0 c0 {3,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {2,S} {6,B} {9,B}
6  C u0 p0 c0 {4,S} {5,B} {8,B}
7  C u0 p0 c0 {8,B} {10,B} {11,S}
8  C u0 p0 c0 {1,S} {6,B} {7,B}
9  C u0 p0 c0 {5,B} {10,B} {21,S}
10 C u0 p0 c0 {7,B} {9,B} {20,S}
11 C u1 p0 c0 {7,S} {22,S} {23,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.38629,0.052836,9.70446e-05,-2.16478e-07,1.22431e-10,-10779,15.1564], Tmin=(10,'K'), Tmax=(587.144,'K')),
            NASAPolynomial(coeffs=[0.565543,0.0924031,-5.60292e-05,1.636e-08,-1.84386e-12,-10798.5,24.2757], Tmin=(587.144,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-89.6982,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (577.856,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 12, 'C-O': 1, 'H-O': 1, 'C-C': 7, 'C=C': 3}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [12, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 18], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [8, 9], dihedral: [5, 8, 9, 21], rotor symmetry: 6, max scan energy: 0.59 kJ/mol (set as a FreeRotor)
* Invalidated! pivots: [10, 11], dihedral: [2, 10, 11, 24], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
C      -3.45579000   -0.91702100    0.16905900
C      -2.10158500   -0.66376700   -0.08313200
C      -1.51887200   -0.96978700   -1.34589000
C      -0.20567800   -0.66545500   -1.61800300
C       0.62199500   -0.05250600   -0.65767100
C       2.06296400    0.23783100   -1.01643400
C       3.01430200   -0.93328400   -0.70428600
C       0.10124200    0.23758200    0.61994300
C       0.93895400    0.88530100    1.69915200
C      -1.23411300   -0.06875400    0.88996000
O      -1.70475900    0.23095400    2.13926700
H      -3.96629700   -0.60022600    1.07067800
H      -4.07014000   -1.39908400   -0.57970100
H      -2.14443600   -1.42922300   -2.10337800
H       0.20452600   -0.89028500   -2.59726200
H       2.11838100    0.45963600   -2.08687200
H       2.41105500    1.13613400   -0.50003400
H       2.71704200   -1.83115800   -1.25215000
H       3.00708500   -1.18051200    0.36039000
H       4.04153000   -0.68675700   -0.98785600
H       0.98967400    1.97156300    1.56206700
H       1.96259500    0.50783400    1.69879800
H       0.50748200    0.70351600    2.68202400
H      -2.53958600   -0.22767700    2.27692800
""",
)

entry(
    index = 2,
    label = "S2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {8,S}
4  C u0 p0 c0 {2,B} {6,B} {9,S}
5  C u0 p0 c0 {3,B} {7,B} {13,S}
6  C u0 p0 c0 {4,B} {7,B} {15,S}
7  C u0 p0 c0 {5,B} {6,B} {14,S}
8  C u1 p0 c0 {3,S} {16,S} {17,S}
9  O u0 p2 c0 {4,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82421,0.0116609,0.000251339,-5.62298e-07,3.89557e-10,-2937.11,13.1045], Tmin=(10,'K'), Tmax=(464.063,'K')),
            NASAPolynomial(coeffs=[0.668013,0.0711594,-4.53617e-05,1.38928e-08,-1.63251e-12,-2991.9,22.1616], Tmin=(464.063,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-24.4507,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 8}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 15], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [8, 9], dihedral: [2, 8, 9, 16], rotor symmetry: 3, max scan energy: 3.11 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -0.76531700   -2.25211600   -0.23625000
C      -0.03277400   -1.06226800   -0.10078800
C      -0.72926800    0.17205100    0.06542000
C      -0.04430900    1.36061000    0.20155900
C       1.35292700    1.37060700    0.17816500
C       2.05807500    0.17089000    0.01611900
O       3.43088300    0.16358300   -0.00900100
C       1.40075800   -1.05150200   -0.12472700
C       2.18784300   -2.32417600   -0.29731600
H      -0.28985300   -3.21392100   -0.36457600
H      -1.84761200   -2.23045200   -0.21446100
H      -1.81307700    0.15859000    0.08285400
H      -0.58409900    2.29231800    0.32726700
H       1.89711300    2.30446100    0.28502500
H       3.74860400    1.06525400    0.09783800
H       3.25684100   -2.12332200   -0.29112000
H       1.93989600   -2.81819900   -1.24268700
H       1.97073200   -3.03625000    0.50585200
""",
)

entry(
    index = 3,
    label = "S3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
4  C u0 p0 c0 {1,S} {5,B} {7,B}
5  C u0 p0 c0 {3,S} {4,B} {6,B}
6  C u0 p0 c0 {5,B} {9,B} {10,S}
7  C u0 p0 c0 {4,B} {8,B} {19,S}
8  C u0 p0 c0 {7,B} {9,B} {20,S}
9  C u1 p0 c0 {6,B} {8,B}
10 O u0 p2 c0 {6,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5273,0.0432568,7.51401e-05,-1.46601e-07,7.1165e-11,6886.32,16.1322], Tmin=(10,'K'), Tmax=(706.48,'K')),
            NASAPolynomial(coeffs=[1.50484,0.0774425,-4.57138e-05,1.29922e-08,-1.42876e-12,6604.72,21.1713], Tmin=(706.48,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (57.2102,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-H': 10, 'H-O': 1, 'C-C': 6, 'C=C': 3}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [11, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
* Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 18], invalidation reason: Inconsistent initial and final conformersInconsistent initial and final conformers
pivots: [9, 10], dihedral: [3, 9, 10, 19], rotor symmetry: 1, max scan energy: 0.37 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.73542500    0.07865700    0.54757400
C      -1.70595800    0.12755400   -0.59585400
C      -1.64091600   -1.15927000   -1.39599900
C      -0.74946800   -2.15785200   -0.98675700
C      -0.66688500   -3.37866100   -1.66752200
C      -1.49793100   -3.52761700   -2.74374000
C      -2.39084300   -2.58590800   -3.20431400
O      -3.18911400   -2.78867200   -4.29966000
C      -2.47722800   -1.36161700   -2.51163400
C      -3.44227200   -0.30772800   -3.00610100
H      -2.49507500   -0.72243100    1.25132300
H      -3.74427000   -0.10772300    0.17042700
H      -2.75063400    1.02263400    1.09983700
H      -0.71706100    0.32828800   -0.17267000
H      -1.93246800    0.97124200   -1.25314300
H      -0.10672300   -1.98274500   -0.12979700
H       0.02419700   -4.15273900   -1.35328100
H      -3.00788400   -3.67211700   -4.63850600
H      -2.90854600    0.53135000   -3.46589800
H      -4.11347000   -0.72162200   -3.75635000
H      -4.04885400    0.09681300   -2.19257600
""",
)

entry(
    index = 4,
    label = "S4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {4,B} {6,B}
4  C u0 p0 c0 {2,S} {3,B} {5,B}
5  C u0 p0 c0 {4,B} {7,B} {10,S}
6  C u0 p0 c0 {3,B} {8,B} {16,S}
7  C u0 p0 c0 {5,B} {8,B} {18,S}
8  C u0 p0 c0 {6,B} {7,B} {17,S}
9  C u1 p0 c0 {1,S} {19,S} {20,S}
10 O u0 p2 c0 {5,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46799,0.0465084,7.85909e-05,-1.71028e-07,9.17967e-11,-364.975,15.2363], Tmin=(10,'K'), Tmax=(635.822,'K')),
            NASAPolynomial(coeffs=[1.72235,0.0787386,-4.75727e-05,1.38157e-08,-1.54804e-12,-572.492,19.49], Tmin=(635.822,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-3.10153,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-H': 10, 'H-O': 1, 'C-C': 6, 'C=C': 3}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [11, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
* Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 18], invalidation reason: Inconsistent initial and final conformersInconsistent initial and final conformers
pivots: [9, 10], dihedral: [3, 9, 10, 19], rotor symmetry: 3, max scan energy: 0.76 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 2

Geometry:
C       2.68597700   -0.82234600    0.46028700
C       1.85252400   -0.38300800   -0.70049000
C       2.28314800   -0.97475600   -2.03121000
C       1.56625700   -2.05222500   -2.56208700
C       1.94019800   -2.62724500   -3.77106200
C       3.03326100   -2.12440300   -4.46638500
C       3.74884700   -1.04684900   -3.94357400
O       4.82546200   -0.51664400   -4.60931800
C       3.39637300   -0.45979200   -2.71758200
C       4.19952500    0.70452700   -2.18816100
H       3.18829400   -1.78145700    0.44492700
H       2.68089600   -0.25872200    1.38583200
H       1.84483600    0.71245400   -0.75465200
H       0.80065100   -0.66385400   -0.52703600
H       0.70826300   -2.43768200   -2.02207400
H       1.38072800   -3.46262400   -4.17656200
H       3.33184700   -2.56091200   -5.41552100
H       4.97163700   -1.02162400   -5.41525200
H       5.17606100    0.75037100   -2.66741900
H       3.69405000    1.65742700   -2.38516100
H       4.34548600    0.62580100   -1.10889600
""",
)

entry(
    index = 5,
    label = "S5",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {15,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,B} {8,B}
4  C u0 p0 c0 {1,S} {3,B} {5,B}
5  C u0 p0 c0 {4,B} {6,B} {13,S}
6  C u0 p0 c0 {5,B} {7,B} {12,S}
7  C u0 p0 c0 {6,B} {8,B} {14,S}
8  C u1 p0 c0 {3,B} {7,B}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86976,0.0087706,0.000201886,-4.51517e-07,3.15602e-10,13173,13.014], Tmin=(10,'K'), Tmax=(451.772,'K')),
            NASAPolynomial(coeffs=[0.785056,0.0584794,-3.7523e-05,1.1508e-08,-1.35045e-12,13223.2,22.9153], Tmin=(451.772,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (109.509,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (349.208,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 4, 'C=C': 3, 'C-H': 6}
1D rotors:
pivots: [1, 2], dihedral: [9, 1, 2, 3], rotor symmetry: 3, max scan energy: 2.86 kJ/mol
pivots: [7, 8], dihedral: [2, 7, 8, 15], rotor symmetry: 1, max scan energy: 15.17 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -2.17823100   -0.55633500    0.43400600
C      -0.69438100   -0.42308200    0.20507100
C       0.21029700   -1.44418100    0.36505700
C       1.57242400   -1.40513100    0.17752100
C       2.09481200   -0.17142500   -0.22559500
C       1.25021300    0.92166400   -0.41293500
C      -0.12566200    0.80304400   -0.20201400
O      -0.98806700    1.85082500   -0.37478500
H      -2.51817800    0.13936000    1.20643000
H      -2.73661500   -0.31887900   -0.47595600
H      -2.42825100   -1.57146500    0.74294200
H       2.21006200   -2.26770200    0.32911600
H       3.16097500   -0.06218400   -0.39374900
H       1.66167500    1.87688700   -0.72595000
H      -0.49125300    2.62822800   -0.65054400
""",
)

entry(
    index = 6,
    label = "S6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
2  C u0 p0 c0 {3,S} {5,D} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {8,D}
4  C u0 p0 c0 {3,S} {6,D} {9,S}
5  C u0 p0 c0 {1,S} {2,D} {12,S}
6  C u0 p0 c0 {1,S} {4,D} {13,S}
7  C u1 p0 c0 {2,S} {14,S} {15,S}
8  C u0 p0 c0 {3,D} {16,S} {17,S}
9  O u0 p2 c0 {4,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81301,0.011546,0.00024182,-5.0045e-07,3.15304e-10,11013.3,13.5769], Tmin=(10,'K'), Tmax=(521.026,'K')),
            NASAPolynomial(coeffs=[1.05949,0.072244,-4.68122e-05,1.45835e-08,-1.74156e-12,10763.3,19.9131], Tmin=(521.026,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (91.5093,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (432.353,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 8}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 16], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 1

Geometry:
C       2.43818600   -0.62037300    0.00700300
C       1.05795500   -0.41015500    0.00320100
C       0.55907800    0.87675000   -0.14729000
C      -0.88818500    1.23062600   -0.16771000
C      -1.79247500    0.04946700   -0.00778900
C      -1.33389200   -1.20238700    0.13903100
O      -2.15931800   -2.28601400    0.28568000
C       0.09906700   -1.54639100    0.15846500
C       0.47427800   -2.82646200    0.31009400
H       2.88438700   -1.59730900    0.12016600
H       3.11150900    0.21985000   -0.10723900
H       1.26803500    1.69125800   -0.25893600
H      -1.12213200    1.76239200   -1.10492300
H      -1.09454000    1.97473500    0.61943300
H      -2.86447000    0.23191700   -0.01310400
H      -3.07255700   -1.98223900    0.26288400
H       1.51347900   -3.12429900    0.33014300
H      -0.26541800   -3.60641000    0.41797600
""",
)

entry(
    index = 7,
    label = "S7",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,D}
2  C u0 p0 c0 {1,S} {4,S} {7,D}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,S} {6,D} {10,S}
5  C u0 p0 c0 {3,D} {6,S} {12,S}
6  C u0 p0 c0 {4,D} {5,S} {11,S}
7  C u0 p0 c0 {2,D} {13,S} {14,S}
8  C u0 p0 c0 {1,D} {15,S} {16,S}
9  O u0 p2 c0 {3,S} {17,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83368,0.00997047,0.000219221,-4.33482e-07,2.60649e-10,6105.83,12.7944], Tmin=(10,'K'), Tmax=(544.346,'K')),
            NASAPolynomial(coeffs=[0.705378,0.0695324,-4.56928e-05,1.4392e-08,-1.73268e-12,5904.54,21.0069], Tmin=(544.346,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (50.7041,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (407.409,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 4, 'C=C': 4, 'C-H': 7}
1D rotors:
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 15], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
C       2.33953400   -0.54924400   -0.25207800
C       1.11705700    0.01572500   -0.16598300
C       0.98418100    1.45648300    0.02064900
C      -0.19522300    2.00988100    0.36849600
C      -1.38408400    1.20593400    0.54641400
C      -1.35801000   -0.12393700    0.29622300
O      -2.44453700   -0.93850000    0.41549700
C      -0.14268700   -0.78908800   -0.19494700
C      -0.21959300   -2.03825000   -0.69214400
H       2.48433900   -1.62091800   -0.29557400
H       3.23091500    0.06677400   -0.26019800
H       1.87776000    2.06313500   -0.07102300
H      -0.26794100    3.07764800    0.54221100
H      -2.30533800    1.68309400    0.86712700
H      -3.20247500   -0.40931900    0.68602800
H       0.63600500   -2.52184500   -1.14527000
H      -1.14990200   -2.58757400   -0.66542900
""",
)

entry(
    index = 8,
    label = "S9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {4,B} {5,B}
4  C u0 p0 c0 {2,S} {3,B} {8,B}
5  C u0 p0 c0 {3,B} {6,B} {9,S}
6  C u0 p0 c0 {5,B} {7,B} {16,S}
7  C u0 p0 c0 {6,B} {8,B} {17,S}
8  C u1 p0 c0 {4,B} {7,B}
9  O u0 p2 c0 {5,S} {18,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59824,0.035131,7.45564e-05,-1.51722e-07,8.00033e-11,9348.26,13.5392], Tmin=(10,'K'), Tmax=(634.721,'K')),
            NASAPolynomial(coeffs=[1.44021,0.0661173,-3.97604e-05,1.15051e-08,-1.28567e-12,9271.98,20.2106], Tmin=(634.721,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (77.6747,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (424.038,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 8}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 4.37 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 15], invalidation reason: Inconsistent initial and final conformersInconsistent initial and final conformers
pivots: [8, 9], dihedral: [2, 8, 9, 16], rotor symmetry: 3, max scan energy: 0.51 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 1

Geometry:
C      -2.35832200   -0.32447100    0.32057300
C      -0.99978500    0.32029600    0.18495700
C      -0.79830200    1.65228800    0.47393500
C       0.38702700    2.33601700    0.38605300
C       1.49819600    1.60187500   -0.04014300
C       1.36181000    0.24638800   -0.34930700
O       2.43934500   -0.49563900   -0.77020100
C       0.12680300   -0.41629800   -0.24528100
C       0.01236300   -1.88149900   -0.58672300
H      -2.70177400   -0.73447200   -0.63456100
H      -3.09482900    0.40252300    0.66316500
H      -2.33664700   -1.15212700    1.03671500
H       0.47609000    3.38850600    0.62976900
H       2.46849200    2.08341000   -0.13158500
H       3.21573600    0.07172000   -0.79809900
H      -0.70372400   -2.04426700   -1.39890800
H      -0.34011200   -2.46208400    0.27209600
H       0.97422500   -2.28452100   -0.89680700
""",
)

entry(
    index = 9,
    label = "S10",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,B} {5,B}
3  C u0 p0 c0 {2,B} {4,B} {8,S}
4  C u0 p0 c0 {3,B} {6,B} {9,S}
5  C u0 p0 c0 {2,B} {7,B} {13,S}
6  C u0 p0 c0 {4,B} {7,B} {15,S}
7  C u0 p0 c0 {5,B} {6,B} {14,S}
8  C u1 p0 c0 {3,S} {16,S} {17,S}
9  O u0 p2 c0 {4,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78885,0.0141512,0.000258861,-6.05309e-07,4.31742e-10,-3463.22,12.669], Tmin=(10,'K'), Tmax=(462.035,'K')),
            NASAPolynomial(coeffs=[1.99834,0.0685187,-4.38238e-05,1.34968e-08,-1.59582e-12,-3712.62,15.4353], Tmin=(462.035,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-28.8281,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (424.038,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 8}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [3, 4], dihedral: [2, 3, 4, 12], rotor symmetry: 3, max scan energy: 8.20 kJ/mol
pivots: [8, 9], dihedral: [2, 8, 9, 18], rotor symmetry: 1, max scan energy: 16.36 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -0.78234600   -1.89144900    0.08969300
C      -0.46184900   -0.53189200    0.03748500
C       0.36813700    0.03685600   -0.98960100
C       0.93321400   -0.84495300   -2.07227000
C       0.64617200    1.39596500   -0.98060800
C       0.13543500    2.23815200    0.01159400
C      -0.67326600    1.71537600    1.02182500
C      -0.96844800    0.36188400    1.03929700
O      -1.75441400   -0.19562400    2.00619100
H      -0.41525100   -2.58720800   -0.65078000
H      -1.40974200   -2.27701800    0.87948000
H       0.14001100   -1.33783200   -2.64441300
H       1.53770900   -0.26289100   -2.76961200
H       1.56640900   -1.63616600   -1.65694600
H       1.27363600    1.81234600   -1.76118400
H       0.36531000    3.29699600   -0.00056200
H      -1.07357400    2.36407100    1.79605500
H      -2.03414100    0.49278400    2.61824000
""",
)

entry(
    index = 10,
    label = "S11",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,B} {5,B}
4  C u0 p0 c0 {1,S} {3,B} {6,B}
5  C u0 p0 c0 {3,B} {7,B} {9,S}
6  C u0 p0 c0 {4,B} {8,B} {16,S}
7  C u0 p0 c0 {5,B} {8,B} {17,S}
8  C u1 p0 c0 {6,B} {7,B}
9  O u0 p2 c0 {5,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63074,0.0316268,0.000100701,-2.12243e-07,1.24199e-10,9369.94,13.5055], Tmin=(10,'K'), Tmax=(550.425,'K')),
            NASAPolynomial(coeffs=[0.766807,0.0681814,-4.18162e-05,1.23313e-08,-1.40133e-12,9446.75,23.4461], Tmin=(550.425,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (77.858,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (424.038,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 8}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 4.91 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 15], invalidation reason: Inconsistent initial and final conformersInconsistent initial and final conformers
pivots: [8, 9], dihedral: [2, 8, 9, 16], rotor symmetry: 3, max scan energy: 0.93 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 1

Geometry:
C      -2.15399500   -0.52908900    0.12332700
C      -0.65289600   -0.64128700    0.00270200
C       0.15402100   -0.34187800    1.11658700
C       1.50955500   -0.45942400    0.95471800
C       2.15117300   -0.84214400   -0.19350800
C       1.33255800   -1.13739000   -1.29568300
O       1.87309700   -1.52991500   -2.49258700
C      -0.06704500   -1.04150800   -1.21214500
C      -0.91773300   -1.36633600   -2.41691300
H      -2.56047000    0.19335100   -0.59188300
H      -2.64478000   -1.48663500   -0.07892200
H      -2.44283300   -0.20866100    1.12533500
H      -0.29612200   -0.03333600    2.05334000
H       3.23253400   -0.91844400   -0.26529800
H       2.83155500   -1.55357600   -2.41111500
H      -1.52421800   -0.50633700   -2.71959400
H      -1.61046900   -2.18755000   -2.20543900
H      -0.30026400   -1.65702900   -3.26396300
""",
)

entry(
    index = 11,
    label = "S12",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,B} {5,B}
4  C u0 p0 c0 {2,S} {3,B} {6,B}
5  C u0 p0 c0 {3,B} {7,B} {16,S}
6  C u0 p0 c0 {4,B} {8,B} {15,S}
7  C u0 p0 c0 {5,B} {8,B} {17,S}
8  C u0 p0 c0 {6,B} {7,B} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 O u1 p2 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7213,0.0373657,4.09997e-05,-7.36095e-08,2.95174e-11,-5917.22,12.5786], Tmin=(10,'K'), Tmax=(912.286,'K')),
            NASAPolynomial(coeffs=[4.53101,0.0577869,-3.19915e-05,8.53243e-09,-8.85428e-13,-7062.49,3.27939], Tmin=(912.286,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-49.1546,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (424.038,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 9}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 3.66 kJ/mol
pivots: [8, 9], dihedral: [2, 8, 9, 16], rotor symmetry: 3, max scan energy: 2.70 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -1.50073500   -1.54749200    0.40448800
C      -0.78615500   -0.23502500    0.18542300
C      -1.17018900    0.59813800   -0.88076100
C      -0.53970300    1.83314800   -1.13329700
C       0.48247600    2.25474100   -0.32636800
C       0.92738700    1.44320200    0.79055400
O       1.86197700    1.82991100    1.52738300
C       0.25038700    0.16370300    1.02584400
C       0.71289500   -0.67237800    2.18112800
H      -0.80864900   -2.39334100    0.34606600
H      -1.96789100   -1.58736600    1.39344400
H      -2.28189500   -1.70139600   -0.34167100
H      -1.97893400    0.27721600   -1.52892700
H      -0.87206900    2.44006800   -1.96819600
H       0.99774000    3.19520000   -0.47977100
H       1.52868500   -0.17034800    2.69772600
H      -0.10030300   -0.85005900    2.89359900
H       1.05931100   -1.65629200    1.84588500
""",
)

entry(
    index = 12,
    label = "S13",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {4,B} {6,B}
4  C u0 p0 c0 {2,S} {3,B} {5,B}
5  C u0 p0 c0 {4,B} {8,B} {9,S}
6  C u0 p0 c0 {3,B} {7,B} {16,S}
7  C u0 p0 c0 {6,B} {8,B} {17,S}
8  C u1 p0 c0 {5,B} {7,B}
9  O u0 p2 c0 {5,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59254,0.0359976,6.83746e-05,-1.38422e-07,7.10677e-11,9686.96,13.2178], Tmin=(10,'K'), Tmax=(658.733,'K')),
            NASAPolynomial(coeffs=[1.65922,0.0654743,-3.91361e-05,1.12589e-08,-1.25169e-12,9556.84,18.8169], Tmin=(658.733,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (80.4931,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (424.038,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 8}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 5.18 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 15], invalidation reason: Inconsistent initial and final conformersInconsistent initial and final conformers
pivots: [8, 9], dihedral: [2, 8, 9, 16], rotor symmetry: 3, max scan energy: 1.33 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -2.14645500   -0.20415200    0.14980000
C      -0.73703000    0.33705000    0.10390500
C       0.24096100   -0.21140500    0.93910800
C       1.55731100    0.26909200    0.91983600
C       1.81752100    1.28946800    0.04776500
C       0.90263200    1.87416500   -0.80078500
O       1.22358800    2.89654500   -1.65472700
C      -0.41815200    1.38864900   -0.77839400
C      -1.45418500    1.99927000   -1.69105500
H      -2.86785700    0.57211800    0.42519000
H      -2.45963500   -0.59680000   -0.82311900
H      -2.23109500   -1.01183400    0.87847600
H      -0.02031100   -1.02072600    1.61277500
H       2.31875000   -0.15334400    1.56581800
H       2.15836800    3.09785400   -1.53758000
H      -1.02109000    2.79117200   -2.29875700
H      -2.28406000    2.42558100   -1.11778800
H      -1.88022400    1.24795100   -2.36408000
""",
)

entry(
    index = 13,
    label = "S14",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {7,D}
3  C u0 p0 c0 {2,S} {4,D} {8,S}
4  C u0 p0 c0 {3,D} {6,S} {9,S}
5  C u0 p0 c0 {1,S} {6,D} {12,S}
6  C u0 p0 c0 {4,S} {5,D} {13,S}
7  C u0 p0 c0 {2,D} {16,S} {17,S}
8  C u1 p0 c0 {3,S} {14,S} {15,S}
9  O u0 p2 c0 {4,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80214,0.0126204,0.000250307,-5.44167e-07,3.6029e-10,8210.24,13.8142], Tmin=(10,'K'), Tmax=(496.667,'K')),
            NASAPolynomial(coeffs=[1.46292,0.0710996,-4.60255e-05,1.42887e-08,-1.69823e-12,7953.69,18.5406], Tmin=(496.667,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (68.2121,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 8}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [3, 4], dihedral: [2, 3, 4, 12], rotor symmetry: 1, max scan energy: 17.67 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       2.20021900   -0.43147300    0.00654700
C       0.89541100   -0.03509300   -0.05839900
C       0.29520000    0.46369100   -1.25951500
O       0.94299800    0.39685100   -2.45637400
C      -0.98911600    1.06023100   -1.27591800
C      -1.67840000    1.30217500   -0.12896000
C      -1.08205800    0.95739900    1.20786800
C      -0.02295200   -0.12296300    1.11523100
C       0.05671700   -1.10616800    2.01506900
H       2.87991600   -0.33814400   -0.83329200
H       2.63110100   -0.79525100    0.92876600
H       1.66995900   -0.23202200   -2.38291400
H      -1.38913400    1.34337800   -2.24329100
H      -2.64391900    1.79307700   -0.15787300
H      -0.62382800    1.87027900    1.62560000
H      -1.85755400    0.65863600    1.91786300
H       0.79746800   -1.89316800    1.94035600
H      -0.63077000   -1.15659500    2.85227900
""",
)

entry(
    index = 14,
    label = "S15",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {3,D} {4,S} {7,S}
3  C u0 p0 c0 {1,S} {2,D} {9,S}
4  C u0 p0 c0 {2,S} {6,S} {8,D}
5  C u0 p0 c0 {1,S} {6,D} {12,S}
6  C u0 p0 c0 {4,S} {5,D} {13,S}
7  C u1 p0 c0 {2,S} {14,S} {15,S}
8  C u0 p0 c0 {4,D} {16,S} {17,S}
9  O u0 p2 c0 {3,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78356,0.0138219,0.000254737,-5.63276e-07,3.76378e-10,9315.27,14.0343], Tmin=(10,'K'), Tmax=(498.15,'K')),
            NASAPolynomial(coeffs=[2.25594,0.0697562,-4.51792e-05,1.40683e-08,-1.679e-12,8925.65,14.9013], Tmin=(498.15,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (77.3951,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 8}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [3, 4], dihedral: [2, 3, 4, 12], rotor symmetry: 1, max scan energy: 20.49 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       1.18884900    1.80477100    0.54158100
C       0.41271200    0.70358100    0.18353300
C      -0.23512400   -0.07512500    1.14652600
O      -0.10022400    0.13878700    2.48080800
C      -1.15747800   -1.21246600    0.86646000
C      -1.31333300   -1.50278400   -0.59202200
C      -0.66863600   -0.80706500   -1.53233200
C       0.23883600    0.30710800   -1.24630900
C       0.86518800    0.91776500   -2.26817800
H       1.26494900    2.16127600    1.56240000
H       1.71510800    2.39777500   -0.19011900
H       0.58831800    0.79591100    2.63288500
H      -0.79353700   -2.10357500    1.39980700
H      -2.13536500   -0.99781200    1.32461800
H      -1.97493700   -2.31697400   -0.86843500
H      -0.80593100   -1.05979400   -2.57895900
H       0.69855100    0.58805300   -3.28674600
H       1.55132800    1.74274300   -2.13556500
""",
)

entry(
    index = 15,
    label = "S16",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {20,S}
2  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {4,B} {5,B}
4  C u0 p0 c0 {3,B} {6,B} {8,S}
5  C u0 p0 c0 {1,S} {3,B} {7,B}
6  C u0 p0 c0 {4,B} {9,B} {15,S}
7  C u0 p0 c0 {5,B} {9,B} {17,S}
8  C u0 p0 c0 {4,S} {10,D} {14,S}
9  C u0 p0 c0 {6,B} {7,B} {16,S}
10 C u0 p0 c0 {8,D} {18,S} {19,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58553,0.0376172,9.60266e-05,-1.8657e-07,9.58953e-11,-10305.6,13.9486], Tmin=(10,'K'), Tmax=(656.898,'K')),
            NASAPolynomial(coeffs=[1.34825,0.075436,-4.55805e-05,1.32138e-08,-1.47696e-12,-10533.7,19.8286], Tmin=(656.898,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-85.7365,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (478.082,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-H': 9, 'H-O': 1, 'C-C': 5, 'C=C': 4}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Inconsistent initial and final conformersInconsistent initial and final conformers
* Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 17], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [9, 10], dihedral: [3, 9, 10, 18], rotor symmetry: 3, max scan energy: 1.70 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.92423300    0.55360400   -0.82349300
C      -1.89530600    0.86435500   -0.03144000
C      -0.73386400    0.00076100    0.25895700
C      -0.28283800   -0.92322200   -0.69734900
C       0.80752300   -1.73859200   -0.43350100
C       1.47175900   -1.63901300    0.78476500
C       1.03858700   -0.71538100    1.73562300
O       1.67643700   -0.58723900    2.94382200
C      -0.06667000    0.11644500    1.49599700
C      -0.51881100    1.08611300    2.56287700
H      -3.00710100   -0.41104700   -1.31244800
H      -3.72938000    1.25802200   -0.99634100
H      -1.90337100    1.83467900    0.45674100
H      -0.77609900   -0.97520900   -1.65998500
H       1.15334800   -2.44596000   -1.17862700
H       2.33148700   -2.26855700    0.99659400
H       2.39606200   -1.22462100    2.98454300
H      -1.59083900    0.99414400    2.75427400
H      -0.32709800    2.12397100    2.26783500
H       0.01184700    0.90694000    3.49555700
""",
)

entry(
    index = 16,
    label = "S17",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {4,B} {6,B}
4  C u0 p0 c0 {3,B} {5,B} {9,S}
5  C u0 p0 c0 {4,B} {7,B} {10,S}
6  C u0 p0 c0 {3,B} {8,B} {18,S}
7  C u0 p0 c0 {5,B} {8,B} {16,S}
8  C u0 p0 c0 {6,B} {7,B} {17,S}
9  C u1 p0 c0 {4,S} {19,S} {20,S}
10 O u0 p2 c0 {5,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73701,0.0203702,0.000280524,-6.86094e-07,5.22173e-10,-6076.34,14.3078], Tmin=(10,'K'), Tmax=(411.893,'K')),
            NASAPolynomial(coeffs=[-0.112656,0.0850353,-5.43141e-05,1.66525e-08,-1.95741e-12,-5990.62,26.6565], Tmin=(411.893,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-50.5233,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-H': 10, 'H-O': 1, 'C-C': 6, 'C=C': 3}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [11, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 13], invalidation reason: Another conformer for S17 exists which is 3.67 kJ/mol lower.Another conformer for S17 exists which is 3.67 kJ/mol lower.
* Invalidated! pivots: [8, 9], dihedral: [2, 8, 9, 10], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [9, 10], dihedral: [8, 9, 10, 19], rotor symmetry: 3, max scan energy: 11.28 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       0.54148000    1.61211000   -1.19971700
C       0.67835800    0.47959000   -0.38679100
C      -0.46159100   -0.34381500   -0.08822300
O      -1.68250200   -0.09469800   -0.64114800
C      -0.37462300   -1.41929500    0.78188200
C       0.84637600   -1.73615300    1.36879800
C       1.98766000   -0.98229000    1.06883900
C       1.93652400    0.10125800    0.20665300
C       3.20425500    0.86492800   -0.10517600
C       3.83043200    0.48951300   -1.46143400
H       1.38542000    2.23050300   -1.46447900
H      -0.42231800    1.97075000   -1.54042900
H      -1.57758800    0.50021800   -1.39053100
H      -1.26809300   -1.99969400    0.97649000
H       0.91468700   -2.57622900    2.05008400
H       2.93543100   -1.24689400    1.52557000
H       3.01455600    1.94268900   -0.07584900
H       3.93152200    0.66498800    0.68676500
H       3.14227500    0.68165900   -2.28788500
H       4.74346600    1.06476300   -1.63935400
H       4.08865400   -0.57224300   -1.48622500
""",
)

entry(
    index = 17,
    label = "S18",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,B} {6,B}
4  C u0 p0 c0 {2,S} {5,B} {8,B}
5  C u0 p0 c0 {3,B} {4,B} {9,S}
6  C u0 p0 c0 {3,B} {7,B} {16,S}
7  C u0 p0 c0 {6,B} {8,B} {17,S}
8  C u1 p0 c0 {4,B} {7,B}
9  O u0 p2 c0 {5,S} {18,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48038,0.0468999,1.87374e-05,-5.9555e-08,2.8465e-11,8765.25,13.1095], Tmin=(10,'K'), Tmax=(794.624,'K')),
            NASAPolynomial(coeffs=[4.12029,0.0592772,-3.40721e-05,9.45418e-09,-1.01842e-12,8171.09,7.07063], Tmin=(794.624,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (72.8365,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (419.881,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 8}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 5.52 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 15], rotor symmetry: 3, max scan energy: 3.83 kJ/mol
pivots: [8, 9], dihedral: [2, 8, 9, 18], rotor symmetry: 1, max scan energy: 13.92 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       2.68857300   -0.15264800   -0.21422400
C       1.25365800    0.29318900   -0.05987400
C       0.45802900   -0.06484700    1.00461700
C      -0.84724200    0.29520200    1.21829700
C      -1.42236700    1.11761500    0.23866500
C      -0.70367700    1.53829300   -0.88014500
C      -1.31662000    2.42223200   -1.93603400
C       0.63058100    1.11953600   -1.01651300
O       1.29843700    1.55676800   -2.13102600
H       2.83696900   -0.73744200   -1.13022800
H       3.37888800    0.69924800   -0.24259800
H       2.98312400   -0.78224600    0.62499400
H      -1.41210100   -0.02743400    2.08470800
H      -2.45405700    1.43728000    0.35071800
H      -0.76270700    3.36001800   -2.03874900
H      -2.35284200    2.66009900   -1.68949500
H      -1.29787100    1.93929400   -2.91747100
H       2.19741600    1.21376400   -2.12471500
""",
)

entry(
    index = 18,
    label = "S19",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
2  C u0 p0 c0 {6,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {4,B} {5,B}
4  C u0 p0 c0 {3,B} {6,S} {7,B}
5  C u0 p0 c0 {3,B} {8,B} {10,S}
6  C u1 p0 c0 {2,S} {4,S} {17,S}
7  C u0 p0 c0 {4,B} {9,B} {18,S}
8  C u0 p0 c0 {5,B} {9,B} {20,S}
9  C u0 p0 c0 {7,B} {8,B} {19,S}
10 O u0 p2 c0 {5,S} {21,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46776,0.0513831,3.5999e-05,-8.39258e-08,3.78155e-11,-7069.73,13.8545], Tmin=(10,'K'), Tmax=(819.12,'K')),
            NASAPolynomial(coeffs=[3.86446,0.071374,-4.07643e-05,1.12321e-08,-1.20177e-12,-7870.36,7.52944], Tmin=(819.12,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-58.8052,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-H': 10, 'H-O': 1, 'C-C': 6, 'C=C': 3}
1D rotors:
pivots: [1, 2], dihedral: [11, 1, 2, 3], rotor symmetry: 3, max scan energy: 1.56 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
* Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 18], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [9, 10], dihedral: [3, 9, 10, 19], rotor symmetry: 3, max scan energy: 3.97 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       3.01780300   -0.34813900   -0.52788600
C       1.84281100    0.49238700   -0.13707800
C       1.87621100    1.51409400    0.83985800
C       3.08326100    1.81191700    1.53574800
C       3.12660600    2.80742600    2.49134300
C       1.98014600    3.54349200    2.79323800
C       0.78235400    3.26884600    2.12243000
O      -0.35727700    3.98256700    2.40555500
C       0.69820000    2.27086900    1.15048900
C      -0.61278200    2.00969600    0.45354500
H       3.84678900    0.25666000   -0.91803200
H       2.74414800   -1.06732900   -1.30154600
H       3.42107300   -0.91479300    0.32152200
H       0.90712500    0.29604400   -0.64388500
H       3.97939700    1.24813700    1.31070500
H       4.05283700    3.02234900    3.01247300
H       2.01066400    4.32736600    3.54444400
H      -0.15501000    4.63042500    3.08720200
H      -1.38577300    2.68035600    0.82186800
H      -0.95170400    0.98088700    0.61475200
H      -0.52489100    2.15548300   -0.62827000
""",
)

entry(
    index = 19,
    label = "S20",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {1,S} {5,B} {6,B}
5  C u0 p0 c0 {3,S} {4,B} {7,B}
6  C u0 p0 c0 {4,B} {8,B} {19,S}
7  C u0 p0 c0 {5,B} {9,B} {18,S}
8  C u0 p0 c0 {6,B} {9,B} {20,S}
9  C u0 p0 c0 {7,B} {8,B} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 O u1 p2 c0 {7,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62343,0.050086,2.73628e-05,-6.0814e-08,2.3996e-11,-8787.15,14.9628], Tmin=(10,'K'), Tmax=(977.187,'K')),
            NASAPolynomial(coeffs=[6.62105,0.0641259,-3.45755e-05,8.99531e-09,-9.12837e-13,-10629.2,-5.85736], Tmin=(977.187,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-73.0072,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (494.711,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-H': 11, 'C-C': 6, 'C=C': 3}
1D rotors:
pivots: [1, 2], dihedral: [11, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.90 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 24.91 kJ/mol
pivots: [9, 10], dihedral: [3, 9, 10, 19], rotor symmetry: 3, max scan energy: 1.45 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       2.47540100   -0.68616800    0.47337200
C       1.40023400   -0.82169200   -0.61986200
C       1.93976700   -0.56976100   -2.01407900
C       1.94817900    0.75106500   -2.50483800
C       2.45655500    1.07985000   -3.77585600
C       2.96283900    0.09433400   -4.58076000
C       2.98170200   -1.28669300   -4.13844200
O       3.44337800   -2.18381600   -4.87830000
C       2.44678900   -1.59575400   -2.80590900
C       2.46294500   -3.03448700   -2.37460000
H       2.90668200    0.31837900    0.47587800
H       2.04910600   -0.87325800    1.46258000
H       3.29246800   -1.39519700    0.31830200
H       0.59448800   -0.10898900   -0.41772100
H       0.95083600   -1.81613700   -0.56629300
H       1.54244200    1.54030200   -1.87973400
H       2.43873500    2.11191800   -4.10820500
H       3.36360100    0.29389200   -5.56720600
H       1.44495300   -3.42546700   -2.26632500
H       2.97938500   -3.63312600   -3.12269700
H       2.96101200   -3.16422900   -1.40969600
""",
)

entry(
    index = 20,
    label = "S21",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {5,D}
4  C u0 p0 c0 {3,S} {7,S} {8,D}
5  C u0 p0 c0 {1,S} {3,D} {14,S}
6  C u0 p0 c0 {1,S} {7,D} {15,S}
7  C u0 p0 c0 {4,S} {6,D} {16,S}
8  C u0 p0 c0 {4,D} {17,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 O u1 p2 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77765,0.0172646,0.000202996,-4.42158e-07,2.95794e-10,7608.16,12.9836], Tmin=(10,'K'), Tmax=(469.584,'K')),
            NASAPolynomial(coeffs=[-0.0708552,0.0726488,-4.61167e-05,1.40043e-08,-1.63008e-12,7720.41,25.988], Tmin=(469.584,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (63.2285,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 9}
1D rotors:
pivots: [3, 4], dihedral: [2, 3, 4, 12], rotor symmetry: 3, max scan energy: 11.94 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       1.24124900    1.81016100   -0.64003700
C       0.30873800    0.90392100   -0.30574700
C       0.61942100   -0.47296100    0.12518200
C       2.06590300   -0.89264400    0.19630000
C      -0.35912500   -1.33431100    0.44702300
C      -1.82323400   -1.01538700    0.40923900
C      -2.13374800    0.36805800   -0.02381700
C      -1.13626500    1.33026200   -0.37908100
O      -1.46149900    2.47250100   -0.73356500
H       0.92973100    2.80084000   -0.94617400
H       2.30102200    1.59391200   -0.61740400
H       2.62711300   -0.26275200    0.89392400
H       2.55251600   -0.80355900   -0.78026200
H       2.15550500   -1.92840400    0.52688500
H      -0.09737900   -2.34059100    0.76041700
H      -2.34905900   -1.72965900   -0.24690900
H      -2.27573300   -1.19807400    1.39872100
H      -3.16515300    0.69869500   -0.08466600
""",
)

entry(
    index = 21,
    label = "S22",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u0 p0 c0 {2,S} {5,S} {8,D}
4  C u0 p0 c0 {2,D} {7,S} {15,S}
5  C u0 p0 c0 {3,S} {6,S} {12,D}
6  C u0 p0 c0 {5,S} {7,D} {13,S}
7  C u0 p0 c0 {4,S} {6,D} {14,S}
8  C u0 p0 c0 {3,D} {16,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80213,0.0151336,0.000195482,-4.23742e-07,2.82908e-10,-253.604,12.2104], Tmin=(10,'K'), Tmax=(470.783,'K')),
            NASAPolynomial(coeffs=[0.131669,0.0682024,-4.33268e-05,1.31639e-08,-1.53279e-12,-150.507,24.5776], Tmin=(470.783,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-2.13646,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 5, 'C=C': 3, 'C-H': 8, 'C=O': 1}
1D rotors:
pivots: [8, 9], dihedral: [2, 8, 9, 15], rotor symmetry: 3, max scan energy: 9.68 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       0.71176500   -2.02895700    0.12319500
C       0.00437700   -0.88528100    0.09257000
C      -1.49760300   -0.99563100    0.29574100
O      -2.04144500   -2.07531700    0.47914900
C      -2.25083400    0.25958700    0.25917600
C      -1.62107600    1.43552800    0.05464500
C      -0.18823900    1.52610800   -0.13762100
C       0.61201000    0.43382400   -0.12426400
C       2.09882000    0.55026200   -0.32614400
H       0.19122400   -2.96476700    0.28843000
H       1.78546600   -2.05716800   -0.01073000
H      -3.32189500    0.18762500    0.40334600
H      -2.19402700    2.35739500    0.03030900
H       0.24381300    2.50813800   -0.29645700
H       2.42892600   -0.01929200   -1.20092800
H       2.65054200    0.16432700    0.53714500
H       2.38848400    1.59157400   -0.47308700
""",
)

entry(
    index = 22,
    label = "S23",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,S} {5,D}
4  C u0 p0 c0 {2,S} {3,S} {7,D}
5  C u0 p0 c0 {3,D} {6,S} {15,S}
6  C u0 p0 c0 {5,S} {8,D} {16,S}
7  C u0 p0 c0 {4,D} {17,D}
8  C u1 p0 c0 {6,D} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 O u0 p2 c0 {7,D}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75769,0.029723,0.000564768,-3.56115e-06,7.173e-09,29475.1,12.6298], Tmin=(10,'K'), Tmax=(161.554,'K')),
            NASAPolynomial(coeffs=[3.34509,0.0676368,-4.44273e-05,1.39901e-08,-1.68363e-12,29452.2,12.7495], Tmin=(161.554,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (246.412,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (419.881,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 4, 'C=C': 3, 'C-H': 9, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Inconsistent initial and final conformersInconsistent initial and final conformers
pivots: [4, 5], dihedral: [3, 4, 5, 13], rotor symmetry: 3, max scan energy: 2.11 kJ/mol
pivots: [4, 6], dihedral: [3, 4, 6, 7], rotor symmetry: 1, max scan energy: 24.41 kJ/mol
pivots: [6, 7], dihedral: [4, 6, 7, 16], rotor symmetry: 3, max scan energy: 11.36 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       1.62059100   -3.04258400    0.68605200
C       1.22725300   -1.80764000    0.93728200
C       0.45209500   -0.97546900    0.03095500
C       0.02989500    0.29353500    0.25112800
C       0.30943900    1.06727900    1.51763900
C      -0.74861500    0.99507000   -0.77657500
C      -1.11738500    0.36200900   -2.10811500
C      -1.16589300    2.23432500   -0.57206100
O      -1.54611200    3.32366900   -0.42057800
H       2.18063500   -3.81442300    1.19158000
H       1.51073400   -1.38412100    1.90563400
H       0.20282600   -1.45090300   -0.91068200
H       0.86752400    1.98410700    1.29859400
H       0.88889000    0.49607000    2.23960100
H      -0.62473900    1.36481100    2.00631000
H      -1.71742700   -0.53923400   -1.95227000
H      -1.69640300    1.04611500   -2.73042100
H      -0.21726900    0.08330500   -2.66371600
""",
)

entry(
    index = 23,
    label = "S24",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {5,D}
4  C u0 p0 c0 {1,S} {6,S} {13,D}
5  C u0 p0 c0 {3,D} {7,S} {16,S}
6  C u0 p0 c0 {4,S} {7,D} {14,S}
7  C u0 p0 c0 {5,S} {6,D} {15,S}
8  C u1 p0 c0 {1,S} {17,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66792,0.0309149,0.00015487,-4.25937e-07,3.60511e-10,12341.2,13.5349], Tmin=(10,'K'), Tmax=(303.606,'K')),
            NASAPolynomial(coeffs=[0.591148,0.0714515,-4.5407e-05,1.38385e-08,-1.618e-12,12528,24.711], Tmin=(303.606,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (102.624,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 6, 'C=C': 2, 'C-H': 9, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [8, 9], dihedral: [2, 8, 9, 16], rotor symmetry: 3, max scan energy: 7.21 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       0.63559900    1.87509100   -0.55924900
C      -0.02081600    0.91144300    0.38727300
C       0.64298200   -0.47068900    0.11513600
O       0.34613600   -1.10638200   -0.87769700
C       1.64299800   -0.91585600    1.08928000
C       1.75234100   -0.30279900    2.28658100
C       0.93579700    0.83714200    2.66845400
C       0.06893100    1.40797100    1.81259300
C      -0.80896100    2.56579200    2.18367500
H       0.49413800    1.73307900   -1.62314900
H       1.43641200    2.51835900   -0.21650700
H      -1.07119300    0.78817400    0.09249100
H       2.21672000   -1.79890700    0.83358300
H       2.45809200   -0.68364500    3.01884400
H       1.03182500    1.21749100    3.68006900
H      -1.86668700    2.29252300    2.09233000
H      -0.64676100    3.41128300    1.50625000
H      -0.62794000    2.89864100    3.20715300
""",
)









entry(
    index = 24,
    label = "S25",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {3,S} {5,D}
5  C u0 p0 c0 {4,D} {7,S} {17,S}
6  C u0 p0 c0 {1,S} {8,S} {16,D}
7  C u0 p0 c0 {5,S} {8,D} {18,S}
8  C u1 p0 c0 {6,S} {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u0 p2 c0 {6,D}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56994,0.0404323,4.49404e-05,-9.30265e-08,4.3096e-11,18171.5,13.9169], Tmin=(10,'K'), Tmax=(767.045,'K')),
            NASAPolynomial(coeffs=[2.86809,0.0631283,-3.66687e-05,1.02573e-08,-1.11205e-12,17719.2,13.4664], Tmin=(767.045,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (151.057,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 6, 'C=C': 2, 'C-H': 9, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 6.05 kJ/mol
* Invalidated! pivots: [8, 9], dihedral: [2, 8, 9, 16], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
C       2.10844200   -0.00469000   -0.03006100
C       0.66948800   -0.43839500   -0.05276200
C      -0.25704700    0.19835300   -0.79240200
C      -1.64265400   -0.26840300   -0.83580300
C      -2.00457600   -1.37678000   -0.19111700
C      -1.11638200   -2.25177400    0.55410300
O      -1.37812300   -3.34863600    1.00084500
C       0.28935500   -1.62750900    0.80203700
C       0.36058100   -1.28180500    2.31294400
H       2.42638300    0.29013500    0.97541800
H       2.27914600    0.84072800   -0.69846800
H       2.76605200   -0.82468200   -0.33999200
H       0.00803700    1.06666100   -1.38661600
H      -2.36298600    0.30284700   -1.41649200
H       0.99731700   -2.44447600    0.61819000
H      -0.32092900   -0.46275600    2.55563100
H       1.37130300   -0.98656400    2.60085800
H       0.07547400   -2.16045900    2.89303600
""",
)

entry(
    index = 25,
    label = "S26",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
3  C u1 p0 c0 {2,S} {4,S} {7,S}
4  C u0 p0 c0 {3,S} {5,S} {8,D}
5  C u0 p0 c0 {1,S} {4,S} {14,D}
6  C u0 p0 c0 {1,S} {7,D} {15,S}
7  C u0 p0 c0 {3,S} {6,D} {16,S}
8  C u0 p0 c0 {4,D} {17,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 O u0 p2 c0 {5,D}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6372,0.033806,8.04434e-05,-1.53095e-07,7.61359e-11,1639,13.758], Tmin=(10,'K'), Tmax=(684.186,'K')),
            NASAPolynomial(coeffs=[1.80773,0.0666219,-3.99976e-05,1.15164e-08,-1.27923e-12,1371.6,18.1063], Tmin=(684.186,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (13.5892,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 6, 'C=C': 2, 'C-H': 9, 'C=O': 1}
1D rotors:
pivots: [3, 4], dihedral: [2, 3, 4, 12], rotor symmetry: 3, max scan energy: 5.82 kJ/mol
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 1

Geometry:
C      -1.56221700    1.42716800    0.83052600
C      -0.48719800    0.74002100    0.34182200
C       0.73041400    1.35348400   -0.09982200
C       0.88009900    2.84730300   -0.04008700
C       1.79991900    0.56334900   -0.59458600
C       1.75697100   -0.79511700   -0.68648000
C       0.55479000   -1.57095700   -0.26411500
C      -0.61996100   -0.76049700    0.27472800
O      -1.62804700   -1.33194200    0.63527600
H      -2.44192500    0.87960800    1.14122000
H      -1.56998500    2.50497400    0.92030200
H       0.76972500    3.21944800    0.98504000
H       1.85734800    3.16219200   -0.40881200
H       0.11391200    3.35020200   -0.64142600
H       2.69870700    1.08131300   -0.91535000
H       2.60838900   -1.34392200   -1.07390700
H       0.81366800   -2.30543600    0.51035100
H       0.16668000   -2.17642700   -1.09420600
""",
)

entry(
    index = 26,
    label = "S27",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {4,S} {7,D}
6  C u0 p0 c0 {1,S} {8,S} {19,D}
7  C u0 p0 c0 {5,D} {9,S} {20,S}
8  C u0 p0 c0 {6,S} {9,D} {22,S}
9  C u0 p0 c0 {7,S} {8,D} {21,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {6,D}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59067,0.0371391,0.000184162,-4.99999e-07,4.18614e-10,-17155.1,14.6621], Tmin=(10,'K'), Tmax=(306.782,'K')),
            NASAPolynomial(coeffs=[-0.133531,0.0856975,-5.32627e-05,1.59498e-08,-1.83954e-12,-16926.6,28.2287], Tmin=(306.782,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-142.631,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (519.654,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 12, 'C=O': 1, 'C-C': 7, 'C=C': 2}
1D rotors:
pivots: [1, 2], dihedral: [11, 1, 2, 3], rotor symmetry: 1, max scan energy: 5.96 kJ/mol
pivots: [8, 9], dihedral: [2, 8, 9, 17], rotor symmetry: 3, max scan energy: 15.13 kJ/mol
pivots: [8, 10], dihedral: [2, 8, 10, 20], rotor symmetry: 3, max scan energy: 15.20 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.28489400    2.19447100    0.38950100
C       0.38540800    0.85767900    0.22108000
C       1.70803300    0.71904600    0.43687400
C       2.39457000   -0.54295500    0.25202700
C       1.76415300   -1.65397000   -0.18145600
C       0.33792100   -1.62763100   -0.49817100
O      -0.23641600   -2.59881400   -0.96484300
C      -0.46772000   -0.33762000   -0.18194700
C      -1.38183300   -0.72636700    1.01714800
C      -1.34762500   -0.01454600   -1.41098700
H      -0.65773500    2.57413700   -0.56736500
H       0.41225800    2.93043300    0.79342700
H      -1.14622900    2.13844500    1.06215600
H       2.29579400    1.57536600    0.75133300
H       3.45987300   -0.57550500    0.46086400
H       2.28047300   -2.59240900   -0.34522800
H      -2.07530700    0.08187700    1.25868000
H      -1.95708700   -1.61358100    0.74632100
H      -0.79140500   -0.95372900    1.90834600
H      -0.74128600    0.34557500   -2.24664300
H      -2.09581200    0.74485000   -1.17461900
H      -1.85715900   -0.92491200   -1.72678300
""",
)

entry(
    index = 27,
    label = "S28",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
4  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {3,S} {6,D}
6  C u0 p0 c0 {4,S} {5,D} {8,S}
7  C u0 p0 c0 {1,S} {9,D} {20,S}
8  C u0 p0 c0 {6,S} {9,S} {21,D}
9  C u0 p0 c0 {7,D} {8,S} {22,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {7,S}
21 O u0 p2 c0 {8,D}
22 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65922,0.0512644,2.51376e-05,-5.39106e-08,1.99981e-11,-18036,13.6697], Tmin=(10,'K'), Tmax=(1048.88,'K')),
            NASAPolynomial(coeffs=[7.42387,0.0645108,-3.32816e-05,8.31127e-09,-8.12838e-13,-20344.1,-11.9104], Tmin=(1048.88,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-149.891,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (523.812,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 12, 'C=O': 1, 'C-C': 7, 'C=C': 2}
1D rotors:
pivots: [1, 2], dihedral: [11, 1, 2, 3], rotor symmetry: 3, max scan energy: 1.18 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 14], rotor symmetry: 3, max scan energy: 2.39 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [3, 5, 6, 18], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.34624600    1.13456000   -0.25755600
C      -0.88872000    0.74469500   -0.23371000
C      -0.01254500    1.08326200   -1.20489100
C      -0.43353900    1.90954800   -2.39596600
C       1.43734400    0.65751500   -1.17996100
C       1.80659200   -0.19536200   -2.42337600
C       1.84728100   -0.06516200    0.06447000
C       0.98890500   -0.38805700    1.03386000
C      -0.44214000   -0.03775900    0.95297400
O      -1.21824200   -0.37163200    1.83913800
H      -2.86498900    0.63339300    0.55834700
H      -2.47511400    2.21428400   -0.12413300
H      -2.82548200    0.86077100   -1.20117700
H       0.40881600    2.47015600   -2.80946400
H      -1.21787500    2.62107900   -2.13429800
H      -0.82724900    1.27708200   -3.20072900
H       2.04457700    1.57518900   -1.24221200
H       1.60507200    0.34389000   -3.35058900
H       1.23064300   -1.12363400   -2.42972600
H       2.86890300   -0.45132200   -2.40788200
H       2.89543800   -0.34431800    0.13998800
H       1.29166400   -0.92737000    1.92443900
""",
)

entry(
    index = 28,
    label = "S29",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {5,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  C u0 p0 c0 {3,S} {5,D} {9,S}
7  C u0 p0 c0 {1,S} {5,S} {20,D}
8  C u0 p0 c0 {1,S} {9,D} {21,S}
9  C u0 p0 c0 {6,S} {8,D} {22,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {7,D}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56591,0.0503998,3.29689e-05,-6.82274e-08,2.71191e-11,-17621.2,15.4073], Tmin=(10,'K'), Tmax=(944.757,'K')),
            NASAPolynomial(coeffs=[4.89675,0.069901,-3.79018e-05,9.94368e-09,-1.01844e-12,-18994.4,3.12553], Tmin=(944.757,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-146.481,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (519.654,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 12, 'C=O': 1, 'C-C': 7, 'C=C': 2}
1D rotors:
pivots: [1, 2], dihedral: [11, 1, 2, 3], rotor symmetry: 3, max scan energy: 0.63 kJ/mol (set as a FreeRotor)
pivots: [3, 4], dihedral: [2, 3, 4, 14], rotor symmetry: 3, max scan energy: 0.69 kJ/mol (set as a FreeRotor)
pivots: [7, 8], dihedral: [5, 7, 8, 18], rotor symmetry: 3, max scan energy: 11.61 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       2.24566600   -1.51574900   -0.49438500
C       0.98172500   -0.71072600   -0.34648600
C       0.18734000   -0.38250700   -1.40240700
C       0.47738500   -0.77591100   -2.83007100
C      -1.03583100    0.42143900   -1.17868000
O      -1.76735400    0.75057900   -2.10102100
C      -1.40353000    0.85050600    0.24870900
C      -1.68058500    2.36941600    0.29453000
C      -0.43648400    0.42448100    1.30602000
C       0.65527800   -0.29140800    1.01706600
H       3.10443600   -0.94440800   -0.12430600
H       2.18945600   -2.42471700    0.11506000
H       2.44753800   -1.80673300   -1.52308900
H      -0.31164600   -0.39076700   -3.47387200
H       1.43203000   -0.36943900   -3.17796600
H       0.51854300   -1.86273300   -2.95057700
H      -2.36094400    0.34569600    0.44904000
H      -2.38185700    2.63263700   -0.49722400
H      -0.75686800    2.93414200    0.14463500
H      -2.10470000    2.65705900    1.25970100
H      -0.64996100    0.72018400    2.32927800
H       1.34055500   -0.58603100    1.80598900
""",
)

entry(
    index = 29,
    label = "S30",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {5,D} {7,S}
4  C u0 p0 c0 {1,S} {6,D} {10,S}
5  C u0 p0 c0 {3,D} {8,S} {16,S}
6  C u0 p0 c0 {4,D} {8,S} {18,S}
7  C u0 p0 c0 {3,S} {9,D} {15,S}
8  C u1 p0 c0 {5,S} {6,S} {17,S}
9  C u0 p0 c0 {7,D} {19,S} {20,S}
10 O u0 p2 c0 {4,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73042,0.0173544,0.000307252,-6.91213e-07,4.68184e-10,232.295,14.193], Tmin=(10,'K'), Tmax=(493.312,'K')),
            NASAPolynomial(coeffs=[2.2518,0.0827963,-5.42666e-05,1.69941e-08,-2.03251e-12,-272.224,13.6895], Tmin=(493.312,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (1.86516,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (494.711,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-H': 10, 'H-O': 1, 'C-C': 6, 'C=C': 3}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 40.16 kJ/mol
pivots: [7, 8], dihedral: [6, 7, 8, 17], rotor symmetry: 1, max scan energy: 23.67 kJ/mol
pivots: [9, 10], dihedral: [3, 9, 10, 19], rotor symmetry: 3, max scan energy: 11.43 kJ/mol
* Invalidated! pivots: [1, 2], dihedral: [11, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
C       2.28436000   -1.94508500   -0.22787500
C       2.09401700   -0.64279500   -0.53475900
C       0.92234000    0.15458000   -0.29579100
C       0.94012700    1.51952000   -0.57122100
C      -0.10920700    2.36456100   -0.21923700
C      -1.23083700    1.85845900    0.50033400
C      -1.32076200    0.52997200    0.77064600
O      -2.32410500   -0.04225100    1.49164800
C      -0.34677800   -0.48490300    0.23912600
C      -1.05574000   -1.34015600   -0.85443400
H       3.22904000   -2.43153900   -0.43680200
H       1.52300800   -2.55214300    0.24761800
H       2.92216800   -0.10876400   -0.99729400
H       1.82558400    1.94252300   -1.03581300
H      -0.05524200    3.42292800   -0.44209900
H      -1.99824200    2.54105700    0.85546000
H      -2.94144100    0.64109000    1.77769600
H      -0.09693100   -1.16275000    1.06659700
H      -0.38568000   -2.11500800   -1.22781300
H      -1.34827200   -0.70535000   -1.69394900
H      -1.95027100   -1.81080300   -0.44243600
""",
)

entry(
    index = 30,
    label = "S31",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {4,B} {5,B}
3  C u0 p0 c0 {6,B} {7,B} {8,S}
4  C u0 p0 c0 {2,B} {6,B} {10,S}
5  C u0 p0 c0 {2,B} {7,B} {16,S}
6  C u0 p0 c0 {3,B} {4,B} {17,S}
7  C u0 p0 c0 {3,B} {5,B} {15,S}
8  C u0 p0 c0 {3,S} {9,D} {14,S}
9  C u0 p0 c0 {8,D} {18,S} {19,S}
10 O u0 p2 c0 {4,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47056,0.0531093,2.23274e-05,-6.67403e-08,3.04821e-11,-11247.8,13.363], Tmin=(10,'K'), Tmax=(849.059,'K')),
            NASAPolynomial(coeffs=[5.59146,0.0649403,-3.71275e-05,1.02141e-08,-1.08982e-12,-12394.6,-1.15433], Tmin=(849.059,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-93.5338,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (469.768,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-H': 9, 'H-O': 1, 'C-C': 5, 'C=C': 4}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 16.99 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 16], rotor symmetry: 3, max scan energy: 3.82 kJ/mol
pivots: [8, 9], dihedral: [6, 8, 9, 19], rotor symmetry: 1, max scan energy: 16.11 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -3.35041600    1.35982200   -0.05218600
C      -2.65975300    0.27504500    0.30827900
C      -1.20859700    0.05810000    0.21457600
C      -0.67100500   -1.15852400    0.64877500
C       0.69961100   -1.39805000    0.57456100
C       1.58545100   -0.44958500    0.07129500
C       3.06827900   -0.68903500   -0.01711900
C       1.04047100    0.77271300   -0.36431200
O       1.92639600    1.69451700   -0.85658600
C      -0.32372400    1.02188700   -0.29489000
H      -2.88194300    2.24167600   -0.47526700
H      -4.42624400    1.39902100    0.06747800
H      -3.21120000   -0.56505200    0.72460400
H      -1.33091200   -1.92139300    1.04692100
H       1.09410900   -2.34917100    0.91725900
H       3.42103400   -0.60845600   -1.04972300
H       3.32553500   -1.68052900    0.35957000
H       3.62429700    0.05587700    0.56007400
H       1.44535500    2.48493800   -1.12203900
H      -0.70119400    1.97912400   -0.64226200
""",
)

entry(
    index = 31,
    label = "S32",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {7,D}
4  C u0 p0 c0 {1,S} {6,S} {13,D}
5  C u0 p0 c0 {3,S} {8,D} {14,S}
6  C u0 p0 c0 {4,S} {8,D} {15,S}
7  C u0 p0 c0 {3,D} {16,S} {17,S}
8  C u0 p0 c0 {5,D} {6,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81773,0.0119481,0.000240178,-5.37424e-07,3.68729e-10,26533.8,13.3868], Tmin=(10,'K'), Tmax=(475.241,'K')),
            NASAPolynomial(coeffs=[1.37021,0.0671449,-4.32361e-05,1.33281e-08,-1.57384e-12,26375.8,19.2635], Tmin=(475.241,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (220.578,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 5, 'C=C': 3, 'C-H': 8, 'C=O': 1}
1D rotors:
pivots: [8, 9], dihedral: [2, 8, 9, 15], rotor symmetry: 3, max scan energy: 14.60 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       0.49049600    2.00465800    0.60664400
C       0.65651100    0.81310000    0.03592700
C       1.97897600    0.19327600   -0.30590000
C       1.99902500   -1.06479100    0.08228400
C       1.11305400   -2.01745200    0.29931000
C      -0.25474900   -1.63988200   -0.20517500
O      -1.18196800   -2.41278700   -0.23054500
C      -0.46803500   -0.10134000   -0.48500100
C      -1.88194400    0.29504700   -0.05289800
H      -0.49112700    2.42571400    0.78807900
H       1.34524400    2.59614700    0.91401900
H       2.64507100    0.63440300   -1.03987800
H       1.17876000   -2.83627000    1.00574500
H      -0.41496500   -0.02355500   -1.58192400
H      -2.14773300    1.28273300   -0.43507700
H      -2.59661100   -0.43194700   -0.43798500
H      -1.96950300    0.30982100    1.03656800
""",
)

entry(
    index = 32,
    label = "S33",
    molecule = 
"""
1  C u0 p0 c0 {3,B} {4,B} {6,S}
2  C u0 p0 c0 {3,B} {5,B} {9,S}
3  C u0 p0 c0 {1,B} {2,B} {14,S}
4  C u0 p0 c0 {1,B} {7,B} {11,S}
5  C u0 p0 c0 {2,B} {7,B} {13,S}
6  C u0 p0 c0 {1,S} {8,D} {10,S}
7  C u0 p0 c0 {4,B} {5,B} {12,S}
8  C u0 p0 c0 {6,D} {15,S} {16,S}
9  O u0 p2 c0 {2,S} {17,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83319,0.0101908,0.000220914,-4.48417e-07,2.77234e-10,-6131.77,13.4752], Tmin=(10,'K'), Tmax=(528.706,'K')),
            NASAPolynomial(coeffs=[0.864741,0.0682553,-4.48404e-05,1.40636e-08,-1.68313e-12,-6315.53,21.1981], Tmin=(528.706,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-51.0399,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 4, 'C=C': 4, 'C-H': 7}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 16.14 kJ/mol
pivots: [7, 8], dihedral: [6, 7, 8, 16], rotor symmetry: 2, max scan energy: 16.17 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       2.73699800   -0.80674000   -0.72342800
C       1.96563700    0.27251400   -0.57197400
C       0.54968700    0.31926700   -0.17400400
C      -0.08331200    1.56499000   -0.07202800
C      -1.42309900    1.65049300    0.30197800
C      -2.15657500    0.50583500    0.58060000
C      -1.53424400   -0.74343800    0.48186400
O      -2.29583700   -1.84216800    0.76559800
C      -0.19734600   -0.83529800    0.10907000
H       3.77357500   -0.71110500   -1.02282400
H       2.37616500   -1.81601800   -0.55868600
H       2.41035500    1.24735800   -0.75832800
H       0.47871600    2.46683900   -0.28705700
H      -1.90058100    2.62100900    0.37698800
H      -3.19834500    0.55150400    0.87270400
H      -1.75953100   -2.63503700    0.66292000
H       0.26574500   -1.81483500    0.03869200
""",
)

entry(
    index = 33,
    label = "S34",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {8,S}
4  C u0 p0 c0 {2,B} {6,B} {12,S}
5  C u0 p0 c0 {3,B} {7,B} {14,S}
6  C u0 p0 c0 {4,B} {7,B} {13,S}
7  C u1 p0 c0 {5,B} {6,B}
8  O u0 p2 c0 {3,S} {15,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75345,0.0208024,0.000113953,-2.33416e-07,1.38257e-10,13284.7,12.1799], Tmin=(10,'K'), Tmax=(550.634,'K')),
            NASAPolynomial(coeffs=[1.47795,0.0564859,-3.54299e-05,1.06174e-08,-1.2204e-12,13244.9,19.1635], Tmin=(550.634,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (110.414,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (349.208,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 4, 'C=C': 3, 'C-H': 6}
1D rotors:
pivots: [1, 2], dihedral: [9, 1, 2, 3], rotor symmetry: 3, max scan energy: 3.75 kJ/mol
pivots: [7, 8], dihedral: [2, 7, 8, 15], rotor symmetry: 1, max scan energy: 15.73 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -1.82186100   -0.82291500    0.15196600
C      -0.39394200   -0.35027200    0.05792400
C       0.16288600    0.51572400    0.99826200
C       1.49280900    0.95846600    0.91413900
C       2.21262100    0.48577700   -0.15237600
C       1.74663300   -0.36725400   -1.12317300
C       0.41421900   -0.78853800   -1.00695400
O      -0.16339000   -1.63723800   -1.91130500
H      -2.39271600   -0.53837900   -0.73679300
H      -2.31491400   -0.39813800    1.02802500
H      -1.87451200   -1.91337600    0.22154200
H      -0.45593900    0.85759300    1.82266100
H       1.90767800    1.63155100    1.65465300
H       2.36801000   -0.70776000   -1.94701800
H       0.48033200   -1.86729500   -2.58903800
""",
)

entry(
    index = 34,
    label = "S36",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {8,S}
3  C u0 p0 c0 {1,B} {5,B} {9,S}
4  C u0 p0 c0 {2,B} {6,B} {12,S}
5  C u0 p0 c0 {3,B} {6,B} {10,S}
6  C u0 p0 c0 {4,B} {5,B} {11,S}
7  C u1 p0 c0 {1,S} {13,S} {14,S}
8  O u0 p2 c0 {2,S} {15,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85142,0.00880393,0.000188311,-3.69225e-07,2.18924e-10,1252.06,11.0526], Tmin=(10,'K'), Tmax=(555.656,'K')),
            NASAPolynomial(coeffs=[1.37465,0.0599997,-3.99653e-05,1.27247e-08,-1.54417e-12,1012.21,16.9111], Tmin=(555.656,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (10.3515,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (353.365,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 4, 'C=C': 3, 'C-H': 6}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [9, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [7, 8], dihedral: [2, 7, 8, 15], rotor symmetry: 2, max scan energy: 16.18 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       2.08859800   -0.66923800   -0.21635000
C       0.72880600   -0.34920200   -0.13796000
C      -0.11379800   -0.33041500   -1.28702400
C      -1.45672000   -0.01404200   -1.20755300
C      -2.02781700    0.30105100    0.03071800
C      -1.23775800    0.29475300    1.18362500
C       0.11065800   -0.02158900    1.11267700
O       0.91653100   -0.03930200    2.21334600
H       2.71295600   -0.67871100    0.66476000
H       2.53823200   -0.91415100   -1.17015100
H       0.33174100   -0.57506800   -2.24528200
H      -2.06728000   -0.00984200   -2.10297300
H      -3.07974900    0.55037900    0.10303100
H      -1.67908700    0.53910000    2.14621400
H       0.39657600    0.19486600    2.98911300
""",
)

entry(
    index = 35,
    label = "S37",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,B} {6,B}
5  C u0 p0 c0 {1,S} {4,B} {9,B}
6  C u0 p0 c0 {4,B} {7,B} {10,S}
7  C u0 p0 c0 {6,B} {8,B} {19,S}
8  C u0 p0 c0 {7,B} {9,B} {20,S}
9  C u1 p0 c0 {5,B} {8,B}
10 O u0 p2 c0 {6,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46219,0.0479829,5.91202e-05,-1.28189e-07,6.38639e-11,6663.25,14.2708], Tmin=(10,'K'), Tmax=(701.052,'K')),
            NASAPolynomial(coeffs=[2.19038,0.0759146,-4.48813e-05,1.27796e-08,-1.40797e-12,6333.51,16.3312], Tmin=(701.052,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (55.3448,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-H': 10, 'H-O': 1, 'C-C': 6, 'C=C': 3}
1D rotors:
pivots: [1, 2], dihedral: [11, 1, 2, 3], rotor symmetry: 3, max scan energy: 12.63 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
* Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 18], invalidation reason: Inconsistent initial and final conformersInconsistent initial and final conformers
pivots: [9, 10], dihedral: [3, 9, 10, 19], rotor symmetry: 3, max scan energy: 1.01 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -2.74955100    0.52839700    0.29629000
C      -1.77852400    0.34329700   -0.87127600
C      -1.87405800   -1.00182800   -1.56340400
C      -2.76559500   -1.97551400   -1.16756700
C      -2.92487900   -3.21668000   -1.72870900
C      -2.09645700   -3.52094900   -2.81231300
C      -1.16940900   -2.57884100   -3.26551000
O      -0.34387300   -2.85510100   -4.32933400
C      -1.03875500   -1.31731000   -2.66107300
C      -0.02566000   -0.32593600   -3.17895100
H      -2.58082000   -0.22103400    1.07370200
H      -3.78725300    0.43425200   -0.03355500
H      -2.62543400    1.51682500    0.74602700
H      -0.74984500    0.48688400   -0.51844900
H      -1.94235400    1.13473800   -1.61293600
H      -3.64978700   -3.93547500   -1.36369100
H      -2.17108500   -4.48789000   -3.30342400
H      -0.53383400   -3.74283900   -4.64753300
H       0.52407900   -0.73840200   -4.02230400
H      -0.50851500    0.60057400   -3.50655800
H       0.69579800   -0.05301800   -2.40183600
""",
)

entry(
    index = 36,
    label = "S38",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {6,D} {7,S}
5  C u0 p0 c0 {1,S} {8,S} {17,D}
6  C u0 p0 c0 {3,S} {4,D} {18,S}
7  C u1 p0 c0 {4,S} {9,S} {19,S}
8  C u0 p0 c0 {5,S} {9,D} {21,S}
9  C u0 p0 c0 {7,S} {8,D} {20,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 O u0 p2 c0 {5,D}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.52847,0.0480051,4.88294e-05,-9.96219e-08,4.42388e-11,-3200.45,14.1901], Tmin=(10,'K'), Tmax=(815.338,'K')),
            NASAPolynomial(coeffs=[3.58159,0.0724565,-4.16181e-05,1.15067e-08,-1.23381e-12,-4030.51,8.90751], Tmin=(815.338,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-26.6198,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-H': 11, 'C-C': 7, 'C=C': 2}
1D rotors:
pivots: [1, 2], dihedral: [11, 1, 2, 3], rotor symmetry: 3, max scan energy: 3.55 kJ/mol
pivots: [9, 10], dihedral: [3, 9, 10, 19], rotor symmetry: 3, max scan energy: 14.77 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
C       2.59697400    0.09568500    0.20992900
C       1.64370300    0.93416700   -0.57844800
C       1.28056800    2.23023100   -0.34366800
C       0.38008300    2.88275000   -1.23617800
C       0.10695700    4.25296900   -1.15505600
C       0.71774900    5.07615500   -0.22868500
C       1.66450800    4.54514200    0.73815800
O       2.31661200    5.26352300    1.48415900
C       1.77886500    3.01717400    0.86046500
C       1.00083500    2.60936200    2.13841800
H       2.07834400   -0.75194400    0.67560500
H       3.36026700   -0.33762500   -0.44638400
H       3.10469600    0.65024100    0.99933800
H       1.19868000    0.44906200   -1.44489000
H      -0.06920700    2.29941400   -2.03287100
H      -0.57936400    4.68629000   -1.87597800
H       0.55173700    6.14666900   -0.21572500
H       2.83854400    2.81425300    1.03475100
H       1.12652600    1.54522100    2.34749300
H       1.37068400    3.18418300    2.98941600
H      -0.06785700    2.80720900    2.02113000
""",
)

entry(
    index = 37,
    label = "S39",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {10,S}
2  C u0 p0 c0 {4,S} {9,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {2,S} {6,D}
5  C u0 p0 c0 {1,S} {7,S} {16,D}
6  C u0 p0 c0 {4,D} {8,S} {17,S}
7  C u0 p0 c0 {5,S} {8,D} {19,S}
8  C u0 p0 c0 {6,S} {7,D} {18,S}
9  C u1 p0 c0 {2,S} {20,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u0 p2 c0 {5,D}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54986,0.0555646,1.51944e-05,-4.9134e-08,1.9936e-11,9379.77,15.33], Tmin=(10,'K'), Tmax=(995.123,'K')),
            NASAPolynomial(coeffs=[7.70132,0.0635755,-3.41095e-05,8.83714e-09,-8.93563e-13,7330.64,-10.8224], Tmin=(995.123,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (78.0282,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-H': 11, 'C-C': 7, 'C=C': 2}
1D rotors:
pivots: [1, 2], dihedral: [11, 1, 2, 3], rotor symmetry: 2, max scan energy: 3.61 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
* Invalidated! pivots: [9, 10], dihedral: [3, 9, 10, 19], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
C       2.83038200   -0.20388400   -0.46085700
C       1.85215900   -0.19855800    0.67025000
C       0.44094500   -0.56110200    0.25850800
C      -0.57844000    0.30693200    0.39553700
C      -1.92607400   -0.01627500   -0.03806400
C      -2.23728300   -1.18408300   -0.63775300
C      -1.20858500   -2.19775700   -0.88050800
O      -1.44440600   -3.23619500   -1.47625600
C       0.20472600   -1.93314500   -0.33127900
C       0.55035300   -3.06441400    0.67105500
H       2.55208900    0.20548600   -1.42467600
H       3.86576600   -0.47651500   -0.30073400
H       2.19982300   -0.88010500    1.45573400
H       1.82407700    0.79836400    1.13899100
H      -0.40340400    1.28707000    0.82741400
H      -2.69969000    0.72934600    0.12025000
H      -3.23922200   -1.41425700   -0.98023500
H       0.88024700   -2.05445700   -1.18817300
H      -0.03558200   -2.96325300    1.58841300
H       0.31408200   -4.02317400    0.20868800
H       1.60965400   -3.05350900    0.93282600
""",
)

entry(
    index = 38,
    label = "S40",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {6,S} {7,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {5,D} {8,S}
5  C u0 p0 c0 {3,S} {4,D} {6,S}
6  C u0 p0 c0 {2,S} {5,S} {17,D}
7  C u0 p0 c0 {2,S} {8,D} {18,S}
8  C u0 p0 c0 {4,S} {7,D} {19,S}
9  C u1 p0 c0 {1,S} {20,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 O u0 p2 c0 {6,D}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67302,0.0554438,7.82713e-06,-3.59374e-08,1.37339e-11,8366.46,15.6447], Tmin=(10,'K'), Tmax=(1113,'K')),
            NASAPolynomial(coeffs=[10.9782,0.0555737,-2.79061e-05,6.76483e-09,-6.41915e-13,5106.13,-27.7221], Tmin=(1113,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (69.6395,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-H': 11, 'C-C': 7, 'C=C': 2}
1D rotors:
pivots: [1, 2], dihedral: [11, 1, 2, 3], rotor symmetry: 2, max scan energy: 1.87 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [4, 5], dihedral: [3, 4, 5, 15], rotor symmetry: 3, max scan energy: 0.89 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 2

Geometry:
C       2.62608700    0.54935200    0.89398800
C       1.89572500    0.46075500   -0.40820800
C       0.49028300   -0.08528300   -0.25628800
C       0.13591100   -1.33062300   -0.67785600
C       1.07663800   -2.30437700   -1.34284800
C      -1.26232100   -1.79234900   -0.50543400
O      -1.63153300   -2.89414100   -0.87957600
C      -2.26360300   -0.85272600    0.16128100
C      -1.74580900    0.47986700    0.58697500
C      -0.46586500    0.81503200    0.39038300
H       3.40937500    1.28268000    1.03978700
H       2.47138600   -0.19763200    1.66245700
H       2.46234300   -0.15118900   -1.12290300
H       1.83779800    1.45874300   -0.86213500
H       0.61634500   -3.29141700   -1.35785000
H       1.27754400   -2.02265700   -2.38255200
H       2.03600000   -2.36953900   -0.82502800
H      -2.68613800   -1.39249800    1.01882700
H      -3.10797700   -0.73705400   -0.53049500
H      -2.43543500    1.17113000    1.06094600
H      -0.09686500    1.78451100    0.70844800
""",
)

entry(
    index = 39,
    label = "S41",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {5,B} {6,B}
4  C u0 p0 c0 {2,S} {5,B} {7,B}
5  C u0 p0 c0 {3,B} {4,B} {9,S}
6  C u0 p0 c0 {3,B} {8,B} {16,S}
7  C u0 p0 c0 {4,B} {8,B} {17,S}
8  C u1 p0 c0 {6,B} {7,B}
9  O u0 p2 c0 {5,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61207,0.0354261,0.000118364,-3.45866e-07,2.99563e-10,9131.89,12.5961], Tmin=(10,'K'), Tmax=(297.549,'K')),
            NASAPolynomial(coeffs=[1.25279,0.0671422,-4.15219e-05,1.23625e-08,-1.41792e-12,9272.29,21.1184], Tmin=(297.549,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (75.926,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (419.881,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 8}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 6.37 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 15], rotor symmetry: 3, max scan energy: 3.68 kJ/mol
pivots: [8, 9], dihedral: [2, 8, 9, 18], rotor symmetry: 2, max scan energy: 11.84 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       2.57933300    0.55261200   -0.05721900
C       1.25672200   -0.16460100    0.07050200
C       0.33945200    0.17311100    1.08074000
C      -0.83942400   -0.52461900    1.13023900
C      -1.20300900   -1.53248200    0.27071700
C      -0.30316200   -1.88627200   -0.74519700
C      -0.60981200   -2.97789700   -1.73671800
C       0.91434000   -1.19058600   -0.82376800
O       1.76091100   -1.57488100   -1.83631400
H       3.42944700   -0.13234600    0.05221700
H       2.68246100    1.31686500    0.71386800
H       2.68037300    1.05699100   -1.02635900
H       0.57708900    0.96227500    1.78641300
H      -2.15149000   -2.05227500    0.35640000
H      -0.60033600   -2.59348800   -2.76088200
H      -1.58908100   -3.41789400   -1.54095700
H       0.14219000   -3.77125000   -1.69380400
H       2.56180000   -1.04342100   -1.80665000
""",
)

entry(
    index = 40,
    label = "S42",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,B} {5,B}
3  C u0 p0 c0 {4,B} {6,B} {8,S}
4  C u0 p0 c0 {2,B} {3,B} {9,S}
5  C u0 p0 c0 {2,B} {7,B} {15,S}
6  C u0 p0 c0 {3,B} {7,B} {13,S}
7  C u0 p0 c0 {5,B} {6,B} {14,S}
8  C u1 p0 c0 {3,S} {16,S} {17,S}
9  O u0 p2 c0 {4,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80397,0.0131867,0.000256057,-5.93169e-07,4.22302e-10,-3475.53,12.7203], Tmin=(10,'K'), Tmax=(457.617,'K')),
            NASAPolynomial(coeffs=[1.42449,0.0694095,-4.4347e-05,1.36249e-08,-1.6062e-12,-3628.66,18.2871], Tmin=(457.617,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-28.9259,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (424.038,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 8}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [6, 7], dihedral: [5, 6, 7, 15], rotor symmetry: 3, max scan energy: 6.01 kJ/mol
pivots: [8, 9], dihedral: [2, 8, 9, 18], rotor symmetry: 2, max scan energy: 14.02 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -2.56259800   -0.60137200    0.52725200
C      -1.31823500   -0.04350800    0.21054500
C      -0.09944200   -0.74837600    0.42545700
C       1.12258900   -0.19031000    0.11014700
C       1.18442800    1.09745400   -0.43438500
C       0.02045400    1.84043900   -0.66893300
C       0.08488500    3.23067700   -1.25664200
C      -1.21188100    1.26999800   -0.34774600
O      -2.38943800    1.93411900   -0.54829500
H      -3.48016600   -0.05723800    0.35980000
H      -2.62232900   -1.59664300    0.94889600
H      -0.15458800   -1.74583700    0.84771600
H       2.03650100   -0.74683400    0.28304100
H       2.14548700    1.53506400   -0.68182300
H      -0.44990300    3.29907400   -2.21222900
H       1.11808100    3.52259100   -1.44772400
H      -0.34168700    3.98330600   -0.58180200
H      -2.21075100    2.80149700   -0.92416200
""",
)

entry(
    index = 41,
    label = "S43",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {5,B} {6,B}
4  C u0 p0 c0 {2,S} {5,B} {7,B}
5  C u0 p0 c0 {3,B} {4,B} {15,S}
6  C u0 p0 c0 {3,B} {8,B} {16,S}
7  C u0 p0 c0 {4,B} {8,B} {18,S}
8  C u0 p0 c0 {6,B} {7,B} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 O u1 p2 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76874,0.0371966,3.84062e-05,-6.75344e-08,2.61256e-11,-7323.34,11.9395], Tmin=(10,'K'), Tmax=(956.383,'K')),
            NASAPolynomial(coeffs=[5.35792,0.0557726,-3.02879e-05,7.92586e-09,-8.08106e-13,-8780.83,-1.68715], Tmin=(956.383,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-60.8237,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (424.038,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 9}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 2.48 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 16], rotor symmetry: 3, max scan energy: 2.48 kJ/mol


External symmetry: 2, optical isomers: 1

Geometry:
C      -2.60670200   -0.61797600    0.24376300
C      -1.21324500   -0.15814500   -0.05623200
C      -0.29418900   -0.93293100   -0.73090000
C       1.00244700   -0.45696100   -0.98878300
C       1.40366900    0.82220200   -0.56797400
C       0.53600600    1.65011500    0.11162600
C       0.91365300    3.02113400    0.58157600
C      -0.82373700    1.18113900    0.39539800
O      -1.63300400    1.90705600    1.00879200
H      -2.79347600   -0.60736700    1.32151900
H      -3.34133400    0.06339800   -0.19509700
H      -2.78394900   -1.62499200   -0.13758900
H      -0.57233000   -1.92578200   -1.06954100
H       1.70543800   -1.08754800   -1.52162400
H       2.41243900    1.15967400   -0.78312300
H       0.24869600    3.77453400    0.14940100
H       0.79655500    3.10376800    1.66601800
H       1.94424100    3.26269800    0.31612800
""",
)

entry(
    index = 42,
    label = "S44",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {5,D}
3  C u0 p0 c0 {4,S} {6,S} {8,D}
4  C u0 p0 c0 {2,S} {3,S} {12,D}
5  C u0 p0 c0 {2,D} {7,S} {15,S}
6  C u0 p0 c0 {3,S} {7,D} {13,S}
7  C u0 p0 c0 {5,S} {6,D} {14,S}
8  C u0 p0 c0 {3,D} {16,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70188,0.0266081,0.000102921,-1.95234e-07,1.03534e-10,-911.951,12.1727], Tmin=(10,'K'), Tmax=(622.528,'K')),
            NASAPolynomial(coeffs=[1.04691,0.0646949,-3.9517e-05,1.15626e-08,-1.30255e-12,-988.845,20.4504], Tmin=(622.528,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-7.62578,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 5, 'C=C': 3, 'C-H': 8, 'C=O': 1}
1D rotors:
pivots: [6, 7], dihedral: [5, 6, 7, 15], rotor symmetry: 3, max scan energy: 4.98 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       2.47197900   -1.13498100    0.36195300
C       1.40891900   -0.32826200    0.18927300
C       1.52594400    1.11861100    0.12667500
C       0.43198400    1.88717800   -0.04775100
C      -0.88463800    1.29422400   -0.17701400
C      -1.10612100   -0.04171900   -0.13306700
C      -2.46225500   -0.66845100   -0.26536000
C       0.04019700   -0.95843800    0.05562500
O      -0.11498000   -2.17128400    0.10112800
H       3.47559400   -0.73734100    0.46337400
H       2.33367800   -2.20863000    0.40211900
H       2.51243100    1.55978500    0.22369100
H       0.51837200    2.96665500   -0.09456600
H      -1.72777500    1.96530900   -0.31563100
H      -2.48830200   -1.35868700   -1.11358800
H      -2.69988500   -1.26661000    0.61913600
H      -3.23728500    0.08816100   -0.40020600
""",
)

entry(
    index = 43,
    label = "S45",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {6,D} {8,S}
4  C u0 p0 c0 {1,S} {3,S} {13,D}
5  C u0 p0 c0 {1,S} {7,D} {14,S}
6  C u0 p0 c0 {3,D} {7,S} {15,S}
7  C u0 p0 c0 {5,D} {6,S} {16,S}
8  C u1 p0 c0 {3,S} {17,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75098,0.0198805,0.000182094,-3.84789e-07,2.4537e-10,2917.8,14.4435], Tmin=(10,'K'), Tmax=(498.825,'K')),
            NASAPolynomial(coeffs=[0.148302,0.072202,-4.57017e-05,1.38254e-08,-1.60302e-12,2985.69,26.3965], Tmin=(498.825,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (24.2198,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 6, 'C=C': 2, 'C-H': 9, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [6, 7], dihedral: [5, 6, 7, 16], rotor symmetry: 3, max scan energy: 10.65 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       2.66882400   -0.67746800   -0.65059500
C       1.47901700   -0.06951600   -0.36509300
C       1.34011600    1.32245400   -0.11661600
C       0.09768100    1.91898000    0.18435500
C      -1.06653500    1.20762200    0.18958700
C      -1.12056000   -0.24823600   -0.16758600
C      -2.09108400   -1.05152100    0.71647900
C       0.24952400   -0.93797400   -0.26627700
O       0.32477900   -2.14835400   -0.29498700
H       2.70567200   -1.74692400   -0.80819900
H       3.58795800   -0.10831500   -0.72438900
H       2.23353000    1.93801100   -0.13397400
H       0.07575200    2.97925400    0.41418300
H      -2.00683700    1.69642100    0.42321600
H      -1.50216200   -0.30802700   -1.20308100
H      -3.10318500   -0.64713700    0.63880100
H      -2.10110600   -2.09619800    0.40803000
H      -1.78402500   -1.00573300    1.76436600
""",
)

entry(
    index = 44,
    label = "S46",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {4,S} {6,S} {8,D}
4  C u0 p0 c0 {2,D} {3,S} {9,S}
5  C u0 p0 c0 {1,S} {6,D} {12,S}
6  C u0 p0 c0 {3,S} {5,D} {13,S}
7  C u1 p0 c0 {2,S} {14,S} {15,S}
8  C u0 p0 c0 {3,D} {16,S} {17,S}
9  O u0 p2 c0 {4,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81005,0.0120902,0.000247331,-5.33168e-07,3.51069e-10,6962.93,14.5559], Tmin=(10,'K'), Tmax=(497.272,'K')),
            NASAPolynomial(coeffs=[1.21227,0.0711387,-4.58705e-05,1.42007e-08,-1.68467e-12,6749.57,20.5308], Tmin=(497.272,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (57.8427,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 8}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [3, 4], dihedral: [2, 3, 4, 12], rotor symmetry: 1, max scan energy: 14.16 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [3, 5, 6, 13], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.97237700    1.49140300   -0.38587400
C      -0.90561900    0.65448400   -0.18815900
C      -0.85623100   -0.28368700    0.87559800
O      -1.83242000   -0.31784100    1.82373500
C       0.17641200   -1.27481200    1.01313800
C       0.18317800   -2.17411600    2.03396800
C       1.23068900   -1.27461200   -0.00766500
C       1.28955300   -0.36782800   -0.98488500
C       0.28220000    0.73245900   -1.13675600
H      -1.97196500    2.21378300   -1.19233800
H      -2.87993000    1.45094200    0.20604300
H      -2.34088900    0.49906100    1.77814300
H       0.96789800   -2.91702100    2.10773300
H      -0.58673900   -2.17223500    2.79216800
H       1.98736900   -2.04846600    0.07086400
H       2.09908500   -0.39555300   -1.70751400
H      -0.08633600    0.74948900   -2.16928100
H       0.78837100    1.69850700   -0.99784300
""",
)

entry(
    index = 45,
    label = "S47",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
2  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {5,S} {9,S}
5  C u0 p0 c0 {4,S} {7,D} {8,S}
6  C u0 p0 c0 {1,S} {8,D} {15,S}
7  C u0 p0 c0 {5,D} {16,S} {17,S}
8  C u1 p0 c0 {5,S} {6,D}
9  O u0 p2 c0 {4,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70486,0.0245663,0.000156933,-3.43468e-07,2.23936e-10,21842.2,15.4546], Tmin=(10,'K'), Tmax=(482.59,'K')),
            NASAPolynomial(coeffs=[0.278682,0.0712088,-4.47502e-05,1.34813e-08,-1.55946e-12,21960.5,27.2865], Tmin=(482.59,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (181.573,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 8}
1D rotors:
pivots: [6, 7], dihedral: [5, 6, 7, 15], rotor symmetry: 1, max scan energy: 0.65 kJ/mol (set as a FreeRotor)
* Invalidated! pivots: [8, 9], dihedral: [2, 8, 9, 18], invalidation reason: Another conformer for S47 exists which is 1.69 kJ/mol lower.Another conformer for S47 exists which is 1.69 kJ/mol lower.
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
C       2.71461100    0.75376100   -0.39104400
C       1.56379400    0.06717300   -0.28194300
C       1.40413600   -1.31759400   -0.64706200
C       0.32991000   -2.07512900   -0.57609000
C      -0.95579000   -1.46467200   -0.05937800
C      -0.84699400   -0.01088600    0.33208200
C      -2.11402500    0.61640300    0.85756100
C       0.31502400    0.66931000    0.24018600
O       0.47176600    1.98020300    0.60680200
H       2.77558100    1.79113200   -0.09450800
H       3.60379100    0.27506000   -0.78055500
H       0.31858100   -3.11952400   -0.87364800
H      -1.31361400   -2.05209500    0.80128500
H      -1.74133900   -1.57900800   -0.82270800
H      -2.26534400    0.40845300    1.92436400
H      -2.98669800    0.21988900    0.33020900
H      -2.14587500    1.70301200    0.72436200
H      -0.33984100    2.29663300    1.01491600
""",
)

entry(
    index = 46,
    label = "S48",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {2,S} {6,D}
4  C u0 p0 c0 {6,S} {7,S} {8,D}
5  C u0 p0 c0 {1,S} {7,D} {14,S}
6  C u0 p0 c0 {3,D} {4,S} {15,S}
7  C u0 p0 c0 {4,S} {5,D} {16,S}
8  C u0 p0 c0 {4,D} {17,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 O u1 p2 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7186,0.032728,6.92786e-05,-1.1886e-07,5.2088e-11,6048,13.1077], Tmin=(10,'K'), Tmax=(795.411,'K')),
            NASAPolynomial(coeffs=[2.5969,0.0637317,-3.70184e-05,1.03196e-08,-1.11339e-12,5424.12,13.219], Tmin=(795.411,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (50.298,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 9}
1D rotors:
pivots: [6, 7], dihedral: [5, 6, 7, 16], rotor symmetry: 3, max scan energy: 2.03 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       2.33316900   -1.63991400   -0.01883900
C       1.39669100   -0.67859000    0.00028500
C       1.72661400    0.74293000    0.06503500
C       0.80061100    1.70668400    0.08448000
C      -0.67057100    1.42356400    0.04168800
C      -1.04546600   -0.02251600   -0.02501900
C      -2.49149000   -0.37813800   -0.07021500
C      -0.05505400   -1.07382400   -0.04664700
O      -0.39050400   -2.26563000   -0.10218300
H       3.38999500   -1.40044000    0.01336600
H       2.04087200   -2.68092700   -0.06733500
H       2.78034300    1.00432300    0.09806500
H       1.09873500    2.74904900    0.13315600
H      -1.16410300    1.87938800    0.91650200
H      -1.12730500    1.94964900   -0.81346100
H      -2.97823800    0.07928000   -0.94121300
H      -2.61854600   -1.45801200   -0.11681400
H      -3.01553800    0.00793900    0.81358900
""",
)

entry(
    index = 47,
    label = "S49",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {4,D} {7,S}
4  C u0 p0 c0 {2,S} {3,D} {6,S}
5  C u0 p0 c0 {6,S} {8,S} {9,D}
6  C u0 p0 c0 {4,S} {5,S} {16,D}
7  C u0 p0 c0 {3,S} {8,D} {18,S}
8  C u0 p0 c0 {5,S} {7,D} {17,S}
9  C u0 p0 c0 {5,D} {19,S} {20,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 O u0 p2 c0 {6,D}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55382,0.052294,1.98052e-05,-5.50337e-08,2.27511e-11,-5403.23,14.2786], Tmin=(10,'K'), Tmax=(952.94,'K')),
            NASAPolynomial(coeffs=[6.65659,0.063023,-3.44718e-05,9.09475e-09,-9.34842e-13,-7073.07,-6.19973], Tmin=(952.94,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-44.8957,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (482.239,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-H': 10, 'C-C': 6, 'C=C': 3}
1D rotors:
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 15], invalidation reason: Another conformer for S49 exists which is 0.56 kJ/mol lower.Another conformer for S49 exists which is 0.56 kJ/mol lower.
* Invalidated! pivots: [7, 8], dihedral: [5, 7, 8, 18], invalidation reason: Another conformer for S49 exists which is 0.56 kJ/mol lower.Another conformer for S49 exists which is 0.56 kJ/mol lower.


External symmetry: 1, optical isomers: 1

Geometry:
C       3.22213900    0.05683400    0.31066100
C       1.90768700   -0.16605600    0.13504300
C       1.37026200   -1.46183100   -0.23134200
C       0.04519000   -1.62693200   -0.39379800
C      -0.91643200   -0.53939700   -0.21644700
C      -2.35514300   -0.92868300   -0.44422100
C      -0.50001500    0.71208400    0.12797300
C      -1.38191200    1.91188000    0.34012800
C       0.94347800    0.97932200    0.32629800
O       1.34167000    2.09534700    0.63588100
H       3.56949900    1.04561300    0.58446300
H       3.95327100   -0.73395100    0.18464700
H       2.05846500   -2.28920600   -0.37026700
H      -0.34956900   -2.59982600   -0.66808400
H      -2.63979000   -1.73518900    0.24046700
H      -2.48308600   -1.31954100   -1.45966800
H      -3.05543400   -0.10840100   -0.30823100
H      -1.24463800    2.30707400    1.35071200
H      -1.08961600    2.71949900   -0.33709100
H      -2.43860400    1.69928300    0.19111700
""",
)









entry(
    index = 48,
    label = "S50",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {11,S} {12,S}
2  C u0 p0 c0 {7,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {4,S} {7,D} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {1,S} {4,D} {10,S}
6  C u0 p0 c0 {1,S} {8,D} {16,S}
7  C u0 p0 c0 {2,S} {3,D} {17,S}
8  C u0 p0 c0 {3,S} {6,D} {18,S}
9  C u1 p0 c0 {4,S} {19,S} {20,S}
10 O u0 p2 c0 {5,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64307,0.0338109,0.000229024,-6.90452e-07,6.60625e-10,5935.41,14.7028], Tmin=(10,'K'), Tmax=(266.76,'K')),
            NASAPolynomial(coeffs=[0.287736,0.0841227,-5.38783e-05,1.6547e-08,-1.94756e-12,6114.43,26.4567], Tmin=(266.76,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (49.3833,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-H': 10, 'H-O': 1, 'C-C': 6, 'C=C': 3}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [11, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [3, 4], dihedral: [2, 3, 4, 13], rotor symmetry: 1, max scan energy: 20.02 kJ/mol
pivots: [9, 10], dihedral: [8, 9, 10, 19], rotor symmetry: 3, max scan energy: 1.85 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.28760900   -2.23652400    0.22168900
C      -0.52250300   -0.86502200    0.17649100
C      -1.15202600   -0.21004300    1.24080800
O      -1.67740800   -0.87269500    2.30580800
C      -1.29088500    1.26600400    1.38763400
C      -0.65180900    2.02590100    0.26998800
C      -0.12552900    1.42472900   -0.80180100
C      -0.10506400   -0.02755100   -0.99497900
C       0.25512300   -0.58656500   -2.17007700
C       0.70065000    0.09769200   -3.42772200
H       0.21322800   -2.76277200   -0.57601200
H      -0.50597800   -2.83355200    1.09953900
H      -1.71079000   -1.81561900    2.10768800
H      -2.35824400    1.52526300    1.46855400
H      -0.86140500    1.56407700    2.35622600
H      -0.64266200    3.10814300    0.34736200
H       0.30241600    2.04088200   -1.58265700
H       0.20931100   -1.66758000   -2.25301800
H       1.68945700   -0.26507900   -3.73256100
H       0.75649600    1.18268700   -3.34571700
H       0.01916700   -0.13623000   -4.25444600
""",
)

entry(
    index = 49,
    label = "S51",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,S} {9,D}
4  C u0 p0 c0 {3,S} {6,D} {7,S}
5  C u1 p0 c0 {1,S} {8,S} {16,S}
6  C u0 p0 c0 {2,S} {4,D} {15,S}
7  C u0 p0 c0 {4,S} {8,D} {17,S}
8  C u0 p0 c0 {5,S} {7,D} {18,S}
9  C u0 p0 c0 {3,D} {19,S} {20,S}
10 O u0 p2 c0 {1,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73477,0.0196328,0.000302022,-7.55758e-07,5.84196e-10,6740.01,15.1115], Tmin=(10,'K'), Tmax=(415.516,'K')),
            NASAPolynomial(coeffs=[0.753358,0.0832081,-5.33795e-05,1.64496e-08,-1.9424e-12,6686.71,23.254], Tmin=(415.516,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (56.0362,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-H': 10, 'H-O': 1, 'C-C': 6, 'C=C': 3}
1D rotors:
pivots: [4, 5], dihedral: [3, 4, 5, 14], rotor symmetry: 3, max scan energy: 1.22 kJ/mol
pivots: [9, 10], dihedral: [2, 9, 10, 21], rotor symmetry: 1, max scan energy: 18.38 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.41527700   -2.11155500    0.35746700
C      -0.53872500   -0.87454200   -0.13023900
C       0.58785800    0.11017000   -0.15306100
C       1.87490800   -0.32005800   -0.33946800
C       3.12155200    0.50644800   -0.33506200
C       0.22937800    1.47875400    0.04665800
C      -1.11808800    1.89449100    0.08621600
C      -2.14500500    1.04467700   -0.21251000
C      -1.88496200   -0.37371300   -0.64736300
O      -2.97283400   -1.23347500   -0.31891000
H      -1.25293400   -2.79691900    0.34355600
H       0.51729400   -2.46722800    0.77827200
H       2.02039500   -1.37801400   -0.53551500
H       3.83535300    0.12005700    0.40243400
H       3.62638700    0.45213100   -1.30733100
H       2.94743400    1.55857700   -0.11018300
H       1.00692600    2.22059700    0.17373700
H      -1.33474800    2.93162500    0.32262100
H      -3.17780600    1.37403000   -0.22931800
H      -1.85773300   -0.39530900   -1.74774500
H      -3.04921800   -1.23275100    0.64286800
""",
)

entry(
    index = 50,
    label = "S52",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {7,D}
3  C u0 p0 c0 {2,S} {5,S} {8,D}
4  C u1 p0 c0 {1,S} {6,S} {11,S}
5  C u0 p0 c0 {3,S} {6,D} {12,S}
6  C u0 p0 c0 {4,S} {5,D} {13,S}
7  C u0 p0 c0 {2,D} {16,S} {17,S}
8  C u0 p0 c0 {3,D} {14,S} {15,S}
9  O u0 p2 c0 {1,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78554,0.0130323,0.000243253,-5.05566e-07,3.15005e-10,10847.8,13.3396], Tmin=(10,'K'), Tmax=(538.397,'K')),
            NASAPolynomial(coeffs=[2.46592,0.069822,-4.58707e-05,1.45303e-08,-1.76289e-12,10308.9,12.5648], Tmin=(538.397,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (90.1177,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 8}
1D rotors:
pivots: [6, 7], dihedral: [5, 6, 7, 16], rotor symmetry: 1, max scan energy: 18.50 kJ/mol
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
C       2.36655000   -0.56637500   -0.57519500
C       1.11714200   -0.32376300   -0.08721800
C       0.00445500   -0.11919700   -0.96141000
C      -1.26521200    0.24833000   -0.47395700
C      -1.46377500    0.57193900    0.83938900
C      -0.32212900    0.61166500    1.82140900
O      -0.76033500    0.34872100    3.15127200
C       0.83408500   -0.28245800    1.37878600
C       1.50904500   -1.01619300    2.26684800
H       3.22409700   -0.67266600    0.07587800
H       2.53929500   -0.63804500   -1.64273800
H       0.15321200   -0.25729500   -2.02644700
H      -2.09493100    0.30919100   -1.17113700
H      -2.42968700    0.89480100    1.21102900
H       0.04806300    1.64736300    1.86862000
H      -1.10989600   -0.55051100    3.15894400
H       2.30051400   -1.68999700    1.96227000
H       1.27741900   -0.95683000    3.32250300
""",
)

entry(
    index = 51,
    label = "S53",
    molecule = 
"""
1  O u0 p2 c0 {9,D}
2  C u0 p0 c0 {3,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {6,S} {7,D}
5  C u0 p0 c0 {8,S} {9,S} {10,D}
6  C u0 p0 c0 {4,S} {8,D} {17,S}
7  C u0 p0 c0 {4,D} {9,S} {18,S}
8  C u0 p0 c0 {5,S} {6,D} {16,S}
9  C u0 p0 c0 {1,D} {5,S} {7,S}
10 C u0 p0 c0 {5,D} {19,S} {20,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5677,0.0389095,9.06708e-05,-1.79834e-07,9.30163e-11,-3736.72,14.0305], Tmin=(10,'K'), Tmax=(655.137,'K')),
            NASAPolynomial(coeffs=[1.52568,0.0748281,-4.52617e-05,1.31293e-08,-1.4682e-12,-3972.42,19.1775], Tmin=(655.137,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-31.122,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (473.925,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-H': 10, 'C-C': 6, 'C=C': 3}
1D rotors:
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 10.70 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 17], rotor symmetry: 3, max scan energy: 15.29 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       3.51960200    0.17821000   -0.42141300
C       2.20586000    0.08726600   -0.15107700
C       1.34097200    1.25171300   -0.05503100
C       0.02840400    1.12367700    0.21755100
C      -0.59127000   -0.18312800    0.42964100
C      -2.07283800   -0.18329900    0.72766000
C      -2.73016700   -1.54384800    0.95092100
C       0.15939900   -1.30833600    0.35394400
C       1.59467600   -1.27990600    0.06334500
O       2.26454800   -2.30175900   -0.00301600
H       4.00336700    1.13516400   -0.58275500
H       4.11885300   -0.72239700   -0.48168300
H       1.78216000    2.23137100   -0.20932900
H      -0.60390600    2.00292500    0.28589900
H      -2.23451300    0.45397700    1.60733000
H      -2.57707200    0.34001300   -0.09573000
H      -2.28646300   -2.06952600    1.80024400
H      -2.63425800   -2.18523100    0.07115400
H      -3.79568600   -1.41898100    1.15688700
H      -0.26131500   -2.29443400    0.50455400
""",
)

entry(
    index = 52,
    label = "S57",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {16,S}
2  C u0 p0 c0 {4,B} {5,B} {8,S}
3  C u0 p0 c0 {1,S} {4,B} {6,B}
4  C u0 p0 c0 {2,B} {3,B} {13,S}
5  C u0 p0 c0 {2,B} {7,B} {10,S}
6  C u0 p0 c0 {3,B} {7,B} {12,S}
7  C u0 p0 c0 {5,B} {6,B} {11,S}
8  C u0 p0 c0 {2,S} {9,D} {14,S}
9  C u1 p0 c0 {8,D} {15,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79483,0.0136297,0.000233133,-5.39966e-07,3.78008e-10,24628,13.6657], Tmin=(10,'K'), Tmax=(473.038,'K')),
            NASAPolynomial(coeffs=[2.24154,0.0636628,-4.25261e-05,1.3426e-08,-1.60717e-12,24362.2,15.6331], Tmin=(473.038,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (204.731,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (374.151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 4, 'C=C': 4, 'C-H': 6}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 20.46 kJ/mol
pivots: [7, 8], dihedral: [6, 7, 8, 15], rotor symmetry: 1, max scan energy: 17.42 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       3.04752000    0.48159500   -0.06825100
C       2.15247500   -0.47780100    0.00146400
C       0.68517700   -0.33767200    0.01176600
C      -0.11787600   -1.48069000    0.09221100
C      -1.50685000   -1.36129400    0.10289700
C      -2.11371000   -0.11493400    0.03437200
C      -1.31527600    1.03182500   -0.04631600
O      -1.95788200    2.23573000   -0.11185400
C       0.07079500    0.92154700   -0.05750700
H       4.12213200    0.57390700   -0.08759800
H       2.51674700   -1.51032600    0.05952400
H       0.34526100   -2.45944300    0.14619300
H      -2.12313500   -2.25110200    0.16542400
H      -3.19095600   -0.00411300    0.04153700
H      -1.30404100    2.94060100   -0.16367100
H       0.68962000    1.81217000   -0.12019300
""",
)

entry(
    index = 53,
    label = "S60",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {10,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {8,D} {9,S}
5  C u0 p0 c0 {1,D} {2,S} {6,S}
6  C u0 p0 c0 {5,S} {7,D} {14,S}
7  C u0 p0 c0 {6,D} {9,S} {15,S}
8  C u0 p0 c0 {4,D} {16,S} {17,S}
9  C u2 p0 c0 {4,S} {7,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82759,0.0115445,0.000241808,-5.45026e-07,3.80105e-10,31044,14.6285], Tmin=(10,'K'), Tmax=(459.71,'K')),
            NASAPolynomial(coeffs=[0.673936,0.0692123,-4.49878e-05,1.39135e-08,-1.64167e-12,31014.6,23.9183], Tmin=(459.71,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (258.088,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 6, 'C=C': 2, 'C-H': 8, 'C=O': 1}
1D rotors:
pivots: [8, 9], dihedral: [2, 8, 9, 15], rotor symmetry: 3, max scan energy: 15.68 kJ/mol
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.03375100    1.15636600   -0.65686000
C      -0.75109000    0.75595400   -0.46855500
C       0.32109200    1.15389700   -1.28872600
C       1.67306700    0.98597100   -1.06454100
C       2.09601700    0.36683200    0.10324500
C       1.13326200   -0.15506000    1.06940000
O       1.48340200   -0.61604500    2.14574900
C      -0.35678100   -0.19191400    0.67463400
C      -0.70884400   -1.65543100    0.31932100
H      -2.82454100    0.84767800    0.01682800
H      -2.30174900    1.79989400   -1.48538100
H       2.39993300    1.35719800   -1.78107600
H       3.14617900    0.26471600    0.35046200
H      -0.91636900    0.08696000    1.57178500
H      -0.17567700   -1.97996300   -0.57817800
H      -1.78003600   -1.75582500    0.13360300
H      -0.42798500   -2.30855700    1.14772800
""",
)

entry(
    index = 54,
    label = "S61",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {3,S} {4,S} {6,D}
3  C u0 p0 c0 {1,S} {2,S} {8,D}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {7,S} {12,S}
6  C u0 p0 c0 {2,D} {16,S} {17,S}
7  C u1 p0 c0 {5,S} {14,S} {15,S}
8  C u0 p0 c0 {3,D} {18,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41338,0.0616076,-3.08914e-05,3.65454e-09,1.09305e-12,16538.4,14.4467], Tmin=(10,'K'), Tmax=(1274.32,'K')),
            NASAPolynomial(coeffs=[13.4206,0.0411873,-1.9793e-05,4.61713e-09,-4.23725e-13,13095.5,-39.7599], Tmin=(1274.32,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (137.48,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 4, 'C=C': 3, 'C-H': 9, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Another conformer for S61 exists which is 2.97 kJ/mol lower.Another conformer for S61 exists which is 2.97 kJ/mol lower.
* Invalidated! pivots: [4, 6], dihedral: [3, 4, 6, 7], invalidation reason: 
pivots: [6, 7], dihedral: [4, 6, 7, 16], rotor symmetry: 3, max scan energy: 4.49 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for S61 exists which is 2.09 kJ/mol lower.Another conformer for S61 exists which is 2.09 kJ/mol lower.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 14], invalidation reason: Another conformer for S61 exists which is 2.00 kJ/mol lower.Another conformer for S61 exists which is 2.00 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
C       2.84797300    1.03977500   -0.48645800
C       1.60510500    0.51496100   -0.68979400
C       0.40535200    1.12113700   -0.26736500
C      -0.91055500    0.60531800   -0.46486600
C      -1.99006200    1.18160100    0.14265400
C      -1.11202000   -0.57629100   -1.37126400
C      -0.89037100   -0.46026900   -2.87008400
C      -1.56858500   -1.69226900   -0.84841300
O      -1.95749900   -2.68978300   -0.38748000
H       3.74028300    0.52319000   -0.81650700
H       2.98395200    1.99128200    0.01667100
H       1.52661700   -0.44543000   -1.19235700
H       0.48152600    2.05633700    0.28261300
H      -1.86794200    2.02579400    0.81266800
H      -2.99393800    0.81208500   -0.02102600
H       0.13131400   -0.14343800   -3.09513100
H      -1.57093200    0.28220900   -3.29898000
H      -1.06607700   -1.41160600   -3.37608200
""",
)

entry(
    index = 55,
    label = "S63",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {8,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {4,S} {6,S} {7,D}
4  C u0 p0 c0 {2,S} {3,S} {9,D}
5  C u0 p0 c0 {1,S} {6,D} {15,S}
6  C u0 p0 c0 {3,S} {5,D} {16,S}
7  C u0 p0 c0 {3,D} {17,S} {18,S}
8  O u0 p2 c0 {1,S} {9,S}
9  C u1 p0 c0 {4,D} {8,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76854,0.0183533,0.000197076,-4.35209e-07,2.95376e-10,29800.7,13.6009], Tmin=(10,'K'), Tmax=(459.369,'K')),
            NASAPolynomial(coeffs=[-0.0909612,0.0723478,-4.58072e-05,1.38927e-08,-1.61624e-12,29940.2,26.8771], Tmin=(459.369,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (247.753,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 4, 'C=C': 3, 'C-H': 9}
1D rotors:
pivots: [8, 9], dihedral: [2, 8, 9, 16], rotor symmetry: 3, max scan energy: 12.53 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.79520300    1.26039500    0.29166200
C      -0.60749500    0.64917700    0.08318400
C       0.59995600    1.38858900    0.48698600
C       1.86555100    0.96306300    0.59968100
C       2.35834300   -0.41894500    0.31012300
O       1.85831800   -0.91059500   -0.97889100
C       0.58705000   -1.21111400   -1.02713300
C      -0.54140800   -0.70213000   -0.52149900
C      -1.82096400   -1.48914900   -0.70411800
H      -1.83652200    2.25601600    0.71764300
H      -2.74144400    0.79386000    0.05614800
H       0.41081200    2.42649400    0.74665400
H       2.61717900    1.67437700    0.92776700
H       2.04498600   -1.14022400    1.07229700
H       3.44280200   -0.44704200    0.21667400
H      -2.51616700   -0.97863000   -1.37940100
H      -1.60279400   -2.46909200   -1.12896800
H      -2.33592500   -1.63324900    0.25115700
""",
)

entry(
    index = 56,
    label = "S64",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {6,S} {7,D}
5  C u0 p0 c0 {2,S} {6,D} {14,S}
6  C u0 p0 c0 {4,S} {5,D} {15,S}
7  C u0 p0 c0 {4,D} {16,S} {17,S}
8  C u1 p0 c0 {1,S} {18,D}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51597,0.0454695,2.91369e-05,-7.47208e-08,3.53555e-11,11909.8,14.1007], Tmin=(10,'K'), Tmax=(786.29,'K')),
            NASAPolynomial(coeffs=[4.1662,0.0606949,-3.52644e-05,9.85966e-09,-1.06788e-12,11234.7,7.47694], Tmin=(786.29,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (98.9917,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (424.038,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 6, 'C=C': 2, 'C-H': 9, 'C=O': 1}
1D rotors:
pivots: [6, 7], dihedral: [2, 6, 7, 16], rotor symmetry: 3, max scan energy: 13.71 kJ/mol
pivots: [6, 8], dihedral: [2, 6, 8, 9], rotor symmetry: 1, max scan energy: 6.65 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.67146500    2.13930700   -0.13733300
C       0.08656200    1.03760100   -0.10961200
C       1.54471400    0.96737700   -0.09795000
C       1.98126400   -0.29794500   -0.08893200
C       0.85295600   -1.29298200   -0.08903900
C      -0.43679300   -0.41122200   -0.10892000
C      -1.38381900   -0.69954200    1.06400500
C      -1.21813000   -0.57724300   -1.43399600
O      -0.88312700   -1.11474400   -2.42773400
H      -1.75306700    2.09050000   -0.16780900
H      -0.22226300    3.12588800   -0.13809400
H       2.17107400    1.85117800   -0.10079000
H       3.02221400   -0.59852800   -0.08644700
H       0.87685700   -1.93341800    0.80008300
H       0.89651100   -1.95537500   -0.95891800
H      -2.26013100   -0.05009000    1.02850100
H      -0.86358400   -0.52685200    2.00904900
H      -1.72680400   -1.73804600    1.04206000
""",
)

entry(
    index = 57,
    label = "S65",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {2,S} {6,D}
5  C u0 p0 c0 {2,S} {7,D} {13,S}
6  C u0 p0 c0 {4,D} {16,S} {17,S}
7  C u0 p0 c0 {5,D} {14,S} {15,S}
8  C u1 p0 c0 {1,S} {18,D}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.30939,0.0614579,-2.58354e-05,-5.85002e-09,5.597e-12,29372.5,14.5729], Tmin=(10,'K'), Tmax=(979.85,'K')),
            NASAPolynomial(coeffs=[8.35527,0.052005,-2.84268e-05,7.52192e-09,-7.76613e-13,27848.6,-12.3981], Tmin=(979.85,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (244.164,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (424.038,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 6, 'C=C': 2, 'C-H': 9, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for S65 exists which is 2.51 kJ/mol lower.Another conformer for S65 exists which is 2.51 kJ/mol lower.
pivots: [6, 7], dihedral: [3, 6, 7, 16], rotor symmetry: 3, max scan energy: 6.86 kJ/mol
pivots: [6, 8], dihedral: [3, 6, 8, 9], rotor symmetry: 1, max scan energy: 19.36 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       2.33177400   -1.25418500   -0.75965600
C       1.16373100   -0.61576500   -0.80832900
C       0.00164500   -0.86500100    0.08010200
C      -0.12187800   -2.02280700    0.95347300
C       0.28746800   -2.69354800    2.01348400
C      -1.03307200   -2.04365500   -0.21212000
C      -0.83293300   -3.03311300   -1.34200000
C      -2.45420800   -1.67787600    0.08746200
O      -2.89136300   -0.78994200    0.73447100
H       3.13023700   -1.01612800   -1.45270000
H       2.52711200   -2.02927500   -0.02652700
H       1.01392100    0.16590700   -1.54967300
H      -0.52753100    0.03027500    0.40438500
H       1.07899700   -2.30932600    2.64780200
H      -0.15857600   -3.64286300    2.28889800
H       0.22794300   -3.17908800   -1.54539300
H      -1.31654000   -2.68047000   -2.25678300
H      -1.26974500   -3.99983400   -1.07913500
""",
)

entry(
    index = 58,
    label = "S66",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,S} {7,D}
4  C u0 p0 c0 {2,S} {3,S} {8,D}
5  C u0 p0 c0 {6,D} {7,S} {15,S}
6  C u0 p0 c0 {5,D} {16,S} {17,S}
7  C u1 p0 c0 {3,D} {5,S}
8  C u0 p0 c0 {4,D} {18,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.15529,0.0733205,-6.58102e-05,3.77399e-08,-1.03289e-11,24457.7,17.1606], Tmin=(10,'K'), Tmax=(754.862,'K')),
            NASAPolynomial(coeffs=[6.15057,0.0574484,-3.42702e-05,9.88461e-09,-1.10358e-12,24005.5,3.55244], Tmin=(754.862,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (203.267,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (415.724,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 4, 'C=C': 3, 'C-H': 9, 'C=O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 0.04 kJ/mol (set as a FreeRotor)
pivots: [4, 5], dihedral: [3, 4, 5, 13], rotor symmetry: 3, max scan energy: 6.64 kJ/mol
pivots: [4, 6], dihedral: [3, 4, 6, 7], rotor symmetry: 1, max scan energy: 19.10 kJ/mol
pivots: [6, 7], dihedral: [4, 6, 7, 16], rotor symmetry: 3, max scan energy: 6.67 kJ/mol
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
C       2.82641300   -0.85852300    0.29728100
C       1.77872800   -1.31503500   -0.49972700
C       1.89962700   -2.11952600   -1.57867000
C       2.01329500   -2.87033400   -2.64806400
C       2.20372500   -2.25308000   -4.02438400
C       1.95992900   -4.34701700   -2.55601700
C       1.76991200   -5.03445800   -1.21808900
C       2.07860600   -5.09006200   -3.63990100
O       2.18162300   -5.76154000   -4.58685500
H       2.63420400   -0.21424100    1.14536100
H       3.85181700   -1.13493800    0.08652000
H       0.77073800   -0.99525000   -0.23032000
H       3.13946700   -2.59786400   -4.47674500
H       1.38423300   -2.53864700   -4.69229000
H       2.23313000   -1.16607900   -3.96242900
H       0.82486600   -4.72288300   -0.76371900
H       1.75977500   -6.12115600   -1.31652700
H       2.57823500   -4.75938600   -0.53426100
""",
)

entry(
    index = 59,
    label = "S67",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u0 p0 c0 {2,S} {6,D} {8,S}
4  C u0 p0 c0 {2,D} {5,S} {13,S}
5  C u0 p0 c0 {4,S} {7,D} {12,S}
6  C u0 p0 c0 {3,D} {16,S} {17,S}
7  C u0 p0 c0 {5,D} {14,S} {15,S}
8  C u1 p0 c0 {3,S} {18,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84511,0.0204167,0.000739367,-5.10064e-06,1.1721e-08,20167.2,12.4662], Tmin=(10,'K'), Tmax=(136.97,'K')),
            NASAPolynomial(coeffs=[3.08293,0.0672334,-4.22822e-05,1.28497e-08,-1.50419e-12,20165,13.7871], Tmin=(136.97,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (171.628,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (432.353,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 4, 'C=C': 3, 'C-H': 9, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for S67 exists which is 2.77 kJ/mol lower.Another conformer for S67 exists which is 2.77 kJ/mol lower.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 14], invalidation reason: Another conformer for S67 exists which is 2.84 kJ/mol lower.Another conformer for S67 exists which is 2.84 kJ/mol lower.
* Invalidated! pivots: [4, 6], dihedral: [3, 4, 6, 7], invalidation reason: 
* Invalidated! pivots: [6, 8], dihedral: [4, 6, 8, 9], invalidation reason: 
* Invalidated! pivots: [6, 7], dihedral: [4, 6, 7, 17], invalidation reason: Another conformer for S67 exists which is 2.82 kJ/mol lower.Another conformer for S67 exists which is 2.82 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
C       2.88017300   -1.12125400    0.47606800
C       1.62776700   -0.88002500    0.06896700
C       0.92635600    0.36455100    0.33317600
C      -0.33797600    0.68734900   -0.00622400
C      -0.89767300    2.06239600    0.25616000
C      -1.27860500   -0.30677700   -0.62593100
C      -1.54211600   -1.58105400   -0.06568800
C      -1.90070800    0.10355400   -1.74693900
O      -2.42050300    0.47033000   -2.72241300
H       3.44144900   -0.39286300    1.05333200
H       3.38178400   -2.05309100    0.24462600
H       1.09904300   -1.63691100   -0.50143000
H       1.50663400    1.12793100    0.84808700
H      -1.76868200    2.01026700    0.91802600
H      -1.23587600    2.54072200   -0.67090800
H      -0.15044300    2.71431600    0.71196300
H      -1.11422100   -1.83077100    0.89334500
H      -2.21826900   -2.27905600   -0.53916500
""",
)

entry(
    index = 60,
    label = "S68",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u1 p0 c0 {1,S} {2,S} {4,S}
4  C u0 p0 c0 {3,S} {6,S} {7,D}
5  C u0 p0 c0 {1,S} {6,D} {13,S}
6  C u0 p0 c0 {4,S} {5,D} {14,S}
7  C u0 p0 c0 {4,D} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92101,0.00493432,0.000186694,-3.56395e-07,2.17149e-10,22384.8,12.343], Tmin=(10,'K'), Tmax=(486.864,'K')),
            NASAPolynomial(coeffs=[-1.80643,0.0654558,-4.12564e-05,1.25478e-08,-1.47022e-12,22782.9,34.2131], Tmin=(486.864,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (186.095,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 5, 'C=C': 2, 'C-H': 9}
1D rotors:
pivots: [6, 7], dihedral: [2, 6, 7, 14], rotor symmetry: 3, max scan energy: 1.09 kJ/mol
* Invalidated! pivots: [1, 2], dihedral: [8, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 1

Geometry:
C       2.10008700   -0.35089700    0.53759600
C       0.87097400    0.21373300    0.26634100
C       0.56751000    1.65962600    0.36032300
C      -0.70951900    1.89552600    0.03528400
C      -1.40142700    0.60218100   -0.31590500
C      -0.31768400   -0.42946700   -0.14249500
C      -0.53359600   -1.88407500   -0.38156400
H       2.27061400   -1.41665500    0.45358400
H       2.93859200    0.26103800    0.84548800
H       1.29978000    2.40143500    0.65475700
H      -1.19951200    2.86026000    0.01826700
H      -2.26627500    0.40618700    0.33581000
H      -1.80128300    0.61278000   -1.34114300
H       0.37087300   -2.46790000   -0.20270600
H      -0.85564200   -2.07759000   -1.41307000
H      -1.32198700   -2.28479600    0.26884300
""",
)

entry(
    index = 61,
    label = "S69",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {5,D}
4  C u0 p0 c0 {3,S} {6,D} {7,S}
5  C u0 p0 c0 {1,S} {3,D} {14,S}
6  C u0 p0 c0 {1,S} {4,D} {13,S}
7  C u1 p0 c0 {4,S} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89302,0.00667565,0.000192733,-3.8196e-07,2.37761e-10,22296.9,11.3519], Tmin=(10,'K'), Tmax=(499.862,'K')),
            NASAPolynomial(coeffs=[-0.51238,0.0629856,-3.94321e-05,1.19538e-08,-1.39919e-12,22474.3,26.9192], Tmin=(499.862,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (185.355,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 5, 'C=C': 2, 'C-H': 9}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [8, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [6, 7], dihedral: [2, 6, 7, 14], rotor symmetry: 3, max scan energy: 8.18 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -0.05667900    2.13012000   -0.37598600
C      -0.29808100    0.78873200   -0.15093200
C       0.65093100   -0.22086600    0.06622400
C      -0.03644900   -1.53681100    0.26797400
C      -1.49279300   -1.16824100    0.14180700
C      -1.64163000    0.14547200   -0.09488000
C      -2.92276500    0.89713400   -0.28083200
H      -0.86293400    2.83501000   -0.53366900
H       0.95457000    2.51734700   -0.40117600
H       1.72315800   -0.07829600    0.08651900
H       0.26849200   -2.28577800   -0.47804500
H       0.19564100   -1.98335400    1.24634900
H      -2.29847800   -1.88624000    0.23369100
H      -2.95743400    1.38361800   -1.26171000
H      -3.03058900    1.68736300    0.47010100
H      -3.78552600    0.23317400   -0.20082300
""",
)

entry(
    index = 62,
    label = "S70",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u0 p0 c0 {2,S} {5,S} {7,D}
4  C u0 p0 c0 {2,D} {6,S} {13,S}
5  C u0 p0 c0 {3,S} {6,D} {11,S}
6  C u0 p0 c0 {4,S} {5,D} {12,S}
7  C u0 p0 c0 {3,D} {14,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92268,0.00493005,0.000178409,-3.5207e-07,2.22088e-10,19706.9,10.9637], Tmin=(10,'K'), Tmax=(472.689,'K')),
            NASAPolynomial(coeffs=[-0.992978,0.0597226,-3.73388e-05,1.12696e-08,-1.31157e-12,20024.2,29.4362], Tmin=(472.689,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (163.834,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (353.365,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 4, 'C=C': 3, 'C-H': 8}
1D rotors:
pivots: [6, 7], dihedral: [2, 6, 7, 13], rotor symmetry: 3, max scan energy: 5.29 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -0.10878000    2.02693500    0.21546500
C       0.29801200    0.77639800   -0.04203800
C       1.47572700    0.38108500   -0.83679700
C       1.52851800   -0.96682000   -0.85210700
C       0.39633000   -1.50227600   -0.07408900
C      -0.34564500   -0.48215000    0.41484300
C      -1.58103200   -0.55729600    1.25600200
H       0.43223100    2.88618900   -0.16552300
H      -0.99126900    2.22922200    0.81243100
H       2.15555300    1.07537800   -1.30965400
H       2.27221700   -1.57607100   -1.34848700
H       0.20015700   -2.55653400    0.07540100
H      -2.43610900   -0.07987700    0.76478600
H      -1.44554600   -0.05762800    2.22158600
H      -1.85036300   -1.59655700    1.45500800
""",
)

entry(
    index = 63,
    label = "S71",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {4,D} {7,S}
4  C u0 p0 c0 {2,S} {3,D} {6,S}
5  C u0 p0 c0 {1,S} {6,D} {13,S}
6  C u0 p0 c0 {4,S} {5,D} {14,S}
7  C u1 p0 c0 {3,S} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92247,0.00492389,0.000190026,-3.69796e-07,2.30615e-10,19490.8,12.1835], Tmin=(10,'K'), Tmax=(472.725,'K')),
            NASAPolynomial(coeffs=[-1.68073,0.0649969,-4.07659e-05,1.23391e-08,-1.43951e-12,19879,33.5212], Tmin=(472.725,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (162.036,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 5, 'C=C': 2, 'C-H': 9}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [8, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [3, 4], dihedral: [2, 3, 4, 10], rotor symmetry: 3, max scan energy: 2.46 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -0.50700200    1.62226900   -1.12492100
C      -0.48730600    0.50310900   -0.35630900
C       0.66690800   -0.18582900    0.14348200
C       2.08472900    0.21839100   -0.10088100
C       0.23471400   -1.30652900    0.90260800
C      -1.13148700   -1.39129600    0.92891600
C      -1.71631000   -0.25511300    0.13543500
H      -1.43824500    2.06889300   -1.45319500
H       0.40850000    2.10988300   -1.43824400
H       2.28466700    1.22783500    0.27770700
H       2.31848600    0.23278200   -1.17206300
H       2.78344500   -0.46569700    0.38494300
H       0.91064300   -1.99781600    1.39285400
H      -1.71742300   -2.14679600    1.43379400
H      -2.33123000   -0.61059800   -0.70048400
H      -2.36501600    0.38334900    0.74764700
""",
)

entry(
    index = 64,
    label = "S72",
    molecule = 
"""
1  O u0 p2 c0 {4,D}
2  C u0 p0 c0 {3,S} {4,S} {8,D}
3  C u0 p0 c0 {2,S} {5,D} {9,S}
4  C u0 p0 c0 {1,D} {2,S} {7,S}
5  C u0 p0 c0 {3,D} {6,S} {10,S}
6  C u0 p0 c0 {5,S} {7,D} {11,S}
7  C u0 p0 c0 {4,S} {6,D} {12,S}
8  C u0 p0 c0 {2,D} {13,S} {14,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90241,0.00572232,0.000164518,-3.02261e-07,1.71719e-10,4650.39,11.2574], Tmin=(10,'K'), Tmax=(553.223,'K')),
            NASAPolynomial(coeffs=[-0.727624,0.0601609,-3.99216e-05,1.25914e-08,-1.51265e-12,4841.9,27.9546], Tmin=(553.223,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (38.6252,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 4, 'C=C': 3, 'C-H': 6, 'C=O': 1}

External symmetry: 1, optical isomers: 1

Geometry:
C      -2.22060300   -0.55557200   -0.10908100
C      -0.91114900   -0.25422600   -0.04249100
C       0.11662500   -1.27107700    0.11793300
C       1.42233300   -0.93799900    0.18152000
C       1.83593300    0.44999600    0.09099100
C       0.94834400    1.45724000   -0.05869100
C      -0.49456800    1.19899600   -0.13843800
O      -1.31152800    2.09824000   -0.27380600
H      -2.94944600    0.23702400   -0.22901500
H      -2.57321800   -1.57895100   -0.04570400
H      -0.19739500   -2.30774600    0.18518600
H       2.18220300   -1.70124700    0.30111500
H       2.89722600    0.67127100    0.14694300
H       1.25524200    2.49405000   -0.12646000
""",
)

entry(
    index = 65,
    label = "S73",
    molecule = 
"""
1  O u0 p2 c0 {7,S} {22,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {11,S}
3  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {7,S} {10,D}
6  C u0 p0 c0 {4,S} {7,D} {9,S}
7  C u0 p0 c0 {1,S} {5,S} {6,D}
8  C u0 p0 c0 {2,S} {9,D} {18,S}
9  C u0 p0 c0 {6,S} {8,D} {19,S}
10 C u0 p0 c0 {5,D} {20,S} {21,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51002,0.0420999,0.000112232,-2.38295e-07,1.36987e-10,-10664.1,13.9359], Tmin=(10,'K'), Tmax=(565.534,'K')),
            NASAPolynomial(coeffs=[0.23262,0.0845732,-5.15931e-05,1.51478e-08,-1.71521e-12,-10601.9,25.1518], Tmin=(565.534,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-88.7299,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (523.812,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 11, 'C-O': 1, 'H-O': 1, 'C-C': 6, 'C=C': 3}
1D rotors:
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 13], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [5, 6], dihedral: [3, 5, 6, 14], rotor symmetry: 3, max scan energy: 2.45 kJ/mol
pivots: [9, 10], dihedral: [2, 9, 10, 20], rotor symmetry: 3, max scan energy: 15.35 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       0.73582400    2.18093200   -1.04152300
C       0.42041900    0.96630100   -0.56102500
C      -0.93605200    0.63977800   -0.10903400
O      -1.82190600    1.67014800    0.09285500
C      -1.35647400   -0.64164000    0.02394200
C      -2.76153300   -0.98972200    0.43080700
C      -0.42144700   -1.72520700   -0.27828100
C       0.87879700   -1.51265300   -0.51188700
C       1.47164700   -0.12882800   -0.43193700
C       2.25201800    0.01885300    0.90088300
H       1.73858500    2.40412800   -1.38707500
H       0.00622600    2.97552100   -1.14777600
H      -1.31681100    2.46103600    0.31216800
H      -3.30929000   -1.44391700   -0.40356100
H      -2.75939200   -1.72106800    1.24623100
H      -3.31146900   -0.10746200    0.75407600
H      -0.81990100   -2.73554000   -0.28740800
H       1.55713400   -2.33949300   -0.69510500
H       2.19214900    0.00053900   -1.24627100
H       1.57710900   -0.08704900    1.75357000
H       2.73069700    1.00016600    0.95595700
H       3.02473500   -0.75067000    0.98078700
""",
)


entry(
    index = 66,
    label = "S75",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {7,S} {8,D}
5  C u0 p0 c0 {1,S} {3,S} {9,D}
6  C u0 p0 c0 {1,S} {7,D} {16,S}
7  C u0 p0 c0 {4,S} {6,D} {17,S}
8  C u0 p0 c0 {4,D} {18,S} {19,S}
9  C u0 p0 c0 {5,D} {20,D}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 O u0 p2 c0 {9,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.25476,0.0642545,-1.01493e-05,-3.27817e-08,1.85107e-11,17968.9,14.1581], Tmin=(10,'K'), Tmax=(815.693,'K')),
            NASAPolynomial(coeffs=[5.91741,0.0651103,-3.73078e-05,1.03255e-08,-1.10998e-12,17071.7,-0.982348], Tmin=(815.693,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (149.328,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (473.925,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-H': 10, 'C-C': 6, 'C=C': 3}
1D rotors:
pivots: [5, 6], dihedral: [2, 5, 6, 15], rotor symmetry: 3, max scan energy: 14.05 kJ/mol
* Invalidated! pivots: [5, 7], dihedral: [2, 5, 7, 8], invalidation reason: Another conformer for S75 exists which is 4.21 kJ/mol lower.Another conformer for S75 exists which is 4.21 kJ/mol lower.
pivots: [7, 8], dihedral: [5, 7, 8, 18], rotor symmetry: 3, max scan energy: 6.58 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.26105900    0.37521200   -1.21219500
C      -1.51985200    0.38324500   -0.10766000
C      -1.63042900    0.91572000    1.25557400
C      -0.43543100    0.42855200    1.63554800
C      -0.13454400   -0.21723900    0.26712300
C      -0.09230200   -1.75176300    0.27549500
C       1.06314800    0.38139100   -0.46245000
C       2.47170300    0.08854100    0.02106600
C       0.89635500    1.18041800   -1.49099200
O       0.79125200    1.88511100   -2.41541500
H      -3.22471700    0.87160200   -1.24682300
H      -1.92829700   -0.12078800   -2.11686300
H      -2.39966400    1.48942000    1.75818700
H       0.12875400    0.45880800    2.55957400
H      -0.07834600   -2.14192500   -0.74549500
H       0.79960600   -2.12103700    0.78960100
H      -0.96871300   -2.15299700    0.78988300
H       2.72263900   -0.97129400   -0.08818000
H       2.58052700    0.35202100    1.07900200
H       3.21501100    0.66130400   -0.53638700
""",
)

entry(
    index = 67,
    label = "S76",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {6,S} {7,S} {10,S}
2  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {2,S} {5,D}
5  C u0 p0 c0 {3,S} {4,D} {6,S}
6  C u0 p0 c0 {1,S} {5,S} {17,D}
7  C u0 p0 c0 {1,S} {9,D} {18,S}
8  C u0 p0 c0 {9,D} {19,S} {20,S}
9  C u0 p0 c0 {7,D} {8,D}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 O u0 p2 c0 {6,D}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.04224,0.095767,-0.00022482,4.48004e-07,-3.45193e-10,16031,14.1732], Tmin=(10,'K'), Tmax=(427.456,'K')),
            NASAPolynomial(coeffs=[2.61424,0.0719211,-4.34085e-05,1.26461e-08,-1.42488e-12,16322,18.8506], Tmin=(427.456,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (133.264,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (469.768,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-H': 10, 'C-C': 6, 'C=C': 3}
1D rotors:
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 11.97 kJ/mol
pivots: [7, 8], dihedral: [5, 7, 8, 15], rotor symmetry: 3, max scan energy: 2.17 kJ/mol
pivots: [9, 10], dihedral: [4, 9, 10, 18], rotor symmetry: 3, max scan energy: 5.22 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       4.08497700    0.28831800    0.03774500
C       2.80977300    0.50222500    0.19737800
C       1.53007700    0.71876100    0.34472600
C       0.46505600    0.20371700   -0.58223500
C      -0.63476100    1.23623800   -1.04628100
O      -0.60451200    2.26531000   -1.66313200
C      -1.67558000    0.41489800   -0.37551800
C      -3.15210200    0.56939600   -0.26147800
C      -0.75574100   -0.48476300    0.05200100
C      -0.81325400   -1.72958800    0.85743000
H       4.57883100   -0.56673300    0.49014200
H       4.70060400    0.96086500   -0.55242600
H       1.19581800    1.32718400    1.18472700
H       0.91510100   -0.34964900   -1.41260800
H      -3.59963400   -0.22563200    0.33942000
H      -3.61939600    0.55616300   -1.25109600
H      -3.40552800    1.53115900    0.19472100
H      -0.45479700   -2.58162600    0.26828700
H      -1.82411900   -1.95014500    1.20622300
H      -0.15088300   -1.65410000    1.72636100
""",
)

entry(
    index = 68,
    label = "S77",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {4,D} {6,S}
4  C u0 p0 c0 {1,S} {3,D} {14,S}
5  C u0 p0 c0 {6,S} {7,D} {8,S}
6  C u0 p0 c0 {3,S} {5,S} {15,D}
7  C u0 p0 c0 {5,D} {16,S} {17,S}
8  C u2 p0 c0 {1,S} {5,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 O u0 p2 c0 {6,D}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67198,0.0275606,0.000132677,-2.99064e-07,1.94762e-10,31922.6,13.3148], Tmin=(10,'K'), Tmax=(493.84,'K')),
            NASAPolynomial(coeffs=[1.13632,0.0665984,-4.20877e-05,1.2718e-08,-1.47369e-12,31947.4,21.475], Tmin=(493.84,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (265.381,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 6, 'C=C': 2, 'C-H': 8, 'C=O': 1}
1D rotors:
pivots: [6, 7], dihedral: [5, 6, 7, 15], rotor symmetry: 3, max scan energy: 5.61 kJ/mol
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 1

Geometry:
C      -2.41669300   -1.63166300    0.34775200
C      -1.49039800   -0.61127100    0.14980400
C      -1.76233800    0.70999900   -0.05702400
C      -0.83886300    1.82860700   -0.27093100
C       0.59759400    1.37124600   -0.24448600
C       0.98731700    0.10286300   -0.05026400
C       2.42942400   -0.32236100   -0.02926200
C      -0.01138300   -0.98586600    0.16129000
O       0.34079100   -2.13549600    0.33736400
H      -2.06748900   -2.64310600    0.50133700
H      -3.47837400   -1.42507200    0.34969100
H      -1.04233100    2.32958600   -1.22966100
H      -0.98449800    2.61065100    0.48981800
H       1.34547000    2.14629000   -0.39632900
H       2.67841700   -0.79192500    0.92604800
H       2.62036900   -1.07402400   -0.79974700
H       3.09467300    0.52750600   -0.19055700
""",
)

entry(
    index = 69,
    label = "S81",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {6,S} {8,D}
5  C u0 p0 c0 {1,S} {6,D} {15,S}
6  C u0 p0 c0 {4,S} {5,D} {16,S}
7  C u0 p0 c0 {1,S} {9,D} {17,S}
8  C u0 p0 c0 {4,D} {18,S} {19,S}
9  C u0 p0 c0 {7,D} {20,D}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 O u0 p2 c0 {9,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.33779,0.0673798,-2.67926e-05,-6.2972e-09,5.29202e-12,18320.6,14.7928], Tmin=(10,'K'), Tmax=(1087.59,'K')),
            NASAPolynomial(coeffs=[11.2765,0.053198,-2.79427e-05,7.10224e-09,-7.06081e-13,15705.7,-28.2562], Tmin=(1087.59,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (152.309,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (469.768,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-H': 10, 'C-C': 6, 'C=C': 3}
1D rotors:
pivots: [5, 6], dihedral: [2, 5, 6, 7], rotor symmetry: 1, max scan energy: 10.79 kJ/mol
pivots: [5, 9], dihedral: [2, 5, 9, 10], rotor symmetry: 1, max scan energy: 20.42 kJ/mol
pivots: [9, 10], dihedral: [5, 9, 10, 18], rotor symmetry: 3, max scan energy: 11.18 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.14113600   -0.97632500    1.33927200
C      -1.31616800   -0.96052700    0.29464600
C      -1.16589400   -1.72089800   -0.95265600
C      -0.16032900   -0.94940300   -1.40267600
C      -0.12713600   -0.05631000   -0.14723800
C      -0.46391000    1.40393500   -0.38946300
C      -1.64850400    1.93955600   -0.21249200
O      -2.68736900    2.43862400   -0.05160600
C       1.16945100   -0.20650500    0.67559500
C       1.13226300    0.41666100    2.07318500
H      -2.93417900   -1.71261200    1.41401300
H      -2.06146300   -0.25307600    2.14182300
H      -1.69334800   -2.57657200   -1.35622000
H       0.43166300   -0.93093800   -2.30955500
H       0.30614900    2.07088400   -0.76381900
H       1.39567000   -1.27480300    0.75256200
H       1.98679900    0.24210900    0.09594600
H       0.37952000   -0.06774900    2.69967700
H       0.90014600    1.48352000    2.02967300
H       2.09985200    0.30225200    2.56928000
""",
)

entry(
    index = 70,
    label = "S82",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {7,S} {10,S}
2  C u0 p0 c0 {3,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {2,S} {6,D}
5  C u0 p0 c0 {1,S} {6,S} {16,D}
6  C u0 p0 c0 {4,D} {5,S} {18,S}
7  C u0 p0 c0 {1,S} {9,D} {17,S}
8  C u0 p0 c0 {9,D} {19,S} {20,S}
9  C u0 p0 c0 {7,D} {8,D}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u0 p2 c0 {5,D}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.3659,0.068943,-3.49552e-05,4.67975e-09,9.81508e-13,19192.5,14.1173], Tmin=(10,'K'), Tmax=(1306.59,'K')),
            NASAPolynomial(coeffs=[15.517,0.0441843,-2.08138e-05,4.75163e-09,-4.26581e-13,14955.2,-51.8178], Tmin=(1306.59,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (159.546,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (473.925,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-H': 10, 'C-C': 6, 'C=C': 3}
1D rotors:
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 12.14 kJ/mol
* Invalidated! pivots: [8, 9], dihedral: [4, 8, 9, 10], invalidation reason: Another conformer for S82 exists which is 2.00 kJ/mol lower.Another conformer for S82 exists which is 2.00 kJ/mol lower.
pivots: [9, 10], dihedral: [8, 9, 10, 18], rotor symmetry: 3, max scan energy: 12.09 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       3.37505200    1.16565200   -0.20048000
C       2.11495200    1.04255300    0.10616200
C       0.85443500    0.91293900    0.42387600
C       0.22544000   -0.36216800    0.90829700
C      -0.70079500   -0.26060600    2.18777300
O      -0.50845600    0.07702600    3.32128400
C      -1.84901100   -0.71383000    1.36711700
C      -1.09717700   -0.79697400    0.24608400
C      -1.37130600   -1.16419700   -1.16846100
C      -0.52961500   -2.36155600   -1.64782300
H       3.73200100    1.00298400   -1.21325800
H       4.11356400    1.43931800    0.54735100
H       0.20506800    1.78526000    0.35608400
H       0.97330700   -1.15628700    0.98653700
H      -2.89335600   -0.90899600    1.57998700
H      -1.13813700   -0.29613700   -1.79814800
H      -2.43730500   -1.37409900   -1.29562800
H      -0.74330100   -3.25403200   -1.05477900
H      -0.75248200   -2.58745300   -2.69294900
H       0.53924300   -2.14984300   -1.56964200
""",
)

entry(
    index = 71,
    label = "S83",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {10,D}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {9,S}
3  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {6,S} {9,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {2,S} {4,S} {8,D}
7  C u0 p0 c0 {2,S} {10,D} {18,S}
8  C u0 p0 c0 {6,D} {19,S} {20,S}
9  C u2 p0 c0 {2,S} {4,S}
10 C u0 p0 c0 {1,D} {7,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.35577,0.0659006,-2.11489e-05,-1.22769e-08,7.39258e-12,55733.9,15.6495], Tmin=(10,'K'), Tmax=(1056.4,'K')),
            NASAPolynomial(coeffs=[10.434,0.0554069,-2.94044e-05,7.54594e-09,-7.56775e-13,53328.5,-23.194], Tmin=(1056.4,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (463.385,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (473.925,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-H': 10, 'C-C': 7, 'C=C': 2}
1D rotors:
pivots: [5, 6], dihedral: [2, 5, 6, 7], rotor symmetry: 1, max scan energy: 8.02 kJ/mol
* Invalidated! pivots: [5, 9], dihedral: [2, 5, 9, 10], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [9, 10], dihedral: [5, 9, 10, 18], rotor symmetry: 3, max scan energy: 13.12 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       2.04306200   -0.55683300    0.79566800
C       1.18484700   -0.84153300   -0.17375300
C       1.11185800   -1.96095500   -1.21172500
C       0.00822400   -1.12103700   -1.80059800
C      -0.02993400   -0.03789600   -0.72576600
C       0.33178500    1.35899000   -1.18487700
C      -0.34941600    2.44324400   -0.89392200
O      -0.94791500    3.40807700   -0.63711200
C      -1.28760900   -0.03391400    0.17509700
C      -1.73357100   -1.40543700    0.68294500
H       1.93984800    0.34896000    1.38393000
H       2.87284200   -1.21488200    1.03029800
H       0.80637500   -2.94238400   -0.82561400
H       2.01545500   -2.09593400   -1.81822100
H       1.20293100    1.49977000   -1.81345300
H      -2.10359700    0.42314600   -0.39596600
H      -1.08750200    0.62549900    1.02786500
H      -0.95557500   -1.88116400    1.28548700
H      -2.62349300   -1.30487500    1.30918300
H      -1.98094000   -2.07356100   -0.14565700
""",
)

entry(
    index = 72,
    label = "S85",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {4,S} {8,D}
3  C u0 p0 c0 {2,S} {6,S} {7,D}
4  C u0 p0 c0 {1,S} {2,S} {11,D}
5  C u0 p0 c0 {1,S} {6,D} {12,S}
6  C u0 p0 c0 {3,S} {5,D} {13,S}
7  C u0 p0 c0 {3,D} {14,S} {15,S}
8  C u0 p0 c0 {2,D} {16,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85638,0.00901907,0.000223887,-4.58729e-07,2.91502e-10,4540.62,14.0766], Tmin=(10,'K'), Tmax=(500.788,'K')),
            NASAPolynomial(coeffs=[-0.182215,0.0700272,-4.49637e-05,1.38141e-08,-1.62632e-12,4584.61,27.1681], Tmin=(500.788,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (37.7116,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (407.409,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 5, 'C=C': 3, 'C-H': 8, 'C=O': 1}

External symmetry: 1, optical isomers: 2

Geometry:
C       2.12516600   -0.84127700    0.63105500
C       0.88257400   -0.53837200    0.21619500
C      -0.11327100   -1.59619400    0.02875500
C      -1.41381600   -1.36269700   -0.17474300
C      -2.01069500    0.01019200   -0.22544900
C      -1.03739200    1.16682000   -0.02848200
O      -1.45571300    2.29937400    0.08179300
C       0.43897500    0.85886900   -0.03498100
C       1.26524700    1.87115300   -0.33094900
H       2.42111400   -1.87191300    0.78771700
H       2.86652600   -0.08155100    0.84326100
H       0.24704100   -2.61834900    0.08827900
H      -2.09693800   -2.19888000   -0.28892500
H      -2.50608200    0.18327300   -1.19073600
H      -2.80650700    0.12296800    0.52048200
H       0.85937800    2.86284100   -0.48732100
H       2.33439200    1.73374200   -0.43595000
""",
)

entry(
    index = 73,
    label = "S86",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {5,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {5,D}
4  C u0 p0 c0 {3,S} {6,S} {7,D}
5  C u0 p0 c0 {1,S} {3,D} {14,S}
6  C u0 p0 c0 {4,S} {8,S} {15,D}
7  C u0 p0 c0 {4,D} {16,S} {17,S}
8  C u2 p0 c0 {1,S} {6,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 O u0 p2 c0 {6,D}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76072,0.0187064,0.000188193,-4.19089e-07,2.82798e-10,36965.6,13.3746], Tmin=(10,'K'), Tmax=(473.152,'K')),
            NASAPolynomial(coeffs=[0.710421,0.0681676,-4.36619e-05,1.33404e-08,-1.55939e-12,36989.3,23.0075], Tmin=(473.152,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (307.318,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 6, 'C=C': 2, 'C-H': 8, 'C=O': 1}
1D rotors:
pivots: [8, 9], dihedral: [2, 8, 9, 15], rotor symmetry: 3, max scan energy: 11.84 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -0.54047000   -2.16263300   -0.02866500
C      -0.58084000   -0.82241300    0.00528300
C      -1.95837300   -0.17499300    0.08172100
O      -2.99347700   -0.84528300    0.11139900
C      -1.92752600    1.24409500    0.11441000
C      -0.77838000    2.15000200    0.08534300
C       0.52228000    1.38094900    0.00938800
C       0.61699300    0.04217400   -0.02692500
C       1.96966400   -0.62166800   -0.10265500
H       0.38710700   -2.71736300   -0.08298600
H      -1.46782700   -2.72085600   -0.00106300
H      -0.85980600    2.84222700   -0.76765400
H      -0.78279200    2.80042900    0.97435100
H       1.42434700    1.98533300   -0.01598800
H       2.05702600   -1.23752500   -1.00322500
H       2.13480700   -1.27974600    0.75618100
H       2.76878700    0.12045900   -0.12017400
""",
)

entry(
    index = 74,
    label = "S87",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {6,D}
4  C u0 p0 c0 {1,S} {3,S} {8,D}
5  C u0 p0 c0 {1,S} {7,D} {14,S}
6  C u0 p0 c0 {3,D} {7,S} {15,S}
7  C u0 p0 c0 {5,D} {6,S} {16,S}
8  C u0 p0 c0 {4,D} {17,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61084,0.0362115,5.29299e-05,-1.06292e-07,5.09697e-11,5687.7,13.0471], Tmin=(10,'K'), Tmax=(728.008,'K')),
            NASAPolynomial(coeffs=[2.57898,0.0605582,-3.57174e-05,1.01262e-08,-1.11038e-12,5343,14.2983], Tmin=(728.008,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (47.257,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 5, 'C=C': 3, 'C-H': 8, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 7.63 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       2.27541700   -0.08775600    0.20478700
C       0.80167300    0.14556600    0.02192100
C       0.07366600   -0.47490600   -0.93237300
C      -1.32911600   -0.14910900   -1.15946900
C      -2.02332800    0.61722900   -0.30910700
C      -1.41278800    1.10665500    0.98143800
C       0.11976800    1.11356700    0.89107900
C       0.79633200    1.97092600    1.63271300
O       1.36504800    2.73521400    2.30271300
H       2.83955100    0.84773500    0.10757500
H       2.65650300   -0.78576700   -0.54181200
H       2.49543100   -0.49222300    1.19869800
H       0.55679800   -1.18940000   -1.58945900
H      -1.80353000   -0.52973700   -2.05802800
H      -3.06117200    0.86822300   -0.49979100
H      -1.73150900    0.44625400    1.80331000
H      -1.79018300    2.10252300    1.23025000
""",
)

entry(
    index = 75,
    label = "S88",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {4,S} {7,D}
4  C u0 p0 c0 {3,S} {6,S} {8,D}
5  C u0 p0 c0 {2,S} {6,D} {13,S}
6  C u0 p0 c0 {4,S} {5,D} {14,S}
7  C u0 p0 c0 {3,D} {15,S} {16,S}
8  C u0 p0 c0 {4,D} {17,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 O u1 p2 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85667,0.00899602,0.000235468,-4.77904e-07,3.02158e-10,10348.2,13.9801], Tmin=(10,'K'), Tmax=(499.129,'K')),
            NASAPolynomial(coeffs=[-0.810726,0.0748359,-4.78515e-05,1.46548e-08,-1.72136e-12,10459.9,29.706], Tmin=(499.129,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (85.9987,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (432.353,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 9}

External symmetry: 1, optical isomers: 2

Geometry:
C       1.34279000   -1.76468100   -0.17462300
C       0.54764700   -0.74887100    0.17442400
C      -0.81778700   -0.96103800    0.78620800
C      -1.90669200   -0.29539400   -0.07744100
C      -1.54812800    1.09589500   -0.46700900
C      -0.20802700    1.61199000   -0.45783900
O       0.01568200    2.78909300   -0.77143300
C       0.90572900    0.67286300   -0.05898800
C       2.14062000    1.16912600    0.08103300
H       1.05825500   -2.79345300    0.01742600
H       2.29325900   -1.59987900   -0.66841200
H      -0.84142800   -0.50929000    1.78535000
H      -1.02577800   -2.02637800    0.90387700
H      -2.87423900   -0.30475500    0.43747800
H      -2.05711900   -0.89044000   -0.99316600
H      -2.31670700    1.78523700   -0.80089500
H       2.32269900    2.21698200   -0.12441300
H       2.96922500    0.55299200    0.40842100
""",
)

entry(
    index = 76,
    label = "S89",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {10,S}
2  C u0 p0 c0 {5,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {7,S} {8,D}
5  C u0 p0 c0 {1,S} {2,S} {16,D}
6  C u0 p0 c0 {2,S} {7,D} {17,S}
7  C u0 p0 c0 {4,S} {6,D} {19,S}
8  C u0 p0 c0 {4,D} {9,S} {18,S}
9  C u1 p0 c0 {8,S} {20,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u0 p2 c0 {5,D}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54843,0.0386222,0.000132841,-2.82616e-07,1.6596e-10,-730.739,14.293], Tmin=(10,'K'), Tmax=(562.723,'K')),
            NASAPolynomial(coeffs=[0.902982,0.0826116,-5.15504e-05,1.53678e-08,-1.75876e-12,-831.753,21.9918], Tmin=(562.723,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-6.14172,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-H': 11, 'C-C': 7, 'C=C': 2}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [11, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [9, 10], dihedral: [3, 9, 10, 19], rotor symmetry: 3, max scan energy: 12.54 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 47.21 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       2.97016200    0.01881700    0.47144100
C       2.01014100   -0.84270100    0.04048400
C       0.60586400   -0.61773600   -0.00252800
C      -0.26526100   -1.63618300   -0.46564500
C      -1.62582400   -1.53920600   -0.45368000
C      -2.33967200   -0.34146900    0.09885100
C      -1.42650200    0.57390300    0.90475800
O      -1.82721400    1.18807600    1.86501800
C       0.01234800    0.71302300    0.40832600
C       0.03676100    1.73115500   -0.76389000
H       4.01427400   -0.26714100    0.46363700
H       2.74034500    1.00906800    0.84583000
H       2.33506300   -1.82022200   -0.31109100
H       0.18777600   -2.55122000   -0.83731900
H      -2.23032200   -2.35918100   -0.82540300
H      -3.18478200   -0.62156800    0.73413300
H      -2.76837700    0.26316700   -0.71635900
H       0.57201800    1.14081600    1.24339300
H      -0.38292200    2.68884600   -0.44603800
H      -0.53553000    1.36322800   -1.61890900
H       1.06382800    1.89366700   -1.09495600
""",
)

entry(
    index = 77,
    label = "S90",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,D} {6,S}
4  C u0 p0 c0 {1,S} {7,S} {14,D}
5  C u0 p0 c0 {3,D} {8,S} {16,S}
6  C u0 p0 c0 {3,S} {9,D} {15,S}
7  C u0 p0 c0 {4,S} {8,D} {18,S}
8  C u0 p0 c0 {5,S} {7,D} {17,S}
9  C u0 p0 c0 {6,D} {19,S} {20,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71775,0.0213521,0.000256329,-6.07981e-07,4.39403e-10,-1873.61,13.5991], Tmin=(10,'K'), Tmax=(445.45,'K')),
            NASAPolynomial(coeffs=[0.677281,0.0808357,-5.23412e-05,1.61616e-08,-1.90628e-12,-1922.01,22.2251], Tmin=(445.45,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-15.6026,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (473.925,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-H': 10, 'C-C': 6, 'C=C': 3}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 29.10 kJ/mol
pivots: [9, 10], dihedral: [3, 9, 10, 18], rotor symmetry: 3, max scan energy: 14.20 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       1.88879100    0.19246100   -2.14924700
C       0.57018700    0.01943100   -1.99064100
C      -0.18460800    0.14468200   -0.74901700
C      -1.53873300    0.06804600   -0.77020100
C      -2.33741900    0.27063400    0.41784800
C      -1.79592400    0.61735900    1.60706800
C      -0.34894600    0.81404800    1.73442400
O       0.16363300    1.28553500    2.73496800
C       0.52890900    0.33367600    0.57042000
C       1.17347000   -1.00452000    1.03292700
H       2.34869800    0.09300000   -3.12485800
H       2.54848700    0.44642000   -1.32786000
H      -0.02808800   -0.21976900   -2.86712200
H      -2.05269600   -0.11771900   -1.70757900
H      -3.41488000    0.17207800    0.32617200
H      -2.39931800    0.82521000    2.48267400
H       1.32999800    1.07100500    0.46692200
H       1.69604800   -0.84110000    1.97684700
H       0.40681800   -1.76837300    1.18481900
H       1.88006500   -1.37321200    0.28859400
""",
)

entry(
    index = 78,
    label = "S91",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {10,S}
2  C u0 p0 c0 {6,S} {7,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,D} {8,S}
5  C u0 p0 c0 {1,S} {7,D} {16,S}
6  C u0 p0 c0 {2,S} {4,D} {17,S}
7  C u0 p0 c0 {2,S} {5,D} {18,S}
8  C u0 p0 c0 {4,S} {9,D} {19,S}
9  C u0 p0 c0 {8,D} {20,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u1 p2 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67627,0.0258747,0.000261976,-6.60028e-07,5.07612e-10,6213.19,14.4406], Tmin=(10,'K'), Tmax=(414.197,'K')),
            NASAPolynomial(coeffs=[0.576513,0.0845377,-5.45065e-05,1.68133e-08,-1.98425e-12,6223.54,23.6883], Tmin=(414.197,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (51.6553,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-H': 11, 'C-C': 6, 'C=C': 3}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 25.93 kJ/mol
pivots: [9, 10], dihedral: [3, 9, 10, 19], rotor symmetry: 3, max scan energy: 12.67 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       2.86951300    0.49716700    0.46624200
C       2.07014800   -0.03722000   -0.46264900
C       0.62589500   -0.27420600   -0.35813200
C      -0.00346200   -0.92124000   -1.35325000
C      -1.45693600   -1.29602800   -1.34163900
C      -2.10751700   -1.11479000   -0.01807100
C      -1.48217400   -0.44501000    1.07969500
O      -2.03828500   -0.36656700    2.18194800
C      -0.12406600    0.22709100    0.86302700
C      -0.35059600    1.75872200    0.81091100
H       2.50556200    0.83598800    1.42910300
H       3.93261600    0.60512100    0.28789500
H       2.51623500   -0.35860200   -1.40164100
H       0.56513800   -1.22767700   -2.22687900
H      -2.00888900   -0.72466100   -2.10964300
H      -1.57570600   -2.34150200   -1.66427900
H      -3.10105300   -1.51340400    0.15866600
H       0.45852700    0.00726800    1.76340100
H      -0.96316300    2.02856600   -0.05387700
H       0.59633300    2.29431300    0.73235100
H      -0.86735000    2.08273200    1.71618300
""",
)

entry(
    index = 79,
    label = "S92",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {4,S}
2  C u0 p0 c0 {1,B} {5,B} {11,S}
3  C u0 p0 c0 {1,B} {7,B} {14,S}
4  C u0 p0 c0 {1,S} {8,D} {10,S}
5  C u0 p0 c0 {2,B} {6,B} {12,S}
6  C u0 p0 c0 {5,B} {7,B} {13,S}
7  C u0 p0 c0 {3,B} {6,B} {9,S}
8  C u0 p0 c0 {4,D} {15,S} {16,S}
9  O u1 p2 c0 {7,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85418,0.00933447,0.000217297,-4.6e-07,3.01077e-10,11403.3,13.7893], Tmin=(10,'K'), Tmax=(488.289,'K')),
            NASAPolynomial(coeffs=[0.358111,0.0660495,-4.31763e-05,1.33811e-08,-1.57927e-12,11410,24.7224], Tmin=(488.289,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (94.7761,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-C': 4, 'C=C': 4, 'C-H': 7}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 16.21 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       2.05647300    2.02502200   -0.09594800
C       0.97461600    1.58547000    0.55050400
C       0.15167700    0.41099500    0.21776100
C       0.43727400   -0.43003200   -0.89217700
C      -0.35876400   -1.54430500   -1.19263700
C      -1.44994100   -1.85841800   -0.41375800
C      -1.79378500   -1.03903100    0.73297300
O      -2.78038700   -1.30444900    1.45545100
C      -0.94183100    0.10196700    1.00395000
H       2.45850900    1.53624600   -0.97616100
H       2.58401700    2.90752200    0.24454900
H       0.63804700    2.13551700    1.42562900
H       1.28859100   -0.21011900   -1.52453300
H      -0.10455200   -2.15894900   -2.04913200
H      -2.08357400   -2.71244100   -0.62061200
H      -1.20672800    0.70843700    1.86306600
""",
)

entry(
    index = 80,
    label = "S94",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,B} {4,B} {8,S}
2  C u0 p0 c0 {3,B} {5,B} {9,S}
3  C u0 p0 c0 {1,B} {2,B} {13,S}
4  C u0 p0 c0 {1,B} {6,B} {10,S}
5  C u0 p0 c0 {2,B} {6,B} {12,S}
6  C u0 p0 c0 {4,B} {5,B} {11,S}
7  C u0 p0 c0 {8,D} {14,S} {15,S}
8  C u1 p0 c0 {1,S} {7,D}
9  O u0 p2 c0 {2,S} {16,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78582,0.014683,0.000237304,-5.71594e-07,4.16953e-10,19486,13.0245], Tmin=(10,'K'), Tmax=(453.552,'K')),
            NASAPolynomial(coeffs=[2.36641,0.063119,-4.16733e-05,1.30731e-08,-1.56039e-12,19245.4,14.6774], Tmin=(453.552,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (161.989,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 4, 'C=C': 4, 'C-H': 6}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: not a torsional mode (angles = 179.78, 120.90 degrees)
pivots: [7, 8], dihedral: [6, 7, 8, 15], rotor symmetry: 2, max scan energy: 16.70 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       3.20596200   -0.41876700   -0.76934100
C       1.94032700   -0.33304900   -0.49804300
C       0.60434000   -0.24791500   -0.21165000
C      -0.18686000   -1.42765300   -0.03863400
C      -1.53418100   -1.31876800    0.25012400
C      -2.15394300   -0.07359100    0.37964100
C      -1.39204500    1.09427100    0.21294500
O      -2.05289400    2.28272600    0.35143400
C      -0.04107200    1.02240200   -0.07670000
H       3.57922000   -0.46037600   -1.79426000
H       3.96684500   -0.45537000    0.01247000
H       0.28630300   -2.39598000   -0.13746600
H      -2.12531000   -2.21861600    0.37944100
H      -3.20857100    0.01707200    0.60565500
H      -1.43320300    3.00716600    0.21647500
H       0.54496300    1.92644200   -0.20493500
""",
)

entry(
    index = 81,
    label = "S95",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {14,S}
2  C u0 p0 c0 {4,B} {5,B} {8,S}
3  C u0 p0 c0 {1,S} {4,B} {6,B}
4  C u0 p0 c0 {2,B} {3,B} {13,S}
5  C u0 p0 c0 {2,B} {7,B} {10,S}
6  C u0 p0 c0 {3,B} {7,B} {12,S}
7  C u0 p0 c0 {5,B} {6,B} {11,S}
8  C u0 p0 c0 {2,S} {9,T}
9  C u0 p0 c0 {8,T} {15,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80719,0.0118891,0.000208999,-4.48053e-07,2.86315e-10,14431.2,12.5056], Tmin=(10,'K'), Tmax=(528.173,'K')),
            NASAPolynomial(coeffs=[3.16035,0.0579711,-3.88331e-05,1.23917e-08,-1.5042e-12,13925.1,9.77532], Tmin=(528.173,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (119.924,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (353.365,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C#C': 1, 'C-O': 1, 'H-O': 1, 'C-C': 4, 'C=C': 3, 'C-H': 5}
1D rotors:
pivots: [7, 8], dihedral: [6, 7, 8, 14], rotor symmetry: 1, max scan energy: 16.83 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       3.43614900    0.53536400    0.03410000
C       2.26117800    0.27238200    0.03144400
C       0.86802800   -0.04195800    0.02858000
C       0.43626300   -1.36955700    0.16629900
C      -0.92628800   -1.65311300    0.16080700
C      -1.86818600   -0.64067100    0.02085000
C      -1.44116800    0.68276100   -0.11653000
O      -2.40398100    1.64117700   -0.25097300
C      -0.08115700    0.98320900   -0.11301000
H       4.47304600    0.76591500    0.03661600
H       1.16755400   -2.15978700    0.27543100
H      -1.26044400   -2.67884400    0.26719600
H      -2.93064100   -0.85030900    0.01527600
H      -1.98550200    2.50407100   -0.33669800
H       0.25515100    2.00936000   -0.21938800
""",
)

entry(
    index = 82,
    label = "S96",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,S} {8,D}
5  C u0 p0 c0 {1,S} {4,S} {16,D}
6  C u0 p0 c0 {1,S} {7,D} {17,S}
7  C u0 p0 c0 {6,D} {8,S} {18,S}
8  C u1 p0 c0 {4,D} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 O u0 p2 c0 {5,D}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57708,0.0435809,2.64544e-05,-6.23681e-08,2.69638e-11,16037.9,14.0632], Tmin=(10,'K'), Tmax=(869.861,'K')),
            NASAPolynomial(coeffs=[4.57805,0.0584965,-3.29241e-05,8.93552e-09,-9.42752e-13,15125.3,5.12911], Tmin=(869.861,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (133.345,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (424.038,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 6, 'C=C': 2, 'C-H': 9, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 3.39 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 16], rotor symmetry: 3, max scan energy: 11.68 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.72712400   -0.54120400   -0.63212300
C      -1.37771900    0.01132300   -0.26966800
C      -0.21834600   -0.26172700   -0.86499000
C       1.10082400    0.20991900   -0.56722900
C       1.23509800    1.07505500    0.45350000
C       0.06661200    1.54755300    1.26661100
C       0.31730000    1.39621300    2.78336200
C      -1.30346900    0.94721400    0.89426700
O      -2.29757800    1.23839600    1.53160100
H      -3.15626200   -1.08454700    0.21437200
H      -2.65690500   -1.21067200   -1.48937400
H      -3.42190600    0.27058200   -0.86499000
H       1.95139800   -0.12493100   -1.14984700
H       2.21408500    1.46455200    0.72009600
H      -0.05096700    2.62437500    1.06790000
H       1.19228300    1.97320300    3.09135200
H       0.48843000    0.34855600    3.04249500
H      -0.55495800    1.75171100    3.33170300
""",
)

entry(
    index = 83,
    label = "S98",
    molecule = 
"""
1  O u0 p2 c0 {8,D}
2  C u0 p0 c0 {3,S} {6,S} {8,S} {11,S}
3  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {2,S} {4,S} {9,D}
7  C u0 p0 c0 {5,S} {8,S} {10,D}
8  C u0 p0 c0 {1,D} {2,S} {7,S}
9  C u0 p0 c0 {6,D} {10,S} {22,S}
10 C u0 p0 c0 {7,D} {9,S} {21,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.472,0.0589012,3.36873e-06,-3.22277e-08,1.27051e-11,-18328.6,13.9095], Tmin=(10,'K'), Tmax=(1087.11,'K')),
            NASAPolynomial(coeffs=[8.30484,0.0628847,-3.21605e-05,7.97819e-09,-7.76427e-13,-20665.5,-15.7252], Tmin=(1087.11,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-152.381,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (523.812,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 12, 'C=O': 1, 'C-C': 7, 'C=C': 2}
1D rotors:
pivots: [1, 2], dihedral: [11, 1, 2, 3], rotor symmetry: 3, max scan energy: 4.70 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 16], rotor symmetry: 3, max scan energy: 6.36 kJ/mol
* Invalidated! pivots: [7, 8], dihedral: [5, 7, 8, 20], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
C       3.14398300    0.36561500   -0.54703600
C       1.73510400   -0.00985900   -0.19238500
C       0.75945900    0.88480400    0.08877000
C      -0.59430900    0.51434900    0.45582500
C      -0.99950000   -0.76711100    0.51108300
C      -2.39261800   -1.15004300    0.92476500
C      -0.03486800   -1.87494000    0.16168800
C      -0.53488000   -2.73671900   -1.02575500
C       1.41321300   -1.44731700   -0.13267300
O       2.26361300   -2.30173900   -0.33033200
H       3.85086600   -0.05712100    0.17276100
H       3.27112300    1.44963200   -0.57149100
H       3.42179100   -0.04587600   -1.52186200
H       0.99308600    1.94593900    0.05576200
H      -1.28654700    1.31274000    0.70397000
H      -2.94397400   -1.62047200    0.10376200
H      -2.37300500   -1.87543400    1.74623100
H      -2.96034400   -0.27772800    1.25344900
H       0.03854600   -2.54479500    1.03002700
H      -0.69455700   -2.11644300   -1.91180900
H      -1.47200200   -3.24128000   -0.78491400
H       0.21980400   -3.48883500   -1.25647700
""",
)

entry(
    index = 84,
    label = "S99",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {5,B} {8,B}
4  C u0 p0 c0 {2,S} {6,B} {7,B}
5  C u0 p0 c0 {3,B} {6,B} {16,S}
6  C u0 p0 c0 {4,B} {5,B} {17,S}
7  C u0 p0 c0 {4,B} {8,B} {15,S}
8  C u0 p0 c0 {3,B} {7,B} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 O u1 p2 c0 {7,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77067,0.036142,4.30506e-05,-7.39199e-08,2.89335e-11,-6454.22,12.9377], Tmin=(10,'K'), Tmax=(935.017,'K')),
            NASAPolynomial(coeffs=[4.89516,0.0568783,-3.11993e-05,8.24157e-09,-8.4745e-13,-7781.24,1.61652], Tmin=(935.017,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-53.6005,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (424.038,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 9}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 1.86 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 15], rotor symmetry: 3, max scan energy: 1.94 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       2.94269100    0.08736100   -0.07333900
C       1.43489800    0.03261300   -0.05798700
C       0.72185800    0.51155400    1.07141100
C      -0.67749400    0.48108800    1.13088100
C      -1.43396600   -0.01903400    0.08797000
C      -2.92951000   -0.07029000    0.10997100
C      -0.73966700   -0.52483300   -1.09942400
O      -1.37795600   -0.98693300   -2.06856300
C       0.71109200   -0.47058300   -1.11069900
H       3.36601500   -0.48947400    0.75482500
H       3.34371100   -0.31519400   -1.00458400
H       3.30035400    1.11628700    0.03241900
H       1.27736900    0.91294700    1.91313400
H      -1.17418800    0.86012600    2.01855000
H      -3.34736700    0.49302300   -0.72953800
H      -3.32930800    0.33269300    1.04205500
H      -3.28229300   -1.09838400   -0.01358800
H       1.19374600   -0.85256300   -2.00363200
""",
)



entry(
    index = 85,
    label = "S100",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,B} {6,B}
4  C u0 p0 c0 {2,S} {7,B} {8,B}
5  C u0 p0 c0 {3,B} {8,B} {9,S}
6  C u0 p0 c0 {3,B} {7,B} {16,S}
7  C u0 p0 c0 {4,B} {6,B} {17,S}
8  C u1 p0 c0 {4,B} {5,B}
9  O u0 p2 c0 {5,S} {18,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6201,0.0333416,9.45228e-05,-1.95476e-07,1.08324e-10,8784.1,13.7415], Tmin=(10,'K'), Tmax=(606.585,'K')),
            NASAPolynomial(coeffs=[1.84197,0.0666194,-4.10644e-05,1.21161e-08,-1.37441e-12,8603.31,18.1627], Tmin=(606.585,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (72.9809,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (419.881,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 8}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 0.72 kJ/mol (set as a FreeRotor)
pivots: [4, 5], dihedral: [3, 4, 5, 13], rotor symmetry: 1, max scan energy: 21.80 kJ/mol
pivots: [6, 7], dihedral: [4, 6, 7, 14], rotor symmetry: 3, max scan energy: 3.21 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       3.03557200    0.43553100    0.01428800
C       1.55191500    0.16441300   -0.04940000
C       0.88826800   -0.59722200    0.88631800
C      -0.45227800   -0.89820800    0.91303600
O      -1.04595100   -1.66493800    1.87894500
C      -1.25957200   -0.38215900   -0.12114300
C      -2.73573000   -0.68389100   -0.13686500
C      -0.63442800    0.39668100   -1.09500000
C       0.73401200    0.67070000   -1.07209000
H       3.60867700   -0.49534100   -0.01951500
H       3.30337000    0.94978700    0.94161000
H       3.35187800    1.05952900   -0.82349600
H      -0.36672500   -1.93730000    2.50586800
H      -3.22332900   -0.32217300    0.77321200
H      -2.91891100   -1.76143800   -0.18359900
H      -3.21718900   -0.21419300   -0.99661700
H      -1.23942600    0.80264800   -1.89897300
H       1.17830700    1.28198300   -1.85125900
""",
)

entry(
    index = 86,
    label = "S101",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {5,B} {6,B}
3  C u0 p0 c0 {4,B} {7,B} {8,S}
4  C u0 p0 c0 {3,B} {5,B} {9,S}
5  C u0 p0 c0 {2,B} {4,B} {15,S}
6  C u0 p0 c0 {2,B} {7,B} {14,S}
7  C u0 p0 c0 {3,B} {6,B} {13,S}
8  C u1 p0 c0 {3,S} {16,S} {17,S}
9  O u0 p2 c0 {4,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78241,0.0166225,0.000221046,-5.06756e-07,3.59298e-10,-3487.29,14.1917], Tmin=(10,'K'), Tmax=(443.258,'K')),
            NASAPolynomial(coeffs=[0.225408,0.0721312,-4.60174e-05,1.40603e-08,-1.64607e-12,-3401.93,25.864], Tmin=(443.258,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-29.0132,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 8}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [5, 6], dihedral: [4, 5, 6, 14], rotor symmetry: 4, max scan energy: 0.16 kJ/mol (set as a FreeRotor)
* Invalidated! pivots: [8, 9], dihedral: [2, 8, 9, 18], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.79921300   -0.76083100   -0.01668300
C      -1.43492300   -0.44689400   -0.00262400
C      -0.43963000   -1.46516100   -0.10493200
C       0.90669200   -1.18106700   -0.05988400
C       1.36139900    0.14478000    0.08703100
C       2.83459700    0.44939200    0.17192500
C       0.41138400    1.16568400    0.16980300
C      -0.94886400    0.89549500    0.12099900
O      -1.79373500    1.96183500    0.19797900
H      -3.58371200   -0.02675500    0.12478500
H      -3.12519600   -1.78561700   -0.13435900
H      -0.77402800   -2.49131500   -0.21398700
H       1.62882100   -1.98712700   -0.13692800
H       3.40815600   -0.16104000   -0.53087900
H       3.22245500    0.23721000    1.17509500
H       3.03924800    1.49995200   -0.04388500
H       0.71782800    2.20136100    0.26532500
H      -2.69320300    1.67153700    0.01744100
""",
)

entry(
    index = 87,
    label = "S102",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,B} {7,B}
4  C u0 p0 c0 {2,S} {6,B} {8,B}
5  C u0 p0 c0 {3,B} {6,B} {9,S}
6  C u0 p0 c0 {4,B} {5,B} {16,S}
7  C u0 p0 c0 {3,B} {8,B} {17,S}
8  C u1 p0 c0 {4,B} {7,B}
9  O u0 p2 c0 {5,S} {18,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61658,0.0331236,9.24168e-05,-1.89445e-07,1.05157e-10,9007.22,15.4088], Tmin=(10,'K'), Tmax=(592.548,'K')),
            NASAPolynomial(coeffs=[1.06987,0.0681812,-4.15565e-05,1.21706e-08,-1.37406e-12,8995.38,23.7158], Tmin=(592.548,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (74.8378,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 8}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 1, max scan energy: 0.05 kJ/mol (set as a FreeRotor)
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 14], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
* Invalidated! pivots: [7, 8], dihedral: [5, 7, 8, 17], invalidation reason: Inconsistent initial and final conformersInconsistent initial and final conformers


External symmetry: 1, optical isomers: 2

Geometry:
C       3.07569400   -0.05256300   -0.22469100
C       1.57616000   -0.20247800   -0.13792200
C       0.83659600   -0.95110000   -1.02461300
C      -0.52843700   -1.10957000   -1.01531300
C      -1.27450400   -0.45985300   -0.02221600
C      -2.77279400   -0.57743400    0.06761100
C      -0.56681600    0.31791700    0.90973400
O      -1.31456300    0.94206300    1.87672400
C       0.82140400    0.44424300    0.85609600
H       3.34789600    0.77520300   -0.88792500
H       3.53652200   -0.95773400   -0.62395700
H       3.51035800    0.15117800    0.75667500
H      -1.03633800   -1.72290100   -1.75290600
H      -3.07858700   -0.99815800    1.03016500
H      -3.16178200   -1.21601300   -0.72744900
H      -3.25099300    0.40343500   -0.01117500
H      -0.72912600    1.44277200    2.45356000
H       1.33117200    1.05259900    1.60105600
""",
)

entry(
    index = 88,
    label = "S103",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,B} {5,B}
3  C u0 p0 c0 {6,B} {7,B} {8,S}
4  C u0 p0 c0 {2,B} {6,B} {9,S}
5  C u0 p0 c0 {2,B} {7,B} {14,S}
6  C u0 p0 c0 {3,B} {4,B} {15,S}
7  C u0 p0 c0 {3,B} {5,B} {13,S}
8  C u1 p0 c0 {3,S} {16,S} {17,S}
9  O u0 p2 c0 {4,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75658,0.0187463,0.000242399,-6.15807e-07,4.81754e-10,-3514.68,12.83], Tmin=(10,'K'), Tmax=(408.844,'K')),
            NASAPolynomial(coeffs=[1.23864,0.0702579,-4.51987e-05,1.39453e-08,-1.64752e-12,-3533.42,19.9784], Tmin=(408.844,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-29.2219,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (424.038,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'H-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 8}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [5, 6], dihedral: [4, 5, 6, 14], rotor symmetry: 3, max scan energy: 3.36 kJ/mol
pivots: [7, 8], dihedral: [5, 7, 8, 17], rotor symmetry: 1, max scan energy: 16.60 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       3.04198200    0.49557200    0.03345800
C       1.67486300    0.18315800    0.02428000
C       1.21963100   -1.16269500    0.10234700
C      -0.13299400   -1.45301600    0.09204000
C      -1.11088000   -0.45434000    0.00563800
C      -2.58192700   -0.76217700   -0.00608700
C      -0.66600000    0.88390400   -0.07215500
O      -1.64349800    1.84067900   -0.15581100
C       0.67977700    1.19847900   -0.06358100
H       3.38527000    1.52080200   -0.02608700
H       3.79002300   -0.28398200    0.10057100
H       1.94874000   -1.96206400    0.17034500
H      -0.45634700   -2.48737200    0.15261200
H      -3.09557300   -0.27613100    0.82940000
H      -2.75567300   -1.83762000    0.06040700
H      -3.05773500   -0.39034800   -0.91902800
H      -1.23063300    2.70902300   -0.20360200
H       0.99097300    2.23812300   -0.12476200
""",
)

entry(
    index = 89,
    label = "S104",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {4,S} {5,D}
4  C u0 p0 c0 {2,S} {3,S} {8,D}
5  C u0 p0 c0 {3,D} {6,S} {17,S}
6  C u0 p0 c0 {5,S} {7,D} {16,S}
7  C u0 p0 c0 {6,D} {9,S} {18,S}
8  C u1 p0 c0 {4,D} {9,S}
9  O u0 p2 c0 {7,S} {8,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81273,0.0171982,0.000298562,-9.8214e-07,1.08412e-09,27657.1,13.0452], Tmin=(10,'K'), Tmax=(229.193,'K')),
            NASAPolynomial(coeffs=[0.816737,0.0694846,-4.36285e-05,1.31847e-08,-1.53331e-12,27794.4,23.0855], Tmin=(229.193,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (229.99,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (424.038,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 4, 'C=C': 3, 'C-H': 9}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 9.58 kJ/mol
pivots: [8, 9], dihedral: [2, 8, 9, 16], rotor symmetry: 3, max scan energy: 8.50 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.54376900   -1.57528500   -0.60352600
C      -0.31628800   -0.91467800   -0.01747000
C       0.75788900   -1.65198400    0.27077500
O       1.95038300   -1.29702300    0.77785500
C       2.63132200   -0.37316800   -0.02946700
C       2.11167400    0.82515800   -0.30786800
C       0.79569600    1.29855500    0.08836700
C      -0.31756900    0.54262000    0.24361900
C      -1.62776900    1.18393100    0.62898400
H      -2.40258400   -1.50614600    0.07162500
H      -1.34849900   -2.63159500   -0.79016200
H      -1.83258700   -1.10669600   -1.55025800
H       3.60989400   -0.71697000   -0.33881100
H       2.74947300    1.51124900   -0.85749900
H       0.70176500    2.37329200    0.21790600
H      -2.03253000    0.72841200    1.53901300
H      -2.38346500    1.05741700   -0.15274300
H      -1.50303600    2.25291700    0.80964400
""",
)

entry(
    index = 90,
    label = "S105",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {7,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {5,S} {15,S}
5  C u0 p0 c0 {4,S} {6,D} {14,S}
6  C u0 p0 c0 {5,D} {16,S} {17,S}
7  C u1 p0 c0 {1,S} {8,D}
8  C u0 p0 c0 {7,D} {18,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.20074,0.079293,-0.000156474,3.01371e-07,-2.33986e-10,27303.7,15.6196], Tmin=(10,'K'), Tmax=(427.25,'K')),
            NASAPolynomial(coeffs=[2.53017,0.0658567,-4.00884e-05,1.17682e-08,-1.3344e-12,27540.9,20.3902], Tmin=(427.25,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (226.995,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 4, 'C=C': 3, 'C-H': 9, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: 
pivots: [4, 5], dihedral: [3, 4, 5, 14], rotor symmetry: 3, max scan energy: 7.74 kJ/mol
* Invalidated! pivots: [4, 6], dihedral: [3, 4, 6, 7], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
* Invalidated! pivots: [6, 7], dihedral: [4, 6, 7, 8], invalidation reason: Internal coordinate error; Internal coordinate error; 


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.47956000    1.36571400    1.54520600
C      -1.46166700    1.09487100    0.71908200
C      -0.96895400   -0.24836700    0.46385300
C       0.02596500   -0.60967800   -0.36815200
C       0.47089600   -2.03775100   -0.51111800
C       0.79610800    0.40622600   -1.20976200
C       1.99814400    0.85093500   -0.50374700
C       3.05151100    0.69077000    0.18588700
O       4.05007100    0.67297400    0.82391400
H      -3.00442500    0.57789000    2.07639000
H      -2.81578900    2.38078000    1.71767200
H      -0.96236800    1.92187000    0.22262300
H      -1.47007000   -1.04071300    1.01695600
H      -0.06191100   -2.69716000    0.17578000
H       0.30362000   -2.39844200   -1.53344900
H       1.54404100   -2.13537100   -0.31375900
H       0.16399700    1.25113400   -1.49248700
H       1.10369700   -0.07380400   -2.14985900
""",
)

entry(
    index = 91,
    label = "S106",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {2,S} {8,D}
5  C u1 p0 c0 {1,S} {6,S} {14,S}
6  C u0 p0 c0 {5,S} {7,D} {15,S}
7  C u0 p0 c0 {6,D} {16,S} {17,S}
8  C u0 p0 c0 {4,D} {18,D}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.36191,0.0576057,-9.19025e-06,-2.76904e-08,1.49941e-11,27018.3,15.5299], Tmin=(10,'K'), Tmax=(869.214,'K')),
            NASAPolynomial(coeffs=[6.68697,0.0565895,-3.20884e-05,8.77939e-09,-9.33266e-13,25900.6,-3.14974], Tmin=(869.214,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (224.595,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 6, 'C=C': 2, 'C-H': 9, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for S106 exists which is 5.96 kJ/mol lower.Another conformer for S106 exists which is 5.96 kJ/mol lower.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Another conformer for S106 exists which is 5.92 kJ/mol lower.Another conformer for S106 exists which is 5.92 kJ/mol lower.
pivots: [4, 5], dihedral: [3, 4, 5, 14], rotor symmetry: 3, max scan energy: 12.53 kJ/mol
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
C       3.04054800   -0.88220500   -0.47844700
C       1.70651900   -0.83705800   -0.13519300
C       0.89138600    0.28060900   -0.26415600
C      -0.56039200    0.34169300    0.04106100
C      -1.08173600    1.72622500    0.40145600
C      -1.51143000   -0.58494900   -0.72500200
C      -1.21415400   -0.84221900    0.69855400
C      -1.49349700   -1.42998200    1.80628700
O      -1.71321300   -1.97248600    2.81928700
H       3.62542600   -1.78308700   -0.34522800
H       3.54779000   -0.01500000   -0.88729900
H       1.25276000   -1.73587200    0.27696000
H       1.32788500    1.20136800   -0.64482200
H      -0.87132200    2.43369900   -0.40729400
H      -0.59904200    2.09737500    1.30907100
H      -2.15958600    1.70665600    0.57133500
H      -1.07314000   -1.25371200   -1.46018200
H      -2.49504600   -0.19664300   -0.97810500
""",
)

entry(
    index = 92,
    label = "S107",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {3,S} {5,D}
5  C u0 p0 c0 {1,S} {4,D} {6,S}
6  C u0 p0 c0 {5,S} {7,D} {15,S}
7  C u0 p0 c0 {6,D} {16,S} {17,S}
8  C u1 p0 c0 {1,S} {18,D}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.09153,0.0807303,-0.000121773,1.54107e-07,-8.60316e-11,30579.9,14.0742], Tmin=(10,'K'), Tmax=(526.459,'K')),
            NASAPolynomial(coeffs=[4.51086,0.0602576,-3.58367e-05,1.03263e-08,-1.15403e-12,30564.8,9.41263], Tmin=(526.459,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (254.199,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (419.881,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 6, 'C=C': 2, 'C-H': 9, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [4, 5], dihedral: [3, 4, 5, 13], rotor symmetry: 3, max scan energy: 4.67 kJ/mol
pivots: [6, 7], dihedral: [3, 6, 7, 16], rotor symmetry: 3, max scan energy: 4.91 kJ/mol
pivots: [6, 8], dihedral: [3, 6, 8, 9], rotor symmetry: 1, max scan energy: 17.40 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       3.04983700   -0.54901700    0.32271400
C       1.99254500   -0.55940100   -0.49623200
C       0.69311600   -1.03268700   -0.11121300
C      -0.55011500   -1.30881200   -0.33815700
C      -1.75147600   -1.40468200   -1.18815500
C      -0.08254300   -1.56675100    1.08743600
C      -0.50526100   -0.66179100    2.24435200
C       0.16355400   -2.99585200    1.46772600
O       0.07389700   -3.48743400    2.54412400
H       4.01547200   -0.18828700   -0.00934000
H       2.97576300   -0.90634500    1.34353300
H       2.09002000   -0.19910500   -1.51722300
H      -1.55472800   -1.03647400   -2.19723800
H      -2.08619700   -2.44511700   -1.25301400
H      -2.57675000   -0.82672400   -0.76010300
H      -1.44670100   -1.00446900    2.68286800
H      -0.63529500    0.36583500    1.89736600
H       0.24375200   -0.66716000    3.04048200
""",
)

entry(
    index = 93,
    label = "S108",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {6,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {5,D} {16,S}
5  C u0 p0 c0 {4,D} {8,S} {17,S}
6  C u0 p0 c0 {3,S} {8,T}
7  C u1 p0 c0 {1,S} {18,D}
8  C u0 p0 c0 {5,S} {6,T}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.98993,0.103204,-0.00032057,6.7618e-07,-5.24449e-10,25993.6,17.6494], Tmin=(10,'K'), Tmax=(421.728,'K')),
            NASAPolynomial(coeffs=[3.25747,0.0620518,-3.68589e-05,1.05777e-08,-1.17619e-12,26314.5,20.6609], Tmin=(421.728,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (216.098,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (419.881,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C#C': 1, 'C-C': 5, 'C=C': 1, 'C-H': 9, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: 
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 0.10 kJ/mol (set as a FreeRotor)
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [6, 7], dihedral: [5, 6, 7, 16], rotor symmetry: 3, max scan energy: 13.05 kJ/mol
pivots: [6, 8], dihedral: [5, 6, 8, 9], rotor symmetry: 1, max scan energy: 4.88 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       4.28193100    0.17693500    0.15399400
C       2.86891100    0.20565100   -0.19577300
C       1.69389500    0.22910400   -0.47238900
C       0.32395900    0.24794500   -0.84214500
C      -0.69144100    0.52291600   -0.00795800
C      -2.12876400    0.52829500   -0.42283500
C      -2.83944100    1.87224800   -0.15233300
C      -2.93701500   -0.54940000    0.35328100
O      -2.78703000   -0.89866000    1.46868700
H       4.89811700   -0.07448500   -0.71404000
H       4.61448900    1.14898100    0.53109200
H       4.47940200   -0.56658100    0.93228500
H       0.10428000    0.02463300   -1.88525300
H      -0.48784400    0.73186800    1.03835400
H      -2.21854400    0.28654500   -1.48459100
H      -2.75548400    2.14952100    0.90095500
H      -2.37851600    2.65709700   -0.75497100
H      -3.89995700    1.81165600   -0.40920800
""",
)

entry(
    index = 94,
    label = "S109",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {9,D}
2  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {3,S} {6,D}
5  C u0 p0 c0 {2,S} {7,D} {14,S}
6  C u0 p0 c0 {4,D} {8,S} {15,S}
7  C u0 p0 c0 {5,D} {8,S} {17,S}
8  C u1 p0 c0 {6,S} {7,S} {16,S}
9  C u1 p0 c0 {1,D} {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66334,0.0415629,2.38655e-05,-5.61684e-08,2.34934e-11,23905.2,14.3953], Tmin=(10,'K'), Tmax=(920.753,'K')),
            NASAPolynomial(coeffs=[6.09671,0.0526139,-2.93627e-05,7.87563e-09,-8.20541e-13,22540.5,-2.12063], Tmin=(920.753,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (198.791,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 6, 'C=C': 2, 'C-H': 8, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 7.00 kJ/mol
pivots: [7, 8], dihedral: [2, 7, 8, 9], rotor symmetry: 1, max scan energy: 10.44 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.08297100    0.63515400    0.38439200
C      -0.61431800    0.39727200    0.20153800
C       0.31541700    1.38950900    0.31055400
C       1.69942600    1.17852500    0.08055800
C       2.16357900   -0.09878200   -0.30636100
C       1.30953800   -1.15100400   -0.44292000
C      -0.17077900   -1.00982700   -0.16686400
C      -0.52930800   -2.07566000    0.87779800
O      -1.17179100   -1.99099500    1.86429200
H      -2.64216700    0.34378300   -0.51434800
H      -2.28931700    1.68838300    0.58358800
H      -2.48279700    0.04249800    1.21222900
H      -0.02114400    2.38771700    0.57542500
H       2.39495500    2.00121800    0.18770400
H       3.22071300   -0.24398600   -0.50251700
H       1.66302900   -2.13387300   -0.72946000
H      -0.73198600   -1.34376600   -1.06216200
""",
)

entry(
    index = 95,
    label = "S110",
    molecule = 
"""
1  O u0 p2 c0 {9,D}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {10,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {9,D}
5  C u0 p0 c0 {2,S} {7,D} {14,S}
6  C u0 p0 c0 {4,S} {8,D} {17,S}
7  C u0 p0 c0 {5,D} {8,S} {15,S}
8  C u0 p0 c0 {6,D} {7,S} {16,S}
9  C u0 p0 c0 {1,D} {4,D}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69949,0.026707,0.000109396,-2.11745e-07,1.14865e-10,6541.76,13.1963], Tmin=(10,'K'), Tmax=(610.96,'K')),
            NASAPolynomial(coeffs=[1.28437,0.0650675,-4.01449e-05,1.18395e-08,-1.34192e-12,6416.02,20.2137], Tmin=(610.96,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (54.3449,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 5, 'C=C': 3, 'C-H': 8, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 14.41 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.01529100   -0.02334000    0.27649800
C      -0.70099000   -0.24576800   -0.50496700
C       0.23705200    0.92491400   -0.29751000
C       0.37648600    1.90477800   -1.20156400
C      -0.27313900    1.84371600   -2.50426800
C      -0.88586100    0.71294200   -2.90849900
C      -0.96455600   -0.43432400   -2.01250800
C      -1.31253600   -1.62593000   -2.46392900
O      -1.61548800   -2.68365700   -2.84224800
H      -2.53922100    0.85749300   -0.10104000
H      -2.67711300   -0.88906500    0.17873200
H      -1.80753100    0.13218200    1.33968100
H      -0.22639200   -1.14991400   -0.10918400
H       0.75176700    0.97353800    0.65681200
H       1.01085600    2.75725200   -0.98194500
H      -0.20848500    2.69505400   -3.17086100
H      -1.30486900    0.62861000   -3.90456600
""",
)

entry(
    index = 96,
    label = "S112",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {7,D}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,S} {6,D} {11,S}
5  C u0 p0 c0 {3,D} {6,S} {13,S}
6  C u0 p0 c0 {4,D} {5,S} {12,S}
7  C u0 p0 c0 {2,D} {14,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02822,-0.00377213,0.000199639,-3.4375e-07,1.88208e-10,20418,11.8303], Tmin=(10,'K'), Tmax=(569.138,'K')),
            NASAPolynomial(coeffs=[-1.8125,0.0619556,-3.86315e-05,1.15375e-08,-1.32215e-12,20683.2,33.2051], Tmin=(569.138,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (169.739,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 4, 'C=C': 3, 'C-H': 8}

External symmetry: 1, optical isomers: 2

Geometry:
C       2.26254800   -0.08528300    0.35154900
C       0.95599500   -0.02183900    0.05045500
C       0.36896500    1.18039000   -0.53442200
C      -0.96513900    1.34915200   -0.62276300
C      -1.89262600    0.33504400   -0.12980400
C      -1.44515500   -0.84428600    0.31811400
C       0.01853500   -1.20088600    0.28283700
H       2.70086800   -0.95957500    0.82015400
H       2.92981500    0.74072500    0.13176800
H       1.04569700    1.96636400   -0.85436100
H      -1.37114800    2.26734700   -1.03317300
H      -2.95410800    0.55812200   -0.12981700
H      -2.13581800   -1.59988600    0.67837100
H       0.16298900   -1.92714200   -0.53278900
H       0.30339500   -1.73513600    1.19483400
""",
)

entry(
    index = 97,
    label = "S113",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {5,S} {6,S} {7,D}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {1,S} {6,D} {11,S}
5  C u0 p0 c0 {2,S} {3,D} {12,S}
6  C u0 p0 c0 {2,S} {4,D} {13,S}
7  C u0 p0 c0 {2,D} {14,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05987,-0.00642847,0.000212767,-3.67309e-07,2.02655e-10,18476.6,10.0524], Tmin=(10,'K'), Tmax=(565.344,'K')),
            NASAPolynomial(coeffs=[-1.87891,0.0619417,-3.8553e-05,1.15011e-08,-1.31748e-12,18727,31.5922], Tmin=(565.344,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (153.599,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 4, 'C=C': 3, 'C-H': 8}

External symmetry: 2, optical isomers: 1

Geometry:
C       2.38023800    0.23988400    0.52688200
C       1.07204600    0.10804200    0.23730500
C       0.45215000   -1.20219000    0.01777000
C      -0.84662600   -1.34369300   -0.27042400
C      -1.78709000   -0.18010500   -0.39558500
C      -1.12080000    1.14541300   -0.16508000
C       0.18028800    1.26592800    0.12222500
H       2.82846000    1.21361900    0.68735800
H       3.03077600   -0.62311700    0.60962400
H       1.09135900   -2.07633500    0.09734400
H      -1.26222200   -2.33497800   -0.42505200
H      -2.62706300   -0.30231800    0.30593500
H      -2.26326600   -0.19053600   -1.38844300
H      -1.74325200    2.03208200   -0.24023000
H       0.61500200    2.24830400    0.28037100
""",
)

entry(
    index = 98,
    label = "S114",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {8,S}
2  C u0 p0 c0 {1,B} {4,B} {7,S}
3  C u0 p0 c0 {1,B} {5,B} {9,S}
4  C u0 p0 c0 {2,B} {6,B} {10,S}
5  C u0 p0 c0 {3,B} {6,B} {11,S}
6  C u1 p0 c0 {4,B} {5,B}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.21158,-0.0177227,0.000198933,-3.18526e-07,1.64804e-10,40225.4,9.55536], Tmin=(10,'K'), Tmax=(613.249,'K')),
            NASAPolynomial(coeffs=[-0.92764,0.045662,-2.91507e-05,8.83329e-09,-1.02084e-12,40294.2,27.2577], Tmin=(613.249,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (334.452,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'C=C': 3, 'C-H': 5}

External symmetry: 2, optical isomers: 1

Geometry:
C       0.15316900   -1.54713600    0.07017700
C      -1.12617300   -1.04555400    0.05185700
C      -1.25232800    0.34949200   -0.01146200
C      -0.11433800    1.15492300   -0.05238000
C       1.15957900    0.58739200   -0.03103500
C       1.30940900   -0.80531900    0.03209100
H      -2.00138000   -1.68483900    0.08422900
H      -2.23983800    0.79879400   -0.02844500
H      -0.22103100    2.23258200   -0.10124500
H       2.03988700    1.22092400   -0.06316900
H       2.29304500   -1.26126000    0.04938300
""",
)

entry(
    index = 99,
    label = "S115",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u1 p0 c0 {1,S} {5,S} {10,S}
4  C u0 p0 c0 {2,D} {6,S} {11,S}
5  C u0 p0 c0 {3,S} {6,D} {13,S}
6  C u0 p0 c0 {4,S} {5,D} {12,S}
7  C u1 p0 c0 {2,S} {14,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90208,0.0057356,0.00017482,-3.17926e-07,1.79383e-10,40403.6,11.4109], Tmin=(10,'K'), Tmax=(551.657,'K')),
            NASAPolynomial(coeffs=[-1.47913,0.0653919,-4.35059e-05,1.37318e-08,-1.64965e-12,40683.3,31.325], Tmin=(551.657,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (335.894,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (353.365,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 5, 'C=C': 2, 'C-H': 8}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 2, max scan energy: 30.00 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -2.29653100   -0.06928300   -0.67010300
C      -0.91442500   -0.11397300   -0.41810000
C      -0.27557000   -1.25156700    0.02424700
C       1.15955800   -1.29106300    0.28390500
C       1.92082400   -0.16329900    0.08650800
C       1.34387400    1.03378200   -0.36249100
C      -0.11397500    1.15371700   -0.64954800
H      -2.77526300    0.83793500   -1.01756600
H      -2.91958200   -0.94316800   -0.52286500
H      -0.85871100   -2.15231100    0.18621100
H       1.60879400   -2.21314900    0.63059500
H       2.98827700   -0.19211400    0.27948000
H       1.96443200    1.91034000   -0.51092700
H      -0.55785800    1.96669500   -0.04779500
H      -0.27387100    1.48750300   -1.69026600
""",
)

entry(
    index = 100,
    label = "S116",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {2,S} {6,D} {12,S}
5  C u0 p0 c0 {3,D} {6,S} {13,S}
6  C u0 p0 c0 {4,D} {5,S} {14,S}
7  C u1 p0 c0 {1,S} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92027,0.00512903,0.000193356,-3.83985e-07,2.4467e-10,32797,12.6164], Tmin=(10,'K'), Tmax=(463.788,'K')),
            NASAPolynomial(coeffs=[-1.43782,0.0643365,-4.0167e-05,1.21081e-08,-1.40751e-12,33154.2,32.8424], Tmin=(463.788,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (272.673,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 5, 'C=C': 2, 'C-H': 9}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 2, max scan energy: 4.47 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       2.03866700    0.54809700    0.16171300
C       0.88383600   -0.00738900   -0.61537500
C       0.25305700   -1.08776300    0.25846900
C       0.59919400   -2.37725100    0.12070000
C       1.53899900   -2.79970400   -0.91780500
C       1.88970000   -1.96285800   -1.90390700
C       1.28544000   -0.58403900   -1.99346500
H       2.95847100   -0.02048900    0.23544600
H       1.89388800    1.37016600    0.85238000
H       0.15180700    0.79021100   -0.77581200
H      -0.40966400   -0.76822600    1.05583500
H       0.19803900   -3.12692000    0.79523000
H       1.93610600   -3.80874500   -0.88056400
H       2.57017700   -2.28240500   -2.68663100
H       0.38904100   -0.64190000   -2.62930700
H       1.96868400    0.11005700   -2.49186300
""",
)

entry(
    index = 101,
    label = "S117",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,D} {9,S}
3  C u0 p0 c0 {5,D} {7,S} {9,S}
4  C u0 p0 c0 {2,D} {6,S} {16,S}
5  C u0 p0 c0 {3,D} {6,S} {14,S}
6  C u1 p0 c0 {4,S} {5,S} {15,S}
7  C u0 p0 c0 {3,S} {8,D} {13,S}
8  C u0 p0 c0 {7,D} {17,S} {18,S}
9  O u0 p2 c0 {2,S} {3,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70321,0.0257624,0.000144359,-2.87259e-07,1.63894e-10,5116.88,12.8686], Tmin=(10,'K'), Tmax=(580.892,'K')),
            NASAPolynomial(coeffs=[1.27786,0.0707156,-4.4675e-05,1.34144e-08,-1.54149e-12,4921.98,19.1491], Tmin=(580.892,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (42.4896,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (424.038,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 4, 'C=C': 3, 'C-H': 9}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 49.54 kJ/mol
pivots: [7, 8], dihedral: [6, 7, 8, 16], rotor symmetry: 3, max scan energy: 8.08 kJ/mol
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 1

Geometry:
C       2.61926000    1.48375500    0.56453900
C       2.31401300    0.18076100    0.37599000
C       1.00908700   -0.35188400    0.15950100
C       0.70495900   -1.69236300   -0.03330300
C      -0.60087200   -2.11214900   -0.23669000
C      -1.62718300   -1.11842400   -0.24163400
C      -1.31631700    0.18531700   -0.05233400
C      -2.25497600    1.34180800   -0.02787400
O      -0.01610500    0.58886400    0.14849000
H       3.64319800    1.79702500    0.72216000
H       1.85403200    2.24896900    0.56369500
H       3.10659700   -0.56183100    0.38271300
H       1.52594800   -2.39927300   -0.01904800
H      -0.83953400   -3.15596000   -0.38704100
H      -2.66418500   -1.38766200   -0.39564600
H      -2.19804500    1.86372900    0.93307900
H      -3.28084600    1.00950900   -0.18795100
H      -1.99270500    2.06715500   -0.80515200
""",
)

entry(
    index = 102,
    label = "S118",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {8,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {3,S} {5,S} {12,D}
3  C u0 p0 c0 {2,S} {4,D} {14,S}
4  C u0 p0 c0 {3,D} {6,S} {15,S}
5  C u0 p0 c0 {2,S} {7,D} {13,S}
6  C u0 p0 c0 {4,S} {8,D} {16,S}
7  C u0 p0 c0 {5,D} {17,S} {18,S}
8  C u1 p0 c0 {1,S} {6,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 O u0 p2 c0 {2,D}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.19284,0.0819293,-0.000172947,3.56508e-07,-2.95302e-10,27606.5,13.6288], Tmin=(10,'K'), Tmax=(399.452,'K')),
            NASAPolynomial(coeffs=[2.66218,0.0671865,-4.22696e-05,1.2716e-08,-1.46843e-12,27808.9,17.7049], Tmin=(399.452,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (229.516,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (419.881,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 4, 'C=C': 3, 'C-H': 9, 'C=O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 25.81 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 6], rotor symmetry: 1, max scan energy: 37.09 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 8], invalidation reason: Inconsistent initial and final conformersInconsistent initial and final conformers
pivots: [8, 9], dihedral: [7, 8, 9, 16], rotor symmetry: 3, max scan energy: 3.63 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       4.15648900    0.64321300   -0.15870000
C       3.05588500    0.21108100    0.45539300
C       1.74913000    0.11082100   -0.26486200
O       1.64237900    0.42146500   -1.44282300
C       0.60260300   -0.38379400    0.53067300
C      -0.62101300   -0.51366500   -0.01642400
C      -1.79969500   -0.98988200    0.68839100
C      -2.99804700   -1.11290100    0.13841700
C      -3.70069800   -0.91485100   -1.13169900
H       5.10838800    0.71983700    0.35341100
H       4.11155800    0.93034700   -1.20373100
H       3.07825800   -0.08154200    1.50115100
H       0.77312600   -0.64083200    1.57221800
H      -0.72326700   -0.23918700   -1.06314900
H      -1.66919500   -1.25839700    1.73697100
H      -4.52150700   -0.19905900   -1.01841700
H      -3.02702200   -0.53425200   -1.91369600
H      -4.13456600   -1.85396100   -1.49051700
""",
)

entry(
    index = 103,
    label = "S119",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,D} {11,S}
2  C u0 p0 c0 {1,S} {3,D} {12,S}
3  C u0 p0 c0 {2,D} {4,S} {13,S}
4  C u0 p0 c0 {3,S} {6,S} {9,D}
5  C u0 p0 c0 {1,D} {7,S} {10,S}
6  C u0 p0 c0 {4,S} {8,D} {14,S}
7  C u1 p0 c0 {5,S} {15,S} {16,S}
8  C u0 p0 c0 {6,D} {17,S} {18,S}
9  O u0 p2 c0 {4,D}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41438,0.0516403,4.96432e-05,-1.44412e-07,8.44507e-11,12344.6,12.0769], Tmin=(10,'K'), Tmax=(633.651,'K')),
            NASAPolynomial(coeffs=[5.02804,0.0658502,-4.17468e-05,1.25009e-08,-1.43012e-12,11650.3,1.16351], Tmin=(633.651,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (102.563,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (415.724,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 4, 'C=C': 3, 'C-H': 9, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 2, max scan energy: 68.97 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 45.52 kJ/mol
pivots: [6, 8], dihedral: [5, 6, 8, 9], rotor symmetry: 1, max scan energy: 26.19 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 2, max scan energy: 49.20 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 1

Geometry:
C       2.50972000    1.31433900    2.92338400
C       2.34194400    0.74844000    1.70263500
C       1.45395900    1.23833600    0.70764800
C       1.29119000    0.64630100   -0.54415200
C       0.43621600    1.10324900   -1.52526300
C       0.32116200    0.42365600   -2.81963800
O       0.97863400   -0.57925400   -3.08703700
C      -0.63913200    1.01501600   -3.79907700
C      -0.82365600    0.47959500   -5.00528300
H       1.95629800    2.20084600    3.21483400
H       3.20006600    0.90280100    3.64879800
H       2.91769300   -0.13997700    1.45252800
H       0.87129800    2.12649300    0.94362200
H       1.87138100   -0.24157700   -0.78459400
H      -0.17136900    1.98583200   -1.34752500
H      -1.18623800    1.90243500   -3.49365500
H      -0.26775600   -0.40667000   -5.29143100
H      -1.51822100    0.90233900   -5.72150000
""",
)

entry(
    index = 104,
    label = "S120",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,D} {12,S}
3  C u0 p0 c0 {2,D} {6,S} {14,S}
4  C u0 p0 c0 {5,S} {7,D} {13,S}
5  C u0 p0 c0 {4,S} {8,D} {15,S}
6  C u0 p0 c0 {3,S} {8,D} {16,S}
7  C u0 p0 c0 {4,D} {17,S} {18,S}
8  C u0 p0 c0 {5,D} {6,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 O u1 p2 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43256,0.0637521,-3.6388e-05,7.89637e-09,-5.12311e-14,27207.6,17.5758], Tmin=(10,'K'), Tmax=(1336.41,'K')),
            NASAPolynomial(coeffs=[15.8316,0.0366196,-1.71346e-05,3.87923e-09,-3.44972e-13,23002.5,-49.1718], Tmin=(1336.41,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (226.194,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (419.881,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-C': 3, 'C=C': 4, 'C-H': 9}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for S120 exists which is 2.39 kJ/mol lower.Another conformer for S120 exists which is 2.39 kJ/mol lower.
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 27.01 kJ/mol
pivots: [8, 9], dihedral: [7, 8, 9, 16], rotor symmetry: 3, max scan energy: 7.50 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 6], rotor symmetry: 1, max scan energy: 0.34 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.11277300    1.57858900   -0.56645100
C      -3.04046100    0.65677100   -0.31127600
C      -2.78888100   -0.79900400   -0.11825500
O      -3.73124600   -1.57460000    0.11603200
C      -1.46825800   -1.28064300   -0.20890000
C      -0.26856700   -1.79599600   -0.19805200
C       0.45340200   -2.32621800   -1.35638700
C       1.68996700   -2.83219700   -1.28052200
C       2.46255800   -3.39146300   -2.43392800
H      -1.06282800    1.32001100   -0.65727400
H      -2.37597400    2.62209900   -0.69297400
H      -4.09013700    0.92017900   -0.22186700
H       0.25957800   -1.84019000    0.75993400
H      -0.06664300   -2.29921500   -2.30986000
H       2.18654600   -2.84931600   -0.31141200
H       1.89535200   -3.33583000   -3.36549800
H       2.72702900   -4.44001000   -2.25674000
H       3.40569700   -2.85132500   -2.57403700
""",
)

entry(
    index = 105,
    label = "S121",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,D} {12,S}
3  C u0 p0 c0 {2,D} {4,S} {15,S}
4  C u0 p0 c0 {3,S} {5,D} {14,S}
5  C u0 p0 c0 {4,D} {6,S} {13,S}
6  C u0 p0 c0 {5,S} {8,D} {16,S}
7  C u0 p0 c0 {8,D} {17,S} {18,S}
8  C u0 p0 c0 {6,D} {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.14354,0.0898396,-0.000243729,5.70203e-07,-5.04704e-10,26144.8,16.0376], Tmin=(10,'K'), Tmax=(378.641,'K')),
            NASAPolynomial(coeffs=[2.34339,0.068866,-4.40669e-05,1.3412e-08,-1.56109e-12,26416.3,21.9063], Tmin=(378.641,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (217.36,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (419.881,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-C': 3, 'C=C': 4, 'C-H': 9}
1D rotors:
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 6], invalidation reason: Another conformer for S121 exists which is 4.45 kJ/mol lower.Another conformer for S121 exists which is 4.45 kJ/mol lower.
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 35.66 kJ/mol
pivots: [8, 9], dihedral: [7, 8, 9, 16], rotor symmetry: 3, max scan energy: 7.33 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 0.29 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 1

Geometry:
C      -3.67205300    1.20468700   -0.21400700
C      -3.05353100    0.08729400   -0.42443400
C      -2.45008200   -1.16616200   -0.67016400
O      -3.15341800   -2.14107000   -0.98702000
C      -0.98306800   -1.28812700   -0.54307900
C      -0.13511200   -0.29809000   -0.20697100
C       1.29853600   -0.45408500   -0.09189100
C       2.13280900    0.54226400    0.24431300
C       3.61753000    0.41929500    0.37304800
H      -4.04642300    1.47954100    0.77300600
H      -3.85472800    1.92235500   -1.01492900
H      -0.61744800   -2.28954100   -0.75188800
H      -0.53564300    0.69349100   -0.00434100
H       1.70395800   -1.44381200   -0.29353800
H       1.71021900    1.52626500    0.44270100
H       3.94713100    0.68646900    1.38366500
H       3.96007000   -0.59517300    0.15853200
H       4.12884200    1.10619800   -0.31112200
""",
)

entry(
    index = 106,
    label = "S122",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {7,D} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {12,S}
4  C u0 p0 c0 {2,S} {6,D} {14,S}
5  C u0 p0 c0 {3,D} {6,S} {16,S}
6  C u0 p0 c0 {4,D} {5,S} {15,S}
7  C u0 p0 c0 {2,D} {8,S} {13,S}
8  C u1 p0 c0 {7,S} {17,S} {18,S}
9  O u0 p2 c0 {1,S} {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84944,0.00905912,0.000230575,-4.46555e-07,2.66267e-10,12232,13.7165], Tmin=(10,'K'), Tmax=(535.521,'K')),
            NASAPolynomial(coeffs=[-1.01698,0.077506,-5.10518e-05,1.59638e-08,-1.90278e-12,12293,29.8578], Tmin=(535.521,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (101.647,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 4, 'C=C': 3, 'C-H': 9}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 45.16 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       2.83818100    0.48411800    1.28956000
C       2.24631400    0.26618500    0.09848700
C       2.92438600    0.25404700   -1.17173600
C       2.23318500   -0.01496300   -2.35540900
C       2.64167800    0.13411500   -3.68097900
C       3.93251100    0.49878200   -4.16188700
C       5.08184700    0.46654500   -3.44097600
C       5.13459200   -0.08878700   -2.05399400
O       4.24223900    0.56721700   -1.11554100
H       2.26186100    0.49131200    2.20615200
H       3.90348200    0.66226000    1.36016600
H       1.17428500    0.10029100    0.05486900
H       1.19449900   -0.29091200   -2.20416100
H       1.86880600    0.00308000   -4.43156400
H       3.98826900    0.81511700   -5.20012100
H       6.01048500    0.80607200   -3.88599100
H       4.88556200   -1.15713300   -2.05500900
H       6.12433100    0.03503500   -1.61602100
""",
)

entry(
    index = 107,
    label = "S123",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,D} {13,S}
4  C u0 p0 c0 {2,S} {6,D} {14,S}
5  C u0 p0 c0 {3,D} {8,S} {15,S}
6  C u0 p0 c0 {4,D} {7,S} {16,S}
7  C u0 p0 c0 {6,S} {8,D} {17,S}
8  C u0 p0 c0 {5,S} {7,D} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88423,0.00750797,0.000237509,-4.88363e-07,3.18925e-10,14516.2,14.0015], Tmin=(10,'K'), Tmax=(465.338,'K')),
            NASAPolynomial(coeffs=[-1.69099,0.0757578,-4.80109e-05,1.45535e-08,-1.69268e-12,14815,34.2692], Tmin=(465.338,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (120.671,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (432.353,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 5, 'C=C': 3, 'C-H': 9, 'C-O': 1}

External symmetry: 1, optical isomers: 2

Geometry:
O       0.69125400    2.66241600   -1.54445500
C       0.43805900    1.75774600   -0.73115100
C      -0.90488800    1.29174500   -0.56104900
C      -1.37529200    0.39938200    0.53434000
C      -1.39791900   -1.08822400    0.12248200
C      -0.07517400   -1.74726900   -0.14335200
C       1.19133500   -1.32741300   -0.00277300
C       1.81881400   -0.06125400    0.40375700
C       1.53925300    1.22056700    0.11411900
H      -1.62211900    1.68474000   -1.27598800
H      -2.39364200    0.68294000    0.81875400
H      -0.74259900    0.51251400    1.41810900
H      -2.03132400   -1.21055300   -0.76498900
H      -1.90287100   -1.65960600    0.91372600
H      -0.18379900   -2.78260300   -0.46165000
H       1.94206600   -2.09280700   -0.19410700
H       2.75382800   -0.22173400    0.93863700
H       2.25501800    1.97941400    0.41558800
""",
)

entry(
    index = 108,
    label = "S124",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,D}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {7,S} {14,S}
6  C u0 p0 c0 {3,S} {7,D} {16,S}
7  C u0 p0 c0 {5,S} {6,D} {15,S}
8  C u1 p0 c0 {1,S} {17,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 O u0 p2 c0 {3,D}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64011,0.0308627,0.000109924,-2.26052e-07,1.29608e-10,16720,13.7637], Tmin=(10,'K'), Tmax=(570.052,'K')),
            NASAPolynomial(coeffs=[0.936609,0.0693661,-4.27899e-05,1.26536e-08,-1.43962e-12,16710.9,22.5033], Tmin=(570.052,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (138.966,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 6, 'C=C': 2, 'C-H': 9, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 2, max scan energy: 6.28 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.41393000    0.51598800    0.70540500
C      -0.98126100    0.15041200    0.53600400
C      -0.08139400    0.78033000    1.63636600
C       1.35395000    0.96425700    1.23621100
C       2.13458800    0.01703700    0.69317300
C       1.77129800   -1.37039700    0.44944900
C       0.55965300   -1.96346700    0.38723700
C      -0.79581200   -1.37322900    0.43202600
O      -1.75730000   -2.11454900    0.33523500
H      -2.69174700    1.55667800    0.81747100
H      -3.18000400   -0.24261800    0.64342400
H      -0.61270000    0.54848700   -0.42822800
H      -0.13875800    0.15793900    2.54116000
H      -0.50395500    1.74896400    1.91081000
H       1.79391100    1.94006200    1.42127600
H       3.16643400    0.27213200    0.47099500
H       2.62326600   -2.03173000    0.30799400
H       0.52139300   -3.03683000    0.23140700
""",
)



entry(
    index = 109,
    label = "S125",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {5,D} {6,S} {9,S}
3  C u1 p0 c0 {1,S} {5,S} {11,S}
4  C u0 p0 c0 {1,S} {7,D} {12,S}
5  C u0 p0 c0 {2,D} {3,S} {14,S}
6  C u0 p0 c0 {2,S} {8,D} {13,S}
7  C u0 p0 c0 {4,D} {17,S} {18,S}
8  C u0 p0 c0 {6,D} {15,S} {16,S}
9  O u0 p2 c0 {1,S} {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83853,0.0109104,0.000255758,-5.72461e-07,4.01333e-10,14437.7,14.6308], Tmin=(10,'K'), Tmax=(448.699,'K')),
            NASAPolynomial(coeffs=[-0.181699,0.0741991,-4.75804e-05,1.45742e-08,-1.70838e-12,14522.1,27.7251], Tmin=(448.699,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (120.021,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (432.353,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 4, 'C=C': 3, 'C-H': 9}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 8], invalidation reason: Another conformer for S125 exists which is 2.46 kJ/mol lower.Another conformer for S125 exists which is 2.46 kJ/mol lower.
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
C       3.05406300    0.14358100   -1.02636000
C       2.56362600   -0.38275200    0.12828300
C       1.24537700   -0.22642400    0.60229700
C       0.63628300   -0.72181700    1.78107900
C      -0.65779500   -0.30936800    1.81820700
C      -0.92645500    0.50842200    0.57894700
C      -2.04163100   -0.03006900   -0.28414100
C      -1.89845000   -0.50139000   -1.51630300
O       0.33823400    0.50225400   -0.12152000
H       4.08131800   -0.02339400   -1.32294500
H       2.43245100    0.74584700   -1.67649000
H       3.21164300   -0.97803300    0.76472600
H       1.14473200   -1.33392900    2.51219900
H      -1.40080100   -0.51655700    2.57360400
H      -1.15007600    1.55810500    0.82889900
H      -3.02052900   -0.00746800    0.19015600
H      -2.74829700   -0.87772400   -2.07352800
H      -0.92988500   -0.52124400   -2.00043600
""",
)

entry(
    index = 110,
    label = "S126",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,D} {13,S}
4  C u0 p0 c0 {1,S} {8,D} {12,S}
5  C u0 p0 c0 {2,S} {7,D} {14,S}
6  C u0 p0 c0 {3,D} {7,S} {16,S}
7  C u0 p0 c0 {5,D} {6,S} {15,S}
8  C u0 p0 c0 {4,D} {17,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 O u1 p2 c0 {7,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76054,0.0188877,0.000211884,-4.93689e-07,3.54237e-10,12039.7,13.7467], Tmin=(10,'K'), Tmax=(436.734,'K')),
            NASAPolynomial(coeffs=[0.303431,0.0722811,-4.6134e-05,1.40975e-08,-1.65062e-12,12134.5,25.1887], Tmin=(436.734,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (100.089,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-C': 5, 'C=C': 3, 'C-H': 9}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 14.64 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.71893400    0.74486000    0.43201200
C      -1.40933700    0.53717100    0.52342900
C      -0.58143200   -0.21804300   -0.49629100
C       0.39163800    0.74083100   -1.14959500
C       1.66853100    0.86242400   -0.76804900
C       2.24994500    0.04308700    0.32570700
O       3.36957300    0.28590800    0.79186000
C       1.44044700   -1.04745400    0.80418800
C       0.16056500   -1.42107700    0.13918600
H      -3.29919800    0.36844100   -0.40533700
H      -3.25992900    1.29882400    1.19073000
H      -0.85528500    0.93490800    1.37163000
H      -1.26555500   -0.59920700   -1.26110100
H      -0.01396200    1.39528600   -1.91597100
H       2.33237100    1.59496800   -1.21415400
H       1.85484100   -1.65717800    1.59966400
H       0.39422500   -2.13927300   -0.66535500
H      -0.50146300   -1.95388300    0.82796800
""",
)

entry(
    index = 111,
    label = "S127",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {11,D}
4  C u0 p0 c0 {1,S} {6,D} {12,S}
5  C u0 p0 c0 {1,S} {8,D} {13,S}
6  C u0 p0 c0 {3,S} {4,D} {14,S}
7  C u1 p0 c0 {2,S} {15,S} {16,S}
8  C u0 p0 c0 {5,D} {17,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 O u0 p2 c0 {3,D}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60703,0.0443213,2.93233e-05,-6.73976e-08,2.90477e-11,16718.3,14.9034], Tmin=(10,'K'), Tmax=(878.979,'K')),
            NASAPolynomial(coeffs=[5.44201,0.0584307,-3.30833e-05,9.00546e-09,-9.51191e-13,15528.1,1.35192], Tmin=(878.979,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (139.02,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 6, 'C=C': 2, 'C-H': 9, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 1, max scan energy: 4.05 kJ/mol
* Invalidated! pivots: [7, 8], dihedral: [2, 7, 8, 9], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.79398100   -1.10780400    0.62166900
C      -0.97313200   -0.41514900   -0.40148300
C      -0.73588700   -1.26141000   -1.67499900
O      -0.49026400   -2.44420100   -1.69524300
C      -0.87260000   -0.34678900   -2.83041100
C      -1.29403700    0.85460700   -2.42258400
C      -1.51479000    0.94881700   -0.92325500
C      -0.86262900    2.15550800   -0.30280600
C      -1.50740500    3.12387900    0.34099400
H      -2.30306300   -0.54686500    1.39511700
H      -1.75877100   -2.18777500    0.68383100
H       0.04477100   -0.23836700   -0.00613500
H      -0.68289800   -0.66202400   -3.84808500
H      -1.49303300    1.70270500   -3.06872200
H      -2.59497100    1.00588300   -0.73875300
H       0.22034400    2.20960000   -0.40663100
H      -2.58595700    3.10447100    0.46535000
H      -0.98133600    3.96913700    0.76956000
""",
)

entry(
    index = 112,
    label = "S128",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {3,D} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {2,D} {12,S}
4  C u1 p0 c0 {1,S} {5,S} {11,S}
5  C u0 p0 c0 {4,S} {7,D} {13,S}
6  C u0 p0 c0 {2,S} {8,D} {14,S}
7  C u0 p0 c0 {5,D} {15,S} {16,S}
8  C u0 p0 c0 {6,D} {17,S} {18,S}
9  O u0 p2 c0 {1,S} {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68356,0.0239093,0.000263607,-7.17906e-07,5.82685e-10,30112.4,14.3082], Tmin=(10,'K'), Tmax=(412.921,'K')),
            NASAPolynomial(coeffs=[3.09967,0.069296,-4.55941e-05,1.43211e-08,-1.71492e-12,29821.9,12.5073], Tmin=(412.921,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (250.368,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (424.038,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 4, 'C=C': 3, 'C-H': 9}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 13.69 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 29.27 kJ/mol
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
C       3.88916300    0.11931300    0.92126900
C       2.63290600    0.53723500    0.53177000
C       1.69184600   -0.25432100   -0.11135000
C       0.37138200    0.23691600   -0.55152000
C      -0.10914600   -0.10589400   -1.95063300
C      -1.06972800   -0.86093900   -1.38666800
C      -2.17801100   -1.69299700   -1.79116000
C      -2.98205400   -2.31450000   -0.92379700
O      -0.74671700   -0.64101100   -0.05261700
H       4.57502900    0.78830500    1.42458900
H       4.22466000   -0.89528800    0.73768700
H       2.35507100    1.56888200    0.74275900
H       1.91815100   -1.29300700   -0.33545800
H       0.17403000    1.26106500   -0.22524600
H       0.21113600    0.14816000   -2.94658400
H      -2.32685900   -1.78863400   -2.86238700
H      -3.80666000   -2.93132800   -1.25923400
H      -2.82926900   -2.21644400    0.14456500
""",
)

entry(
    index = 113,
    label = "S129",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {7,S} {9,S} {10,S}
2  C u0 p0 c0 {5,D} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {5,S} {12,S}
5  C u0 p0 c0 {2,D} {4,S} {13,S}
6  C u0 p0 c0 {2,S} {8,D} {14,S}
7  C u1 p0 c0 {1,S} {15,S} {16,S}
8  C u0 p0 c0 {6,D} {17,S} {18,S}
9  O u0 p2 c0 {1,S} {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8005,0.0132322,0.000258471,-5.83533e-07,4.03884e-10,23805.3,14.6512], Tmin=(10,'K'), Tmax=(469.219,'K')),
            NASAPolynomial(coeffs=[0.955808,0.0733283,-4.82349e-05,1.50471e-08,-1.78565e-12,23677.6,22.0178], Tmin=(469.219,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (197.892,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (424.038,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-C': 4, 'C=C': 3, 'C-H': 9}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 2, max scan energy: 4.00 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 36.10 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.04481100   -0.43240700    1.34672000
C      -1.41412700   -0.44597100   -0.00359600
C      -2.38007800    0.08202700   -1.03832900
C      -2.36573900    1.39349100   -1.33012500
C      -1.34331300    2.24489100   -0.76416300
C      -0.26713800    1.67635800   -0.16301000
C       0.89123700    2.42502700    0.29700900
C       1.95159500    1.88656000    0.90866500
O      -0.16652700    0.32563700   -0.01719700
H      -2.16307600   -1.34002400    1.92444600
H      -2.42573500    0.49815800    1.74865800
H      -1.08633500   -1.45516200   -0.25563900
H      -3.08978700   -0.60970200   -1.47529500
H      -3.08446700    1.81714500   -2.02338500
H      -1.37855600    3.31880400   -0.88663100
H       0.85467400    3.49220900    0.10020900
H       1.99872700    0.82407900    1.11095000
H       2.79211700    2.49730000    1.21465800
""",
)

entry(
    index = 114,
    label = "S130",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {6,S} {8,D}
3  C u0 p0 c0 {1,S} {5,D} {12,S}
4  C u1 p0 c0 {2,S} {5,S} {14,S}
5  C u0 p0 c0 {3,D} {4,S} {15,S}
6  C u0 p0 c0 {2,S} {7,D} {13,S}
7  C u0 p0 c0 {6,D} {16,S} {17,S}
8  C u0 p0 c0 {2,D} {18,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2269,0.0760213,-0.00012953,2.34897e-07,-1.8066e-10,16426.6,14.6335], Tmin=(10,'K'), Tmax=(428.597,'K')),
            NASAPolynomial(coeffs=[2.62884,0.0660911,-4.04883e-05,1.19532e-08,-1.36176e-12,16620.3,18.6741], Tmin=(428.597,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (136.558,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 4, 'C=C': 3, 'C-H': 9, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
* Invalidated! pivots: [3, 6], dihedral: [2, 3, 6, 7], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
* Invalidated! pivots: [6, 7], dihedral: [3, 6, 7, 8], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [8, 9], dihedral: [7, 8, 9, 16], rotor symmetry: 3, max scan energy: 5.54 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: 
* Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 9], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
C       3.17278200    1.38783300    0.65658400
C       2.74812800    0.15633800    0.95160700
C       1.47159100   -0.43708700    0.51411600
C       1.30602600   -1.74141700    0.76436500
O       1.16547100   -2.87529400    0.96977500
C       0.40996500    0.31759800   -0.11635600
C      -0.68803900   -0.22274500   -0.80072700
C      -1.72846300    0.50262300   -1.32087900
C      -2.88031100   -0.08216800   -2.07323800
H       4.11846200    1.74750300    1.04187000
H       2.60960000    2.06618500    0.02745900
H       3.37629800   -0.47822300    1.57024000
H       0.46983300    1.39360100    0.00508100
H      -0.71608600   -1.30390000   -0.94231300
H      -1.72304700    1.58275700   -1.18865200
H      -3.83675900    0.15195700   -1.58917400
H      -2.94384600    0.32435900   -3.09053800
H      -2.80079200   -1.16932900   -2.15119800
""",
)

entry(
    index = 115,
    label = "S131",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,D}
3  C u0 p0 c0 {2,S} {4,D} {14,S}
4  C u0 p0 c0 {3,D} {5,S} {13,S}
5  C u0 p0 c0 {4,S} {8,D} {16,S}
6  C u0 p0 c0 {7,D} {8,S} {15,S}
7  C u0 p0 c0 {6,D} {17,S} {18,S}
8  C u1 p0 c0 {5,D} {6,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 O u0 p2 c0 {2,D}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70213,0.0632004,-3.66399e-05,9.12949e-09,-6.52615e-13,22230.9,16.2299], Tmin=(10,'K'), Tmax=(1610.92,'K')),
            NASAPolynomial(coeffs=[27.3029,0.0161635,-3.61071e-06,-8.27485e-11,8.5411e-14,13126.5,-113.541], Tmin=(1610.92,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (184.82,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (415.724,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 4, 'C=C': 3, 'C-H': 9, 'C=O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 0.02 kJ/mol (set as a FreeRotor)
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 32.64 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 33.15 kJ/mol
pivots: [7, 8], dihedral: [6, 7, 8, 16], rotor symmetry: 3, max scan energy: 3.15 kJ/mol
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
C       3.48373100    0.59845600   -1.86897200
C       3.23568000    0.05644600   -0.60893600
C       2.07447200   -0.48766400   -0.19965000
C       0.93966000   -1.00033700    0.21548900
C       0.58200500   -2.40518100    0.09056100
C      -0.57885000   -2.93412000    0.51480900
C      -0.87219300   -4.38200000    0.35260600
C      -2.21706900   -4.85547400    0.87233000
O      -0.08350400   -5.14960300   -0.16630700
H       4.45479700    1.01113500   -2.10650000
H       2.71750400    0.61519900   -2.63299100
H       4.04756000    0.06461000    0.11878900
H       0.20377000   -0.34477600    0.68725200
H       1.30153100   -3.07157900   -0.37651800
H      -1.33192400   -2.30993900    0.98850900
H      -3.02899900   -4.31981600    0.36946300
H      -2.32149200   -5.92555600    0.70046800
H      -2.30716100   -4.64296900    1.94273800
""",
)

entry(
    index = 116,
    label = "S132",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {11,S}
3  C u0 p0 c0 {2,D} {4,S} {12,S}
4  C u0 p0 c0 {3,S} {7,D} {14,S}
5  C u0 p0 c0 {6,D} {7,S} {13,S}
6  C u0 p0 c0 {5,D} {15,S} {16,S}
7  C u1 p0 c0 {4,D} {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6183,0.0356339,7.25579e-05,-2.2128e-07,1.84394e-10,38970.9,15.0513], Tmin=(10,'K'), Tmax=(312.634,'K')),
            NASAPolynomial(coeffs=[1.84469,0.0583261,-3.63166e-05,1.08828e-08,-1.25506e-12,39081.8,21.5458], Tmin=(312.634,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (324.019,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (369.994,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'C=C': 3, 'C-H': 9}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 0.02 kJ/mol (set as a FreeRotor)
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 28.11 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 14], rotor symmetry: 3, max scan energy: 7.57 kJ/mol
* Invalidated! pivots: [1, 2], dihedral: [8, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
C       3.35103800    0.91301000   -0.75333600
C       2.89716500   -0.13733900    0.04298200
C       3.60047100   -1.23983000    0.37176500
C       4.26874300   -2.32389200    0.67671200
C       5.12697500   -2.49056200    1.85091300
C       5.79427500   -3.61638200    2.13111700
C       6.67922500   -3.81976300    3.32238800
H       2.71241300    1.76104600   -0.96197500
H       4.34667800    0.90417500   -1.17796400
H       1.88400100   -0.06795300    0.44087100
H       4.19370300   -3.18880400    0.01176800
H       5.20855800   -1.63470300    2.51660600
H       5.69791000   -4.46105800    1.45013000
H       6.32698000   -4.65465700    3.93914200
H       7.70244100   -4.06785500    3.01742400
H       6.71965200   -2.92714200    3.95090700
""",
)

entry(
    index = 117,
    label = "S133",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {8,S} {11,S} {12,S}
2  C u0 p0 c0 {6,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {7,D}
5  C u0 p0 c0 {1,S} {4,S} {9,D}
6  C u0 p0 c0 {2,S} {7,S} {8,D}
7  C u0 p0 c0 {4,D} {6,S} {10,S}
8  C u0 p0 c0 {1,S} {6,D} {19,S}
9  C u0 p0 c0 {5,D} {20,S} {21,S}
10 O u0 p2 c0 {7,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61322,0.0379409,0.000269071,-1.02237e-06,1.2643e-09,-11410.4,13.2516], Tmin=(10,'K'), Tmax=(204.763,'K')),
            NASAPolynomial(coeffs=[1.38784,0.0814136,-4.93932e-05,1.44922e-08,-1.64335e-12,-11319.3,20.4585], Tmin=(204.763,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-94.819,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (519.654,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 11, 'C-O': 1, 'H-O': 1, 'C-C': 6, 'C=C': 3}
1D rotors:
pivots: [5, 6], dihedral: [4, 5, 6, 16], rotor symmetry: 3, max scan energy: 8.78 kJ/mol
pivots: [7, 8], dihedral: [5, 7, 8, 19], rotor symmetry: 1, max scan energy: 16.51 kJ/mol
pivots: [9, 10], dihedral: [2, 9, 10, 20], rotor symmetry: 3, max scan energy: 3.77 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.55119500   -1.06783700   -0.24848200
C      -1.27819900   -0.75355900    0.04794100
C      -0.29327900   -1.84421000    0.43409400
C       1.14737700   -1.50582700    0.18694800
C       1.56717800   -0.24596400    0.01778400
C       3.01443700    0.11978000   -0.18079600
C       0.56760300    0.83488900    0.02868200
O       1.14033200    2.07530600   -0.03561900
C      -0.77574000    0.62391500    0.05926000
C      -1.76256800    1.76297300   -0.00555600
H      -2.87939100   -2.10091200   -0.26869100
H      -3.29954600   -0.31971300   -0.47577900
H      -0.40664200   -2.04515100    1.51212600
H      -0.55850400   -2.78072700   -0.06497000
H       1.86648600   -2.31920000    0.20041200
H       3.16461100    0.64518800   -1.12823300
H       3.36430800    0.79233800    0.60727700
H       3.63802800   -0.77592700   -0.17666000
H       0.44917100    2.74326300   -0.08536300
H      -2.62340300    1.56154800    0.63677900
H      -1.34353900    2.71382500    0.34060700
H      -2.14543700    1.92302900   -1.02052500
""",
)

entry(
    index = 118,
    label = "S134",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
3  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {2,S} {7,D}
5  C u0 p0 c0 {1,S} {6,S} {9,D}
6  C u0 p0 c0 {3,S} {5,S} {8,D}
7  C u0 p0 c0 {4,D} {8,S} {19,S}
8  C u0 p0 c0 {6,D} {7,S} {18,S}
9  C u0 p0 c0 {5,D} {20,S} {21,S}
10 O u0 p2 c0 {1,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5635,0.0396695,0.000146959,-3.53543e-07,2.52236e-10,-9744.99,14.056], Tmin=(10,'K'), Tmax=(363.995,'K')),
            NASAPolynomial(coeffs=[-0.897226,0.0886901,-5.50556e-05,1.64592e-08,-1.89514e-12,-9420.26,31.0683], Tmin=(363.995,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-81.0369,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (532.126,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-H': 11, 'H-O': 1, 'C-C': 6, 'C=C': 3}
1D rotors:
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 13], invalidation reason: Another conformer for S134 exists which is 1.49 kJ/mol lower.Another conformer for S134 exists which is 1.49 kJ/mol lower.
* Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 18], invalidation reason: Another conformer for S134 exists which is 1.55 kJ/mol lower.Another conformer for S134 exists which is 1.55 kJ/mol lower.
* Invalidated! pivots: [9, 10], dihedral: [2, 9, 10, 22], invalidation reason: Another conformer for S134 exists which is 1.54 kJ/mol lower.Another conformer for S134 exists which is 1.54 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.31113400    2.10068600   -0.24062100
C      -0.68395500    0.92704900   -0.05942500
C      -1.39958400   -0.33997800    0.13238500
C      -2.89629100   -0.33768700    0.29593300
C      -0.69240000   -1.49301700    0.12432400
C       0.74806700   -1.53728700   -0.07226600
C       1.49609200   -0.42564700   -0.17036700
C       2.98260700   -0.43050400   -0.37327600
C       0.84436900    0.92750000    0.01408100
O       1.29827800    1.50298600    1.26121100
H      -0.74741000    3.01480000   -0.38860100
H      -2.39010800    2.19103300   -0.23514200
H      -3.39584700    0.06262600   -0.59296900
H      -3.26879600   -1.35021000    0.46014100
H      -3.20738000    0.28247800    1.14326600
H      -1.21333600   -2.43733400    0.24849600
H       1.21911200   -2.51350900   -0.14438200
H       3.24933500    0.04466800   -1.32547100
H       3.47724400    0.14418300    0.41527800
H       3.38576400   -1.44515800   -0.37544400
H       1.23046300    1.62311400   -0.73568200
H       0.97132100    0.93257200    1.96685400
""",
)

entry(
    index = 119,
    label = "S135",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {2,S} {5,D}
5  C u0 p0 c0 {3,S} {4,D} {8,S}
6  C u0 p0 c0 {1,S} {7,S} {9,D}
7  C u0 p0 c0 {6,S} {8,D} {18,S}
8  C u0 p0 c0 {5,S} {7,D} {19,S}
9  C u0 p0 c0 {6,D} {20,S} {21,S}
10 O u0 p2 c0 {1,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54945,0.0490754,4.54343e-05,-8.88702e-08,3.7161e-11,-8706.75,14.5874], Tmin=(10,'K'), Tmax=(872.701,'K')),
            NASAPolynomial(coeffs=[3.7873,0.0737335,-4.12045e-05,1.11222e-08,-1.16836e-12,-9728.77,7.85456], Tmin=(872.701,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-72.3793,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (523.812,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-H': 11, 'H-O': 1, 'C-C': 6, 'C=C': 3}
1D rotors:
pivots: [5, 6], dihedral: [4, 5, 6, 15], rotor symmetry: 3, max scan energy: 1.64 kJ/mol
pivots: [7, 8], dihedral: [5, 7, 8, 18], rotor symmetry: 3, max scan energy: 1.40 kJ/mol
* Invalidated! pivots: [9, 10], dihedral: [2, 9, 10, 22], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
C       3.01202000    0.04252800    0.82489500
C       1.81639700   -0.15186800    0.24516200
C       1.42802600   -1.43406500   -0.31888700
C       0.15340500   -1.68025900   -0.66870400
C      -0.93005300   -0.70518100   -0.49488700
C      -2.30980000   -1.22548400   -0.82160500
C      -0.64799300    0.54519900   -0.07014900
C      -1.64775900    1.65281500    0.12073100
C       0.79967500    0.98183300    0.14708100
O       0.92819500    1.90026500    1.23801600
H       3.27878600    0.99713900    1.25960100
H       3.74457900   -0.75573600    0.87054400
H       2.18454400   -2.20812500   -0.39769700
H      -0.11531400   -2.65701900   -1.05959600
H      -2.54708400   -2.09472400   -0.19824300
H      -3.09774200   -0.48949000   -0.67604400
H      -2.35403400   -1.56345700   -1.86311600
H      -1.67628100    1.98258100    1.16276500
H      -2.65592600    1.37254600   -0.17860400
H      -1.35167700    2.53382900   -0.46096800
H       1.06627800    1.59258400   -0.72823900
H       0.84642100    1.38300400    2.04842600
""",
)

entry(
    index = 120,
    label = "S136",
    molecule = 
"""
1  C u0 p0 c0 {6,S} {8,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {5,S} {8,D}
5  C u0 p0 c0 {3,S} {4,S} {7,D}
6  C u0 p0 c0 {1,S} {7,S} {9,D}
7  C u0 p0 c0 {5,D} {6,S} {10,S}
8  C u0 p0 c0 {1,S} {4,D} {19,S}
9  C u0 p0 c0 {6,D} {20,S} {21,S}
10 O u0 p2 c0 {7,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54617,0.0408529,0.000156929,-4.26798e-07,3.49354e-10,-10954.4,13.5288], Tmin=(10,'K'), Tmax=(314.818,'K')),
            NASAPolynomial(coeffs=[0.0972914,0.0846734,-5.18603e-05,1.53399e-08,-1.75156e-12,-10737.3,26.1816], Tmin=(314.818,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-91.0884,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (523.812,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-H': 11, 'H-O': 1, 'C-C': 6, 'C=C': 3}
1D rotors:
pivots: [5, 6], dihedral: [4, 5, 6, 16], rotor symmetry: 3, max scan energy: 9.79 kJ/mol
pivots: [7, 8], dihedral: [5, 7, 8, 19], rotor symmetry: 3, max scan energy: 4.14 kJ/mol
* Invalidated! pivots: [9, 10], dihedral: [2, 9, 10, 22], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.98824500   -0.09998800    0.68794500
C      -1.75368900   -0.20016200    0.16902200
C      -1.27538900   -1.44352000   -0.54871800
C       0.20764600   -1.66586500   -0.44495200
C       1.05796200   -0.66544200   -0.16813600
C       2.54673800   -0.90421800   -0.10686400
C       0.54801600    0.70155400    0.07162400
C       1.51193200    1.85437100    0.18011400
C      -0.78436800    0.89784400    0.23545200
O      -1.25051800    2.14810300    0.56300300
H      -3.68740400   -0.92621800    0.63642900
H      -3.33102500    0.78598300    1.21004200
H      -1.82892400   -2.31620400   -0.19167500
H      -1.53210500   -1.34395600   -1.61686500
H       0.58199500   -2.66265300   -0.65420600
H       2.77462100   -1.95634800   -0.28560700
H       2.95809900   -0.63065000    0.87028100
H       3.08475000   -0.31215500   -0.85413900
H       2.17488100    1.90007000   -0.68987900
H       0.97624700    2.79854200    0.25477400
H       2.15317400    1.76107300    1.06373800
H      -2.17716600    2.19802900    0.30270100
""",
)

entry(
    index = 121,
    label = "S137",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {11,S}
2  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {1,S} {7,S} {9,D}
5  C u0 p0 c0 {3,S} {6,D} {8,S}
6  C u0 p0 c0 {1,S} {5,D} {10,S}
7  C u0 p0 c0 {4,S} {8,D} {18,S}
8  C u0 p0 c0 {5,S} {7,D} {19,S}
9  C u0 p0 c0 {4,D} {20,S} {21,S}
10 O u0 p2 c0 {6,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65183,0.0315519,0.000198847,-4.87802e-07,3.73249e-10,-11227.9,15.4022], Tmin=(10,'K'), Tmax=(336.224,'K')),
            NASAPolynomial(coeffs=[-1.14331,0.0885981,-5.56508e-05,1.68114e-08,-1.95245e-12,-10905.4,33.3095], Tmin=(336.224,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-93.3493,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (523.812,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 11, 'C-O': 1, 'H-O': 1, 'C-C': 6, 'C=C': 3}
1D rotors:
pivots: [5, 6], dihedral: [4, 5, 6, 15], rotor symmetry: 1, max scan energy: 0.54 kJ/mol (set as a FreeRotor)
* Invalidated! pivots: [7, 8], dihedral: [5, 7, 8, 18], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [9, 10], dihedral: [2, 9, 10, 20], rotor symmetry: 3, max scan energy: 14.82 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.78668400   -0.18422100    0.77124400
C      -1.52473300   -0.30207800    0.32698800
C      -1.02218700   -1.52907900   -0.27462700
C       0.29980100   -1.72266900   -0.45801500
C       1.31319400   -0.74667700   -0.07007100
C       2.77165400   -1.13144400   -0.15058400
C       0.89114800    0.45249900    0.38322600
O       1.70647900    1.45754900    0.81827100
C      -0.55659100    0.87456200    0.38566200
C      -0.79853000    1.83452900   -0.80909100
H      -3.49859300   -0.99495000    0.66266700
H      -3.14113200    0.72002300    1.25374800
H      -1.73345000   -2.30924000   -0.52352800
H       0.65022400   -2.66017200   -0.87955100
H       2.94077600   -1.82150500   -0.98112700
H       3.42885800   -0.27257900   -0.32990800
H       3.12229300   -1.63071700    0.76048100
H       2.62469000    1.16929800    0.77101400
H      -0.73137000    1.43960200    1.30649600
H      -1.82095600    2.21760800   -0.77663300
H      -0.65924100    1.30768100   -1.75613700
H      -0.10249700    2.67497800   -0.76978100
""",
)

entry(
    index = 122,
    label = "S140",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {8,D}
2  C u0 p0 c0 {3,B} {4,B} {8,S}
3  C u0 p0 c0 {2,B} {5,B} {9,S}
4  C u0 p0 c0 {2,B} {7,B} {13,S}
5  C u0 p0 c0 {3,B} {6,B} {10,S}
6  C u0 p0 c0 {5,B} {7,B} {11,S}
7  C u0 p0 c0 {4,B} {6,B} {12,S}
8  C u1 p0 c0 {1,D} {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89879,0.0059208,0.000154723,-2.88307e-07,1.64655e-10,12871,11.9535], Tmin=(10,'K'), Tmax=(559.15,'K')),
            NASAPolynomial(coeffs=[0.134886,0.0551488,-3.71671e-05,1.18132e-08,-1.42381e-12,12943.3,24.8065], Tmin=(559.15,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (106.973,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-C': 4, 'C=C': 3, 'C-H': 5}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 2, max scan energy: 17.98 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       3.22049000    0.20792300   -1.11409400
C       2.54960800   -0.16760800   -0.21101400
C       1.07770500   -0.08579200   -0.05893800
C       0.47982800   -0.59464200    1.09722100
C      -0.90115700   -0.52395900    1.25202200
C      -1.68174400    0.05444800    0.25231600
C      -1.08733100    0.56417900   -0.90475100
C       0.29012800    0.49610700   -1.06397100
H       1.10686900   -1.03987200    1.86104100
H      -1.36862300   -0.91734400    2.14708300
H      -2.75790300    0.10945700    0.37298000
H      -1.70166000    1.01243900   -1.67742200
H       0.77378800    0.88466400   -1.95247300
""",
)

entry(
    index = 123,
    label = "S141",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,D} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {10,S}
3  C u0 p0 c0 {2,D} {5,S} {11,S}
4  C u0 p0 c0 {1,D} {6,S} {8,S}
5  C u0 p0 c0 {3,S} {7,D} {12,S}
6  C u1 p0 c0 {4,S} {13,S} {14,S}
7  C u0 p0 c0 {5,D} {15,S} {16,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8339,0.010332,0.000217261,-4.53794e-07,2.88604e-10,26617.7,11.345], Tmin=(10,'K'), Tmax=(514.701,'K')),
            NASAPolynomial(coeffs=[1.23686,0.0650378,-4.27799e-05,1.33392e-08,-1.58774e-12,26427.8,17.7072], Tmin=(514.701,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (221.26,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (369.994,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'C=C': 3, 'C-H': 9}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [8, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 70.66 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 46.07 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 46.07 kJ/mol


External symmetry: 2, optical isomers: 1

Geometry:
C      -3.66236000   -0.08042200    0.34094300
C      -2.42861300    0.06288900    0.88014200
C      -2.14658100    0.74312600    2.09908200
C      -0.87364900    0.88085100    2.63825000
C      -0.57879800    1.54022900    3.82497300
C       0.73387300    1.67078100    4.36156100
C       1.03851200    2.30962600    5.51589100
H      -3.81564300   -0.60947700   -0.59120000
H      -4.54163400    0.33096900    0.82567000
H      -1.57854000   -0.36860800    0.35436800
H      -2.98570100    1.18012100    2.63679400
H      -0.04362200    0.43816300    2.08871800
H      -1.39767800    1.98751500    4.38496600
H       1.54193600    1.21792500    3.78954000
H       0.26974800    2.77720300    6.12227300
H       2.05786200    2.37677000    5.87464000
""",
)

entry(
    index = 124,
    label = "S142",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,D} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {2,D} {7,S} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  C u0 p0 c0 {7,D} {15,S} {16,S}
7  C u1 p0 c0 {4,S} {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2413,0.0765481,-0.000206398,4.30004e-07,-3.32053e-10,41859.1,12.8575], Tmin=(10,'K'), Tmax=(433.205,'K')),
            NASAPolynomial(coeffs=[2.47791,0.0549218,-3.22257e-05,9.1692e-09,-1.01341e-12,42194.3,19.0074], Tmin=(433.205,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (348.017,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (374.151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'C=C': 3, 'C-H': 9}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: not a torsional mode (angles = 179.75, 125.93 degrees)
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 10.09 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 12.82 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
C      -3.04587700   -0.58246000    1.04721900
C      -1.94388600   -1.10576400    0.60088100
C      -0.80296400   -1.65414700    0.13696700
C       0.28117500   -0.95782600   -0.40106500
C       1.53549900   -1.61981300   -0.89339000
C       2.75824400   -1.17746500   -0.12276700
C       3.79219500   -0.52398600   -0.64400000
H      -3.16305300   -0.28489900    2.08917500
H      -3.90736600   -0.41285500    0.40141500
H      -0.73123600   -2.74137900    0.18759800
H       0.23431800    0.12533400   -0.45515200
H       1.69026900   -1.39308500   -1.95683200
H       1.42642700   -2.70838300   -0.81349300
H       2.75137600   -1.40958300    0.94038500
H       4.63921200   -0.22279900   -0.03792800
H       3.83026400   -0.26868800   -1.69903600
""",
)

entry(
    index = 124,
    label = "S143",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {12,S}
4  C u1 p0 c0 {2,S} {6,S} {13,S}
5  C u0 p0 c0 {3,D} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {7,T}
7  C u0 p0 c0 {6,T} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55979,0.0498066,-2.17098e-05,5.23783e-10,1.39891e-12,43226.6,13.7324], Tmin=(10,'K'), Tmax=(1322.38,'K')),
            NASAPolynomial(coeffs=[12.4845,0.0334744,-1.52799e-05,3.38029e-09,-2.93984e-13,39933.9,-35.3435], Tmin=(1322.38,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (359.386,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (374.151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C#C': 1, 'C-C': 4, 'C=C': 1, 'C-H': 9}
1D rotors:
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 12.39 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 22.26 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
C      -3.35898700    1.26042900    0.27760400
C      -2.41001200    0.50653900    0.43243000
C      -1.34677700   -0.34470900    0.59709400
C      -0.70118700   -1.09115500   -0.53338800
C      -0.42695700   -2.58127500   -0.21079900
C       0.59098300   -2.77895800    0.87633100
C       0.37304200   -3.39520200    2.03480100
H      -4.18350700    1.91708400    0.14824700
H      -0.93635600   -0.47462000    1.59414400
H      -1.32643700   -1.01815600   -1.42663500
H       0.25701100   -0.61177900   -0.78697800
H      -1.36477400   -3.07637300    0.05880100
H      -0.06482300   -3.05795900   -1.13028600
H       1.58134700   -2.37091000    0.67494400
H       1.15601500   -3.50727700    2.77645100
H      -0.59732100   -3.81639300    2.28042900
""",
)

entry(
    index = 126,
    label = "S145",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {6,D}
3  C u0 p0 c0 {2,S} {4,S} {7,D}
4  C u0 p0 c0 {1,S} {3,S} {10,D}
5  C u0 p0 c0 {1,S} {8,D} {11,S}
6  C u0 p0 c0 {2,D} {14,S} {15,S}
7  C u0 p0 c0 {3,D} {16,S} {17,S}
8  C u0 p0 c0 {5,D} {12,S} {13,S}
9  H u0 p0 c0 {1,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45311,0.0490752,1.29827e-05,-5.79359e-08,2.97733e-11,18408.5,13.5586], Tmin=(10,'K'), Tmax=(765.267,'K')),
            NASAPolynomial(coeffs=[4.94801,0.0570209,-3.34817e-05,9.45181e-09,-1.03226e-12,17718.3,3.73143], Tmin=(765.267,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (153.007,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 5, 'C=C': 3, 'C-H': 8, 'C=O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 12.52 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       3.02878800   -0.08692100   -0.04768600
C       1.77465200   -0.31554800    0.33295300
C       0.56890700   -0.06076500   -0.51216500
C      -0.63098600    0.67246700    0.12405000
C      -0.74029400    1.84450900    0.74323400
C      -1.56464900   -0.44124400   -0.17050400
C      -2.86626700   -0.70232400   -0.03290100
C      -0.42842800   -1.25222800   -0.74138400
O      -0.31457000   -2.36166800   -1.17575400
H       3.26214200    0.31881800   -1.02707700
H       3.86659200   -0.30293100    0.60524400
H       1.57993800   -0.72278300    1.32293300
H       0.85823400    0.37189600   -1.47708000
H      -1.68603500    2.18730700    1.14913500
H       0.11669700    2.49687300    0.86702400
H      -3.26541600   -1.65575700   -0.36127400
H      -3.55930100    0.01031600    0.40125400
""",
)

entry(
    index = 127,
    label = "S146",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {5,D}
3  C u0 p0 c0 {2,S} {4,S} {7,D}
4  C u0 p0 c0 {1,S} {3,S} {11,D}
5  C u0 p0 c0 {2,D} {6,S} {13,S}
6  C u0 p0 c0 {5,S} {8,D} {12,S}
7  C u0 p0 c0 {3,D} {16,S} {17,S}
8  C u0 p0 c0 {6,D} {14,S} {15,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66134,0.0315642,0.000106027,-2.1416e-07,1.16235e-10,15813.4,12.3653], Tmin=(10,'K'), Tmax=(633.989,'K')),
            NASAPolynomial(coeffs=[2.98834,0.064724,-4.08367e-05,1.22086e-08,-1.39526e-12,15317.6,10.7227], Tmin=(633.989,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (131.43,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 5, 'C=C': 3, 'C-H': 8, 'C=O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 32.86 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       3.14131000    0.89248400   -0.79289500
C       2.10942700    0.13796400   -0.39109500
C       0.74167300    0.60692200   -0.30870200
C      -0.29891800   -0.14136800    0.09262800
C      -0.43770100   -1.59517200    0.56108400
C      -1.95331600   -1.29809200    0.72059100
O      -2.90036200   -1.94065100    1.07405700
C      -1.74355800    0.12272400    0.25051100
C      -2.59334600    1.14014300    0.07920400
H       4.14912000    0.49850600   -0.83876200
H       3.00473800    1.92809000   -1.08767600
H       2.28969600   -0.89527000   -0.10426300
H       0.55950100    1.64077400   -0.59540900
H       0.06483700   -1.85098800    1.49893000
H      -0.21308600   -2.36619500   -0.18229500
H      -2.27297500    2.11479400   -0.27243500
H      -3.64730800    1.00483700    0.29489800
""",
)




