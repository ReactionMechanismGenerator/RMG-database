#!/usr/bin/env python
# encoding: utf-8

name = "C1_C3_hydrofluorocarbons_NIST"
shortDesc = "/work/westgroup/Importer/RMG-models/C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt"
longDesc = """
b'Obtained by email from Linteris and Burgess on 3/10/23. \nNo changes made to the model. \n\n'
"""
entry(
    index = 0,
    label = "H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.34433,0.00798052,-1.94782e-05,2.01572e-08,-7.37612e-12,-917.935,0.68301], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.33728,-4.94025e-05,4.99457e-07,-1.79566e-10,2.00255e-14,-950.159,-3.20502], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-8.65194,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """TPIS78""",
    longDesc = 
"""
TPIS78.
[H][H]
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 1,
    label = "H",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,7.05333e-13,-1.99592e-15,2.30082e-18,-9.27732e-22,25473.7,-0.446683], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,-2.30843e-11,1.61562e-14,-4.73515e-18,4.98197e-22,25473.7,-0.446683], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (211.8,'kJ/mol'),
        Cp0 = (20.7862,'J/mol/K'),
        CpInf = (20.7862,'J/mol/K'),
    ),
    shortDesc = """L 7/88""",
    longDesc = 
"""
L 7/88.
[H]
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 2,
    label = "O2",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78246,-0.00299673,9.8473e-06,-9.6813e-09,3.24373e-12,-1063.94,3.65768], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.28254,0.00148309,-7.57967e-07,2.09471e-10,-2.16718e-14,-1088.46,5.45323], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-8.63696,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """TPIS89""",
    longDesc = 
"""
TPIS89.
[O][O]
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 3,
    label = "OH",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99202,-0.00240132,4.61794e-06,-3.88113e-09,1.36411e-12,3615.08,-0.103925], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.09289,0.00054843,1.26505e-07,-8.79462e-11,1.17412e-14,3858.66,4.4767], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (30.4447,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """RUS 78""",
    longDesc = 
"""
RUS 78.
[OH]
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 4,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.19864,-0.00203643,6.5204e-06,-5.48797e-09,1.77198e-12,-30293.7,-0.849032], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.03399,0.00217692,-1.64073e-07,-9.7042e-11,1.68201e-14,-30004.3,4.96677], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-251.755,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """L 8/89""",
    longDesc = 
"""
L 8/89.
O
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 5,
    label = "HO2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.3018,-0.00474912,2.11583e-05,-2.42764e-08,9.29225e-12,294.808,3.71666], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.01721,0.00223982,-6.33658e-07,1.14246e-10,-1.07909e-14,111.857,3.7851], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (2.67719,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """L 5/89""",
    longDesc = 
"""
L 5/89.
[O]O
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 6,
    label = "CH2CFCF3",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u0 p0 c0 {4,S} {5,S} {7,D}
7 C u0 p0 c0 {6,D} {8,S} {9,S}
8 H u0 p0 c0 {7,S}
9 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.00153,0.0498008,-4.61878e-05,1.64792e-08,-3.13156e-13,-99948.7,20.7747], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.311,0.00944785,-3.52268e-06,5.79392e-10,-3.50621e-14,-103384,-46.913], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-832.404,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (203.705,'J/mol/K'),
    ),
    shortDesc = """2,3,3,3-T 1/10""",
    longDesc = 
"""
2,3,3,3-T 1/10.
C=C(F)C(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 7,
    label = "CH3F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.03514,-0.0146119,6.06479e-05,-6.6065e-08,2.42867e-11,-29597.3,0.30807], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.31348,0.00859183,-3.07886e-06,4.9607e-10,-2.96515e-14,-30012.3,4.75257], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-245.47,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """FC-41 -236  T05/11""",
    longDesc = 
"""
FC-41 -236  T05/11
************************
*** C1 Fluorocarbons ***
************************.
CF
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 8,
    label = "CH2F2",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.25023,-0.00684861,4.85583e-05,-5.83443e-08,2.24504e-11,-55607.3,5.76716], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.06948,0.00723193,-2.64021e-06,4.30855e-10,-2.59873e-14,-56599.2,-2.3459], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-462.171,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """FC-32     T 9/99""",
    longDesc = 
"""
FC-32     T 9/99.
FCF
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 9,
    label = "CHF3",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.73539,0.00872479,1.74822e-05,-3.21505e-08,1.41695e-11,-85182.1,12.488], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.24609,0.00542386,-2.02314e-06,3.34946e-10,-2.04068e-14,-86823.9,-12.8982], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-709.678,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """FLUOROFORM  T 9/99""",
    longDesc = 
"""
FLUOROFORM  T 9/99.
FC(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 10,
    label = "HF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48137,0.000212246,-6.86359e-07,8.56186e-10,-2.34582e-13,-33860.7,1.0258], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.92491,0.000850523,-1.5818e-07,1.17507e-11,-1.43309e-16,-33635.2,4.19019], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-281.551,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """T 2/11""",
    longDesc = 
"""
T 2/11.
F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 11,
    label = "CF2O",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 O u0 p2 c0 {4,D}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.12979,0.014102,-5.94383e-06,-5.30542e-09,3.97366e-12,-74163.7,15.1109], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.81632,0.00316473,-1.21776e-06,2.05582e-10,-1.26893e-14,-75537.5,-9.52865], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-618.401,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """T 5/11""",
    longDesc = 
"""
T 5/11.
O=C(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 12,
    label = "CF4",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {5,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.0512,0.0278318,-2.46683e-05,6.75883e-09,9.14851e-13,-113574,18.1937], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.47337,0.00359408,-1.40334e-06,2.39114e-10,-1.48513e-14,-115817,-24.9737], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-945.719,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """FC-14      g 7/99""",
    longDesc = 
"""
FC-14      g 7/99.
FC(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 13,
    label = "CH3-CHF2",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.25213,0.0118718,2.57924e-05,-4.29489e-08,1.82238e-11,-62276.8,11.1052], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.67996,0.0122243,-4.37574e-06,7.04756e-10,-4.21224e-14,-64085.1,-14.7344], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-518.265,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """HFC-152aT 6/11""",
    longDesc = 
"""
HFC-152aT 6/11.
CC(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 14,
    label = "CH2F-CF3",
    molecule = 
"""
1 F u0 p3 c0 {6,S}
2 F u0 p3 c0 {6,S}
3 F u0 p3 c0 {6,S}
4 F u0 p3 c0 {5,S}
5 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6 C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.2924,0.0303108,-5.33714e-06,-2.19457e-08,1.2997e-11,-111354,16.2831], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.5551,0.00840186,-3.12077e-06,5.12285e-10,-3.1011e-14,-114410,-38.0374], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-926.575,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """T 5/03""",
    longDesc = 
"""
T 5/03.
FCC(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 15,
    label = "C3F7H",
    molecule = 
"""
1  F u0 p3 c0 {8,S}
2  F u0 p3 c0 {8,S}
3  F u0 p3 c0 {10,S}
4  F u0 p3 c0 {10,S}
5  F u0 p3 c0 {10,S}
6  F u0 p3 c0 {9,S}
7  F u0 p3 c0 {9,S}
8  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
9  C u0 p0 c0 {6,S} {7,S} {8,S} {11,S}
10 C u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
11 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.19382,0.0564358,-4.24436e-05,6.01423e-09,4.21731e-12,-191303,14.797], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[20.3196,0.0104619,-3.99352e-06,6.70977e-10,-4.12887e-14,-196070,-73.9088], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-1589.46,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (249.434,'J/mol/K'),
    ),
    shortDesc = """FC227EA    T12/99""",
    longDesc = 
