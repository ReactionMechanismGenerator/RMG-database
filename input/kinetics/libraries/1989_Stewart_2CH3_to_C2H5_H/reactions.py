#!/usr/bin/env python
# encoding: utf-8

name = "1989_Stewart_2CH3_to_C2H5_H"
shortDesc = u"Chemically Activated Methyl Recombination to Ethyl + H from 1989 Stewart Calculations"
longDesc = u"""
Chebyshev fit to the T,P-dependent k for 2CH3 = C2H5 + H from:
P.H. Stewart, et al.,
"Pressure and Temperature Dependence of Reactions Proceeding Via A Bound Complex. 2. Application to 2CH3 -> C2H5 + H",
Combustion and Flame 75: 25-31 (1989)
The k computed by Stewart that we fit was for a "strong collider" because "weak collider" correction they provide is only valid to 900 K
"""
entry(
    index = 0,
    label = "CH3 + CH3 <=> C2H5 + H",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.267, -0.5559, -0.2081, -0.02475],
            [3.774, 0.482, 0.1485, -0.005274],
            [0.06503, 0.08914, 0.05444, 0.01846],
            [-0.01057, -0.01794, 0.005877, 0.0101],
            [-0.006027, -0.01206, -0.002669, 0.002541],
            [-0.002256, -0.006865, -0.005809, -0.002549],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        Pmin = (0.001, 'atm'),
        Pmax = (10, 'atm'),
    ),
)

