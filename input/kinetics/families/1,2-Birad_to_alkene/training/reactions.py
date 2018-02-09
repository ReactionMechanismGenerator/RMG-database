#!/usr/bin/env python
# encoding: utf-8

name = "1,2-Birad_to_alkene/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""

"""

entry(
    index = 1,
    label = "SO2(T) => SO2(S)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.0e+10, 's^-1'), n=0, Ea=(0, 'kcal/mol')),
    rank = 1,
    shortDesc = u"""""",
    longDesc =
u"""
taken from:
F.B. Wampler, K. Otsuka, J.G. Calvert, E.K. Damon, Int. J. Chem. Kin., 1973, 5(4), 669-690, doi: 10.1002/kin.550050417
and adjusted to a first order reaction at 1 atm
Similar rates were determined by:
T.N. Rao, S.S. Collier, J.G. Calvet, JACS, 1969, 91(7), 1616-1612, doi: 10.1021/ja01035a006
""",
)