"""
FC227EA    T12/99
****************
***C3-fluorinated,etc***
************************.
FC(F)C(F)(F)C(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 16,
    label = "O",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16827,-0.00327932,6.64306e-06,-6.12807e-09,2.11266e-12,29122.3,2.05193], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.56942,-8.59741e-05,4.19485e-08,-1.00178e-11,1.22834e-15,29217.6,4.78434], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (242.976,'kJ/mol'),
        Cp0 = (20.7862,'J/mol/K'),
        CpInf = (20.7862,'J/mol/K'),
    ),
    shortDesc = """L 1/90""",
    longDesc = 
"""
L 1/90
GRI-Mech Version 3.0 Thermodynamics released 7/30/99
NASA Polynomial format for CHEMKIN-II
see README file for disclaimer.
[O]
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 17,
    label = "H2O2",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.27611,-0.000542822,1.67336e-05,-2.15771e-08,8.62454e-12,-17702.6,3.43505], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.165,0.00490832,-1.90139e-06,3.71186e-10,-2.87908e-14,-17861.8,2.91616], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-146.921,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (78.9875,'J/mol/K'),
    ),
    shortDesc = """L 7/88""",
    longDesc = 
"""
L 7/88.
OO
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 18,
    label = "C",
    molecule = 
"""
1 C u0 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.55424,-0.000321538,7.33792e-07,-7.32235e-10,2.66521e-13,85443.9,4.53131], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.49267,4.79889e-05,-7.24335e-08,3.74291e-11,-4.87278e-15,85451.3,4.8015], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (710.479,'kJ/mol'),
        Cp0 = (20.7862,'J/mol/K'),
        CpInf = (20.7862,'J/mol/K'),
    ),
    shortDesc = """L11/88""",
    longDesc = 
"""
L11/88.
[C]
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 19,
    label = "CH",
    molecule = 
"""
multiplicity 2
1 C u1 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48982,0.000323836,-1.68899e-06,3.16217e-09,-1.40609e-12,70797.3,2.08401], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.87846,0.000970914,1.44446e-07,-1.30688e-10,1.76079e-14,71012.4,5.48498], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (588.632,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """TPIS79""",
    longDesc = 
"""
TPIS79.
[CH]
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 20,
    label = "CH3",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67359,0.00201095,5.73022e-06,-6.87117e-09,2.54386e-12,16445,1.60456], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.28572,0.0072399,-2.98714e-06,5.95685e-10,-4.67154e-14,16775.6,8.48007], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (136.42,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """L11/89""",
    longDesc = 
"""
L11/89.
[CH3]
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 21,
    label = "CH4",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.14988,-0.013671,4.91801e-05,-4.84743e-08,1.66694e-11,-10246.6,-4.6413], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.0748515,0.0133909,-5.73286e-06,1.22293e-09,-1.01815e-13,-9468.34,18.4373], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-84.4922,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """L 8/88""",
    longDesc = 
"""
L 8/88.
C
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 22,
    label = "CO",
    molecule = 
"""
1 O u0 p1 c+1 {2,T}
2 C u0 p1 c-1 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57953,-0.000610354,1.01681e-06,9.07006e-10,-9.04424e-13,-14344.1,3.50841], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.71519,0.00206253,-9.98826e-07,2.30053e-10,-2.03648e-14,-14151.9,7.81869], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-119.169,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """TPIS79""",
    longDesc = 
"""
TPIS79.
[C-]#[O+]
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 23,
    label = "CO2",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.35677,0.0089846,-7.12356e-06,2.45919e-09,-1.437e-13,-48372,9.90105], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.85746,0.00441437,-2.21481e-06,5.2349e-10,-4.72084e-14,-48759.2,2.27164], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-402.81,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (62.3585,'J/mol/K'),
    ),
    shortDesc = """L 7/88""",
    longDesc = 
"""
L 7/88.
O=C=O
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 24,
    label = "CH3OH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.7154,-0.0152309,6.52441e-05,-7.10807e-08,2.61353e-11,-25642.8,-1.5041], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.78971,0.0140938,-6.36501e-06,1.38171e-09,-1.1706e-13,-25374.9,14.5024], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-211.924,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (128.874,'J/mol/K'),
    ),
    shortDesc = """L 8/88""",
    longDesc = 
"""
L 8/88.
CO
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 25,
    label = "C2H",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {3,S}
2 C u1 p0 c0 {1,T}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.88966,0.01341,-2.8477e-05,2.94791e-08,-1.09332e-11,66839.4,6.22296], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.16781,0.00475222,-1.83787e-06,3.0419e-10,-1.77233e-14,67121.1,6.63589], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (555.472,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (62.3585,'J/mol/K'),
    ),
    shortDesc = """L 1/91""",
    longDesc = 
"""
L 1/91.
[C]#C
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 26,
    label = "C2H4",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9592,-0.00757052,5.7099e-05,-6.91589e-08,2.69884e-11,5089.78,4.09733], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.03611,0.0146454,-6.71078e-06,1.47223e-09,-1.25706e-13,4939.89,10.3054], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (42.313,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (133.032,'J/mol/K'),
    ),
    shortDesc = """L 1/91""",
    longDesc = 
"""
L 1/91.
C=C
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 27,
    label = "C2H5",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.30647,-0.00418659,4.97143e-05,-5.99127e-08,2.30509e-11,12841.6,4.70721], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.95466,0.0173973,-7.98207e-06,1.75218e-09,-1.49642e-13,12857.5,13.4624], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (106.955,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """L12/92""",
    longDesc = 
"""
L12/92.
C[CH2]
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 28,
    label = "C2H6",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.29142,-0.00550154,5.99438e-05,-7.08466e-08,2.68686e-11,-11522.2,2.66682], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.07188,0.0216853,-1.00256e-05,2.21412e-09,-1.90003e-13,-11426.4,15.1156], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-95.6539,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """L 8/88""",
    longDesc = 
"""
L 8/88.
CC
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 29,
    label = "AR",
    molecule = 
"""
1 Ar u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.366], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.366], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-6.19738,'kJ/mol'),
        Cp0 = (20.7862,'J/mol/K'),
        CpInf = (20.7862,'J/mol/K'),
    ),
    shortDesc = """120186""",
    longDesc = 
"""
120186
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[Ar]
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 30,
    label = "C3H8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.933554,0.0264246,6.10597e-06,-2.19775e-08,9.51493e-12,-13958.5,19.2017], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.53414,0.0188722,-6.27185e-06,9.14756e-10,-4.78381e-14,-16467.5,-17.8923], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-118.828,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (249.434,'J/mol/K'),
    ),
    shortDesc = """L 4/85""",
    longDesc = 
"""
L 4/85
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 31,
    label = "N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29868,0.00140824,-3.96322e-06,5.64152e-09,-2.44485e-12,-1020.9,3.95037], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.92664,0.00148798,-5.68476e-07,1.0097e-10,-6.75335e-15,-922.798,5.98053], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-8.62479,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """121286""",
    longDesc = 
"""
121286
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
N#N
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 32,
    label = "F",
    molecule = 
