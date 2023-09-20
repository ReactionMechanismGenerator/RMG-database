#!/usr/bin/env python
# encoding: utf-8

name = "2BF_thermo_3"
shortDesc = ""
longDesc = """
ARC v1.1.0
ARC project 2BF_thermo_3

Levels of theory used:

Conformers:       wb97xd/def2svp, software: gaussian (dft)
TS guesses:       None
Composite method: cbs-qb3, software: gaussian (composite) (using a fine grid)
Frequencies:      b3lyp/cbsb7, software: gaussian (dft)
Rotor scans:      b3lyp/cbsb7, software: gaussian (dft)
Using p-type bond additivity corrections for thermo

Using the following ESS settings: {'gaussian': ['local'], 'molpro': ['local']}

Considered the following species and TSs:
Species TB1 (run time: 4:20:25)
Species TB2 (run time: 18:57:25)
Species TB3 (run time: 1 day, 3:53:30)
Species TB4 (run time: 3:22:13)
Species TB5 (run time: 3:16:31)
Species TB6 (run time: 3:59:35)
Species TB7 (run time: 0:07:50)
Species TB8 (run time: 1:31:26)
Species TB9 (run time: 1:31:01)
Species TB10 (run time: 3:14:53)
Species TB11 (run time: 0:00:39)

Overall time since project initiation: 11:11:21
"""
entry(
    index = 0,
    label = "TB1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {7,S} {9,S} {17,S} {18,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {6,D} {8,S} {9,S}
6  C u0 p0 c0 {2,S} {5,D} {19,S}
7  C u0 p0 c0 {3,S} {8,D} {20,S}
8  C u0 p0 c0 {5,S} {7,D} {21,S}
9  O u0 p2 c0 {3,S} {5,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77944,0.0442429,3.59045e-05,-6.2821e-08,2.28113e-11,-13509.5,13.971], Tmin=(10,'K'), Tmax=(1039.85,'K')),
            NASAPolynomial(coeffs=[6.9487,0.06162,-3.18149e-05,7.94045e-09,-7.75431e-13,-15767.2,-9.12939], Tmin=(1039.85,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-112.229,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 12, 'C=C': 2, 'C-O': 2, 'C-C': 5}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.80 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for TB1 exists which is 1.00 kJ/mol lower.Another conformer for TB1 exists which is 1.00 kJ/mol lower.
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 10.59 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       2.29761000    1.17032500   -0.95104900
C       2.94543700   -0.07621800   -0.34242300
C       2.28052100   -1.38546300   -0.80897800
C       2.87947900   -2.61208300   -0.18696600
C       3.49165800   -3.59925400   -0.85642400
C       4.10953400   -4.81647800   -0.34299300
C       4.59976200   -5.52536300   -1.36341400
C       4.32199400   -4.78921000   -2.64157300
O       3.62785300   -3.59973900   -2.23154400
H       1.23941300    1.23947100   -0.67930700
H       2.35676700    1.15185500   -2.04378100
H       2.78929100    2.08454800   -0.60715900
H       4.00903400   -0.10780900   -0.60219800
H       2.89939600   -0.01767800    0.75168200
H       2.34753900   -1.46050400   -1.89766400
H       1.20992800   -1.33544800   -0.56438800
H       2.83057700   -2.71462000    0.89266600
H       4.14432000   -5.06913700    0.70711200
H       5.11640500   -6.47395800   -1.31767400
H       3.68477900   -5.35369100   -3.33459700
H       5.23414300   -4.50250400   -3.18084900
""",
)

entry(
    index = 1,
    label = "TB2",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {5,D} {16,S}
5  C u0 p0 c0 {4,D} {6,S} {17,S}
6  C u0 p0 c0 {5,S} {7,D} {19,S}
7  C u0 p0 c0 {6,D} {8,S} {18,S}
8  C u1 p0 c0 {7,S} {20,S} {21,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 O u1 p2 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29191,0.0701904,-2.73855e-05,-6.92069e-09,5.58034e-12,6808.52,15.9785], Tmin=(10,'K'), Tmax=(1086.17,'K')),
            NASAPolynomial(coeffs=[11.1538,0.0565944,-2.9817e-05,7.58842e-09,-7.55162e-13,4194.78,-26.7705], Tmin=(1086.17,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (56.5841,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (486.397,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 12, 'C=C': 2, 'C-O': 1, 'C-C': 5}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 37.75 kJ/mol
pivots: [6, 7], dihedral: [4, 6, 7, 8], rotor symmetry: 1, max scan energy: 12.15 kJ/mol
pivots: [7, 8], dihedral: [6, 7, 8, 9], rotor symmetry: 1, max scan energy: 20.57 kJ/mol
pivots: [8, 9], dihedral: [7, 8, 9, 19], rotor symmetry: 3, max scan energy: 12.01 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 68.98 kJ/mol
* Invalidated! pivots: [4, 6], dihedral: [3, 4, 6, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C       4.58129700   -0.39039300    0.06112600
C       3.22841800   -0.60171800   -0.02756900
C       2.35546000    0.17193900   -0.79336700
C       0.91683900   -0.10098800   -0.85137900
O       0.42848600   -1.05682700   -0.20396300
C       0.06694500    0.74082100   -1.65890700
C      -1.39967400    0.53344200   -1.77365200
C      -2.22940700    1.72478600   -1.24126700
C      -3.73525500    1.50764500   -1.40888000
H       5.06368900    0.41786700   -0.47828100
H       5.21164400   -1.02371300    0.67245700
H       2.77984300   -1.42140300    0.52647400
H       2.74593100    1.00605000   -1.37000200
H       0.51953200    1.57368800   -2.19171200
H      -1.66033900    0.38388000   -2.83215200
H      -1.67093700   -0.37892100   -1.23783600
H      -1.99167100    1.87537700   -0.18328600
H      -1.92720500    2.64110000   -1.76119800
H      -4.06517700    0.61005200   -0.87774700
H      -4.30254200    2.35532900   -1.01556900
H      -4.00332300    1.38698300   -2.46306500
""",
)

