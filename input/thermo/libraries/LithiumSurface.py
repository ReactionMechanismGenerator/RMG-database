name = "LithiumSurface"
shortDesc = ""
longDesc = """
Thermochemistry for Pynta with H298 and S298 from BEEF-vdW using Harmonic assumptions on Li110 using Simple Reaction Error Cancelling Schemes
Cp data is taken from surfaceThermoPt111
"""
entry(
    index = 1,
    label = "vacant",
    molecule =
"""
1 X u0 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             0.000000000E+00,   0.000000000E+00,   0.000000000E+00,   0.000000000E+00,
             0.000000000E+00,   0.000000000E+00,   0.000000000E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             0.000000000E+00,   0.000000000E+00,   0.000000000E+00,   0.000000000E+00,
             0.000000000E+00,   0.000000000E+00,   0.000000000E+00], Tmin=(1000.0,'K'), Tmax=(3000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (3000.0, 'K'),
    ),
    metal = "Li",
    facet = "110",
)

entry(
    index = 2,
    label = "HX",
    molecule =
"""
1 X u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.49222,-0.0248622,0.000156469,-3.19754e-07,2.2211e-10,-7275.62,-5.29516], Tmin=(10,'K'), Tmax=(459.908,'K')), NASAPolynomial(coeffs=[0.0569449,0.00612859,-4.97169e-06,1.76395e-09,-2.27644e-13,-7339.33,-1.61358], Tmin=(459.908,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K'), E0=(-60.4935,'kJ/mol'), Cp0=(10.4048,'J/(mol*K)'), CpInf=(24.3158,'J/(mol*K)')),
    longDesc = u"""Used H2 + 2X => 2 HX""",
    metal = "Li",
    facet = "110",
)

entry(
    index = 2,
    label = "FX",
    molecule =
"""
1 X u0 p0 c0 {2,S}
2 F u0 p3 c0 {1,S}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.50565,-0.0185736,0.000129335,-3.00079e-07,2.35921e-10,-68044.4,-9.56038], Tmin=(10,'K'), Tmax=(411.404,'K')), NASAPolynomial(coeffs=[1.83169,0.00277731,-2.46573e-06,9.30911e-10,-1.25477e-13,-68114.2,-8.42952], Tmin=(411.404,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K'), E0=(-565.748,'kJ/mol'), Cp0=(19.4659,'J/(mol*K)'), CpInf=(24.7538,'J/(mol*K)')), 
    longDesc = u"""Used F2 + 2X => 2 FX""",
    metal = "Li",
    facet = "110",
)

entry(
    index = 3,
    label = "O=X",
    molecule =
"""
1 X u0 p0 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.50565,-0.0185736,0.000129335,-3.00079e-07,2.35921e-10,-70781.2,-10.9592], Tmin=(10,'K'), Tmax=(411.404,'K')), NASAPolynomial(coeffs=[1.83169,0.00277731,-2.46573e-06,9.30911e-10,-1.25477e-13,-70851,-9.82833], Tmin=(411.404,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K'), E0=(-588.503,'kJ/mol'), Cp0=(19.4659,'J/(mol*K)'), CpInf=(24.7538,'J/(mol*K)')),    
    longDesc = u"""Used O2 + 2X => 2 O=X""",
    metal = "Li",
    facet = "110",
)

entry(
    index = 4,
    label = "OX",
    molecule =
"""
1 X u0 p0 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[4.30087,-0.0267655,0.000181442,-4.08695e-07,3.11012e-10,-60381.4,-18.9524], Tmin=(10,'K'), Tmax=(429.065,'K')), NASAPolynomial(coeffs=[3.59746,0.00272646,-1.83914e-06,6.58692e-10,-9.00975e-14,-60532.1,-18.6141], Tmin=(429.065,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K'), E0=(-502.035,'kJ/mol'), Cp0=(33.6497,'J/(mol*K)'), CpInf=(46.0242,'J/(mol*K)')),    
    longDesc = u"""Used H2O + 2X => HOX + HX""",
    metal = "Li",
    facet = "110",
)

entry(
    index = 5,
    label = "N#X",
    molecule =
"""
1 X u0 p0 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.25331,-0.0251248,0.000173476,-3.98588e-07,3.10612e-10,-14324.1,-8.83576], Tmin=(10,'K'), Tmax=(414.234,'K')), NASAPolynomial(coeffs=[1.28051,0.00401087,-3.51617e-06,1.3163e-09,-1.76413e-13,-14412.9,-7.04436], Tmin=(414.234,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K'), E0=(-119.09,'kJ/mol'), Cp0=(16.8758,'J/(mol*K)'), CpInf=(24.6591,'J/(mol*K)')),    
    longDesc = u"""Used N2 + 2X => 2 NX""",
    metal = "Li",
    facet = "110",
)

entry(
    index = 6,
    label = "CC#X",
    molecule =
"""
1 X u0 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S} 
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[6.11001,-0.0415887,0.000238604,-4.29989e-07,2.69555e-10,10276.6,-26.2267], Tmin=(10,'K'), Tmax=(484.867,'K')), NASAPolynomial(coeffs=[1.49191,0.0177524,-1.06939e-05,3.14203e-09,-3.5937e-13,10474.7,-9.86497], Tmin=(484.867,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K'), E0=(85.4499,'kJ/mol'), Cp0=(47.1245,'J/(mol*K)'), CpInf=(113.506,'J/(mol*K)')),    
    longDesc = u"""Used N#CC + 2X => N#X + CC#X""",
    metal = "Li",
    facet = "110",
)

entry(
    index = 6,
    label = "XOC[=O]OX",
    molecule =
"""
1 X u0 p0 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 O u0 p2 c0 {3,D}
5 O u0 p2 c0 {3,S} {6,S}
6 X u0 p0 c0 {5,S}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[6.76894,-0.039618,0.00022937,-4.16434e-07,2.56995e-10,-131204,-25.3197], Tmin=(10,'K'), Tmax=(512.853,'K')), NASAPolynomial(coeffs=[3.54376,0.0139739,-1.0549e-05,3.55937e-09,-4.43134e-13,-131248,-15.5597], Tmin=(512.853,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K'), E0=(-1090.9,'kJ/mol'), Cp0=(52.7942,'J/(mol*K)'), CpInf=(89.2455,'J/(mol*K)')),    
    longDesc = u"""Used O=C1OCCO1+ 2X => C2H4 + XOC[=O]OX""",
    metal = "Li",
    facet = "110",
)