#!/usr/bin/env python
# encoding: utf-8

name = "FA2025"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "DHC",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p1 c+1 {3,D} {4,S}
3 C u0 p1 c-1 {1,S} {2,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07335,-0.00551665,5.35174e-05,-7.42433e-08,3.36234e-11,-26056.1,6.51176], Tmin=(10,'K'), Tmax=(669.93,'K')),
            NASAPolynomial(coeffs=[1.39698,0.0166722,-1.00661e-05,2.86469e-09,-3.13776e-13,-25836.8,17.3117], Tmin=(669.93,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-216.634,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (103.931,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 2, 'C-O': 2}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 5], rotor symmetry: 1, max scan energy: 76.57 kJ/mol
* Invalidated! pivots: [1, 2], dihedral: [4, 1, 2, 3], invalidation reason: Another conformer for DHC exists which is 3.74 kJ/mol lower.Another conformer for DHC exists which is 3.74 kJ/mol lower.


External symmetry: 1, optical isomers: 1

Geometry:
O      -0.78982700   -0.69533800    0.24542900
C      -0.29640200    0.46228900    0.60519900
O      -0.87328500    1.39980900   -0.15486200
H      -1.44656600   -0.59221300   -0.47698800
H      -0.50625500    2.25078100    0.11425000
""",
)

entry(
    index = 1,
    label = "O=C1OOO1",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {3,S} {5,S}
3 O u0 p2 c0 {1,S} {2,S}
4 O u0 p2 c0 {5,D}
5 C u0 p0 c0 {1,S} {2,S} {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9588,0.00225325,4.9986e-05,-8.93951e-08,4.71859e-11,-19013.3,7.89072], Tmin=(10,'K'), Tmax=(629.161,'K')),
            NASAPolynomial(coeffs=[2.92159,0.0191089,-1.46647e-05,5.03245e-09,-6.36001e-13,-19085.9,10.8], Tmin=(629.161,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-158.105,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'C=O': 1, 'O-O': 2}

External symmetry: 2, optical isomers: 1

Geometry:
O       1.69896900   -0.10715400   -0.38756400
C       0.52638500   -0.03319900   -0.41099400
O      -0.35389500    0.78723700    0.23965400
O      -1.44808700    0.09133100   -0.45044800
O      -0.42337200   -0.73821500   -1.09821000
""",
)

