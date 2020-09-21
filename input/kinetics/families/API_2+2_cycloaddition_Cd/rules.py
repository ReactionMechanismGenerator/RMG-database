#!/usr/bin/env python
# encoding: utf-8

name = "API_2+2_cycloaddition_Cd/rules"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "db;doublebond",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (1.05605e+06, 'cm^3/(mol*s)'),
        n = 1.86,
        alpha = 0,
        E0 = (232.89994, 'kJ/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = """Zalotai et al. 1983""",
    longDesc = """
Kinetics fitted from reverse direction using rate of 

C3H6O <=> C2H4 + CH2O, low or high pressure extrapolation with thermal excitation technique, taken from 

Zalotai, L. et al, Kinetics of gas phase decomposition of oxetan and oxetan-2,2-d2, Int. J. Chem. Kinet., 15, 505, 1983
http://kinetics.nist.gov/kinetics/Detail?id=1983ZAL/HUN505:1 """
)

