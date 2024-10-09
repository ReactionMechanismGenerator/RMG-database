#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond_Disprop/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "C3H4LiO3 + Li <=> CLi2O3 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.82969e+15,'m^3/(mol*s)'), n=-2.51461, Ea=(7.6717,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1000,'K'), comment="""Fitted to 50 data points; dA = *|/ 3.36722, dn = +|- 0.167182, dEa = +|- 0.694638 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OC(=O)OC[CH2] + [Li] <=> C=C + [Li]OC(=O)O[Li]
TS method summary for TS1 in [Li]OC(=O)OC[CH2] + [Li] <=> C=C + [Li]OC(=O)O[Li]:
Computed using CVTST
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)
""",
)

entry(
    index = 2,
    label = "C3H4LiO3 + C2H5 <=> C3H5LiO3-2 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.60363e+10,'m^3/(mol*s)'), n=-1.06749, Ea=(2.37772,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1000,'K'), comment="""Fitted to 50 data points; dA = *|/ 2.80611, dn = +|- 0.142081, dEa = +|- 0.590342 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OC(=O)OC[CH2] + C[CH2] <=> C=C + [Li]OC(=O)OCC
TS method summary for TS5 in [Li]OC(=O)OC[CH2] + C[CH2] <=> C=C + [Li]OC(=O)OCC:
Computed using CVTST
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)
""",
)

