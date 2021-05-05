entry(
    index = 1,
    label = "H2_ads",
    molecule =
"""
1 X  u0 p0 c0
2 H  u0 p0 c0 {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78935111E+00, 1.10148021E-03,  -2.31320100E-06, 2.11937826E-09, -6.31350224E-13, -2.16864504027E+03, -1.00616465E+01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.06700165E+00, -5.01780079E-04,   6.70738856E-07, -1.79170942E-10, 8.86886631E-15, -2.19271858027E+03, -1.12621699E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Using the Pt111 value for NASA polynomial, but adjusting the a5 parameter by (delta Binding Energy)/R.
            DFT binding energy on Pt111: -0.054 eV.
            DFT binfing energy on Cu111: -0.08 eV. 
            delta BE: -0.054 - (-0.08) = +0.026 eV = 0.026 eV * (1.602176565e-19 J/eV) * (6.02214*10^23) = 2508 J/mol
            
            a5_low = -1.86700333*10^3 - (2508 J/mol) / (8.3145 J/mol K) = -2.16864504027E+03
            a5_high = -1.89107687*10^3 - (2508 J/mol) / (8.3145 J/mol K) = -2.19271858027E+03
            
            Source for H2 Binding Energy: 
            "On the hydrogen adsorption and dissociation on Cu surfaces and nanorows"
            Álvarez-Falcón et al.
            Table 7, PBE-D2 value
            DOI:10.1016/j.susc.2015.08.005""",

    metal = "Cu",
    facet = "111",
)