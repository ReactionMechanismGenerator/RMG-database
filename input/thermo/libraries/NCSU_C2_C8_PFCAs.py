#!/usr/bin/env python
# encoding: utf-8

name = "NCSU_C2_C8_PFCAs"
shortDesc = "C2-C8 PFCA thermo library (Westmoreland, 2023)"
longDesc = """
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 

This library contains C/H/O/F/ chemistry
It is recommended for fluorinated hydrocarbons, specifically PFCAs and their degradation products. 
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(6000.0,'K')),
            NASAPolynomial(coeffs=[2.5, 0.0, 0.0, 0.0, 0.0, 25473.66, -0.44668285], Tmin=(6000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'GBR3M Atomic species',
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
        Cp0 = (26.342438367274774,'J/(mol*K)'),
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[2.6716339, -0.00017461853, 6.9066504e-08, -1.1953478e-11, 7.5236739e-16, 8787.4123, 3.9842568], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[2.93286575, 0.000826608026, -1.46402364e-07, 1.54100414e-11, -6.888048e-16, -813.065581, -1.02432865], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'GBR3M Permanent gases',
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[3.66096065, 0.000656365811, -1.41149627e-07, 2.05797935e-11, -1.29913436e-15, -1215.97718, 3.41536279], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[3.86166219, 0.000788367679, -1.8198294e-07, -9.1743656e-12, 2.65193472e-15, -1232.38655, 2.04119869], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[2.83853033, 0.00110741289, -2.94000209e-07, 4.20698729e-11, -2.4228989e-15, 3697.80808, 5.84494652], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'GBR3M  H/O/F species',
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[2.6770389, 0.0029731816, -7.7376889e-07, 9.4433514e-11, -4.2689991e-15, -29885.894, 6.88255], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[4.17228741, 0.00188117627, -3.46277286e-07, 1.94657549e-11, 1.76256905e-16, 31.0206839, 2.95767672], Tmin=(1000.0,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (5000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[4.57977305, 0.00405326003, -1.2984473e-06, 1.982114e-10, -1.13968792e-14, -18007.1775, 0.664970694], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[2.92491143, 0.000850523032, -1.58179777e-07, 1.17507204e-11, -1.43309132e-16, -33635.2481, 4.19018883], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[3.0484859, 0.0013517281, -4.8579405e-07, 7.8853644e-11, -4.6980746e-15, -14266.117, 6.0170977], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'GBR3M One-carbon species',
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[4.6365111, 0.0027414569, -9.9589759e-07, 1.6038666e-10, -9.1619857e-15, -49024.904, -1.9348955], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[5.39206152, 0.00411221455, -1.481949e-06, 2.3987546e-10, -1.43903104e-14, -23860.6717, -2.23529091], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[4.14879557, 0.00558144141, -1.99182194e-06, 3.15300327e-10, -1.85171887e-14, -16689.6104, 5.08764733], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'GBR3M 
cis_HOCOr         GBR3M C   1H   1O   2     G    200.000  2500.000  1000.      1
 5.31835901E+00 4.09513897E-03-1.45743318E-06 2.34001740E-10-1.39610583E-14    2
-2.29140632E+04-1.76489310E+00 2.91857836E+00 8.11744264E-03 1.06216106E-06    3
-7.89057499E-09 3.96849841E-12-2.25251756E+04 1.12426809E+01-2.12954245E+04    4
trans_HOCOr       GBR3M C   1H   1O   2     G    200.000  2500.000  1000.      1
 5.40551345E+00 3.91841122E-03-1.37264274E-06 2.18152683E-10-1.29266159E-14    2
-2.38714810E+04-2.21101524E+00 2.89476190E+00 8.72409710E-03-4.90387397E-07    3
-6.49000220E-09 3.51803859E-12-2.34113119E+04 1.12391388E+01-2.21734128E+04    4
cis_HOCOr         NCSU23C   1H   1O   2     G   200.000  2500.000 1000.00      1
 3.45741524E+00 7.35635873E-03-4.00649459E-06 1.05384208E-09-1.07701230E-13    2
-2.09504423E+04 8.07613754E+00 3.59618268E+00 4.79495678E-03 2.84510664E-06    3
-5.52022428E-09 2.03739841E-12-2.08778792E+04 7.90824791E+00                   4
trans_HOCOr       NCSU23C   1H   1O   2     G   200.000  2500.000 1000.00      1
 3.78970367E+00 6.77266730E-03-3.65939855E-06 9.62908607E-10-9.83594965E-14    2
-2.19322171E+04 6.21493856E+00 3.37372141E+00 4.88088925E-03 4.51182920E-06    3
-8.04028367E-09 3.04136535E-12-2.16712352E+04 9.11073931E+00                   4',
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[1.65326226, 0.0100263099, -3.31661238e-06, 5.36483138e-10, -3.14696758e-14, -10009.5936, 9.90506283], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'GBR3M 
HCOOr             NCSU23C   1H   1O   2     G   200.000  2500.000 1000.00      1
 3.76248908E+00 7.67867280E-03-4.12589556E-06 1.05829200E-09-1.05019503E-13    2
-1.54814392E+04 5.52866107E+00 2.76127438E+00 6.37915567E-03 5.77994402E-06    3
-1.08499770E-08 4.19814172E-12-1.50159775E+04 1.16850372E+01                   4',
    referenceType = "Theory",
)


entry(
    index = 16,
    label = "CF2s",
    molecule = 
"""
multiplicity 1
1 F u0 p3 c0 {2,S}
2 C u0 p1 c0 {1,S} {3,S}
3 F u0 p3 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[5.35787718, 0.00180622418, -7.80465045e-07, 1.47642691e-10, -9.44754424e-15, -25172.8166, -2.63410779], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'GBR3M 
** C1-F (and O) species ***',
    referenceType = "Theory",
)


