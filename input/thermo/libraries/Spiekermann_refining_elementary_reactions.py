#!/usr/bin/env python
# encoding: utf-8

name = "Spiekermann_refining_elementary_reactions"
shortDesc = "Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann."
longDesc = """
This library is made by Kevin Spiekermann and contains the thermochemistry for a subset of the species from 
Spiekermann, K. A.; Pattanaik, L.; Green, W. H. 
High accuracy barrier heights, enthalpies, and rate coefficients for chemical reactions.
Sci. data 9, 1-12 (2022).
https://www.nature.com/articles/s41597-022-01529-6

This published work reports nearly 12,000 reactions, with over 1,000 reactions matching RMG templates. 
The species included in this file represent a subset of the species participating in these RMG reactions.
All species were calculated with multiplicity 1 and charge 0 using CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP i.e.
Optimization and frequency calculations were done at wB97X-D3/def2-TZVP with QChem.
High level single point calculations were done with CCSD(T)-F12a/cc-pVDZ-F12 with MOLPRO.

Many of the geometry optimizations and frequency calculations were originally done by Grambow et al. in 
Grambow, C. A., Pattanaik, L. & Green, W. H. 
Reactants, products, and transition states of elementary chemical reactions based on quantum chemistry.
Sci. data 7, 1–8 (2020).
https://www.nature.com/articles/s41597-020-0460-4

Note that neither the published work from Spiekermann et al. nor from Grambow et al. included a systematic conformer search. 
Here, a thorough conformer search was done for all species included in this file, so many values are an improvement from those in the originally published work.
If the species has rotatable bonds, a conformer search was done with the Automated Conformer Search (ACS) software developed by Oscar Wu and Xiaorui Dong and modified by Kevin Spiekermann (qchem branch). 
The lowest energy conformer was then used when calculating thermochemistry values. 
Although transition states are not included in this file, a conformer search was done on the TS as well since this is relevant for the kinetics of the training reactions added to the corresponding reaction families.
Species were chosen so that ring conformers did not need to be explored i.e. any rings present in a species are planar (either aromatic or 3-membered).
The relevant settings in ACS were:
n_point_each_torsion: 30
n_rotors_to_couple: 2
vdw_collision_threshold: 0.3

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
    label = "p000017",
    molecule = 
"""
1 O u0 p2 c0 {5,D}
2 N u0 p1 c0 {5,S} {6,S} {7,S}
3 N u0 p1 c0 {4,S} {5,S} {9,S}
4 N u0 p1 c0 {3,S} {6,D}
5 C u0 p0 c0 {1,D} {2,S} {3,S}
6 C u0 p0 c0 {2,S} {4,D} {8,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08315,-0.00834958,0.00015685,-2.81708e-07,1.60589e-10,-3863.8,9.73083], Tmin=(10,'K'), Tmax=(568.266,'K')),
            NASAPolynomial(coeffs=[1.5925,0.0344212,-2.26705e-05,7.0561e-09,-8.33299e-13,-3988.25,16.7535], Tmin=(568.266,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-32.1451,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 1,
    label = "p000049",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {12,S}
2  N u0 p1 c0 {4,S} {5,D}
3  N u0 p1 c0 {5,S} {6,D}
4  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {2,D} {3,S} {11,S}
6  C u0 p0 c0 {1,S} {3,D} {10,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63265,0.0311299,1.5192e-06,-1.86464e-08,7.80231e-12,-7886.38,11.1185], Tmin=(10,'K'), Tmax=(1010.22,'K')),
            NASAPolynomial(coeffs=[5.01781,0.0356248,-1.99727e-05,5.31518e-09,-5.47381e-13,-8675.47,1.9015], Tmin=(1010.22,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-65.6001,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 2,
    label = "p000208",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {5,S} {9,S}
3 C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
4 C u0 p0 c0 {1,S} {3,S} {5,D}
5 C u0 p0 c0 {2,S} {4,D} {8,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81333,0.0204806,3.62902e-06,-1.57751e-08,6.56952e-12,-10720,9.23438], Tmin=(10,'K'), Tmax=(983.11,'K')),
            NASAPolynomial(coeffs=[5.08542,0.0231528,-1.24222e-05,3.22948e-09,-3.28088e-13,-11349.4,1.1901], Tmin=(983.11,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-89.126,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 3,
    label = "p000314",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {6,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,S} {4,S} {8,S}
4 C u0 p0 c0 {2,D} {3,S} {5,S}
5 C u0 p0 c0 {4,S} {6,D} {7,S}
6 C u0 p0 c0 {1,S} {5,D} {9,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10247,-0.0101348,0.000168818,-3.04704e-07,1.75036e-10,-11128.5,9.78109], Tmin=(10,'K'), Tmax=(564.253,'K')),
            NASAPolynomial(coeffs=[1.54673,0.0350531,-2.32712e-05,7.27411e-09,-8.61354e-13,-11271,16.8299], Tmin=(564.253,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-92.548,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 4,
    label = "p000399",
    molecule = 
"""
1 O u0 p3 c-1 {6,S}
2 N u0 p0 c+1 {5,D} {6,S} {8,S}
3 N u0 p1 c0 {4,S} {5,S} {9,S}
4 N u0 p1 c0 {3,S} {6,D}
5 C u0 p0 c0 {2,D} {3,S} {7,S}
6 C u0 p0 c0 {1,S} {2,S} {4,D}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.13164,-0.0124889,0.000177785,-3.16891e-07,1.80337e-10,5043.18,9.73761], Tmin=(10,'K'), Tmax=(570.396,'K')),
            NASAPolynomial(coeffs=[1.51597,0.0348951,-2.31945e-05,7.2699e-09,-8.62857e-13,4869.14,16.747], Tmin=(570.396,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (41.9129,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 5,
    label = "p000401",
    molecule = 
"""
1 O u0 p2 c0 {5,D}
2 N u0 p1 c0 {3,S} {5,S} {7,S}
3 N u0 p1 c0 {2,S} {6,S} {8,S}
4 N u0 p1 c0 {5,S} {6,D}
5 C u0 p0 c0 {1,D} {2,S} {4,S}
6 C u0 p0 c0 {3,S} {4,D} {9,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.1036,-0.00984831,0.000159384,-2.79814e-07,1.56573e-10,4040.08,9.73985], Tmin=(10,'K'), Tmax=(576.554,'K')),
            NASAPolynomial(coeffs=[1.29232,0.0349484,-2.29648e-05,7.12335e-09,-8.38528e-13,3943.87,18.1088], Tmin=(576.554,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (33.5744,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 6,
    label = "p000634",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {10,S}
2  N u0 p1 c0 {3,S} {4,D}
3  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {2,D} {9,S}
5  C u0 p0 c0 {3,S} {6,T}
6  C u0 p0 c0 {5,T} {11,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83886,0.0139251,0.000191255,-6.59717e-07,6.99288e-10,11212.2,10.4675], Tmin=(10,'K'), Tmax=(310.255,'K')),
            NASAPolynomial(coeffs=[3.36206,0.0394479,-2.58155e-05,8.00429e-09,-9.4812e-13,11148.5,10.7069], Tmin=(310.255,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (93.2547,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 7,
    label = "p000721",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {11,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  C u0 p0 c0 {4,S} {6,T}
6  C u0 p0 c0 {5,T} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80596,0.0145653,0.000179922,-5.26243e-07,4.55672e-10,5604.76,10.3639], Tmin=(10,'K'), Tmax=(396.315,'K')),
            NASAPolynomial(coeffs=[4.37112,0.0387071,-2.44151e-05,7.50698e-09,-8.9093e-13,5325.58,5.20332], Tmin=(396.315,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (46.6098,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 8,
    label = "p000726",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {11,S}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {9,S} {10,S}
5  C u0 p0 c0 {2,S} {6,T}
6  C u0 p0 c0 {5,T} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79047,0.0134968,0.000172855,-4.23838e-07,2.98893e-10,8411.79,10.4369], Tmin=(10,'K'), Tmax=(501.479,'K')),
            NASAPolynomial(coeffs=[6.25923,0.036542,-2.39093e-05,7.68141e-09,-9.49864e-13,7626.81,-5.12745], Tmin=(501.479,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (69.887,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 9,
    label = "p000744",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {11,S}
2  N u0 p1 c0 {6,T}
3  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {1,S} {4,D} {10,S}
6  C u0 p0 c0 {2,T} {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86044,0.0145339,0.000207876,-9.15058e-07,1.28653e-09,-2838.79,11.247], Tmin=(10,'K'), Tmax=(224.356,'K')),
            NASAPolynomial(coeffs=[3.22672,0.037547,-2.43061e-05,7.59276e-09,-9.09665e-13,-2839.84,12.7002], Tmin=(224.356,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-23.5639,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 10,
    label = "p000813",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {6,S}
2  O u0 p2 c0 {6,S} {12,S}
3  N u0 p1 c0 {6,D} {13,S}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
5  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {1,S} {2,S} {3,D}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90723,0.0359907,-7.07218e-06,-9.51471e-09,4.13273e-12,-46353.2,8.70544], Tmin=(10,'K'), Tmax=(1260.14,'K')),
            NASAPolynomial(coeffs=[13.2832,0.0222572,-9.80344e-06,2.02375e-09,-1.58842e-13,-49988.8,-43.7455], Tmin=(1260.14,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-385.336,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (291.007,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 11,
    label = "p000842",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  N u0 p1 c0 {1,D} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93846,0.00746404,0.000362497,-2.43626e-06,5.88578e-09,-1497.43,9.00632], Tmin=(10,'K'), Tmax=(103.642,'K')),
            NASAPolynomial(coeffs=[3.25927,0.0336765,-1.68703e-05,3.96667e-09,-3.52153e-13,-1483.36,10.7434], Tmin=(103.642,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-9.71827,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 12,
    label = "p001050",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {6,S} {12,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
5  C u0 p0 c0 {1,S} {3,S} {6,D}
6  C u0 p0 c0 {2,S} {5,D} {11,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62708,0.0349892,-1.38434e-05,-1.85582e-09,1.91845e-12,-16444.3,10.5772], Tmin=(10,'K'), Tmax=(1154.87,'K')),
            NASAPolynomial(coeffs=[7.34748,0.0288117,-1.4533e-05,3.57203e-09,-3.45359e-13,-17751,-9.8441], Tmin=(1154.87,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-136.75,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 13,
    label = "p001085",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {9,S}
2  O u0 p2 c0 {6,D}
3  N u0 p1 c0 {5,S} {6,S} {7,S}
4  N u0 p1 c0 {5,D} {10,S}
5  C u0 p0 c0 {1,S} {3,S} {4,D}
6  C u0 p0 c0 {2,D} {3,S} {8,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74528,0.0199317,4.9871e-05,-1.20506e-07,8.0885e-11,-40053.6,10.9897], Tmin=(10,'K'), Tmax=(391.235,'K')),
            NASAPolynomial(coeffs=[1.83109,0.0395023,-2.51626e-05,7.35157e-09,-8.1563e-13,-39903.8,18.4281], Tmin=(391.235,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-333.065,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 14,
    label = "p001088",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {6,S}
2  O u0 p2 c0 {6,D}
3  N u0 p1 c0 {5,S} {7,S} {8,S}
4  N u0 p1 c0 {5,D} {10,S}
5  C u0 p0 c0 {1,S} {3,S} {4,D}
6  C u0 p0 c0 {1,S} {2,D} {9,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72242,0.0294883,1.41007e-06,-2.49661e-08,1.24941e-11,-36583,10.6782], Tmin=(10,'K'), Tmax=(876.419,'K')),
            NASAPolynomial(coeffs=[6.76815,0.0278153,-1.66549e-05,4.69481e-09,-5.07772e-13,-37586.5,-6.29309], Tmin=(876.419,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-304.168,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 15,
    label = "p001089",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {10,S}
2  O u0 p2 c0 {5,D}
3  N u0 p1 c0 {5,S} {8,S} {9,S}
4  N u0 p1 c0 {5,S} {6,D}
5  C u0 p0 c0 {2,D} {3,S} {4,S}
6  C u0 p0 c0 {1,S} {4,D} {7,S}
7  H u0 p0 c0 {6,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73273,0.0255802,2.61114e-05,-6.5876e-08,3.38022e-11,-42219.2,9.69998], Tmin=(10,'K'), Tmax=(735.919,'K')),
            NASAPolynomial(coeffs=[5.35014,0.0327411,-2.09989e-05,6.25594e-09,-7.07968e-13,-42889.3,-0.541993], Tmin=(735.919,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-351.052,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 16,
    label = "p001091_0",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 N u0 p1 c0 {3,D} {4,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98565,0.000809807,2.38288e-05,-4.13856e-08,2.21924e-11,-15775.5,4.98696], Tmin=(10,'K'), Tmax=(587.751,'K')),
            NASAPolynomial(coeffs=[3.21484,0.00929968,-6.11737e-06,1.97211e-09,-2.44116e-13,-15740.9,7.81935], Tmin=(587.751,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-131.172,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 17,
    label = "p001091_1",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {5,S}
2 N u0 p1 c0 {3,D} {6,S}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03412,-0.00275045,5.5691e-05,-8.33609e-08,3.96279e-11,-17161.3,7.11129], Tmin=(10,'K'), Tmax=(659.917,'K')),
            NASAPolynomial(coeffs=[1.85443,0.01866,-1.16107e-05,3.45518e-09,-3.93126e-13,-17052.1,15.3685], Tmin=(659.917,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-142.687,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 18,
    label = "p001147",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {13,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {3,S} {5,D}
5  C u0 p0 c0 {1,S} {4,D} {12,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65306,0.0315714,-4.7653e-06,-8.32774e-09,3.49633e-12,-24168.8,10.2154], Tmin=(10,'K'), Tmax=(1158.43,'K')),
            NASAPolynomial(coeffs=[5.6154,0.0324883,-1.59135e-05,3.8204e-09,-3.6245e-13,-25139.6,-1.7682], Tmin=(1158.43,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-200.977,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 19,
    label = "p001169",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {7,S}
2 O u0 p2 c0 {5,D}
3 N u0 p1 c0 {4,D} {8,S}
4 C u0 p0 c0 {1,S} {3,D} {5,S}
5 C u0 p0 c0 {2,D} {4,S} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94233,0.00322041,0.000105484,-2.14975e-07,1.33819e-10,-31718.4,9.45332], Tmin=(10,'K'), Tmax=(523.115,'K')),
            NASAPolynomial(coeffs=[2.43759,0.031122,-2.15359e-05,6.81512e-09,-8.09867e-13,-31785.3,13.5936], Tmin=(523.115,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-263.746,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (174.604,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 20,
    label = "p001235",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {4,D}
3 N u0 p1 c0 {5,D} {8,S}
4 C u0 p0 c0 {1,S} {2,D} {6,S}
5 C u0 p0 c0 {1,S} {3,D} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90417,0.00687764,9.87203e-05,-2.47877e-07,1.88703e-10,58261.1,9.18629], Tmin=(10,'K'), Tmax=(433.032,'K')),
            NASAPolynomial(coeffs=[3.31187,0.026356,-1.7272e-05,5.39569e-09,-6.42742e-13,58181,10.0317], Tmin=(433.032,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (484.404,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 21,
    label = "p001357",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {15,S}
2  N u0 p1 c0 {3,S} {6,D}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {1,S} {2,D} {14,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88185,0.0101296,0.00026352,-8.24169e-07,8.42998e-10,-27192.1,10.3398], Tmin=(10,'K'), Tmax=(295.269,'K')),
            NASAPolynomial(coeffs=[1.65322,0.0545043,-3.39624e-05,1.01821e-08,-1.17885e-12,-27122.4,17.326], Tmin=(295.269,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-226.057,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (340.893,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 22,
    label = "p001387",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {14,S}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
5  C u0 p0 c0 {1,S} {2,S} {6,D}
6  C u0 p0 c0 {5,D} {12,S} {13,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85754,0.00856986,0.000169806,-3.43926e-07,2.10051e-10,-9429.2,10.4147], Tmin=(10,'K'), Tmax=(545.135,'K')),
            NASAPolynomial(coeffs=[2.44471,0.0505768,-3.28419e-05,1.03712e-08,-1.25827e-12,-9745.29,12.0616], Tmin=(545.135,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-78.4517,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 23,
    label = "p001388",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {14,S}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {6,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {3,S} {6,D}
6  C u0 p0 c0 {1,S} {4,S} {5,D}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86246,0.00881132,0.000178944,-3.89233e-07,2.58997e-10,-4839.64,10.6522], Tmin=(10,'K'), Tmax=(492.332,'K')),
            NASAPolynomial(coeffs=[2.08613,0.0506836,-3.22323e-05,9.92755e-09,-1.17592e-12,-4997.29,14.5858], Tmin=(492.332,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-40.2735,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 24,
    label = "p001614",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {11,S}
2  O u0 p2 c0 {5,D}
3  N u0 p1 c0 {5,S} {9,S} {10,S}
4  C u0 p0 c0 {5,S} {6,D} {7,S}
5  C u0 p0 c0 {2,D} {3,S} {4,S}
6  C u0 p0 c0 {1,S} {4,D} {8,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72702,0.0224947,0.000134371,-4.47717e-07,4.13474e-10,-39632.5,10.3516], Tmin=(10,'K'), Tmax=(381.842,'K')),
            NASAPolynomial(coeffs=[4.78479,0.0372583,-2.51495e-05,8.04806e-09,-9.77345e-13,-39901.7,3.7998], Tmin=(381.842,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-329.508,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 25,
    label = "p001615",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {11,S}
2  O u0 p2 c0 {6,D}
3  N u0 p1 c0 {4,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {3,S} {5,D}
5  C u0 p0 c0 {4,D} {6,S} {7,S}
6  C u0 p0 c0 {2,D} {5,S} {8,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.858,0.00968688,0.000155078,-3.88805e-07,2.93332e-10,-41383.7,10.2394], Tmin=(10,'K'), Tmax=(450.972,'K')),
            NASAPolynomial(coeffs=[4.14523,0.0347414,-2.00658e-05,5.82841e-09,-6.74665e-13,-41690.3,5.97052], Tmin=(450.972,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-344.1,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 26,
    label = "p001627",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {6,S} {10,S}
3  N u0 p1 c0 {6,D} {11,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
6  C u0 p0 c0 {2,S} {3,D} {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91608,0.00487646,0.000129902,-2.40017e-07,1.35521e-10,-24978.8,10.4281], Tmin=(10,'K'), Tmax=(564.273,'K')),
            NASAPolynomial(coeffs=[0.501141,0.0476099,-3.29423e-05,1.05596e-08,-1.27439e-12,-24888.3,22.3357], Tmin=(564.273,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-207.721,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 27,
    label = "p001956_0",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08222,-0.00485602,3.07495e-05,-3.09496e-08,1.01414e-11,9102.79,4.36603], Tmin=(10,'K'), Tmax=(927.515,'K')),
            NASAPolynomial(coeffs=[0.891011,0.0136941,-6.99295e-06,1.74363e-09,-1.70675e-13,9488.83,18.4115], Tmin=(927.515,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (75.7069,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 28,
    label = "p001958",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 O u0 p2 c0 {5,D}
3 N u0 p1 c0 {4,S} {5,S} {6,S}
4 C u0 p0 c0 {1,D} {3,S} {7,S}
5 C u0 p0 c0 {2,D} {3,S} {8,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66855,0.0286017,-5.31907e-05,8.57569e-08,-5.31814e-11,-40063.3,8.52118], Tmin=(10,'K'), Tmax=(555.319,'K')),
            NASAPolynomial(coeffs=[2.60947,0.0252908,-1.4698e-05,4.07179e-09,-4.37269e-13,-39777,14.5264], Tmin=(555.319,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-333.124,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (174.604,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 29,
    label = "p002203",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {13,S}
2  N u0 p1 c0 {3,S} {5,S} {12,S}
3  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
5  C u0 p0 c0 {2,S} {3,S} {6,D}
6  C u0 p0 c0 {1,S} {4,S} {5,D}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82764,0.0125963,0.000188724,-5.1754e-07,4.28856e-10,4508.76,10.2277], Tmin=(10,'K'), Tmax=(406.756,'K')),
            NASAPolynomial(coeffs=[3.77374,0.0419153,-2.55621e-05,7.67524e-09,-8.97285e-13,4274.99,7.51173], Tmin=(406.756,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (37.4913,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 30,
    label = "p002204",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {13,S}
2  N u0 p1 c0 {3,S} {4,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {3,S} {6,D}
6  C u0 p0 c0 {5,D} {11,S} {12,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86782,0.00750574,0.000152415,-2.86946e-07,1.61025e-10,-1164.11,10.1179], Tmin=(10,'K'), Tmax=(596.695,'K')),
            NASAPolynomial(coeffs=[2.2463,0.0501745,-3.47846e-05,1.15167e-08,-1.44251e-12,-1536.69,12.3599], Tmin=(596.695,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-9.73776,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 31,
    label = "p002312",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {13,S}
2  N u0 p1 c0 {3,S} {6,D}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
6  C u0 p0 c0 {1,S} {2,D} {12,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89827,0.00614791,0.000156893,-3.05477e-07,1.83212e-10,-6980.98,10.1325], Tmin=(10,'K'), Tmax=(531.611,'K')),
            NASAPolynomial(coeffs=[0.578424,0.0526025,-3.4778e-05,1.08762e-08,-1.29424e-12,-6931.46,21.1971], Tmin=(531.611,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-58.0801,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 32,
    label = "p002395_0",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,D}
2 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84282,0.0114012,1.08963e-05,-1.69991e-08,6.2854e-12,8031.38,6.84947], Tmin=(10,'K'), Tmax=(759.897,'K')),
            NASAPolynomial(coeffs=[1.64636,0.0229631,-1.19263e-05,3.02345e-09,-3.01857e-13,8365.19,16.843], Tmin=(759.897,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (66.752,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 33,
    label = "p002513",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {6,D}
3 N u0 p0 c+1 {5,D} {6,S} {7,S}
4 N u0 p2 c-1 {1,S} {6,S}
5 N u0 p1 c0 {1,S} {3,D}
6 C u0 p0 c0 {2,D} {3,S} {4,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.09657,-0.00907939,0.000135813,-2.38726e-07,1.32296e-10,19122.4,9.71784], Tmin=(10,'K'), Tmax=(593.188,'K')),
            NASAPolynomial(coeffs=[2.40613,0.0272365,-1.9027e-05,6.10616e-09,-7.33056e-13,18884.5,13.2953], Tmin=(593.188,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (158.977,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 34,
    label = "p002594",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {5,S} {9,S}
3  N u0 p1 c0 {5,D} {10,S}
4  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {1,S} {2,S} {3,D}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9103,0.00575796,0.000122298,-2.62827e-07,1.7312e-10,-41720.2,10.2154], Tmin=(10,'K'), Tmax=(490.434,'K')),
            NASAPolynomial(coeffs=[2.19959,0.0367526,-2.46225e-05,7.74213e-09,-9.2073e-13,-41757.4,15.1603], Tmin=(490.434,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-346.904,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 35,
    label = "p002675",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {11,S}
2  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {3,S} {5,D}
5  C u0 p0 c0 {1,S} {4,D} {10,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91425,0.00491787,0.000118211,-2.17517e-07,1.21734e-10,1003.28,9.06703], Tmin=(10,'K'), Tmax=(580.799,'K')),
            NASAPolynomial(coeffs=[1.48157,0.0415479,-2.77244e-05,8.91584e-09,-1.0942e-12,950.621,16.5956], Tmin=(580.799,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (8.30413,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 36,
    label = "p002689",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {11,S}
2  N u0 p1 c0 {6,T}
3  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {1,S} {4,D} {6,S}
6  C u0 p0 c0 {2,T} {5,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82036,0.0189417,0.000221985,-1.14186e-06,1.76217e-09,-3680.95,10.2873], Tmin=(10,'K'), Tmax=(222.234,'K')),
            NASAPolynomial(coeffs=[4.11775,0.0342765,-2.11515e-05,6.38507e-09,-7.47089e-13,-3745.25,8.15052], Tmin=(222.234,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-30.5603,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 37,
    label = "p002760",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {9,S}
2 O u0 p2 c0 {5,D}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {3,D} {7,S} {8,S}
5 C u0 p0 c0 {2,D} {3,S} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91878,0.00553418,9.26815e-05,-1.86784e-07,1.21047e-10,-33219.5,9.29758], Tmin=(10,'K'), Tmax=(396.506,'K')),
            NASAPolynomial(coeffs=[0.910002,0.0358871,-2.2145e-05,6.28032e-09,-6.80819e-13,-32980.9,21.0299], Tmin=(396.506,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-276.226,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 38,
    label = "p002774",
    molecule = 
"""
1 O u0 p2 c0 {5,D}
2 N u0 p1 c0 {3,S} {4,S} {5,S}
3 N u0 p1 c0 {2,S} {4,D}
4 C u0 p0 c0 {2,S} {3,D} {6,S}
5 C u0 p0 c0 {1,D} {2,S} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.896,0.0161115,2.88027e-06,-1.34886e-08,5.73028e-12,32730.1,9.54122], Tmin=(10,'K'), Tmax=(998.201,'K')),
            NASAPolynomial(coeffs=[5.95965,0.0158419,-8.7362e-06,2.29845e-09,-2.34419e-13,31919.6,-2.40737], Tmin=(998.201,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (272.157,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 39,
    label = "p002801",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {6,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
5  C u0 p0 c0 {1,S} {3,S} {6,D}
6  C u0 p0 c0 {2,S} {4,S} {5,D}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86044,0.0151987,0.000330194,-1.80935e-06,3.07654e-09,-16645.6,9.69766], Tmin=(10,'K'), Tmax=(199.852,'K')),
            NASAPolynomial(coeffs=[4.09868,0.0361854,-2.06257e-05,5.73488e-09,-6.23456e-13,-16706.6,7.64512], Tmin=(199.852,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-138.241,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 40,
    label = "p002874",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {8,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u0 p0 c0 {2,D} {6,S} {7,S}
4 C u0 p0 c0 {2,S} {5,T}
5 C u0 p0 c0 {4,T} {9,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86792,0.0084503,0.00011779,-2.79503e-07,1.93169e-10,12258,9.19808], Tmin=(10,'K'), Tmax=(504.792,'K')),
            NASAPolynomial(coeffs=[4.95457,0.026928,-1.76106e-05,5.62279e-09,-6.89654e-13,11803.2,1.27999], Tmin=(504.792,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (101.884,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 41,
    label = "p002881",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {12,S}
2  O u0 p2 c0 {4,D}
3  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {3,S} {5,S}
5  C u0 p0 c0 {1,S} {4,S} {6,D}
6  C u0 p0 c0 {5,D} {10,S} {11,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69017,0.0225328,5.08911e-05,-1.12327e-07,6.89656e-11,-39468.1,10.8486], Tmin=(10,'K'), Tmax=(427.27,'K')),
            NASAPolynomial(coeffs=[1.36919,0.0442611,-2.5389e-05,6.69167e-09,-6.72742e-13,-39269.8,20.0724], Tmin=(427.27,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-328.233,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 42,
    label = "p003070",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {9,S}
2  N u0 p1 c0 {5,D} {10,S}
3  N u0 p1 c0 {6,T}
4  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {1,S} {2,D} {4,S}
6  C u0 p0 c0 {3,T} {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85817,0.00996158,0.000148892,-3.91546e-07,3.07498e-10,-6652.54,10.5691], Tmin=(10,'K'), Tmax=(432.843,'K')),
            NASAPolynomial(coeffs=[4.0374,0.0337178,-2.15e-05,6.53263e-09,-7.662e-13,-6906.11,7.10456], Tmin=(432.843,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-55.3208,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 43,
    label = "p003183",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {6,S}
2 N u0 p1 c0 {3,D} {7,S}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 C u0 p0 c0 {3,S} {5,T}
5 C u0 p0 c0 {4,T} {8,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92139,0.00449384,9.2293e-05,-1.75513e-07,9.92664e-11,10875.7,8.99332], Tmin=(10,'K'), Tmax=(589.697,'K')),
            NASAPolynomial(coeffs=[2.76273,0.0309312,-2.22119e-05,7.36225e-09,-9.1209e-13,10689.4,11.2324], Tmin=(589.697,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (90.3914,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 44,
    label = "p003195",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {10,S}
2  O u0 p2 c0 {5,S} {9,S}
3  O u0 p2 c0 {6,D}
4  C u0 p0 c0 {1,S} {5,D} {6,S}
5  C u0 p0 c0 {2,S} {4,D} {7,S}
6  C u0 p0 c0 {3,D} {4,S} {8,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91369,0.0073615,0.000189066,-6.19452e-07,6.54015e-10,-52568.8,10.8658], Tmin=(10,'K'), Tmax=(298.063,'K')),
            NASAPolynomial(coeffs=[2.85217,0.0353819,-2.12683e-05,6.0461e-09,-6.68696e-13,-52566.7,13.6757], Tmin=(298.063,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-437.062,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 45,
    label = "p003323",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {8,S}
2 N u0 p1 c0 {5,T}
3 C u0 p0 c0 {1,S} {4,D} {7,S}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 C u0 p0 c0 {2,T} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88496,0.00897189,9.54324e-05,-2.63293e-07,2.1839e-10,-642.782,8.99471], Tmin=(10,'K'), Tmax=(398.048,'K')),
            NASAPolynomial(coeffs=[3.43636,0.0261666,-1.7173e-05,5.37551e-09,-6.41803e-13,-707.576,9.48319], Tmin=(398.048,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-5.34073,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 46,
    label = "p003344",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {11,S}
2  N u0 p1 c0 {5,S} {9,S} {10,S}
3  N u0 p1 c0 {4,S} {5,D}
4  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {1,S} {2,S} {3,D}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93375,0.00753724,0.000315939,-1.88131e-06,3.99066e-09,-22602.1,8.71993], Tmin=(10,'K'), Tmax=(118.139,'K')),
            NASAPolynomial(coeffs=[3.15661,0.0338523,-1.82138e-05,4.51698e-09,-4.22639e-13,-22583.7,10.8092], Tmin=(118.139,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-186.665,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 47,
    label = "p003346",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {10,S}
2  N u0 p1 c0 {4,S} {5,S} {9,S}
3  N u0 p1 c0 {5,D} {11,S}
4  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {1,S} {2,S} {3,D}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72914,0.0209959,3.3901e-05,-7.49023e-08,4.28295e-11,-22643.5,10.1494], Tmin=(10,'K'), Tmax=(467.895,'K')),
            NASAPolynomial(coeffs=[1.64191,0.0388395,-2.33029e-05,6.60325e-09,-7.1962e-13,-22448.2,18.6338], Tmin=(467.895,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-188.314,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 48,
    label = "p003348",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u0 p0 c0 {2,D} {5,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96458,0.00201312,5.8329e-05,-1.02463e-07,5.55792e-11,-16471.7,6.25516], Tmin=(10,'K'), Tmax=(582.088,'K')),
            NASAPolynomial(coeffs=[2.1722,0.0223264,-1.46231e-05,4.68929e-09,-5.77452e-13,-16398.5,12.7688], Tmin=(582.088,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-136.97,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 49,
    label = "p003431",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {11,S}
2  O u0 p2 c0 {5,D}
3  N u0 p1 c0 {5,S} {6,D}
4  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {2,D} {3,S} {4,S}
6  C u0 p0 c0 {1,S} {3,D} {10,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91064,0.0237174,1.73272e-05,-3.43609e-08,1.31223e-11,-39980.3,10.8451], Tmin=(10,'K'), Tmax=(1023.99,'K')),
            NASAPolynomial(coeffs=[7.32512,0.0282348,-1.54454e-05,4.00383e-09,-4.01477e-13,-41615.7,-10.2796], Tmin=(1023.99,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-332.347,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 50,
    label = "p003437",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {12,S}
2  N u0 p1 c0 {6,D} {13,S}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
6  C u0 p0 c0 {1,S} {2,D} {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87031,0.0162902,6.72365e-05,-1.03494e-07,4.41068e-11,-12355.7,10.2333], Tmin=(10,'K'), Tmax=(796.601,'K')),
            NASAPolynomial(coeffs=[1.94139,0.0462748,-2.74475e-05,7.73435e-09,-8.39351e-13,-12692.4,15.058], Tmin=(796.601,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-102.714,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 51,
    label = "p003440",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {13,S}
2  N u0 p1 c0 {6,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {4,S} {6,D}
6  C u0 p0 c0 {1,S} {2,S} {5,D}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84221,0.0107492,0.00017705,-4.24284e-07,3.08195e-10,-363.607,11.2834], Tmin=(10,'K'), Tmax=(456.254,'K')),
            NASAPolynomial(coeffs=[2.85792,0.0466002,-3.031e-05,9.47233e-09,-1.13027e-12,-557.124,12.1546], Tmin=(456.254,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-3.04447,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 52,
    label = "p003454",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {11,S}
2  N u0 p1 c0 {4,S} {5,S} {6,S}
3  N u0 p1 c0 {6,D} {12,S}
4  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
5  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
6  C u0 p0 c0 {1,S} {2,S} {3,D}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93071,0.00400401,0.000134186,-2.37377e-07,1.30188e-10,-2213.4,11.1003], Tmin=(10,'K'), Tmax=(559.016,'K')),
            NASAPolynomial(coeffs=[-1.05604,0.0537607,-3.70905e-05,1.19213e-08,-1.44314e-12,-1875.78,30.2914], Tmin=(559.016,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-18.4335,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 53,
    label = "p003718",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {12,S}
2  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {6,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  C u0 p0 c0 {2,S} {6,T}
6  C u0 p0 c0 {3,S} {5,T}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81777,0.0189526,0.000239308,-1.12816e-06,1.6444e-09,6587.54,10.3937], Tmin=(10,'K'), Tmax=(226.98,'K')),
            NASAPolynomial(coeffs=[3.63445,0.0406158,-2.56677e-05,7.88671e-09,-9.34435e-13,6548.38,9.96025], Tmin=(226.98,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (54.8133,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 54,
    label = "p003937",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {10,S}
2  N u0 p1 c0 {4,S} {5,D}
3  N u0 p1 c0 {6,T}
4  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {1,S} {2,D} {9,S}
6  C u0 p0 c0 {3,T} {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8793,0.0123597,0.00024728,-1.16525e-06,1.73112e-09,-1348.66,10.3028], Tmin=(10,'K'), Tmax=(220.963,'K')),
            NASAPolynomial(coeffs=[3.62058,0.034557,-2.22982e-05,6.79804e-09,-7.92977e-13,-1379.98,10.1929], Tmin=(220.963,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-11.1718,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 55,
    label = "p003958",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {15,S}
2  N u0 p1 c0 {4,S} {6,D}
3  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
6  C u0 p0 c0 {1,S} {2,D} {14,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4651,0.0589936,-0.000198921,5.80714e-07,-5.66297e-10,-25575.5,10.807], Tmin=(10,'K'), Tmax=(377.465,'K')),
            NASAPolynomial(coeffs=[-0.306317,0.0585795,-3.68106e-05,1.09918e-08,-1.25752e-12,-25003.1,29.138], Tmin=(377.465,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-212.671,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (340.893,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 54,
    label = "p004006",
    molecule = 
"""
1 O u0 p2 c0 {6,D}
2 N u0 p1 c0 {5,S} {6,S} {7,S}
3 N u0 p0 c+1 {4,S} {5,D} {8,S}
4 N u0 p2 c-1 {3,S} {6,S}
5 N u0 p1 c0 {2,S} {3,D}
6 C u0 p0 c0 {1,D} {2,S} {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10691,-0.00968671,0.000141912,-2.42133e-07,1.31199e-10,21199.9,9.69375], Tmin=(10,'K'), Tmax=(598.956,'K')),
            NASAPolynomial(coeffs=[1.63057,0.0310738,-2.083e-05,6.52701e-09,-7.71966e-13,21062,16.7443], Tmin=(598.956,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (176.254,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 57,
    label = "p004007",
    molecule = 
"""
1 O u0 p2 c0 {6,D}
2 N u0 p1 c0 {3,S} {6,S} {7,S}
3 N u0 p1 c0 {2,S} {4,S} {8,S}
4 N u0 p1 c0 {3,S} {5,D}
5 N u0 p1 c0 {4,D} {6,S}
6 C u0 p0 c0 {1,D} {2,S} {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08633,-0.00876052,0.000151467,-2.77042e-07,1.60533e-10,24999.5,9.7236], Tmin=(10,'K'), Tmax=(563.232,'K')),
            NASAPolynomial(coeffs=[2.12198,0.0305244,-2.06272e-05,6.51774e-09,-7.77103e-13,24819,14.5055], Tmin=(563.232,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (207.838,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 58,
    label = "p004142",
    molecule = 
"""
1 N u0 p1 c0 {3,S} {4,S} {5,S}
2 N u0 p1 c0 {5,D} {9,S}
3 C u0 p0 c0 {1,S} {4,D} {6,S}
4 C u0 p0 c0 {1,S} {3,D} {7,S}
5 C u0 p0 c0 {1,S} {2,D} {8,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91383,0.00502838,0.000100635,-1.96294e-07,1.14637e-10,58617,9.64666], Tmin=(10,'K'), Tmax=(571.872,'K')),
            NASAPolynomial(coeffs=[2.962,0.031621,-2.14053e-05,6.93266e-09,-8.53688e-13,58399.8,10.8567], Tmin=(571.872,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (487.333,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 59,
    label = "p004295",
    molecule = 
"""
1  O u0 p2 c0 {4,D}
2  N u0 p1 c0 {4,S} {5,S} {7,S}
3  N u0 p1 c0 {4,S} {6,S} {10,S}
4  C u0 p0 c0 {1,D} {2,S} {3,S}
5  C u0 p0 c0 {2,S} {6,D} {8,S}
6  C u0 p0 c0 {3,S} {5,D} {9,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94212,0.00327142,0.000103808,-1.79634e-07,9.58448e-11,-12872.5,8.41273], Tmin=(10,'K'), Tmax=(582.737,'K')),
            NASAPolynomial(coeffs=[0.0763484,0.0423709,-2.91775e-05,9.50459e-09,-1.17035e-12,-12635.3,23.1448], Tmin=(582.737,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-107.054,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 60,
    label = "p004414",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {11,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  C u0 p0 c0 {1,S} {3,D} {10,S}
5  C u0 p0 c0 {3,S} {6,T}
6  C u0 p0 c0 {5,T} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83602,0.0136053,0.000163827,-4.90397e-07,4.52511e-10,7814.11,11.5083], Tmin=(10,'K'), Tmax=(350.288,'K')),
            NASAPolynomial(coeffs=[2.89462,0.041158,-2.61113e-05,8.03227e-09,-9.50738e-13,7776.98,13.5911], Tmin=(350.288,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (64.9926,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 61,
    label = "p004467",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {11,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  C u0 p0 c0 {1,S} {3,D} {5,S}
5  C u0 p0 c0 {4,S} {6,T}
6  C u0 p0 c0 {5,T} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78918,0.0170915,0.000168895,-5.35296e-07,5.01214e-10,7926.15,10.6828], Tmin=(10,'K'), Tmax=(363.96,'K')),
            NASAPolynomial(coeffs=[4.04299,0.0392086,-2.49045e-05,7.7083e-09,-9.18713e-13,7742.71,7.44865], Tmin=(363.96,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (65.9248,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 62,
    label = "p004505",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {11,S}
2  N u0 p1 c0 {6,T}
3  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  C u0 p0 c0 {1,S} {4,D} {10,S}
6  C u0 p0 c0 {2,T} {4,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66996,0.0299912,-3.16416e-06,-1.52793e-08,7.72203e-12,-5068.88,10.4117], Tmin=(10,'K'), Tmax=(896.133,'K')),
            NASAPolynomial(coeffs=[5.23008,0.0306747,-1.7109e-05,4.61763e-09,-4.85401e-13,-5655.56,1.34281], Tmin=(896.133,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-42.1674,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 63,
    label = "p004547",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {13,S}
2  N u0 p1 c0 {3,S} {4,S} {5,S}
3  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
5  C u0 p0 c0 {2,S} {6,D} {11,S}
6  C u0 p0 c0 {1,S} {5,D} {12,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73051,0.0241363,6.93902e-05,-1.9221e-07,1.54862e-10,5164.25,11.1143], Tmin=(10,'K'), Tmax=(321.184,'K')),
            NASAPolynomial(coeffs=[2.07304,0.0447784,-2.70135e-05,7.89148e-09,-8.91937e-13,5270.72,17.2282], Tmin=(321.184,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (42.9277,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 64,
    label = "p004625",
    molecule = 
"""
1 O u0 p2 c0 {5,S} {9,S}
2 N u0 p1 c0 {5,S} {6,S} {7,S}
3 N u0 p1 c0 {4,S} {5,D}
4 N u0 p1 c0 {3,S} {6,D}
5 C u0 p0 c0 {1,S} {2,S} {3,D}
6 C u0 p0 c0 {2,S} {4,D} {8,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08627,-0.00820118,0.000155302,-2.66393e-07,1.4341e-10,2334.39,9.64406], Tmin=(10,'K'), Tmax=(606.544,'K')),
            NASAPolynomial(coeffs=[1.46698,0.0369679,-2.5389e-05,8.03362e-09,-9.5377e-13,2139,16.7411], Tmin=(606.544,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (19.3912,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 65,
    label = "p004630_0",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10262,-0.00690278,5.101e-05,-6.04464e-08,2.36156e-11,5054.04,3.22285], Tmin=(10,'K'), Tmax=(766.154,'K')),
            NASAPolynomial(coeffs=[0.461586,0.0180921,-9.64418e-06,2.52852e-09,-2.60696e-13,5436.28,18.6724], Tmin=(766.154,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (42.044,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 66,
    label = "p004630_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {5,S}
3  C u0 p0 c0 {1,D} {9,S} {10,S}
4  C u0 p0 c0 {2,D} {7,S} {8,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96442,0.00207043,8.73536e-05,-1.46868e-07,7.98099e-11,11657,7.39883], Tmin=(10,'K'), Tmax=(476.493,'K')),
            NASAPolynomial(coeffs=[-0.172729,0.0368331,-2.21823e-05,6.5293e-09,-7.47901e-13,12050.9,24.2874], Tmin=(476.493,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (96.9049,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 67,
    label = "p004643",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {8,S}
2 N u0 p1 c0 {5,T}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {3,D} {6,S} {7,S}
5 C u0 p0 c0 {2,T} {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88273,0.00815436,0.000105928,-2.79617e-07,2.16681e-10,1075.01,9.44408], Tmin=(10,'K'), Tmax=(445.905,'K')),
            NASAPolynomial(coeffs=[4.43085,0.0237291,-1.53979e-05,4.83737e-09,-5.82526e-13,822.405,4.95805], Tmin=(445.905,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (8.92689,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 68,
    label = "p004717",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {6,S}
2 O u0 p2 c0 {5,D}
3 N u0 p1 c0 {1,S} {5,S} {7,S}
4 N u0 p1 c0 {5,S} {6,D}
5 C u0 p0 c0 {2,D} {3,S} {4,S}
6 C u0 p0 c0 {1,S} {4,D} {8,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08042,-0.00779049,0.000138331,-2.43168e-07,1.3531e-10,-10427.9,9.73178], Tmin=(10,'K'), Tmax=(583.22,'K')),
            NASAPolynomial(coeffs=[1.78109,0.0310328,-2.08113e-05,6.51853e-09,-7.71045e-13,-10551.8,16.2237], Tmin=(583.22,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-86.7186,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 69,
    label = "p004719",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {6,S}
2 O u0 p3 c-1 {5,S}
3 N u0 p0 c+1 {5,S} {6,D} {7,S}
4 N u0 p1 c0 {1,S} {5,D}
5 C u0 p0 c0 {2,S} {3,S} {4,D}
6 C u0 p0 c0 {1,S} {3,D} {8,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.11098,-0.0107656,0.000160722,-2.8983e-07,1.65966e-10,-5405.64,9.752], Tmin=(10,'K'), Tmax=(570.433,'K')),
            NASAPolynomial(coeffs=[2.04089,0.0310762,-2.11601e-05,6.71421e-09,-8.02345e-13,-5614.05,14.68], Tmin=(570.433,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-44.964,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 70,
    label = "p004749",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {9,S}
2  N u0 p1 c0 {5,S} {6,S} {7,S}
3  N u0 p1 c0 {5,D} {11,S}
4  N u0 p1 c0 {6,D} {10,S}
5  C u0 p0 c0 {1,S} {2,S} {3,D}
6  C u0 p0 c0 {2,S} {4,D} {8,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85255,0.0124039,0.000146465,-4.60037e-07,4.79632e-10,-13024.5,10.9216], Tmin=(10,'K'), Tmax=(242.729,'K')),
            NASAPolynomial(coeffs=[2.18536,0.0398779,-2.33156e-05,6.27326e-09,-6.44719e-13,-12943.6,16.6044], Tmin=(242.729,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-108.299,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 71,
    label = "p004778",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {12,S}
2  N u0 p1 c0 {3,S} {4,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {2,S} {5,D}
5  C u0 p0 c0 {4,D} {10,S} {11,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83381,0.010622,0.000156501,-3.65874e-07,2.51396e-10,-18062.5,9.59093], Tmin=(10,'K'), Tmax=(503.873,'K')),
            NASAPolynomial(coeffs=[4.87846,0.0366766,-2.33127e-05,7.32217e-09,-8.90901e-13,-18603.8,0.9404], Tmin=(503.873,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-150.224,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 72,
    label = "p004794",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {15,S}
2  N u0 p1 c0 {3,S} {4,S} {5,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {2,S} {6,D}
6  C u0 p0 c0 {5,D} {13,S} {14,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71518,0.0440718,-2.12556e-05,3.73914e-09,1.92182e-14,-17747.8,9.58673], Tmin=(10,'K'), Tmax=(1669.94,'K')),
            NASAPolynomial(coeffs=[21.1952,0.0122056,-1.61781e-06,-5.13346e-10,1.1881e-13,-24980.8,-87.8841], Tmin=(1669.94,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-147.622,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (340.893,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 73,
    label = "p004852",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {12,S}
2  O u0 p2 c0 {6,D}
3  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {1,S} {4,D} {6,S}
6  C u0 p0 c0 {2,D} {5,S} {11,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64706,0.0282324,6.42592e-06,-1.86683e-08,6.4372e-12,-37959.2,10.72], Tmin=(10,'K'), Tmax=(1157.93,'K')),
            NASAPolynomial(coeffs=[3.9264,0.0383156,-2.09481e-05,5.33204e-09,-5.23603e-13,-38764.6,6.13308], Tmin=(1157.93,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-315.655,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 74,
    label = "p005032",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {8,S}
2 O u0 p2 c0 {5,D}
3 N u0 p1 c0 {4,D} {5,S}
4 C u0 p0 c0 {1,S} {3,D} {6,S}
5 C u0 p0 c0 {2,D} {3,S} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8329,0.013903,2.66783e-05,-4.93548e-08,2.27189e-11,-33074.4,10.1698], Tmin=(10,'K'), Tmax=(750.443,'K')),
            NASAPolynomial(coeffs=[3.02057,0.0269852,-1.69647e-05,4.95729e-09,-5.51773e-13,-33198.9,12.2136], Tmin=(750.443,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-275.014,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (174.604,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 75,
    label = "p005102",
    molecule = 
"""
1 O u0 p2 c0 {5,D}
2 N u0 p1 c0 {3,S} {5,S} {7,S}
3 N u0 p1 c0 {2,S} {4,S} {8,S}
4 N u0 p1 c0 {3,S} {6,D}
5 C u0 p0 c0 {1,D} {2,S} {6,S}
6 C u0 p0 c0 {4,D} {5,S} {9,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10625,-0.010297,0.000165783,-2.95888e-07,1.68331e-10,14198.6,9.76357], Tmin=(10,'K'), Tmax=(568.519,'K')),
            NASAPolynomial(coeffs=[1.43938,0.0348626,-2.30121e-05,7.16751e-09,-8.46661e-13,14075.2,17.372], Tmin=(568.519,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (118.035,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 76,
    label = "p005118",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {6,S}
2  O u0 p2 c0 {6,S} {13,S}
3  N u0 p1 c0 {4,S} {6,D}
4  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
6  C u0 p0 c0 {1,S} {2,S} {3,D}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53848,0.0464096,-0.000122743,3.20634e-07,-2.83128e-10,-40970.4,11.0149], Tmin=(10,'K'), Tmax=(426.538,'K')),
            NASAPolynomial(coeffs=[-0.340623,0.0518072,-3.27786e-05,9.74134e-09,-1.10542e-12,-40357.6,29.7277], Tmin=(426.538,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-340.659,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (291.007,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 77,
    label = "p005148",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {5,S} {8,S}
3 N u0 p1 c0 {5,D} {6,S}
4 N u0 p1 c0 {1,S} {6,D}
5 C u0 p0 c0 {1,S} {2,S} {3,D}
6 C u0 p0 c0 {3,S} {4,D} {7,S}
7 H u0 p0 c0 {6,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10924,-0.010865,0.000169698,-3.10681e-07,1.78969e-10,-14461,9.68359], Tmin=(10,'K'), Tmax=(574.532,'K')),
            NASAPolynomial(coeffs=[2.62701,0.0309781,-2.18492e-05,7.08461e-09,-8.5815e-13,-14810.9,11.4852], Tmin=(574.532,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-120.259,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 78,
    label = "p005196",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {10,S}
2  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {8,S} {9,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91532,0.00513114,0.000106228,-2.14837e-07,1.32152e-10,-22138.8,8.11858], Tmin=(10,'K'), Tmax=(537.356,'K')),
            NASAPolynomial(coeffs=[2.87373,0.031565,-1.97063e-05,6.09666e-09,-7.33743e-13,-22296.5,9.98724], Tmin=(537.356,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-184.102,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 79,
    label = "p005308",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {14,S}
2  N u0 p1 c0 {4,S} {6,S} {13,S}
3  N u0 p1 c0 {5,S} {6,D}
4  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {1,S} {2,S} {3,D}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53949,0.039169,-1.04812e-05,-5.85351e-09,2.82972e-12,-21456.1,11.9599], Tmin=(10,'K'), Tmax=(1276.71,'K')),
            NASAPolynomial(coeffs=[8.4109,0.0344058,-1.72204e-05,4.10685e-09,-3.81985e-13,-23555.7,-16.083], Tmin=(1276.71,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-178.453,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (315.95,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 80,
    label = "p005356",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {11,S}
2  O u0 p2 c0 {6,S} {12,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {4,S} {6,D}
6  C u0 p0 c0 {2,S} {5,D} {10,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84702,0.0101717,0.000162506,-3.8237e-07,2.69959e-10,-17787.7,11.2434], Tmin=(10,'K'), Tmax=(474.481,'K')),
            NASAPolynomial(coeffs=[3.24953,0.0429029,-2.85204e-05,9.04297e-09,-1.08841e-12,-18042.7,10.3954], Tmin=(474.481,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-147.924,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 81,
    label = "p005432",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {9,S}
2  O u0 p2 c0 {5,D}
3  N u0 p1 c0 {5,S} {7,S} {8,S}
4  N u0 p1 c0 {6,D} {10,S}
5  C u0 p0 c0 {2,D} {3,S} {6,S}
6  C u0 p0 c0 {1,S} {4,D} {5,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86365,0.00994296,0.000147869,-3.79219e-07,2.95985e-10,-41907,9.78703], Tmin=(10,'K'), Tmax=(417.404,'K')),
            NASAPolynomial(coeffs=[2.70624,0.039861,-2.73019e-05,8.61777e-09,-1.02703e-12,-41974.4,12.395], Tmin=(417.404,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-348.437,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 82,
    label = "p005491",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {10,S}
2  N u0 p1 c0 {3,S} {4,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4  C u0 p0 c0 {2,S} {3,S} {5,D}
5  C u0 p0 c0 {1,S} {4,D} {9,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89957,0.00658032,0.000122061,-2.78486e-07,1.93453e-10,10453.9,9.09847], Tmin=(10,'K'), Tmax=(477.686,'K')),
            NASAPolynomial(coeffs=[3.21634,0.0320351,-1.98367e-05,6.03054e-09,-7.11568e-13,10294,9.53323], Tmin=(477.686,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (86.8978,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 83,
    label = "p005546",
    molecule = 
"""
1  O u0 p2 c0 {4,D}
2  N u0 p1 c0 {3,S} {4,S} {7,S}
3  N u0 p1 c0 {2,S} {5,S} {8,S}
4  C u0 p0 c0 {1,D} {2,S} {6,S}
5  C u0 p0 c0 {3,S} {6,D} {9,S}
6  C u0 p0 c0 {4,S} {5,D} {10,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.13036,-0.0123963,0.000187244,-3.31879e-07,1.88303e-10,2393.39,9.79119], Tmin=(10,'K'), Tmax=(567.709,'K')),
            NASAPolynomial(coeffs=[0.931998,0.0391285,-2.54905e-05,7.8851e-09,-9.27888e-13,2289.38,19.2963], Tmin=(567.709,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (19.8809,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 84,
    label = "p005588",
    molecule = 
"""
1 O u0 p2 c0 {5,S} {8,S}
2 N u0 p1 c0 {4,S} {5,D}
3 N u0 p1 c0 {4,D} {9,S}
4 C u0 p0 c0 {2,S} {3,D} {7,S}
5 C u0 p0 c0 {1,S} {2,D} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94254,0.00372339,0.00010797,-2.24256e-07,1.465e-10,-7163.48,10.2253], Tmin=(10,'K'), Tmax=(470.028,'K')),
            NASAPolynomial(coeffs=[1.49205,0.0346629,-2.29529e-05,7.091e-09,-8.30501e-13,-7044.53,19.0124], Tmin=(470.028,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-59.5727,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 85,
    label = "p005591_0",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99634,0.000168319,4.75233e-06,-5.28777e-09,1.93772e-12,14028.4,-2.98844], Tmin=(10,'K'), Tmax=(693.882,'K')),
            NASAPolynomial(coeffs=[3.54694,0.00275826,-8.44924e-07,8.84639e-11,1.24421e-15,14090.8,-0.984441], Tmin=(693.882,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (116.638,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 86,
    label = "p005763",
    molecule = 
"""
1 O u0 p2 c0 {5,D}
2 N u0 p1 c0 {3,S} {4,S} {5,S}
3 C u0 p0 c0 {2,S} {4,D} {6,S}
4 C u0 p0 c0 {2,S} {3,D} {7,S}
5 C u0 p0 c0 {1,D} {2,S} {8,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90764,0.00573914,9.62134e-05,-2.1046e-07,1.36691e-10,32479.2,9.82126], Tmin=(10,'K'), Tmax=(523.227,'K')),
            NASAPolynomial(coeffs=[3.86584,0.0256532,-1.70506e-05,5.42837e-09,-6.5961e-13,32215.4,7.43276], Tmin=(523.227,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (270.018,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 87,
    label = "p005826",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {7,S}
2 N u0 p1 c0 {4,S} {5,S} {6,S}
3 N u0 p1 c0 {4,D} {8,S}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94959,0.00376692,9.10792e-05,-2.08913e-07,1.5705e-10,-22676.2,8.53103], Tmin=(10,'K'), Tmax=(339.914,'K')),
            NASAPolynomial(coeffs=[1.8449,0.028535,-1.82232e-05,5.46623e-09,-6.267e-13,-22533.2,16.4138], Tmin=(339.914,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-188.542,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (174.604,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 88,
    label = "p005998",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {13,S}
2  N u0 p1 c0 {3,S} {4,S} {5,S}
3  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  C u0 p0 c0 {2,S} {3,S} {6,D}
6  C u0 p0 c0 {1,S} {5,D} {12,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84087,0.0123529,0.00019779,-5.81469e-07,5.2568e-10,9453.01,10.1111], Tmin=(10,'K'), Tmax=(366.362,'K')),
            NASAPolynomial(coeffs=[3.33342,0.0424009,-2.55771e-05,7.58059e-09,-8.76088e-13,9325.72,9.80498], Tmin=(366.362,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (78.6172,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 89,
    label = "p006089",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {13,S}
2  N u0 p1 c0 {3,S} {5,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
5  C u0 p0 c0 {2,S} {3,S} {6,D}
6  C u0 p0 c0 {1,S} {5,D} {12,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8356,0.0128195,0.000196784,-5.82469e-07,5.28756e-10,5381.75,10.2389], Tmin=(10,'K'), Tmax=(365.52,'K')),
            NASAPolynomial(coeffs=[3.37798,0.0424411,-2.57828e-05,7.69562e-09,-8.94012e-13,5250.78,9.73694], Tmin=(365.52,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (44.7675,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 90,
    label = "p006263",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {14,S}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
3  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {2,S} {3,S} {6,D}
6  C u0 p0 c0 {1,S} {5,D} {13,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85725,0.00921034,0.000179683,-3.97852e-07,2.68854e-10,-2878.7,10.6368], Tmin=(10,'K'), Tmax=(487.975,'K')),
            NASAPolynomial(coeffs=[2.45509,0.0492,-3.08373e-05,9.42969e-09,-1.11491e-12,-3081.13,12.9191], Tmin=(487.975,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-23.9686,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 91,
    label = "p006320",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {6,S}
2 O u0 p2 c0 {4,S} {9,S}
3 N u0 p1 c0 {4,D} {5,S}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
5 C u0 p0 c0 {3,S} {6,D} {7,S}
6 C u0 p0 c0 {1,S} {5,D} {8,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.15411,-0.0145665,0.000200127,-3.5905e-07,2.03248e-10,-26710.5,9.73058], Tmin=(10,'K'), Tmax=(585.346,'K')),
            NASAPolynomial(coeffs=[2.46604,0.0350423,-2.45655e-05,7.9791e-09,-9.68942e-13,-27165.2,11.399], Tmin=(585.346,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-222.108,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 92,
    label = "p006396",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {6,S}
2  O u0 p2 c0 {4,S} {7,S}
3  O u0 p2 c0 {6,S} {15,S}
4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {1,S} {3,S} {7,D}
7  C u0 p0 c0 {2,S} {6,D} {14,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70248,0.0305716,0.000309157,-1.57589e-06,2.34863e-09,-53802,11.7158], Tmin=(10,'K'), Tmax=(233.988,'K')),
            NASAPolynomial(coeffs=[4.51832,0.0502145,-3.20964e-05,9.90503e-09,-1.17533e-12,-53932.1,6.99996], Tmin=(233.988,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-447.289,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (336.736,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 93,
    label = "p006798",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {12,S}
2  O u0 p2 c0 {7,D}
3  N u0 p1 c0 {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {4,S} {6,D}
6  C u0 p0 c0 {1,S} {5,D} {10,S}
7  C u0 p0 c0 {2,D} {3,S} {11,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80593,0.0175497,0.000205165,-7.49604e-07,8.38744e-10,-5480.15,11.3802], Tmin=(10,'K'), Tmax=(293.215,'K')),
            NASAPolynomial(coeffs=[3.30283,0.0438686,-2.90045e-05,9.10975e-09,-1.09087e-12,-5534.29,11.764], Tmin=(293.215,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-45.529,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 94,
    label = "p007269",
    molecule = 
"""
1  N u0 p1 c0 {4,S} {5,S} {6,S}
2  N u0 p1 c0 {6,D} {10,S}
3  N u0 p1 c0 {7,T}
4  C u0 p0 c0 {1,S} {5,D} {8,S}
5  C u0 p0 c0 {1,S} {4,D} {9,S}
6  C u0 p0 c0 {1,S} {2,D} {7,S}
7  C u0 p0 c0 {3,T} {6,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81129,0.0125028,0.000153033,-3.89114e-07,2.84008e-10,76163.2,11.8603], Tmin=(10,'K'), Tmax=(482.416,'K')),
            NASAPolynomial(coeffs=[5.57357,0.0335342,-2.31887e-05,7.56972e-09,-9.33021e-13,75578.4,0.34418], Tmin=(482.416,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (633.219,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 95,
    label = "p007773",
    molecule = 
"""
1  O u0 p2 c0 {7,S} {12,S}
2  N u0 p1 c0 {4,S} {7,S} {11,S}
3  N u0 p1 c0 {6,S} {7,D}
4  N u0 p1 c0 {2,S} {6,D}
5  C u0 p0 c0 {6,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {3,S} {4,D} {5,S}
7  C u0 p0 c0 {1,S} {2,S} {3,D}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91233,0.00557554,0.000152006,-3.11236e-07,1.98867e-10,-7077.23,11.2029], Tmin=(10,'K'), Tmax=(487.209,'K')),
            NASAPolynomial(coeffs=[0.550275,0.0494164,-3.29631e-05,1.02735e-08,-1.21034e-12,-6942.36,23.0275], Tmin=(487.209,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-58.8661,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 96,
    label = "p007777",
    molecule = 
"""
1  O u0 p2 c0 {7,S} {12,S}
2  N u0 p1 c0 {6,S} {7,S} {11,S}
3  N u0 p1 c0 {4,S} {6,D}
4  N u0 p1 c0 {3,S} {7,D}
5  C u0 p0 c0 {6,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {2,S} {3,D} {5,S}
7  C u0 p0 c0 {1,S} {2,S} {4,D}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90177,0.00637248,0.000155865,-3.31653e-07,2.19468e-10,-3668.66,11.0459], Tmin=(10,'K'), Tmax=(476.556,'K')),
            NASAPolynomial(coeffs=[1.07965,0.0480164,-3.1731e-05,9.84659e-09,-1.15959e-12,-3603.58,20.4301], Tmin=(476.556,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-30.5245,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 97,
    label = "p007945",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  N u0 p1 c0 {5,S} {7,S} {8,S}
3  N u0 p1 c0 {4,S} {6,D}
4  N u0 p1 c0 {3,S} {7,D}
5  C u0 p0 c0 {1,D} {2,S} {6,S}
6  C u0 p0 c0 {3,D} {5,S} {9,S}
7  C u0 p0 c0 {2,S} {4,D} {10,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94087,0.00338192,0.000109386,-1.91888e-07,1.03994e-10,12268.1,10.164], Tmin=(10,'K'), Tmax=(570.3,'K')),
            NASAPolynomial(coeffs=[-0.0951325,0.0441247,-3.04821e-05,9.8469e-09,-1.19947e-12,12526.3,25.5959], Tmin=(570.3,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (101.976,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 98,
    label = "p008426_1",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {11,S}
2  C u0 p0 c0 {3,S} {4,D} {7,S}
3  C u0 p0 c0 {2,S} {5,D} {6,S}
4  C u0 p0 c0 {1,S} {2,D} {8,S}
5  C u0 p0 c0 {3,D} {9,S} {10,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93029,0.00562132,0.000135256,-3.24402e-07,2.57464e-10,-9475.72,9.3012], Tmin=(10,'K'), Tmax=(321.039,'K')),
            NASAPolynomial(coeffs=[1.18628,0.0398101,-2.44837e-05,7.30799e-09,-8.42928e-13,-9299.53,19.4218], Tmin=(321.039,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-78.7789,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 99,
    label = "p008828",
    molecule = 
"""
1  O u0 p2 c0 {7,D}
2  N u0 p1 c0 {3,S} {5,S} {13,S}
3  N u0 p1 c0 {2,S} {7,S} {12,S}
4  C u0 p0 c0 {5,S} {8,S} {9,S} {10,S}
5  C u0 p0 c0 {2,S} {4,S} {6,D}
6  C u0 p0 c0 {5,D} {7,S} {11,S}
7  C u0 p0 c0 {1,D} {3,S} {6,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9144,0.0053403,0.000153976,-3.05374e-07,1.89912e-10,-3569.97,11.3176], Tmin=(10,'K'), Tmax=(500.057,'K')),
            NASAPolynomial(coeffs=[0.338625,0.0506842,-3.22579e-05,9.85772e-09,-1.15629e-12,-3421.66,23.9977], Tmin=(500.057,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-29.7079,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 100,
    label = "p009289",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {14,S}
2  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {3,S} {5,D}
5  C u0 p0 c0 {1,S} {4,D} {6,S}
6  C u0 p0 c0 {5,S} {7,T}
7  C u0 p0 c0 {6,T} {15,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72698,0.0275308,0.000288229,-1.37207e-06,1.94005e-09,3155.48,11.1256], Tmin=(10,'K'), Tmax=(243.475,'K')),
            NASAPolynomial(coeffs=[4.25583,0.0490313,-3.02187e-05,9.1332e-09,-1.07074e-12,3040.25,7.48377], Tmin=(243.475,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (26.2699,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (345.051,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 101,
    label = "p009379",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {9,S}
2  N u0 p1 c0 {6,T}
3  C u0 p0 c0 {1,S} {4,D} {6,S}
4  C u0 p0 c0 {3,D} {5,S} {8,S}
5  C u0 p0 c0 {4,S} {7,T}
6  C u0 p0 c0 {2,T} {3,S}
7  C u0 p0 c0 {5,T} {10,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73427,0.0197222,0.000167474,-5.40533e-07,4.78768e-10,29634.3,11.1324], Tmin=(10,'K'), Tmax=(412.048,'K')),
            NASAPolynomial(coeffs=[6.93218,0.0299901,-2.0295e-05,6.58643e-09,-8.12793e-13,29020.1,-5.71597], Tmin=(412.048,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (246.395,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 102,
    label = "p009513",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {7,S}
2  O u0 p2 c0 {7,D}
3  N u0 p1 c0 {5,S} {7,S} {11,S}
4  C u0 p0 c0 {5,S} {8,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {4,S} {6,D}
6  C u0 p0 c0 {1,S} {5,D} {12,S}
7  C u0 p0 c0 {1,S} {2,D} {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87221,0.0095011,0.000138178,-3.05118e-07,2.07869e-10,-36800.1,10.6838], Tmin=(10,'K'), Tmax=(464.216,'K')),
            NASAPolynomial(coeffs=[1.56818,0.0452889,-2.89505e-05,8.8418e-09,-1.03376e-12,-36757.9,18.182], Tmin=(464.216,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-305.991,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 103,
    label = "p009772",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {12,S}
2  O u0 p2 c0 {5,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
4  C u0 p0 c0 {5,D} {7,S} {11,S}
5  C u0 p0 c0 {2,S} {4,D} {10,S}
6  C u0 p0 c0 {3,S} {7,T}
7  C u0 p0 c0 {4,S} {6,T}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69302,0.0303832,0.000195373,-9.17719e-07,1.21314e-09,-10367.5,12.0315], Tmin=(10,'K'), Tmax=(265.816,'K')),
            NASAPolynomial(coeffs=[4.47215,0.044396,-2.89355e-05,9.09241e-09,-1.09435e-12,-10499.8,7.5946], Tmin=(265.816,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-86.1644,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 104,
    label = "p009945",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {11,S}
2  O u0 p2 c0 {5,D}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {1,S} {5,S} {6,D}
5  C u0 p0 c0 {2,D} {4,S} {7,S}
6  C u0 p0 c0 {4,D} {9,S} {10,S}
7  C u0 p0 c0 {3,D} {5,S} {8,S}
8  H u0 p0 c0 {7,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75638,0.0282337,3.75684e-05,-8.87626e-08,4.53133e-11,-44724.1,11.9247], Tmin=(10,'K'), Tmax=(742.624,'K')),
            NASAPolynomial(coeffs=[6.62206,0.0355397,-2.31234e-05,6.95798e-09,-7.92472e-13,-45776.8,-5.26991], Tmin=(742.624,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-371.862,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 105,
    label = "p010048_0",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {4,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54088,0.0373295,-3.27655e-05,3.68394e-08,-2.06852e-11,-7437.08,8.71567], Tmin=(10,'K'), Tmax=(634.963,'K')),
            NASAPolynomial(coeffs=[1.6326,0.0412156,-2.27277e-05,6.1226e-09,-6.46816e-13,-7030.75,18.3467], Tmin=(634.963,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-61.8823,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 106,
    label = "p010048_1",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51742,-0.00128731,1.4657e-05,-2.00286e-08,8.91208e-12,-49030,5.35368], Tmin=(10,'K'), Tmax=(674.921,'K')),
            NASAPolynomial(coeffs=[2.70647,0.0050852,-2.9869e-06,8.38117e-10,-9.09403e-14,-48956.2,8.68291], Tmin=(674.921,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-407.656,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (54.0441,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 107,
    label = "p010345",
    molecule = 
"""
1  O u0 p2 c0 {7,S} {14,S}
2  N u0 p1 c0 {4,S} {5,S} {13,S}
3  N u0 p1 c0 {7,D} {15,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
6  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
7  C u0 p0 c0 {1,S} {3,D} {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86713,0.00804737,0.000190333,-3.76696e-07,2.28139e-10,-8673.12,11.5164], Tmin=(10,'K'), Tmax=(532.719,'K')),
            NASAPolynomial(coeffs=[0.450195,0.0620141,-4.13379e-05,1.2984e-08,-1.54939e-12,-8710.77,22.0789], Tmin=(532.719,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-72.1602,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (345.051,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 108,
    label = "p010419",
    molecule = 
"""
1  O u0 p2 c0 {7,D}
2  N u0 p1 c0 {5,S} {7,S} {13,S}
3  N u0 p1 c0 {6,S} {7,S} {12,S}
4  C u0 p0 c0 {5,S} {8,S} {9,S} {10,S}
5  C u0 p0 c0 {2,S} {4,S} {6,D}
6  C u0 p0 c0 {3,S} {5,D} {11,S}
7  C u0 p0 c0 {1,D} {2,S} {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8763,0.00907103,0.000167954,-3.96278e-07,2.93654e-10,-18030.6,10.6775], Tmin=(10,'K'), Tmax=(421.203,'K')),
            NASAPolynomial(coeffs=[1.39064,0.0488014,-3.09602e-05,9.44747e-09,-1.10672e-12,-17964.3,18.8222], Tmin=(421.203,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-149.919,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (303.478,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 109,
    label = "p010564",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {7,S} {13,S}
3  N u0 p1 c0 {7,D} {14,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
6  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
7  C u0 p0 c0 {2,S} {3,D} {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85487,0.00928251,0.000191096,-4.13575e-07,2.73214e-10,-30624.6,11.4914], Tmin=(10,'K'), Tmax=(493.475,'K')),
            NASAPolynomial(coeffs=[1.61208,0.0559147,-3.71375e-05,1.15993e-08,-1.37653e-12,-30749.7,17.2174], Tmin=(493.475,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-254.664,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (320.107,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 110,
    label = "p011399",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {7,S}
2  O u0 p2 c0 {7,S} {10,S}
3  N u0 p1 c0 {6,S} {8,S} {9,S}
4  N u0 p1 c0 {6,S} {7,D}
5  N u0 p1 c0 {1,S} {6,D}
6  C u0 p0 c0 {3,S} {4,S} {5,D}
7  C u0 p0 c0 {1,S} {2,S} {4,D}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86414,0.00827743,0.000135438,-2.91288e-07,1.84123e-10,-17028.5,11.1865], Tmin=(10,'K'), Tmax=(540.689,'K')),
            NASAPolynomial(coeffs=[3.94813,0.0370814,-2.61036e-05,8.54494e-09,-1.05044e-12,-17467.7,6.85549], Tmin=(540.689,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-141.631,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 111,
    label = "p011443",
    molecule = 
"""
1  O u0 p2 c0 {7,D}
2  N u0 p1 c0 {6,S} {7,S} {8,S}
3  N u0 p1 c0 {5,S} {7,S} {9,S}
4  N u0 p1 c0 {6,S} {10,S} {11,S}
5  N u0 p1 c0 {3,S} {6,D}
6  C u0 p0 c0 {2,S} {4,S} {5,D}
7  C u0 p0 c0 {1,D} {2,S} {3,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85954,0.00890907,0.000147401,-3.30894e-07,2.2109e-10,-5241.36,11.1283], Tmin=(10,'K'), Tmax=(507.172,'K')),
            NASAPolynomial(coeffs=[3.70601,0.0387889,-2.5762e-05,8.18029e-09,-9.89393e-13,-5594.5,8.12972], Tmin=(507.172,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-43.6181,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 112,
    label = "p011506",
    molecule = 
"""
1  O u0 p2 c0 {4,D}
2  N u0 p1 c0 {4,S} {5,S} {8,S}
3  N u0 p1 c0 {6,D} {7,S}
4  C u0 p0 c0 {1,D} {2,S} {6,S}
5  C u0 p0 c0 {2,S} {7,D} {9,S}
6  C u0 p0 c0 {3,D} {4,S} {10,S}
7  C u0 p0 c0 {3,S} {5,D} {11,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07209,-0.00749772,0.000179243,-3.16872e-07,1.77511e-10,-1165.4,10.5595], Tmin=(10,'K'), Tmax=(572.918,'K')),
            NASAPolynomial(coeffs=[0.511141,0.0447271,-2.91313e-05,8.9634e-09,-1.04859e-12,-1206.45,21.8363], Tmin=(572.918,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-9.71276,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 113,
    label = "p011937",
    molecule = 
"""
1  O u0 p2 c0 {7,D}
2  N u0 p1 c0 {5,S} {7,S} {10,S}
3  N u0 p1 c0 {6,S} {7,S} {9,S}
4  N u0 p1 c0 {5,S} {11,S} {12,S}
5  C u0 p0 c0 {2,S} {4,S} {6,D}
6  C u0 p0 c0 {3,S} {5,D} {8,S}
7  C u0 p0 c0 {1,D} {2,S} {3,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85694,0.00927896,0.000160381,-3.65786e-07,2.51062e-10,-11389.5,11.5195], Tmin=(10,'K'), Tmax=(488.227,'K')),
            NASAPolynomial(coeffs=[3.26256,0.0422679,-2.73641e-05,8.54373e-09,-1.02191e-12,-11666.6,10.5288], Tmin=(488.227,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-94.7307,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 114,
    label = "r000017",
    molecule = 
"""
1 O u0 p2 c0 {5,S} {9,S}
2 N u0 p1 c0 {4,S} {5,S} {7,S}
3 N u0 p1 c0 {5,D} {6,S}
4 N u0 p1 c0 {2,S} {6,D}
5 C u0 p0 c0 {1,S} {2,S} {3,D}
6 C u0 p0 c0 {3,S} {4,D} {8,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0803,-0.00732929,0.000143859,-2.38332e-07,1.23504e-10,-1052.96,9.63266], Tmin=(10,'K'), Tmax=(629.654,'K')),
            NASAPolynomial(coeffs=[1.2622,0.0371665,-2.54934e-05,8.0517e-09,-9.53182e-13,-1225.24,17.7386], Tmin=(629.654,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-8.76833,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 115,
    label = "r000049",
    molecule = 
"""
1  O u0 p2 c0 {6,D}
2  N u0 p1 c0 {5,S} {6,S} {10,S}
3  N u0 p1 c0 {4,S} {5,D}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {2,S} {3,D} {11,S}
6  C u0 p0 c0 {1,D} {2,S} {12,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47881,0.0456237,-8.90262e-05,1.56198e-07,-1.02388e-10,-14356.3,10.8945], Tmin=(10,'K'), Tmax=(540.815,'K')),
            NASAPolynomial(coeffs=[0.985387,0.0433803,-2.54308e-05,7.07886e-09,-7.61831e-13,-13784.1,24.188], Tmin=(540.815,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-119.389,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 116,
    label = "r000208",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {5,D}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
5 C u0 p0 c0 {2,D} {3,S} {9,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94423,0.00319184,9.27872e-05,-1.65378e-07,9.06193e-11,-21428.1,9.16342], Tmin=(10,'K'), Tmax=(574.793,'K')),
            NASAPolynomial(coeffs=[1.03557,0.0357635,-2.43904e-05,7.84959e-09,-9.56338e-13,-21297.4,19.8136], Tmin=(574.793,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-178.188,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 117,
    label = "r000314",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {6,S}
2 O u0 p2 c0 {4,S} {9,S}
3 N u0 p1 c0 {1,S} {4,D}
4 C u0 p0 c0 {2,S} {3,D} {5,S}
5 C u0 p0 c0 {4,S} {6,D} {7,S}
6 C u0 p0 c0 {1,S} {5,D} {8,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.14314,-0.012772,0.000180682,-3.07049e-07,1.63711e-10,-13839.9,9.74514], Tmin=(10,'K'), Tmax=(620.774,'K')),
            NASAPolynomial(coeffs=[2.06582,0.0366733,-2.59275e-05,8.40936e-09,-1.01588e-12,-14276.8,13.1803], Tmin=(620.774,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-115.088,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 118,
    label = "r000399",
    molecule = 
"""
1 O u0 p2 c0 {5,S} {9,S}
2 N u0 p1 c0 {3,S} {6,S} {7,S}
3 N u0 p1 c0 {2,S} {5,D}
4 N u0 p1 c0 {5,S} {6,D}
5 C u0 p0 c0 {1,S} {3,D} {4,S}
6 C u0 p0 c0 {2,S} {4,D} {8,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94235,0.00320109,9.25409e-05,-1.59438e-07,8.37365e-11,-701.018,9.51065], Tmin=(10,'K'), Tmax=(601.582,'K')),
            NASAPolynomial(coeffs=[0.616382,0.0382592,-2.71471e-05,8.96348e-09,-1.10926e-12,-535.058,21.9197], Tmin=(601.582,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-5.85576,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 119,
    label = "r000634",
    molecule = 
"""
1  O u0 p2 c0 {4,D}
2  N u0 p1 c0 {3,S} {4,S} {9,S}
3  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {1,D} {2,S} {10,S}
5  C u0 p0 c0 {3,S} {6,T}
6  C u0 p0 c0 {5,T} {11,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59855,0.0352029,-1.93983e-05,3.86983e-09,1.14201e-13,6050.43,11.5181], Tmin=(10,'K'), Tmax=(1243.33,'K')),
            NASAPolynomial(coeffs=[8.07321,0.0251851,-1.25941e-05,3.05354e-09,-2.91113e-13,4599.35,-12.4049], Tmin=(1243.33,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (50.2695,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 120,
    label = "r000721",
    molecule = 
"""
1  O u0 p2 c0 {4,D}
2  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,D} {2,S} {3,S}
5  C u0 p0 c0 {2,S} {6,T}
6  C u0 p0 c0 {5,T} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85612,0.0157803,0.000219581,-1.10874e-06,1.91889e-09,2570.55,11.7834], Tmin=(10,'K'), Tmax=(145.276,'K')),
            NASAPolynomial(coeffs=[3.00091,0.0393263,-2.35264e-05,6.82078e-09,-7.65685e-13,2595.4,14.2595], Tmin=(145.276,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (21.6655,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 121,
    label = "r000744",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  N u0 p1 c0 {6,T}
3  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {1,D} {3,S} {11,S}
6  C u0 p0 c0 {2,T} {4,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78574,0.0181084,0.000196515,-7.51293e-07,8.25469e-10,-7574.76,10.3769], Tmin=(10,'K'), Tmax=(324.042,'K')),
            NASAPolynomial(coeffs=[5.36242,0.0316194,-1.86637e-05,5.43169e-09,-6.20499e-13,-7850.06,1.87582], Tmin=(324.042,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-62.9455,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 122,
    label = "r000813",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {6,S}
2  O u0 p2 c0 {6,D}
3  N u0 p1 c0 {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
5  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {1,S} {2,D} {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5098,0.0507652,-0.000136283,3.50844e-07,-3.17409e-10,-55957.2,10.992], Tmin=(10,'K'), Tmax=(402.453,'K')),
            NASAPolynomial(coeffs=[0.871363,0.0498127,-3.14431e-05,9.38988e-09,-1.0734e-12,-55524.7,24.0538], Tmin=(402.453,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-465.269,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (291.007,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 123,
    label = "r000842",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {12,S}
2  N u0 p1 c0 {1,S} {5,D}
3  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {2,D} {3,S} {4,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78182,0.0200174,3.34314e-05,-5.56058e-08,2.29537e-11,-9877.45,10.0198], Tmin=(10,'K'), Tmax=(836.558,'K')),
            NASAPolynomial(coeffs=[2.29376,0.0391789,-2.25263e-05,6.20113e-09,-6.61012e-13,-10050,14.4139], Tmin=(836.558,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-82.1344,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 124,
    label = "r001050",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {6,D}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
5  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {2,D} {4,S} {12,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84107,0.013959,0.000130878,-3.70016e-07,3.38511e-10,-26355.7,10.1926], Tmin=(10,'K'), Tmax=(278.507,'K')),
            NASAPolynomial(coeffs=[1.79877,0.0432912,-2.71012e-05,8.14237e-09,-9.40573e-13,-26241.9,17.4348], Tmin=(278.507,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-219.124,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 125,
    label = "r001085",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  O u0 p2 c0 {6,D}
3  N u0 p1 c0 {5,S} {6,S} {7,S}
4  N u0 p1 c0 {5,S} {9,S} {10,S}
5  C u0 p0 c0 {1,D} {3,S} {4,S}
6  C u0 p0 c0 {2,D} {3,S} {8,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88928,0.0103767,0.000212721,-8.26685e-07,1.02496e-09,-48518.4,9.69993], Tmin=(10,'K'), Tmax=(257.92,'K')),
            NASAPolynomial(coeffs=[3.20526,0.0359325,-2.28358e-05,6.87388e-09,-7.95667e-13,-48532.8,11.1092], Tmin=(257.92,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-403.385,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 126,
    label = "r001147",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {1,D} {2,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60074,0.0337286,-2.19956e-05,2.75355e-08,-1.93979e-11,-27959.2,10.4819], Tmin=(10,'K'), Tmax=(588.792,'K')),
            NASAPolynomial(coeffs=[1.15713,0.0423606,-2.36849e-05,6.4617e-09,-6.89966e-13,-27533.3,22.1496], Tmin=(588.792,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-232.498,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 127,
    label = "r001169",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 O u0 p2 c0 {5,D}
3 N u0 p1 c0 {4,S} {7,S} {8,S}
4 C u0 p0 c0 {1,D} {3,S} {5,S}
5 C u0 p0 c0 {2,D} {4,S} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87785,0.00985029,0.000111657,-3.3666e-07,3.06237e-10,-38050.8,8.61326], Tmin=(10,'K'), Tmax=(362.75,'K')),
            NASAPolynomial(coeffs=[3.46831,0.0278891,-1.88532e-05,5.9594e-09,-7.14121e-13,-38110.1,8.94744], Tmin=(362.75,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-316.358,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (174.604,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 128,
    label = "r001235",
    molecule = 
"""
1 N u0 p1 c0 {4,S} {5,S} {6,S}
2 N u0 p1 c0 {3,S} {4,D}
3 N u0 p1 c0 {2,S} {5,D}
4 C u0 p0 c0 {1,S} {2,D} {7,S}
5 C u0 p0 c0 {1,S} {3,D} {8,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.19196,-0.0148682,0.000135852,-2.02053e-07,9.6988e-11,24989.6,7.94616], Tmin=(10,'K'), Tmax=(665.052,'K')),
            NASAPolynomial(coeffs=[0.275355,0.0315389,-2.03558e-05,6.1976e-09,-7.16272e-13,25005.3,21.4448], Tmin=(665.052,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (207.791,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 129,
    label = "r001357",
    molecule = 
"""
1  O u0 p2 c0 {6,D}
2  N u0 p1 c0 {3,S} {6,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {1,D} {2,S} {15,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58775,0.0400818,-6.12051e-06,-1.25044e-08,5.53931e-12,-32566.3,11.6241], Tmin=(10,'K'), Tmax=(1098.01,'K')),
            NASAPolynomial(coeffs=[6.6601,0.0396724,-2.02921e-05,5.04393e-09,-4.9254e-13,-33891,-6.4455], Tmin=(1098.01,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-270.789,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (340.893,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 130,
    label = "r001387",
    molecule = 
"""
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
5  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
6  C u0 p0 c0 {1,D} {2,S} {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82859,0.0233408,4.35094e-05,-7.01401e-08,2.84301e-11,-16385.6,10.4118], Tmin=(10,'K'), Tmax=(867.519,'K')),
            NASAPolynomial(coeffs=[3.13547,0.0447625,-2.50439e-05,6.75895e-09,-7.09429e-13,-16951.2,9.70437], Tmin=(867.519,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-136.208,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 131,
    label = "r001614",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  O u0 p2 c0 {6,D}
3  N u0 p1 c0 {5,S} {10,S} {11,S}
4  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {1,D} {3,S} {4,S}
6  C u0 p0 c0 {2,D} {4,S} {9,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83725,0.0185434,0.000284942,-1.72662e-06,3.15396e-09,-42834.7,10.6846], Tmin=(10,'K'), Tmax=(189.643,'K')),
            NASAPolynomial(coeffs=[4.26207,0.033339,-1.9985e-05,5.84995e-09,-6.66287e-13,-42893.6,8.21508], Tmin=(189.643,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-355.887,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 132,
    label = "r001627",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {6,D}
3  N u0 p1 c0 {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
6  C u0 p0 c0 {2,D} {3,S} {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89194,0.00625897,0.000132368,-2.53588e-07,1.45691e-10,-31147.5,10.5218], Tmin=(10,'K'), Tmax=(576.506,'K')),
            NASAPolynomial(coeffs=[2.08868,0.0437911,-3.03865e-05,9.90193e-09,-1.2163e-12,-31355.4,14.6222], Tmin=(576.506,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-259.021,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 133,
    label = "r001958",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {5,D}
3 N u0 p1 c0 {4,D} {8,S}
4 C u0 p0 c0 {1,S} {3,D} {6,S}
5 C u0 p0 c0 {1,S} {2,D} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93348,0.00416331,9.65262e-05,-1.99086e-07,1.25771e-10,-32358.3,9.91543], Tmin=(10,'K'), Tmax=(506.733,'K')),
            NASAPolynomial(coeffs=[2.18116,0.031008,-2.14561e-05,6.80901e-09,-8.1008e-13,-32347.7,15.5298], Tmin=(506.733,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-269.062,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (174.604,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 134,
    label = "r002203",
    molecule = 
"""
1  O u0 p2 c0 {6,D}
2  N u0 p1 c0 {3,S} {4,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
5  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {1,D} {3,S} {5,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95032,0.0034355,0.000165845,-3.51422e-07,2.44892e-10,-7842.34,11.5867], Tmin=(10,'K'), Tmax=(367.423,'K')),
            NASAPolynomial(coeffs=[-0.529974,0.0522225,-3.33749e-05,1.01361e-08,-1.17586e-12,-7513.18,28.7146], Tmin=(367.423,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-65.2048,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 135,
    label = "r002312",
    molecule = 
"""
1  O u0 p2 c0 {6,D}
2  N u0 p1 c0 {3,S} {6,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
6  C u0 p0 c0 {1,D} {2,S} {13,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89481,0.00900335,0.000172137,-4.50122e-07,3.89162e-10,-11694.6,10.6737], Tmin=(10,'K'), Tmax=(294.319,'K')),
            NASAPolynomial(coeffs=[0.966709,0.0487989,-3.06844e-05,9.29936e-09,-1.08469e-12,-11522.2,21.2187], Tmin=(294.319,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-97.218,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 136,
    label = "r002395",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {6,S}
2  O u0 p2 c0 {6,D}
3  N u0 p1 c0 {4,S} {5,D}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {3,D} {10,S}
6  C u0 p0 c0 {1,S} {2,D} {11,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59526,0.0448418,-0.000148775,4.35247e-07,-4.38817e-10,-32733.3,10.9855], Tmin=(10,'K'), Tmax=(358.079,'K')),
            NASAPolynomial(coeffs=[1.60378,0.0414234,-2.69453e-05,8.26649e-09,-9.66008e-13,-32426.2,20.8454], Tmin=(358.079,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-272.176,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 137,
    label = "r002513",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {6,S} {7,S}
3 N u0 p1 c0 {1,S} {6,D}
4 N u0 p1 c0 {5,D} {6,S}
5 N u0 p1 c0 {1,S} {4,D}
6 C u0 p0 c0 {2,S} {3,D} {4,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94217,0.00316915,7.51695e-05,-1.32801e-07,6.98018e-11,9290.77,9.79178], Tmin=(10,'K'), Tmax=(624.801,'K')),
            NASAPolynomial(coeffs=[2.05328,0.0294963,-2.2209e-05,7.56521e-09,-9.52665e-13,9248.97,15.7928], Tmin=(624.801,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (77.2205,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 138,
    label = "r002594",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {5,D}
3  N u0 p1 c0 {5,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {1,S} {2,D} {3,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55649,0.0447116,-0.000156842,3.70957e-07,-2.9886e-10,-51633.3,10.1328], Tmin=(10,'K'), Tmax=(440.297,'K')),
            NASAPolynomial(coeffs=[1.0653,0.0362349,-2.19834e-05,6.2943e-09,-6.92228e-13,-51112.4,23.5321], Tmin=(440.297,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-429.312,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 139,
    label = "r002675",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
5  C u0 p0 c0 {1,D} {2,S} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98716,0.00059573,0.00011649,-2.03868e-07,1.16084e-10,-9520.51,9.61522], Tmin=(10,'K'), Tmax=(453.162,'K')),
            NASAPolynomial(coeffs=[-0.950031,0.0441715,-2.77354e-05,8.28798e-09,-9.47028e-13,-9073,29.527], Tmin=(453.162,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-79.1653,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (253.591,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 140,
    label = "r002689",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  N u0 p1 c0 {6,T}
3  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
5  C u0 p0 c0 {1,D} {3,S} {6,S}
6  C u0 p0 c0 {2,T} {5,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.39264,0.0507281,-0.000100584,1.38285e-07,-7.38699e-11,-6543.14,10.6187], Tmin=(10,'K'), Tmax=(594.114,'K')),
            NASAPolynomial(coeffs=[3.93055,0.0326331,-1.83561e-05,5.01055e-09,-5.3429e-13,-6351.62,10.4535], Tmin=(594.114,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-54.4522,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 141,
    label = "r002760",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 O u0 p2 c0 {5,D}
3 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
4 C u0 p0 c0 {1,D} {3,S} {5,S}
5 C u0 p0 c0 {2,D} {4,S} {9,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69446,0.0349524,-0.000138541,4.32315e-07,-4.46542e-10,-34925.8,9.64959], Tmin=(10,'K'), Tmax=(353.752,'K')),
            NASAPolynomial(coeffs=[1.59971,0.0329829,-2.14034e-05,6.5481e-09,-7.62926e-13,-34617.1,19.8477], Tmin=(353.752,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-290.406,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 142,
    label = "r002774",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {5,S}
2 N u0 p1 c0 {3,S} {4,D}
3 N u0 p1 c0 {2,S} {5,D}
4 C u0 p0 c0 {1,S} {2,D} {6,S}
5 C u0 p0 c0 {1,S} {3,D} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.18172,-0.0135629,0.000115447,-1.65195e-07,7.60845e-11,6657.02,7.92825], Tmin=(10,'K'), Tmax=(694.888,'K')),
            NASAPolynomial(coeffs=[0.550055,0.0278615,-1.8266e-05,5.58302e-09,-6.44511e-13,6666.33,20.5623], Tmin=(694.888,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (55.3711,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 143,
    label = "r002801",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {6,D}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
4  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
5  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {2,D} {3,S} {5,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81324,0.0238081,2.59734e-05,-4.8698e-08,2.02206e-11,-28175,10.6668], Tmin=(10,'K'), Tmax=(883.013,'K')),
            NASAPolynomial(coeffs=[4.43505,0.0360151,-2.02844e-05,5.49467e-09,-5.77845e-13,-28870.5,4.42775], Tmin=(883.013,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-234.238,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 144,
    label = "r002874",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
3 C u0 p0 c0 {1,D} {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,T}
5 C u0 p0 c0 {4,T} {9,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88407,0.0120773,0.00012427,-5.57224e-07,8.4074e-10,7322.67,9.36884], Tmin=(10,'K'), Tmax=(167.007,'K')),
            NASAPolynomial(coeffs=[3.22964,0.0277516,-1.65136e-05,4.76504e-09,-5.32777e-13,7344.53,11.3548], Tmin=(167.007,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (60.9552,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 145,
    label = "r002881",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  O u0 p2 c0 {6,D}
3  C u0 p0 c0 {5,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {1,D} {3,S} {6,S}
6  C u0 p0 c0 {2,D} {4,S} {5,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.473,0.0575986,-0.000215741,5.62256e-07,-5.08033e-10,-42054.3,10.3215], Tmin=(10,'K'), Tmax=(384.753,'K')),
            NASAPolynomial(coeffs=[1.71872,0.0423904,-2.60572e-05,7.65275e-09,-8.6446e-13,-41671.8,20.3264], Tmin=(384.753,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-349.68,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 146,
    label = "r003070",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  N u0 p1 c0 {5,S} {9,S} {10,S}
3  N u0 p1 c0 {6,T}
4  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {1,D} {2,S} {4,S}
6  C u0 p0 c0 {3,T} {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84074,0.0107791,0.000142598,-3.63598e-07,2.71162e-10,-12665.7,11.0067], Tmin=(10,'K'), Tmax=(464.531,'K')),
            NASAPolynomial(coeffs=[4.70602,0.0324552,-2.14478e-05,6.80898e-09,-8.25114e-13,-13060.3,4.1131], Tmin=(464.531,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-105.332,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 147,
    label = "r003183",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 N u0 p1 c0 {3,S} {6,S} {7,S}
3 C u0 p0 c0 {1,D} {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,T}
5 C u0 p0 c0 {4,T} {8,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84781,0.0102147,0.000114565,-3.08304e-07,2.3458e-10,5414.55,8.43127], Tmin=(10,'K'), Tmax=(472.718,'K')),
            NASAPolynomial(coeffs=[6.0474,0.0210911,-1.3519e-05,4.29341e-09,-5.29079e-13,4877.11,-4.01742], Tmin=(472.718,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (44.9935,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 148,
    label = "r003195",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {10,S}
2  O u0 p2 c0 {5,D}
3  O u0 p2 c0 {6,D}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {2,D} {4,S} {8,S}
6  C u0 p0 c0 {3,D} {4,S} {9,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74977,0.0247196,2.20066e-05,-4.77242e-08,2.04272e-11,-53024.4,10.2329], Tmin=(10,'K'), Tmax=(895.361,'K')),
            NASAPolynomial(coeffs=[5.7407,0.0331994,-2.13069e-05,6.19885e-09,-6.80393e-13,-54077.3,-3.0412], Tmin=(895.361,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-440.867,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 149,
    label = "r003323",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {5,T}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,D} {3,S} {8,S}
5 C u0 p0 c0 {2,T} {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82658,0.0160054,2.92058e-05,-9.68375e-08,8.66392e-11,-2633.01,9.89265], Tmin=(10,'K'), Tmax=(290.304,'K')),
            NASAPolynomial(coeffs=[3.20775,0.0245321,-1.48516e-05,4.33775e-09,-4.89482e-13,-2597.08,12.1128], Tmin=(290.304,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-21.8957,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 150,
    label = "r003344",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  N u0 p1 c0 {4,S} {5,S} {9,S}
3  N u0 p1 c0 {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {1,D} {2,S} {3,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63726,0.0344771,-4.61877e-05,8.11645e-08,-6.12713e-11,-29710.5,10.3702], Tmin=(10,'K'), Tmax=(472.283,'K')),
            NASAPolynomial(coeffs=[2.51988,0.0351889,-2.06523e-05,5.88224e-09,-6.51344e-13,-29507.3,15.956], Tmin=(472.283,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-247.04,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 151,
    label = "r003348",
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
            NASAPolynomial(coeffs=[3.9738,0.00137426,3.91207e-05,-5.62547e-08,2.61134e-11,-21449.8,7.33205], Tmin=(10,'K'), Tmax=(556.409,'K')),
            NASAPolynomial(coeffs=[1.45062,0.0195144,-9.78575e-06,2.34672e-09,-2.18451e-13,-21169.1,18.0256], Tmin=(556.409,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-178.358,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 152,
    label = "r003431",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  O u0 p2 c0 {6,D}
3  N u0 p1 c0 {5,S} {6,S} {10,S}
4  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {1,D} {3,S} {4,S}
6  C u0 p0 c0 {2,D} {3,S} {11,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60031,0.0374981,-6.70704e-05,1.41011e-07,-1.11264e-10,-46539.6,10.9125], Tmin=(10,'K'), Tmax=(470.791,'K')),
            NASAPolynomial(coeffs=[1.27367,0.0407993,-2.51236e-05,7.31808e-09,-8.18792e-13,-46138,22.3225], Tmin=(470.791,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-386.964,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 153,
    label = "r003437",
    molecule = 
"""
1  O u0 p2 c0 {6,D}
2  N u0 p1 c0 {6,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
6  C u0 p0 c0 {1,D} {2,S} {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86464,0.00813316,0.000159056,-3.22649e-07,1.96944e-10,-18461.2,10.6957], Tmin=(10,'K'), Tmax=(546.587,'K')),
            NASAPolynomial(coeffs=[2.6327,0.0472492,-3.08953e-05,9.78597e-09,-1.18889e-12,-18776.1,11.7818], Tmin=(546.587,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-153.545,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 154,
    label = "r003454",
    molecule = 
"""
1  O u0 p2 c0 {6,D}
2  N u0 p1 c0 {4,S} {5,S} {6,S}
3  N u0 p1 c0 {6,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
5  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
6  C u0 p0 c0 {1,D} {2,S} {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81214,0.019999,4.45235e-05,-7.70682e-08,3.44587e-11,-9708.75,10.6531], Tmin=(10,'K'), Tmax=(771.048,'K')),
            NASAPolynomial(coeffs=[2.75441,0.0402387,-2.35502e-05,6.60407e-09,-7.16305e-13,-9984.16,12.6374], Tmin=(771.048,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-80.7251,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 155,
    label = "r003718",
    molecule = 
"""
1  O u0 p2 c0 {4,D}
2  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {5,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,D} {2,S} {6,S}
5  C u0 p0 c0 {3,S} {6,T}
6  C u0 p0 c0 {4,S} {5,T}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47135,0.0533914,-0.000144443,3.05137e-07,-2.36598e-10,1183.86,10.884], Tmin=(10,'K'), Tmax=(436.519,'K')),
            NASAPolynomial(coeffs=[2.61691,0.0396432,-2.30532e-05,6.50584e-09,-7.14081e-13,1464.04,16.6527], Tmin=(436.519,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (9.8301,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 156,
    label = "r003937",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  N u0 p1 c0 {4,S} {5,S} {9,S}
3  N u0 p1 c0 {6,T}
4  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {1,D} {2,S} {10,S}
6  C u0 p0 c0 {3,T} {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70695,0.0294465,-1.20901e-05,-1.21261e-09,1.48383e-12,-5883.48,11.6657], Tmin=(10,'K'), Tmax=(1193.54,'K')),
            NASAPolynomial(coeffs=[7.57607,0.0226921,-1.1409e-05,2.76799e-09,-2.63426e-13,-7249.56,-9.53882], Tmin=(1193.54,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-48.9316,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 157,
    label = "r003958",
    molecule = 
"""
1  O u0 p2 c0 {6,D}
2  N u0 p1 c0 {4,S} {6,S} {14,S}
3  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
6  C u0 p0 c0 {1,D} {2,S} {15,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47497,0.0545043,-0.000138611,3.36993e-07,-2.87593e-10,-31232.3,13.0289], Tmin=(10,'K'), Tmax=(425.326,'K')),
            NASAPolynomial(coeffs=[0.591341,0.0527895,-3.08737e-05,8.73228e-09,-9.59117e-13,-30726.2,27.5414], Tmin=(425.326,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-259.694,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (340.893,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 158,
    label = "r004006",
    molecule = 
"""
1 O u0 p2 c0 {6,S} {8,S}
2 N u0 p1 c0 {3,S} {5,S} {7,S}
3 N u0 p1 c0 {2,S} {6,D}
4 N u0 p1 c0 {5,D} {6,S}
5 N u0 p1 c0 {2,S} {4,D}
6 C u0 p0 c0 {1,S} {3,D} {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93535,0.00361396,8.57411e-05,-1.54366e-07,8.34006e-11,17018.1,9.28743], Tmin=(10,'K'), Tmax=(605.304,'K')),
            NASAPolynomial(coeffs=[1.96967,0.0320645,-2.30753e-05,7.6792e-09,-9.54767e-13,16972.8,15.4443], Tmin=(605.304,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (141.467,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 159,
    label = "r004142",
    molecule = 
"""
1 N u0 p1 c0 {3,S} {5,S} {6,S}
2 N u0 p1 c0 {4,S} {5,D}
3 C u0 p0 c0 {1,S} {4,D} {7,S}
4 C u0 p0 c0 {2,S} {3,D} {8,S}
5 C u0 p0 c0 {1,S} {2,D} {9,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.21464,-0.0168371,0.000155578,-2.33813e-07,1.13789e-10,14473.2,8.67808], Tmin=(10,'K'), Tmax=(653.143,'K')),
            NASAPolynomial(coeffs=[-0.29332,0.0357942,-2.27634e-05,6.87882e-09,-7.92183e-13,14528.3,24.4202], Tmin=(653.143,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (120.351,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 160,
    label = "r004202",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 N u0 p1 c0 {4,D} {5,S}
3 N u0 p1 c0 {1,S} {5,D}
4 C u0 p0 c0 {1,S} {2,D} {6,S}
5 C u0 p0 c0 {2,S} {3,D} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.18044,-0.0133193,0.000112507,-1.58902e-07,7.22187e-11,9260.36,8.62329], Tmin=(10,'K'), Tmax=(703.315,'K')),
            NASAPolynomial(coeffs=[0.444821,0.0279624,-1.82683e-05,5.56364e-09,-6.40182e-13,9290.28,21.8079], Tmin=(703.315,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (77.0185,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 161,
    label = "r004295",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {10,S}
2  N u0 p1 c0 {4,S} {5,S} {8,S}
3  N u0 p1 c0 {4,D} {6,S}
4  C u0 p0 c0 {1,S} {2,S} {3,D}
5  C u0 p0 c0 {2,S} {6,D} {7,S}
6  C u0 p0 c0 {3,S} {5,D} {9,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10371,-0.00995022,0.000179042,-3.1189e-07,1.71401e-10,-8788.3,9.67848], Tmin=(10,'K'), Tmax=(592.645,'K')),
            NASAPolynomial(coeffs=[1.1941,0.0406697,-2.7494e-05,8.65291e-09,-1.02607e-12,-8987.51,17.6032], Tmin=(592.645,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-73.0911,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 162,
    label = "r004414",
    molecule = 
"""
1  O u0 p2 c0 {4,D}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,D} {2,S} {11,S}
5  C u0 p0 c0 {2,S} {6,T}
6  C u0 p0 c0 {5,T} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91508,0.0112862,0.000457476,-3.21785e-06,7.51634e-09,5274.03,8.95723], Tmin=(10,'K'), Tmax=(136.224,'K')),
            NASAPolynomial(coeffs=[3.52911,0.0387889,-2.34075e-05,6.86935e-09,-7.81649e-13,5269.55,9.49926], Tmin=(136.224,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (46.4775,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 163,
    label = "r004467",
    molecule = 
"""
1  O u0 p2 c0 {4,D}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,D} {2,S} {5,S}
5  C u0 p0 c0 {4,S} {6,T}
6  C u0 p0 c0 {5,T} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40686,0.048024,-6.72642e-05,7.40868e-08,-3.50097e-11,4113.55,10.6937], Tmin=(10,'K'), Tmax=(640.639,'K')),
            NASAPolynomial(coeffs=[4.02415,0.0360872,-2.03903e-05,5.6148e-09,-6.04314e-13,4200.32,9.28502], Tmin=(640.639,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (34.1374,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 164,
    label = "r004505",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  N u0 p1 c0 {6,T}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
5  C u0 p0 c0 {1,D} {3,S} {11,S}
6  C u0 p0 c0 {2,T} {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54716,0.0405001,-5.15858e-05,6.22935e-08,-3.54552e-11,-6622.96,10.5931], Tmin=(10,'K'), Tmax=(523.891,'K')),
            NASAPolynomial(coeffs=[3.81099,0.0339832,-2.00346e-05,5.73859e-09,-6.38722e-13,-6588.82,10.0805], Tmin=(523.891,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-55.0947,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 165,
    label = "r004547",
    molecule = 
"""
1  O u0 p2 c0 {6,D}
2  N u0 p1 c0 {3,S} {4,S} {5,S}
3  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
5  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
6  C u0 p0 c0 {1,D} {5,S} {13,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95837,0.0223625,3.26208e-05,-5.00299e-08,1.82748e-11,654.574,10.4751], Tmin=(10,'K'), Tmax=(1005.87,'K')),
            NASAPolynomial(coeffs=[5.68131,0.036315,-1.92095e-05,4.88371e-09,-4.83862e-13,-744.487,-3.07867], Tmin=(1005.87,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (5.52696,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 166,
    label = "r004630",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {6,D} {15,S}
6  C u0 p0 c0 {4,S} {5,D} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.09508,-0.00781826,0.000187838,-2.83686e-07,1.3799e-10,-2520.35,9.35346], Tmin=(10,'K'), Tmax=(619.535,'K')),
            NASAPolynomial(coeffs=[-4.55262,0.0671742,-4.0118e-05,1.15287e-08,-1.27985e-12,-1816.52,43.9658], Tmin=(619.535,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-20.9589,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (382.466,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 167,
    label = "r004643",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {5,T}
3 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
4 C u0 p0 c0 {1,D} {3,S} {5,S}
5 C u0 p0 c0 {2,T} {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72633,0.0225271,-1.25847e-05,3.22993e-09,-2.80997e-13,-3217.6,9.56394], Tmin=(10,'K'), Tmax=(1573.86,'K')),
            NASAPolynomial(coeffs=[8.36858,0.0129527,-5.57914e-06,1.1603e-09,-9.4861e-14,-4954.29,-15.8127], Tmin=(1573.86,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-26.7934,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 168,
    label = "r004717",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {6,S}
2 O u0 p2 c0 {5,S} {8,S}
3 N u0 p1 c0 {5,S} {6,D}
4 N u0 p1 c0 {1,S} {5,D}
5 C u0 p0 c0 {2,S} {3,S} {4,D}
6 C u0 p0 c0 {1,S} {3,D} {7,S}
7 H u0 p0 c0 {6,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05867,-0.00575043,0.000127057,-2.17279e-07,1.15784e-10,-13240,10.1523], Tmin=(10,'K'), Tmax=(616.588,'K')),
            NASAPolynomial(coeffs=[2.07328,0.0312434,-2.16031e-05,6.88285e-09,-8.20981e-13,-13453.5,15.0535], Tmin=(616.588,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-110.1,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 169,
    label = "r004749",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  N u0 p1 c0 {5,S} {6,S} {7,S}
3  N u0 p1 c0 {5,S} {9,S} {10,S}
4  N u0 p1 c0 {6,D} {11,S}
5  C u0 p0 c0 {1,D} {2,S} {3,S}
6  C u0 p0 c0 {2,S} {4,D} {8,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87779,0.0117495,0.000176459,-6.10491e-07,7.05557e-10,-21489.2,9.96896], Tmin=(10,'K'), Tmax=(218.929,'K')),
            NASAPolynomial(coeffs=[2.25484,0.0414026,-2.67143e-05,8.20996e-09,-9.66753e-13,-21418.2,15.3334], Tmin=(218.929,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-178.644,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 170,
    label = "r004778",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  N u0 p1 c0 {3,S} {5,S} {12,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {1,D} {2,S} {4,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75728,0.0207672,2.84138e-05,-5.1798e-08,2.31406e-11,-30315.1,12.1033], Tmin=(10,'K'), Tmax=(737.639,'K')),
            NASAPolynomial(coeffs=[1.69568,0.0386948,-2.17646e-05,5.95453e-09,-6.36117e-13,-30194.6,20.1776], Tmin=(737.639,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-252.079,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 171,
    label = "r004794",
    molecule = 
"""
1  O u0 p2 c0 {6,D}
2  N u0 p1 c0 {3,S} {4,S} {6,S}
3  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {1,D} {2,S} {5,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.34487,0.0665201,-0.000210814,4.64385e-07,-3.56138e-10,-29752.7,10.098], Tmin=(10,'K'), Tmax=(452.99,'K')),
            NASAPolynomial(coeffs=[0.946242,0.0493713,-2.71084e-05,7.23555e-09,-7.55435e-13,-29142.1,24.1112], Tmin=(452.99,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-247.389,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (340.893,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 172,
    label = "r004852",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  O u0 p2 c0 {6,D}
3  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
5  C u0 p0 c0 {1,D} {3,S} {6,S}
6  C u0 p0 c0 {2,D} {5,S} {12,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44288,0.0523764,-0.000114382,2.08001e-07,-1.47095e-10,-37951.7,10.7976], Tmin=(10,'K'), Tmax=(467.571,'K')),
            NASAPolynomial(coeffs=[2.99662,0.0402857,-2.45591e-05,7.16459e-09,-8.05502e-13,-37736.1,14.4709], Tmin=(467.571,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-315.567,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 173,
    label = "r005102",
    molecule = 
"""
1 O u0 p2 c0 {5,S} {9,S}
2 N u0 p1 c0 {3,S} {4,S} {8,S}
3 N u0 p1 c0 {2,S} {5,D}
4 N u0 p1 c0 {2,S} {6,D}
5 C u0 p0 c0 {1,S} {3,D} {6,S}
6 C u0 p0 c0 {4,D} {5,S} {7,S}
7 H u0 p0 c0 {6,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92648,0.00402319,9.66004e-05,-1.69272e-07,8.86746e-11,8097.7,8.94156], Tmin=(10,'K'), Tmax=(626.05,'K')),
            NASAPolynomial(coeffs=[1.50069,0.0376978,-2.76315e-05,9.39358e-09,-1.19e-12,8045.25,16.6638], Tmin=(626.05,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (67.2932,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 174,
    label = "r005118",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {6,S}
2  O u0 p2 c0 {6,D}
3  N u0 p1 c0 {4,S} {6,S} {13,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {1,S} {2,D} {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46811,0.0481552,-0.000102156,1.9927e-07,-1.40875e-10,-51420,11.2306], Tmin=(10,'K'), Tmax=(511.451,'K')),
            NASAPolynomial(coeffs=[0.318229,0.0479002,-2.84103e-05,7.99232e-09,-8.67504e-13,-50772.3,27.4974], Tmin=(511.451,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-427.547,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (291.007,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 175,
    label = "r005148",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {5,D}
3 N u0 p1 c0 {5,S} {6,S} {7,S}
4 N u0 p1 c0 {1,S} {6,D}
5 C u0 p0 c0 {1,S} {2,D} {3,S}
6 C u0 p0 c0 {3,S} {4,D} {8,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0797,-0.00780614,0.000140519,-2.48772e-07,1.39155e-10,-17804.1,9.72764], Tmin=(10,'K'), Tmax=(582.348,'K')),
            NASAPolynomial(coeffs=[1.9372,0.0308663,-2.0798e-05,6.54341e-09,-7.76664e-13,-17960.8,15.4178], Tmin=(582.348,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-148.049,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 176,
    label = "r005196",
    molecule = 
"""
1  O u0 p2 c0 {4,D}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {1,D} {2,S} {3,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73713,0.0305419,-0.000127759,3.76111e-07,-3.44699e-10,-27937.5,8.94659], Tmin=(10,'K'), Tmax=(410.113,'K')),
            NASAPolynomial(coeffs=[0.128924,0.0331953,-1.84518e-05,4.96363e-09,-5.19954e-13,-27367.9,26.4742], Tmin=(410.113,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-232.297,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 177,
    label = "r005308",
    molecule = 
"""
1  O u0 p2 c0 {6,D}
2  N u0 p1 c0 {4,S} {6,S} {14,S}
3  N u0 p1 c0 {5,S} {6,S} {13,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
6  C u0 p0 c0 {1,D} {2,S} {3,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.25423,0.0760547,-0.000274043,6.00408e-07,-4.60214e-10,-29305.2,9.98099], Tmin=(10,'K'), Tmax=(441.735,'K')),
            NASAPolynomial(coeffs=[1.92586,0.0454705,-2.54875e-05,6.90731e-09,-7.29287e-13,-28772.1,20.0101], Tmin=(441.735,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-243.672,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (315.95,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 178,
    label = "r005356",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {12,S}
2  O u0 p2 c0 {6,D}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {1,S} {3,S} {5,S} {8,S}
5  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
6  C u0 p0 c0 {2,D} {3,S} {11,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87516,0.00724038,0.000146596,-2.83682e-07,1.63999e-10,-29128.1,10.0984], Tmin=(10,'K'), Tmax=(576.932,'K')),
            NASAPolynomial(coeffs=[2.28834,0.0472386,-3.27874e-05,1.07178e-08,-1.32124e-12,-29427.6,12.6988], Tmin=(576.932,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-242.238,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 179,
    label = "r005432",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  O u0 p2 c0 {6,D}
3  N u0 p1 c0 {5,S} {9,S} {10,S}
4  N u0 p1 c0 {6,S} {7,S} {8,S}
5  C u0 p0 c0 {1,D} {3,S} {6,S}
6  C u0 p0 c0 {2,D} {4,S} {5,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79706,0.013989,0.00016029,-4.45182e-07,3.51927e-10,-49253.4,8.13997], Tmin=(10,'K'), Tmax=(452.195,'K')),
            NASAPolynomial(coeffs=[6.32438,0.0298284,-1.89509e-05,5.86282e-09,-7.06145e-13,-49872.5,-6.36501], Tmin=(452.195,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-409.539,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 180,
    label = "r005491",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  N u0 p1 c0 {3,S} {4,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
5  C u0 p0 c0 {1,D} {3,S} {10,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96531,0.00221584,0.000108049,-2.05358e-07,1.26945e-10,-855.051,9.54708], Tmin=(10,'K'), Tmax=(417.228,'K')),
            NASAPolynomial(coeffs=[0.119742,0.0391509,-2.49797e-05,7.58813e-09,-8.82236e-13,-534.741,24.7312], Tmin=(417.228,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-7.11776,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 181,
    label = "r005546",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {10,S}
2  N u0 p1 c0 {3,S} {6,S} {9,S}
3  N u0 p1 c0 {2,S} {4,D}
4  C u0 p0 c0 {1,S} {3,D} {5,S}
5  C u0 p0 c0 {4,S} {6,D} {8,S}
6  C u0 p0 c0 {2,S} {5,D} {7,S}
7  H u0 p0 c0 {6,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.1478,-0.0144462,0.00021733,-3.96703e-07,2.28328e-10,-1593.28,9.76824], Tmin=(10,'K'), Tmax=(575.688,'K')),
            NASAPolynomial(coeffs=[2.40645,0.0383892,-2.6478e-05,8.55121e-09,-1.03673e-12,-2067.81,11.3449], Tmin=(575.688,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-13.276,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 182,
    label = "r005588",
    molecule = 
"""
1 O u0 p2 c0 {5,D}
2 N u0 p1 c0 {4,S} {5,S} {6,S}
3 N u0 p1 c0 {4,D} {9,S}
4 C u0 p0 c0 {2,S} {3,D} {7,S}
5 C u0 p0 c0 {1,D} {2,S} {8,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7722,0.0165499,2.0681e-05,-4.14136e-08,2.04212e-11,-13864.7,9.9967], Tmin=(10,'K'), Tmax=(551.161,'K')),
            NASAPolynomial(coeffs=[1.84299,0.0305509,-1.74231e-05,4.67605e-09,-4.84479e-13,-13652.1,18.1547], Tmin=(551.161,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-115.324,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 183,
    label = "r005763",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {5,S}
2 N u0 p1 c0 {4,S} {5,D}
3 C u0 p0 c0 {1,S} {4,D} {6,S}
4 C u0 p0 c0 {2,S} {3,D} {7,S}
5 C u0 p0 c0 {1,S} {2,D} {8,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.20556,-0.0156206,0.000135691,-1.97337e-07,9.27042e-11,-3397.72,8.66008], Tmin=(10,'K'), Tmax=(678.475,'K')),
            NASAPolynomial(coeffs=[0.00143003,0.0321485,-2.07317e-05,6.29117e-09,-7.24355e-13,-3356.23,23.4134], Tmin=(678.475,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-28.2297,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 184,
    label = "r005826",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {4,S} {7,S} {8,S}
3 N u0 p1 c0 {4,S} {5,S} {6,S}
4 C u0 p0 c0 {1,D} {2,S} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91818,0.00509993,8.79711e-05,-1.91958e-07,1.25285e-10,-29936.1,8.61375], Tmin=(10,'K'), Tmax=(519.461,'K')),
            NASAPolynomial(coeffs=[3.87025,0.0230136,-1.44185e-05,4.46514e-09,-5.38442e-13,-30167.8,6.53517], Tmin=(519.461,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-248.928,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (174.604,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 185,
    label = "r005998",
    molecule = 
"""
1  O u0 p2 c0 {6,D}
2  N u0 p1 c0 {3,S} {4,S} {5,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
5  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {1,D} {3,S} {13,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89968,0.00631904,0.000157636,-3.23814e-07,2.0661e-10,-1145.33,10.5234], Tmin=(10,'K'), Tmax=(498.142,'K')),
            NASAPolynomial(coeffs=[1.06053,0.0490965,-3.13373e-05,9.60521e-09,-1.12973e-12,-1110.36,19.754], Tmin=(498.142,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-9.55095,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 186,
    label = "r006089",
    molecule = 
"""
1  O u0 p2 c0 {6,D}
2  N u0 p1 c0 {3,S} {4,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
5  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {1,D} {4,S} {13,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90261,0.0066036,0.000166565,-3.7089e-07,2.60543e-10,-4735.23,10.5242], Tmin=(10,'K'), Tmax=(442.96,'K')),
            NASAPolynomial(coeffs=[1.07345,0.0485043,-3.06995e-05,9.34132e-09,-1.09103e-12,-4645.03,20.0585], Tmin=(442.96,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-39.3819,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 187,
    label = "r006263",
    molecule = 
"""
1  O u0 p2 c0 {6,D}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
4  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
5  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
6  C u0 p0 c0 {1,D} {3,S} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79939,0.0257272,3.35591e-05,-5.66387e-08,2.24546e-11,-13112.8,10.0042], Tmin=(10,'K'), Tmax=(904.437,'K')),
            NASAPolynomial(coeffs=[3.58758,0.04353,-2.39389e-05,6.36208e-09,-6.59015e-13,-13764.3,7.19114], Tmin=(904.437,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-108.999,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 188,
    label = "r006320",
    molecule = 
"""
1 O u0 p2 c0 {5,S} {6,S}
2 O u0 p2 c0 {5,D}
3 N u0 p1 c0 {4,S} {5,S} {7,S}
4 C u0 p0 c0 {3,S} {6,D} {8,S}
5 C u0 p0 c0 {1,S} {2,D} {3,S}
6 C u0 p0 c0 {1,S} {4,D} {9,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0933,-0.00914814,0.000160807,-2.86387e-07,1.61867e-10,-31226.3,9.75233], Tmin=(10,'K'), Tmax=(573.958,'K')),
            NASAPolynomial(coeffs=[1.55657,0.0348779,-2.3108e-05,7.21398e-09,-8.53207e-13,-31369.1,16.8016], Tmin=(573.958,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-259.65,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 189,
    label = "r006396",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {6,S} {7,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
7  C u0 p0 c0 {2,S} {3,D} {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1275,0.0765231,-0.000199038,3.42298e-07,-2.13476e-10,-66436.3,12.6431], Tmin=(10,'K'), Tmax=(541.259,'K')),
            NASAPolynomial(coeffs=[1.34206,0.0527094,-3.04805e-05,8.36136e-09,-8.87152e-13,-65700.9,25.1686], Tmin=(541.259,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-552.42,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (336.736,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 190,
    label = "r006798",
    molecule = 
"""
1  O u0 p2 c0 {6,D}
2  O u0 p2 c0 {7,D}
3  N u0 p1 c0 {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
5  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
6  C u0 p0 c0 {1,D} {4,S} {11,S}
7  C u0 p0 c0 {2,D} {3,S} {12,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61896,0.0310019,1.38437e-05,-4.18429e-08,1.98312e-11,-15632.7,9.8542], Tmin=(10,'K'), Tmax=(790.923,'K')),
            NASAPolynomial(coeffs=[3.58678,0.041322,-2.49921e-05,7.12884e-09,-7.80492e-13,-15945.3,7.99349], Tmin=(790.923,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-130.021,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 191,
    label = "r007269",
    molecule = 
"""
1  N u0 p1 c0 {4,S} {5,S} {9,S}
2  N u0 p1 c0 {4,D} {6,S}
3  N u0 p1 c0 {7,T}
4  C u0 p0 c0 {1,S} {2,D} {7,S}
5  C u0 p0 c0 {1,S} {6,D} {8,S}
6  C u0 p0 c0 {2,S} {5,D} {10,S}
7  C u0 p0 c0 {3,T} {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.923,0.00445466,0.000113713,-2.09913e-07,1.18244e-10,31729.6,10.421], Tmin=(10,'K'), Tmax=(570.304,'K')),
            NASAPolynomial(coeffs=[1.20052,0.04091,-2.78318e-05,8.92428e-09,-1.08349e-12,31757.8,19.5513], Tmin=(570.304,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (263.782,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 192,
    label = "r007773",
    molecule = 
"""
1  O u0 p2 c0 {7,D}
2  N u0 p1 c0 {6,S} {7,S} {11,S}
3  N u0 p1 c0 {4,S} {7,S} {12,S}
4  N u0 p1 c0 {3,S} {6,D}
5  C u0 p0 c0 {6,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {2,S} {4,D} {5,S}
7  C u0 p0 c0 {1,D} {2,S} {3,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83021,0.0138801,0.000103183,-2.19465e-07,1.39626e-10,-10282.8,10.7154], Tmin=(10,'K'), Tmax=(498.756,'K')),
            NASAPolynomial(coeffs=[1.65741,0.0443936,-2.79465e-05,8.42273e-09,-9.74057e-13,-10228.9,18.0545], Tmin=(498.756,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-85.5207,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (278.535,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 193,
    label = "r007945",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {10,S}
2  N u0 p1 c0 {5,D} {7,S}
3  N u0 p1 c0 {4,S} {6,D}
4  N u0 p1 c0 {3,S} {7,D}
5  C u0 p0 c0 {1,S} {2,D} {6,S}
6  C u0 p0 c0 {3,D} {5,S} {8,S}
7  C u0 p0 c0 {2,S} {4,D} {9,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05946,-0.00587327,0.000156843,-2.60839e-07,1.35022e-10,12448.8,10.4065], Tmin=(10,'K'), Tmax=(627.735,'K')),
            NASAPolynomial(coeffs=[0.5839,0.0444161,-3.05737e-05,9.62021e-09,-1.13378e-12,12330.7,21.1391], Tmin=(627.735,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (103.487,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 194,
    label = "r008426",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {17,S}
2  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {6,S} {8,S}
4  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {3,S} {7,D} {16,S}
7  C u0 p0 c0 {5,S} {6,D} {15,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93164,0.00458165,0.000207109,-4.2221e-07,2.83594e-10,-22598.9,11.8482], Tmin=(10,'K'), Tmax=(380.951,'K')),
            NASAPolynomial(coeffs=[-2.07256,0.0676193,-4.10758e-05,1.20682e-08,-1.37199e-12,-22141.4,35.0211], Tmin=(380.951,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-187.907,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 195,
    label = "r008828",
    molecule = 
"""
1  O u0 p2 c0 {7,S} {13,S}
2  N u0 p1 c0 {3,S} {5,S} {12,S}
3  N u0 p1 c0 {2,S} {7,D}
4  C u0 p0 c0 {5,S} {8,S} {9,S} {10,S}
5  C u0 p0 c0 {2,S} {4,S} {6,D}
6  C u0 p0 c0 {5,D} {7,S} {11,S}
7  C u0 p0 c0 {1,S} {3,D} {6,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88411,0.0066883,0.000151633,-2.84874e-07,1.61745e-10,-6689.67,11.4162], Tmin=(10,'K'), Tmax=(577.29,'K')),
            NASAPolynomial(coeffs=[1.24109,0.0518102,-3.52678e-05,1.14056e-08,-1.39788e-12,-6831.23,18.846], Tmin=(577.29,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-55.671,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 196,
    label = "r009033",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {8,S}
3  C u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
5  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {3,S} {7,D} {16,S}
7  C u0 p0 c0 {4,S} {6,D} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93467,0.00408488,0.000189259,-3.49805e-07,2.10532e-10,-19295.7,11.5848], Tmin=(10,'K'), Tmax=(427.622,'K')),
            NASAPolynomial(coeffs=[-3.16246,0.0704542,-4.34877e-05,1.29526e-08,-1.49026e-12,-18688.6,39.7971], Tmin=(427.622,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-160.454,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 197,
    label = "r009289",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
3  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  C u0 p0 c0 {1,D} {2,S} {6,S}
6  C u0 p0 c0 {5,S} {7,T}
7  C u0 p0 c0 {6,T} {15,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37801,0.0505732,-3.17767e-05,1.00978e-08,-1.28997e-12,598.192,12.7676], Tmin=(10,'K'), Tmax=(1541.05,'K')),
            NASAPolynomial(coeffs=[11.6551,0.0307784,-1.41538e-05,3.18545e-09,-2.84018e-13,-2153.52,-31.3951], Tmin=(1541.05,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (4.9002,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (345.051,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 198,
    label = "r009379",
    molecule = 
"""
1  O u0 p2 c0 {4,D}
2  N u0 p1 c0 {6,T}
3  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {1,D} {3,S} {6,S}
5  C u0 p0 c0 {3,S} {7,T}
6  C u0 p0 c0 {2,T} {4,S}
7  C u0 p0 c0 {5,T} {10,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72675,0.0266593,0.000106216,-4.98068e-07,6.14774e-10,28496.2,12.733], Tmin=(10,'K'), Tmax=(289.873,'K')),
            NASAPolynomial(coeffs=[4.45768,0.0340904,-2.28844e-05,7.31646e-09,-8.89663e-13,28380.2,8.84239], Tmin=(289.873,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (236.962,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 199,
    label = "r009513",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {7,S}
2  O u0 p2 c0 {7,S} {12,S}
3  N u0 p1 c0 {5,S} {7,D}
4  C u0 p0 c0 {5,S} {8,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {4,S} {6,D}
6  C u0 p0 c0 {1,S} {5,D} {11,S}
7  C u0 p0 c0 {1,S} {2,S} {3,D}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87493,0.00750804,0.000149483,-3.02275e-07,1.83747e-10,-32247.6,10.7883], Tmin=(10,'K'), Tmax=(546.719,'K')),
            NASAPolynomial(coeffs=[2.44098,0.0455985,-3.07462e-05,9.8305e-09,-1.19268e-12,-32503.3,13.0682], Tmin=(546.719,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-268.168,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 200,
    label = "r009772",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {13,S}
2  O u0 p2 c0 {5,D}
3  C u0 p0 c0 {5,S} {6,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
5  C u0 p0 c0 {2,D} {3,S} {12,S}
6  C u0 p0 c0 {3,S} {7,T}
7  C u0 p0 c0 {4,S} {6,T}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.39971,0.0588001,-0.000124397,2.24483e-07,-1.62875e-10,-12685.8,12.3694], Tmin=(10,'K'), Tmax=(438.48,'K')),
            NASAPolynomial(coeffs=[3.71663,0.0429733,-2.60032e-05,7.60365e-09,-8.59888e-13,-12589.2,12.5198], Tmin=(438.48,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-105.493,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 201,
    label = "r009945",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  O u0 p2 c0 {6,D}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {5,S} {8,S} {9,S} {10,S}
5  C u0 p0 c0 {1,D} {4,S} {6,S}
6  C u0 p0 c0 {2,D} {5,S} {7,S}
7  C u0 p0 c0 {3,D} {6,S} {11,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.15066,0.0823308,-0.000280165,5.23265e-07,-3.57862e-10,-46049.6,10.3415], Tmin=(10,'K'), Tmax=(458.584,'K')),
            NASAPolynomial(coeffs=[5.71541,0.031094,-1.81544e-05,5.10699e-09,-5.57385e-13,-45981.3,3.2769], Tmin=(458.584,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-382.899,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 202,
    label = "r010048",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {7,S}
2  O u0 p2 c0 {7,D}
3  N u0 p1 c0 {4,S} {7,S} {16,S}
4  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
7  C u0 p0 c0 {1,S} {2,D} {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.32154,0.0708267,-0.000219658,5.43119e-07,-4.69758e-10,-55447.1,11.5567], Tmin=(10,'K'), Tmax=(409.188,'K')),
            NASAPolynomial(coeffs=[0.388388,0.0602301,-3.68583e-05,1.07567e-08,-1.20827e-12,-54878.3,27.1036], Tmin=(409.188,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-461.034,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (361.68,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 203,
    label = "r010345",
    molecule = 
"""
1  O u0 p2 c0 {7,D}
2  N u0 p1 c0 {4,S} {5,S} {13,S}
3  N u0 p1 c0 {7,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
6  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
7  C u0 p0 c0 {1,D} {3,S} {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76587,0.0185473,0.000164042,-3.92394e-07,2.82824e-10,-15338,10.4026], Tmin=(10,'K'), Tmax=(444.339,'K')),
            NASAPolynomial(coeffs=[1.54928,0.0584459,-3.79761e-05,1.17231e-08,-1.38113e-12,-15337.9,17.0828], Tmin=(444.339,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-127.545,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (345.051,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 204,
    label = "r010419",
    molecule = 
"""
1  O u0 p2 c0 {7,S} {13,S}
2  N u0 p1 c0 {6,S} {7,S} {12,S}
3  N u0 p1 c0 {5,S} {7,D}
4  C u0 p0 c0 {5,S} {8,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {4,S} {6,D}
6  C u0 p0 c0 {2,S} {5,D} {11,S}
7  C u0 p0 c0 {1,S} {2,S} {3,D}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89746,0.00662895,0.00016815,-3.54398e-07,2.32905e-10,-13964.6,10.9654], Tmin=(10,'K'), Tmax=(477.67,'K')),
            NASAPolynomial(coeffs=[0.681258,0.0523493,-3.44211e-05,1.06664e-08,-1.25531e-12,-13871.7,21.8618], Tmin=(477.67,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-116.132,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 205,
    label = "r010564",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {7,D}
3  N u0 p1 c0 {7,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
6  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
7  C u0 p0 c0 {2,D} {3,S} {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68656,0.028609,6.8426e-05,-1.47108e-07,8.07383e-11,-37127.5,10.55], Tmin=(10,'K'), Tmax=(636.768,'K')),
            NASAPolynomial(coeffs=[3.62428,0.0500262,-3.15552e-05,9.42363e-09,-1.07592e-12,-37545.8,7.47521], Tmin=(636.768,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-308.738,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (320.107,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 206,
    label = "r011399",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {7,S}
2  O u0 p2 c0 {7,D}
3  N u0 p1 c0 {6,S} {7,S} {8,S}
4  N u0 p1 c0 {6,S} {9,S} {10,S}
5  N u0 p1 c0 {1,S} {6,D}
6  C u0 p0 c0 {3,S} {4,S} {5,D}
7  C u0 p0 c0 {1,S} {2,D} {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87916,0.00725781,0.000128337,-2.66523e-07,1.64035e-10,-19723.5,11.2851], Tmin=(10,'K'), Tmax=(550.334,'K')),
            NASAPolynomial(coeffs=[3.50068,0.0368306,-2.53731e-05,8.23851e-09,-1.01077e-12,-20088,9.19478], Tmin=(550.334,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-164.036,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 207,
    label = "r011443",
    molecule = 
"""
1  O u0 p2 c0 {7,S} {11,S}
2  N u0 p1 c0 {5,S} {7,S} {8,S}
3  N u0 p1 c0 {6,S} {9,S} {10,S}
4  N u0 p1 c0 {6,S} {7,D}
5  N u0 p1 c0 {2,S} {6,D}
6  C u0 p0 c0 {3,S} {4,S} {5,D}
7  C u0 p0 c0 {1,S} {2,S} {4,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88601,0.0066499,0.000138399,-2.68846e-07,1.56178e-10,-2924.99,11.4773], Tmin=(10,'K'), Tmax=(570.545,'K')),
            NASAPolynomial(coeffs=[2.05084,0.0455458,-3.22948e-05,1.05687e-08,-1.29351e-12,-3139.24,15.5883], Tmin=(570.545,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-24.3672,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 208,
    label = "r011506",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {7,S}
2  N u0 p1 c0 {5,D} {6,S}
3  N u0 p1 c0 {4,D} {11,S}
4  C u0 p0 c0 {1,S} {3,D} {5,S}
5  C u0 p0 c0 {2,D} {4,S} {8,S}
6  C u0 p0 c0 {2,S} {7,D} {9,S}
7  C u0 p0 c0 {1,S} {6,D} {10,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9387,0.00352108,0.000120697,-2.10886e-07,1.14353e-10,10695.2,10.3098], Tmin=(10,'K'), Tmax=(564.202,'K')),
            NASAPolynomial(coeffs=[-0.725958,0.0491002,-3.37353e-05,1.0888e-08,-1.32744e-12,11022.5,28.38], Tmin=(564.202,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (88.8977,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 209,
    label = "r011937",
    molecule = 
"""
1  O u0 p2 c0 {7,S} {12,S}
2  N u0 p1 c0 {6,S} {7,S} {9,S}
3  N u0 p1 c0 {5,S} {10,S} {11,S}
4  N u0 p1 c0 {5,S} {7,D}
5  C u0 p0 c0 {3,S} {4,S} {6,D}
6  C u0 p0 c0 {2,S} {5,D} {8,S}
7  C u0 p0 c0 {1,S} {2,S} {4,D}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85666,0.00880064,0.00015955,-3.37865e-07,2.13526e-10,-8362.51,11.2149], Tmin=(10,'K'), Tmax=(530.936,'K')),
            NASAPolynomial(coeffs=[2.96574,0.0459772,-3.15492e-05,1.01596e-08,-1.23353e-12,-8697.3,10.9054], Tmin=(530.936,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-69.5783,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

