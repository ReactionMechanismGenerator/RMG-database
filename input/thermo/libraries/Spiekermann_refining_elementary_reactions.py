#!/usr/bin/env python
# encoding: utf-8

name = "Spiekermann_refining_elementary_reactions"
shortDesc = "Calculated at CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP by Kevin Spiekermann."
longDesc = """
This library is made by Kevin Spiekermann and contains the thermochemistry for a subset of the species from 
Spiekermann, K. A.; Pattanaik, L.; Green, W. H. 
Refining elementary reactions with a highly accurate quantum method. 
Sci. data. (In preparation)

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
    index = 2,
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
    index = 3,
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
    index = 4,
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
    index = 5,
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
    index = 6,
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
    index = 7,
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
    index = 8,
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
    index = 9,
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
    index = 10,
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
    index = 11,
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
    index = 12,
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
    index = 13,
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
    index = 14,
    label = "p004006",
    molecule = 
"""
1 O u0 p3 c-1 {6,S}
2 N u0 p0 c+1 {5,D} {6,S} {7,S}
3 N u0 p1 c0 {4,S} {5,S} {8,S}
4 N u0 p1 c0 {3,S} {6,D}
5 N u0 p1 c0 {2,D} {3,S}
6 C u0 p0 c0 {1,S} {2,S} {4,D}
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
    index = 15,
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
    index = 16,
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
    index = 17,
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
    index = 18,
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
    index = 19,
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
    index = 20,
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
    index = 21,
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
    index = 22,
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
    index = 24,
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
    index = 25,
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
    index = 26,
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
    index = 27,
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
    index = 28,
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
    index = 29,
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
    index = 30,
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
    index = 31,
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
    index = 32,
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
    index = 33,
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
    index = 35,
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
    index = 36,
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
    index = 37,
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
    index = 38,
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
    index = 39,
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
    index = 40,
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
    index = 41,
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
    index = 42,
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
    index = 43,
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
    index = 44,
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
    index = 45,
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
    index = 46,
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
    index = 47,
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
    index = 48,
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
    index = 49,
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
    index = 50,
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
    index = 51,
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
    index = 52,
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
    index = 53,
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
    index = 54,
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
    index = 55,
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
    index = 56,
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
    index = 57,
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
    index = 58,
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
    index = 59,
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
    index = 60,
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
    index = 61,
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
    index = 62,
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
    index = 63,
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
    index = 64,
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
    index = 65,
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
    index = 66,
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

