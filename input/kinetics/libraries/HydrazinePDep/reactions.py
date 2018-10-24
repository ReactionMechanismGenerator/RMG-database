#!/usr/bin/env python
# encoding: utf-8

name = "HydrazinePDep"
shortDesc = u"HydrazinePDep"
longDesc =u"""
This library includes well-skipping pressure-dependent reactions on the N3H3, N3H5 and N4H6 PESs
Calculated by alongd at CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)
Using the modified strong collision method

opt, freq: wB97x-D3/6-311++G(3df,3pd)
sp: CCSD(T)-F12a/aug-cc-pVTZ
rotors: B3LYP/6-311++G(3df,3pd)
Each TS was traced with an IRC calculation in both direction to verify adjacent wells
"""

entry(
    index = 1,
    label = "N2H3 + NH2 <=> H2NN(S) + NH3",
    duplicate = True,
    kinetics = Chebyshev(
        coeffs = [
            [5.99733, -1.25278, -0.138491, 0.0112705],
            [1.20942, 0.91757, -0.0517129, -0.0366242],
            [0.087011, 0.27912, 0.073579, -0.0228933],
            [-0.0798328, -0.00734786, 0.052327, 0.00771303],
            [-0.0439692, -0.049873, 0.00687501, 0.0126567],
            [-0.011542, -0.0213651, -0.00890094, 0.0038924],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
    ),
)

entry(
    index = 2,
    label = 'N2H3 + NH2 <=> H2NN(S) + NH3',
    duplicate = True,
    kinetics = Arrhenius(A=(1.03+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""estimated""",
    longDesc =
u"""
This is the direct non-PDep route.
Estimated by alongd as having the same A factor as 'N2H3 + NH2 <=> H2NN(T) + NH3' with Ea = 0 (barrierless)
The A factor was refitted into a classical (non-modified) Arrhenius form:
Arrhenius(A=(1.03198e+12,'cm^3/(mol*s)'), n=0, Ea=(20.0354,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'),
Fitted to 51 data points; dA = *|/ 1.18263, dn = +|- 0, dEa = +|- 1.27006 kJ/mol
Note that the 'N2H3 + NH2 <=> H2NN(T) + NH3' reaction has a barrier of ~5 kJ/mol in the forward direction although
it's Ea in the modified Arrhenius form is negative: Arrhenius(A=(1.65e+00, 'cm^3/(mol*s)'), n=3.41, Ea=(-4.0, 'kJ/mol')
""",
)

entry(
    index = 3,
    label = "N2H3 + NH2 <=> N2H2 + NH3",
    duplicate = True,
    kinetics = Chebyshev(
        coeffs = [
            [2.88998, -1.10761, -0.173345, 0.0166179],
            [2.51639, 0.898096, 0.00518803, -0.0532882],
            [0.209791, 0.207873, 0.0930165, -0.011894],
            [-0.0215097, -0.036282, 0.0388755, 0.0172118],
            [-0.0220245, -0.0485522, -0.00566483, 0.0117104],
            [-0.00409225, -0.0151944, -0.0112795, 0.000190639],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
    ),
)

entry(
    index = 4,
    label = "N2H3 + NH2 <=> N2H2 + NH3",
    duplicate = True,
    kinetics = Arrhenius(A = (9.2e+05, 'cm^3/(mol*s)'), n = 1.94, Ea = (-1.152, 'kcal/mol'), T0 = (1, 'K')),
    longDesc =
u"""
Taken from the Nitrogen_Dean_and_Bozzelli library
The same rate appears in the NOx2018 library
D&B estimated this rate of the direct hydrogen transfer reaction (not including the well-skipping rate)
""",
)