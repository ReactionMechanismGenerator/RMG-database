#!/usr/bin/env python
# encoding: utf-8

name = "primaryNitrogenLibrary/LowT"
shortDesc = u"Low T nitrogen reactions"
longDesc =u"""
This library includes low temperature kinetics for reactions included in the primaryNitrogenLibrary
For low temperature applications, this library should precede and used conjointly with the primaryNitrogenLibrary
"""

entry(
    index = 1,
    label = "N2O + OH <=> N2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.87e+08, 'cm^3/(mol*s)'), n=0, Ea=(20436, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(300, 'K'), Tmax=(1000, 'K')),
    shortDesc = u"""[Lin1996b]""",
    longDesc =
u"""
Part of the "N2O Pathway"
k2A on p. 702
T range: 300-1000 K (also available at 1000-5000 K)
calculations done at the B3LYP/6-311G(d,p)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 2,
    label = "N2H4 + NO3 <=> HONO + N2H3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.10e+18, 'cm^3/(mol*s)'), n=-1.84, Ea=(-642, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(300, 'K'), Tmax=(1000, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
p. 269
T range: 300-1000 K (also available at 1000-3000 K)
calculations done at the CCSD(T)//BHandHLYP/6-311þþG(3df,2p) level of theoty
Pressure independent at least up to 100 atm

A different rate for the same reaction is available from the same author (M.C. Lin) published in the same year...: [Lin2014a]
But this [Lin2014a] rate is a O(2) lower at 1500 K:
    kinetics = Arrhenius(A=(2.04e+03, 'cm^3/(mol*s)'), n=2.59, Ea=(5612, 'cal/mol'), T0=(1, 'K')),
T range: 1000-2000 K
    kinetics = Arrhenius(A=(1.63e+11, 'cm^3/(mol*s)'), n=0.20, Ea=(2180, 'cal/mol'), T0=(1, 'K')),
T range: 300-1000 K
[Lin2014a] reaction (7), p. 79
calculations done at the CCSD(T)/CBS//CCSD level of theoty,
and the moment of inertia and harmonic vibrational frequencies were obtained by the CCSD/6-31G(d,p) level
""",
)

entry(
    index = 3,
    label = "N2H3 + NO2 <=> N2H2 + HONO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.99e+46, 'cm^3/(mol*s)'), n=-11.8, Ea=(6055, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(300, 'K'), Tmax=(800, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
k5, p. 278
T range: 300-800 K (also available at 800-3000 K), P = 1 atm
calculations done at the CCSD(T)/6-311++G(3df,2p)//B3LYP/6-311++G(3df,2p) level of theoty
""",
)

entry(
    index = 4,
    label = "N2H3 + NO2 <=> N2H2 + HNO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.07e+08, 'cm^3/(mol*s)'), n=0.5, Ea=(-2395, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(300, 'K'), Tmax=(1500, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
k7 p. 278
T range: 300-1500 K (also available at 1500-3000 K), P = 1 atm
calculations done at the CCSD(T)/6-311++G(3df,2p)//B3LYP/6-311++G(3df,2p) level of theoty
""",
)

entry(
    index = 5,
    label = "N2H3 + NO2 <=> N2H3O + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.08e+20, 'cm^3/(mol*s)'), n=-2.9, Ea=(792.3, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(300, 'K'), Tmax=(1000, 'K')),
    shortDesc = u"""[Lin2014b]""",
    longDesc =
u"""
Part of the "N2H4 + N2O4" subset
k6, p. 278
T range: 300-1000 K (also available at 1000-3000 K), P = 1 atm
calculations done at the CCSD(T)/6-311++G(3df,2p)//B3LYP/6-311++G(3df,2p) level of theoty
""",
)

entry(
    index = 6,
    label = "HCO + HNO <=> HNOH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.16e+08, 'cm^3/(mol*s)'), n=1.19, Ea=(914, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(400, 'K'), Tmax=(1000, 'K')),
    shortDesc = u"""[Lin2004]""",
    longDesc =
u"""
Part of the "NOx" subset
T range: 400-1000 K (also available at 200-400 K as well as 1000-3000 K)
calculations done at the G2M//BH&HLYP/6-311G(d, p) level of theory
k4(HNOH+CO), p. 213
""",
)

entry(
    index = 61,
    label = "CN + NCO <=> NCN + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.29e+13, 'cm^3/(mol*s)'), n=0.155, Ea=(129, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(200, 'K'), Tmax=(1000, 'K')),
    shortDesc = u"""[Lin2009b]""",
    longDesc =
u"""
Several levels of theory were used:
G2M//B3LYP/6-311+G(d), QCISD(T)/6-311+G(3df)//QCISD/6-311+G(d), CCSD(T)/6-311+G(3df)//CCSD/6-311+G(d),
CASPT2(10,10)/6-311+G(d)//CAS(10,10)/6-311+G(d).
""",
)
