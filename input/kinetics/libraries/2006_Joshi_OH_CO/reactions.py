#!/usr/bin/env python
# encoding: utf-8

name = "2006_Joshi_OH_CO"
shortDesc = u"Computed rates on OH + CO = HOCO = H + CO2 surface"
longDesc = u"""
Chebyshev fit to T,P-dependent k's calculated with CCSD(T)/cc-pvTZ for the small OH + CO surface by:
A.V. Joshi and H. Wang,
"Master equation modeling of wide range temperature and pressure dependence of CO + OH -> Products'
Int. J. Chem. Kin., Vol. 38, Iss. 1, January 2006, Pages 57-73
The surface includes OH+CO, HOCO and H+CO2 only.
Calculated for an N2/Ar bath gas
"""
entry(
    index = 0,
    label = "OH + CO <=> HOCO",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.415, 2.41, -0.2151, -0.05592],
            [-1.187, 0.4925, 0.226, 0.03057],
            [-0.4109, -0.01515, 0.0145, 0.02892],
            [-0.141, -0.0386, -0.01717, 0.004195],
            [-0.03786, -0.02215, -0.01361, 0.00278],
            [-0.03699, 0.01123, 0.0004769, -0.01677],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        Pmin = (0.001, 'atm'),
        Pmax = (641.5, 'atm'),
    ),
)

entry(
    index = 1,
    label = "OH + CO <=> H + CO2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [10.89, -0.4346, -0.2152, -0.05574],
            [0.6535, 0.4928, 0.2262, 0.03006],
            [0.2008, -0.01527, 0.01434, 0.02917],
            [0.07196, -0.03864, -0.01717, 0.00435],
            [0.02016, -0.02204, -0.01345, 0.002451],
            [0.01154, 0.01113, 0.0004633, -0.01646],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        Pmin = (0.001, 'atm'),
        Pmax = (641.5, 'atm'),
    ),
)

