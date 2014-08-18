#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/Hexanethial_nr"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "C6H12SHOH <=> C6H12O + H2S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.43e+14, 's^-1'), n=-0.41, Ea=(44.42, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
First one should be 36.30 kcal/mol, second 44.42 kcal/mol
C6H12O + H2S = C6H12SHOH    6.13E+01    2.77    36.30    0.0    0.0    0.0
""",
)

entry(
    index = 2,
    label = "C5H11COHS <=> C5H11COSH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.1e+12, 's^-1'), n=0.13, Ea=(28.48, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Correct value of next reaction is in R_Addition_MultipleBond
C5H11COHS + HJ = C5H11CJOHSH    1.18E+09    1.15    -0.06    0.0    0.0    0.0
""",
)

entry(
    index = 3,
    label = "C5H11J + COS <=> C5H11COSJ",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (603000, 'cm^3/(mol*s)'),
        n = 1.83,
        Ea = (11.84, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 4,
    label = "CHOHS + C5H11J <=> C6H12OHSJ",
    degeneracy = 1,
    kinetics = Arrhenius(A=(774, 'cm^3/(mol*s)'), n=2.56, Ea=(3.56, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 5,
    label = "C4H9CHJCHOHSH <=> SH + hexen-1-ol",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.01e+12, 's^-1'), n=0.13, Ea=(4.99, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
reverse of next reaction is in R_Addition_MultipleBond library:
""",
)

entry(
    index = 6,
    label = "hexen-1-ol <=> C6H12O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.32e-33, 's^-1'), n=12.94, Ea=(31.33, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "CO + H2O <=> CO2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5000, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Approx water gas shift reaction
""",
)

