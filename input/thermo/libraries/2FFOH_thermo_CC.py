#!/usr/bin/env python
# encoding: utf-8

name = "2FFOH_coupled_cluster"
shortDesc = ""
longDesc = """
ARC v1.1.0
ARC project 2FFOH_Wang_3

Levels of theory used:

Conformers:       wb97xd/def2svp, software: gaussian
TS guesses:       wb97xd/def2svp, software: gaussian
Optimization:     wb97xd/def2tzvp, software: gaussian (using a fine grid)
Frequencies:      wb97xd/def2tzvp, software: gaussian
Single point:     ccsd(t)-f12/cc-pvtz-f12, software: molpro
Rotor scans:      wb97xd/def2tzvp, software: gaussian
Using p-type bond additivity corrections for thermo

Using the following ESS settings: {'gaussian': ['local'], 'molpro': ['local'], 'orca': ['local']}
"""
entry(
    index = 0,
    label = "furfuryl",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {7,S}
2  O u0 p2 c0 {3,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {3,S} {5,D}
5  C u0 p0 c0 {4,D} {6,S} {10,S}
6  C u0 p0 c0 {5,S} {7,D} {11,S}
7  C u0 p0 c0 {1,S} {6,D} {12,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85691,0.0249605,3.1236e-05,-5.4466e-08,2.17206e-11,-30328.5,12.447], Tmin=(10,'K'), Tmax=(922.182,'K')),
            NASAPolynomial(coeffs=[5.07028,0.0385125,-2.14116e-05,5.71862e-09,-5.9312e-13,-31352.3,2.35377], Tmin=(922.182,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-252.115,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'H-O': 1, 'C-O': 3, 'C-H': 5, 'C=C': 2}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 1, max scan energy: 10.43 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 11.99 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.41135500   -0.22549500    0.83384100
C      -1.69351100    0.31298300   -0.26028200
C      -0.22132300    0.14948000   -0.14160700
C       0.80133500    1.00474600    0.08577400
C       1.99256000    0.21529200    0.10937400
C       1.59688100   -1.05812200   -0.10055800
O       0.25573500   -1.11718700   -0.25978300
H      -2.20363000   -1.15935300    0.89901700
H      -2.03782800   -0.12928200   -1.20340300
H      -1.92299900    1.37737800   -0.28713100
H       0.71683300    2.06948500    0.22571700
H       3.00299600    0.55409400    0.26383700
H       2.12430700   -1.99401400   -0.16479700
""",
)

entry(
    index = 1,
    label = "P368",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,D} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 C u1 p0 c0 {2,D} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93144,0.00387247,9.08264e-05,-1.64809e-07,9.04653e-11,40261.6,8.14011], Tmin=(10,'K'), Tmax=(596.182,'K')),
            NASAPolynomial(coeffs=[2.11621,0.0323648,-2.19051e-05,7.14721e-09,-8.88305e-13,40188.2,13.5273], Tmin=(596.182,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (334.723,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 1, 'C-H': 5, 'C=C': 2}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 24.76 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -1.62246200    0.05671300   -0.10871000
C      -0.38238300    0.30969200    0.29525200
C       0.80731600   -0.19096900   -0.39014400
C       2.04408600    0.03608600   -0.02369400
H      -2.47975300    0.44505000    0.42496800
H      -1.81891200   -0.54773600   -0.98730500
H      -0.21104700    0.91714400    1.17739600
H       0.62944800   -0.80326300   -1.27948300
H       3.03370500   -0.22284200   -0.36644000
""",
)

entry(
    index = 2,
    label = "P367",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {5,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,D} {7,S} {8,S}
4  C u0 p0 c0 {2,D} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95298,0.00269446,9.57653e-05,-1.65103e-07,8.89066e-11,10182.8,6.91126], Tmin=(10,'K'), Tmax=(564.567,'K')),
            NASAPolynomial(coeffs=[0.144869,0.0391137,-2.60744e-05,8.38334e-09,-1.02891e-12,10462.4,21.774], Tmin=(564.567,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (84.6437,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 1, 'C-H': 6, 'C=C': 2}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 25.77 kJ/mol


External symmetry: 2, optical isomers: 1

Geometry:
C       1.83343600    0.08472500   -0.10624700
C       0.59933300   -0.40715600   -0.07494500
C      -0.59932200    0.40713900    0.07512300
C      -1.83342400   -0.08474200    0.10642500
H       2.01785200    1.14984300   -0.01908400
H       2.69717100   -0.55720300   -0.21949300
H       0.44654600   -1.47927700   -0.16472700
H      -0.44653500    1.47926100    0.16490500
H      -2.01784000   -1.14986000    0.01926200
H      -2.69715900    0.55718700    0.21967100
""",
)

entry(
    index = 3,
    label = "P2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {7,S} {12,S}
3  C u0 p0 c0 {1,S} {4,S} {7,D}
4  C u0 p0 c0 {3,S} {5,D} {8,S}
5  C u0 p0 c0 {4,D} {6,S} {9,S}
6  C u1 p0 c0 {1,S} {5,S} {11,S}
7  C u0 p0 c0 {2,S} {3,D} {10,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87972,0.00675384,0.00014583,-2.6845e-07,1.47339e-10,-15392.8,11.0414], Tmin=(10,'K'), Tmax=(604.87,'K')),
            NASAPolynomial(coeffs=[1.53809,0.051314,-3.67763e-05,1.22802e-08,-1.53519e-12,-15641.4,16.7645], Tmin=(604.87,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-128.038,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'H-O': 1, 'C-O': 3, 'C-H': 4, 'C=C': 2}
1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 1, max scan energy: 25.05 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O       2.49593500   -0.47869800   -0.49470300
C       1.68460800    0.55711400   -0.19649500
C       2.13805300    1.85408100   -0.07032600
C       1.51632500    3.06485800    0.22329300
C       2.53235500    4.04550600    0.20542400
C       3.69427900    3.40910800   -0.08942400
O       3.47908300    2.07711500   -0.26114700
H       3.39549200   -0.15182100   -0.59503200
H       0.64800700    0.29389300   -0.06317000
H       0.46747200    3.20457900    0.42158100
H       2.42123200    5.10123900    0.38892700
H       4.70958700    3.74401600   -0.20797500
""",
)

