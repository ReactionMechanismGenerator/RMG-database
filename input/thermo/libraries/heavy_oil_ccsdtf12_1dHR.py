#!/usr/bin/env python
# encoding: utf-8

name = "heavy_oil_ccsdtf12_1dHR"
shortDesc = "Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann."
longDesc = """
This library is made by Kevin Spiekermann and contains the thermochemistry for select species from heavy oil pryolysis mechanisms.

All species were calculated using CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP i.e.
Optimization and frequency calculations were done at wB97X-D3/def2-TZVP with QChem.
High level single point calculations were done with CCSD(T)-F12a/cc-pVDZ-F12 with MOLPRO.

A thorough conformer search was done for all species included in this file. 
Although transition states are not included in this file, a conformer search was done on the TS as well since this is relevant for the kinetics of the training reactions added to the corresponding reaction families.
1D Hindered Rotors were calculated for steps of 10 degrees up to the full 360 degree cycle, with geometry optimization on each step.

The frequency scaling factor at ωB97X-D3/def2-TZVP was calculated as 0.984 using the method from Alecu et al. (https://pubs.acs.org/doi/abs/10.1021/ct100326h)
All values include atom energy corrections, which were fit to the single point energies of experimental geometries for 16 small molecules (no geometry optimization was performed).
All values also include bond additivity corrections.
BACs were fit using about 400 species from our reference set using the procedure from Petersson et al. 1998 (http://aip.scitation.org/doi/10.1063/1.477794)

Disclaimer: The number of significant figures displayed does not reflect the accuracy of the thermochemistry values.
After fitting the Petersson BACs, the enthalpy values at the coupled cluster level have an MAE (RMSE) of 0.52 (0.83) kcal/mol relative to our reference set.
These values are similar to those from other published works:
- Bischoff, F. A., Wolfsegger, S., Tew, D. P. & Klopper, W. Assessment of basis sets for f12 explicitly-correlated molecular electronic-structure methodfs. Mol. Phys. 107, 963–975 (2009).
- Knizia, G., Adler, T. B. & Werner, H.-J. Simplified ccsd (t)-f12 methods: Theory and benchmarks. The J. chemical physics 130, 054104 (2009). 
- Adler, T. B., Knizia, G. & Werner, H.-J. A simple and efficient ccsd(t)-f12 approximation (2007).
- Pfeiffer, F., Rauhut, G., Feller, D. & Peterson, K. A. Anharmonic zero point vibrational energies: Tipping the scales in accurate thermochemistry calculations? The J. chemical physics 138, 044311 (2013).
- Shang, Y., Ning, H., Shi, J., Wang, H. & Luo, S.-N. Chemical kinetics of h-abstractions from dimethyl amine by h, ch 3, oh, and ho 2 radicals with multi-structural torsional anharmonicity. Phys. Chem. Chem. Phys. 21, 12685–12696 (2019).
"""
entry(
    index = 0,
    label = "product0",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
5  C u1 p0 c0 {3,S} {4,S} {15,S}
6  C u0 p0 c0 {1,S} {7,D} {16,S}
7  C u0 p0 c0 {6,D} {17,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9257,0.00488388,0.000218528,-4.34102e-07,2.83245e-10,19471.1,12.6608], Tmin=(10,'K'), Tmax=(392.75,'K')),
            NASAPolynomial(coeffs=[-2.84849,0.0738789,-4.49891e-05,1.32176e-08,-1.50109e-12,20003.2,39.011], Tmin=(392.75,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (161.878,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (432.353,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 1,
    label = "product1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {6,D} {15,S}
6  C u0 p0 c0 {3,S} {5,D} {16,S}
7  C u1 p0 c0 {1,S} {17,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93148,0.00443778,0.000214765,-4.15326e-07,2.62941e-10,18256.3,11.7966], Tmin=(10,'K'), Tmax=(408.605,'K')),
            NASAPolynomial(coeffs=[-3.22181,0.0750039,-4.62666e-05,1.37976e-08,-1.59062e-12,18836.4,39.8497], Tmin=(408.605,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (151.777,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (432.353,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 2,
    label = "reactant0",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {5,D} {12,S}
4  C u0 p0 c0 {1,S} {6,D} {13,S}
5  C u0 p0 c0 {3,D} {7,S} {14,S}
6  C u0 p0 c0 {4,D} {17,S} {18,S}
7  C u1 p0 c0 {5,S} {15,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71953,0.0393074,2.68863e-05,-5.10858e-08,1.9113e-11,21097.9,12.6025], Tmin=(10,'K'), Tmax=(1008.73,'K')),
            NASAPolynomial(coeffs=[5.44059,0.0545486,-2.85895e-05,7.26324e-09,-7.22401e-13,19628.1,-1.28013], Tmin=(1008.73,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (175.467,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (432.353,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

