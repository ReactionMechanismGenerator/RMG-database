#!/usr/bin/env python
# encoding: utf-8

name = "Aromatics_high_pressure/C9H11"
shortDesc = u"Phenyl radical propene addition and H-abstraction"
longDesc = u"""
Phenyl radical + propene: a prototypical reaction surface for aromatic-catalyzed 1,2-hydrogenmigration and subsequent resonance-stabilized radical formation
Zachary J. Buras, Te-Chun Chu, Adeel Jamal, Nathan W. Yee, Joshua E. Middaugh and William H. Green
Phys. Chem. Chem. Phys., 2018,20, 13191-13214

Adapt surface calculated by Kislov et al. at the G3(MP2,CC)//B3LYP/6-311G** level theory, and add new found aromatic-catalyzed pathway. Arkane was used to calculate TST rates.
"""
entry(
    index = 0,
    label = "C6H5 + C3H6 <=> C6H6 + CH3CHCH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.00551, 'cm^3/(mol*s)'),
        n = 4.401,
        Ea = (4.745, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1,
    label = "C6H5 + C3H6 <=> C6H6 + CH3CCH2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.06725, 'cm^3/(mol*s)'),
        n = 4.149,
        Ea = (3.361, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2,
    label = "C6H5 + C3H6 <=> C6H6 + CH2CHCH2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.2601, 'cm^3/(mol*s)'),
        n = 4.002,
        Ea = (1.735, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 3,
    label = "C6H5 + C3H6 <=> i1",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3132, 'cm^3/(mol*s)'), n=2.668, Ea=(0.41, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 4,
    label = "C6H5 + C3H6 <=> i2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (681.8, 'cm^3/(mol*s)'),
        n = 2.75,
        Ea = (2.279, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 5,
    label = "i1 <=> i3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.597e+08, 's^-1'), n=0.953, Ea=(15.885, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 6,
    label = "i2 <=> i3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.732e+09, 's^-1'), n=0.671, Ea=(15.317, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 7,
    label = "i1 <=> i4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.68e-11, 's^-1'), n=6.833, Ea=(28.023, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 8,
    label = "i1 <=> i6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.329e-13, 's^-1'), n=6.797, Ea=(28.919, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 9,
    label = "i1 <=> i7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.842e-10, 's^-1'), n=6.38, Ea=(25.872, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 10,
    label = "i1 <=> p2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.532e+07, 's^-1'), n=1.831, Ea=(34.3, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 11,
    label = "i1 <=> p3 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.133e+08, 's^-1'), n=1.389, Ea=(34.424, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 12,
    label = "i2 <=> i8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.162e+09, 's^-1'), n=0.771, Ea=(31.613, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 13,
    label = "i2 <=> i9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.414e-06, 's^-1'), n=5.188, Ea=(22.253, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 14,
    label = "i2 <=> i10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.03778, 's^-1'), n=4.026, Ea=(36.559, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 15,
    label = "i2 <=> p1 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.169e+10, 's^-1'), n=0.925, Ea=(28.785, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 16,
    label = "i2 <=> p4 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.145e+09, 's^-1'), n=1.255, Ea=(34.391, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 17,
    label = "i4 <=> i5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.066e+08, 's^-1'), n=0.949, Ea=(16.873, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 18,
    label = "i4 <=> p2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.77e+08, 's^-1'), n=1.506, Ea=(35.156, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 19,
    label = "i5 <=> i11",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.255e+12, 's^-1'), n=0.347, Ea=(57.413, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 20,
    label = "i5 <=> p5 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.595e+09, 's^-1'), n=1.097, Ea=(22.941, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 21,
    label = "i6 <=> p2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.6e+09, 's^-1'), n=1.106, Ea=(25.978, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 22,
    label = "i7 <=> p1 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.276e+11, 's^-1'), n=0.842, Ea=(35.998, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 23,
    label = "i7 <=> p3 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.757e+10, 's^-1'), n=1.083, Ea=(40.433, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 24,
    label = "i8 <=> p7 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.37e+13, 's^-1'), n=0.61, Ea=(48.173, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 25,
    label = "i8 <=> p8 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.945e+09, 's^-1'), n=1.096, Ea=(26.664, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 26,
    label = "i10 <=> p4 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.086e+10, 's^-1'), n=0.921, Ea=(25.035, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 27,
    label = "i1 <=> inew",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.478, 's^-1'), n=3.436, Ea=(23.671, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 28,
    label = "inew <=> i4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(721.5, 's^-1'), n=2.46, Ea=(3.681, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 29,
    label = "i4 <=> benzyl + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.39e+09, 's^-1'), n=1.1, Ea=(22.881, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