"""
multiplicity 2
1 F u1 p3 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.41967,0.00293929,-8.92122e-06,9.91185e-09,-3.79472e-12,8757.32,4.7469], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.67163,-0.000174619,6.90665e-08,-1.19535e-11,7.52367e-16,8787.41,3.98426], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (73.192,'kJ/mol'),
        Cp0 = (20.7862,'J/mol/K'),
        CpInf = (20.7862,'J/mol/K'),
    ),
    shortDesc = """J 6/82""",
    longDesc = 
"""
J 6/82
********************************
*** Hydrogen/Oxygen/Fluorine ***
********************************.
[F]
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 33,
    label = "CH2",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76268,0.000968872,2.7949e-06,-3.85091e-09,1.68742e-12,46004,1.56253], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.8741,0.00365639,-1.40895e-06,2.6018e-10,-1.87728e-14,46263.6,6.17119], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (382.229,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """L S/93""",
    longDesc = 
"""
L S/93.
[CH2]
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 34,
    label = "CH2(S)",
    molecule = 
"""
1 C u0 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.1986,-0.00236661,8.23296e-06,-6.68816e-09,1.94315e-12,50496.8,-0.769119], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.29204,0.00465589,-2.01192e-06,4.17906e-10,-3.39716e-14,50926,8.6265], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (419.976,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """L S/93""",
    longDesc = 
"""
L S/93.
[CH2]
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 35,
    label = "HCCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 C u1 p0 c0 {3,D} {4,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.25172,0.017655,-2.37291e-05,1.72758e-08,-5.06648e-12,20059.4,12.4904], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.62821,0.00408534,-1.59345e-06,2.86261e-10,-1.94078e-14,19327.2,-3.93026], Tmin=(1000,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (4000,'K'),
        E0 = (165.461,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """SRIC91""",
    longDesc = 
"""
SRIC91
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=C=O
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 36,
    label = "HCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.22119,-0.00324393,1.37799e-05,-1.33144e-08,4.33769e-12,3839.56,3.39437], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.77217,0.00495696,-2.48446e-06,5.89162e-10,-5.33509e-14,4011.92,9.79834], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (32.0523,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """L12/89""",
    longDesc = 
"""
L12/89.
[CH]=O
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 37,
    label = "CH2O",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.79372,-0.00990833,3.7322e-05,-3.79285e-08,1.31773e-11,-14309,0.602813], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.76069,0.0092,-4.42259e-06,1.00641e-09,-8.83856e-14,-13995.8,13.6563], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-118.464,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """L 8/88""",
    longDesc = 
"""
L 8/88.
C=O
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 38,
    label = "C2H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u1 p0 c0 {1,D} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.21247,0.00151479,2.59209e-05,-3.57658e-08,1.47151e-11,34859.8,8.51054], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.01672,0.0103302,-4.68082e-06,1.01763e-09,-8.62607e-14,34612.9,7.78732], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (289.567,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """L 2/92""",
    longDesc = 
"""
L 2/92.
[CH]=C
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 39,
    label = "CHF2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u1 p0 c0 {1,S} {2,S} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.12221,-0.00233707,2.99283e-05,-3.88423e-08,1.55353e-11,-30599,7.22245], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.52321,0.0042197,-1.58435e-06,2.63969e-10,-1.61338e-14,-31440.5,-2.40335], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-254.255,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """g 6/88""",
    longDesc = 
"""
g 6/88.
F[CH]F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 40,
    label = "CF3",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u1 p0 c0 {1,S} {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.38179,0.013727,-3.47675e-06,-9.01697e-09,5.57384e-12,-57687.1,14.3743], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.42982,0.00261729,-1.02142e-06,1.73976e-10,-1.08028e-14,-59179.6,-12.2817], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-481.087,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """ATcT/A""",
    longDesc = 
"""
ATcT/A.
F[C](F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 41,
    label = "CHF2-CHF2",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {6,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
6 C u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98924,0.0172572,2.36854e-05,-4.89143e-08,2.21226e-11,-108019,9.12365], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.9961,0.00898721,-3.36363e-06,5.54e-10,-3.35655e-14,-110810,-35.3416], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-897.479,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """T 5/03""",
    longDesc = 
"""
T 5/03.
FC(F)C(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 42,
    label = "CF3CHCH2",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 C u0 p0 c0 {4,S} {6,D} {7,S}
6 C u0 p0 c0 {5,D} {8,S} {9,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.56835,0.0370716,-1.66535e-05,-1.1567e-08,9.46282e-12,-77857,19.2579], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.2166,0.0111177,-4.07567e-06,6.63455e-10,-3.9873e-14,-80878,-36.334], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-648.629,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (203.705,'J/mol/K'),
    ),
    shortDesc = """*** C3HFx ***""",
    longDesc = 
"""
*** C3HFx ***.
C=CC(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 43,
    label = "CF3-CF3",
    molecule = 
"""
1 F u0 p3 c0 {7,S}
2 F u0 p3 c0 {7,S}
3 F u0 p3 c0 {7,S}
4 F u0 p3 c0 {8,S}
5 F u0 p3 c0 {8,S}
6 F u0 p3 c0 {8,S}
7 C u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
8 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.56504,0.051091,-5.07168e-05,1.88994e-08,-7.73771e-13,-164148,18.9556], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.0285,0.00464175,-1.92155e-06,3.37539e-10,-2.13452e-14,-168162,-59.8113], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-1365.5,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """T 6/11""",
    longDesc = 
"""
T 6/11.
FC(F)(F)C(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 44,
    label = "CHF2-CF2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {6,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
6 C u1 p0 c0 {3,S} {4,S} {5,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.03038,0.0313636,-2.9519e-05,1.39839e-08,-2.71243e-12,-82031.4,14.0888], Tmin=(298,'K'), Tmax=(1250,'K')),
            NASAPolynomial(coeffs=[11.6275,0.00710202,-3.03218e-06,5.8031e-10,-4.05959e-14,-84517.3,-30.4865], Tmin=(1250,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-682.532,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """95BURZAC91CHE""",
    longDesc = 
"""
95BURZAC91CHE
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[C](F)C(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 45,
    label = "CF3-CHF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u1 p0 c0 {4,S} {5,S} {7,S}
7 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.17776,0.0376992,-4.16073e-05,2.31106e-08,-5.13915e-12,-86121.6,17.2676], Tmin=(298,'K'), Tmax=(1250,'K')),
            NASAPolynomial(coeffs=[11.7531,0.00713118,-3.12251e-06,6.15301e-10,-4.44146e-14,-88644.2,-31.3333], Tmin=(1250,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-716.572,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """95BURZAC91CHE""",
    longDesc = 
"""
95BURZAC91CHE
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[CH]C(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 46,
    label = "C2H2",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.808681,0.0233616,-3.55172e-05,2.80152e-08,-8.50073e-12,26429,13.9397], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.14757,0.00596167,-2.37295e-06,4.67412e-10,-3.61235e-14,25936,-1.23028], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (217.646,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (87.302,'J/mol/K'),
    ),
    shortDesc = """L 1/91""",
    longDesc = 
"""
L 1/91.
C#C
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 47,
    label = "C3H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.05155,0.025992,2.38005e-06,-1.96096e-08,9.37325e-12,10631.9,21.1226], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.7027,0.0160442,-5.28332e-06,7.62986e-10,-3.93923e-14,8298.43,-15.4802], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (85.757,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """L 9/84""",
    longDesc = 
"""
L 9/84
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 48,
    label = "F2",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 F u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.20832,0.00125919,3.89748e-06,-7.22185e-09,3.31838e-12,-1034.26,5.61904], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.86166,0.000788368,-1.81983e-07,-9.17437e-12,2.65193e-15,-1232.39,2.0412], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-9.01653,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """REF ELEMENT   RUS 89""",
    longDesc = 
