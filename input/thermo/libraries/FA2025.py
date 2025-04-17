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
