#!/usr/bin/env python
# encoding: utf-8

name = "Cyclic_Thioether_Formation/rules"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 812,
    label = "RnSS;Y_rad_intra;SS_intra",
    kinetics = ArrheniusEP(
        A = (1e+11, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (10, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
)