"""
REF ELEMENT   RUS 89.
FF
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 49,
    label = "CH2CF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.936646,0.023455,-2.60991e-05,1.68334e-08,-4.66583e-12,12014,19.5947], Tmin=(298,'K'), Tmax=(1050,'K')),
            NASAPolynomial(coeffs=[5.93667,0.00654409,-2.37413e-06,3.82235e-10,-2.2536e-14,10745.2,-5.57304], Tmin=(1050,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (97.1583,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """96ZACWES""",
    longDesc = 
"""
96ZACWES
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=[C]F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 50,
    label = "C3F7",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {8,S}
2  F u0 p3 c0 {8,S}
3  F u0 p3 c0 {9,S}
4  F u0 p3 c0 {9,S}
5  F u0 p3 c0 {9,S}
6  F u0 p3 c0 {10,S}
7  F u0 p3 c0 {10,S}
8  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
9  C u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
10 C u1 p0 c0 {6,S} {7,S} {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.14242,0.0603443,-6.17598e-05,2.7938e-08,-4.02551e-12,-165147,16.6898], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[20.5301,0.00760063,-2.96491e-06,5.04882e-10,-3.13453e-14,-169702,-71.9281], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-1371.96,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """CF3CF*CF3 M  T12/99""",
    longDesc = 
"""
CF3CF*CF3 M  T12/99.
F[C](F)C(F)(F)C(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 51,
    label = "CH3O",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.1062,0.0072166,5.33847e-06,-7.37764e-09,2.07561e-12,978.601,13.1522], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.7708,0.0078715,-2.65638e-06,3.94443e-10,-2.11262e-14,127.833,2.92957], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (6.64192,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """121686""",
    longDesc = 
"""
121686
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[O]
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 52,
    label = "CH2OH",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86389,0.00559672,5.93272e-06,-1.04532e-08,4.36967e-12,-3193.91,5.47302], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.69267,0.00864577,-3.75101e-06,7.87235e-10,-6.48554e-14,-3242.51,5.81043], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-26.5115,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (103.931,'J/mol/K'),
    ),
    shortDesc = """GUNL93""",
    longDesc = 
"""
GUNL93.
[CH2]O
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 53,
    label = "CH3-CF2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u1 p0 c0 {1,S} {2,S} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.31422,0.0237018,-1.63892e-05,5.72572e-09,-8.07296e-13,-37472.8,15.3584], Tmin=(298,'K'), Tmax=(1150,'K')),
            NASAPolynomial(coeffs=[6.47721,0.0124876,-5.35782e-06,1.03049e-09,-7.24509e-14,-38679.9,-6.31953], Tmin=(1150,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-312.418,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """78ROD90CHERAU""",
    longDesc = 
"""
78ROD90CHERAU
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[C](F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 54,
    label = "CHF2-CH2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 C u1 p0 c0 {3,S} {6,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.21237,0.0299528,-2.78097e-05,1.45866e-08,-3.35363e-12,-35475.7,21.1127], Tmin=(298,'K'), Tmax=(1100,'K')),
            NASAPolynomial(coeffs=[6.79826,0.0121309,-5.28714e-06,1.03624e-09,-7.40874e-14,-36927,-7.21609], Tmin=(1100,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-296.893,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """90CHERAU""",
    longDesc = 
"""
90CHERAU
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 55,
    label = "CH3CHO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.72946,-0.00319329,4.75349e-05,-5.74586e-08,2.19311e-11,-21572.9,4.10302], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.40411,0.0117231,-4.22631e-06,6.83725e-10,-4.09849e-14,-22593.1,-3.48079], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-178.765,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """L 8/88""",
    longDesc = 
"""
L 8/88.
CC=O
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 56,
    label = "CH3CO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u1 p0 c0 {1,D} {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.16343,-0.000232616,3.42678e-05,-4.41052e-08,1.72756e-11,-2657.45,7.34683], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.94477,0.00786672,-2.88659e-06,4.72709e-10,-2.85999e-14,-3787.31,-5.01368], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-22.0975,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (128.874,'J/mol/K'),
    ),
    shortDesc = """T 9/92""",
    longDesc = 
"""
T 9/92.
C[C]=O
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 57,
    label = "HCCOH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.24237,0.0310722,-5.08669e-05,4.31371e-08,-1.40146e-11,8031.61,13.8743], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.92383,0.00679236,-2.56586e-06,4.49878e-10,-2.99401e-14,7264.63,-7.60177], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (65.1111,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (103.931,'J/mol/K'),
    ),
    shortDesc = """SRI91""",
    longDesc = 
"""
SRI91
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#CO
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 58,
    label = "C3H6",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.49331,0.0209252,4.48679e-06,-1.66891e-08,7.15815e-12,1074.83,16.1453], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.73226,0.0149083,-4.9499e-06,7.21202e-10,-3.7662e-14,-923.57,-13.3133], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (6.62319,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (203.705,'J/mol/K'),
    ),
    shortDesc = """120186""",
    longDesc = 
"""
120186
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 59,
    label = "CH3-CF3",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.75261,0.0304396,-1.49789e-05,-5.70776e-09,5.66225e-12,-92409.2,16.2401], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.0541,0.0102516,-3.70172e-06,5.99864e-10,-3.60117e-14,-94813,-27.2331], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-769.648,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """FC-143A   T11/03""",
    longDesc = 
"""
FC-143A   T11/03.
CC(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 60,
    label = "CH3CCH2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,D} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.73292,0.0223946,-5.14906e-06,-6.75965e-09,3.82532e-12,29040.5,16.5689], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.42555,0.0155111,-5.66784e-06,7.92244e-10,-1.6878e-14,27843,-3.35272], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (239.753,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """PD5/98""",
    longDesc = 
"""
PD5/98
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=[C]C
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 61,
    label = "CH2F-CHF2",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.647376,0.0362925,-3.11432e-05,1.44646e-08,-3.0121e-12,-81941.3,23.2953], Tmin=(298,'K'), Tmax=(1100,'K')),
            NASAPolynomial(coeffs=[9.27265,0.0120402,-4.8606e-06,8.86567e-10,-5.96506e-14,-84398.3,-21.388], Tmin=(1100,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-683.512,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """68LACSKI96ZAC""",
    longDesc = 
"""
68LACSKI96ZAC
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FCC(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 62,
    label = "CHF2-CF3",
    molecule = 
"""
1 F u0 p3 c0 {6,S}
2 F u0 p3 c0 {6,S}
3 F u0 p3 c0 {7,S}
4 F u0 p3 c0 {7,S}
5 F u0 p3 c0 {7,S}
6 C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
7 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.56681,0.0363878,-1.93607e-05,-9.02363e-09,8.52266e-12,-136274,15.6969], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.5281,0.00680985,-2.67133e-06,4.54434e-10,-2.81434e-14,-139669,-46.7174], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-1133.23,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """A 4/05""",
    longDesc = 
