name = "test_thermo_cov"
shortDesc = u"test for thermo coverage dependent models"
longDesc = u"""
A few surface species adsorbed on Ni(111), to test the coverage-dependent thermo models.
"""


entry(
    index = 1,
    label = "*",
    molecule = 
"""
1 X u0 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0,0,0,0,0,0.0,0.0], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.0,0,0,0,0,0.0,0.0], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""library value for a vacant surface site""",
    longDesc = u"""Zeros, by definition.""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 2,
    label = "O_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,D}
2 O  u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.79722382E-01, 1.25453156E-02, -2.29924588E-05, 1.94187177E-08, -6.22414099E-12, -1.73402246E+04, -2.22409728E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.92050897E+00, -2.70455589E-04, 5.15610634E-07, -2.93911213E-10, 5.54030466E-14, -1.78369003E+04, -1.50940536E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
        thermo_coverage_dependence = {"""
                                      1 X  u0 p0 c0 {2,D}
                                      2 O  u0 p2 c0 {1,D}
                                      """:{'model': 'polynomial', 'enthalpy-coefficients':[-0.04321765,1.04225839,0], 'entropy-coefficients':[0,0,0]}},
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.586 eV.
            Linear scaling parameters: ref_adatom_O = -3.586 eV, psi = 0.00000 eV, gamma_O(X) = 1.000.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 3,
    label = "CO*",
    molecule =  
"""
1 C u0 p0 {2,D} {3,D}
2 O u0 p2 {1,D} 
3 X u0 p0 {1,D} 
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[ 3.13851368E+00,  7.37719433E-03, -1.21673211E-05,  1.06231734E-08, -3.55085256E-12, -3.01011015E+04, -1.40684039E+01], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[ 4.39015575E+00,  1.21423223E-03,  2.26543548E-08, -2.74772156E-10,  6.84375847E-14, -3.03339593E+04, -1.99186406E+01], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
        thermo_coverage_dependence = {"""
                                      1 C u0 p0 {2,D} {3,D}
                                      2 O u0 p2 {1,D} 
                                      3 X u0 p0 {1,D} 
                                      """:{'model': 'polynomial', 'enthalpy-coefficients':[-0.0503, 0.8575, 0], 'entropy-coefficients':[0,0,0]}},
    ),
    shortDesc = u"""CO adsorbed on nickel (?)""",
    longDesc =  u"""Estimated via CFG-TiC
    Unsure of adjacency list.""",
    metal = "Ni",
    facet = "111",
)
