#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/DMDS"
shortDesc = u"dimethyl disulfide library"
longDesc = u"""
Sulfur library originally created by Caleb in RMG-Java. No mention of source of kinetics in Java git commits.
"""
entry(
    index = 1,
    label = "C2H5SJ1 <=> C2H5SJ2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(85.5, 's^-1'), n=3.04, Ea=(11.62, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
small molecule oxidation library, reaction file, version 2, JS, August 6, 2003
originally from Leeds methane oxidation mechanism v1.5
http://www.chem.leeds.ac.uk/Combustion/Combustion.html
fix bug for O2 + HCO = HO2 + CO 1.52E13 0.00 -7.09, change E into positive, change A into 5.12E13 according to NIST




Ontbinding DMDS
""",
)

entry(
    index = 2,
    label = "C2H4 + SH <=> C2H5SJ2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9960, 'cm^3/(mol*s)'), n=2.7, Ea=(-0.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "Sa + Sa <=> S2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+11, 'cm^3/(mol*s)'),
        n = 1.3,
        Ea = (-0.88, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

