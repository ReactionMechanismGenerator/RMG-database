name = "NCSU_2025_revised"
shortDesc = "Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids"
longDesc = u"""
New thermochemical properties, Cp°(T), H°(T), S°(T), and G°(T), are predicted for 123 species involved in the thermal destruction of perfluorinated carboxylic acids (PFCAs) using computational quantum chemistry and ideal-gas statistical mechanics. Partition functions were obtained from the results of calculations at the G4 level for species up to C4 in length and M06-2X-D3(0)/def2-QZVPP for species C5 to C8 in length. The 1D hindered-rotor approximation was used to correct for torsional modes in the larger species. Ideal-gas thermochemistry was computed and fitted to 7-parameter NASA polynomials over a 200–2500 K temperature range, and the data are provided in standardized format. INCLUDED CORRECTIONS FROM 2025. 

Citation:

Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids
Hrishikesh Ram, Thomas P. Sadej, C. Claire Murphy, Tim J. Mallo, and Phillip R. Westmoreland
The Journal of Physical Chemistry A 2024 128 (7), 1313-1326
DOI: 10.1021/acs.jpca.3c06937
"""

entry(
    index = 0,
    label = "H",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5, 0.0, 0.0, 0.0, 0.0, 25473.66, -0.44668285], Tmin=(200.0,'K'), Tmax=(6000.0,'K')),
            NASAPolynomial(coeffs=[2.5, 0.0, 0.0, 0.0, 0.0, 25473.66, -0.44668285], Tmin=(6000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 1,
    label = "O",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[2.54363697, -2.73162486e-05, -4.1902952e-09, 4.95481845e-12, -4.79553694e-16, 29226.012, 4.92229457], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 2,
    label = "F",
    molecule = 
"""
multiplicity 2
1 F u1 p3 c0

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.4196743, 0.0029392909, -8.9212228e-06, 9.9118537e-09, -3.7947152e-12, 8757.322, 4.7468987], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[2.6716339, -0.00017461853, 6.9066504e-08, -1.1953478e-11, 7.5236739e-16, 8787.4123, 3.9842568], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 3,
    label = "H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.34433112, 0.00798052075, -1.9478151e-05, 2.01572094e-08, -7.37611761e-12, -917.935173, 0.683010238], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[2.93286575, 0.000826608026, -1.46402364e-07, 1.54100414e-11, -6.888048e-16, -813.065581, -1.02432865], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 4,
    label = "O2",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78245636, -0.00299673416, 9.84730201e-06, -9.68129509e-09, 3.24372837e-12, -1063.94356, 3.65767573], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[3.66096065, 0.000656365811, -1.41149627e-07, 2.05797935e-11, -1.29913436e-15, -1215.97718, 3.41536279], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 5,
    label = "F2",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 F u0 p3 c0 {1,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.20832415, 0.00125919179, 3.89747979e-06, -7.22184984e-09, 3.31837862e-12, -1034.25794, 5.61903603], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[3.86166219, 0.000788367679, -1.8198294e-07, -9.1743656e-12, 2.65193472e-15, -1232.38655, 2.04119869], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 6,
    label = "OHr",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99198424, -0.00240106655, 4.61664033e-06, -3.87916306e-09, 1.36319502e-12, 3368.89836, -0.103998477], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[2.83853033, 0.00110741289, -2.94000209e-07, 4.20698729e-11, -2.4228989e-15, 3697.80808, 5.84494652], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 7,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.1986352, -0.0020364017, 6.5203416e-06, -5.4879269e-09, 1.771968e-12, -30293.726, -0.84900901], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[2.6770389, 0.0029731816, -7.7376889e-07, 9.4433514e-11, -4.2689991e-15, -29885.894, 6.88255], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 8,
    label = "HO2r",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.30179807, -0.00474912097, 2.11582905e-05, -2.42763914e-08, 9.29225225e-12, 264.018485, 3.7166622], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[4.17228741, 0.00188117627, -3.46277286e-07, 1.94657549e-11, 1.76256905e-16, 31.0206839, 2.95767672], Tmin=(1000.0,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 9,
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
            NASAPolynomial(coeffs=[4.31515149, -0.000847390622, 1.76404323e-05, -2.26762944e-08, 9.08950158e-12, -17706.7437, 3.27373319], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[4.57977305, 0.00405326003, -1.2984473e-06, 1.982114e-10, -1.13968792e-14, -18007.1775, 0.664970694], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[3.48137108, 0.000212245717, -6.86359044e-07, 8.56185857e-10, -2.34581508e-13, -33860.7305, 1.0257999], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[2.92491143, 0.000850523032, -1.58179777e-07, 1.17507204e-11, -1.43309132e-16, -33635.2481, 4.19018883], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 11,
    label = "CO",
    molecule = 
"""
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5795335, -0.00061035369, 1.0168143e-06, 9.0700586e-10, -9.0442449e-13, -14344.086, 3.5084093], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[3.0484859, 0.0013517281, -4.8579405e-07, 7.8853644e-11, -4.6980746e-15, -14266.117, 6.0170977], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 12,
    label = "CO2",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.356813, 0.0089841299, -7.1220632e-06, 2.4573008e-09, -1.4288548e-13, -48371.971, 9.9009035], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[4.6365111, 0.0027414569, -9.9589759e-07, 1.6038666e-10, -9.1619857e-15, -49024.904, -1.9348955], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 13,
    label = "HOCOr",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.92207919, 0.00762453859, 3.29884437e-06, -1.07135205e-08, 5.11587057e-12, -23028.1524, 11.2925886], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[5.39206152, 0.00411221455, -1.481949e-06, 2.3987546e-10, -1.43903104e-14, -23860.6717, -2.23529091], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 14,
    label = "HCOOr",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.76686225, -0.00465307002, 2.66314064e-05, -2.95373687e-08, 1.08273683e-11, -16437.5073, 3.9805095], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[4.14879557, 0.00558144141, -1.99182194e-06, 3.15300327e-10, -1.85171887e-14, -16689.6104, 5.08764733], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 15,
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
            NASAPolynomial(coeffs=[5.14911468, -0.0136622009, 4.91453921e-05, -4.84246767e-08, 1.66603441e-11, -10246.5983, -4.63848842], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[1.65326226, 0.0100263099, -3.31661238e-06, 5.36483138e-10, -3.14696758e-14, -10009.5936, 9.90506283], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 16,
    label = "CF2(s)",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p1 c0 {1,S} {3,S}
3 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56435487, 0.00123021056, 1.39909866e-05, -2.13708286e-08, 9.10710807e-12, -24458.7979, 7.83907808], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[5.35787718, 0.00180622418, -7.80465045e-07, 1.47642691e-10, -9.44754424e-15, -25172.8166, -2.63410779], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 17,
    label = "CF2(t)",
    molecule = 