"""
A 4/05
CHF2-CF3          A 4/05C  2.H  1.F  5.   0.G   200.000  6000.000 1000.        1 2018GAN/KAL(burcat,2013)
1.45281312E+01 6.80984691E-03-2.67132939E-06 4.54433791E-10-2.81433657E-14    2
-1.39040339E+05-4.67174252E+01 2.56680624E+00 3.63877723E-02-1.93606756E-05    3
-9.02362714E-09 8.52266342E-12-1.36273767E+05 1.56968804E+01-1.34704270E+05    4.
FC(F)C(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 63,
    label = "CH2F-CF2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 C u1 p0 c0 {2,S} {3,S} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.09008,0.0293901,-2.55533e-05,1.17108e-08,-2.31129e-12,-55373.1,17.8136], Tmin=(298,'K'), Tmax=(1150,'K')),
            NASAPolynomial(coeffs=[8.87024,0.0100895,-4.39156e-06,8.57582e-10,-6.11641e-14,-57295.5,-17.249], Tmin=(1150,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-461.245,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """91CHERAU""",
    longDesc = 
"""
91CHERAU
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC[C](F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 64,
    label = "CHF2-CHF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 C u1 p0 c0 {3,S} {4,S} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.81368,0.0327767,-3.24205e-05,1.68313e-08,-3.60024e-12,-56094.6,18.5911], Tmin=(298,'K'), Tmax=(1250,'K')),
            NASAPolynomial(coeffs=[9.42456,0.00938455,-4.0695e-06,7.95489e-10,-5.68744e-14,-58166,-20.3132], Tmin=(1250,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-467.484,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """91CHERAU""",
    longDesc = 
"""
91CHERAU
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[CH]C(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 65,
    label = "CF3-CH2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 C u1 p0 c0 {4,S} {6,S} {7,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.717008,0.0405315,-4.78641e-05,2.94408e-08,-7.31258e-12,-65142.1,22.1032], Tmin=(298,'K'), Tmax=(1150,'K')),
            NASAPolynomial(coeffs=[9.58796,0.00929988,-4.07747e-06,8.05717e-10,-5.81855e-14,-67287.3,-22.1077], Tmin=(1150,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-543.696,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """78ROD90CHERAU""",
    longDesc = 
"""
78ROD90CHERAU
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 66,
    label = "CF3-CF2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {6,S}
2 F u0 p3 c0 {6,S}
3 F u0 p3 c0 {6,S}
4 F u0 p3 c0 {7,S}
5 F u0 p3 c0 {7,S}
6 C u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
7 C u1 p0 c0 {4,S} {5,S} {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.35962,0.040676,-3.97029e-05,1.42584e-08,-3.10091e-13,-110282,17.0749], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.5576,0.00416794,-1.72789e-06,3.02375e-10,-1.90424e-14,-113453,-45.0857], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-917.208,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """T03/10""",
    longDesc = 
"""
T03/10.
F[C](F)C(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 67,
    label = "CHFCO",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {4,D}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.96237,0.0225075,-2.56389e-05,1.67917e-08,-4.73482e-12,-19104,15.6743], Tmin=(298,'K'), Tmax=(1050,'K')),
            NASAPolynomial(coeffs=[6.77764,0.00623359,-2.55958e-06,4.75314e-10,-3.25951e-14,-20336.9,-8.59113], Tmin=(1050,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-160.19,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """96ZACWES""",
    longDesc = 
"""
96ZACWES
*********************
*** Fluoroketenes ***
*********************
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=C=CF
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 68,
    label = "CF2CO",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 O u0 p2 c0 {5,D}
4 C u0 p0 c0 {1,S} {2,S} {5,D}
5 C u0 p0 c0 {3,D} {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40543,0.0226943,-2.80353e-05,1.91247e-08,-5.5122e-12,-36737.3,9.64872], Tmin=(298,'K'), Tmax=(1050,'K')),
            NASAPolynomial(coeffs=[8.86841,0.00426277,-1.73813e-06,3.12287e-10,-2.04266e-14,-38145.6,-17.9075], Tmin=(1050,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-305.506,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """96ZACWES""",
    longDesc = 
"""
96ZACWES
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=C=C(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 69,
    label = "CFCO",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {4,D}
3 C u1 p0 c0 {1,S} {4,D}
4 C u0 p0 c0 {2,D} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75942,0.014232,-1.60103e-05,9.88857e-09,-2.66132e-12,6674.73,8.18592], Tmin=(298,'K'), Tmax=(1050,'K')),
            NASAPolynomial(coeffs=[7.30331,0.00297939,-1.30582e-06,2.54074e-10,-1.81035e-14,5735.56,-9.84341], Tmin=(1050,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (55.396,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """96ZACWES""",
    longDesc = 
"""
96ZACWES
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=C=[C]F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 70,
    label = "CF3COF",
    molecule = 
"""
1 F u0 p3 c0 {6,S}
2 F u0 p3 c0 {6,S}
3 F u0 p3 c0 {6,S}
4 F u0 p3 c0 {7,S}
5 O u0 p2 c0 {7,D}
6 C u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
7 C u0 p0 c0 {4,S} {5,D} {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.76997,0.0424508,-5.06967e-05,3.11138e-08,-7.89598e-12,-125712,20.183], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.0627,0.0121434,-7.26341e-06,2.01144e-09,-2.11896e-13,-127590,-20.7307], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-1044.19,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """hynes""",
    longDesc = 
"""
hynes
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=C(F)C(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 71,
    label = "CF3CO",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 O u0 p2 c0 {6,D}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u1 p0 c0 {4,D} {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.05844,0.104164,-0.000237752,2.50068e-07,-9.59472e-11,-73284.3,49.502], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.27366,0.00945656,-5.54495e-06,1.5095e-09,-1.56671e-13,-75683.5,-18.8993], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-616.142,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (128.874,'J/mol/K'),
    ),
    shortDesc = """NIST""",
    longDesc = 
"""
NIST
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=[C]C(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 72,
    label = "CF3CHO",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 O u0 p2 c0 {6,D}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u0 p0 c0 {4,D} {5,S} {7,S}
7 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.9864,0.028195,-2.0916e-05,5.04802e-09,6.02563e-13,-95261.9,13.7466], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.04771,0.013775,-7.75122e-06,2.0531e-09,-2.09098e-13,-96590.4,-12.1768], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-790.736,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """NIST""",
    longDesc = 
"""
NIST
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=CC(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 73,
    label = "CF3CCH2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
5 C u0 p0 c0 {6,D} {7,S} {8,S}
6 C u1 p0 c0 {4,S} {5,D}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.34294,0.0437082,-4.41291e-05,1.98066e-08,-2.52758e-12,-47085.9,20.2494], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.586,0.00812318,-2.95983e-06,4.80632e-10,-2.89086e-14,-49927.8,-36.5972], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-392.724,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
C=[C]C(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 74,
    label = "CF3CCH",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 C u0 p0 c0 {4,S} {6,T}
6 C u0 p0 c0 {5,T} {7,S}
7 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.281616,0.052517,-7.44406e-05,5.3525e-08,-1.53176e-11,-53396.6,23.4333], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.0876,0.00673608,-2.69301e-06,4.89992e-10,-3.33727e-14,-56020.5,-34.348], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-446.183,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#CC(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 75,
    label = "CH2CO",
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
            NASAPolynomial(coeffs=[2.13584,0.0181189,-1.73947e-05,9.34398e-09,-2.01458e-12,-7042.92,12.2156], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.5113,0.0090036,-4.1694e-06,9.23346e-10,-7.94838e-14,-7551.05,0.632247], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-59.9051,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """L 5/90""",
    longDesc = 