entry(
    index = 2,
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

entry(
    index = 3,
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
    index = 4,
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
    index = 5,
    label = "[C]1OO1",
    molecule = 
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u2 p0 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02353,-0.00205332,2.01618e-05,-3.30115e-08,1.81491e-11,26414.8,6.69132], Tmin=(10,'K'), Tmax=(543.095,'K')),
            NASAPolynomial(coeffs=[3.37855,0.00442935,-2.52748e-06,7.13421e-10,-7.88855e-14,26459.3,9.17402], Tmin=(543.095,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (219.626,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 2, 'O-O': 1}

External symmetry: 2, optical isomers: 1

Geometry:
C      -0.14871100    0.61738500   -0.01032400
O      -0.83209300   -0.52801300   -0.05350100
O       0.98080500   -0.08937200    0.06382500
""",
)

entry(
    index = 6,
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
    index = 7,
    label = "[O]C1[O]OO1",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {5,S} {6,S}
4 O u1 p2 c0 {5,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92232,0.00476147,7.29026e-05,-1.60404e-07,1.02914e-10,-35594.7,10.2387], Tmin=(10,'K'), Tmax=(537.749,'K')),
            NASAPolynomial(coeffs=[4.23929,0.0190827,-1.35694e-05,4.4765e-09,-5.53349e-13,-35870,6.66386], Tmin=(537.749,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-295.978,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 4, 'H-O': 1, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 6], invalidation reason: Another conformer for [O]C1[O]OO1[323] exists which is 2.67 kJ/mol lower.Another conformer for [O]C1[O]OO1[323] exists which is 2.67 kJ/mol lower.


External symmetry: 1, optical isomers: 1

Geometry:
O       0.13168800    1.56944100   -0.39826200
C      -0.01896600    0.42541800   -0.10941300
O       0.89006200   -0.49985100    0.15169600
O      -1.33292400   -0.07273100   -0.01693000
O      -1.42331600   -1.35383600    0.30862600
H       1.75345400   -0.06844100    0.06428200
""",
)

entry(
    index = 8,
    label = "[O]C1OO1",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {4,S}
3 O u1 p2 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93632,0.00523728,2.95862e-05,-5.9734e-08,3.43164e-11,-10291.8,8.67808], Tmin=(10,'K'), Tmax=(582.122,'K')),
            NASAPolynomial(coeffs=[3.53284,0.0141503,-9.20351e-06,2.81019e-09,-3.26242e-13,-10348.9,9.51273], Tmin=(582.122,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-85.5835,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-O': 3, 'O-O': 1, 'C-H': 1}

External symmetry: 1, optical isomers: 1

Geometry:
O       1.46439500   -0.59205100    0.49694800
C       0.52222200   -0.00147300    0.10219500
O      -0.75496200   -0.63074200    0.07987000
O      -1.66656300    0.20632300   -0.39733900
H       0.43413300    1.02117600   -0.28168700
""",
)

entry(
    index = 9,
    label = "O[CH]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {3,S} {6,S}
3 C u1 p0 c0 {1,S} {2,S} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93294,0.00398729,5.80929e-05,-1.24559e-07,7.73948e-11,-23332.1,8.04999], Tmin=(10,'K'), Tmax=(565.246,'K')),
            NASAPolynomial(coeffs=[4.70854,0.0139186,-9.18191e-06,3.04904e-09,-3.89996e-13,-23666.1,2.5716], Tmin=(565.246,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-194.02,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 2, 'C-O': 2, 'C-H': 1}
1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [4, 1, 2, 3], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [2, 3], dihedral: [1, 2, 3, 6], rotor symmetry: 1, max scan energy: 16.17 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -1.26385900    0.10555800    0.39811000
C      -0.00644600    0.35447800   -0.11540000
O       0.53122600    1.49114500    0.39520100
H      -1.67487300   -0.58879300   -0.12800600
H       0.70490700   -0.46880000   -0.10152200
H      -0.17687700    2.14325200    0.47561800
""",
)

entry(
    index = 10,
    label = "CH2O3[20]",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {1,S} {6,S}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94605,0.00299625,6.16257e-05,-1.13518e-07,6.16657e-11,-75640.7,6.85646], Tmin=(10,'K'), Tmax=(617.147,'K')),
            NASAPolynomial(coeffs=[3.10828,0.0217263,-1.62249e-05,5.50008e-09,-6.9305e-13,-75790.5,8.44184], Tmin=(617.147,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-628.937,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (124.717,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'H-O': 2, 'C-O': 2}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 5], rotor symmetry: 1, max scan energy: 44.00 kJ/mol
pivots: [2, 4], dihedral: [1, 2, 4, 6], rotor symmetry: 1, max scan energy: 44.00 kJ/mol


External symmetry: 2, optical isomers: 1

Geometry:
O       0.62733600    1.44401200    0.23764000
C       0.03063800    0.40692200    0.10049800
O      -1.27020700    0.21576800    0.34845400
O       0.55768300   -0.74682700   -0.32530500
H      -1.61600800    1.06611200    0.65249700
H       1.49362800   -0.57146800   -0.49371100
""",
)

entry(
    index = 11,
    label = "C2H4O3[183]",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {4,S} {9,S}
3 O u0 p2 c0 {5,D}
4 C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
5 C u0 p0 c0 {1,S} {3,D} {8,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92374,0.0044405,9.92695e-05,-1.8914e-07,1.08907e-10,-67674.2,10.2514], Tmin=(10,'K'), Tmax=(569.557,'K')),
            NASAPolynomial(coeffs=[2.28908,0.0333374,-2.27034e-05,7.31907e-09,-8.93064e-13,-67770.5,14.7376], Tmin=(569.557,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-562.707,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'H-O': 1, 'C-H': 3, 'C-O': 3}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [4, 5], dihedral: [3, 4, 5, 9], rotor symmetry: 1, max scan energy: 25.04 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.84273600    0.80564200    0.59027800
C       1.58279400   -0.19083500   -0.03942700
O       0.35680200   -0.59234100   -0.38294400
C      -0.70769300    0.30827600    0.03350700
O      -0.84723000    0.36286600    1.40437300
H       2.32859700   -0.90161300   -0.40996300
H      -0.49407200    1.28248400   -0.40747200
H      -1.60610300   -0.13109000   -0.38428600
H      -0.10633500    0.87990500    1.74773400
""",
)

