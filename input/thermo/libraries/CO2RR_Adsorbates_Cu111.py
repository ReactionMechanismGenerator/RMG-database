#!/usr/bin/env python
# encoding: utf-8

name = "CO2RR_Adsorbates_Cu111"
solvent = "water"
shortDesc = u"Place holder for short description"
longDesc = u"""
Place holder for long description
"""

entry(
    index = 0,
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
        NASAPolynomial(coeffs=[0.472735789, 0.0241008939, -2.46801184e-05, 1.37773161e-08, -3.0813789e-12, -21157.4578, 2.60923861], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[10.5681808, -0.00792065082, 1.40261804e-05, -7.39838131e-09, 1.31411936e-12, -23729.4054, -48.4995382], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""CH2OHX""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu",
    facet = "111",
)


entry(
    index = 1,
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
        NASAPolynomial(coeffs=[0.466416892, 0.0226076886, -3.69343557e-05, 3.09744704e-08, -9.99641342e-12, 8004.29404, -3.72629114], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[7.09877494, -0.00433095407, 7.66695886e-06, -4.02988705e-09, 7.12914077e-13, 6583.37634, -35.9122248], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""CH2X""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu",
    facet = "111",
)


entry(
    index = 2,
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
        NASAPolynomial(coeffs=[0.797287316, 0.0196521154, -2.31595564e-05, 1.66221917e-08, -4.97799024e-12, -3111.00157, -4.77956538], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[8.91016513, -0.00741666648, 1.31686499e-05, -6.96776478e-09, 1.239664e-12, -5144.93228, -45.607756], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""CH3X""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu",
    facet = "111",
)


entry(
    index = 3,
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
        NASAPolynomial(coeffs=[1.41019307, 0.0224007435, -2.72300418e-05, 1.76532667e-08, -4.60273486e-12, -11957.2586, -6.3198189], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[9.6152098, -0.00536925487, 9.50116088e-06, -5.00366325e-09, 8.87974014e-13, -13954.9197, -47.4140367], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""CHOHX""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu",
    facet = "111",
)


entry(
    index = 4,
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
        NASAPolynomial(coeffs=[2.37863592, 0.012408481, -1.25801919e-05, 7.24790581e-09, -1.8141235e-12, -13935.0226, -9.04256939], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[7.62620563, -0.00385204041, 6.94355702e-06, -3.75812385e-09, 6.81108837e-13, -15307.787, -35.7479814], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""CHOX""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu",
    facet = "111",
)


entry(
    index = 5,
    label = "CHX",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,T}
2 H u0 p0 c0 {1,S}
3 X u0 p0 c0 {1,T}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[-2.08855354, 0.0294663183, -5.2247455e-05, 4.3854041e-08, -1.3978891e-11, 15687.781, 6.79987743], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[4.98902907, -0.00223592875, 3.9741247e-06, -2.09265476e-09, 3.70889503e-13, 14337.5132, -26.7707539], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""CHX""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu",
    facet = "111",
)


entry(
    index = 6,
    label = "COCHOX",
    molecule =
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {4,D}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 C u0 p0 c0 {2,D} {3,S} {6,S}
5 H u0 p0 c0 {3,S}
6 X u0 p0 c0 {4,S}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[1.93949246, 0.0256383446, -2.77539412e-05, 1.63477437e-08, -4.11348733e-12, -34804.6135, -3.52046277], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[12.0315845, -0.00610743143, 1.11113129e-05, -6.09316938e-09, 1.11585568e-12, -37414.5425, -54.7480472], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""COCHOX""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu",
    facet = "111",
)


entry(
    index = 7,
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
        NASAPolynomial(coeffs=[1.88601171, 0.0175443623, -2.3496585e-05, 1.60954951e-08, -4.3767108e-12, -10766.6389, -8.99891253], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[7.64233194, -0.00292695859, 5.17262432e-06, -2.71697657e-09, 4.81552239e-13, -12112.2365, -37.5691896], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""COHX""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu",
    facet = "111",
)


entry(
    index = 8,
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
        NASAPolynomial(coeffs=[1.05917125, 0.0219066236, -2.43200647e-05, 1.36437162e-08, -3.01907804e-12, -48232.3178, 0.75905578], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[9.25517481, -0.00446613856, 8.00866345e-06, -4.303982e-09, 7.76650481e-13, -50290.4042, -40.6148991], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""COOHX""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu",
    facet = "111",
)


entry(
    index = 9,
    label = "COX",
    molecule =
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 X u0 p0 c0 {2,D} 
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[3.52678302, 0.00519878526, -6.77403179e-06, 5.45808928e-09, -1.86754692e-12, -22933.4167, -15.777435], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[5.53299166, -0.00147915536, 2.70209812e-06, -1.4866849e-09, 2.72829319e-13, -23451.2467, -25.9161271], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""COX""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu",
    facet = "111",
)


entry(
    index = 10,
    label = "OCH2CH3X",
    molecule =
"""
1 O u0 p2 c0 {2,S} {9,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[0.526183454, 0.0258797543, -4.36025144e-06, -1.14542255e-08, 6.25217239e-12, -36161.4155, 3.24649437], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[16.8038419, -0.0159680235, 2.8516839e-05, -1.52454216e-08, 2.73639731e-12, -40823.2612, -81.6436784], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""OCH2CH3X""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu",
    facet = "111",
)


entry(
    index = 11,
    label = "OCHCH2OHX",
    molecule =
"""
1 O u0 p2 c0 {3,S} {8,S}
2 O u0 p2 c0 {4,D}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {2,D} {3,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {1,S}
9 X u0 p0 c0 
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[3.09646829, 0.0237384116, -3.87127221e-06, -1.13323939e-08, 6.16656379e-12, -46953.0529, -4.1727781], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[17.7632799, -0.0135012658, 2.41421777e-05, -1.29323226e-08, 2.32590842e-12, -51169.7292, -80.7610976], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""OCHCH2OHX""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu",
    facet = "111",
)


entry(
    index = 12,
    label = "OCHCH2X",
    molecule =
"""
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u0 p0 c0 {2,D} {5,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[-0.628328912, 0.0328527253, -3.1908806e-05, 1.59572749e-08, -3.05474396e-12, -23681.7878, 7.83815501], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[13.1893158, -0.00985950398, 1.76359697e-05, -9.44590688e-09, 1.69824677e-12, -27258.0458, -62.3914324], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""OCHCH2X""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu",
    facet = "111",
)


entry(
    index = 13,
    label = "OCHCH3X",
    molecule =
"""
1 O u0 p2 c0 {3,D} 
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 X u0 p0 c0 
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[2.93148616, 0.0156994161, 5.27680207e-06, -1.57739035e-08, 6.86352711e-12, -27771.7175, -4.21488209], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[14.9647333, -0.0130728691, 2.33574302e-05, -1.24959647e-08, 2.24399815e-12, -31341.2771, -67.5434017], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""OCHCH3X""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu",
    facet = "111",
)


entry(
    index = 14,
    label = "OCHCHOHX",
    molecule =
"""
1 O u0 p2 c0 {3,S} {8,S}
2 O u0 p2 c0 {4,S} {7,S} 
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {2,S} {3,D} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[0.00911478161, 0.0397758564, -4.14240749e-05, 2.21262211e-08, -4.59902949e-12, -44975.5239, 5.06918604], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[15.8574169, -0.0102903723, 1.83673581e-05, -9.80550942e-09, 1.75919459e-12, -49009.9016, -75.1821401], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""OCHCHOHX""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu",
    facet = "111",
)


entry(
    index = 15,
    label = "OCHCHX",
    molecule =
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {6,D}
3 C u0 p0 c0 {1,D} {2,S} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
6 X u0 p0 c0 {2,D}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[0.276809443, 0.0301374978, -3.16219676e-05, 1.72227608e-08, -3.75111053e-12, -18198.9697, -1.71302897], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[12.2388819, -0.00757866622, 1.36344476e-05, -7.36324538e-09, 1.33257199e-12, -21258.6668, -62.3317273], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""OCHCHX""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu",
    facet = "111",
)


entry(
    index = 16,
    label = "OCHOCHX",
    molecule =
"""
1 O u0 p2 c0 {3,S} {7,S}
2 O u0 p2 c0 {4,S} {8,S} 
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {2,S} {3,D} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 X u0 p0 c0 {1,S}
8 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[-0.188361028, 0.0359884107, -3.77327255e-05, 2.00961226e-08, -4.20161128e-12, -41417.7273, 5.73697635], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[13.933618, -0.00846409226, 1.52416698e-05, -8.24316109e-09, 1.493801e-12, -45025.8482, -65.8263189], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""OCHOCHX""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu",
    facet = "111",
)


entry(
    index = 17,
    label = "OCHOX",
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
        NASAPolynomial(coeffs=[1.6663831, 0.0145773007, -7.54839692e-06, -1.28850802e-09, 1.76379918e-12, -56459.297, -1.41903333], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[9.15358298, -0.00545271031, 9.86437499e-06, -5.37406014e-09, 9.79390495e-13, -58557.4789, -40.2571999], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""OCHOX""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu",
    facet = "111",
)


entry(
    index = 18,
    label = "XCOXCO",
    molecule =
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {4,D}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 C u0 p0 c0 {2,D} {3,S} {6,S}
5 X u0 p0 c0 {3,S}
6 X u0 p0 c0 {4,S}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[2.49554898, 0.0242026474, -3.27700315e-05, 2.26836821e-08, -6.38929534e-12, -25528.1387, -6.08127138], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[10.2047191, -0.00286178768, 5.28404531e-06, -2.95345619e-09, 5.49031049e-13, -27368.1643, -44.4858043], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""XCOXCO""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu",
    facet = "111",
)