"""
L 5/90.
C=C=O
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 76,
    label = "CH2CHO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 C u1 p0 c0 {3,S} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40906,0.0107386,1.89149e-06,-7.15858e-09,2.86738e-12,1521.48,9.55829], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.97567,0.00813059,-2.74362e-06,4.0703e-10,-2.17602e-14,490.322,-5.04525], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (12.5013,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (128.874,'J/mol/K'),
    ),
    shortDesc = """SAND86""",
    longDesc = 
"""
SAND86
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C=O
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 77,
    label = "CFCCF3",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {7,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u0 p0 c0 {5,S} {7,T}
7 C u0 p0 c0 {4,S} {6,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.66217,0.0504259,-7.06033e-05,4.9667e-08,-1.39443e-11,-66089.2,18.0213], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.8905,0.00504275,-2.01504e-06,3.33703e-10,-1.85456e-14,-68934.9,-42.3902], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-550.221,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC#CC(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 78,
    label = "CF3COCH3",
    molecule = 
"""
1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {6,S}
3  F u0 p3 c0 {6,S}
4  O u0 p2 c0 {7,D}
5  C u0 p0 c0 {7,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
7  C u0 p0 c0 {4,D} {5,S} {6,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.31184,0.0462932,-3.86726e-05,1.4578e-08,-1.48757e-12,-103128,17.5782], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.7707,0.0139114,-5.56646e-06,1.01277e-09,-6.89535e-14,-106312,-41.5671], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-857.388,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """*** C2HOFx ***""",
    longDesc = 
"""
*** C2HOFx ***
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)C(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 79,
    label = "CHFCF2",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {1,S} {5,D} {6,S}
5 C u0 p0 c0 {2,S} {3,S} {4,D}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.00354,0.0274141,-2.30032e-05,7.09389e-09,1.96149e-13,-60300,16.5697], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.56304,0.00603922,-2.24656e-06,3.71317e-10,-2.25981e-14,-62366.6,-22.3574], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-502.477,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (133.032,'J/mol/K'),
    ),
    shortDesc = """T 6/11""",
    longDesc = 
"""
T 6/11.
FC=C(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 80,
    label = "CF2CF2",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {6,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {2,S} {6,D}
6 C u0 p0 c0 {3,S} {4,S} {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.99309,0.0384734,-5.32323e-05,3.92123e-08,-1.19303e-11,-83002.1,15.3134], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.4178,0.00459161,-1.77521e-06,3.00599e-10,-1.85921e-14,-85292.8,-31.6446], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-690.904,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (133.032,'J/mol/K'),
    ),
    shortDesc = """ATcT/A""",
    longDesc = 
"""
ATcT/A.
FC(F)=C(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 81,
    label = "CH2F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78124,-0.00044984,1.88358e-05,-2.40703e-08,9.53478e-12,-4885.01,5.56895], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.11284,0.00500104,-1.74096e-06,2.75008e-10,-1.621e-14,-5259.25,2.38853], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-40.8767,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """T 8/09""",
    longDesc = 
"""
T 8/09.
[CH2]F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 82,
    label = "CFO",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {3,D}
3 C u1 p0 c0 {1,S} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37992,0.00419051,2.12354e-06,-6.20587e-09,2.85352e-12,-22406.3,9.39467], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.01566,0.00195763,-7.49685e-07,1.2561e-10,-7.59885e-15,-22978.5,0.369669], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-186.746,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """(CFO/COF)    T 9/11""",
    longDesc = 
"""
(CFO/COF)    T 9/11.
O=[C]F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 83,
    label = "CH-CFCF3",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u0 p0 c0 {4,S} {5,S} {7,D}
7 C u1 p0 c0 {6,D} {8,S}
8 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.499663,0.0571202,-7.49546e-05,4.83898e-08,-1.22362e-11,-70396.9,23.0298], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.3232,0.00655667,-2.43588e-06,3.98836e-10,-2.40439e-14,-73556.3,-45.2117], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-586.972,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
[CH]=C(F)C(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 84,
    label = "CH2CF2",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {4,D} {5,S} {6,S}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.28302,0.0231904,-9.70095e-06,-4.40974e-09,3.38826e-12,-43542.4,18.2379], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.9519,0.00714641,-2.79505e-06,4.77439e-10,-2.97191e-14,-46029.5,-22.9204], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-364.356,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (133.032,'J/mol/K'),
    ),
    shortDesc = """FC-1132A  T 6/11""",
    longDesc = 
"""
FC-1132A  T 6/11.
C=C(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 85,
    label = "CHFO",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74246,-0.00131011,2.46793e-05,-3.12954e-08,1.22625e-11,-47227,7.8972], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.78813,0.0047665,-1.74367e-06,2.84956e-10,-1.72051e-14,-47942.4,0.351967], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-392.858,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """T07/11""",
    longDesc = 
"""
T07/11
*********************************
*** Oxidized C1 Fluorocarbons ***
*********************************.
O=CF
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 86,
    label = "CF2",
    molecule = 
"""
multiplicity 3
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u2 p0 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56435,0.00123021,1.3991e-05,-2.13708e-08,9.10711e-12,-24541.9,7.83908], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.35788,0.00180622,-7.80465e-07,1.47643e-10,-9.44754e-15,-25255.9,-2.63411], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-204.745,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """ATcT/A""",
    longDesc = 
"""
ATcT/A.
F[C]F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 87,
    label = "CHFCCF3",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
6 C u0 p0 c0 {4,S} {7,D} {8,S}
7 C u1 p0 c0 {5,S} {6,D}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.32858,0.0408063,-3.76794e-05,1.5829e-08,-2.20385e-12,-68139.5,17.9311], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.72422,0.0166944,-9.71761e-06,2.65852e-09,-2.78897e-13,-69892.1,-19.1162], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-566.683,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """0""",
    longDesc = 
"""
0
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC=[C]C(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 88,
    label = "CFCHCF3",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {7,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u0 p0 c0 {5,S} {7,D} {8,S}
7 C u1 p0 c0 {4,S} {6,D}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.21378,0.0419375,-4.01432e-05,1.79433e-08,-2.84775e-12,-70085,18.24], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.79425,0.0166275,-9.69601e-06,2.65705e-09,-2.79155e-13,-71851.7,-19.5844], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-582.965,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """0""",
    longDesc = 