entry(
    index = 2,
    label = "TB3",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {6,D} {17,S}
6  C u0 p0 c0 {5,D} {7,S} {18,S}
7  C u1 p0 c0 {6,S} {19,S} {20,S}
8  C u1 p0 c0 {2,S} {21,D}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.01191,0.0947304,-0.000171176,2.83509e-07,-1.96345e-10,10759.4,15.8425], Tmin=(10,'K'), Tmax=(456.937,'K')),
            NASAPolynomial(coeffs=[3.34215,0.0739684,-4.43537e-05,1.28839e-08,-1.45006e-12,10915.8,16.5494], Tmin=(456.937,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (89.4258,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (494.711,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 12, 'C=C': 1, 'C=O': 1, 'C-C': 6}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Another conformer for TB3 exists which is 0.99 kJ/mol lower.Another conformer for TB3 exists which is 0.99 kJ/mol lower.
pivots: [4, 7], dihedral: [3, 4, 7, 8], rotor symmetry: 1, max scan energy: 19.13 kJ/mol
pivots: [7, 8], dihedral: [4, 7, 8, 9], rotor symmetry: 1, max scan energy: 25.53 kJ/mol
pivots: [8, 9], dihedral: [7, 8, 9, 19], rotor symmetry: 3, max scan energy: 11.82 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C       3.97884600    0.47564700   -0.29567400
C       2.77428600    0.09656900    0.26476300
C       1.77763100    0.96888600    0.67241000
C       0.47871400    0.53228400    1.29042500
C      -0.63230000    0.93704400    0.31229200
O      -1.38894400    0.24137400   -0.26859500
C       0.23111000    1.18349900    2.66994600
C      -1.05439400    0.70910400    3.35754200
C      -1.25844700    1.34937500    4.73318200
H       4.71902500   -0.25761800   -0.58812800
H       4.21681200    1.52035100   -0.46196900
H       2.59273400   -0.96828800    0.40094000
H       1.91790000    2.03858300    0.53977400
H       0.45034400   -0.56142100    1.38196800
H       1.09675800    0.95758300    3.30188200
H       0.20679400    2.27204300    2.54543200
H      -1.91598700    0.93310800    2.71863000
H      -1.02636400   -0.38206900    3.46028700
H      -0.42835200    1.11486500    5.40670600
H      -2.17847200    0.99246100    5.20304000
H      -1.32561800    2.43883500    4.65662600
""",
)

entry(
    index = 3,
    label = "TB4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {8,S} {19,D}
7  C u0 p0 c0 {4,S} {8,D} {20,S}
8  C u0 p0 c0 {6,S} {7,D} {21,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u0 p2 c0 {6,D}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56936,0.0565729,1.14598e-07,-2.69437e-08,1.0622e-11,-23430.4,12.8066], Tmin=(10,'K'), Tmax=(1129.44,'K')),
            NASAPolynomial(coeffs=[10.0563,0.0555609,-2.77092e-05,6.69655e-09,-6.35143e-13,-26296.5,-25.4801], Tmin=(1129.44,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-194.777,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (494.711,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 12, 'C=C': 1, 'C=O': 1, 'C-C': 7}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.90 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 24.44 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 23.14 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       3.14439200   -0.38760300    0.30955400
C       1.84726500    0.42531100    0.35166400
C       1.98474300    1.80060100   -0.31082500
C       0.69915000    2.63654500   -0.29163800
C       0.26517500    3.19292400    1.08296500
C       0.03492400    4.66361500    0.83919100
C       0.33273500    5.04374800   -0.40832800
C       0.80995700    3.88338200   -1.19392800
O       1.22176900    3.88927200   -2.33260700
H       3.95234400    0.12856700    0.83735700
H       3.47422800   -0.54900500   -0.72111800
H       3.01624000   -1.36805800    0.77601100
H       1.52698500    0.54342000    1.39378600
H       1.04852700   -0.13383400   -0.15068100
H       2.78746900    2.36705800    0.17930500
H       2.28770100    1.67978200   -1.35602200
H      -0.11231200    2.03216900   -0.71643600
H      -0.63511100    2.71085600    1.47800600
H       1.04299300    3.05347300    1.84387200
H      -0.32402200    5.32440600    1.62089600
H       0.27063500    6.04222200   -0.82048300
""",
)

entry(
    index = 4,
    label = "TB5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {5,D} {7,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  C u0 p0 c0 {2,D} {6,S} {11,S}
6  C u1 p0 c0 {5,S} {13,S} {14,S}
7  O u0 p2 c0 {1,S} {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91485,0.00505625,0.000160959,-2.9543e-07,1.69391e-10,6296.87,11.5333], Tmin=(10,'K'), Tmax=(537.633,'K')),
            NASAPolynomial(coeffs=[-1.05845,0.0593558,-3.87989e-05,1.21151e-08,-1.44555e-12,6581.63,30.1152], Tmin=(537.633,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (52.3216,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'C-H': 7, 'C=C': 2, 'C-O': 2}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [8, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
C       2.56557700    0.69744500    0.13396200
C       1.62668700   -0.27552700   -0.01391200
C       1.89407000   -1.64630400   -0.20921300
C       1.00076800   -2.73371200   -0.37320100
C       1.71879900   -3.87809400   -0.53219100
C       3.17282800   -3.52176700   -0.46893700
O       3.18783400   -2.09251600   -0.26289700
H       2.27958200    1.73081700    0.28050000
H       3.62234200    0.46423500    0.10902400
H       0.57304800   -0.01399700    0.01513200
H      -0.07539700   -2.63711400   -0.36810400
H       1.34431800   -4.88001900   -0.67961100
H       3.71002200   -3.99674000    0.36306400
H       3.72440900   -3.74381900   -1.39243800
""",
)

entry(
    index = 5,
    label = "TB6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {9,S}
2  C u0 p0 c0 {1,D} {4,S} {7,S}
3  C u0 p0 c0 {1,S} {5,D} {8,S}
4  C u0 p0 c0 {2,S} {6,D} {10,S}
5  C u0 p0 c0 {3,D} {11,S} {12,S}
6  C u0 p0 c0 {4,D} {13,S} {14,S}
7  O u1 p2 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74465,0.0202156,0.000180536,-4.97035e-07,4.06193e-10,8490.7,11.8934], Tmin=(10,'K'), Tmax=(406.181,'K')),
            NASAPolynomial(coeffs=[2.97408,0.0532155,-3.51727e-05,1.10332e-08,-1.31807e-12,8343.67,12.3364], Tmin=(406.181,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (70.598,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (320.107,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'C-H': 7, 'C=C': 3, 'C-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 66.45 kJ/mol
pivots: [4, 6], dihedral: [3, 4, 6, 7], rotor symmetry: 1, max scan energy: 26.16 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 47.92 kJ/mol
* Invalidated! pivots: [1, 2], dihedral: [8, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
C       2.46719900   -1.36385100    0.54863300
C       1.85174800   -0.20836800    0.15262100
C       2.51992900    0.99964100   -0.08121000
C       1.80750800    2.20289800   -0.50342100
O       0.58800000    2.20454300   -0.67139300
C       2.63121900    3.42907000   -0.72078200
C       2.08140100    4.57988300   -1.10651900
H       1.90483500   -2.27387200    0.71667800
H       3.53955800   -1.40717100    0.70762400
H       0.77622400   -0.19464800    0.00117400
H       3.59659300    1.05052500    0.05298000
H       3.70165700    3.35150800   -0.55282400
H       2.67277500    5.47361700   -1.26618800
H       1.01067100    4.63781500   -1.26922500
""",
)

entry(
    index = 6,
    label = "TB7",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {5,S}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {5,D} {9,S}
4  C u0 p0 c0 {2,S} {6,D} {10,S}
5  C u0 p0 c0 {1,S} {3,D} {6,S}
6  C u0 p0 c0 {4,D} {5,S} {11,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0945,-0.00914745,0.000179528,-3.11949e-07,1.72915e-10,7230.53,10.5421], Tmin=(10,'K'), Tmax=(575.423,'K')),
            NASAPolynomial(coeffs=[0.211161,0.0442362,-2.8421e-05,8.6726e-09,-1.00923e-12,7240.56,23.3346], Tmin=(575.423,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (60.099,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'C-H': 5, 'C-O': 1, 'C=C': 2}

External symmetry: 1, optical isomers: 1

Geometry:
O      -2.11183600    1.44157200   -0.34260300
C      -1.09179700    0.77674700   -0.18192800
C      -1.00461600   -0.65589200    0.04189600
C       0.42204500   -1.06270700    0.18675400
C       1.16236300    0.25104200    0.02907400
C       0.31953000    1.26955000   -0.17533300
H      -1.86259200   -1.31232300    0.09237900
H       0.72574600   -1.79975800   -0.57011800
H       0.62553700   -1.53589300    1.15784600
H       2.24203400    0.31669200    0.08166200
H       0.57358500    2.31097000   -0.31962800
""",
)

entry(
    index = 7,
    label = "TB8",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {7,S}
2  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {5,D}
4  C u0 p0 c0 {2,S} {8,D} {11,S}
5  C u0 p0 c0 {3,D} {6,S} {12,S}
6  C u0 p0 c0 {5,S} {7,D} {13,S}
7  C u0 p0 c0 {1,S} {6,D} {14,S}
8  C u0 p0 c0 {4,D} {15,S} {16,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93819,0.00441581,0.000223009,-4.91293e-07,3.57711e-10,-1173.84,15.2268], Tmin=(10,'K'), Tmax=(350.921,'K')),
            NASAPolynomial(coeffs=[-1.50772,0.0664957,-4.23677e-05,1.28938e-08,-1.50218e-12,-791.649,35.7968], Tmin=(350.921,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-9.75185,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 3, 'C-H': 8, 'C=C': 3, 'C-O': 2}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for TB8 exists which is 2.43 kJ/mol lower.Another conformer for TB8 exists which is 2.43 kJ/mol lower.
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 8.71 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -3.03873800   -0.72658000    0.90310200
C      -2.10857200    0.05955800    0.37309100
C      -1.12418200   -0.36844900   -0.68978700
C      -1.19470600    0.45643300   -1.93394500
C      -0.34167600    1.33985200   -2.52215700
C      -0.99345800    1.81495500   -3.70827600
C      -2.19470100    1.18611700   -3.75263700
O      -2.33647200    0.35532200   -2.68038500
H      -3.71793500   -0.36700300    1.66768100
H      -3.15698300   -1.75932000    0.58922200
H      -2.02411600    1.09333600    0.70159000
H      -1.28698300   -1.42373700   -0.93479800
H      -0.10323800   -0.28278300   -0.30144900
H       0.63493200    1.61785900   -2.15804100
H      -0.61410800    2.52540400   -4.42541800
H      -3.02364100    1.21058900   -4.43936600
""",
)

entry(
    index = 8,
    label = "TB9",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47381,0.0578817,-0.000238343,6.11233e-07,-5.31602e-10,-8196.22,11.9037], Tmin=(10,'K'), Tmax=(401.316,'K')),
            NASAPolynomial(coeffs=[1.247,0.0402143,-2.33129e-05,6.51511e-09,-7.05963e-13,-7696.49,24.6131], Tmin=(401.316,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-68.1679,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 2, 'C-H': 7, 'O-O': 1, 'C-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.63 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 19.13 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 12.18 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.59008800   -0.06910500   -0.04184300
C      -0.21016700   -0.17188000    0.61280800
C       0.10210500   -1.55303400    1.16802700
O      -0.82443400   -1.92356100    2.23926500
O      -0.60771900   -1.21564900    3.33004900
H      -2.38109900   -0.31568200    0.66977700
H      -1.77225800    0.94401500   -0.40753600
H      -1.67862300   -0.75218400   -0.89219200
H       0.57428300    0.07458300   -0.11150600
H      -0.11804100    0.54651600    1.43242300
H      -0.04147100   -2.34296700    0.42735700
H       1.10838300   -1.61092000    1.58631200
""",
)

entry(
    index = 10,
    label = "TB10",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  C u1 p0 c0 {1,D} {4,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.42577,0.0552483,-0.000102567,1.93129e-07,-1.41819e-10,-11714.3,12.9525], Tmin=(10,'K'), Tmax=(471.22,'K')),
            NASAPolynomial(coeffs=[1.9455,0.049925,-2.86778e-05,8.03163e-09,-8.7749e-13,-11376.2,21.0875], Tmin=(471.22,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-97.4162,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (345.051,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 4, 'C-H': 9, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [7, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.89 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 23.09 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 22.24 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Another conformer for TB10 exists which is 1.37 kJ/mol lower.Another conformer for TB10 exists which is 1.37 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
C       2.14521500   -0.50295600    0.08536900
C       0.94242100    0.39919600    0.37487400
C      -0.39072100   -0.24342900   -0.02476200
C      -1.61902300    0.63079100    0.27407500
C      -1.76371800    1.86747500   -0.60000300
O      -1.09020600    2.20888600   -1.50936800
H       2.21539900   -0.73602800   -0.98139700
H       2.07170800   -1.45065100    0.62813000
H       3.08115700   -0.02231100    0.38157700
H       1.06004100    1.34630300   -0.15996800
H       0.91753700    0.64419200    1.44385900
H      -0.37680700   -0.48233100   -1.09338900
H      -0.51171600   -1.19420300    0.50788200
H      -1.63307100    0.97648000    1.31381200
H      -2.55356300    0.07359600    0.14195800
""",
)

entry(
    index = 11,
    label = "TB11",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u1 p0 c0 {2,D} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94764,0.00319149,5.64828e-05,-1.18956e-07,7.50654e-11,41022.3,5.4829], Tmin=(10,'K'), Tmax=(537.535,'K')),
            NASAPolynomial(coeffs=[3.91782,0.0150707,-9.19614e-06,2.84527e-09,-3.46567e-13,40857.1,4.04168], Tmin=(537.535,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (341.061,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 3, 'C=C': 2}

External symmetry: 2, optical isomers: 1

Geometry:
C       1.50226700   -0.00969800    0.11174200
C       0.28357700   -0.00183100    0.02109300
C      -1.07978000    0.00697100   -0.08031700
H       2.56148000   -0.01653600    0.19052900
H      -1.62316900    0.93822700   -0.18356100
H      -1.64437500   -0.91713300   -0.05948700
""",
)

