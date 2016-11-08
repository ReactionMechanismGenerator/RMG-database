#!/usr/bin/env python
# encoding: utf-8

name = "Ethylamine"
shortDesc = u""
longDesc = u"""
Automated Reaction Mechanism Generation Including Heteroatoms: Nitrogen
Alon Grinberg Dana, Beat Buesser, Shamel S. Merchant, William H. Green
Table 2
Kinetic data for reactions 1–9, 13–24 were calculated using:
CBS-QB3 for energy barriers, B3LYP/6-311G(2d,d,p) for partition functions, hybrid meta-GGA BMK/6-311G(2d,d,p) for addition reactions.

Kinetic data for reactions 10–12 (NCC + OH) were adopted from the literature (VTST):
S. Li, E. Dames, D.F. Davidson, R.K. Hanson
"High-Temperature Measurements of the Reactions of OH with Ethylamine and Dimethylamine"
The Journal of Physical Chemistry A, 2014, 118, 70-77, http://dx.doi.org/10.1021/jp411141w
(with geometries from http://dx.doi.org/10.1021/ct7002786 CCSD(T)/6-311++G(2d,2p) single-point calculations)
"""

entry(
    index = 1,
    label = "NCC + H <=> CH2CH2NH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.07e+04, 'cm^3/(mol*s)'), n=2.75, Ea=(6800, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R1: EA H abstraction""",
)

entry(
    index = 2,
    label = "NCC + H <=> CH3CHNH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.54e+03, 'cm^3/(mol*s)'), n=2.94, Ea=(500, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R2: EA H abstraction""",
)

entry(
    index = 3,
    label = "NCC + H <=> CH3CH2NH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.04e+04, 'cm^3/(mol*s)'), n=2.64, Ea=(5500, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R3: EA H abstraction""",
)

entry(
    index = 4,
    label = "NCC + CH3 <=> CH2CH2NH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.28e-04, 'cm^3/(mol*s)'), n=4.85, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R4: EA H abstraction""",
)

entry(
    index = 5,
    label = "NCC + CH3 <=> CH3CHNH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.76e-02, 'cm^3/(mol*s)'), n=4.23, Ea=(4200, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R5: EA H abstraction""",
)

entry(
    index = 6,
    label = "NCC + CH3 <=> CH3CH2NH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.27e-02, 'cm^3/(mol*s)'), n=4.41, Ea=(4800, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R6: EA H abstraction""",
)

entry(
    index = 7,
    label = "NCC + NH2 <=> CH2CH2NH2 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.44e-02, 'cm^3/(mol*s)'), n=4.43, Ea=(3600, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R7: EA H abstraction""",
)

entry(
    index = 8,
    label = "NCC + NH2 <=> CH3CHNH2 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.28e+00, 'cm^3/(mol*s)'), n=3.75, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R8: EA H abstraction""",
)

entry(
    index = 9,
    label = "NCC + NH2 <=> CH3CH2NH + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.73e-02, 'cm^3/(mol*s)'), n=4.03, Ea=(1900, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R9: EA H abstraction""",
)

entry(
    index = 10,
    label = "NCC + OH <=> CH2CH2NH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.94e+02, 'cm^3/(mol*s)'), n=2.97, Ea=(-1040, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R10: EA H abstraction""",
)

entry(
    index = 11,
    label = "NCC + OH <=> CH3CHNH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.28e+05, 'cm^3/(mol*s)'), n=2.24, Ea=(-3040, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R11: EA H abstraction""",
)

entry(
    index = 12,
    label = "NCC + OH <=> CH3CH2NH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+05, 'cm^3/(mol*s)'), n=2.36, Ea=(-2860, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R12: EA H abstraction""",
)

entry(
    index = 13,
    label = "N2H4 + H <=> N2H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.48e+08, 'cm^3/(mol*s)'), n=1.69, Ea=(4000, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R13: H abstraction""",
)

entry(
    index = 14,
    label = "N2H4 + CH3 <=> N2H3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.77e+01, 'cm^3/(mol*s)'), n=3.60, Ea=(3500, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R14: H abstraction""",
)

entry(
    index = 15,
    label = "N2H4 + NH2 <=> N2H3 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.59e+03, 'cm^3/(mol*s)'), n=2.83, Ea=(700, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R15: H abstraction""",
)

entry(
    index = 16,
    label = "CH3CHNH + H <=> CH2CHNH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.98e+04, 'cm^3/(mol*s)'), n=2.76, Ea=(4400, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R16: H abstraction""",
)

entry(
    index = 17,
    label = "CH3CHNH + H <=> CH3CHN + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.19e+07, 'cm^3/(mol*s)'), n=1.96, Ea=(2400, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R17: H abstraction""",
)

entry(
    index = 18,
    label = "CH2CHNH2 + H <=> CH2CH2NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.14e+07, 'cm^3/(mol*s)'), n=1.77, Ea=(3729, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R18: beta scission""",
)

entry(
    index = 19,
    label = "C2H4 + NH2 <=> CH2CH2NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.23e+03, 'cm^3/(mol*s)'), n=2.76, Ea=(1658, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R19: beta scission""",
)

entry(
    index = 20,
    label = "CH3CHNH2 <=> CH2CHNH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.14e+09, 's^-1'), n=1.49, Ea=(35100, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R20: beta scission""",
)

entry(
    index = 21,
    label = "CH2NH + H <=> CH2NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.48e+08, 'cm^3/(mol*s)'), n=1.67, Ea=(2.295, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R21: beta scission""",
)

entry(
    index = 22,
    label = "CH2CHNH <=> CH2CNH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.18e+07, 's^-1'), n=2.26, Ea=(50300, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R22: beta scission""",
)

entry(
    index = 23,
    label = "CH3CHN <=> CH3 + HCN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.52e+10, 's^-1'), n=1.10, Ea=(26200, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R23: beta scission""",
)

entry(
    index = 24,
    label = "CH3CHN <=> CH3CN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.49e+09, 's^-1'), n=1.44, Ea=(27000, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R24: beta scission""",
)

entry(
    index = 25,
    label = "CH2CH2NH2 <=> CH3CHNH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+04, 's^-1'), n=2.33, Ea=(31800, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R25: intra H transfer""",
)

entry(
    index = 26,
    label = "CH2CHNH <=> CH3CHN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.20e+05, 's^-1'), n=2.16, Ea=(37400, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R26: intra H transfer""",
)

entry(
    index = 27,
    label = "NCC <=> C2H4 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.90e+04, 's^-1'), n=2.65, Ea=(65100, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Table 2, R27: 1,2-elimination""",
)

