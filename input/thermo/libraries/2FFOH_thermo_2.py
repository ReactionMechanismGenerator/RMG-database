#!/usr/bin/env python
# encoding: utf-8

name = "2FFOH_thermo_2"
shortDesc = ""
longDesc = """
ARC v1.1.0
ARC project 2FFOH_thermo_2

Levels of theory used:

Conformers:       wb97xd/def2svp, software: gaussian (dft)
TS guesses:       None
Composite method: cbs-qb3, software: gaussian (composite) (using a fine grid)
Frequencies:      b3lyp/cbsb7, software: gaussian (dft)
Rotor scans:      b3lyp/cbsb7, software: gaussian (dft)
Using p-type bond additivity corrections for thermo

Using the following ESS settings: {'gaussian': ['local'], 'molpro': ['local']}

Considered the following species and TSs:
Species PROO1 (run time: 5:07:47)
Species PROO2 (run time: 7:26:53)
Species PROO3 (run time: 12:35:09)
Species PROO4 (run time: 3:41:19)
Species PROO5 (run time: 6:28:36)
Species PROO6 (run time: 6:49:31)
Species PROO7 (run time: 10:23:56)
Species PROO8 (run time: 5:42:34)
Species PROO9 (run time: 4:10:57)
Species PROO10 (run time: 2:59:04)
Species PROO11 (run time: 23:56:12)
Species PROO12 (run time: 1 day, 3:14:47)
Species PROO13 (run time: 17:23:51)
Species PROO14 (run time: 13:51:56)

Overall time since project initiation: 21:30:33
"""
entry(
    index = 0,
    label = "PROO1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {2,D} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {6,S} {13,S}
6  O u0 p2 c0 {2,S} {5,S}
7  O u0 p2 c0 {1,S} {8,S}
8  O u0 p2 c0 {7,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75239,0.0441119,-4.78448e-06,-2.04444e-08,9.25977e-12,-1828.09,14.4039], Tmin=(10,'K'), Tmax=(1073.8,'K')),
            NASAPolynomial(coeffs=[11.3866,0.0348252,-1.85641e-05,4.7196e-09,-4.65711e-13,-4571.73,-28.1113], Tmin=(1073.8,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-15.1288,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 2, 'C-O': 3, 'C=C': 2, 'O-O': 2}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for PROO1 exists which is 5.83 kJ/mol lower.Another conformer for PROO1 exists which is 5.83 kJ/mol lower.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Bond ([[2, 3]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[2, 3]]) broke during the scan. But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       3.78436700    0.80395700   -0.74701200
O       3.02176800    0.62036000   -1.68100400
O       1.43572500    0.23190300   -1.23181100
C       1.42245600   -0.03285900    0.13743100
C       1.51167700   -1.47787700    0.48738300
C       2.49714000   -2.25235000    1.02003700
C       1.97806900   -3.58535100    1.08624000
C       0.71629500   -3.52064800    0.58766500
O       0.41304400   -2.24669800    0.21931400
H       0.50305200    0.42758200    0.52278800
H       2.25888600    0.50453200    0.61923600
H       3.47578000   -1.91560300    1.32382400
H       2.47813800   -4.46664100    1.45472300
H      -0.06098600   -4.25034100    0.43617000
""",
)

entry(
    index = 1,
    label = "PROO2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {6,S} {12,S}
6  O u0 p2 c0 {2,S} {5,S}
7  O u0 p2 c0 {1,S} {13,S}
8  O u0 p2 c0 {1,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 O u1 p2 c0 {7,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61645,0.0378065,3.73332e-05,-9.67064e-08,5.07771e-11,-25552.6,14.7008], Tmin=(10,'K'), Tmax=(717.741,'K')),
            NASAPolynomial(coeffs=[5.81753,0.0477489,-2.986e-05,8.81711e-09,-9.94836e-13,-26440.6,0.826698], Tmin=(717.741,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-212.488,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-C': 2, 'C-O': 4, 'C=C': 2, 'H-O': 1, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 11], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 5], dihedral: [2, 3, 5, 6], rotor symmetry: 1, max scan energy: 19.97 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -3.04267600   -1.62259200    0.63179500
O      -1.78002800   -1.51018700    0.30847600
C      -1.45327500   -0.04044200   -0.03817600
O      -2.15561300    0.77440000    0.80420300
C       0.00007800    0.13183700    0.12688800
C       0.76926900    0.57352900    1.15875800
C       2.12371400    0.48005600    0.71109100
C       2.07208500   -0.01259800   -0.55530700
O       0.78379400   -0.22948600   -0.93122000
H      -1.75985000    0.01416200   -1.08947000
H      -3.04231700    0.38094000    0.87195000
H       0.40626000    0.92526900    2.11021000
H       3.01324100    0.74676600    1.25875400
H       2.82093200   -0.25240800   -1.29086500
""",
)

