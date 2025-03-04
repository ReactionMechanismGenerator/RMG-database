#!/usr/bin/env python
# encoding: utf-8

name = "oxygenated_fuels"
shortDesc = u""
longDesc = u"""
Thermodynamic properties for pyrolysis and combustion of oxygenated fuels
"""

entry(
    index = 0,
    label = "C1=COCC1",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {5,S} {11,S}
5  O u0 p2 c0 {2,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08768,-0.00668489,0.000122976,-1.76005e-07,8.04191e-11,-12067,10.1471], Tmin=(10,'K'), Tmax=(674.754,'K')),
            NASAPolynomial(coeffs=[-1.85954,0.0447349,-2.72651e-05,7.93817e-09,-8.86948e-13,-11632.4,33.7726], Tmin=(674.754,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-100.324,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CCSD(T)-F12/cc-pVTZ-F12//wB97xD/def2TZVP

Bond corrections: {'C-O': 2, 'C-H': 6, 'C-C': 2, 'C=C': 1}

External symmetry: 1, optical isomers: 2

Geometry:
C       0.81332100    0.85267800    0.04904000
C       1.36827300   -0.34483800   -0.05768400
O       0.49981300   -1.38146200   -0.16624100
C      -0.81831700   -0.83956800    0.03631900
C      -0.68413700    0.69292600   -0.02751900
H       1.34236000    1.78827500    0.12332200
H       2.41156200   -0.62287700   -0.08454600
H      -1.16516400   -1.17208300    1.01776500
H      -1.47205000   -1.25511100   -0.72884300
H      -1.21123800    1.17621000    0.79641100
H      -1.08442400    1.10585200   -0.95802400
""",
)

entry(
    index = 1,
    label = "C=CCC=O",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {1,S} {8,D} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65263,0.0377385,-0.000117655,3.1866e-07,-2.88323e-10,-12711.4,11.9246], Tmin=(10,'K'), Tmax=(406.905,'K')),
            NASAPolynomial(coeffs=[1.0455,0.0375814,-2.20192e-05,6.23303e-09,-6.84344e-13,-12285.7,24.7813], Tmin=(406.905,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-105.701,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CCSD(T)-F12/cc-pVTZ-F12//wB97xD/def2TZVP

Bond corrections: {'C-H': 6, 'C-C': 2, 'C=O': 1, 'C=C': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 9.62 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 9.73 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.84925000   -0.45324100   -0.22514900
C      -0.68978200    0.15178400   -0.42149000
C       0.44849700    0.12125600    0.54582500
C       1.77584400   -0.26808200   -0.05560200
O       1.97240500   -0.47403300   -1.21938900
H      -2.64593400   -0.39502600   -0.95559000
H      -2.04552000   -1.03218300    0.67109100
H      -0.52123600    0.71037000   -1.33590400
H       0.60603900    1.11057500    0.99755300
H       0.24854100   -0.55226500    1.38555100
H       2.60573100   -0.34334500    0.67845000
""",
)

entry(
    index = 2,
    label = "CCC=C=O",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7482,0.0239823,4.94456e-06,-1.74078e-08,6.84307e-12,-13618.4,11.2344], Tmin=(10,'K'), Tmax=(1006.41,'K')),
            NASAPolynomial(coeffs=[4.23712,0.0299053,-1.56075e-05,3.97266e-09,-3.9723e-13,-14115.2,6.89336], Tmin=(1006.41,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-113.239,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CCSD(T)-F12/cc-pVTZ-F12//wB97xD/def2TZVP

Bond corrections: {'C-H': 6, 'C-C': 2, 'C=O': 1, 'C=C': 1}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 3], rotor symmetry: 3, max scan energy: 13.44 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 6.33 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.34873100    0.40939300    0.28904400
C      -0.29770100   -0.32710800   -0.53619200
C      -0.70407300   -1.74406000   -0.86653900
C      -0.88652200   -2.17146100   -2.08808100
O      -1.04245000   -2.54412400   -3.17430200
H      -1.54963700   -0.11784100    1.22380700
H      -2.28881600    0.48664900   -0.25907900
H      -1.01069700    1.41721000    0.53739000
H      -0.10343900    0.22090600   -1.46012600
H       0.64853000   -0.34827700    0.01117900
H      -0.88108700   -2.46420800   -0.07778300
""",
)

entry(
    index = 3,
    label = "C=C=O",
    molecule =
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9814,0.00110135,3.63061e-05,-6.56405e-08,3.73659e-11,-7925.38,4.88101], Tmin=(10,'K'), Tmax=(539.067,'K')),
            NASAPolynomial(coeffs=[2.84308,0.0133374,-8.28633e-06,2.54759e-09,-3.0505e-13,-7857.71,9.15866], Tmin=(539.067,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-65.9027,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CCSD(T)-F12/cc-pVTZ-F12//wB97xD/def2TZVP

Bond corrections: {'C-H': 2, 'C=O': 1, 'C=C': 1}

External symmetry: 2, optical isomers: 1

Geometry:
C      -0.54197900    0.01171500    0.00819000
C       0.76458600   -0.01652700   -0.01155400
O       1.91904400   -0.04148000   -0.02900000
H      -1.09115500   -0.91652100    0.01492100
H      -1.05049500    0.96281200    0.01744300
""",
)