entry(
    index = 12,
    label = "CH2O4[194]",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {5,D}
2 O u0 p2 c0 {1,S} {4,S}
3 O u0 p2 c0 {1,S} {6,S}
4 O u0 p2 c0 {2,S} {7,S}
5 O u0 p2 c0 {1,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85404,0.00959427,0.00010179,-2.6977e-07,1.99028e-10,-63896.8,9.16176], Tmin=(10,'K'), Tmax=(490.885,'K')),
            NASAPolynomial(coeffs=[6.17327,0.0190312,-1.36304e-05,4.57166e-09,-5.76383e-13,-64465.9,-3.85431], Tmin=(490.885,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-531.3,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (149.66,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C=O': 1, 'O-O': 1, 'H-O': 2, 'C-O': 2}
1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 6], rotor symmetry: 1, max scan energy: 36.90 kJ/mol
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 5], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.
pivots: [4, 5], dihedral: [2, 4, 5, 7], rotor symmetry: 1, max scan energy: 13.84 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       0.22532000    1.14212400    0.42977700
C       0.37536100    0.04990500   -0.06283500
O       1.46072100   -0.71698300   -0.00378500
O      -0.55376500   -0.60152400   -0.77752500
O      -1.74840600    0.19689500   -0.86571800
H       2.11929900   -0.23249300    0.51434800
H      -1.47982300    0.99058700   -0.35171900
""",
)

entry(
    index = 13,
    label = "[O]C[[O]]O[222]",
    molecule = 
"""
multiplicity 3
1 O u0 p2 c0 {4,S} {6,S}
2 O u1 p2 c0 {4,S}
3 O u1 p2 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94547,0.00319543,6.16641e-05,-1.21967e-07,7.1897e-11,-10258.9,9.8819], Tmin=(10,'K'), Tmax=(569.247,'K')),
            NASAPolynomial(coeffs=[3.47466,0.0190356,-1.3098e-05,4.26377e-09,-5.25052e-13,-10408.4,10.1046], Tmin=(569.247,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-85.3198,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'H-O': 1, 'C-H': 1, 'C-O': 3}
1D rotors:
* Invalidated! pivots: [2, 4], dihedral: [1, 2, 4, 6], invalidation reason: Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.Significant difference observed between consecutive conformers But unable to propose troubleshooting methods.


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.83633100    1.32959800    0.30960400
C      -0.34906800    0.05785900    0.24481300
O      -0.44550300   -0.31103400   -1.07739600
O       0.92882600   -0.14457400    0.73046000
H      -1.03690100   -0.49735300    0.91296400
H       1.54993300    0.25726300    0.10679800
""",
)

entry(
    index = 14,
    label = "OC1OO1[239]",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {1,S} {2,S}
4 O u0 p2 c0 {1,S} {6,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0955,-0.00811778,0.000106168,-1.74792e-07,8.97178e-11,-28933.5,8.10056], Tmin=(10,'K'), Tmax=(650.132,'K')),
            NASAPolynomial(coeffs=[3.05265,0.0215236,-1.58069e-05,5.23388e-09,-6.38612e-13,-29288.7,8.90783], Tmin=(650.132,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-240.572,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'O-O': 1, 'H-O': 1, 'C-H': 1, 'C-O': 3}
1D rotors:
pivots: [1, 2], dihedral: [5, 1, 2, 3], rotor symmetry: 1, max scan energy: 26.02 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       1.08900000    0.44632000   -0.00610100
C      -0.24765200    0.26502000    0.00223000
O      -0.78833000   -0.75358100    0.76819600
O      -0.79834000   -0.75006600   -0.76126700
H       1.50999700   -0.42577800   -0.01086200
H      -0.76467500    1.21808600    0.00780500
""",
)