entry(
    index = 17,
    label = "CF2t",
    molecule = 
"""
multiplicity 3
1 F u0 p3 c0 {2,S}
2 C u2 p0 c0 {1,S} {3,S}
3 F u0 p3 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[5.45344707, 0.00156561882, -6.08817038e-07, 1.03459271e-10, -6.41400747e-15, 3375.44779, -1.83921649], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[7.42981696, 0.00261728694, -1.02141596e-06, 1.73975666e-10, -1.08028191e-14, -59179.5501, -12.2816891], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 19,
    label = "CHF2",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 F u0 p3 c0 {1,S}
3 F u0 p3 c0 {1,S}
4 H u0 p0 c0 {1,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[5.5232112, 0.00421970092, -1.58435294e-06, 2.63969157e-10, -1.61337618e-14, -30894.516, -2.40335469], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[5.06948195, 0.00723193135, -2.64021025e-06, 4.30854708e-10, -2.59873096e-14, -56727.0077, -2.34590394], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[7.24609031, 0.00542386441, -2.02314394e-06, 3.34946402e-10, -2.04067524e-14, -86823.9019, -12.8982398], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[9.47336526, 0.00359407743, -1.40334012e-06, 2.39113889e-10, -1.48513407e-14, -115816.621, -24.9736848], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[5.01565891, 0.00195763376, -7.49685297e-07, 1.25610155e-10, -7.59885072e-15, -22978.5255, 0.369669039], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[6.81631709, 0.00316473302, -1.21776278e-06, 2.05582278e-10, -1.26893138e-14, -75537.4518, -9.52865117], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[6.13972159, 0.00792804091, -4.71368414e-06, 1.43546348e-09, -1.78081858e-13, -54824.6016, -4.89266668], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 26,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[5.50001605, 0.00662261862, -4.03433136e-06, 1.13531886e-09, -1.21388652e-13, -45103.1347, -1.16444208], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 27,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[4.3795147, 0.0113011606, -6.4374204e-06, 1.71357905e-09, -1.75182363e-13, -74045.135, 3.19271169], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 28,
    label = "PF2enylr",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[9.28002368, 0.00372628116, -1.44027826e-06, 2.43838247e-10, -1.50793717e-14, -30844.8687, -19.2329718], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'GBR3M Two-carbon species',
    referenceType = "Theory",
)


entry(
    index = 29,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[11.4178412, 0.00459161071, -1.77520928e-06, 3.00598731e-10, -1.8592126e-14, -85292.7617, -31.6445526], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'GBR3M 
PF2enylr          NC9/23C   2F   3          G    10.000  3000.000  585.58      1
 4.13560004E+00 1.66114290E-02-1.28781920E-05 4.41369218E-09-5.55306019E-13    2
-2.70226932E+04 7.25275999E+00 3.93832497E+00 3.57355305E-03 5.73687385E-05    3
-1.17513208E-07 6.94095470E-11-2.67529509E+04 1.02048692E+01                   4',
    referenceType = "Theory",
)


entry(
    index = 30,
    label = "PF2s",
    molecule = 
"""
multiplicity 1
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 C u0 p1 c0 {2,S} {6,S}
6 F u0 p3 c0 {5,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[8.25263035, 0.0114284629, -7.38811507e-06, 2.18625884e-09, -2.43837964e-13, -62651.6833, -13.472365], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23
PF2ene            NC9/23C   2F   4          G    10.000  3000.000  470.45      1
 5.38113095E+00 1.91825633E-02-1.42411855E-05 4.78498327E-09-5.96924706E-13    2
-8.10813584E+04 1.56447590E+00 3.86818146E+00 8.94980196E-03 9.20281064E-05    3
-2.50166340E-07 1.90343261E-10-8.06834166E+04 1.04391566E+01                   4',
    referenceType = "Theory",
)


entry(
    index = 31,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[9.9123955, 0.0135437838, -8.74369637e-06, 2.58317152e-09, -2.88077635e-13, -108638.882, -20.6025142], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 32,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[9.25586783, 0.0176883768, -1.08841678e-05, 3.12922591e-09, -3.42911768e-13, -134152.791, -19.1284414], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 33,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[17.0284831, 0.00464174937, -1.92155485e-06, 3.37538839e-10, -2.13452416e-14, -168769.576, -59.8112608], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'GBR3M',
    referenceType = "Theory",
)


entry(
    index = 34,
    label = "CF3COr",
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[7.89952523, 0.0115343902, -7.27854318e-06, 2.12167246e-09, -2.34588118e-13, -73463.1008, -11.0240517], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23
PF2alkane         NCSU23C   2F   6          G   200.000  2500.000 1000.00      1
 1.13971628E+01 1.62299297E-02-1.06589624E-05 3.19734531E-09-3.60928809E-13    2
-1.62471611E+05-3.03901205E+01 1.04896487E+00 5.66422483E-02-6.98067308E-05    3
 4.16487180E-08-9.72865373E-12-1.60352948E+05 1.97790708E+01                   4
 *****',
    referenceType = "Theory",
)


entry(
    index = 35,
    label = "rCF2CFO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 F u0 p3 c0 {1,S}
4 F u0 p3 c0 {1,S}
5 F u0 p3 c0 {2,S}
6 O u1 p2 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[7.32262579, 0.0135933456, -8.53365759e-06, 2.4510407e-09, -2.67723777e-13, -73906.0318, -7.69477579], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 36,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[9.20214968, 0.0140186914, -8.76705559e-06, 2.53090213e-09, -2.77332113e-13, -123462.18, -17.645425], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 37,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[8.27246204, 0.0110513744, -6.65131771e-06, 1.88110086e-09, -2.05957792e-13, -70563.8182, -14.9081906], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 38,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[8.04197402, 0.0134840166, -8.06640146e-06, 2.29446418e-09, -2.50685517e-13, -71789.1232, -12.4836212], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 39,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[7.27302862, 0.0153939852, -9.00768376e-06, 2.47339313e-09, -2.60504179e-13, -65680.9765, -7.96959414], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 40,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[9.16042693, 0.014565104, -9.34306887e-06, 2.74972343e-09, -3.05560104e-13, -93907.8104, -16.6976241], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 41,
    label = "rCF2COOH",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 C u0 p0 c0 {1,S} {5,S} {6,D}
3 F u0 p3 c0 {1,S}
4 F u0 p3 c0 {1,S}
5 O u0 p2 c0 {2,S} {7,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {5,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[6.92915274, 0.0178264509, -1.10444825e-05, 3.12781695e-09, -3.36778605e-13, -73537.2115, -6.08031369], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 42,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[8.41880929, 0.0184199668, -1.10398151e-05, 3.07796368e-09, -3.27998753e-13, -123547.69, -14.5059092], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 43,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[11.3850383, 0.0182954015, -1.14697572e-05, 3.36632859e-09, -3.75857002e-13, -160307.961, -29.7880116], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 44,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[11.7445177, 0.0199815618, -1.21384958e-05, 3.51717032e-09, -3.90307332e-13, -157234.256, -32.5564225], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 45,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[11.2903907, 0.0171351129, -1.10099766e-05, 3.20612517e-09, -3.52839963e-13, -88276.3021, -25.1802104], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23 Three-carbon species ',
    referenceType = "Theory",
)


entry(
    index = 46,
    label = "PF3-1ene",
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[12.2243588, 0.0189048419, -1.20174494e-05, 3.51423106e-09, -3.89121284e-13, -138453.26, -31.4269731], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 47,
    label = "PF3s",
    molecule = 
"""
multiplicity 1
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[13.2418504, 0.0181546305, -1.2012196e-05, 3.57260818e-09, -3.98338793e-13, -112761.858, -37.8437919], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 48,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[14.6120761, 0.0203364479, -1.34410617e-05, 4.0257959e-09, -4.52937528e-13, -160230.142, -42.9322446], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 49,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[13.5742296, 0.0250650134, -1.56956135e-05, 4.51134696e-09, -4.91275031e-13, -184363.61, -39.6190171], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 50,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[15.7053265, 0.0236894225, -1.5537286e-05, 4.59980592e-09, -5.11493938e-13, -212487.457, -50.5210536], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 51,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[12.3006288, 0.0180939179, -1.15598204e-05, 3.3967817e-09, -3.77736373e-13, -125031.033, -31.0188724], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23
 *****',
    referenceType = "Theory",
)


entry(
    index = 52,
    label = "rPF3acylF",
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[12.4438169, 0.0181957526, -1.17728726e-05, 3.49005269e-09, -3.90600867e-13, -121259.628, -31.3520552], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 53,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[14.0309788, 0.0206720088, -1.34806683e-05, 4.01747963e-09, -4.51335571e-13, -174083.338, -40.7834998], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 54,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[12.0691761, 0.0193090834, -1.24020337e-05, 3.66416336e-09, -4.09425231e-13, -123604.806, -31.2408526], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 55,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[15.3869021, 0.0265421122, -1.69897034e-05, 4.98498775e-09, -5.52744197e-13, -210278.066, -48.9011097], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 56,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[13.8492258, 0.0209197562, -1.36012772e-05, 4.04060373e-09, -4.52618169e-13, -145287.115, -38.5278697], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 57,
    label = "rPF3acid",
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[11.2750302, 0.022629669, -1.3756777e-05, 3.88230731e-09, -4.18030036e-13, -121602.934, -25.5638187], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 58,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[13.2974244, 0.024892241, -1.55944358e-05, 4.5123644e-09, -4.95981186e-13, -174647.787, -37.8521439], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 59,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[16.2094155, 0.0279402291, -1.78228038e-05, 5.28567101e-09, -5.9410411e-13, -207730.102, -54.4826833], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 60,
    label = "rPF4-1ene",
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[15.5746698, 0.0226845736, -1.46853539e-05, 4.36171539e-09, -4.892985e-13, -136398.153, -45.6647323], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = ' Four-carbon species',
    referenceType = "Theory",
)


entry(
    index = 61,
    label = "PF4-1ene",
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[16.9360032, 0.0256594527, -1.67243444e-05, 4.97562387e-09, -5.57910898e-13, -189327.195, -53.8149221], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 62,
    label = "PF4s",
    molecule = 
"""
multiplicity 1
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[17.6413362, 0.0243547559, -1.6186582e-05, 4.88889622e-09, -5.54744491e-13, -162658.066, -57.6972237], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 63,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[19.143041, 0.0273703683, -1.81418675e-05, 5.42613873e-09, -6.08976045e-13, -210758.826, -64.6692907], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 64,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[18.9617029, 0.0313679588, -2.03774674e-05, 6.02084031e-09, -6.70033585e-13, -234520.808, -66.6028245], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 65,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[20.8226936, 0.0302775613, -2.02720823e-05, 6.09342301e-09, -6.85710742e-13, -262604.633, -75.9252339], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 66,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[16.9321382, 0.0246789772, -1.60886998e-05, 4.80625169e-09, -5.41697616e-13, -175604.238, -52.9715536], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23
 *****',
    referenceType = "Theory",
)


entry(
    index = 67,
    label = "rPF4acylF",
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[17.3289726, 0.0245873227, -1.62343944e-05, 4.88359895e-09, -5.5264529e-13, -172281.863, -54.8103504], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 68,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[18.9860579, 0.0274288714, -1.82598966e-05, 5.50394991e-09, -6.22660805e-13, -224429.952, -65.123439], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 69,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[16.6742245, 0.0263017794, -1.71083148e-05, 5.06045078e-09, -5.63715004e-13, -174176.678, -53.2782211], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 71,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[18.5114953, 0.0278239091, -1.82091153e-05, 5.39293111e-09, -6.00437796e-13, -196045.829, -61.0706811], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 72,
    label = "rPF4acid",
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[16.2880311, 0.0289080563, -1.82242333e-05, 5.29715576e-09, -5.84203467e-13, -172703.343, -49.8310932], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 73,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[17.9259357, 0.0316806803, -2.01834282e-05, 5.89799661e-09, -6.52326165e-13, -224879.757, -59.9631672], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 74,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[20.8234506, 0.035993138, -2.33719317e-05, 6.9230913e-09, -7.72898319e-13, -257806.335, -77.8809052], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 75,
    label = "rPF5-1ene",
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[19.8909222, 0.0298795922, -1.95358378e-05, 5.82395025e-09, -6.54011493e-13, -188318.46, -66.7368104], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23 Five-carbon species',
    referenceType = "Theory",
)


entry(
    index = 76,
    label = "PF5-1ene",
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[21.0861914, 0.0331143649, -2.1565467e-05, 6.3828442e-09, -7.11452279e-13, -240907.226, -74.2841224], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 77,
    label = "PF5s",
    molecule = 
"""
multiplicity 1
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[22.3946879, 0.0317643195, -2.13021762e-05, 6.41462937e-09, -7.23016827e-13, -213684.32, -81.9940852], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 78,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[24.2718123, 0.0346268145, -2.34010727e-05, 7.05672098e-09, -7.94807841e-13, -260902.705, -92.049197], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 79,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[23.6588967, 0.0394031209, -2.5730908e-05, 7.53644998e-09, -8.28155002e-13, -285755.499, -92.0005706], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 80,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[25.7676556, 0.0379427763, -2.55527671e-05, 7.63462551e-09, -8.51146375e-13, -313741.736, -102.680687], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 81,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[21.6424881, 0.0318592929, -2.10515685e-05, 6.30221216e-09, -7.08801378e-13, -225077.106, -76.6830036], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23
 *****',
    referenceType = "Theory",
)


entry(
    index = 82,
    label = "rPF5acylF",
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[22.1053904, 0.0315592872, -2.11853884e-05, 6.43353261e-09, -7.32365765e-13, -222442.859, -79.1525888], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 83,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[23.5117104, 0.0348460341, -2.32873217e-05, 6.99999542e-09, -7.88272845e-13, -275362.186, -88.3710346], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[21.5717, 0.0332852829, -2.21147107e-05, 6.62914342e-09, -7.45285837e-13, -226165.605, -78.3495699], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 85,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[25.3373894, 0.0411618598, -2.70684019e-05, 7.98277224e-09, -8.8279731e-13, -312302.644, -100.212933], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 86,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[23.5611287, 0.0345960439, -2.30395263e-05, 6.90729024e-09, -7.76261122e-13, -244432.884, -87.4867978], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 87,
    label = "rPF5acid",
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[21.0425334, 0.0356398417, -2.29541672e-05, 6.77436318e-09, -7.55544392e-13, -223669.206, -73.7220261], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 88,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[22.5146967, 0.0388423743, -2.51233627e-05, 7.39817894e-09, -8.21555201e-13, -276503.014, -83.4271078], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 89,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[25.1137198, 0.0438459472, -2.83854186e-05, 8.316633e-09, -9.1704412e-13, -310918.8, -99.793846], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 90,
    label = "rPF6-1ene",
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[25.1742213, 0.0365086313, -2.45030708e-05, 7.43510134e-09, -8.45628305e-13, -238585.904, -93.4950722], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23 Six-carbon species',
    referenceType = "Theory",
)


entry(
    index = 91,
    label = "PF6-1ene",
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[26.5405324, 0.0396349588, -2.65107485e-05, 7.98689471e-09, -9.01557684e-13, -291206.46, -102.217764], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 92,
    label = "PF6s",
    molecule = 
"""
multiplicity 1
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[27.1739493, 0.0384334474, -2.6074508e-05, 7.94122658e-09, -9.04060434e-13, -263861.981, -105.809797], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 93,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[27.3017896, 0.0490501033, -3.24042976e-05, 9.55507331e-09, -1.05519236e-12, -335779.869, -110.184426], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 94,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.2288155, 0.0415713155, -2.82987601e-05, 8.55828082e-09, -9.6501597e-13, -311305.959, -117.16435], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 95,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.6299317, 0.0471328144, -3.18365831e-05, 9.51449601e-09, -1.06048636e-12, -363827.185, -120.798731], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 96,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[26.1387778, 0.0387225447, -2.56398123e-05, 7.68122328e-09, -8.6411593e-13, -275218.199, -98.9212718], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23
 *****',
    referenceType = "Theory",
)


entry(
    index = 97,
    label = "rPF6acylF",
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[27.1421323, 0.0384548633, -2.60723653e-05, 7.93280098e-09, -9.02182171e-13, -272890.703, -104.157002], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 98,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[28.4893061, 0.0416459612, -2.81866647e-05, 8.54264275e-09, -9.67559084e-13, -325719.398, -113.395597], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 99,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[26.598234, 0.0405502738, -2.71083244e-05, 8.09449437e-09, -9.03867649e-13, -276727.653, -104.035539], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 100,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.5154246, 0.0496006359, -3.29087341e-05, 9.75184584e-09, -1.08189729e-12, -362497.597, -121.613168], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 101,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[28.4674532, 0.0414009103, -2.79682442e-05, 8.48053462e-09, -9.61742702e-13, -294711.575, -112.030379], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 102,
    label = "rPF6acid",
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[25.9412373, 0.0426692469, -2.78923074e-05, 8.28283838e-09, -9.25986214e-13, -274104.701, -98.5604437], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 103,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[27.3917621, 0.0457741333, -3.00221738e-05, 8.91745637e-09, -9.96086225e-13, -326835.552, -107.925875], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 104,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.330079, 0.0521164633, -3.39553309e-05, 9.96908369e-09, -1.10000456e-12, -361103.493, -120.933706], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 105,
    label = "PF7-1ene1r",
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[30.5354499, 0.0440298668, -2.98903539e-05, 9.00159601e-09, -1.01080767e-12, -288384.143, -123.236817], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23 Seven-carbon species',
    referenceType = "Theory",
)


