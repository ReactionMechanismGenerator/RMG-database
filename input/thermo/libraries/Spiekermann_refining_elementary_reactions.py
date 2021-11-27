#!/usr/bin/env python
# encoding: utf-8

name = "Spiekermann_refining_elementary_reactions"
shortDesc = "Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann."
longDesc = """
This library is made by Kevin Spiekermann and contains the thermochemistry for a subset of the species from 
Spiekermann, K. A.; Pattanaik, L.; Green, W. H. 
Refining elementary reactions with a highly accurate quantum method. 
Sci. data. (In preparation)

This published work reports nearly 12,000 reactions, with about 1,500 reactions matching RMG templates. 
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

The frequency scaling factor at ωB97X-D3/def2-TZVP was calculated as 0.984 using the method from Alecu et al. (https://pubs.acs.org/doi/abs/10.1021/ct100326h)
It was added to RMG-database in PR #459: https://github.com/ReactionMechanismGenerator/RMG-database/pull/459/commits/e2e93fb51dad93fa9d8271209cfbb50641a84c58

All values include atom energy corrections, which were fit to the single point energies of experimental geometries for 16 small molecules (no geometry optimization was performed).
The ωB97X-D3/def2-TZVP AEC values were added in RMG-database PR #459: https://github.com/ReactionMechanismGenerator/RMG-database/pull/459
The CCSD(T)-F12a/cc-pVDZ-F12 AEC values were added in RMG-database PR #508: https://github.com/ReactionMechanismGenerator/RMG-database/pull/508

All values also include bond additivity corrections.
BACs were fit using about 400 species from our reference set using the procedure from Petersson et al. 1998 (http://aip.scitation.org/doi/10.1063/1.477794)
The ωB97X-D3/def2-TZVP BAC values were added in RMG-database PR #459: https://github.com/ReactionMechanismGenerator/RMG-database/pull/459
The CCSD(T)-F12a/cc-pVDZ-F12 BAC values were added in RMG-database PR #508: https://github.com/ReactionMechanismGenerator/RMG-database/pull/508

Disclaimer: The number of significant figures displayed does not reflect the accuracy of the thermochemistry values.
As described in RMG-database PR #508, after fitting the Petersson BACs, the enthalpy values at the coupled cluster level have an MAE (RMSE) of 0.517 (0.826) kcal/mol relative to our reference set. 
As described in the publication from Spiekermann et al., the enthalpy values have an MAE (RMSE) of 0.995 (1.246) kcal/mol relative to an external test set from Pedley: Pedley, J. Thermochemical data and structures of organic compounds, vol. 1 (CRC Press, 1994).
These values are similar to those from other published works:
- Bischoff, F. A., Wolfsegger, S., Tew, D. P. & Klopper, W. Assessment of basis sets for f12 explicitly-correlated molecular electronic-structure methodfs. Mol. Phys. 107, 963–975 (2009).
- Knizia, G., Adler, T. B. & Werner, H.-J. Simplified ccsd (t)-f12 methods: Theory and benchmarks. The J. chemical physics 130, 054104 (2009). 
- Adler, T. B., Knizia, G. & Werner, H.-J. A simple and efficient ccsd(t)-f12 approximation (2007).
- Pfeiffer, F., Rauhut, G., Feller, D. & Peterson, K. A. Anharmonic zero point vibrational energies: Tipping the scales in accurate thermochemistry calculations? The J. chemical physics 138, 044311 (2013).
- Shang, Y., Ning, H., Shi, J., Wang, H. & Luo, S.-N. Chemical kinetics of h-abstractions from dimethyl amine by h, ch 3, oh, and ho 2 radicals with multi-structural torsional anharmonicity. Phys. Chem. Chem. Phys. 21, 12685–12696 (2019).
"""
entry(
    index = 0,
    label = "p001084",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {10,S}
2  O u0 p2 c0 {6,D}
3  N u0 p1 c0 {5,S} {7,S} {8,S}
4  N u0 p1 c0 {5,D} {6,S}
5  C u0 p0 c0 {1,S} {3,S} {4,D}
6  C u0 p0 c0 {2,D} {4,S} {9,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90453,0.0068491,0.000125755,-2.92973e-07,2.12971e-10,-45444.2,10.0669], Tmin=(10,'K'), Tmax=(433.425,'K')),
            NASAPolynomial(coeffs=[2.09778,0.0367646,-2.36023e-05,7.24527e-09,-8.51275e-13,-45412,15.8381], Tmin=(433.425,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-377.851,'kJ/mol'),
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
    index = 1,
    label = "r001084",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  O u0 p2 c0 {6,D}
3  N u0 p1 c0 {5,S} {6,S} {7,S}
4  N u0 p1 c0 {5,S} {8,S} {9,S}
5  C u0 p0 c0 {1,D} {3,S} {4,S}
6  C u0 p0 c0 {2,D} {3,S} {10,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88423,0.00825528,0.000133399,-3.31802e-07,2.52823e-10,-51045.1,10.3937], Tmin=(10,'K'), Tmax=(428.701,'K')),
            NASAPolynomial(coeffs=[2.89294,0.0351772,-2.26349e-05,7.00331e-09,-8.2982e-13,-51122.5,12.4424], Tmin=(428.701,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-424.419,'kJ/mol'),
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
    index = 2,
    label = "p001085",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {10,S}
2  O u0 p2 c0 {6,D}
3  N u0 p1 c0 {5,S} {6,S} {7,S}
4  N u0 p1 c0 {5,D} {9,S}
5  C u0 p0 c0 {1,S} {3,S} {4,D}
6  C u0 p0 c0 {2,D} {3,S} {8,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89676,0.0069668,0.00013048,-3.0221e-07,2.14699e-10,-42491.9,10.4941], Tmin=(10,'K'), Tmax=(458.393,'K')),
            NASAPolynomial(coeffs=[2.64332,0.0359324,-2.32967e-05,7.23252e-09,-8.575e-13,-42566.4,13.4975], Tmin=(458.393,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-353.313,'kJ/mol'),
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
    index = 3,
    label = "p001086",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {6,S}
2  O u0 p2 c0 {5,D}
3  N u0 p1 c0 {5,S} {7,S} {8,S}
4  N u0 p1 c0 {6,D} {10,S}
5  C u0 p0 c0 {1,S} {2,D} {3,S}
6  C u0 p0 c0 {1,S} {4,D} {9,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66393,0.0292743,-2.15322e-06,-2.1046e-08,1.21524e-11,-42414,10.6522], Tmin=(10,'K'), Tmax=(757.562,'K')),
            NASAPolynomial(coeffs=[4.9002,0.0298984,-1.75495e-05,4.96452e-09,-5.43608e-13,-42806.5,3.67671], Tmin=(757.562,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-352.685,'kJ/mol'),
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
    index = 4,
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
            NASAPolynomial(coeffs=[3.82631,0.0162512,0.000125687,-4.39385e-07,4.659e-10,-38718.2,11.4505], Tmin=(10,'K'), Tmax=(302.995,'K')),
            NASAPolynomial(coeffs=[3.20335,0.0354034,-2.32286e-05,7.3043e-09,-8.77305e-13,-38730.7,12.8843], Tmin=(302.995,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-321.895,'kJ/mol'),
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
    index = 5,
    label = "p001089",
    molecule = 
"""
1  O u0 p2 c0 {6,S} {10,S}
2  O u0 p2 c0 {5,D}
3  N u0 p1 c0 {5,S} {7,S} {8,S}
4  N u0 p1 c0 {5,S} {6,D}
5  C u0 p0 c0 {2,D} {3,S} {4,S}
6  C u0 p0 c0 {1,S} {4,D} {9,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85067,0.0143143,0.000141804,-5.0958e-07,5.7187e-10,-44659.9,10.5534], Tmin=(10,'K'), Tmax=(279.306,'K')),
            NASAPolynomial(coeffs=[3.04532,0.0354442,-2.32093e-05,7.29584e-09,-8.76641e-13,-44652.3,12.7415], Tmin=(279.306,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-371.297,'kJ/mol'),
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
    index = 6,
    label = "p001235",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {4,D}
3 N u0 p1 c0 {5,D} {8,S}
4 C u0 p0 c0 {1,S} {2,D} {7,S}
5 C u0 p0 c0 {1,S} {3,D} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9412,0.00367745,8.97937e-05,-1.83545e-07,1.16062e-10,55343.3,9.94177], Tmin=(10,'K'), Tmax=(504.787,'K')),
            NASAPolynomial(coeffs=[2.34563,0.028174,-1.82207e-05,5.62546e-09,-6.6405e-13,55353.3,15.0529], Tmin=(504.787,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (460.132,'kJ/mol'),
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
    index = 7,
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
            NASAPolynomial(coeffs=[4.19196,-0.0148682,0.000135852,-2.02053e-07,9.69878e-11,22059.2,7.94616], Tmin=(10,'K'), Tmax=(665.053,'K')),
            NASAPolynomial(coeffs=[0.275364,0.0315389,-2.03558e-05,6.19759e-09,-7.1627e-13,22074.8,21.4447], Tmin=(665.053,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (183.426,'kJ/mol'),
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
    index = 8,
    label = "p001691",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {6,S}
2  O u0 p2 c0 {5,S} {8,S}
3  N u0 p1 c0 {5,D} {9,S}
4  N u0 p1 c0 {6,D} {10,S}
5  C u0 p0 c0 {1,S} {2,S} {3,D}
6  C u0 p0 c0 {1,S} {4,D} {7,S}
7  H u0 p0 c0 {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90256,0.00616103,0.000124812,-2.67251e-07,1.74325e-10,-32914,10.7644], Tmin=(10,'K'), Tmax=(502.975,'K')),
            NASAPolynomial(coeffs=[2.59734,0.0362399,-2.36378e-05,7.37722e-09,-8.78888e-13,-33031.9,13.6874], Tmin=(502.975,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-273.69,'kJ/mol'),
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
    index = 9,
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
            NASAPolynomial(coeffs=[3.92559,0.0149988,1.20319e-05,-2.22577e-08,8.39575e-12,-34102,9.23015], Tmin=(10,'K'), Tmax=(1007.89,'K')),
            NASAPolynomial(coeffs=[5.16881,0.0201742,-1.07157e-05,2.74036e-09,-2.73287e-13,-34866.1,0.67534], Tmin=(1007.89,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-283.507,'kJ/mol'),
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
    index = 10,
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
            NASAPolynomial(coeffs=[3.83419,0.0137275,2.22867e-05,-4.30261e-08,2.07116e-11,-42139.6,8.49502], Tmin=(10,'K'), Tmax=(688.898,'K')),
            NASAPolynomial(coeffs=[2.66155,0.0257622,-1.52963e-05,4.35569e-09,-4.79311e-13,-42102,12.8153], Tmin=(688.898,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-350.389,'kJ/mol'),
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
    index = 11,
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
            NASAPolynomial(coeffs=[4.18171,-0.0135628,0.000115446,-1.65192e-07,7.60827e-11,4321.24,7.92826], Tmin=(10,'K'), Tmax=(694.897,'K')),
            NASAPolynomial(coeffs=[0.550232,0.0278611,-1.82656e-05,5.58285e-09,-6.44488e-13,4330.5,20.5614], Tmin=(694.897,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (35.9504,'kJ/mol'),
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
    index = 12,
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
            NASAPolynomial(coeffs=[3.87984,0.0117384,2.85566e-05,-5.71836e-08,2.93799e-11,29991.5,9.75096], Tmin=(10,'K'), Tmax=(680.825,'K')),
            NASAPolynomial(coeffs=[3.8194,0.0214159,-1.33042e-05,3.91873e-09,-4.42129e-13,29783.7,8.43258], Tmin=(680.825,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (249.351,'kJ/mol'),
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
    index = 13,
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
            NASAPolynomial(coeffs=[3.87783,0.00807989,0.000106218,-2.66769e-07,1.94606e-10,2643.25,9.21739], Tmin=(10,'K'), Tmax=(480.43,'K')),
            NASAPolynomial(coeffs=[4.97716,0.0228572,-1.46347e-05,4.60813e-09,-5.60578e-13,2261.45,1.84547], Tmin=(480.43,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (21.9533,'kJ/mol'),
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
    index = 14,
    label = "p003183",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {7,S}
2 N u0 p1 c0 {3,D} {6,S}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 C u0 p0 c0 {3,S} {5,T}
5 C u0 p0 c0 {4,T} {8,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91038,0.00533575,9.19269e-05,-1.89724e-07,1.1583e-10,8195.7,9.02564], Tmin=(10,'K'), Tmax=(558.847,'K')),
            NASAPolynomial(coeffs=[3.92299,0.0256042,-1.71204e-05,5.54909e-09,-6.87347e-13,7876.38,6.1278], Tmin=(558.847,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (68.1082,'kJ/mol'),
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
    index = 15,
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
            NASAPolynomial(coeffs=[3.92982,0.00414922,0.00013109,-2.39364e-07,1.36465e-10,-5592.01,11.2179], Tmin=(10,'K'), Tmax=(541.878,'K')),
            NASAPolynomial(coeffs=[-0.123429,0.0484905,-3.15733e-05,9.87276e-09,-1.18128e-12,-5364.46,26.3353], Tmin=(541.878,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-46.5227,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 16,
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
            NASAPolynomial(coeffs=[3.91708,0.00519553,0.000141656,-2.84791e-07,1.79102e-10,-13149.5,11.6965], Tmin=(10,'K'), Tmax=(498.878,'K')),
            NASAPolynomial(coeffs=[0.943721,0.0454404,-2.86746e-05,8.74058e-09,-1.02535e-12,-13057,21.9276], Tmin=(498.878,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-109.355,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

entry(
    index = 17,
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
            NASAPolynomial(coeffs=[3.92814,0.00424912,9.85243e-05,-1.8956e-07,1.11209e-10,55412.4,9.7156], Tmin=(10,'K'), Tmax=(554.554,'K')),
            NASAPolynomial(coeffs=[2.23392,0.0325191,-2.13545e-05,6.74321e-09,-8.14556e-13,55353.5,14.6652], Tmin=(554.554,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (460.696,'kJ/mol'),
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
    index = 18,
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
            NASAPolynomial(coeffs=[4.21464,-0.0168371,0.000155578,-2.33813e-07,1.13789e-10,11267.3,8.67808], Tmin=(10,'K'), Tmax=(653.143,'K')),
            NASAPolynomial(coeffs=[-0.293321,0.0357942,-2.27634e-05,6.87882e-09,-7.92183e-13,11322.5,24.4202], Tmin=(653.143,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (93.6961,'kJ/mol'),
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
    index = 19,
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
            NASAPolynomial(coeffs=[4.18045,-0.0133194,0.000112508,-1.58903e-07,7.22193e-11,7844.5,8.62328], Tmin=(10,'K'), Tmax=(703.312,'K')),
            NASAPolynomial(coeffs=[0.444753,0.0279626,-1.82684e-05,5.56371e-09,-6.40191e-13,7874.44,21.8082], Tmin=(703.312,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (65.2464,'kJ/mol'),
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
    index = 20,
    label = "p004749",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {9,S}
2  N u0 p1 c0 {5,S} {6,S} {7,S}
3  N u0 p1 c0 {5,D} {10,S}
4  N u0 p1 c0 {6,D} {11,S}
5  C u0 p0 c0 {1,S} {2,S} {3,D}
6  C u0 p0 c0 {2,S} {4,D} {8,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89437,0.00667872,0.000136356,-2.91615e-07,1.90382e-10,-15654.2,10.5049], Tmin=(10,'K'), Tmax=(502.61,'K')),
            NASAPolynomial(coeffs=[2.50709,0.0392486,-2.50987e-05,7.7663e-09,-9.23056e-13,-15786.7,13.5381], Tmin=(502.61,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-130.186,'kJ/mol'),
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
    index = 21,
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
            NASAPolynomial(coeffs=[3.88963,0.0071797,0.000140299,-3.13164e-07,2.13624e-10,-24203.6,10.4972], Tmin=(10,'K'), Tmax=(481.856,'K')),
            NASAPolynomial(coeffs=[2.70714,0.0385412,-2.4398e-05,7.49517e-09,-8.86622e-13,-24339.8,12.7432], Tmin=(481.856,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-201.264,'kJ/mol'),
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
    index = 22,
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
            NASAPolynomial(coeffs=[3.85265,0.0142526,1.9194e-05,-3.6021e-08,1.58841e-11,-35075.3,9.93557], Tmin=(10,'K'), Tmax=(801.355,'K')),
            NASAPolynomial(coeffs=[3.49583,0.0239762,-1.38743e-05,3.85765e-09,-4.15466e-13,-35273.1,9.9868], Tmin=(801.355,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-291.638,'kJ/mol'),
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
    index = 23,
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
            NASAPolynomial(coeffs=[3.86738,0.00842115,0.000132184,-3.01176e-07,2.03049e-10,-44204.8,10.5243], Tmin=(10,'K'), Tmax=(507.624,'K')),
            NASAPolynomial(coeffs=[4.18501,0.0332134,-2.17311e-05,6.88788e-09,-8.36332e-13,-44588.7,5.74335], Tmin=(507.624,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-367.576,'kJ/mol'),
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
    index = 24,
    label = "r005432",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  O u0 p2 c0 {6,D}
3  N u0 p1 c0 {5,S} {7,S} {8,S}
4  N u0 p1 c0 {6,S} {9,S} {10,S}
5  C u0 p0 c0 {1,D} {3,S} {6,S}
6  C u0 p0 c0 {2,D} {4,S} {5,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85473,0.00947281,0.00013695,-3.28904e-07,2.32268e-10,-51635.8,9.66211], Tmin=(10,'K'), Tmax=(489.046,'K')),
            NASAPolynomial(coeffs=[4.61323,0.0320794,-2.07566e-05,6.54296e-09,-7.9293e-13,-52054.5,3.0229], Tmin=(489.046,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-429.357,'kJ/mol'),
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
    index = 25,
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
            NASAPolynomial(coeffs=[3.86718,0.0122449,3.89079e-05,-6.79101e-08,3.26697e-11,-16154.8,9.29021], Tmin=(10,'K'), Tmax=(683.636,'K')),
            NASAPolynomial(coeffs=[2.36025,0.0294686,-1.73287e-05,4.91801e-09,-5.40737e-13,-16145.2,14.5503], Tmin=(683.636,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-134.333,'kJ/mol'),
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
    index = 26,
    label = "p005588",
    molecule = 
"""
1 O u0 p2 c0 {5,S} {9,S}
2 N u0 p1 c0 {4,S} {5,D}
3 N u0 p1 c0 {4,D} {8,S}
4 C u0 p0 c0 {2,S} {3,D} {6,S}
5 C u0 p0 c0 {1,S} {2,D} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89148,0.00928569,5.89762e-05,-1.09647e-07,6.0365e-11,-9375.62,9.94308], Tmin=(10,'K'), Tmax=(573.894,'K')),
            NASAPolynomial(coeffs=[1.97725,0.0308188,-1.87146e-05,5.47283e-09,-6.17596e-13,-9290.8,16.9399], Tmin=(573.894,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-77.9714,'kJ/mol'),
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
    index = 27,
    label = "p005593",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {5,S}
2 N u0 p1 c0 {4,D} {8,S}
3 N u0 p1 c0 {5,D} {9,S}
4 C u0 p0 c0 {1,S} {2,D} {6,S}
5 C u0 p0 c0 {1,S} {3,D} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9237,0.0155513,1.84862e-05,-3.04153e-08,1.14421e-11,-6556.28,9.49339], Tmin=(10,'K'), Tmax=(977.812,'K')),
            NASAPolynomial(coeffs=[4.65854,0.0243097,-1.29968e-05,3.35413e-09,-3.37727e-13,-7262.4,3.08884], Tmin=(977.812,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-54.4747,'kJ/mol'),
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
    index = 28,
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
            NASAPolynomial(coeffs=[4.20556,-0.0156206,0.000135691,-1.97337e-07,9.27042e-11,-6008.9,8.66008], Tmin=(10,'K'), Tmax=(678.476,'K')),
            NASAPolynomial(coeffs=[0.00143082,0.0321485,-2.07317e-05,6.29117e-09,-7.24355e-13,-5967.41,23.4134], Tmin=(678.476,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-49.9403,'kJ/mol'),
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
    index = 29,
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
            NASAPolynomial(coeffs=[3.92614,0.00459907,9.36823e-05,-1.96966e-07,1.25816e-10,29470.8,9.9431], Tmin=(10,'K'), Tmax=(515.053,'K')),
            NASAPolynomial(coeffs=[2.94794,0.0275793,-1.80449e-05,5.63866e-09,-6.73193e-13,29367.5,12.0325], Tmin=(515.053,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (245.011,'kJ/mol'),
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
    index = 30,
    label = "p005826",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {8,S}
2 N u0 p1 c0 {4,S} {5,S} {6,S}
3 N u0 p1 c0 {4,D} {7,S}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94131,0.00334279,7.65673e-05,-1.40641e-07,7.83088e-11,-24364.4,8.41878], Tmin=(10,'K'), Tmax=(589.47,'K')),
            NASAPolynomial(coeffs=[2.60078,0.0263478,-1.73647e-05,5.61951e-09,-6.97619e-13,-24448.1,12.1279], Tmin=(589.47,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-202.604,'kJ/mol'),
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
    index = 31,
    label = "r005826",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {4,S} {5,S} {6,S}
3 N u0 p1 c0 {4,S} {7,S} {8,S}
4 C u0 p0 c0 {1,D} {2,S} {3,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93687,0.00367548,7.83773e-05,-1.49834e-07,8.6724e-11,-31705,7.74707], Tmin=(10,'K'), Tmax=(571.929,'K')),
            NASAPolynomial(coeffs=[2.99134,0.0249769,-1.60134e-05,5.09724e-09,-6.27524e-13,-31837.1,9.6802], Tmin=(571.929,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-263.637,'kJ/mol'),
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
    index = 32,
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
            NASAPolynomial(coeffs=[3.92299,0.00445513,0.000113709,-2.09901e-07,1.18235e-10,27155,10.421], Tmin=(10,'K'), Tmax=(570.325,'K')),
            NASAPolynomial(coeffs=[1.20078,0.0409092,-2.78311e-05,8.92399e-09,-1.08345e-12,27183.2,19.55], Tmin=(570.325,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (225.747,'kJ/mol'),
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
    index = 33,
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
            NASAPolynomial(coeffs=[3.81607,0.0130338,0.000148737,-3.98101e-07,3.1032e-10,71581.9,11.9623], Tmin=(10,'K'), Tmax=(442.945,'K')),
            NASAPolynomial(coeffs=[4.48889,0.0355277,-2.41865e-05,7.77793e-09,-9.46038e-13,71242,6.10048], Tmin=(442.945,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (595.15,'kJ/mol'),
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
    index = 34,
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
            NASAPolynomial(coeffs=[4.07209,-0.0074976,0.000179242,-3.1687e-07,1.77508e-10,-5051.56,10.5595], Tmin=(10,'K'), Tmax=(572.922,'K')),
            NASAPolynomial(coeffs=[0.511206,0.0447269,-2.91311e-05,8.96333e-09,-1.04858e-12,-5092.62,21.836], Tmin=(572.922,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-42.0241,'kJ/mol'),
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
    index = 35,
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
            NASAPolynomial(coeffs=[3.93833,0.00353767,0.00012055,-2.1048e-07,1.14013e-10,7208.85,10.3105], Tmin=(10,'K'), Tmax=(565.219,'K')),
            NASAPolynomial(coeffs=[-0.717119,0.0490743,-3.37099e-05,1.08778e-08,-1.32602e-12,7534,28.3352], Tmin=(565.219,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (59.9102,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.""",
    longDesc = 
"""
Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann.
""",
)

