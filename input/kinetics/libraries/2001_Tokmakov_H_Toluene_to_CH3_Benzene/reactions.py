#!/usr/bin/env python
# encoding: utf-8

name = "2001_Tokmakov_H_Toluene_to_CH3_Benzene"
shortDesc = u"Cantherm computed T,P-dependent rates using quantum calcs of 2001 Tokmakov for H + Toluene = CH3 + Benzene"
longDesc = u"""
Computed T,P-dependent k's for the methyl-hydrogen exchange reaction of toluene (H + Toluene = CH3 + Benzene)
using Cantherm and the molecular properties computed with G2M(cc,MP2)//B3LYP/6-311++G(3df,2p) from:
I.V. Tokmakov and M.C. Lin,
"Kinetics and Mechanism for the H-for-X Exchange Process in the H+C6H5X Reactions: A Computational Study",
Int. J. Chem. Kin., Vol. 33, Iss. 11, November 2001, Pages 633-653
Calculated for an N2 bath gas
"""
entry(
    index = 1,
    label = "C6H5CH3 + H <=> ipso-(C7H9)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [10.3, 0.4378, -0.06555, 0.0005308],
            [1.278, 0.6505, -0.06177, -0.01036],
            [-0.2451, 0.2798, 0.02277, -0.01323],
            [-0.1451, 0.06763, 0.03706, -0.002604],
            [-0.07194, 0.007107, 0.01811, 0.003786],
            [-0.03465, -0.005259, 0.005851, 0.003213],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (0.1, 'atm'),
        Pmax = (100, 'atm'),
    ),
)

entry(
    index = 2,
    label = "ipso-(C7H9) <=> C6H6 + CH3",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [4.9, 0.3872, -0.05504, -0.0009308],
            [5.716, 0.6158, -0.06469, -0.007937],
            [-0.3614, 0.3125, 0.005812, -0.01142],
            [-0.208, 0.09791, 0.03132, -0.004837],
            [-0.09645, 0.01443, 0.02134, 0.001782],
            [-0.04212, -0.006098, 0.008707, 0.002987],
        ],
        kunits = 's^-1',
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (0.1, 'atm'),
        Pmax = (100, 'atm'),
    ),
)

entry(
    index = 3,
    label = "C6H5CH3 + H <=> C6H6 + CH3",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.422, -0.9213, -0.08453, 0.000839],
            [3.45, 0.7276, -0.0409, -0.0175],
            [0.04877, 0.174, 0.05977, -0.01032],
            [-0.005075, -0.01084, 0.03801, 0.006718],
            [0.03466, -0.004496, 0.004886, 0.006774],
            [0.006253, 0.001523, -0.0008725, 0.001804],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (0.1, 'atm'),
        Pmax = (100, 'atm'),
    ),
)

