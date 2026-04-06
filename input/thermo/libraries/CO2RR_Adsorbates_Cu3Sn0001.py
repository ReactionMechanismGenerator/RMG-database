#!/usr/bin/env python
# encoding: utf-8

name = "CO2RR_Adsorbates_Cu3Sn0001"
solvent = "water"
shortDesc = u"Place holder for short description"
longDesc = u"""
Place holder for long description
"""

entry(
    index = 0,
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
        NASAPolynomial(coeffs=[1.74349313, 0.0148300711, -1.65536121e-05, 1.03768953e-08, -2.77422703e-12, -14068.2838, -8.10961736], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[7.60674062, -0.00396066968, 7.15100332e-06, -3.87857554e-09, 7.04121665e-13, -15569.5014, -37.7908267], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""CHOX""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu3Sn",
    facet = "0001",
)


entry(
    index = 1,
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
        NASAPolynomial(coeffs=[2.51074428, 0.0220340273, -2.02688214e-05, 9.54750791e-09, -1.82176149e-12, -30765.8755, -4.81098828], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[11.9774317, -0.0061910143, 1.12437071e-05, -6.15372406e-09, 1.12529604e-12, -33288.3219, -53.2387915], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""COCHOX""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu3Sn",
    facet = "0001",
)


entry(
    index = 2,
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
        NASAPolynomial(coeffs=[1.57291532, 0.0239770732, -2.79387799e-05, 1.65750947e-08, -3.92695945e-12, -48808.2078, -6.7526346], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[10.2432721, -0.0045092048, 8.09079692e-06, -4.35111478e-09, 7.85594402e-13, -50956.2429, -50.3765829], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""COOHX""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu3Sn",
    facet = "0001",
)


entry(
    index = 3,
    label = "COX",
    molecule =
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 X u0 p0 c0 {2,D} 
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[2.15374115, 0.00711964156, -1.13374895e-05, 1.00074377e-08, -3.47838511e-12, -19372.6808, -4.67420257], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[4.45424836, -0.00162230699, 2.9503086e-06, -1.61116576e-09, 2.93861513e-13, -19914.6116, -16.0376878], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""COX""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu3Sn",
    facet = "0001",
)


entry(
    index = 4,
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
        NASAPolynomial(coeffs=[0.788155367, 0.0249548897, -2.96759698e-06, -1.24467075e-08, 6.52723015e-12, -34237.4683, 2.48957937], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[16.8164772, -0.0159260566, 2.84392268e-05, -1.52019708e-08, 2.72829405e-12, -38845.6552, -81.1844559], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""OCH2CH3X""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu3Sn",
    facet = "0001",
)


entry(
    index = 5,
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
        NASAPolynomial(coeffs=[2.97459822, 0.0242885566, -4.95324176e-06, -1.04154645e-08, 5.88135443e-12, -46058.3536, -4.8074186], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[17.7412996, -0.0135023109, 2.41363604e-05, -1.29228777e-08, 2.32333159e-12, -50287.6975, -81.8408018], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""OCHCH2OHX""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu3Sn",
    facet = "0001",
)


entry(
    index = 6,
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
        NASAPolynomial(coeffs=[-0.163426185, 0.0309141687, -2.93377835e-05, 1.44116925e-08, -2.69761991e-12, -22710.7822, 5.99423326], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[13.0987573, -0.00985382394, 1.7589596e-05, -9.39193391e-09, 1.68443623e-12, -26156.9338, -61.4743534], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""OCHCH2X""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu3Sn",
    facet = "0001",
)


entry(
    index = 7,
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
        NASAPolynomial(coeffs=[3.00634079, 0.0152798875, 6.13476544e-06, -1.65540464e-08, 7.12691885e-12, -26918.8699, -4.30723606], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[14.9615622, -0.0130702141, 2.33503201e-05, -1.24906387e-08, 2.24283666e-12, -30476.5943, -67.2821044], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""OCHCH3X""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu3Sn",
    facet = "0001",
)


entry(
    index = 8,
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
        NASAPolynomial(coeffs=[1.31738489, 0.0337353549, -3.07765911e-05, 1.35163088e-08, -1.94956551e-12, -41257.9069, -0.331264019], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[15.8143526, -0.0101891781, 1.81561425e-05, -9.67051827e-09, 1.73209325e-12, -45043.1443, -74.2060751], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""OCHCHOHX""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu3Sn",
    facet = "0001",
)


entry(
    index = 9,
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
        NASAPolynomial(coeffs=[-0.186083938, 0.0313033805, -3.31640683e-05, 1.83063923e-08, -4.06516487e-12, -16607.1771, -0.533154725], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[12.1682959, -0.00776604449, 1.39731944e-05, -7.54695754e-09, 1.3659676e-12, -19762.1543, -63.1133931], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""OCHCHX""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu3Sn",
    facet = "0001",
)


entry(
    index = 10,
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
        NASAPolynomial(coeffs=[0.0579249054, 0.0344787757, -3.46894579e-05, 1.74808247e-08, -3.37110895e-12, -40845.0891, 4.97109633], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[13.9289506, -0.00853520745, 1.53752974e-05, -8.32061068e-09, 1.50852866e-12, -44422.9436, -65.4843799], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""OCHOCHX""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu3Sn",
    facet = "0001",
)


entry(
    index = 11,
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
        NASAPolynomial(coeffs=[1.67220889, 0.0144593325, -7.37932862e-06, -1.33628765e-09, 1.74722736e-12, -57413.8836, -1.50759757], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[9.14577907, -0.00549354708, 9.94099598e-06, -5.41764493e-09, 9.87569455e-13, -59512.1847, -40.2901072], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""OCHOX""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu3Sn",
    facet = "0001",
)


entry(
    index = 12,
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
        NASAPolynomial(coeffs=[2.41884657, 0.0278294959, -3.94623871e-05, 2.87941258e-08, -8.50641432e-12, -26978.4777, -12.375979], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[11.0515201, -0.00331790688, 6.11806441e-06, -3.41065788e-09, 6.32647174e-13, -29007.55, -55.2010354], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
    ],
    Tmin=(298.0, 'K'),
    Tmax=(2000.0, 'K'),
),
    shortDesc = u"""XCOXCO""",
    longDesc =
u"""Calculated by Torrie Asifor at Northeastern University using Statistical Mechanics. Based on DFT calculations by Colin Gallagher at Northeastern University
""",
    metal = "Cu3Sn",
    facet = "0001",
)
