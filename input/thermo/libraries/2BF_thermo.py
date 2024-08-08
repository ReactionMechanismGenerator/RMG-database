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
    index = 39,
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
    index = 40,
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
    index = 41,
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
    index = 42,
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
    index = 43,
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
    index = 44,
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
    index = 45,
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

entry(
    index = 46,
    label = "TB18",
    molecule = 
"""
multiplicity 3
1  O u1 p2 c0 {8,S}
2  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {6,S} {9,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {8,D} {19,S}
7  C u0 p0 c0 {3,S} {9,D} {20,S}
8  C u0 p0 c0 {1,S} {6,D} {21,S}
9  C u1 p0 c0 {4,S} {7,D}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.03486,0.0998102,-0.000274873,6.22842e-07,-5.1755e-10,22922.8,17.5468], Tmin=(10,'K'), Tmax=(411.281,'K')),
            NASAPolynomial(coeffs=[1.12384,0.0778508,-4.69093e-05,1.36241e-08,-1.52967e-12,23422.9,29.2373], Tmin=(411.281,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (190.565,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (494.711,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-H': 12, 'C-C': 5, 'C=C': 2}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.94 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 21.49 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 10.82 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 8], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 9], invalidation reason: Another conformer for R1 exists which is 7.30 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.30995000   -0.66834100   -1.76561000
C      -1.49442000   -0.74764400   -0.47223200
C      -1.12705500    0.63854600    0.08366100
C      -0.35054200    0.55572600    1.38676600
C       0.83811800    1.06694300    1.60837400
C       1.87478800    1.84731500    0.88699400
C       2.91493100    0.94136700    0.31162900
C       3.05669100    0.75845100   -1.09854200
O       2.34537200    1.32306500   -1.93419100
H      -2.55772500   -1.66559400   -2.13902600
H      -3.24929800   -0.12871200   -1.60940300
H      -1.75400000   -0.14744900   -2.55070000
H      -0.57425700   -1.31468800   -0.64877800
H      -2.05792000   -1.30357600    0.28644400
H      -2.04977100    1.20698600    0.26116800
H      -0.54963500    1.19013100   -0.66348700
H      -0.84616600    0.01185000    2.19330100
H       1.42014700    2.42894300    0.07495000
H       2.34305800    2.56178300    1.57818500
H       3.54718400    0.36780600    0.98233600
H       3.85598000    0.06691100   -1.42376200
""",
)

entry(
    index = 47,
    label = "TB19",
    molecule = 
"""
1  O u0 p2 c0 {9,D}
2  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {7,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {7,D} {19,S}
7  C u0 p0 c0 {4,S} {6,D} {20,S}
8  C u0 p0 c0 {4,S} {9,D} {21,S}
9  C u0 p0 c0 {1,D} {8,D}
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
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.81605,0.119304,-0.000370106,7.58278e-07,-5.65499e-10,-10038.2,14.8821], Tmin=(10,'K'), Tmax=(441.307,'K')),
            NASAPolynomial(coeffs=[2.81407,0.0708196,-4.04504e-05,1.12339e-08,-1.21627e-12,-9565.71,20.2411], Tmin=(441.307,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-83.4897,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (490.554,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-H': 12, 'C-C': 5, 'C=C': 2}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.85 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for P1 exists which is 1.42 kJ/mol lower.
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 9.62 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 13.62 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 9.69 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -3.36023700    0.44824800   -1.34226400
C      -2.68098900   -0.34704700   -0.22432600
C      -2.06740700    0.55182700    0.86489700
C      -1.36096300   -0.22169800    1.94194600
C      -1.68539300   -0.22044600    3.23371600
C      -0.97115100   -1.01233000    4.29893000
C      -1.88324700   -2.02340000    4.97923000
C      -2.18114900   -1.98786100    6.25492300
O      -2.43756600   -1.95087900    7.39073700
H      -4.17087300    1.06979700   -0.94944500
H      -2.64919300    1.11148500   -1.84475500
H      -3.78785000   -0.21490400   -2.09895600
H      -1.89594800   -0.98275800   -0.65071800
H      -3.40393600   -1.02532200    0.24189800
H      -1.35630700    1.23995900    0.38731800
H      -2.85069300    1.17470700    1.31098900
H      -0.52026200   -0.83524600    1.61507000
H      -2.52953400    0.37714500    3.57500600
H      -0.56527500   -0.33280000    5.05621300
H      -0.11442200   -1.53283500    3.85749200
H      -2.34304900   -2.81097800    4.39405200
""",
)