entry(
    index = 106,
    label = "PF7-1ene2r",
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.755056, 0.0440456678, -2.97675277e-05, 8.9894231e-09, -1.01420422e-12, -291995.721, -117.699287], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 107,
    label = "PF7-1ene3r",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u1 p0 c0 {1,S} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {5,D}
4  F u0 p3 c0 {3,S}
5  C u0 p0 c0 {3,D} {6,S} {7,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.1353777, 0.0467356369, -3.08681596e-05, 9.1542164e-09, -1.01864311e-12, -298726.485, -114.989341], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 108,
    label = "PF7-1ene4r",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u1 p0 c0 {1,S} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  F u0 p3 c0 {3,S}
5  F u0 p3 c0 {3,S}
6  C u0 p0 c0 {3,S} {7,S} {8,D}
7  F u0 p3 c0 {6,S}
8  C u0 p0 c0 {6,D} {9,S} {10,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.2006831, 0.0448127352, -2.95763447e-05, 8.81019347e-09, -9.85379043e-13, -293504.37, -111.326649], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 109,
    label = "PF7-1ene5r",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u1 p0 c0 {1,S} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  F u0 p3 c0 {3,S}
5  F u0 p3 c0 {3,S}
6  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  F u0 p3 c0 {6,S}
10 C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,D}
17 F u0 p3 c0 {16,S}
18 C u0 p0 c0 {16,D} {19,S} {20,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.6515982, 0.0444174726, -2.95554728e-05, 8.85262586e-09, -9.93952094e-13, -294203.154, -114.159885], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 110,
    label = "PF7-1ene6r",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u1 p0 c0 {1,S} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  F u0 p3 c0 {3,S}