"""
multiplicity 3
1 F u0 p3 c0 {2,S}
2 C u2 p0 c0 {1,S} {3,S}
3 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65863299, 0.00253462065, 7.99625743e-06, -1.34330295e-08, 5.75081256e-12, 4050.07968, 8.36023714], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[5.45344707, 0.00156561882, -6.08817038e-07, 1.03459271e-10, -6.41400747e-15, 3375.44779, -1.83921649], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 18,
    label = "CF3r",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.38179059, 0.0137269527, -3.47674937e-06, -9.01697393e-09, 5.57384083e-12, -57687.1035, 14.3743316], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[7.42981696, 0.00261728694, -1.02141596e-06, 1.73975666e-10, -1.08028191e-14, -59179.5501, -12.2816891], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 19,
    label = "CHF2r",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 H u0 p0 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.12220872, -0.00233706659, 2.99282606e-05, -3.88422961e-08, 1.55352879e-11, -30053.0523, 7.22245467], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[5.5232112, 0.00421970092, -1.58435294e-06, 2.63969157e-10, -1.61337618e-14, -30894.516, -2.40335469], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 20,
    label = "CH2F2",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.25023157, -0.00684861262, 4.85583334e-05, -5.83442752e-08, 2.24503933e-11, -55735.1602, 5.76716418], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[5.06948195, 0.00723193135, -2.64021025e-06, 4.30854708e-10, -2.59873096e-14, -56727.0077, -2.34590394], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 21,
    label = "CHF3",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.73539203, 0.00872478957, 1.7482151e-05, -3.2150475e-08, 1.41694928e-11, -85182.0557, 12.4879863], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[7.24609031, 0.00542386441, -2.02314394e-06, 3.34946402e-10, -2.04067524e-14, -86823.9019, -12.8982398], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 22,
    label = "CF4",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 F u0 p3 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.05119594, 0.0278318369, -2.46683439e-05, 6.75882532e-09, 9.14850873e-13, -113574.198, 18.1936795], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[9.47336526, 0.00359407743, -1.40334012e-06, 2.39113889e-10, -1.48513407e-14, -115816.621, -24.9736848], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 23,
    label = "CFOr",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 F u0 p3 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37992233, 0.00419050548, 2.12353533e-06, -6.20586665e-09, 2.85352218e-12, -22406.32, 9.39466699], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[5.01565891, 0.00195763376, -7.49685297e-07, 1.25610155e-10, -7.59885072e-15, -22978.5255, 0.369669039], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 24,
    label = "CF2O",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.12979433, 0.0141019782, -5.94383395e-06, -5.30542094e-09, 3.97366263e-12, -74163.7142, 15.1109046], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[6.81631709, 0.00316473302, -1.21776278e-06, 2.05582278e-10, -1.26893138e-14, -75537.4518, -9.52865117], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 25,
    label = "CF2OHr",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {1,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.82296204, 0.014628917, -4.91575497e-06, -4.9959848e-09, 3.07132075e-12, -57511.2591, 12.7503214], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[6.13972159, 0.00792804091, -4.71368414e-06, 1.43546348e-09, -1.78081858e-13, -58502.9191, -4.89266668], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 26,
    label = "HOCF2CO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 O u0 p2 c0 {3,S} {7,S}
5 F u0 p3 c0 {3,S}
6 F u0 p3 c0 {3,S}
7 H u0 p0 c0 {4,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.09960867, 0.0362710893, -4.07734276e-05, 2.31167596e-08, -5.2106622e-12, -73237.9027, 16.4304537], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[8.04197402, 0.0134840166, -8.06640146e-06, 2.29446418e-09, -2.50685517e-13, -74475.4953, -12.4836212], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 27,
    label = "CHF2CO2",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {4,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5959844, 0.0277761077, -1.80917861e-05, 2.203407e-09, 1.38850594e-12, -67111.2333, 16.1759542], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[7.27302862, 0.0153939852, -9.00768376e-06, 2.47339313e-09, -2.60504179e-13, -68362.9449, -7.96959414], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 28,
    label = "FCOOH",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {5,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.74744564, 0.0156039351, -3.55332951e-06, -6.43464995e-09, 3.41825032e-12, -75305.3467, 17.4472988], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[4.3795147, 0.0113011606, -6.4374204e-06, 1.71357905e-09, -1.75182363e-13, -76143.0356, 3.19271169], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 29,
    label = "PF2acid",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {8,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 F u0 p3 c0 {4,S}
8 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.29288001, 0.0363697973, -2.81337307e-05, 7.92002073e-09, 9.99586583e-14, -125557.862, 16.6866301], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[8.41880929, 0.0184199668, -1.10398151e-05, 3.07796368e-09, -3.27998753e-13, -127110.742, -14.5059092], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 30,
    label = "PF3acid",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {11,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 F u0 p3 c0 {7,S}
11 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.25253889, 0.0651622972, -7.0135291e-05, 3.69634486e-08, -7.63138074e-12, -176595.185, 16.4104158], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[13.2974244, 0.024892241, -1.55944358e-05, 4.5123644e-09, -4.95981186e-13, -178999.636, -37.8521439], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 31,
    label = "PF4acid",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {14,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 F u0 p3 c0 {10,S}
14 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.26013535, 0.0852018304, -9.27520764e-05, 4.91350442e-08, -1.01760753e-11, -227189.536, 12.0763544], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[17.9259357, 0.0316806803, -2.01834282e-05, 5.89799661e-09, -6.52326165e-13, -230379.799, -59.9631672], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 32,
    label = "PF5acid",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {17,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 F u0 p3 c0 {13,S}
17 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.85259858, 0.109751676, -0.000119878678, 6.28292983e-08, -1.27445623e-11, -278737.342, 13.3659226], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[22.5146967, 0.0388423743, -2.51233627e-05, 7.39817894e-09, -8.21555201e-13, -283056.716, -83.4271078], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 33,
    label = "PF6acid",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {20,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 F u0 p3 c0 {16,S}
20 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.42624047, 0.137282695, -0.000154754728, 8.3718967e-08, -1.76080826e-11, -329073.5, 14.6067168], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[27.3917621, 0.0457741333, -3.00221738e-05, 8.91745637e-09, -9.96086225e-13, -334484.28, -107.925875], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 34,
    label = "PF7acid",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {23,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 C u0 p0 c0 {16,S} {20,S} {21,S} {22,S}
20 F u0 p3 c0 {19,S}
21 F u0 p3 c0 {19,S}
22 F u0 p3 c0 {19,S}
23 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.26403677, 0.147458264, -0.000151512846, 7.21787045e-08, -1.27308063e-11, -379583.555, 6.53688745], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[30.9812066, 0.0557890782, -3.68083076e-05, 1.09085056e-08, -1.21312987e-12, -385686.964, -126.157886], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 35,
    label = "PF8acid",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {26,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 C u0 p0 c0 {16,S} {20,S} {21,S} {22,S}
20 F u0 p3 c0 {19,S}
21 F u0 p3 c0 {19,S}
22 C u0 p0 c0 {19,S} {23,S} {24,S} {25,S}
23 F u0 p3 c0 {22,S}
24 F u0 p3 c0 {22,S}
25 F u0 p3 c0 {22,S}
26 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29110517, 0.177967023, -0.000191157976, 9.59300069e-08, -1.81585653e-11, -429840.784, 10.1142128], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[36.7949757, 0.06062944, -4.016845e-05, 1.19482222e-08, -1.33259389e-12, -437375.453, -155.69207], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 36,
    label = "FCOOr",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 F u0 p3 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.95155346, 0.0170102644, -1.39064933e-05, 3.91055562e-09, 1.3635329e-13, -45823.6888, 16.9063898], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[5.50001605, 0.00662261862, -4.03433136e-06, 1.13531886e-09, -1.21388652e-13, -46723.6916, -1.16444208], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 37,
    label = "PF2carboxylr",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 F u0 p3 c0 {4,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.48332506, 0.0421886654, -4.61511419e-05, 2.42035928e-08, -4.89781592e-12, -94880.2063, 21.1111662], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[9.16042693, 0.014565104, -9.34306887e-06, 2.74972343e-09, -3.05560104e-13, -96569.8689, -16.6976241], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 38,
    label = "PF3carboxylr",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 F u0 p3 c0 {7,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.02957966, 0.0664328838, -7.92227834e-05, 4.60228177e-08, -1.05068075e-11, -146655.865, 18.9364545], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[13.8492258, 0.0209197562, -1.36012772e-05, 4.04060373e-09, -4.52618169e-13, -149108.067, -38.5278697], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 39,
    label = "PF4carboxylr",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 F u0 p3 c0 {10,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60385454, 0.0804797157, -8.67306905e-05, 4.40992248e-08, -8.53332209e-12, -197684.793, 12.5937573], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[18.5114953, 0.0278239091, -1.82091153e-05, 5.39293111e-09, -6.00437796e-13, -201015.059, -61.0706811], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 40,
    label = "PF5carboxylr",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 F u0 p3 c0 {13,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.52156005, 0.108768246, -0.000125318719, 6.91073459e-08, -1.48297568e-11, -246178.372, 10.6890553], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[23.5611287, 0.0345960439, -2.30395263e-05, 6.90729024e-09, -7.76261122e-13, -250485.589, -87.4867978], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 41,
    label = "PF6carboxylr",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 F u0 p3 c0 {16,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.09968063, 0.143559072, -0.000176236093, 1.04012838e-07, -2.40165864e-11, -296418.788, 16.0071135], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[28.4674532, 0.0414009103, -2.79682442e-05, 8.48053462e-09, -9.61742702e-13, -301857.989, -112.030379], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 42,
    label = "PF7carboxylr",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 C u0 p0 c0 {16,S} {20,S} {21,S} {22,S}
20 F u0 p3 c0 {19,S}
21 F u0 p3 c0 {19,S}
22 F u0 p3 c0 {19,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.70641376, 0.147995951, -0.00015951857, 8.01611566e-08, -1.52178066e-11, -347041.381, 5.26001696], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[32.388114, 0.0508862149, -3.42795648e-05, 1.02855517e-08, -1.15317168e-12, -353258.574, -131.692452], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 43,
    label = "PF8carboxylr",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 C u0 p0 c0 {16,S} {20,S} {21,S} {22,S}
20 F u0 p3 c0 {19,S}
21 F u0 p3 c0 {19,S}
22 C u0 p0 c0 {19,S} {23,S} {24,S} {25,S}
23 F u0 p3 c0 {22,S}
24 F u0 p3 c0 {22,S}
25 F u0 p3 c0 {22,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.89488297, 0.162157617, -0.000166218156, 7.90847382e-08, -1.40635805e-11, -397458.046, -0.581700733], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[33.9871917, 0.0653003947, -4.42003424e-05, 1.32515418e-08, -1.48328457e-12, -403852.108, -139.988855], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 44,
    label = "PF2acylF",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 F u0 p3 c0 {4,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.73765568, 0.0366140978, -3.77663109e-05, 1.86011694e-08, -3.47925655e-12, -124792.249, 14.3576641], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[9.20214968, 0.0140186914, -8.76705559e-06, 2.53090213e-09, -2.77332113e-13, -126248.276, -17.645425], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 45,
    label = "PF3acylF",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 F u0 p3 c0 {7,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.29853129, 0.066675114, -8.10952986e-05, 4.81672148e-08, -1.12570981e-11, -175601.851, 16.0504489], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[14.0309788, 0.0206720088, -1.34806683e-05, 4.01747963e-09, -4.51335571e-13, -177994.675, -40.7834998], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 46,
    label = "PF4acylF",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 F u0 p3 c0 {10,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.25422082, 0.0933752557, -0.000115708027, 6.9488406e-08, -1.63735338e-11, -226062.833, 15.8432442], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[18.9860579, 0.0274288714, -1.82598966e-05, 5.50394991e-09, -6.22660805e-13, -229458.248, -65.123439], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 47,
    label = "PF5acylF",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 F u0 p3 c0 {13,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.41976525, 0.113760003, -0.000133477556, 7.50063399e-08, -1.64264059e-11, -276949.504, 14.7488616], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[23.5117104, 0.0348460341, -2.32873217e-05, 6.99999542e-09, -7.88272845e-13, -281440.583, -88.3710346], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 48,
    label = "PF6acylF",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 F u0 p3 c0 {16,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.44232971, 0.144679584, -0.000175005675, 1.012677e-07, -2.28602527e-11, -327223.073, 18.379], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[28.4893061, 0.0416459612, -2.81866647e-05, 8.54264275e-09, -9.67559084e-13, -332890.182, -113.395597], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 49,
    label = "PF7acylF",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 C u0 p0 c0 {16,S} {20,S} {21,S} {22,S}
20 F u0 p3 c0 {19,S}
21 F u0 p3 c0 {19,S}
22 F u0 p3 c0 {19,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95185531, 0.150577909, -0.000162686464, 8.16761089e-08, -1.54306675e-11, -377814.322, 7.90582552], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[32.5826703, 0.0503948873, -3.39222884e-05, 1.01735631e-08, -1.14009051e-12, -384257.496, -133.806366], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 50,
    label = "PF2alkane",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6 F u0 p3 c0 {5,S}
7 F u0 p3 c0 {5,S}
8 F u0 p3 c0 {5,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.56503771, 0.0510909623, -5.07167534e-05, 1.88993955e-08, -7.73770882e-13, -164755.649, 18.955643], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[17.0284831, 0.00464174937, -1.92155485e-06, 3.37538839e-10, -2.13452416e-14, -168769.576, -59.8112608], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 51,
    label = "PF3alkane",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  F u0 p3 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 F u0 p3 c0 {8,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.21204618, 0.0707962204, -7.58979976e-05, 3.79739567e-08, -7.13845076e-12, -213916.905, 16.2928052], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[15.7053265, 0.0236894225, -1.5537286e-05, 4.59980592e-09, -5.11493938e-13, -216958.877, -50.5210536], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 52,
    label = "PF4alkane",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  F u0 p3 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12 F u0 p3 c0 {11,S}
13 F u0 p3 c0 {11,S}
14 F u0 p3 c0 {11,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.11540367, 0.0995106489, -0.000115727606, 6.41343664e-08, -1.37969286e-11, -264186.599, 15.7256443], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[20.8226936, 0.0302775613, -2.02720823e-05, 6.09342301e-09, -6.85710742e-13, -268207.86, -75.9252339], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 53,
    label = "PF5alkane",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  F u0 p3 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12 F u0 p3 c0 {11,S}
13 F u0 p3 c0 {11,S}
14 C u0 p0 c0 {11,S} {15,S} {16,S} {17,S}
15 F u0 p3 c0 {14,S}
16 F u0 p3 c0 {14,S}
17 F u0 p3 c0 {14,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.58862868, 0.114771074, -0.000116963499, 5.2687304e-08, -8.14236355e-12, -314931.715, 13.1166721], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[25.7676556, 0.0379427763, -2.55527671e-05, 7.63462551e-09, -8.51146375e-13, -320361.91, -102.680687], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 54,
    label = "PF6alkane",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  F u0 p3 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12 F u0 p3 c0 {11,S}
13 F u0 p3 c0 {11,S}
14 C u0 p0 c0 {11,S} {15,S} {16,S} {17,S}
15 F u0 p3 c0 {14,S}
16 F u0 p3 c0 {14,S}
17 C u0 p0 c0 {14,S} {18,S} {19,S} {20,S}
18 F u0 p3 c0 {17,S}
19 F u0 p3 c0 {17,S}
20 F u0 p3 c0 {17,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55697233, 0.132202771, -0.000130608696, 5.61406902e-08, -7.91156464e-12, -365372.728, 9.79369696], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.6299317, 0.0471328144, -3.18365831e-05, 9.51449601e-09, -1.06048636e-12, -371548.414, -120.798731], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 55,
    label = "PF7alkane",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  F u0 p3 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12 F u0 p3 c0 {11,S}
13 F u0 p3 c0 {11,S}
14 C u0 p0 c0 {11,S} {15,S} {16,S} {17,S}
15 F u0 p3 c0 {14,S}
16 F u0 p3 c0 {14,S}
17 C u0 p0 c0 {14,S} {18,S} {19,S} {20,S}
18 F u0 p3 c0 {17,S}
19 F u0 p3 c0 {17,S}
20 C u0 p0 c0 {17,S} {21,S} {22,S} {23,S}
21 F u0 p3 c0 {20,S}
22 F u0 p3 c0 {20,S}
23 F u0 p3 c0 {20,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00233183, 0.153020544, -0.00015194596, 6.67190934e-08, -9.9991825e-12, -415750.321, 6.13965989], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[32.9390649, 0.0575194959, -3.90632132e-05, 1.17098124e-08, -1.30833318e-12, -422549.962, -138.524821], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 56,
    label = "PF8alkane",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  F u0 p3 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12 F u0 p3 c0 {11,S}
13 F u0 p3 c0 {11,S}
14 C u0 p0 c0 {11,S} {15,S} {16,S} {17,S}
15 F u0 p3 c0 {14,S}
16 F u0 p3 c0 {14,S}
17 C u0 p0 c0 {14,S} {18,S} {19,S} {20,S}
18 F u0 p3 c0 {17,S}
19 F u0 p3 c0 {17,S}
20 C u0 p0 c0 {17,S} {21,S} {22,S} {23,S}
21 F u0 p3 c0 {20,S}
22 F u0 p3 c0 {20,S}
23 C u0 p0 c0 {20,S} {24,S} {25,S} {26,S}
24 F u0 p3 c0 {23,S}
25 F u0 p3 c0 {23,S}
26 F u0 p3 c0 {23,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.3438849, 0.175325574, -0.000178438142, 8.32372072e-08, -1.42499633e-11, -466150.887, 5.24518987], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[35.4074357, 0.0694732072, -4.72623461e-05, 1.41885133e-08, -1.58824895e-12, -473283.689, -149.218945], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 57,
    label = "PF2-1H",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 F u0 p3 c0 {4,S}
8 H u0 p0 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.28142439, 0.0464767776, -4.94027096e-05, 2.56988808e-08, -5.20798227e-12, -135773.646, 20.1209818], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[9.25586783, 0.0176883768, -1.08841678e-05, 3.12922591e-09, -3.42911768e-13, -137524.004, -19.1284414], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 58,
    label = "PF3-1H",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {11,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 F u0 p3 c0 {7,S}
11 H u0 p0 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.26945416, 0.0613300054, -5.66619365e-05, 2.2868119e-08, -2.84194054e-12, -186084.005, 17.1585173], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[13.5742296, 0.0250650134, -1.56956135e-05, 4.51134696e-09, -4.91275031e-13, -188792.666, -39.6190171], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 59,
    label = "PF4-1H",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {14,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 F u0 p3 c0 {10,S}
14 H u0 p0 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.74838132, 0.0935559421, -0.000103661488, 5.48782178e-08, -1.12180522e-11, -236308.995, 18.1078275], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[18.9617029, 0.0313679588, -2.03774674e-05, 6.02084031e-09, -6.70033585e-13, -240084.925, -66.6028245], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 60,
    label = "PF5-1H",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {17,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 F u0 p3 c0 {13,S}
17 H u0 p0 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.08704195, 0.102668957, -9.20972868e-05, 3.27591192e-08, -2.37842647e-12, -287256.201, 12.002133], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[23.6588967, 0.0394031209, -2.5730908e-05, 7.53644998e-09, -8.28155002e-13, -292321.651, -92.0005706], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 61,
    label = "PF6-1H",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {20,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 F u0 p3 c0 {16,S}
20 H u0 p0 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7068198, 0.122404024, -0.00011089624, 4.08570763e-08, -3.62420345e-12, -337664.654, 8.90415366], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[27.3017896, 0.0490501033, -3.24042976e-05, 9.55507331e-09, -1.05519236e-12, -343434.946, -110.184426], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 62,
    label = "PF7-1H",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {23,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 C u0 p0 c0 {16,S} {20,S} {21,S} {22,S}
20 F u0 p3 c0 {19,S}
21 F u0 p3 c0 {19,S}
22 F u0 p3 c0 {19,S}
23 H u0 p0 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.12316533, 0.143706623, -0.000133813522, 5.3143776e-08, -6.30836457e-12, -388053.339, 6.56105592], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[30.4841491, 0.0596212707, -3.97233675e-05, 1.17755895e-08, -1.30596366e-12, -394393.465, -125.955098], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 63,
    label = "PF2ene",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,D} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.99308667, 0.0384734406, -5.32322754e-05, 3.9212272e-08, -1.19302747e-11, -83002.1485, 15.3134111], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[11.4178412, 0.00459161071, -1.77520928e-06, 3.00598731e-10, -1.8592126e-14, -85292.7617, -31.6445526], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 64,
    label = "PF3ene",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,D} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7 F u0 p3 c0 {6,S}
8 F u0 p3 c0 {6,S}
9 F u0 p3 c0 {6,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.140993, 0.0523824217, -5.79499942e-05, 3.12800442e-08, -6.61660375e-12, -139966.932, 13.108987], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[12.2243588, 0.0189048419, -1.20174494e-05, 3.51423106e-09, -3.89121284e-13, -141926.4, -31.4269731], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 65,
    label = "PF4ene",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,D} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 F u0 p3 c0 {9,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.99566707, 0.0793943304, -9.42869609e-05, 5.46575682e-08, -1.24717803e-11, -191032.682, 13.945758], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[16.9360032, 0.0256594527, -1.67243444e-05, 4.97562387e-09, -5.57910898e-13, -193922.072, -53.8149221], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 66,
    label = "PF5ene",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,D} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 F u0 p3 c0 {12,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.11049368, 0.0949162206, -0.000105116848, 5.59828297e-08, -1.15862149e-11, -242885.12, 9.13903994], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[21.0861914, 0.0331143649, -2.1565467e-05, 6.3828442e-09, -7.11452279e-13, -246585.306, -74.2841224], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 67,
    label = "PF6ene",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,D} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 C u0 p0 c0 {12,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}
18 F u0 p3 c0 {15,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.4501589, 0.13139897, -0.000157260541, 9.05559401e-08, -2.03944483e-11, -292924.086, 15.1537338], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[26.5405324, 0.0396349588, -2.65107485e-05, 7.98689471e-09, -9.01557684e-13, -297972.035, -102.217764], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 68,
    label = "PF7ene",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,D} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 C u0 p0 c0 {12,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 F u0 p3 c0 {18,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60056166, 0.146718124, -0.000164356866, 8.68181733e-08, -1.75960857e-11, -343374.371, 10.1878417], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[31.3772154, 0.0468509557, -3.14152843e-05, 9.42989934e-09, -1.05887889e-12, -349491.674, -126.628318], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 69,
    label = "PF2ol",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {9,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6 F u0 p3 c0 {5,S}
7 F u0 p3 c0 {5,S}
8 F u0 p3 c0 {5,S}
9 H u0 p0 c0 {1,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.06775152, 0.0593961922, -7.28684089e-05, 4.41304067e-08, -1.05247875e-11, -162077.898, 20.0290221], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[11.3850383, 0.0182954015, -1.14697572e-05, 3.36632859e-09, -3.75857002e-13, -164149.773, -29.7880116], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 70,
    label = "PF3ol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  F u0 p3 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 F u0 p3 c0 {8,S}
12 H u0 p0 c0 {1,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.3079003, 0.0778932456, -8.65690929e-05, 4.64063738e-08, -9.66687228e-12, -212078.415, 20.2631539], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[15.3869021, 0.0265421122, -1.69897034e-05, 4.98498775e-09, -5.52744197e-13, -215142.459, -48.9011097], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 71,
    label = "PF4ol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  F u0 p3 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12 F u0 p3 c0 {11,S}
13 F u0 p3 c0 {11,S}
14 F u0 p3 c0 {11,S}
15 H u0 p0 c0 {1,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.05798011, 0.109595066, -0.000133212446, 7.84471965e-08, -1.81163149e-11, -262400.358, 19.7249952], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[20.8598033, 0.0328044795, -2.16516254e-05, 6.49002213e-09, -7.31197872e-13, -266481.558, -76.4115319], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 72,
    label = "PF5ol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {18,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  F u0 p3 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12 F u0 p3 c0 {11,S}
13 F u0 p3 c0 {11,S}
14 C u0 p0 c0 {11,S} {15,S} {16,S} {17,S}
15 F u0 p3 c0 {14,S}
16 F u0 p3 c0 {14,S}
17 F u0 p3 c0 {14,S}
18 H u0 p0 c0 {1,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1301134, 0.113315999, -0.000110287162, 4.67869807e-08, -6.41510813e-12, -314120.005, 11.0930781], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[25.3373894, 0.0411618598, -2.70684019e-05, 7.98277224e-09, -8.8279731e-13, -319395.208, -100.212933], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 73,
    label = "PF6ol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {21,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  F u0 p3 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12 F u0 p3 c0 {11,S}
13 F u0 p3 c0 {11,S}
14 C u0 p0 c0 {11,S} {15,S} {16,S} {17,S}
15 F u0 p3 c0 {14,S}
16 F u0 p3 c0 {14,S}
17 C u0 p0 c0 {14,S} {18,S} {19,S} {20,S}
18 F u0 p3 c0 {17,S}
19 F u0 p3 c0 {17,S}
20 F u0 p3 c0 {17,S}
21 H u0 p0 c0 {1,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53522974, 0.134443651, -0.00013155661, 5.64393321e-08, -7.98432775e-12, -364504.929, 8.49569473], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.5154246, 0.0496006359, -3.29087341e-05, 9.75184584e-09, -1.08189729e-12, -370654.856, -121.613168], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 74,
    label = "PF7ol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {24,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  F u0 p3 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12 F u0 p3 c0 {11,S}
13 F u0 p3 c0 {11,S}
14 C u0 p0 c0 {11,S} {15,S} {16,S} {17,S}
15 F u0 p3 c0 {14,S}
16 F u0 p3 c0 {14,S}
17 C u0 p0 c0 {14,S} {18,S} {19,S} {20,S}
18 F u0 p3 c0 {17,S}
19 F u0 p3 c0 {17,S}
20 C u0 p0 c0 {17,S} {21,S} {22,S} {23,S}
21 F u0 p3 c0 {20,S}
22 F u0 p3 c0 {20,S}
23 F u0 p3 c0 {20,S}
24 H u0 p0 c0 {1,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94653596, 0.155827296, -0.000154597897, 6.87334589e-08, -1.0641693e-11, -414890.619, 6.20787615], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[32.8178635, 0.0598982212, -4.00386394e-05, 1.19168559e-08, -1.32660123e-12, -421642.696, -137.968649], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 75,
    label = "PF2diol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  O u0 p2 c0 {2,S} {10,S}
4  F u0 p3 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  F u0 p3 c0 {5,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.626147587, 0.0632700011, -7.5293593e-05, 4.44355274e-08, -1.03236363e-11, -159302.802, 21.3795465], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[11.7445177, 0.0199815618, -1.21384958e-05, 3.51717032e-09, -3.90307332e-13, -161585.729, -32.5564225], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 76,
    label = "PF3diol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  O u0 p2 c0 {2,S} {13,S}
4  F u0 p3 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 F u0 p3 c0 {8,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.613774712, 0.0956046014, -0.000119876779, 7.3693266e-08, -1.77889057e-11, -209826.785, 26.586582], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[16.2094155, 0.0279402291, -1.78228038e-05, 5.28567101e-09, -5.9410411e-13, -213172.843, -54.4826833], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 77,
    label = "PF4diol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  O u0 p2 c0 {2,S} {16,S}
4  F u0 p3 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12 F u0 p3 c0 {11,S}
13 F u0 p3 c0 {11,S}
14 F u0 p3 c0 {11,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.464227325, 0.111941742, -0.000129062405, 7.1895118e-08, -1.56438328e-11, -259989.902, 21.7126505], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[20.8234506, 0.035993138, -2.33719317e-05, 6.9230913e-09, -7.72898319e-13, -264336.161, -77.8809052], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 78,
    label = "PF5diol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {18,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  O u0 p2 c0 {2,S} {19,S}
4  F u0 p3 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12 F u0 p3 c0 {11,S}
13 F u0 p3 c0 {11,S}
14 C u0 p0 c0 {11,S} {15,S} {16,S} {17,S}
15 F u0 p3 c0 {14,S}
16 F u0 p3 c0 {14,S}
17 F u0 p3 c0 {14,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.8188827, 0.117338595, -0.000115094339, 5.04358797e-08, -7.52518066e-12, -313262.914, 11.6875303], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[25.1137198, 0.0438459472, -2.83854186e-05, 8.316633e-09, -9.1704412e-13, -318506.216, -99.793846], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 79,
    label = "PF6diol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {21,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  O u0 p2 c0 {2,S} {22,S}
4  F u0 p3 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12 F u0 p3 c0 {11,S}
13 F u0 p3 c0 {11,S}
14 C u0 p0 c0 {11,S} {15,S} {16,S} {17,S}
15 F u0 p3 c0 {14,S}
16 F u0 p3 c0 {14,S}
17 C u0 p0 c0 {14,S} {18,S} {19,S} {20,S}
18 F u0 p3 c0 {17,S}
19 F u0 p3 c0 {17,S}
20 F u0 p3 c0 {17,S}
21 H u0 p0 c0 {1,S}
22 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5528715, 0.13592943, -0.000130730986, 5.51903234e-08, -7.58134864e-12, -363662.867, 8.25038566], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.330079, 0.0521164633, -3.39553309e-05, 9.96908369e-09, -1.10000456e-12, -369783.102, -120.933706], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 80,
    label = "PF7diol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {24,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  O u0 p2 c0 {2,S} {25,S}
4  F u0 p3 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12 F u0 p3 c0 {11,S}
13 F u0 p3 c0 {11,S}
14 C u0 p0 c0 {11,S} {15,S} {16,S} {17,S}
15 F u0 p3 c0 {14,S}
16 F u0 p3 c0 {14,S}
17 C u0 p0 c0 {14,S} {18,S} {19,S} {20,S}
18 F u0 p3 c0 {17,S}
19 F u0 p3 c0 {17,S}
20 C u0 p0 c0 {17,S} {21,S} {22,S} {23,S}
21 F u0 p3 c0 {20,S}
22 F u0 p3 c0 {20,S}
23 F u0 p3 c0 {20,S}
24 H u0 p0 c0 {1,S}
25 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8088088, 0.158049514, -0.000155207526, 6.87337707e-08, -1.0633549e-11, -414024.066, 6.08139607], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[32.4960468, 0.0627076051, -4.13052283e-05, 1.22059488e-08, -1.35335441e-12, -420731.865, -137.169705], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 81,
    label = "PF2lactone",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.75293689, 0.03224099, -3.11030134e-05, 1.32937463e-08, -1.83699789e-12, -71257.2383, 17.7668708], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[8.27246204, 0.0110513744, -6.65131771e-06, 1.88110086e-09, -2.05957792e-13, -72805.5675, -14.9081906], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 82,
    label = "PF3lactone",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7 F u0 p3 c0 {6,S}
8 F u0 p3 c0 {6,S}
9 F u0 p3 c0 {6,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.30440608, 0.0614056255, -7.41030397e-05, 4.38356294e-08, -1.02116572e-11, -124777.332, 20.9335746], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[12.0691761, 0.0193090834, -1.24020337e-05, 3.66416336e-09, -4.09425231e-13, -126978.413, -31.2408526], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 83,
    label = "PF4lactone",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 F u0 p3 c0 {9,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.25387422, 0.0787660405, -8.79789962e-05, 4.70904317e-08, -9.76692521e-12, -175519.719, 17.5959183], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[16.6742245, 0.0263017794, -1.71083148e-05, 5.06045078e-09, -5.63715004e-13, -178664.646, -53.2782211], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 84,
    label = "PF5lactone",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 F u0 p3 c0 {12,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.10134521, 0.109827547, -0.000128919373, 7.24930957e-08, -1.5876485e-11, -227357.82, 21.7428481], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[21.5717, 0.0332852829, -2.21147107e-05, 6.62914342e-09, -7.45285837e-13, -231718.849, -78.3495699], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 85,
    label = "PF6lactone",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 C u0 p0 c0 {12,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}
18 F u0 p3 c0 {15,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.25428539, 0.124176059, -0.000131921989, 6.42202616e-08, -1.14978072e-11, -277815.812, 16.8474434], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[26.598234, 0.0405502738, -2.71083244e-05, 8.09449437e-09, -9.03867649e-13, -283372.103, -104.035539], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 86,
    label = "PF7lactone",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 C u0 p0 c0 {12,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 F u0 p3 c0 {18,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.52038933, 0.138781633, -0.000137753702, 5.96556063e-08, -8.50741884e-12, -328294.106, 10.7722173], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[31.2796454, 0.0480596944, -3.21434218e-05, 9.56383806e-09, -1.06324811e-12, -334861.711, -128.228918], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 87,
    label = "PF8lactone",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 C u0 p0 c0 {12,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 F u0 p3 c0 {21,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.22281155, 0.158062144, -0.000156078649, 6.78240298e-08, -9.89628403e-12, -378714.274, 7.59704869], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[34.5302165, 0.0585539932, -3.93986278e-05, 1.17588182e-08, -1.31034847e-12, -385861.828, -144.049028], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 88,
    label = "PF2acidr",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {7,S}
4 C u1 p0 c0 {2,S} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.73183993, 0.0312637435, -2.61724834e-05, 9.86119226e-09, -1.18213277e-12, -75182.5361, 15.007284], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[6.92915274, 0.0178264509, -1.10444825e-05, 3.12781695e-09, -3.36778605e-13, -76189.5966, -6.08031369], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 89,
    label = "PF3acidr",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {10,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u1 p0 c0 {4,S} {8,S} {9,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67504217, 0.0464026959, -3.94759292e-05, 1.44014833e-08, -1.39109268e-12, -123516.294, 12.758462], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[11.2750302, 0.022629669, -1.3756777e-05, 3.88230731e-09, -4.18030036e-13, -125367.638, -25.5638187], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 90,
    label = "PF4acidr",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {13,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u1 p0 c0 {7,S} {11,S} {12,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95023637, 0.0741729995, -7.99922944e-05, 4.23896273e-08, -8.83576238e-12, -174980.279, 10.7131936], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[16.2880311, 0.0289080563, -1.82242333e-05, 5.29715576e-09, -5.84203467e-13, -177652.15, -49.8310932], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 91,
    label = "PF5acidr",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {16,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u1 p0 c0 {10,S} {14,S} {15,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55514034, 0.102607729, -0.000118933471, 6.77788814e-08, -1.52612528e-11, -226079.406, 11.389958], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[21.0425334, 0.0356398417, -2.29541672e-05, 6.77436318e-09, -7.55544392e-13, -229725.969, -73.7220261], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 92,
    label = "PF6acidr",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {19,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u1 p0 c0 {13,S} {17,S} {18,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.36091384, 0.126884087, -0.000145054886, 8.02847704e-08, -1.73998558e-11, -276414.257, 11.9031776], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[25.9412373, 0.0426692469, -2.78923074e-05, 8.28283838e-09, -9.25986214e-13, -281235.645, -98.5604437], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 93,
    label = "PF7acidr",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {22,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 C u1 p0 c0 {16,S} {20,S} {21,S}
20 F u0 p3 c0 {19,S}
21 F u0 p3 c0 {19,S}
22 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.5161089, 0.142482289, -0.000153270792, 7.79317927e-08, -1.51215516e-11, -326886.069, 6.49110861], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[30.5609956, 0.0503172182, -3.30449e-05, 9.79567381e-09, -1.09114083e-12, -332695.77, -122.164033], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 94,
    label = "PF8acidr",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {25,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 C u0 p0 c0 {16,S} {20,S} {21,S} {22,S}
20 F u0 p3 c0 {19,S}
21 F u0 p3 c0 {19,S}
22 C u1 p0 c0 {19,S} {23,S} {24,S}
23 F u0 p3 c0 {22,S}
24 F u0 p3 c0 {22,S}
25 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.93481939, 0.163969914, -0.000175373325, 8.80348249e-08, -1.67332417e-11, -377294.118, 4.31738398], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[35.276721, 0.0574655577, -3.79116673e-05, 1.12569703e-08, -1.25459069e-12, -384105.66, -145.780565], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 95,
    label = "PF2acylFr",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 C u1 p0 c0 {2,S} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.82584473, 0.0315503268, -3.54239151e-05, 2.03477361e-08, -4.73436188e-12, -75302.5197, 14.0071292], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[7.32262579, 0.0135933456, -8.53365759e-06, 2.4510407e-09, -2.67723777e-13, -76203.3831, -7.69477579], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 96,
    label = "PF3acylFr",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 C u1 p0 c0 {4,S} {8,S} {9,S}
8 F u0 p3 c0 {7,S}
9 F u0 p3 c0 {7,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.48200726, 0.0568110684, -6.78479625e-05, 3.96415234e-08, -9.12048789e-12, -122518.012, 17.0158983], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[12.4438169, 0.0181957526, -1.17728726e-05, 3.49005269e-09, -3.90600867e-13, -124571.97, -31.3520552], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 97,
    label = "PF4acylFr",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u1 p0 c0 {7,S} {11,S} {12,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.13452345, 0.0819773762, -0.00010323786, 6.34981661e-08, -1.53593513e-11, -173962.105, 13.5165974], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[17.3289726, 0.0245873227, -1.62343944e-05, 4.88359895e-09, -5.5264529e-13, -176770.382, -54.8103504], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 98,
    label = "PF5acylFr",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u1 p0 c0 {10,S} {14,S} {15,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.09227395, 0.112866259, -0.000145027605, 9.02495167e-08, -2.19999883e-11, -224060.565, 17.0855028], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[22.1053904, 0.0315592872, -2.11853884e-05, 6.43353261e-09, -7.32365765e-13, -228000.463, -79.1525888], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 99,
    label = "PF6acylFr",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u1 p0 c0 {13,S} {17,S} {18,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.01513382, 0.137083682, -0.00017119683, 1.02803268e-07, -2.41500052e-11, -274441.966, 17.5360345], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[27.1421323, 0.0384548633, -2.60723653e-05, 7.93280098e-09, -9.02182171e-13, -279561.325, -104.157002], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 100,
    label = "PF7acylFr",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 C u1 p0 c0 {16,S} {20,S} {21,S}
20 F u0 p3 c0 {19,S}
21 F u0 p3 c0 {19,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.73863902, 0.137423672, -0.000140275517, 6.42313212e-08, -1.03551505e-11, -324958.672, 6.17179947], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[31.5860477, 0.0475840206, -3.18410133e-05, 9.49163521e-09, -1.05772473e-12, -331205.654, -127.738924], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 101,
    label = "PFvinylr",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 F u0 p3 c0 {2,S}
4 C u1 p0 c0 {2,D} {5,S}
5 F u0 p3 c0 {4,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.4146424, 0.0268291562, -3.39283388e-05, 2.31906358e-08, -6.71131007e-12, -29099.0246, 15.3576825], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[9.28002368, 0.00372628116, -1.44027826e-06, 2.43838247e-10, -1.50793717e-14, -30844.8687, -19.2329718], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 102,
    label = "PFallylr",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,D} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 C u1 p0 c0 {4,S} {7,S} {8,S}
7 F u0 p3 c0 {6,S}
8 F u0 p3 c0 {6,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.99602149, 0.0390221301, -3.89048133e-05, 1.85122236e-08, -3.35674971e-12, -89721.1258, 6.00909715], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[11.2903907, 0.0171351129, -1.10099766e-05, 3.20612517e-09, -3.52839963e-13, -91144.5226, -25.1802104], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 103,
    label = "PF4ener",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,D} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u1 p0 c0 {6,S} {10,S} {11,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.19080346, 0.067838694, -8.18445172e-05, 4.8753146e-08, -1.14918199e-11, -138169.787, 9.35117837], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[15.5746698, 0.0226845736, -1.46853539e-05, 4.36171539e-09, -4.892985e-13, -140465.627, -45.6647323], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 104,
    label = "PF5ener",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,D} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u1 p0 c0 {9,S} {13,S} {14,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03417309, 0.0912898708, -0.000108626179, 6.32007928e-08, -1.44940426e-11, -190191.236, 10.2670177], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[19.8909222, 0.0298795922, -1.95358378e-05, 5.82395025e-09, -6.54011493e-13, -193463.421, -66.7368104], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 105,
    label = "PF6ener",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,D} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 C u1 p0 c0 {12,S} {16,S} {17,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.34119082, 0.128646217, -0.000163917645, 1.01183615e-07, -2.44841226e-11, -240300.569, 16.4597353], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[25.1742213, 0.0365086313, -2.45030708e-05, 7.43510134e-09, -8.45628305e-13, -244826.902, -93.4950722], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 106,
    label = "PF7ener",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,D} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 C u0 p0 c0 {12,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}
18 C u1 p0 c0 {15,S} {19,S} {20,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.09517255, 0.146484793, -0.000176336465, 1.01907163e-07, -2.30194619e-11, -290468.787, 13.0796072], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[30.083294, 0.0435053006, -2.93267174e-05, 8.87365806e-09, -1.00433419e-12, -296115.061, -118.365726], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 107,
    label = "PF2alkylr",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 F u0 p3 c0 {4,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.30899358, 0.0422577504, -4.92651847e-05, 2.7897856e-08, -6.19183848e-12, -110540.861, 16.5044151], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[9.9123955, 0.0135437838, -8.74369637e-06, 2.58317152e-09, -2.88077635e-13, -112146.523, -20.6025142], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 108,
    label = "PF3alkylr",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 F u0 p3 c0 {7,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.43479501, 0.0668059801, -7.97859718e-05, 4.60161438e-08, -1.03906265e-11, -161635.821, 16.3759957], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[14.6120761, 0.0203364479, -1.34410617e-05, 4.0257959e-09, -4.52937528e-13, -164183.257, -42.9322446], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 109,
    label = "PF4alkylr",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 F u0 p3 c0 {10,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56635367, 0.0850007952, -9.75730239e-05, 5.37039204e-08, -1.15093408e-11, -212487.839, 11.6483023], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[19.143041, 0.0273703683, -1.81418675e-05, 5.42613873e-09, -6.08976045e-13, -215836.992, -64.6692907], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 110,
    label = "PF5alkylr",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 F u0 p3 c0 {13,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.32109559, 0.114425653, -0.000131093287, 7.08475023e-08, -1.4741496e-11, -262211.936, 15.8513295], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[24.2718123, 0.0346268145, -2.34010727e-05, 7.05672098e-09, -7.94807841e-13, -267002.281, -92.049197], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 111,
    label = "PF6alkylr",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 F u0 p3 c0 {16,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.19757047, 0.138930211, -0.000158187975, 8.43850058e-08, -1.72301759e-11, -312550.149, 15.9373033], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.2288155, 0.0415713155, -2.82987601e-05, 8.55828082e-09, -9.6501597e-13, -318494.702, -117.16435], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 112,
    label = "PF7alkylr",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 C u0 p0 c0 {16,S} {20,S} {21,S} {22,S}
20 F u0 p3 c0 {19,S}
21 F u0 p3 c0 {19,S}
22 F u0 p3 c0 {19,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.36261609, 0.147456147, -0.000151855234, 7.0153564e-08, -1.14837017e-11, -363099.808, 6.84635227], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[33.2619613, 0.0504192766, -3.41406933e-05, 1.02377134e-08, -1.14486653e-12, -369807.702, -137.216411], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 113,
    label = "PF8alkylr",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 C u0 p0 c0 {16,S} {20,S} {21,S} {22,S}
20 F u0 p3 c0 {19,S}
21 F u0 p3 c0 {19,S}
22 C u0 p0 c0 {19,S} {23,S} {24,S} {25,S}
23 F u0 p3 c0 {22,S}
24 F u0 p3 c0 {22,S}
25 F u0 p3 c0 {22,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.58404937, 0.170058253, -0.000177530449, 8.4798177e-08, -1.48826085e-11, -413475.643, 4.84290967], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[36.4733387, 0.0609029469, -4.14002674e-05, 1.24465736e-08, -1.39517049e-12, -420773.593, -153.60494], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 114,
    label = "PF2alkyl(s)",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p1 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 F u0 p3 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.95647817, 0.034083685, -3.75768683e-05, 1.97827077e-08, -4.01060351e-12, -62947.6417, 17.5352764], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[8.25263035, 0.0114284629, -7.38811507e-06, 2.18625884e-09, -2.43837964e-13, -64333.3415, -13.472365], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 115,
    label = "PF3alkyl(s)",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p1 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
7 F u0 p3 c0 {6,S}
8 F u0 p3 c0 {6,S}
9 F u0 p3 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.35160602, 0.0562836531, -6.10577976e-05, 3.08377211e-08, -5.85662832e-12, -113614.981, 16.0533306], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[13.2418504, 0.0181546305, -1.2012196e-05, 3.57260818e-09, -3.98338793e-13, -116064.627, -37.8437919], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 116,
    label = "PF4alkyl(s)",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p1 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  F u0 p3 c0 {3,S}
5  F u0 p3 c0 {3,S}
6  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 F u0 p3 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.17478667, 0.0831667319, -0.000105823213, 6.55924281e-08, -1.59670719e-11, -164348.181, 11.8590709], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[17.6413362, 0.0243547559, -1.6186582e-05, 4.88889622e-09, -5.54744491e-13, -167194.202, -57.6972237], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 117,
    label = "PF5alkyl(s)",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p1 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  F u0 p3 c0 {3,S}
5  F u0 p3 c0 {3,S}
6  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 F u0 p3 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.07833612, 0.103764488, -0.000121404571, 6.78843203e-08, -1.47741299e-11, -215166.164, 12.512456], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[22.3946879, 0.0317643195, -2.13021762e-05, 6.41462937e-09, -7.23016827e-13, -219292.696, -81.9940852], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 118,
    label = "PF6alkyl(s)",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p1 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  F u0 p3 c0 {3,S}
5  F u0 p3 c0 {3,S}
6  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 C u0 p0 c0 {12,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}
18 F u0 p3 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.99842716, 0.138043382, -0.000173851179, 1.05366853e-07, -2.49874285e-11, -265481.914, 15.9205826], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[27.1739493, 0.0384334474, -2.6074508e-05, 7.94122658e-09, -9.04060434e-13, -270571.627, -105.809797], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 119,
    label = "PF7alkyl(s)",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p1 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  F u0 p3 c0 {3,S}
5  F u0 p3 c0 {3,S}
6  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 C u0 p0 c0 {12,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 F u0 p3 c0 {18,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68858738, 0.149327434, -0.000172302709, 9.42381125e-08, -1.99416393e-11, -315988.688, 8.69871566], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[31.9142261, 0.0457639556, -3.09661064e-05, 9.35278748e-09, -1.05507716e-12, -322100.77, -129.808444], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 120,
    label = "PF2COr",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 F u0 p3 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.17938295, 0.032927959, -3.71383959e-05, 2.05412407e-08, -4.4677301e-12, -74607.3571, 16.9440783], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[7.89952523, 0.0115343902, -7.27854318e-06, 2.12167246e-09, -2.34588118e-13, -75825.7356, -11.0240517], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 121,
    label = "PF3COr",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
7 F u0 p3 c0 {6,S}
8 F u0 p3 c0 {6,S}
9 F u0 p3 c0 {6,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54155563, 0.0512803861, -5.85647861e-05, 3.28836011e-08, -7.28698512e-12, -126512.283, 11.7010484], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[12.3006288, 0.0180939179, -1.15598204e-05, 3.3967817e-09, -3.77736373e-13, -128356.589, -31.0188724], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 122,
    label = "PF4COr",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u1 p0 c0 {1,D} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  F u0 p3 c0 {3,S}
5  F u0 p3 c0 {3,S}
6  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 F u0 p3 c0 {9,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92968225, 0.0774501917, -9.63876073e-05, 5.91002473e-08, -1.43055442e-11, -177520.995, 9.56743268], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[16.9321382, 0.0246789772, -1.60886998e-05, 4.80625169e-09, -5.41697616e-13, -180083.417, -52.9715536], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 123,
    label = "PF5COr",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u1 p0 c0 {1,D} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  F u0 p3 c0 {3,S}
5  F u0 p3 c0 {3,S}
6  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 F u0 p3 c0 {12,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78752542, 0.0998061455, -0.00011776235, 6.73030687e-08, -1.5090766e-11, -226902.718, 10.3251195], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[21.6424881, 0.0318592929, -2.10515685e-05, 6.30221216e-09, -7.08801378e-13, -230647.36, -76.6830036], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 124,
    label = "PF6COr",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u1 p0 c0 {1,D} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  F u0 p3 c0 {3,S}
5  F u0 p3 c0 {3,S}
6  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 C u0 p0 c0 {12,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}
18 F u0 p3 c0 {15,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.86340282, 0.119416735, -0.000140070134, 7.95607947e-08, -1.77321814e-11, -277427.243, 4.82194158], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[26.1387778, 0.0387225447, -2.56398123e-05, 7.68122328e-09, -8.6411593e-13, -281902.684, -98.9212718], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 125,
    label = "PF7COr",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u1 p0 c0 {1,D} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  F u0 p3 c0 {3,S}
5  F u0 p3 c0 {3,S}
6  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 C u0 p0 c0 {12,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 F u0 p3 c0 {18,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.77495665, 0.155866787, -0.000189410958, 1.10668194e-07, -2.53002344e-11, -327538.786, 13.0114804], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[31.3522627, 0.0458967614, -3.09647177e-05, 9.3765662e-09, -1.06212714e-12, -333471.208, -125.942302], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 126,
    label = "PF8COr",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u1 p0 c0 {1,D} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  F u0 p3 c0 {3,S}
5  F u0 p3 c0 {3,S}
6  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 C u0 p0 c0 {12,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 F u0 p3 c0 {21,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.2408365, 0.165956062, -0.000192976365, 1.08276057e-07, -2.38264605e-11, -378191.618, 1.96069643], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[34.6700558, 0.0550969817, -3.69744401e-05, 1.11325706e-08, -1.25503827e-12, -384420.352, -141.732724], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 127,
    label = "PF8acid2r",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {25,S}
4  C u1 p0 c0 {2,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 C u0 p0 c0 {12,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 F u0 p3 c0 {21,S}
25 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.49567106, 0.160250616, -0.000158736201, 7.12492746e-08, -1.13713189e-11, -384996.15, 6.58854933], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[33.0704668, 0.0645861479, -4.31915711e-05, 1.2854236e-08, -1.43123792e-12, -391642.845, -135.927001], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 128,
    label = "PF8acid3r",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {25,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u1 p0 c0 {4,S} {8,S} {9,S}
8  F u0 p3 c0 {7,S}
9  C u0 p0 c0 {7,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 C u0 p0 c0 {12,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 F u0 p3 c0 {21,S}
25 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.31368152, 0.158352375, -0.000159709715, 7.31922813e-08, -1.19596906e-11, -381631.616, 5.74275617], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[35.0815849, 0.0583425777, -3.8287744e-05, 1.13061169e-08, -1.25360356e-12, -388538.287, -142.635624], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 129,
    label = "PF8acid4r",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {25,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u1 p0 c0 {7,S} {11,S} {12,S}
11 F u0 p3 c0 {10,S}
12 C u0 p0 c0 {10,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 C u0 p0 c0 {12,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 F u0 p3 c0 {21,S}
25 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7529301, 0.17582076, -0.000206202407, 1.16921372e-07, -2.59880198e-11, -382718.809, 10.0851308], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[35.2870077, 0.0564896084, -3.74134172e-05, 1.12005372e-08, -1.25910081e-12, -389365.883, -143.749855], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 130,
    label = "PF8acid5r",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {25,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u1 p0 c0 {10,S} {14,S} {15,S}
14 F u0 p3 c0 {13,S}
15 C u0 p0 c0 {13,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 F u0 p3 c0 {21,S}
25 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.4048447, 0.173057946, -0.000204176408, 1.17158633e-07, -2.6441449e-11, -382439.17, 7.97819362], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[34.8682893, 0.0564754499, -3.72095867e-05, 1.11187005e-08, -1.2492865e-12, -388795.423, -140.308138], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 131,
    label = "PF8acid6r",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {25,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u1 p0 c0 {13,S} {17,S} {18,S}
17 F u0 p3 c0 {16,S}
18 C u0 p0 c0 {16,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 F u0 p3 c0 {21,S}
25 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.43877998, 0.159802003, -0.000167489538, 8.15684828e-08, -1.47954586e-11, -382525.737, 4.44197351], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[35.2214156, 0.0568950094, -3.74643721e-05, 1.11085877e-08, -1.23637211e-12, -389293.441, -143.297915], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 132,
    label = "PF8acid7r",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {25,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 C u1 p0 c0 {16,S} {20,S} {21,S}
20 F u0 p3 c0 {19,S}
21 C u0 p0 c0 {19,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 F u0 p3 c0 {21,S}
25 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.53408163, 0.169511876, -0.000192386829, 1.04950491e-07, -2.23155202e-11, -381788.145, 6.99934312], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[35.1375819, 0.056634416, -3.73754503e-05, 1.11461119e-08, -1.24856071e-12, -388385.672, -143.02899], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 133,
    label = "PF8alkane2r",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  F u0 p3 c0 {2,S}
5  C u1 p0 c0 {2,S} {6,S} {7,S}
6  F u0 p3 c0 {5,S}
7  C u0 p0 c0 {5,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 C u0 p0 c0 {16,S} {20,S} {21,S} {22,S}
20 F u0 p3 c0 {19,S}
21 F u0 p3 c0 {19,S}
22 C u0 p0 c0 {19,S} {23,S} {24,S} {25,S}
23 F u0 p3 c0 {22,S}
24 F u0 p3 c0 {22,S}
25 F u0 p3 c0 {22,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.93494222, 0.170243173, -0.000181357365, 8.86080053e-08, -1.59872357e-11, -418034.796, 4.46381176], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[38.0162756, 0.0562878392, -3.79793633e-05, 1.13926705e-08, -1.27590195e-12, -425569.563, -159.726999], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 134,
    label = "PF8alkane3r",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  F u0 p3 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u1 p0 c0 {5,S} {9,S} {10,S}
9  F u0 p3 c0 {8,S}
10 C u0 p0 c0 {8,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 C u0 p0 c0 {16,S} {20,S} {21,S} {22,S}
20 F u0 p3 c0 {19,S}
21 F u0 p3 c0 {19,S}
22 C u0 p0 c0 {19,S} {23,S} {24,S} {25,S}
23 F u0 p3 c0 {22,S}
24 F u0 p3 c0 {22,S}
25 F u0 p3 c0 {22,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.16397268, 0.158449503, -0.000151921001, 6.12613487e-08, -7.24272044e-12, -418807.805, 0.438152855], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[38.1422083, 0.056532391, -3.80390797e-05, 1.13358987e-08, -1.26031567e-12, -426503.243, -160.337307], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 135,
    label = "PF8alkane4r",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  F u0 p3 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 C u1 p0 c0 {8,S} {12,S} {13,S}
12 F u0 p3 c0 {11,S}
13 C u0 p0 c0 {11,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 C u0 p0 c0 {16,S} {20,S} {21,S} {22,S}
20 F u0 p3 c0 {19,S}
21 F u0 p3 c0 {19,S}
22 C u0 p0 c0 {19,S} {23,S} {24,S} {25,S}
23 F u0 p3 c0 {22,S}
24 F u0 p3 c0 {22,S}
25 F u0 p3 c0 {22,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.78859061, 0.17078536, -0.000180626807, 8.67141162e-08, -1.51408825e-11, -418680.608, 5.74398173], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[38.5496194, 0.0556330643, -3.77360925e-05, 1.13454594e-08, -1.27167316e-12, -426427.405, -162.106421], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 136,
    label = "PF7acylF2r",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u1 p0 c0 {2,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 C u0 p0 c0 {12,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 F u0 p3 c0 {18,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77881719, 0.143983797, -0.000157789386, 8.25004599e-08, -1.67680664e-11, -333408.726, 9.75642551], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[28.7482877, 0.0535314719, -3.6249233e-05, 1.08992476e-08, -1.22415248e-12, -338873.898, -113.063225], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 137,
    label = "PF7acylF3r",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u1 p0 c0 {4,S} {8,S} {9,S}
8  F u0 p3 c0 {7,S}
9  C u0 p0 c0 {7,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 C u0 p0 c0 {12,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 F u0 p3 c0 {18,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.41209093, 0.163713622, -0.000200560673, 1.1713958e-07, -2.66611318e-11, -329658.336, 19.7185986], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[32.3193797, 0.0454093429, -3.10915677e-05, 9.48505255e-09, -1.07871882e-12, -336106.038, -130.722422], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 138,
    label = "PF7acylF4r",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u1 p0 c0 {7,S} {11,S} {12,S}
11 F u0 p3 c0 {10,S}
12 C u0 p0 c0 {10,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 C u0 p0 c0 {12,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 F u0 p3 c0 {18,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.09559204, 0.133927709, -0.000150467903, 8.13683274e-08, -1.71525686e-11, -330501.217, 2.75467634], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[30.0161576, 0.0460232419, -3.02778946e-05, 9.01945063e-09, -1.00979814e-12, -335674.22, -114.592674], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 139,
    label = "PF7acylF5r",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u1 p0 c0 {10,S} {14,S} {15,S}
14 F u0 p3 c0 {13,S}
15 C u0 p0 c0 {13,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 F u0 p3 c0 {18,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.20412344, 0.154848158, -0.000190720953, 1.1336227e-07, -2.64089392e-11, -330145.889, 13.4249866], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[31.2272849, 0.0454205674, -3.05771504e-05, 9.26479e-09, -1.05083309e-12, -335883.773, -122.436832], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 140,
    label = "PF7acylF6r",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u1 p0 c0 {13,S} {17,S} {18,S}
17 F u0 p3 c0 {16,S}
18 C u0 p0 c0 {16,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 F u0 p3 c0 {18,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.8769569, 0.156966024, -0.000194429966, 1.16322825e-07, -2.72863518e-11, -329089.582, 13.7383483], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[31.1669922, 0.0458713155, -3.08860527e-05, 9.35898152e-09, -1.06174923e-12, -334850.861, -123.261077], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 141,
    label = "PF7ene1r",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u1 p0 c0 {1,S} {3,D}
3  C u0 p0 c0 {2,D} {4,S} {5,S}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12 F u0 p3 c0 {11,S}
13 F u0 p3 c0 {11,S}
14 C u0 p0 c0 {11,S} {15,S} {16,S} {17,S}
15 F u0 p3 c0 {14,S}
16 F u0 p3 c0 {14,S}
17 C u0 p0 c0 {14,S} {18,S} {19,S} {20,S}
18 F u0 p3 c0 {17,S}
19 F u0 p3 c0 {17,S}
20 F u0 p3 c0 {17,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.83212545, 0.140674078, -0.000153603041, 7.73076347e-08, -1.45450458e-11, -289355.862, 13.9579809], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[30.5354499, 0.0440298668, -2.98903539e-05, 9.00159601e-09, -1.01080767e-12, -295604.981, -123.236817], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 142,
    label = "PF7ene2r",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  F u0 p3 c0 {2,S}
4  C u1 p0 c0 {2,D} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12 F u0 p3 c0 {11,S}
13 F u0 p3 c0 {11,S}
14 C u0 p0 c0 {11,S} {15,S} {16,S} {17,S}
15 F u0 p3 c0 {14,S}
16 F u0 p3 c0 {14,S}
17 C u0 p0 c0 {14,S} {18,S} {19,S} {20,S}
18 F u0 p3 c0 {17,S}
19 F u0 p3 c0 {17,S}
20 F u0 p3 c0 {17,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.58818377, 0.148006191, -0.000172647863, 9.55360141e-08, -2.04741105e-11, -293127.113, 20.3663315], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.755056, 0.0440456678, -2.97675277e-05, 8.9894231e-09, -1.01420422e-12, -299195.836, -117.699287], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 143,
    label = "PF7ene3r",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,D} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u1 p0 c0 {4,S} {7,S} {8,S}
7  F u0 p3 c0 {6,S}
8  C u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12 F u0 p3 c0 {11,S}
13 F u0 p3 c0 {11,S}
14 C u0 p0 c0 {11,S} {15,S} {16,S} {17,S}
15 F u0 p3 c0 {14,S}
16 F u0 p3 c0 {14,S}
17 C u0 p0 c0 {14,S} {18,S} {19,S} {20,S}
18 F u0 p3 c0 {17,S}
19 F u0 p3 c0 {17,S}
20 F u0 p3 c0 {17,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.73947076, 0.131236632, -0.000137995703, 6.74899459e-08, -1.23319173e-11, -300432.251, 5.97746557], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.1353777, 0.0467356369, -3.08681596e-05, 9.1542164e-09, -1.01864311e-12, -305965.564, -114.989341], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 144,
    label = "PF7ene4r",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,D} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u1 p0 c0 {6,S} {10,S} {11,S}
10 F u0 p3 c0 {9,S}
11 C u0 p0 c0 {9,S} {12,S} {13,S} {14,S}
12 F u0 p3 c0 {11,S}
13 F u0 p3 c0 {11,S}
14 C u0 p0 c0 {11,S} {15,S} {16,S} {17,S}
15 F u0 p3 c0 {14,S}
16 F u0 p3 c0 {14,S}
17 C u0 p0 c0 {14,S} {18,S} {19,S} {20,S}
18 F u0 p3 c0 {17,S}
19 F u0 p3 c0 {17,S}
20 F u0 p3 c0 {17,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.4456423, 0.130647426, -0.000144550173, 7.62739401e-08, -1.55549477e-11, -295683.242, 5.57405896], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.2006831, 0.0448127352, -2.95763447e-05, 8.81019347e-09, -9.85379043e-13, -300893.524, -111.326649], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 145,
    label = "PF7ene5r",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,D} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u1 p0 c0 {9,S} {13,S} {14,S}
13 F u0 p3 c0 {12,S}
14 C u0 p0 c0 {12,S} {15,S} {16,S} {17,S}
15 F u0 p3 c0 {14,S}
16 F u0 p3 c0 {14,S}
17 C u0 p0 c0 {14,S} {18,S} {19,S} {20,S}
18 F u0 p3 c0 {17,S}
19 F u0 p3 c0 {17,S}
20 F u0 p3 c0 {17,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.5218746, 0.136452456, -0.000154882081, 8.3919787e-08, -1.76397646e-11, -296105.99, 9.19748248], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.6515982, 0.0444174726, -2.95554728e-05, 8.85262586e-09, -9.93952094e-13, -301556.13, -114.159885], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 146,
    label = "PF7ene6r",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,D} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 C u1 p0 c0 {12,S} {16,S} {17,S}
16 F u0 p3 c0 {15,S}
17 C u0 p0 c0 {15,S} {18,S} {19,S} {20,S}
18 F u0 p3 c0 {17,S}
19 F u0 p3 c0 {17,S}
20 F u0 p3 c0 {17,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9024842, 0.143515395, -0.000175940362, 1.04787285e-07, -2.45347653e-11, -294771.762, 10.3586484], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.2619314, 0.0438989399, -2.92476809e-05, 8.81349922e-09, -9.9665233e-13, -299934.718, -112.441359], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)
