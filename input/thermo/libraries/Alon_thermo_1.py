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

