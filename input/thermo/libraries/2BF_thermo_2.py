#!/usr/bin/env python
# encoding: utf-8

name = "2BF_thermo_2"
shortDesc = ""
longDesc = """
ARC v1.1.0
ARC project 2BF_thermo_2

Levels of theory used:

Conformers:       wb97xd/def2svp, software: gaussian (dft)
TS guesses:       None
Composite method: cbs-qb3, software: gaussian (composite) (using a fine grid)
Frequencies:      b3lyp/cbsb7, software: gaussian (dft)
Rotor scans:      b3lyp/cbsb7, software: gaussian (dft)
Using p-type bond additivity corrections for thermo

Using the following ESS settings: {'gaussian': ['local'], 'molpro': ['local']}

Considered the following species and TSs:
Species PBROO1 (run time: 1 day, 15:23:55)
Species PBROO2 (run time: 3 days, 1:37:36)
Species PBROO3 (run time: 15:16:21)
Species PBROO4 (run time: 21:53:56)
Species PBROO5 (run time: 2 days, 3:05:09)
Species PBROO6 (run time: 1 day, 9:37:54)
Species PBROO7 (run time: 1 day, 2:49:21)
Species PBROO8 (run time: 15:45:30)
Species PBROO9 (run time: 10:10:59)
Species PBROO10 (run time: 4:55:57)
Species PBROO11 (run time: 3:25:33)
Species PBROO12 (run time: 0:38:34)
Species PBROO13 (run time: 0:03:51)

Overall time since project initiation: 1.0 days, 08:53:21
"""
entry(
    index = 0,
    label = "PBROO1",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {17,S} {18,S} {19,S}
6  C u1 p0 c0 {1,S} {7,S} {20,S}
7  C u0 p0 c0 {6,S} {8,D} {21,S}
8  C u0 p0 c0 {7,D} {9,S} {22,S}
9  O u0 p2 c0 {1,S} {8,S}
10 O u0 p2 c0 {1,S} {23,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 O u1 p2 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.31539,0.182367,-0.000789284,1.89858e-06,-1.60768e-09,-22759,19.4784], Tmin=(10,'K'), Tmax=(390.421,'K')),
            NASAPolynomial(coeffs=[2.46222,0.0856637,-5.1994e-05,1.50687e-08,-1.68105e-12,-22044.9,28.2], Tmin=(390.421,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-189.29,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (544.598,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 12, 'C-O': 3, 'C=C': 1, 'C-C': 6, 'O-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [12, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.88 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 23.54 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 19.17 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Bond ([[7, 11]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[7, 11]]) broke during the scan. But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: Bond ([[5, 6]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[5, 6]]) broke during the scan. But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C       1.28625400    1.16700800    0.86498000
C       1.79644600    0.17580500   -0.18468500
C       3.02137700   -0.61687300    0.28268800
C       3.53064500   -1.61452700   -0.77509000
C       4.70320800   -2.41913800   -0.33103300
O       3.81197300   -5.11621000   -2.00181000
O       4.21805500   -5.96443600   -1.24615800
C       6.00578800   -2.48460400   -0.72424300
C       6.64380300   -3.45747700    0.11413300
C       5.68436600   -3.91347400    0.95775700
O       4.49571700   -3.29216900    0.70367400
H       0.41130700    1.71479900    0.50468100
H       2.05561400    1.90160200    1.12216500
H       0.99991000    0.65240100    1.78734400
H       0.99347500   -0.52338200   -0.44793300
H       2.04394500    0.71561700   -1.10701300
H       2.77740300   -1.16501400    1.19897000
H       3.83224800    0.07388600    0.54160800
H       2.71445800   -2.29268200   -1.05274000
H       3.81558600   -1.07838400   -1.68540500
H       6.45714500   -1.91150900   -1.51878000
H       7.67487900   -3.77231300    0.08616900
H       5.67406600   -4.63887300    1.75314100
""",
)

entry(
    index = 1,
    label = "PBROO2",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {15,S} {16,S}
4  C u0 p0 c0 {6,S} {7,S} {10,S} {17,S}
5  C u0 p0 c0 {2,S} {18,S} {19,S} {20,S}
6  C u1 p0 c0 {3,S} {4,S} {9,S}
7  C u0 p0 c0 {4,S} {8,D} {21,S}
8  C u0 p0 c0 {7,D} {9,S} {22,S}
9  O u0 p2 c0 {6,S} {8,S}
10 O u0 p2 c0 {4,S} {23,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 O u1 p2 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.53003,0.163034,-0.000737409,1.90399e-06,-1.69524e-09,-22687.4,21.0665], Tmin=(10,'K'), Tmax=(381.529,'K')),
            NASAPolynomial(coeffs=[-0.275707,0.0910486,-5.57319e-05,1.62495e-08,-1.82054e-12,-21735.3,41.5709], Tmin=(381.529,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-188.701,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (548.755,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 12, 'C-O': 3, 'C=C': 1, 'C-C': 6, 'O-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [12, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.97 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Bond ([[10, 15]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[10, 15]]) broke during the scan. But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Bond ([[10, 15]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[10, 15]]) broke during the scan. But unable to propose troubleshooting methods.
pivots: [9, 10], dihedral: [5, 9, 10, 11], rotor symmetry: 2, max scan energy: 1.33 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       3.62507600   -0.22448300    0.79123100
C       2.20844800    0.35651100    0.82110000
C       1.25695300   -0.35515800   -0.14726900
C      -0.18557700    0.19884900   -0.16170100
C      -0.98011600   -0.06046600    1.07405900
O      -0.73139400    0.73096300    2.16485900
C      -1.55403200    0.31201500    3.17062000
C      -2.32207100   -0.72366900    2.74978000
C      -1.94957000   -0.96583800    1.38655500
O       1.16117900   -1.81004000    3.78474300
O       1.11896200   -2.60021200    2.87454200
H       4.06326400   -0.15633200   -0.20965000
H       3.62411600   -1.28021100    1.07997500
H       4.28740200    0.30664200    1.48022700
H       1.80948600    0.29956200    1.83744700
H       2.24331500    1.42349400    0.56915800
H       1.65966100   -0.27711100   -1.16458900
H       1.22171700   -1.42415900    0.09168000
H      -0.15758800    1.27885900   -0.34818000
H      -0.72907200   -0.24983300   -0.99796900
H      -1.47038400    0.84956200    4.09961500
H      -3.06362800   -1.24909600    3.33035200
H      -2.35379400   -1.71468800    0.72367700
""",
)

entry(
    index = 2,
    label = "PBROO3",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,S} {9,S}
2  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {3,S} {7,D}
6  C u1 p0 c0 {2,S} {4,S} {17,S}
7  C u0 p0 c0 {5,D} {8,S} {18,S}
8  C u0 p0 c0 {7,S} {9,D} {19,S}
9  C u0 p0 c0 {1,S} {8,D} {20,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96064,0.0453376,2.23208e-05,-4.41171e-08,1.51244e-11,2865.56,13.9798], Tmin=(10,'K'), Tmax=(1168.6,'K')),
            NASAPolynomial(coeffs=[12.6167,0.0479464,-2.24073e-05,5.00566e-09,-4.34565e-13,-1358.76,-38.5474], Tmin=(1168.6,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (23.9644,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (478.082,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 11, 'C-O': 2, 'C=C': 2, 'C-C': 5}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 2.12 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C      -3.07518600    0.58610100    0.83711800
C      -3.19258700   -0.63625700   -0.00725500
C      -2.80681200   -1.97687100    0.52006600
C      -2.68390600   -3.07431800   -0.56144900
C      -3.96965700   -3.41041300   -1.23587900
C      -4.42173200   -3.29984300   -2.51579500
C      -5.76475200   -3.80514800   -2.52654900
C      -6.03278300   -4.18501000   -1.25268400
O      -4.95219500   -3.95384700   -0.45115600
H      -2.10997000    0.62873600    1.35699200
H      -3.84733000    0.61993300    1.62468600
H      -3.18366300    1.50050300    0.24839000
H      -3.78089700   -0.59119000   -0.91814200
H      -1.85170500   -1.90394600    1.05845900
H      -3.53576200   -2.32130300    1.27367300
H      -1.97210300   -2.75647900   -1.32800600
H      -2.27429000   -3.97999100   -0.09970800
H      -3.86475000   -2.90842800   -3.35248300
H      -6.43307500   -3.87334300   -3.37019500
H      -6.89236900   -4.61603300   -0.76829200
""",
)

entry(
    index = 3,
    label = "PBROO4",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {15,S} {16,S}
4  C u0 p0 c0 {7,S} {9,S} {10,S} {17,S}
5  C u0 p0 c0 {2,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {3,S} {8,D} {9,S}
7  C u1 p0 c0 {4,S} {8,S} {21,S}
8  C u0 p0 c0 {6,D} {7,S} {22,S}
9  O u0 p2 c0 {4,S} {6,S}
10 O u0 p2 c0 {4,S} {23,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 O u1 p2 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.94071,0.105576,-0.000201425,3.7793e-07,-2.95681e-10,-8386.74,17.5646], Tmin=(10,'K'), Tmax=(412.369,'K')),
            NASAPolynomial(coeffs=[2.82945,0.0857808,-5.34875e-05,1.60061e-08,-1.8422e-12,-8200.08,20.1548], Tmin=(412.369,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-69.7557,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (540.441,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 12, 'C-O': 3, 'C=C': 1, 'C-C': 6, 'O-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [12, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.84 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 26.54 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 18.08 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 12.17 kJ/mol
* Invalidated! pivots: [8, 9], dihedral: [7, 8, 9, 10], invalidation reason: Bond ([[8, 9]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[8, 9]]) broke during the scan. But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C       2.82677000    2.25748300   -0.84849000
C       2.72319900    0.81249000   -1.34400200
C       1.45490000    0.10675900   -0.85330700
C       1.29845700   -1.34053500   -1.37248900
C       2.37572700   -2.25761100   -0.92443100
C       3.31401200   -3.02293500   -1.60076400
C       4.10235100   -3.67716500   -0.66671600
C       3.66329300   -3.21482800    0.66780000
O       4.72980000   -2.32380300    1.25913200
O       4.66522300   -2.29878600    2.57271400
O       2.52272700   -2.41292200    0.43471600
H       2.84051400    2.29861700    0.24473900
H       3.74084300    2.73616200   -1.20939000
H       1.97861300    2.85782200   -1.19262400
H       3.60265900    0.25055700   -1.01162800
H       2.74505400    0.79821900   -2.44098800
H       0.57204500    0.67582200   -1.16564100
H       1.44548300    0.08905600    0.24102900
H       1.27373100   -1.35024000   -2.46622900
H       0.33307900   -1.73326300   -1.02682600
H       3.39491500   -3.08394100   -2.67559300
H       4.93195000   -4.34485600   -0.83333500
H       3.46139100   -3.93189100    1.46320900
""",
)

entry(
    index = 4,
    label = "PBROO5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {6,D} {9,S}
6  C u0 p0 c0 {5,D} {7,S} {19,S}
7  C u0 p0 c0 {6,S} {8,D} {20,S}
8  C u0 p0 c0 {7,D} {9,S} {21,S}
9  O u0 p2 c0 {5,S} {8,S}
10 O u0 p2 c0 {1,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 O u1 p2 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.09608,0.0920506,-0.000161511,3.37721e-07,-2.96316e-10,-16464.3,16.8378], Tmin=(10,'K'), Tmax=(389.323,'K')),
            NASAPolynomial(coeffs=[1.76811,0.0849098,-5.3919e-05,1.6357e-08,-1.90172e-12,-16203.4,24.0148], Tmin=(389.323,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-136.908,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (515.497,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 11, 'C-O': 3, 'C=C': 2, 'C-C': 5, 'O-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [12, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.04 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 23.42 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Another conformer for PBROO5 exists which is 2.16 kJ/mol lower.Another conformer for PBROO5 exists which is 2.16 kJ/mol lower.
pivots: [3, 10], dihedral: [2, 3, 10, 11], rotor symmetry: 1, max scan energy: 12.93 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 11.86 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -3.84026100   -0.99866100    0.57182400
C      -3.09995000   -0.82626000   -0.75747700
C      -1.85997300    0.04955700   -0.65558700
C      -1.01619800    0.13624300   -1.93752300
C      -0.31552200   -1.13418500   -2.26869900
C      -0.39983600   -2.01516500   -3.30353100
C       0.55819100   -3.05041300   -3.04311200
C       1.15188800   -2.72625800   -1.86756000
O       0.63367200   -1.56203900   -1.37896400
O      -2.35080700    1.40349000   -0.34333100
O      -1.38944400    2.19888400    0.07803800
H      -4.16450700   -0.03497300    0.96984600
H      -3.19946600   -1.47390400    1.32038200
H      -4.72547200   -1.62620000    0.44435300
H      -3.76702100   -0.39089100   -1.51029700
H      -2.78576400   -1.79981800   -1.14530200
H      -1.22728900   -0.24086700    0.18620800
H      -0.28727200    0.93933600   -1.79037400
H      -1.65747700    0.41689700   -2.77729400
H      -1.05963800   -1.93497300   -4.15302300
H       0.77183600   -3.91361100   -3.65297300
H       1.92050600   -3.18447300   -1.26888600
""",
)

entry(
    index = 5,
    label = "PBROO6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {15,S}
3  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {6,D} {9,S}
6  C u0 p0 c0 {5,D} {7,S} {19,S}
7  C u0 p0 c0 {6,S} {8,D} {20,S}
8  C u0 p0 c0 {7,D} {9,S} {21,S}
9  O u0 p2 c0 {5,S} {8,S}
10 O u0 p2 c0 {2,S} {22,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 O u1 p2 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.10992,0.091946,-0.000182184,4.20009e-07,-3.81631e-10,-15193.6,15.5918], Tmin=(10,'K'), Tmax=(386.562,'K')),
            NASAPolynomial(coeffs=[0.98,0.0865417,-5.47219e-05,1.65303e-08,-1.91478e-12,-14823.8,26.4952], Tmin=(386.562,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-126.345,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (519.654,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 11, 'C-O': 3, 'C=C': 2, 'C-C': 5, 'O-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [12, 1, 2, 3], rotor symmetry: 3, max scan energy: 12.06 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 25.09 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 10.82 kJ/mol
* Invalidated! pivots: [4, 7], dihedral: [3, 4, 7, 8], invalidation reason: Another conformer for PBROO6 exists which is 1.54 kJ/mol lower.Another conformer for PBROO6 exists which is 1.54 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
C       2.93750900    1.02415100    0.01428100
C       2.08122100   -0.24501500   -0.02141100
C       2.64152500   -1.35156100    0.88026600
C       1.77880900   -2.61060100    0.89436800
O       2.32188400   -3.54633300    1.93048200
O       2.06458900   -3.11809600    3.14550800
C       1.72741200   -3.37158800   -0.37523900
C       0.72103300   -4.03059800   -1.01506700
C       1.28936500   -4.59521500   -2.20000900
C       2.60060600   -4.23935500   -2.19227100
O       2.88687200   -3.49303800   -1.09284600
H       3.95760200    0.82144700   -0.32525700
H       2.51983900    1.80046200   -0.63187900
H       2.99995400    1.43141900    1.02779600
H       2.01086300   -0.60949400   -1.05138900
H       1.05814300   -0.00474300    0.29159000
H       3.65190600   -1.62361200    0.56109600
H       2.70588400   -0.99592900    1.91244200
H       0.76226300   -2.39032700    1.22559400
H      -0.30110100   -4.10688900   -0.67919700
H       0.78872600   -5.18402300   -2.95166100
H       3.42458400   -4.42503200   -2.86024300
""",
)

entry(
    index = 6,
    label = "PBROO7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {10,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {6,D} {9,S}
6  C u0 p0 c0 {5,D} {7,S} {19,S}
7  C u0 p0 c0 {6,S} {8,D} {20,S}
8  C u0 p0 c0 {7,D} {9,S} {21,S}
9  O u0 p2 c0 {5,S} {8,S}
10 O u0 p2 c0 {4,S} {22,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 O u1 p2 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.6501,0.149705,-0.000665416,1.73271e-06,-1.56018e-09,-14111.5,17.5631], Tmin=(10,'K'), Tmax=(377.585,'K')),
            NASAPolynomial(coeffs=[0.0446138,0.0865149,-5.37043e-05,1.58421e-08,-1.79207e-12,-13267.6,36.1658], Tmin=(377.585,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-117.392,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (515.497,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 11, 'C-O': 3, 'C=C': 2, 'C-C': 5, 'O-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 11.51 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 19.78 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 21.98 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: Another conformer for PBROO7 exists which is 1.65 kJ/mol lower.Another conformer for PBROO7 exists which is 1.65 kJ/mol lower.
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 8.58 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       2.25121200    2.59946700    1.18392700
O       2.52438900    1.31156500    1.24824600
C       3.69801800    0.97252700    0.44126000
C       3.40342500    1.08314600   -1.04623900
C       2.35021000    0.08803400   -1.54349500
C       2.04499600    0.25764700   -3.04375300
C       1.06246800   -0.73145700   -3.56921900
C      -0.20381700   -0.63369000   -4.05871900
C      -0.62281800   -1.96510300   -4.39134200
C       0.41817200   -2.77586400   -4.07880700
O       1.45552700   -2.04377700   -3.57631700
H       3.92749200   -0.05033500    0.74738400
H       4.49962200    1.64457100    0.75205000
H       4.34776400    0.93133800   -1.58269500
H       3.08813100    2.11180600   -1.24902100
H       2.69454400   -0.93585700   -1.36385600
H       1.42537500    0.21344300   -0.97288500
H       1.64935400    1.26023300   -3.23057400
H       2.97928600    0.17601000   -3.61367600
H      -0.77219100    0.27615900   -4.17094700
H      -1.57045100   -2.26934800   -4.80649500
H       0.58310900   -3.83766100   -4.14674600
""",
)

entry(
    index = 7,
    label = "PBROO8",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {6,D} {9,S}
6  C u0 p0 c0 {5,D} {7,S} {19,S}
7  C u0 p0 c0 {6,S} {8,D} {20,S}
8  C u0 p0 c0 {7,D} {9,S} {21,S}
9  O u0 p2 c0 {5,S} {8,S}
10 O u0 p2 c0 {1,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 O u1 p2 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54086,0.0801163,-4.71942e-05,1.1668e-08,-7.1851e-13,-16930.6,16.0338], Tmin=(10,'K'), Tmax=(1510.64,'K')),
            NASAPolynomial(coeffs=[28.1431,0.029054,-1.0474e-05,1.63348e-09,-7.9062e-14,-25970.4,-118.125], Tmin=(1510.64,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-140.772,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (511.34,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 11, 'C-O': 3, 'C=C': 2, 'C-C': 5, 'O-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [12, 1, 2, 3], rotor symmetry: 3, max scan energy: 12.98 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 26.51 kJ/mol
pivots: [2, 10], dihedral: [1, 2, 10, 11], rotor symmetry: 1, max scan energy: 11.07 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 22.32 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 12.47 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.98308700    0.93016500    0.93862400
C      -2.19469500    0.14894900   -0.09889500
C      -0.70063200    0.05856100    0.17841400
C       0.10703500   -0.63093300   -0.94147500
C       0.13598900    0.13146100   -2.22194900
C      -0.34670300   -0.10497700   -3.47277000
C       0.00839500    1.03048900   -4.27513600
C       0.67845700    1.87639300   -3.45406300
O       0.76682800    1.34830700   -2.19788900
O      -2.67383200   -1.25143900   -0.10982500
O      -3.86767900   -1.36464500   -0.65200600
H      -2.69272400    1.98345500    0.91311700
H      -4.05053100    0.86032600    0.72455600
H      -2.79708600    0.54210100    1.94355400
H      -2.39034400    0.52731400   -1.10472200
H      -0.31950700    1.07233000    0.33029100
H      -0.55234900   -0.48240400    1.11886700
H       1.13281300   -0.78188100   -0.58782300
H      -0.31009800   -1.62053400   -1.13936500
H      -0.88937900   -0.98275200   -3.78653400
H      -0.20845300    1.18794100   -5.31965900
H       1.13777500    2.84057200   -3.59079100
""",
)

entry(
    index = 8,
    label = "PBROO9",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {7,S} {10,S}
2  O u0 p2 c0 {3,S} {6,S}
3  O u1 p2 c0 {2,S}
4  C u0 p0 c0 {5,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
7  C u0 p0 c0 {1,S} {5,S} {8,D}
8  C u0 p0 c0 {7,D} {9,S} {17,S}
9  C u0 p0 c0 {8,S} {10,D} {18,S}
10 C u0 p0 c0 {1,S} {9,D} {19,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.03728,0.104971,-0.000381457,9.97835e-07,-9.23399e-10,-11042.3,15.6903], Tmin=(10,'K'), Tmax=(370.834,'K')),
            NASAPolynomial(coeffs=[0.889543,0.0753412,-4.80523e-05,1.45375e-08,-1.68109e-12,-10520,28.816], Tmin=(370.834,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-91.8462,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (444.824,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 9, 'C-O': 3, 'C=C': 2, 'C-C': 4, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for PBROO9 exists which is 1.18 kJ/mol lower.Another conformer for PBROO9 exists which is 1.18 kJ/mol lower.
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 18.67 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 22.87 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 8.91 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       3.61610700    0.70588900   -1.89947600
O       3.64310800   -0.10542100   -0.86046700
C       2.64848600    0.27641000    0.14375900
C       1.23390000    0.00506600   -0.33950600
C       0.95913300   -1.48513600   -0.61788100
C      -0.43915400   -1.75167200   -1.05560600
C      -0.99367400   -2.20847000   -2.21131500
C      -2.41349800   -2.23477800   -2.00614800
C      -2.61929400   -1.79036000   -0.74166200
O      -1.42853600   -1.49011700   -0.14448400
H       2.80876500    1.33283100    0.36457900
H       2.91966000   -0.33163800    1.00966600
H       1.05722400    0.59428300   -1.24325000
H       0.54025700    0.37084500    0.42382800
H       1.63601600   -1.84676600   -1.39503200
H       1.17413100   -2.06716900    0.28727900
H      -0.45732500   -2.49351800   -3.10263100
H      -3.17116900   -2.54418900   -2.70833100
H      -3.49819300   -1.63533600   -0.13939100
""",
)

entry(
    index = 9,
    label = "PBROO10",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,S} {9,S}
2  O u0 p2 c0 {3,S} {5,S}
3  O u1 p2 c0 {2,S}
4  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
6  C u0 p0 c0 {1,S} {4,S} {7,D}
7  C u0 p0 c0 {6,D} {8,S} {14,S}
8  C u0 p0 c0 {7,S} {9,D} {15,S}
9  C u0 p0 c0 {1,S} {8,D} {16,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.35412,0.0681196,-0.000158872,3.94603e-07,-3.73611e-10,-7618.96,15.4516], Tmin=(10,'K'), Tmax=(369.381,'K')),
            NASAPolynomial(coeffs=[1.84057,0.0616545,-3.98071e-05,1.2203e-08,-1.42844e-12,-7351.22,23.3568], Tmin=(369.381,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-63.3603,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (369.994,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'C-H': 7, 'C-C': 3, 'C=C': 2, 'O-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 10.54 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 27.56 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 8.99 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -4.09292500    0.21247400   -0.43541700
O      -3.11516300    0.06206700    0.43700100
C      -1.80944800    0.16616600   -0.20248700
C      -1.53673500    1.60645800   -0.64151500
C      -0.19249600    1.75902400   -1.26267600
C       0.23520800    2.03010700   -2.52578400
C       1.66879200    2.03464800   -2.48289600
C       2.00813700    1.76213000   -1.19832300
O       0.88827300    1.58942400   -0.43754500
H      -1.79880600   -0.52318300   -1.04795700
H      -1.11067200   -0.16547600    0.56569300
H      -2.30046000    1.89967900   -1.36387200
H      -1.62897500    2.26431300    0.22918600
H      -0.39322600    2.20992700   -3.38372000
H       2.34750300    2.21899400   -3.30020700
H       2.94665100    1.66166900   -0.68038400
""",
)

entry(
    index = 10,
    label = "PBROO11",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,S} {8,S}
2  O u0 p2 c0 {3,S} {4,S}
3  O u1 p2 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {1,S} {4,S} {6,D}
6  C u0 p0 c0 {5,D} {7,S} {11,S}
7  C u0 p0 c0 {6,S} {8,D} {12,S}
8  C u0 p0 c0 {1,S} {7,D} {13,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95233,0.0266522,3.22401e-05,-5.5974e-08,2.16969e-11,-3237.89,13.7542], Tmin=(10,'K'), Tmax=(974.505,'K')),
            NASAPolynomial(coeffs=[7.38045,0.0366825,-2.0297e-05,5.34622e-09,-5.44941e-13,-5050.44,-8.56773], Tmin=(974.505,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-26.8196,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'C-H': 5, 'C-C': 2, 'C=C': 2, 'O-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 10.23 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       3.34266300   -0.49581500    1.18714400
O       2.03381900   -0.48860600    1.06965000
C       1.60163400    0.31430900   -0.10060000
C       1.71120300    1.76466800    0.13793200
C       2.70241100    2.67298600   -0.08304000
C       2.22861500    3.92339400    0.42284300
C       0.98476100    3.68210400    0.91581200
O       0.65058200    2.37580500    0.75336900
H       0.56597800    0.00752500   -0.24668000
H       2.22412400   -0.00338900   -0.93558200
H       3.65657900    2.46877900   -0.54157200
H       2.74363300    4.87051800    0.41734100
H       0.24000600    4.30216500    1.38546900
""",
)

entry(
    index = 11,
    label = "PBROO12",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {7,S}
2  O u0 p2 c0 {3,S} {4,S}
3  O u1 p2 c0 {2,S}
4  C u0 p0 c0 {1,S} {2,S} {5,D}
5  C u0 p0 c0 {4,D} {6,S} {8,S}
6  C u0 p0 c0 {5,S} {7,D} {9,S}
7  C u0 p0 c0 {1,S} {6,D} {10,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91332,0.00495963,0.000118627,-2.19037e-07,1.22202e-10,2767.49,11.4934], Tmin=(10,'K'), Tmax=(583.098,'K')),
            NASAPolynomial(coeffs=[1.35642,0.0425775,-2.9793e-05,9.7067e-09,-1.18902e-12,2724.34,19.5229], Tmin=(583.098,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (22.972,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'C-H': 3, 'C-C': 1, 'C=C': 2, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for PBROO12 exists which is 3.91 kJ/mol lower.Another conformer for PBROO12 exists which is 3.91 kJ/mol lower.


External symmetry: 1, optical isomers: 1

Geometry:
O       2.90355900   -0.59112800    0.24553700
O       2.18335700    0.45148800   -0.16961200
C       0.84877400    0.22562500   -0.15047800
C       0.06172300   -0.83103900    0.19820600
C      -1.27263400   -0.37412100   -0.03211300
C      -1.17971700    0.90250000   -0.49413000
O       0.13298900    1.28560900   -0.57175400
H       0.40209100   -1.78394800    0.56252900
H      -2.18318700   -0.92899800    0.12737000
H      -1.89695200    1.64401200   -0.79911700
""",
)

entry(
    index = 12,
    label = "PBROO13",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {5,S}
2 C u0 p0 c0 {3,S} {4,D} {6,S}
3 C u0 p0 c0 {2,S} {5,D} {7,S}
4 C u0 p0 c0 {1,S} {2,D} {8,S}
5 C u1 p0 c0 {1,S} {3,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10667,-0.0100644,7.23179e-05,1.26342e-07,-4.05365e-10,28954.7,9.47007], Tmin=(10,'K'), Tmax=(287.347,'K')),
            NASAPolynomial(coeffs=[-1.3724,0.0375469,-2.66127e-05,8.76487e-09,-1.08062e-12,29387.9,31.1295], Tmin=(287.347,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (240.757,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-H': 3, 'C-C': 1, 'C=C': 2}

External symmetry: 1, optical isomers: 1

Geometry:
C      -0.63442000   -1.18853600    0.56443900
C      -1.14677900   -0.15893900   -0.15043600
C       0.01408400    0.64286000   -0.46327100
C       1.08933200    0.02428900    0.08620200
O       0.68188600   -1.12956700    0.73388000
H      -2.17352100    0.01749400   -0.41973700
H       0.02492200    1.56207500   -1.02829400
H       2.14449600    0.23032400    0.12414500
""",
)

