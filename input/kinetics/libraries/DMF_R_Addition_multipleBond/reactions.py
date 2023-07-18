#!/usr/bin/env python
# encoding: utf-8

name = "DMF_R_Addition_multipleBond_kinetics"
shortDesc = u"DMF_R_Addition_multipleBond"
longDesc = u"""

"""

entry(
    index = 0,
    label = "H_rad + DMF <=> CC1=C[CH]C(C)O1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (431195000, 'cm^3/(mol*s)'),
        n = 1.53,
        Ea = (2.9754015296e+03, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1,
    label = "H_rad + DMF <=> C[C]1CC=C(C)O1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4246600, 'cm^3/(mol*s)'),
        n = 1.98,
        Ea = (3.4996367113e+03, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

