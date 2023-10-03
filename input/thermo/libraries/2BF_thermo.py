#!/usr/bin/env python
# encoding: utf-8

name = "2BF_thermo_1"
shortDesc = ""
longDesc = """
ARC v1.1.0
ARC projects 2BF_thermo_1, 2BF_thermo_2, 2BF_thermo_3, 2BF_thermo_4

Levels of theory used:

Conformers:       wb97xd/def2svp, software: gaussian (dft)
TS guesses:       None
Composite method: cbs-qb3, software: gaussian (composite) (using a fine grid)
Frequencies:      b3lyp/cbsb7, software: gaussian (dft)
Rotor scans:      b3lyp/cbsb7, software: gaussian (dft)
Using p-type bond additivity corrections for thermo

Using the following ESS settings: {'gaussian': ['local'], 'molpro': ['local']}
"""
entry(
    index = 0,
    label = "2BF",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {9,S}
2  C u0 p0 c0 {3,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {4,S} {7,D}
7  C u0 p0 c0 {6,D} {8,S} {19,S}
8  C u0 p0 c0 {7,S} {9,D} {20,S}
9  C u0 p0 c0 {1,S} {8,D} {21,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.27968,0.0778335,-0.000210571,5.86559e-07,-5.54501e-10,-20561.5,14.3607], Tmin=(10,'K'), Tmax=(394.541,'K')),
            NASAPolynomial(coeffs=[-1.77769,0.0823342,-4.98564e-05,1.45185e-08,-1.63212e-12,-19798.3,38.6695], Tmin=(394.541,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-170.984,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (494.711,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-C': 5, 'C-H': 12, 'C-O': 2}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.89 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 23.58 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Another conformer for 2BF exists which is 0.94 kJ/mol lower.Another conformer for 2BF exists which is 0.94 kJ/mol lower.
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 8.35 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -3.07491600   -1.68527100    0.50462700
C      -1.75938300   -1.28375200   -0.16827000
C      -1.83149900    0.07992600   -0.86279100
C      -0.50686500    0.48084000   -1.53999000
C      -0.56307700    1.79094000   -2.24753300
C       0.03818900    2.99625300   -2.04865400
C      -0.44488300    3.87513500   -3.07495800
C      -1.30570900    3.14139000   -3.82291300
O      -1.39174600    1.86895300   -3.33555100
H      -3.88965000   -1.74130400   -0.22382000
H      -2.99385900   -2.66241600    0.98841800
H      -3.36567700   -0.95870400    1.26963500
H      -1.47636500   -2.04795300   -0.90234600
H      -0.95664700   -1.26821700    0.57922800
H      -2.10747300    0.85172200   -0.13489000
H      -2.62574200    0.06760700   -1.61681600
H      -0.21736200   -0.30201500   -2.25223800
H       0.29086500    0.53522300   -0.79295700
H       0.74299900    3.23181000   -1.26678500
H      -0.18214700    4.90960800   -3.22960000
H      -1.90822200    3.35339400   -4.68969700
""",
)

entry(
    index = 1,
    label = "PB1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {8,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {6,S} {16,S}
6  C u0 p0 c0 {5,S} {7,D} {17,S}
7  C u0 p0 c0 {6,D} {9,S} {20,S}
8  C u1 p0 c0 {3,S} {18,S} {19,S}
9  O u0 p2 c0 {4,S} {7,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.27556,0.0796449,-0.000244065,7.00254e-07,-6.78083e-10,4332.22,15.023], Tmin=(10,'K'), Tmax=(381.045,'K')),
            NASAPolynomial(coeffs=[-1.57283,0.0803934,-4.96036e-05,1.46507e-08,-1.66448e-12,5065.77,38.5129], Tmin=(381.045,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (35.9896,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (473.925,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-C': 5, 'C-H': 11, 'C-O': 2}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 2, max scan energy: 3.07 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 10.88 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       2.81975700    0.42892200   -1.30550200
C       1.57160500    0.59137700   -0.50801300
C       1.69142100    0.12010000    0.95217900
C       1.90846100   -1.40055700    1.10482900
C       0.75357700   -2.22811300    0.65359800
C       0.57273200   -3.12916700   -0.35118000
C      -0.78526700   -3.58423300   -0.26157900
C      -1.33315000   -2.92563600    0.78965700
O      -0.41278500   -2.09475400    1.36086900
H       2.78664500    0.28442800   -2.37828900
H       3.78879800    0.61406300   -0.85382200
H       1.27733900    1.65557600   -0.49391600
H       0.74219000    0.07009700   -0.99900700
H       2.52898900    0.64051300    1.43064200
H       0.78965200    0.40545700    1.50177300
H       2.78768900   -1.70825400    0.53222700
H       2.11819400   -1.62399100    2.15729900
H       1.31777600   -3.43369000   -1.06919000
H      -1.27911000   -4.30358500   -0.89542200
H      -2.30852800   -2.92952200    1.24569800
""",
)

entry(
    index = 2,
    label = "PB2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {6,D} {9,S}
5  C u1 p0 c0 {1,S} {3,S} {17,S}
6  C u0 p0 c0 {4,D} {7,S} {18,S}
7  C u0 p0 c0 {6,S} {8,D} {19,S}
8  C u0 p0 c0 {7,D} {9,S} {20,S}
9  O u0 p2 c0 {4,S} {8,S}
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
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96059,0.0453369,2.23246e-05,-4.41223e-08,1.51265e-11,2865.55,13.98], Tmin=(10,'K'), Tmax=(1168.56,'K')),
            NASAPolynomial(coeffs=[12.6148,0.0479503,-2.24101e-05,5.00658e-09,-4.34672e-13,-1358.06,-38.5373], Tmin=(1168.56,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (23.9643,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (478.082,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-C': 5, 'C-H': 11, 'C-O': 2}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 2.12 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C      -3.07518400    0.58610300    0.83711500
C      -3.19258700   -0.63625600   -0.00725800
C      -2.80680800   -1.97687000    0.52006300
C      -2.68390500   -3.07431700   -0.56145200
C      -3.96965800   -3.41041300   -1.23587800
C      -4.42173700   -3.29984400   -2.51579300
C      -5.76475700   -3.80515100   -2.52654300
C      -6.03278400   -4.18501200   -1.25267600
O      -4.95219300   -3.95384800   -0.45115200
H      -2.10996700    0.62873900    1.35698500
H      -3.84732600    0.61993400    1.62468500
H      -3.18366400    1.50050500    0.24838600
H      -3.78089900   -0.59119000   -0.91814300
H      -1.85170000   -1.90394300    1.05845300
H      -3.53575600   -2.32130200    1.27367200
H      -1.97210500   -2.75647700   -1.32801100
H      -2.27428700   -3.97998900   -0.09971200
H      -3.86475800   -2.90842900   -3.35248300
H      -6.43308200   -3.87334700   -3.37018600
H      -6.89236700   -4.61603600   -0.76828200
""",
)

entry(
    index = 3,
    label = "PB3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {6,D} {9,S}
5  C u1 p0 c0 {1,S} {2,S} {17,S}
6  C u0 p0 c0 {4,D} {7,S} {18,S}
7  C u0 p0 c0 {6,S} {8,D} {19,S}
8  C u0 p0 c0 {7,D} {9,S} {20,S}
9  O u0 p2 c0 {4,S} {8,S}
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
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86799,0.050677,6.15397e-06,-2.84813e-08,1.01215e-11,3469.98,13.7078], Tmin=(10,'K'), Tmax=(1226.17,'K')),
            NASAPolynomial(coeffs=[14.6491,0.0435912,-1.95339e-05,4.16444e-09,-3.42988e-13,-1285.16,-49.1123], Tmin=(1226.17,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (28.9517,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (473.925,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-C': 5, 'C-H': 11, 'C-O': 2}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.66 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 7.46 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Another conformer for PB3 exists which is 1.32 kJ/mol lower.Another conformer for PB3 exists which is 1.32 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.68516700    1.61998500    1.30759800
C      -2.78657800    0.42856600    0.34825500
C      -2.21066500   -0.83475500    0.89390500
C      -1.99011000   -2.04334200    0.02811600
C      -3.18004700   -2.95549700   -0.02304500
C      -3.42610500   -4.20711100    0.45366500
C      -4.78233000   -4.52178100    0.10709200
C      -5.26347200   -3.43847400   -0.55175800
O      -4.30232700   -2.47222500   -0.64115300
H      -1.64227300    1.84062400    1.55138300
H      -3.12736500    2.51880200    0.87020400
H      -3.20990600    1.41343900    2.24512000
H      -2.29434300    0.67147100   -0.60417900
H      -3.84530600    0.26721000    0.08169900
H      -2.20613800   -0.98400600    1.97053200
H      -1.73583600   -1.73154100   -0.99266300
H      -1.14765200   -2.63369300    0.40315000
H      -2.72628100   -4.83235500    0.98539500
H      -5.31886700   -5.43274300    0.32014700
H      -6.21125900   -3.20041100   -1.00365600
""",
)

entry(
    index = 4,
    label = "PB4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {5,S} {6,D} {9,S}
5  C u1 p0 c0 {2,S} {4,S} {17,S}
6  C u0 p0 c0 {4,D} {7,S} {18,S}
7  C u0 p0 c0 {6,S} {8,D} {19,S}
8  C u0 p0 c0 {7,D} {9,S} {20,S}
9  O u0 p2 c0 {4,S} {8,S}
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
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70947,0.0394271,5.66509e-05,-9.70712e-08,3.95516e-11,-4361.54,15.2644], Tmin=(10,'K'), Tmax=(881.82,'K')),
            NASAPolynomial(coeffs=[3.90035,0.0666233,-3.7345e-05,1.00786e-08,-1.05687e-12,-5486.27,8.18113], Tmin=(881.82,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-36.216,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (473.925,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-C': 5, 'C-H': 11, 'C-O': 2}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.79 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for PB4 exists which is 1.05 kJ/mol lower.Another conformer for PB4 exists which is 1.05 kJ/mol lower.
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 11.52 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C       3.35985200   -0.22815000   -0.79776200
C       2.29305400    0.54005700   -0.01327200
C       1.69340200   -0.28632600    1.14405500
C       0.61606600    0.43290900    1.89158600
C       0.67035200    0.78372700    3.22508600
C      -0.23375700    1.45774000    4.06732200
C       0.36155300    1.52860800    5.34406600
C       1.57909600    0.91160500    5.24441500
O       1.78928800    0.45389400    3.97862500
H       2.94631100   -1.13973000   -1.24062700
H       3.77097900    0.37866700   -1.60902700
H       4.19062100   -0.52332100   -0.14941600
H       2.72148900    1.46148300    0.39490100
H       1.48814100    0.84908300   -0.69028800
H       2.48986600   -0.57786400    1.83341400
H       1.28631500   -1.21766100    0.72384900
H      -0.28170200    0.72184600    1.35488900
H      -1.19683800    1.83904400    3.76767800
H      -0.04922300    1.97754000    6.23486000
H       2.37183000    0.72610200    5.94943600
""",
)

entry(
    index = 5,
    label = "PB5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {8,S} {9,D}
6  C u0 p0 c0 {7,D} {9,S} {19,S}
7  C u0 p0 c0 {6,D} {8,S} {20,S}
8  O u0 p2 c0 {5,S} {7,S}
9  C u1 p0 c0 {5,D} {6,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.24541,0.0817742,-0.000246164,6.67511e-07,-6.21293e-10,13817.3,15.111], Tmin=(10,'K'), Tmax=(390.592,'K')),
            NASAPolynomial(coeffs=[-1.0797,0.0780647,-4.75742e-05,1.39142e-08,-1.56892e-12,14521.3,36.5986], Tmin=(390.592,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (114.855,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (469.768,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-C': 5, 'C-H': 11, 'C-O': 2}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.89 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 23.53 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Another conformer for PB5 exists which is 0.95 kJ/mol lower.Another conformer for PB5 exists which is 0.95 kJ/mol lower.
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 7.99 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.05888000   -0.80927200    0.56461600
C      -3.18679600    0.05142500   -0.01117600
C      -2.69414500    1.08189200   -1.03222100
C      -3.83229800    1.94492900   -1.60977800
C      -3.38104300    2.93495200   -2.62402500
C      -3.30549000    4.28215100   -2.69408100
C      -2.75747000    4.68692100   -3.94337100
C      -2.51827000    3.51223300   -4.58654000
O      -2.88292000    2.44315200   -3.81795600
H      -1.31262500   -0.19302400    1.07543000
H      -1.54375600   -1.36475900   -0.22510900
H      -2.44056000   -1.53567800    1.28710800
H      -3.70458400    0.56932300    0.80542100
H      -3.93544100   -0.59587800   -0.48393400
H      -1.95077300    1.73891100   -0.56641100
H      -2.18336200    0.56997500   -1.85487300
H      -4.58997500    1.29028600   -2.05800500
H      -4.32822800    2.49620900   -0.80571200
H      -2.56968600    5.68236700   -4.31020500
H      -2.11125600    3.27272100   -5.55484800
""",
)

entry(
    index = 6,
    label = "PB6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {6,D} {8,S}
6  C u0 p0 c0 {5,D} {9,S} {19,S}
7  C u0 p0 c0 {8,S} {9,D} {20,S}
8  O u0 p2 c0 {5,S} {7,S}
9  C u1 p0 c0 {6,S} {7,D}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.25593,0.0798923,-0.000224018,5.97901e-07,-5.53339e-10,13743.3,15.037], Tmin=(10,'K'), Tmax=(393.641,'K')),
            NASAPolynomial(coeffs=[-0.86343,0.0776301,-4.72707e-05,1.38256e-08,-1.55956e-12,14409.5,35.4119], Tmin=(393.641,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (114.242,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (469.768,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-C': 5, 'C-H': 11, 'C-O': 2}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.88 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 23.56 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Another conformer for PB6 exists which is 0.96 kJ/mol lower.Another conformer for PB6 exists which is 0.96 kJ/mol lower.
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 7.88 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.27476000   -0.94090500   -1.61412500
C      -1.66675300   -1.12852600   -0.22140500
C      -1.73138000    0.13888900    0.63707000
C      -1.11759900   -0.05337900    2.03730900
C      -1.14071200    1.17673000    2.87852100
C      -1.80145000    1.51044100    4.02709700
C      -1.39351700    2.84622300    4.29592400
C      -0.53658000    3.26201500    3.34467900
O      -0.36947300    2.22532000    2.44955800
H      -1.75537800   -0.15337700   -2.16866500
H      -2.21168800   -1.85945800   -2.20366400
H      -3.33015600   -0.65870500   -1.55025100
H      -0.62133300   -1.44554200   -0.31864400
H      -2.18521500   -1.94457300    0.29678300
H      -1.20725600    0.95519100    0.12893600
H      -2.77386500    0.45965300    0.74566800
H      -0.08034000   -0.39522800    1.93219200
H      -1.65467200   -0.84097300    2.57442800
H      -2.47579700    0.88494200    4.58846500
H       0.01261500    4.16348400    3.14207400
""",
)

entry(
    index = 7,
    label = "PB7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {6,D} {8,S}
6  C u0 p0 c0 {5,D} {7,S} {19,S}
7  C u0 p0 c0 {6,S} {9,D} {20,S}
8  O u0 p2 c0 {5,S} {9,S}
9  C u1 p0 c0 {7,D} {8,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.25741,0.0788689,-0.000205119,5.33753e-07,-4.89131e-10,13644.1,14.9515], Tmin=(10,'K'), Tmax=(397.119,'K')),
            NASAPolynomial(coeffs=[-0.55467,0.0771312,-4.69573e-05,1.37409e-08,-1.55123e-12,14263.4,33.8066], Tmin=(397.119,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (113.42,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (469.768,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-C': 5, 'C-H': 11, 'C-O': 2}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.88 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 23.56 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Another conformer for PB7 exists which is 0.91 kJ/mol lower.Another conformer for PB7 exists which is 0.91 kJ/mol lower.
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 9.07 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -3.04414500   -1.20496800    0.84392800
C      -1.80293900   -1.01889300   -0.03315500
C      -1.66683700    0.40326700   -0.58659500
C      -0.41835900    0.58620300   -1.47058900
C      -0.27220800    1.95223400   -2.04076500
C       0.61761100    2.96797800   -1.87943100
C       0.19646600    4.06709400   -2.72070100
C      -0.92432700    3.59618500   -3.31237000
O      -1.24824200    2.35716500   -2.95144700
H      -3.95930400   -0.99276100    0.28278000
H      -3.11563400   -2.22845500    1.22159700
H      -3.02284500   -0.53279300    1.70724400
H      -1.83559000   -1.72940100   -0.86801300
H      -0.90560900   -1.27049800    0.54550100
H      -2.55683700    0.65686600   -1.17238300
H      -1.62570900    1.12080300    0.24094900
H       0.48445300    0.37499800   -0.88832500
H      -0.44313900   -0.14780600   -2.28575700
H       1.48520300    2.95191300   -1.23726400
H       0.66188800    5.02913800   -2.84740800
""",
)

entry(
    index = 8,
    label = "PB8",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {9,S} {16,S}
2  C u0 p0 c0 {3,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {2,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {17,S} {18,S} {19,S}
6  C u1 p0 c0 {1,S} {7,S} {20,S}
7  C u0 p0 c0 {6,S} {8,D} {21,S}
8  C u0 p0 c0 {7,D} {9,S} {22,S}
9  O u0 p2 c0 {1,S} {8,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4616,0.0630024,-1.00978e-05,-1.82735e-08,7.88527e-12,-10642.4,13.6226], Tmin=(10,'K'), Tmax=(1165.1,'K')),
            NASAPolynomial(coeffs=[11.035,0.0569675,-2.80338e-05,6.69814e-09,-6.29114e-13,-13762.3,-29.8877], Tmin=(1165.1,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-88.4782,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (519.654,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C-C': 6, 'C-H': 13, 'C-O': 2}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.92 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 23.42 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 22.68 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Another conformer for PB8 exists which is 2.21 kJ/mol lower.Another conformer for PB8 exists which is 2.21 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
C       3.87540300   -0.06346800    0.48938600
C       2.46410900   -0.63933300    0.34220000
C       1.41434500    0.42122600   -0.00752600
C       0.00160400   -0.15230800   -0.15554300
C      -1.05188600    0.89651900   -0.53135000
C      -2.44952600    0.38088700   -0.72024900
C      -2.83440400    0.65588200   -2.02111600
C      -1.78907800    1.30483300   -2.65417300
O      -0.71663900    1.47716000   -1.83281200
H       3.91522600    0.68785600    1.28431300
H       4.60201700   -0.84333800    0.73313800
H       4.20284300    0.41888600   -0.43674500
H       2.46538700   -1.41393000   -0.43408600
H       2.17613700   -1.14311500    1.27318600
H       1.69375600    0.92074400   -0.94091100
H       1.41103300    1.19749000    0.76900100
H      -0.01298500   -0.93863800   -0.91809000
H      -0.31577900   -0.61804600    0.78576400
H      -1.00365500    1.72459800    0.19370000
H      -3.02330500   -0.11026200    0.05059100
H      -3.77950000    0.41149700   -2.48375700
H      -1.68094700    1.67974900   -3.65927300
""",
)

entry(
    index = 9,
    label = "PB9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {7,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {18,S} {19,S} {20,S}
6  C u1 p0 c0 {3,S} {4,S} {9,S}
7  C u0 p0 c0 {4,S} {8,D} {21,S}
8  C u0 p0 c0 {7,D} {9,S} {22,S}
9  O u0 p2 c0 {6,S} {8,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2721,0.0787246,-0.000199847,5.72889e-07,-5.52862e-10,-4950.42,14.423], Tmin=(10,'K'), Tmax=(392.991,'K')),
            NASAPolynomial(coeffs=[-2.3408,0.0881236,-5.35371e-05,1.56348e-08,-1.76181e-12,-4140.67,40.9491], Tmin=(392.991,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-41.1874,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (523.812,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C-C': 6, 'C-H': 13, 'C-O': 2}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.93 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for PB9 exists which is 3.32 kJ/mol lower.Another conformer for PB9 exists which is 3.32 kJ/mol lower.
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 19.36 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C       2.56646100   -1.32008800   -1.48294200
C       2.86583100   -0.80184100   -0.07334300
C       1.97396200    0.37328700    0.33992500
C       2.28463400    0.90073000    1.76178800
C       1.45282200    2.05804900    2.18435100
C       0.01985900    2.05652400    2.64604000
C      -0.38962800    3.47416200    2.32091300
C       0.62515300    4.07005900    1.69762900
O       1.72954100    3.26566700    1.54025000
H       2.70839600   -0.53377700   -2.23073100
H       3.22131200   -2.15429400   -1.74956800
H       1.53269400   -1.67024200   -1.56461500
H       2.74689000   -1.61872300    0.64916800
H       3.91671600   -0.49385200   -0.01296700
H       2.09507900    1.19732800   -0.37160600
H       0.92145900    0.06874600    0.28741500
H       3.34265100    1.18661700    1.80698700
H       2.14889600    0.09036800    2.48712700
H      -0.60204000    1.31138400    2.11529200
H      -0.07965900    1.81451300    3.71475900
H      -1.34583400    3.92137300    2.54438900
H       0.73233400    5.06834100    1.30141200
""",
)

entry(
    index = 10,
    label = "PB10",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {7,S} {8,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {3,S} {7,D} {9,S}
7  C u0 p0 c0 {4,S} {6,D} {21,S}
8  C u1 p0 c0 {4,S} {9,S} {22,S}
9  O u0 p2 c0 {6,S} {8,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.23659,0.0789494,-0.000158228,3.94022e-07,-3.56074e-10,-5382.14,15.0159], Tmin=(10,'K'), Tmax=(412.618,'K')),
            NASAPolynomial(coeffs=[-0.938979,0.0844107,-5.07816e-05,1.47424e-08,-1.65546e-12,-4739.46,35.0764], Tmin=(412.618,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-44.7714,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (519.654,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C-C': 6, 'C-H': 13, 'C-O': 2}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.91 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 23.47 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Another conformer for PB10 exists which is 0.80 kJ/mol lower.Another conformer for PB10 exists which is 0.80 kJ/mol lower.
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 11.47 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.50254000    1.31800600    0.47446100
C      -3.68269500    0.35675600    0.30770400
C      -3.27469900   -0.99700400   -0.28216300
C      -4.46405200   -1.96084400   -0.45061800
C      -4.07372400   -3.29605400   -0.98470600
C      -4.36106500   -3.93484200   -2.12186000
C      -3.67261200   -5.27951500   -2.12767100
C      -2.89667700   -5.18877400   -0.84840000
O      -3.23610800   -4.03696000   -0.16156900
H      -2.02359900    1.52666700   -0.48718600
H      -2.82257300    2.27283900    0.90024600
H      -1.74110900    0.89627900    1.13766700
H      -4.44247100    0.81907500   -0.33447400
H      -4.16330700    0.19613300    1.28039700
H      -2.79807500   -0.84620900   -1.25779600
H      -2.52412900   -1.46884200    0.35998300
H      -5.20974900   -1.52558400   -1.12221900
H      -4.95184000   -2.10130900    0.52210600
H      -4.99428500   -3.55522600   -2.90909800
H      -3.02829200   -5.42786000   -3.00777700
H      -4.38957900   -6.11973300   -2.14049700
H      -2.53294000   -5.99209000   -0.22502100
""",
)

entry(
    index = 11,
    label = "PB11",
    molecule = 
"""
multiplicity 2
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
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77815,0.0256921,0.000662404,-3.43751e-06,5.9816e-09,-35146.1,13.6953], Tmin=(10,'K'), Tmax=(172.695,'K')),
            NASAPolynomial(coeffs=[1.94883,0.088289,-5.69798e-05,1.77579e-08,-2.12429e-12,-35113,18.4347], Tmin=(172.695,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-291.538,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (540.441,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-C': 6, 'C=C': 1, 'C-H': 12, 'C-O': 3}
1D rotors:
pivots: [1, 2], dihedral: [11, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.96 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 23.70 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 25.55 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Another conformer for PB11 exists which is 0.80 kJ/mol lower.Another conformer for PB11 exists which is 0.80 kJ/mol lower.
pivots: [5, 6], dihedral: [4, 5, 6, 20], rotor symmetry: 1, max scan energy: 21.60 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       3.60167200    0.38907500    0.48005700
C       2.27271800    0.74772600   -0.19099500
C       2.01600600    2.25814300   -0.24016500
C       0.68572400    2.60814100   -0.91607800
C       0.39096300    4.10752600   -0.98422000
O       0.44786300    4.60814300    0.32619300
C      -0.85934200    4.49086600   -1.73202900
C      -0.50846500    5.26062100   -2.82500300
C       0.87317700    5.38692500   -2.83269900
O       1.45714700    4.75050800   -1.79046200
H       3.63285500    0.75290600    1.51170000
H       4.44596900    0.83726100   -0.05288700
H       3.75937100   -0.69278400    0.50356000
H       2.25785300    0.34175100   -1.21006800
H       1.45051500    0.25634900    0.34384000
H       2.82993200    2.75254200   -0.78013600
H       2.02072600    2.66739600    0.77408000
H       0.66537600    2.21960000   -1.93887800
H      -0.14603600    2.14138300   -0.37695100
H       0.13781600    5.52101400    0.30302800
H      -1.84389900    4.17811200   -1.41992700
H      -1.17272500    5.69938600   -3.55510600
H       1.53476300    5.90832900   -3.50682500
""",
)

entry(
    index = 12,
    label = "PB12",
    molecule = 
"""
multiplicity 2
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
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43347,0.0686688,-1.2554e-05,-1.93249e-08,8.65887e-12,-25566.5,14.5887], Tmin=(10,'K'), Tmax=(1151.59,'K')),
            NASAPolynomial(coeffs=[12.1946,0.0601119,-2.99007e-05,7.21203e-09,-6.82923e-13,-29034.8,-35.2127], Tmin=(1151.59,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-212.553,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (548.755,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C-C': 6, 'H-O': 1, 'C-H': 12, 'C-O': 3}
1D rotors:
pivots: [1, 2], dihedral: [11, 1, 2, 3], rotor symmetry: 3, max scan energy: 12.02 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 23.59 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Another conformer for PB12 exists which is 1.73 kJ/mol lower.Another conformer for PB12 exists which is 1.73 kJ/mol lower.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [9, 10], dihedral: [5, 9, 10, 23], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C       1.83091000    2.58436400   -0.52935600
C       3.25838500    2.07500500   -0.74790300
C       3.36231900    0.54744500   -0.70728200
C       4.80505600    0.03258900   -0.93475300
C       4.94667800   -1.44077400   -0.86526500
O       4.90237400   -2.02603800    0.38762500
C       4.84565300   -3.38798200    0.18644700
C       4.79808000   -3.73426100   -1.10179000
C       4.75732300   -2.47662700   -1.93385700
O       3.53760000   -2.32618000   -2.71222500
H       1.15278600    2.19807700   -1.29650500
H       1.78644400    3.67625600   -0.56583300
H       1.44330200    2.26819300    0.44408400
H       3.63122900    2.43643100   -1.71394300
H       3.92070900    2.50299900    0.01440600
H       3.00543900    0.17890200    0.26115300
H       2.71381600    0.11153400   -1.47420200
H       5.46671900    0.49158700   -0.18925400
H       5.15106700    0.36433800   -1.91941800
H       4.85511000   -3.97643900    1.09099200
H       4.75045200   -4.73659300   -1.49769600
H       5.53355000   -2.43076000   -2.70598800
H       2.80272000   -2.47149600   -2.10401800
""",
)

entry(
    index = 13,
    label = "PB13",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {15,S} {16,S}
4  C u0 p0 c0 {7,S} {8,S} {10,S} {17,S}
5  C u0 p0 c0 {2,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {3,S} {7,D} {9,S}
7  C u0 p0 c0 {4,S} {6,D} {21,S}
8  C u1 p0 c0 {4,S} {9,S} {22,S}
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
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.27298,0.0803147,-4.57417e-05,1.13749e-08,-7.91673e-13,-25990.2,16.0796], Tmin=(10,'K'), Tmax=(1494.37,'K')),
            NASAPolynomial(coeffs=[21.8566,0.0412723,-1.72929e-05,3.47515e-09,-2.71713e-13,-32739.1,-85.0382], Tmin=(1494.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-216.16,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (540.441,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C-C': 6, 'H-O': 1, 'C-H': 12, 'C-O': 3}
1D rotors:
pivots: [1, 2], dihedral: [11, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.91 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for PB13 exists which is 3.51 kJ/mol lower.Another conformer for PB13 exists which is 3.51 kJ/mol lower.
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 19.45 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 10.86 kJ/mol
pivots: [7, 8], dihedral: [6, 7, 8, 22], rotor symmetry: 1, max scan energy: 13.95 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       2.63768900    0.93071500    2.21720100
C       1.83338200   -0.04332800    1.35195400
C       2.69529800   -1.15107800    0.73760900
C       1.88165000   -2.13124500   -0.12891900
C       2.71271700   -3.19157800   -0.76302300
C       2.74761200   -4.52280100   -0.63803000
C       3.85033500   -5.08624100   -1.50168900
O       4.87767700   -5.79899700   -0.77345900
C       4.31331900   -3.82885500   -2.16259800
O       3.66422400   -2.72796800   -1.67041800
H       3.42171900    1.42245800    1.63331700
H       3.12204400    0.41246200    3.05053300
H       1.99808700    1.71090600    2.63832400
H       1.33141200    0.50974400    0.54895600
H       1.03641400   -0.49545700    1.95483900
H       3.19683200   -1.71258500    1.53455100
H       3.48602600   -0.70620800    0.12501500
H       1.10921300   -2.61609000    0.47465700
H       1.36673500   -1.56981600   -0.91828700
H       2.11213600   -5.11743300   -0.00014200
H       3.50022700   -5.84064900   -2.21624500
H       5.21171800   -5.19026400   -0.10353100
H       5.14704100   -3.64554900   -2.82009900
""",
)

entry(
    index = 14,
    label = "PB14",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {6,S}
2  O u0 p2 c0 {4,S} {15,S}
3  O u0 p2 c0 {5,S} {14,S}
4  C u0 p0 c0 {1,S} {2,S} {7,S} {9,S}
5  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
6  C u0 p0 c0 {1,S} {5,S} {8,D}
7  C u1 p0 c0 {4,S} {8,S} {12,S}
8  C u0 p0 c0 {6,D} {7,S} {13,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80608,0.0123602,0.000213186,-4.76189e-07,3.18529e-10,-43508.2,14.0243], Tmin=(10,'K'), Tmax=(502.17,'K')),
            NASAPolynomial(coeffs=[3.0133,0.0576182,-3.83263e-05,1.2141e-08,-1.46226e-12,-43919.6,12.4139], Tmin=(502.17,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-361.8,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (353.365,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 2, 'C-C': 3, 'C=C': 1, 'C-H': 5, 'C-O': 4}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [9, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [6, 7], dihedral: [5, 6, 7, 15], rotor symmetry: 1, max scan energy: 22.32 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.39903100   -0.91008000    1.00354200
C       1.74670800    0.36908000    0.46921100
C       1.98531800    0.32244000   -0.99745700
C       1.33484400    0.89723000   -2.08257200
C       1.95608400    0.47012700   -3.24093300
C       3.05303500   -0.48302800   -2.86744300
O       2.92279200   -1.78115100   -3.36567100
O       3.01081700   -0.48249500   -1.39998800
H       2.11243100   -1.51249500    0.76585900
H       2.63960800    0.76531000    0.97570200
H       0.91133800    1.03654200    0.68397500
H       0.48402500    1.55842600   -2.00584100
H       1.72566900    0.73162200   -4.26213400
H       4.06396000   -0.17227600   -3.14467200
H       1.99347200   -2.03133800   -3.28738800
""",
)

entry(
    index = 15,
    label = "PB15",
    molecule = 
"""
multiplicity 2
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
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.25869,0.075439,-3.01202e-05,-4.53347e-09,4.44475e-12,-35055.6,15.9068], Tmin=(10,'K'), Tmax=(1158.57,'K')),
            NASAPolynomial(coeffs=[12.6582,0.0591093,-2.98519e-05,7.32329e-09,-7.05537e-13,-38315.6,-35.4936], Tmin=(1158.57,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-291.495,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (540.441,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C-C': 6, 'H-O': 1, 'C-H': 12, 'C-O': 3}
1D rotors:
pivots: [1, 2], dihedral: [11, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.92 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 23.51 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Another conformer for PB15 exists which is 0.97 kJ/mol lower.Another conformer for PB15 exists which is 0.97 kJ/mol lower.
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 9.27 kJ/mol
pivots: [8, 9], dihedral: [7, 8, 9, 23], rotor symmetry: 1, max scan energy: 22.06 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       4.18305500    1.02961200    0.84759100
C       3.33097800    1.31788000   -0.39155000
C       2.57397100    0.08620600   -0.89797700
C       1.71693200    0.37911800   -2.14780500
C       0.92483600   -0.78913700   -2.61150500
C       0.97865700   -1.54739700   -3.77460400
C       0.02952500   -2.55208200   -3.69159900
C      -0.65799300   -2.43891600   -2.36427900
O      -0.54565200   -3.55271800   -1.52523800
O      -0.02562400   -1.26460600   -1.75656100
H       4.93706900    0.26400400    0.64007700
H       4.70632400    1.92674700    1.18920300
H       3.56532100    0.66892100    1.67563300
H       3.97117600    1.70673800   -1.19300600
H       2.61163400    2.11356700   -0.16336900
H       1.92171700   -0.29959500   -0.10818900
H       3.28620600   -0.71356200   -1.13328100
H       1.03001100    1.20425200   -1.91539000
H       2.35521500    0.71695100   -2.96991500
H       1.66176500   -1.36407200   -4.59137100
H      -0.21502300   -3.30846700   -4.42115700
H      -1.72999900   -2.22497000   -2.40358600
H       0.36205500   -3.87423900   -1.59387700
""",
)

entry(
    index = 16,
    label = "PB16",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {5,S}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {2,D} {4,S} {7,S}
4  C u0 p0 c0 {3,S} {5,D} {8,S}
5  C u0 p0 c0 {1,S} {4,D} {9,S}
6  C u1 p0 c0 {2,S} {10,S} {11,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.1537,-0.0147656,0.000219245,-3.93122e-07,2.25597e-10,6062.27,10.4373], Tmin=(10,'K'), Tmax=(563.018,'K')),
            NASAPolynomial(coeffs=[0.720469,0.043979,-2.87874e-05,8.94419e-09,-1.05631e-12,5904.39,20.1931], Tmin=(563.018,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (50.3816,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-C': 2, 'C-H': 5, 'C-O': 2}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [7, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
C       2.02109400   -0.18580200    0.10117700
C       0.64839300   -0.17889700    0.04738200
C      -0.32184000   -1.19639500    0.13726200
C      -1.58221300   -0.57941500    0.01147700
C      -1.34755000    0.76121700   -0.14719100
O      -0.01480000    1.02782500   -0.12915400
H       2.55099200   -1.11709000    0.23811600
H       2.58159100    0.73312800    0.00782900
H      -0.11190800   -2.24481100    0.27651700
H      -2.55049400   -1.05429700    0.03354900
H      -1.99657600    1.61076300   -0.27849800
""",
)

entry(
    index = 17,
    label = "PB17",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  C u0 p0 c0 {4,S} {6,D} {11,S}
6  C u0 p0 c0 {1,S} {5,D} {14,S}
7  C u1 p0 c0 {2,S} {12,S} {13,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89588,0.00651104,0.000174717,-3.51549e-07,2.20617e-10,11207.2,13.151], Tmin=(10,'K'), Tmax=(501.088,'K')),
            NASAPolynomial(coeffs=[0.246218,0.0562825,-3.60518e-05,1.10582e-08,-1.29971e-12,11313.9,25.6513], Tmin=(501.088,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (93.1513,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-C': 3, 'C-H': 7, 'C-O': 2}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [8, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for PB17 exists which is 0.71 kJ/mol lower.Another conformer for PB17 exists which is 0.71 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.29162500   -0.18453300   -0.60780400
C      -1.42469600    0.18238700    0.54717500
C       0.04009400    0.06265500    0.26917600
C       0.79280600    0.07814000   -0.86497700
C       2.16071200   -0.05202600   -0.45140900
C       2.13922700   -0.13602800    0.90186500
O       0.85477300   -0.06968800    1.36020700
H      -3.27528000    0.25317900   -0.71520600
H      -2.01880800   -1.00566100   -1.25868700
H      -1.64767400   -0.45970700    1.41719500
H      -1.65816300    1.20141500    0.88416000
H       0.42076100    0.17874100   -1.87181300
H       3.03527800   -0.07982200   -1.08184200
H       2.90066000   -0.24486700    1.65522500
""",
)

entry(
    index = 18,
    label = "PB18",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {7,S}
2  C u0 p0 c0 {3,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {2,S} {5,D}
5  C u0 p0 c0 {4,D} {6,S} {13,S}
6  C u0 p0 c0 {5,S} {7,D} {14,S}
7  C u0 p0 c0 {1,S} {6,D} {17,S}
8  C u1 p0 c0 {3,S} {15,S} {16,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9088,0.037347,2.08282e-05,-4.07077e-08,1.44137e-11,7557.59,14.7203], Tmin=(10,'K'), Tmax=(1114.65,'K')),
            NASAPolynomial(coeffs=[9.48871,0.0429339,-2.11549e-05,5.01505e-09,-4.64416e-13,4722.65,-19.942], Tmin=(1114.65,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (62.9432,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (399.095,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-C': 4, 'C-H': 9, 'C-O': 2}
1D rotors:
pivots: [1, 2], dihedral: [9, 1, 2, 3], rotor symmetry: 1, max scan energy: 0.92 kJ/mol (set as a FreeRotor)
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for PB18 exists which is 0.56 kJ/mol lower.Another conformer for PB18 exists which is 0.56 kJ/mol lower.
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 8.62 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       1.82252500   -1.18008700    0.90643600
C       2.29079800    0.19853200    0.59931400
C       1.13430900    1.21021100    0.42334700
C       1.59203900    2.60318600    0.16373900
C       1.49082000    3.44434300   -0.90216700
C       2.15622500    4.66117100   -0.53451500
C       2.61573100    4.47152500    0.72720100
O       2.28257100    3.22407600    1.17091400
H       2.42059300   -2.04406600    0.64546500
H       0.94608000   -1.34082100    1.52427000
H       2.94343000    0.57168900    1.40576000
H       2.91440400    0.19880500   -0.30191700
H       0.49706400    0.89840300   -0.40813400
H       0.51020800    1.19262400    1.32519100
H       0.99937000    3.22631800   -1.83729000
H       2.27197400    5.55144400   -1.13203700
H       3.16643300    5.08430400    1.42037900
""",
)

entry(
    index = 19,
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
    index = 20,
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
    index = 21,
    label = "PBROO3",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {9,S} {11,S}
2  O u0 p2 c0 {3,S} {7,S}
3  O u1 p2 c0 {2,S}
4  C u0 p0 c0 {5,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {4,S} {8,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {9,S} {16,S} {17,S}
7  C u0 p0 c0 {2,S} {10,S} {11,S} {18,S}
8  C u0 p0 c0 {5,S} {19,S} {20,S} {21,S}
9  C u0 p0 c0 {1,S} {6,S} {10,D}
10 C u0 p0 c0 {7,S} {9,D} {22,S}
11 C u1 p0 c0 {1,S} {7,S} {23,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.47404,0.169731,-0.000783286,2.02863e-06,-1.80817e-09,-22788.6,21.8703], Tmin=(10,'K'), Tmax=(381.016,'K')),
            NASAPolynomial(coeffs=[-0.435429,0.0927259,-5.67218e-05,1.65168e-08,-1.8478e-12,-21786.2,43.344], Tmin=(381.016,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-189.547,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (557.07,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 12, 'C-C': 6, 'C-O': 3, 'O-O': 1, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [12, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[9, 14]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[9, 14]]) broke during the scan. But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Bond ([[9, 14]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[9, 14]]) broke during the scan. But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Bond ([[9, 14]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[9, 14]]) broke during the scan. But unable to propose troubleshooting methods.
* Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 9], invalidation reason: Bond ([[9, 14]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[9, 14]]) broke during the scan. But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C      -3.11387000    0.53315300   -1.22646600
C      -2.29215300   -0.60701900   -0.61825100
C      -2.97957700   -1.26239400    0.58403500
C      -2.16886700   -2.40697100    1.22671000
C      -1.96804500   -3.59184200    0.34365100
C      -0.87053000   -4.20034700   -0.18469000
C      -1.34383800   -5.31351800   -0.95666600
O      -4.68354400   -2.98715200   -2.75477800
O      -5.48448000   -2.38883300   -2.08087700
C      -2.69500800   -5.30082100   -0.84404500
O      -3.09552000   -4.26039300   -0.05548600
H      -3.29991200    1.32441300   -0.49329800
H      -2.59875000    0.98495100   -2.07857000
H      -4.08566100    0.17369200   -1.57789900
H      -1.31041600   -0.22678900   -0.30912100
H      -2.09647900   -1.36622300   -1.38297900
H      -3.17108800   -0.50354700    1.35175700
H      -3.95794600   -1.64977500    0.28080800
H      -2.67637100   -2.72825000    2.14410800
H      -1.18158400   -2.04189800    1.52627200
H       0.15384400   -3.89447100   -0.04128400
H      -0.75369500   -6.02162700   -1.51646900
H      -3.48197300   -5.92172200   -1.23673200
""",
)

entry(
    index = 22,
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
    index = 23,
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
    index = 24,
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
    index = 25,
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
    index = 26,
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
    index = 27,
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
    index = 28,
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
    index = 29,
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
    index = 30,
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
    index = 31,
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

entry(
    index = 32,
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
    index = 33,
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
    index = 34,
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
    index = 35,
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
    index = 36,
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
    index = 37,
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
    index = 38,
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
    index = 39,
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
    index = 40,
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
    index = 41,
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
    index = 42,
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

entry(
    index = 43,
    label = "TB13",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {8,D}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {7,S} {11,S} {12,S}
5  C u0 p0 c0 {2,S} {9,S} {15,S} {16,S}
6  C u0 p0 c0 {8,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {4,S} {17,S} {18,S} {19,S}
8  C u0 p0 c0 {1,D} {2,S} {6,S}
9  C u2 p0 c0 {5,S} {6,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.26357,0.0761612,-0.000143448,3.55917e-07,-3.28816e-10,16535.9,14.4905], Tmin=(10,'K'), Tmax=(403.227,'K')),
            NASAPolynomial(coeffs=[-0.309385,0.0812954,-4.97969e-05,1.46674e-08,-1.66601e-12,17070.4,31.5382], Tmin=(403.227,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (137.467,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (494.711,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 8, 'C-H': 12, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.93 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 25.28 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 22.95 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       3.18846600    0.26549100   -0.07572600
C       1.77119400    0.48373200   -0.61287600
C       0.71917300   -0.34307400    0.13479600
C      -0.70454300   -0.16451500   -0.39605900
C      -1.36664900    1.23411000   -0.17089300
C      -2.80163600    0.89738000   -0.00234500
C      -3.11363100   -0.51831200    0.27377400
C      -1.70773000   -1.17372400    0.18560400
O      -1.45152000   -2.29662700    0.52813000
H       3.48223200   -0.78556700   -0.15421300
H       3.26010900    0.55044700    0.97843000
H       3.92029100    0.85862500   -0.63039100
H       1.52008500    1.54889000   -0.55060900
H       1.73987200    0.22446700   -1.67828800
H       0.73662200   -0.08393100    1.20096900
H       0.97180900   -1.40669300    0.07602300
H      -0.70808900   -0.36503300   -1.47790800
H      -0.94404300    1.70765300    0.73008900
H      -1.17408900    1.92119000   -1.00138500
H      -3.54501300   -0.72438800    1.26309300
H      -3.78115100   -0.99656800   -0.45791800
""",
)

entry(
    index = 44,
    label = "TB14",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {6,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {6,S} {9,S} {12,S} {13,S}
4  C u0 p0 c0 {8,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {9,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {1,D} {2,S} {3,S}
7  C u0 p0 c0 {2,S} {8,D} {20,S}
8  C u0 p0 c0 {4,S} {7,D} {21,S}
9  C u2 p0 c0 {3,S} {5,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.67908,0.138049,-0.000523506,1.16255e-06,-9.1297e-10,22200.3,16.277], Tmin=(10,'K'), Tmax=(422.486,'K')),
            NASAPolynomial(coeffs=[2.35691,0.0715783,-4.06818e-05,1.11923e-08,-1.19838e-12,22848,24.8966], Tmin=(422.486,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (184.551,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (490.554,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 12, 'C=O': 1, 'C-C': 6, 'C=C': 1}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 1.76 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 9.94 kJ/mol
pivots: [4, 6], dihedral: [3, 4, 6, 7], rotor symmetry: 1, max scan energy: 8.63 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [4, 6, 7, 8], invalidation reason: Another conformer for R1 exists which is 0.60 kJ/mol lower.
pivots: [8, 9], dihedral: [7, 8, 9, 18], rotor symmetry: 3, max scan energy: 7.96 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.05707200    1.00261300    0.26980600
C      -1.39793500    0.61486900    0.72887300
C      -2.56525500    0.05165200    0.02862500
C      -2.22550700   -1.38089900   -0.43312300
O      -1.74009200   -1.58300600   -1.52092900
C      -2.50304200   -2.49082200    0.57625100
C      -1.84092200   -3.79695700    0.25185300
C      -1.14136000   -4.52284000    1.12062900
C      -0.47735600   -5.83277600    0.81335800
H       0.43510300    0.18862600   -0.28441100
H      -0.09358500    1.87502900   -0.40231200
H      -2.81241800    0.64008400   -0.86827100
H      -3.44115100    0.03993900    0.68723900
H      -2.23184700   -2.13789400    1.57640800
H      -3.59952000   -2.60416200    0.58950500
H      -1.94832300   -4.13881800   -0.77419300
H      -1.02758000   -4.15629800    2.14086100
H       0.60186300   -5.78008700    0.99531800
H      -0.63223600   -6.12555200   -0.22754900
H      -0.86478600   -6.63292100    1.45415100
H       0.59001700    1.26804000    1.11146200
""",
)

entry(
    index = 45,
    label = "TB15",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {5,S} {8,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {7,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,D} {2,S} {3,S}
6  C u0 p0 c0 {3,S} {7,D} {18,S}
7  C u0 p0 c0 {4,S} {6,D} {19,S}
8  C u0 p0 c0 {2,S} {9,D} {17,S}
9  C u0 p0 c0 {8,D} {20,S} {21,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.96268,0.106184,-0.000313285,6.81615e-07,-5.3822e-10,-12623.2,15.8341], Tmin=(10,'K'), Tmax=(427.56,'K')),
            NASAPolynomial(coeffs=[1.44846,0.0748472,-4.3708e-05,1.23683e-08,-1.35979e-12,-12077.8,26.7166], Tmin=(427.56,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-104.981,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (494.711,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 12, 'C=O': 1, 'C-C': 5, 'C=C': 2}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for P1 exists which is 0.70 kJ/mol lower.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [4, 6], dihedral: [3, 4, 6, 7], rotor symmetry: 1, max scan energy: 6.46 kJ/mol
pivots: [6, 7], dihedral: [4, 6, 7, 8], rotor symmetry: 1, max scan energy: 16.02 kJ/mol
pivots: [8, 9], dihedral: [7, 8, 9, 19], rotor symmetry: 3, max scan energy: 7.92 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -3.84404700    0.35346400    0.33515000
C      -2.52762700    0.40135300    0.16209500
C      -1.55125200   -0.53832500    0.80544900
C      -0.48964300   -1.08402200   -0.14742100
O      -0.28235100   -0.60126100   -1.23573600
C       0.30411100   -2.29614700    0.35076600
C      -0.41302800   -3.57203900   -0.01371100
C      -0.89402800   -4.45604500    0.85922000
C      -1.61044000   -5.72366200    0.49816100
H      -4.50447800    1.06227400   -0.15124400
H      -4.31280100   -0.39542700    0.96705600
H      -2.09264500    1.15142200   -0.49136100
H      -2.05926900   -1.37319200    1.29824500
H      -0.99086900   -0.01954000    1.59988300
H       1.28181900   -2.25742200   -0.13837700
H       0.44481900   -2.24131000    1.43449400
H      -0.53984500   -3.74764000   -1.08044200
H      -0.75735100   -4.26821800    1.92398600
H      -1.08135700   -6.60010200    0.88844400
H      -1.70498700   -5.83720000   -0.58404700
H      -2.61619900   -5.74561100    0.93226700
""",
)

entry(
    index = 46,
    label = "TB16",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
2  C u0 p0 c0 {4,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {9,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {6,D} {8,S} {9,S}
6  C u0 p0 c0 {1,S} {5,D} {20,S}
7  C u0 p0 c0 {2,S} {8,D} {19,S}
8  C u0 p0 c0 {5,S} {7,D} {21,S}
9  O u0 p2 c0 {3,S} {5,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73551,0.0440978,4.85903e-05,-8.51373e-08,3.3265e-11,-13154.2,12.9532], Tmin=(10,'K'), Tmax=(945.238,'K')),
            NASAPolynomial(coeffs=[5.74439,0.0666477,-3.64692e-05,9.60729e-09,-9.85043e-13,-14921.1,-3.96299], Tmin=(945.238,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-109.287,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 12, 'C-O': 2, 'C=C': 2, 'C-C': 5}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 12.38 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for P1 exists which is 2.00 kJ/mol lower.
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 30.99 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       3.53745600   -0.69656300    0.64619200
C       3.13573000    0.38353100   -0.37311400
C       1.79169600    0.98314300   -0.08529500
C       0.74114500    0.94577900   -0.91399800
C      -0.55814300    1.51855100   -0.61799900
C      -1.66739300    1.54547200   -1.37335400
C      -2.78598600    2.19320700   -0.59458000
C      -2.00543700    2.77285700    0.60576000
O      -0.71405200    2.11380300    0.61253500
H       2.83257700   -1.53175400    0.62768300
H       3.54904400   -0.29337700    1.66297900
H       4.53542300   -1.08728600    0.42953000
H       3.14659000   -0.03659400   -1.38415200
H       3.89305200    1.17853000   -0.35657800
H       1.66926000    1.47306500    0.87769400
H       0.82483400    0.46194600   -1.88342800
H      -1.76142000    1.11209900   -2.35741300
H      -3.54061000    1.45897900   -0.28316300
H      -3.31095300    2.97655200   -1.14916900
H      -1.83039300    3.84715700    0.48809900
H      -2.47445300    2.59284100    1.57314400
""",
)

entry(
    index = 47,
    label = "TB17",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {3,S} {8,D}
6  C u0 p0 c0 {3,S} {7,D} {18,S}
7  C u0 p0 c0 {6,D} {19,S} {20,S}
8  C u0 p0 c0 {5,D} {21,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.81825,0.113842,-0.000288699,5.13988e-07,-3.48784e-10,-9710.24,14.9962], Tmin=(10,'K'), Tmax=(468.13,'K')),
            NASAPolynomial(coeffs=[4.33658,0.0684545,-3.94065e-05,1.10592e-08,-1.21055e-12,-9497.23,12.617], Tmin=(468.13,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-80.7707,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (486.397,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 12, 'C-C': 5, 'C=O': 1, 'C=C': 2}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 19.34 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 18.75 kJ/mol
pivots: [4, 7], dihedral: [3, 4, 7, 8], rotor symmetry: 1, max scan energy: 18.98 kJ/mol
pivots: [7, 8], dihedral: [4, 7, 8, 9], rotor symmetry: 1, max scan energy: 22.24 kJ/mol
pivots: [8, 9], dihedral: [7, 8, 9, 19], rotor symmetry: 3, max scan energy: 11.63 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.72709000    1.87417000    0.95634500
C      -2.02808200    1.11136400   -0.09039600
C      -1.94464300   -0.39398500   -0.11218800
C      -0.93254400   -0.90378500   -1.13603700
C      -1.35407900   -1.58177400   -2.17689900
O      -1.72956400   -2.18412200   -3.10420800
C       0.55180000   -0.61881200   -0.96455000
C       1.21653700   -1.41712900    0.17039400
C       2.69900000   -1.07191500    0.33876300
H      -1.39695800    1.44357600    1.89729500
H      -1.80692200    2.95464500    0.91551200
H      -2.34967700    1.57645400   -1.02032200
H      -1.67798600   -0.76206500    0.88484100
H      -2.93233400   -0.80847900   -0.34080700
H       0.67387000    0.45436900   -0.77270000
H       1.08008400   -0.82244800   -1.90150900
H       0.68961500   -1.22520400    1.11117300
H       1.10216300   -2.48707400   -0.03357500
H       2.83519900   -0.01125300    0.57145700
H       3.15147900   -1.65020600    1.14855500
H       3.26178200   -1.28478800   -0.57553800
""",
)


