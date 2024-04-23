#!/usr/bin/env python
# encoding: utf-8

name = "NCSU_C2_C8_PFAS"
shortDesc = "C2-C8 PFCA thermo library (Westmoreland, 2023)"
longDesc = """
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 

This library contains C/H/O/F/ chemistry
It is recommended for fluorinated hydrocarbons, specifically PFSA & PFCA Destruction Thermochemistry.

Thermochemistry produced by: 

  ******************** North Carolina State University - PFSA & PFCA Destruction Thermochemistry ***************************************
  PI: Phillip R. Westmoreland <prwestmo@ncsu.edu>
  Authors: Hrishikesh Ram <hram@ncsu.edu>, Tommy J. Sadej <tpsadej@ncsu.edu>, C. Claire Murphy <ccmurph@ncsu.edu>, Tim J. Mallo <tmallo@ncsu.edu>

  02/2024 - Hrishikesh Ram
      - Compiled thermochemistry for 53 sulfur-containing species involved in PFSA thermal destruction skeletal mechanism
          - 4 polynomials sourced from Extended Third Millennium Database of Goos/Burcat/Ruscic (SO, SO2, SO3, SO3Hr) (Ref. [1])
          - 17 polynomials computed based on quantum chemistry @ G4//B3LYP/GTBas3
          - 32 polynomials computed based on quantum chemistry @ M06-2X-D3(0)/def2-QZVPP
      - Appended and organized thermochemistry for 147 CHOF-containing species involved in PFCA thermal destruction skeletal mechanism (Ref. [2])
          - PFSA thermal destruction skeletal mechanism builds upon PFCA thermal destruction skeletal mechanism (Ref. [2])
          - 30 polynomials sourced from Extended Third Millennium Database of Goos/Burcat/Ruscic (Ref. [1])
          - 45 polynomials computed based on quantum chemistry @ G4//B3LYP/GTBas3 (Ref. [2])
          - 72 polynomials computed based on quantum chemistry @ M06-2X-D3(0)/def2-QZVPP (Ref. [2])
          - Note that nomenclature scheme is slightly modified from the original (Ref. [2])
      - Compiled extrapolated NASA polynomials for 126 large species > C8/C8S1 in size, for PFSA and PFCA oxidation mechanisms (based on present work and Ref. [2])
      - Maximum absolute percentage deviations between polynomial fits of Cp(T) and "true" (directly extrapolated) values of Cp(T) and corresponding temperatures are given

  [1] Goos, E.; Burcat, A.; Ruscic, B. http://burcat.technion.ac.il/dir, mirrored at http://garfield.chem.elte.hu/Burcat/burcat.html
  [2] Ram et al., J. Phys. Chem. A, 2024, DOI: 10.1021/acs.jpca.3c06937.

  References:
      GBR3M = Extended Third Millennium Database of Goos/Burcat/Ruscic (Ref. [1], http://garfield.chem.elte.hu/Burcat/burcat.html)
      NCSU23 = previous work from North Carolina State University (Ref. [2], DOI: 10.1021/acs.jpca.3c06937) (work was carried out in 2023)
      NCSU24 = present work from North Carolina State University

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
        Cp0 = (20.7861565453831,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
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
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
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
        Cp0 = (20.118291515456107,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
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
        Cp0 = (19.49185346181332,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
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
        Cp0 = (31.449092010015974,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
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
        Cp0 = (26.67549121209327,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
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
        Cp0 = (33.19120373573688,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
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
        Cp0 = (34.90939541766235,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
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
        Cp0 = (35.76713924385876,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
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
        Cp0 = (35.87816575527326,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
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
            NASAPolynomial(coeffs=[3.48137108, 0.000212245717, -6.86359044e-07, 8.56185857e-10, -2.34581508e-13, -33860.7305, 1.0257999], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[2.92491143, 0.000850523032, -1.58179777e-07, 1.17507204e-11, -1.43309132e-16, -33635.2481, 4.19018883], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (28.945729704579776,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 11,
    label = "SO3Hr",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 S u1 p0 c0 {1,S} {3,D} {4,D}
3 O u0 p2 c0 {2,D}
4 O u0 p2 c0 {2,D}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.18471474, 0.0192277645, -1.85975873e-05, 7.95502482e-09, -9.4225491e-13, -44215.6599, 13.0496771], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[8.19420431, 0.00377828016, -1.34903219e-06, 2.17197023e-10, -1.29874848e-14, -45501.3223, -12.3824851], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (26.479191655211615,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 12,
    label = "SO",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 S u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61859514, -0.00232173768, 1.16462669e-05, -1.4209251e-08, 5.6076537e-12, -480.621641, 6.36504115], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[3.96894225, 0.000377296831, 7.67102696e-09, -1.37544433e-11, 1.37139416e-15, -728.571725, 3.73493087], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (30.08667402176099,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 13,
    label = "SO2",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 S u0 p1 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67480752, 0.00228302107, 8.46893049e-06, -1.36562039e-08, 5.76271873e-12, -36945.5073, 7.9686643], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[5.38423482, 0.0016793056, -6.32062944e-07, 1.08465348e-10, -6.66890336e-15, -37606.7022, -1.83130517], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (30.554049753948416,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 14,
    label = "SO3",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 S u0 p0 c0 {1,D} {3,D} {4,D}
3 O u0 p2 c0 {2,D}
4 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.37461122, 0.0159543297, -1.26322543e-05, 2.81827264e-09, 6.23371547e-13, -48926.9231, 13.1043046], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[7.29677572, 0.00273576437, -1.06377755e-06, 1.80776031e-10, -1.12077527e-14, -50309.6739, -12.4246659], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (19.74361622133726,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 15,
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
        Cp0 = (29.761897476177232,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 16,
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
        Cp0 = (19.59563358647759,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 17,
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
        Cp0 = (24.2955181925385,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 18,
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
        Cp0 = (39.63389798351085,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 19,
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
        Cp0 = (42.81212152344409,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 20,
    label = "CF2(s)",
    molecule = 
"""
multiplicity 1
1 F u0 p3 c0 {2,S}
2 C u0 p1 c0 {1,S} {3,S}
3 F u0 p3 c0 {2,S}""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56435487, 0.00123021056, 1.39909866e-05, -2.13708286e-08, 9.10710807e-12, -24458.7979, 7.83907808], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[5.35787718, 0.00180622418, -7.80465045e-07, 1.47642691e-10, -9.44754424e-15, -25172.8166, -2.63410779], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (29.63569532444745,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 21,
    label = "CF2(t)",
    molecule = 
"""
multiplicity 3
1 F u0 p3 c0 {2,S}
2 C u2 p0 c0 {1,S} {3,S}
3 F u0 p3 c0 {2,S}""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65863299, 0.00253462065, 7.99625743e-06, -1.34330295e-08, 5.75081256e-12, 4050.07968, 8.36023714], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[5.45344707, 0.00156561882, -6.08817038e-07, 1.03459271e-10, -6.41400747e-15, 3375.44779, -1.83921649], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
        Cp0 = (30.41956722889722,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 22,
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
        Cp0 = (19.80330882482415,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 23,
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
        Cp0 = (34.27395030666531,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 24,
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
        Cp0 = (35.33839150725976,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 25,
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
        Cp0 = (22.74331477942931,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 26,
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
        Cp0 = (8.740129347484455,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 27,
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
        Cp0 = (28.102237865046398,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 28,
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
        Cp0 = (17.708095341139728,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 29,
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
            NASAPolynomial(coeffs=[2.82296204, 0.014628917, -4.91575497e-06, -4.9959848e-09, 3.07132075e-12, -53832.9416, 12.7503214], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[6.13972159, 0.00792804091, -4.71368414e-06, 1.43546348e-09, -1.78081858e-13, -54824.6016, -4.89266668], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (23.47141235404561,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 30,
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
            NASAPolynomial(coeffs=[2.09960867, 0.0362710893, -4.07734276e-05, 2.31167596e-08, -5.2106622e-12, -70551.5307, 16.4304537], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[8.04197402, 0.0134840166, -8.06640146e-06, 2.29446418e-09, -2.50685517e-13, -71789.1232, -12.4836212], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (17.457117799465443,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 31,
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
            NASAPolynomial(coeffs=[2.5959844, 0.0277761077, -1.80917861e-05, 2.203407e-09, 1.38850594e-12, -64429.265, 16.1759542], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[7.27302862, 0.0153939852, -9.00768376e-06, 2.47339313e-09, -2.60504179e-13, -65680.9765, -7.96959414], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (21.584215251108965,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 32,
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
            NASAPolynomial(coeffs=[1.74744564, 0.0156039351, -3.55332951e-06, -6.43464995e-09, 3.41825032e-12, -73207.4461, 17.4472988], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[4.3795147, 0.0113011606, -6.4374204e-06, 1.71357905e-09, -1.75182363e-13, -74045.135, 3.19271169], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (14.529071451034865,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 33,
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
            NASAPolynomial(coeffs=[2.29288001, 0.0363697973, -2.81337307e-05, 7.92002073e-09, 9.99586583e-14, -121994.81, 16.6866301], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[8.41880929, 0.0184199668, -1.10398151e-05, 3.07796368e-09, -3.27998753e-13, -123547.69, -14.5059092], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (19.064065131055827,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 34,
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
            NASAPolynomial(coeffs=[2.25253889, 0.0651622972, -7.0135291e-05, 3.69634486e-08, -7.63138074e-12, -172243.335, 16.4104158], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[13.2974244, 0.024892241, -1.55944358e-05, 4.5123644e-09, -4.95981186e-13, -174647.787, -37.8521439], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (18.72865039684139,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 35,
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
            NASAPolynomial(coeffs=[3.26013535, 0.0852018304, -9.27520764e-05, 4.91350442e-08, -1.01760753e-11, -221689.494, 12.0763544], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[17.9259357, 0.0316806803, -2.01834282e-05, 5.89799661e-09, -6.52326165e-13, -224879.757, -59.9631672], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (27.106273497694932,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 36,
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
            NASAPolynomial(coeffs=[2.85259858, 0.109751676, -0.000119878678, 6.28292983e-08, -1.27445623e-11, -272183.639, 13.3659226], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[22.5146967, 0.0388423743, -2.51233627e-05, 7.39817894e-09, -8.21555201e-13, -276503.014, -83.4271078], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (23.717824258007013,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 37,
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
            NASAPolynomial(coeffs=[2.42624047, 0.137282695, -0.000154754728, 8.3718967e-08, -1.76080826e-11, -321424.771, 14.6067168], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[27.3917621, 0.0457741333, -3.00221738e-05, 8.91745637e-09, -9.96086225e-13, -326835.552, -107.925875], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (20.172885690465552,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 38,
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
            NASAPolynomial(coeffs=[4.26403677, 0.147458264, -0.000151512846, 7.21787045e-08, -1.27308063e-11, -370851.905, 6.53688745], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[30.9812066, 0.0557890782, -3.68083076e-05, 1.09085056e-08, -1.21312987e-12, -376955.313, -126.157886], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (35.453174326595885,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 39,
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
            NASAPolynomial(coeffs=[3.29110517, 0.177967023, -0.000191157976, 9.59300069e-08, -1.81585653e-11, -420015.617, 10.1142128], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[36.7949757, 0.06062944, -4.016845e-05, 1.19482222e-08, -1.33259389e-12, -427550.286, -155.69207], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (27.363770908375862,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 40,
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
            NASAPolynomial(coeffs=[1.95155346, 0.0170102644, -1.39064933e-05, 3.91055562e-09, 1.3635329e-13, -44203.1319, 16.9063898], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[5.50001605, 0.00662261862, -4.03433136e-06, 1.13531886e-09, -1.21388652e-13, -45103.1347, -1.16444208], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (16.226118290497613,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 41,
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
            NASAPolynomial(coeffs=[1.48332506, 0.0421886654, -4.61511419e-05, 2.42035928e-08, -4.89781592e-12, -92218.1477, 21.1111662], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[9.16042693, 0.014565104, -9.34306887e-06, 2.74972343e-09, -3.05560104e-13, -93907.8104, -16.6976241], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (12.333050761939912,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 42,
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
            NASAPolynomial(coeffs=[2.02957966, 0.0664328838, -7.92227834e-05, 4.60228177e-08, -1.05068075e-11, -142834.913, 18.9364545], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[13.8492258, 0.0209197562, -1.36012772e-05, 4.04060373e-09, -4.52618169e-13, -145287.115, -38.5278697], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (16.87486421363416,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 43,
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
            NASAPolynomial(coeffs=[3.60385454, 0.0804797157, -8.67306905e-05, 4.40992248e-08, -8.53332209e-12, -192715.563, 12.5937573], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[18.5114953, 0.0278239091, -1.82091153e-05, 5.39293111e-09, -6.00437796e-13, -196045.829, -61.0706811], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (29.96411385409184,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 44,
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
            NASAPolynomial(coeffs=[3.52156005, 0.108768246, -0.000125318719, 6.91073459e-08, -1.48297568e-11, -240125.667, 10.6890553], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[23.5611287, 0.0345960439, -2.30395263e-05, 6.90729024e-09, -7.76261122e-13, -244432.884, -87.4867978], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (29.279879393306857,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 45,
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
            NASAPolynomial(coeffs=[2.09968063, 0.143559072, -0.000176236093, 1.04012838e-07, -2.40165864e-11, -289272.374, 16.0071135], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[28.4674532, 0.0414009103, -2.79682442e-05, 8.48053462e-09, -9.61742702e-13, -294711.575, -112.030379], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (17.457716108195445,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 46,
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
            NASAPolynomial(coeffs=[4.70641376, 0.147995951, -0.00015951857, 8.01611566e-08, -1.52178066e-11, -338799.523, 5.26001696], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[32.388114, 0.0508862149, -3.42795648e-05, 1.02855517e-08, -1.15317168e-12, -345016.716, -131.692452], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (39.13130127308204,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 47,
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
            NASAPolynomial(coeffs=[5.89488297, 0.162157617, -0.000166218156, 7.90847382e-08, -1.40635805e-11, -388170.496, -0.581700733], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[33.9871917, 0.0653003947, -4.42003424e-05, 1.32515418e-08, -1.48328457e-12, -394564.558, -139.988855], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (49.012784092453145,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 48,
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
            NASAPolynomial(coeffs=[2.73765568, 0.0366140978, -3.77663109e-05, 1.86011694e-08, -3.47925655e-12, -122006.153, 14.3576641], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[9.20214968, 0.0140186914, -8.76705559e-06, 2.53090213e-09, -2.77332113e-13, -123462.18, -17.645425], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (22.76213581273489,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 49,
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
            NASAPolynomial(coeffs=[2.29853129, 0.066675114, -8.10952986e-05, 4.81672148e-08, -1.12570981e-11, -171690.514, 16.0504489], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[14.0309788, 0.0206720088, -1.34806683e-05, 4.01747963e-09, -4.51335571e-13, -174083.338, -40.7834998], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (19.111052487360546,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 50,
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
            NASAPolynomial(coeffs=[2.25422082, 0.0933752557, -0.000115708027, 6.9488406e-08, -1.63735338e-11, -221034.536, 15.8432442], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[18.9860579, 0.0274288714, -1.82598966e-05, 5.50394991e-09, -6.22660805e-13, -224429.952, -65.123439], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (18.742634740952745,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 51,
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
            NASAPolynomial(coeffs=[2.41976525, 0.113760003, -0.000133477556, 7.50063399e-08, -1.64264059e-11, -270871.106, 14.7488616], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[23.5117104, 0.0348460341, -2.32873217e-05, 6.99999542e-09, -7.88272845e-13, -275362.186, -88.3710346], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (20.119047715831233,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 52,
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
            NASAPolynomial(coeffs=[1.44232971, 0.144679584, -0.000175005675, 1.012677e-07, -2.28602527e-11, -320052.289, 18.379], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[28.4893061, 0.0416459612, -2.81866647e-05, 8.54264275e-09, -9.67559084e-13, -325719.398, -113.395597], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (11.992196456846806,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 53,
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
            NASAPolynomial(coeffs=[3.95185531, 0.150577909, -0.000162686464, 8.16761089e-08, -1.54306675e-11, -369535.405, 7.90582552], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[32.5826703, 0.0503948873, -3.39222884e-05, 1.01735631e-08, -1.14009051e-12, -375978.58, -133.806366], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (32.857553247345386,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 54,
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
        Cp0 = (13.01244753579515,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 55,
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
            NASAPolynomial(coeffs=[2.21204618, 0.0707962204, -7.58979976e-05, 3.79739567e-08, -7.13845076e-12, -209445.485, 16.2928052], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[15.7053265, 0.0236894225, -1.5537286e-05, 4.59980592e-09, -5.11493938e-13, -212487.457, -50.5210536], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (18.39197527323868,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 56,
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
            NASAPolynomial(coeffs=[2.11540367, 0.0995106489, -0.000115727606, 6.41343664e-08, -1.37969286e-11, -258583.372, 15.7256443], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[20.8226936, 0.0302775613, -2.02720823e-05, 6.09342301e-09, -6.85710742e-13, -262604.633, -75.9252339], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (17.588444736519172,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 57,
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
            NASAPolynomial(coeffs=[2.58862868, 0.114771074, -0.000116963499, 5.2687304e-08, -8.14236355e-12, -308311.54, 13.1166721], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[25.7676556, 0.0379427763, -2.55527671e-05, 7.63462551e-09, -8.51146375e-13, -313741.736, -102.680687], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (21.523056392139367,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 58,
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
            NASAPolynomial(coeffs=[3.55697233, 0.132202771, -0.000130608696, 5.61406902e-08, -7.91156464e-12, -357651.499, 9.79369696], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.6299317, 0.0471328144, -3.18365831e-05, 9.51449601e-09, -1.06048636e-12, -363827.185, -120.798731], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (29.57431347159043,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 59,
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
            NASAPolynomial(coeffs=[4.00233183, 0.153020544, -0.00015194596, 6.67190934e-08, -9.9991825e-12, -406973.145, 6.13965989], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[32.9390649, 0.0575194959, -3.90632132e-05, 1.17098124e-08, -1.30833318e-12, -413772.786, -138.524821], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (33.27723838597985,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 60,
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
            NASAPolynomial(coeffs=[4.3438849, 0.175325574, -0.000178438142, 8.32372072e-08, -1.42499633e-11, -456244.344, 5.24518987], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[35.4074357, 0.0694732072, -4.72623461e-05, 1.41885133e-08, -1.58824895e-12, -463377.146, -149.218945], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (36.117068618610325,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 61,
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
            NASAPolynomial(coeffs=[1.28142439, 0.0464767776, -4.94027096e-05, 2.56988808e-08, -5.20798227e-12, -132402.434, 20.1209818], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[9.25586783, 0.0176883768, -1.08841678e-05, 3.12922591e-09, -3.42911768e-13, -134152.791, -19.1284414], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (10.654355188644818,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 62,
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
            NASAPolynomial(coeffs=[2.26945416, 0.0613300054, -5.66619365e-05, 2.2868119e-08, -2.84194054e-12, -181654.95, 17.1585173], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[13.5742296, 0.0250650134, -1.56956135e-05, 4.51134696e-09, -4.91275031e-13, -184363.61, -39.6190171], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (18.86929177693236,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 63,
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
            NASAPolynomial(coeffs=[1.74838132, 0.0935559421, -0.000103661488, 5.48782178e-08, -1.12180522e-11, -230744.878, 18.1078275], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[18.9617029, 0.0313679588, -2.03774674e-05, 6.02084031e-09, -6.70033585e-13, -234520.808, -66.6028245], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (14.536851127417417,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 64,
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
            NASAPolynomial(coeffs=[3.08704195, 0.102668957, -9.20972868e-05, 3.27591192e-08, -2.37842647e-12, -280690.049, 12.002133], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[23.6588967, 0.0394031209, -2.5730908e-05, 7.53644998e-09, -8.28155002e-13, -285755.499, -92.0005706], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (25.667094893945887,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 65,
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
            NASAPolynomial(coeffs=[3.7068198, 0.122404024, -0.00011089624, 4.08570763e-08, -3.62420345e-12, -330009.577, 8.90415366], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[27.3017896, 0.0490501033, -3.24042976e-05, 9.55507331e-09, -1.05519236e-12, -335779.869, -110.184426], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (30.820214659330272,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 66,
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
            NASAPolynomial(coeffs=[4.12316533, 0.143706623, -0.000133813522, 5.3143776e-08, -6.30836457e-12, -379309.55, 6.56105592], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[30.4841491, 0.0596212707, -3.97233675e-05, 1.17755895e-08, -1.30596366e-12, -385649.676, -125.955098], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (34.281904004750466,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 67,
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
        Cp0 = (16.571444612454524,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 68,
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
            NASAPolynomial(coeffs=[3.140993, 0.0523824217, -5.79499942e-05, 3.12800442e-08, -6.61660375e-12, -136493.792, 13.108987], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[12.2243588, 0.0189048419, -1.20174494e-05, 3.51423106e-09, -3.89121284e-13, -138453.26, -31.4269731], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.115668882381,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 69,
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
            NASAPolynomial(coeffs=[2.99566707, 0.0793943304, -9.42869609e-05, 5.46575682e-08, -1.24717803e-11, -186437.804, 13.945758], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[16.9360032, 0.0256594527, -1.67243444e-05, 4.97562387e-09, -5.57910898e-13, -189327.195, -53.8149221], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (24.907361869947646,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 70,
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
            NASAPolynomial(coeffs=[4.11049368, 0.0949162206, -0.000105116848, 5.59828297e-08, -1.15862149e-11, -237207.04, 9.13903994], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[21.0861914, 0.0331143649, -2.1565467e-05, 6.3828442e-09, -7.11452279e-13, -240907.226, -74.2841224], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (34.17654604451515,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 71,
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
            NASAPolynomial(coeffs=[2.4501589, 0.13139897, -0.000157260541, 9.05559401e-08, -2.03944483e-11, -286158.511, 15.1537338], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[26.5405324, 0.0396349588, -2.65107485e-05, 7.98689471e-09, -9.01557684e-13, -291206.46, -102.217764], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (20.37175458258546,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 72,
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
            NASAPolynomial(coeffs=[3.60056166, 0.146718124, -0.000164356866, 8.68181733e-08, -1.75960857e-11, -335508.041, 10.1878417], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[31.3772154, 0.0468509557, -3.14152843e-05, 9.42989934e-09, -1.05887889e-12, -341625.344, -126.628318], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (29.936735326425776,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 73,
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
            NASAPolynomial(coeffs=[1.06775152, 0.0593961922, -7.28684089e-05, 4.41304067e-08, -1.05247875e-11, -158236.086, 20.0290221], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[11.3850383, 0.0182954015, -1.14697572e-05, 3.36632859e-09, -3.75857002e-13, -160307.961, -29.7880116], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (8.877780098516302,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 74,
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
            NASAPolynomial(coeffs=[1.3079003, 0.0778932456, -8.65690929e-05, 4.64063738e-08, -9.66687228e-12, -207214.022, 20.2631539], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[15.3869021, 0.0265421122, -1.69897034e-05, 4.98498775e-09, -5.52744197e-13, -210278.066, -48.9011097], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (10.874488152621408,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 75,
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
            NASAPolynomial(coeffs=[1.05798011, 0.109595066, -0.000133212446, 7.84471965e-08, -1.81163149e-11, -256359.837, 19.7249952], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[20.8598033, 0.0328044795, -2.16516254e-05, 6.49002213e-09, -7.31197872e-13, -260441.037, -76.4115319], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (8.796536075344653,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 76,
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
            NASAPolynomial(coeffs=[3.1301134, 0.113315999, -0.000110287162, 4.67869807e-08, -6.41510813e-12, -307027.44, 11.0930781], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[25.3373894, 0.0411618598, -2.70684019e-05, 7.98277224e-09, -8.8279731e-13, -312302.644, -100.212933], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.02521085488054,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 77,
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
            NASAPolynomial(coeffs=[3.53522974, 0.134443651, -0.00013155661, 5.64393321e-08, -7.98432775e-12, -356347.67, 8.49569473], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.5154246, 0.0496006359, -3.29087341e-05, 9.75184584e-09, -1.08189729e-12, -362497.597, -121.613168], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (29.3935355198136,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 78,
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
            NASAPolynomial(coeffs=[3.94653596, 0.155827296, -0.000154597897, 6.87334589e-08, -1.0641693e-11, -405639.132, 6.20787615], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[32.8178635, 0.0598982212, -4.00386394e-05, 1.19168559e-08, -1.32660123e-12, -412391.209, -137.968649], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (32.813325710617505,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 79,
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
            NASAPolynomial(coeffs=[0.626147587, 0.0632700011, -7.5293593e-05, 4.44355274e-08, -1.03236363e-11, -154951.33, 21.3795465], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[11.7445177, 0.0199815618, -1.21384958e-05, 3.51717032e-09, -3.90307332e-13, -157234.256, -32.5564225], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (5.206080705558354,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 80,
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
            NASAPolynomial(coeffs=[-0.613774712, 0.0956046014, -0.000119876779, 7.3693266e-08, -1.77889057e-11, -204384.044, 26.586582], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[16.2094155, 0.0279402291, -1.78228038e-05, 5.28567101e-09, -5.9410411e-13, -207730.102, -54.4826833], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (-5.103206898891771,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 81,
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
            NASAPolynomial(coeffs=[0.464227325, 0.111941742, -0.000129062405, 7.1895118e-08, -1.56438328e-11, -253460.076, 21.7126505], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[20.8234506, 0.035993138, -2.33719317e-05, 6.9230913e-09, -7.72898319e-13, -257806.335, -77.8809052], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (3.8598007400377754,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 82,
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
            NASAPolynomial(coeffs=[2.8188827, 0.117338595, -0.000115094339, 5.04358797e-08, -7.52518066e-12, -305675.498, 11.6875303], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[25.1137198, 0.0438459472, -2.83854186e-05, 8.316633e-09, -9.1704412e-13, -310918.8, -99.793846], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (23.437494834108875,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 83,
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
            NASAPolynomial(coeffs=[3.5528715, 0.13592943, -0.000130730986, 5.51903234e-08, -7.58134864e-12, -354983.258, 8.25038566], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.330079, 0.0521164633, -3.39553309e-05, 9.96908369e-09, -1.10000456e-12, -361103.493, -120.933706], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (29.540217273852033,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 84,
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
            NASAPolynomial(coeffs=[3.8088088, 0.158049514, -0.000155207526, 6.87337707e-08, -1.0633549e-11, -404281.193, 6.08139607], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[32.4960468, 0.0627076051, -4.13052283e-05, 1.22059488e-08, -1.35335441e-12, -410988.993, -137.169705], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (31.668198387293103,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 85,
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
            NASAPolynomial(coeffs=[1.75293689, 0.03224099, -3.11030134e-05, 1.32937463e-08, -1.83699789e-12, -69015.4889, 17.7668708], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[8.27246204, 0.0110513744, -6.65131771e-06, 1.88110086e-09, -2.05957792e-13, -70563.8182, -14.9081906], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (14.574728243886799,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 86,
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
            NASAPolynomial(coeffs=[1.30440608, 0.0614056255, -7.41030397e-05, 4.38356294e-08, -1.02116572e-11, -121403.725, 20.9335746], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[12.0691761, 0.0193090834, -1.24020337e-05, 3.66416336e-09, -4.09425231e-13, -123604.806, -31.2408526], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (10.845435591051805,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 87,
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
            NASAPolynomial(coeffs=[2.25387422, 0.0787660405, -8.79789962e-05, 4.70904317e-08, -9.76692521e-12, -171031.751, 17.5959183], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[16.6742245, 0.0263017794, -1.71083148e-05, 5.06045078e-09, -5.63715004e-13, -174176.678, -53.2782211], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (18.739752948209293,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 88,
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
            NASAPolynomial(coeffs=[1.10134521, 0.109827547, -0.000128919373, 7.24930957e-08, -1.5876485e-11, -221804.576, 21.7428481], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[21.5717, 0.0332852829, -2.21147107e-05, 6.62914342e-09, -7.45285837e-13, -226165.605, -78.3495699], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (9.157093578227132,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 89,
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
            NASAPolynomial(coeffs=[2.25428539, 0.124176059, -0.000131921989, 6.42202616e-08, -1.14978072e-11, -271171.362, 16.8474434], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[26.598234, 0.0405502738, -2.71083244e-05, 8.09449437e-09, -9.03867649e-13, -276727.653, -104.035539], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (18.743171605804,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 90,
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
            NASAPolynomial(coeffs=[3.52038933, 0.138781633, -0.000137753702, 5.96556063e-08, -8.50741884e-12, -320578.055, 10.7722173], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[31.2796454, 0.0480596944, -3.21434218e-05, 9.56383806e-09, -1.06324811e-12, -327145.66, -128.228918], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (29.270145485630533,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 91,
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
            NASAPolynomial(coeffs=[4.22281155, 0.158062144, -0.000156078649, 6.78240298e-08, -9.89628403e-12, -369893.62, 7.59704869], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[34.5302165, 0.0585539932, -3.93986278e-05, 1.17588182e-08, -1.31034847e-12, -377041.175, -144.049028], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (35.110408775980744,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 92,
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
            NASAPolynomial(coeffs=[2.73183993, 0.0312637435, -2.61724834e-05, 9.86119226e-09, -1.18213277e-12, -72530.151, 15.007284], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[6.92915274, 0.0178264509, -1.10444825e-05, 3.12781695e-09, -3.36778605e-13, -73537.2115, -6.08031369], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (22.713780976763367,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 93,
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
            NASAPolynomial(coeffs=[3.67504217, 0.0464026959, -3.94759292e-05, 1.44014833e-08, -1.39109268e-12, -119751.59, 12.758462], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[11.2750302, 0.022629669, -1.3756777e-05, 3.88230731e-09, -4.18030036e-13, -121602.934, -25.5638187], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (30.556000742601768,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 94,
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
            NASAPolynomial(coeffs=[3.95023637, 0.0741729995, -7.99922944e-05, 4.23896273e-08, -8.83576238e-12, -170031.472, 10.7131936], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[16.2880311, 0.0289080563, -1.82242333e-05, 5.29715576e-09, -5.84203467e-13, -172703.343, -49.8310932], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (32.84409263123435,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 95,
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
            NASAPolynomial(coeffs=[3.55514034, 0.102607729, -0.000118933471, 6.77788814e-08, -1.52612528e-11, -220022.643, 11.389958], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[21.0425334, 0.0356398417, -2.29541672e-05, 6.77436318e-09, -7.55544392e-13, -223669.206, -73.7220261], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (29.5590814592186,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 96,
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
            NASAPolynomial(coeffs=[3.36091384, 0.126884087, -0.000145054886, 8.02847704e-08, -1.73998558e-11, -269283.314, 11.9031776], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[25.9412373, 0.0426692469, -2.78923074e-05, 8.28283838e-09, -9.25986214e-13, -274104.701, -98.5604437], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (27.94419248551386,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 97,
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
            NASAPolynomial(coeffs=[4.5161089, 0.142482289, -0.000153270792, 7.79317927e-08, -1.51215516e-11, -318666.333, 6.49110861], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[30.5609956, 0.0503172182, -3.30449e-05, 9.79567381e-09, -1.09114083e-12, -324476.034, -122.164033], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (37.549018628559146,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 98,
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
            NASAPolynomial(coeffs=[4.93481939, 0.163969914, -0.000175373325, 8.80348249e-08, -1.67332417e-11, -367968.538, 4.31738398], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[35.276721, 0.0574655577, -3.79116673e-05, 1.12569703e-08, -1.25459069e-12, -374780.081, -145.780565], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (41.03037134549278,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 99,
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
            NASAPolynomial(coeffs=[2.82584473, 0.0315503268, -3.54239151e-05, 2.03477361e-08, -4.73436188e-12, -73005.1684, 14.0071292], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[7.32262579, 0.0135933456, -8.53365759e-06, 2.4510407e-09, -2.67723777e-13, -73906.0318, -7.69477579], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (23.495380372290334,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 100,
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
            NASAPolynomial(coeffs=[2.48200726, 0.0568110684, -6.78479625e-05, 3.96415234e-08, -9.12048789e-12, -119205.67, 17.0158983], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[12.4438169, 0.0181957526, -1.17728726e-05, 3.49005269e-09, -3.90600867e-13, -121259.628, -31.3520552], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (20.63655658125495,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 101,
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
            NASAPolynomial(coeffs=[3.13452345, 0.0819773762, -0.00010323786, 6.34981661e-08, -1.53593513e-11, -169473.586, 13.5165974], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[17.3289726, 0.0245873227, -1.62343944e-05, 4.88359895e-09, -5.5264529e-13, -172281.863, -54.8103504], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.06187805074973,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 102,
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
            NASAPolynomial(coeffs=[2.09227395, 0.112866259, -0.000145027605, 9.02495167e-08, -2.19999883e-11, -218502.961, 17.0855028], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[22.1053904, 0.0315592872, -2.11853884e-05, 6.43353261e-09, -7.32365765e-13, -222442.859, -79.1525888], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (17.39613354421082,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 103,
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
            NASAPolynomial(coeffs=[2.01513382, 0.137083682, -0.00017119683, 1.02803268e-07, -2.41500052e-11, -267771.345, 17.5360345], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[27.1421323, 0.0384548633, -2.60723653e-05, 7.93280098e-09, -9.02182171e-13, -272890.703, -104.157002], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (16.75475481696634,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 104,
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
            NASAPolynomial(coeffs=[4.73863902, 0.137423672, -0.000140275517, 6.42313212e-08, -1.03551505e-11, -317228.041, 6.17179947], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[31.5860477, 0.0475840206, -3.18410133e-05, 9.49163521e-09, -1.05772473e-12, -323475.022, -127.738924], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (39.39923699271231,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 105,
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
        Cp0 = (20.076453971007826,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 106,
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
            NASAPolynomial(coeffs=[4.99602149, 0.0390221301, -3.89048133e-05, 1.85122236e-08, -3.35674971e-12, -86852.9053, 6.00909715], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[11.2903907, 0.0171351129, -1.10099766e-05, 3.20612517e-09, -3.52839963e-13, -88276.3021, -25.1802104], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (41.539233918095256,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 107,
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
            NASAPolynomial(coeffs=[4.19080346, 0.067838694, -8.18445172e-05, 4.8753146e-08, -1.14918199e-11, -134102.313, 9.35117837], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[15.5746698, 0.0226845736, -1.46853539e-05, 4.36171539e-09, -4.892985e-13, -136398.153, -45.6647323], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (34.84427870819726,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 108,
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
            NASAPolynomial(coeffs=[4.03417309, 0.0912898708, -0.000108626179, 6.32007928e-08, -1.44940426e-11, -185046.274, 10.2670177], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[19.8909222, 0.0298795922, -1.95358378e-05, 5.82395025e-09, -6.54011493e-13, -188318.46, -66.7368104], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (33.54198135196475,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 109,
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
            NASAPolynomial(coeffs=[2.34119082, 0.128646217, -0.000163917645, 1.01183615e-07, -2.44841226e-11, -234059.571, 16.4597353], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[25.1742213, 0.0365086313, -2.45030708e-05, 7.43510134e-09, -8.45628305e-13, -238585.904, -93.4950722], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (19.465743554853532,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 110,
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
            NASAPolynomial(coeffs=[3.09517255, 0.146484793, -0.000176336465, 1.01907163e-07, -2.30194619e-11, -283139.413, 13.0796072], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[30.083294, 0.0435053006, -2.93267174e-05, 8.87365806e-09, -1.00433419e-12, -288785.687, -118.365726], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (25.734696463709042,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 111,
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
            NASAPolynomial(coeffs=[2.30899358, 0.0422577504, -4.92651847e-05, 2.7897856e-08, -6.19183848e-12, -107033.219, 16.5044151], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[9.9123955, 0.0135437838, -8.74369637e-06, 2.58317152e-09, -2.88077635e-13, -108638.882, -20.6025142], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (19.198040806465826,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 112,
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
            NASAPolynomial(coeffs=[2.43479501, 0.0668059801, -7.97859718e-05, 4.60161438e-08, -1.03906265e-11, -157682.706, 16.3759957], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[14.6120761, 0.0203364479, -1.34410617e-05, 4.0257959e-09, -4.52937528e-13, -160230.142, -42.9322446], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (20.244012093511046,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 113,
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
            NASAPolynomial(coeffs=[3.56635367, 0.0850007952, -9.75730239e-05, 5.37039204e-08, -1.15093408e-11, -207409.673, 11.6483023], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[19.143041, 0.0273703683, -1.81418675e-05, 5.42613873e-09, -6.08976045e-13, -210758.826, -64.6692907], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (29.652314272328613,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 114,
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
            NASAPolynomial(coeffs=[2.32109559, 0.114425653, -0.000131093287, 7.08475023e-08, -1.4741496e-11, -256112.361, 15.8513295], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[24.2718123, 0.0346268145, -2.34010727e-05, 7.05672098e-09, -7.94807841e-13, -260902.705, -92.049197], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (19.29866251621534,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 115,
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
            NASAPolynomial(coeffs=[2.19757047, 0.138930211, -0.000158187975, 8.43850058e-08, -1.72301759e-11, -305361.405, 15.9373033], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.2288155, 0.0415713155, -2.82987601e-05, 8.55828082e-09, -9.6501597e-13, -311305.959, -117.16435], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (18.27161752357245,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 116,
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
            NASAPolynomial(coeffs=[4.36261609, 0.147456147, -0.000151855234, 7.0153564e-08, -1.14837017e-11, -354800.159, 6.84635227], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[33.2619613, 0.0504192766, -3.41406933e-05, 1.02377134e-08, -1.14486653e-12, -361508.054, -137.216411], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (36.27280839765886,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 117,
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
            NASAPolynomial(coeffs=[4.58404937, 0.170058253, -0.000177530449, 8.4798177e-08, -1.48826085e-11, -404107.036, 4.84290967], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[36.4733387, 0.0609029469, -4.14002674e-05, 1.24465736e-08, -1.39517049e-12, -411404.987, -153.60494], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (38.11390712663391,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 118,
    label = "PF2alkyl(s)",
    molecule = 
"""
multiplicity 1
1 F u0 p3 c0 {2,S}
2 C u0 p1 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 F u0 p3 c0 {3,S}""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.95647817, 0.034083685, -3.75768683e-05, 1.97827077e-08, -4.01060351e-12, -61265.9836, 17.5352764], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[8.25263035, 0.0114284629, -7.38811507e-06, 2.18625884e-09, -2.43837964e-13, -62651.6833, -13.472365], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (16.26706460769786,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 119,
    label = "PF3alkyl(s)",
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
9 F u0 p3 c0 {6,S}""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.35160602, 0.0562836531, -6.10577976e-05, 3.08377211e-08, -5.85662832e-12, -110312.211, 16.0533306], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[13.2418504, 0.0181546305, -1.2012196e-05, 3.57260818e-09, -3.98338793e-13, -112761.858, -37.8437919], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (19.55234034591412,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 120,
    label = "PF4alkyl(s)",
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
12 F u0 p3 c0 {9,S}""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.17478667, 0.0831667319, -0.000105823213, 6.55924281e-08, -1.59670719e-11, -159812.045, 11.8590709], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[17.6413362, 0.0243547559, -1.6186582e-05, 4.88889622e-09, -5.54744491e-13, -162658.066, -57.6972237], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.396645088326206,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 121,
    label = "PF5alkyl(s)",
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
15 F u0 p3 c0 {12,S}""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.07833612, 0.103764488, -0.000121404571, 6.78843203e-08, -1.47741299e-11, -209557.788, 12.512456], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[22.3946879, 0.0317643195, -2.13021762e-05, 6.41462937e-09, -7.23016827e-13, -213684.32, -81.9940852], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (25.594710595850888,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 122,
    label = "PF6alkyl(s)",
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
18 F u0 p3 c0 {15,S}""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.99842716, 0.138043382, -0.000173851179, 1.05366853e-07, -2.49874285e-11, -258772.269, 15.9205826], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[27.1739493, 0.0384334474, -2.6074508e-05, 7.94122658e-09, -9.04060434e-13, -263861.981, -105.809797], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (16.615847916922146,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 123,
    label = "PF7alkyl(s)",
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
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 F u0 p3 c0 {18,S}""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68858738, 0.149327434, -0.000172302709, 9.42381125e-08, -1.99416393e-11, -308184.226, 8.69871566], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[31.9142261, 0.0457639556, -3.09661064e-05, 9.35278748e-09, -1.05507716e-12, -314296.307, -129.808444], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (30.6686218848018,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 124,
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
            NASAPolynomial(coeffs=[2.17938295, 0.032927959, -3.71383959e-05, 2.05412407e-08, -4.4677301e-12, -72244.7223, 16.9440783], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[7.89952523, 0.0115343902, -7.27854318e-06, 2.12167246e-09, -2.34588118e-13, -73463.1008, -11.0240517], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (18.120398068415533,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 125,
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
            NASAPolynomial(coeffs=[3.54155563, 0.0512803861, -5.85647861e-05, 3.28836011e-08, -7.28698512e-12, -123186.727, 11.7010484], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[12.3006288, 0.0180939179, -1.15598204e-05, 3.3967817e-09, -3.77736373e-13, -125031.033, -31.0188724], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (29.446131895745147,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 126,
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
            NASAPolynomial(coeffs=[3.92968225, 0.0774501917, -9.63876073e-05, 5.91002473e-08, -1.43055442e-11, -173041.817, 9.56743268], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[16.9321382, 0.0246789772, -1.60886998e-05, 4.80625169e-09, -5.41697616e-13, -175604.238, -52.9715536], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (32.673196168845315,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 127,
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
            NASAPolynomial(coeffs=[3.78752542, 0.0998061455, -0.00011776235, 6.73030687e-08, -1.5090766e-11, -221332.463, 10.3251195], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[21.6424881, 0.0318592929, -2.10515685e-05, 6.30221216e-09, -7.08801378e-13, -225077.106, -76.6830036], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (31.491238519895152,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 128,
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
            NASAPolynomial(coeffs=[4.86340282, 0.119416735, -0.000140070134, 7.95607947e-08, -1.77321814e-11, -270742.758, 4.82194158], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[26.1387778, 0.0387225447, -2.56398123e-05, 7.68122328e-09, -8.6411593e-13, -275218.199, -98.9212718], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (40.43658094391105,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 129,
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
            NASAPolynomial(coeffs=[2.77495665, 0.155866787, -0.000189410958, 1.10668194e-07, -2.53002344e-11, -319799.625, 13.0114804], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[31.3522627, 0.0458967614, -3.09647177e-05, 9.3765662e-09, -1.06212714e-12, -325732.047, -125.942302], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (23.072273333420743,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 130,
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
            NASAPolynomial(coeffs=[5.2408365, 0.165956062, -0.000192976365, 1.08276057e-07, -2.38264605e-11, -369318.532, 1.96069643], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[34.6700558, 0.0550969817, -3.69744401e-05, 1.11325706e-08, -1.25503827e-12, -375547.266, -141.732724], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (43.57473916710307,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 131,
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
            NASAPolynomial(coeffs=[4.49567106, 0.160250616, -0.000158736201, 7.12492746e-08, -1.13713189e-11, -375773.354, 6.58854933], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[33.0704668, 0.0645861479, -4.31915711e-05, 1.2854236e-08, -1.43123792e-12, -382420.049, -135.927001], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (37.379088971883355,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 132,
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
            NASAPolynomial(coeffs=[5.31368152, 0.158352375, -0.000159709715, 7.31922813e-08, -1.19596906e-11, -372272.557, 5.74275617], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[35.0815849, 0.0583425777, -3.8287744e-05, 1.13061169e-08, -1.25360356e-12, -379179.229, -142.635624], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (44.180406362811695,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 133,
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
            NASAPolynomial(coeffs=[3.7529301, 0.17582076, -0.000206202407, 1.16921372e-07, -2.59880198e-11, -373330.462, 10.0851308], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[35.2870077, 0.0564896084, -3.74134172e-05, 1.12005372e-08, -1.25910081e-12, -379977.535, -143.749855], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (31.2035970249921,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 134,
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
            NASAPolynomial(coeffs=[4.4048447, 0.173057946, -0.000204176408, 1.17158633e-07, -2.6441449e-11, -373019.116, 7.97819362], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[34.8682893, 0.0564754499, -3.72095867e-05, 1.11187005e-08, -1.2492865e-12, -379375.369, -140.308138], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (36.623916596920424,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 135,
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
            NASAPolynomial(coeffs=[5.43877998, 0.159802003, -0.000167489538, 8.15684828e-08, -1.47954586e-11, -373167.085, 4.44197351], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[35.2214156, 0.0568950094, -3.74643721e-05, 1.11085877e-08, -1.23637211e-12, -379934.79, -143.297915], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (45.22053283207023,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 136,
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
            NASAPolynomial(coeffs=[4.53408163, 0.169511876, -0.000192386829, 1.04950491e-07, -2.23155202e-11, -372404.375, 6.99934312], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[35.1375819, 0.056634416, -3.73754503e-05, 1.11461119e-08, -1.24856071e-12, -379001.902, -143.02899], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (37.69845222029031,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 137,
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
            NASAPolynomial(coeffs=[4.93494222, 0.170243173, -0.000181357365, 8.86080053e-08, -1.59872357e-11, -408597.314, 4.46381176], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[38.0162756, 0.0562878392, -3.79793633e-05, 1.13926705e-08, -1.27590195e-12, -416132.081, -159.726999], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (41.031392610936166,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 138,
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
            NASAPolynomial(coeffs=[6.16397268, 0.158449503, -0.000151921001, 6.12613487e-08, -7.24272044e-12, -409391.427, 0.438152855], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[38.1422083, 0.056532391, -3.80390797e-05, 1.13358987e-08, -1.26031567e-12, -417086.866, -160.337307], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (51.25012042717784,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 139,
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
            NASAPolynomial(coeffs=[4.78859061, 0.17078536, -0.000180626807, 8.67141162e-08, -1.51408825e-11, -409229.543, 5.74398173], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[38.5496194, 0.0556330643, -3.77360925e-05, 1.13454594e-08, -1.27167316e-12, -416976.34, -162.106421], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (39.81455762048462,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 140,
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
            NASAPolynomial(coeffs=[3.77881719, 0.143983797, -0.000157789386, 8.25004599e-08, -1.67680664e-11, -325716.599, 9.75642551], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[28.7482877, 0.0535314719, -3.6249233e-05, 1.08992476e-08, -1.22415248e-12, -331181.771, -113.063225], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (31.418834267089867,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 141,
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
            NASAPolynomial(coeffs=[1.41209093, 0.163713622, -0.000200560673, 1.1713958e-07, -2.66611318e-11, -321902.889, 19.7185986], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[32.3193797, 0.0454093429, -3.10915677e-05, 9.48505255e-09, -1.07871882e-12, -328350.59, -130.722422], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (11.740777250918244,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 142,
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
            NASAPolynomial(coeffs=[6.09559204, 0.133927709, -0.000150467903, 8.13683274e-08, -1.71525686e-11, -322667.375, 2.75467634], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[30.0161576, 0.0460232419, -3.02778946e-05, 9.01945063e-09, -1.00979814e-12, -327840.378, -114.592674], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (50.68157215209245,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 143,
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
            NASAPolynomial(coeffs=[3.20412344, 0.154848158, -0.000190720953, 1.1336227e-07, -2.64089392e-11, -322340.186, 13.4249866], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[31.2272849, 0.0454205674, -3.05771504e-05, 9.26479e-09, -1.05083309e-12, -328078.071, -122.436832], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.64056456582857,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 144,
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
            NASAPolynomial(coeffs=[2.8769569, 0.156966024, -0.000194429966, 1.16322825e-07, -2.72863518e-11, -321292.986, 13.7383483], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[31.1669922, 0.0458713155, -3.08860527e-05, 9.35898152e-09, -1.06174923e-12, -327054.265, -123.261077], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (23.92035059908803,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 145,
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
            NASAPolynomial(coeffs=[2.83212545, 0.140674078, -0.000153603041, 7.73076347e-08, -1.45450458e-11, -282135.024, 13.9579809], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[30.5354499, 0.0440298668, -2.98903539e-05, 9.00159601e-09, -1.01080767e-12, -288384.143, -123.236817], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (23.54760118394542,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 146,
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
            NASAPolynomial(coeffs=[1.58818377, 0.148006191, -0.000172647863, 9.55360141e-08, -2.04741105e-11, -285926.999, 20.3663315], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.755056, 0.0440456678, -2.97675277e-05, 8.9894231e-09, -1.01420422e-12, -291995.721, -117.699287], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (13.204894586422684,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 147,
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
            NASAPolynomial(coeffs=[4.73947076, 0.131236632, -0.000137995703, 6.74899459e-08, -1.23319173e-11, -293193.172, 5.97746557], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.1353777, 0.0467356369, -3.08681596e-05, 9.1542164e-09, -1.01864311e-12, -298726.485, -114.989341], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (39.406152463850326,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 148,
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
            NASAPolynomial(coeffs=[5.4456423, 0.130647426, -0.000144550173, 7.62739401e-08, -1.55549477e-11, -288294.088, 5.57405896], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.2006831, 0.0448127352, -2.95763447e-05, 8.81019347e-09, -9.85379043e-13, -293504.37, -111.326649], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (45.27758933518403,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 149,
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
            NASAPolynomial(coeffs=[4.5218746, 0.136452456, -0.000154882081, 8.3919787e-08, -1.76397646e-11, -288753.014, 9.19748248], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.6515982, 0.0444174726, -2.95554728e-05, 8.85262586e-09, -9.93952094e-13, -294203.154, -114.159885], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (37.59695732567664,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 150,
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
            NASAPolynomial(coeffs=[3.9024842, 0.143515395, -0.000175940362, 1.04787285e-07, -2.45347653e-11, -287389.074, 10.3586484], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.2619314, 0.0438989399, -2.92476809e-05, 8.81349922e-09, -9.9665233e-13, -292552.03, -112.441359], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (32.447058998833654,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 151,
    label = "FSO3H",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3 O u0 p2 c0 {2,D}
4 O u0 p2 c0 {2,D}
5 F u0 p3 c0 {2,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.54986757, 0.0329417704, -3.28121737e-05, 1.36282064e-08, -1.5703127e-12, -89095.9028, 17.9132258], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[9.41380673, 0.00803486401, -5.27508954e-06, 1.81900058e-09, -2.5522382e-13, -90996.1331, -21.6629475], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (12.886315973853,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 152,
    label = "PF1Sacid",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {9,S}
2 S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3 O u0 p2 c0 {2,D}
4 O u0 p2 c0 {2,D}
5 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6 F u0 p3 c0 {5,S}
7 F u0 p3 c0 {5,S}
8 F u0 p3 c0 {5,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.714276189, 0.0679026604, -9.20312309e-05, 6.06865638e-08, -1.56249347e-11, -134701.624, 22.0688885], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[11.2734378, 0.0213045835, -1.55919696e-05, 5.36562565e-09, -7.04342488e-13, -136595.385, -27.7826046], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (5.938822672477459,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 153,
    label = "PF2Sacid",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {12,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
            NASAPolynomial(coeffs=[0.408308355, 0.0958596826, -0.000131416754, 8.78511919e-08, -2.29781132e-11, -184328.481, 23.7709928], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[14.1298424, 0.0328505954, -2.47186967e-05, 8.59620249e-09, -1.13362808e-12, -186666.64, -40.3967394], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (3.394864554327143,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 154,
    label = "PF3Sacid",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {15,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
            NASAPolynomial(coeffs=[0.0521173096, 0.122931489, -0.000164872589, 1.07322616e-07, -2.73930919e-11, -233530.822, 25.0751771], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[18.6020541, 0.0413172855, -3.13295999e-05, 1.08795005e-08, -1.42869917e-12, -236870.087, -62.5639311], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (0.43332742242791905,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 155,
    label = "PF4Sacid",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {18,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
            NASAPolynomial(coeffs=[1.05706652, 0.13240426, -0.000152659991, 8.38374381e-08, -1.79537429e-11, -283919.27, 21.0490764], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[23.7373531, 0.0478929081, -3.5207656e-05, 1.17456764e-08, -1.48325119e-12, -288765.817, -89.9226446], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (8.788940065441334,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 156,
    label = "PF5Sacid",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {21,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
            NASAPolynomial(coeffs=[2.56596308, 0.144742507, -0.000153019282, 7.43163508e-08, -1.34045098e-11, -333320.642, 13.8996966], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[28.4000534, 0.0554669275, -4.01970867e-05, 1.31623357e-08, -1.63120158e-12, -339190.499, -114.250051], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (21.334604108221352,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 157,
    label = "PF6Sacid",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {24,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
            NASAPolynomial(coeffs=[3.49718155, 0.162114689, -0.0001660943, 7.68700094e-08, -1.27915777e-11, -382656.127, 9.85036565], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[32.4748184, 0.0642523478, -4.63730962e-05, 1.51040794e-08, -1.86214664e-12, -389354.064, -134.462033], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (29.077185266370208,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 158,
    label = "PF7Sacid",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {27,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
27 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61553188, 0.1866104, -0.000197080426, 9.66443291e-08, -1.78857435e-11, -431978.613, 8.40908041], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[35.0413995, 0.0767507433, -5.60566612e-05, 1.84722992e-08, -2.30368941e-12, -439055.978, -147.163518], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (30.061204661001305,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 159,
    label = "PF8Sacid",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {30,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 F u0 p3 c0 {26,S}
30 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.12411877, 0.206313359, -0.000214486649, 1.02651813e-07, -1.83016432e-11, -481264.232, 5.89762746], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[38.8127914, 0.0865425874, -6.33063706e-05, 2.08488798e-08, -2.5968898e-12, -489151.163, -166.201146], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (34.28983134598912,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 160,
    label = "FSO3r",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3 O u0 p2 c0 {2,D}
4 O u0 p2 c0 {2,D}
5 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.55203417, 0.0310931283, -4.12341855e-05, 2.65670604e-08, -6.71905855e-12, -60009.2552, 15.9002612], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[7.31244239, 0.0104477219, -7.86041559e-06, 2.71410698e-09, -3.54876805e-13, -60881.1482, -6.66501327], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (21.218792706714733,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 161,
    label = "PF1Sulfonater",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3 O u0 p2 c0 {2,D}
4 O u0 p2 c0 {2,D}
5 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6 F u0 p3 c0 {5,S}
7 F u0 p3 c0 {5,S}
8 F u0 p3 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.1601049, 0.048603794, -6.16606422e-05, 3.85310153e-08, -9.54471161e-12, -106500.688, 9.8154405], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[11.1697474, 0.0186429438, -1.38359467e-05, 4.72560485e-09, -6.12788951e-13, -107806.502, -23.5214625], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (34.589036678646124,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 162,
    label = "PF2Sulfonater",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
            NASAPolynomial(coeffs=[3.63151241, 0.0763513299, -9.78400912e-05, 6.1152463e-08, -1.50915807e-11, -156719.651, 11.7015427], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[15.1451771, 0.0276497678, -2.08173931e-05, 7.15709423e-09, -9.31012637e-13, -158890.038, -43.183508], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (30.194074180304582,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 163,
    label = "PF3Sulfonater",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
            NASAPolynomial(coeffs=[2.5351642, 0.110330819, -0.000147692738, 9.55957792e-08, -2.42714468e-11, -206470.187, 15.3694538], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[19.2491357, 0.0372382243, -2.86987827e-05, 1.00297667e-08, -1.32076652e-12, -209501.146, -63.7066199], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (21.078527971780364,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 164,
    label = "PF4Sulfonater",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
            NASAPolynomial(coeffs=[3.19474448, 0.122564759, -0.000141441418, 7.725536e-08, -1.64123597e-11, -253145.06, 12.3213295], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[24.3489565, 0.0440946592, -3.29563913e-05, 1.1078757e-08, -1.40489605e-12, -257683.24, -91.2722021], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.562583553511413,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 165,
    label = "PF5Sulfonater",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
            NASAPolynomial(coeffs=[3.85337642, 0.141661846, -0.000157525336, 8.18061115e-08, -1.62733327e-11, -302482.844, 8.75360465], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[28.786819, 0.0522149997, -3.87854517e-05, 1.29331125e-08, -1.62681396e-12, -307983.879, -114.107574], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (32.03875419776316,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 166,
    label = "PF6Sulfonater",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
            NASAPolynomial(coeffs=[5.01685405, 0.157350432, -0.000168130068, 8.37457957e-08, -1.59030092e-11, -351833.342, 3.7072156], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[30.9473144, 0.0656931229, -4.8740904e-05, 1.62175525e-08, -2.03708161e-12, -357622.661, -124.4084], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (41.71244545945569,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 167,
    label = "PF7Sulfonater",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
            NASAPolynomial(coeffs=[5.28765706, 0.179819522, -0.00019299821, 9.69555427e-08, -1.8672619e-11, -401142.019, 1.60167369], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[34.5538089, 0.0757067903, -5.62569258e-05, 1.87465621e-08, -2.35834274e-12, -407642.843, -142.82856], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (43.964026962984065,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 168,
    label = "PF8Sulfonater",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 F u0 p3 c0 {26,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.70481299, 0.201392416, -0.000216756159, 1.10165982e-07, -2.17123062e-11, -450439.736, -0.563366815], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[36.9989139, 0.0885881725, -6.6108033e-05, 2.21060575e-08, -2.7903651e-12, -457317.165, -154.632354], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (47.432454348910014,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 169,
    label = "PF1Sulfite",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 O u0 p2 c0 {2,S} {4,S}
4 S u0 p1 c0 {3,S} {5,D} {6,S}
5 O u0 p2 c0 {4,D}
6 O u0 p2 c0 {4,S} {9,S}
7 F u0 p3 c0 {2,S}
8 F u0 p3 c0 {2,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.550810261, 0.0688680869, -9.46353641e-05, 6.27495838e-08, -1.61810853e-11, -138625.018, 23.997891], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[11.6621188, 0.0200295834, -1.47877051e-05, 5.124542e-09, -6.76507547e-13, -140627.616, -28.5094326], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (4.579691324779729,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 170,
    label = "PF2Sulfite",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  F u0 p3 c0 {3,S}
5  F u0 p3 c0 {3,S}
6  F u0 p3 c0 {3,S}
7  O u0 p2 c0 {2,S} {8,S}
8  S u0 p1 c0 {7,S} {9,D} {10,S}
9  O u0 p2 c0 {8,D}
10 O u0 p2 c0 {8,S} {12,S}
11 F u0 p3 c0 {2,S}
12 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.504551551, 0.0994907745, -0.000143326315, 9.93499534e-08, -2.66643863e-11, -188642.975, 23.8636562], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[14.81312, 0.0310336479, -2.38063455e-05, 8.44712107e-09, -1.13296502e-12, -190943.546, -42.361202], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (4.195075009720738,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 171,
    label = "PF3Sulfite",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  F u0 p3 c0 {4,S}
8  F u0 p3 c0 {3,S}
9  F u0 p3 c0 {3,S}
10 O u0 p2 c0 {2,S} {11,S}
11 S u0 p1 c0 {10,S} {12,D} {13,S}
12 O u0 p2 c0 {11,D}
13 O u0 p2 c0 {11,S} {15,S}
14 F u0 p3 c0 {2,S}
15 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.20591765, 0.115803953, -0.000154930938, 1.01212508e-07, -2.59736023e-11, -237704.615, 22.4621918], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[18.0933084, 0.0405537361, -3.05046316e-05, 1.05609824e-08, -1.38555749e-12, -240697.06, -57.084543], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (10.026557221496203,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 172,
    label = "PF4Sulfite",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  F u0 p3 c0 {5,S}
9  F u0 p3 c0 {4,S}
10 F u0 p3 c0 {4,S}
11 F u0 p3 c0 {3,S}
12 F u0 p3 c0 {3,S}
13 O u0 p2 c0 {2,S} {14,S}
14 S u0 p1 c0 {13,S} {15,D} {16,S}
15 O u0 p2 c0 {14,D}
16 O u0 p2 c0 {14,S} {18,S}
17 F u0 p3 c0 {2,S}
18 H u0 p0 c0 {16,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.206261131, 0.141587015, -0.000175130051, 1.04124144e-07, -2.43315902e-11, -289362.794, 24.6385499], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[23.7346408, 0.0482626498, -3.63272335e-05, 1.23780851e-08, -1.59236397e-12, -294107.928, -89.0695698], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (1.7149504632775083,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 173,
    label = "PF5Sulfite",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {20,S}
3  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,S} {12,S} {13,S}
5  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
6  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  F u0 p3 c0 {6,S}
10 F u0 p3 c0 {5,S}
11 F u0 p3 c0 {5,S}
12 F u0 p3 c0 {4,S}
13 F u0 p3 c0 {4,S}
14 F u0 p3 c0 {3,S}
15 F u0 p3 c0 {3,S}
16 O u0 p2 c0 {2,S} {17,S}
17 S u0 p1 c0 {16,S} {18,D} {19,S}
18 O u0 p2 c0 {17,D}
19 O u0 p2 c0 {17,S} {21,S}
20 F u0 p3 c0 {2,S}
21 H u0 p0 c0 {19,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.593110158, 0.171252814, -0.000214847253, 1.29439473e-07, -3.06323648e-11, -339623.769, 27.9157774], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[27.8325866, 0.0572668992, -4.34436893e-05, 1.48873029e-08, -1.92354037e-12, -345294.752, -109.150996], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (-4.931392237137962,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 174,
    label = "PF6Sulfite",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {19,S} {23,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
6  C u0 p0 c0 {5,S} {7,S} {11,S} {12,S}
7  C u0 p0 c0 {6,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 F u0 p3 c0 {7,S}
11 F u0 p3 c0 {6,S}
12 F u0 p3 c0 {6,S}
13 F u0 p3 c0 {5,S}
14 F u0 p3 c0 {5,S}
15 F u0 p3 c0 {4,S}
16 F u0 p3 c0 {4,S}
17 F u0 p3 c0 {3,S}
18 F u0 p3 c0 {3,S}
19 O u0 p2 c0 {2,S} {20,S}
20 S u0 p1 c0 {19,S} {21,D} {22,S}
21 O u0 p2 c0 {20,D}
22 O u0 p2 c0 {20,S} {24,S}
23 F u0 p3 c0 {2,S}
24 H u0 p0 c0 {22,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.801065823, 0.18574986, -0.000222653421, 1.2766171e-07, -2.87058583e-11, -388973.349, 22.2104637], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[32.1610611, 0.0650743303, -4.87868041e-05, 1.65150844e-08, -2.11031471e-12, -395483.571, -130.274499], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (6.6604318400136595,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 175,
    label = "PF7Sulfite",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {22,S} {26,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
6  C u0 p0 c0 {5,S} {7,S} {14,S} {15,S}
7  C u0 p0 c0 {6,S} {8,S} {12,S} {13,S}
8  C u0 p0 c0 {7,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 F u0 p3 c0 {8,S}
12 F u0 p3 c0 {7,S}
13 F u0 p3 c0 {7,S}
14 F u0 p3 c0 {6,S}
15 F u0 p3 c0 {6,S}
16 F u0 p3 c0 {5,S}
17 F u0 p3 c0 {5,S}
18 F u0 p3 c0 {4,S}
19 F u0 p3 c0 {4,S}
20 F u0 p3 c0 {3,S}
21 F u0 p3 c0 {3,S}
22 O u0 p2 c0 {2,S} {23,S}
23 S u0 p1 c0 {22,S} {24,D} {25,S}
24 O u0 p2 c0 {23,D}
25 O u0 p2 c0 {23,S} {27,S}
26 F u0 p3 c0 {2,S}
27 H u0 p0 c0 {25,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.9435132, 0.194428383, -0.000216466629, 1.13169497e-07, -2.27618961e-11, -437903.639, 12.4831616], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[36.7545008, 0.0724666078, -5.34472287e-05, 1.77720722e-08, -2.23308366e-12, -445329.945, -153.955853], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (24.47373046744062,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 176,
    label = "PF8Sulfite",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {25,S} {29,S}
3  C u0 p0 c0 {2,S} {4,S} {23,S} {24,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {19,S} {20,S}
6  C u0 p0 c0 {5,S} {7,S} {17,S} {18,S}
7  C u0 p0 c0 {6,S} {8,S} {15,S} {16,S}
8  C u0 p0 c0 {7,S} {9,S} {13,S} {14,S}
9  C u0 p0 c0 {8,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 F u0 p3 c0 {9,S}
13 F u0 p3 c0 {8,S}
14 F u0 p3 c0 {8,S}
15 F u0 p3 c0 {7,S}
16 F u0 p3 c0 {7,S}
17 F u0 p3 c0 {6,S}
18 F u0 p3 c0 {6,S}
19 F u0 p3 c0 {5,S}
20 F u0 p3 c0 {5,S}
21 F u0 p3 c0 {4,S}
22 F u0 p3 c0 {4,S}
23 F u0 p3 c0 {3,S}
24 F u0 p3 c0 {3,S}
25 O u0 p2 c0 {2,S} {26,S}
26 S u0 p1 c0 {25,S} {27,D} {28,S}
27 O u0 p2 c0 {26,D}
28 O u0 p2 c0 {26,S} {30,S}
29 F u0 p3 c0 {2,S}
30 H u0 p0 c0 {28,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.42129976, 0.22913555, -0.000265740598, 1.45972996e-07, -3.12088492e-11, -487470.132, 18.8618684], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[41.0610762, 0.0816096858, -6.10016641e-05, 2.05136153e-08, -2.60231447e-12, -495949.749, -175.13545], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (11.817343723710172,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 177,
    label = "PF1Sultone",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 S u0 p0 c0 {2,S} {4,S} {6,D} {7,D}
6 O u0 p2 c0 {5,D}
7 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.64732913, 0.0472632465, -5.86553817e-05, 3.59249085e-08, -8.72897734e-12, -82614.1489, 18.537647], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[8.70642308, 0.01791334, -1.29602258e-05, 4.34794057e-09, -5.56352662e-13, -83970.2911, -15.2400181], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (13.696656471179898,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 178,
    label = "PF2Sultone",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  F u0 p3 c0 {3,S}
5  O u0 p2 c0 {3,S} {6,S}
6  S u0 p0 c0 {3,S} {5,S} {7,D} {8,D}
7  O u0 p2 c0 {6,D}
8  O u0 p2 c0 {6,D}
9  F u0 p3 c0 {2,S}
10 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.03809887, 0.0703702856, -8.83471636e-05, 5.46147376e-08, -1.33738059e-11, -134517.07, 18.0281287], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[12.5494095, 0.0262970282, -1.91952553e-05, 6.48545058e-09, -8.34480418e-13, -136517.931, -32.1758653], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (16.94569686671536,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 179,
    label = "PF3Sultone",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  O u0 p2 c0 {4,S} {7,S}
7  S u0 p0 c0 {4,S} {6,S} {8,D} {9,D}
8  O u0 p2 c0 {7,D}
9  O u0 p2 c0 {7,D}
10 F u0 p3 c0 {3,S}
11 F u0 p3 c0 {3,S}
12 F u0 p3 c0 {2,S}
13 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.18771295, 0.0949455047, -0.0001187862, 7.26922595e-08, -1.75964653e-11, -184293.748, 17.5260584], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[16.7247242, 0.0348655017, -2.57682581e-05, 8.74834021e-09, -1.12749599e-12, -187104.553, -52.123628], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (18.189657542024747,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 180,
    label = "PF4Sultone",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  O u0 p2 c0 {5,S} {8,S}
8  S u0 p0 c0 {5,S} {7,S} {9,D} {10,D}
9  O u0 p2 c0 {8,D}
10 O u0 p2 c0 {8,D}
11 F u0 p3 c0 {4,S}
12 F u0 p3 c0 {4,S}
13 F u0 p3 c0 {3,S}
14 F u0 p3 c0 {3,S}
15 F u0 p3 c0 {2,S}
16 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.10702702, 0.116860328, -0.000141609569, 8.35876916e-08, -1.95131645e-11, -234622.65, 17.7660531], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[20.5129433, 0.0435078005, -3.19874831e-05, 1.07774384e-08, -1.37838551e-12, -238317.39, -71.0996374], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (17.51879739322882,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 181,
    label = "PF5Sultone",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {5,S} {14,S} {15,S}
5  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
6  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  O u0 p2 c0 {6,S} {9,S}
9  S u0 p0 c0 {6,S} {8,S} {10,D} {11,D}
10 O u0 p2 c0 {9,D}
11 O u0 p2 c0 {9,D}
12 F u0 p3 c0 {5,S}
13 F u0 p3 c0 {5,S}
14 F u0 p3 c0 {4,S}
15 F u0 p3 c0 {4,S}
16 F u0 p3 c0 {3,S}
17 F u0 p3 c0 {3,S}
18 F u0 p3 c0 {2,S}
19 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.30820634, 0.138447155, -0.000160633556, 8.94229623e-08, -1.95263289e-11, -283926.668, 16.2667308], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[25.2878134, 0.0515888781, -3.79363685e-05, 1.26849883e-08, -1.60687323e-12, -288775.597, -95.8616275], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (19.191495328914307,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 182,
    label = "PF6Sultone",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {21,S} {22,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {17,S} {18,S}
5  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {5,S} {7,S} {13,S} {14,S}
7  C u0 p0 c0 {6,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  O u0 p2 c0 {7,S} {10,S}
10 S u0 p0 c0 {7,S} {9,S} {11,D} {12,D}
11 O u0 p2 c0 {10,D}
12 O u0 p2 c0 {10,D}
13 F u0 p3 c0 {6,S}
14 F u0 p3 c0 {6,S}
15 F u0 p3 c0 {5,S}
16 F u0 p3 c0 {5,S}
17 F u0 p3 c0 {4,S}
18 F u0 p3 c0 {4,S}
19 F u0 p3 c0 {3,S}
20 F u0 p3 c0 {3,S}
21 F u0 p3 c0 {2,S}
22 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.76568898, 0.158570852, -0.000177759784, 9.42435325e-08, -1.93460888e-11, -333226.613, 14.1044642], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.9159829, 0.059602387, -4.37561515e-05, 1.45404877e-08, -1.82850516e-12, -339138.307, -119.288187], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (22.995217637648366,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 183,
    label = "PF7Sultone",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {24,S} {25,S}
3  C u0 p0 c0 {2,S} {4,S} {22,S} {23,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {18,S} {19,S}
6  C u0 p0 c0 {5,S} {7,S} {16,S} {17,S}
7  C u0 p0 c0 {6,S} {8,S} {14,S} {15,S}
8  C u0 p0 c0 {7,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 O u0 p2 c0 {8,S} {11,S}
11 S u0 p0 c0 {8,S} {10,S} {12,D} {13,D}
12 O u0 p2 c0 {11,D}
13 O u0 p2 c0 {11,D}
14 F u0 p3 c0 {7,S}
15 F u0 p3 c0 {7,S}
16 F u0 p3 c0 {6,S}
17 F u0 p3 c0 {6,S}
18 F u0 p3 c0 {5,S}
19 F u0 p3 c0 {5,S}
20 F u0 p3 c0 {4,S}
21 F u0 p3 c0 {4,S}
22 F u0 p3 c0 {3,S}
23 F u0 p3 c0 {3,S}
24 F u0 p3 c0 {2,S}
25 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.30598319, 0.170107861, -0.000175232197, 8.18230908e-08, -1.38562139e-11, -382370.671, 6.93735599], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[34.404507, 0.0679550323, -4.93648545e-05, 1.61527962e-08, -1.99895697e-12, -389302.439, -142.830939], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (35.801936267651236,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 184,
    label = "PF8Sultone",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {27,S} {28,S}
3  C u0 p0 c0 {2,S} {4,S} {25,S} {26,S}
4  C u0 p0 c0 {3,S} {5,S} {23,S} {24,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {7,S} {19,S} {20,S}
7  C u0 p0 c0 {6,S} {8,S} {17,S} {18,S}
8  C u0 p0 c0 {7,S} {9,S} {15,S} {16,S}
9  C u0 p0 c0 {8,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 O u0 p2 c0 {9,S} {12,S}
12 S u0 p0 c0 {9,S} {11,S} {13,D} {14,D}
13 O u0 p2 c0 {12,D}
14 O u0 p2 c0 {12,D}
15 F u0 p3 c0 {8,S}
16 F u0 p3 c0 {8,S}
17 F u0 p3 c0 {7,S}
18 F u0 p3 c0 {7,S}
19 F u0 p3 c0 {6,S}
20 F u0 p3 c0 {6,S}
21 F u0 p3 c0 {5,S}
22 F u0 p3 c0 {5,S}
23 F u0 p3 c0 {4,S}
24 F u0 p3 c0 {4,S}
25 F u0 p3 c0 {3,S}
26 F u0 p3 c0 {3,S}
27 F u0 p3 c0 {2,S}
28 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.76050062, 0.191240542, -0.0001973727, 9.30235954e-08, -1.61219171e-11, -431668.422, 4.5993444], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[37.429651, 0.0794891647, -5.81334703e-05, 1.91226667e-08, -2.37799092e-12, -439148.514, -157.741728], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (39.58100444868532,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 185,
    label = "PF1Sacidr",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {8,S}
2 S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3 O u0 p2 c0 {2,D}
4 O u0 p2 c0 {2,D}
5 C u1 p0 c0 {2,S} {6,S} {7,S}
6 F u0 p3 c0 {5,S}
7 F u0 p3 c0 {5,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.64346523, 0.0558749701, -7.65030225e-05, 5.12549614e-08, -1.3413074e-11, -83372.4827, 18.9551227], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[9.82957671, 0.018519627, -1.35536623e-05, 4.67782413e-09, -6.16065422e-13, -84779.1602, -19.3854089], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (13.664530219069619,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 186,
    label = "PF2Sacidr",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {11,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u1 p0 c0 {5,S} {9,S} {10,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.3390865, 0.083936031, -0.000117060291, 7.97880056e-08, -2.12273085e-11, -132725.732, 21.0681602], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[12.8431124, 0.0292077687, -2.18996597e-05, 7.63542605e-09, -1.01112395e-12, -134590.93, -32.2540751], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (11.13378464672366,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 187,
    label = "PF3Sacidr",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {14,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 C u1 p0 c0 {8,S} {12,S} {13,S}
12 F u0 p3 c0 {11,S}
13 F u0 p3 c0 {11,S}
14 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.95919811, 0.106481289, -0.000143885449, 9.50580369e-08, -2.46482857e-11, -182409.34, 18.2122963], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[17.1074973, 0.0376849333, -2.83861765e-05, 9.85536302e-09, -1.29682753e-12, -185028.842, -52.8187012], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (16.28967944715148,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 188,
    label = "PF4Sacidr",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {17,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12 F u0 p3 c0 {11,S}
13 F u0 p3 c0 {11,S}
14 C u1 p0 c0 {11,S} {15,S} {16,S}
15 F u0 p3 c0 {14,S}
16 F u0 p3 c0 {14,S}
17 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.815524469, 0.132390902, -0.000168779279, 1.04469871e-07, -2.54806623e-11, -231739.14, 22.5878202], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[21.6053236, 0.0460760753, -3.45735957e-05, 1.18437854e-08, -1.53523352e-12, -235739.318, -76.9220358], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (6.780647711689771,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 189,
    label = "PF5Sacidr",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {20,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
17 C u1 p0 c0 {14,S} {18,S} {19,S}
18 F u0 p3 c0 {17,S}
19 F u0 p3 c0 {17,S}
20 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.34813729, 0.151777293, -0.000184094493, 1.07567661e-07, -2.4736183e-11, -281053.417, 19.9983755], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[26.3233095, 0.0538598483, -4.0193191e-05, 1.3616703e-08, -1.74425449e-12, -286147.613, -100.988204], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (11.209037101843414,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 190,
    label = "PF6Sacidr",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {23,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
20 C u1 p0 c0 {17,S} {21,S} {22,S}
21 F u0 p3 c0 {20,S}
22 F u0 p3 c0 {20,S}
23 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.94619982, 0.163750526, -0.000183874118, 9.76604497e-08, -2.00918782e-11, -330417.242, 13.4509844], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[30.9743965, 0.0614657674, -4.51890209e-05, 1.50317464e-08, -1.89170928e-12, -336514.282, -124.22587], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (24.496068268999803,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 191,
    label = "PF7Sacidr",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {26,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
23 C u1 p0 c0 {20,S} {24,S} {25,S}
24 F u0 p3 c0 {23,S}
25 F u0 p3 c0 {23,S}
26 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5233649, 0.191338491, -0.000219839168, 1.20385919e-07, -2.57478529e-11, -379699.623, 13.9161135], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[34.7530286, 0.0711271219, -5.25830436e-05, 1.75891216e-08, -2.22547505e-12, -386580.92, -143.750205], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (20.980423133009985,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 192,
    label = "PF8Sacidr",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {29,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
26 C u1 p0 c0 {23,S} {27,S} {28,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7621457, 0.205695624, -0.000225234845, 1.15712558e-07, -2.27961101e-11, -429043.883, 8.38344229], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[39.0824581, 0.0793456799, -5.81068855e-05, 1.92252237e-08, -2.40710261e-12, -436854.511, -165.749474], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (31.280219786695955,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 193,
    label = "PF8Sacid1r",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {29,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 F u0 p3 c0 {25,S}
29 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.2360272, 0.206384212, -0.000234794108, 1.28733621e-07, -2.77928049e-11, -434561.533, 9.07576261], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[36.9668286, 0.0829757354, -6.09534864e-05, 2.03546024e-08, -2.57673253e-12, -441483.43, -150.710116], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (35.22028980388034,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 194,
    label = "PF8Sacid2r",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {29,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 F u0 p3 c0 {25,S}
29 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.9371424, 0.196286106, -0.000202027936, 9.45388729e-08, -1.61494474e-11, -434974.253, 4.48364283], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[38.8425788, 0.0808326883, -5.91003015e-05, 1.94221109e-08, -2.41233892e-12, -442763.756, -164.132571], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (41.04968592529937,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 195,
    label = "PF8Sacid3r",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {29,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 F u0 p3 c0 {25,S}
29 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.38700877, 0.216264483, -0.000247209088, 1.33506488e-07, -2.79718744e-11, -434189.683, 15.1498929], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[39.8553938, 0.0783578198, -5.82994079e-05, 1.95335784e-08, -2.47036626e-12, -442281.703, -168.605126], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (19.846695187368947,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 196,
    label = "PF8Sacid4r",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {29,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
11 C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12 F u0 p3 c0 {11,S}
13 F u0 p3 c0 {11,S}
14 C u1 p0 c0 {11,S} {15,S} {16,S}
15 F u0 p3 c0 {14,S}
16 C u0 p0 c0 {14,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 C u0 p0 c0 {16,S} {20,S} {21,S} {22,S}
20 F u0 p3 c0 {19,S}
21 F u0 p3 c0 {19,S}
22 C u0 p0 c0 {19,S} {23,S} {24,S} {25,S}
23 F u0 p3 c0 {22,S}
24 F u0 p3 c0 {22,S}
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 F u0 p3 c0 {25,S}
29 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10495014, 0.205970055, -0.000229576393, 1.20492331e-07, -2.43912416e-11, -434178.646, 9.20106909], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[39.5743095, 0.0775658993, -5.71800828e-05, 1.90347394e-08, -2.39516433e-12, -441946.182, -165.286407], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (34.13045448841291,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 197,
    label = "PF8Sacid5r",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {29,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
17 C u1 p0 c0 {14,S} {18,S} {19,S}
18 F u0 p3 c0 {17,S}
19 C u0 p0 c0 {17,S} {20,S} {21,S} {22,S}
20 F u0 p3 c0 {19,S}
21 F u0 p3 c0 {19,S}
22 C u0 p0 c0 {19,S} {23,S} {24,S} {25,S}
23 F u0 p3 c0 {22,S}
24 F u0 p3 c0 {22,S}
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 F u0 p3 c0 {25,S}
29 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.26761507, 0.204422218, -0.000225310747, 1.16393456e-07, -2.30571131e-11, -434200.676, 8.05214662], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[39.6905892, 0.0774715255, -5.69965151e-05, 1.89251725e-08, -2.37534323e-12, -442022.331, -166.528528], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (35.48292596818242,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 198,
    label = "PF8Sacid6r",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {29,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
20 C u1 p0 c0 {17,S} {21,S} {22,S}
21 F u0 p3 c0 {20,S}
22 C u0 p0 c0 {20,S} {23,S} {24,S} {25,S}
23 F u0 p3 c0 {22,S}
24 F u0 p3 c0 {22,S}
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 F u0 p3 c0 {25,S}
29 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.73171877, 0.199282869, -0.000213320841, 1.05826745e-07, -1.97863458e-11, -434283.246, 6.59615639], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[39.5446377, 0.0773795006, -5.64882489e-05, 1.86199908e-08, -2.32173396e-12, -442113.246, -165.69313], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (39.341698832779024,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 199,
    label = "PF8Sacid7r",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {29,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
23 C u1 p0 c0 {20,S} {24,S} {25,S}
24 F u0 p3 c0 {23,S}
25 C u0 p0 c0 {23,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 F u0 p3 c0 {25,S}
29 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9244829, 0.209101336, -0.00024180394, 1.3464472e-07, -2.94892382e-11, -433484.908, 9.37634278], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[37.8652614, 0.0802942821, -5.90274487e-05, 1.97497858e-08, -2.50451964e-12, -440620.867, -156.107309], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (32.629966367631624,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 200,
    label = "PF9acid",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {29,S}
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 F u0 p3 c0 {25,S}
29 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80394391, 0.201304214, -0.000222527806, 1.17138908e-07, -2.39308e-11, -470083.993, 8.1485859], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[40.0200577, 0.0701595993, -4.68874663e-05, 1.40548872e-08, -1.5778257e-12, -477974.17, -169.925925], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (31.627749441246674,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 201,
    label = "PF10acid",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {32,S}
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 F u0 p3 c0 {28,S}
32 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04177771, 0.224395054, -0.000249079994, 1.31594213e-07, -2.69878855e-11, -519725.811, 6.92247653], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[44.5270896, 0.0775362143, -5.19730309e-05, 1.56054314e-08, -1.75373992e-12, -528533.658, -192.080402], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (33.605209680680005,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 202,
    label = "PF11acid",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {35,S}
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 F u0 p3 c0 {31,S}
35 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.27961157, 0.247485893, -0.000275632182, 1.46049517e-07, -3.00449708e-11, -569367.628, 5.69636689], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[49.0341216, 0.0849128291, -5.70585953e-05, 1.71559756e-08, -1.92965414e-12, -579093.147, -214.234881], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (35.582670418981095,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 203,
    label = "PF12acid",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {38,S}
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 F u0 p3 c0 {34,S}
38 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.51744566, 0.270576731, -0.000302184366, 1.60504817e-07, -3.31020548e-11, -619009.446, 4.47025631], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[53.5411537, 0.0922894436, -6.21441595e-05, 1.87065196e-08, -2.10556835e-12, -629652.635, -236.389359], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (37.5601330696086,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 204,
    label = "PF13acid",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {41,S}
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 C u0 p0 c0 {34,S} {38,S} {39,S} {40,S}
38 F u0 p3 c0 {37,S}
39 F u0 p3 c0 {37,S}
40 F u0 p3 c0 {37,S}
41 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.75527965, 0.29366757, -0.000328736551, 1.74960119e-07, -3.61591393e-11, -668651.264, 3.24414615], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[58.0481856, 0.0996660585, -6.7229724e-05, 2.02570638e-08, -2.28148257e-12, -680212.124, -258.543837], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (39.537594888789826,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 205,
    label = "PF14acid",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {44,S}
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 C u0 p0 c0 {34,S} {38,S} {39,S} {40,S}
38 F u0 p3 c0 {37,S}
39 F u0 p3 c0 {37,S}
40 C u0 p0 c0 {37,S} {41,S} {42,S} {43,S}
41 F u0 p3 c0 {40,S}
42 F u0 p3 c0 {40,S}
43 F u0 p3 c0 {40,S}
44 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.99311369, 0.316758408, -0.000355288735, 1.8941542e-07, -3.92162235e-11, -718293.081, 2.01803575], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[62.5552178, 0.107042673, -7.23152878e-05, 2.18076078e-08, -2.45739676e-12, -730771.613, -280.698317], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (41.51505712369419,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 206,
    label = "PF15acid",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {47,S}
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 C u0 p0 c0 {34,S} {38,S} {39,S} {40,S}
38 F u0 p3 c0 {37,S}
39 F u0 p3 c0 {37,S}
40 C u0 p0 c0 {37,S} {41,S} {42,S} {43,S}
41 F u0 p3 c0 {40,S}
42 F u0 p3 c0 {40,S}
43 C u0 p0 c0 {40,S} {44,S} {45,S} {46,S}
44 F u0 p3 c0 {43,S}
45 F u0 p3 c0 {43,S}
46 F u0 p3 c0 {43,S}
47 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.2309475, 0.339849248, -0.000381840924, 2.03870725e-07, -4.22733091e-11, -767934.899, 0.791926339], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[67.0622498, 0.114419287, -7.74008521e-05, 2.33581519e-08, -2.63331097e-12, -781331.101, -302.852796], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (43.492517446272146,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 207,
    label = "PF16acid",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {50,S}
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 C u0 p0 c0 {34,S} {38,S} {39,S} {40,S}
38 F u0 p3 c0 {37,S}
39 F u0 p3 c0 {37,S}
40 C u0 p0 c0 {37,S} {41,S} {42,S} {43,S}
41 F u0 p3 c0 {40,S}
42 F u0 p3 c0 {40,S}
43 C u0 p0 c0 {40,S} {44,S} {45,S} {46,S}
44 F u0 p3 c0 {43,S}
45 F u0 p3 c0 {43,S}
46 C u0 p0 c0 {43,S} {47,S} {48,S} {49,S}
47 F u0 p3 c0 {46,S}
48 F u0 p3 c0 {46,S}
49 F u0 p3 c0 {46,S}
50 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.46878147, 0.362940087, -0.000408393109, 2.18326027e-07, -4.53303936e-11, -817576.717, -0.434183751], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[71.5692817, 0.121795902, -8.24864168e-05, 2.49086961e-08, -2.8092252e-12, -831890.59, -325.007273], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (45.46997909916412,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 208,
    label = "PF9carboxylr",
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 F u0 p3 c0 {25,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.41690951, 0.193544905, -0.000214058731, 1.12785566e-07, -2.31515252e-11, -437145.215, 1.61462094], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[39.3812042, 0.0699666185, -4.75808629e-05, 1.43730552e-08, -1.6202763e-12, -444516.111, -165.241704], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (45.03869162681379,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 209,
    label = "PF10carboxylr",
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 F u0 p3 c0 {28,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.92765534, 0.215124738, -0.000237694707, 1.25064909e-07, -2.56342915e-11, -486279.974, -0.868271197], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[43.6261996, 0.0780376241, -5.31469595e-05, 1.60633427e-08, -1.81128427e-12, -494465.087, -186.089246], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (49.28526873772644,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 210,
    label = "PF11carboxylr",
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 F u0 p3 c0 {31,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.43840121, 0.236704571, -0.000261330683, 1.37344251e-07, -2.81170576e-11, -535414.733, -3.35116352], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[47.8711947, 0.0861086306, -5.87130569e-05, 1.77536305e-08, -2.00229227e-12, -544414.063, -206.936786], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (53.531846181217595,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 211,
    label = "PF12carboxylr",
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 F u0 p3 c0 {34,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.94914699, 0.258284404, -0.00028496666, 1.49623594e-07, -3.05998242e-11, -584549.492, -5.83405548], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[52.11619, 0.0941796365, -6.42791538e-05, 1.94439182e-08, -2.19330026e-12, -594363.039, -227.784327], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (57.778422876407106,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 212,
    label = "PF13carboxylr",
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 C u0 p0 c0 {34,S} {38,S} {39,S} {40,S}
38 F u0 p3 c0 {37,S}
39 F u0 p3 c0 {37,S}
40 F u0 p3 c0 {37,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.45989292, 0.279864236, -0.000308602634, 1.61902935e-07, -3.30825899e-11, -633684.251, -8.31694804], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[56.3611853, 0.102250642, -6.98452507e-05, 2.11342058e-08, -2.38430824e-12, -644312.015, -248.631868], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (62.02500081876602,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 213,
    label = "PF14carboxylr",
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 C u0 p0 c0 {34,S} {38,S} {39,S} {40,S}
38 F u0 p3 c0 {37,S}
39 F u0 p3 c0 {37,S}
40 C u0 p0 c0 {37,S} {41,S} {42,S} {43,S}
41 F u0 p3 c0 {40,S}
42 F u0 p3 c0 {40,S}
43 F u0 p3 c0 {40,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.97063881, 0.301444068, -0.000332238609, 1.74182277e-07, -3.55653559e-11, -682819.01, -10.7998404], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[60.6061803, 0.110321649, -7.54113483e-05, 2.28244937e-08, -2.57531626e-12, -694260.991, -269.479407], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (66.27157842854642,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 214,
    label = "PF15carboxylr",
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 C u0 p0 c0 {34,S} {38,S} {39,S} {40,S}
38 F u0 p3 c0 {37,S}
39 F u0 p3 c0 {37,S}
40 C u0 p0 c0 {37,S} {41,S} {42,S} {43,S}
41 F u0 p3 c0 {40,S}
42 F u0 p3 c0 {40,S}
43 C u0 p0 c0 {40,S} {44,S} {45,S} {46,S}
44 F u0 p3 c0 {43,S}
45 F u0 p3 c0 {43,S}
46 F u0 p3 c0 {43,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.48138459, 0.323023901, -0.000355874586, 1.8646162e-07, -3.80481225e-11, -731953.769, -13.2827323], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[64.851176, 0.118392654, -8.09774444e-05, 2.45147811e-08, -2.7663242e-12, -744209.967, -290.32695], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (70.51815512373594,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 215,
    label = "PF16carboxylr",
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 C u0 p0 c0 {34,S} {38,S} {39,S} {40,S}
38 F u0 p3 c0 {37,S}
39 F u0 p3 c0 {37,S}
40 C u0 p0 c0 {37,S} {41,S} {42,S} {43,S}
41 F u0 p3 c0 {40,S}
42 F u0 p3 c0 {40,S}
43 C u0 p0 c0 {40,S} {44,S} {45,S} {46,S}
44 F u0 p3 c0 {43,S}
45 F u0 p3 c0 {43,S}
46 C u0 p0 c0 {43,S} {47,S} {48,S} {49,S}
47 F u0 p3 c0 {46,S}
48 F u0 p3 c0 {46,S}
49 F u0 p3 c0 {46,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.99213059, 0.344603733, -0.000379510559, 1.9874096e-07, -4.05308877e-11, -781088.527, -15.7656252], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[69.0961711, 0.12646366, -8.65435416e-05, 2.62050689e-08, -2.9573322e-12, -794158.943, -311.17449], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (74.76473364810724,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 216,
    label = "PF8acylF",
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
22 C u0 p0 c0 {19,S} {23,S} {24,S} {25,S}
23 F u0 p3 c0 {22,S}
24 F u0 p3 c0 {22,S}
25 F u0 p3 c0 {22,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.92240113, 0.184340712, -0.000214635047, 1.19141093e-07, -2.57762479e-11, -418679.989, 12.37521], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[36.6468422, 0.0584017638, -3.97610649e-05, 1.20581684e-08, -1.36399554e-12, -425838.003, -152.491774], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (24.29819495063379,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 217,
    label = "PF9acylF",
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
22 C u0 p0 c0 {19,S} {23,S} {24,S} {25,S}
23 F u0 p3 c0 {22,S}
24 F u0 p3 c0 {22,S}
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 F u0 p3 c0 {25,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.05418847, 0.208147084, -0.000242456202, 1.34534795e-07, -2.90873138e-11, -468017.337, 11.7450803], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[41.1570147, 0.0658744682, -4.49530945e-05, 1.36464469e-08, -1.54431174e-12, -476104.738, -174.528492], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (25.39393586260964,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 218,
    label = "PF10acylF",
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
22 C u0 p0 c0 {19,S} {23,S} {24,S} {25,S}
23 F u0 p3 c0 {22,S}
24 F u0 p3 c0 {22,S}
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 F u0 p3 c0 {28,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.18597586, 0.231953456, -0.000270277357, 1.49928496e-07, -3.23983794e-11, -517354.685, 11.1149503], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[45.6671875, 0.0733471722, -5.01451236e-05, 1.52347253e-08, -1.72462792e-12, -526371.473, -196.565211], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (26.489677190308623,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 219,
    label = "PF11acylF",
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
22 C u0 p0 c0 {19,S} {23,S} {24,S} {25,S}
23 F u0 p3 c0 {22,S}
24 F u0 p3 c0 {22,S}
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 F u0 p3 c0 {31,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.31776321, 0.255759828, -0.000298098513, 1.65322198e-07, -3.57094453e-11, -566692.032, 10.4848205], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[50.17736, 0.0808198768, -5.53371533e-05, 1.68230039e-08, -1.90494413e-12, -576638.208, -218.601929], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (27.5854181854291,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 220,
    label = "PF12acylF",
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
22 C u0 p0 c0 {19,S} {23,S} {24,S} {25,S}
23 F u0 p3 c0 {22,S}
24 F u0 p3 c0 {22,S}
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 F u0 p3 c0 {34,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44955059, 0.2795662, -0.000325919668, 1.80715898e-07, -3.90205109e-11, -616029.38, 9.85469059], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[54.6875325, 0.0882925813, -6.05291828e-05, 1.84112825e-08, -2.08526033e-12, -626904.944, -240.638647], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (28.681159429983452,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 221,
    label = "PF13acylF",
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
22 C u0 p0 c0 {19,S} {23,S} {24,S} {25,S}
23 F u0 p3 c0 {22,S}
24 F u0 p3 c0 {22,S}
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 C u0 p0 c0 {34,S} {38,S} {39,S} {40,S}
38 F u0 p3 c0 {37,S}
39 F u0 p3 c0 {37,S}
40 F u0 p3 c0 {37,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58133786, 0.303372573, -0.000353740825, 1.96109601e-07, -4.23315772e-11, -665366.728, 9.22456113], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[59.1977051, 0.0957652858, -6.57212124e-05, 1.99995611e-08, -2.26557653e-12, -677171.679, -262.675366], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (29.77689975994692,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 222,
    label = "PF14acylF",
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
22 C u0 p0 c0 {19,S} {23,S} {24,S} {25,S}
23 F u0 p3 c0 {22,S}
24 F u0 p3 c0 {22,S}
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 C u0 p0 c0 {34,S} {38,S} {39,S} {40,S}
38 F u0 p3 c0 {37,S}
39 F u0 p3 c0 {37,S}
40 C u0 p0 c0 {37,S} {41,S} {42,S} {43,S}
41 F u0 p3 c0 {40,S}
42 F u0 p3 c0 {40,S}
43 F u0 p3 c0 {40,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71312544, 0.327178944, -0.000381561976, 2.11503299e-07, -4.56426418e-11, -714704.075, 8.59443038], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[63.7078777, 0.10323799, -7.09132418e-05, 2.15878396e-08, -2.44589272e-12, -727438.414, -284.712084], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (30.872642667393805,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 223,
    label = "PF15acylF",
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
22 C u0 p0 c0 {19,S} {23,S} {24,S} {25,S}
23 F u0 p3 c0 {22,S}
24 F u0 p3 c0 {22,S}
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 C u0 p0 c0 {34,S} {38,S} {39,S} {40,S}
38 F u0 p3 c0 {37,S}
39 F u0 p3 c0 {37,S}
40 C u0 p0 c0 {37,S} {41,S} {42,S} {43,S}
41 F u0 p3 c0 {40,S}
42 F u0 p3 c0 {40,S}
43 C u0 p0 c0 {40,S} {44,S} {45,S} {46,S}
44 F u0 p3 c0 {43,S}
45 F u0 p3 c0 {43,S}
46 F u0 p3 c0 {43,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84491257, 0.350985318, -0.000409383136, 2.26897005e-07, -4.8953709e-11, -764041.423, 7.96430154], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[68.2180504, 0.110710694, -7.61052712e-05, 2.31761181e-08, -2.62620892e-12, -777705.149, -306.748803], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (31.968381833332504,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 224,
    label = "PF16acylF",
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
22 C u0 p0 c0 {19,S} {23,S} {24,S} {25,S}
23 F u0 p3 c0 {22,S}
24 F u0 p3 c0 {22,S}
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 C u0 p0 c0 {34,S} {38,S} {39,S} {40,S}
38 F u0 p3 c0 {37,S}
39 F u0 p3 c0 {37,S}
40 C u0 p0 c0 {37,S} {41,S} {42,S} {43,S}
41 F u0 p3 c0 {40,S}
42 F u0 p3 c0 {40,S}
43 C u0 p0 c0 {40,S} {44,S} {45,S} {46,S}
44 F u0 p3 c0 {43,S}
45 F u0 p3 c0 {43,S}
46 C u0 p0 c0 {43,S} {47,S} {48,S} {49,S}
47 F u0 p3 c0 {46,S}
48 F u0 p3 c0 {46,S}
49 F u0 p3 c0 {46,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97670003, 0.374791689, -0.000437204289, 2.42290704e-07, -5.2264774e-11, -813378.771, 7.33417126], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[72.7282231, 0.118183398, -8.12973004e-05, 2.47643966e-08, -2.80652511e-12, -827971.884, -328.785522], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (33.06412374304387,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 225,
    label = "PF9alkane",
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 F u0 p3 c0 {26,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.73818789, 0.196924176, -0.000200712077, 9.36169582e-08, -1.61398782e-11, -504299.86, 3.74741768], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[39.3737581, 0.0783843816, -5.37581925e-05, 1.6233158e-08, -1.82354572e-12, -512167.477, -168.228257], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (39.39548608919138,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 226,
    label = "PF10alkane",
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 F u0 p3 c0 {29,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.23600408, 0.217435483, -0.000220837967, 1.02488853e-07, -1.753386e-11, -553160.495, 1.54438182], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[43.1858946, 0.0876356865, -6.01938649e-05, 1.81866864e-08, -2.04328398e-12, -561781.095, -186.898351], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (43.534560191657846,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 227,
    label = "PF11alkane",
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 F u0 p3 c0 {32,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.73382069, 0.237946787, -0.000240963851, 1.11360741e-07, -1.89278394e-11, -602021.13, -0.658655774], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[46.9980311, 0.0968869912, -6.6629537e-05, 2.01402147e-08, -2.26302223e-12, -611394.712, -205.568446], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (47.67363778619862,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 228,
    label = "PF12alkane",
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 F u0 p3 c0 {35,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.23163666, 0.258458095, -0.000261089745, 1.20232639e-07, -2.03218223e-11, -650881.765, -2.8616907], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[50.8101673, 0.106138297, -7.30652098e-05, 2.20937432e-08, -2.48276051e-12, -661008.33, -224.23854], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (51.812710059483315,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 229,
    label = "PF13alkane",
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 C u0 p0 c0 {35,S} {39,S} {40,S} {41,S}
39 F u0 p3 c0 {38,S}
40 F u0 p3 c0 {38,S}
41 F u0 p3 c0 {38,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.7294528, 0.278969403, -0.000281215636, 1.29104534e-07, -2.17158043e-11, -699742.4, -5.06472634], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[54.6223036, 0.115389602, -7.95008826e-05, 2.40472717e-08, -2.7024988e-12, -710621.947, -242.908634], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (55.95178374622665,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 230,
    label = "PF14alkane",
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 C u0 p0 c0 {35,S} {39,S} {40,S} {41,S}
39 F u0 p3 c0 {38,S}
40 F u0 p3 c0 {38,S}
41 C u0 p0 c0 {38,S} {42,S} {43,S} {44,S}
42 F u0 p3 c0 {41,S}
43 F u0 p3 c0 {41,S}
44 F u0 p3 c0 {41,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.22726901, 0.29948071, -0.000301341527, 1.37976429e-07, -2.31097862e-11, -748603.035, -7.26776231], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[58.43444, 0.124640907, -8.59365551e-05, 2.60008001e-08, -2.92223707e-12, -760235.564, -261.578728], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (60.09085801498237,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 231,
    label = "PF15alkane",
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 C u0 p0 c0 {35,S} {39,S} {40,S} {41,S}
39 F u0 p3 c0 {38,S}
40 F u0 p3 c0 {38,S}
41 C u0 p0 c0 {38,S} {42,S} {43,S} {44,S}
42 F u0 p3 c0 {41,S}
43 F u0 p3 c0 {41,S}
44 C u0 p0 c0 {41,S} {45,S} {46,S} {47,S}
45 F u0 p3 c0 {44,S}
46 F u0 p3 c0 {44,S}
47 F u0 p3 c0 {44,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.72508543, 0.319992015, -0.000321467413, 1.4684832e-07, -2.45037666e-11, -797463.67, -9.47079915], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[62.2465764, 0.133892212, -9.23722274e-05, 2.79543285e-08, -3.14197532e-12, -809849.182, -280.248823], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (64.22993402977525,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 232,
    label = "PF16alkane",
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 C u0 p0 c0 {35,S} {39,S} {40,S} {41,S}
39 F u0 p3 c0 {38,S}
40 F u0 p3 c0 {38,S}
41 C u0 p0 c0 {38,S} {42,S} {43,S} {44,S}
42 F u0 p3 c0 {41,S}
43 F u0 p3 c0 {41,S}
44 C u0 p0 c0 {41,S} {45,S} {46,S} {47,S}
45 F u0 p3 c0 {44,S}
46 F u0 p3 c0 {44,S}
47 C u0 p0 c0 {44,S} {48,S} {49,S} {50,S}
48 F u0 p3 c0 {47,S}
49 F u0 p3 c0 {47,S}
50 F u0 p3 c0 {47,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.22290163, 0.340503322, -0.000341593304, 1.55720214e-07, -2.58977482e-11, -846324.305, -11.673835], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[66.0587127, 0.143143517, -9.88079001e-05, 2.99078569e-08, -3.3617136e-12, -859462.799, -298.918917], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (68.36900821538634,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 233,
    label = "PF8-1H",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {26,S}
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
26 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.09222386, 0.168267383, -0.00016325143, 7.06145845e-08, -1.06575238e-11, -428087.283, 7.22264904], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[34.4376688, 0.0684547967, -4.60793902e-05, 1.37596075e-08, -1.53335233e-12, -435194.871, -144.499076], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (34.02464230908476,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 234,
    label = "PF9-1H",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {29,S}
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 F u0 p3 c0 {25,S}
29 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.49071465, 0.189214504, -0.000183879245, 7.96721723e-08, -1.20729497e-11, -477256.649, 5.41314805], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[38.5960523, 0.0769807295, -5.19941549e-05, 1.55472765e-08, -1.73353296e-12, -485243.456, -165.096837], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (37.33787908621811,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 235,
    label = "PF10-1H",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {32,S}
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 F u0 p3 c0 {28,S}
32 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.88920561, 0.210161624, -0.000204507057, 8.87297569e-08, -1.34883746e-11, -526426.016, 3.60364639], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[42.7544361, 0.0855066613, -5.79089187e-05, 1.73349452e-08, -1.93371355e-12, -535292.04, -185.694601], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (40.65111727681011,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 236,
    label = "PF11-1H",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {35,S}
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 F u0 p3 c0 {31,S}
35 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.28769656, 0.231108744, -0.000225134869, 9.77873421e-08, -1.49037996e-11, -575595.382, 1.79414475], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[46.9128195, 0.0940325944, -6.38236836e-05, 1.91226143e-08, -2.13389419e-12, -585340.624, -206.292362], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (43.96435538425747,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 237,
    label = "PF12-1H",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {38,S}
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 F u0 p3 c0 {34,S}
38 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.68618768, 0.252055862, -0.000245762678, 1.06844924e-07, -1.63192235e-11, -624764.748, -0.0153575845], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[51.0712033, 0.102558526, -6.97384473e-05, 2.0910283e-08, -2.33407477e-12, -635389.209, -226.890125], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (47.2775949051635,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 238,
    label = "PF13-1H",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {41,S}
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 C u0 p0 c0 {34,S} {38,S} {39,S} {40,S}
38 F u0 p3 c0 {37,S}
39 F u0 p3 c0 {37,S}
40 F u0 p3 c0 {37,S}
41 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.08467805, 0.273002986, -0.0002663905, 1.15902519e-07, -1.77346518e-11, -673934.114, -1.8248568], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[55.2295871, 0.111084458, -7.56532112e-05, 2.26979517e-08, -2.53425537e-12, -685437.793, -247.487888], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (50.59082819022255,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 239,
    label = "PF14-1H",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {44,S}
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 C u0 p0 c0 {34,S} {38,S} {39,S} {40,S}
38 F u0 p3 c0 {37,S}
39 F u0 p3 c0 {37,S}
40 C u0 p0 c0 {37,S} {41,S} {42,S} {43,S}
41 F u0 p3 c0 {40,S}
42 F u0 p3 c0 {40,S}
43 F u0 p3 c0 {40,S}
44 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.48316906, 0.293950106, -0.000287018311, 1.24960103e-07, -1.91500764e-11, -723103.481, -3.63435866], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[59.3879707, 0.119610391, -8.15679756e-05, 2.44856206e-08, -2.73443598e-12, -735486.378, -268.08565], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (53.90406679653768,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 240,
    label = "PF15-1H",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {47,S}
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 C u0 p0 c0 {34,S} {38,S} {39,S} {40,S}
38 F u0 p3 c0 {37,S}
39 F u0 p3 c0 {37,S}
40 C u0 p0 c0 {37,S} {41,S} {42,S} {43,S}
41 F u0 p3 c0 {40,S}
42 F u0 p3 c0 {40,S}
43 C u0 p0 c0 {40,S} {44,S} {45,S} {46,S}
44 F u0 p3 c0 {43,S}
45 F u0 p3 c0 {43,S}
46 F u0 p3 c0 {43,S}
47 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.88166015, 0.314897225, -0.000307646121, 1.34017685e-07, -2.05655005e-11, -772272.847, -5.44386087], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[63.546354, 0.128136324, -8.74827406e-05, 2.62732897e-08, -2.93461663e-12, -785534.962, -288.683411], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (57.21730606800982,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 241,
    label = "PF16-1H",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {50,S}
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 C u0 p0 c0 {34,S} {38,S} {39,S} {40,S}
38 F u0 p3 c0 {37,S}
39 F u0 p3 c0 {37,S}
40 C u0 p0 c0 {37,S} {41,S} {42,S} {43,S}
41 F u0 p3 c0 {40,S}
42 F u0 p3 c0 {40,S}
43 C u0 p0 c0 {40,S} {44,S} {45,S} {46,S}
44 F u0 p3 c0 {43,S}
45 F u0 p3 c0 {43,S}
46 C u0 p0 c0 {43,S} {47,S} {48,S} {49,S}
47 F u0 p3 c0 {46,S}
48 F u0 p3 c0 {46,S}
49 F u0 p3 c0 {46,S}
50 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.28015085, 0.335844346, -0.000328273937, 1.43075275e-07, -2.19809272e-11, -821442.213, -7.25336149], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[67.7047375, 0.136662257, -9.33975051e-05, 2.80609587e-08, -3.13479725e-12, -835583.546, -309.281172], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (60.53054209684154,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 242,
    label = "PF8ene",
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
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 F u0 p3 c0 {21,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57612422, 0.171455908, -0.000196198389, 1.06608131e-07, -2.24062494e-11, -387015.062, 11.103662], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[34.4407181, 0.0566265051, -3.83150416e-05, 1.15915424e-08, -1.30944975e-12, -393557.95, -139.815674], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (29.733551145062414,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 243,
    label = "PF9ene",
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
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 C u0 p0 c0 {21,S} {25,S} {26,S} {27,S}
25 F u0 p3 c0 {24,S}
26 F u0 p3 c0 {24,S}
27 F u0 p3 c0 {24,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71584342, 0.194666431, -0.000222420271, 1.20312921e-07, -2.5099979e-11, -437360.931, 10.6610359], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[38.7440096, 0.0644228332, -4.37500463e-05, 1.32592165e-08, -1.49908818e-12, -444780.792, -160.612134], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (30.895241210500693,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 244,
    label = "PF10ene",
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
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 C u0 p0 c0 {21,S} {25,S} {26,S} {27,S}
25 F u0 p3 c0 {24,S}
26 F u0 p3 c0 {24,S}
27 C u0 p0 c0 {24,S} {28,S} {29,S} {30,S}
28 F u0 p3 c0 {27,S}
29 F u0 p3 c0 {27,S}
30 F u0 p3 c0 {27,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85556248, 0.217876955, -0.000248642156, 1.34017714e-07, -2.77937093e-11, -487706.799, 10.2184104], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[43.0473012, 0.0722191614, -4.91850509e-05, 1.49268906e-08, -1.68872661e-12, -496003.633, -181.408593], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (32.0569301119142,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 245,
    label = "PF11ene",
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
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 C u0 p0 c0 {21,S} {25,S} {26,S} {27,S}
25 F u0 p3 c0 {24,S}
26 F u0 p3 c0 {24,S}
27 C u0 p0 c0 {24,S} {28,S} {29,S} {30,S}
28 F u0 p3 c0 {27,S}
29 F u0 p3 c0 {27,S}
30 C u0 p0 c0 {27,S} {31,S} {32,S} {33,S}
31 F u0 p3 c0 {30,S}
32 F u0 p3 c0 {30,S}
33 F u0 p3 c0 {30,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99528242, 0.241087473, -0.000274864026, 1.47722492e-07, -3.04874345e-11, -538052.667, 9.77578123], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[47.3505928, 0.0800154893, -5.46200554e-05, 1.65945647e-08, -1.87836503e-12, -547226.475, -202.205054], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (33.21862633005482,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 246,
    label = "PF12ene",
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
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 C u0 p0 c0 {21,S} {25,S} {26,S} {27,S}
25 F u0 p3 c0 {24,S}
26 F u0 p3 c0 {24,S}
27 C u0 p0 c0 {24,S} {28,S} {29,S} {30,S}
28 F u0 p3 c0 {27,S}
29 F u0 p3 c0 {27,S}
30 C u0 p0 c0 {27,S} {31,S} {32,S} {33,S}
31 F u0 p3 c0 {30,S}
32 F u0 p3 c0 {30,S}
33 C u0 p0 c0 {30,S} {34,S} {35,S} {36,S}
34 F u0 p3 c0 {33,S}
35 F u0 p3 c0 {33,S}
36 F u0 p3 c0 {33,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.13500137, 0.264297997, -0.000301085913, 1.61427286e-07, -3.31811653e-11, -588398.535, 9.33315619], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[51.6538844, 0.0878118174, -6.005506e-05, 1.82622387e-08, -2.06800346e-12, -598449.317, -223.001514], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (34.38031431687744,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 247,
    label = "PF13ene",
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
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 C u0 p0 c0 {21,S} {25,S} {26,S} {27,S}
25 F u0 p3 c0 {24,S}
26 F u0 p3 c0 {24,S}
27 C u0 p0 c0 {24,S} {28,S} {29,S} {30,S}
28 F u0 p3 c0 {27,S}
29 F u0 p3 c0 {27,S}
30 C u0 p0 c0 {27,S} {31,S} {32,S} {33,S}
31 F u0 p3 c0 {30,S}
32 F u0 p3 c0 {30,S}
33 C u0 p0 c0 {30,S} {34,S} {35,S} {36,S}
34 F u0 p3 c0 {33,S}
35 F u0 p3 c0 {33,S}
36 C u0 p0 c0 {33,S} {37,S} {38,S} {39,S}
37 F u0 p3 c0 {36,S}
38 F u0 p3 c0 {36,S}
39 F u0 p3 c0 {36,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.27472069, 0.287508519, -0.000327307794, 1.75132074e-07, -3.58748942e-11, -638744.403, 8.89052954], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[55.9571759, 0.0956081456, -6.54900647e-05, 1.99299128e-08, -2.25764189e-12, -649672.158, -243.797973], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (35.54200538005122,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 248,
    label = "PF14ene",
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
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 C u0 p0 c0 {21,S} {25,S} {26,S} {27,S}
25 F u0 p3 c0 {24,S}
26 F u0 p3 c0 {24,S}
27 C u0 p0 c0 {24,S} {28,S} {29,S} {30,S}
28 F u0 p3 c0 {27,S}
29 F u0 p3 c0 {27,S}
30 C u0 p0 c0 {27,S} {31,S} {32,S} {33,S}
31 F u0 p3 c0 {30,S}
32 F u0 p3 c0 {30,S}
33 C u0 p0 c0 {30,S} {34,S} {35,S} {36,S}
34 F u0 p3 c0 {33,S}
35 F u0 p3 c0 {33,S}
36 C u0 p0 c0 {33,S} {37,S} {38,S} {39,S}
37 F u0 p3 c0 {36,S}
38 F u0 p3 c0 {36,S}
39 C u0 p0 c0 {36,S} {40,S} {41,S} {42,S}
40 F u0 p3 c0 {39,S}
41 F u0 p3 c0 {39,S}
42 F u0 p3 c0 {39,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.41443966, 0.310719044, -0.00035352968, 1.88836868e-07, -3.85686249e-11, -689090.272, 8.44790443], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[60.2604675, 0.103404474, -7.09250693e-05, 2.15975869e-08, -2.44728032e-12, -700895.0, -264.594433], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (36.703693533163104,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 249,
    label = "PF15ene",
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
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 C u0 p0 c0 {21,S} {25,S} {26,S} {27,S}
25 F u0 p3 c0 {24,S}
26 F u0 p3 c0 {24,S}
27 C u0 p0 c0 {24,S} {28,S} {29,S} {30,S}
28 F u0 p3 c0 {27,S}
29 F u0 p3 c0 {27,S}
30 C u0 p0 c0 {27,S} {31,S} {32,S} {33,S}
31 F u0 p3 c0 {30,S}
32 F u0 p3 c0 {30,S}
33 C u0 p0 c0 {30,S} {34,S} {35,S} {36,S}
34 F u0 p3 c0 {33,S}
35 F u0 p3 c0 {33,S}
36 C u0 p0 c0 {33,S} {37,S} {38,S} {39,S}
37 F u0 p3 c0 {36,S}
38 F u0 p3 c0 {36,S}
39 C u0 p0 c0 {36,S} {40,S} {41,S} {42,S}
40 F u0 p3 c0 {39,S}
41 F u0 p3 c0 {39,S}
42 C u0 p0 c0 {39,S} {43,S} {44,S} {45,S}
43 F u0 p3 c0 {42,S}
44 F u0 p3 c0 {42,S}
45 F u0 p3 c0 {42,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.55415997, 0.333929559, -0.000379751544, 2.0254164e-07, -4.1262348e-11, -739436.14, 8.00527367], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[64.563759, 0.111200802, -7.63600741e-05, 2.32652611e-08, -2.63691876e-12, -752117.841, -285.390893], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (37.86539282765488,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 250,
    label = "PF16ene",
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
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 C u0 p0 c0 {21,S} {25,S} {26,S} {27,S}
25 F u0 p3 c0 {24,S}
26 F u0 p3 c0 {24,S}
27 C u0 p0 c0 {24,S} {28,S} {29,S} {30,S}
28 F u0 p3 c0 {27,S}
29 F u0 p3 c0 {27,S}
30 C u0 p0 c0 {27,S} {31,S} {32,S} {33,S}
31 F u0 p3 c0 {30,S}
32 F u0 p3 c0 {30,S}
33 C u0 p0 c0 {30,S} {34,S} {35,S} {36,S}
34 F u0 p3 c0 {33,S}
35 F u0 p3 c0 {33,S}
36 C u0 p0 c0 {33,S} {37,S} {38,S} {39,S}
37 F u0 p3 c0 {36,S}
38 F u0 p3 c0 {36,S}
39 C u0 p0 c0 {36,S} {40,S} {41,S} {42,S}
40 F u0 p3 c0 {39,S}
41 F u0 p3 c0 {39,S}
42 C u0 p0 c0 {39,S} {43,S} {44,S} {45,S}
43 F u0 p3 c0 {42,S}
44 F u0 p3 c0 {42,S}
45 C u0 p0 c0 {42,S} {46,S} {47,S} {48,S}
46 F u0 p3 c0 {45,S}
47 F u0 p3 c0 {45,S}
48 F u0 p3 c0 {45,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.69387769, 0.357140092, -0.000405973451, 2.16246455e-07, -4.39560858e-11, -789782.008, 7.56265376], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[68.8670507, 0.11899713, -8.17950785e-05, 2.49329351e-08, -2.82655718e-12, -803340.683, -306.187354], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (39.027070587688485,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 251,
    label = "PF8ol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {27,S}
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
27 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.43120286, 0.175856991, -0.000172312455, 7.5227014e-08, -1.14700618e-11, -455293.08, 3.90285253], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[36.6922064, 0.0693901769, -4.68272193e-05, 1.40150041e-08, -1.56563098e-12, -462826.972, -157.296173], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (36.843070532923726,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 252,
    label = "PF9ol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {30,S}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 F u0 p3 c0 {26,S}
30 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.05097933, 0.194936753, -0.000188187572, 7.98542361e-08, -1.14753533e-11, -504863.319, 0.840741282], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[40.8939683, 0.0779881167, -5.27754774e-05, 1.58052447e-08, -1.76551719e-12, -513299.074, -178.589061], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (41.9961788243497,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 253,
    label = "PF10ol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {33,S}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 F u0 p3 c0 {29,S}
33 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.67075541, 0.214016517, -0.000204062695, 8.44814655e-08, -1.14806473e-11, -554433.559, -2.22136838], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[45.0957293, 0.0865860586, -5.87237374e-05, 1.7595486e-08, -1.9654035e-12, -563771.176, -199.881945], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (47.14928387313525,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 254,
    label = "PF11ol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {36,S}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 F u0 p3 c0 {32,S}
36 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.29053198, 0.233096278, -0.000219937809, 8.91086853e-08, -1.14859379e-11, -604003.798, -5.28348003], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[49.2974907, 0.0951839998, -6.46719968e-05, 1.93857271e-08, -2.16528977e-12, -614243.279, -221.17483], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (52.30239299600749,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 255,
    label = "PF12ol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {39,S}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 F u0 p3 c0 {35,S}
39 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.91030828, 0.252176041, -0.000235812929, 9.37359114e-08, -1.14912308e-11, -653574.038, -8.34559062], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[53.4992526, 0.10378194, -7.0620255e-05, 2.11759677e-08, -2.36517599e-12, -664715.381, -242.467718], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (57.45549987397481,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 256,
    label = "PF13ol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {42,S}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 C u0 p0 c0 {35,S} {39,S} {40,S} {41,S}
39 F u0 p3 c0 {38,S}
40 F u0 p3 c0 {38,S}
41 F u0 p3 c0 {38,S}
42 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.53008465, 0.271255803, -0.000251688046, 9.83631338e-08, -1.14965223e-11, -703144.277, -11.4077014], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[57.7010139, 0.112379881, -7.65685143e-05, 2.29662088e-08, -2.56506227e-12, -715187.484, -263.760604], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (62.608607333954524,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 257,
    label = "PF14ol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {45,S}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 C u0 p0 c0 {35,S} {39,S} {40,S} {41,S}
39 F u0 p3 c0 {38,S}
40 F u0 p3 c0 {38,S}
41 C u0 p0 c0 {38,S} {42,S} {43,S} {44,S}
42 F u0 p3 c0 {41,S}
43 F u0 p3 c0 {41,S}
44 F u0 p3 c0 {41,S}
45 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.14986074, 0.290335567, -0.00026756317, 1.02990363e-07, -1.15018164e-11, -752714.517, -14.4698111], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[61.9027755, 0.120977822, -8.25167733e-05, 2.47564497e-08, -2.76494852e-12, -765659.586, -285.05349], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (67.7617124658847,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 258,
    label = "PF15ol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {48,S}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 C u0 p0 c0 {35,S} {39,S} {40,S} {41,S}
39 F u0 p3 c0 {38,S}
40 F u0 p3 c0 {38,S}
41 C u0 p0 c0 {38,S} {42,S} {43,S} {44,S}
42 F u0 p3 c0 {41,S}
43 F u0 p3 c0 {41,S}
44 C u0 p0 c0 {41,S} {45,S} {46,S} {47,S}
45 F u0 p3 c0 {44,S}
46 F u0 p3 c0 {44,S}
47 F u0 p3 c0 {44,S}
48 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.76963716, 0.309415329, -0.000283438286, 1.07617586e-07, -1.15071079e-11, -802284.756, -17.5319222], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[66.1045375, 0.129575761, -8.84650311e-05, 2.65466902e-08, -2.96483473e-12, -816131.688, -306.346379], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (72.91482034158754,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 259,
    label = "PF16ol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {51,S}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 C u0 p0 c0 {35,S} {39,S} {40,S} {41,S}
39 F u0 p3 c0 {38,S}
40 F u0 p3 c0 {38,S}
41 C u0 p0 c0 {38,S} {42,S} {43,S} {44,S}
42 F u0 p3 c0 {41,S}
43 F u0 p3 c0 {41,S}
44 C u0 p0 c0 {41,S} {45,S} {46,S} {47,S}
45 F u0 p3 c0 {44,S}
46 F u0 p3 c0 {44,S}
47 C u0 p0 c0 {44,S} {48,S} {49,S} {50,S}
48 F u0 p3 c0 {47,S}
49 F u0 p3 c0 {47,S}
50 F u0 p3 c0 {47,S}
51 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.38941362, 0.328495091, -0.000299313404, 1.1224481e-07, -1.15124001e-11, -851854.996, -20.5940334], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[70.3062989, 0.138173702, -9.44132903e-05, 2.83369312e-08, -3.16472099e-12, -866603.791, -327.639265], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (78.06792854986888,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 260,
    label = "PF8diol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {27,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  O u0 p2 c0 {2,S} {28,S}
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
27 H u0 p0 c0 {1,S}
28 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.62354823, 0.175649501, -0.000168206794, 7.15762271e-08, -1.04464213e-11, -454669.051, 2.72160401], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[36.0936181, 0.0726301619, -4.8302278e-05, 1.43401262e-08, -1.59392299e-12, -462059.097, -154.73328], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (38.442318921563576,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 261,
    label = "PF9diol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {30,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  O u0 p2 c0 {2,S} {31,S}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 F u0 p3 c0 {26,S}
30 H u0 p0 c0 {1,S}
31 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.45816448, 0.193174569, -0.000181221324, 7.40846588e-08, -9.88280876e-12, -504684.146, -1.14277709], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[40.1020438, 0.081479336, -5.43501235e-05, 1.61426249e-08, -1.79366535e-12, -512903.129, -174.902859], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (45.38170453269181,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 262,
    label = "PF10diol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {33,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  O u0 p2 c0 {2,S} {34,S}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 F u0 p3 c0 {29,S}
33 H u0 p0 c0 {1,S}
34 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.29278074, 0.210699638, -0.000194235854, 7.65930901e-08, -9.3191961e-12, -554699.241, -5.00715822], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[44.1104696, 0.0903285101, -6.03979689e-05, 1.79451235e-08, -1.9934077e-12, -563747.16, -195.072438], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (52.32109022696469,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 263,
    label = "PF11diol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {36,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  O u0 p2 c0 {2,S} {37,S}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 F u0 p3 c0 {32,S}
36 H u0 p0 c0 {1,S}
37 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.12739748, 0.228224702, -0.000207250376, 7.91015131e-08, -8.75558054e-12, -604714.335, -8.87154137], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[48.1188955, 0.0991776841, -6.64458143e-05, 1.97476221e-08, -2.19315005e-12, -614591.191, -215.242018], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (59.26047991217961,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 264,
    label = "PF12diol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {39,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  O u0 p2 c0 {2,S} {40,S}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 F u0 p3 c0 {35,S}
39 H u0 p0 c0 {1,S}
40 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.96201385, 0.24574977, -0.000220264904, 8.16099427e-08, -8.19196732e-12, -654729.43, -12.7359229], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[52.1273222, 0.108026856, -7.24936579e-05, 2.155012e-08, -2.39289231e-12, -665435.223, -235.411602], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (66.19986652104335,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 265,
    label = "PF13diol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {42,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  O u0 p2 c0 {2,S} {43,S}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 C u0 p0 c0 {35,S} {39,S} {40,S} {41,S}
39 F u0 p3 c0 {38,S}
40 F u0 p3 c0 {38,S}
41 F u0 p3 c0 {38,S}
42 H u0 p0 c0 {1,S}
43 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.79663039, 0.263274836, -0.000233279429, 8.41183688e-08, -7.6283528e-12, -704744.525, -16.6003052], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[56.1357476, 0.116876031, -7.8541504e-05, 2.33526189e-08, -2.5926347e-12, -716279.254, -255.581179], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (73.13925454336577,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 266,
    label = "PF14diol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {45,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  O u0 p2 c0 {2,S} {46,S}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 C u0 p0 c0 {35,S} {39,S} {40,S} {41,S}
39 F u0 p3 c0 {38,S}
40 F u0 p3 c0 {38,S}
41 C u0 p0 c0 {38,S} {42,S} {43,S} {44,S}
42 F u0 p3 c0 {41,S}
43 F u0 p3 c0 {41,S}
44 F u0 p3 c0 {41,S}
45 H u0 p0 c0 {1,S}
46 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.63124701, 0.280799901, -0.000246293952, 8.66267928e-08, -7.06473754e-12, -754759.62, -20.4646878], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[60.1441735, 0.125725205, -8.45893494e-05, 2.51551175e-08, -2.79237705e-12, -767123.286, -275.750759], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (80.07864323084516,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 267,
    label = "PF15diol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {48,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  O u0 p2 c0 {2,S} {49,S}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 C u0 p0 c0 {35,S} {39,S} {40,S} {41,S}
39 F u0 p3 c0 {38,S}
40 F u0 p3 c0 {38,S}
41 C u0 p0 c0 {38,S} {42,S} {43,S} {44,S}
42 F u0 p3 c0 {41,S}
43 F u0 p3 c0 {41,S}
44 C u0 p0 c0 {41,S} {45,S} {46,S} {47,S}
45 F u0 p3 c0 {44,S}
46 F u0 p3 c0 {44,S}
47 F u0 p3 c0 {44,S}
48 H u0 p0 c0 {1,S}
49 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.4658627, 0.298324974, -0.000259308494, 8.91352364e-08, -6.50112924e-12, -804774.714, -24.3290665], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[64.1525993, 0.134574379, -9.06371949e-05, 2.69576161e-08, -2.9921194e-12, -817967.317, -295.920338], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (87.01802418587434,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 268,
    label = "PF16diol",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {51,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  O u0 p2 c0 {2,S} {52,S}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 C u0 p0 c0 {35,S} {39,S} {40,S} {41,S}
39 F u0 p3 c0 {38,S}
40 F u0 p3 c0 {38,S}
41 C u0 p0 c0 {38,S} {42,S} {43,S} {44,S}
42 F u0 p3 c0 {41,S}
43 F u0 p3 c0 {41,S}
44 C u0 p0 c0 {41,S} {45,S} {46,S} {47,S}
45 F u0 p3 c0 {44,S}
46 F u0 p3 c0 {44,S}
47 C u0 p0 c0 {44,S} {48,S} {49,S} {50,S}
48 F u0 p3 c0 {47,S}
49 F u0 p3 c0 {47,S}
50 F u0 p3 c0 {47,S}
51 H u0 p0 c0 {1,S}
52 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.3004795, 0.315850038, -0.000272323013, 9.16436569e-08, -5.93751283e-12, -854789.809, -28.1934502], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[68.1610255, 0.143423552, -9.66850394e-05, 2.87601144e-08, -3.19186171e-12, -868811.348, -316.08992], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (93.95741436995701,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 269,
    label = "PF9lactone",
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
24 C u0 p0 c0 {21,S} {25,S} {26,S} {27,S}
25 F u0 p3 c0 {24,S}
26 F u0 p3 c0 {24,S}
27 F u0 p3 c0 {24,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83295958, 0.184695413, -0.000189743514, 8.86319538e-08, -1.5160005e-11, -420842.701, 9.62874944], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[38.5107451, 0.0671757714, -4.56543982e-05, 1.37377631e-08, -1.54005538e-12, -428790.813, -162.88208], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (31.86899914480234,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 270,
    label = "PF10lactone",
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
24 C u0 p0 c0 {21,S} {25,S} {26,S} {27,S}
25 F u0 p3 c0 {24,S}
26 F u0 p3 c0 {24,S}
27 C u0 p0 c0 {24,S} {28,S} {29,S} {30,S}
28 F u0 p3 c0 {27,S}
29 F u0 p3 c0 {27,S}
30 F u0 p3 c0 {27,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.22485471, 0.205586417, -0.000209995151, 9.70807591e-08, -1.63127953e-11, -470880.124, 7.91161567], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[42.8833048, 0.0751974898, -5.12228406e-05, 1.54247222e-08, -1.72933262e-12, -479770.897, -184.555912], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (35.12739655342365,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 271,
    label = "PF11lactone",
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
24 C u0 p0 c0 {21,S} {25,S} {26,S} {27,S}
25 F u0 p3 c0 {24,S}
26 F u0 p3 c0 {24,S}
27 C u0 p0 c0 {24,S} {28,S} {29,S} {30,S}
28 F u0 p3 c0 {27,S}
29 F u0 p3 c0 {27,S}
30 C u0 p0 c0 {27,S} {31,S} {32,S} {33,S}
31 F u0 p3 c0 {30,S}
32 F u0 p3 c0 {30,S}
33 F u0 p3 c0 {30,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.61674961, 0.226477422, -0.000230246792, 1.05529568e-07, -1.74655867e-11, -520917.547, 6.19448285], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[47.2558646, 0.083219208, -5.67912829e-05, 1.71116813e-08, -1.91860985e-12, -530750.981, -206.229744], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (38.38579204971855,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 272,
    label = "PF12lactone",
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
24 C u0 p0 c0 {21,S} {25,S} {26,S} {27,S}
25 F u0 p3 c0 {24,S}
26 F u0 p3 c0 {24,S}
27 C u0 p0 c0 {24,S} {28,S} {29,S} {30,S}
28 F u0 p3 c0 {27,S}
29 F u0 p3 c0 {27,S}
30 C u0 p0 c0 {27,S} {31,S} {32,S} {33,S}
31 F u0 p3 c0 {30,S}
32 F u0 p3 c0 {30,S}
33 C u0 p0 c0 {30,S} {34,S} {35,S} {36,S}
34 F u0 p3 c0 {33,S}
35 F u0 p3 c0 {33,S}
36 F u0 p3 c0 {33,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.00864476, 0.247368426, -0.00025049843, 1.13978373e-07, -1.8618377e-11, -570954.97, 4.47734899], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[51.6284237, 0.0912409278, -6.23597265e-05, 1.87986408e-08, -2.10788715e-12, -581731.066, -227.903573], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (41.64418962462911,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 273,
    label = "PF13lactone",
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
24 C u0 p0 c0 {21,S} {25,S} {26,S} {27,S}
25 F u0 p3 c0 {24,S}
26 F u0 p3 c0 {24,S}
27 C u0 p0 c0 {24,S} {28,S} {29,S} {30,S}
28 F u0 p3 c0 {27,S}
29 F u0 p3 c0 {27,S}
30 C u0 p0 c0 {27,S} {31,S} {32,S} {33,S}
31 F u0 p3 c0 {30,S}
32 F u0 p3 c0 {30,S}
33 C u0 p0 c0 {30,S} {34,S} {35,S} {36,S}
34 F u0 p3 c0 {33,S}
35 F u0 p3 c0 {33,S}
36 C u0 p0 c0 {33,S} {37,S} {38,S} {39,S}
37 F u0 p3 c0 {36,S}
38 F u0 p3 c0 {36,S}
39 F u0 p3 c0 {36,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.4005399, 0.26825943, -0.000270750066, 1.22427178e-07, -1.97711667e-11, -620992.393, 2.76021515], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[56.0009833, 0.0992626464, -6.7928169e-05, 2.04856e-08, -2.29716439e-12, -632711.15, -249.577405], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (44.90258711639503,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 274,
    label = "PF14lactone",
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
24 C u0 p0 c0 {21,S} {25,S} {26,S} {27,S}
25 F u0 p3 c0 {24,S}
26 F u0 p3 c0 {24,S}
27 C u0 p0 c0 {24,S} {28,S} {29,S} {30,S}
28 F u0 p3 c0 {27,S}
29 F u0 p3 c0 {27,S}
30 C u0 p0 c0 {27,S} {31,S} {32,S} {33,S}
31 F u0 p3 c0 {30,S}
32 F u0 p3 c0 {30,S}
33 C u0 p0 c0 {30,S} {34,S} {35,S} {36,S}
34 F u0 p3 c0 {33,S}
35 F u0 p3 c0 {33,S}
36 C u0 p0 c0 {33,S} {37,S} {38,S} {39,S}
37 F u0 p3 c0 {36,S}
38 F u0 p3 c0 {36,S}
39 C u0 p0 c0 {36,S} {40,S} {41,S} {42,S}
40 F u0 p3 c0 {39,S}
41 F u0 p3 c0 {39,S}
42 F u0 p3 c0 {39,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.79243528, 0.289150432, -0.000291001699, 1.30875978e-07, -2.09239554e-11, -671029.816, 1.04308032], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[60.3735433, 0.107284364, -7.34966109e-05, 2.21725589e-08, -2.4864416e-12, -683691.234, -271.251238], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (48.160986603632004,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 275,
    label = "PF15lactone",
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
24 C u0 p0 c0 {21,S} {25,S} {26,S} {27,S}
25 F u0 p3 c0 {24,S}
26 F u0 p3 c0 {24,S}
27 C u0 p0 c0 {24,S} {28,S} {29,S} {30,S}
28 F u0 p3 c0 {27,S}
29 F u0 p3 c0 {27,S}
30 C u0 p0 c0 {27,S} {31,S} {32,S} {33,S}
31 F u0 p3 c0 {30,S}
32 F u0 p3 c0 {30,S}
33 C u0 p0 c0 {30,S} {34,S} {35,S} {36,S}
34 F u0 p3 c0 {33,S}
35 F u0 p3 c0 {33,S}
36 C u0 p0 c0 {33,S} {37,S} {38,S} {39,S}
37 F u0 p3 c0 {36,S}
38 F u0 p3 c0 {36,S}
39 C u0 p0 c0 {36,S} {40,S} {41,S} {42,S}
40 F u0 p3 c0 {39,S}
41 F u0 p3 c0 {39,S}
42 C u0 p0 c0 {39,S} {43,S} {44,S} {45,S}
43 F u0 p3 c0 {42,S}
44 F u0 p3 c0 {42,S}
45 F u0 p3 c0 {42,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.18433022, 0.310041437, -0.000311253339, 1.39324787e-07, -2.20767467e-11, -721067.239, -0.674052674], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[64.7461029, 0.115306083, -7.90650534e-05, 2.38595181e-08, -2.67571885e-12, -734671.318, -292.92507], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (51.4193824325054,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 276,
    label = "PF16lactone",
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
24 C u0 p0 c0 {21,S} {25,S} {26,S} {27,S}
25 F u0 p3 c0 {24,S}
26 F u0 p3 c0 {24,S}
27 C u0 p0 c0 {24,S} {28,S} {29,S} {30,S}
28 F u0 p3 c0 {27,S}
29 F u0 p3 c0 {27,S}
30 C u0 p0 c0 {27,S} {31,S} {32,S} {33,S}
31 F u0 p3 c0 {30,S}
32 F u0 p3 c0 {30,S}
33 C u0 p0 c0 {30,S} {34,S} {35,S} {36,S}
34 F u0 p3 c0 {33,S}
35 F u0 p3 c0 {33,S}
36 C u0 p0 c0 {33,S} {37,S} {38,S} {39,S}
37 F u0 p3 c0 {36,S}
38 F u0 p3 c0 {36,S}
39 C u0 p0 c0 {36,S} {40,S} {41,S} {42,S}
40 F u0 p3 c0 {39,S}
41 F u0 p3 c0 {39,S}
42 C u0 p0 c0 {39,S} {43,S} {44,S} {45,S}
43 F u0 p3 c0 {42,S}
44 F u0 p3 c0 {42,S}
45 C u0 p0 c0 {42,S} {46,S} {47,S} {48,S}
46 F u0 p3 c0 {45,S}
47 F u0 p3 c0 {45,S}
48 F u0 p3 c0 {45,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.57622549, 0.33093244, -0.000331504974, 1.4777359e-07, -2.32295361e-11, -771104.662, -2.39118703], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[69.1186624, 0.123327802, -8.46334964e-05, 2.55464774e-08, -2.86499611e-12, -785651.403, -314.598901], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (54.67778100515147,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 277,
    label = "PF9alkylr",
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 F u0 p3 c0 {25,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.23125788, 0.197784178, -0.000214541595, 1.08590151e-07, -2.09909866e-11, -453885.685, 7.03281317], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[40.7785637, 0.0687032992, -4.70776885e-05, 1.42540907e-08, -1.60651602e-12, -462006.732, -173.478871], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (35.180635471026335,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 278,
    label = "PF10alkylr",
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 F u0 p3 c0 {28,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.52429268, 0.219903697, -0.000238052671, 1.20116249e-07, -2.31234142e-11, -503356.929, 5.6561663], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[45.1358107, 0.0766845343, -5.26173722e-05, 1.59381368e-08, -1.79644965e-12, -512391.496, -194.982453], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (37.61706236144434,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 279,
    label = "PF11alkylr",
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 F u0 p3 c0 {31,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.8173275, 0.242023215, -0.000261563746, 1.31642346e-07, -2.52558418e-11, -552828.172, 4.27951933], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[49.4930582, 0.0846657682, -5.81570549e-05, 1.76221824e-08, -1.98638324e-12, -562776.261, -216.486037], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (40.05348941815161,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 280,
    label = "PF12alkylr",
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 F u0 p3 c0 {34,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.11036222, 0.264142735, -0.000285074824, 1.43168446e-07, -2.73882699e-11, -602299.416, 2.90287282], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[53.8503053, 0.0926470032, -6.36967386e-05, 1.93062284e-08, -2.17631687e-12, -613161.025, -237.98962], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (42.48991564341261,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 281,
    label = "PF13alkylr",
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 C u0 p0 c0 {34,S} {38,S} {39,S} {40,S}
38 F u0 p3 c0 {37,S}
39 F u0 p3 c0 {37,S}
40 F u0 p3 c0 {37,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.40339719, 0.286262253, -0.000308585897, 1.54694541e-07, -2.95206966e-11, -651770.66, 1.52622521], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[58.2075526, 0.100628238, -6.92364217e-05, 2.09902742e-08, -2.36625048e-12, -663545.789, -259.493203], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (44.926343947289254,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 282,
    label = "PF14alkylr",
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 C u0 p0 c0 {34,S} {38,S} {39,S} {40,S}
38 F u0 p3 c0 {37,S}
39 F u0 p3 c0 {37,S}
40 C u0 p0 c0 {37,S} {41,S} {42,S} {43,S}
41 F u0 p3 c0 {40,S}
42 F u0 p3 c0 {40,S}
43 F u0 p3 c0 {40,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.6964317, 0.308381774, -0.000332096978, 1.66220644e-07, -3.1653126e-11, -701241.904, 0.149579559], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[62.5647999, 0.108609472, -7.47761047e-05, 2.267432e-08, -2.55618408e-12, -713930.553, -280.996787], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (47.362768426513114,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 283,
    label = "PF15alkylr",
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 C u0 p0 c0 {34,S} {38,S} {39,S} {40,S}
38 F u0 p3 c0 {37,S}
39 F u0 p3 c0 {37,S}
40 C u0 p0 c0 {37,S} {41,S} {42,S} {43,S}
41 F u0 p3 c0 {40,S}
42 F u0 p3 c0 {40,S}
43 C u0 p0 c0 {40,S} {44,S} {45,S} {46,S}
44 F u0 p3 c0 {43,S}
45 F u0 p3 c0 {43,S}
46 F u0 p3 c0 {43,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.98946655, 0.330501292, -0.000355608053, 1.77746741e-07, -3.37855533e-11, -750713.148, -1.22706755], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[66.9220473, 0.116590706, -8.03157877e-05, 2.43583658e-08, -2.74611768e-12, -764315.317, -302.500371], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (49.79919573265426,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 284,
    label = "PF16alkylr",
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
25 C u0 p0 c0 {22,S} {26,S} {27,S} {28,S}
26 F u0 p3 c0 {25,S}
27 F u0 p3 c0 {25,S}
28 C u0 p0 c0 {25,S} {29,S} {30,S} {31,S}
29 F u0 p3 c0 {28,S}
30 F u0 p3 c0 {28,S}
31 C u0 p0 c0 {28,S} {32,S} {33,S} {34,S}
32 F u0 p3 c0 {31,S}
33 F u0 p3 c0 {31,S}
34 C u0 p0 c0 {31,S} {35,S} {36,S} {37,S}
35 F u0 p3 c0 {34,S}
36 F u0 p3 c0 {34,S}
37 C u0 p0 c0 {34,S} {38,S} {39,S} {40,S}
38 F u0 p3 c0 {37,S}
39 F u0 p3 c0 {37,S}
40 C u0 p0 c0 {37,S} {41,S} {42,S} {43,S}
41 F u0 p3 c0 {40,S}
42 F u0 p3 c0 {40,S}
43 C u0 p0 c0 {40,S} {44,S} {45,S} {46,S}
44 F u0 p3 c0 {43,S}
45 F u0 p3 c0 {43,S}
46 C u0 p0 c0 {43,S} {47,S} {48,S} {49,S}
47 F u0 p3 c0 {46,S}
48 F u0 p3 c0 {46,S}
49 F u0 p3 c0 {46,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.28250132, 0.352620811, -0.00037911913, 1.8927284e-07, -3.59179812e-11, -800184.391, -2.60371431], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[71.2792944, 0.124571941, -8.58554713e-05, 2.60424118e-08, -2.93605131e-12, -814700.081, -324.003953], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (52.235622373638385,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 285,
    label = "PF8alkyl(s)",
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
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 F u0 p3 c0 {21,S}""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44667589, 0.178423116, -0.000215060984, 1.2412417e-07, -2.79913791e-11, -357621.47, 9.4178231], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[36.0757586, 0.0534438163, -3.640672e-05, 1.10766441e-08, -1.25792668e-12, -364397.133, -149.324582], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (28.657257844295046,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 286,
    label = "PF9alkyl(s)",
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
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 C u0 p0 c0 {21,S} {25,S} {26,S} {27,S}
25 F u0 p3 c0 {24,S}
26 F u0 p3 c0 {24,S}
27 F u0 p3 c0 {24,S}""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66064623, 0.202487086, -0.000244433576, 1.4123084e-07, -3.1880301e-11, -407041.924, 8.16450601], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[40.7204045, 0.0604438204, -4.12414436e-05, 1.25573609e-08, -1.42673567e-12, -414733.104, -172.110267], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (30.436306237618588,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 287,
    label = "PF10alkyl(s)",
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
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 C u0 p0 c0 {21,S} {25,S} {26,S} {27,S}
25 F u0 p3 c0 {24,S}
26 F u0 p3 c0 {24,S}
27 C u0 p0 c0 {24,S} {28,S} {29,S} {30,S}
28 F u0 p3 c0 {27,S}
29 F u0 p3 c0 {27,S}
30 F u0 p3 c0 {27,S}""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87461658, 0.226551056, -0.000273806168, 1.58337511e-07, -3.5769223e-11, -456462.378, 6.91118893], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[45.36505, 0.0674438256, -4.6076168e-05, 1.40380781e-08, -1.59554471e-12, -465069.074, -194.89595], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (32.21535471408676,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 288,
    label = "PF11alkyl(s)",
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
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 C u0 p0 c0 {21,S} {25,S} {26,S} {27,S}
25 F u0 p3 c0 {24,S}
26 F u0 p3 c0 {24,S}
27 C u0 p0 c0 {24,S} {28,S} {29,S} {30,S}
28 F u0 p3 c0 {27,S}
29 F u0 p3 c0 {27,S}
30 C u0 p0 c0 {27,S} {31,S} {32,S} {33,S}
31 F u0 p3 c0 {30,S}
32 F u0 p3 c0 {30,S}
33 F u0 p3 c0 {30,S}""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08858694, 0.250615026, -0.000303178759, 1.7544418e-07, -3.96581448e-11, -505882.832, 5.65787175], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[50.0096961, 0.0744438295, -5.09108914e-05, 1.55187948e-08, -1.76435369e-12, -515405.044, -217.681636], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (33.99440327369955,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 289,
    label = "PF12alkyl(s)",
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
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 C u0 p0 c0 {21,S} {25,S} {26,S} {27,S}
25 F u0 p3 c0 {24,S}
26 F u0 p3 c0 {24,S}
27 C u0 p0 c0 {24,S} {28,S} {29,S} {30,S}
28 F u0 p3 c0 {27,S}
29 F u0 p3 c0 {27,S}
30 C u0 p0 c0 {27,S} {31,S} {32,S} {33,S}
31 F u0 p3 c0 {30,S}
32 F u0 p3 c0 {30,S}
33 C u0 p0 c0 {30,S} {34,S} {35,S} {36,S}
34 F u0 p3 c0 {33,S}
35 F u0 p3 c0 {33,S}
36 F u0 p3 c0 {33,S}""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.3025573, 0.274678996, -0.000332551351, 1.9255085e-07, -4.35470667e-11, -555303.286, 4.40455459], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[54.6543423, 0.0814438329, -5.57456143e-05, 1.69995114e-08, -1.93316265e-12, -565741.015, -240.467323], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (35.77345183331234,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 290,
    label = "PF13alkyl(s)",
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
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 C u0 p0 c0 {21,S} {25,S} {26,S} {27,S}
25 F u0 p3 c0 {24,S}
26 F u0 p3 c0 {24,S}
27 C u0 p0 c0 {24,S} {28,S} {29,S} {30,S}
28 F u0 p3 c0 {27,S}
29 F u0 p3 c0 {27,S}
30 C u0 p0 c0 {27,S} {31,S} {32,S} {33,S}
31 F u0 p3 c0 {30,S}
32 F u0 p3 c0 {30,S}
33 C u0 p0 c0 {30,S} {34,S} {35,S} {36,S}
34 F u0 p3 c0 {33,S}
35 F u0 p3 c0 {33,S}
36 C u0 p0 c0 {33,S} {37,S} {38,S} {39,S}
37 F u0 p3 c0 {36,S}
38 F u0 p3 c0 {36,S}
39 F u0 p3 c0 {36,S}""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.51652769, 0.298742965, -0.000361923942, 2.0965752e-07, -4.74359883e-11, -604723.74, 3.15123729], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[59.2989881, 0.0884438375, -6.05803382e-05, 1.84802284e-08, -2.10197166e-12, -616076.985, -263.253007], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (37.55250064235901,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 291,
    label = "PF14alkyl(s)",
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
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 C u0 p0 c0 {21,S} {25,S} {26,S} {27,S}
25 F u0 p3 c0 {24,S}
26 F u0 p3 c0 {24,S}
27 C u0 p0 c0 {24,S} {28,S} {29,S} {30,S}
28 F u0 p3 c0 {27,S}
29 F u0 p3 c0 {27,S}
30 C u0 p0 c0 {27,S} {31,S} {32,S} {33,S}
31 F u0 p3 c0 {30,S}
32 F u0 p3 c0 {30,S}
33 C u0 p0 c0 {30,S} {34,S} {35,S} {36,S}
34 F u0 p3 c0 {33,S}
35 F u0 p3 c0 {33,S}
36 C u0 p0 c0 {33,S} {37,S} {38,S} {39,S}
37 F u0 p3 c0 {36,S}
38 F u0 p3 c0 {36,S}
39 C u0 p0 c0 {36,S} {40,S} {41,S} {42,S}
40 F u0 p3 c0 {39,S}
41 F u0 p3 c0 {39,S}
42 F u0 p3 c0 {39,S}""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.73049805, 0.322806935, -0.000391296534, 2.26764189e-07, -5.13249102e-11, -654144.194, 1.89792013], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[63.9436338, 0.0954438421, -6.54150622e-05, 1.99609454e-08, -2.27078067e-12, -666412.956, -286.038692], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (39.3315492019718,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 292,
    label = "PF15alkyl(s)",
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
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 C u0 p0 c0 {21,S} {25,S} {26,S} {27,S}
25 F u0 p3 c0 {24,S}
26 F u0 p3 c0 {24,S}
27 C u0 p0 c0 {24,S} {28,S} {29,S} {30,S}
28 F u0 p3 c0 {27,S}
29 F u0 p3 c0 {27,S}
30 C u0 p0 c0 {27,S} {31,S} {32,S} {33,S}
31 F u0 p3 c0 {30,S}
32 F u0 p3 c0 {30,S}
33 C u0 p0 c0 {30,S} {34,S} {35,S} {36,S}
34 F u0 p3 c0 {33,S}
35 F u0 p3 c0 {33,S}
36 C u0 p0 c0 {33,S} {37,S} {38,S} {39,S}
37 F u0 p3 c0 {36,S}
38 F u0 p3 c0 {36,S}
39 C u0 p0 c0 {36,S} {40,S} {41,S} {42,S}
40 F u0 p3 c0 {39,S}
41 F u0 p3 c0 {39,S}
42 C u0 p0 c0 {39,S} {43,S} {44,S} {45,S}
43 F u0 p3 c0 {42,S}
44 F u0 p3 c0 {42,S}
45 F u0 p3 c0 {42,S}""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.94446841, 0.346870905, -0.000420669125, 2.43870859e-07, -5.52138321e-11, -703564.648, 0.644602975], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[68.5882798, 0.102443846, -7.02497857e-05, 2.14416622e-08, -2.43958967e-12, -716748.926, -308.824377], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (41.11059776158459,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 293,
    label = "PF16alkyl(s)",
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
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 C u0 p0 c0 {21,S} {25,S} {26,S} {27,S}
25 F u0 p3 c0 {24,S}
26 F u0 p3 c0 {24,S}
27 C u0 p0 c0 {24,S} {28,S} {29,S} {30,S}
28 F u0 p3 c0 {27,S}
29 F u0 p3 c0 {27,S}
30 C u0 p0 c0 {27,S} {31,S} {32,S} {33,S}
31 F u0 p3 c0 {30,S}
32 F u0 p3 c0 {30,S}
33 C u0 p0 c0 {30,S} {34,S} {35,S} {36,S}
34 F u0 p3 c0 {33,S}
35 F u0 p3 c0 {33,S}
36 C u0 p0 c0 {33,S} {37,S} {38,S} {39,S}
37 F u0 p3 c0 {36,S}
38 F u0 p3 c0 {36,S}
39 C u0 p0 c0 {36,S} {40,S} {41,S} {42,S}
40 F u0 p3 c0 {39,S}
41 F u0 p3 c0 {39,S}
42 C u0 p0 c0 {39,S} {43,S} {44,S} {45,S}
43 F u0 p3 c0 {42,S}
44 F u0 p3 c0 {42,S}
45 C u0 p0 c0 {42,S} {46,S} {47,S} {48,S}
46 F u0 p3 c0 {45,S}
47 F u0 p3 c0 {45,S}
48 F u0 p3 c0 {45,S}""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.15843875, 0.370934874, -0.000450041717, 2.6097753e-07, -5.91027541e-11, -752985.102, -0.608714094], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[73.2329255, 0.109443851, -7.50845097e-05, 2.29223792e-08, -2.60839868e-12, -767084.896, -331.610062], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (42.88964615490813,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 294,
    label = "PF9Sacid",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {33,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 F u0 p3 c0 {29,S}
33 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08944983, 0.229758937, -0.000240695287, 1.17092385e-07, -2.16573594e-11, -530263.835, 6.45872105], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[42.0016383, 0.0972674416, -7.11707857e-05, 2.33557931e-08, -2.8911821e-12, -538757.53, -181.146168], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (34.001577740348125,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 295,
    label = "PF10Sacid",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {36,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 F u0 p3 c0 {32,S}
36 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.52341146, 0.250056832, -0.000259680149, 1.24677084e-07, -2.26233455e-11, -579543.95, 4.435523], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[45.7788348, 0.106878443, -7.81874413e-05, 2.56209571e-08, -3.16546809e-12, -588835.292, -199.960571], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (37.609735490695975,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 296,
    label = "PF11Sacid",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {39,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 F u0 p3 c0 {35,S}
39 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.95737311, 0.270354726, -0.00027866501, 1.32261783e-07, -2.35893314e-11, -628824.066, 2.41232488], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[49.5560307, 0.116489446, -8.52040982e-05, 2.78861215e-08, -3.43975415e-12, -638913.054, -218.774971], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (41.217893407333065,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 297,
    label = "PF12Sacid",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {42,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 C u0 p0 c0 {35,S} {39,S} {40,S} {41,S}
39 F u0 p3 c0 {38,S}
40 F u0 p3 c0 {38,S}
41 F u0 p3 c0 {38,S}
42 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.39133521, 0.290652618, -0.000297649864, 1.39846474e-07, -2.45553146e-11, -678104.181, 0.389124912], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[53.3332271, 0.126100448, -9.2220754e-05, 3.01512855e-08, -3.71404016e-12, -688990.816, -237.589373], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (44.82605506547835,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 298,
    label = "PF13Sacid",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {45,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 C u0 p0 c0 {35,S} {39,S} {40,S} {41,S}
39 F u0 p3 c0 {38,S}
40 F u0 p3 c0 {38,S}
41 C u0 p0 c0 {38,S} {42,S} {43,S} {44,S}
42 F u0 p3 c0 {41,S}
43 F u0 p3 c0 {41,S}
44 F u0 p3 c0 {41,S}
45 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.82529737, 0.310950509, -0.000316634717, 1.47431163e-07, -2.55212975e-11, -727384.296, -1.63407536], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[57.1104235, 0.135711451, -9.92374099e-05, 3.24164496e-08, -3.98832617e-12, -739068.578, -256.403776], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (48.43421722249139,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 299,
    label = "PF14Sacid",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {48,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 C u0 p0 c0 {35,S} {39,S} {40,S} {41,S}
39 F u0 p3 c0 {38,S}
40 F u0 p3 c0 {38,S}
41 C u0 p0 c0 {38,S} {42,S} {43,S} {44,S}
42 F u0 p3 c0 {41,S}
43 F u0 p3 c0 {41,S}
44 C u0 p0 c0 {41,S} {45,S} {46,S} {47,S}
45 F u0 p3 c0 {44,S}
46 F u0 p3 c0 {44,S}
47 F u0 p3 c0 {44,S}
48 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.25925909, 0.331248403, -0.000335619577, 1.5501586e-07, -2.64872828e-11, -776664.412, -3.65727374], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[60.8876204, 0.145322451, -0.000106254065, 3.46816132e-08, -4.26261212e-12, -789146.34, -275.218181], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (52.042375721140864,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 300,
    label = "PF15Sacid",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {51,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 C u0 p0 c0 {35,S} {39,S} {40,S} {41,S}
39 F u0 p3 c0 {38,S}
40 F u0 p3 c0 {38,S}
41 C u0 p0 c0 {38,S} {42,S} {43,S} {44,S}
42 F u0 p3 c0 {41,S}
43 F u0 p3 c0 {41,S}
44 C u0 p0 c0 {41,S} {45,S} {46,S} {47,S}
45 F u0 p3 c0 {44,S}
46 F u0 p3 c0 {44,S}
47 C u0 p0 c0 {44,S} {48,S} {49,S} {50,S}
48 F u0 p3 c0 {47,S}
49 F u0 p3 c0 {47,S}
50 F u0 p3 c0 {47,S}
51 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.69322141, 0.351546293, -0.000354604427, 1.62600548e-07, -2.74532647e-11, -825944.527, -5.68047468], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[64.6648164, 0.154933454, -0.000113270721, 3.69467775e-08, -4.53689816e-12, -839224.102, -294.032581], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (55.65053920846792,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 301,
    label = "PF16Sacid",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {54,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 C u0 p0 c0 {35,S} {39,S} {40,S} {41,S}
39 F u0 p3 c0 {38,S}
40 F u0 p3 c0 {38,S}
41 C u0 p0 c0 {38,S} {42,S} {43,S} {44,S}
42 F u0 p3 c0 {41,S}
43 F u0 p3 c0 {41,S}
44 C u0 p0 c0 {41,S} {45,S} {46,S} {47,S}
45 F u0 p3 c0 {44,S}
46 F u0 p3 c0 {44,S}
47 C u0 p0 c0 {44,S} {48,S} {49,S} {50,S}
48 F u0 p3 c0 {47,S}
49 F u0 p3 c0 {47,S}
50 C u0 p0 c0 {47,S} {51,S} {52,S} {53,S}
51 F u0 p3 c0 {50,S}
52 F u0 p3 c0 {50,S}
53 F u0 p3 c0 {50,S}
54 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.12718288, 0.371844189, -0.000373589292, 1.7018525e-07, -2.84192518e-11, -875224.642, -7.70367202], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[68.4420127, 0.164544456, -0.000120287377, 3.92119417e-08, -4.81118418e-12, -889301.864, -312.846983], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (59.25869562850175,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 302,
    label = "PF9Sulfonater",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 F u0 p3 c0 {29,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.54753028, 0.225481515, -0.000242885713, 1.23063118e-07, -2.41646457e-11, -498618.356, -0.211853132], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[41.3990695, 0.0966736263, -7.20539361e-05, 2.40219892e-08, -3.01904303e-12, -506478.715, -176.746204], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (46.12473313613318,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 303,
    label = "PF10Sulfonater",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 F u0 p3 c0 {32,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.86165952, 0.246791244, -0.000264155747, 1.32654943e-07, -2.57463446e-11, -547481.35, -2.01394132], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[45.1111167, 0.106523288, -7.93702745e-05, 2.6438301e-08, -3.31947625e-12, -556123.2, -195.465536], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (48.73654895938207,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 304,
    label = "PF11Sulfonater",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 F u0 p3 c0 {35,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.17578856, 0.268100976, -0.000285425785, 1.42246772e-07, -2.73280447e-11, -596344.344, -3.81602866], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[48.8231632, 0.116372952, -8.66866142e-05, 2.88546132e-08, -3.61990954e-12, -605767.684, -214.184865], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (51.34836311973843,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 305,
    label = "PF12Sulfonater",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 C u0 p0 c0 {35,S} {39,S} {40,S} {41,S}
39 F u0 p3 c0 {38,S}
40 F u0 p3 c0 {38,S}
41 F u0 p3 c0 {38,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.48991773, 0.289410706, -0.00030669582, 1.51838599e-07, -2.8909744e-11, -645207.339, -5.61811652], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[52.5352105, 0.126222614, -9.40029522e-05, 3.12709249e-08, -3.92034274e-12, -655412.169, -232.904198], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (53.960178360974936,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 306,
    label = "PF13Sulfonater",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 C u0 p0 c0 {35,S} {39,S} {40,S} {41,S}
39 F u0 p3 c0 {38,S}
40 F u0 p3 c0 {38,S}
41 C u0 p0 c0 {38,S} {42,S} {43,S} {44,S}
42 F u0 p3 c0 {41,S}
43 F u0 p3 c0 {41,S}
44 F u0 p3 c0 {41,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.80404709, 0.310720435, -0.000327965852, 1.61430423e-07, -3.04914423e-11, -694070.333, -7.42020521], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[56.2472574, 0.136072276, -0.000101319291, 3.36872369e-08, -4.220776e-12, -705056.654, -251.623528], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (56.57199518195933,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 307,
    label = "PF14Sulfonater",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 C u0 p0 c0 {35,S} {39,S} {40,S} {41,S}
39 F u0 p3 c0 {38,S}
40 F u0 p3 c0 {38,S}
41 C u0 p0 c0 {38,S} {42,S} {43,S} {44,S}
42 F u0 p3 c0 {41,S}
43 F u0 p3 c0 {41,S}
44 C u0 p0 c0 {41,S} {45,S} {46,S} {47,S}
45 F u0 p3 c0 {44,S}
46 F u0 p3 c0 {44,S}
47 F u0 p3 c0 {44,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.11817576, 0.332030169, -0.000349235896, 1.71022259e-07, -3.20731447e-11, -742933.327, -9.22229101], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[59.9593047, 0.145921938, -0.000108635629, 3.61035485e-08, -4.52120921e-12, -754701.139, -270.342861], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (59.18380626596453,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 308,
    label = "PF15Sulfonater",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 C u0 p0 c0 {35,S} {39,S} {40,S} {41,S}
39 F u0 p3 c0 {38,S}
40 F u0 p3 c0 {38,S}
41 C u0 p0 c0 {38,S} {42,S} {43,S} {44,S}
42 F u0 p3 c0 {41,S}
43 F u0 p3 c0 {41,S}
44 C u0 p0 c0 {41,S} {45,S} {46,S} {47,S}
45 F u0 p3 c0 {44,S}
46 F u0 p3 c0 {44,S}
47 C u0 p0 c0 {44,S} {48,S} {49,S} {50,S}
48 F u0 p3 c0 {47,S}
49 F u0 p3 c0 {47,S}
50 F u0 p3 c0 {47,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.4323053, 0.353339897, -0.000370505925, 1.80614079e-07, -3.36548417e-11, -791796.322, -11.0243804], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[63.6713515, 0.155771601, -0.000115951968, 3.85198605e-08, -4.82164246e-12, -804345.624, -289.062191], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (61.795624583552204,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 309,
    label = "PF16Sulfonater",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,D}
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
26 C u0 p0 c0 {23,S} {27,S} {28,S} {29,S}
27 F u0 p3 c0 {26,S}
28 F u0 p3 c0 {26,S}
29 C u0 p0 c0 {26,S} {30,S} {31,S} {32,S}
30 F u0 p3 c0 {29,S}
31 F u0 p3 c0 {29,S}
32 C u0 p0 c0 {29,S} {33,S} {34,S} {35,S}
33 F u0 p3 c0 {32,S}
34 F u0 p3 c0 {32,S}
35 C u0 p0 c0 {32,S} {36,S} {37,S} {38,S}
36 F u0 p3 c0 {35,S}
37 F u0 p3 c0 {35,S}
38 C u0 p0 c0 {35,S} {39,S} {40,S} {41,S}
39 F u0 p3 c0 {38,S}
40 F u0 p3 c0 {38,S}
41 C u0 p0 c0 {38,S} {42,S} {43,S} {44,S}
42 F u0 p3 c0 {41,S}
43 F u0 p3 c0 {41,S}
44 C u0 p0 c0 {41,S} {45,S} {46,S} {47,S}
45 F u0 p3 c0 {44,S}
46 F u0 p3 c0 {44,S}
47 C u0 p0 c0 {44,S} {48,S} {49,S} {50,S}
48 F u0 p3 c0 {47,S}
49 F u0 p3 c0 {47,S}
50 C u0 p0 c0 {47,S} {51,S} {52,S} {53,S}
51 F u0 p3 c0 {50,S}
52 F u0 p3 c0 {50,S}
53 F u0 p3 c0 {50,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.74643412, 0.37464963, -0.000391775966, 1.90205912e-07, -3.52365431e-11, -840659.316, -12.8264668], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[67.3833988, 0.165621263, -0.000123268307, 4.09361722e-08, -5.12207568e-12, -853990.108, -307.781523], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (64.40743691472679,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 310,
    label = "PF9Sulfite",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {28,S} {32,S}
3  C u0 p0 c0 {2,S} {4,S} {26,S} {27,S}
4  C u0 p0 c0 {3,S} {5,S} {24,S} {25,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {20,S} {21,S}
7  C u0 p0 c0 {6,S} {8,S} {18,S} {19,S}
8  C u0 p0 c0 {7,S} {9,S} {16,S} {17,S}
9  C u0 p0 c0 {8,S} {10,S} {14,S} {15,S}
10 C u0 p0 c0 {9,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 F u0 p3 c0 {10,S}
14 F u0 p3 c0 {9,S}
15 F u0 p3 c0 {9,S}
16 F u0 p3 c0 {8,S}
17 F u0 p3 c0 {8,S}
18 F u0 p3 c0 {7,S}
19 F u0 p3 c0 {7,S}
20 F u0 p3 c0 {6,S}
21 F u0 p3 c0 {6,S}
22 F u0 p3 c0 {5,S}
23 F u0 p3 c0 {5,S}
24 F u0 p3 c0 {4,S}
25 F u0 p3 c0 {4,S}
26 F u0 p3 c0 {3,S}
27 F u0 p3 c0 {3,S}
28 O u0 p2 c0 {2,S} {29,S}
29 S u0 p1 c0 {28,S} {30,D} {31,S}
30 O u0 p2 c0 {29,D}
31 O u0 p2 c0 {29,S} {33,S}
32 F u0 p3 c0 {2,S}
33 H u0 p0 c0 {31,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.66416153, 0.249891716, -0.000284856215, 1.53450019e-07, -3.21780347e-11, -538117.521, 17.5680882], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[44.2209903, 0.0926960758, -6.92219375e-05, 2.31824419e-08, -2.92519835e-12, -547238.295, -190.916253], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (13.836608831753704,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 311,
    label = "PF10Sulfite",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {31,S} {35,S}
3  C u0 p0 c0 {2,S} {4,S} {29,S} {30,S}
4  C u0 p0 c0 {3,S} {5,S} {27,S} {28,S}
5  C u0 p0 c0 {4,S} {6,S} {25,S} {26,S}
6  C u0 p0 c0 {5,S} {7,S} {23,S} {24,S}
7  C u0 p0 c0 {6,S} {8,S} {21,S} {22,S}
8  C u0 p0 c0 {7,S} {9,S} {19,S} {20,S}
9  C u0 p0 c0 {8,S} {10,S} {17,S} {18,S}
10 C u0 p0 c0 {9,S} {11,S} {15,S} {16,S}
11 C u0 p0 c0 {10,S} {12,S} {13,S} {14,S}
12 F u0 p3 c0 {11,S}
13 F u0 p3 c0 {11,S}
14 F u0 p3 c0 {11,S}
15 F u0 p3 c0 {10,S}
16 F u0 p3 c0 {10,S}
17 F u0 p3 c0 {9,S}
18 F u0 p3 c0 {9,S}
19 F u0 p3 c0 {8,S}
20 F u0 p3 c0 {8,S}
21 F u0 p3 c0 {7,S}
22 F u0 p3 c0 {7,S}
23 F u0 p3 c0 {6,S}
24 F u0 p3 c0 {6,S}
25 F u0 p3 c0 {5,S}
26 F u0 p3 c0 {5,S}
27 F u0 p3 c0 {4,S}
28 F u0 p3 c0 {4,S}
29 F u0 p3 c0 {3,S}
30 F u0 p3 c0 {3,S}
31 O u0 p2 c0 {2,S} {32,S}
32 S u0 p1 c0 {31,S} {33,D} {34,S}
33 O u0 p2 c0 {32,D}
34 O u0 p2 c0 {32,S} {36,S}
35 F u0 p3 c0 {2,S}
36 H u0 p0 c0 {34,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.83032493, 0.271982057, -0.000307022796, 1.63222544e-07, -3.36812157e-11, -588023.317, 16.6038084], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[48.3729263, 0.101619757, -7.58464318e-05, 2.535414e-08, -3.19221521e-12, -598074.255, -211.793089], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (15.218168209558947,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 312,
    label = "PF11Sulfite",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {34,S} {38,S}
3  C u0 p0 c0 {2,S} {4,S} {32,S} {33,S}
4  C u0 p0 c0 {3,S} {5,S} {30,S} {31,S}
5  C u0 p0 c0 {4,S} {6,S} {28,S} {29,S}
6  C u0 p0 c0 {5,S} {7,S} {26,S} {27,S}
7  C u0 p0 c0 {6,S} {8,S} {24,S} {25,S}
8  C u0 p0 c0 {7,S} {9,S} {22,S} {23,S}
9  C u0 p0 c0 {8,S} {10,S} {20,S} {21,S}
10 C u0 p0 c0 {9,S} {11,S} {18,S} {19,S}
11 C u0 p0 c0 {10,S} {12,S} {16,S} {17,S}
12 C u0 p0 c0 {11,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 F u0 p3 c0 {12,S}
16 F u0 p3 c0 {11,S}
17 F u0 p3 c0 {11,S}
18 F u0 p3 c0 {10,S}
19 F u0 p3 c0 {10,S}
20 F u0 p3 c0 {9,S}
21 F u0 p3 c0 {9,S}
22 F u0 p3 c0 {8,S}
23 F u0 p3 c0 {8,S}
24 F u0 p3 c0 {7,S}
25 F u0 p3 c0 {7,S}
26 F u0 p3 c0 {6,S}
27 F u0 p3 c0 {6,S}
28 F u0 p3 c0 {5,S}
29 F u0 p3 c0 {5,S}
30 F u0 p3 c0 {4,S}
31 F u0 p3 c0 {4,S}
32 F u0 p3 c0 {3,S}
33 F u0 p3 c0 {3,S}
34 O u0 p2 c0 {2,S} {35,S}
35 S u0 p1 c0 {34,S} {36,D} {37,S}
36 O u0 p2 c0 {35,D}
37 O u0 p2 c0 {35,S} {39,S}
38 F u0 p3 c0 {2,S}
39 H u0 p0 c0 {37,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.99648777, 0.294072403, -0.000329189387, 1.72995079e-07, -3.51844e-11, -637929.113, 15.639531], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[52.5248625, 0.110543438, -8.24709256e-05, 2.7525838e-08, -3.45923205e-12, -648910.215, -232.669926], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (16.599722931265124,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 313,
    label = "PF12Sulfite",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {37,S} {41,S}
3  C u0 p0 c0 {2,S} {4,S} {35,S} {36,S}
4  C u0 p0 c0 {3,S} {5,S} {33,S} {34,S}
5  C u0 p0 c0 {4,S} {6,S} {31,S} {32,S}
6  C u0 p0 c0 {5,S} {7,S} {29,S} {30,S}
7  C u0 p0 c0 {6,S} {8,S} {27,S} {28,S}
8  C u0 p0 c0 {7,S} {9,S} {25,S} {26,S}
9  C u0 p0 c0 {8,S} {10,S} {23,S} {24,S}
10 C u0 p0 c0 {9,S} {11,S} {21,S} {22,S}
11 C u0 p0 c0 {10,S} {12,S} {19,S} {20,S}
12 C u0 p0 c0 {11,S} {13,S} {17,S} {18,S}
13 C u0 p0 c0 {12,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 F u0 p3 c0 {13,S}
17 F u0 p3 c0 {12,S}
18 F u0 p3 c0 {12,S}
19 F u0 p3 c0 {11,S}
20 F u0 p3 c0 {11,S}
21 F u0 p3 c0 {10,S}
22 F u0 p3 c0 {10,S}
23 F u0 p3 c0 {9,S}
24 F u0 p3 c0 {9,S}
25 F u0 p3 c0 {8,S}
26 F u0 p3 c0 {8,S}
27 F u0 p3 c0 {7,S}
28 F u0 p3 c0 {7,S}
29 F u0 p3 c0 {6,S}
30 F u0 p3 c0 {6,S}
31 F u0 p3 c0 {5,S}
32 F u0 p3 c0 {5,S}
33 F u0 p3 c0 {4,S}
34 F u0 p3 c0 {4,S}
35 F u0 p3 c0 {3,S}
36 F u0 p3 c0 {3,S}
37 O u0 p2 c0 {2,S} {38,S}
38 S u0 p1 c0 {37,S} {39,D} {40,S}
39 O u0 p2 c0 {38,D}
40 O u0 p2 c0 {38,S} {42,S}
41 F u0 p3 c0 {2,S}
42 H u0 p0 c0 {40,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.16265145, 0.316162743, -0.000351355963, 1.827676e-07, -3.66875794e-11, -687834.909, 14.6752501], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[56.6767983, 0.119467119, -8.90954205e-05, 2.96975364e-08, -3.72624894e-12, -699746.175, -253.546761], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (17.981284637119902,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 314,
    label = "PF13Sulfite",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {40,S} {44,S}
3  C u0 p0 c0 {2,S} {4,S} {38,S} {39,S}
4  C u0 p0 c0 {3,S} {5,S} {36,S} {37,S}
5  C u0 p0 c0 {4,S} {6,S} {34,S} {35,S}
6  C u0 p0 c0 {5,S} {7,S} {32,S} {33,S}
7  C u0 p0 c0 {6,S} {8,S} {30,S} {31,S}
8  C u0 p0 c0 {7,S} {9,S} {28,S} {29,S}
9  C u0 p0 c0 {8,S} {10,S} {26,S} {27,S}
10 C u0 p0 c0 {9,S} {11,S} {24,S} {25,S}
11 C u0 p0 c0 {10,S} {12,S} {22,S} {23,S}
12 C u0 p0 c0 {11,S} {13,S} {20,S} {21,S}
13 C u0 p0 c0 {12,S} {14,S} {18,S} {19,S}
14 C u0 p0 c0 {13,S} {15,S} {16,S} {17,S}
15 F u0 p3 c0 {14,S}
16 F u0 p3 c0 {14,S}
17 F u0 p3 c0 {14,S}
18 F u0 p3 c0 {13,S}
19 F u0 p3 c0 {13,S}
20 F u0 p3 c0 {12,S}
21 F u0 p3 c0 {12,S}
22 F u0 p3 c0 {11,S}
23 F u0 p3 c0 {11,S}
24 F u0 p3 c0 {10,S}
25 F u0 p3 c0 {10,S}
26 F u0 p3 c0 {9,S}
27 F u0 p3 c0 {9,S}
28 F u0 p3 c0 {8,S}
29 F u0 p3 c0 {8,S}
30 F u0 p3 c0 {7,S}
31 F u0 p3 c0 {7,S}
32 F u0 p3 c0 {6,S}
33 F u0 p3 c0 {6,S}
34 F u0 p3 c0 {5,S}
35 F u0 p3 c0 {5,S}
36 F u0 p3 c0 {4,S}
37 F u0 p3 c0 {4,S}
38 F u0 p3 c0 {3,S}
39 F u0 p3 c0 {3,S}
40 O u0 p2 c0 {2,S} {41,S}
41 S u0 p1 c0 {40,S} {42,D} {43,S}
42 O u0 p2 c0 {41,D}
43 O u0 p2 c0 {41,S} {45,S}
44 F u0 p3 c0 {2,S}
45 H u0 p0 c0 {43,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.32881571, 0.338253079, -0.00037352253, 1.92540111e-07, -3.81907554e-11, -737740.705, 13.7109668], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[60.8287346, 0.1283908, -9.57199142e-05, 3.18692344e-08, -3.99326577e-12, -750582.135, -274.423599], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (19.362851165362997,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 315,
    label = "PF14Sulfite",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {43,S} {47,S}
3  C u0 p0 c0 {2,S} {4,S} {41,S} {42,S}
4  C u0 p0 c0 {3,S} {5,S} {39,S} {40,S}
5  C u0 p0 c0 {4,S} {6,S} {37,S} {38,S}
6  C u0 p0 c0 {5,S} {7,S} {35,S} {36,S}
7  C u0 p0 c0 {6,S} {8,S} {33,S} {34,S}
8  C u0 p0 c0 {7,S} {9,S} {31,S} {32,S}
9  C u0 p0 c0 {8,S} {10,S} {29,S} {30,S}
10 C u0 p0 c0 {9,S} {11,S} {27,S} {28,S}
11 C u0 p0 c0 {10,S} {12,S} {25,S} {26,S}
12 C u0 p0 c0 {11,S} {13,S} {23,S} {24,S}
13 C u0 p0 c0 {12,S} {14,S} {21,S} {22,S}
14 C u0 p0 c0 {13,S} {15,S} {19,S} {20,S}
15 C u0 p0 c0 {14,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}
18 F u0 p3 c0 {15,S}
19 F u0 p3 c0 {14,S}
20 F u0 p3 c0 {14,S}
21 F u0 p3 c0 {13,S}
22 F u0 p3 c0 {13,S}
23 F u0 p3 c0 {12,S}
24 F u0 p3 c0 {12,S}
25 F u0 p3 c0 {11,S}
26 F u0 p3 c0 {11,S}
27 F u0 p3 c0 {10,S}
28 F u0 p3 c0 {10,S}
29 F u0 p3 c0 {9,S}
30 F u0 p3 c0 {9,S}
31 F u0 p3 c0 {8,S}
32 F u0 p3 c0 {8,S}
33 F u0 p3 c0 {7,S}
34 F u0 p3 c0 {7,S}
35 F u0 p3 c0 {6,S}
36 F u0 p3 c0 {6,S}
37 F u0 p3 c0 {5,S}
38 F u0 p3 c0 {5,S}
39 F u0 p3 c0 {4,S}
40 F u0 p3 c0 {4,S}
41 F u0 p3 c0 {3,S}
42 F u0 p3 c0 {3,S}
43 O u0 p2 c0 {2,S} {44,S}
44 S u0 p1 c0 {43,S} {45,D} {46,S}
45 O u0 p2 c0 {44,D}
46 O u0 p2 c0 {44,S} {48,S}
47 F u0 p3 c0 {2,S}
48 H u0 p0 c0 {46,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.49497929, 0.360343419, -0.000395689107, 2.02312634e-07, -3.96939354e-11, -787646.501, 12.7466863], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[64.980671, 0.13731448, -0.000102344408, 3.40409322e-08, -4.26028259e-12, -801418.094, -295.300437], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (20.74441203977151,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 316,
    label = "PF15Sulfite",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {46,S} {50,S}
3  C u0 p0 c0 {2,S} {4,S} {44,S} {45,S}
4  C u0 p0 c0 {3,S} {5,S} {42,S} {43,S}
5  C u0 p0 c0 {4,S} {6,S} {40,S} {41,S}
6  C u0 p0 c0 {5,S} {7,S} {38,S} {39,S}
7  C u0 p0 c0 {6,S} {8,S} {36,S} {37,S}
8  C u0 p0 c0 {7,S} {9,S} {34,S} {35,S}
9  C u0 p0 c0 {8,S} {10,S} {32,S} {33,S}
10 C u0 p0 c0 {9,S} {11,S} {30,S} {31,S}
11 C u0 p0 c0 {10,S} {12,S} {28,S} {29,S}
12 C u0 p0 c0 {11,S} {13,S} {26,S} {27,S}
13 C u0 p0 c0 {12,S} {14,S} {24,S} {25,S}
14 C u0 p0 c0 {13,S} {15,S} {22,S} {23,S}
15 C u0 p0 c0 {14,S} {16,S} {20,S} {21,S}
16 C u0 p0 c0 {15,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 F u0 p3 c0 {16,S}
20 F u0 p3 c0 {15,S}
21 F u0 p3 c0 {15,S}
22 F u0 p3 c0 {14,S}
23 F u0 p3 c0 {14,S}
24 F u0 p3 c0 {13,S}
25 F u0 p3 c0 {13,S}
26 F u0 p3 c0 {12,S}
27 F u0 p3 c0 {12,S}
28 F u0 p3 c0 {11,S}
29 F u0 p3 c0 {11,S}
30 F u0 p3 c0 {10,S}
31 F u0 p3 c0 {10,S}
32 F u0 p3 c0 {9,S}
33 F u0 p3 c0 {9,S}
34 F u0 p3 c0 {8,S}
35 F u0 p3 c0 {8,S}
36 F u0 p3 c0 {7,S}
37 F u0 p3 c0 {7,S}
38 F u0 p3 c0 {6,S}
39 F u0 p3 c0 {6,S}
40 F u0 p3 c0 {5,S}
41 F u0 p3 c0 {5,S}
42 F u0 p3 c0 {4,S}
43 F u0 p3 c0 {4,S}
44 F u0 p3 c0 {3,S}
45 F u0 p3 c0 {3,S}
46 O u0 p2 c0 {2,S} {47,S}
47 S u0 p1 c0 {46,S} {48,D} {49,S}
48 O u0 p2 c0 {47,D}
49 O u0 p2 c0 {47,S} {51,S}
50 F u0 p3 c0 {2,S}
51 H u0 p0 c0 {49,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.66114184, 0.382433767, -0.000417855703, 2.12085174e-07, -4.11971214e-11, -837552.296, 11.7824101], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[69.132607, 0.146238161, -0.000108968902, 3.62126304e-08, -4.52729946e-12, -852254.054, -316.177273], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (22.12596435028353,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 317,
    label = "PF16Sulfite",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {49,S} {53,S}
3  C u0 p0 c0 {2,S} {4,S} {47,S} {48,S}
4  C u0 p0 c0 {3,S} {5,S} {45,S} {46,S}
5  C u0 p0 c0 {4,S} {6,S} {43,S} {44,S}
6  C u0 p0 c0 {5,S} {7,S} {41,S} {42,S}
7  C u0 p0 c0 {6,S} {8,S} {39,S} {40,S}
8  C u0 p0 c0 {7,S} {9,S} {37,S} {38,S}
9  C u0 p0 c0 {8,S} {10,S} {35,S} {36,S}
10 C u0 p0 c0 {9,S} {11,S} {33,S} {34,S}
11 C u0 p0 c0 {10,S} {12,S} {31,S} {32,S}
12 C u0 p0 c0 {11,S} {13,S} {29,S} {30,S}
13 C u0 p0 c0 {12,S} {14,S} {27,S} {28,S}
14 C u0 p0 c0 {13,S} {15,S} {25,S} {26,S}
15 C u0 p0 c0 {14,S} {16,S} {23,S} {24,S}
16 C u0 p0 c0 {15,S} {17,S} {21,S} {22,S}
17 C u0 p0 c0 {16,S} {18,S} {19,S} {20,S}
18 F u0 p3 c0 {17,S}
19 F u0 p3 c0 {17,S}
20 F u0 p3 c0 {17,S}
21 F u0 p3 c0 {16,S}
22 F u0 p3 c0 {16,S}
23 F u0 p3 c0 {15,S}
24 F u0 p3 c0 {15,S}
25 F u0 p3 c0 {14,S}
26 F u0 p3 c0 {14,S}
27 F u0 p3 c0 {13,S}
28 F u0 p3 c0 {13,S}
29 F u0 p3 c0 {12,S}
30 F u0 p3 c0 {12,S}
31 F u0 p3 c0 {11,S}
32 F u0 p3 c0 {11,S}
33 F u0 p3 c0 {10,S}
34 F u0 p3 c0 {10,S}
35 F u0 p3 c0 {9,S}
36 F u0 p3 c0 {9,S}
37 F u0 p3 c0 {8,S}
38 F u0 p3 c0 {8,S}
39 F u0 p3 c0 {7,S}
40 F u0 p3 c0 {7,S}
41 F u0 p3 c0 {6,S}
42 F u0 p3 c0 {6,S}
43 F u0 p3 c0 {5,S}
44 F u0 p3 c0 {5,S}
45 F u0 p3 c0 {4,S}
46 F u0 p3 c0 {4,S}
47 F u0 p3 c0 {3,S}
48 F u0 p3 c0 {3,S}
49 O u0 p2 c0 {2,S} {50,S}
50 S u0 p1 c0 {49,S} {51,D} {52,S}
51 O u0 p2 c0 {50,D}
52 O u0 p2 c0 {50,S} {54,S}
53 F u0 p3 c0 {2,S}
54 H u0 p0 c0 {52,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.82730616, 0.404524103, -0.000440022268, 2.21857684e-07, -4.27002971e-11, -887458.093, 10.8181265], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[73.2845432, 0.155161842, -0.000115593396, 3.83843284e-08, -4.7943163e-12, -903090.014, -337.054111], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (23.507531377394386,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 318,
    label = "PF9Sultone",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {30,S} {31,S}
3  C u0 p0 c0 {2,S} {4,S} {28,S} {29,S}
4  C u0 p0 c0 {3,S} {5,S} {26,S} {27,S}
5  C u0 p0 c0 {4,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {6,S} {8,S} {20,S} {21,S}
8  C u0 p0 c0 {7,S} {9,S} {18,S} {19,S}
9  C u0 p0 c0 {8,S} {10,S} {16,S} {17,S}
10 C u0 p0 c0 {9,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 O u0 p2 c0 {10,S} {13,S}
13 S u0 p0 c0 {10,S} {12,S} {14,D} {15,D}
14 O u0 p2 c0 {13,D}
15 O u0 p2 c0 {13,D}
16 F u0 p3 c0 {9,S}
17 F u0 p3 c0 {9,S}
18 F u0 p3 c0 {8,S}
19 F u0 p3 c0 {8,S}
20 F u0 p3 c0 {7,S}
21 F u0 p3 c0 {7,S}
22 F u0 p3 c0 {6,S}
23 F u0 p3 c0 {6,S}
24 F u0 p3 c0 {5,S}
25 F u0 p3 c0 {5,S}
26 F u0 p3 c0 {4,S}
27 F u0 p3 c0 {4,S}
28 F u0 p3 c0 {3,S}
29 F u0 p3 c0 {3,S}
30 F u0 p3 c0 {2,S}
31 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.48071526, 0.216938789, -0.000229510148, 1.12696061e-07, -2.10331322e-11, -482252.617, 6.04919476], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[41.0868986, 0.088752833, -6.50521416e-05, 2.14241844e-08, -2.66356474e-12, -490441.102, -175.028842], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (37.25473953185878,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 319,
    label = "PF10Sultone",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {33,S} {34,S}
3  C u0 p0 c0 {2,S} {4,S} {31,S} {32,S}
4  C u0 p0 c0 {3,S} {5,S} {29,S} {30,S}
5  C u0 p0 c0 {4,S} {6,S} {27,S} {28,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {8,S} {23,S} {24,S}
8  C u0 p0 c0 {7,S} {9,S} {21,S} {22,S}
9  C u0 p0 c0 {8,S} {10,S} {19,S} {20,S}
10 C u0 p0 c0 {9,S} {11,S} {17,S} {18,S}
11 C u0 p0 c0 {10,S} {12,S} {13,S} {14,S}
12 F u0 p3 c0 {11,S}
13 O u0 p2 c0 {11,S} {14,S}
14 S u0 p0 c0 {11,S} {13,S} {15,D} {16,D}
15 O u0 p2 c0 {14,D}
16 O u0 p2 c0 {14,D}
17 F u0 p3 c0 {10,S}
18 F u0 p3 c0 {10,S}
19 F u0 p3 c0 {9,S}
20 F u0 p3 c0 {9,S}
21 F u0 p3 c0 {8,S}
22 F u0 p3 c0 {8,S}
23 F u0 p3 c0 {7,S}
24 F u0 p3 c0 {7,S}
25 F u0 p3 c0 {6,S}
26 F u0 p3 c0 {6,S}
27 F u0 p3 c0 {5,S}
28 F u0 p3 c0 {5,S}
29 F u0 p3 c0 {4,S}
30 F u0 p3 c0 {4,S}
31 F u0 p3 c0 {3,S}
32 F u0 p3 c0 {3,S}
33 F u0 p3 c0 {2,S}
34 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.86816761, 0.237655849, -0.000249295145, 1.20748772e-07, -2.20781526e-11, -531997.063, 4.20836078], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[45.1500167, 0.0976953692, -7.16041381e-05, 2.35545372e-08, -2.92395625e-12, -541061.288, -195.324289], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (40.47619761224941,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 320,
    label = "PF11Sultone",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {36,S} {37,S}
3  C u0 p0 c0 {2,S} {4,S} {34,S} {35,S}
4  C u0 p0 c0 {3,S} {5,S} {32,S} {33,S}
5  C u0 p0 c0 {4,S} {6,S} {30,S} {31,S}
6  C u0 p0 c0 {5,S} {7,S} {28,S} {29,S}
7  C u0 p0 c0 {6,S} {8,S} {26,S} {27,S}
8  C u0 p0 c0 {7,S} {9,S} {24,S} {25,S}
9  C u0 p0 c0 {8,S} {10,S} {22,S} {23,S}
10 C u0 p0 c0 {9,S} {11,S} {20,S} {21,S}
11 C u0 p0 c0 {10,S} {12,S} {18,S} {19,S}
12 C u0 p0 c0 {11,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 O u0 p2 c0 {12,S} {15,S}
15 S u0 p0 c0 {12,S} {14,S} {16,D} {17,D}
16 O u0 p2 c0 {15,D}
17 O u0 p2 c0 {15,D}
18 F u0 p3 c0 {11,S}
19 F u0 p3 c0 {11,S}
20 F u0 p3 c0 {10,S}
21 F u0 p3 c0 {10,S}
22 F u0 p3 c0 {9,S}
23 F u0 p3 c0 {9,S}
24 F u0 p3 c0 {8,S}
25 F u0 p3 c0 {8,S}
26 F u0 p3 c0 {7,S}
27 F u0 p3 c0 {7,S}
28 F u0 p3 c0 {6,S}
29 F u0 p3 c0 {6,S}
30 F u0 p3 c0 {5,S}
31 F u0 p3 c0 {5,S}
32 F u0 p3 c0 {4,S}
33 F u0 p3 c0 {4,S}
34 F u0 p3 c0 {3,S}
35 F u0 p3 c0 {3,S}
36 F u0 p3 c0 {2,S}
37 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.25561983, 0.258372911, -0.000269080145, 1.28801486e-07, -2.31231739e-11, -581741.509, 2.36752736], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[49.2131353, 0.106637904, -7.81561335e-05, 2.56848896e-08, -3.18434771e-12, -591681.474, -215.619739], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (43.69765461175989,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 321,
    label = "PF12Sultone",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {39,S} {40,S}
3  C u0 p0 c0 {2,S} {4,S} {37,S} {38,S}
4  C u0 p0 c0 {3,S} {5,S} {35,S} {36,S}
5  C u0 p0 c0 {4,S} {6,S} {33,S} {34,S}
6  C u0 p0 c0 {5,S} {7,S} {31,S} {32,S}
7  C u0 p0 c0 {6,S} {8,S} {29,S} {30,S}
8  C u0 p0 c0 {7,S} {9,S} {27,S} {28,S}
9  C u0 p0 c0 {8,S} {10,S} {25,S} {26,S}
10 C u0 p0 c0 {9,S} {11,S} {23,S} {24,S}
11 C u0 p0 c0 {10,S} {12,S} {21,S} {22,S}
12 C u0 p0 c0 {11,S} {13,S} {19,S} {20,S}
13 C u0 p0 c0 {12,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 O u0 p2 c0 {13,S} {16,S}
16 S u0 p0 c0 {13,S} {15,S} {17,D} {18,D}
17 O u0 p2 c0 {16,D}
18 O u0 p2 c0 {16,D}
19 F u0 p3 c0 {12,S}
20 F u0 p3 c0 {12,S}
21 F u0 p3 c0 {11,S}
22 F u0 p3 c0 {11,S}
23 F u0 p3 c0 {10,S}
24 F u0 p3 c0 {10,S}
25 F u0 p3 c0 {9,S}
26 F u0 p3 c0 {9,S}
27 F u0 p3 c0 {8,S}
28 F u0 p3 c0 {8,S}
29 F u0 p3 c0 {7,S}
30 F u0 p3 c0 {7,S}
31 F u0 p3 c0 {6,S}
32 F u0 p3 c0 {6,S}
33 F u0 p3 c0 {5,S}
34 F u0 p3 c0 {5,S}
35 F u0 p3 c0 {4,S}
36 F u0 p3 c0 {4,S}
37 F u0 p3 c0 {3,S}
38 F u0 p3 c0 {3,S}
39 F u0 p3 c0 {2,S}
40 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.64307226, 0.279089971, -0.000288865141, 1.36854196e-07, -2.4168194e-11, -631485.955, 0.526692996], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[53.2762534, 0.11558044, -8.470813e-05, 2.78152424e-08, -3.44473922e-12, -642301.661, -235.915186], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (46.91911335730753,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 322,
    label = "PF13Sultone",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {42,S} {43,S}
3  C u0 p0 c0 {2,S} {4,S} {40,S} {41,S}
4  C u0 p0 c0 {3,S} {5,S} {38,S} {39,S}
5  C u0 p0 c0 {4,S} {6,S} {36,S} {37,S}
6  C u0 p0 c0 {5,S} {7,S} {34,S} {35,S}
7  C u0 p0 c0 {6,S} {8,S} {32,S} {33,S}
8  C u0 p0 c0 {7,S} {9,S} {30,S} {31,S}
9  C u0 p0 c0 {8,S} {10,S} {28,S} {29,S}
10 C u0 p0 c0 {9,S} {11,S} {26,S} {27,S}
11 C u0 p0 c0 {10,S} {12,S} {24,S} {25,S}
12 C u0 p0 c0 {11,S} {13,S} {22,S} {23,S}
13 C u0 p0 c0 {12,S} {14,S} {20,S} {21,S}
14 C u0 p0 c0 {13,S} {15,S} {16,S} {17,S}
15 F u0 p3 c0 {14,S}
16 O u0 p2 c0 {14,S} {17,S}
17 S u0 p0 c0 {14,S} {16,S} {18,D} {19,D}
18 O u0 p2 c0 {17,D}
19 O u0 p2 c0 {17,D}
20 F u0 p3 c0 {13,S}
21 F u0 p3 c0 {13,S}
22 F u0 p3 c0 {12,S}
23 F u0 p3 c0 {12,S}
24 F u0 p3 c0 {11,S}
25 F u0 p3 c0 {11,S}
26 F u0 p3 c0 {10,S}
27 F u0 p3 c0 {10,S}
28 F u0 p3 c0 {9,S}
29 F u0 p3 c0 {9,S}
30 F u0 p3 c0 {8,S}
31 F u0 p3 c0 {8,S}
32 F u0 p3 c0 {7,S}
33 F u0 p3 c0 {7,S}
34 F u0 p3 c0 {6,S}
35 F u0 p3 c0 {6,S}
36 F u0 p3 c0 {5,S}
37 F u0 p3 c0 {5,S}
38 F u0 p3 c0 {4,S}
39 F u0 p3 c0 {4,S}
40 F u0 p3 c0 {3,S}
41 F u0 p3 c0 {3,S}
42 F u0 p3 c0 {2,S}
43 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.03052479, 0.299807031, -0.000308650136, 1.44906904e-07, -2.52132134e-11, -681230.401, -1.31414171], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[57.3393714, 0.124522977, -9.12601266e-05, 2.99455953e-08, -3.70513074e-12, -692921.847, -256.210633], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (50.140572934301424,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 323,
    label = "PF14Sultone",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {45,S} {46,S}
3  C u0 p0 c0 {2,S} {4,S} {43,S} {44,S}
4  C u0 p0 c0 {3,S} {5,S} {41,S} {42,S}
5  C u0 p0 c0 {4,S} {6,S} {39,S} {40,S}
6  C u0 p0 c0 {5,S} {7,S} {37,S} {38,S}
7  C u0 p0 c0 {6,S} {8,S} {35,S} {36,S}
8  C u0 p0 c0 {7,S} {9,S} {33,S} {34,S}
9  C u0 p0 c0 {8,S} {10,S} {31,S} {32,S}
10 C u0 p0 c0 {9,S} {11,S} {29,S} {30,S}
11 C u0 p0 c0 {10,S} {12,S} {27,S} {28,S}
12 C u0 p0 c0 {11,S} {13,S} {25,S} {26,S}
13 C u0 p0 c0 {12,S} {14,S} {23,S} {24,S}
14 C u0 p0 c0 {13,S} {15,S} {21,S} {22,S}
15 C u0 p0 c0 {14,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 O u0 p2 c0 {15,S} {18,S}
18 S u0 p0 c0 {15,S} {17,S} {19,D} {20,D}
19 O u0 p2 c0 {18,D}
20 O u0 p2 c0 {18,D}
21 F u0 p3 c0 {14,S}
22 F u0 p3 c0 {14,S}
23 F u0 p3 c0 {13,S}
24 F u0 p3 c0 {13,S}
25 F u0 p3 c0 {12,S}
26 F u0 p3 c0 {12,S}
27 F u0 p3 c0 {11,S}
28 F u0 p3 c0 {11,S}
29 F u0 p3 c0 {10,S}
30 F u0 p3 c0 {10,S}
31 F u0 p3 c0 {9,S}
32 F u0 p3 c0 {9,S}
33 F u0 p3 c0 {8,S}
34 F u0 p3 c0 {8,S}
35 F u0 p3 c0 {7,S}
36 F u0 p3 c0 {7,S}
37 F u0 p3 c0 {6,S}
38 F u0 p3 c0 {6,S}
39 F u0 p3 c0 {5,S}
40 F u0 p3 c0 {5,S}
41 F u0 p3 c0 {4,S}
42 F u0 p3 c0 {4,S}
43 F u0 p3 c0 {3,S}
44 F u0 p3 c0 {3,S}
45 F u0 p3 c0 {2,S}
46 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.41797681, 0.320524094, -0.00032843514, 1.52959622e-07, -2.62582361e-11, -730974.848, -3.15497433], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[61.4024899, 0.133465512, -9.78121221e-05, 3.20759478e-08, -3.96552221e-12, -743542.033, -276.506082], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (53.362028270919375,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 324,
    label = "PF15Sultone",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {48,S} {49,S}
3  C u0 p0 c0 {2,S} {4,S} {46,S} {47,S}
4  C u0 p0 c0 {3,S} {5,S} {44,S} {45,S}
5  C u0 p0 c0 {4,S} {6,S} {42,S} {43,S}
6  C u0 p0 c0 {5,S} {7,S} {40,S} {41,S}
7  C u0 p0 c0 {6,S} {8,S} {38,S} {39,S}
8  C u0 p0 c0 {7,S} {9,S} {36,S} {37,S}
9  C u0 p0 c0 {8,S} {10,S} {34,S} {35,S}
10 C u0 p0 c0 {9,S} {11,S} {32,S} {33,S}
11 C u0 p0 c0 {10,S} {12,S} {30,S} {31,S}
12 C u0 p0 c0 {11,S} {13,S} {28,S} {29,S}
13 C u0 p0 c0 {12,S} {14,S} {26,S} {27,S}
14 C u0 p0 c0 {13,S} {15,S} {24,S} {25,S}
15 C u0 p0 c0 {14,S} {16,S} {22,S} {23,S}
16 C u0 p0 c0 {15,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 O u0 p2 c0 {16,S} {19,S}
19 S u0 p0 c0 {16,S} {18,S} {20,D} {21,D}
20 O u0 p2 c0 {19,D}
21 O u0 p2 c0 {19,D}
22 F u0 p3 c0 {15,S}
23 F u0 p3 c0 {15,S}
24 F u0 p3 c0 {14,S}
25 F u0 p3 c0 {14,S}
26 F u0 p3 c0 {13,S}
27 F u0 p3 c0 {13,S}
28 F u0 p3 c0 {12,S}
29 F u0 p3 c0 {12,S}
30 F u0 p3 c0 {11,S}
31 F u0 p3 c0 {11,S}
32 F u0 p3 c0 {10,S}
33 F u0 p3 c0 {10,S}
34 F u0 p3 c0 {9,S}
35 F u0 p3 c0 {9,S}
36 F u0 p3 c0 {8,S}
37 F u0 p3 c0 {8,S}
38 F u0 p3 c0 {7,S}
39 F u0 p3 c0 {7,S}
40 F u0 p3 c0 {6,S}
41 F u0 p3 c0 {6,S}
42 F u0 p3 c0 {5,S}
43 F u0 p3 c0 {5,S}
44 F u0 p3 c0 {4,S}
45 F u0 p3 c0 {4,S}
46 F u0 p3 c0 {3,S}
47 F u0 p3 c0 {3,S}
48 F u0 p3 c0 {2,S}
49 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.8054294, 0.341241152, -0.000348220133, 1.61012329e-07, -2.7303255e-11, -780719.294, -4.99580933], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[65.4656082, 0.142408047, -0.000104364118, 3.42063004e-08, -4.2259137e-12, -794162.219, -296.801531], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (56.58348834678104,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)


entry(
    index = 325,
    label = "PF16Sultone",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {51,S} {52,S}
3  C u0 p0 c0 {2,S} {4,S} {49,S} {50,S}
4  C u0 p0 c0 {3,S} {5,S} {47,S} {48,S}
5  C u0 p0 c0 {4,S} {6,S} {45,S} {46,S}
6  C u0 p0 c0 {5,S} {7,S} {43,S} {44,S}
7  C u0 p0 c0 {6,S} {8,S} {41,S} {42,S}
8  C u0 p0 c0 {7,S} {9,S} {39,S} {40,S}
9  C u0 p0 c0 {8,S} {10,S} {37,S} {38,S}
10 C u0 p0 c0 {9,S} {11,S} {35,S} {36,S}
11 C u0 p0 c0 {10,S} {12,S} {33,S} {34,S}
12 C u0 p0 c0 {11,S} {13,S} {31,S} {32,S}
13 C u0 p0 c0 {12,S} {14,S} {29,S} {30,S}
14 C u0 p0 c0 {13,S} {15,S} {27,S} {28,S}
15 C u0 p0 c0 {14,S} {16,S} {25,S} {26,S}
16 C u0 p0 c0 {15,S} {17,S} {23,S} {24,S}
17 C u0 p0 c0 {16,S} {18,S} {19,S} {20,S}
18 F u0 p3 c0 {17,S}
19 O u0 p2 c0 {17,S} {20,S}
20 S u0 p0 c0 {17,S} {19,S} {21,D} {22,D}
21 O u0 p2 c0 {20,D}
22 O u0 p2 c0 {20,D}
23 F u0 p3 c0 {16,S}
24 F u0 p3 c0 {16,S}
25 F u0 p3 c0 {15,S}
26 F u0 p3 c0 {15,S}
27 F u0 p3 c0 {14,S}
28 F u0 p3 c0 {14,S}
29 F u0 p3 c0 {13,S}
30 F u0 p3 c0 {13,S}
31 F u0 p3 c0 {12,S}
32 F u0 p3 c0 {12,S}
33 F u0 p3 c0 {11,S}
34 F u0 p3 c0 {11,S}
35 F u0 p3 c0 {10,S}
36 F u0 p3 c0 {10,S}
37 F u0 p3 c0 {9,S}
38 F u0 p3 c0 {9,S}
39 F u0 p3 c0 {8,S}
40 F u0 p3 c0 {8,S}
41 F u0 p3 c0 {7,S}
42 F u0 p3 c0 {7,S}
43 F u0 p3 c0 {6,S}
44 F u0 p3 c0 {6,S}
45 F u0 p3 c0 {5,S}
46 F u0 p3 c0 {5,S}
47 F u0 p3 c0 {4,S}
48 F u0 p3 c0 {4,S}
49 F u0 p3 c0 {3,S}
50 F u0 p3 c0 {3,S}
51 F u0 p3 c0 {2,S}
52 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.19288182, 0.361958213, -0.00036800513, 1.69065039e-07, -2.83482753e-11, -830463.74, -6.8366436], Tmin=(298.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[69.5287263, 0.151350583, -0.000110916115, 3.63366532e-08, -4.48630521e-12, -844782.406, -317.096978], Tmin=(1000.0,'K'), Tmax=(2500.0,'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2500.0,'K'),
        Cp0 = (59.80494700918405,'J/(mol*K)'),
    ),
    reference = Reference(authors=["H. Ram", "Thomas P. Sadej", "C. Claire Murphy", "Tim J. Mallo", "Phillip R. Westmoreland"], title="NCSU_C2_C8_PFCAs", year="2023", url="https://doi.org/10.1021/acs.jpca.3c06937"),
    referenceType = "Theory",
    shortDesc = "QC calcs from North Carolina State University ( DOI: 10.1021/acs.jpca.3c06937) (work carried out in 2023)",
    longDesc = """QC calcs from : 
1. Ram, H.; Sadej, T.P.; Murphy, C.C.; Mallo, T.J.; Westmoreland, P.R. Thermochemistry of Species in Gas-Phase Thermal Oxidation of C2 to C8 Perfluorinated Carboxylic Acids. J. Phys. Chem. A 2024, 128, 7, 1313-1326. DOI: 10.1021/acs.jpca.3c06937. 
2. Ram, H.; Murphy, C.C.; Westmoreland, P.R. Thermochemistry for Gas-Phase Thermal Oxidation of PFAS: Perfluorinated Sulfonic Acids. Under Review, J. Phys. Chem. A, 2024. 
""",
)
