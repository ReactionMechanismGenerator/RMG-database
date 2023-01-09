#!/usr/bin/env python
# encoding: utf-8

name = "MyNH3species"
shortDesc = ""
longDesc = """
ARC v1.1.0
ARC project ra1020

Levels of theory used:

Conformers:       wb97xd/def2svp, software: gaussian (dft)
TS guesses:       wb97xd/def2svp, software: gaussian (dft)
Composite method: cbs-qb3, software: gaussian (composite) (using a fine grid)
Frequencies:      b3lyp/cbsb7, software: gaussian (dft)
Rotor scans:      b3lyp/cbsb7, software: gaussian (dft)
Using p-type bond additivity corrections for thermo

Using the following ESS settings: {'gaussian': ['local'], 'orca': ['local'], 'molpro': ['local']}

Considered the following species and TSs:
Species NO2 (run time: 0:01:07)
Species O (run time: 0:00:19)
Species NO (run time: 0:01:00)
TS TS0 (Failed!) (run time: None)
Considered reaction: NO2 <=> O + NO

Overall time since project initiation: 00:01:45
"""
entry(
    index = 0,
    label = "cNO2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {3,S}
3 N u1 p1 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04346,-0.00365568,3.58377e-05,-5.91447e-08,3.09852e-11,40486.2,6.27989], Tmin=(10,'K'), Tmax=(629.849,'K')),
            NASAPolynomial(coeffs=[3.60537,0.00621864,-4.56826e-06,1.50057e-09,-1.82076e-13,40400.7,7.07417], Tmin=(629.849,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (336.621,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'O-O': 1, 'N-O': 2}

External symmetry: 2, optical isomers: 1

Geometry:
O      -0.47018000   -0.69173300   -0.00000000
O      -0.28774500    0.78534500   -0.00000000
N       0.75792500   -0.09361200   -0.00000000
""",
)

