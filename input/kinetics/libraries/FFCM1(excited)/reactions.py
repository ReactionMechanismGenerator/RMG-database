#!/usr/bin/env python
# encoding: utf-8

name = "FFCM1(excited)"
shortDesc = u""
longDesc = u"""
Foundational Fuel Chemistry Model Version 1.0 (excited species removed)
http://web.stanford.edu/group/haiwanglab/FFCM1/pages/FFCM1.html

FFCM-1
H2/CO/C1 reaction model - Chemkin form - version v1.0c
Release date: 05/31/3016.

G. P. Smith, Y. Tao, and H. Wang, Foundational Fuel Chemistry Model Version 1.0 (FFCM-1),
http://nanoenergy.stanford.edu/ffcm1, 2016.

This library contains only reactions from FFCM-1 involving excited species (CH*, OH*)

Note that some reactions in this library are irreversible; consider setting 'keepIrreversible = True' under 'options' in your input file
"""

entry(
    index = 1,
    label = "CH + O2 <=> CO + OH*",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.80E+11,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "C2H + O <=> CO + CH*",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.50E+12,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "C2H + O2 <=> CO2 + CH*",
    degeneracy = 1,
    kinetics=Arrhenius(A=(3.20E+11,'cm^3/(mol*s)'), n=0, Ea=(1600,'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "H + O => OH*",
    degeneracy = 1,
    kinetics=ThirdBody(arrheniusLow=Arrhenius(A=(5.45E+12,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 5,
    label = "OH + OH + H => OH* + H2O",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.45E+15,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "CH* => CH",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.85E+06,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "CH* + N2 <=> CH + N2",
    degeneracy = 1,
    kinetics=Arrhenius(A=(3.03E+02,'cm^3/(mol*s)'), n=3.40, Ea=(-381,'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 8,
    label = "CH* + O2 <=> CH + O2",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.40E+06,'cm^3/(mol*s)'), n=2.14, Ea=(-1720,'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 9,
    label = "CH* + H2O <=> CH + H2O",
    degeneracy = 1,
    kinetics=Arrhenius(A=(5.30E+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 10,
    label = "CH* + H2 <=> CH + H2",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.47E+14,'cm^3/(mol*s)'), n=0, Ea=(1361,'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 11,
    label = "CH* + CO2 <=> CH + CO2",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.41E-01,'cm^3/(mol*s)'), n=4.30, Ea=(-1694,'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 12,
    label = "CH* + CO <=> CH + CO",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.44E+12,'cm^3/(mol*s)'), n=0.50, Ea=(0,'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "CH* + CH4 <=> CH + CH4",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.73E+13,'cm^3/(mol*s)'), n=0, Ea=(167,'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 14,
    label = "CH* + Ar <=> CH + Ar",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.25E+10,'cm^3/(mol*s)'), n=0.50, Ea=(0,'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 15,
    label = "CH* + He <=> CH + He",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.95E+09,'cm^3/(mol*s)'), n=0.50, Ea=(0,'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 16,
    label = "OH* => OH",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.45E+06,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 17,
    label = "OH* + N2 <=> OH + N2",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.08E+11,'cm^3/(mol*s)'), n=0.50, Ea=(-1238,'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 18,
    label = "OH* + O2 <=> OH + O2",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.10E+12,'cm^3/(mol*s)'), n=0.50, Ea=(-482,'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 19,
    label = "OH* + H2O <=> OH + H2O",
    degeneracy = 1,
    kinetics=Arrhenius(A=(5.92E+12,'cm^3/(mol*s)'), n=0.50, Ea=(-861,'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 20,
    label = "OH* + H2 <=> OH + H2",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.95E+12,'cm^3/(mol*s)'), n=0.50, Ea=(-444,'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 21,
    label = "OH* + CO2 <=> OH + CO2",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.75E+12,'cm^3/(mol*s)'), n=0.50, Ea=(-968,'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 22,
    label = "OH* + CO <=> OH + CO",
    degeneracy = 1,
    kinetics=Arrhenius(A=(3.23E+12,'cm^3/(mol*s)'), n=0.50, Ea=(-787,'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 23,
    label = "OH* + CH4 <=> OH + CH4",
    degeneracy = 1,
    kinetics=Arrhenius(A=(3.36E+12,'cm^3/(mol*s)'), n=0.50, Ea=(-635,'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 24,
    label = "OH* + Ar <=> OH + Ar",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.25E+12,'cm^3/(mol*s)'), n=0.50, Ea=(0,'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 25,
    label = "OH* + He <=> OH + He",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.95E+09,'cm^3/(mol*s)'), n=0.50, Ea=(0,'cal/mol'), T0=(1, 'K')),
)