5  F u0 p3 c0 {3,S}
6  F u0 p3 c0 {3,S}
7  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,D}
17 F u0 p3 c0 {16,S}
18 C u0 p0 c0 {16,D} {19,S} {20,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.2619314, 0.0438989399, -2.92476809e-05, 8.81349922e-09, -9.9665233e-13, -292552.03, -112.441359], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 111,
    label = "rPF7-1ene",
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
16 C u0 p0 c0 {13,S} {17,S} {18,D}
17 F u0 p3 c0 {16,S}
18 C u0 p0 c0 {16,D} {19,S} {20,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[30.083294, 0.0435053006, -2.93267174e-05, 8.87365806e-09, -1.00433419e-12, -288785.687, -118.365726], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 112,
    label = "PF7-1ene",
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[31.3772154, 0.0468509557, -3.14152843e-05, 9.42989934e-09, -1.05887889e-12, -341625.344, -126.628318], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 113,
    label = "PF7s",
    molecule = 
"""
multiplicity 4
1  C u3 p0 c0 {2,S}
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[31.9142261, 0.0457639556, -3.09661064e-05, 9.35278748e-09, -1.05507716e-12, -314296.307, -129.808444], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 114,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[33.2619613, 0.0504192766, -3.41406933e-05, 1.02377134e-08, -1.14486653e-12, -361508.054, -137.216411], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 115,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[30.4841491, 0.0596212707, -3.97233675e-05, 1.17755895e-08, -1.30596366e-12, -385649.676, -125.955098], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 116,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[32.9390649, 0.0575194959, -3.90632132e-05, 1.17098124e-08, -1.30833318e-12, -413772.786, -138.524821], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 117,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[31.3522627, 0.0458967614, -3.09647177e-05, 9.3765662e-09, -1.06212714e-12, -325732.047, -125.942302], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23
 *****',
    referenceType = "Theory",
)


entry(
    index = 118,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[28.7482877, 0.0535314719, -3.6249233e-05, 1.08992476e-08, -1.22415248e-12, -331181.771, -113.063225], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 119,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[32.3193797, 0.0454093429, -3.10915677e-05, 9.48505255e-09, -1.07871882e-12, -328350.59, -130.722422], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 120,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[30.0161576, 0.0460232419, -3.02778946e-05, 9.01945063e-09, -1.00979814e-12, -327840.378, -114.592674], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 121,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[31.2272849, 0.0454205674, -3.05771504e-05, 9.26479e-09, -1.05083309e-12, -328078.071, -122.436832], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 122,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[31.1669922, 0.0458713155, -3.08860527e-05, 9.35898152e-09, -1.06174923e-12, -327054.265, -123.261077], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 123,
    label = "rPF7acylF",
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[31.5860477, 0.0475840206, -3.18410133e-05, 9.49163521e-09, -1.05772473e-12, -323475.022, -127.738924], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 124,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[32.5826703, 0.0503948873, -3.39222884e-05, 1.01735631e-08, -1.14009051e-12, -375978.58, -133.806366], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 125,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[31.2796454, 0.0480596944, -3.21434218e-05, 9.56383806e-09, -1.06324811e-12, -327145.66, -128.228918], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 126,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[32.8178635, 0.0598982212, -4.00386394e-05, 1.19168559e-08, -1.32660123e-12, -412391.209, -137.968649], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 127,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[32.388114, 0.0508862149, -3.42795648e-05, 1.02855517e-08, -1.15317168e-12, -345016.716, -131.692452], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 128,
    label = "rPF7acid",
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[30.5609956, 0.0503172182, -3.30449e-05, 9.79567381e-09, -1.09114083e-12, -324476.034, -122.164033], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 129,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[30.9812066, 0.0557890782, -3.68083076e-05, 1.09085056e-08, -1.21312987e-12, -376955.313, -126.157886], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 130,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[32.4960468, 0.0627076051, -4.13052283e-05, 1.22059488e-08, -1.35335441e-12, -410988.993, -137.169705], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 131,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[36.4733387, 0.0609029469, -4.14002674e-05, 1.24465736e-08, -1.39517049e-12, -411404.987, -153.60494], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23 Eight-carbon species',
    referenceType = "Theory",
)


entry(
    index = 132,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[38.0162756, 0.0562878392, -3.79793633e-05, 1.13926705e-08, -1.27590195e-12, -416132.081, -159.726999], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 133,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[38.1422083, 0.056532391, -3.80390797e-05, 1.13358987e-08, -1.26031567e-12, -417086.866, -160.337307], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 134,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[38.5496194, 0.0556330643, -3.77360925e-05, 1.13454594e-08, -1.27167316e-12, -416976.34, -162.106421], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 135,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[35.4074357, 0.0694732072, -4.72623461e-05, 1.41885133e-08, -1.58824895e-12, -463377.146, -149.218945], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 136,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[34.6700558, 0.0550969817, -3.69744401e-05, 1.11325706e-08, -1.25503827e-12, -375547.266, -141.732724], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23
 *****',
    referenceType = "Theory",
)


entry(
    index = 137,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[34.5302165, 0.0585539932, -3.93986278e-05, 1.17588182e-08, -1.31034847e-12, -377041.175, -144.049028], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 138,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[33.9871917, 0.0653003947, -4.42003424e-05, 1.32515418e-08, -1.48328457e-12, -394564.558, -139.988855], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 139,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[33.0704668, 0.0645861479, -4.31915711e-05, 1.2854236e-08, -1.43123792e-12, -382420.049, -135.927001], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 140,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[35.0815849, 0.0583425777, -3.8287744e-05, 1.13061169e-08, -1.25360356e-12, -379179.229, -142.635624], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 141,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[35.2870077, 0.0564896084, -3.74134172e-05, 1.12005372e-08, -1.25910081e-12, -379977.535, -143.749855], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 142,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[34.8682893, 0.0564754499, -3.72095867e-05, 1.11187005e-08, -1.2492865e-12, -379375.369, -140.308138], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 143,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[35.2214156, 0.0568950094, -3.74643721e-05, 1.11085877e-08, -1.23637211e-12, -379934.79, -143.297915], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 144,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[35.1375819, 0.056634416, -3.73754503e-05, 1.11461119e-08, -1.24856071e-12, -379001.902, -143.02899], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 145,
    label = "rPF8acid",
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[35.276721, 0.0574655577, -3.79116673e-05, 1.12569703e-08, -1.25459069e-12, -374780.081, -145.780565], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)


entry(
    index = 146,
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
            NASAPolynomial(coeffs=[3.1682671, -0.00327931884, 6.64306396e-06, -6.12806624e-09, 2.11265971e-12, 29122.2592, 2.05193346], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[36.7949757, 0.06062944, -4.016845e-05, 1.19482222e-08, -1.33259389e-12, -427550.286, -155.69207], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.342438367274774,'J/(mol*K)'),
    ),
    reference = 'NCSU23',
    referenceType = "Theory",
)