"""
0
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[C]=CC(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 89,
    label = "CH2CHF",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,S} {2,D} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.6115,0.00668684,2.76818e-05,-4.33825e-08,1.85254e-11,-18432.6,12.6328], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.92787,0.00889384,-3.17972e-06,5.11682e-10,-3.05632e-14,-19827.7,-7.04448], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-153.943,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (133.032,'J/mol/K'),
    ),
    shortDesc = """RUS 91""",
    longDesc = 
"""
RUS 91
***********************
*** Fluoroethylenes ***
***********************.
C=CF
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 90,
    label = "CHFCHCF3",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {7,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u0 p0 c0 {5,S} {7,D} {8,S}
7 C u0 p0 c0 {4,S} {6,D} {9,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.941993,0.0482324,-4.46848e-05,1.93728e-08,-2.9209e-12,-101894,23.2937], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.48122,0.0200031,-1.12323e-05,2.9987e-09,-3.09262e-13,-103898,-19.385], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-848.567,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (203.705,'J/mol/K'),
    ),
    shortDesc = """0""",
    longDesc = 
"""
0
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC=CC(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 91,
    label = "CF3CHCH",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 C u0 p0 c0 {4,S} {6,D} {7,S}
6 C u1 p0 c0 {5,D} {8,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.681987,0.0469264,-4.86401e-05,2.2047e-08,-2.75415e-12,-47231.4,22.9561], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.7774,0.00793163,-2.8875e-06,4.67652e-10,-2.80481e-14,-50230.6,-37.9661], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-394.539,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """CF3-CH=CH A10/04""",
    longDesc = 
"""
CF3-CH=CH A10/04.
[CH]=CC(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 92,
    label = "CHF",
    molecule = 
"""
multiplicity 3
1 F u0 p3 c0 {2,S}
2 C u2 p0 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.42273,-0.00560196,2.21849e-05,-2.39634e-08,8.91307e-12,16651.6,2.54111], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.09415,0.00534934,-1.69763e-06,2.19446e-10,-1.00206e-14,17204.2,13.7861], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (138.483,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """singlet      T 7/11""",
    longDesc = 
"""
singlet      T 7/11.
[CH]F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 93,
    label = "CH2F-CH2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u1 p0 c0 {2,S} {6,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.38589,0.00444185,2.81593e-05,-3.89282e-08,1.56056e-11,-8871.72,6.2837], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.17561,0.0107043,-3.7837e-06,6.04072e-10,-3.58779e-14,-9899.78,-5.63727], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-73.2316,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """beta-Flu T 4/10""",
    longDesc = 
"""
beta-Flu T 4/10
********************
*** Fluoroethyls ***
********************.
[CH2]CF
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 94,
    label = "CH3-CHF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u1 p0 c0 {1,S} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.74844,0.000509115,3.62637e-05,-4.54978e-08,1.75184e-11,-10583.2,4.50274], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.75331,0.0111538,-3.96206e-06,6.34664e-10,-3.77832e-14,-11523.7,-3.95889], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-87.2395,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """alfa-Flu  T 4/10""",
    longDesc = 
"""
alfa-Flu  T 4/10.
C[CH]F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 95,
    label = "CH3-CH2F",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00577,-0.000311044,5.57189e-05,-7.28405e-08,2.90642e-11,-34321.4,7.92813], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.18082,0.013589,-4.8704e-06,7.84862e-10,-4.69209e-14,-35834.1,-7.96595], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-285.421,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """T 6/11""",
    longDesc = 
"""
T 6/11
*********************
*** Fluoroethanes ***
*********************.
CCF
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 96,
    label = "CF2CH",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,D}
4 C u1 p0 c0 {3,D} {5,S}
5 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.647126,0.0316596,-4.14529e-05,2.86094e-08,-8.06098e-12,-9438.54,21.7994], Tmin=(298,'K'), Tmax=(1050,'K')),
            NASAPolynomial(coeffs=[7.41103,0.0064817,-3.06314e-06,6.25625e-10,-4.55126e-14,-11017.4,-11.6171], Tmin=(1050,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-81.0671,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """96ZACWES""",
    longDesc = 
"""
96ZACWES
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=C(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 97,
    label = "CHFCH[Z]",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u1 p0 c0 {2,D} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.444202,0.0266069,-3.1481e-05,2.05356e-08,-5.52525e-12,13722.2,21.6689], Tmin=(298,'K'), Tmax=(1050,'K')),
            NASAPolynomial(coeffs=[5.27205,0.00817547,-3.46738e-06,6.47886e-10,-4.39229e-14,12647.8,-1.99725], Tmin=(1050,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (110.849,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """96ZACWES""",
    longDesc = 
"""
96ZACWES
********************
*** Fluorovinyls ***
********************
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=CF
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 98,
    label = "CHFCF[Z]",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u1 p0 c0 {2,S} {3,D}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.48306,0.0252896,-2.89899e-05,1.83569e-08,-4.98659e-12,-6275.04,18.7682], Tmin=(298,'K'), Tmax=(1050,'K')),
            NASAPolynomial(coeffs=[7.72646,0.00500295,-1.86131e-06,3.11994e-10,-1.95361e-14,-7900.3,-12.8643], Tmin=(1050,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-53.9692,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """96ZACWES""",
    longDesc = 
"""
96ZACWES
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[C]=CF
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 99,
    label = "CH2CFO",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 O u0 p2 c0 {4,D}
3 C u1 p0 c0 {4,S} {5,S} {6,S}
4 C u0 p0 c0 {1,S} {2,D} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.807509,0.0306962,-3.16571e-05,1.70422e-08,-3.7773e-12,-31492.8,20.5216], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.36521,0.00720529,-2.94165e-06,5.42254e-10,-3.72494e-14,-33493.1,-17.9789], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-264.345,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (128.874,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(=O)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 100,
    label = "CHFCHF[Z]",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {2,S} {3,D} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.69825,0.0123878,1.53769e-05,-3.23558e-08,1.47697e-11,-38297.2,12.826], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.64663,0.00755623,-2.746e-06,4.46891e-10,-2.69076e-14,-40030.2,-14.6983], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-318.991,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (133.032,'J/mol/K'),
    ),
    shortDesc = """RUS 91""",
    longDesc = 