entry(
    index = 4,
    label = "C1CCOC1",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
5  O u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05456,-0.00405656,0.000121844,-1.67276e-07,7.34872e-11,-24755.3,10.1401], Tmin=(10,'K'), Tmax=(667.796,'K')),
            NASAPolynomial(coeffs=[-4.05532,0.0545605,-3.23728e-05,9.19403e-09,-1.0056e-12,-23896,44.3149], Tmin=(667.796,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-205.822,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CCSD(T)-F12/cc-pVTZ-F12//wB97xD/def2TZVP

Bond corrections: {'C-O': 2, 'C-H': 8, 'C-C': 3}

External symmetry: 2, optical isomers: 2

Geometry:
C      -0.90336800   -0.47199800    0.33342400
C       0.43887900   -0.95559600   -0.21035400
C       1.31315000    0.27476500    0.00257800
O       0.45550300    1.39997700   -0.12068900
C      -0.90294400    0.98599000   -0.11126500
H      -0.91664800   -0.53829300    1.42350800
H      -1.75584400   -1.02919000   -0.05328700
H       0.35595500   -1.18498200   -1.27494700
H       0.82303500   -1.83777200    0.30044300
H       2.11608300    0.36198800   -0.73208400
H       1.76258300    0.26810800    1.00302600
H      -1.32120800    1.08844500   -1.11997200
H      -1.46517600    1.63855900    0.55962000
""",
)

entry(
    index = 5,
    label = "C=CCCO",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {2,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86023,0.0105006,0.000186149,-5.19904e-07,4.49027e-10,-22084.4,10.4303], Tmin=(10,'K'), Tmax=(382.649,'K')),
            NASAPolynomial(coeffs=[3.2863,0.0402005,-2.3183e-05,6.66791e-09,-7.57309e-13,-22214,10.3807], Tmin=(382.649,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-183.608,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CCSD(T)-F12/cc-pVTZ-F12//wB97xD/def2TZVP

Bond corrections: {'C-O': 1, 'C-H': 7, 'H-O': 1, 'C-C': 2, 'C=C': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 18.86 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [4, 5], dihedral: [3, 4, 5, 13], rotor symmetry: 1, max scan energy: 14.13 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C       1.88016800    0.49512300   -0.16819800
C       0.90396600   -0.04076900    0.55063000
C      -0.20319600   -0.88272700   -0.00241700
C      -1.52420700   -0.11221700   -0.02974000
O      -1.48265800    0.99556600   -0.89819600
H       1.96281500    0.30794600   -1.23361100
H       2.63774200    1.12403700    0.28256500
H       0.85702900    0.17088800    1.61667400
H       0.03753000   -1.20496000   -1.01808600
H      -0.33606500   -1.77778500    0.61241700
H      -1.79185800    0.19786000    0.98995400
H      -2.32146700   -0.75917600   -0.39739300
H      -0.69865400    1.50955300   -0.68629600
""",
)

entry(
    index = 6,
    label = "CCCC=O",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,D} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47703,0.0506886,-0.000146302,3.16247e-07,-2.35257e-10,-28471.2,9.59924], Tmin=(10,'K'), Tmax=(479.292,'K')),
            NASAPolynomial(coeffs=[0.444874,0.0438398,-2.4238e-05,6.49269e-09,-6.78869e-13,-27811.2,25.8505], Tmin=(479.292,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-236.73,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CCSD(T)-F12/cc-pVTZ-F12//wB97xD/def2TZVP

Bond corrections: {'C-H': 8, 'C-C': 3, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 3], rotor symmetry: 3, max scan energy: 12.49 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 7.54 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C      -1.78326700    0.25332600   -0.02311900
C      -0.36523600    0.10464200   -0.55758800
C      -0.22953800   -1.06526000   -1.51726400
C       1.14811300   -1.26694400   -2.08150800
O       2.10299200   -0.58635600   -1.82765800
H      -2.09864100   -0.64276200    0.51670800
H      -1.85797600    1.09793400    0.66286800
H      -2.49643400    0.41919200   -0.83412400
H      -0.05667200    1.02042200   -1.06596700
H       0.33629700   -0.02865500    0.26848600
H      -0.51967000   -2.00987700   -1.03957300
H      -0.91174400   -0.96318900   -2.37098600
H       1.24242900   -2.12357200   -2.78271700
""",
)

entry(
    index = 7,
    label = "C=CCOC",
    molecule =
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {5,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.52299,0.0511405,-0.000175398,4.40761e-07,-3.72365e-10,-16268.2,9.57118], Tmin=(10,'K'), Tmax=(424.962,'K')),
            NASAPolynomial(coeffs=[0.468821,0.044179,-2.47818e-05,6.7473e-09,-7.16356e-13,-15686.2,25.4859], Tmin=(424.962,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-135.274,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CCSD(T)-F12/cc-pVTZ-F12//wB97xD/def2TZVP

Bond corrections: {'C-O': 2, 'C-H': 8, 'C-C': 1, 'C=C': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 12.45 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [4, 5], dihedral: [3, 4, 5, 11], rotor symmetry: 3, max scan energy: 9.81 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
C       2.25315700    1.05785400    0.21632400
C       1.12544100    0.59420800    0.72705100
C       0.19487000   -0.35427000    0.04582500
O       0.66498000   -0.70328000   -1.22377400
C      -0.18550100   -1.59334300   -1.89160900
H       2.58327900    0.76345200   -0.77131900
H       2.87591300    1.74504300    0.77441600
H       0.80834900    0.89967800    1.71992200
H      -0.80329400    0.10771100   -0.02847500
H       0.07329600   -1.25439000    0.67055000
H      -1.18284800   -1.15959100   -2.04349200
H       0.25921000   -1.80545900   -2.86260700
H      -0.29777300   -2.53487900   -1.33770000
""",
)

entry(
    index = 8,
    label = "[CH2]COC=C",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,D} {5,S} {10,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72362,0.0268578,8.74998e-06,-2.45029e-08,9.84034e-12,5114.46,11.6462], Tmin=(10,'K'), Tmax=(960.915,'K')),
            NASAPolynomial(coeffs=[4.14178,0.0347162,-1.85013e-05,4.79944e-09,-4.87882e-13,4590.93,7.33954], Tmin=(960.915,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (42.5173,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CCSD(T)-F12/cc-pVTZ-F12//wB97xD/def2TZVP

Bond corrections: {'C-H': 7, 'C=C': 1, 'C-O': 2, 'C-C': 1}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 3], rotor symmetry: 1, max scan energy: 4.31 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.23239600    0.08686700    0.14470500
C      -0.79799800   -0.24053500    0.05082900
O      -0.46692000   -0.49806300   -1.29838500
C       0.80987900   -0.82463900   -1.56547500
C       1.82658100   -0.93551100   -0.71729700
H      -2.88344200   -0.07694000   -0.70093300
H      -2.64414900    0.41994000    1.08609100
H      -0.17655400    0.58261600    0.43582900
H      -0.54927500   -1.12515100    0.66149200
H       0.93365400   -1.00124500   -2.62725200
H       1.74299800   -0.76654700    0.34640400
H       2.79589200   -1.20947000   -1.10650600
""",
)

entry(
    index = 9,
    label = "[CH2]CCC=O",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {9,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {4,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62614,0.0402174,-0.000111984,3.0444e-07,-2.77245e-10,-3673.44,12.1899], Tmin=(10,'K'), Tmax=(409.884,'K')),
            NASAPolynomial(coeffs=[0.690784,0.0426639,-2.50594e-05,7.11512e-09,-7.83607e-13,-3212.73,26.4179], Tmin=(409.884,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-30.5554,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CCSD(T)-F12/cc-pVTZ-F12//wB97xD/def2TZVP

Bond corrections: {'C-H': 7, 'C-C': 3, 'C=O': 1}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 3], rotor symmetry: 1, max scan energy: 1.55 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.85858400    0.07568800   -0.63821400
C      -0.54008600    0.61664700   -0.22904100
C       0.52102800    0.49190700   -1.31166200
C       1.87921300    1.00003900   -0.92005900
O       2.15678800    1.46832500    0.14906500
H      -1.93966000   -0.66971200   -1.41910300
H      -2.74945600    0.31809100   -0.07553800
H      -0.17896700    0.10528600    0.67505700
H      -0.63360000    1.66445100    0.07222700
H       0.22558800    1.02672600   -2.22211800
H       0.64771600   -0.55192200   -1.62471800
H       2.65286000    0.91535600   -1.71241500
""",
)

entry(
    index = 10,
    label = "[CH2]CCC[O]_S",
    molecule =
"""
multiplicity 1
1  C u1 p0 c0 {2,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {12,S} {13,S}
5  O u1 p2 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7441,0.0268162,1.94111e-05,-3.82824e-08,1.51967e-11,2850.68,10.4451], Tmin=(10,'K'), Tmax=(925.719,'K')),
            NASAPolynomial(coeffs=[3.66378,0.0395904,-2.14243e-05,5.62719e-09,-5.77886e-13,2333.07,7.95039], Tmin=(925.719,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (23.7061,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CCSD(T)-F12/cc-pVTZ-F12//wB97xD/def2TZVP

Bond corrections: {'C-H': 8, 'C-O': 1, 'C-C': 3}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 3], rotor symmetry: 2, max scan energy: 9.23 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Bond ([[4, 12]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[4, 12]]) broke during the scan. But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Bond ([[1, 2]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[1, 2]]) broke during the scan. But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
C      -2.08594000   -0.12658400   -0.14140200
C      -0.67052800    0.16011700   -0.47462300
C      -0.53926900    0.83368000   -1.84320900
C      -1.13115700   -0.08093900   -2.91431600
O      -1.32987000    0.46801000   -4.11820200
H      -2.38379300   -1.04570500    0.34373700
H      -2.83038900    0.65466800   -0.24066300
H      -0.08245200   -0.76146500   -0.45185900
H      -0.22745800    0.82074600    0.28322600
H       0.50500700    1.05436100   -2.07314300
H      -1.08719600    1.77888400   -1.85304800
H      -2.15656200   -0.35467000   -2.54238200
H      -0.59868500   -1.04781800   -2.96494800
""",
)

entry(
    index = 11,
    label = "[CH2]COC[CH2]_S",
    molecule =
"""
multiplicity 1
1  C u1 p0 c0 {2,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  C u1 p0 c0 {4,S} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6039,0.0371534,-1.38363e-05,-1.56495e-09,1.57882e-12,15295.7,10.4484], Tmin=(10,'K'), Tmax=(1262.1,'K')),
            NASAPolynomial(coeffs=[8.08415,0.0302951,-1.44099e-05,3.34665e-09,-3.06972e-13,13580.1,-14.5254], Tmin=(1262.1,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (127.143,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
CCSD(T)-F12/cc-pVTZ-F12//wB97xD/def2TZVP

Bond corrections: {'C-H': 8, 'C-O': 2, 'C-C': 2}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [6, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Bond ([[1, 2]]) broke during the scan. But unable to propose troubleshooting methods.Bond ([[1, 2]]) broke during the scan. But unable to propose troubleshooting methods.
pivots: [4, 5], dihedral: [3, 4, 5, 12], rotor symmetry: 2, max scan energy: 6.62 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
C      -1.38556500    0.36512200   -0.90413200
C      -1.09097300    0.43619600    0.54713800
O      -1.73154800   -0.57450400    1.29453200
C      -1.24758200   -1.86094200    0.98174800
C      -2.06731900   -2.88487000    1.64265900
H      -2.38828000    0.12045500   -1.23033900
H      -0.66635200    0.70148200   -1.63810600
H      -1.45803200    1.37878700    0.97292100
H      -0.00455200    0.41171000    0.71938000
H      -0.18895400   -1.95433400    1.27384300
H      -1.26693900   -1.99200700   -0.12118300
H      -1.66488200   -3.87014400    1.82852200
H      -3.11388500   -2.69297300    1.83218400
""",
)

