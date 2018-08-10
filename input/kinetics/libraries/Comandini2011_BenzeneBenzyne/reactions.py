#!/usr/bin/env python
# encoding: utf-8

name = "Comandini2011_BenzeneBenzyne"
shortDesc = u"Naphthalene formation from o-benzyne and benzene"
longDesc = u"""
Calculated using uCCSD(T) method and cc-pVDZ basis set.

Citation:

Andrea Comandini and Kenneth Brezinsky, Theoretical Study of 
the Formation of Naphthalene from the Radical/π-Bond Addition 
between Single-Ring Aromatic Hydrocarbons, J. Phys. Chem. A 
2011, 115, 5547–5559, dx.doi.org/10.1021/jp200201c
"""
entry(
    index = 1,
    label = "C6H6 + oC6H4 <=> C12H10",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.809e+03, 'cm^3/(mol*s)'),
        n = 2.526,
        Ea = (5.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2,
    label = "C12H10 <=> C10H8 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A=(7.458e+14, 's^-1'), 
        n=0.0956, 
        Ea=(54.82, 'kcal/mol'), 
        T0=(1, 'K')),
)