"""
RUS 91.
FC=CF
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 101,
    label = "C2HF",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,T} {4,S}
3 C u0 p0 c0 {1,S} {2,T}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.30649,0.0277924,-4.86269e-05,4.25957e-08,-1.42676e-11,11286,13.9347], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.2095,0.00369585,-1.29974e-06,2.06831e-10,-1.22578e-14,10401.7,-8.93525], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (92.4999,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (87.302,'J/mol/K'),
    ),
    shortDesc = """T 7/11""",
    longDesc = 
"""
T 7/11
************************
*** Fluoroacetylenes ***
************************.
C#CF
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 102,
    label = "CH2F-CHF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u1 p0 c0 {2,S} {3,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.28983,0.0255773,-1.99128e-05,7.58804e-09,-1.12378e-12,-31476.5,15.4313], Tmin=(298,'K'), Tmax=(1250,'K')),
            NASAPolynomial(coeffs=[8.72145,0.00868155,-3.54229e-06,6.63135e-10,-4.47423e-14,-33406,-18.2518], Tmin=(1250,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-262.495,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """95BURZAC91CHE""",
    longDesc = 
"""
95BURZAC91CHE
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[CH]CF
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 103,
    label = "CF2CF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {1,S} {2,S} {5,D}
5 C u1 p0 c0 {3,S} {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.41464,0.0268292,-3.39283e-05,2.31906e-08,-6.71131e-12,-29099,15.3577], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.28002,0.00372628,-1.44028e-06,2.43838e-10,-1.50794e-14,-30844.9,-19.233], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-242.631,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """tpis91""",
    longDesc = 
"""
tpis91.
F[C]=C(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 104,
    label = "CH2F-CH2F",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.58944,-0.0113537,9.78443e-05,-1.22111e-07,4.76646e-11,-55683.5,2.61082], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.0316,0.0111994,-4.26519e-06,7.11447e-10,-4.35029e-14,-58529.6,-28.5865], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-462.2,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """HFC-152T 9/10""",
    longDesc = 
"""
HFC-152T 9/10.
FCCF
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 105,
    label = "C2F2",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {2,S} {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.21917,0.0174655,-2.90187e-05,2.55813e-08,-8.81244e-12,-1150.82,2.68489], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.53994,0.00275655,-1.01925e-06,1.67696e-10,-1.01707e-14,-1857.34,-13.2743], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-8.84137,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (87.302,'J/mol/K'),
    ),
    shortDesc = """T 7/11""",
    longDesc = 
"""
T 7/11.
FC#CF
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 106,
    label = "CF3O",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 O u1 p2 c0 {5,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.82041,0.0265327,-2.45067e-05,7.86172e-09,2.73541e-13,-77378.1,16.8622], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.76423,0.00330092,-1.28962e-06,2.19816e-10,-1.3656e-14,-79477.1,-23.7694], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-644.739,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """Radical      T07/04""",
    longDesc = 
"""
Radical      T07/04.
[O]C(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 107,
    label = "C3F7O2",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {10,S}
2  F u0 p3 c0 {10,S}
3  F u0 p3 c0 {11,S}
4  F u0 p3 c0 {11,S}
5  F u0 p3 c0 {12,S}
6  F u0 p3 c0 {12,S}
7  F u0 p3 c0 {12,S}
8  O u0 p2 c0 {9,S} {11,S}
9  O u1 p2 c0 {8,S}
10 C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
11 C u0 p0 c0 {3,S} {4,S} {8,S} {10,S}
12 C u0 p0 c0 {5,S} {6,S} {7,S} {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.64147,0.0875162,-0.000110022,7.25182e-08,-2.04158e-11,-182807,22.5219], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.8741,0.0237351,-1.36711e-05,3.71839e-09,-3.93068e-13,-186071,-56.0759], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-1513.32,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (270.22,'J/mol/K'),
    ),
    shortDesc = """Hynes""",
    longDesc = 
"""
Hynes
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OC(F)(F)C(F)(F)C(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 108,
    label = "C3F7OH",
    molecule = 
"""
1  F u0 p3 c0 {9,S}
2  F u0 p3 c0 {9,S}
3  F u0 p3 c0 {10,S}
4  F u0 p3 c0 {10,S}
5  F u0 p3 c0 {11,S}
6  F u0 p3 c0 {11,S}
7  F u0 p3 c0 {11,S}
8  O u0 p2 c0 {10,S} {12,S}
9  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
10 C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
11 C u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
12 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.42913,0.0890912,-0.000114105,7.6941e-08,-2.2121e-11,-215936,19.1804], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.9628,0.0256577,-1.51304e-05,4.19266e-09,-4.49003e-13,-218892,-55.3445], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-1789.22,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (270.22,'J/mol/K'),
    ),
    shortDesc = """hynes""",
    longDesc = 
"""
hynes
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
OC(F)(F)C(F)(F)C(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 109,
    label = "C3F6O",
    molecule = 
"""
1  F u0 p3 c0 {8,S}
2  F u0 p3 c0 {8,S}
3  F u0 p3 c0 {8,S}
4  F u0 p3 c0 {9,S}
5  F u0 p3 c0 {9,S}
6  F u0 p3 c0 {9,S}
7  O u0 p2 c0 {10,D}
8  C u0 p0 c0 {1,S} {2,S} {3,S} {10,S}
9  C u0 p0 c0 {4,S} {5,S} {6,S} {10,S}
10 C u0 p0 c0 {7,D} {8,S} {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.60628,0.0723195,-0.000100511,7.05279e-08,-1.99518e-11,-171357,14.8256], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.0456,0.0145586,-8.8123e-06,2.46295e-09,-2.61338e-13,-174404,-55.2406], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-1418.58,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """hynes""",
    longDesc = 
"""
hynes
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=C(C(F)(F)F)C(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 110,
    label = "CF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p1 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99599,-0.00462546,1.58271e-05,-1.73528e-08,6.45554e-12,28604.5,3.67055], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.74644,0.000801632,-2.95064e-07,5.03804e-11,-3.08738e-15,28455.5,3.84192], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (238.16,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """ATcT/A""",
    longDesc = 
"""
ATcT/A.
[CH2]F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 111,
    label = "C3F6",
    molecule = 
"""
1 F u0 p3 c0 {7,S}
2 F u0 p3 c0 {7,S}
3 F u0 p3 c0 {7,S}
4 F u0 p3 c0 {8,S}
5 F u0 p3 c0 {9,S}
6 F u0 p3 c0 {9,S}
7 C u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
8 C u0 p0 c0 {4,S} {7,S} {9,D}
9 C u0 p0 c0 {5,S} {6,S} {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.35781,0.0580498,-6.67558e-05,3.6811e-08,-7.9299e-12,-141947,16.8586], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.7296,0.00574055,-2.31302e-06,4.01018e-10,-2.51742e-14,-146124,-65.9854], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-1180.16,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (203.705,'J/mol/K'),
    ),
    shortDesc = """CF2=CF-CF3  A11/04""",
    longDesc = 
"""
CF2=CF-CF3  A11/04.
FC(F)=C(F)C(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

entry(
    index = 112,
    label = "C3F7O",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {9,S}
2  F u0 p3 c0 {10,S}
3  F u0 p3 c0 {10,S}
4  F u0 p3 c0 {10,S}
5  F u0 p3 c0 {11,S}
6  F u0 p3 c0 {11,S}
7  F u0 p3 c0 {11,S}
8  O u1 p2 c0 {9,S}
9  C u0 p0 c0 {1,S} {8,S} {10,S} {11,S}
10 C u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
11 C u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.13622,0.0733659,-7.41376e-05,3.25698e-08,-4.25576e-12,-182354,24.1334], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[22.8718,0.00764005,-1.65735e-06,-2.94155e-10,1.03517e-13,-188043,-86.6605], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-1510.54,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (249.434,'J/mol/K'),
    ),
    shortDesc = """Hynes""",
    longDesc = 
"""
Hynes
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]C(F)(C(F)(F)F)C(F)(F)F
_imported from C1_C3_hydrofluorocarbons_NIST/thermo-frozen3.txt.
""",
)

