#!/usr/bin/env python
# encoding: utf-8

name = "Aromatics_high_pressure/C10H11-1"
shortDesc = u"Phenyl radical 1,3-butadiene addition"
longDesc = u"""
A theoretical and experimental kinetic study of phenyl radical addition to butadiene
Huzeifa Ismail, J. Park, Bryan M. Wong, William H. Green Jr., M.C. Lin
Proceedings of the Combustion Institute 30 (2005) 1049–1056

Calculated at the B3LYP/6-31G(d,p) level of theory
"""
entry(
    index = 1,
    label = "phenyl + 1_3_butadiene <=> 4_phenyl_buten_3_yl",
    degeneracy = 1,
    kinetics = Arrhenius(A=(813000, 'cm^3/(mol*s)'), n=2.56, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2,
    label = "phenyl + 1_3_butadiene <=> 3_phenyl_buten_4_yl",
    degeneracy = 1,
    kinetics = Arrhenius(A=(47900, 'cm^3/(mol*s)'), n=2.65, Ea=(16.7, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 3,
    label = "phenyl + 1_3_butadiene <=> benzene + 1_3_butadien_2_yl",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8710, 'cm^3/(mol*s)'), n=3.12, Ea=(8.1, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 4,
    label = "phenyl + 1_3_butadiene <=> benzene + 1_3_butadien_1_yl",
    degeneracy = 1,
    kinetics = Arrhenius(A=(31600, 'cm^3/(mol*s)'), n=3.11, Ea=(16.7, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 5,
    label = "4_phenyl_buten_3_yl <=> trihydronaphthalene",
    degeneracy = 1,
    kinetics = Arrhenius(A=(324000, 's^-1'), n=1.64, Ea=(110.61, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 6,
    label = "4_phenyl_buten_3_yl <=> 1_phenyl_1_3_butadiene + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.61e+07, 's^-1'), n=2.11, Ea=(161.62, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 7,
    label = "trihydronaphthalene <=> 1_4_dihydro_naphthalene + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.38e+10, 's^-1'), n=1.25, Ea=(92.6, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

