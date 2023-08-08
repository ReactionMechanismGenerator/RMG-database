#!/usr/bin/env python
# encoding: utf-8

name = "SABIC_aromatics_1dHR_extended"
shortDesc = u"Species relevant to aromatics formation, up to Benzo[a]pyrene (C20H12)"
longDesc = u"""
CBS-QB3 calculations for most species obtained from SABIC
Rotor scans performed using ARC v1.0.0
Some species were rerun with ARC because the original CBS-QB3 optimized geometries had imaginary frequencies

Levels of theory used:

Conformers:       b97-d3/6-311+g(d,p)
TS guesses:       b3lyp/6-31+g(d,p)
Composite method: cbs-qb3 (using a fine grid)
Frequencies:      b3lyp/cbsb7
Rotor scans:      b3lyp/cbsb7
Using bond additivity corrections for thermo

NOTE: This extended library is similar to the SABIC_aromatics_1dHR library, but contains all of the species that
has at least one invalidated rotor scan job. It is not clear how much these invalidated rotors affect the 
accuracy of these species, and thus they have been included here in a separate library from the main one.
"""
entry(
    index = 0,
    label = "C10H8_9",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {9,S}
3  C u0 p0 c0 {1,B} {6,B} {14,S}
4  C u0 p0 c0 {2,B} {5,B} {11,S}
5  C u0 p0 c0 {4,B} {6,B} {12,S}
6  C u0 p0 c0 {3,B} {5,B} {13,S}
7  C u1 p0 c0 {1,S} {15,S} {16,S}
8  C u1 p0 c0 {10,S} {17,S} {18,S}
9  C u0 p0 c0 {2,S} {10,T}
10 C u0 p0 c0 {8,S} {9,T}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.48534,0.0905321,-7.93611e-05,3.6381e-08,-6.78067e-12,65837,38.6568], Tmin=(200,'K'), Tmax=(1247.6,'K')),
            NASAPolynomial(coeffs=[13.9392,0.0410799,-1.99058e-05,4.61129e-09,-4.14672e-13,61988.2,-39.1704], Tmin=(1247.6,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (544.986,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (424.038,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C:C': 6, 'C-C': 3, 'C#C': 1, 'C-H': 8}
1D rotors:
pivots: [1, 7], dihedral: [2, 1, 7, 15], rotor symmetry: 1, max scan energy: 1.52 kJ/mol
pivots: [2, 9], dihedral: [1, 2, 9, 10], rotor symmetry: 1, max scan energy: 1.52 kJ/mol
* Invalidated! pivots: [8, 10], dihedral: [17, 8, 10, 9], invalidation reason: scan job crashed
* Invalidated! pivots: [9, 10], dihedral: [2, 9, 10, 8], invalidation reason: scan job crashed


External symmetry: 1, optical isomers: 1

Geometry:
C      -0.06210800    1.09468000    0.00872000
H      -0.04079700    0.01151900    0.00497400
H       0.88435600    1.62190300    0.00455200
C      -1.24337700    1.77229500    0.01836800
C      -2.31092300    2.38183500    0.02709000
C      -3.55059200    3.06716200    0.03694600
C      -4.74545100    2.34563700    0.04147000
C      -5.98701200    2.99276900    0.05117500
C      -6.03984600    4.38367800    0.05648500
C      -4.86354800    5.12635600    0.05214600
C      -3.59105800    4.51040500    0.04237700
C      -2.41241700    5.28369300    0.03811900
H      -1.43691100    4.81884400    0.03061600
H      -2.46820800    6.36473600    0.04228800
H      -4.69849000    1.26328500    0.03733500
H      -6.89884600    2.40756000    0.05452800
H      -6.99717500    4.89235400    0.06402600
H      -4.91080900    6.20997800    0.05626500
""",
)

entry(
    index = 1,
    label = "C6H5O2_10",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,D} {5,S} {11,S}
5  C u0 p0 c0 {3,D} {4,S} {12,S}
6  O u0 p2 c0 {1,S} {7,S}
7  C u1 p0 c0 {6,S} {13,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.450451,0.0582732,-3.59733e-05,4.58127e-09,2.29423e-12,2955.52,30.9558], Tmin=(200,'K'), Tmax=(1070.09,'K')),
            NASAPolynomial(coeffs=[11.2319,0.028728,-1.43557e-05,3.4473e-09,-3.22334e-13,-353.329,-29.9743], Tmin=(1070.09,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (22.2373,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C=O': 1, 'C-O': 2, 'C-C': 3, 'C=C': 2, 'C-H': 5}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: scan has a barrier larger than 40 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 10.41 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.70214600    1.17181600    0.28594700
C       0.43015000    0.90709500    0.04471200
O       1.48236800    1.66485400   -0.13658300
C       1.26829000    3.13876500   -0.02602700
C       1.30604100    3.64489300    1.39428600
C       2.24833400    4.59483000    1.47811300
C       2.92558300    4.73590000    0.16877200
C       2.39192400    3.87016800   -0.70495300
H       0.29741100    3.34564000   -0.49065500
H       0.63003600    3.30503500    2.16484500
H       2.48909500    5.18145400    2.35493200
H       3.72584700    5.43589300   -0.03172400
H       2.66577800    3.70986600   -1.73726700
""",
)

entry(
    index = 2,
    label = "C10H10_59",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,B} {5,B}
4  C u0 p0 c0 {3,B} {6,B} {15,S}
5  C u0 p0 c0 {3,B} {8,B} {19,S}
6  C u0 p0 c0 {4,B} {7,B} {16,S}
7  C u0 p0 c0 {6,B} {8,B} {17,S}
8  C u0 p0 c0 {5,B} {7,B} {18,S}
9  C u0 p0 c0 {2,S} {10,T}
10 C u0 p0 c0 {9,T} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.32242,0.0924993,-7.0585e-05,2.77256e-08,-4.41731e-12,30827.7,37.0785], Tmin=(200,'K'), Tmax=(1441.44,'K')),
            NASAPolynomial(coeffs=[15.095,0.044166,-2.02882e-05,4.46339e-09,-3.82769e-13,25806.5,-53.3192], Tmin=(1441.44,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (253.205,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (473.925,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C=C': 3, 'C-C': 6, 'C#C': 1, 'C-H': 10}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: scan job crashed
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 24.06 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 2, max scan energy: 6.77 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -0.01619100   -1.25145400   -0.00441200
C      -0.03132000   -0.04978200    0.00288100
C      -0.01497100    1.40997800    0.01134500
C       1.42055400    1.99695100   -0.00168600
C       1.42115300    3.50872900    0.00683200
C       1.39111100    4.23220100   -1.19020000
C       1.35631500    5.62464300   -1.18475900
C       1.35133600    6.31910000    0.02306400
C       1.38343000    5.61137700    1.22272900
C       1.41826600    4.21894900    1.21212900
H      -0.01271300   -2.31361800   -0.01078200
H      -0.56739600    1.78697400   -0.85620000
H      -0.54720400    1.77661200    0.89578200
H       1.96151100    1.61452200    0.86795900
H       1.94148600    1.62462900   -0.88778900
H       1.40240400    3.69886600   -2.13586300
H       1.33825000    6.16723400   -2.12355300
H       1.32768000    7.40296200    0.02931500
H       1.38664600    6.14362000    2.16759700
H       1.45097400    3.67530600    2.15139200
""",
)

entry(
    index = 3,
    label = "C9H11_19",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
3  C u1 p0 c0 {1,S} {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,B} {6,B}
5  C u0 p0 c0 {4,B} {7,B} {16,S}
6  C u0 p0 c0 {4,B} {9,B} {20,S}
7  C u0 p0 c0 {5,B} {8,B} {17,S}
8  C u0 p0 c0 {7,B} {9,B} {18,S}
9  C u0 p0 c0 {6,B} {8,B} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.9449,0.0725295,-2.14256e-05,-1.71797e-08,9.92166e-12,15414,37.266], Tmin=(200,'K'), Tmax=(1028.13,'K')),
            NASAPolynomial(coeffs=[7.36139,0.0568353,-2.84554e-05,6.78396e-09,-6.23984e-13,12416.3,-13.162], Tmin=(1028.13,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (124.964,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (473.925,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C=C': 3, 'C-C': 6, 'C-H': 11}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 0.60 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 13], rotor symmetry: 3, max scan energy: 0.60 kJ/mol
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 5], invalidation reason: scan has a barrier larger than 40 kJ/mol


External symmetry: 2, optical isomers: 1

Geometry:
C      -0.05714400    1.49776900    0.22551600
C      -0.02828700    0.00691700    0.03634300
C      -1.33036800   -0.74392200    0.01922500
C       1.21142400   -0.68251000   -0.12235400
C       1.26593100   -2.09324200   -0.30686400
C       2.47188600   -2.75746400   -0.45918300
C       3.68040200   -2.05613000   -0.43627100
C       3.65861300   -0.67029700   -0.25718800
C       2.45849600    0.00422400   -0.10382600
H       0.48853300    1.80889900    1.12606200
H       0.40734500    2.02885200   -0.61544500
H      -1.07999000    1.86524400    0.31974800
H      -2.17716300   -0.07073900    0.15969800
H      -1.48657700   -1.27591000   -0.92839200
H      -1.37835900   -1.50318700    0.81064200
H       0.34675700   -2.66479700   -0.32980200
H       2.47480700   -3.83341600   -0.59761400
H       4.62172200   -2.57978300   -0.55584300
H       4.58977600   -0.11405100   -0.23755000
H       2.47520800    1.07798300    0.03359800
""",
)

entry(
    index = 4,
    label = "C10H9_17",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {12,S}
4  C u0 p0 c0 {2,B} {7,B} {16,S}
5  C u0 p0 c0 {3,B} {6,B} {13,S}
6  C u0 p0 c0 {5,B} {7,B} {14,S}
7  C u0 p0 c0 {4,B} {6,B} {15,S}
8  C u1 p0 c0 {1,S} {17,S} {18,S}
9  C u0 p0 c0 {1,S} {10,T}
10 C u0 p0 c0 {9,T} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.51732,0.0918381,-7.21119e-05,2.78684e-08,-4.03292e-12,56769.3,42.4758], Tmin=(200,'K'), Tmax=(1169.99,'K')),
            NASAPolynomial(coeffs=[14.4154,0.0426081,-2.00986e-05,4.55728e-09,-4.03656e-13,52214.3,-44.4061], Tmin=(1169.99,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (468.739,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 6, 'C=C': 3, 'C#C': 1, 'C-H': 9}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: scan job crashed
pivots: [3, 7], dihedral: [2, 3, 7, 8], rotor symmetry: 1, max scan energy: 6.49 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 2.23 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       0.30904400   -1.24789300   -0.07055500
C       0.13923500   -0.05863100   -0.06104300
C      -0.04701400    1.39563900   -0.04226100
C       1.26366500    2.12362300    0.08996500
H       2.16460700    1.70743600   -0.34060900
H       1.26318000    3.15497300    0.41927300
C      -0.80744400    1.91248300   -1.27803700
C      -0.48331900    1.46906300   -2.56333000
C      -1.14362400    1.98534400   -3.67409500
C      -2.13411400    2.95402900   -3.51603000
C      -2.46197900    3.40033500   -2.23851700
C      -1.80103500    2.88178500   -1.12658000
H       0.44995800   -2.30074800   -0.07507100
H      -0.66711700    1.63821700    0.83044200
H       0.27760400    0.70719300   -2.68956200
H      -0.88738700    1.62821100   -4.66545300
H      -2.64917100    3.35369500   -4.38221200
H      -3.23602500    4.14791300   -2.10469300
H      -2.06447100    3.23012300   -0.13275100
""",
)

entry(
    index = 5,
    label = "C10H9_14",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {10,S}
3  C u0 p0 c0 {1,B} {6,B} {14,S}
4  C u0 p0 c0 {2,B} {5,B} {11,S}
5  C u0 p0 c0 {4,B} {6,B} {12,S}
6  C u0 p0 c0 {3,B} {5,B} {13,S}
7  C u0 p0 c0 {1,S} {8,D} {15,S}
8  C u0 p0 c0 {7,D} {16,S} {17,S}
9  C u0 p0 c0 {10,D} {18,S} {19,S}
10 C u1 p0 c0 {2,S} {9,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.67371,0.0937313,-7.29322e-05,2.7396e-08,-3.73124e-12,48340.3,39.7306], Tmin=(200,'K'), Tmax=(1162.19,'K')),
            NASAPolynomial(coeffs=[14.7312,0.0436174,-2.08876e-05,4.78985e-09,-4.27577e-13,43633.6,-49.6986], Tmin=(1162.19,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (398.57,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (453.139,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C=C': 5, 'C-C': 5, 'C-H': 9}
1D rotors:
pivots: [8, 9], dihedral: [3, 8, 9, 10], rotor symmetry: 1, max scan energy: 19.91 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: scan job crashed
* Invalidated! pivots: [9, 10], dihedral: [8, 9, 10, 18], invalidation reason: scan has a barrier larger than 40 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.53091500    1.02061600    0.10134800
C       0.48230800    0.21517500    0.00738700
C       1.57655700   -0.59835300   -0.05784300
C       2.88377300   -0.00358900   -0.11311900
C       4.01506500   -0.78126500   -0.17231400
C       3.91011700   -2.18376800   -0.18698900
C       2.65795000   -2.78524000   -0.13868800
C       1.47478100   -2.04480100   -0.06786700
C       0.15709500   -2.67842500   -0.01633300
C      -0.11111100   -3.96697400    0.23078000
H      -0.91720300    1.35572700    1.06563500
H      -1.05296100    1.40284500   -0.77725400
H       2.95401000    1.07718900   -0.10519700
H       4.99057300   -0.30984100   -0.21419000
H       4.80227900   -2.79580900   -0.24652100
H       2.59472400   -3.86658300   -0.17510300
H      -0.68220300   -2.01001800   -0.18593900
H      -1.13245900   -4.32780700    0.23372900
H       0.65945000   -4.69888000    0.44588800
""",
)

entry(
    index = 6,
    label = "C10H9_13",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {4,B} {5,B}
3  C u1 p0 c0 {1,S} {2,S} {13,S}
4  C u0 p0 c0 {2,B} {6,B} {14,S}
5  C u0 p0 c0 {2,B} {8,B} {18,S}
6  C u0 p0 c0 {4,B} {7,B} {15,S}
7  C u0 p0 c0 {6,B} {8,B} {16,S}
8  C u0 p0 c0 {5,B} {7,B} {17,S}
9  C u0 p0 c0 {1,S} {10,T}
10 C u0 p0 c0 {9,T} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.50377,0.0885307,-6.00534e-05,1.53205e-08,2.02933e-13,50082.8,39.3902], Tmin=(200,'K'), Tmax=(1087.78,'K')),
            NASAPolynomial(coeffs=[13.3951,0.0455479,-2.21293e-05,5.16093e-09,-4.68936e-13,45708,-42.8605], Tmin=(1087.78,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (413.082,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (453.139,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 6, 'C=C': 3, 'C#C': 1, 'C-H': 9}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: scan job crashed
pivots: [3, 4], dihedral: [2, 3, 4, 6], rotor symmetry: 1, max scan energy: 13.86 kJ/mol
* Invalidated! pivots: [4, 6], dihedral: [3, 4, 6, 7], invalidation reason: scan has a barrier larger than 40 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       0.03394700   -1.29148000   -0.00503200
C       0.00849100   -0.09093600    0.00275700
C      -0.01317000    1.36993800    0.01197600
C       1.35743700    1.99259100   -0.00103900
H       2.20833900    1.32208700   -0.01555400
C       1.59323000    3.38444400    0.00485100
C       0.54534800    4.34784200    0.02331800
C       0.82385000    5.70483600    0.02865200
C       2.14481200    6.16216600    0.01598200
C       3.19383900    5.23517500   -0.00232700
C       2.92911300    3.87840000   -0.00784600
H       0.05230300   -2.35348700   -0.01178300
H      -0.59834500    1.72023700   -0.85162400
H      -0.57674400    1.70960400    0.89399500
H      -0.48713900    4.01886400    0.03337800
H       0.00719800    6.41845100    0.04279100
H       2.35471500    7.22530800    0.02028300
H       4.22114500    5.58253000   -0.01227600
H       3.74681100    3.16553100   -0.02201100
""",
)

entry(
    index = 7,
    label = "C10H9_12",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {11,S}
3  C u0 p0 c0 {1,B} {6,B} {15,S}
4  C u0 p0 c0 {2,B} {5,B} {12,S}
5  C u0 p0 c0 {4,B} {6,B} {13,S}
6  C u0 p0 c0 {3,B} {5,B} {14,S}
7  C u0 p0 c0 {1,S} {10,D} {17,S}
8  C u0 p0 c0 {9,D} {10,S} {16,S}
9  C u0 p0 c0 {8,D} {18,S} {19,S}
10 C u1 p0 c0 {7,D} {8,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.35351,0.0841632,-4.74975e-05,3.44028e-09,3.97002e-12,51836.7,39.9921], Tmin=(200,'K'), Tmax=(1068.04,'K')),
            NASAPolynomial(coeffs=[12.4292,0.0481197,-2.40106e-05,5.71677e-09,-5.2732e-13,47577,-37.4576], Tmin=(1068.04,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (427.683,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (453.139,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C=C': 5, 'C-C': 5, 'C-H': 9}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: scan job crashed
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 2, max scan energy: 24.48 kJ/mol
* Invalidated! pivots: [1, 2], dihedral: [11, 1, 2, 3], invalidation reason: scan job crashed


External symmetry: 1, optical isomers: 2

Geometry:
C       0.00548800    1.40352900    0.00809500
C      -0.06468900    0.06450700    0.00597400
C       1.04621700   -0.82409400   -0.01129500
C       1.27931500   -2.12932800   -0.02297200
C       2.58095600   -2.80240400   -0.03804300
C       3.79060500   -2.08599700   -0.04077200
C       5.00819500   -2.75155400   -0.05497600
C       5.05012400   -4.14749000   -0.06689100
C       3.85992700   -4.87044800   -0.06439700
C       2.63823300   -4.20431000   -0.05012400
H       0.95914200    1.91819900   -0.00392400
H      -0.89062600    2.01130000    0.02197900
H      -1.05025600   -0.41221200    0.01899100
H       0.40702600   -2.79480500   -0.02168700
H       3.76048400   -1.00219800   -0.03161500
H       5.93146400   -2.18263700   -0.05686300
H       6.00302900   -4.66424700   -0.07802900
H       3.88207900   -5.95451200   -0.07354400
H       1.71387600   -4.77290000   -0.04823500
""",
)

entry(
    index = 8,
    label = "C10H10_67",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {9,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {8,D}
4  C u0 p0 c0 {1,S} {6,D} {14,S}
5  C u0 p0 c0 {3,S} {7,D} {17,S}
6  C u0 p0 c0 {4,D} {7,S} {15,S}
7  C u0 p0 c0 {5,D} {6,S} {16,S}
8  C u0 p0 c0 {3,D} {18,S} {19,S}
9  C u0 p0 c0 {2,S} {10,T}
10 C u0 p0 c0 {9,T} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.96043,0.0975681,-7.50647e-05,2.77033e-08,-3.60342e-12,46312.9,39.5848], Tmin=(200,'K'), Tmax=(1144.85,'K')),
            NASAPolynomial(coeffs=[14.8327,0.046203,-2.19192e-05,4.99766e-09,-4.45028e-13,41530.9,-51.7557], Tmin=(1144.85,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (381.568,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (478.082,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 6, 'C=C': 3, 'C#C': 1, 'C-H': 10}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: scan job crashed
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 26.55 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       3.71834600   -0.07120100    0.02378100
C       2.59495700    0.24322500    0.31339000
C       1.22760000    0.63683200    0.63718700
C       0.18969700    0.28511300   -0.48634200
C       0.14371100   -1.21103000   -0.67697500
C      -0.87957500   -1.95083000   -0.22975100
C      -2.03763700   -1.32977100    0.40156300
C      -2.16975700    0.01085600    0.44604500
C      -1.16493400    0.89570000   -0.13192500
C      -1.40934900    2.20271300   -0.32237000
H       4.71431600   -0.34796500   -0.22069600
H       0.91328200    0.15762800    1.57005000
H       1.19059900    1.71800300    0.80662000
H       0.56007100    0.75344300   -1.40365900
H       1.00981500   -1.67516700   -1.13495300
H      -0.86356800   -3.03023000   -0.33621700
H      -2.81463800   -1.96844500    0.80718600
H      -3.05983400    0.46507500    0.86954300
H      -2.34865800    2.65016800   -0.01663400
H      -0.68504300    2.85768300   -0.79454500
""",
)

entry(
    index = 9,
    label = "C10H11_26",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
2  C u0 p0 c0 {4,S} {5,B} {6,B}
3  C u0 p0 c0 {1,S} {7,D} {14,S}
4  C u1 p0 c0 {2,S} {7,S} {15,S}
5  C u0 p0 c0 {2,B} {8,B} {17,S}
6  C u0 p0 c0 {2,B} {10,B} {21,S}
7  C u0 p0 c0 {3,D} {4,S} {16,S}
8  C u0 p0 c0 {5,B} {9,B} {18,S}
9  C u0 p0 c0 {8,B} {10,B} {19,S}
10 C u0 p0 c0 {6,B} {9,B} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.44165,0.0862879,-4.27917e-05,-1.09326e-09,5.16359e-12,23061.1,38.8924], Tmin=(200,'K'), Tmax=(1067.02,'K')),
            NASAPolynomial(coeffs=[10.5853,0.0566736,-2.81805e-05,6.65977e-09,-6.08332e-13,19186.9,-29.9273], Tmin=(1067.02,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (188.405,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C=C': 4, 'C-C': 6, 'C-H': 11}
1D rotors:
pivots: [1, 2], dihedral: [12, 1, 2, 3], rotor symmetry: 3, max scan energy: 5.67 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 6], invalidation reason: scan has a barrier larger than 40 kJ/mol
pivots: [4, 6], dihedral: [3, 4, 6, 7], rotor symmetry: 2, max scan energy: 35.91 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: scan has a barrier larger than 40 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -4.44427200    0.45045900    0.00002900
C      -3.21636700   -0.40147400    0.00004600
C      -1.93367200    0.07594700    0.00002400
C      -0.78420400   -0.73281500    0.00002900
H      -0.94189000   -1.80883700    0.00005300
C       0.58378200   -0.29827200    0.00000700
C       0.97554600    1.06322600   -0.00000500
C       2.31421100    1.42247500   -0.00002400
C       3.31486200    0.44691200   -0.00002800
C       2.95372100   -0.90188100   -0.00001100
C       1.61655700   -1.26748400    0.00000900
H      -4.19744800    1.51493300    0.00002600
H      -5.07096200    0.24815400    0.87759600
H      -5.07094100    0.24814900   -0.87755400
H      -3.36673300   -1.47952300    0.00007100
H      -1.80561900    1.15647200   -0.00000400
H       0.22207800    1.84160000    0.00000200
H       2.58546600    2.47275000   -0.00003600
H       4.35976600    0.73493500   -0.00004100
H       3.72079800   -1.66862200   -0.00001200
H       1.34541900   -2.31830800    0.00002200
""",
)

entry(
    index = 10,
    label = "C9H9_23",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {8,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {3,B} {4,B} {9,S}
3  C u0 p0 c0 {2,B} {5,B} {14,S}
4  C u0 p0 c0 {2,B} {7,B} {18,S}
5  C u0 p0 c0 {3,B} {6,B} {15,S}
6  C u0 p0 c0 {5,B} {7,B} {16,S}
7  C u0 p0 c0 {4,B} {6,B} {17,S}
8  C u0 p0 c0 {1,S} {9,D} {13,S}
9  C u1 p0 c0 {2,S} {8,D}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.55363,0.0757967,-4.39338e-05,6.26638e-09,2.10608e-12,37724.9,35.1285], Tmin=(200,'K'), Tmax=(1081.57,'K')),
            NASAPolynomial(coeffs=[10.3102,0.0461588,-2.25764e-05,5.27355e-09,-4.77833e-13,34325.8,-26.8877], Tmin=(1081.57,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (310.821,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 5, 'C=C': 4, 'C-H': 9}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 3], rotor symmetry: 3, max scan energy: 6.31 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: scan job crashed


External symmetry: 1, optical isomers: 1

Geometry:
C       0.35567600    1.49194500   -0.01261900
C      -0.52036000    0.29239000   -0.30678900
C      -0.11037000   -0.92749400   -0.48797000
C       0.22306900   -2.24135600   -0.69393100
C       0.30060500   -3.16878300    0.39543000
C       0.64377600   -4.48815300    0.17445000
C       0.92542200   -4.95062100   -1.11786400
C       0.85708400   -4.06153800   -2.19865100
C       0.51659900   -2.73708000   -2.00573500
H       0.07337600    1.94800500    0.94197400
H       1.40904700    1.21341500    0.03358400
H       0.23083000    2.25699300   -0.78599700
H      -1.59417200    0.50133000   -0.36630600
H       0.08319300   -2.81467500    1.39586500
H       0.69456100   -5.17302000    1.01402100
H       1.19432900   -5.98758100   -1.28002800
H       1.07348800   -4.41520100   -3.20093500
H       0.46473700   -2.05237600   -2.84359000
""",
)

entry(
    index = 11,
    label = "C9H9_25",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,B} {4,B}
2  C u0 p0 c0 {1,S} {8,S} {9,D}
3  C u0 p0 c0 {1,B} {5,B} {10,S}
4  C u0 p0 c0 {1,B} {7,B} {14,S}
5  C u0 p0 c0 {3,B} {6,B} {11,S}
6  C u0 p0 c0 {5,B} {7,B} {12,S}
7  C u0 p0 c0 {4,B} {6,B} {13,S}
8  C u1 p0 c0 {2,S} {17,S} {18,S}
9  C u0 p0 c0 {2,D} {15,S} {16,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.76925,0.0743788,-3.46571e-05,-5.6145e-09,6.5632e-12,30293.9,35.3594], Tmin=(200,'K'), Tmax=(1054.48,'K')),
            NASAPolynomial(coeffs=[11.6804,0.0443782,-2.18801e-05,5.21055e-09,-4.84869e-13,26288.9,-35.7816], Tmin=(1054.48,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (248.819,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 5, 'C=C': 4, 'C-H': 9}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [2, 1, 4, 5], invalidation reason: scan has a barrier larger than 40 kJ/mol
pivots: [4, 6], dihedral: [1, 4, 6, 7], rotor symmetry: 1, max scan energy: 10.09 kJ/mol


External symmetry: 2, optical isomers: 2

Geometry:
C      -0.00953400    1.09481500    0.27531600
H       0.01931800    0.02424200    0.42919800
H       0.93064800    1.63276700    0.30230300
C      -1.20131400    1.76320400    0.01818300
C      -1.22230600    3.12947000   -0.23957500
C      -2.48615700    0.99795100    0.01921300
C      -2.76507700    0.06474800    1.02625400
C      -3.96190400   -0.64641400    1.02907300
C      -4.90235800   -0.44060900    0.02203800
C      -4.63675700    0.48324200   -0.98642900
C      -3.44096500    1.19618800   -0.98660600
H      -0.30163000    3.70005300   -0.26764000
H      -2.15034800    3.66406000   -0.39318500
H      -2.04654400   -0.08808000    1.82370000
H      -4.16245400   -1.35768000    1.82273600
H      -5.83401100   -0.99508800    0.02310400
H      -5.35899600    0.64536700   -1.77897300
H      -3.23363100    1.89969500   -1.78510000
""",
)

entry(
    index = 12,
    label = "C10H9_27",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {10,S}
2  C u0 p0 c0 {1,B} {4,B} {12,S}
3  C u0 p0 c0 {1,B} {6,B} {16,S}
4  C u0 p0 c0 {2,B} {5,B} {13,S}
5  C u0 p0 c0 {4,B} {6,B} {14,S}
6  C u0 p0 c0 {3,B} {5,B} {15,S}
7  C u0 p0 c0 {8,S} {9,D} {11,S}
8  C u0 p0 c0 {7,S} {10,D} {17,S}
9  C u0 p0 c0 {7,D} {18,S} {19,S}
10 C u1 p0 c0 {1,S} {8,D}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.86746,0.0901843,-5.66132e-05,8.27007e-09,3.15501e-12,48806.6,41.0257], Tmin=(200,'K'), Tmax=(1069.61,'K')),
            NASAPolynomial(coeffs=[15.1851,0.0440046,-2.17662e-05,5.19572e-09,-4.84354e-13,43724.6,-52.9863], Tmin=(1069.61,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (402.204,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (453.139,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 5, 'C=C': 5, 'C-H': 9}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 28.03 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: scan job crashed


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.61199400    1.08810900    0.03366700
C       0.22813600    0.10029300    0.35438400
C       1.21665400   -0.46080800   -0.57157000
C       2.05546200   -1.42588600   -0.29381100
C       2.99392000   -2.41476400   -0.15531000
C       4.31860100   -2.12145000    0.30528100
C       5.25193300   -3.12892900    0.45068500
C       4.92552600   -4.45874600    0.15451300
C       3.63558600   -4.76944900   -0.29505600
C       2.68249400   -3.78194300   -0.44962300
H      -0.60762400    1.53863000   -0.95391600
H      -1.32860500    1.47612100    0.74719200
H       0.20270200   -0.33303200    1.35016600
H       1.23224100   -0.01648700   -1.57302300
H       4.57333800   -1.09418200    0.53567400
H       6.24968200   -2.88407300    0.79829100
H       5.66526300   -5.24143000    0.27296900
H       3.37905300   -5.79756500   -0.52628800
H       1.68573300   -4.02511900   -0.79691600
""",
)

entry(
    index = 13,
    label = "C9H9_20",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {4,B} {7,S}
2  C u0 p0 c0 {1,B} {3,B} {8,S}
3  C u0 p0 c0 {2,B} {5,B} {10,S}
4  C u0 p0 c0 {1,B} {6,B} {13,S}
5  C u0 p0 c0 {3,B} {6,B} {11,S}
6  C u0 p0 c0 {4,B} {5,B} {12,S}
7  C u0 p0 c0 {1,S} {9,D} {14,S}
8  C u1 p0 c0 {2,S} {15,S} {16,S}
9  C u0 p0 c0 {7,D} {17,S} {18,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.92609,0.0778476,-4.30634e-05,1.84054e-09,4.27672e-12,30954.9,35.754], Tmin=(200,'K'), Tmax=(1059.25,'K')),
            NASAPolynomial(coeffs=[12.2091,0.0434449,-2.12174e-05,5.00354e-09,-4.61398e-13,26895.8,-38.279], Tmin=(1059.25,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (254.27,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 5, 'C=C': 4, 'C-H': 9}
1D rotors:
pivots: [9, 10], dihedral: [4, 9, 10, 11], rotor symmetry: 1, max scan energy: 13.28 kJ/mol
* Invalidated! pivots: [1, 4], dihedral: [2, 1, 4, 5], invalidation reason: scan has a barrier larger than 40 kJ/mol
* Invalidated! pivots: [10, 11], dihedral: [9, 10, 11, 17], invalidation reason: scan has a barrier larger than 40 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.03747400    1.03862500   -0.08919600
H       0.03052400   -0.03915400   -0.11785600
H       0.88782200    1.59546400   -0.16843600
C      -1.25829800    1.71791600    0.01287700
C      -1.26719800    3.14552400   -0.03938300
C      -2.43940400    3.86857500    0.00045800
C      -3.66804900    3.20065300    0.10697200
C      -3.69496400    1.81053600    0.17987800
C      -2.52811400    1.04357600    0.13569700
C      -2.59348500   -0.42027400    0.24569600
C      -3.59262300   -1.19677800   -0.18563800
H      -0.31546000    3.65893800   -0.12586600
H      -2.41131100    4.95157200   -0.04409600
H      -4.59344300    3.76291100    0.15364800
H      -4.64526800    1.30544000    0.30948900
H      -1.74642400   -0.90196800    0.72627200
H      -4.45234300   -0.79506900   -0.71099500
H      -3.57079600   -2.26978800   -0.03642300
""",
)

entry(
    index = 14,
    label = "C10H10_74",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {4,S}
2  C u0 p0 c0 {1,D} {6,S} {14,S}
3  C u0 p0 c0 {1,S} {7,D} {15,S}
4  C u0 p0 c0 {1,S} {8,D} {18,S}
5  C u0 p0 c0 {6,D} {9,S} {12,S}
6  C u0 p0 c0 {2,S} {5,D} {13,S}
7  C u0 p0 c0 {3,D} {8,S} {16,S}
8  C u0 p0 c0 {4,D} {7,S} {17,S}
9  C u0 p0 c0 {5,S} {10,D} {11,S}
10 C u0 p0 c0 {9,D} {19,S} {20,S}
11 H u0 p0 c0 {9,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.89157,0.0883178,-4.36593e-05,-4.95747e-09,7.38486e-12,37007,39.3974], Tmin=(200,'K'), Tmax=(1061.72,'K')),
            NASAPolynomial(coeffs=[14.2883,0.0492916,-2.48297e-05,6.01638e-09,-5.67072e-13,31910.5,-51.3358], Tmin=(1061.72,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (304.025,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (478.082,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C=C': 5, 'C-C': 5, 'C-H': 10}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 36.14 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: scan has a barrier larger than 40 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       0.01341900    1.48180900    0.00898000
C       0.00104500    0.14123500    0.00069900
C       1.18861700   -0.68178500   -0.01335500
C       1.18090300   -2.03607700   -0.02170700
C       2.37441800   -2.83198900   -0.03563700
C       2.43491900   -4.19167300   -0.04446400
C       1.33148200   -5.15931300   -0.04190700
C       1.87140200   -6.40256800   -0.05372700
C       3.33635300   -6.29078500   -0.06431100
C       3.67195800   -4.97825300   -0.05875800
H       0.94440700    2.03966100    0.00545000
H      -0.90337200    2.05826200    0.01951600
H      -0.95315300   -0.38130100    0.00464600
H       2.14527100   -0.16212600   -0.01732100
H       0.22537800   -2.55319400   -0.01774000
H       3.31603600   -2.28615300   -0.03944100
H       0.27995200   -4.91421900   -0.03227000
H       1.32542300   -7.33660100   -0.05527900
H       4.01841800   -7.13013000   -0.07471600
H       4.66601600   -4.55380000   -0.06375800
""",
)

entry(
    index = 15,
    label = "C10H11_16",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {5,D}
3  C u1 p0 c0 {1,S} {6,S} {13,S}
4  C u0 p0 c0 {2,S} {7,D} {16,S}
5  C u0 p0 c0 {2,D} {8,S} {17,S}
6  C u0 p0 c0 {3,S} {8,D} {19,S}
7  C u0 p0 c0 {4,D} {9,S} {15,S}
8  C u0 p0 c0 {5,S} {6,D} {18,S}
9  C u0 p0 c0 {7,S} {10,D} {14,S}
10 C u0 p0 c0 {9,D} {20,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.99732,0.0895883,-3.98528e-05,-9.24973e-09,8.73874e-12,32562.9,40.2924], Tmin=(200,'K'), Tmax=(1057.72,'K')),
            NASAPolynomial(coeffs=[13.3743,0.0542282,-2.7363e-05,6.61226e-09,-6.20121e-13,27614.2,-46.6314], Tmin=(1057.72,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (267.015,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 6, 'C=C': 4, 'C-H': 11}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 40.00 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: scan job crashed
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: scan has a barrier larger than 40 kJ/mol
* Invalidated! pivots: [1, 2], dihedral: [12, 1, 2, 3], invalidation reason: scan has a barrier larger than 40 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       0.16677000    1.39086500    0.00619100
C       0.04615300    0.04996100    0.00261700
C      -1.20134400   -0.66398700    0.00991100
C      -1.29396100   -2.03072300    0.00585200
C      -2.48626800   -2.80110800    0.01239400
C      -2.42234200   -4.20156900    0.00693100
C      -3.55276300   -5.00147100    0.01273700
C      -4.85937300   -4.41031600    0.02473300
C      -5.01183000   -3.06776900    0.03070800
H      -6.00304100   -2.62640500    0.03969800
C      -3.84201700   -2.12675600    0.02529400
H       1.13610100    1.87368600    0.00022600
H      -0.70476400    2.03766800    0.01516800
H       0.95031200   -0.55652400   -0.00649000
H      -2.10618000   -0.06200000    0.01907300
H      -0.36301700   -2.59548400   -0.00341100
H      -1.44165600   -4.66821400   -0.00229600
H      -3.45420400   -6.08034800    0.00821800
H      -5.73036100   -5.05698100    0.02895500
H      -3.91289800   -1.45389500    0.89566600
H      -3.92621900   -1.44733100   -0.83875700
""",
)

entry(
    index = 16,
    label = "C10H11_11",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u1 p0 c0 {1,S} {5,S} {12,S}
3  C u0 p0 c0 {1,S} {6,D} {13,S}
4  C u0 p0 c0 {1,S} {7,D} {14,S}
5  C u0 p0 c0 {2,S} {8,D} {17,S}
6  C u0 p0 c0 {3,D} {7,S} {18,S}
7  C u0 p0 c0 {4,D} {6,S} {19,S}
8  C u0 p0 c0 {5,D} {9,S} {16,S}
9  C u0 p0 c0 {8,S} {10,D} {15,S}
10 C u0 p0 c0 {9,D} {20,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.22007,0.102008,-7.91366e-05,3.03042e-08,-4.34606e-12,41295.1,41.9577], Tmin=(200,'K'), Tmax=(1170.04,'K')),
            NASAPolynomial(coeffs=[15.1908,0.048569,-2.28098e-05,5.15129e-09,-4.54767e-13,36336.3,-52.5351], Tmin=(1170.04,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (339.733,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C=C': 4, 'C-C': 6, 'C-H': 11}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: scan has a barrier larger than 40 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 7], invalidation reason: scan has a barrier larger than 40 kJ/mol
pivots: [5, 7], dihedral: [4, 5, 7, 8], rotor symmetry: 1, max scan energy: 13.47 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: scan has a barrier larger than 40 kJ/mol
* Invalidated! pivots: [1, 2], dihedral: [12, 1, 2, 3], invalidation reason: scan has a barrier larger than 40 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.05890300    1.56036500   -0.33916300
C      -0.12859500    0.20693300   -0.47565700
C      -1.07842400   -0.62588900    0.15636300
C      -1.12966700   -2.02704500   -0.00292700
C      -2.03953800   -2.85117700    0.59418700
H      -2.79695900   -2.42606800    1.24858200
C      -2.09200500   -4.34400200    0.41718300
C      -1.99485200   -5.10534300    1.72464500
C      -3.08120200   -5.88351300    1.87560800
C      -3.96695400   -5.71229600    0.71573500
C      -3.41660600   -4.83086200   -0.13777300
H       0.69518000    2.14320100   -0.85262300
H      -0.75867100    2.10025400    0.29001500
H       0.59958900   -0.28282000   -1.12055200
H      -1.81576300   -0.15719100    0.80473900
H      -0.38163500   -2.47709700   -0.65541200
H      -1.27634500   -4.65479700   -0.25191000
H      -1.16339600   -4.99972300    2.40776500
H      -3.28529000   -6.54167000    2.71072200
H      -4.90953900   -6.22819800    0.58311300
H      -3.82372600   -4.48627100   -1.07833100
""",
)

entry(
    index = 17,
    label = "C9H9_8",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
2  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,D} {13,S}
4  C u0 p0 c0 {1,S} {6,D} {14,S}
5  C u0 p0 c0 {3,D} {7,S} {16,S}
6  C u0 p0 c0 {4,D} {7,S} {17,S}
7  C u1 p0 c0 {5,S} {6,S} {15,S}
8  C u0 p0 c0 {2,S} {9,T}
9  C u0 p0 c0 {8,T} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.14196,0.082062,-5.22524e-05,9.63434e-09,1.91754e-12,48916.1,37.2025], Tmin=(200,'K'), Tmax=(1070.29,'K')),
            NASAPolynomial(coeffs=[13.0429,0.0423924,-2.05942e-05,4.82576e-09,-4.42126e-13,44687.4,-41.6576], Tmin=(1070.29,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (403.531,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 6, 'C=C': 2, 'C#C': 1, 'C-H': 9}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: scan job crashed
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 21.68 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.09397700   -1.27190200    0.14432900
C      -0.08500600   -0.07192500    0.07538900
C      -0.04415600    1.38405400   -0.00006400
C       1.41474300    1.96909100   -0.04921100
C       2.15539500    1.51285100   -1.27445800
C       2.70301200    2.38695400   -2.16588800
C       2.61568200    3.78838000   -1.97943700
H       3.05676200    4.46487200   -2.70075900
C       1.94844500    4.29661100   -0.83831000
C       1.38287900    3.46623100    0.08299200
H      -0.11412800   -2.33218100    0.20559600
H      -0.58909200    1.72769700   -0.88487000
H      -0.55640700    1.80450400    0.87236700
H       1.91268100    1.54560500    0.84083700
H       2.23033500    0.44311800   -1.43485000
H       3.21936900    2.00221100   -3.03962900
H       1.89187000    5.37090700   -0.69396300
H       0.88260400    3.87742300    0.95452800
""",
)

entry(
    index = 18,
    label = "C9H9_9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,S} {4,B}
2  C u0 p0 c0 {1,B} {5,B} {12,S}
3  C u0 p0 c0 {1,S} {8,D} {11,S}
4  C u0 p0 c0 {1,B} {7,B} {16,S}
5  C u0 p0 c0 {2,B} {6,B} {13,S}
6  C u0 p0 c0 {5,B} {7,B} {14,S}
7  C u0 p0 c0 {4,B} {6,B} {15,S}
8  C u0 p0 c0 {3,D} {9,S} {10,S}
9  C u1 p0 c0 {8,S} {17,S} {18,S}
10 H u0 p0 c0 {8,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.55059,0.0699084,-2.2676e-05,-1.61355e-08,9.67203e-12,27416.2,33.707], Tmin=(200,'K'), Tmax=(1053.41,'K')),
            NASAPolynomial(coeffs=[10.5311,0.0474479,-2.40364e-05,5.82704e-09,-5.48095e-13,23571.6,-31.3756], Tmin=(1053.41,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (224.962,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 5, 'C=C': 4, 'C-H': 9}
1D rotors:
* Invalidated! pivots: [4, 5], dihedral: [1, 4, 5, 6], invalidation reason: scan has a barrier larger than 40 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 2, max scan energy: 35.78 kJ/mol
* Invalidated! pivots: [1, 4], dihedral: [2, 1, 4, 5], invalidation reason: scan has a barrier larger than 40 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       0.14233700    1.05599900    0.00715900
H       0.23396400   -0.02261000    0.00228000
H       1.06156400    1.63215500    0.00321700
C      -1.07898100    1.66839600    0.01742100
C      -1.26660300    3.06194600    0.02391900
C      -2.51517400    3.77039500    0.03465800
C      -3.77959400    3.13192300    0.04116300
C      -4.95266800    3.86983200    0.05129100
C      -4.91595400    5.26688400    0.05537700
C      -3.68148600    5.91897900    0.04920200
C      -2.50457600    5.18632000    0.03908700
H      -1.95916600    1.03083900    0.02061000
H      -0.36930600    3.67631900    0.02025100
H      -3.83808500    2.05032600    0.03830700
H      -5.90757100    3.35563900    0.05614600
H      -5.83715500    5.83784200    0.06331500
H      -3.64053500    7.00263600    0.05230600
H      -1.54931100    5.70099000    0.03428100
""",
)

entry(
    index = 19,
    label = "C9H7_3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,B} {7,B}
3  C u0 p0 c0 {2,B} {4,B} {14,S}
4  C u0 p0 c0 {3,B} {5,B} {13,S}
5  C u0 p0 c0 {4,B} {6,B} {12,S}
6  C u0 p0 c0 {5,B} {7,B} {15,S}
7  C u1 p0 c0 {2,B} {6,B}
8  C u0 p0 c0 {1,S} {9,T}
9  C u0 p0 c0 {8,T} {16,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.25585,0.0704075,-4.31761e-05,6.86465e-09,1.98204e-12,66017.1,34.8669], Tmin=(200,'K'), Tmax=(1072.93,'K')),
            NASAPolynomial(coeffs=[11.2227,0.0384684,-1.89108e-05,4.45483e-09,-4.08083e-13,62500,-30.1248], Tmin=(1072.93,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (546.179,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 5, 'C=C': 3, 'C#C': 1, 'C-H': 7}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: scan job crashed
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 4.13 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.49780000   -0.79050000   -1.08620000
C      -0.18530000    0.10020000   -0.34340000
C       0.18080000    1.18060000    0.56660000
C       1.51080000    1.86620000    0.27200000
C       1.97090000    2.89410000    1.06900000
C       3.14100000    3.59150000    0.91490000
C       3.95580000    3.22130000   -0.16620000
C       3.55180000    2.19090000   -1.01070000
C       2.34640000    1.51920000   -0.79880000
H      -0.78030000   -1.57950000   -1.73910000
H      -0.61300000    1.93640000    0.55780000
H       0.20660000    0.78970000    1.59010000
H       3.43190000    4.39040000    1.58810000
H       4.89370000    3.73870000   -0.33700000
H       4.17950000    1.90290000   -1.84630000
H       2.04270000    0.71770000   -1.46340000
""",
)

entry(
    index = 20,
    label = "C12H17_1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {4,S} {17,S} {18,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {7,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {21,S} {22,S} {23,S}
6  C u0 p0 c0 {7,S} {8,B} {9,B}
7  C u1 p0 c0 {4,S} {6,S} {24,S}
8  C u0 p0 c0 {6,B} {10,B} {25,S}
9  C u0 p0 c0 {6,B} {12,B} {29,S}
10 C u0 p0 c0 {8,B} {11,B} {26,S}
11 C u0 p0 c0 {10,B} {12,B} {27,S}
12 C u0 p0 c0 {9,B} {11,B} {28,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {11,S}
28 H u0 p0 c0 {12,S}
29 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.53221,0.0917496,-1.36302e-05,-3.54279e-08,1.67745e-11,7239.69,26.4763], Tmin=(200,'K'), Tmax=(1031.84,'K')),
            NASAPolynomial(coeffs=[12.1726,0.0802019,-4.00191e-05,9.51737e-09,-8.73737e-13,3462.75,-32.8525], Tmin=(1031.84,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (58.9064,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (685.944,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 9, 'C=C': 3, 'C-H': 17}
1D rotors:
pivots: [1, 2], dihedral: [14, 1, 2, 3], rotor symmetry: 3, max scan energy: 11.86 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 23.39 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 23.60 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 21.16 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 8], rotor symmetry: 1, max scan energy: 18.92 kJ/mol
* Invalidated! pivots: [6, 8], dihedral: [5, 6, 8, 9], invalidation reason: scan has a barrier larger than 40 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       0.13357600    1.59942800    0.00689900
C       0.07672900    0.06925000    0.00213900
C      -1.35321200   -0.48340500    0.01192600
C      -1.42028200   -2.01333400    0.00665600
C      -2.85387400   -2.56014500    0.01600200
C      -2.92311800   -4.05577500    0.00976600
H      -1.98337500   -4.60122600   -0.00074300
C      -4.11394800   -4.81686000    0.01588200
C      -5.40708200   -4.22126900    0.02959500
C      -6.55279200   -4.99985900    0.03493200
C      -6.46800900   -6.39535800    0.02691000
C      -5.20853200   -7.00675600    0.01340900
C      -4.05787700   -6.24005700    0.00801500
H       1.16531500    1.96122700   -0.00034300
H      -0.37083400    2.01633700   -0.87041600
H      -0.35634500    2.01036400    0.89516700
H       0.60475300   -0.31315400   -0.87977000
H       0.61915200   -0.31916000    0.87261400
H      -1.88186300   -0.10047800    0.89465000
H      -1.89632600   -0.09390100   -0.85907300
H      -0.89540400   -2.39807100   -0.87645800
H      -0.88136100   -2.40482600    0.87827300
H      -3.38484600   -2.16304600    0.89487400
H      -3.39913100   -2.15530100   -0.85051400
H      -5.49694400   -3.14147800    0.03589700
H      -7.52561300   -4.51995500    0.04542000
H      -7.36872300   -6.99807100    0.03111500
H      -5.13383700   -8.08882700    0.00713200
H      -3.08559600   -6.72199600   -0.00257700
""",
)

entry(
    index = 21,
    label = "C12H16_128",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {4,S} {17,S} {18,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {6,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {12,S} {21,S} {22,S}
6  C u0 p0 c0 {4,S} {7,B} {8,B}
7  C u0 p0 c0 {6,B} {9,B} {23,S}
8  C u0 p0 c0 {6,B} {11,B} {27,S}
9  C u0 p0 c0 {7,B} {10,B} {24,S}
10 C u0 p0 c0 {9,B} {11,B} {25,S}
11 C u0 p0 c0 {8,B} {10,B} {26,S}
12 C u2 p0 c0 {5,S} {28,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {11,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.30904,0.0860002,-1.31927e-05,-3.20634e-08,1.51185e-11,42159.1,21.2584], Tmin=(200,'K'), Tmax=(1041.1,'K')),
            NASAPolynomial(coeffs=[13.2409,0.0753613,-3.75152e-05,8.90196e-09,-8.15597e-13,38599.6,-34.2197], Tmin=(1041.1,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (350.241,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (661.001,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 9, 'C=C': 3, 'C-H': 16}
1D rotors:
* Invalidated! pivots: [1, 3], dihedral: [2, 1, 3, 4], invalidation reason: scan job crashed
pivots: [3, 4], dihedral: [1, 3, 4, 5], rotor symmetry: 1, max scan energy: 17.68 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 23.28 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 23.44 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 1, max scan energy: 21.61 kJ/mol
pivots: [7, 8], dihedral: [6, 7, 8, 9], rotor symmetry: 2, max scan energy: 5.81 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       0.05410800    0.92460200   -0.04989200
H      -0.36641500   -0.04075000    0.20055400
C       1.40048300    1.50952900   -0.03120400
C       1.40478900    3.05334800   -0.01750200
C       2.81731300    3.64648400   -0.01891300
C       2.82933300    5.17876400   -0.00720400
C       4.25106400    5.77303100   -0.00799200
C       4.26307700    7.28554100    0.00291100
C       4.24695200    8.01257000   -1.19235000
C       4.22045800    9.40523700   -1.18530300
C       4.21040400   10.09851400    0.02316100
C       4.22904900    9.38804400    1.22148400
C       4.25556700    7.99540100    1.20852100
H       1.94743600    1.14446600    0.85490300
H       1.98243600    1.16520000   -0.90375200
H       0.84964600    3.41681200   -0.88900800
H       0.85629700    3.40134200    0.86438800
H       3.36969400    3.27293900    0.85315100
H       3.36197300    3.28623500   -0.90125300
H       2.28247900    5.55803600   -0.87838300
H       2.28908900    5.54487500    0.87368300
H       4.79566900    5.39678100    0.86510800
H       4.78936800    5.40958800   -0.89037000
H       4.26066100    7.48089600   -2.13898100
H       4.21227800    9.94917200   -2.12361500
H       4.19300000   11.18254700    0.03097900
H       4.22761400    9.91855500    2.16748800
H       4.27610000    7.45033200    2.14737800
""",
)

entry(
    index = 22,
    label = "C10H8_14",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {4,S}
2  C u0 p0 c0 {1,B} {5,B} {12,S}
3  C u0 p0 c0 {1,B} {7,B} {16,S}
4  C u0 p0 c0 {1,S} {8,D} {11,S}
5  C u0 p0 c0 {2,B} {6,B} {13,S}
6  C u0 p0 c0 {5,B} {7,B} {14,S}
7  C u0 p0 c0 {3,B} {6,B} {15,S}
8  C u0 p0 c0 {4,D} {9,S} {17,S}
9  C u0 p0 c0 {8,S} {10,T}
10 C u0 p0 c0 {9,T} {18,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.23269,0.0832217,-5.31582e-05,9.82013e-09,1.91866e-12,43608.1,36.766], Tmin=(200,'K'), Tmax=(1074.44,'K')),
            NASAPolynomial(coeffs=[13.2617,0.0429087,-2.11287e-05,4.99343e-09,-4.59385e-13,39275.9,-43.7637], Tmin=(1074.44,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (359.348,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 5, 'C=C': 4, 'C#C': 1, 'C-H': 8}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: scan job crashed
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 2, max scan energy: 20.12 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       0.11131500   -1.29398400   -0.00557600
C       0.06823500   -0.08884100    0.00292800
C      -0.02638600    1.32465500    0.01393900
C       1.04179200    2.14637300    0.00041500
C       1.03160000    3.60961200    0.01028000
C      -0.14660900    4.37774400    0.02832400
C      -0.09205400    5.76460600    0.03723500
C       1.13847200    6.42424400    0.02828200
C       2.31511100    5.68028500    0.01011700
C       2.26041700    4.29036600    0.00106400
H       0.15963800   -2.35496700   -0.01346500
H      -1.03413900    1.73004500    0.03489200
H       2.02696300    1.68863000   -0.01955400
H      -1.11359800    3.88864500    0.03497500
H      -1.01268200    6.33728600    0.05103200
H       1.17625400    7.50753400    0.03519300
H       3.27638900    6.18163100    0.00282200
H       3.18076100    3.71583700   -0.01321300
""",
)

entry(
    index = 23,
    label = "C10H8_17",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,B} {4,B}
2  C u0 p0 c0 {1,S} {8,D} {9,S}
3  C u0 p0 c0 {1,B} {5,B} {11,S}
4  C u0 p0 c0 {1,B} {7,B} {15,S}
5  C u0 p0 c0 {3,B} {6,B} {12,S}
6  C u0 p0 c0 {5,B} {7,B} {13,S}
7  C u0 p0 c0 {4,B} {6,B} {14,S}
8  C u0 p0 c0 {2,D} {16,S} {17,S}
9  C u0 p0 c0 {2,S} {10,T}
10 C u0 p0 c0 {9,T} {18,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.23998,0.0831397,-5.33613e-05,9.91688e-09,1.95057e-12,44095.2,38.442], Tmin=(200,'K'), Tmax=(1071.08,'K')),
            NASAPolynomial(coeffs=[13.4644,0.0420957,-2.05356e-05,4.83099e-09,-4.44151e-13,39721.3,-43.1148], Tmin=(1071.08,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (363.391,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 5, 'C=C': 4, 'C#C': 1, 'C-H': 8}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: scan job crashed
pivots: [3, 5], dihedral: [2, 3, 5, 6], rotor symmetry: 1, max scan energy: 10.16 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -3.12094500   -1.40693800   -0.36926900
C      -2.34579000   -0.51309700   -0.14575700
C      -1.41175100    0.54043400    0.12003600
C      -1.86633300    1.76519500    0.44041400
C       0.04002500    0.20836100    0.04321400
C       0.49143800   -1.08645000    0.33080700
C       1.84875600   -1.39144400    0.29434200
C       2.77972200   -0.41219600   -0.04350500
C       2.34121100    0.87495600   -0.35025400
C       0.98540800    1.18148400   -0.31076900
H      -3.81180900   -2.18811700   -0.57182300
H      -2.92735800    1.97447900    0.47535000
H      -1.18778400    2.57163500    0.68795000
H      -0.22842500   -1.85343600    0.59030100
H       2.17862300   -2.39744700    0.52844300
H       3.83652900   -0.65137700   -0.07822400
H       3.05594400    1.63955500   -0.63355700
H       0.65463900    2.17710200   -0.58189900
""",
)

entry(
    index = 24,
    label = "C14H10_14",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {6,B} {7,B}
2  C u0 p0 c0 {1,B} {5,B} {8,B}
3  C u0 p0 c0 {4,B} {5,B} {11,S}
4  C u0 p0 c0 {3,B} {6,B} {13,S}
5  C u0 p0 c0 {2,B} {3,B} {20,S}
6  C u0 p0 c0 {1,B} {4,B} {15,S}
7  C u0 p0 c0 {1,B} {9,B} {16,S}
8  C u0 p0 c0 {2,B} {10,B} {19,S}
9  C u0 p0 c0 {7,B} {10,B} {17,S}
10 C u0 p0 c0 {8,B} {9,B} {18,S}
11 C u0 p0 c0 {3,S} {12,D} {21,S}
12 C u0 p0 c0 {11,D} {22,S} {23,S}
13 C u0 p0 c0 {4,S} {14,T}
14 C u0 p0 c0 {13,T} {24,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {12,S}
23 H u0 p0 c0 {12,S}
24 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.19919,0.127009,-0.000100179,3.65536e-08,-4.38963e-12,50635.4,49.9524], Tmin=(200,'K'), Tmax=(1127.43,'K')),
            NASAPolynomial(coeffs=[19.7182,0.0552226,-2.67812e-05,6.22615e-09,-5.63806e-13,43960.7,-77.9322], Tmin=(1127.43,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (416.338,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (577.856,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C=C': 6, 'C-C': 8, 'C#C': 1, 'C-H': 10}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: scan job crashed
pivots: [12, 13], dihedral: [3, 12, 13, 14], rotor symmetry: 1, max scan energy: 17.27 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       0.05169800   -1.17346400    0.03247800
C       0.05401000    0.03103700    0.01444200
C       0.03831800    1.45897000   -0.00763500
C      -1.17483100    2.12041800    0.07081000
C      -1.25478100    3.53076100    0.05929200
C      -2.49170300    4.22294500    0.13785100
C      -2.52886500    5.59549300    0.11414700
C      -1.33006200    6.34094200    0.00844100
C      -0.11771600    5.70026900   -0.07029400
C      -0.04308300    4.28281300   -0.04407200
C       1.18614900    3.58797100   -0.12568500
C       1.26454300    2.20966200   -0.09752000
C       2.55295000    1.50124100   -0.17499200
C       3.73945800    1.98640100    0.19804900
H       0.04771100   -2.23553900    0.05304700
H      -2.08739700    1.54011800    0.14459200
H      -3.40874400    3.64869300    0.21708200
H      -3.47830400    6.11511300    0.17538100
H      -1.37423200    7.42401900   -0.01036100
H       0.80125000    6.27118500   -0.15187000
H       2.09601500    4.16748300   -0.23655800
H       2.50274500    0.48470800   -0.55319900
H       3.85494200    2.97305900    0.63378300
H       4.64062700    1.39460300    0.09119100
""",
)

entry(
    index = 25,
    label = "C14H10_16",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {4,B} {8,B}
2  C u0 p0 c0 {1,B} {6,B} {7,B}
3  C u0 p0 c0 {4,B} {5,B} {9,S}
4  C u0 p0 c0 {1,B} {3,B} {13,S}
5  C u0 p0 c0 {3,B} {6,B} {16,S}
6  C u0 p0 c0 {2,B} {5,B} {17,S}
7  C u0 p0 c0 {2,B} {10,B} {18,S}
8  C u0 p0 c0 {1,B} {11,B} {21,S}
9  C u0 p0 c0 {3,S} {12,D} {15,S}
10 C u0 p0 c0 {7,B} {11,B} {19,S}
11 C u0 p0 c0 {8,B} {10,B} {20,S}
12 C u0 p0 c0 {9,D} {22,S} {23,S}
13 C u0 p0 c0 {4,S} {14,T}
14 C u0 p0 c0 {13,T} {24,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {12,S}
23 H u0 p0 c0 {12,S}
24 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.36417,0.12703,-9.66082e-05,3.11986e-08,-2.27187e-12,50172.3,48.919], Tmin=(200,'K'), Tmax=(1099,'K')),
            NASAPolynomial(coeffs=[20.2733,0.0547972,-2.67898e-05,6.29843e-09,-5.77713e-13,43264.2,-82.9785], Tmin=(1099,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (412.352,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (577.856,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 8, 'C=C': 6, 'C#C': 1, 'C-H': 10}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: scan job crashed
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 3, max scan energy: 19.38 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.37878300    3.13800100    0.01672500
C      -1.04768500    1.97908800    0.00929900
C      -0.63137900    0.61403100    0.00092100
C      -1.57568300   -0.42128800   -0.00641700
C      -3.01244900   -0.11745400   -0.00407400
C      -4.01935600   -0.99281200   -0.08810900
C      -1.10900300   -1.76452400   -0.01288200
C       0.22419100   -2.06454200   -0.01655700
C       1.20582600   -1.03893700   -0.01291900
C       2.59209000   -1.33074400   -0.01635100
C       3.52502200   -0.32163000   -0.01119500
C       3.10411700    1.02562900   -0.00195900
C       1.76518400    1.34037000    0.00196900
C       0.77790700    0.32275300   -0.00314200
H      -1.67723700    4.15757700    0.02243500
H      -3.25786600    0.93657500    0.06945200
H      -3.87298300   -2.06326300   -0.17509900
H      -5.04705900   -0.65045900   -0.07617700
H      -1.83175700   -2.57054300   -0.00832800
H       0.55005800   -3.09945500   -0.01957700
H       2.90500900   -2.36961400   -0.02340400
H       4.58341800   -0.55615800   -0.01432700
H       3.84357200    1.81850800    0.00198400
H       1.44804400    2.37549400    0.00893400
""",
)

entry(
    index = 26,
    label = "C14H10_13",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {7,B}
2  C u0 p0 c0 {1,B} {4,B} {11,S}
3  C u0 p0 c0 {1,B} {5,B} {6,B}
4  C u0 p0 c0 {2,B} {8,B} {13,S}
5  C u0 p0 c0 {3,B} {8,B} {16,S}
6  C u0 p0 c0 {3,B} {9,B} {17,S}
7  C u0 p0 c0 {1,B} {10,B} {20,S}
8  C u0 p0 c0 {4,B} {5,B} {15,S}
9  C u0 p0 c0 {6,B} {10,B} {18,S}
10 C u0 p0 c0 {7,B} {9,B} {19,S}
11 C u0 p0 c0 {2,S} {12,D} {21,S}
12 C u0 p0 c0 {11,D} {22,S} {23,S}
13 C u0 p0 c0 {4,S} {14,T}
14 C u0 p0 c0 {13,T} {24,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {12,S}
23 H u0 p0 c0 {12,S}
24 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.91442,0.127154,-0.000105902,4.48357e-08,-7.61051e-12,51645.4,48.706], Tmin=(200,'K'), Tmax=(1379.56,'K')),
            NASAPolynomial(coeffs=[20.9229,0.0522387,-2.44459e-05,5.47231e-09,-4.77147e-13,44516.6,-84.2574], Tmin=(1379.56,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (424.96,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (577.856,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 8, 'C=C': 6, 'C#C': 1, 'C-H': 10}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: scan job crashed
pivots: [12, 13], dihedral: [3, 12, 13, 14], rotor symmetry: 1, max scan energy: 12.85 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.21106600   -1.22381200    0.01239700
C      -0.06772600   -0.02813200    0.04008300
C      -0.00688400    1.39902700    0.06106500
C      -1.25305300    2.09319900    0.03677100
C      -1.30268400    3.45744300   -0.00025600
C      -0.10928900    4.22407900   -0.00315100
C      -0.14068600    5.64090900   -0.03378400
C       1.02002000    6.37492000   -0.01810700
C       2.26663000    5.71521200    0.03987300
C       2.32966100    4.34223000    0.07029200
C       1.15111400    3.54782200    0.03518500
C       1.19526500    2.11227900    0.06058600
C       2.50960000    1.43686700    0.03500500
C       2.89066400    0.42394300    0.81249200
H      -0.31222300   -2.28088300   -0.01095000
H      -2.16359300    1.50703700    0.03434400
H      -2.25821000    3.96997600   -0.02826700
H      -1.10480300    6.13748700   -0.06632100
H       0.98271600    7.45809100   -0.04152900
H       3.18109300    6.29697000    0.06830900
H       3.29466700    3.85783400    0.14106900
H       3.22128200    1.82792900   -0.68812500
H       3.87713900   -0.01387000    0.71007900
H       2.24136600    0.00061200    1.56893000
""",
)

entry(
    index = 27,
    label = "C10H9_34",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {14,S}
4  C u0 p0 c0 {2,B} {7,B} {18,S}
5  C u0 p0 c0 {3,B} {6,B} {15,S}
6  C u0 p0 c0 {5,B} {7,B} {16,S}
7  C u0 p0 c0 {4,B} {6,B} {17,S}
8  C u1 p0 c0 {1,S} {9,S} {13,S}
9  C u0 p0 c0 {8,S} {10,T}
10 C u0 p0 c0 {9,T} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.43864,0.0902238,-6.68363e-05,2.30433e-08,-2.56703e-12,49452.8,41.0022], Tmin=(200,'K'), Tmax=(1139.27,'K')),
            NASAPolynomial(coeffs=[13.5802,0.0449008,-2.15394e-05,4.94988e-09,-4.42779e-13,45094.3,-41.4779], Tmin=(1139.27,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (407.934,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (453.139,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 6, 'C=C': 3, 'C#C': 1, 'C-H': 9}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 5], invalidation reason: scan job crashed
pivots: [3, 5], dihedral: [2, 3, 5, 6], rotor symmetry: 1, max scan energy: 6.06 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [3, 5, 6, 7], invalidation reason: scan job crashed


External symmetry: 1, optical isomers: 2

Geometry:
C       4.22391600    0.66971200    0.06150300
C       3.16912200    0.09239700    0.27913500
C       1.98216800   -0.55430900    0.51099500
H       1.72747900   -0.82421900    1.53160300
C       0.99794700   -0.90860500   -0.57293400
C      -0.39777300   -0.37198200   -0.29516300
C      -1.45928800   -1.23433000   -0.01242200
C      -2.73544600   -0.73564300    0.24729900
C      -2.96578800    0.63686800    0.22724500
C      -1.91270600    1.50752500   -0.05252700
C      -0.64022300    1.00661800   -0.30878600
H       5.14245200    1.17038700   -0.12183400
H       1.36357500   -0.52990800   -1.53121300
H       0.94110400   -2.00088400   -0.66783400
H      -1.28777700   -2.30611000    0.00081100
H      -3.54800000   -1.42071600    0.46291700
H      -3.95744100    1.02688400    0.42706800
H      -2.08411100    2.57820100   -0.07130600
H       0.17629000    1.68911500   -0.52095800
""",
)

entry(
    index = 28,
    label = "C9H11_21",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {4,S} {5,B} {6,B}
4  C u1 p0 c0 {1,S} {3,S} {15,S}
5  C u0 p0 c0 {3,B} {7,B} {16,S}
6  C u0 p0 c0 {3,B} {9,B} {20,S}
7  C u0 p0 c0 {5,B} {8,B} {17,S}
8  C u0 p0 c0 {7,B} {9,B} {18,S}
9  C u0 p0 c0 {6,B} {8,B} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.81744,0.0741879,-2.28536e-05,-1.73082e-08,1.0152e-11,16558.8,36.7165], Tmin=(200,'K'), Tmax=(1044.96,'K')),
            NASAPolynomial(coeffs=[9.59882,0.053669,-2.66756e-05,6.35965e-09,-5.89432e-13,12907.2,-24.9183], Tmin=(1044.96,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (134.572,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (473.925,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 6, 'C=C': 3, 'C-H': 11}
1D rotors:
pivots: [1, 2], dihedral: [11, 1, 2, 3], rotor symmetry: 3, max scan energy: 12.29 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 5], rotor symmetry: 1, max scan energy: 18.55 kJ/mol
* Invalidated! pivots: [3, 5], dihedral: [2, 3, 5, 6], invalidation reason: scan has a barrier larger than 40 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -0.01336200    1.62328900   -0.00218300
C      -0.00512000    0.09094800    0.00975200
C       0.67648300   -0.50685900   -1.18244300
H       1.08832200    0.17709300   -1.91964300
C       0.82870700   -1.89081100   -1.42676400
C       0.33349300   -2.88800400   -0.53921600
C       0.50177400   -4.23555500   -0.81293900
C       1.16431500   -4.65165200   -1.97175700
C       1.66097800   -3.69162000   -2.86162100
C       1.49910000   -2.34380500   -2.59911000
H       1.00557700    2.02057600   -0.01633400
H      -0.53328200    2.00602600   -0.88506700
H      -0.51616200    2.02331500    0.88158600
H       0.47793100   -0.26251300    0.93275400
H      -1.03953500   -0.27796600    0.07291200
H      -0.18375700   -2.58850700    0.36440600
H       0.11442700   -4.97465800   -0.11982100
H       1.29194800   -5.70768200   -2.17925500
H       2.17599200   -4.00604300   -3.76290800
H       1.88687100   -1.60595200   -3.29395000
""",
)

entry(
    index = 29,
    label = "C8H9_19",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
2  C u1 p0 c0 {5,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {1,S} {6,D} {12,S}
5  C u0 p0 c0 {2,S} {3,D} {14,S}
6  C u0 p0 c0 {2,S} {4,D} {15,S}
7  C u0 p0 c0 {2,S} {8,D} {13,S}
8  C u0 p0 c0 {7,D} {16,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.872041,0.0607272,-1.25869e-05,-2.12294e-08,1.06411e-11,27148.1,30.1367], Tmin=(200,'K'), Tmax=(1049.07,'K')),
            NASAPolynomial(coeffs=[8.63964,0.0464316,-2.35621e-05,5.70931e-09,-5.36161e-13,23943.4,-21.9697], Tmin=(1049.07,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (223.08,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 5, 'C=C': 3, 'C-H': 9}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 2, max scan energy: 38.85 kJ/mol
* Invalidated! pivots: [1, 2], dihedral: [9, 1, 2, 3], invalidation reason: scan has a barrier larger than 40 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -0.13645500    1.37488700   -0.18800200
C       0.06168400    0.03712200   -0.09226800
C       1.29857000   -0.65842700    0.10153500
C       2.56928000    0.00861400    0.22697000
C       3.72421100   -0.66726600    0.40974700
C       3.78264700   -2.16313800    0.49799300
C       2.43740500   -2.81055900    0.36105400
C       1.30462100   -2.09086900    0.17861500
H       0.67136800    2.09410200   -0.12315600
H      -1.13085900    1.77694500   -0.33555000
H      -0.81584000   -0.60219000   -0.17002300
H       2.59766500    1.09112300    0.17263700
H       4.65991700   -0.12453400    0.49935600
H       4.47276800   -2.55790200   -0.26738700
H       4.25306700   -2.46508700    1.44954300
H       2.39149900   -3.89342200    0.41251800
H       0.35385200   -2.60799800    0.08479800
""",
)

entry(
    index = 30,
    label = "C10H7_7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {8,S}
3  C u0 p0 c0 {1,B} {5,B} {11,S}
4  C u0 p0 c0 {2,B} {6,B} {14,S}
5  C u0 p0 c0 {3,B} {6,B} {12,S}
6  C u0 p0 c0 {4,B} {5,B} {13,S}
7  C u0 p0 c0 {1,S} {9,D} {15,S}
8  C u0 p0 c0 {2,S} {10,T}
9  C u1 p0 c0 {7,D} {16,S}
10 C u0 p0 c0 {8,T} {17,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.41717,0.0923508,-8.23444e-05,3.71916e-08,-6.69456e-12,73478.7,36.4989], Tmin=(200,'K'), Tmax=(1316.22,'K')),
            NASAPolynomial(coeffs=[16.7135,0.034213,-1.60895e-05,3.63374e-09,-3.20698e-13,68442.7,-61.0522], Tmin=(1316.22,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (607.774,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 5, 'C=C': 4, 'C#C': 1, 'C-H': 7}
1D rotors:
pivots: [3, 4], dihedral: [1, 3, 4, 5], rotor symmetry: 1, max scan energy: 22.89 kJ/mol
* Invalidated! pivots: [9, 10], dihedral: [4, 9, 10, 11], invalidation reason: scan job crashed


External symmetry: 1, optical isomers: 1

Geometry:
C       0.03947800    0.95317100    0.00980200
H      -0.15676700   -0.10789100    0.00640900
C       1.09073000    1.74240400    0.00245200
C       1.08774700    3.21487600    0.01052300
C      -0.11484100    3.93621100    0.02772900
C      -0.12596300    5.32266900    0.03540000
C       1.07725100    6.03199200    0.02601800
C       2.28027500    5.34330400    0.00903000
C       2.30598600    3.93714600    0.00102000
C       3.57025000    3.27278100   -0.01665300
C       4.64979700    2.73808700   -0.03164300
H       2.08124600    1.27730800   -0.01110900
H      -1.04780200    3.38421200    0.03509800
H      -1.07078600    5.85416600    0.04875200
H       1.07447900    7.11576500    0.03193300
H       3.22090600    5.88018800    0.00155700
H       5.60211300    2.26748100   -0.04481900
""",
)

entry(
    index = 31,
    label = "C10H9_7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,B} {8,B}
4  C u0 p0 c0 {3,B} {5,B} {17,S}
5  C u0 p0 c0 {4,B} {6,B} {16,S}
6  C u0 p0 c0 {5,B} {7,B} {15,S}
7  C u0 p0 c0 {6,B} {8,B} {18,S}
8  C u1 p0 c0 {3,B} {7,B}
9  C u0 p0 c0 {2,S} {10,T}
10 C u0 p0 c0 {9,T} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.48239,0.091835,-7.31471e-05,2.98314e-08,-4.90401e-12,62725.5,40.4863], Tmin=(200,'K'), Tmax=(1414.09,'K')),
            NASAPolynomial(coeffs=[15.7238,0.0403327,-1.85127e-05,4.07278e-09,-3.49815e-13,57576.8,-53.6549], Tmin=(1414.09,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (518.273,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C=C': 3, 'C-C': 6, 'C#C': 1, 'C-H': 9}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: scan job crashed
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 24.30 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 1, max scan energy: 6.89 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.01970000   -1.26490000   -0.06220000
C      -0.03370000   -0.06340000   -0.08270000
C      -0.01890000    1.39600000   -0.10120000
C       1.40030000    1.98410000    0.10120000
C       1.39960000    3.49550000    0.08410000
C       1.25680000    4.23340000   -1.07330000
C       1.22770000    5.60090000   -1.18120000
C       1.35150000    6.32890000    0.01130000
C       1.49630000    5.65220000    1.22070000
C       1.51960000    4.25810000    1.25920000
H      -0.01700000   -2.32700000   -0.04680000
H      -0.42270000    1.75530000   -1.05370000
H      -0.68430000    1.77850000    0.68040000
H       1.80300000    1.62540000    1.05150000
H       2.05220000    1.60270000   -0.68870000
H       1.11740000    6.10410000   -2.13550000
H       1.33620000    7.41320000   -0.01380000
H       1.59550000    6.21350000    2.14280000
H       1.63950000    3.74480000    2.20910000
""",
)

entry(
    index = 32,
    label = "C10H9_6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {4,S}
2  C u0 p0 c0 {1,B} {5,B} {12,S}
3  C u0 p0 c0 {1,B} {7,B} {16,S}
4  C u0 p0 c0 {1,S} {8,D} {11,S}
5  C u0 p0 c0 {2,B} {6,B} {13,S}
6  C u0 p0 c0 {5,B} {7,B} {14,S}
7  C u0 p0 c0 {3,B} {6,B} {15,S}
8  C u0 p0 c0 {4,D} {10,S} {17,S}
9  C u0 p0 c0 {10,D} {18,S} {19,S}
10 C u1 p0 c0 {8,S} {9,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.40901,0.0854579,-5.01917e-05,5.82307e-09,3.21809e-12,44793.3,38.2131], Tmin=(200,'K'), Tmax=(1071.58,'K')),
            NASAPolynomial(coeffs=[12.5517,0.0481774,-2.39936e-05,5.69181e-09,-5.23157e-13,40521,-39.9717], Tmin=(1071.58,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (369.106,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (453.139,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C=C': 5, 'C-C': 5, 'C-H': 9}
1D rotors:
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: scan has a barrier larger than 40 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 2, max scan energy: 38.24 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: scan job crashed


External symmetry: 1, optical isomers: 1

Geometry:
C      -0.52394800    1.17497500    0.06688800
C       0.53436700    0.42412900    0.00398600
C       1.62446900   -0.34362300   -0.06122500
C       1.62319800   -1.75528600    0.04894600
C       2.76765300   -2.61321700   -0.01457900
C       4.09343400   -2.14574500   -0.19630800
C       5.16131200   -3.02729900   -0.24944200
C       4.95651400   -4.40416200   -0.12458200
C       3.65897400   -4.88900000    0.05544600
C       2.58627700   -4.01356200    0.10961000
H      -0.88618500    1.57797000    1.01123500
H      -1.09687700    1.43439300   -0.82189400
H       2.57117900    0.17147400   -0.21037400
H       0.66051100   -2.23460900    0.19495000
H       4.28372800   -1.08383500   -0.29535100
H       6.16548400   -2.64208900   -0.38923200
H       5.79614200   -5.08806600   -0.16711700
H       3.48762700   -5.95536700    0.15333500
H       1.58171200   -4.39898100    0.24959600
""",
)

entry(
    index = 33,
    label = "C10H11_31",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,B} {5,B}
3  C u1 p0 c0 {1,S} {9,S} {13,S}
4  C u0 p0 c0 {2,B} {6,B} {15,S}
5  C u0 p0 c0 {2,B} {8,B} {19,S}
6  C u0 p0 c0 {4,B} {7,B} {16,S}
7  C u0 p0 c0 {6,B} {8,B} {17,S}
8  C u0 p0 c0 {5,B} {7,B} {18,S}
9  C u0 p0 c0 {3,S} {10,D} {14,S}
10 C u0 p0 c0 {9,D} {20,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.56478,0.0847045,-3.60867e-05,-9.4879e-09,8.35759e-12,27522.8,42.1715], Tmin=(200,'K'), Tmax=(1051.26,'K')),
            NASAPolynomial(coeffs=[11.8041,0.0540944,-2.67448e-05,6.36153e-09,-5.89594e-13,23172.1,-34.1922], Tmin=(1051.26,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (225.359,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (498.868,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 6, 'C=C': 4, 'C-H': 11}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 5], invalidation reason: scan has a barrier larger than 40 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 6], rotor symmetry: 1, max scan energy: 14.06 kJ/mol
pivots: [5, 6], dihedral: [3, 5, 6, 7], rotor symmetry: 2, max scan energy: 7.84 kJ/mol
* Invalidated! pivots: [1, 2], dihedral: [12, 1, 2, 3], invalidation reason: scan has a barrier larger than 40 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -3.70207900    0.62076700    0.51493400
C      -3.10097600    0.08600900   -0.60894900
C      -1.89063200   -0.59396500   -0.68098500
H      -1.55975900   -0.94101400   -1.65538500
C      -0.96958200   -0.89580500    0.46592300
C       0.43918400   -0.36647900    0.24234900
C       0.66835400    1.01067700    0.13748000
C       1.95318600    1.50570100   -0.06313300
C       3.03381500    0.63027800   -0.16877500
C       2.81758600   -0.74121000   -0.07129300
C       1.52881600   -1.23340300    0.13280400
H      -4.65441300    1.13002300    0.44232700
H      -3.25593600    0.55623800    1.49981400
H      -3.63267600    0.20760600   -1.55052100
H      -1.36880000   -0.48642400    1.39792600
H      -0.91377200   -1.98270700    0.60838300
H      -0.16928800    1.69654300    0.21138600
H       2.11257600    2.57588600   -0.13772500
H       4.03494800    1.01557700   -0.32613400
H       3.65086200   -1.43058300   -0.15271600
H       1.36858500   -2.30421400    0.21089300
""",
)

entry(
    index = 34,
    label = "C10H11_33",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
2  C u0 p0 c0 {4,S} {5,S} {6,D}
3  C u0 p0 c0 {1,S} {7,D} {14,S}
4  C u1 p0 c0 {2,S} {10,S} {21,S}
5  C u0 p0 c0 {2,S} {8,D} {18,S}
6  C u0 p0 c0 {2,D} {9,S} {15,S}
7  C u0 p0 c0 {3,D} {8,S} {16,S}
8  C u0 p0 c0 {5,D} {7,S} {17,S}
9  C u0 p0 c0 {6,S} {10,D} {19,S}
10 C u0 p0 c0 {4,S} {9,D} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.69263,0.0933105,-6.05875e-05,1.53419e-08,-6.42636e-14,33912.2,40.1758], Tmin=(200,'K'), Tmax=(1112.04,'K')),
            NASAPolynomial(coeffs=[12.3364,0.0534194,-2.58904e-05,5.99808e-09,-5.39386e-13,29693.7,-37.8652], Tmin=(1112.04,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (278.582,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 6, 'C=C': 4, 'C-H': 11}
1D rotors:
pivots: [1, 2], dihedral: [12, 1, 2, 3], rotor symmetry: 3, max scan energy: 6.50 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: scan has a barrier larger than 40 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: scan has a barrier larger than 40 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: scan has a barrier larger than 40 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: scan has a barrier larger than 40 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -0.04331700    1.60633700   -0.00715000
C      -0.02802800    0.11326500   -0.06056100
C      -1.12287800   -0.68104300    0.03377600
C      -1.09290700   -2.10382200   -0.01906800
C      -2.22047700   -2.90247000    0.07960100
C      -2.24925800   -4.29936300    0.03596000
C      -1.12774400   -5.22371500   -0.11916100
H      -0.09060500   -4.94267000   -0.22610600
C      -1.62679900   -6.48780600   -0.10351400
C      -3.08445500   -6.41826400    0.06176300
C      -3.44893300   -5.10705900    0.14418200
H       0.57162300    1.97836300    0.82107200
H       0.37977000    2.03810900   -0.92208700
H      -1.05549600    1.99720500    0.11761700
H       0.94424400   -0.36035100   -0.18510500
H      -2.09745100   -0.21084800    0.15891100
H      -0.12318100   -2.57784800   -0.14402600
H      -3.17739300   -2.39848700    0.20380500
H      -1.05867300   -7.40358000   -0.19617100
H      -3.74321700   -7.27486300    0.10829200
H      -4.44743200   -4.71220200    0.26815800
""",
)

entry(
    index = 35,
    label = "C10H11_32",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {5,S} {6,D}
3  C u1 p0 c0 {1,S} {2,S} {13,S}
4  C u0 p0 c0 {1,S} {5,D} {14,S}
5  C u0 p0 c0 {2,S} {4,D} {19,S}
6  C u0 p0 c0 {2,D} {8,S} {18,S}
7  C u0 p0 c0 {8,D} {9,S} {16,S}
8  C u0 p0 c0 {6,S} {7,D} {17,S}
9  C u0 p0 c0 {7,S} {10,D} {15,S}
10 C u0 p0 c0 {9,D} {20,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.03505,0.0964086,-6.24915e-05,1.44188e-08,7.04055e-13,36134.4,40.8725], Tmin=(200,'K'), Tmax=(1095.13,'K')),
            NASAPolynomial(coeffs=[13.2891,0.0533454,-2.61918e-05,6.13024e-09,-5.56227e-13,31565.9,-43.8995], Tmin=(1095.13,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (296.849,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 6, 'C=C': 4, 'C-H': 11}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: scan has a barrier larger than 40 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: scan has a barrier larger than 40 kJ/mol
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 38.94 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: scan has a barrier larger than 40 kJ/mol
* Invalidated! pivots: [1, 2], dihedral: [12, 1, 2, 3], invalidation reason: scan has a barrier larger than 40 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -0.01863100    1.48426100    0.00874500
C       0.01434200    0.13068800    0.00093500
C       1.20071400   -0.65726500   -0.01220800
C       1.21417200   -2.04640300   -0.02013900
C       2.36603900   -2.82355200   -0.03316300
C       2.41681100   -4.24805200   -0.04187400
C       3.55880200   -5.01197600   -0.05507400
H       4.57170100   -4.63196300   -0.06055200
C       3.20422900   -6.46868500   -0.06088400
C       1.69854100   -6.44550900   -0.04938600
C       1.26351300   -5.17625900   -0.03856500
H       0.89381900    2.07152000    0.00529500
H      -0.95456400    2.02860200    0.01870500
H      -0.93020500   -0.41097100    0.00487000
H       2.15332700   -0.13097600   -0.01631700
H       0.25053700   -2.55133400   -0.01579500
H       3.32312600   -2.30692900   -0.03738800
H       3.60110900   -6.99109500   -0.94320900
H       3.61436200   -7.00138600    0.80914800
H       1.08312200   -7.33525100   -0.04992800
H       0.22714300   -4.86636600   -0.02880600
""",
)

entry(
    index = 36,
    label = "C8H9_12",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {3,S} {4,B} {5,B}
3  C u1 p0 c0 {1,S} {2,S} {12,S}
4  C u0 p0 c0 {2,B} {6,B} {13,S}
5  C u0 p0 c0 {2,B} {8,B} {17,S}
6  C u0 p0 c0 {4,B} {7,B} {14,S}
7  C u0 p0 c0 {6,B} {8,B} {15,S}
8  C u0 p0 c0 {5,B} {7,B} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.609542,0.0568654,-6.91216e-06,-2.48497e-08,1.15293e-11,19332.7,30.1599], Tmin=(200,'K'), Tmax=(1048.04,'K')),
            NASAPolynomial(coeffs=[7.94572,0.0462593,-2.32855e-05,5.6368e-09,-5.30699e-13,16328.7,-17.2921], Tmin=(1048.04,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (158.226,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C=C': 3, 'C-C': 5, 'C-H': 9}
1D rotors:
pivots: [1, 2], dihedral: [10, 1, 2, 4], rotor symmetry: 3, max scan energy: 0.89 kJ/mol
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 5], invalidation reason: scan has a barrier larger than 40 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -0.07549200    1.53070200   -0.08152700
C       0.00783200    0.04110500    0.01181400
H      -0.44742300   -0.54515700   -0.77976500
C       0.63823100   -0.66704500    1.06007200
C       1.27001700   -0.01442300    2.15621900
C       1.87739400   -0.74103500    3.16716000
C       1.88534600   -2.13884900    3.13577700
C       1.27146800   -2.80574200    2.06869000
C       0.66197700   -2.09114400    1.05401500
H       0.91820900    1.99720200   -0.11228400
H      -0.61143700    1.84086300   -0.97987100
H      -0.59533300    1.96865000    0.78100600
H       1.27560700    1.06819900    2.20104900
H       2.35119600   -0.21845500    3.99123900
H       2.36232800   -2.70092700    3.93018600
H       1.27339700   -3.88990300    2.03681900
H       0.18838200   -2.61582100    0.23057000
""",
)

entry(
    index = 37,
    label = "C8H9_17",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,D} {5,S}
3  C u0 p0 c0 {1,S} {6,D} {11,S}
4  C u0 p0 c0 {2,D} {7,S} {14,S}
5  C u0 p0 c0 {2,S} {8,D} {13,S}
6  C u0 p0 c0 {3,D} {7,S} {15,S}
7  C u1 p0 c0 {4,S} {6,S} {12,S}
8  C u0 p0 c0 {5,D} {16,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.17887,0.0631665,-1.31166e-05,-2.32474e-08,1.15979e-11,27026.2,31.0639], Tmin=(200,'K'), Tmax=(1065.32,'K')),
            NASAPolynomial(coeffs=[10.7459,0.044278,-2.29685e-05,5.72619e-09,-5.53759e-13,23016.5,-34.1147], Tmin=(1065.32,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (221.858,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C=C': 3, 'C-C': 5, 'C-H': 9}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 39.65 kJ/mol
* Invalidated! pivots: [1, 2], dihedral: [10, 1, 2, 3], invalidation reason: scan has a barrier larger than 40 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -0.10708300    1.37761900    0.00977900
C       0.04496900    0.03677100   -0.00120600
C       1.28911200   -0.68442100   -0.01630200
C       1.29646200   -2.07419800   -0.02663500
C       2.47553900   -2.81982200   -0.04138100
H       2.43217300   -3.90212700   -0.04891800
C       3.74062400   -2.15949700   -0.04658600
C       3.81977900   -0.80653500   -0.03724900
C       2.60013200    0.06674100   -0.02102400
H       0.73543400    2.05922900    0.00804600
H      -1.09241600    1.82687300    0.02085900
H      -0.85130400   -0.58056200    0.00138800
H       0.34244100   -2.59363800   -0.02292600
H       4.64808000   -2.75418800   -0.05820000
H       4.78602900   -0.31305700   -0.04130600
H       2.62828800    0.75557800   -0.88247000
H       2.64203000    0.74242200    0.85023000
""",
)

# Species with imaginary frequencies from first run which converged on the second run

entry(
    index = 38,
    label = "C10H8_11",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {9,S}
3  C u0 p0 c0 {1,B} {6,B} {14,S}
4  C u0 p0 c0 {2,B} {5,B} {11,S}
5  C u0 p0 c0 {4,B} {6,B} {12,S}
6  C u0 p0 c0 {3,B} {5,B} {13,S}
7  C u0 p0 c0 {1,S} {8,D} {15,S}
8  C u0 p0 c0 {7,D} {16,S} {17,S}
9  C u0 p0 c0 {2,S} {10,T}
10 C u0 p0 c0 {9,T} {18,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.57062,0.0900569,-6.93325e-05,2.3852e-08,-2.33051e-12,43674.1,37.8577], Tmin=(200,'K'), Tmax=(1104.61,'K')),
            NASAPolynomial(coeffs=[15.0272,0.0396578,-1.89892e-05,4.38968e-09,-3.97526e-13,38973.3,-52.4727], Tmin=(1104.61,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (359.779,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (428.195,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 5, 'C=C': 4, 'C#C': 1, 'C-H': 8}
1D rotors:
pivots: [1, 7], dihedral: [2, 1, 7, 8], rotor symmetry: 1, max scan energy: 17.76 kJ/mol
* Invalidated! pivots: [2, 9], dihedral: [1, 2, 9, 10], invalidation reason: scan job crashed


External symmetry: 1, optical isomers: 2

Geometry:
C      -0.14045900   -0.58610900   -0.05054100
C      -0.07284100    0.83034900   -0.01783500
C       1.06584600   -1.30168000   -0.03764600
C       1.17708400    1.47058800    0.04264600
C       2.35236300    0.73502900    0.06693000
C       2.29414300   -0.65869000    0.02439900
C      -1.44486000   -1.26412900   -0.10953200
C      -1.68707900   -2.54507200    0.18032400
C      -1.25318700    1.63488100   -0.03481000
C      -2.23185300    2.33710200   -0.04875000
H       1.20565800    2.55297900    0.07071300
H       3.30861700    1.24318800    0.11088600
H       3.20785800   -1.24216800    0.02955500
H       1.03662800   -2.38303100   -0.09713300
H      -2.27896400   -0.63405100   -0.40203400
H      -0.91521800   -3.22778300    0.51831700
H      -2.68812600   -2.95120100    0.09933500
H      -3.09542700    2.95564100   -0.05794100
""",
)

entry(
    index = 39,
    label = "C10H9_29",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {4,B} {7,S}
2  C u0 p0 c0 {1,B} {3,B} {8,S}
3  C u0 p0 c0 {2,B} {5,B} {11,S}
4  C u0 p0 c0 {1,B} {6,B} {14,S}
5  C u0 p0 c0 {3,B} {6,B} {12,S}
6  C u0 p0 c0 {4,B} {5,B} {13,S}
7  C u0 p0 c0 {1,S} {10,D} {15,S}
8  C u1 p0 c0 {2,S} {16,S} {17,S}
9  C u0 p0 c0 {10,D} {18,S} {19,S}
10 C u0 p0 c0 {7,D} {9,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.79269,0.0943294,-7.30511e-05,2.64608e-08,-3.18406e-12,47572.6,39.8915], Tmin=(200,'K'), Tmax=(1127.76,'K')),
            NASAPolynomial(coeffs=[14.9799,0.0430945,-2.06025e-05,4.73575e-09,-4.25156e-13,42813.4,-51.3152], Tmin=(1127.76,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (392.107,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (453.139,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C-C': 5, 'C=C': 5, 'C-H': 9}
1D rotors:
pivots: [1, 7], dihedral: [2, 1, 7, 10], rotor symmetry: 1, max scan energy: 16.16 kJ/mol
* Invalidated! pivots: [2, 8], dihedral: [1, 2, 8, 16], invalidation reason: scan has a barrier larger than 40 kJ/mol
* Invalidated! pivots: [7, 10], dihedral: [1, 7, 10, 9], invalidation reason: scan job crashed


External symmetry: 1, optical isomers: 2

Geometry:
C       0.05243600    0.13496000   -0.00213700
C      -1.32192900    0.55722200    0.12041000
C      -2.32500500   -0.46300500    0.13331700
C       0.33463100   -1.23250500   -0.08662100
C      -2.01052400   -1.79976200    0.04675700
C      -0.66698700   -2.19427500   -0.06169400
C       1.14132300    1.12059900   -0.04638400
C      -1.72315700    1.89397200    0.23693500
C       3.70399200    0.60215900   -0.03041600
C       2.42728000    0.85320400   -0.03875200
H      -3.36117100   -0.15413900    0.22038200
H      -2.79739700   -2.54548800    0.06195700
H      -0.40991800   -3.24483700   -0.13172100
H       1.36974900   -1.54176700   -0.18008300
H       0.86836300    2.17007100   -0.09703500
H      -2.77549000    2.13479800    0.31904700
H      -1.03077200    2.72249700    0.26231300
H       4.25874000    0.44520700   -0.95216100
H       4.26583700    0.54108800    0.89827400
""",
)

entry(
    index = 40,
    label = "N15-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {15,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {8,S}
4  C u0 p0 c0 {2,B} {9,S} {10,B}
5  C u0 p0 c0 {3,B} {11,B} {13,S}
6  C u1 p0 c0 {1,S} {12,S} {16,S}
7  C u0 p0 c0 {1,S} {8,D} {17,S}
8  C u0 p0 c0 {3,S} {7,D} {19,S}
9  C u0 p0 c0 {4,S} {12,D} {21,S}
10 C u0 p0 c0 {4,B} {11,B} {22,S}
11 C u0 p0 c0 {5,B} {10,B} {23,S}
12 C u0 p0 c0 {6,S} {9,D} {20,S}
13 C u0 p0 c0 {5,S} {14,D} {18,S}
14 C u0 p0 c0 {13,D} {24,S} {25,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {13,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {12,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {14,S}
25 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78472,0.013241,0.00035794,-7.28989e-07,4.59407e-10,48879.4,16.2332], Tmin=(10,'K'), Tmax=(505.2,'K')),
            NASAPolynomial(coeffs=[-2.87694,0.112387,-7.42057e-05,2.30778e-08,-2.72228e-12,48960.3,37.9628], Tmin=(505.2,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (406.339,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (602.799,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Bond corrections: {'C=C': 6, 'C-C': 10, 'C-H': 11}
1D rotors:
pivots: [5, 13], dihedral: [3, 5, 13, 14], rotor symmetry: 1, max scan energy: 18.27 kJ/mol
* Invalidated! pivots: [13, 14], dihedral: [5, 13, 14, 24], invalidation reason: scan has a barrier larger than 40 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       1.71086300   -1.26419500    0.30977000
C       0.74586300   -0.12777900    0.23982900
C      -0.56252300   -0.57483400    0.39379500
C       1.09183200    1.17820200   -0.10934500
C      -1.62342000    0.35709900    0.39180100
C       2.89260700   -1.03345000   -0.58857900
C       0.77705200   -2.46143900    0.29955500
C      -0.50017200   -2.04660800    0.42892100
C       2.41526300    1.37946200   -0.61386100
C       0.03061100    2.11980200   -0.09116600
C      -1.26557500    1.71310200    0.17820700
C       3.22907600    0.25935900   -0.91552600
C      -3.00606800   -0.08007500    0.58050900
C      -4.11767800    0.66308000    0.50222500
H       2.12653400   -1.26928100    1.34277700
H       3.53919700   -1.86090500   -0.85763700
H       1.11443700   -3.48960000    0.31666400
H      -3.12627900   -1.13537500    0.81065600
H      -1.35556400   -2.70167200    0.53040600
H       4.15421000    0.43447700   -1.45584900
H       2.74206900    2.37311100   -0.89826600
H       0.22912800    3.16072500   -0.32425800
H      -2.04669000    2.46428900    0.18811400
H      -5.09218400    0.22093200    0.66959000
H      -4.10259200    1.72157200    0.26906800
""",
)
