#!/usr/bin/env python
# encoding: utf-8

name = "computationalLithiumElectrode"
shortDesc = u"computational lithium electrode"
longDesc = u"""
This library uses the computational lithum electrode model where
Li+ + e- = Li(s) @ -3.04 V vs SHE

If using this library, the potential in your input file
will be referenced to the Li/Li+ electrode (not SHE)
For example, if you set your reactor potential to O V,
that would be -3.04 V vs SHEs
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
)

entry(
    index = 2,
    label = "electron",
    molecule =
"""
1 e u0 p0 c-1
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
)

entry(
    index = 3,
    label = "Li_ion",
    molecule =
"""
1 Li u0 p0 c+1
""",
    thermo = ThermoData(
        Tdata=([300,400,500,600,800,1000,1500],'K'), 
        Cpdata=([24.67,27.61,27.61,27.61,27.61,27.61,27.61],'J/(mol*K)'), 
        H298=(0,'kcal/mol'), S298=(29.12, 'J/(mol*K)','+|-',0.2),
        comment = 'Li(s)'),
    shortDesc = u"""""",
    longDesc = 
u"""
Li+ + e- = Li(s) @ -3.04 V vs SHE
S, Cp300, Cp400 for Li(s) from NIST
https://webbook.nist.gov/cgi/cbook.cgi?ID=C7439932&Units=SI&Mask=2&Type=JANAFS&Table=on#JANAFS
Cp > 400K approximated as Cp400
""",
)