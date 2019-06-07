#!/usr/bin/env python
# encoding: utf-8

name = "intra_NO2_ONO_conversion/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "C2H5NO2 <=> C2H5ONO",
    degeneracy = 1,
    rank = 8,
    kinetics = Arrhenius(A=(2.1e+10, 's^-1'), n=1, Ea=(60660, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""From kinetic library NOx2018""",
    longDesc =
u"""
Ea calculation at B3LYP/6-31+G(d) is taken from:
Q. Wang., D. Ng, M.S. Mannan, Ind. Eng. Chem. Res. 2009, 48(18), 8745-8751, doi: 10.1021/ie900849n

Rate expression including the frequency factor is given by:
P. Glarborg, J.A. Miller, B. Ruscic, S.J. Klippenstein
Modeling nitrogen chemistry in combustion
Progress in Energy and Combustion Science
Volume 67, July 2018, Pages 31-68
https://doi.org/10.1016/j.pecs.2018.01.002
""",
)
