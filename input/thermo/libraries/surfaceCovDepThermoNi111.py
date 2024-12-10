name = "surfaceCovDepThermoNi111"
shortDesc = u"Data for thermo coverage dependent models on Ni(111)"
longDesc = u"""
A few surface species adsorbed on Ni(111) to test the coverage-dependent thermo models.
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
                                      """:{'model': 'polynomial', 'enthalpy-coefficients':[(-17983.61447181034, 'J/mol'), (44587.872022684605, 'J/mol'), (123096.5401042523, 'J/mol')], 'entropy-coefficients':[(0, 'J/(mol*K)'), (0, 'J/(mol*K)'), (0, 'J/(mol*K)')]}},
    ),
    shortDesc = u"""CO adsorbed on nickel (?)""",
    longDesc =  u"""Estimated via CFG-TiC
    Unsure of adjacency list.""",
    metal = "Ni",
    facet = "111",
)
