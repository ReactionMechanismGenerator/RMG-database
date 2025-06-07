#!/usr/bin/env python
# encoding: utf-8

name = "phi05_2"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "[O]OC[=O]O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {1,S} {6,S}
4 O u0 p2 c0 {1,D}
5 O u1 p2 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88492,0.00720949,8.56618e-05,-2.06726e-07,1.40058e-10,-36327.1,10.0503], Tmin=(10,'K'), Tmax=(527.147,'K')),
            NASAPolynomial(coeffs=[5.45622,0.0188774,-1.46672e-05,5.05104e-09,-6.39e-13,-36820.6,0.36677], Tmin=(527.147,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-302.076,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (124.717,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'O-O': 1, 'C-O': 2, 'H-O': 1}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 25.16 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 6], rotor symmetry: 1, max scan energy: 40.62 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       1.97154800   -0.51314500   -0.06349200
O       0.67270200   -0.69642200    0.09340900
C      -0.06751500    0.43319400   -0.33328700
O       0.38354600    1.43317000   -0.77936900
O      -1.33426100    0.09614400   -0.11405700
H      -1.88307700    0.84402600   -0.39292900
""",
)

entry(
    index = 1,
    label = "O[C]1OOO1",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {5,S}
2 O u0 p2 c0 {1,S} {4,S}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p2 c0 {2,S} {3,S}
5 O u0 p2 c0 {1,S} {6,S}
6 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90463,0.00589849,7.81231e-05,-1.80117e-07,1.18554e-10,9650.5,9.9171], Tmin=(10,'K'), Tmax=(534.789,'K')),
            NASAPolynomial(coeffs=[4.86565,0.0187317,-1.40288e-05,4.76438e-09,-5.9818e-13,9261.41,3.2054], Tmin=(534.789,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (80.2075,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'O-O': 2, 'C-O': 3, 'H-O': 1}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 3], rotor symmetry: 1, max scan energy: 17.33 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       1.25547800   -0.10084000    0.43121100
C       0.11531600   -0.08069300   -0.27714900
O      -0.61842800    1.10069200   -0.25205800
O      -1.80956900    0.29758000    0.05355500
O      -0.92934600   -0.86996000    0.19234100
H       1.98655100   -0.34677900   -0.14790000
""",
)

entry(
    index = 2,
    label = "[O][C]1OO1",
    molecule = 
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {4,S}
3 O u1 p2 c0 {4,S}
4 C u1 p0 c0 {1,S} {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16232,0.0926311,-0.000549637,1.29378e-06,-1.05934e-09,-11777,15.6206], Tmin=(10,'K'), Tmax=(388.93,'K')),
            NASAPolynomial(coeffs=[6.54607,0.00420699,-1.79705e-06,2.3099e-10,7.54724e-15,-11634.7,7.70545], Tmin=(388.93,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-97.9559,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'O-O': 1}

External symmetry: 1, optical isomers: 1

Geometry:
O       1.36797300   -0.75525400    0.27943300
C       2.09070800    0.09366700    0.09443800
O      -1.48598500    0.87122900   -0.31715400
O      -1.97269600   -0.20964100   -0.05671800
""",
)

entry(
    index = 3,
    label = "[O]C[=O]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {5,S}
2 O u1 p2 c0 {4,S}
3 O u0 p2 c0 {4,D}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96887,0.00169203,3.94826e-05,-6.91081e-08,3.59659e-11,-38527.7,8.4465], Tmin=(10,'K'), Tmax=(634.15,'K')),
            NASAPolynomial(coeffs=[3.02302,0.0154686,-1.15787e-05,3.99334e-09,-5.09425e-13,-38564.8,11.3406], Tmin=(634.15,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-320.352,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (103.931,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'C-O': 2, 'H-O': 1}
1D rotors:
pivots: [2, 4], dihedral: [1, 2, 4, 5], rotor symmetry: 2, max scan energy: 33.72 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.49052300    0.83432000   -0.92320200
C      -0.32015100   -0.14009300   -0.13752900
O      -1.19378700   -1.01499700   -0.17822400
O       0.72010700   -0.22944700    0.67921700
H       1.28435300    0.55021700    0.55973900
""",
)