entry(
    index = 15,
    label = "[O]O[C]1OO1[268]",
    molecule = 
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {5,S}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {4,S} {5,S}
4 O u1 p2 c0 {3,S}
5 C u1 p0 c0 {1,S} {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86872,0.014298,7.12427e-06,-2.99464e-08,1.7165e-11,65677.5,10.8387], Tmin=(10,'K'), Tmax=(728.917,'K')),
            NASAPolynomial(coeffs=[6.04348,0.0121154,-8.45172e-06,2.653e-09,-3.10647e-13,65101.3,-0.742717], Tmin=(728.917,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (546.066,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'O-O': 2, 'C-O': 3}
1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: Another conformer for [O]O[C]1OO1[268] exists which is 1.60 kJ/mol lower.Another conformer for [O]O[C]1OO1[268] exists which is 1.60 kJ/mol lower.


External symmetry: 1, optical isomers: 1

Geometry:
O       2.00068600    0.09623500   -0.03518900
O       0.83328800   -0.15390900    0.54986400
C      -0.23828500    0.10068600   -0.31905500
O      -1.26708100   -0.75989700   -0.35214800
O      -1.32875700    0.72020600    0.15758300
""",
)

entry(
    index = 16,
    label = "OC1[O]OO1[283]",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {1,S} {2,S}
4 O u0 p2 c0 {1,S} {6,S}
5 O u0 p2 c0 {1,S} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84606,0.00998608,0.000101388,-2.68274e-07,1.95365e-10,-54677.9,8.26505], Tmin=(10,'K'), Tmax=(502.184,'K')),
            NASAPolynomial(coeffs=[6.68619,0.0178346,-1.30697e-05,4.49808e-09,-5.77985e-13,-55347.3,-7.30618], Tmin=(502.184,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-454.655,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (149.66,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'O-O': 1, 'H-O': 2, 'C-O': 4}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 3], rotor symmetry: 1, max scan energy: 16.88 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 7], rotor symmetry: 1, max scan energy: 16.87 kJ/mol


External symmetry: 2, optical isomers: 1

Geometry:
O       1.36902900   -0.00830400   -0.20727200
C       0.04188400    0.12816000   -0.03901400
O      -0.29380500    1.40144000   -0.31163000
O      -0.80012800   -0.89573400   -0.45391600
O      -0.57405800   -0.51965800    1.02420500
H       1.59526700   -0.92582400   -0.00843100
H      -1.24779400    1.48451300   -0.18685900
""",
)

entry(
    index = 17,
    label = "O1OC12OO2[297]",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {4,S} {5,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94698,0.00292556,5.4325e-05,-1.01803e-07,5.5408e-11,-1582.16,7.12897], Tmin=(10,'K'), Tmax=(626.885,'K')),
            NASAPolynomial(coeffs=[3.60176,0.018385,-1.43864e-05,5.00229e-09,-6.38218e-13,-1799.36,6.55567], Tmin=(626.885,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-13.1793,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'O-O': 2, 'C-O': 4}

External symmetry: 4, optical isomers: 1

Geometry:
O       1.09233900   -0.57132100    0.52937300
O       1.08036900    0.58654100   -0.53723300
C       0.00000000    0.00000000    0.00000000
O      -1.08471200   -0.54091800   -0.57502500
O      -1.08799500    0.52569800    0.58288500
""",
)

