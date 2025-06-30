#!/usr/bin/env python
# encoding: utf-8

name = "CO2RR_Adsorbates_Ag111"
shortDesc = u"Place holder for short description"
longDesc = u"""
Place holder for long description
"""

entry(
    index = 0,
    label = "CHX",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,T}
2 H u0 p0 c0 {1,S}
3 X u0 p0 c0 {1,T}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[0.266342243, 0.0255005593, -4.67302907e-05, 3.94631134e-08, -1.2647867e-11, 31227.7542, -4.07584264], Tmin=(300.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[5.83835547, -0.000550143917, 1.04877997e-06, -5.97825593e-10, 1.12691258e-13, 30217.8588, -30.2412718], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(300.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""CHX""",
    longDesc = 
u"""Calculated by Su Sun at Northeastern University using Statistical Mechanics. Based on DFT calculations by Manish Kumar Kothakonda at Northeastern University
""",
)


entry(
    index = 1,
    label = "COX",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 X u0 p0 c0 {2,D}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[4.76251327, 0.00111269978, -2.10966611e-06, 1.82404356e-09, -5.94635137e-13, -14561.0462, -12.3594921], Tmin=(300.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[4.99431896, -1.76936326e-05, 3.42262824e-08, -1.96003384e-11, 3.70408721e-15, -14601.0429, -13.4373387], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(300.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""COX""",
    longDesc = 
u"""Calculated by Su Sun at Northeastern University using Statistical Mechanics. Based on DFT calculations by Manish Kumar Kothakonda at Northeastern University
""",
)


entry(
    index = 2,
    label = "HCOOH",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[13.9828152, 8.07094773e-05, -1.53259344e-07, 1.32648986e-10, -4.32758868e-14, -50413.5699, -21.9105715], Tmin=(300.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[13.9995921, -1.26354032e-06, 2.44635089e-09, -1.40132815e-12, 2.64862147e-16, -50416.4578, -21.9885437], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(300.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""HCOOH""",
    longDesc = 
u"""Calculated by Su Sun at Northeastern University using Statistical Mechanics. Based on DFT calculations by Manish Kumar Kothakonda at Northeastern University
""",
)


entry(
    index = 3,
    label = "COHX",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 C u0 p0 c0 {1,S} {4,T}
3 H u0 p0 c0 {1,S}
4 X u0 p0 c0 {2,T}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[7.90698765, 0.00510752439, -9.66734244e-06, 8.34878241e-09, -2.71941775e-12, 7452.81979, -31.9152917], Tmin=(300.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[8.97362495, -8.26142943e-05, 1.59656769e-07, -9.14041331e-11, 1.72709588e-14, 7268.29432, -36.8774988], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(300.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""COHX""",
    longDesc = 
u"""Calculated by Su Sun at Northeastern University using Statistical Mechanics. Based on DFT calculations by Manish Kumar Kothakonda at Northeastern University
""",
)


entry(
    index = 4,
    label = "CHOHX",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 C u0 p0 c0 {1,S} {3,S} {5,D}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 X u0 p0 c0 {2,D}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[10.4790225, 0.00244168743, -4.63031562e-06, 4.00396281e-09, -1.30541023e-12, -3872.00194, -32.829477], Tmin=(300.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[10.9875496, -3.87497326e-05, 7.49655069e-08, -4.29319322e-11, 8.11345985e-15, -3959.71854, -35.1938771], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(300.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""CHOHX""",
    longDesc = 
u"""Calculated by Su Sun at Northeastern University using Statistical Mechanics. Based on DFT calculations by Manish Kumar Kothakonda at Northeastern University
""",
)


entry(
    index = 5,
    label = "COOHX",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {5,S}
4 H u0 p0 c0 {1,S}
5 X u0 p0 c0 {3,S}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[10.986781, 6.20842133e-05, -1.17891803e-07, 1.02037681e-10, -3.32891347e-14, -44411.4442, -16.4053971], Tmin=(300.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[10.9996863, -9.71979115e-07, 1.88183405e-09, -1.07795624e-12, 2.03742017e-16, -44413.6656, -16.4653759], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(300.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""COOHX""",
    longDesc = 
u"""Calculated by Su Sun at Northeastern University using Statistical Mechanics. Based on DFT calculations by Manish Kumar Kothakonda at Northeastern University
""",
)


entry(
    index = 6,
    label = "HCOOX",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
5 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[10.6983745, 0.00141493133, -2.68478436e-06, 2.32253402e-09, -7.57431101e-13, -54136.7261, -30.7077828], Tmin=(300.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[10.9928138, -2.2323418e-05, 4.3200796e-08, -2.47430431e-11, 4.6762909e-15, -54187.4686, -32.0765361], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(300.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""HCOOX""",
    longDesc = 
u"""Calculated by Su Sun at Northeastern University using Statistical Mechanics. Based on DFT calculations by Manish Kumar Kothakonda at Northeastern University
""",
)


entry(
    index = 7,
    label = "CX",
    molecule = 
"""
1 C u0 p0 c0 {2,Q}
2 X u0 p0 c0 {1,Q}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[-0.208109795, 0.0141255843, -2.57114636e-05, 2.16103094e-08, -6.90214919e-12, 49419.1139, -0.591413039], Tmin=(300.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[2.90679495, -0.000321226726, 6.11116124e-07, -3.48106063e-10, 6.55928418e-14, 48849.4769, -15.2453553], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(300.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""CX""",
    longDesc = 
u"""Calculated by Su Sun at Northeastern University using Statistical Mechanics. Based on DFT calculations by Manish Kumar Kothakonda at Northeastern University
""",
)


entry(
    index = 8,
    label = "CH3X",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[10.7907888, 0.000981788117, -1.86336377e-06, 1.61221374e-09, -5.25842614e-13, 2355.68713, -30.4031728], Tmin=(300.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[10.9950211, -1.54504782e-05, 2.99051637e-08, -1.71288833e-11, 3.23734262e-15, 2320.50412, -31.3525114], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(300.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""CH3X""",
    longDesc = 
u"""Calculated by Su Sun at Northeastern University using Statistical Mechanics. Based on DFT calculations by Manish Kumar Kothakonda at Northeastern University
""",
)


entry(
    index = 9,
    label = "CHOX",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[7.78973681, 0.000986354049, -1.87157965e-06, 1.61905637e-09, -5.28011849e-13, -9861.74615, -21.3183986], Tmin=(300.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[7.9949907, -1.55613972e-05, 3.01146711e-08, -1.72480167e-11, 3.25977367e-15, -9897.11865, -22.2725571], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(300.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""CHOX""",
    longDesc = 
u"""Calculated by Su Sun at Northeastern University using Statistical Mechanics. Based on DFT calculations by Manish Kumar Kothakonda at Northeastern University
""",
)


entry(
    index = 10,
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
        NASAPolynomial(coeffs=[13.9828152, 8.07094773e-05, -1.53259344e-07, 1.32648986e-10, -4.32758868e-14, -11094.9704, -22.9645165], Tmin=(300.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[13.9995921, -1.26354032e-06, 2.44635089e-09, -1.40132815e-12, 2.64862147e-16, -11097.8583, -23.0424887], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(300.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""CH4""",
    longDesc = 
u"""Calculated by Su Sun at Northeastern University using Statistical Mechanics. Based on DFT calculations by Manish Kumar Kothakonda at Northeastern University
""",
)


entry(
    index = 11,
    label = "CH2X",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 X u0 p0 c0 {1,D}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[3.85100003, 0.0235194683, -4.38661963e-05, 3.75015562e-08, -1.21265551e-11, 19076.9562, -20.014004], Tmin=(300.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[8.86633631, -0.000437192952, 8.38897191e-07, -4.79205188e-10, 9.04376865e-14, 18190.0445, -43.4485995], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(300.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""CH2X""",
    longDesc = 
u"""Calculated by Su Sun at Northeastern University using Statistical Mechanics. Based on DFT calculations by Manish Kumar Kothakonda at Northeastern University
""",
)


entry(
    index = 12,
    label = "CH2OHX",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[13.6992407, 0.00141127697, -2.6783469e-06, 2.31725865e-09, -7.55779555e-13, -15621.9329, -39.5967286], Tmin=(300.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[13.9928408, -2.22232177e-05, 4.3012071e-08, -2.46358334e-11, 4.65611636e-15, -15672.516, -40.9615025], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(300.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""CH2OHX""",
    longDesc = 
u"""Calculated by Su Sun at Northeastern University using Statistical Mechanics. Based on DFT calculations by Manish Kumar Kothakonda at Northeastern University
""",
)

