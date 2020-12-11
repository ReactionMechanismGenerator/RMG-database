#!/usr/bin/env python
# encoding: utf-8

name = "Alon_thermo_1"
shortDesc = ""
longDesc = """
ARC v1.1.0
ARC project Alon_thermo_1

Levels of theory used:

Conformers:       wb97xd/def2tzvp, software: gaussian (dft)
TS guesses:       None
Composite method: cbs-qb3, software: gaussian (composite) (using a fine grid)
Frequencies:      b3lyp/cbsb7, software: gaussian (dft)
Rotor scans:      b3lyp/cbsb7, software: gaussian (dft)
Using p-type bond additivity corrections for thermo

Using the following ESS settings: {'gaussian': ['local'], 'orca': ['local']}

Considered the following species and TSs:
Species 1_heptene (run time: 4 days, 3:05:05)
Species 2_carbene_heptane (run time: 8 days, 5:05:47)
Species 1_heptyl (run time: 3 days, 7:18:51)
Species o_Xylene (run time: 1:09:06)
Species 1_octyl (Failed!) (run time: None)
Species 4_octyl (run time: 6 days, 13:35:09)
Species 1_pentyl (run time: 8 days, 9:57:43)
Species 5_pentyl (run time: 8 days, 7:17:39)
Species C8H9O2 (run time: 3 days, 2:55:36)
Species C7H7O2 (run time: 5 days, 5:10:45)
Species 2_dodecyl (run time: 2 days, 12:41:18)
Species 3_dodecyl (run time: 3 days, 10:59:12)

Overall time since project initiation: 16:12:48
"""
entry(
    index = 0,
    label = "1_heptene",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {7,D} {19,S}
7  C u0 p0 c0 {6,D} {20,S} {21,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37007,0.0677673,-0.000174812,4.9354e-07,-4.51577e-10,-11043.7,12.6269], Tmin=(10,'K'), Tmax=(420.929,'K')),
            NASAPolynomial(coeffs=[-3.18615,0.0809203,-4.65367e-05,1.29826e-08,-1.40934e-12,-10056.3,43.7559], Tmin=(420.929,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-91.8417,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C-H': 14, 'C-C': 5}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: 
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Another conformer for 1_heptene exists which is 1.26 kJ/mol lower.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: 
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: 
pivots: [6, 7], dihedral: [5, 6, 7, 19], rotor symmetry: 3, max scan energy: 11.86 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       3.27497600    0.92236600   -1.01826000
C       2.33383400    0.16391900   -0.46388500
C       2.38419700   -0.41216500    0.92295100
C       2.34620200   -1.95113400    0.93901000
C       2.35206300   -2.54257200    2.35268800
C       2.31739200   -4.07494900    2.37642600
C       2.32534700   -4.65871700    3.79214200
H       3.17966400    1.30186800   -2.02952100
H       4.17677500    1.19479000   -0.47745200
H       1.44727200   -0.08392600   -1.04710300
H       1.52841200   -0.03618900    1.50030400
H       3.28621000   -0.05941300    1.43518400
H       1.45202500   -2.29591700    0.40444100
H       3.20523800   -2.33394400    0.37563800
H       3.24485100   -2.19387700    2.88790000
H       1.49166000   -2.15308600    2.91246100
H       3.17655800   -4.46332200    1.81636800
H       1.42486100   -4.42351200    1.84278900
H       1.45879700   -4.31601700    4.36630700
H       2.29989800   -5.75169400    3.77400300
H       3.22380500   -4.35669700    4.33944200
""",
)

entry(
    index = 1,
    label = "2_carbene_heptane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
7  C u0 p1 c0 {4,S} {6,S}
8  H u0 p0 c0 {1,S}
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
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.99689,0.0935542,-0.000214033,3.91448e-07,-2.67134e-10,22191.2,12.7127], Tmin=(10,'K'), Tmax=(496.248,'K')),
            NASAPolynomial(coeffs=[1.08084,0.0726387,-4.09083e-05,1.12234e-08,-1.20326e-12,22829.1,25.1249], Tmin=(496.248,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (184.477,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (494.711,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 14, 'C-C': 6}
1D rotors:
pivots: [1, 2], dihedral: [3, 1, 2, 4], rotor symmetry: 1, max scan energy: 22.79 kJ/mol
pivots: [1, 3], dihedral: [2, 1, 3, 5], rotor symmetry: 1, max scan energy: 23.08 kJ/mol
pivots: [2, 4], dihedral: [1, 2, 4, 7], rotor symmetry: 1, max scan energy: 15.86 kJ/mol
* Invalidated! pivots: [3, 5], dihedral: [1, 3, 5, 16], invalidation reason: 
* Invalidated! pivots: [4, 7], dihedral: [2, 4, 7, 6], invalidation reason: 
* Invalidated! pivots: [6, 7], dihedral: [19, 6, 7, 4], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
C       1.92849100    0.29836500   -3.99386500
C       2.26086900    0.14147600   -2.50640400
C       2.21744100   -0.95620000   -4.82440300
C       1.94341500    1.41190500   -1.70972900
C       1.87641200   -0.79062900   -6.30812600
C       0.28931700    3.14596600   -1.19358500
C       0.52623300    1.72036400   -1.48487700
H       0.86687000    0.56147700   -4.08665100
H       2.49455600    1.14439400   -4.40728700
H       3.27645600   -1.22275100   -4.72050200
H       1.64999600   -1.79830900   -4.41078300
H       1.67816200   -0.68468000   -2.08699100
H       3.32092000   -0.11345100   -2.38956100
H       2.20402100    1.24759300   -0.63825300
H       2.57739100    2.26556700   -2.01963100
H       2.45515500    0.02172100   -6.75909500
H       2.09046000   -1.70279000   -6.87182800
H       0.81623600   -0.55633500   -6.44544400
H      -0.05347000    3.49519400   -2.18712800
H      -0.55992900    3.32314000   -0.52873200
H       1.15542600    3.77086200   -0.91373000
""",
)

entry(
    index = 2,
    label = "1_heptyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  C u1 p0 c0 {5,S} {21,S} {22,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.92592,0.100465,-0.000249798,4.63096e-07,-3.14529e-10,-1776.86,14.6177], Tmin=(10,'K'), Tmax=(498.272,'K')),
            NASAPolynomial(coeffs=[0.904681,0.0738684,-4.08185e-05,1.10109e-08,-1.16343e-12,-1043.85,28.2953], Tmin=(498.272,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-14.8038,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (511.34,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 15, 'C-C': 6}
1D rotors:
pivots: [1, 4], dihedral: [2, 1, 4, 5], rotor symmetry: 1, max scan energy: 0.64 kJ/mol (set as a FreeRotor)
* Invalidated! pivots: [4, 5], dihedral: [1, 4, 5, 6], invalidation reason: Significant difference observed between consecutive conformers
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 23.54 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 23.43 kJ/mol
pivots: [7, 8], dihedral: [6, 7, 8, 9], rotor symmetry: 1, max scan energy: 23.47 kJ/mol
pivots: [8, 9], dihedral: [7, 8, 9, 20], rotor symmetry: 3, max scan energy: 11.86 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       3.94743200   -0.44351000    0.41630500
H       4.03008800   -1.48990400    0.14884600
H       4.82160300    0.03966200    0.83805900
C       2.74603000    0.35318700    0.04199200
C       2.53261400    1.60508600    0.90743600
C       1.31206200    2.43340900    0.49297600
C       1.09829900    3.68336500    1.35381700
C      -0.12311400    4.51303700    0.94161200
C      -0.32874800    5.75967200    1.80685100
H       1.85071700   -0.28131400    0.08199900
H       2.81962500    0.66984600   -1.01458300
H       3.43232700    2.23122500    0.85606300
H       2.43124800    1.30124100    1.95602500
H       0.41409300    1.80383000    0.54131400
H       1.41699700    2.73171800   -0.55829600
H       1.99545000    4.31424700    1.30570600
H       0.99365800    3.38560100    2.40522900
H      -0.01857300    4.81088100   -0.10877900
H      -1.01959000    3.88302900    0.99024400
H       0.53713700    6.42689700    1.75126000
H      -1.20646500    6.32819100    1.48737900
H      -0.47142700    5.49197200    2.85851700
""",
)

entry(
    index = 3,
    label = "o_Xylene",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,B} {5,B}
4  C u0 p0 c0 {2,S} {3,B} {6,B}
5  C u0 p0 c0 {3,B} {7,B} {15,S}
6  C u0 p0 c0 {4,B} {8,B} {18,S}
7  C u0 p0 c0 {5,B} {8,B} {16,S}
8  C u0 p0 c0 {6,B} {7,B} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77762,0.0265909,7.15206e-05,-1.10005e-07,4.53577e-11,-950.561,10.4478], Tmin=(10,'K'), Tmax=(822.928,'K')),
            NASAPolynomial(coeffs=[0.920412,0.0628513,-3.53529e-05,9.61134e-09,-1.01692e-12,-1237.85,19.0727], Tmin=(822.928,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-7.8835,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (424.038,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 10, 'C=C': 3, 'C-C': 5}
1D rotors:
pivots: [1, 2], dihedral: [9, 1, 2, 3], rotor symmetry: 3, max scan energy: 4.96 kJ/mol
pivots: [7, 8], dihedral: [2, 7, 8, 16], rotor symmetry: 3, max scan energy: 4.96 kJ/mol


External symmetry: 2, optical isomers: 1

Geometry:
C      -1.62671800   -1.36607500    0.07537500
C      -0.28490400   -0.67581000    0.02889700
C       0.08070600    0.21629500    1.03979900
C       1.31143400    0.86859400    1.02505000
C       2.20055000    0.63042600   -0.01699600
C       1.84763800   -0.25701400   -1.03105100
C       0.61659700   -0.91729600   -1.02766600
C       0.26555000   -1.87295800   -2.14237000
H      -2.23262600   -1.13156800   -0.80630600
H      -2.19239000   -1.06329600    0.95826400
H      -1.51992300   -2.45567700    0.10441600
H      -0.61348000    0.40223500    1.85337300
H       1.57062900    1.55641400    1.82222400
H       3.16258300    1.12997700   -0.04355200
H       2.54180800   -0.44297300   -1.84463400
H      -0.63855800   -1.55856300   -2.67455900
H       1.07517000   -1.93858700   -2.87131500
H       0.07410900   -2.88267200   -1.76380900
""",
)

entry(
    index = 4,
    label = "4_octyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
3  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {8,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {8,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
8  C u1 p0 c0 {4,S} {5,S} {25,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.77987,0.128462,-0.000456199,1.06431e-06,-8.59618e-10,-6013.29,15.3507], Tmin=(10,'K'), Tmax=(427.655,'K')),
            NASAPolynomial(coeffs=[-1.15113,0.0889163,-4.98254e-05,1.35557e-08,-1.43845e-12,-4979.23,39.1353], Tmin=(427.655,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-50.0272,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (586.17,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 17, 'C-C': 7}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.74 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: 
pivots: [3, 4], dihedral: [2, 3, 4, 6], rotor symmetry: 1, max scan energy: 13.09 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 3 4 6 5 F
D 3 4 6 7 F
pivots: [4, 6], dihedral: [3, 4, 6, 7], rotor symmetry: 1, max scan energy: 8.66 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [4, 6, 7, 8], invalidation reason: Another conformer for 4_octyl exists which is 1.28 kJ/mol lower.
pivots: [7, 8], dihedral: [6, 7, 8, 9], rotor symmetry: 1, max scan energy: 23.57 kJ/mol
pivots: [8, 9], dihedral: [7, 8, 9, 23], rotor symmetry: 3, max scan energy: 11.88 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       3.57872700    1.63328400    0.10177700
C       2.31611800    0.84186900    0.45545600
C       2.52864800   -0.68162900    0.46756100
C       2.83584000   -1.27268300   -0.86887400
H       2.38685500   -0.81188100   -1.74661200
C       3.42546000   -2.63616000   -1.01476000
C       3.95569400   -2.94399100   -2.42252300
C       4.54336900   -4.35215400   -2.56256900
C       5.06791300   -4.65109000   -3.96980700
H       3.95734800    1.35502100   -0.88547500
H       3.38511700    2.70952900    0.09689900
H       4.37665000    1.44192000    0.82657700
H       1.95132500    1.15785100    1.43880300
H       1.51845300    1.08331300   -0.25744300
H       3.32967200   -0.93441800    1.17729100
H       1.62125000   -1.15617200    0.88464900
H       2.67466200   -3.40362300   -0.74722400
H       4.23274600   -2.76866600   -0.27984400
H       3.14158600   -2.81775000   -3.14759100
H       4.71843600   -2.20201800   -2.68796600
H       5.35562200   -4.47792600   -1.83629100
H       3.77863700   -5.09090200   -2.29319400
H       5.85847500   -3.94965600   -4.25428700
H       5.48097700   -5.66131700   -4.03657400
H       4.27037400   -4.56863300   -4.71489100
""",
)

entry(
    index = 5,
    label = "1_pentyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {6,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {4,S} {8,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {9,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
9  C u1 p0 c0 {7,S} {27,S} {28,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.62077,0.144077,-0.000488634,1.12414e-06,-9.01803e-10,-7904.84,16.2349], Tmin=(10,'K'), Tmax=(429.991,'K')),
            NASAPolynomial(coeffs=[-1.56712,0.101734,-5.73038e-05,1.56755e-08,-1.67227e-12,-6793.09,41.6443], Tmin=(429.991,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-65.7575,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (665.158,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 19, 'C-C': 8}
1D rotors:
pivots: [1, 4], dihedral: [2, 1, 4, 5], rotor symmetry: 1, max scan energy: 0.64 kJ/mol (set as a FreeRotor)
pivots: [4, 5], dihedral: [1, 4, 5, 6], rotor symmetry: 1, max scan energy: 21.37 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 3 1 4 5 F
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: 
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 23.48 kJ/mol
* Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 9], invalidation reason: 
* Invalidated! pivots: [8, 9], dihedral: [7, 8, 9, 10], invalidation reason: 
pivots: [9, 10], dihedral: [8, 9, 10, 11], rotor symmetry: 1, max scan energy: 23.48 kJ/mol
* Invalidated! pivots: [10, 11], dihedral: [9, 10, 11, 26], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
C      -5.25580900    0.04642400    0.62758400
H      -6.16590300   -0.09789900    0.05626200
H      -5.33174100    0.57200800    1.57167600
C      -3.98918400   -0.62250200    0.21965800
C      -3.86302900   -0.85011400   -1.29496100
C      -2.57068800   -1.56696100   -1.69941000
C      -2.44387800   -1.79636200   -3.20970700
C      -1.15065400   -2.51232200   -3.61590200
C      -1.02340900   -2.74214700   -5.12597300
C       0.26956600   -3.45797000   -5.53325000
C       0.38794700   -3.68308500   -7.04334600
H      -3.90115800   -1.60102900    0.72639300
H      -3.12883800   -0.04284800    0.57963900
H      -3.92214100    0.11731200   -1.80755200
H      -4.72633000   -1.43265800   -1.64071600
H      -1.70881400   -0.98439500   -1.34897000
H      -2.51486700   -2.53285300   -1.18068700
H      -3.30532400   -2.37931400   -3.56032100
H      -2.50054600   -0.83046000   -3.72792700
H      -1.09391900   -3.47814900   -3.09729900
H      -0.28928400   -1.92916300   -3.26527300
H      -1.88437100   -3.32559200   -5.47757200
H      -1.07976600   -1.77664400   -5.64548600
H       1.12990400   -2.87502300   -5.18259000
H       0.32581200   -4.42289500   -5.01485100
H       0.37026900   -2.73343200   -7.58731400
H      -0.43997300   -4.29298000   -7.41836300
H       1.31955900   -4.19489400   -7.29996800
""",
)

entry(
    index = 6,
    label = "5_pentyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {12,S} {13,S}
2  C u0 p0 c0 {4,S} {6,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {8,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {9,S} {18,S} {19,S}
6  C u0 p0 c0 {2,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {3,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {4,S} {25,S} {26,S} {27,S}
9  C u1 p0 c0 {5,S} {6,S} {28,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5687,0.155338,-0.000625506,1.54722e-06,-1.29914e-09,-9206.4,15.4496], Tmin=(10,'K'), Tmax=(414.663,'K')),
            NASAPolynomial(coeffs=[-3.3437,0.105607,-5.94026e-05,1.61606e-08,-1.71104e-12,-7798.19,49.8367], Tmin=(414.663,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-76.5914,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (673.472,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 19, 'C-C': 8}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [11, 1, 2, 3], invalidation reason: 
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: 
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: 
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 7], invalidation reason: 
pivots: [5, 7], dihedral: [4, 5, 7, 8], rotor symmetry: 1, max scan energy: 9.22 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 6 4 5 7 F
D 18 4 5 7 F
* Invalidated! pivots: [7, 8], dihedral: [5, 7, 8, 9], invalidation reason: 
pivots: [8, 9], dihedral: [7, 8, 9, 10], rotor symmetry: 1, max scan energy: 23.58 kJ/mol
* Invalidated! pivots: [9, 10], dihedral: [8, 9, 10, 26], invalidation reason: 


External symmetry: 1, optical isomers: 1

Geometry:
C       5.00055600    0.31581900    0.85914300
C       3.84365400   -0.29635300    0.06438100
C       4.01834700   -0.17025900   -1.45264100
C       2.86407200   -0.78371700   -2.25794000
C       3.02990800   -0.68080400   -3.73775700
H       4.03857400   -0.63081900   -4.14140900
C       1.90416400   -0.95723900   -4.67809300
C       2.16646800   -0.50502400   -6.12165900
C       1.01001000   -0.80859100   -7.07989800
C       1.28148300   -0.35647800   -8.51750700
H       5.10833300    1.38311000    0.64185900
H       4.84574400    0.21059700    1.93645900
H       5.95035500   -0.16845100    0.61137700
H       2.90323800    0.18430700    0.36044200
H       3.73909500   -1.35572400    0.32885000
H       4.11976700    0.88807000   -1.72183200
H       4.95837600   -0.65224200   -1.75005800
H       2.75379200   -1.84413100   -1.96243600
H       1.91593000   -0.31245800   -1.95948900
H       0.98592700   -0.48057500   -4.30424400
H       1.67396300   -2.03933200   -4.68493600
H       2.37235300    0.57219000   -6.12747100
H       3.07860700   -0.99204800   -6.48939300
H       0.80510800   -1.88610100   -7.06841400
H       0.09857800   -0.32269200   -6.71076100
H       2.16697800   -0.85237200   -8.92740000
H       0.43855900   -0.58609100   -9.17508300
H       1.45614400    0.72290300   -8.56616100
""",
)

entry(
    index = 7,
    label = "C8H9O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {7,S} {10,D}
6  C u0 p0 c0 {3,S} {8,D} {14,S}
7  C u0 p0 c0 {5,S} {9,D} {15,S}
8  C u0 p0 c0 {6,D} {9,S} {17,S}
9  C u0 p0 c0 {7,D} {8,S} {16,S}
10 C u0 p0 c0 {5,D} {18,S} {19,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67486,0.025828,0.000204898,-4.73079e-07,3.24098e-10,20054.7,14.4207], Tmin=(10,'K'), Tmax=(475.419,'K')),
            NASAPolynomial(coeffs=[1.14344,0.076821,-4.96804e-05,1.52872e-08,-1.79601e-12,19959.8,21.2218], Tmin=(475.419,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (166.704,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (453.139,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 3, 'C-H': 9, 'C-C': 5, 'C-O': 1, 'O-O': 1}
1D rotors:
pivots: [7, 8], dihedral: [2, 7, 8, 17], rotor symmetry: 3, max scan energy: 14.90 kJ/mol
* Invalidated! pivots: [7, 9], dihedral: [2, 7, 9, 10], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.49133100    1.70387200    0.25310500
C      -0.35826100    0.99184700    0.13533100
C       0.93975500    1.64066800    0.01774200
C       2.09261700    0.94616600    0.07180900
C       2.08256600   -0.49527400    0.27732600
C       0.93637600   -1.18471500    0.33781600
C      -0.39894700   -0.53185600    0.12787100
C      -1.09027300   -1.08634700   -1.11952200
O      -1.27974400   -0.88149700    1.32043100
O      -1.49785000   -2.16749000    1.43623100
H      -1.46662100    2.78774800    0.25163200
H      -2.45720600    1.23269300    0.38083600
H       0.94660200    2.72081200   -0.08270400
H       3.04553200    1.45775600    0.00221800
H       3.03048300   -1.00981300    0.39275300
H       0.91357900   -2.25473300    0.50601800
H      -0.49496500   -0.84436700   -2.00210000
H      -2.07910600   -0.63572900   -1.23355700
H      -1.19026700   -2.16959100   -1.04063500
""",
)

entry(
    index = 8,
    label = "C7H7O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {8,S} {16,S}
2  O u0 p2 c0 {9,D}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {5,S} {9,D}
5  C u0 p0 c0 {4,S} {6,D} {13,S}
6  C u0 p0 c0 {5,D} {7,S} {14,S}
7  C u0 p0 c0 {6,S} {8,D} {15,S}
8  C u1 p0 c0 {1,S} {7,D}
9  C u0 p0 c0 {2,D} {4,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56259,0.0340622,0.000267578,-9.02535e-07,8.41088e-10,11901.8,14.3224], Tmin=(10,'K'), Tmax=(387.669,'K')),
            NASAPolynomial(coeffs=[7.39735,0.0534716,-3.57199e-05,1.14669e-08,-1.40242e-12,11161.3,-6.26015], Tmin=(387.669,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (98.984,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (369.994,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C=C': 3, 'C-O': 1, 'C-C': 3, 'C-H': 6, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 9.76 kJ/mol
pivots: [2, 5], dihedral: [1, 2, 5, 6], rotor symmetry: 1, max scan energy: 26.75 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 8], invalidation reason: 
pivots: [8, 9], dihedral: [7, 8, 9, 16], rotor symmetry: 1, max scan energy: 19.01 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 15 7 8 9 F


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.12591300    1.09738700    0.24310500
C      -1.78341700   -0.32206900   -0.16993300
C      -0.70668800   -0.88342800    0.35509000
O       0.24313500   -1.36556900    0.82415400
C      -2.59822700   -1.07088000   -1.11635300
C      -3.71545200   -0.60427200   -1.71243700
C      -4.49673800   -1.36967200   -2.66020600
C      -5.61927000   -0.93693300   -3.23310800
O      -6.29018200   -1.45751300   -4.26291200
H      -2.13830100    1.75567700   -0.63087200
H      -1.40447300    1.49767400    0.95675500
H      -3.11577700    1.13059300    0.70829300
H      -2.26734800   -2.07938500   -1.35060200
H      -4.06922300    0.39873400   -1.49575700
H      -4.17012100   -2.38473900   -2.90039200
H      -7.23885400   -1.37704500   -4.10477800
""",
)

entry(
    index = 9,
    label = "2_dodecyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {8,S} {25,S} {26,S}
7  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
8  C u0 p0 c0 {6,S} {10,S} {27,S} {28,S}
9  C u0 p0 c0 {7,S} {12,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {12,S} {34,S} {35,S} {36,S}
12 C u1 p0 c0 {9,S} {11,S} {37,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.14967,0.293782,-0.0011846,2.52529e-06,-1.89447e-09,-18575.1,17.7023], Tmin=(10,'K'), Tmax=(436.974,'K')),
            NASAPolynomial(coeffs=[3.41607,0.120295,-6.47519e-05,1.6891e-08,-1.72072e-12,-17314.9,25.3305], Tmin=(436.974,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-154.499,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (860.548,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 25, 'C-C': 11}
1D rotors:
pivots: [1, 2], dihedral: [14, 1, 2, 4], rotor symmetry: 3, max scan energy: 2.56 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 2 4 3 F
D 1 2 4 18 F
pivots: [2, 4], dihedral: [1, 2, 4, 5], rotor symmetry: 1, max scan energy: 8.99 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 3 1 2 4 F
D 15 1 2 4 F
pivots: [4, 5], dihedral: [2, 4, 5, 6], rotor symmetry: 1, max scan energy: 21.60 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 15 1 2 4 F
D 1 2 4 18 F
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 23.62 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 23.50 kJ/mol
pivots: [7, 8], dihedral: [6, 7, 8, 9], rotor symmetry: 1, max scan energy: 23.54 kJ/mol
pivots: [8, 9], dihedral: [7, 8, 9, 10], rotor symmetry: 1, max scan energy: 23.55 kJ/mol
pivots: [9, 10], dihedral: [8, 9, 10, 11], rotor symmetry: 1, max scan energy: 23.54 kJ/mol
pivots: [10, 11], dihedral: [9, 10, 11, 12], rotor symmetry: 1, max scan energy: 23.51 kJ/mol
pivots: [11, 12], dihedral: [10, 11, 12, 13], rotor symmetry: 1, max scan energy: 23.49 kJ/mol
pivots: [12, 13], dihedral: [11, 12, 13, 35], rotor symmetry: 3, max scan energy: 11.86 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -6.69475700    0.37354300   -0.94482300
C      -5.89754700   -0.42975100    0.02510000
H      -6.16910900   -0.40015500    1.07636100
C      -4.57723200   -1.01684000   -0.34885700
C      -4.04083900   -2.04744800    0.65464000
C      -2.67861500   -2.63086300    0.26530200
C      -2.14194300   -3.65814300    1.26849100
C      -0.77976400   -4.24373600    0.87929500
C      -0.24280600   -5.27095900    1.88248300
C       1.11932200   -5.85668700    1.49323200
C       1.65652100   -6.88392000    2.49601000
C       3.01871600   -7.47007600    2.10753200
C       3.54721000   -8.49519700    3.11496800
H      -6.24879500    1.36664100   -1.12608500
H      -6.75086800   -0.11621500   -1.92497100
H      -7.71537500    0.54437700   -0.59302000
H      -3.82573400   -0.21318600   -0.46508500
H      -4.64804200   -1.47597500   -1.34632500
H      -4.77100600   -2.85912600    0.75737600
H      -3.96537600   -1.57747300    1.64335200
H      -1.95196000   -1.81482000    0.15957300
H      -2.75492000   -3.09878500   -0.72478900
H      -2.06481600   -3.19030500    2.25849500
H      -2.86908000   -4.47350800    1.37463400
H      -0.85706300   -4.71159600   -0.11070100
H      -0.05275000   -3.42819800    0.77288100
H      -0.16548600   -4.80312700    2.87248400
H      -0.96984800   -6.08644000    1.98891900
H       1.84638300   -5.04116000    1.38684500
H       1.04199800   -6.32447500    0.50317800
H       1.73448500   -6.41693200    3.48654300
H       0.93021900   -7.70024500    2.60278500
H       3.74471200   -6.65480500    2.00145200
H       2.94101600   -7.93718900    1.11821400
H       2.85935200   -9.34051800    3.21674200
H       4.51865400   -8.89319900    2.80898600
H       3.66905100   -8.04844900    4.10675800
""",
)

entry(
    index = 10,
    label = "3_dodecyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {7,S} {23,S} {24,S}
6  C u0 p0 c0 {1,S} {8,S} {13,S} {14,S}
7  C u0 p0 c0 {5,S} {10,S} {25,S} {26,S}
8  C u0 p0 c0 {6,S} {12,S} {29,S} {30,S}
9  C u0 p0 c0 {11,S} {12,S} {27,S} {28,S}
10 C u0 p0 c0 {7,S} {34,S} {35,S} {36,S}
11 C u0 p0 c0 {9,S} {31,S} {32,S} {33,S}
12 C u1 p0 c0 {8,S} {9,S} {37,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {11,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {10,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.63097,0.246469,-0.000932813,2.05307e-06,-1.58971e-09,-18413.1,17.4612], Tmin=(10,'K'), Tmax=(430.487,'K')),
            NASAPolynomial(coeffs=[0.303115,0.129061,-7.16265e-05,1.92915e-08,-2.02764e-12,-17096.6,36.7116], Tmin=(430.487,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-153.149,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (873.02,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 25, 'C-C': 11}
1D rotors:
pivots: [1, 2], dihedral: [14, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.80 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 5], rotor symmetry: 1, max scan energy: 9.00 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 2 3 5 4 F
D 2 3 5 19 F
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 6], invalidation reason: 
pivots: [5, 6], dihedral: [3, 5, 6, 7], rotor symmetry: 1, max scan energy: 21.62 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 17 2 3 5 F
D 4 3 5 20 F
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 23.64 kJ/mol
pivots: [7, 8], dihedral: [6, 7, 8, 9], rotor symmetry: 1, max scan energy: 23.49 kJ/mol
pivots: [8, 9], dihedral: [7, 8, 9, 10], rotor symmetry: 1, max scan energy: 23.55 kJ/mol
* Invalidated! pivots: [9, 10], dihedral: [8, 9, 10, 11], invalidation reason: 
* Invalidated! pivots: [10, 11], dihedral: [9, 10, 11, 12], invalidation reason: 
pivots: [11, 12], dihedral: [10, 11, 12, 13], rotor symmetry: 1, max scan energy: 23.49 kJ/mol
pivots: [12, 13], dihedral: [11, 12, 13, 35], rotor symmetry: 3, max scan energy: 11.86 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       6.93348400    0.63209900    1.28532600
C       5.92202200    0.37369900    0.16202400
C       4.51582900    0.72160600    0.52267900
H       4.35234700    1.49254000    1.27242600
C       3.35771900    0.29321700   -0.31578500
C       1.99314100    0.45483100    0.36976700
C       0.81208500    0.02588900   -0.50701200
C      -0.55017300    0.18924800    0.17657400
C      -1.73279700   -0.24092800   -0.69879400
C      -3.09509100   -0.07769600   -0.01507400
C      -4.27793200   -0.50770900   -0.88990000
C      -5.64062800   -0.34497400   -0.20678200
C      -6.81609600   -0.77677900   -1.08821000
H       6.69328800    0.03898800    2.17198000
H       7.94934800    0.37667800    0.97260600
H       6.93057700    1.68594600    1.57953800
H       6.23275600    0.94240900   -0.73355400
H       5.97172900   -0.67982200   -0.14746700
H       3.34485100    0.86417000   -1.26329400
H       3.49311500   -0.75390400   -0.62412900
H       1.98958400   -0.12690100    1.29928700
H       1.86388700    1.50363900    0.66537400
H       0.94372000   -1.02272900   -0.80387000
H       0.82182900    0.60781900   -1.43781700
H      -0.68235800    1.23788300    0.47291600
H      -0.55920400   -0.39202200    1.10762500
H      -1.72368500    0.34039500   -1.62988800
H      -1.60047800   -1.28953900   -0.99517700
H      -3.22736000    0.97092300    0.28141600
H      -3.10411700   -0.65906200    0.91601000
H      -4.14669100   -1.55648800   -1.18679300
H      -4.27005800    0.07356600   -1.82122800
H      -5.77223700    0.70280800    0.08955300
H      -5.64906800   -0.92621200    0.72330700
H      -6.73122800   -1.83043700   -1.37224900
H      -6.85538900   -0.18907600   -2.01078200
H      -7.77167600   -0.64838200   -0.57235200
""",
)

entry(
    index = 11,
    label = "S_31007",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {4,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {8,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {20,S} {21,S} {22,S}
7  C u0 p0 c0 {9,S} {23,S} {24,S} {25,S}
8  C u0 p0 c0 {5,S} {9,D} {27,S}
9  C u0 p0 c0 {7,S} {8,D} {26,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.50571,0.144446,-0.000426794,8.38151e-07,-5.9233e-10,-18457.6,14.2631], Tmin=(10,'K'), Tmax=(474.068,'K')),
            NASAPolynomial(coeffs=[0.799912,0.0922879,-5.11879e-05,1.38258e-08,-1.46048e-12,-17548,29.1067], Tmin=(474.068,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-153.497,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (631.9,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 18, 'C-C': 7, 'C=C': 1}
1D rotors:
pivots: [1, 2], dihedral: [3, 1, 2, 4], rotor symmetry: 1, max scan energy: 23.41 kJ/mol
pivots: [1, 3], dihedral: [2, 1, 3, 5], rotor symmetry: 1, max scan energy: 23.57 kJ/mol
pivots: [2, 4], dihedral: [1, 2, 4, 6], rotor symmetry: 1, max scan energy: 23.47 kJ/mol
pivots: [3, 5], dihedral: [1, 3, 5, 8], rotor symmetry: 1, max scan energy: 21.43 kJ/mol
pivots: [4, 6], dihedral: [2, 4, 6, 20], rotor symmetry: 3, max scan energy: 11.86 kJ/mol
* Invalidated! pivots: [5, 8], dihedral: [3, 5, 8, 9], invalidation reason: 
pivots: [7, 9], dihedral: [23, 7, 9, 8], rotor symmetry: 3, max scan energy: 8.03 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       0.97301500   -0.59998500    0.57517300
C       2.24608200    0.19320700    0.25990200
C      -0.31523100    0.20921100    0.38925000
C       3.53607600   -0.61447600    0.44366700
C      -1.59076000   -0.59330400    0.70417400
C       4.80245100    0.18587100    0.12613800
C      -5.09247900    0.77786900   -0.43317400
C      -2.84954100    0.21615700    0.56483800
C      -3.83991600   -0.03669600   -0.28892900
H      -0.28121500    1.09903500    1.03061400
H      -0.37340700    0.57856500   -0.64141100
H       0.93537800   -1.49177800   -0.06379900
H       1.02270800   -0.96891000    1.60791400
H       2.28506000    1.08494900    0.89905500
H       2.19616600    0.56281800   -0.77254700
H       3.49749000   -1.50521100   -0.19512500
H       3.58646300   -0.98334700    1.47534800
H      -1.64331500   -1.47060500    0.04959200
H      -1.51616400   -0.97576500    1.73159000
H       4.79771200    0.53886700   -0.90991200
H       5.70325400   -0.41787400    0.26665300
H       4.88757100    1.06459100    0.77317700
H      -5.98452400    0.17279000   -0.23484300
H      -5.19822900    1.16614700   -1.45256400
H      -5.10000100    1.62688200    0.25475900
H      -3.75460200   -0.90405600   -0.94357000
H      -2.93235700    1.08474400    1.21957700
""",
)

entry(
    index = 12,
    label = "S_1294",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {5,S} {16,S} {17,S}
4  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {7,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {9,S} {25,S} {26,S} {27,S}
9  C u0 p1 c0 {6,S} {8,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.32754,0.162439,-0.000490856,9.39918e-07,-6.58193e-10,16069,14.4273], Tmin=(10,'K'), Tmax=(464.652,'K')),
            NASAPolynomial(coeffs=[3.38185,0.0897536,-5.08666e-05,1.40158e-08,-1.50687e-12,16657.7,17.538], Tmin=(464.652,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (133.566,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (623.585,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 18, 'C-C': 8}
1D rotors:
pivots: [1, 2], dihedral: [4, 1, 2, 3], rotor symmetry: 1, max scan energy: 23.13 kJ/mol
pivots: [1, 4], dihedral: [2, 1, 4, 6], rotor symmetry: 1, max scan energy: 22.74 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 5], rotor symmetry: 1, max scan energy: 23.35 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 7], rotor symmetry: 1, max scan energy: 23.46 kJ/mol
pivots: [4, 6], dihedral: [1, 4, 6, 9], rotor symmetry: 1, max scan energy: 15.89 kJ/mol
pivots: [5, 7], dihedral: [3, 5, 7, 22], rotor symmetry: 3, max scan energy: 11.87 kJ/mol
pivots: [6, 9], dihedral: [4, 6, 9, 8], rotor symmetry: 1, max scan energy: 37.11 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 9 8 26 F
A 9 8 27 F
D 11 4 6 21 F
D 27 8 9 6 F
pivots: [8, 9], dihedral: [25, 8, 9, 6], rotor symmetry: 3, max scan energy: 7.76 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       0.48580800   -0.13207900    0.21379400
C      -0.92925600   -0.71859800    0.18832500
C      -2.02861600    0.33868100    0.03645600
C       1.58614000   -1.18858500    0.35952200
C      -3.44519600   -0.24634900    0.00491700
C       2.98546100   -0.56303300    0.36508200
C      -4.53669500    0.81694000   -0.14713800
C       4.54910400    0.96691600   -0.74109600
C       3.48647800   -0.04061500   -0.91167300
H       1.52644400   -1.89570700   -0.47376800
H       1.43167100   -1.75819800    1.28363300
H       0.66604900    0.43029000   -0.71131100
H       0.56416800    0.59144700    1.03667600
H      -1.00460300   -1.43989200   -0.63526500
H      -1.10194300   -1.29010700    1.10970400
H      -1.85448400    0.91157500   -0.88354400
H      -1.95486700    1.05977900    0.86112700
H      -3.51920700   -0.96586300   -0.81947700
H      -3.61918800   -0.81927000    0.92391400
H       3.14558000    0.08834100    1.24644300
H       3.74734500   -1.36962100    0.47429800
H      -4.40992100    1.38369100   -1.07489000
H      -5.53337600    0.36753800   -0.16669100
H      -4.51103000    1.53151800    0.68163600
H       5.04209100    1.04158900    0.24397200
H       3.96292200    1.89622900   -0.88022800
H       5.28055600    0.97566300   -1.55321600
""",
)

entry(
    index = 13,
    label = "S_1176",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
6  C u0 p1 c0 {3,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2773,0.0672546,-0.000109571,1.85839e-07,-1.29227e-10,25266.7,11.4684], Tmin=(10,'K'), Tmax=(488.956,'K')),
            NASAPolynomial(coeffs=[1.85894,0.0609796,-3.54755e-05,1.00344e-08,-1.10474e-12,25619.1,19.4818], Tmin=(488.956,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (210.051,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (411.566,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 12, 'C-C': 5}
1D rotors:
pivots: [1, 2], dihedral: [3, 1, 2, 4], rotor symmetry: 1, max scan energy: 23.12 kJ/mol
pivots: [1, 3], dihedral: [2, 1, 3, 6], rotor symmetry: 1, max scan energy: 15.70 kJ/mol
pivots: [2, 4], dihedral: [1, 2, 4, 13], rotor symmetry: 3, max scan energy: 11.82 kJ/mol
pivots: [3, 6], dihedral: [1, 3, 6, 5], rotor symmetry: 1, max scan energy: 36.51 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 6 5 17 F
A 6 5 16 F
D 2 1 3 12 F
D 18 5 6 3 F
pivots: [5, 6], dihedral: [16, 5, 6, 3], rotor symmetry: 3, max scan energy: 7.77 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.15268900    0.29021400    0.48209000
C      -1.78158400    0.64495800   -0.86965500
C      -0.86946200   -1.21070300    0.60865900
C      -2.08924700    2.13640900   -1.02128000
C      -1.75029900   -3.48724200    0.38244600
C      -2.02827100   -2.09505300    0.77983800
H      -0.22267700    0.85578600    0.61558500
H      -1.83204900    0.58435900    1.28842800
H      -1.11061600    0.32498100   -1.67724300
H      -2.70409700    0.06324100   -0.98439900
H      -0.41199600   -1.41478000    1.60463700
H      -0.10791400   -1.55236000   -0.11941800
H      -1.18017600    2.73996200   -0.93343800
H      -2.53914500    2.35429700   -1.99375200
H      -2.78670600    2.47483700   -0.24904300
H      -2.31497800   -4.22815500    0.95413700
H      -2.20977200   -3.49957000   -0.62517800
H      -0.69651200   -3.79292000    0.25971500
""",
)

entry(
    index = 14,
    label = "S_3459",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {5,S} {6,D}
5  C u0 p0 c0 {4,S} {7,D} {15,S}
6  C u0 p0 c0 {4,D} {16,S} {17,S}
7  C u0 p0 c0 {5,D} {18,S} {19,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84593,0.0147137,0.000343365,-1.17542e-06,1.3652e-09,1325.86,12.4535], Tmin=(10,'K'), Tmax=(217.477,'K')),
            NASAPolynomial(coeffs=[0.788549,0.0709475,-4.44968e-05,1.35573e-08,-1.59355e-12,1458.84,22.539], Tmin=(217.477,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (11.0722,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (440.667,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 12, 'C-C': 4, 'C=C': 2}
1D rotors:
pivots: [1, 2], dihedral: [3, 1, 2, 9], rotor symmetry: 3, max scan energy: 15.56 kJ/mol
pivots: [1, 3], dihedral: [2, 1, 3, 12], rotor symmetry: 3, max scan energy: 12.14 kJ/mol
pivots: [1, 4], dihedral: [2, 1, 4, 5], rotor symmetry: 1, max scan energy: 33.56 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 4 5 15 F
pivots: [4, 5], dihedral: [1, 4, 5, 7], rotor symmetry: 1, max scan energy: 25.37 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 2 1 4 5 F


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.62823200    0.30608100   -0.16433200
C      -0.93526800    1.80211300   -0.31098300
C      -1.53543400   -0.32557400    0.91273300
C       0.83708100   -0.00306600    0.11861500
C       1.36072600   -1.33593700   -0.22033800
C       1.67177200    0.88353300    0.68244600
C       0.71769700   -2.33194100   -0.83817200
H      -0.87454900   -0.16548900   -1.12284300
H      -0.29558900    2.27144900   -1.06243000
H      -0.79990200    2.33793100    0.63300900
H      -1.97602800    1.94184000   -0.61584300
H      -1.35073300   -1.39572000    1.02242400
H      -1.35621600    0.14648500    1.88318800
H      -2.59017400   -0.18606300    0.65773100
H       2.39739000   -1.49899800    0.06732700
H       1.36645200    1.88745200    0.94719000
H       2.70237100    0.62021100    0.89501800
H       1.21825600   -3.27044500   -1.04514500
H      -0.31390600   -2.25582900   -1.16111600
""",
)

entry(
    index = 15,
    label = "S_15853",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {7,S} {8,S}
2  O u0 p2 c0 {4,D}
3  C u0 p0 c0 {4,S} {6,D} {11,S}
4  C u0 p0 c0 {2,D} {3,S} {5,S}
5  C u0 p0 c0 {4,S} {8,D} {10,S}
6  C u0 p0 c0 {3,D} {7,S} {9,S}
7  C u1 p0 c0 {1,S} {6,S} {12,S}
8  C u0 p0 c0 {1,S} {5,D} {13,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89084,0.00648003,0.000160305,-3.06982e-07,1.79976e-10,-3972.7,12.2265], Tmin=(10,'K'), Tmax=(548.441,'K')),
            NASAPolynomial(coeffs=[0.576965,0.0545245,-3.63967e-05,1.1496e-08,-1.38009e-12,-3968.27,22.95], Tmin=(548.441,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-33.0738,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 5, 'C-C': 3, 'C=O': 1, 'C=C': 2, 'C-O': 2}

External symmetry: 1, optical isomers: 1

Geometry:
O      -0.50870600   -1.74081100   -0.07772600
O       1.91353500    1.96727800    0.12821300
C      -0.35424900    1.42941600    0.04053400
C       1.06161500    1.08704100    0.07098500
C       1.50519900   -0.32887400    0.03364800
C      -1.43842500    0.55406200   -0.02356400
C      -1.50718400   -0.81572500   -0.07472900
C       0.82431300   -1.48037700   -0.02815500
H      -2.42226200    1.01442800   -0.03676700
H       2.58393600   -0.43089600    0.06256300
H      -0.54983200    2.49429100    0.07278700
H      -2.45984400   -1.32381900   -0.12168200
H       1.35190300   -2.42601400   -0.04610700
""",
)

entry(
    index = 16,
    label = "S_20960",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {4,S} {7,S}
4  C u1 p0 c0 {3,S} {6,S} {9,S}
5  C u0 p0 c0 {2,S} {6,D} {10,S}
6  C u0 p0 c0 {4,S} {5,D} {11,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.21613,-0.0188782,0.000222077,-3.72401e-07,2.00645e-10,19868.2,10.2919], Tmin=(10,'K'), Tmax=(597.604,'K')),
            NASAPolynomial(coeffs=[-0.0520593,0.0456031,-2.99143e-05,9.27049e-09,-1.08996e-12,19737.1,23.3206], Tmin=(597.604,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (165.182,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 5, 'C-C': 4, 'C=C': 1, 'C-O': 2}

External symmetry: 1, optical isomers: 1

Geometry:
O       1.11328700   -0.43631600   -1.25795300
C       1.15565100    0.18306300    0.05664700
C       0.42091100   -1.08219100   -0.15472400
C      -1.02213600   -0.73502400   -0.06755000
C       0.11777700    1.22796700    0.26039800
C      -1.13900400    0.63636300    0.14996800
H       0.80466900   -2.06006500    0.11393400
H       2.14355900    0.24560200    0.49915500
H      -1.83624100   -1.43307100   -0.20346200
H       0.31906400    2.27848700    0.41659600
H      -2.07753600    1.17518400    0.18699200
""",
)

entry(
    index = 17,
    label = "S_22779",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {6,D}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {1,S} {6,S} {7,S} {9,S}
5  C u0 p0 c0 {6,S} {8,S} {10,S} {11,S}
6  C u0 p0 c0 {2,D} {4,S} {5,S}
7  C u0 p0 c0 {4,S} {8,D} {13,S}
8  C u0 p0 c0 {5,S} {7,D} {12,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78921,0.0288802,3.47002e-05,-6.87712e-08,3.01846e-11,-2997.6,14.0622], Tmin=(10,'K'), Tmax=(845.986,'K')),
            NASAPolynomial(coeffs=[5.53473,0.0414109,-2.43692e-05,6.81776e-09,-7.34728e-13,-4036.68,1.53728], Tmin=(845.986,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-24.893,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 5, 'C-C': 4, 'O-O': 1, 'C=O': 1, 'C=C': 1, 'C-O': 1}
1D rotors:
pivots: [1, 4], dihedral: [3, 1, 4, 6], rotor symmetry: 1, max scan energy: 14.43 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.84054200    0.27826000   -1.09961000
O      -0.30730100   -1.79998500   -1.10780700
O       2.71736700   -0.64970500   -1.42773800
C       1.02990400   -0.11223200    0.05676600
C      -1.46315800    0.01960100    0.05602400
C      -0.27200700   -0.80662200   -0.44078600
C       0.52708700    1.10200200    0.76745700
C      -0.80664900    1.16849100    0.77091100
H       1.64777900   -0.79293400    0.64590700
H      -2.09190100   -0.59652000    0.70894800
H      -2.09399700    0.32638300   -0.78533000
H      -1.37580000    1.95906900    1.24497500
H       1.19319500    1.82305500    1.22274600
""",
)

entry(
    index = 18,
    label = "S_29505",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {4,D}
2  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {6,D} {8,S}
4  C u0 p0 c0 {1,D} {2,S} {3,S}
5  C u0 p0 c0 {2,S} {7,D} {11,S}
6  C u0 p0 c0 {3,D} {7,S} {12,S}
7  C u0 p0 c0 {5,D} {6,S} {13,S}
8  C u1 p0 c0 {3,S} {14,S} {15,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87961,0.00719059,0.000184306,-3.52831e-07,2.08094e-10,6717.31,13.1923], Tmin=(10,'K'), Tmax=(541.628,'K')),
            NASAPolynomial(coeffs=[-0.0802741,0.0624291,-4.06625e-05,1.26807e-08,-1.51467e-12,6764.98,26.3485], Tmin=(541.628,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (55.8047,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (353.365,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 7, 'C-C': 5, 'C=O': 1, 'C=C': 2}
1D rotors:
pivots: [3, 8], dihedral: [4, 3, 8, 14], rotor symmetry: 2, max scan energy: 91.17 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 3 8 14 15 F
D 10 2 4 3 F
D 9 2 5 7 F
D 6 3 4 2 F


External symmetry: 1, optical isomers: 1

Geometry:
O       0.70920500   -2.25352100   -0.53999200
C      -1.29689900   -0.99307900   -0.33273300
C       1.06497200    0.02370800    0.06883000
C       0.22026800   -1.17235100   -0.28967600
C      -1.82624500    0.36780000   -0.01258700
C       0.40881300    1.25359400    0.34769100
C      -0.99453100    1.40187500    0.30333700
C       2.42084600   -0.14137100    0.10605300
H      -1.72170000   -1.74608400    0.34481500
H      -1.62298800   -1.31332200   -1.33155800
H      -2.90064300    0.51335300   -0.03827700
H       1.02107000    2.11165600    0.60525500
H      -1.41679100    2.37533600    0.52977500
H       3.08171600    0.67982900    0.35696200
H       2.85291000   -1.10742200   -0.11789500
""",
)

entry(
    index = 19,
    label = "S_47623",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {15,S}
2  O u0 p2 c0 {9,S} {16,S}
3  C u0 p0 c0 {4,S} {5,D} {10,S}
4  C u0 p0 c0 {1,S} {3,S} {9,D}
5  C u0 p0 c0 {3,D} {6,S} {11,S}
6  C u0 p0 c0 {5,S} {8,D} {12,S}
7  C u0 p0 c0 {8,D} {13,S} {14,S}
8  C u0 p0 c0 {6,D} {7,D}
9  C u1 p0 c0 {2,S} {4,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59528,0.0456927,5.12152e-05,-1.27357e-07,6.52214e-11,23040.9,13.8584], Tmin=(10,'K'), Tmax=(747.24,'K')),
            NASAPolynomial(coeffs=[8.13573,0.0551831,-3.56763e-05,1.06908e-08,-1.21413e-12,21418.9,-13.037], Tmin=(747.24,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (191.564,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (365.837,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 5, 'C-C': 2, 'H-O': 2, 'C=C': 4, 'C-O': 2}
1D rotors:
pivots: [1, 4], dihedral: [15, 1, 4, 3], rotor symmetry: 1, max scan energy: 22.19 kJ/mol
pivots: [2, 9], dihedral: [16, 2, 9, 4], rotor symmetry: 1, max scan energy: 61.41 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 2 9 4 F
D 1 4 9 2 F
pivots: [3, 4], dihedral: [5, 3, 4, 1], rotor symmetry: 1, max scan energy: 49.78 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 4 9 2 F
D 16 2 9 4 F
pivots: [5, 6], dihedral: [3, 5, 6, 8], rotor symmetry: 1, max scan energy: 37.65 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.86268100    1.23275400    1.40854800
O       3.54626000   -0.73120700   -0.96947100
C       0.88545100   -0.20886900   -0.20923500
C       2.03934400    0.39676800    0.35382600
C      -0.39345700    0.02876000    0.20280900
C      -1.54407800   -0.62792800   -0.36684100
C      -4.01312500   -0.21331600    0.40390800
C      -2.78847600   -0.41904800    0.02176500
C       3.34762300    0.33182500   -0.17103200
H       1.07816200   -0.90576100   -1.01797400
H      -0.56585900    0.74071500    1.00256700
H      -1.37051600   -1.34312500   -1.16969400
H      -4.62841900    0.55957400   -0.05009400
H      -4.46959200   -0.80533100    1.19335000
H       2.73658700    1.61272800    1.58873600
H       4.39483400   -0.60896100   -1.40785000
""",
)

entry(
    index = 20,
    label = "S_68639",
    molecule =
"""
1  O u0 p2 c0 {5,S} {12,S}
2  O u0 p2 c0 {6,S} {11,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {5,S} {8,S} {9,S} {10,S}
5  C u0 p0 c0 {1,S} {4,S} {6,D}
6  C u0 p0 c0 {2,S} {5,D} {7,S}
7  C u0 p0 c0 {3,D} {6,S} {8,S}
8  C u0 p1 c0 {4,S} {7,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8267,0.0114195,0.000184977,-4.32871e-07,3.02493e-10,-8276.92,12.1055], Tmin=(10,'K'), Tmax=(479.675,'K')),
            NASAPolynomial(coeffs=[3.09842,0.0495043,-3.4223e-05,1.09076e-08,-1.30971e-12,-8575.33,11.2452], Tmin=(479.675,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-68.8535,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 2, 'C-C': 4, 'C=O': 1, 'H-O': 2, 'C=C': 1, 'C-O': 2}
1D rotors:
pivots: [1, 5], dihedral: [12, 1, 5, 4], rotor symmetry: 1, max scan energy: 38.18 kJ/mol
pivots: [2, 6], dihedral: [11, 2, 6, 5], rotor symmetry: 1, max scan energy: 45.38 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.61477700   -1.91434900    0.60216300
O       1.99026000    0.54403800   -0.24195900
O      -0.16906300    2.50695600   -0.95326400
C      -1.44517600   -0.61686900    0.18722500
C       0.03991100   -0.82138000    0.09417000
C       0.66534600    0.34598800   -0.26095400
C      -0.34353000    1.43605800   -0.39619400
C      -1.19877000    0.82945500    0.58229900
H      -1.87180000   -1.23645000    0.97572900
H      -1.98402100   -0.76451100   -0.75157500
H       2.14978500    1.42916000   -0.60747700
H       1.55228200   -1.73809400    0.76984400
""",
)

entry(
    index = 21,
    label = "S_32820",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {12,S}
2  O u0 p2 c0 {7,S} {13,S}
3  O u0 p2 c0 {5,D}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {9,S}
5  C u0 p0 c0 {3,D} {4,S} {7,S}
6  C u1 p0 c0 {4,S} {8,S} {10,S}
7  C u0 p0 c0 {2,S} {5,S} {8,D}
8  C u0 p0 c0 {6,S} {7,D} {11,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77394,0.0165733,0.000166685,-4.01129e-07,2.85501e-10,-40184.4,12.8078], Tmin=(10,'K'), Tmax=(466.282,'K')),
            NASAPolynomial(coeffs=[2.62088,0.0530761,-3.63488e-05,1.15538e-08,-1.38453e-12,-40366.1,14.3889], Tmin=(466.282,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-334.141,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 2, 'C-H': 3, 'H-O': 2, 'C=O': 1, 'C-C': 4, 'C=C': 1}
1D rotors:
pivots: [1, 4], dihedral: [12, 1, 4, 5], rotor symmetry: 1, max scan energy: 17.22 kJ/mol
pivots: [2, 7], dihedral: [13, 2, 7, 5], rotor symmetry: 1, max scan energy: 43.78 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.19064600   -0.37960400    0.21863500
O       2.34574200    0.83398400    0.14380800
O       0.60088300   -1.48250600    0.35563700
C      -1.13550600   -0.03419800   -0.65909300
C       0.25196700   -0.39889600   -0.10686200
C      -1.02043800    1.45228500   -0.88173200
C       1.05687500    0.79012900   -0.20617500
C       0.26384200    1.87355900   -0.66236500
H      -1.25352600   -0.53852600   -1.63419500
H      -1.84730700    2.06822200   -1.20439000
H       0.63357500    2.88154000   -0.79684800
H      -2.00685600   -1.27593500    0.52678300
H       2.57324800   -0.05438300    0.46573400
""",
)

entry(
    index = 22,
    label = "S_1244",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84434,0.0120439,0.00010282,-1.81867e-07,1.01063e-10,-3103.52,9.45246], Tmin=(10,'K'), Tmax=(466.439,'K')),
            NASAPolynomial(coeffs=[-0.982493,0.0534366,-3.02915e-05,8.38365e-09,-9.06264e-13,-2653.23,29.0581], Tmin=(466.439,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-25.8353,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (349.208,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 10, 'C-C': 5}
1D rotors:
pivots: [1, 4], dihedral: [2, 1, 4, 10], rotor symmetry: 3, max scan energy: 10.28 kJ/mol
pivots: [2, 5], dihedral: [1, 2, 5, 13], rotor symmetry: 3, max scan energy: 10.28 kJ/mol


External symmetry: 2, optical isomers: 2

Geometry:
C      -0.62183400   -0.17906300    0.34124600
C       0.62286100    0.13226000   -0.45183200
C      -0.03609800    1.21437800    0.37313800
C      -1.94236700   -0.44337200   -0.34797600
C       1.96787600   -0.43116000   -0.04911100
H      -0.45789600   -0.76935500    1.23955300
H       0.47392500    0.21534000   -1.52570000
H      -0.57330800    2.00149900   -0.14496500
H       0.46819100    1.54029700    1.27649500
H      -2.02895500   -1.49021700   -0.65669500
H      -2.78761400   -0.21778000    0.31026500
H      -2.04787600    0.17589300   -1.24388700
H       2.11522800   -1.43867600   -0.45146500
H       2.05690100   -0.49311100    1.03970200
H       2.78786900    0.19706700   -0.41182100
""",
)

entry(
    index = 23,
    label = "S_59420",
    molecule =
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {4,S}
3  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {6,S} {7,D}
5  C u0 p0 c0 {3,S} {6,D} {10,S}
6  C u0 p0 c0 {4,S} {5,D} {11,S}
7  C u0 p0 c0 {4,D} {12,S} {13,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91643,0.00483717,0.000146955,-2.63323e-07,1.46046e-10,4660.43,10.968], Tmin=(10,'K'), Tmax=(562.462,'K')),
            NASAPolynomial(coeffs=[-0.779966,0.0561312,-3.75624e-05,1.19441e-08,-1.44475e-12,4905.67,28.4066], Tmin=(562.462,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (38.7129,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 2, 'C-H': 6, 'C-C': 2, 'C=C': 2, 'O-O': 1}

External symmetry: 1, optical isomers: 2

Geometry:
O      -0.83926400   -1.40261400    0.68250200
O       0.45708200   -1.38850600   -0.01851900
C      -1.73872600   -0.60751600   -0.07761400
C       1.02172300   -0.13349400    0.09767200
C      -1.19599300    0.78014400   -0.26391000
C       0.11490700    0.99049600   -0.11720200
C       2.34677200   -0.05806100    0.25878900
H      -2.64503600   -0.60048300    0.53661500
H      -1.97420900   -1.09095000   -1.03643200
H      -1.88558100    1.58530900   -0.49140100
H       0.54947700    1.98159100   -0.17079900
H       2.93636400   -0.95164600    0.41215000
H       2.85248600    0.89573000    0.18814900
""",
)

entry(
    index = 24,
    label = "S_3584",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {7,S} {8,S} {16,S} {17,S}
5  C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {2,S} {5,S} {7,D}
7  C u0 p0 c0 {4,S} {6,D} {21,S}
8  O u0 p2 c0 {4,S} {22,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {7,S}
22 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.96533,0.10778,-0.00032453,7.48207e-07,-6.19363e-10,-6694.54,15.5424], Tmin=(10,'K'), Tmax=(414.454,'K')),
            NASAPolynomial(coeffs=[0.561301,0.0811965,-4.81373e-05,1.3785e-08,-1.52957e-12,-6067.68,30.1814], Tmin=(414.454,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-55.6902,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (519.654,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 13, 'C-C': 5, 'C-O': 1, 'O-O': 1, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 6], dihedral: [2, 1, 6, 9], invalidation reason: 
* Invalidated! pivots: [3, 4], dihedral: [5, 3, 4, 8], invalidation reason: 
pivots: [3, 5], dihedral: [4, 3, 5, 14], rotor symmetry: 3, max scan energy: 11.90 kJ/mol
pivots: [4, 8], dihedral: [3, 4, 8, 7], rotor symmetry: 1, max scan energy: 18.70 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 18 6 9 8 F
* Invalidated! pivots: [6, 9], dihedral: [1, 6, 9, 8], invalidation reason: 
pivots: [7, 8], dihedral: [19, 7, 8, 4], rotor symmetry: 3, max scan energy: 7.58 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.87465200    1.85592100   -1.02250000
O       2.26190600    3.09978900   -0.84470200
C      -1.45183700    0.30952400   -0.52812100
C      -0.53390100   -0.25875900    0.57588600
C      -2.69528200    0.99833400    0.03931100
C       2.21016400    1.01122600    0.15362000
C       0.45343600   -2.42407800   -0.35158500
C       0.67429600   -0.98194700    0.02465100
C       1.87088200   -0.40480400   -0.16045000
H      -1.75694700   -0.49809800   -1.20230300
H      -0.87475000    1.01542200   -1.13243800
H      -1.11268900   -0.95328400    1.19650000
H      -0.23087100    0.56277600    1.23142800
H      -3.32295000    1.39888800   -0.76090200
H      -3.30499300    0.30243600    0.62413300
H      -2.42221800    1.83163600    0.69398500
H       1.64727000    1.42765400    0.98941400
H       3.27615800    1.15748900    0.32950700
H      -0.37881500   -2.52299300   -1.05652200
H       0.18650900   -3.01419900    0.53258300
H       1.34036800   -2.86789800   -0.80660600
H       2.66611600   -0.99324800   -0.60888100
""",
)

entry(
    index = 25,
    label = "S_4449",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {13,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {14,S}
3  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {2,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {7,S} {9,D}
6  C u0 p0 c0 {2,S} {8,S} {10,D}
7  C u0 p0 c0 {5,S} {11,D} {21,S}
8  C u0 p0 c0 {6,S} {12,D} {22,S}
9  C u0 p0 c0 {5,D} {23,S} {24,S}
10 C u0 p0 c0 {6,D} {27,S} {28,S}
11 C u0 p0 c0 {7,D} {25,S} {26,S}
12 C u0 p0 c0 {8,D} {29,S} {30,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {11,S}
27 H u0 p0 c0 {10,S}
28 H u0 p0 c0 {10,S}
29 H u0 p0 c0 {12,S}
30 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.9433,0.101582,-2.969e-05,-2.6152e-08,1.52985e-11,14767.2,17.5136], Tmin=(10,'K'), Tmax=(977.244,'K')),
            NASAPolynomial(coeffs=[11.9024,0.0896137,-4.92358e-05,1.30483e-08,-1.34694e-12,11836.6,-31.5377], Tmin=(977.244,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (122.736,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (702.573,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 18, 'C-C': 7, 'C=C': 4}
1D rotors:
pivots: [1, 2], dihedral: [3, 1, 2, 4], rotor symmetry: 1, max scan energy: 48.48 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 13 1 5 9 F
pivots: [1, 3], dihedral: [2, 1, 3, 15], rotor symmetry: 3, max scan energy: 13.61 kJ/mol
pivots: [1, 5], dihedral: [2, 1, 5, 7], rotor symmetry: 1, max scan energy: 101.21 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 3 2 1 5 F
D 1 5 7 9 F
D 13 2 1 5 F
D 1 5 7 9 F
D 5 7 21 11 F
D 14 2 4 19 F
D 2 1 3 15 F
D 1 5 7 21 F
D 13 1 2 14 F
pivots: [2, 4], dihedral: [1, 2, 4, 18], rotor symmetry: 3, max scan energy: 11.21 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 3 1 5 7 F
pivots: [2, 6], dihedral: [1, 2, 6, 8], rotor symmetry: 1, max scan energy: 46.91 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 13 1 3 17 F
D 2 6 8 12 F
D 13 1 2 14 F
D 2 1 5 9 F
pivots: [5, 7], dihedral: [1, 5, 7, 11], rotor symmetry: 1, max scan energy: 26.22 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 13 1 5 9 F
pivots: [6, 8], dihedral: [2, 6, 8, 12], rotor symmetry: 1, max scan energy: 15.81 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       0.30607800   -0.45187600   -0.46004300
C       0.41166500    0.67711100    0.61091500
C       0.75982900   -1.81678400    0.08959300
C      -0.04631800    2.04230900    0.06076600
C       1.07329400   -0.10727600   -1.73616900
C      -0.34569100    0.32812700    1.88839800
C       0.36631100    0.02004000   -3.01806600
C      -1.79761600    0.07254900    1.77254700
C       2.40496200    0.06296400   -1.72319900
C       0.27535800    0.29743200    3.07357400
C      -0.94086400   -0.12701600   -3.25859600
C      -2.48151500   -0.84206100    2.46335600
H      -0.75313400   -0.54485800   -0.71332200
H       1.46784100    0.77129500    0.88613400
H       1.79795900   -1.78003900    0.43136000
H       0.69151100   -2.58294400   -0.68653800
H       0.13918800   -2.12670900    0.93246000
H      -1.08189300    2.01484200   -0.28918200
H       0.02803200    2.81041200    0.83427100
H       0.57593600    2.34531100   -0.78315400
H       1.01198800    0.25868000   -3.86121800
H      -2.33589800    0.67395200    1.04329300
H       2.95068700    0.29598400   -2.63101900
H       2.99216400   -0.02603000   -0.81668300
H      -1.33309000   -0.00915700   -4.26184300
H      -1.66183900   -0.36889600   -2.48719800
H      -0.26721200    0.12534300    3.99612000
H       1.34416900    0.46408400    3.15421100
H      -1.99382500   -1.50517100    3.17007900
H      -3.55173100   -0.95972600    2.33693800
""",
)

entry(
    index = 26,
    label = "S_34913",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,D}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,S} {5,S} {10,D}
5  C u0 p0 c0 {3,D} {4,S} {11,S}
6  O u0 p2 c0 {1,S} {12,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73218,0.0220873,0.000100455,-2.43232e-07,1.62677e-10,-39850.3,12.437], Tmin=(10,'K'), Tmax=(512.886,'K')),
            NASAPolynomial(coeffs=[3.67419,0.0445206,-2.94403e-05,9.17198e-09,-1.08495e-12,-40133.5,9.85965], Tmin=(512.886,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-331.375,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 1, 'C-H': 3, 'C=C': 1, 'C=O': 2, 'C-C': 4, 'H-O': 1}
1D rotors:
pivots: [1, 4], dihedral: [12, 1, 4, 5], rotor symmetry: 1, max scan energy: 20.15 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.82585700   -1.08080300    0.17383300
O       1.42741000    1.71077900   -0.56683100
O      -1.50676000    2.04097100   -1.09325700
C       0.70981100   -0.31681300    0.57634000
C       0.53910800    0.97740700   -0.23129200
C      -0.59019200   -1.02910500    0.30220200
C      -0.96362900    1.07663000   -0.61711200
C      -1.51548200   -0.25260400   -0.28563800
H       0.77206900   -0.05619500    1.64658600
H      -0.72635700   -2.06559500    0.58769400
H      -2.52863300   -0.54079000   -0.53345700
H       2.55680800   -0.46386500    0.04092600
""",
)

entry(
    index = 27,
    label = "S_3475",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {7,D} {19,S}
7  C u0 p0 c0 {6,D} {20,S} {21,S}
8  O u0 p2 c0 {4,S} {22,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.04485,0.102878,-0.000339373,8.70501e-07,-7.70483e-10,-5237.42,15.4826], Tmin=(10,'K'), Tmax=(400.869,'K')),
            NASAPolynomial(coeffs=[-1.39554,0.0865813,-5.16223e-05,1.48226e-08,-1.64629e-12,-4394.47,38.9195], Tmin=(400.869,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-43.5799,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (532.126,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 13, 'C-C': 5, 'C-O': 1, 'O-O': 1, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 6], dihedral: [2, 1, 6, 3], invalidation reason: 
* Invalidated! pivots: [3, 4], dihedral: [6, 3, 4, 5], invalidation reason: 
* Invalidated! pivots: [3, 6], dihedral: [4, 3, 6, 1], invalidation reason: 
* Invalidated! pivots: [3, 8], dihedral: [4, 3, 8, 9], invalidation reason: 
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 7], invalidation reason: 
* Invalidated! pivots: [5, 7], dihedral: [4, 5, 7, 17], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.81036600    1.37153700    0.90592900
O      -3.56727900    2.44263100    0.78955600
C      -0.72682100    0.25562500    0.37645900
C       0.72484300    0.50186100   -0.09744100
C       1.67159500   -0.67814300    0.14720400
C      -1.51528000    1.55874800    0.25937500
C       3.10120600   -0.39765100   -0.32387600
C      -1.39538500   -0.85136000   -0.39926800
C      -1.89564300   -1.96547000    0.12353300
H      -0.70334100   -0.02028400    1.43749500
H       1.11814100    1.38738200    0.41661300
H       0.71629900    0.74721900   -1.16753800
H       1.67787300   -0.91454900    1.21798200
H       1.28428800   -1.56834200   -0.35769600
H      -1.70717300    1.84089400   -0.77894100
H      -1.01822500    2.38475300    0.77329400
H       3.52810000    0.46878500    0.19091800
H       3.13106300   -0.19134300   -1.39831100
H       3.75566400   -1.25206900   -0.13284600
H      -1.45859600   -0.69267300   -1.47614800
H      -2.36532300   -2.72198100   -0.49473300
H      -1.86132000   -2.15792300    1.19126000
""",
)

entry(
    index = 28,
    label = "S_1272",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {4,S} {13,S} {15,S}
4  C u0 p0 c0 {3,S} {11,S} {32,S} {33,S}
5  C u0 p0 c0 {6,S} {11,S} {18,S} {19,S}
6  C u0 p0 c0 {5,S} {7,S} {20,S} {21,S}
7  C u0 p0 c0 {6,S} {8,S} {22,S} {23,S}
8  C u0 p0 c0 {7,S} {9,S} {24,S} {25,S}
9  C u0 p0 c0 {8,S} {10,S} {26,S} {27,S}
10 C u0 p0 c0 {9,S} {12,S} {28,S} {29,S}
11 C u0 p0 c0 {4,S} {5,S} {16,S} {17,S}
12 C u0 p0 c0 {10,S} {14,S} {30,S} {31,S}
13 C u0 p0 c0 {3,S} {37,S} {38,S} {39,S}
14 C u0 p0 c0 {12,S} {34,S} {35,S} {36,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {11,S}
17 H u0 p0 c0 {11,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {10,S}
29 H u0 p0 c0 {10,S}
30 H u0 p0 c0 {12,S}
31 H u0 p0 c0 {12,S}
32 H u0 p0 c0 {4,S}
33 H u0 p0 c0 {4,S}
34 H u0 p0 c0 {14,S}
35 H u0 p0 c0 {14,S}
36 H u0 p0 c0 {14,S}
37 H u0 p0 c0 {13,S}
38 H u0 p0 c0 {13,S}
39 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.16866,0.287272,-0.00103658,2.13317e-06,-1.57535e-09,-38193.5,19.2315], Tmin=(10,'K'), Tmax=(439.323,'K')),
            NASAPolynomial(coeffs=[4.54147,0.130843,-7.32319e-05,1.99106e-08,-2.11283e-12,-37276.6,19.5417], Tmin=(439.323,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-317.62,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (914.592,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 25, 'C-C': 11, 'C-O': 1, 'O-O': 1}
1D rotors:
pivots: [1, 3], dihedral: [2, 1, 3, 4], rotor symmetry: 1, max scan energy: 12.48 kJ/mol
pivots: [3, 4], dihedral: [1, 3, 4, 11], rotor symmetry: 1, max scan energy: 19.33 kJ/mol
pivots: [3, 13], dihedral: [1, 3, 13, 37], rotor symmetry: 3, max scan energy: 13.04 kJ/mol
pivots: [4, 11], dihedral: [3, 4, 11, 5], rotor symmetry: 1, max scan energy: 22.32 kJ/mol
pivots: [5, 6], dihedral: [11, 5, 6, 7], rotor symmetry: 1, max scan energy: 23.30 kJ/mol
pivots: [5, 11], dihedral: [6, 5, 11, 4], rotor symmetry: 1, max scan energy: 23.56 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 23.52 kJ/mol
pivots: [7, 8], dihedral: [6, 7, 8, 9], rotor symmetry: 1, max scan energy: 23.52 kJ/mol
* Invalidated! pivots: [8, 9], dihedral: [7, 8, 9, 10], invalidation reason: 
* Invalidated! pivots: [9, 10], dihedral: [8, 9, 10, 12], invalidation reason: 
pivots: [10, 12], dihedral: [9, 10, 12, 14], rotor symmetry: 1, max scan energy: 23.49 kJ/mol
pivots: [12, 14], dihedral: [10, 12, 14, 34], rotor symmetry: 3, max scan energy: 11.86 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -5.58672900    0.29158700    1.87778000
O      -6.46679100   -0.40907700    2.56047900
C      -5.58675900   -0.05972200    0.44080400
C      -4.29169700    0.51255500   -0.12005600
C      -1.73447400    0.46493100   -0.12793300
C      -0.46091600   -0.19161200    0.41661800
C       0.83022000    0.42262900   -0.13593100
C       2.10403700   -0.23371000    0.40856900
C       3.39570300    0.38092900   -0.14254600
C       4.66961400   -0.27488800    0.40187400
C      -3.02282700   -0.14632500    0.43333100
C       5.96196000    0.33936100   -0.14820100
C      -6.85309700    0.49036200   -0.19486400
C       7.22911500   -0.32207800    0.40123400
H      -5.58312000   -1.15271700    0.41372000
H      -3.02170800   -0.06315800    1.52502000
H      -3.04556600   -1.21965800    0.20565700
H      -1.71431500    1.53795400    0.10164300
H      -1.74140700    0.38850400   -1.22316800
H      -0.47944600   -1.26430500    0.18476200
H      -0.45758900   -0.11805600    1.51152600
H       0.84847900    1.49519700    0.09661900
H       0.82585800    0.34991000   -1.23125300
H       2.08600600   -1.30627000    0.17581700
H       2.10783400   -0.16146500    1.50378400
H       3.41360000    1.45350000    0.09031800
H       3.39186400    0.30877000   -1.23791300
H       4.65293800   -1.34764100    0.16905800
H       4.67433600   -0.20311000    1.49733700
H       5.95779600    0.26733700   -1.24264400
H       5.97917000    1.41096100    0.08489700
H      -4.27528200    1.59025600    0.08152500
H      -4.32388100    0.40235400   -1.21004700
H       7.25812600   -1.38785400    0.15358000
H       8.13156400    0.13855800   -0.00995200
H       7.27949200   -0.23567100    1.49119400
H      -6.86474000    1.58265200   -0.15411800
H      -7.72989800    0.10760600    0.32945400
H      -6.91233700    0.18106500   -1.24148600
""",
)

entry(
    index = 29,
    label = "S_4248",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {2,S} {3,D} {13,S}
5  C u0 p0 c0 {3,S} {6,D} {14,S}
6  C u0 p0 c0 {5,D} {15,S} {16,S}
7  O u0 p2 c0 {1,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43267,0.0583678,-2.98381e-05,2.17491e-09,1.93253e-12,10995.1,14.8698], Tmin=(10,'K'), Tmax=(1150.94,'K')),
            NASAPolynomial(coeffs=[11.6464,0.0406809,-2.094e-05,5.21875e-09,-5.0936e-13,8385.18,-29.0361], Tmin=(1150.94,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (91.4015,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (390.78,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 9, 'C-O': 1, 'C=C': 2, 'O-O': 1, 'C-C': 3}
1D rotors:
pivots: [1, 3], dihedral: [2, 1, 3, 5], rotor symmetry: 1, max scan energy: 13.06 kJ/mol
pivots: [3, 5], dihedral: [1, 3, 5, 6], rotor symmetry: 1, max scan energy: 32.64 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 12 4 6 5 F
D 6 5 7 15 F
D 2 1 3 9 F
pivots: [4, 6], dihedral: [11, 4, 6, 5], rotor symmetry: 3, max scan energy: 2.86 kJ/mol
pivots: [5, 7], dihedral: [3, 5, 7, 8], rotor symmetry: 1, max scan energy: 24.70 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.14380900   -2.54636300   -2.71791800
O      -2.11768500   -3.70129500   -2.08855100
C      -2.05025000   -1.41553800   -1.77635100
C      -1.15587000   -2.29365400    1.05483400
C      -0.66042100   -1.23927800   -1.23420500
C      -0.32113100   -1.61922100    0.01293900
C       0.35062200   -0.63465700   -2.10972800
C       0.20813100   -0.32392200   -3.40181500
H      -2.35664200   -0.56277300   -2.38326900
H      -2.79051400   -1.59518000   -1.00068200
H      -0.67750800   -3.23054300    1.36030600
H      -1.22724600   -1.67269500    1.95552100
H      -2.16102200   -2.54007500    0.71694800
H       0.70805700   -1.42694300    0.31285900
H       1.31074300   -0.44545300   -1.63478200
H       1.02581900    0.11507500   -3.96035400
H      -0.70522600   -0.51300400   -3.95389000
""",
)

entry(
    index = 30,
    label = "S_6914",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {3,D} {7,S} {8,S}
5 C u0 p0 c0 {3,S} {6,T}
6 C u0 p0 c0 {5,T} {9,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81942,0.0123953,0.000136974,-3.71899e-07,2.87284e-10,40305.9,11.1119], Tmin=(10,'K'), Tmax=(459.495,'K')),
            NASAPolynomial(coeffs=[5.64692,0.0284108,-1.95231e-05,6.36102e-09,-7.83822e-13,39800.9,0.0491449], Tmin=(459.495,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (335.099,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 1, 'C-H': 3, 'C#C': 1, 'C=C': 1, 'O-O': 1, 'C-C': 1}
1D rotors:
pivots: [1, 3], dihedral: [2, 1, 3, 4], rotor symmetry: 1, max scan energy: 17.76 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.97290900    1.32552300   -0.07672800
O      -2.28020000    1.22654700   -0.18256700
C      -0.28014900    0.08561200   -0.02378400
C      -0.90376100   -1.09132900   -0.07701400
C       1.11642800    0.30778600    0.08956100
C       2.29635800    0.51806000    0.18537800
H      -0.32886100   -2.00440400   -0.03279600
H      -1.97987700   -1.13196900   -0.16403400
H       3.34083100    0.69593400    0.27017500
""",
)

entry(
    index = 31,
    label = "S_3457",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
6  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
7  C u1 p0 c0 {2,S} {19,S} {20,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43451,0.0496666,4.18576e-05,-1.44002e-07,1.09414e-10,13967.3,13.7026], Tmin=(10,'K'), Tmax=(350.68,'K')),
            NASAPolynomial(coeffs=[1.76132,0.0687518,-3.97775e-05,1.11923e-08,-1.22493e-12,14084.7,20.0214], Tmin=(350.68,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (116.083,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (465.61,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 13, 'C-C': 7}
1D rotors:
pivots: [1, 4], dihedral: [2, 1, 4, 5], rotor symmetry: 1, max scan energy: 15.95 kJ/mol
pivots: [2, 7], dihedral: [1, 2, 7, 19], rotor symmetry: 2, max scan energy: 14.42 kJ/mol
pivots: [4, 5], dihedral: [1, 4, 5, 6], rotor symmetry: 1, max scan energy: 22.35 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 16], rotor symmetry: 3, max scan energy: 11.78 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       0.64706600   -0.55832400   -0.17525500
C       1.42286900    0.68048000   -0.65647400
C       1.91589100   -0.74544500   -0.94089600
C      -0.69707700   -0.89328800   -0.78684900
C      -1.86791000   -0.13105200   -0.15237700
C      -3.22210900   -0.48276900   -0.77434000
C       2.12356800    1.54672600    0.27550200
H       0.71301000   -0.73204400    0.89580600
H       0.97430700    1.17938700   -1.51032600
H      -0.87440600   -1.97350900   -0.69432500
H      -0.66565000   -0.68401800   -1.86376100
H      -1.68649500    0.94556700   -0.24476200
H      -1.89288000   -0.34340400    0.92305200
H       2.80315200   -1.07146900   -0.41079200
H       1.85056900   -1.09229700   -1.96682700
H      -3.44231000   -1.54968700   -0.66786300
H      -3.23997500   -0.24776500   -1.84332600
H      -4.03557500    0.07254300   -0.29973800
H       2.62239300    1.13545200    1.14514100
H       2.15130000    2.61806600    0.13018400
""",
)

entry(
    index = 32,
    label = "S_4315",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {7,D}
5  C u0 p0 c0 {2,S} {8,D} {16,S}
6  C u0 p0 c0 {4,S} {9,D} {17,S}
7  C u0 p0 c0 {4,D} {18,S} {19,S}
8  C u0 p0 c0 {5,D} {22,S} {23,S}
9  C u0 p0 c0 {6,D} {20,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29097,0.0712358,-2.00666e-05,-1.3058e-08,7.01494e-12,10769.2,14.071], Tmin=(10,'K'), Tmax=(1119.95,'K')),
            NASAPolynomial(coeffs=[10.5754,0.0626582,-3.19358e-05,7.91128e-09,-7.69635e-13,8043.89,-26.7803], Tmin=(1119.95,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (89.5166,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (544.598,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 14, 'C-C': 5, 'C=C': 3}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [3, 1, 2, 5], invalidation reason: 
* Invalidated! pivots: [1, 3], dihedral: [2, 1, 3, 13], invalidation reason: 
pivots: [1, 4], dihedral: [2, 1, 4, 6], rotor symmetry: 1, max scan energy: 38.77 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 1 4 6 17 F
pivots: [2, 5], dihedral: [1, 2, 5, 8], rotor symmetry: 1, max scan energy: 18.50 kJ/mol
pivots: [4, 6], dihedral: [1, 4, 6, 9], rotor symmetry: 1, max scan energy: 26.25 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 10 1 4 7 F


External symmetry: 1, optical isomers: 2

Geometry:
C       0.04237200   -0.07840600    0.56719400
C       0.61866400    0.14500800   -0.86188300
C       0.89380100   -1.08139200    1.35499600
C      -1.43297900   -0.44821100    0.48063300
C       1.96883800    0.80366200   -0.87158500
C      -2.42295200    0.61786600    0.25856400
C      -1.87134100   -1.71281700    0.57722500
C       3.07413600    0.29568800   -1.40944300
C      -2.20428500    1.93526400    0.19498800
H       0.10326300    0.88057300    1.09574800
H      -0.08352700    0.76939900   -1.42523500
H       0.66703400   -0.81974600   -1.37807600
H       1.91580000   -0.71091400    1.45713700
H       0.48554900   -1.24595900    2.35501000
H       0.95129100   -2.04888800    0.84773300
H       2.01940000    1.78397000   -0.39740900
H      -3.44599600    0.26514700    0.14514300
H      -1.20807400   -2.54936000    0.75395300
H      -2.92692900   -1.94416700    0.48345100
H      -3.02407100    2.62590900    0.03673700
H      -1.21947400    2.37517000    0.29953000
H       3.07543600   -0.67675700   -1.89298000
H       4.01546700    0.83367900   -1.39281800
""",
)

entry(
    index = 33,
    label = "S_1215",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,D} {15,S}
4  C u0 p0 c0 {3,D} {5,S} {16,S}
5  C u0 p0 c0 {4,S} {6,D} {18,S}
6  C u0 p0 c0 {5,D} {7,S} {17,S}
7  C u0 p0 c0 {6,S} {8,D} {19,S}
8  C u1 p0 c0 {2,S} {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.28178,0.0757166,-0.000185379,4.70434e-07,-4.31094e-10,38134.5,12.0933], Tmin=(10,'K'), Tmax=(393.563,'K')),
            NASAPolynomial(coeffs=[0.23252,0.0727727,-4.48197e-05,1.32473e-08,-1.50787e-12,38637.4,27.2996], Tmin=(393.563,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (317.047,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (444.824,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 11, 'C=C': 3, 'C-C': 4}
1D rotors:
pivots: [1, 3], dihedral: [9, 1, 3, 4], rotor symmetry: 3, max scan energy: 7.40 kJ/mol
pivots: [2, 8], dihedral: [12, 2, 8, 7], rotor symmetry: 3, max scan energy: 2.98 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 2, max scan energy: 33.88 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 8], invalidation reason: 


External symmetry: 1, optical isomers: 1

Geometry:
C       2.88394600   -1.41507300    0.83189400
C       0.68538700    6.42654400    0.13267400
C       1.75374700   -0.44110500    0.95828500
C       1.83959600    0.87813200    0.72727500
C       0.73788300    1.80841800    0.85352100
C       0.82550500    3.13427100    0.62101900
C      -0.29261600    4.06148700    0.75183500
C      -0.24542200    5.36492600    0.53295400
H       3.07353500   -1.92864100    1.78184800
H       3.80848800   -0.92128600    0.52341300
H       2.65452900   -2.19629700    0.09761500
H       0.77104100    7.19434600    0.90903900
H       0.35011800    6.92546500   -0.78289800
H       1.69522600    6.03068700   -0.05564700
H       0.79258100   -0.85304700    1.26287000
H       2.79817900    1.29676800    0.42226800
H       1.78303700    3.55104200    0.31657000
H      -0.22160500    1.39303700    1.15823600
H      -1.24233300    3.61971900    1.05831300
""",
)

entry(
    index = 34,
    label = "C8H9_2233",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {6,S} {7,S} {9,S}
2  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {2,S} {8,S}
5  C u0 p0 c0 {2,S} {3,S} {6,D}
6  C u0 p0 c0 {1,S} {5,D} {15,S}
7  C u0 p0 c0 {1,S} {8,D} {16,S}
8  C u0 p0 c0 {4,S} {7,D} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90732,0.00568374,0.000201705,-3.79644e-07,2.26193e-10,47252.5,12.7931], Tmin=(10,'K'), Tmax=(505.052,'K')),
            NASAPolynomial(coeffs=[-2.35644,0.0722463,-4.63368e-05,1.42358e-08,-1.67709e-12,47669,36.5928], Tmin=(505.052,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (392.849,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 9, 'C=C': 2, 'C-C': 7}
1D rotors:
pivots: [3, 5], dihedral: [12, 3, 5, 2], rotor symmetry: 3, max scan energy: 7.97 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.30419200   -0.26760500    0.34332200
C       0.64031500    1.17261600    0.99363000
C       2.40380500   -0.01181600   -0.56207500
C      -0.76274600    0.76884600    1.34766400
C       1.00772800    0.08758600   -0.02807600
C      -0.03657700   -0.68782200   -0.35621900
C      -1.78157100   -0.99014900    1.61767500
C      -1.28242100   -0.01100200    2.43635200
H      -2.10451900    0.04244300   -0.33795200
H       1.31528900    1.17706200    1.85787000
H       0.71356200    2.16938900    0.53334700
H       3.12116500   -0.20503800    0.24390800
H       2.49607900   -0.81272100   -1.29876300
H       2.71059900    0.92743600   -1.03712200
H       0.01532700   -1.49395000   -1.08083200
H      -2.31031600   -1.92076500    1.78719000
H      -1.22916000    0.09918900    3.51368300
""",
)

entry(
    index = 35,
    label = "S_2885",
    molecule =
"""
1  O u0 p2 c0 {2,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
3  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
4  C u0 p1 c0 {2,S} {3,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95383,0.00414089,0.000163909,-5.27665e-07,5.827e-10,14701.8,8.79863], Tmin=(10,'K'), Tmax=(228.48,'K')),
            NASAPolynomial(coeffs=[2.36431,0.031969,-1.87889e-05,5.42653e-09,-6.12974e-13,14774.4,14.1205], Tmin=(228.48,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (122.253,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 1, 'C-H': 5, 'C-C': 2, 'H-O': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 4], invalidation reason: 
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 3], invalidation reason: Another conformer for S_2885 exists which is 9.09 kJ/mol lower.
pivots: [3, 4], dihedral: [7, 3, 4, 2], rotor symmetry: 3, max scan energy: 11.14 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 4 2 5 F
A 4 2 6 F
D 5 2 4 3 F
D 10 1 2 6 F


External symmetry: 1, optical isomers: 2

Geometry:
O       1.81535200    1.27547100    0.33681600
C       0.76785600    0.66862800   -0.37380300
C      -1.38516000   -0.48387000   -0.40573300
C      -0.47550900    0.43175600    0.31351100
H       1.18862800   -0.12782900   -1.00794100
H       0.28451900    1.38959500   -1.10103400
H      -1.30830900   -1.40150800    0.20422700
H      -1.13771300   -0.75565700   -1.44512500
H      -2.43478900   -0.18968900   -0.32285100
H       1.40994600    1.62293300    1.14224700
""",
)

entry(
    index = 36,
    label = "S_1976",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {8,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {5,S} {16,S}
5  C u0 p0 c0 {4,S} {6,D} {18,S}
6  C u0 p0 c0 {5,D} {7,S} {17,S}
7  C u0 p0 c0 {6,S} {8,D} {19,S}
8  C u1 p0 c0 {2,S} {7,D}
9  O u0 p2 c0 {3,S} {20,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.52558,0.048341,0.000362044,-1.82759e-06,2.61687e-09,15032.7,13.5027], Tmin=(10,'K'), Tmax=(246.532,'K')),
            NASAPolynomial(coeffs=[4.94989,0.0702446,-4.51033e-05,1.4021e-08,-1.67539e-12,14825.7,5.85134], Tmin=(246.532,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (125.042,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (461.453,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 10, 'C-C': 4, 'H-O': 1, 'C-O': 1, 'C=C': 3}
1D rotors:
pivots: [1, 4], dihedral: [20, 1, 4, 2], rotor symmetry: 1, max scan energy: 18.50 kJ/mol
pivots: [2, 4], dihedral: [10, 2, 4, 1], rotor symmetry: 3, max scan energy: 7.98 kJ/mol
pivots: [3, 9], dihedral: [13, 3, 9, 8], rotor symmetry: 2, max scan energy: 4.77 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 23.00 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 20 1 4 5 F
pivots: [7, 8], dihedral: [6, 7, 8, 9], rotor symmetry: 1, max scan energy: 33.65 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -2.68461200    2.29538800    1.75949500
C      -3.11910900    1.53714700    3.94608400
C       4.64092400    0.00393200   -0.15168700
C      -2.14736400    1.61230600    2.81350400
C      -0.90681300    1.07691000    2.83149800
C       0.06072100    1.12659400    1.76213900
C       1.29595600    0.58133400    1.80824600
C       2.25516300    0.64215500    0.72127800
C       3.47103300    0.12352100    0.72474700
H      -2.69831200    0.99356600    4.79148000
H      -4.03862400    1.03769400    3.62418300
H      -3.39802800    2.54383300    4.27375800
H       4.45887100    0.49850900   -1.11889900
H       5.52848400    0.46495400    0.29521100
H       4.88671400   -1.04394400   -0.35555500
H      -0.61296900    0.56069700    3.73863500
H       1.61214200    0.05901300    2.70751000
H      -0.21146900    1.64068900    0.83856300
H       1.92700200    1.17210900   -0.18387500
H      -2.04704800    2.33507800    1.03871200
""",
)

entry(
    index = 37,
    label = "S_2403",
    molecule =
"""
1  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {5,S} {6,D}
3  C u0 p0 c0 {2,S} {7,D} {8,S}
4  C u0 p0 c0 {1,S} {5,D} {11,S}
5  C u0 p0 c0 {2,S} {4,D} {12,S}
6  C u0 p0 c0 {2,D} {15,S} {16,S}
7  C u0 p0 c0 {3,D} {13,S} {14,S}
8  C u0 p1 c0 {1,S} {3,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87324,0.00771926,0.000199913,-3.91371e-07,2.37136e-10,63504.2,12.378], Tmin=(10,'K'), Tmax=(524.591,'K')),
            NASAPolynomial(coeffs=[-0.299533,0.0660422,-4.26431e-05,1.31921e-08,-1.56373e-12,63577.3,26.341], Tmin=(524.591,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (527.96,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (382.466,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 8, 'C=C': 3, 'C-C': 5}

External symmetry: 1, optical isomers: 2

Geometry:
C       0.81195300    0.89902200   -1.59183500
C      -0.55864300   -0.03014800    0.80789200
C      -0.20623300   -0.92114600   -0.32982500
C       0.63914800    1.75837300   -0.36263500
C      -0.01319700    1.32670700    0.72303600
C      -1.33146100   -0.44458800    1.82443700
C       0.07467100   -2.25115100   -0.19221500
C       0.18737000   -0.45629600   -1.61162800
H       1.88169000    0.70770800   -1.79367300
H       0.50232600    1.44045100   -2.49758900
H       1.03105500    2.77153700   -0.39511500
H      -0.16345200    1.98162200    1.57598500
H       0.25153400   -2.70138600    0.78057100
H       0.22301600   -2.85065800   -1.08074300
H      -1.55741100    0.20458100    2.66331300
H      -1.77236700   -1.43462900    1.83186100
""",
)

entry(
    index = 38,
    label = "S_4214",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {6,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {5,S} {6,D}
5  C u1 p0 c0 {2,S} {4,S} {15,S}
6  C u0 p0 c0 {3,S} {4,D} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90198,0.019719,5.83184e-05,-8.28386e-08,3.17666e-11,25433.3,10.5602], Tmin=(10,'K'), Tmax=(895.385,'K')),
            NASAPolynomial(coeffs=[1.97629,0.0495043,-2.7066e-05,7.15681e-09,-7.38155e-13,24929.1,14.8961], Tmin=(895.385,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (211.518,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (353.365,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 9, 'C=C': 1, 'C-C': 5}
1D rotors:
pivots: [3, 6], dihedral: [11, 3, 6, 4], rotor symmetry: 3, max scan energy: 3.72 kJ/mol
* Invalidated! pivots: [4, 6], dihedral: [1, 4, 6, 3], invalidation reason: 


External symmetry: 1, optical isomers: 1

Geometry:
C       0.02777100    2.24274200   -2.12447500
C       0.94648300    2.26638400   -3.39688900
C       0.20664600    0.93862700    0.87460900
C       1.11701400    1.39370100   -1.45712800
C       1.91715200    1.42839500   -2.60030700
C       1.23272700    0.82815800   -0.20693600
H      -0.14609200    3.22120500   -1.66941400
H      -0.93365600    1.74228200   -2.26553300
H       0.51591000    1.78773000   -4.28394300
H       1.30067000    3.26138900   -3.68994700
H      -0.15638700   -0.04910200    1.18654800
H       0.62087900    1.41048300    1.77487100
H      -0.65667000    1.52691300    0.55569000
H       2.13373800    0.25987200    0.01256400
H       2.88751900    1.00671500   -2.83615700
""",
)

entry(
    index = 39,
    label = "S_3988",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {5,D}
4  C u0 p0 c0 {3,S} {6,D} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  C u0 p0 c0 {4,D} {15,S} {16,S}
7  O u0 p2 c0 {2,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.52953,0.0556778,-2.17389e-05,-4.54297e-09,3.75236e-12,11226.8,13.7036], Tmin=(10,'K'), Tmax=(1169.67,'K')),
            NASAPolynomial(coeffs=[12.0461,0.0405949,-2.04038e-05,4.95967e-09,-4.72387e-13,8273.93,-32.8249], Tmin=(1169.67,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (93.354,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 9, 'C-O': 1, 'C=C': 2, 'O-O': 1, 'C-C': 3}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [2, 1, 4, 3], invalidation reason: 
* Invalidated! pivots: [3, 4], dihedral: [5, 3, 4, 1], invalidation reason: 
pivots: [3, 5], dihedral: [4, 3, 5, 6], rotor symmetry: 1, max scan energy: 31.99 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 3 5 6 13 F
pivots: [5, 6], dihedral: [3, 5, 6, 8], rotor symmetry: 1, max scan energy: 26.68 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
D 10 3 5 7 F


External symmetry: 1, optical isomers: 2

Geometry:
O       2.71860600    0.84409700    0.15904400
O       2.48121500    1.14975700    1.41852500
C       0.46780500    1.43602500   -0.67019600
C       1.51883000    0.33887400   -0.50592200
C       0.87249600    2.53381900   -1.63052400
C       0.76284800    2.30555300   -3.07627100
C       1.34667400    3.70163900   -1.17356100
C       0.26004900    1.22607700   -3.68463900
H       0.27396400    1.85332600    0.31986300
H      -0.46124800    0.96006500   -1.00040100
H       1.14266500   -0.48566100    0.10247800
H       1.89472400   -0.03366400   -1.45886400
H       1.13233400    3.12009100   -3.69516400
H       1.44139800    3.90218300   -0.11305300
H       1.65815700    4.48776000   -1.85284600
H       0.21969000    1.16406100   -4.76538900
H      -0.13447700    0.37497000   -3.14106200
""",
)

entry(
    index = 40,
    label = "S_38434",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {6,S}
4  C u0 p0 c0 {3,D} {5,S} {7,S}
5  C u0 p0 c0 {2,S} {4,S} {11,D}
6  O u0 p2 c0 {1,S} {3,S}
7  O u0 p2 c0 {4,S} {12,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {5,D}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85774,0.00839441,0.000163442,-3.2619e-07,1.93779e-10,-9536.87,12.0192], Tmin=(10,'K'), Tmax=(562.582,'K')),
            NASAPolynomial(coeffs=[2.32418,0.0513359,-3.64735e-05,1.19383e-08,-1.46115e-12,-9871.32,14.0297], Tmin=(562.582,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-79.351,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-O': 3, 'C-H': 3, 'C=C': 1, 'C=O': 1, 'C-C': 4, 'H-O': 1}
1D rotors:
pivots: [2, 7], dihedral: [12, 2, 7, 6], rotor symmetry: 1, max scan energy: 28.74 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.06498500    1.27121400   -1.52993600
O       2.22570200   -0.05286400   -1.08596800
O       1.11981400   -1.55134400    1.06703700
C      -1.11572600    1.01354600   -0.01248900
C      -1.02599800   -0.34465100    0.65047100
C       0.06612900    1.09609800   -0.80354700
C       1.07538900    0.27021500   -0.47027600
C       0.51733800   -0.60888500    0.60390700
H      -1.50804900    1.88245600    0.50032800
H      -1.49699000   -1.13689600    0.05951700
H      -1.45068800   -0.37289200    1.65542000
H       2.63614100   -0.74226800   -0.53946600
""",
)

entry(
    index = 41,
    label = "S_4316",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {5,D} {7,S}
5  C u0 p0 c0 {3,S} {4,D} {17,S}
6  C u0 p0 c0 {2,S} {8,D} {18,S}
7  C u0 p0 c0 {4,S} {9,D} {19,S}
8  C u0 p0 c0 {6,D} {22,S} {23,S}
9  C u0 p0 c0 {7,D} {20,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54911,0.0658136,-1.24163e-05,-1.56233e-08,6.67282e-12,10303.6,14.2897], Tmin=(10,'K'), Tmax=(1250.47,'K')),
            NASAPolynomial(coeffs=[14.8885,0.0525673,-2.41476e-05,5.35667e-09,-4.65586e-13,5667.4,-50.1495], Tmin=(1250.47,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (85.6962,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (544.598,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 14, 'C-C': 5, 'C=C': 3}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [4, 1, 2, 6], invalidation reason: 
* Invalidated! pivots: [1, 4], dihedral: [2, 1, 4, 5], invalidation reason: 
pivots: [2, 6], dihedral: [1, 2, 6, 8], rotor symmetry: 1, max scan energy: 10.01 kJ/mol
pivots: [3, 5], dihedral: [14, 3, 5, 4], rotor symmetry: 3, max scan energy: 3.02 kJ/mol
pivots: [4, 7], dihedral: [1, 4, 7, 9], rotor symmetry: 1, max scan energy: 27.81 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.26368800    1.96075300    1.95132800
C      -3.58024000    2.77608500    1.97986500
C      -0.61379400    2.93218400   -0.50106800
C      -2.07480300    1.18035800    0.66764600
C      -1.35608100    1.63671600   -0.37696800
C      -3.76679800    3.52238700    3.27020300
C      -2.72547300   -0.13034700    0.54032500
C      -4.78018400    3.35539800    4.11507500
C      -3.46318900   -0.76338800    1.45925900
H      -1.42243100    2.64038500    2.10763300
H      -2.25540400    1.27399300    2.80252500
H      -4.43161800    2.11231800    1.80643200
H      -3.56037800    3.48718800    1.14461400
H       0.44402100    2.75263600   -0.72590800
H      -1.00908900    3.52434800   -1.33490800
H      -0.66700900    3.54846700    0.39674400
H      -1.29985100    0.99525400   -1.25505600
H      -2.99041500    4.24626500    3.51732900
H      -2.57377500   -0.62136500   -0.41906000
H      -3.66519400   -0.34662200    2.43916900
H      -3.89200400   -1.73660000    1.25207800
H      -4.85479900    3.92323000    5.03583000
H      -5.57732700    2.64588900    3.91271800
""",
)

entry(
    index = 42,
    label = "S_2887",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u0 p1 c0 {1,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70368,0.0241318,6.15067e-06,-1.60824e-08,5.64947e-12,31619.9,9.24082], Tmin=(10,'K'), Tmax=(1085.13,'K')),
            NASAPolynomial(coeffs=[2.94393,0.0339795,-1.72034e-05,4.25023e-09,-4.13705e-13,31369.9,11.0565], Tmin=(1085.13,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (262.872,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 8, 'C-C': 3}
1D rotors:
pivots: [1, 2], dihedral: [4, 1, 2, 7], rotor symmetry: 3, max scan energy: 8.99 kJ/mol
* Invalidated! pivots: [1, 4], dihedral: [2, 1, 4, 3], invalidation reason: Another conformer for S_2887 exists which is 11.15 kJ/mol lower.Significant difference observed between consecutive conformers
pivots: [3, 4], dihedral: [10, 3, 4, 1], rotor symmetry: 3, max scan energy: 7.93 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       0.15498400   -0.09744500    0.97653800
C      -0.71271700    0.89786800    1.75055800
C       1.67880800   -0.45898200   -0.90587800
C       1.25440500    0.45142500    0.17336300
H      -0.44756000   -0.88782100    0.48972500
H       0.80529000   -0.65075500    1.69427400
H      -1.36660300    1.44403600    1.06570000
H      -1.34561300    0.39113100    2.48414200
H      -0.08575800    1.62806000    2.26529800
H       2.73971900   -0.38037700   -1.15633800
H       1.15178500    0.00040400   -1.76509800
H       1.35474300   -1.51341700   -0.85603900
""",
)

entry(
    index = 43,
    label = "S_1017",
    molecule =
"""
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3 C u0 p1 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88907,0.00764705,0.00010922,-2.8833e-07,2.25436e-10,34860.3,6.6256], Tmin=(10,'K'), Tmax=(445.602,'K')),
            NASAPolynomial(coeffs=[4.80297,0.0214729,-1.14771e-05,3.1916e-09,-3.64024e-13,34560.2,0.501207], Tmin=(445.602,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (289.835,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 6, 'C-C': 2}
1D rotors:
pivots: [1, 3], dihedral: [4, 1, 3, 2], rotor symmetry: 1, max scan energy: 16.10 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 3 2 7 F
A 3 2 8 F
A 3 1 5 F
A 3 1 6 F
D 8 2 3 1 F
pivots: [2, 3], dihedral: [7, 2, 3, 1], rotor symmetry: 1, max scan energy: 16.10 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 3 2 8 F
A 3 2 9 F
A 3 1 6 F
A 3 1 4 F
D 6 1 3 2 F


External symmetry: 2, optical isomers: 2

Geometry:
C       1.22328700    0.01971700   -0.17307800
C      -1.22167600    0.03637700   -0.24585900
C       0.01979500    0.68754300   -0.69653900
H       1.42784600    0.67342200    0.69918800
H       1.12177900   -1.00811700    0.21770600
H       2.10353600    0.12114000   -0.81241000
H      -1.42562400   -0.59743100   -1.13283200
H      -2.07962800    0.70963500   -0.17869200
H      -1.16931500   -0.64228800    0.62369900
""",
)

entry(
    index = 44,
    label = "S_1033",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {3,S} {6,D}
5  C u1 p0 c0 {1,S} {7,S} {16,S}
6  C u0 p0 c0 {4,D} {8,S} {17,S}
7  C u0 p0 c0 {5,S} {8,D} {19,S}
8  C u0 p0 c0 {6,S} {7,D} {18,S}
9  O u0 p2 c0 {1,S} {20,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75779,0.0157589,0.000282246,-6.42105e-07,4.41871e-10,-8139.7,13.9171], Tmin=(10,'K'), Tmax=(484.486,'K')),
            NASAPolynomial(coeffs=[2.3877,0.0746921,-4.76549e-05,1.47286e-08,-1.75157e-12,-8565.85,13.7661], Tmin=(484.486,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-67.7311,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (469.768,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C-H': 10, 'C-C': 6, 'H-O': 1, 'C-O': 1, 'C=C': 2}
1D rotors:
pivots: [1, 2], dihedral: [20, 1, 2, 3], rotor symmetry: 1, max scan energy: 20.01 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 10], rotor symmetry: 3, max scan energy: 13.48 kJ/mol
pivots: [4, 5], dihedral: [13, 4, 5, 2], rotor symmetry: 3, max scan energy: 5.60 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.87113400   -0.44596000   -2.04607900
C       0.04838300    0.53323000   -1.47589900
C      -0.37286500    0.61277500    0.00218300
C       1.81223200   -1.30685000   -1.04313600
C       1.47927900    0.03459100   -1.63030300
C      -0.17876100    1.86054200   -2.15008800
C       2.41319100    0.77991400   -2.30060300
C       0.79998600    2.54874300   -2.79989700
C       2.11690300    2.03486100   -2.87720800
H      -0.33673400   -0.37723700    0.46028100
H       0.28059200    1.29016300    0.55537400
H      -1.39996500    0.97873800    0.06515700
H       1.04581700   -2.04173600   -1.30351500
H       2.78030700   -1.66363800   -1.40027500
H       1.85598800   -1.26921600    0.05214500
H      -1.19404800    2.24045500   -2.10053300
H       3.42037300    0.38543100   -2.40215700
H       2.88907500    2.58815600   -3.39759500
H       0.56978900    3.49825800   -3.27234900
H      -0.70568500   -0.45958300   -2.99607900
""",
)

entry(
    index = 45,
    label = "S_36966",
    molecule =
"""
1  O u0 p2 c0 {4,S} {12,S}
2  O u0 p2 c0 {7,D}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
6  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
7  C u0 p0 c0 {2,D} {4,S} {8,S}
8  C u0 p0 c0 {3,D} {5,S} {7,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82069,0.0108734,0.000171769,-3.7048e-07,2.33702e-10,-28501.8,12.1178], Tmin=(10,'K'), Tmax=(545.77,'K')),
            NASAPolynomial(coeffs=[4.4287,0.0457357,-3.21096e-05,1.05618e-08,-1.30719e-12,-29153.8,4.18796], Tmin=(545.77,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-237.042,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'H-O': 1, 'C=O': 2, 'C-H': 3, 'C-O': 1, 'C-C': 6}
1D rotors:
pivots: [1, 4], dihedral: [12, 1, 4, 5], rotor symmetry: 1, max scan energy: 26.24 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.28401500    1.99482800    0.07094500
O      -2.26170000    0.56885200   -0.82714200
O      -1.48241600   -2.24093600    0.55303100
C       0.10216600    0.67634800   -0.19185400
C       0.43370400   -0.66499200    0.70773600
C       1.25161000   -0.21012000   -0.47995900
C      -1.22445300    0.05433400   -0.50866200
C      -0.85994200   -1.26345300    0.25707400
H       0.84277300   -0.71704100    1.70770000
H       2.20246200    0.23897500   -0.21010200
H       1.28591600   -0.81265700   -1.38165300
H      -0.57414200    2.37586200    0.30288700
""",
)

entry(
    index = 46,
    label = "S_937",
    molecule =
"""
multiplicity 3
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
4  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {5,S} {8,D}
7  C u1 p0 c0 {3,S} {9,S} {17,S}
8  C u0 p0 c0 {6,D} {10,S} {18,S}
9  C u0 p0 c0 {7,S} {10,D} {20,S}
10 C u0 p0 c0 {8,S} {9,D} {19,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.89589,0.120593,-0.000478239,1.22018e-06,-1.08481e-09,-2490.06,21.3341], Tmin=(10,'K'), Tmax=(384.718,'K')),
            NASAPolynomial(coeffs=[0.380653,0.0785268,-4.8248e-05,1.41557e-08,-1.59703e-12,-1791.7,37.6271], Tmin=(384.718,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-20.7475,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (478.082,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Bond corrections: {'C=C': 2, 'C-H': 10, 'C-C': 6, 'C-O': 1, 'O-O': 1}
1D rotors:
pivots: [1, 3], dihedral: [2, 1, 3, 4], rotor symmetry: 1, max scan energy: 2.68 kJ/mol
Troubleshot with the following constraints and 8.0 degrees resolution:
A 2 1 14 F
A 1 2 11 F
D 1 2 4 12 F
D 2 1 5 15 F
* Invalidated! pivots: [3, 4], dihedral: [1, 3, 4, 11], invalidation reason: Bond ([[1, 14]]) broke during the scan.Significant difference observed between consecutive conformersCould not read energies
* Invalidated! pivots: [5, 6], dihedral: [14, 5, 6, 3], invalidation reason: Bond ([[1, 14]]) broke during the scan.Bond ([[2, 11]]) broke during the scan.Significant difference observed between consecutive conformersCould not read energies


External symmetry: 1, optical isomers: 1

Geometry:
O      -2.96273700    1.09542400    3.44758100
O      -2.34191100    0.24868200    4.03997300
C       0.41010600   -0.50068300    0.29253000
C      -0.29942000   -1.55618400    1.10613800
C      -1.82444600    0.52377600   -0.34901600
C      -0.31591300    0.48952300   -0.40022500
C       1.80504300   -0.49374400    0.21722300
C       0.38226500    1.44676200   -1.14036700
C       2.48964500    0.46671900   -0.52388900
C       1.77365000    1.44325300   -1.20707900
H      -0.89222500   -1.11430600    1.91376000
H       0.41463600   -2.24679500    1.55824300
H      -0.98952500   -2.14417000    0.49183500
H      -2.19190100    0.65830300    0.67363100
H      -2.26296700   -0.40734100   -0.72326200
H      -2.21755300    1.34320900   -0.95334600
H       2.36401900   -1.25655200    0.75018500
H      -0.17681700    2.20885700   -1.67423700
H       2.29096400    2.19798900   -1.78892000
H       3.57303700    0.44938800   -0.56558700
""",
)