entry(
    index = 48,
    label = "TB12",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {6,S}
2  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {8,S} {12,S}
4  C u0 p0 c0 {2,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {3,S} {7,D}
7  C u0 p0 c0 {4,S} {6,D} {19,S}
8  C u0 p0 c0 {3,S} {9,D} {18,S}
9  C u0 p0 c0 {8,D} {20,S} {21,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85435,0.0191944,0.000828934,-6.14013e-06,1.62612e-08,1816.37,9.64874], Tmin=(10,'K'), Tmax=(94.584,'K')),
            NASAPolynomial(coeffs=[2.55278,0.0742382,-4.39976e-05,1.26196e-08,-1.40166e-12,1841,12.8586], Tmin=(94.584,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (24.5784,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (494.711,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C=C': 2, 'C-H': 12, 'C-C': 5}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 19.18 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 8.80 kJ/mol
* Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 9], invalidation reason: Another conformer for P1_3 exists which is 1.14 kJ/mol lower.
pivots: [8, 9], dihedral: [7, 8, 9, 19], rotor symmetry: 3, max scan energy: 11.76 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       1.08150400    1.10498800    2.35395700
C       1.82909500    0.72266400    1.32103900
C       2.07602000   -0.68945800    0.98085100
O       3.46647900   -1.00806300    0.50010800
C       2.42133000   -1.11604000   -0.35495900
C       2.16927400   -1.43475600   -1.61165200
C       0.79318200   -1.41446400   -2.22083600
C       0.65643800   -0.41951100   -3.38712800
C      -0.73229500   -0.44191200   -4.03095000
H       0.62303100    0.38324700    3.02273700
H       0.89657700    2.15161100    2.56333000
H       2.28470200    1.45341000    0.65912800
H       1.70133500   -1.43138000    1.68173300
H       3.00922500   -1.72116900   -2.23923200
H       0.05271600   -1.17483700   -1.44995200
H       0.54149700   -2.41875900   -2.58780300
H       0.88265000    0.58800100   -3.02155500
H       1.41632700   -0.64727000   -4.14389000
H      -1.50988400   -0.18605500   -3.30429900
H      -0.96762800   -1.43322700   -4.43096400
H      -0.80076700    0.27310900   -4.85512700
""",
)

entry(
    index = 49,
    label = "PBROO15",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {7,D} {9,S}
6  C u0 p0 c0 {7,S} {8,D} {10,S}
7  C u0 p0 c0 {5,D} {6,S} {20,S}
8  C u0 p0 c0 {6,D} {9,S} {21,S}
9  O u0 p2 c0 {5,S} {8,S}
10 O u0 p2 c0 {6,S} {22,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 O u1 p2 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.93521,0.1124,-0.000330529,7.92494e-07,-6.99163e-10,-12452.8,16.53], Tmin=(10,'K'), Tmax=(384.69,'K')),
            NASAPolynomial(coeffs=[1.32006,0.0852985,-5.36961e-05,1.61254e-08,-1.85712e-12,-12003.7,27.0007], Tmin=(384.69,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-103.568,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (515.497,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 11, 'O-O': 1, 'C-C': 5, 'C=C': 2, 'C-O': 3}
1D rotors:
pivots: [1, 2], dihedral: [12, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.87 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 23.45 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Another conformer for PBROO15 exists which is 1.14 kJ/mol lower.
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 7.84 kJ/mol
pivots: [7, 8], dihedral: [6, 7, 8, 9], rotor symmetry: 1, max scan energy: 19.24 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       3.64251100    1.62108600    0.67051500
C       3.25620000    1.61436900   -0.81102500
C       2.76076200    0.24751700   -1.29434500
C       2.37331800    0.24609000   -2.78616900
C       1.91349800   -1.07888300   -3.28441700
C       0.71577300   -1.54636800   -3.72919000
C       0.93992400   -2.92045400   -4.04359500
O       0.05619700   -3.84841300   -4.53269500
O      -1.16947300   -3.37125400   -4.72870500
C       2.24458300   -3.20923700   -3.77492600
O       2.85005800   -2.08398300   -3.30824300
H       4.44246400    0.90255900    0.87343300
H       2.79023600    1.35443500    1.30291000
H       3.99387400    2.60716300    0.98536400
H       2.47762100    2.36600900   -0.98927600
H       4.11877300    1.91993200   -1.41544200
H       3.53774200   -0.50599300   -1.12755100
H       1.89367200   -0.06306000   -0.70031000
H       3.23372500    0.57249000   -3.38291700
H       1.57244600    0.96914600   -2.96525600
H      -0.20989200   -1.00775700   -3.83025000
H       2.84172300   -4.09932700   -3.86039600
""",
)

entry(
    index = 50,
    label = "PBROO16",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {6,D} {9,S}
6  C u0 p0 c0 {5,D} {7,S} {20,S}
7  C u0 p0 c0 {6,S} {8,D} {21,S}
8  C u0 p0 c0 {7,D} {9,S} {10,S}
9  O u0 p2 c0 {5,S} {8,S}
10 O u0 p2 c0 {8,S} {22,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 O u1 p2 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.89304,0.114317,-0.000306103,6.70796e-07,-5.60334e-10,-12839.7,16.5658], Tmin=(10,'K'), Tmax=(393.929,'K')),
            NASAPolynomial(coeffs=[2.59759,0.0824234,-5.17904e-05,1.55521e-08,-1.79237e-12,-12545.6,21.1523], Tmin=(393.929,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-106.781,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (511.34,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 11, 'O-O': 1, 'C-C': 5, 'C=C': 2, 'C-O': 3}
1D rotors:
pivots: [1, 2], dihedral: [12, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.86 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 23.47 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 19.21 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 8.42 kJ/mol
pivots: [8, 9], dihedral: [7, 8, 9, 10], rotor symmetry: 1, max scan energy: 19.18 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -3.75942900    0.98804000    0.07033300
C      -2.50552400    0.38283800   -0.56661700
C      -2.82429400   -0.60526700   -1.69326500
C      -1.55795500   -1.21115400   -2.33127300
C      -1.83694300   -2.15647100   -3.44408700
C      -1.65444700   -3.49855700   -3.62149900
C      -2.14385000   -3.83380100   -4.92057600
C      -2.59042500   -2.65220900   -5.43179400
O      -3.15955900   -2.27632700   -6.59701600
O      -3.33241500   -3.28308200   -7.45826100
O      -2.42171500   -1.62508500   -4.57307800
H      -4.39689700    0.21182000    0.50453700
H      -4.35585600    1.53016500   -0.66963900
H      -3.50095600    1.68983300    0.86756100
H      -1.91228000   -0.12446500    0.20396200
H      -1.87105700    1.18607700   -0.96013600
H      -3.40836600   -0.10181400   -2.47071600
H      -3.45270900   -1.41632500   -1.30799100
H      -0.97932400   -1.74939100   -1.57472800
H      -0.91782300   -0.40028500   -2.70038900
H      -1.21638600   -4.17366700   -2.90342700
H      -2.16942900   -4.78834400   -5.41563800
""",
)

entry(
    index = 51,
    label = "PBROO14",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {8,S} {11,S}
2  O u0 p2 c0 {3,S} {9,S}
3  O u1 p2 c0 {2,S}
4  C u0 p0 c0 {5,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {4,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {8,S} {16,S} {17,S}
7  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
8  C u0 p0 c0 {1,S} {6,S} {9,D}
9  C u0 p0 c0 {2,S} {8,D} {10,S}
10 C u0 p0 c0 {9,S} {11,D} {21,S}
11 C u0 p0 c0 {1,S} {10,D} {22,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.91218,0.113589,-0.000325355,7.4825e-07,-6.38926e-10,-12755,16.8069], Tmin=(10,'K'), Tmax=(393.237,'K')),
            NASAPolynomial(coeffs=[1.76073,0.08363,-5.21181e-05,1.55376e-08,-1.77993e-12,-12342.2,25.384], Tmin=(393.237,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-106.08,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (515.497,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'O-O': 1, 'C=C': 2, 'C-H': 11, 'C-C': 5}
1D rotors:
pivots: [1, 2], dihedral: [12, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.87 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 23.36 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 18.57 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 7.22 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 8], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C       4.45820300   -0.22545300   -0.66901400
C       3.32008100   -0.43221800    0.33403900
C       1.97054600    0.08081700   -0.17831900
C       0.82877800   -0.13366100    0.83596600
C      -0.48565500    0.38010800    0.37356100
C      -1.66576700   -0.21995600    0.02539400
O      -1.84048900   -1.58036700    0.07444900
O      -3.05247500   -1.98441200   -0.29510400
C      -2.59843600    0.78869600   -0.36440700
C      -1.91751400    1.95186100   -0.22921900
O      -0.64293400    1.72707100    0.21423900
H       4.58939800    0.83501000   -0.90499000
H       4.25854700   -0.75113100   -1.60770500
H       5.40743200   -0.59813800   -0.27531500
H       3.56519600    0.07446300    1.27530000
H       3.23389900   -1.49852200    0.57510800
H       1.71397600   -0.42526800   -1.11578100
H       2.04559400    1.14845000   -0.41073500
H       1.08911400    0.35442800    1.78312900
H       0.71329300   -1.19990000    1.04942800
H      -3.61269900    0.63818900   -0.68936000
H      -2.17798500    2.98292100   -0.39574600
""",
)

entry(
    index = 52,
    label = "TB24",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {6,D} {18,S}
6  C u0 p0 c0 {5,D} {7,S} {20,S}
7  C u0 p0 c0 {6,S} {8,D} {19,S}
8  C u0 p0 c0 {7,D} {21,S} {22,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u1 p2 c0 {5,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.00409,0.0984215,-0.000205629,3.98567e-07,-3.0438e-10,-13315.3,14.1057], Tmin=(10,'K'), Tmax=(436.53,'K')),
            NASAPolynomial(coeffs=[2.00668,0.0800874,-4.82245e-05,1.40061e-08,-1.57399e-12,-12966.5,21.0891], Tmin=(436.53,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-110.737,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (511.34,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-C': 5, 'C-O': 1, 'C-H': 13}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 67.29 kJ/mol
pivots: [4, 6], dihedral: [3, 4, 6, 7], rotor symmetry: 1, max scan energy: 9.59 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [4, 6, 7, 8], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [7, 8], dihedral: [6, 7, 8, 9], rotor symmetry: 1, max scan energy: 23.61 kJ/mol
pivots: [8, 9], dihedral: [7, 8, 9, 20], rotor symmetry: 3, max scan energy: 11.90 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 42.93 kJ/mol
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
C       4.67189700    0.34836600   -0.18292800
C       3.41996200    0.87438300   -0.36058800
C       2.23543100    0.13339100   -0.30372200
C       0.92414100    0.75689700   -0.50298000
O       0.81195500    1.95597100   -0.72810300
C      -0.29049000   -0.16057100   -0.41604000
C      -1.62492700    0.54947600   -0.63252800
C      -2.82956800   -0.39329900   -0.54034100
C      -4.16616700    0.32159400   -0.75785300
H       4.81765900   -0.70770000    0.01842700
H       5.55760400    0.96893600   -0.23752700
H       3.30733500    1.93626000   -0.56082400
H       2.27815100   -0.93445800   -0.10698700
H      -0.15691300   -0.96817800   -1.14899000
H      -0.26927800   -0.65710500    0.56390500
H      -1.61281000    1.04376900   -1.60944200
H      -1.72512200    1.35468700    0.10261100
H      -2.83456100   -0.88387300    0.44098600
H      -2.72166300   -1.19641100   -1.27997400
H      -4.31907700    1.10735000   -0.01172400
H      -5.00749300   -0.37313700   -0.68687600
H      -4.20538400    0.79260400   -1.74482500
""",
)

entry(
    index = 53,
    label = "TB25",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {7,S} {9,S} {19,S} {20,S}
5  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {8,D} {9,S}
7  C u1 p0 c0 {4,S} {8,S} {21,S}
8  C u0 p0 c0 {6,D} {7,S} {22,S}
9  O u0 p2 c0 {4,S} {6,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.20802,0.0828488,-0.000193479,4.88833e-07,-4.3837e-10,-11269.4,15.0563], Tmin=(10,'K'), Tmax=(409.878,'K')),
            NASAPolynomial(coeffs=[-1.1183,0.0844412,-5.06222e-05,1.46421e-08,-1.6386e-12,-10573.5,36.2328], Tmin=(409.878,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-93.7228,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (519.654,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C-C': 6, 'C-O': 2, 'C-H': 13}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.93 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 23.64 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Another conformer for TB25 exists which is 0.80 kJ/mol lower.
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 10.04 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       3.37994500    1.60035600   -0.59888800
C       2.03568600    0.89863700   -0.81179000
C       2.01897600   -0.53965800   -0.28494300
C       0.66389600   -1.24548200   -0.50254500
C       0.64427900   -2.65986100   -0.04814300
C      -0.06483200   -3.31469800    0.94601500
C       0.30514900   -4.65060800    0.96103200
C       1.33533500   -4.83711600   -0.11013700
O       1.48523700   -3.52300100   -0.70468300
H       4.18883200    1.06456600   -1.10504800
H       3.36335300    2.62208300   -0.98800200
H       3.63427100    1.65371700    0.46424000
H       1.79159900    0.89358100   -1.88104400
H       1.24130100    1.47480000   -0.32132400
H       2.80226400   -1.12407000   -0.77829800
H       2.25513900   -0.54431600    0.78562300
H       0.41971500   -1.20981600   -1.57351100
H      -0.12818900   -0.70191100    0.02169100
H      -0.78860300   -2.83900300    1.59202100
H      -0.05759700   -5.43431500    1.60770600
H       1.04093700   -5.53744000   -0.90496100
H       2.32035700   -5.15587600    0.26105600
""",
)

entry(
    index = 54,
    label = "TB26",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {5,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {7,S} {16,S} {17,S} {18,S}
5  C u1 p0 c0 {1,S} {2,S} {19,S}
6  C u0 p0 c0 {2,S} {8,S} {20,D}
7  C u0 p0 c0 {4,S} {8,D} {21,S}
8  C u0 p0 c0 {6,S} {7,D} {22,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {6,D}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.86236,0.116303,-0.000346199,7.44145e-07,-5.8439e-10,-5935.11,14.2274], Tmin=(10,'K'), Tmax=(425.272,'K')),
            NASAPolynomial(coeffs=[1.88415,0.0783678,-4.61415e-05,1.31431e-08,-1.45266e-12,-5425.67,23.1216], Tmin=(425.272,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-49.3761,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (515.497,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C=C': 1, 'C-C': 6, 'C-H': 13}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 7.75 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 30.24 kJ/mol
* Invalidated! pivots: [4, 6], dihedral: [3, 4, 6, 7], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [6, 7], dihedral: [4, 6, 7, 8], invalidation reason: Another conformer for TB26 exists which is 2.24 kJ/mol lower.
pivots: [7, 8], dihedral: [6, 7, 8, 9], rotor symmetry: 1, max scan energy: 7.18 kJ/mol
pivots: [8, 9], dihedral: [7, 8, 9, 20], rotor symmetry: 3, max scan energy: 11.71 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       4.58514900   -0.01854200   -0.40766300
C       3.41609500    0.87358300   -0.14807200
C       2.13966100    0.48577000   -0.06610900
C       1.04457500    1.45910600    0.19742100
O       1.25088900    2.64699000    0.35063500
C      -0.36027900    0.86550000    0.26295500
C      -1.44250300    1.84640500    0.52618300
C      -2.86912500    1.42268200    0.61923300
C      -3.83912200    2.57607800    0.89559900
H       5.11924100    0.29883000   -1.31042000
H       4.28852800   -1.06227900   -0.52968900
H       5.30749000    0.04371300    0.41410200
H       3.61616900    1.93473300   -0.01293000
H       1.86651600   -0.55929000   -0.19089500
H      -0.52702200    0.31614900   -0.68138700
H      -0.34091800    0.06394900    1.02355800
H      -1.16230800    2.88545300    0.64935200
H      -3.16867700    0.90819400   -0.30945500
H      -2.98175700    0.65499000    1.40336300
H      -3.78695100    3.32798400    0.10328400
H      -4.87152300    2.22233600    0.95598100
H      -3.59739000    3.07122300    1.84018600
""",
)

entry(
    index = 55,
    label = "TB27",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {9,S}
2  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {6,S} {7,D}
5  C u0 p0 c0 {2,S} {6,D} {15,S}
6  C u0 p0 c0 {4,S} {5,D} {16,S}
7  C u0 p0 c0 {4,D} {8,S} {17,S}
8  C u0 p0 c0 {7,S} {9,D} {18,S}
9  C u0 p0 c0 {1,S} {8,D} {19,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64421,0.0401415,5.38354e-05,-1.00832e-07,4.39628e-11,-7298.36,13.2961], Tmin=(10,'K'), Tmax=(823.874,'K')),
            NASAPolynomial(coeffs=[3.76531,0.0649061,-3.74113e-05,1.03544e-08,-1.10998e-12,-8178.74,7.51349], Tmin=(823.874,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-60.6701,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 3, 'C-C': 4, 'C-O': 2, 'C-H': 10}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 12.44 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for TB27 exists which is 2.21 kJ/mol lower.
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 28.67 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.86881700    0.08462600    1.25571500
C      -2.73780200   -0.03713900   -0.27237700
C      -3.61417500   -1.10871600   -0.84981500
C      -4.58161100   -0.90173100   -1.75314000
C      -5.44252400   -1.91392100   -2.31940500
C      -6.45675000   -1.84534400   -3.23740600
C      -6.94880100   -3.17621800   -3.41045700
C      -6.20428600   -3.96209000   -2.58994100
O      -5.28391500   -3.21474000   -1.91857600
H      -2.62552500   -0.86131000    1.74836600
H      -2.19184000    0.84902400    1.64690200
H      -3.88923900    0.35467000    1.53955500
H      -2.96966800    0.92400600   -0.74283200
H      -1.69028700   -0.25894700   -0.51633600
H      -3.44544000   -2.12151400   -0.49034200
H      -4.76735400    0.10375000   -2.12243000
H      -6.80604800   -0.95023900   -3.72738600
H      -7.74747000   -3.50184100   -4.05767700
H      -6.19835300   -5.01702100   -2.37424500
""",
)

entry(
    index = 56,
    label = "TB28",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,S} {9,S}
2  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {6,D} {7,S}
6  C u0 p0 c0 {3,S} {5,D} {17,S}
7  C u0 p0 c0 {5,S} {8,D} {18,S}
8  C u0 p0 c0 {7,D} {9,S} {19,S}
9  C u1 p0 c0 {1,S} {8,S} {20,S}
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
            NASAPolynomial(coeffs=[3.69877,0.0459106,3.03234e-05,-6.21067e-08,2.42321e-11,-4367.59,15.2039], Tmin=(10,'K'), Tmax=(981.272,'K')),
            NASAPolynomial(coeffs=[6.85704,0.0599528,-3.22871e-05,8.38395e-09,-8.48734e-13,-6283.29,-6.57633], Tmin=(981.272,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-36.2444,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (469.768,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 5, 'C-O': 2, 'C=C': 2, 'C-H': 11}
1D rotors:
pivots: [2, 4], dihedral: [3, 2, 4, 14], rotor symmetry: 3, max scan energy: 11.79 kJ/mol
pivots: [2, 3], dihedral: [4, 2, 3, 6], rotor symmetry: 1, max scan energy: 21.03 kJ/mol
pivots: [3, 6], dihedral: [2, 3, 6, 5], rotor symmetry: 1, max scan energy: 11.52 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [1, 5, 6, 3], invalidation reason: Another conformer for R1 exists which is 2.28 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
O       0.64234900   -0.45457200   -3.06055100
C      -2.07694600    0.75863300   -0.35312500
C      -1.89342300   -0.07189600   -1.64092800
C      -2.60848700   -0.07363700    0.81666700
C      -0.22101800    0.55457800   -3.46655900
C      -1.41915300    0.73634800   -2.80650300
C       0.37355400    1.21893700   -4.55567700
C       1.61301400    0.59120400   -4.79895000
C       1.73365600   -0.41104000   -3.87483500
H      -1.11643700    1.21021000   -0.08351800
H      -2.76160400    1.59056000   -0.55529700
H      -2.85901700   -0.53679000   -1.88827400
H      -1.19410100   -0.88975300   -1.44954800
H      -1.92715300   -0.89522500    1.05839300
H      -2.72680700    0.53557000    1.71681800
H      -3.58350100   -0.51152000    0.58059400
H      -2.04870700    1.54334700   -3.16695800
H      -0.05913300    2.05072000   -5.08824100
H       2.33563600    0.84016500   -5.56028200
H       2.49779800   -1.14371800   -3.67694000
""",
)

entry(
    index = 57,
    label = "TB20",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {6,S} {10,S}
5  C u0 p0 c0 {1,S} {6,D} {11,S}
6  C u1 p0 c0 {4,S} {5,D}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9627,0.00232621,0.000117577,-2.15433e-07,1.27677e-10,22985.3,10.8796], Tmin=(10,'K'), Tmax=(434.805,'K')),
            NASAPolynomial(coeffs=[-0.683813,0.0449686,-2.91752e-05,9.02945e-09,-1.0683e-12,23390.3,29.4377], Tmin=(434.805,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (191.099,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C=C': 2, 'C-C': 2, 'C-H': 5}
1D rotors:
pivots: [1, 2], dihedral: [7, 1, 2, 3], rotor symmetry: 3, max scan energy: 3.62 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -1.59781700   -0.44182100    0.11405400
C      -0.18721200    0.02047900    0.02656700
C       0.41863600    1.04431300   -0.64434100
C       1.79326600    0.93039400   -0.29644500
C       1.96825300   -0.11209800    0.53673900
O       0.73324200   -0.69146900    0.74734000
H      -1.69834900   -1.47234600   -0.24031000
H      -2.23872700    0.19551300   -0.49647700
H      -1.96099700   -0.40858000    1.14587700
H      -0.05661000    1.76589300   -1.28814600
H       2.80198800   -0.56462800    1.04199700
""",
)

entry(
    index = 58,
    label = "TB21",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {6,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {3,S} {4,S} {20,D}
7  C u0 p0 c0 {4,S} {8,D} {21,S}
8  C u1 p0 c0 {7,D} {22,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {6,D}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.82771,0.117338,-0.00032983,6.64213e-07,-4.95918e-10,2351.35,15.5104], Tmin=(10,'K'), Tmax=(440.293,'K')),
            NASAPolynomial(coeffs=[2.69908,0.076003,-4.42056e-05,1.24843e-08,-1.37151e-12,2774.66,20.704], Tmin=(440.293,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (19.5212,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (515.497,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 13, 'C=C': 1, 'C-C': 6, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 10.00 kJ/mol
pivots: [4, 6], dihedral: [3, 4, 6, 7], rotor symmetry: 1, max scan energy: 12.01 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [4, 6, 7, 8], invalidation reason: Another conformer for TB21 exists which is 1.01 kJ/mol lower.
pivots: [7, 8], dihedral: [6, 7, 8, 9], rotor symmetry: 1, max scan energy: 23.54 kJ/mol
pivots: [8, 9], dihedral: [7, 8, 9, 20], rotor symmetry: 3, max scan energy: 11.90 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -4.51265800   -0.25726200   -1.81455100
C      -3.64753800   -0.06486700   -0.85469500
C      -2.71171000   -1.11323400   -0.30705400
C      -1.30471900   -0.57945800   -0.02831100
O      -1.09564400    0.59947000    0.14364600
C      -0.20102100   -1.62308100    0.04373100
C       1.13600500   -1.09256100    0.55873600
C       2.24199600   -2.15343600    0.56158300
C       3.58003300   -1.61959600    1.08061000
H      -5.25704600    0.31417500   -2.34836800
H      -3.54730700    0.92308700   -0.39486700
H      -2.66999700   -1.98851300   -0.96009400
H      -3.08670300   -1.47536700    0.66252700
H      -0.08994700   -2.03587500   -0.96922100
H      -0.55855100   -2.46320600    0.65377800
H       0.99949800   -0.69772300    1.57147300
H       1.43895500   -0.23784000   -0.05360000
H       1.92816100   -3.00755600    1.17437000
H       2.37482300   -2.54246300   -0.45550400
H       3.48826800   -1.25678900    2.10893500
H       3.93649500   -0.78624800    0.46760200
H       4.35064500   -2.39501600    1.06904100
""",
)

entry(
    index = 59,
    label = "TB22",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {6,D} {18,S}
6  C u0 p0 c0 {5,D} {7,S} {19,S}
7  C u0 p0 c0 {6,S} {8,D} {20,S}
8  C u0 p0 c0 {7,D} {21,S} {22,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 O u1 p2 c0 {8,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.91899,0.106437,-0.000279389,5.67783e-07,-4.26006e-10,-12026.7,15.2799], Tmin=(10,'K'), Tmax=(449.596,'K')),
            NASAPolynomial(coeffs=[1.28996,0.0787223,-4.61024e-05,1.30526e-08,-1.43495e-12,-11453.6,26.581], Tmin=(449.596,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-100.022,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (511.34,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 13, 'C=C': 2, 'C-O': 1, 'C-C': 5}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.81 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 23.38 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 20.97 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 7.80 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 8], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [7, 8], dihedral: [6, 7, 8, 9], rotor symmetry: 2, max scan energy: 57.12 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C      -3.44832400    0.95624800    1.51379100
C      -2.62481000    0.11831500    0.53196000
C      -1.92935200   -1.07447000    1.19745100
C      -1.09645500   -1.91648900    0.20754500
C      -0.45801300   -3.10767400    0.84284500
C       0.89471900   -3.34442700    0.89672100
C       1.48792900   -4.45701400    1.49844300
C       2.91784300   -4.65403800    1.52287300
O       3.47273200   -5.61287700    2.03931500
H      -2.81946600    1.36261800    2.31178100
H      -3.93056500    1.79817100    1.01021700
H      -4.23360100    0.35671800    1.98436000
H      -3.27388500   -0.24629400   -0.27324300
H      -1.87107900    0.75362100    0.05170000
H      -1.27580700   -0.71820700    2.00191800
H      -2.68101300   -1.71607400    1.67326200
H      -0.33244500   -1.28732100   -0.26127300
H      -1.76314100   -2.25493000   -0.59877400
H      -1.12503500   -3.83319500    1.30574400
H       1.55924400   -2.61402100    0.43527900
H       0.88031400   -5.22117200    1.97462400
H       3.51287100   -3.85579500    1.02739500
""",
)

entry(
    index = 60,
    label = "TB23",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {6,S} {9,S}
2  O u0 p2 c0 {3,S} {5,S}
3  O u0 p2 c0 {2,S} {14,S}
4  O u1 p2 c0 {7,S}
5  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
6  C u0 p0 c0 {1,S} {5,S} {7,D}
7  C u0 p0 c0 {4,S} {6,D} {8,S}
8  C u0 p0 c0 {7,S} {9,D} {12,S}
9  C u0 p0 c0 {1,S} {8,D} {13,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82976,0.0102416,0.000197133,-4.0304e-07,2.4613e-10,-27278.2,14.8115], Tmin=(10,'K'), Tmax=(546.139,'K')),
            NASAPolynomial(coeffs=[2.08126,0.0602108,-4.21802e-05,1.36829e-08,-1.66403e-12,-27641.4,17.1153], Tmin=(546.139,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-226.867,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 4, 'C=C': 2, 'O-O': 1, 'H-O': 1, 'C-C': 2, 'C-H': 4}
1D rotors:
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 22.28 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Inconsistent initial and final conformersInconsistent initial and final conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 12], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.23238400    1.97435300    0.30689900
C       0.44139500    0.92846000    0.33176000
C       0.04190900   -0.38774800   -0.12627400
C      -1.20902500   -0.90098800   -0.76688800
O      -1.94732600    0.10714500   -1.41949000
O      -2.63794500    0.87469400   -0.40380400
O       1.03940200   -1.26431600    0.07951600
C       2.09648900   -0.56961900    0.66169400
C       1.80766000    0.72723500    0.82977500
H      -1.83810900   -1.41371900   -0.02685900
H      -0.93778000   -1.62171700   -1.54608700
H      -1.94725400    1.53920300   -0.18592700
H       2.96015000   -1.17669900    0.87622500
H       2.43769400    1.49280900    1.25168300
""",
)

# entry(
#     index = 61,
#     label = "TB53",
#     molecule = 
# """
# 1  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
# 2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
# 3  C u0 p0 c0 {6,S} {7,S} {13,S} {14,S}
# 4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
# 5  C u0 p0 c0 {2,S} {6,D} {18,S}
# 6  C u0 p0 c0 {3,S} {5,D} {19,S}
# 7  C u0 p0 c0 {3,S} {8,D} {20,S}
# 8  C u0 p0 c0 {7,D} {21,D}
# 9  H u0 p0 c0 {1,S}
# 10 H u0 p0 c0 {1,S}
# 11 H u0 p0 c0 {2,S}
# 12 H u0 p0 c0 {2,S}
# 13 H u0 p0 c0 {3,S}
# 14 H u0 p0 c0 {3,S}
# 15 H u0 p0 c0 {4,S}
# 16 H u0 p0 c0 {4,S}
# 17 H u0 p0 c0 {4,S}
# 18 H u0 p0 c0 {5,S}
# 19 H u0 p0 c0 {6,S}
# 20 H u0 p0 c0 {7,S}
# 21 O u0 p2 c0 {8,D}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[2.81229,0.121556,-0.000401323,8.57693e-07,-6.58401e-10,-10037.3,14.9399], Tmin=(10,'K'), Tmax=(433.017,'K')),
#             NASAPolynomial(coeffs=[2.20639,0.0723967,-4.13564e-05,1.14689e-08,-1.23902e-12,-9471.5,23.2835], Tmin=(433.017,'K'), Tmax=(3000,'K')),
#         ],
#         Tmin = (10,'K'),
#         Tmax = (3000,'K'),
#         E0 = (-83.4828,'kJ/mol'),
#         Cp0 = (33.2579,'J/(mol*K)'),
#         CpInf = (494.711,'J/(mol*K)'),
#     ),
#     shortDesc = """""",
#     longDesc = 
# """
# Bond corrections: {'C-C': 5, 'C=O': 1, 'C=C': 2, 'C-H': 12}
# 1D rotors:
# * Invalidated! pivots: [2, 3], dihedral: [5, 2, 3, 6], invalidation reason: Another conformer for S0 exists which is 1.42 kJ/mol lower.Another conformer for S0 exists which is 1.42 kJ/mol lower.
# * Invalidated! pivots: [2, 5], dihedral: [3, 2, 5, 16], invalidation reason: 
# pivots: [3, 6], dihedral: [2, 3, 6, 7], rotor symmetry: 1, max scan energy: 9.62 kJ/mol
# pivots: [4, 7], dihedral: [8, 4, 7, 6], rotor symmetry: 1, max scan energy: 13.62 kJ/mol
# pivots: [4, 8], dihedral: [7, 4, 8, 9], rotor symmetry: 1, max scan energy: 9.69 kJ/mol


# External symmetry: 1, optical isomers: 2

# Geometry:
# O      -1.56772200    7.84688900   -0.51352700
# C      -2.78474700    0.22304000    0.49468600
# C      -2.06984200    0.86851200   -0.70662100
# C      -0.51745700    4.46125600   -0.35555900
# C      -3.61840200   -1.00086700    0.10644800
# C      -1.21483300    2.04357900   -0.32502400
# C      -1.37930300    3.29216900   -0.75849800
# C      -1.30953900    5.54558600    0.36125600
# C      -1.45066400    6.76449600   -0.09890000
# H      -2.03907100   -0.06378700    1.24563600
# H      -3.42510500    0.97353200    0.97089700
# H      -1.44291300    0.10561900   -1.18851700
# H      -2.81099700    1.17779000   -1.45197500
# H      -0.04258700    4.89457000   -1.24252700
# H       0.29410000    4.11334300    0.29259900
# H      -2.99382800   -1.77883500   -0.34370500
# H      -4.11525000   -1.43632800    0.97749400
# H      -4.39314400   -0.73757700   -0.62033600
# H      -0.40246400    1.83558800    0.37273100
# H      -2.19285700    3.51934600   -1.44602100
# H      -1.81373800    5.31571500    1.29242300
# """,
# )

entry(
    index = 62,
    label = "TB54",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {7,S} {8,S} {19,S} {20,S}
6  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
7  C u0 p0 c0 {1,S} {5,S} {21,D}
8  C u0 p1 c0 {4,S} {5,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49953,0.0628244,-1.51974e-05,-1.29409e-08,6.1702e-12,12861.4,13.1067], Tmin=(10,'K'), Tmax=(1199.68,'K')),
            NASAPolynomial(coeffs=[12.7812,0.0511934,-2.48064e-05,5.81991e-09,-5.36157e-13,9244.37,-39.1549], Tmin=(1199.68,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (106.951,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (494.711,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 8, 'C=O': 1, 'C-H': 12}
1D rotors:
pivots: [1, 2], dihedral: [4, 1, 2, 3], rotor symmetry: 1, max scan energy: 22.74 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 6], rotor symmetry: 1, max scan energy: 24.41 kJ/mol
pivots: [3, 6], dihedral: [2, 3, 6, 16], rotor symmetry: 3, max scan energy: 11.89 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.67987900   -0.30739000   -0.26936300
C       0.65413400   -0.25359700    0.47749700
C       1.85836000    0.06697500   -0.41541100
C      -1.27090200    1.02539600   -0.77824500
C      -3.10898000   -0.17500700    0.05724600
C       3.18040100    0.09169100    0.35679200
C      -1.83507400   -0.85416600    0.58329300
C      -2.76207600    1.07874500   -0.65164900
H      -0.58337500   -1.00203000   -1.11764500
H       1.91766200   -0.67851500   -1.21791000
H       1.70858000    1.03437400   -0.90895900
H       0.58296800    0.49221600    1.27976000
H       0.80603600   -1.21697900    0.97591100
H      -1.00872500    1.85127800   -0.08514600
H      -0.91525600    1.38156800   -1.74885900
H       3.37528900   -0.87281700    0.83519700
H       3.16531200    0.85293600    1.14281200
H       4.02314200    0.31289100   -0.30336500
H      -3.44893900   -0.77745800   -0.81238100
H      -3.96048300   -0.15116700    0.74049600
O      -1.75406800   -1.61681300    1.50955300
""",
)

entry(
    index = 63,
    label = "TB55",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u1 p0 c0 {1,S} {5,S} {10,S}
4  C u0 p0 c0 {2,D} {6,S} {11,S}
5  C u0 p0 c0 {3,S} {6,D} {12,S}
6  C u0 p0 c0 {4,S} {5,D} {13,S}
7  O u0 p2 c0 {2,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88647,0.0066235,0.000164267,-3.0733e-07,1.75737e-10,-263.568,10.1673], Tmin=(10,'K'), Tmax=(563.903,'K')),
            NASAPolynomial(coeffs=[0.366943,0.0571217,-3.79777e-05,1.20663e-08,-1.46172e-12,-272.585,21.5313], Tmin=(563.903,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-2.23891,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-C': 4, 'C-H': 6, 'H-O': 1, 'C-O': 1}
1D rotors:
pivots: [1, 3], dihedral: [14, 1, 3, 2], rotor symmetry: 2, max scan energy: 22.30 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       2.24038600    0.83277000   -0.58017900
C       0.85685000   -0.99603800    0.05691200
C       0.96616400    0.46050200   -0.27170200
C      -0.54589400   -1.41291600    0.39800100
C      -0.10372700    1.30643100   -0.25840300
C      -1.58598900   -0.53030900    0.39815400
C      -1.39898000    0.83443900    0.07501300
H       1.55171700   -1.22787500    0.88261800
H       1.25022200   -1.58287700   -0.79117700
H      -0.70771700   -2.45535800    0.64824600
H       0.03964700    2.35530100   -0.50668800
H      -2.58159200   -0.87957900    0.65156700
H      -2.23626900    1.52016100    0.08039400
H       2.25518000    1.77534600   -0.78275900
""",
)

entry(
    index = 64,
    label = "TB56",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {5,S} {9,S}
4  C u0 p0 c0 {2,S} {7,D} {8,S}
5  C u0 p0 c0 {3,S} {6,D} {10,S}
6  C u0 p0 c0 {1,S} {5,D} {11,S}
7  C u0 p0 c0 {4,D} {12,S} {13,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90648,0.00548257,0.000150941,-2.7934e-07,1.59271e-10,155.985,10.6063], Tmin=(10,'K'), Tmax=(555.209,'K')),
            NASAPolynomial(coeffs=[-0.071809,0.054474,-3.63433e-05,1.14936e-08,-1.38212e-12,284.399,24.6365], Tmin=(555.209,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (1.25832,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 3, 'C-C': 2, 'C-H': 6, 'C-O': 2}
1D rotors:
pivots: [2, 4], dihedral: [1, 2, 4, 7], rotor symmetry: 1, max scan energy: 30.92 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.58290800    0.62412500    0.74008500
C       0.13244400   -0.12723000   -0.15471400
C      -0.70256600   -1.03267200   -0.75382400
C       1.54400200    0.13538800   -0.31113500
C      -2.00223700   -0.82723100   -0.19740900
C      -1.87038000    0.18554400    0.69921700
C       2.24542700    1.06421500    0.34725800
H       2.03797700   -0.50215800   -1.03848400
H      -0.41801000   -1.75625200   -1.50137000
H      -2.90940000   -1.36036600   -0.43285000
H      -2.55803000    0.68891400    1.35753300
H       3.30511600    1.19410100    0.16780300
H       1.77856100    1.71362200    1.07788900
""",
)

entry(
    index = 65,
    label = "TB57",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {6,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {4,S} {19,D}
7  C u0 p0 c0 {1,S} {8,D} {20,S}
8  C u0 p0 c0 {4,S} {7,D} {21,S}
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
            NASAPolynomial(coeffs=[3.53569,0.0494059,2.98994e-05,-6.55852e-08,2.68042e-11,-21434.3,13.2464], Tmin=(10,'K'), Tmax=(917.478,'K')),
            NASAPolynomial(coeffs=[4.40053,0.0680688,-3.72894e-05,9.88655e-09,-1.02269e-12,-22537.2,4.00298], Tmin=(917.478,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-178.206,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 7, 'C=C': 1, 'C=O': 1, 'C-H': 12}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [6, 1, 2, 3], invalidation reason: Another conformer for S4 exists which is 0.69 kJ/mol lower.Another conformer for S4 exists which is 0.69 kJ/mol lower.
pivots: [2, 3], dihedral: [1, 2, 3, 5], rotor symmetry: 1, max scan energy: 25.28 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 16], rotor symmetry: 3, max scan energy: 11.95 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.61861600   -0.64365200   -0.12020900
C      -0.34040800   -1.15487200   -0.81263200
C       0.51276100   -0.04908700   -1.44338000
C      -2.93266600   -1.62484000    1.76917500
C       1.75913000   -0.59270400   -2.14803500
C      -2.55058300   -1.80167100    0.29326600
C      -1.43265400    0.10338400    1.17826000
C      -2.13113600   -0.42166900    2.18686500
H      -2.17025400   -0.02904400   -0.84780600
H      -0.09939700    0.50962200   -2.16170900
H       0.81714400    0.67114000   -0.67531600
H      -0.64739000   -1.87021600   -1.58288800
H       0.26023600   -1.71487400   -0.08564800
H      -2.70061900   -2.53707000    2.33020300
H      -4.01652900   -1.47826600    1.85523300
H       1.48786100   -1.29315500   -2.94364000
H       2.40938300   -1.12486900   -1.44694700
H       2.34511800    0.21285600   -2.59851700
O      -2.89810500   -2.70488000   -0.42299000
H      -0.79859100    0.97784600    1.26415000
H      -2.13902700   -0.03487700    3.19892400
""",
)

entry(
    index = 66,
    label = "TB58",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {6,S} {18,D}
6  C u0 p0 c0 {5,S} {8,D} {19,S}
7  C u0 p0 c0 {8,D} {20,S} {21,S}
8  C u0 p0 c0 {6,D} {7,D}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u0 p2 c0 {5,D}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.20748,0.0715284,-3.6313e-05,4.70158e-09,1.21691e-12,-8770.01,14.326], Tmin=(10,'K'), Tmax=(1209.62,'K')),
            NASAPolynomial(coeffs=[11.8595,0.0533224,-2.66391e-05,6.48107e-09,-6.20591e-13,-11624.3,-32.2081], Tmin=(1209.62,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-72.982,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (494.711,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 5, 'C=C': 2, 'C=O': 1, 'C-H': 12}
1D rotors:
pivots: [1, 2], dihedral: [3, 1, 2, 4], rotor symmetry: 1, max scan energy: 23.23 kJ/mol
* Invalidated! pivots: [1, 3], dihedral: [2, 1, 3, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 4], dihedral: [1, 2, 4, 15], rotor symmetry: 3, max scan energy: 11.92 kJ/mol
* Invalidated! pivots: [3, 5], dihedral: [1, 3, 5, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [5, 6], dihedral: [3, 5, 6, 8], rotor symmetry: 1, max scan energy: 28.10 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.21927800   -0.44968700    0.08145700
C      -1.96123600    0.88037900    0.26288200
C       0.29619800   -0.29812700   -0.07103600
C      -3.47225400    0.69915900    0.43015100
C       0.73100000    0.26643800   -1.41708600
C       2.16523900    0.64663300   -1.59835000
C       3.99950500    0.53661400    0.25542700
C       3.08614300    0.58971700   -0.66855300
H      -1.55671100    1.40228400    1.13949100
H      -1.76541400    1.52041700   -0.60227000
H      -1.42024700   -1.09496900    0.94432500
H      -1.61340100   -0.96485600   -0.79968000
H       0.79158600   -1.27211400    0.03212100
H       0.71552100    0.32365400    0.72784100
H      -3.70480900    0.07964500    1.30244100
H      -3.90900700    0.21296400   -0.44742200
H      -3.97660600    1.66028600    0.56180500
O      -0.03610800    0.39393400   -2.34976900
H       2.41420100    0.99367800   -2.59774000
H       4.19574700    1.38533900    0.90356000
H       4.59699000   -0.35721800    0.40687000
""",
)

entry(
    index = 67,
    label = "TB59",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {6,D}
3  C u0 p0 c0 {2,S} {4,D} {8,S}
4  C u0 p0 c0 {3,D} {5,S} {7,S}
5  C u1 p0 c0 {1,S} {4,S} {9,S}
6  C u0 p0 c0 {2,D} {10,S} {11,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.15367,-0.0147633,0.000219242,-3.93132e-07,2.2561e-10,6062.05,10.4373], Tmin=(10,'K'), Tmax=(562.999,'K')),
            NASAPolynomial(coeffs=[0.720755,0.0439786,-2.87873e-05,8.94417e-09,-1.05632e-12,5904.18,20.192], Tmin=(562.999,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (50.3798,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-C': 2, 'C-H': 5, 'C-O': 2}
1D rotors:
* Invalidated! pivots: [2, 6], dihedral: [1, 2, 6, 10], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.00249000   -1.25182500   -0.12389800
C       0.65952600   -0.04063300    0.02432300
C      -0.31143900    0.97843100    0.08337200
C      -1.57102500    0.35784900   -0.03212400
C      -1.33522400   -0.98634100   -0.15491500
C       2.03195800   -0.03171200    0.08418200
H      -2.53954700    0.83272300   -0.02678400
H      -0.10246700    2.03019500    0.19635900
H      -1.98338900   -1.83927700   -0.26711400
H       2.56088400    0.90307200    0.19935100
H       2.59321100   -0.95248000    0.01724800
""",
)

entry(
    index = 68,
    label = "TB60",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {2,S} {6,D} {12,S}
5  C u0 p0 c0 {3,D} {6,S} {14,S}
6  C u0 p0 c0 {4,D} {5,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 O u1 p2 c0 {6,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95107,0.00309872,0.00016394,-3.0522e-07,1.84088e-10,3188.48,12.0371], Tmin=(10,'K'), Tmax=(428.415,'K')),
            NASAPolynomial(coeffs=[-2.27425,0.0612835,-3.99935e-05,1.24546e-08,-1.48239e-12,3721.33,36.7872], Tmin=(428.415,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (26.4985,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-O': 1, 'C-C': 4, 'C-H': 7}

External symmetry: 1, optical isomers: 2

Geometry:
C      -1.26587800   -0.37782700    0.21779100
C      -0.83265100    0.90020600   -0.52490000
C      -0.15936600   -1.39374400    0.31558000
C       0.56474600    1.31239700   -0.20720700
C       1.13595300   -1.06142000    0.26582900
C       1.58365900    0.34714800    0.11837400
H      -2.14012300   -0.81643700   -0.27164100
H      -1.59078400   -0.12192200    1.23588900
H      -0.89044300    0.71146500   -1.61086200
H      -1.53401400    1.71772900   -0.33340200
H      -0.44616800   -2.42930500    0.47754600
H       0.88303800    2.34247800   -0.32556300
O       2.76899600    0.66822600    0.26519100
H       1.92303400   -1.79899400    0.37737500
""",
)

entry(
    index = 69,
    label = "TB61",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {2,S} {18,D}
7  C u0 p0 c0 {2,S} {8,D} {19,S}
8  C u0 p0 c0 {7,D} {20,S} {21,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 O u0 p2 c0 {6,D}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.19115,0.0817229,-0.000145296,3.11842e-07,-2.6759e-10,-1424.94,14.1974], Tmin=(10,'K'), Tmax=(412.107,'K')),
            NASAPolynomial(coeffs=[1.00199,0.079045,-4.846e-05,1.43079e-08,-1.62946e-12,-1041.33,25.2833], Tmin=(412.107,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-11.8679,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (494.711,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 7, 'C=C': 1, 'C=O': 1, 'C-H': 12}
1D rotors:
pivots: [1, 3], dihedral: [2, 1, 3, 4], rotor symmetry: 1, max scan energy: 15.59 kJ/mol
* Invalidated! pivots: [2, 7], dihedral: [1, 2, 7, 8], invalidation reason: Another conformer for S14 exists which is 3.40 kJ/mol lower.Another conformer for S14 exists which is 3.40 kJ/mol lower.
pivots: [3, 4], dihedral: [1, 3, 4, 5], rotor symmetry: 1, max scan energy: 18.82 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 15], rotor symmetry: 3, max scan energy: 12.21 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.19290400   -0.77433200    0.16390700
C       1.39169500   -0.80323900    0.02899200
C      -1.07394400   -1.20705900   -0.99848600
C      -2.50265600   -1.58726600   -0.57488600
C      -2.58390800   -2.85773200    0.27728400
C       0.63116500   -1.69839800    0.94290500
C       2.21253100    0.31811400    0.52994900
C       3.33646800    0.75307100   -0.03726100
H      -0.56383000    0.08664700    0.72081600
H       1.74884600   -1.27654400   -0.88425100
H      -2.94932700   -0.74616800   -0.03126500
H      -3.10569700   -1.71624300   -1.48038300
H      -1.11008700   -0.38778400   -1.72540300
H      -0.60795700   -2.05775500   -1.50962100
H      -1.99391000   -2.77523900    1.19307500
H      -2.20691900   -3.72368500   -0.27620000
H      -3.61784800   -3.07148200    0.56055600
O       0.68541300   -2.57058900    1.76000600
H       1.85389300    0.80089600    1.43709300
H       3.89786100    1.57737400    0.38600200
H       3.73559700    0.29787000   -0.93788900
""",
)

entry(
    index = 70,
    label = "TB62",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {3,D} {4,S} {7,S}
3  C u0 p0 c0 {1,S} {2,D} {11,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {6,S} {12,S}
6  C u1 p0 c0 {5,S} {7,S} {14,S}
7  O u0 p2 c0 {2,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92067,0.00482691,0.000160772,-3.02286e-07,1.79e-10,1771.21,12.3455], Tmin=(10,'K'), Tmax=(514.419,'K')),
            NASAPolynomial(coeffs=[-0.89299,0.0574495,-3.69714e-05,1.13927e-08,-1.34487e-12,2065.43,30.4151], Tmin=(514.419,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (14.6991,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-O': 2, 'C-C': 3, 'C-H': 7}
1D rotors:
pivots: [1, 3], dihedral: [8, 1, 3, 2], rotor symmetry: 3, max scan energy: 2.17 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [4, 2, 3, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
C      -2.35141900   -0.54631800   -0.32449100
C      -0.91708300    1.42998000   -1.05056200
C      -1.26214200    0.45764500   -0.13462500
C       0.06277200    2.44019100   -1.03953700
C      -0.04973600    3.14064000   -2.25876600
C      -1.06816400    2.55158100   -2.95782300
O      -1.60736800    1.51839500   -2.25188800
H      -1.96198700   -1.57095800   -0.27626300
H      -2.84876700   -0.41827900   -1.28602000
H      -3.10963000   -0.46588400    0.46450600
H      -0.68798600    0.43757000    0.78484200
H       0.54323800    3.97866300   -2.59025500
H       0.75820900    2.62393200   -0.23622900
H      -1.50741600    2.74207000   -3.92250900
""",
)

entry(
    index = 71,
    label = "TB63",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {4,D} {6,S}
4  C u0 p0 c0 {3,D} {5,S} {13,S}
5  C u0 p0 c0 {4,S} {7,D} {14,S}
6  O u0 p2 c0 {3,S} {7,S}
7  C u1 p0 c0 {5,D} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82822,0.024406,4.24631e-05,-6.98504e-08,2.84078e-11,19873.9,12.8537], Tmin=(10,'K'), Tmax=(873.011,'K')),
            NASAPolynomial(coeffs=[3.58434,0.0446198,-2.50796e-05,6.78402e-09,-7.12818e-13,19188.7,9.82929], Tmin=(873.011,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (165.275,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-O': 2, 'C-C': 3, 'C-H': 7}
1D rotors:
pivots: [1, 2], dihedral: [3, 1, 2, 10], rotor symmetry: 3, max scan energy: 12.40 kJ/mol
pivots: [1, 3], dihedral: [2, 1, 3, 4], rotor symmetry: 1, max scan energy: 8.43 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.00625100   -0.26041800   -0.63542100
C      -2.12549700    0.18517500    0.32080000
C       0.36211700   -0.12302800   -0.06670700
C       1.45633700    0.62414200   -0.37287100
C       2.49509500    0.30461100    0.58211700
O       0.65739400   -0.90803800    1.04771100
C       1.91194700   -0.61672300    1.38158100
H      -1.17315500   -1.30311200   -0.93054800
H      -1.03746700    0.33210200   -1.55449300
H      -2.01517800    1.23945600    0.58617400
H      -2.10232600   -0.39926000    1.24295000
H      -3.10562200    0.04875700   -0.14336000
H       1.53273500    1.32896500   -1.18695800
H       3.49298200    0.70289500    0.64353200
""",
)

entry(
    index = 72,
    label = "TB64",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {6,D} {17,S}
5  C u0 p0 c0 {3,S} {7,D} {18,S}
6  C u0 p0 c0 {4,D} {8,S} {20,S}
7  C u0 p0 c0 {5,D} {8,S} {21,S}
8  C u0 p0 c0 {6,S} {7,S} {19,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 O u0 p2 c0 {8,D}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.06023,0.0871443,-0.000146046,2.42208e-07,-1.66667e-10,-15232.4,13.9772], Tmin=(10,'K'), Tmax=(482.742,'K')),
            NASAPolynomial(coeffs=[1.92879,0.0755891,-4.51052e-05,1.29944e-08,-1.45002e-12,-14879.2,21.1377], Tmin=(482.742,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-126.686,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (490.554,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 5, 'C=C': 2, 'C=O': 1, 'C-H': 12}
1D rotors:
pivots: [1, 2], dihedral: [4, 1, 2, 11], rotor symmetry: 3, max scan energy: 12.15 kJ/mol
* Invalidated! pivots: [1, 4], dihedral: [2, 1, 4, 6], invalidation reason: Another conformer for S20 exists which is 1.03 kJ/mol lower.Another conformer for S20 exists which is 1.03 kJ/mol lower.
pivots: [3, 5], dihedral: [14, 3, 5, 7], rotor symmetry: 3, max scan energy: 7.77 kJ/mol
pivots: [6, 8], dihedral: [4, 6, 8, 7], rotor symmetry: 1, max scan energy: 30.55 kJ/mol
pivots: [7, 8], dihedral: [5, 7, 8, 6], rotor symmetry: 1, max scan energy: 30.90 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -3.63298100    0.36744700   -0.33930000
C      -3.23101000    0.35730100   -1.82487200
C       0.99657200   -1.60212800    5.31366600
C      -2.46898700    0.61358300    0.56822400
C       0.54329100   -0.66761900    4.24080300
C      -2.04187400   -0.20309800    1.53677400
C      -0.49550000   -0.86184700    3.42225500
C      -0.86385000    0.13762900    2.38174000
H      -4.12391600   -0.57433700   -0.07554400
H      -4.37165100    1.16461400   -0.18257500
H      -2.75610900    1.29975300   -2.11116600
H      -2.52420300   -0.44976700   -2.03304400
H      -4.10744100    0.21531900   -2.46210400
H       0.98025700   -1.10518800    6.29035000
H       2.03449500   -1.91028100    5.14369500
H       0.37449100   -2.49775000    5.37055600
H      -1.91105400    1.53764000    0.42254700
H       1.10464600    0.25531000    4.10889000
O      -0.23638300    1.17578500    2.22981100
H      -2.55103200   -1.14334500    1.73284600
H      -1.10056300   -1.76171600    3.49793800
""",
)				

entry(
    index = 73,
    label = "TB65",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {6,D} {9,S}
6  C u0 p0 c0 {2,S} {5,D} {19,S}
7  C u0 p0 c0 {3,S} {8,D} {20,S}
8  C u0 p0 c0 {7,D} {9,S} {21,S}
9  O u0 p2 c0 {5,S} {8,S}
10 H u0 p0 c0 {1,S}
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
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75358,0.0445874,3.77079e-05,-6.67654e-08,2.47581e-11,-12094,13.8742], Tmin=(10,'K'), Tmax=(1013.42,'K')),
            NASAPolynomial(coeffs=[6.4963,0.0631035,-3.31283e-05,8.40331e-09,-8.33143e-13,-14156.6,-6.82823], Tmin=(1013.42,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-100.467,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 12, 'C-C': 5, 'C=C': 2, 'C-O': 2}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [4, 1, 2, 6], invalidation reason: Another conformer for S1 exists which is 1.09 kJ/mol lower.Another conformer for S1 exists which is 1.09 kJ/mol lower.
pivots: [1, 4], dihedral: [2, 1, 4, 16], rotor symmetry: 3, max scan energy: 11.72 kJ/mol
pivots: [2, 6], dihedral: [1, 2, 6, 5], rotor symmetry: 1, max scan energy: 13.83 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -3.05253400   -0.03204500   -0.24159500
C      -2.14254100    0.50940000   -1.36043000
C      -0.74153500    3.37917100   -1.45219800
C      -2.52137700   -1.32129500    0.39028900
C      -2.07480300    2.93068100   -2.03183300
C      -2.68260500    1.74713000   -2.01741700
C      -0.71773300    4.83667700   -1.85034600
C      -1.83363100    5.09962600   -2.52198600
O      -2.67698900    4.02245100   -2.66792400
H      -4.05425000   -0.20795100   -0.65041900
H      -3.16930800    0.74013800    0.52662100
H      -1.14420500    0.69834000   -0.95127000
H      -2.01631200   -0.27946300   -2.11519700
H      -0.70129500    3.23709900   -0.36586400
H       0.09690200    2.81343000   -1.87556100
H      -3.18803500   -1.68320000    1.17762800
H      -1.53409300   -1.16652400    0.83711300
H      -2.42491600   -2.11704700   -0.35509500
H      -3.64789500    1.67663000   -2.51097000
H       0.07161600    5.53697000   -1.62737700
H      -2.19397500    6.01148500   -2.97358000
""",
)	

entry(
    index = 74,
    label = "TB30",
    molecule = 
"""
1  C u0 p0 c0 {6,S} {7,S} {8,S} {13,S}
2  C u0 p0 c0 {3,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {4,S} {7,D}
7  C u0 p0 c0 {1,S} {6,D} {19,S}
8  C u0 p0 c0 {1,S} {20,D} {21,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
20 O u0 p2 c0 {8,D}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.99362,0.0956208,-0.000201529,3.68841e-07,-2.63468e-10,1683.55,13.5773], Tmin=(10,'K'), Tmax=(465.257,'K')),
            NASAPolynomial(coeffs=[1.99788,0.0756533,-4.51772e-05,1.30115e-08,-1.45092e-12,2084.97,20.9375], Tmin=(465.257,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (13.9662,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (490.554,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-H': 12, 'C-C': 7, 'C=C': 1}
1D rotors:
pivots: [2, 9], dihedral: [7, 2, 9, 1], rotor symmetry: 1, max scan energy: 33.82 kJ/mol
pivots: [3, 4], dihedral: [5, 3, 4, 6], rotor symmetry: 1, max scan energy: 23.21 kJ/mol
pivots: [3, 5], dihedral: [4, 3, 5, 7], rotor symmetry: 1, max scan energy: 20.88 kJ/mol
pivots: [4, 6], dihedral: [3, 4, 6, 17], rotor symmetry: 3, max scan energy: 11.87 kJ/mol
* Invalidated! pivots: [5, 7], dihedral: [3, 5, 7, 2], invalidation reason: Another conformer for C8H12O[26] exists which is 0.95 kJ/mol lower.Another conformer for C8H12O[26] exists which is 0.95 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
O      -3.42632100   -3.47808200   -0.85517200
C      -1.08179100   -3.38222100   -0.39783500
C       1.98021900   -0.75362500   -0.71732600
C       2.44766800    0.65436800   -0.33305000
C       0.56220400   -1.06919100   -0.22191200
C       3.86185300    0.97166500   -0.82656000
C       0.09486800   -2.42500900   -0.58190300
C       0.25294600   -3.59052900   -1.10227000
C      -2.30865500   -3.19184700   -1.21130600
H       2.40799800    0.76352900    0.75744800
H       1.74488900    1.39201900   -0.73875300
H       2.67544100   -1.49609300   -0.30927100
H       2.01217700   -0.86679600   -1.80694800
H      -1.26659800   -3.83467600    0.57786400
H       0.50677900   -0.96770700    0.86993200
H      -0.15306200   -0.33640800   -0.61651100
H       3.92457500    0.90499500   -1.91701100
H       4.59267700    0.27199700   -0.40961700
H       4.16640900    1.98090600   -0.53775100
H       0.84191400   -4.32877600   -1.61672800
H      -2.11525800   -2.74887700   -2.21844000
""",
)
				
entry(
    index = 75,
    label = "TB33",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {6,S} {7,D}
6  C u0 p0 c0 {5,S} {8,D} {19,S}
7  C u0 p0 c0 {5,D} {9,S} {20,S}
8  C u0 p0 c0 {6,D} {9,S} {21,S}
9  O u0 p2 c0 {7,S} {8,S}
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
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.27943,0.078137,-0.000216992,6.08098e-07,-5.75663e-10,-19224,14.4345], Tmin=(10,'K'), Tmax=(393.851,'K')),
            NASAPolynomial(coeffs=[-1.89358,0.0824705,-4.99089e-05,1.45232e-08,-1.63146e-12,-18442.6,39.3175], Tmin=(393.851,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-159.865,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (494.711,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-H': 12, 'C-C': 5, 'C=C': 2}
1D rotors:
pivots: [2, 3], dihedral: [4, 2, 3, 5], rotor symmetry: 1, max scan energy: 23.68 kJ/mol
* Invalidated! pivots: [2, 4], dihedral: [3, 2, 4, 6], invalidation reason: Another conformer for C8H12O[45] exists which is 1.13 kJ/mol lower.Another conformer for C8H12O[45] exists which is 1.13 kJ/mol lower.
pivots: [3, 5], dihedral: [2, 3, 5, 16], rotor symmetry: 3, max scan energy: 11.82 kJ/mol
pivots: [4, 6], dihedral: [2, 4, 6, 7], rotor symmetry: 1, max scan energy: 6.95 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.12452100    3.42972800   -3.27883000
C       1.18882400    1.11012500   -0.03534700
C       1.65379600    0.74358400    1.37800400
C      -0.12942600    1.90543300   -0.05231000
C       2.96606200   -0.04539700    1.39551300
C      -0.60471000    2.25798500   -1.43210800
C      -1.09600600    1.35839300   -2.44482600
C      -0.64730200    3.49279900   -2.00142300
C      -1.39216100    2.11899300   -3.52866800
H       0.86991200    0.16027300    1.87646900
H       1.77126500    1.66044000    1.96855600
H       1.06833000    0.19540700   -0.62803000
H       1.96516600    1.69808300   -0.53877800
H      -0.00297400    2.82424700    0.53058000
H      -0.90369400    1.32241100    0.46144100
H       3.77731900    0.52652500    0.93459100
H       3.27114500   -0.29064200    2.41643400
H       2.86987900   -0.98515900    0.84284900
H      -1.21416300    0.28882000   -2.36330200
H      -0.38959800    4.47622000   -1.64491000
H      -1.78445500    1.89785500   -4.50693400
""",
)	

entry(
    index = 76,
    label = "TB31",
    molecule = 
"""
1  O u0 p2 c0 {7,S} {9,S}
2  O u0 p2 c0 {9,S} {22,S}
3  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {7,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {17,S} {18,S} {19,S}
7  C u0 p0 c0 {1,S} {5,S} {8,D}
8  C u0 p0 c0 {7,D} {10,S} {21,S}
9  C u0 p0 c0 {1,S} {2,S} {10,D}
10 C u0 p0 c0 {8,S} {9,D} {20,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.05271,0.0940583,-0.000188038,3.70385e-07,-2.89334e-10,-41896.1,15.157], Tmin=(10,'K'), Tmax=(431.371,'K')),
            NASAPolynomial(coeffs=[1.76726,0.0799,-4.81247e-05,1.40106e-08,-1.57843e-12,-41542.6,23.0901], Tmin=(431.371,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-348.37,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (515.497,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-O': 3, 'C-H': 11, 'C-C': 5, 'C=C': 2}
1D rotors:
pivots: [2, 9], dihedral: [22, 2, 9, 1], rotor symmetry: 1, max scan energy: 8.38 kJ/mol
pivots: [3, 4], dihedral: [5, 3, 4, 6], rotor symmetry: 1, max scan energy: 23.67 kJ/mol
* Invalidated! pivots: [3, 5], dihedral: [4, 3, 5, 7], invalidation reason: Another conformer for C8H12O2[69] exists which is 0.91 kJ/mol lower.Another conformer for C8H12O2[69] exists which is 0.91 kJ/mol lower.
pivots: [4, 6], dihedral: [3, 4, 6, 17], rotor symmetry: 3, max scan energy: 11.89 kJ/mol
pivots: [5, 7], dihedral: [3, 5, 7, 1], rotor symmetry: 1, max scan energy: 10.40 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.12762100    2.00670200   -3.04456100
O       1.34430200    3.71126000   -3.99092200
C      -1.31843900    0.57733000   -0.70288800
C      -2.54176600   -0.14277600   -0.12651300
C      -0.85432700   -0.00752200   -2.05107100
C      -3.00631000    0.43779400    1.21205700
C       0.31937500    0.68467100   -2.64754100
C       1.60406300    0.33795900   -2.90902000
C       1.30926400    2.44333400   -3.54533600
C       2.26013100    1.47824500   -3.49655100
H      -0.48812500    0.52699800    0.01089300
H      -1.54746900    1.64050500   -0.83561800
H      -2.30961600   -1.20760200   -0.00172200
H      -3.36398100   -0.09425800   -0.85088400
H      -0.58533800   -1.06082400   -1.92341900
H      -1.69382300    0.01491900   -2.75845900
H      -3.27783500    1.49323300    1.11172200
H      -3.88027500   -0.09484900    1.59666300
H      -2.21720900    0.37062300    1.96732600
H       3.27926700    1.56605100   -3.83192500
H       2.04636300   -0.62611000   -2.71074100
H       0.46700400    4.09498800   -3.87748500
""",
)
				
entry(
    index = 77,
    label = "TB39",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {2,S} {13,D}
5  C u0 p0 c0 {1,S} {6,D} {15,S}
6  C u0 p0 c0 {3,S} {5,D} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60395,0.0362273,1.79504e-05,-4.73248e-08,2.12349e-11,4636.88,12.0882], Tmin=(10,'K'), Tmax=(830.649,'K')),
            NASAPolynomial(coeffs=[3.65572,0.0486661,-2.74243e-05,7.48126e-09,-7.94578e-13,4190.55,9.21322], Tmin=(830.649,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (38.5272,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (353.365,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C-H': 8, 'C=O': 1, 'C-C': 5}
1D rotors:
* Invalidated! pivots: [2, 6], dihedral: [3, 2, 6, 7], invalidation reason: Another conformer for C6H8O[84] exists which is 1.55 kJ/mol lower.Another conformer for C6H8O[84] exists which is 1.55 kJ/mol lower.
pivots: [4, 7], dihedral: [11, 4, 7, 6], rotor symmetry: 3, max scan energy: 7.86 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       3.56335700   -1.09472400   -0.92224900
C       1.55991500   -2.61019700   -1.46371000
C       2.08721700   -1.96972800   -2.81762800
C      -1.87203000   -2.54001000    0.38233400
C       2.72976600   -1.69920700   -1.52870700
C       0.27617800   -2.17486100   -0.87283300
C      -0.57710600   -2.97715000   -0.23474000
H       1.78987400   -3.66813500   -1.35989400
H       2.56036000   -2.64421800   -3.52415000
H       1.48763200   -1.18442300   -3.26993200
H      -2.04528900   -1.47089200    0.23885200
H      -1.88472000   -2.74377300    1.45893800
H      -2.71973900   -3.08355000   -0.04970000
H      -0.33046800   -4.03369900   -0.13996400
H       0.04025200   -1.11562500   -0.96760000
""",
)

entry(
    index = 78,
    label = "TB29_a",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {6,D} {14,S}
5  C u0 p0 c0 {2,S} {6,S} {13,D}
6  C u0 p0 c0 {4,D} {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {5,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92519,0.00467245,0.000175137,-3.34886e-07,2.04135e-10,-16999.3,12.1834], Tmin=(10,'K'), Tmax=(487.524,'K')),
            NASAPolynomial(coeffs=[-1.42248,0.0613947,-3.89085e-05,1.18586e-08,-1.38981e-12,-16630.6,32.5753], Tmin=(487.524,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-141.362,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (353.365,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C-H': 8, 'C=O': 1, 'C-C': 5}
1D rotors:
pivots: [2, 4], dihedral: [3, 2, 4, 11], rotor symmetry: 3, max scan energy: 14.50 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       2.91909600   -0.40510800    0.71429400
C      -0.47948100   -0.02950500   -0.51822100
C       0.72680300   -0.95309400   -0.23747100
C      -1.80124300   -0.49955700    0.10820100
C      -0.02347600    1.31004700    0.02026800
C       1.80697200   -0.05792900    0.38943500
C       1.21855600    1.29719900    0.51536700
H      -0.63692400    0.06927200   -1.59998200
H       0.48127500   -1.75106600    0.46922700
H       1.12675100   -1.43298700   -1.13354600
H      -1.69842200   -0.61612100    1.19100500
H      -2.10697000   -1.46233800   -0.30937100
H      -2.60582200    0.21742700   -0.07933200
H      -0.67376900    2.17868100   -0.00872100
H       1.75922000    2.12765400    0.95006300
""",
)        		

entry(
    index = 78,
    label = "TB34",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {4,D} {7,S}
4  C u0 p0 c0 {3,D} {5,S} {14,S}
5  C u0 p0 c0 {4,S} {6,D} {13,S}
6  C u0 p0 c0 {5,D} {7,S} {15,S}
7  O u0 p2 c0 {3,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93844,0.00428393,0.000189969,-4.08044e-07,2.89678e-10,-14255.8,13.4545], Tmin=(10,'K'), Tmax=(359.879,'K')),
            NASAPolynomial(coeffs=[-0.9405,0.0585141,-3.60726e-05,1.07033e-08,-1.22426e-12,-13904.6,32.0062], Tmin=(359.879,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-118.531,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (349.208,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-H': 8, 'C-C': 3, 'C-O': 2}
1D rotors:
pivots: [2, 3], dihedral: [4, 2, 3, 10], rotor symmetry: 3, max scan energy: 12.46 kJ/mol
pivots: [2, 4], dihedral: [3, 2, 4, 1], rotor symmetry: 1, max scan energy: 7.69 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.74012500   -0.85248900    0.71554100
C      -1.31102400   -0.28522400   -0.47075000
C      -2.10379600    0.28852900    0.71615400
C       0.16680700   -0.16160700   -0.31887900
C       1.12999800    0.52062800   -0.99743500
C       2.37660400    0.23534600   -0.34646800
C       2.08106100   -0.59832100    0.68139700
H      -1.57165200   -1.34204800   -0.60297900
H      -1.59546600    0.22500600   -1.39495500
H      -1.90514500    1.35628900    0.83802200
H      -1.82692800   -0.21410400    1.64520500
H      -3.17804400    0.15516600    0.56394500
H       3.35473100    0.60321400   -0.61291500
H       0.97333000    1.15019200   -1.85921500
H       2.66939800   -1.08059000    1.44334000
""",
)       

entry(
    index = 79,
    label = "TB44",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {6,D}
4  C u0 p0 c0 {2,S} {5,D} {12,S}
5  C u0 p0 c0 {3,S} {4,D} {15,S}
6  C u0 p0 c0 {3,D} {7,S} {14,S}
7  C u0 p0 c0 {6,S} {8,D} {13,S}
8  C u0 p0 c0 {1,S} {7,D} {16,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69265,0.0296146,6.76626e-05,-1.27696e-07,6.23248e-11,-4330,11.5208], Tmin=(10,'K'), Tmax=(703.817,'K')),
            NASAPolynomial(coeffs=[2.42366,0.0571329,-3.42626e-05,9.84248e-09,-1.09039e-12,-4654.31,13.6243], Tmin=(703.817,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-36.0287,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (374.151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 3, 'C-H': 8, 'C-C': 3, 'C-O': 2}
1D rotors:
pivots: [2, 4], dihedral: [9, 2, 4, 5], rotor symmetry: 3, max scan energy: 7.70 kJ/mol
pivots: [3, 5], dihedral: [1, 3, 5, 4], rotor symmetry: 1, max scan energy: 28.33 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       1.27931800    0.50156400   -0.68779400
C      -3.08188900    0.31594600   -0.24328100
C       0.56872500    1.60610500   -0.29687500
C      -1.59408900    0.39811200   -0.38963500
C      -0.86568900    1.49906100   -0.16358200
C       1.43153600    2.65172600   -0.10165600
C       2.74434500    2.16374500   -0.38810300
C       2.59314600    0.85975300   -0.73686900
H      -3.55678300    0.02613300   -1.18787500
H      -3.51087700    1.26973300    0.07326000
H      -3.36542500   -0.44552000    0.49261900
H      -1.08118800   -0.50772400   -0.70227400
H       3.67267200    2.71031200   -0.34041000
H       1.15754500    3.64756200    0.20903800
H      -1.35762400    2.41636700    0.14988800
H       3.27922100    0.08434900   -1.03261900
""",
)

entry(
    index = 80,
    label = "TB37",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {1,S} {8,D} {14,S}
5  C u0 p0 c0 {3,D} {6,S} {16,S}
6  C u0 p0 c0 {5,S} {7,D} {15,S}
7  C u0 p0 c0 {6,D} {9,S} {17,S}
8  C u0 p0 c0 {4,D} {18,S} {19,S}
9  O u0 p2 c0 {3,S} {7,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72449,0.0421678,3.40852e-05,-6.53735e-08,2.55863e-11,-5196.89,14.0787], Tmin=(10,'K'), Tmax=(963.162,'K')),
            NASAPolynomial(coeffs=[6.16395,0.0581833,-3.15767e-05,8.26021e-09,-8.41854e-13,-6879.59,-3.89458], Tmin=(963.162,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-43.143,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-H': 10, 'C-C': 4, 'C=C': 3}
1D rotors:
pivots: [2, 3], dihedral: [4, 2, 3, 11], rotor symmetry: 3, max scan energy: 12.99 kJ/mol
pivots: [2, 4], dihedral: [3, 2, 4, 1], rotor symmetry: 1, max scan energy: 8.88 kJ/mol
* Invalidated! pivots: [2, 5], dihedral: [3, 2, 5, 9], invalidation reason: Another conformer for C8H10O[144] exists which is 1.75 kJ/mol lower.Another conformer for C8H10O[144] exists which is 1.75 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
O       0.96903800   -0.36593500    1.27299800
C      -0.68345800   -0.24773200   -0.52712700
C      -1.14836000   -1.71150100   -0.35752500
C       0.72173800   -0.05759400   -0.03806800
C      -1.63441800    0.70481800    0.16689100
C       1.86773500    0.38092100   -0.62668100
C       2.88989500    0.34178000    0.37967800
C       2.29107700   -0.11557800    1.50695300
C      -2.39337000    1.60392400   -0.45014300
H      -0.67409000   -0.00492100   -1.59443200
H      -1.15649600   -1.99384900    0.69768300
H      -2.15811900   -1.83698800   -0.75480300
H      -0.47639700   -2.39292400   -0.88536800
H      -1.67768400    0.61197000    1.25012100
H       3.92677300    0.61783800    0.27148300
H       1.97322700    0.69764700   -1.65227600
H       2.63577800   -0.31413900    2.50740600
H      -2.37061100    1.72567300   -1.52925800
H      -3.06484000    2.25403100    0.09938100
""",
)

entry(
    index = 81,
    label = "TB50",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {7,D} {9,S}
4  C u0 p0 c0 {6,S} {8,D} {9,S}
5  C u0 p0 c0 {2,S} {6,D} {16,S}
6  C u0 p0 c0 {4,S} {5,D} {17,S}
7  C u0 p0 c0 {3,D} {8,S} {18,S}
8  C u0 p0 c0 {4,D} {7,S} {19,S}
9  O u0 p2 c0 {3,S} {4,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53344,0.0526626,2.24797e-07,-2.84297e-08,1.20358e-11,-10354.9,12.1275], Tmin=(10,'K'), Tmax=(1038.04,'K')),
            NASAPolynomial(coeffs=[8.08408,0.0537795,-2.83425e-05,7.2277e-09,-7.2093e-13,-12304.5,-14.837], Tmin=(1038.04,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-86.0798,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (444.824,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-H': 10, 'C-C': 4, 'C=C': 3}
1D rotors:
pivots: [2, 4], dihedral: [10, 2, 4, 1], rotor symmetry: 3, max scan energy: 4.43 kJ/mol
pivots: [3, 6], dihedral: [13, 3, 6, 7], rotor symmetry: 3, max scan energy: 7.62 kJ/mol
pivots: [5, 7], dihedral: [1, 5, 7, 6], rotor symmetry: 1, max scan energy: 29.49 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       0.77119400   -0.02883100    0.29184700
C       2.90197900   -1.01554800   -0.33264100
C      -3.57210000    0.50788800    0.66945600
C       2.13520500    0.06826700    0.33455800
C       0.25104200    1.05487000    0.95603900
C      -2.08883300    0.33996400    0.54983200
C      -1.18275300    1.18832900    1.05414700
C       2.49214500    1.19352300    1.01353500
C       1.27829100    1.83254000    1.41598700
H       2.66054900   -1.07512500   -1.39874300
H       3.97227000   -0.83025400   -0.23288100
H       2.67852200   -1.99139000    0.11031800
H      -3.83321600    1.41352300    1.22244600
H      -4.02783500   -0.34675500    1.18318400
H      -4.04571000    0.56455500   -0.31771600
H      -1.73594100   -0.53687500    0.01323300
H      -1.51476200    2.07153800    1.59436500
H       3.50059400    1.52603600    1.20341900
H       1.17524400    2.74985200    1.97418400
""",
)

entry(
    index = 82,
    label = "TB48",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {2,S} {13,D}
5  C u0 p0 c0 {1,S} {6,D} {15,S}
6  C u0 p0 c0 {2,S} {5,D} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92582,0.00486948,0.000185279,-3.77579e-07,2.47801e-10,-15190.1,12.2195], Tmin=(10,'K'), Tmax=(447.878,'K')),
            NASAPolynomial(coeffs=[-0.934169,0.0598026,-3.73096e-05,1.12149e-08,-1.29943e-12,-14870.4,30.4716], Tmin=(447.878,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-126.309,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (353.365,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 1, 'C-H': 8, 'C=O': 1, 'C-C': 5}
1D rotors:
pivots: [2, 4], dihedral: [5, 2, 4, 11], rotor symmetry: 3, max scan energy: 11.11 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.06775600   -2.28936100    0.03982900
C       0.67332400   -0.05098500   -0.60739100
C      -1.72480200   -0.49378000   -0.05230900
C       1.92158200   -0.03311500    0.28703600
C      -0.33625300   -1.13669200   -0.17964300
C      -0.16952200    1.20034000   -0.59471400
C      -1.44879500    0.96552800   -0.29701800
H       0.99086500   -0.29347600   -1.63212500
H      -2.40539100   -0.93801500   -0.78938100
H      -2.15325400   -0.71228800    0.93215900
H       2.37992400   -1.02391900    0.30331400
H       2.65738100    0.68536300   -0.08269200
H       1.66274300    0.24220400    1.31291500
H      -2.21871000    1.72554200   -0.23836600
H       0.24312600    2.17946800   -0.81013300
""",
)

entry(
    index = 83,
    label = "TB46",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {7,S} {10,S}
2  O u0 p2 c0 {10,D}
3  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {7,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {17,S} {18,S} {19,S}
7  C u0 p0 c0 {1,S} {5,S} {8,D}
8  C u0 p0 c0 {7,D} {9,S} {21,S}
9  C u1 p0 c0 {8,S} {10,S} {20,S}
10 C u0 p0 c0 {1,S} {2,D} {9,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.19117,0.0858528,-0.000217544,5.64396e-07,-5.24949e-10,-35610.1,16.1159], Tmin=(10,'K'), Tmax=(388.373,'K')),
            NASAPolynomial(coeffs=[-0.347342,0.0825364,-5.11687e-05,1.51945e-08,-1.73535e-12,-35035.4,33.701], Tmin=(388.373,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-296.104,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (494.711,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-O': 2, 'C-H': 11, 'C-C': 6, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [3, 4], dihedral: [5, 3, 4, 6], invalidation reason: Another conformer for C8H11O2[285] exists which is 3.41 kJ/mol lower.Another conformer for C8H11O2[285] exists which is 3.41 kJ/mol lower.
pivots: [3, 5], dihedral: [4, 3, 5, 7], rotor symmetry: 1, max scan energy: 19.26 kJ/mol
pivots: [4, 6], dihedral: [3, 4, 6, 17], rotor symmetry: 3, max scan energy: 11.86 kJ/mol
pivots: [5, 7], dihedral: [3, 5, 7, 1], rotor symmetry: 1, max scan energy: 7.04 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.53118400   -1.47895100   -2.62958600
O       2.41043000   -2.08592000   -3.79540300
C      -0.99730700   -0.57118100   -0.15168500
C      -2.07215300    0.28821500    0.52141000
C      -1.53659300   -1.34936800   -1.37152900
C      -1.54433800    1.05984100    1.73396300
C      -0.49661600   -2.14823900   -2.06729400
C      -0.35778200   -3.52299700   -2.25301700
C       0.81136800   -3.73217300   -2.96715100
C       1.41343900   -2.44611600   -3.22841800
H      -0.58546900   -1.28277900    0.57299600
H      -0.16526900    0.06068800   -0.47692800
H      -2.90876500   -0.35047600    0.82987800
H      -2.48059200    0.99368300   -0.21198500
H      -2.34409900   -2.02052300   -1.06471700
H      -1.96377900   -0.63432100   -2.08636600
H      -0.72790700    1.73054500    1.45015200
H      -1.16218000    0.37921900    2.50084200
H      -2.33022200    1.66703400    2.19063500
H       1.24682200   -4.66088200   -3.29862900
H      -1.05413500   -4.26587700   -1.89473500
""",
)

entry(
    index = 84,
    label = "TB66",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {3,D} {4,S} {10,S}
3  C u0 p0 c0 {2,D} {5,S} {12,S}
4  C u0 p0 c0 {2,S} {7,D} {11,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {1,S} {13,S}
7  C u0 p0 c0 {4,D} {14,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54399,0.0438681,-3.67172e-06,-2.73886e-08,1.44143e-11,-40163.3,13.0295], Tmin=(10,'K'), Tmax=(863.228,'K')),
            NASAPolynomial(coeffs=[6.79277,0.0423159,-2.44365e-05,6.76745e-09,-7.25295e-13,-41227.2,-5.07998], Tmin=(863.228,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-333.959,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'C=O': 1, 'C-H': 5, 'C-C': 1, 'C=C': 2, 'H-O': 1}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [6, 1, 4, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [1, 6], dihedral: [4, 1, 6, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 4], dihedral: [14, 2, 4, 1], invalidation reason: 
pivots: [5, 7], dihedral: [6, 5, 7, 8], rotor symmetry: 2, max scan energy: 24.10 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       3.03166300    0.31866200    1.06284100
O       1.32962300    1.86242300    1.55743900
O       7.81552900   -1.93956800    1.76271600
C       1.89670900    1.02664400    0.58896100
C       5.33149900    0.54773200    1.55101200
C       4.12347500    1.09325700    1.37244100
C       5.60217600   -0.87657300    1.41192700
C       6.78036500   -1.43463600    1.59955500
H       2.16861400    1.67841600   -0.24587900
H       1.21154100    0.24329700    0.25379400
H       6.14502400    1.20875200    1.82150200
H       4.79818000   -1.54925200    1.13562400
H       3.93496600    2.15200200    1.50278200
H       1.02122700    1.30961400    2.28467600
""",
)				

entry(
    index = 85,
    label = "TB67",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {10,S}
3  C u0 p0 c0 {4,S} {8,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {5,D} {7,S}
5  C u0 p0 c0 {1,S} {4,D} {13,S}
6  O u0 p2 c0 {1,S} {2,S}
7  O u0 p2 c0 {2,S} {4,S}
8  O u0 p2 c0 {3,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86518,0.00885568,0.000190767,-4.19499e-07,2.84866e-10,-36931.2,12.9517], Tmin=(10,'K'), Tmax=(472.432,'K')),
            NASAPolynomial(coeffs=[1.20446,0.0559306,-3.66376e-05,1.13814e-08,-1.34555e-12,-36953.7,20.8937], Tmin=(472.432,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-307.09,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 5, 'C-H': 5, 'C-C': 3, 'C=C': 1, 'H-O': 1}
1D rotors:
* Invalidated! pivots: [3, 6], dihedral: [14, 3, 6, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [6, 7], dihedral: [3, 6, 7, 2], rotor symmetry: 1, max scan energy: 13.85 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.66375800    0.93855100    3.96237600
O       1.16717800   -0.92353000    2.56961200
O       2.44101000    0.45487600   -0.57169900
C       2.12671400    0.85126000    3.75504700
C       1.24817100   -0.32581800    3.84849600
C       1.82582700   -0.49995000    0.27252700
C       1.88433300   -0.11356100    1.71695000
C       2.50958400    0.90506000    2.32915800
H       2.72089800    1.25424100    4.56498200
H       1.09922700   -1.04117300    4.64716400
H       0.77719300   -0.68771200    0.00207200
H       2.36541500   -1.44003800    0.12417100
H       3.16496500    1.61901500    1.85856300
H       1.93425700    1.27134200   -0.50704300
""",
)

entry(
    index = 86,
    label = "TB68",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {2,D} {4,S} {11,S}
4  C u1 p0 c0 {3,S} {5,S} {10,S}
5  C u0 p0 c0 {4,S} {6,S} {12,D}
6  O u0 p2 c0 {2,S} {5,S}
7  O u0 p2 c0 {1,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85614,0.00957397,0.00018366,-4.17192e-07,2.90168e-10,-43298.1,13.6512], Tmin=(10,'K'), Tmax=(467.593,'K')),
            NASAPolynomial(coeffs=[1.90706,0.0518745,-3.42466e-05,1.06963e-08,-1.26996e-12,-43396,18.5771], Tmin=(467.593,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-360.027,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'C=O': 1, 'C-H': 4, 'C-C': 3, 'C=C': 1, 'H-O': 1}
1D rotors:
* Invalidated! pivots: [2, 4], dihedral: [13, 2, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [2, 4, 5, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       0.44835900    0.11809500   -2.31630800
O       2.16586900   -0.86073500    0.73568400
O      -0.72178100   -0.31551000   -4.24437400
C       1.77393000    0.04350400   -0.28079300
C       1.11180700   -0.64378600   -1.42985900
C       1.06810500   -1.99261400   -1.77159200
C       0.33345000   -2.09125900   -2.94311200
C      -0.08359300   -0.76455700   -3.33200400
H       2.69085000    0.53255300   -0.62706700
H       1.11160600    0.83927700    0.08747300
H       0.08545200   -2.97147400   -3.51387300
H       1.54174400   -2.78192000   -1.21008000
H       1.36941300   -1.20146500    1.15609900
""",
)

entry(
    index = 87,
    label = "TB69",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {9,S}
2  C u0 p0 c0 {4,S} {5,D} {6,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {2,S} {3,D} {11,S}
5  C u0 p0 c0 {2,D} {8,S} {12,S}
6  O u0 p2 c0 {1,S} {2,S}
7  O u0 p2 c0 {1,S} {13,S}
8  O u0 p2 c0 {5,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 O u1 p2 c0 {7,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78944,0.0137893,0.000214168,-4.98167e-07,3.44363e-10,-19732.8,15.1775], Tmin=(10,'K'), Tmax=(487.175,'K')),
            NASAPolynomial(coeffs=[3.14601,0.0577505,-4.02768e-05,1.29904e-08,-1.57242e-12,-20129.1,13.1082], Tmin=(487.175,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-164.114,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 4, 'C-H': 4, 'C-C': 2, 'C=C': 2, 'O-O': 1, 'H-O': 1}
1D rotors:
pivots: [2, 5], dihedral: [4, 2, 5, 1], rotor symmetry: 1, max scan energy: 14.21 kJ/mol
pivots: [3, 9], dihedral: [14, 3, 9, 6], rotor symmetry: 1, max scan energy: 31.02 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       3.61641100   -0.57526600    2.13350300
O       5.24276300   -2.26757600    1.93319300
O       2.41161000    1.43837200    0.61113800
O       6.35855600   -1.83753800    2.49018400
C       4.04686300   -1.79766200    2.68119100
C       2.41804400   -0.79257500    1.44842100
C       2.93153300   -2.76075800    2.43667800
C       2.00385800   -2.15216600    1.68050600
C       1.86843300    0.20718600    0.74417100
H       4.40902800   -1.64606100    3.69841400
H       2.94362000   -3.78136100    2.78623900
H       1.09191400   -2.58258000    1.29281700
H       0.92612800    0.09048900    0.22790800
H       3.25467900    1.45239000    1.08458000
""",
)

entry(
    index = 88,
    label = "TB70",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,D} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {6,S} {10,D}
5  C u0 p0 c0 {1,D} {7,S} {11,S}
6  O u0 p2 c0 {1,S} {4,S}
7  O u0 p2 c0 {5,S} {12,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88636,0.00668833,0.00015668,-3.00957e-07,1.75025e-10,-46344.2,11.6165], Tmin=(10,'K'), Tmax=(557.943,'K')),
            NASAPolynomial(coeffs=[0.807521,0.0538985,-3.78228e-05,1.2197e-08,-1.47278e-12,-46391.9,21.1673], Tmin=(557.943,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-385.373,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'C=O': 1, 'C-H': 3, 'C-C': 2, 'C=C': 2, 'H-O': 1}
1D rotors:
pivots: [2, 8], dihedral: [12, 2, 8, 4], rotor symmetry: 1, max scan energy: 38.03 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.18042900    1.10019000    0.11274500
O       2.60041400    0.93735300    0.15207100
O      -2.36399900    1.75015900    0.13711100
C       0.47226200   -0.11181100   -0.00222700
C      -0.50008100   -1.15955700   -0.13286700
C      -1.72575900   -0.59502800   -0.09806000
C      -1.57430500    0.85613600    0.05857200
C       1.81767100   -0.14654400    0.02146100
H      -0.25521800   -2.20667600   -0.23868600
H      -2.69124700   -1.06975800   -0.16792800
H       2.36771100   -1.07357200   -0.06544400
H       2.03298000    1.71911100    0.22325000
""",
)

entry(
    index = 89,
    label = "TB71",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,D} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {5,D}
3  C u1 p0 c0 {2,S} {7,S} {8,S}
4  C u0 p0 c0 {1,D} {9,S} {10,S}
5  O u0 p2 c0 {2,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89316,0.00697195,0.000126783,-2.88668e-07,1.99262e-10,6711.52,9.35662], Tmin=(10,'K'), Tmax=(481.637,'K')),
            NASAPolynomial(coeffs=[3.19848,0.0336493,-2.14162e-05,6.59564e-09,-7.82208e-13,6535.93,9.68302], Tmin=(481.637,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (55.7798,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 2, 'C=C': 1, 'C=O': 1}
1D rotors:
pivots: [2, 3], dihedral: [5, 2, 3, 1], rotor symmetry: 2, max scan energy: 25.46 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [1, 3, 4, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.97965100   -0.58024600   -0.95796800
C       0.72978200   -0.07560300    0.63499500
C      -0.54009200   -0.72600100    0.19136700
C      -1.24848100   -1.53502900    1.14189900
C       1.44563000    0.69013200   -0.18643800
H       1.05178500   -0.24969500    1.65768800
H      -0.89236200   -1.68346000    2.15453000
H      -2.16948400   -2.00996300    0.82879300
H       2.36715500    1.16448100    0.12914100
H       1.10858900    0.85279300   -1.20437600
""",
)

entry(
    index = 90,
    label = "TB72",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
3 C u0 p0 c0 {1,D} {2,S} {8,S}
4 C u0 p0 c0 {2,S} {5,T}
5 C u0 p0 c0 {4,T} {9,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90344,0.00803714,0.000116723,-3.36197e-07,3.05507e-10,9421.18,10.8473], Tmin=(10,'K'), Tmax=(343.857,'K')),
            NASAPolynomial(coeffs=[2.84196,0.0297467,-1.88178e-05,5.7655e-09,-6.79933e-13,9438.83,14.0304], Tmin=(343.857,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (78.3473,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C#C': 1, 'C-H': 4, 'C-C': 2, 'C=O': 1}
1D rotors:
pivots: [2, 3], dihedral: [4, 2, 3, 1], rotor symmetry: 1, max scan energy: 12.06 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.45950100    0.53602900   -0.28026400
C      -0.36086000   -0.62002300   -0.04580700
C      -1.27487300    0.53283300   -0.47144000
C       0.96280600   -0.17230800    0.36494300
C       2.03954900    0.23833300    0.70253400
H      -0.86713500   -1.18302100    0.74270200
H      -0.27435100   -1.28943600   -0.91340300
H      -0.76136000    1.36712800   -0.99302800
H       2.99572700    0.59046400    1.00358400
""",
)

entry(
    index = 91,
    label = "TB73",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {4,D} {5,S} {6,S}
3  C u0 p0 c0 {1,S} {6,S} {10,D}
4  C u0 p0 c0 {2,D} {7,S} {11,S}
5  C u0 p1 c0 {1,S} {2,S}
6  O u0 p2 c0 {2,S} {3,S}
7  O u0 p2 c0 {4,S} {12,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87437,0.00779103,0.000161366,-3.3714e-07,2.1433e-10,-17325.1,11.594], Tmin=(10,'K'), Tmax=(517.464,'K')),
            NASAPolynomial(coeffs=[2.20941,0.0472945,-3.03475e-05,9.31555e-09,-1.10452e-12,-17509.4,15.0842], Tmin=(517.464,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-144.089,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'C=O': 1, 'C-H': 3, 'C-C': 3, 'C=C': 1, 'H-O': 1}
1D rotors:
pivots: [2, 7], dihedral: [12, 2, 7, 5], rotor symmetry: 1, max scan energy: 83.29 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.52764300    1.17219700    0.47098800
O       2.78060100   -0.10800200   -0.21941600
O      -2.77903700    0.95748700    0.41507700
C      -1.30774300   -0.83294000   -0.48315800
C       0.51566800    0.34209500    0.04683000
C      -1.70790500    0.49837300    0.16993900
C       1.84232300    0.70083200    0.19220400
C       0.18910000   -0.87375600   -0.53485900
H      -1.75417500   -0.91881900   -1.48079100
H      -1.72080500   -1.67597100    0.08308100
H       2.19035700    1.62877000    0.63404100
H       2.27925900   -0.89024700   -0.58744400
""",
)

entry(
    index = 92,
    label = "TB74",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,D}
3  C u0 p0 c0 {2,S} {5,D} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  C u1 p0 c0 {3,D} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70765,0.0296283,1.78912e-05,-5.46337e-08,2.80863e-11,-4969.19,11.3351], Tmin=(10,'K'), Tmax=(759.803,'K')),
            NASAPolynomial(coeffs=[5.83485,0.0338467,-2.08729e-05,6.08415e-09,-6.7881e-13,-5737.45,-1.2715], Tmin=(759.803,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-41.332,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-H': 4, 'C=O': 1, 'C-C': 2, 'C=C': 1, 'H-O': 1}
1D rotors:
pivots: [1, 3], dihedral: [10, 1, 3, 4], rotor symmetry: 1, max scan energy: 25.71 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [1, 3, 4, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [4, 5], dihedral: [2, 4, 5, 6], rotor symmetry: 1, max scan energy: 24.93 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -1.81351200    0.88656900   -1.20767400
O       0.72852300    1.36955500   -1.76674200
C      -0.90064000    0.76976500   -0.15040900
C       0.51957500    1.07292000   -0.60710400
C       1.63488900    1.00050300    0.38004400
C       1.49403300    0.68914000    1.64474300
H      -1.15113900    1.46057900    0.66686200
H      -0.91372900   -0.24413700    0.27354500
H       2.61455300    1.23530500   -0.04643200
H      -1.28648300    1.13849400   -1.98153000
H       2.09970200    0.56928700    2.52990400
""",
)

entry(
    index = 93,
    label = "TB75",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,D}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {6,S} {11,S}
5  O u0 p2 c0 {1,S} {12,S}
6  C u1 p0 c0 {4,S} {13,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {2,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85614,0.00957408,0.00018366,-4.17195e-07,2.90172e-10,-43353.5,13.6513], Tmin=(10,'K'), Tmax=(467.591,'K')),
            NASAPolynomial(coeffs=[1.90709,0.0518744,-3.42466e-05,1.06963e-08,-1.26995e-12,-43451.4,18.577], Tmin=(467.591,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-360.487,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C=O': 2, 'C-H': 4, 'C-C': 3, 'C=C': 1, 'H-O': 1}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [13, 1, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [1, 4, 5, 2], invalidation reason: Another conformer for C5H5O3[3135] exists which is 0.95 kJ/mol lower.Another conformer for C5H5O3[3135] exists which is 0.95 kJ/mol lower.
* Invalidated! pivots: [5, 6], dihedral: [2, 5, 6, 7], invalidation reason: 
* Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 3], invalidation reason: Bond ([[2, 8]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[2, 8]]) broke during the scan. But unable to propose troubleshooting methods.
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 8], invalidation reason: 


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.24199800   -1.36029200    0.52540100
O       0.21944100   -1.02418100   -2.12995500
O       1.96011600   -1.77778700   -3.42487200
C      -1.50096700   -0.65535600   -0.45359100
C      -0.37564400   -1.46572200   -1.00864700
C       0.20401400   -2.64314000   -0.54419800
C       1.22611100   -2.96692200   -1.42305500
C       1.27592800   -1.95794400   -2.45493700
H      -1.09950100    0.23302500    0.04583000
H      -2.12413800   -0.29585500   -1.28423200
H      -0.10512800   -3.16804900    0.34548500
H       1.90195200   -3.80626100   -1.39477100
H      -2.72227000   -2.06868400    0.08414600
""",
)

entry(
    index = 94,
    label = "TB76",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {2,D} {7,S} {10,S}
4  C u0 p0 c0 {5,S} {6,S} {11,D}
5  C u0 p1 c0 {1,S} {4,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {3,S} {12,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88649,0.00668204,0.00015672,-3.01069e-07,1.75124e-10,-46438.3,11.6154], Tmin=(10,'K'), Tmax=(557.774,'K')),
            NASAPolynomial(coeffs=[0.803817,0.0539073,-3.78304e-05,1.21997e-08,-1.47314e-12,-46485.1,21.1853], Tmin=(557.774,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-386.156,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'C=O': 1, 'C-H': 3, 'C-C': 3, 'C=C': 1, 'H-O': 1}
1D rotors:
pivots: [2, 6], dihedral: [12, 2, 6, 5], rotor symmetry: 1, max scan energy: 38.03 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       0.44743300    1.01418600   -0.16405400
O      -1.90622300    1.14540100   -1.64872100
O       2.43678700    1.40119300    0.87697000
C       0.10170400   -1.13942000    0.55107900
C      -0.42247600   -0.05670500   -0.23202700
C      -1.54929200    0.04812200   -0.96085500
C       1.53909600    0.64274400    0.65794900
C       1.27237700   -0.73476000    1.08770600
H       1.94585200   -1.27895300    1.73012500
H      -0.38488900   -2.09721300    0.66714700
H      -2.25686600   -0.76578400   -1.04068600
H      -1.22349500    1.82118200   -1.52464600
""",
)

entry(
    index = 95,
    label = "TB77",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {5,D} {6,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {2,S} {3,D} {11,S}
5  C u0 p0 c0 {2,D} {7,S} {12,S}
6  O u0 p2 c0 {1,S} {2,S}
7  O u0 p2 c0 {5,S} {13,S}
8  O u1 p2 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87527,0.00755967,0.000180334,-3.63562e-07,2.2322e-10,-19686.4,13.2281], Tmin=(10,'K'), Tmax=(526.96,'K')),
            NASAPolynomial(coeffs=[0.790583,0.0580088,-4.02231e-05,1.28239e-08,-1.53119e-12,-19736.6,22.5724], Tmin=(526.96,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-163.726,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 4, 'C-H': 4, 'C-C': 2, 'C=C': 2, 'H-O': 1}
1D rotors:
pivots: [2, 8], dihedral: [13, 2, 8, 5], rotor symmetry: 1, max scan energy: 36.99 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       3.29895000    1.72858400   -0.66416800
O       2.98423200   -0.32312600    1.15252400
O       2.31896700    2.52986500   -2.66595800
C       3.06081000    2.85393600   -1.61728600
C       2.33592800    1.79407300    0.30357100
C       2.05534800    3.70836200   -0.86414800
C       1.58304500    3.00194300    0.19185700
C       2.21340900    0.77837300    1.19448100
H       4.05315000    3.26174200   -1.84495800
H       1.69845600    4.64549000   -1.25993000
H       0.78649300    3.29049400    0.86302700
H       1.50023300    0.79162000    2.00601200
H       3.56607500   -0.24602200    0.38095900
""",
)

entry(
    index = 96,
    label = "TB78",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {5,S} {6,S}
2  C u0 p0 c0 {1,D} {4,S} {9,S}
3  C u0 p0 c0 {4,D} {6,S} {7,S}
4  C u0 p0 c0 {2,S} {3,D} {10,S}
5  C u1 p0 c0 {1,S} {8,S} {11,S}
6  O u0 p2 c0 {1,S} {3,S}
7  O u0 p2 c0 {3,S} {13,S}
8  O u0 p2 c0 {5,S} {12,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75664,0.0161966,0.000202276,-5.10898e-07,3.72664e-10,-35941,12.5909], Tmin=(10,'K'), Tmax=(479.376,'K')),
            NASAPolynomial(coeffs=[5.57484,0.0460117,-3.17837e-05,1.03701e-08,-1.27557e-12,-36632.2,-0.235373], Tmin=(479.376,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-298.877,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 2, 'C-O': 4, 'C-H': 3, 'C-C': 2, 'C=C': 2}
1D rotors:
pivots: [2, 6], dihedral: [13, 2, 6, 1], rotor symmetry: 1, max scan energy: 7.26 kJ/mol
pivots: [3, 8], dihedral: [12, 3, 8, 4], rotor symmetry: 1, max scan energy: 19.89 kJ/mol
* Invalidated! pivots: [4, 8], dihedral: [1, 4, 8, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O       0.20507200    0.82972500   -0.03118900
O       2.47918100    1.18305600   -0.11661500
O      -2.52783600    1.29518700    0.04527200
C      -0.68103900   -0.26313400    0.03021300
C       0.08183500   -1.43781500    0.03962100
C       1.46566800    0.30703100   -0.05739200
C       1.45075700   -1.05388500   -0.01684200
C      -2.02727500    0.02685400    0.06609100
H      -0.31221200   -2.43991900    0.08211800
H       2.31924400   -1.69082100   -0.02674600
H      -2.78058200   -0.74376000    0.11362600
H      -1.78714900    1.91201000    0.00268000
H       2.11433500    2.07547200   -0.13084600
""",
)

entry(
    index = 97,
    label = "TB79",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,D} {10,S}
3  C u0 p0 c0 {4,S} {5,S} {7,D}
4  C u0 p0 c0 {2,D} {3,S} {11,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {1,S} {12,S}
7  C u1 p0 c0 {3,D} {8,S}
8  O u0 p2 c0 {7,S} {13,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83397,0.0109499,0.00018693,-4.30073e-07,2.98469e-10,-15352.8,13.3771], Tmin=(10,'K'), Tmax=(478.305,'K')),
            NASAPolynomial(coeffs=[2.65373,0.0511548,-3.42878e-05,1.08585e-08,-1.30245e-12,-15586.9,14.5734], Tmin=(478.305,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-127.684,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 2, 'C-O': 4, 'C-H': 3, 'C-C': 2, 'C=C': 2}
1D rotors:
* Invalidated! pivots: [2, 4], dihedral: [12, 2, 4, 1], invalidation reason: Another conformer for C5H5O3[3457] exists which is 4.50 kJ/mol lower.Another conformer for C5H5O3[3457] exists which is 4.50 kJ/mol lower.
* Invalidated! pivots: [3, 8], dihedral: [13, 3, 8, 6], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.16034200    0.88372400    1.11777200
O      -1.74684000   -1.14617200    0.07560400
O      -1.77504300    3.39329100    2.53974700
C      -0.77820000   -0.48481700    0.83729800
C      -0.54259100   -1.08130600    2.20099800
C      -1.22223200    1.06241300    2.48851600
C      -0.83776000   -0.17608300    3.14128300
C      -1.66690200    2.17946700    3.07828100
H       0.10582500   -0.44673500    0.19594000
H      -0.22018200   -2.10328600    2.33807300
H      -0.81495300   -0.29901400    4.21428100
H      -2.52319500   -1.27292600    0.63491600
H      -2.56040500    3.83115300    2.89070000
""",
)

entry(
    index = 98,
    label = "TB80",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,D} {8,S} {12,S}
5  C u0 p0 c0 {3,D} {7,S} {11,S}
6  O u0 p2 c0 {1,S} {2,S}
7  O u0 p2 c0 {5,S} {13,S}
8  O u0 p2 c0 {4,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71249,0.0209874,0.000214979,-6.0742e-07,4.95476e-10,-27388.7,13.1329], Tmin=(10,'K'), Tmax=(426.844,'K')),
            NASAPolynomial(coeffs=[5.10984,0.0498009,-3.35487e-05,1.07611e-08,-1.30955e-12,-27889.7,3.10907], Tmin=(426.844,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-227.733,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 2, 'C-O': 4, 'C-H': 4, 'C-C': 2, 'C=C': 2}
1D rotors:
* Invalidated! pivots: [2, 8], dihedral: [13, 2, 8, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 7], dihedral: [14, 3, 7, 5], rotor symmetry: 1, max scan energy: 14.51 kJ/mol
pivots: [4, 6], dihedral: [1, 4, 6, 8], rotor symmetry: 1, max scan energy: 26.01 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.24142500    0.99421400   -0.62238100
O       2.12266400    0.80609200    0.77840500
O      -2.64438300    1.12208000    1.39305600
C      -0.03368700   -0.48201500   -0.90243800
C      -1.04928400    0.03656300   -0.02404600
C       1.24551700   -1.07069500   -0.45098900
C      -2.06337600    0.02262000    0.81880500
C       2.16429400   -0.45543400    0.30763200
H      -0.34342800   -0.73670700   -1.91392100
H       1.45285800   -2.07808800   -0.79060100
H       3.07480400   -0.96466500    0.60348900
H      -2.51932100   -0.90606500    1.13083800
H       1.31816200    1.22859500    0.42866700
H      -2.21721600    1.91603000    1.05119600
""",
)

entry(
    index = 99,
    label = "TB81",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {5,D} {6,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {6,S} {11,S}
5  C u0 p0 c0 {2,D} {8,S} {12,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {1,S} {13,S}
8  O u0 p2 c0 {5,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85856,0.00819281,0.000180118,-3.42871e-07,1.96208e-10,-41729.2,12.3675], Tmin=(10,'K'), Tmax=(574.894,'K')),
            NASAPolynomial(coeffs=[0.915572,0.0611553,-4.28312e-05,1.39604e-08,-1.70795e-12,-41927.7,20.2676], Tmin=(574.894,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-347.017,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 2, 'C-O': 4, 'C-H': 4, 'C-C': 2, 'C=C': 2}
1D rotors:
* Invalidated! pivots: [2, 4], dihedral: [13, 2, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 8], dihedral: [14, 3, 8, 5], rotor symmetry: 1, max scan energy: 33.29 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.10172900   -0.59965700   -2.51206900
O      -1.65825200   -1.19033100    0.45924100
O      -1.70763700   -3.54303800   -1.30776300
C      -0.38481400   -1.10181000   -0.22156200
C      -0.46683200   -1.55638400   -1.66241400
C       0.19267700    0.27598200   -0.40668600
C       0.43959600    0.45552400   -1.70714600
C      -1.07384400   -2.65253400   -2.11865100
H       0.25480300   -1.75013200    0.38823100
H       0.41335100    0.96815200    0.39050200
H       0.87241400    1.29326300   -2.23369300
H      -1.10301700   -2.91709500   -3.16802900
H      -2.26142200   -0.58623500    0.00735600
H      -1.87226600   -3.10640500   -0.45652000
""",
)

entry(
    index = 100,
    label = "TB82",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {8,S} {12,S}
6  O u0 p2 c0 {1,S} {2,S}
7  O u0 p2 c0 {1,S} {13,S}
8  O u0 p2 c0 {5,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69443,0.019946,0.000229195,-5.85732e-07,4.23194e-10,-31049.8,12.9632], Tmin=(10,'K'), Tmax=(494.801,'K')),
            NASAPolynomial(coeffs=[7.76337,0.0467073,-3.27771e-05,1.08948e-08,-1.36404e-12,-32182.7,-11.1835], Tmin=(494.801,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-258.233,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (320.107,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 2, 'C-O': 4, 'C-H': 4, 'C-C': 2, 'C=C': 2}
1D rotors:
pivots: [2, 4], dihedral: [13, 2, 4, 1], rotor symmetry: 1, max scan energy: 24.06 kJ/mol
pivots: [3, 8], dihedral: [14, 3, 8, 7], rotor symmetry: 1, max scan energy: 20.11 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 25.33 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -3.17214600   -1.22090600   -0.58491000
O      -2.56505300    1.00183800   -1.40917300
O       0.03873900    0.49600500    4.44295300
C      -2.13862300   -0.21800700   -0.97057000
C      -2.32351100   -0.71085900    0.36115300
C      -2.12316600   -0.79580800    1.67295000
C      -1.09124600   -0.06367200    2.38439500
C      -0.90472600   -0.15358000    3.70905300
H      -1.38744500   -0.61927900   -1.64092300
H      -2.77436200   -1.45772900    2.23722300
H      -0.44092800    0.58553400    1.80031700
H      -1.51923200   -0.78361700    4.34229900
H      -3.13345200    1.39389900   -0.73531900
H       0.57524200    1.04464000    3.85882900
""",
)

entry(
    index = 101,
    label = "TB83",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,D}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u1 p0 c0 {3,D} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8528,0.0180467,3.07816e-05,-5.70292e-08,2.5583e-11,13900.9,10.5659], Tmin=(10,'K'), Tmax=(799.854,'K')),
            NASAPolynomial(coeffs=[4.18206,0.0301829,-1.78254e-05,5.02753e-09,-5.4677e-13,13407.3,6.29489], Tmin=(799.854,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (115.588,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 2, 'C=C': 1, 'C=O': 1}
1D rotors:
pivots: [2, 3], dihedral: [6, 2, 3, 1], rotor symmetry: 3, max scan energy: 1.70 kJ/mol
pivots: [3, 4], dihedral: [1, 3, 4, 5], rotor symmetry: 1, max scan energy: 26.45 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       0.82472700    0.65987000    0.67412600
C      -1.22143400   -0.48836500    0.19818100
C      -0.33724600    0.73284600    0.33961600
C      -0.94596500    2.07615600    0.04875900
C      -2.18621200    2.27676600   -0.31914900
H      -0.64454900   -1.37962900    0.44002100
H      -2.08443800   -0.40939800    0.86510100
H      -1.60802600   -0.55890200   -0.82229300
H      -0.24398700    2.90570400    0.17344200
H      -2.84167000    3.09485700   -0.57667000
""",
)

entry(
    index = 102,
    label = "TB84",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
4 C u0 p0 c0 {2,S} {3,S} {5,D}
5 C u0 p0 c0 {4,D} {8,S} {9,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97124,0.00176686,9.32807e-05,-1.67038e-07,9.60949e-11,7907.66,8.89338], Tmin=(10,'K'), Tmax=(449.64,'K')),
            NASAPolynomial(coeffs=[-0.0382726,0.0373421,-2.50869e-05,7.99994e-09,-9.69373e-13,8269.17,25.0426], Tmin=(449.64,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (65.7385,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-H': 4, 'C-C': 1, 'C=C': 1, 'O-O': 1}

External symmetry: 1, optical isomers: 1

Geometry:
O      -1.56059400    0.91968100   -0.68206800
O      -0.14797500    1.11409400   -1.08991700
C      -1.13442600   -0.09888600    0.27038200
C       0.26565400    0.14516700   -0.18513200
C       1.49492900   -0.27839200    0.05174300
H      -1.55990600   -1.07613400    0.03041000
H      -1.36810800    0.18938600    1.29796300
H       2.33982400    0.13153300   -0.48536900
H       1.67060200   -1.04645100    0.79198800
""",
)

entry(
    index = 103,
    label = "TB85",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {4,D} {9,S}
4 C u1 p0 c0 {2,S} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.15682,-0.0119771,0.000123764,-1.78888e-07,8.38588e-11,48059.6,8.47065], Tmin=(10,'K'), Tmax=(664.908,'K')),
            NASAPolynomial(coeffs=[-0.659185,0.0346061,-2.1054e-05,6.14747e-09,-6.9026e-13,48310.8,26.8123], Tmin=(664.908,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (399.605,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 5, 'C-C': 3, 'C=C': 1}

External symmetry: 1, optical isomers: 1

Geometry:
C      -0.53682800   -0.44148800    0.22233400
C       1.00763800   -0.27121800   -0.03574800
C      -0.72387300    1.00460900   -0.25525000
C       0.58225100    1.11849300   -0.46305100
H      -1.00550100   -1.19943900   -0.41181900
H      -0.78845900   -0.61509600    1.27249200
H       1.42122100   -0.90659500   -0.82087200
H       1.63705900   -0.32547100    0.85423000
H      -1.59350700    1.63620500   -0.36231600
""",
)

entry(
    index = 104,
    label = "TB86",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {7,S} {10,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {6,S}
4  C u0 p0 c0 {2,S} {3,D} {11,S}
5  C u0 p0 c0 {2,S} {12,D} {13,S}
6  O u0 p2 c0 {1,S} {3,S}
7  O u0 p2 c0 {1,S} {14,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62637,0.0330792,4.64305e-05,-1.09645e-07,6.00843e-11,-34858.2,12.6055], Tmin=(10,'K'), Tmax=(644.065,'K')),
            NASAPolynomial(coeffs=[3.46016,0.0501788,-3.08137e-05,9.04317e-09,-1.02034e-12,-35170,10.7471], Tmin=(644.065,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-289.874,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'C=O': 1, 'C-H': 5, 'C-C': 3, 'C=C': 1, 'H-O': 1}
1D rotors:
* Invalidated! pivots: [2, 4], dihedral: [14, 2, 4, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 7], dihedral: [8, 5, 7, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 8], dihedral: [7, 5, 8, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.47736000    1.80712500    1.75342700
O      -1.07162900   -0.14419300    2.35259300
O       0.57780200   -0.12188300    0.03370400
C      -1.21824800    1.19585900    2.36822500
C       0.69084700    2.28643000   -0.30543000
C      -1.27662100    1.98587900    1.17116900
C      -0.75379500    2.48384500    0.06048000
C       1.16204400    0.84556800   -0.39219400
H       1.38499900    2.76757700    0.40255900
H       0.91884300    2.75765600   -1.26755600
H      -1.03175600    1.63690600    3.34018100
H      -1.41029700    2.97083700   -0.65078800
H       2.15274600    0.71784200   -0.87667300
H      -0.75354500   -0.39836300    1.46934400
""",
)

entry(
    index = 105,
    label = "TB87",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {6,S}
4  C u0 p0 c0 {3,D} {7,S} {12,S}
5  C u0 p0 c0 {2,S} {11,D} {13,S}
6  O u0 p2 c0 {1,S} {3,S}
7  O u0 p2 c0 {4,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {5,D}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61053,0.0350184,3.49156e-05,-8.7306e-08,4.60673e-11,-30596.7,12.5889], Tmin=(10,'K'), Tmax=(686.026,'K')),
            NASAPolynomial(coeffs=[3.89171,0.0489729,-2.96925e-05,8.61317e-09,-9.62094e-13,-31002.2,8.66383], Tmin=(686.026,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-254.439,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'C=O': 1, 'C-H': 5, 'C-C': 3, 'C=C': 1, 'H-O': 1}
1D rotors:
* Invalidated! pivots: [2, 7], dihedral: [14, 2, 7, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [1, 4, 5, 8], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 8], dihedral: [4, 5, 8, 3], invalidation reason: Inconsistent initial and final conformers But unable to propose troubleshooting methods.Inconsistent initial and final conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       0.52954600   -1.98824400   -0.36592000
O       1.98703700    1.45521600   -0.28841400
O      -0.87444000    1.71523700    0.51504400
C      -0.46553000   -0.90082100   -0.51784400
C      -1.38187500   -0.64874800    0.65293100
C       0.94192100   -0.67385800   -0.40531600
C       2.01263800    0.08800800   -0.27438400
C      -1.54476100    0.82228700    0.97598200
H      -0.92258500   -0.88430300   -1.50434800
H      -2.37661700   -1.08703900    0.50953100
H      -0.96415300   -1.12848200    1.54799300
H       3.00553700   -0.32580200   -0.15762700
H      -2.34558200    1.05221900    1.70810200
H       1.06309300    1.73954400   -0.20695100
""",
)

entry(
    index = 106,
    label = "TB88",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {2,S} {11,D}
5  C u0 p0 c0 {3,S} {12,D} {13,S}
6  O u0 p2 c0 {2,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {4,D}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63217,0.04069,2.24714e-06,-2.88484e-08,1.31748e-11,-34626.6,12.476], Tmin=(10,'K'), Tmax=(944.544,'K')),
            NASAPolynomial(coeffs=[7.12007,0.0412544,-2.30025e-05,6.16167e-09,-6.41039e-13,-35969.6,-7.7733], Tmin=(944.544,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-287.892,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C=O': 2, 'C-H': 5, 'C-C': 5, 'H-O': 1}
1D rotors:
* Invalidated! pivots: [1, 5], dihedral: [14, 1, 5, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 6], dihedral: [5, 4, 6, 8], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [6, 8], dihedral: [4, 6, 8, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.65235900   -2.72872600    0.81824000
O       1.41412100   -1.62411000    1.50687700
O      -3.59465800   -1.59913700    2.61275500
C      -0.87417500   -0.66000600    2.13936200
C      -1.05045200   -1.47707300    0.79733700
C      -1.35687300   -1.24128200    3.45720700
C       0.26433900   -1.30703600    1.44055600
C      -2.86353700   -1.38919100    3.55165200
H      -1.02714600    0.40967700    2.01860000
H      -1.27657100   -0.83890100   -0.05912000
H      -0.94869700   -2.25009200    3.60986100
H      -0.99877500   -0.64599200    4.30250800
H      -3.28430100   -1.32483400    4.57653900
H      -2.56802900   -2.57374200    1.09970900
""",
)

entry(
    index = 107,
    label = "BT89",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {10,D}
4  C u0 p0 c0 {2,S} {11,D} {12,S}
5  C u0 p0 c0 {3,S} {13,D} {14,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 O u0 p2 c0 {3,D}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {4,S}
13 O u0 p2 c0 {5,D}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88407,0.0454906,-2.23478e-05,3.55374e-09,1.89151e-13,-51633.1,12.9929], Tmin=(10,'K'), Tmax=(1637.8,'K')),
            NASAPolynomial(coeffs=[25.2627,0.00618557,1.82829e-06,-1.47502e-09,2.2222e-13,-60367.1,-105.979], Tmin=(1637.8,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-429.323,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 3, 'C-H': 6, 'C-C': 4}
1D rotors:
* Invalidated! pivots: [4, 5], dihedral: [6, 4, 5, 7], invalidation reason: Inconsistent initial and final conformers But unable to propose troubleshooting methods.Inconsistent initial and final conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 6], dihedral: [5, 4, 6, 1], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 7], dihedral: [4, 5, 7, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [6, 8], dihedral: [1, 6, 8, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       0.52974000   -0.65006800   -1.59511800
O      -0.50270300   -2.74120800    0.84466200
O       3.04294600    0.04662100    0.67163600
C       0.13165300   -0.00934000    0.69873800
C      -1.30709700   -0.49128600    0.56579000
C       0.97246200   -0.35407800   -0.50947800
C      -1.43244700   -1.99500800    0.67275200
C       2.49925800   -0.27986800   -0.34934800
H      -1.73632900   -0.19388200   -0.39806100
H      -1.95061900   -0.04716500    1.33489300
H       0.61705600   -0.41872500    1.58705400
H       0.16832500    1.08128100    0.81239800
H      -2.46832900   -2.38706500    0.58488200
H       3.04438800   -0.55038100   -1.27617200
""",
)

entry(
    index = 108,
    label = "TB90",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {5,S} {13,S}
2  O u1 p2 c0 {6,S}
3  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {6,D} {10,S}
5  C u0 p0 c0 {1,S} {7,D} {11,S}
6  C u0 p0 c0 {2,S} {4,D} {12,S}
7  C u1 p0 c0 {3,S} {5,D}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71193,0.0259784,5.27539e-05,-1.08636e-07,5.66959e-11,12272.8,12.7943], Tmin=(10,'K'), Tmax=(658.138,'K')),
            NASAPolynomial(coeffs=[2.83144,0.0464165,-2.82127e-05,8.21e-09,-9.20057e-13,12062,14.1915], Tmin=(658.138,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (102.007,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-H': 5, 'C-C': 2, 'C=C': 2, 'H-O': 1}
1D rotors:
* Invalidated! pivots: [1, 5], dihedral: [13, 1, 5, 7], invalidation reason: Another conformer for C5H6O2[6897] exists which is 11.82 kJ/mol lower.Another conformer for C5H6O2[6897] exists which is 11.82 kJ/mol lower.
* Invalidated! pivots: [3, 4], dihedral: [7, 3, 4, 6], invalidation reason: Inconsistent initial and final conformers But unable to propose troubleshooting methods.Inconsistent initial and final conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 7], dihedral: [4, 3, 7, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 6], dihedral: [3, 4, 6, 2], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       2.53043800    0.43324900    0.44092600
O       5.19386200    0.25293100    0.82067500
C       4.11109200   -2.36108300    0.21934800
C       5.29442900   -1.72532200   -0.44733100
C       2.25630900   -0.61077600   -0.37013200
C       5.75852500   -0.45018600   -0.03961200
C       2.90941500   -1.77094000   -0.41410700
H       4.10549300   -2.14997200    1.29729500
H       4.12290000   -3.44778300    0.09906100
H       5.75808600   -2.20910600   -1.29979900
H       1.38382400   -0.42939100   -0.99082600
H       6.68381800   -0.08050800   -0.51136800
H       3.44326800    0.34406000    0.80164100
""",
)

entry(
    index = 109,
    label = "TB91",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {11,S}
3  C u1 p0 c0 {1,S} {4,S} {12,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  C u0 p0 c0 {4,D} {9,S} {13,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {1,S} {8,S}
8  O u0 p2 c0 {2,S} {7,S}
9  O u0 p2 c0 {5,S} {14,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84785,0.00898145,0.000192894,-3.77805e-07,2.22424e-10,-18214.3,14.0561], Tmin=(10,'K'), Tmax=(558.654,'K')),
            NASAPolynomial(coeffs=[0.950556,0.0636279,-4.48592e-05,1.45436e-08,-1.76462e-12,-18419.6,21.6122], Tmin=(558.654,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-151.504,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 5, 'C-H': 4, 'C-C': 3, 'C=C': 1, 'O-O': 1, 'H-O': 1}
1D rotors:
pivots: [4, 9], dihedral: [14, 4, 9, 8], rotor symmetry: 1, max scan energy: 38.80 kJ/mol
* Invalidated! pivots: [8, 9], dihedral: [1, 8, 9, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.61416300    1.22064600    0.21595800
O      -1.35982700   -1.42160800    1.61606900
O      -1.86602200   -0.03252700    1.80640500
O       1.69666900    2.62557300    0.03355800
C      -1.06756700   -1.11664200    0.19569700
C      -1.64817100    0.27770000    0.43564700
C       0.35772800   -0.84802700   -0.09971000
C       0.57431800    0.51085800    0.00529700
C       1.71837300    1.28314300   -0.09059300
H      -1.58151200   -1.83757900   -0.44061500
H      -2.55082400    0.65378800   -0.04413000
H       1.11209300   -1.59269800   -0.29583800
H       2.69606400    0.86389000   -0.27278800
H       0.78487700    2.89451800    0.21846700
""",
)

entry(
    index = 110,
    label = "TB92",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {7,S} {10,S}
2  C u0 p0 c0 {3,S} {4,D} {5,S}
3  C u0 p0 c0 {2,S} {6,D} {11,S}
4  C u0 p0 c0 {2,D} {8,S} {12,S}
5  O u0 p2 c0 {1,S} {2,S}
6  C u1 p0 c0 {1,S} {3,D}
7  O u0 p2 c0 {1,S} {9,S}
8  O u0 p2 c0 {4,S} {13,S}
9  O u0 p2 c0 {7,S} {14,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51202,0.0461988,3.04663e-05,-1.11165e-07,6.59855e-11,-5215.37,13.5957], Tmin=(10,'K'), Tmax=(672.599,'K')),
            NASAPolynomial(coeffs=[7.98152,0.0466783,-3.09512e-05,9.52632e-09,-1.10778e-12,-6428.69,-10.7445], Tmin=(672.599,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-43.4194,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (320.107,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 2, 'C-O': 4, 'C-H': 3, 'C-C': 2, 'C=C': 2, 'O-O': 1}
1D rotors:
pivots: [2, 4], dihedral: [5, 2, 4, 14], rotor symmetry: 1, max scan energy: 22.60 kJ/mol
pivots: [2, 5], dihedral: [4, 2, 5, 1], rotor symmetry: 1, max scan energy: 41.39 kJ/mol
pivots: [3, 8], dihedral: [13, 3, 8, 6], rotor symmetry: 1, max scan energy: 26.83 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.16415300   -1.74050700   -1.61107000
O       1.59072400   -0.18538100   -1.48088000
O      -1.94808600   -3.27204300   -3.11004000
O       1.07223500    0.62524200   -2.56503700
C       0.52301000   -0.76926100   -0.78563300
C      -1.52148500   -1.40615400   -1.68844100
C      -1.77211200   -0.22467800   -0.88071600
C      -2.34446700   -2.17402200   -2.41345700
C      -0.60054500    0.12139200   -0.36301600
H       1.04430300   -1.28882200    0.02500300
H      -2.73705100    0.24540500   -0.76135500
H      -3.40218000   -1.96848900   -2.49300300
H      -1.00294700   -3.39897600   -2.95313400
H       1.08378600   -0.01951000   -3.28727900
""",
)

entry(
    index = 111,
    label = "BT93",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {7,S} {10,S}
2  C u0 p0 c0 {4,D} {5,S} {6,S}
3  C u0 p0 c0 {1,S} {6,D} {11,S}
4  C u0 p0 c0 {2,D} {8,S} {12,S}
5  O u0 p2 c0 {1,S} {2,S}
6  C u1 p0 c0 {2,S} {3,D}
7  O u0 p2 c0 {1,S} {9,S}
8  O u0 p2 c0 {4,S} {13,S}
9  O u0 p2 c0 {7,S} {14,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55977,0.0366639,0.000115051,-3.19272e-07,2.22944e-10,-5642.52,13.6903], Tmin=(10,'K'), Tmax=(522.681,'K')),
            NASAPolynomial(coeffs=[6.53986,0.051596,-3.61037e-05,1.16573e-08,-1.41129e-12,-6469.55,-3.68473], Tmin=(522.681,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-46.9842,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (320.107,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 2, 'C-O': 4, 'C-H': 3, 'C-C': 2, 'C=C': 2, 'O-O': 1}
1D rotors:
pivots: [2, 4], dihedral: [5, 2, 4, 14], rotor symmetry: 1, max scan energy: 21.14 kJ/mol
pivots: [2, 5], dihedral: [4, 2, 5, 1], rotor symmetry: 1, max scan energy: 40.99 kJ/mol
pivots: [3, 8], dihedral: [13, 3, 8, 6], rotor symmetry: 1, max scan energy: 28.13 kJ/mol
* Invalidated! pivots: [6, 8], dihedral: [1, 6, 8, 3], invalidation reason: Significant difference observed between consecutive conformersSignificant difference observed between consecutive conformers


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.85800900    1.28629200    1.06641000
O      -2.09954800   -0.41071700   -0.52469900
O      -2.81235500    2.74584800    3.26502100
O      -2.74887100   -1.31049200    0.40836400
C      -1.17567200    0.39023700    0.16366000
C      -1.33690200    1.11232800    2.35829100
C      -0.14990500   -0.33349400    1.02033600
C      -1.81463100    1.83400500    3.37943800
C      -0.30289400    0.12703400    2.25156400
H      -0.74364900    0.97346000   -0.65772100
H       0.52590300   -1.07380700    0.62231300
H      -1.42447300    1.73388600    4.38148600
H      -3.06954200    2.79472400    2.33469500
H      -3.50444600   -0.76903900    0.67976900
""",
)

entry(
    index = 112,
    label = "TB94",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {9,S}
2  C u0 p0 c0 {4,D} {5,S} {6,S}
3  C u1 p0 c0 {1,S} {4,S} {10,S}
4  C u0 p0 c0 {2,D} {3,S} {11,S}
5  C u0 p0 c0 {2,S} {12,D} {13,S}
6  O u0 p2 c0 {1,S} {2,S}
7  O u0 p2 c0 {1,S} {8,S}
8  O u0 p2 c0 {7,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59749,0.0324212,0.000142088,-4.11632e-07,3.21851e-10,-28438.3,13.4959], Tmin=(10,'K'), Tmax=(448.588,'K')),
            NASAPolynomial(coeffs=[4.6193,0.0547742,-3.78677e-05,1.21665e-08,-1.47234e-12,-28846.6,5.85679], Tmin=(448.588,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-236.478,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (320.107,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'C=O': 1, 'C-H': 4, 'C-C': 3, 'C=C': 1, 'O-O': 1, 'H-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [5, 2, 3, 14], rotor symmetry: 1, max scan energy: 27.01 kJ/mol
pivots: [2, 5], dihedral: [3, 2, 5, 1], rotor symmetry: 1, max scan energy: 43.00 kJ/mol
pivots: [6, 9], dihedral: [1, 6, 9, 4], rotor symmetry: 1, max scan energy: 71.66 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.63413300   -0.11153100    1.70778400
O      -2.25834800    0.04350900   -0.54764400
O      -2.68597200    1.42750900   -0.44262300
O      -0.35806900    1.76991700    4.42987500
C      -1.18895000   -0.16910500    0.32752900
C      -0.83741700    0.76498400    2.37339900
C      -0.04230300    0.79921200    0.27465800
C       0.13961000    1.32569100    1.50753700
C      -1.05206100    1.00018600    3.77381400
H      -0.91978100   -1.20841500    0.10313200
H       0.50441200    1.00513600   -0.63274900
H       0.86989500    2.05237100    1.82823600
H      -1.89118900    0.43549300    4.22169400
H      -3.45487100    1.32718500    0.13718900
""",
)

entry(
    index = 113,
    label = "TB95",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,D}
5  O u0 p2 c0 {1,S} {4,S}
6  C u1 p0 c0 {1,S} {11,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78467,0.0217044,6.07701e-05,-1.24543e-07,6.58888e-11,-26521,12.9628], Tmin=(10,'K'), Tmax=(668.898,'K')),
            NASAPolynomial(coeffs=[4.34246,0.0391805,-2.509e-05,7.54451e-09,-8.63587e-13,-27061.2,7.0159], Tmin=(668.898,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-220.533,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C=O': 2, 'C-H': 3, 'C-C': 3, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [4, 8], dihedral: [1, 4, 8, 3], invalidation reason: Another conformer for C5H3O3[7318] exists which is 4.27 kJ/mol lower.Another conformer for C5H3O3[7318] exists which is 4.27 kJ/mol lower.


External symmetry: 1, optical isomers: 2

Geometry:
O       0.19261900   -1.38329900   -0.18363900
O       2.45104200   -1.38450600   -0.36454700
O      -2.53249000    0.11555200    1.55855000
C      -0.81951400   -0.40145700   -0.08750500
C      -0.11741600    0.92148800   -0.19816100
C       1.19149900    0.69743900   -0.29350000
C       1.43322100   -0.76716000   -0.28764300
C      -1.57948300   -0.50791100    1.26790800
H      -1.57117100   -0.56623300   -0.86749300
H      -0.64473900    1.86447400   -0.16856600
H       1.99643300    1.41161200   -0.37540200
""",
)

entry(
    index = 114,
    label = "TB96",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {5,D}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {5,S} {6,D}
5  C u0 p0 c0 {2,D} {3,S} {4,S}
6  C u0 p0 c0 {4,D} {9,S} {10,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93019,0.00412266,0.000111628,-2.08923e-07,1.20594e-10,-15332.8,9.94807], Tmin=(10,'K'), Tmax=(549.287,'K')),
            NASAPolynomial(coeffs=[1.15038,0.0394534,-2.60559e-05,8.18945e-09,-9.81504e-13,-15255,19.6217], Tmin=(549.287,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-127.512,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C-H': 4, 'C-C': 2, 'C=C': 1, 'C=O': 1}

External symmetry: 1, optical isomers: 1

Geometry:
O      -0.16371000   -1.17883200    0.37062300
O      -0.92470200    1.91809800   -0.40233100
C      -1.43402200   -0.45187200    0.37314900
C       0.55951800   -0.07943400   -0.07117300
C      -0.66134800    0.78919000   -0.11820300
C       1.85682300    0.04383400   -0.32566100
H      -2.14932400   -0.87769400   -0.33318200
H      -1.86143200   -0.38056000    1.37520700
H       2.54558100   -0.78161900   -0.20152500
H       2.23261500    0.99889000   -0.66690600
""",
)

entry(
    index = 115,
    label = "TB97",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {10,S}
3  C u1 p0 c0 {1,S} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {7,S}
5  C u0 p0 c0 {4,D} {8,S} {12,S}
6  O u0 p2 c0 {1,S} {2,S}
7  O u0 p2 c0 {2,S} {4,S}
8  O u0 p2 c0 {5,S} {13,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87585,0.00707168,0.000165915,-3.06358e-07,1.70146e-10,-23098.5,12.564], Tmin=(10,'K'), Tmax=(587.939,'K')),
            NASAPolynomial(coeffs=[0.368294,0.0598994,-4.27597e-05,1.40505e-08,-1.72564e-12,-23186.7,23.3656], Tmin=(587.939,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-192.107,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 5, 'C-H': 4, 'C-C': 3, 'C=C': 1, 'H-O': 1}
1D rotors:
pivots: [3, 8], dihedral: [13, 3, 8, 7], rotor symmetry: 1, max scan energy: 36.54 kJ/mol
* Invalidated! pivots: [7, 8], dihedral: [2, 7, 8, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.72504300    1.49774000    0.27768800
O      -0.36507100   -0.14150600    1.33194900
O       2.27110000   -0.43851800    1.91929600
C      -1.48246100    0.35326000   -0.66786000
C      -1.62172800    0.20583600    0.78836000
C      -0.06496400    0.12215800   -0.94061100
C       0.55682800   -0.09311600    0.28174000
C       1.88244000   -0.25261600    0.63888900
H      -2.27838800    0.20490700   -1.38499600
H      -2.43989600   -0.19243500    1.37607100
H       0.42634100    0.17530300   -1.89846700
H       2.68827900   -0.25030300   -0.07907300
H       1.48153400   -0.39667100    2.47788000
""",
)

entry(
    index = 116,
    label = "BT98",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {6,S} {10,S}
4  C u0 p0 c0 {5,S} {7,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {4,S} {13,D}
6  O u0 p2 c0 {2,S} {3,S}
7  O u0 p2 c0 {4,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 O u0 p2 c0 {5,D}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66888,0.0340343,5.3946e-05,-1.22117e-07,6.36661e-11,-20247.5,11.944], Tmin=(10,'K'), Tmax=(705.274,'K')),
            NASAPolynomial(coeffs=[5.64502,0.0483285,-3.06937e-05,9.15897e-09,-1.04109e-12,-21160.5,-1.39616], Tmin=(705.274,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-168.374,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'C=O': 1, 'C-H': 5, 'C-C': 5, 'H-O': 1}
1D rotors:
pivots: [2, 7], dihedral: [14, 2, 7, 8], rotor symmetry: 1, max scan energy: 26.91 kJ/mol
pivots: [4, 8], dihedral: [5, 4, 8, 3], rotor symmetry: 1, max scan energy: 19.49 kJ/mol
* Invalidated! pivots: [7, 8], dihedral: [2, 7, 8, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O       0.43298500    1.75321100    4.43901800
O      -2.64058800    0.27576900   -0.46791000
O      -2.70518000    0.37027800    2.18321500
C      -0.52253000    1.27525300    2.50444500
C      -0.32825200    0.65548700    3.87629800
C      -0.85996700    1.95899500    3.81687400
C      -1.50390200    0.76899700    0.18036200
C      -1.66915300    0.77029300    1.68756700
H       0.36460500    1.61282800    1.97145100
H      -0.58500200   -0.26424900    4.37244000
H      -1.70154200    2.47296900    4.24765700
H      -0.61341500    0.16751900   -0.06099400
H      -1.27931200    1.79994100   -0.13540700
H      -3.26706800    0.05242000    0.23832500
""",
)

entry(
    index = 117,
    label = "TB99",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {2,S} {3,D} {9,S}
5  O u0 p2 c0 {1,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93852,0.00369149,0.000120806,-2.24119e-07,1.30299e-10,23450.3,13.2444], Tmin=(10,'K'), Tmax=(526.67,'K')),
            NASAPolynomial(coeffs=[0.207063,0.0441374,-2.8866e-05,8.98204e-09,-1.06636e-12,23675.5,27.26], Tmin=(526.67,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (194.954,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-H': 5, 'C-C': 3, 'C=C': 1, 'O-O': 1}
1D rotors:
pivots: [1, 3], dihedral: [2, 1, 3, 4], rotor symmetry: 1, max scan energy: 8.90 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.81959200    0.16844800    0.35349000
O       2.63276500   -0.85456800    0.16516500
C       0.58746700    0.01344600   -0.40677100
C      -0.52918400   -0.81620200    0.31152400
C      -0.33487700    1.19972200   -0.28762800
C      -1.31980500    0.48176200    0.26420100
H       0.86903800   -0.32578300   -1.40478800
H      -0.92627100   -1.66265600   -0.25532300
H      -0.23217300   -1.15351000    1.30663500
H      -2.33946400    0.71684200    0.54555600
H      -0.22708600    2.23249400   -0.59205700
""",
)

entry(
    index = 118,
    label = "BT100",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {5,S} {7,S}
5  C u0 p0 c0 {4,S} {11,D} {12,S}
6  O u0 p2 c0 {1,S} {2,S}
7  O u0 p2 c0 {2,S} {4,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {5,D}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89755,0.00632453,0.000161122,-3.27392e-07,2.04822e-10,-27185.4,12.1891], Tmin=(10,'K'), Tmax=(509.683,'K')),
            NASAPolynomial(coeffs=[0.82369,0.0517089,-3.50147e-05,1.09969e-08,-1.30186e-12,-27148.2,22.238], Tmin=(509.683,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-226.064,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 4, 'C-H': 4, 'C-C': 3, 'C=C': 1, 'C=O': 1}
1D rotors:
pivots: [7, 8], dihedral: [2, 7, 8, 3], rotor symmetry: 1, max scan energy: 40.40 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.90604600   -0.63788200   -0.59131700
O      -0.15862100   -0.73586700    1.00734600
O       2.99229000   -0.16485300   -0.52124100
C      -1.31029900    0.70215400   -0.44691500
C      -1.44099700   -0.26237600    0.66948000
C       0.13422600    0.70538200   -0.74361400
C       0.71050400   -0.17764700    0.09468400
C       2.11961100   -0.60337700    0.18951000
H      -1.98212200    1.52451800   -0.65447400
H      -2.12871100   -0.28296400    1.50485000
H       0.65335300    1.28830100   -1.48722300
H       2.31673100   -1.35608200    0.97788500
""",
)

entry(
    index = 119,
    label = "TB101",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {7,S} {12,S}
2  O u1 p2 c0 {4,S}
3  O u0 p2 c0 {8,D}
4  C u0 p0 c0 {2,S} {5,S} {7,D}
5  C u0 p0 c0 {4,S} {6,D} {9,S}
6  C u0 p0 c0 {5,D} {8,S} {10,S}
7  C u0 p0 c0 {1,S} {4,D} {11,S}
8  C u1 p0 c0 {3,D} {6,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81295,0.0124219,0.000181706,-4.38003e-07,3.12336e-10,-20516,13.0249], Tmin=(10,'K'), Tmax=(477.208,'K')),
            NASAPolynomial(coeffs=[3.90614,0.0459105,-3.12772e-05,1.00243e-08,-1.21398e-12,-20915.1,8.55581], Tmin=(477.208,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-170.616,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C=O': 1, 'C-H': 3, 'C-C': 2, 'C=C': 2, 'H-O': 1}
1D rotors:
* Invalidated! pivots: [1, 7], dihedral: [12, 1, 7, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [2, 4, 5, 6], invalidation reason: Bond ([[2, 8]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[2, 8]]) broke during the scan. But unable to propose troubleshooting methods.
* Invalidated! pivots: [6, 8], dihedral: [5, 6, 8, 3], invalidation reason: 
* Invalidated! pivots: [4, 7], dihedral: [2, 4, 7, 1], invalidation reason: Another conformer for C5H4O3[14895] exists which is 1.63 kJ/mol lower.Another conformer for C5H4O3[14895] exists which is 1.63 kJ/mol lower.
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 8], invalidation reason: Bond ([[2, 8]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[2, 8]]) broke during the scan. But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 1

Geometry:
O      -2.56677000    0.26427600    0.66802400
O      -0.13914100   -0.86313200    0.62239000
O       1.56846800   -2.37848700    0.24867100
C      -0.20999900    0.35447500    1.18401700
C       1.02452300    0.79812600    1.64178000
C       1.94999000   -0.22777700    1.34245800
C      -1.53037700    0.93925200    1.19539800
C       1.27389100   -1.29993600    0.69960000
H       1.21688400    1.74084300    2.12626500
H       3.00862400   -0.24997600    1.54457500
H      -1.75943100    1.90813000    1.60761900
H      -2.23823200   -0.58487000    0.33241000
""",
)

entry(
    index = 120,
    label = "TB102",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {5,S} {6,S}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  C u1 p0 c0 {2,S} {4,S} {8,S}
4  C u0 p0 c0 {3,S} {6,S} {9,D}
5  C u0 p0 c0 {1,S} {10,D} {11,S}
6  O u0 p2 c0 {1,S} {4,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  O u0 p2 c0 {4,D}
10 O u0 p2 c0 {5,D}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87089,0.00784134,0.000152135,-3.14218e-07,1.94394e-10,-35207,12.1197], Tmin=(10,'K'), Tmax=(537.64,'K')),
            NASAPolynomial(coeffs=[2.48518,0.0459762,-3.18918e-05,1.02359e-08,-1.23707e-12,-35460.1,14.205], Tmin=(537.64,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-292.773,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C=O': 2, 'C-H': 3, 'C-C': 3, 'C=C': 1}
1D rotors:
pivots: [4, 8], dihedral: [1, 4, 8, 3], rotor symmetry: 1, max scan energy: 54.89 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       0.08399700    1.06949200   -0.69514200
O      -2.05532000    1.84058900   -0.95009600
O       2.60840700   -1.13051000    0.43289600
C       0.62739000    0.00611200   -0.07414500
C      -0.36067800   -0.79069200    0.54735100
C      -1.56702200   -0.19828100    0.30253700
C      -1.33506900    1.00294800   -0.49363500
C       2.06707900   -0.18575100   -0.11227500
H      -0.14550600   -1.69130300    1.10072200
H      -2.55279300   -0.50764400    0.61123600
H       2.62951400    0.58503800   -0.66944800
""",
)

entry(
    index = 121,
    label = "TB103",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,D}
3  C u0 p0 c0 {1,S} {6,D} {10,S}
4  C u0 p0 c0 {6,D} {7,S} {11,S}
5  O u0 p2 c0 {1,S} {2,S}
6  C u0 p0 c0 {3,D} {4,D}
7  O u0 p2 c0 {4,S} {12,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {2,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72404,0.0183752,0.000199915,-5.30785e-07,3.96116e-10,-17473.1,13.2674], Tmin=(10,'K'), Tmax=(481.165,'K')),
            NASAPolynomial(coeffs=[7.45271,0.0393823,-2.76931e-05,9.19286e-09,-1.14916e-12,-18433.9,-8.24924], Tmin=(481.165,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-145.332,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'C=O': 1, 'C-H': 3, 'C-C': 2, 'C=C': 2, 'H-O': 1}
1D rotors:
pivots: [2, 7], dihedral: [12, 2, 7, 8], rotor symmetry: 1, max scan energy: 23.48 kJ/mol
pivots: [4, 6], dihedral: [1, 4, 6, 8], rotor symmetry: 1, max scan energy: 17.26 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.47044600    0.50116500    0.02281600
O      -0.53473100   -3.42924700    3.62362000
O      -1.00481200    1.18875400   -1.68144700
C      -1.37867000   -0.61669300    0.11615900
C      -1.43430000    0.51994700   -0.80052300
C      -0.57790300   -0.61154800    1.35244600
C       0.11982600   -2.80557400    2.60018500
C      -0.24326300   -1.71120300    1.98288700
H      -1.76498700   -1.57452300   -0.21506600
H      -0.24153600    0.36259500    1.70582100
H       1.02625200   -3.33632400    2.32951800
H      -1.32628100   -2.92337300    3.84402900
""",
)

entry(
    index = 122,
    label = "TB104",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {5,S}
3  C u0 p0 c0 {1,S} {6,D} {9,S}
4  C u0 p0 c0 {2,D} {7,S} {10,S}
5  O u0 p2 c0 {1,S} {2,S}
6  C u0 p0 c0 {3,D} {11,D}
7  O u0 p2 c0 {4,S} {12,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 O u0 p2 c0 {6,D}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71245,0.0201234,0.000199667,-5.68489e-07,4.53976e-10,-16065.7,13.4358], Tmin=(10,'K'), Tmax=(449.266,'K')),
            NASAPolynomial(coeffs=[6.95835,0.0397177,-2.76639e-05,9.10684e-09,-1.12987e-12,-16846.7,-5.07328], Tmin=(449.266,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-133.606,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'C=O': 1, 'C-H': 3, 'C-C': 2, 'C=C': 2, 'H-O': 1}
1D rotors:
pivots: [2, 7], dihedral: [12, 2, 7, 5], rotor symmetry: 1, max scan energy: 14.87 kJ/mol
pivots: [4, 6], dihedral: [1, 4, 6, 8], rotor symmetry: 1, max scan energy: 18.84 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.79725600   -1.15423600   -1.07538700
O      -2.95515900    0.57359800    0.44029600
O       3.78782900   -1.48846100   -0.97718300
C       0.48481300   -0.35805000   -0.94492300
C      -0.78231900    0.05280300   -0.41865900
C       1.54183000   -0.93130800   -0.09631000
C      -1.62311500    0.83229400    0.23746400
C       2.73194800   -1.24125600   -0.56997300
H       0.80066000    0.03780500   -1.90551800
H       1.34908900   -1.15798900    0.94485900
H      -1.30226100    1.76675000    0.67460200
H      -3.17304700   -0.26778800    0.02267700
""",
)

entry(
    index = 123,
    label = "TB105",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {6,D}
3  C u0 p0 c0 {1,D} {5,S} {8,S}
4  C u0 p0 c0 {2,S} {9,D} {10,S}
5  C u1 p0 c0 {3,S} {11,D}
6  O u0 p2 c0 {2,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  O u0 p2 c0 {4,D}
10 H u0 p0 c0 {4,S}
11 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87092,0.00784007,0.000152153,-3.1427e-07,1.94438e-10,-35282.3,12.1193], Tmin=(10,'K'), Tmax=(537.6,'K')),
            NASAPolynomial(coeffs=[2.4848,0.0459779,-3.18938e-05,1.02368e-08,-1.2372e-12,-35535.4,14.2066], Tmin=(537.6,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-293.4,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 3, 'C-H': 3, 'C-C': 3, 'C=C': 1}
1D rotors:
* Invalidated! pivots: [4, 5], dihedral: [6, 4, 5, 1], invalidation reason: The rotor scan has a barrier of 286.21 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)The rotor scan has a barrier of 286.21 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)
pivots: [5, 7], dihedral: [1, 5, 7, 2], rotor symmetry: 1, max scan energy: 54.89 kJ/mol
* Invalidated! pivots: [6, 8], dihedral: [4, 6, 8, 3], invalidation reason: 
* Invalidated! pivots: [4, 6], dihedral: [5, 4, 6, 8], invalidation reason: The rotor scan has a barrier of 133.43 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)The rotor scan has a barrier of 133.43 kJ/mol, which is higher than the maximal barrier for rotation (40.00 kJ/mol)


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.44566000    0.05309000    1.47170800
O      -2.16174300   -0.31961400   -1.59444200
O       1.38040600    0.30623800    2.82731600
C       0.62094400   -0.01016700   -0.54328200
C      -0.61449100   -0.06096300    0.14122700
C       1.59705600    0.14161900    0.40028400
C      -1.95458800   -0.21256500   -0.39926600
C       0.96217100    0.18785900    1.71384000
H       0.71714200   -0.08283200   -1.61523600
H       2.66450100    0.22014700    0.26937100
H      -2.76569900   -0.22328600    0.35098200
""",
)

entry(
    index = 124,
    label = "TB106",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {7,D} {10,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {11,S}
7  C u0 p0 c0 {4,D} {12,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69241,0.0222472,0.000193915,-5.72958e-07,4.71625e-10,-20322.6,12.8236], Tmin=(10,'K'), Tmax=(435.696,'K')),
            NASAPolynomial(coeffs=[6.62646,0.0411505,-2.8981e-05,9.57604e-09,-1.18833e-12,-21013.3,-3.887], Tmin=(435.696,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-168.989,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'C=O': 1, 'C-H': 3, 'C-C': 2, 'C=C': 2, 'H-O': 1}
1D rotors:
pivots: [2, 4], dihedral: [12, 2, 4, 1], rotor symmetry: 1, max scan energy: 23.55 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 19.28 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -3.04244500   -1.61525900    1.09834900
O      -2.39173600    0.55749500    0.17039100
O      -2.26993400   -5.96819500   -2.39019700
C      -1.98891100   -0.61757400    0.72880000
C      -2.13254000   -1.89958800    0.11384000
C      -1.88079500   -2.87794100   -0.74820000
C      -2.67786400   -4.09825100   -0.81290200
C      -2.45619600   -5.08884300   -1.65268300
H      -1.28401700   -0.43483100    1.53134400
H      -1.04388300   -2.75450500   -1.42391000
H      -3.51353400   -4.23415600   -0.13525200
H      -2.90375400    0.36699800   -0.62496200
""",
)

entry(
    index = 125,
    label = "TB107",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {5,D}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {2,D} {4,S} {6,S}
6  C u0 p0 c0 {5,S} {7,D} {10,S}
7  C u0 p0 c0 {6,D} {11,S} {12,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6878,0.039642,-1.78459e-05,-1.2714e-09,2.15661e-12,-6227.23,13.5909], Tmin=(10,'K'), Tmax=(1177.49,'K')),
            NASAPolynomial(coeffs=[10.5673,0.0261341,-1.32014e-05,3.212e-09,-3.05495e-13,-8531,-23.6256], Tmin=(1177.49,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-51.7614,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-H': 5, 'C-C': 2, 'C=C': 1, 'O-O': 1, 'C=O': 1}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [3, 1, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [4, 5], dihedral: [1, 4, 5, 2], rotor symmetry: 1, max scan energy: 16.82 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [2, 5, 6, 7], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       2.53441600    0.16081600   -0.33405300
O       0.30273800   -2.19419500    1.22717700
O       2.83378300    1.00231600    0.64207500
C       1.27935700   -0.51056600   -0.08430200
C       1.34833800   -1.65351600    0.93894700
C       2.66684600   -2.05231400    1.49568000
C       2.74905500   -3.04779800    2.37963700
H       0.97810400   -0.92089100   -1.05028600
H       0.54939500    0.22547700    0.25372800
H       3.54668900   -1.51548000    1.16566600
H       1.85340600   -3.56850000    2.70069900
H       3.69837200   -3.36030100    2.79778700
""",
)

entry(
    index = 126,
    label = "BT108",
    molecule = 
"""
multiplicity 3
1  O u1 p2 c0 {3,S}
2  O u0 p2 c0 {4,D}
3  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
4  C u0 p0 c0 {2,D} {3,S} {6,S}
5  C u0 p0 c0 {6,D} {9,S} {10,S}
6  C u1 p0 c0 {4,S} {5,D}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75424,0.0328425,-1.73634e-05,1.53921e-09,9.79788e-13,22080.4,15.2191], Tmin=(10,'K'), Tmax=(1214.02,'K')),
            NASAPolynomial(coeffs=[10.2008,0.0190478,-9.519e-06,2.2835e-09,-2.13825e-13,19966.4,-19.3919], Tmin=(1214.02,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (183.601,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 1, 'C-H': 4, 'C-C': 2, 'C=C': 1, 'C=O': 1}
1D rotors:
pivots: [3, 4], dihedral: [1, 3, 4, 2], rotor symmetry: 1, max scan energy: 16.15 kJ/mol
pivots: [4, 6], dihedral: [2, 4, 6, 5], rotor symmetry: 1, max scan energy: 0.06 kJ/mol (set as a FreeRotor)


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.37497700   -1.50192400    0.25988100
O      -0.00084200    1.00632600   -1.81226800
C      -1.46624200   -0.40944000   -0.52244600
C      -0.13411600    0.35178600   -0.77503900
C       1.78687500    0.19834500    1.10178100
C       0.85892800    0.25121600    0.20416400
H      -2.10090200    0.31633600    0.03241400
H      -1.96364700   -0.57075700   -1.49357300
H       1.86552200    0.94450500    1.89213700
H       2.52940500   -0.59899300    1.10877600
""",
)

entry(
    index = 127,
    label = "TB109",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {6,S} {13,S}
3  O u0 p2 c0 {8,S} {14,S}
4  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
5  C u0 p0 c0 {1,S} {6,D} {8,S}
6  C u0 p0 c0 {2,S} {5,D} {7,S}
7  C u1 p0 c0 {4,S} {6,S} {11,S}
8  C u1 p0 c0 {3,S} {5,S} {12,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77309,0.0148273,0.000213238,-5.10494e-07,3.59032e-10,-18836.2,13.9037], Tmin=(10,'K'), Tmax=(488.721,'K')),
            NASAPolynomial(coeffs=[4.53884,0.0521983,-3.53993e-05,1.13759e-08,-1.38442e-12,-19432.2,5.42586], Tmin=(488.721,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-156.664,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (328.422,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 2, 'C-O': 4, 'C-H': 4, 'C-C': 3, 'C=C': 1}
1D rotors:
pivots: [2, 6], dihedral: [13, 2, 6, 5], rotor symmetry: 1, max scan energy: 23.30 kJ/mol
* Invalidated! pivots: [3, 8], dihedral: [14, 3, 8, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 8], dihedral: [1, 5, 8, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O       1.75324600   -2.45519300    1.23279300
O       4.78207100   -0.59423800    1.72070200
O       1.90282700   -0.04330800   -0.92744200
C       2.53438000   -3.43315100    1.96663300
C       2.54112200   -1.33124100    1.06293000
C       3.79321900   -1.52063600    1.68883700
C       3.84299200   -2.76811200    2.25009800
C       2.01391500   -0.14057100    0.43497900
H       1.96708600   -3.70827400    2.86597000
H       2.61489400   -4.33177200    1.33880700
H       4.65922300   -3.20478900    2.80339400
H       1.34959300    0.55436000    0.93684400
H       4.44435400    0.20925900    1.30208700
H       2.39900600   -0.77229200   -1.32238300
""",
)

entry(
    index = 128,
    label = "TB110",
    molecule = 
"""
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {7,S} {11,S} {12,S}
5  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {1,D} {2,S} {3,S}
7  C u0 p1 c0 {2,S} {4,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76784,0.0261388,5.30066e-05,-8.95734e-08,3.86145e-11,18890,11.4626], Tmin=(10,'K'), Tmax=(804.616,'K')),
            NASAPolynomial(coeffs=[2.51562,0.0513773,-2.94899e-05,8.14783e-09,-8.73186e-13,18476.1,13.407], Tmin=(804.616,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (157.068,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (353.365,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 8, 'C-C': 6, 'C=O': 1}
1D rotors:
pivots: [2, 5], dihedral: [6, 2, 5, 13], rotor symmetry: 3, max scan energy: 5.48 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.18953500    1.37830700    1.70425600
C      -0.74058200   -0.21264900   -0.08010600
C       1.58160200    0.01685100    0.67823100
C       1.49660500   -0.48943800   -0.77467000
C      -2.14930100    0.32720500   -0.28821100
C       0.16363000    0.53011700    0.92934700
C       0.07499200   -0.66416800   -1.22546200
H      -0.79859800   -1.24464000    0.35476400
H       2.32180300    0.79668700    0.85915100
H       1.78240000   -0.79578000    1.38584800
H       1.82723700    0.29230600   -1.48306400
H       2.12424400   -1.34875400   -1.02633900
H      -2.10545600    1.31213200   -0.75814500
H      -2.71886200   -0.33583200   -0.94029900
H      -2.66918400    0.43885700    0.66477500
""",
)

entry(
    index = 129,
    label = "TB111",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {5,D}
4  C u0 p0 c0 {1,S} {5,D} {11,S}
5  C u0 p0 c0 {3,D} {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86273,0.021641,1.21246e-05,-2.33741e-08,8.33946e-12,64076.2,9.59818], Tmin=(10,'K'), Tmax=(1077.35,'K')),
            NASAPolynomial(coeffs=[5.32326,0.0284213,-1.43058e-05,3.49457e-09,-3.35083e-13,63053.3,-0.843578], Tmin=(1077.35,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (532.79,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=C': 2, 'C-C': 3, 'C-H': 6}
1D rotors:
pivots: [2, 3], dihedral: [8, 2, 3, 1], rotor symmetry: 3, max scan energy: 3.86 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.25959600    1.44691400   -1.00963800
C      -1.68312400   -0.54078500    0.38207800
C      -0.50969100    0.15912700   -0.18799200
C       1.33069900    1.77189000   -0.27523800
C       0.67350800    0.65552600    0.07068200
H      -0.83747500    2.30872700   -0.69174100
H      -0.08323000    1.31357000   -2.07316600
H      -2.26569900   -1.05460000   -0.38707100
H      -1.34657700   -1.28945100    1.10244700
H      -2.35488400    0.14978400    0.90713700
H       2.16111500    1.70810600   -0.97847100
""",
)