entry(
    index = 2,
    label = "PROO3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {2,D} {4,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {6,S} {12,S}
6  O u0 p2 c0 {2,S} {5,S}
7  O u0 p2 c0 {1,S} {13,S}
8  O u0 p2 c0 {3,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
14 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69324,0.0293249,7.41076e-05,-1.55461e-07,8.34591e-11,-20772.3,13.7085], Tmin=(10,'K'), Tmax=(656.083,'K')),
            NASAPolynomial(coeffs=[4.0388,0.0516298,-3.27003e-05,9.78219e-09,-1.11706e-12,-21343,8.18299], Tmin=(656.083,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-172.75,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-C': 2, 'C-O': 4, 'C=C': 2, 'H-O': 1, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for PROO3 exists which is 6.66 kJ/mol lower.Another conformer for PROO3 exists which is 6.66 kJ/mol lower.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 12], invalidation reason: Inconsistent initial and final conformers But unable to propose troubleshooting methods.Inconsistent initial and final conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       0.36014000    2.30345400    1.27426100
O      -0.78759700    1.95715500    0.69238800
C      -0.85663200    0.66165000    0.26008700
C       0.13000000   -0.29432900    0.20946400
C       1.56855700   -0.32571600    0.61840100
O       1.75142200   -0.12602700    2.00853300
O      -0.42376200   -1.42475300   -0.30687500
C      -1.73752600   -1.17397200   -0.58593200
C      -2.06375200    0.09849900   -0.25724800
H       1.96309500   -1.31407100    0.37763900
H       2.12641800    0.41710900    0.03284900
H       1.46108200    0.78005900    2.18213400
H      -2.29191400   -1.99439700   -1.00760200
H      -3.01986300    0.58509700   -0.35475600
""",
)

entry(
    index = 3,
    label = "PROO4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {4,S} {5,D} {8,S}
4  C u0 p0 c0 {2,D} {3,S} {11,S}
5  C u0 p0 c0 {3,D} {6,S} {12,S}
6  O u0 p2 c0 {2,S} {5,S}
7  O u0 p2 c0 {1,S} {13,S}
8  O u0 p2 c0 {3,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
14 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6226,0.0525941,-3.3794e-05,8.97464e-09,-5.25932e-13,-20465.3,14.7943], Tmin=(10,'K'), Tmax=(1332.44,'K')),
            NASAPolynomial(coeffs=[15.9515,0.0241228,-1.13566e-05,2.55876e-09,-2.24689e-13,-24508.9,-51.0692], Tmin=(1332.44,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-170.144,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (320.107,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-C': 2, 'C-O': 4, 'C=C': 2, 'H-O': 1, 'O-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 18.43 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 10.33 kJ/mol
pivots: [7, 8], dihedral: [6, 7, 8, 13], rotor symmetry: 1, max scan energy: 10.28 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -3.23353700   -1.67930700   -0.16966800
O      -3.08122600   -0.36736000   -0.02217200
C      -1.77398400    0.02359900    0.12708800
C      -1.40399700    1.32551700    0.28922500
O      -0.05030900    1.38135600    0.40214000
C       0.43056400    0.09610400    0.31623700
C       1.90733100   -0.05251600    0.45231500
O       2.38246300    0.25196600    1.76062000
C      -0.59463800   -0.77953200    0.14725500
H      -1.94880500    2.25134700    0.33817800
H       2.40831600    0.57023900   -0.30165000
H       2.17345600   -1.09213000    0.26025300
H       2.17833800    1.17631800    1.93625600
H      -0.54423200   -1.85007900    0.05359500
""",
)

entry(
    index = 4,
    label = "PROO5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {2,D} {5,S} {12,S}
4  C u0 p0 c0 {5,D} {6,S} {8,S}
5  C u0 p0 c0 {3,S} {4,D} {11,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {1,S} {13,S}
8  O u0 p2 c0 {4,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67546,0.0504661,-2.86654e-05,5.09299e-09,4.67249e-13,-20961.2,14.0589], Tmin=(10,'K'), Tmax=(1316.21,'K')),
            NASAPolynomial(coeffs=[15.7247,0.0245555,-1.13392e-05,2.49778e-09,-2.13748e-13,-25060.6,-50.9055], Tmin=(1316.21,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-174.257,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 4, 'C-C': 2, 'C-O': 4, 'C=C': 2, 'H-O': 1, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for PROO5 exists which is 2.66 kJ/mol lower.Another conformer for PROO5 exists which is 2.66 kJ/mol lower.
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 12.26 kJ/mol
pivots: [7, 8], dihedral: [6, 7, 8, 14], rotor symmetry: 1, max scan energy: 11.25 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       3.69830600    1.25998900    0.57930100
O       2.41357400    1.62059000    0.60125000
C       1.56774200    0.62641200    0.24877700
C       1.72256600   -0.67450300   -0.12660700
C       0.39231500   -1.14278500   -0.34925100
C      -0.45638800   -0.10388900   -0.10233700
C      -1.93498100    0.06565600   -0.11213400
O      -2.49822000    0.18857600    1.19184000
O       0.27475300    1.00557000    0.27126100
H       2.65597500   -1.20052400   -0.22124400
H       0.10015100   -2.13544700   -0.65325600
H      -2.20250800    0.92819200   -0.73758800
H      -2.38197700   -0.82366100   -0.55754200
H      -2.15000000    0.99519200    1.58583400
""",
)

entry(
    index = 5,
    label = "PROO6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {6,S} {14,S}
6  O u0 p2 c0 {1,S} {5,S}
7  O u0 p2 c0 {2,S} {15,S}
8  O u0 p2 c0 {3,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 O u1 p2 c0 {7,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47759,0.0502758,-1.66504e-06,-3.59321e-08,1.8808e-11,-30803.5,14.8504], Tmin=(10,'K'), Tmax=(845.939,'K')),
            NASAPolynomial(coeffs=[7.10084,0.0493343,-2.87051e-05,8.00286e-09,-8.62546e-13,-31995.8,-5.44762], Tmin=(845.939,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-256.142,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (374.151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C-C': 3, 'C-O': 4, 'C=C': 1, 'H-O': 1, 'O-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 11.39 kJ/mol
* Invalidated! pivots: [7, 8], dihedral: [3, 7, 8, 9], invalidation reason: Inconsistent initial and final conformers But unable to propose troubleshooting methods.Inconsistent initial and final conformers But unable to propose troubleshooting methods.
pivots: [8, 9], dihedral: [7, 8, 9, 16], rotor symmetry: 1, max scan energy: 15.15 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.63198500   -2.58133900    0.60088600
O      -1.76041700   -1.32199500    0.96567600
C      -1.00807600   -0.42345300    0.05343400
C      -1.20002700    0.98761800    0.48855600
C      -0.01248600    1.47573300    0.85098400
O       1.04057500    0.62589600    0.72622400
C       0.51229300   -0.64002200    0.21697900
C       1.24817200   -0.98046000   -1.06856400
O       0.99813100   -0.03796100   -2.09748300
H      -1.36920700   -0.66362700   -0.94738100
H      -2.13990200    1.51542800    0.49265400
H       0.24563200    2.45811900    1.22210300
H       0.70058300   -1.40409800    0.97448300
H       0.88774400   -1.94646600   -1.42885100
H       2.32082400   -1.07060500   -0.85383200
H       1.35186600    0.80768800   -1.80136900
""",
)

entry(
    index = 6,
    label = "PROO7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {6,S} {14,S}
6  O u0 p2 c0 {1,S} {5,S}
7  O u0 p2 c0 {1,S} {15,S}
8  O u0 p2 c0 {3,S} {16,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 O u1 p2 c0 {7,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76706,0.0154498,0.000242062,-5.75234e-07,4.08093e-10,-33260,14.1814], Tmin=(10,'K'), Tmax=(475.507,'K')),
            NASAPolynomial(coeffs=[3.3406,0.0621866,-4.14868e-05,1.31409e-08,-1.58093e-12,-33707.2,10.7923], Tmin=(475.507,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-276.583,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C-C': 3, 'C-O': 4, 'C=C': 1, 'H-O': 1, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for PROO7 exists which is 1.18 kJ/mol lower.Another conformer for PROO7 exists which is 1.18 kJ/mol lower.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [4, 5], dihedral: [3, 4, 5, 12], rotor symmetry: 1, max scan energy: 21.44 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.04767400    1.57008100    1.62037500
O       0.40917500    1.71750200    0.47910900
C       0.16639400    0.40655600   -0.19684100
C       1.51092700   -0.10304900   -0.70166700
O       1.36128900   -1.31397500   -1.41525200
C      -0.66633600   -0.51381600    0.70203700
C      -2.05550300   -0.27650900    0.16217200
C      -1.95375400    0.43113200   -0.95495700
O      -0.64560000    0.75920700   -1.29464600
H       2.15477300   -0.30347200    0.15483500
H       1.96907600    0.68625800   -1.30980800
H       0.82332500   -1.12249300   -2.19176900
H      -0.52423800   -0.23967500    1.74877200
H      -0.34818500   -1.55313000    0.57352200
H      -2.97036000   -0.65018500    0.59450400
H      -2.69568000    0.78431900   -1.65411800
""",
)

entry(
    index = 7,
    label = "PROO8",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {8,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  C u0 p0 c0 {2,S} {4,D} {14,S}
6  O u0 p2 c0 {1,S} {4,S}
7  O u0 p2 c0 {1,S} {15,S}
8  O u0 p2 c0 {3,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 O u1 p2 c0 {7,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43009,0.0544469,-1.86739e-05,-1.27607e-08,8.41517e-12,-32180.4,14.1082], Tmin=(10,'K'), Tmax=(940.776,'K')),
            NASAPolynomial(coeffs=[8.50118,0.0458906,-2.57668e-05,6.95939e-09,-7.29926e-13,-33710,-13.106], Tmin=(940.776,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-267.59,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (374.151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C-C': 3, 'C-O': 4, 'C=C': 1, 'H-O': 1, 'O-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 9.47 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 8], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [7, 8], dihedral: [6, 7, 8, 16], rotor symmetry: 1, max scan energy: 17.01 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.28952100    2.48923300    0.38539000
O      -1.93163400    1.30715900    0.84995900
C      -1.50288800    0.41851200   -0.23354200
C      -1.40536100   -0.99287700    0.35787900
C       0.08778100   -1.14254600    0.52182300
C       0.68979100   -0.11223100   -0.06355600
C       2.11735000    0.28225400   -0.24031400
O       2.40265100    1.54462300    0.34776800
O      -0.20554600    0.78964600   -0.64155100
H      -2.19557500    0.58507400   -1.05489500
H      -1.83433100   -1.73725300   -0.32069500
H      -1.95929700   -1.04114700    1.29910300
H       0.58015200   -1.95798400    1.02772300
H       2.76028400   -0.45069400    0.24764800
H       2.35592900    0.28521800   -1.31431900
H       1.77105800    2.17623700   -0.01390600
""",
)

entry(
    index = 8,
    label = "PROO9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {8,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  C u0 p0 c0 {1,S} {4,D} {14,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {1,S} {15,S}
8  O u0 p2 c0 {3,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 O u1 p2 c0 {7,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37327,0.0596336,-3.69599e-05,8.25284e-09,3.17802e-13,-30785.9,14.5938], Tmin=(10,'K'), Tmax=(1117.01,'K')),
            NASAPolynomial(coeffs=[11.4328,0.0391724,-2.07627e-05,5.31781e-09,-5.31994e-13,-33110.4,-27.526], Tmin=(1117.01,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-256.003,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (369.994,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 6, 'C-C': 3, 'C-O': 4, 'C=C': 1, 'H-O': 1, 'O-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 11.39 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 13.87 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 14], rotor symmetry: 1, max scan energy: 15.31 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -3.35467000    0.27679100   -1.52731500
O      -2.04045000    0.30678300   -1.47463300
C      -1.55983300    0.48170900   -0.06711400
C      -0.07145900    0.48468100   -0.08156800
C       0.35277400   -0.69831500    0.38295100
C       1.72234900   -1.28698400    0.50483200
O       2.00361900   -1.72328100    1.82673500
O      -0.64147500   -1.52434400    0.82152100
C      -1.87084200   -0.75799500    0.77344200
H      -2.06066300    1.38368300    0.28327100
H       0.54708500    1.27531600   -0.47412500
H       2.46867700   -0.53507300    0.24863800
H       1.81070200   -2.11417900   -0.21505700
H       1.30219200   -2.33404900    2.07794700
H      -2.13306700   -0.48207900    1.79742100
H      -2.65840900   -1.37170600    0.33988400
""",
)

entry(
    index = 9,
    label = "PROO10",
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
Bond corrections: {'C-H': 5, 'C-C': 2, 'C-O': 3, 'C=C': 2, 'O-O': 1}
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
    index = 10,
    label = "PROO11",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {10,S}
3  C u0 p0 c0 {1,S} {9,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {6,S} {14,S}
6  O u0 p2 c0 {1,S} {5,S}
7  O u0 p2 c0 {1,S} {16,S}
8  O u0 p2 c0 {2,S} {15,S}
9  O u0 p2 c0 {3,S} {17,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 O u1 p2 c0 {8,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74691,0.016419,0.000261795,-6.00516e-07,4.10049e-10,-54880.8,14.8232], Tmin=(10,'K'), Tmax=(492.997,'K')),
            NASAPolynomial(coeffs=[2.90751,0.0708885,-4.89423e-05,1.57768e-08,-1.9119e-12,-55377.2,12.4052], Tmin=(492.997,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-456.366,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 3, 'C-O': 5, 'C=C': 1, 'H-O': 2, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for PROO11 exists which is 3.34 kJ/mol lower.Another conformer for PROO11 exists which is 3.34 kJ/mol lower.
* Invalidated! pivots: [7, 8], dihedral: [3, 7, 8, 14], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [7, 9], dihedral: [3, 7, 9, 10], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [9, 10], dihedral: [7, 9, 10, 17], rotor symmetry: 1, max scan energy: 25.67 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.34549900   -2.49140700    0.70331300
O      -1.18194800   -1.58352300    1.16331100
C      -0.92918000   -0.22512200    0.61754000
C      -1.16867900   -0.14489400   -0.84880700
C      -0.00834500    0.14154400   -1.44424800
O       1.05462900    0.32168200   -0.62177900
C       0.56431400    0.23793200    0.75178000
O       1.38241600   -0.57804600    1.50281900
C       0.66008900    1.63987700    1.35765900
O       0.16386500    1.65477600    2.68077000
H      -1.57987500    0.36907200    1.25845600
H      -2.11309800   -0.33000300   -1.33450900
H       0.21083900    0.25974100   -2.49652000
H       1.23632700   -1.49449100    1.21957400
H       1.71007900    1.94915800    1.29793200
H       0.05506200    2.33685600    0.77585000
H       0.67986800    1.00909200    3.17812000
""",
)

entry(
    index = 11,
    label = "PROO12",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {10,S}
3  C u0 p0 c0 {1,S} {9,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {6,S} {14,S}
6  O u0 p2 c0 {1,S} {5,S}
7  O u0 p2 c0 {1,S} {15,S}
8  O u0 p2 c0 {2,S} {17,S}
9  O u0 p2 c0 {3,S} {16,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 O u1 p2 c0 {7,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55627,0.0379992,0.000108905,-2.61394e-07,1.64095e-10,-51575.2,14.5875], Tmin=(10,'K'), Tmax=(552.823,'K')),
            NASAPolynomial(coeffs=[3.59979,0.0657433,-4.25085e-05,1.30125e-08,-1.51819e-12,-52008.8,10.5254], Tmin=(552.823,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-428.887,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (407.409,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 3, 'C-O': 5, 'C=C': 1, 'H-O': 2, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 13], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [9, 10], dihedral: [3, 9, 10, 17], invalidation reason: Another conformer for PROO12 exists which is 5.39 kJ/mol lower.Another conformer for PROO12 exists which is 5.39 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
O       0.89111800    0.67432900    2.27442000
O      -0.02235600   -0.13650200    1.77477900
C       0.12761600   -0.36181400    0.31873300
C       1.59658200   -0.52702700   -0.06321100
O       2.27142400    0.70148600   -0.20102400
O      -0.57004100   -1.57188900    0.12836800
C      -1.74617800   -1.27829700   -0.53694000
C      -1.88118300   -0.00779500   -0.89482700
C      -0.66189100    0.76360300   -0.45247500
O      -0.91222900    1.92514100    0.30623600
H       2.07320300   -1.19588600    0.66510400
H       1.61701200   -1.01901900   -1.03781900
H       2.21287500    1.14187600    0.65655600
H      -2.38734500   -2.13401100   -0.68606500
H      -2.71060800    0.42520200   -1.43170400
H      -0.05034300    1.10777300   -1.28845200
H      -1.47372400    1.68215500    1.05175500
""",
)

entry(
    index = 12,
    label = "PROO13",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {11,S}
3  C u0 p0 c0 {4,S} {9,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  C u0 p0 c0 {1,S} {4,D} {14,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {1,S} {17,S}
8  O u0 p2 c0 {2,S} {15,S}
9  O u0 p2 c0 {3,S} {16,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 O u1 p2 c0 {8,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.26057,0.0658094,-3.57415e-05,-2.01271e-09,6.28746e-12,-51581.4,15.5031], Tmin=(10,'K'), Tmax=(883.061,'K')),
            NASAPolynomial(coeffs=[9.408,0.0498447,-2.88052e-05,7.98707e-09,-8.57045e-13,-53130.4,-16.0131], Tmin=(883.061,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-428.936,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 3, 'C-O': 5, 'C=C': 1, 'H-O': 2, 'O-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 10.81 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: Another conformer for PROO13 exists which is 0.80 kJ/mol lower.Another conformer for PROO13 exists which is 0.80 kJ/mol lower.
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 14], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [9, 10], dihedral: [3, 9, 10, 17], rotor symmetry: 1, max scan energy: 21.07 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.38959400    2.58800400    0.37112000
O      -1.85180100    1.57316700    1.02501100
C      -1.55379200    0.46549700    0.13474500
O      -0.36406600    0.76403400   -0.56988900
C       0.64766800    0.02646600    0.01706800
C       2.01885900    0.34182000   -0.49229900
O       3.03390600   -0.34858300    0.20890600
C       0.22760100   -0.84323500    0.93754000
C      -1.27247200   -0.77505100    1.01686400
O      -1.93734200   -1.94433600    0.55384200
H      -2.38303200    0.36707300   -0.56176000
H       2.15663200    1.43193900   -0.47353800
H       2.09186200    0.03261900   -1.53908200
H       3.06556900    0.00158400    1.10524600
H       0.84709900   -1.53031700    1.49068000
H      -1.66101700   -0.59382100    2.02102700
H      -1.42984500   -2.28923700   -0.18966900
""",
)

entry(
    index = 13,
    label = "PROO14",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {11,S}
3  C u0 p0 c0 {4,S} {9,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  C u0 p0 c0 {1,S} {4,D} {14,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {1,S} {15,S}
8  O u0 p2 c0 {2,S} {17,S}
9  O u0 p2 c0 {3,S} {16,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 O u1 p2 c0 {7,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.18623,0.0761469,-7.40456e-05,4.40357e-08,-1.20084e-11,-53756.4,14.7375], Tmin=(10,'K'), Tmax=(778.624,'K')),
            NASAPolynomial(coeffs=[7.16855,0.0556887,-3.46333e-05,1.02904e-08,-1.17349e-12,-54376.5,-3.47837], Tmin=(778.624,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-447.02,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (394.937,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 3, 'C-O': 5, 'C=C': 1, 'H-O': 2, 'O-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 10.04 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 15.91 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 15], invalidation reason: Another conformer for PROO14 exists which is 1.36 kJ/mol lower.Another conformer for PROO14 exists which is 1.36 kJ/mol lower.
pivots: [9, 10], dihedral: [3, 9, 10, 17], rotor symmetry: 1, max scan energy: 16.78 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -3.30844000   -0.62300400    1.22780200
O      -2.02819800   -0.90670400    1.35327800
C      -1.29293300   -0.67243500    0.08341400
C       0.13796100   -1.01379400    0.29030000
C       0.83471400    0.12817300    0.32783800
C       2.29507100    0.36217400    0.55493800
O       2.98178800   -0.80201600    0.96933100
O       0.09033700    1.25990500    0.13905500
C      -1.24429300    0.83085900   -0.23745300
O      -1.43549300    0.99165100   -1.60454400
H      -1.83621900   -1.22002100   -0.68558800
H       0.54249800   -2.00709500    0.38772600
H       2.40483600    1.19515500    1.26402200
H       2.75769200    0.68124100   -0.38346000
H       2.63002800   -1.06296600    1.82704800
H      -1.94426300    1.41582600    0.36236500
H      -1.38966800    1.93170900   -1.80996400
""",
)

