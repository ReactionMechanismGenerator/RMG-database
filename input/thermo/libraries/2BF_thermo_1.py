#!/usr/bin/env python
# encoding: utf-8

name = "2BF_thermo_1"
shortDesc = ""
longDesc = """
ARC v1.1.0
ARC project 2BF_thermo_1

Levels of theory used:

Conformers:       wb97xd/def2svp, software: gaussian (dft)
TS guesses:       None
Composite method: cbs-qb3, software: gaussian (composite) (using a fine grid)
Frequencies:      b3lyp/cbsb7, software: gaussian (dft)
Rotor scans:      b3lyp/cbsb7, software: gaussian (dft)
Using p-type bond additivity corrections for thermo

Using the following ESS settings: {'gaussian': ['local'], 'molpro': ['local']}

Considered the following species and TSs:
Species 2BF (run time: 7:28:34)
Species PB1 (run time: 11:55:01)
Species PB2 (run time: 15:32:24)
Species PB3 (run time: 13:53:07)
Species PB4 (run time: 9:32:33)
Species PB5 (run time: 13:28:23)
Species PB6 (run time: 13:07:14)
Species PB7 (run time: 14:18:18)
Species PB8 (run time: 11:12:09)
Species PB9 (run time: 16:56:00)
Species PB10 (run time: 15:16:22)
Species PB11 (run time: 17:20:40)
Species PB12 (run time: 21:02:50)
Species PB13 (run time: 1 day, 3:26:43)
Species PB14 (run time: 5:18:20)
Species PB15 (run time: 20:15:28)
Species PB16 (run time: 0:49:39)
Species PB17 (run time: 1:45:25)
Species PB18 (run time: 5:21:21)

Overall time since project initiation: 15:20:31
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

