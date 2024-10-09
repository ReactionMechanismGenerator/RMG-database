#!/usr/bin/env python
# encoding: utf-8

name = "Substitution_O/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "H + CH4O <=> H2O + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(39.0416,'cm^3/(mol*s)'), n=4.3597, Ea=(79.9065,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(HHH);HJ
""",
)

entry(
    index = 1,
    label = "H + C2H6O <=> H2O + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5567.88,'cm^3/(mol*s)'), n=3.20344, Ea=(85.6473,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(CsHH);HJ
""",
)

entry(
    index = 2,
    label = "H + C3H8O <=> H2O + C3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(114441,'cm^3/(mol*s)'), n=2.92889, Ea=(90.8706,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(CsCsH);HJ
""",
)

entry(
    index = 3,
    label = "H + C4H10O <=> H2O + C4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.20136e+07,'cm^3/(mol*s)'), n=2.47266, Ea=(89.8552,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(CsCsCs);HJ
""",
)

entry(
    index = 4,
    label = "H + C2H4O <=> H2O + C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(211470,'cm^3/(mol*s)'), n=2.48131, Ea=(120.285,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCds(H);HJ
""",
)

entry(
    index = 5,
    label = "H + C3H6O <=> H2O + C3H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.77054e+06,'cm^3/(mol*s)'), n=2.2995, Ea=(113.405,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCds(Cs);HJ
""",
)

entry(
    index = 6,
    label = "H + C3H6O-2 <=> H2O + C3H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.34234,'cm^3/(mol*s)'), n=3.69086, Ea=(61.9265,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(CdHH);HJ
""",
)

entry(
    index = 7,
    label = "H + C4H8O <=> H2O + C4H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(86.3518,'cm^3/(mol*s)'), n=3.29954, Ea=(64.6742,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(CdCsH);HJ
""",
)

entry(
    index = 8,
    label = "H + C5H10O <=> H2O + C5H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(61645,'cm^3/(mol*s)'), n=2.05568, Ea=(74.4647,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(CdCsCs);HJ
""",
)

entry(
    index = 9,
    label = "H + C3H4O <=> H2O + C3H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(389.816,'cm^3/(mol*s)'), n=3.3844, Ea=(66.7277,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(CtHH);HJ
""",
)

entry(
    index = 10,
    label = "H + C4H6O <=> H2O + C4H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(135928,'cm^3/(mol*s)'), n=2.59024, Ea=(68.9055,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(CtCsH);HJ
""",
)

entry(
    index = 11,
    label = "H + C5H8O <=> H2O + C5H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(178246,'cm^3/(mol*s)'), n=2.81287, Ea=(69.5929,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(CtCsCs);HJ
""",
)

entry(
    index = 12,
    label = "H + C2H6O-2 <=> CH4O-2 + CH3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(67650,'cm^3/(mol*s)'), n=2.90685, Ea=(101.985,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)Cs(HHH);HJ
""",
)

entry(
    index = 13,
    label = "H + C3H8O-2 <=> CH4O-2 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(552923,'cm^3/(mol*s)'), n=2.23663, Ea=(97.3621,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)Cs(CsHH);HJ
""",
)

entry(
    index = 14,
    label = "H + C4H10O-2 <=> CH4O-2 + C3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7919.31,'cm^3/(mol*s)'), n=2.85451, Ea=(95.9839,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)Cs(CsCsH);HJ
""",
)

entry(
    index = 15,
    label = "H + C5H12O <=> CH4O-2 + C4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5310.83,'cm^3/(mol*s)'), n=3.32233, Ea=(88.664,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)Cs(CsCsCs);HJ
""",
)

entry(
    index = 16,
    label = "H + C3H6O-3 <=> CH4O-2 + C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.84382e+09,'cm^3/(mol*s)'), n=0.40855, Ea=(127.023,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)Cds(H);HJ
""",
)

entry(
    index = 17,
    label = "H + C4H8O-2 <=> CH4O-2 + C3H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.01997e+11,'cm^3/(mol*s)'), n=0.59721, Ea=(131.953,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)Cds(Cs);HJ
""",
)

entry(
    index = 18,
    label = "H + C4H8O-3 <=> CH4O-2 + C3H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.271178,'cm^3/(mol*s)'), n=4.39592, Ea=(62.1119,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)Cs(CdHH);HJ
""",
)

entry(
    index = 19,
    label = "H + C5H10O-2 <=> CH4O-2 + C4H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(39.8648,'cm^3/(mol*s)'), n=3.10695, Ea=(62.7219,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)Cs(CdCsH);HJ
""",
)

entry(
    index = 20,
    label = "H + C6H12O <=> CH4O-2 + C5H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.27488,'cm^3/(mol*s)'), n=3.93967, Ea=(78.0237,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)Cs(CdCsCs);HJ
""",
)

entry(
    index = 21,
    label = "H + C4H6O-2 <=> CH4O-2 + C3H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(74.6326,'cm^3/(mol*s)'), n=3.47951, Ea=(70.5619,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)Cs(CtHH);HJ
""",
)

entry(
    index = 22,
    label = "H + C5H8O-2 <=> CH4O-2 + C4H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2084.17,'cm^3/(mol*s)'), n=2.71832, Ea=(76.1191,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)Cs(CtCsH);HJ
""",
)

entry(
    index = 23,
    label = "H + C6H10O <=> CH4O-2 + C5H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3599.97,'cm^3/(mol*s)'), n=3.2324, Ea=(75.3174,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)Cs(CtCsCs);HJ
""",
)

entry(
    index = 24,
    label = "H + C3H8O-3 <=> C2H6O-3 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8855.14,'cm^3/(mol*s)'), n=2.87556, Ea=(93.3065,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(CsHH)Cs(HHH);HJ
""",
)

entry(
    index = 25,
    label = "H + C4H10O-3 <=> C3H8O-4 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.31229,'cm^3/(mol*s)'), n=3.87313, Ea=(95.0496,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(CsCsH)Cs(HHH);HJ
""",
)

entry(
    index = 26,
    label = "H + C5H12O-2 <=> C4H10O-4 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.02268,'cm^3/(mol*s)'), n=4.01774, Ea=(90.42,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(CsCsCs)Cs(HHH);HJ
""",
)

entry(
    index = 27,
    label = "H + C3H6O-4 <=> C2H4O-2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(20.283,'cm^3/(mol*s)'), n=3.09138, Ea=(103.903,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cds(H)Cs(HHH);HJ
""",
)

entry(
    index = 28,
    label = "H + C4H8O-4 <=> C3H6O-5 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(12.5685,'cm^3/(mol*s)'), n=3.66046, Ea=(109.67,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cds(Cs)Cs(HHH);HJ
""",
)

entry(
    index = 29,
    label = "H + C4H8O-5 <=> C3H6O-6 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(131.885,'cm^3/(mol*s)'), n=3.52145, Ea=(91.5283,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(CdHH)Cs(HHH);HJ
""",
)

entry(
    index = 30,
    label = "H + C5H10O-3 <=> C4H8O-6 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0459721,'cm^3/(mol*s)'), n=4.358, Ea=(87.2916,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(CdCsH)Cs(HHH);HJ
""",
)

entry(
    index = 31,
    label = "H + C6H12O-2 <=> C5H10O-4 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.000646694,'cm^3/(mol*s)'), n=4.90628, Ea=(102.846,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(CdCsCs)Cs(HHH);HJ
""",
)

entry(
    index = 32,
    label = "H + C5H8O-3 <=> C4H6O-3 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.731898,'cm^3/(mol*s)'), n=4.2888, Ea=(92.6869,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(CtCsH)Cs(HHH);HJ
""",
)

entry(
    index = 33,
    label = "C2H6O + CH3-2 <=> CH4O-3 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(39.3494,'cm^3/(mol*s)'), n=4.19271, Ea=(170.476,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(CsHH);CsJ-HHH
""",
)

entry(
    index = 34,
    label = "C3H8O + CH3-2 <=> CH4O-3 + C3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1798.65,'cm^3/(mol*s)'), n=3.18285, Ea=(168.367,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(CsCsH);CsJ-HHH
""",
)

entry(
    index = 35,
    label = "C4H10O + CH3-2 <=> CH4O-3 + C4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(747648,'cm^3/(mol*s)'), n=2.3481, Ea=(172.012,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(CsCsCs);CsJ-HHH
""",
)

entry(
    index = 36,
    label = "C2H4O + CH3-2 <=> CH4O-3 + C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3250.38,'cm^3/(mol*s)'), n=3.24041, Ea=(208.587,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCds(H);CsJ-HHH
""",
)

entry(
    index = 37,
    label = "C3H6O + CH3-2 <=> CH4O-3 + C3H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.51813e+06,'cm^3/(mol*s)'), n=1.59641, Ea=(201.206,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCds(Cs);CsJ-HHH
""",
)

entry(
    index = 38,
    label = "C3H6O-2 + CH3-2 <=> CH4O-3 + C3H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0537217,'cm^3/(mol*s)'), n=3.93783, Ea=(133.915,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(CdHH);CsJ-HHH
""",
)

entry(
    index = 39,
    label = "C4H8O + CH3-2 <=> CH4O-3 + C4H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.29521e-08,'cm^3/(mol*s)'), n=5.86437, Ea=(159.665,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(CdCsH);CsJ-HHH
""",
)

entry(
    index = 40,
    label = "C5H10O + CH3-2 <=> CH4O-3 + C5H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.49022e-09,'cm^3/(mol*s)'), n=6.15234, Ea=(161.614,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(CdCsCs);CsJ-HHH
""",
)

entry(
    index = 41,
    label = "C3H4O + CH3-2 <=> CH4O-3 + C3H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(401.198,'cm^3/(mol*s)'), n=3.12619, Ea=(139.187,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(CtHH);CsJ-HHH
""",
)

entry(
    index = 42,
    label = "C4H6O + CH3-2 <=> CH4O-3 + C4H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2115.14,'cm^3/(mol*s)'), n=3.15487, Ea=(141.462,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(CtCsH);CsJ-HHH
""",
)

entry(
    index = 43,
    label = "C5H8O + CH3-2 <=> CH4O-3 + C5H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(76057.9,'cm^3/(mol*s)'), n=1.88123, Ea=(139.096,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(CtCsCs);CsJ-HHH
""",
)

entry(
    index = 44,
    label = "H + H2O2 <=> H2O + HO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.56874e+08,'cm^3/(mol*s)'), n=1.83697, Ea=(19.9718,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HOs(H);HJ
""",
)

entry(
    index = 45,
    label = "H + CH4O2 <=> CH4O-2 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.01017e+06,'cm^3/(mol*s)'), n=1.98323, Ea=(28.3773,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)O2s(H);HJ
""",
)

entry(
    index = 46,
    label = "H + CH4O2-2 <=> H2O + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.59061e+07,'cm^3/(mol*s)'), n=1.81476, Ea=(18.9999,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HOs(Cs);HJ
""",
)

entry(
    index = 47,
    label = "H + C2H6O2 <=> CH4O-2 + CH3O",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.4055e+11,'cm^3/(mol*s)'), n=0.29359, Ea=(26.5261,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)O2s(Cs);HJ
""",
)

entry(
    index = 48,
    label = "H2O2 + CH3-2 <=> CH4O-3 + HO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(89119.8,'cm^3/(mol*s)'), n=2.58699, Ea=(41.2803,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HOs(H);CsJ-HHH
""",
)

entry(
    index = 49,
    label = "CH4O2-2 + CH3-2 <=> CH4O-3 + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(26526.7,'cm^3/(mol*s)'), n=2.4453, Ea=(40.8852,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HOs(Cs);CsJ-HHH
""",
)

entry(
    index = 50,
    label = "CH4O2 + CH3-2 <=> C2H6O-4 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(20989.5,'cm^3/(mol*s)'), n=2.47358, Ea=(57.1003,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)O2s(H);CsJ-HHH
""",
)

entry(
    index = 51,
    label = "CH3-2 + C2H6O2 <=> C2H6O-4 + CH3O",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.5992e+07,'cm^3/(mol*s)'), n=1.07449, Ea=(53.6899,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)O2s(Cs);CsJ-HHH
""",
)

entry(
    index = 52,
    label = "H + H2O3 <=> H2O2-2 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.73772e+06,'cm^3/(mol*s)'), n=2.13626, Ea=(37.1751,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-O2s(H)O2s(H);HJ
""",
)

entry(
    index = 53,
    label = "H + H2O3-2 <=> H2O + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.17266e+08,'cm^3/(mol*s)'), n=1.4407, Ea=(18.1507,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-HOs(O2s);HJ
""",
)

entry(
    index = 54,
    label = "H + CH4O3 <=> CH4O2-3 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.95051e+06,'cm^3/(mol*s)'), n=2.54316, Ea=(36.5109,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-O2s(Cs)O2s(H);HJ
""",
)

entry(
    index = 55,
    label = "H + CH4O3-2 <=> CH4O-2 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.56529e+07,'cm^3/(mol*s)'), n=2.045, Ea=(32.2283,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-Cs(HHH)O2s(O2s);HJ
""",
)

entry(
    index = 56,
    label = "H + CH4O3-3 <=> H2O2-2 + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2409e+06,'cm^3/(mol*s)'), n=2.35959, Ea=(37.3413,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-O2s(H)O2s(Cs);HJ
""",
)

entry(
    index = 57,
    label = "H + C2H6O3 <=> CH4O2-3 + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.95424e+06,'cm^3/(mol*s)'), n=2.71236, Ea=(38.1455,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-O2s(Cs)O2s(Cs);HJ
""",
)

entry(
    index = 58,
    label = "H2O3 + CH3-2 <=> CH4O2-4 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1119.49,'cm^3/(mol*s)'), n=3.06029, Ea=(58.0576,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-O2s(H)O2s(H);CsJ-HHH
""",
)

entry(
    index = 59,
    label = "H2O3-2 + CH3-2 <=> CH4O-3 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(17942.7,'cm^3/(mol*s)'), n=2.60187, Ea=(35.1911,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-HOs(O2s);CsJ-HHH
""",
)

entry(
    index = 60,
    label = "CH4O3-3 + CH3-2 <=> CH4O2-4 + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(152659,'cm^3/(mol*s)'), n=2.22409, Ea=(58.7609,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-O2s(H)O2s(Cs);CsJ-HHH
""",
)

entry(
    index = 61,
    label = "CH4O3-2 + CH3-2 <=> C2H6O-4 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(101433,'cm^3/(mol*s)'), n=2.72306, Ea=(57.6936,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-Cs(HHH)O2s(O2s);CsJ-HHH
""",
)

entry(
    index = 62,
    label = "CH4O3 + CH3-2 <=> C2H6O2-2 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(26016.1,'cm^3/(mol*s)'), n=2.61392, Ea=(62.8261,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-O2s(Cs)O2s(H);CsJ-HHH
""",
)

entry(
    index = 63,
    label = "CH3-2 + C2H6O3 <=> C2H6O2-2 + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(98402.5,'cm^3/(mol*s)'), n=2.87073, Ea=(58.3526,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-O2s(Cs)O2s(Cs);CsJ-HHH
""",
)

entry(
    index = 64,
    label = "H2O-2 + CH3-2 <=> CH4O-3 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.0141707,'cm^3/(mol*s)'), n=5.12614, Ea=(187.817,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HH;CsJ-HHH
""",
)

entry(
    index = 65,
    label = "H2O-2 + C2H5-2 <=> C2H6O-5 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.905842,'cm^3/(mol*s)'), n=3.53834, Ea=(186.248,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HH;CsJ-CsHH
""",
)

entry(
    index = 66,
    label = "H2O-2 + C3H7-2 <=> C3H8O-5 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.8163e-05,'cm^3/(mol*s)'), n=5.13525, Ea=(183.95,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HH;CsJ-CsCsH
""",
)

entry(
    index = 67,
    label = "H2O-2 + C4H9-2 <=> C4H10O-5 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.37409e-05,'cm^3/(mol*s)'), n=5.03769, Ea=(174.549,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HH;CsJ-CsCsCs
""",
)

entry(
    index = 68,
    label = "H2O-2 + C2H3-2 <=> C2H4O-3 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.029503,'cm^3/(mol*s)'), n=4.11084, Ea=(158.494,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HH;CdsJ-H
""",
)

entry(
    index = 69,
    label = "H2O-2 + C3H5-3 <=> C3H6O-7 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.028266,'cm^3/(mol*s)'), n=4.04095, Ea=(155.106,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HH;CdsJ-Cs
""",
)

entry(
    index = 70,
    label = "H2O-2 + C3H5-4 <=> C3H6O-8 + H-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(0.00134884,'cm^3/(mol*s)'), n=4.79715, Ea=(226.202,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HH;CsJ-CdHH
""",
)

entry(
    index = 71,
    label = "H2O-2 + C4H7-2 <=> C4H8O-7 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.000213922,'cm^3/(mol*s)'), n=4.07435, Ea=(213.908,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HH;CsJ-CdCsH
""",
)

entry(
    index = 72,
    label = "H2O-2 + C5H9-2 <=> C5H10O-5 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.07987e-05,'cm^3/(mol*s)'), n=4.75792, Ea=(225.972,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HH;CsJ-CdCsCs
""",
)

entry(
    index = 73,
    label = "H2O-2 + C3H3-2 <=> C3H4O-2 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.00180117,'cm^3/(mol*s)'), n=4.62782, Ea=(219.844,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HH;CsJ-CtHH
""",
)

entry(
    index = 74,
    label = "H2O-2 + C4H5-2 <=> C4H6O-4 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.000533538,'cm^3/(mol*s)'), n=4.5494, Ea=(213.231,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HH;CsJ-CtCsH
""",
)

entry(
    index = 75,
    label = "H2O-2 + C5H7-2 <=> C5H8O-4 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.83141e-06,'cm^3/(mol*s)'), n=5.48115, Ea=(209.73,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HH;CsJ-CtCsCs
""",
)

entry(
    index = 76,
    label = "CH4O-4 + CH3-2 <=> C2H6O-4 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.02386e-06,'cm^3/(mol*s)'), n=5.80487, Ea=(174.909,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)H;CsJ-HHH
""",
)

entry(
    index = 77,
    label = "CH4O-4 + C2H5-2 <=> C3H8O-6 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.43164e-05,'cm^3/(mol*s)'), n=4.81746, Ea=(177.51,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)H;CsJ-CsHH
""",
)

entry(
    index = 78,
    label = "CH4O-4 + C3H7-2 <=> C4H10O-6 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.62031e-09,'cm^3/(mol*s)'), n=6.05127, Ea=(172.031,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)H;CsJ-CsCsH
""",
)

entry(
    index = 79,
    label = "CH4O-4 + C4H9-2 <=> C5H12O-3 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.95558e-11,'cm^3/(mol*s)'), n=6.18012, Ea=(165.796,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)H;CsJ-CsCsCs
""",
)

entry(
    index = 80,
    label = "C2H3-2 + CH4O-4 <=> C3H6O-9 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0166055,'cm^3/(mol*s)'), n=3.78744, Ea=(137.831,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)H;CdsJ-H
""",
)

entry(
    index = 81,
    label = "CH4O-4 + C3H5-3 <=> C4H8O-8 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00341995,'cm^3/(mol*s)'), n=3.88799, Ea=(141.357,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)H;CdsJ-Cs
""",
)

entry(
    index = 82,
    label = "CH4O-4 + C3H5-4 <=> C4H8O-9 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.53604e-08,'cm^3/(mol*s)'), n=6.23988, Ea=(204.751,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)H;CsJ-CdHH
""",
)

entry(
    index = 83,
    label = "CH4O-4 + C4H7-2 <=> C5H10O-6 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.44203e-07,'cm^3/(mol*s)'), n=4.39147, Ea=(197.003,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)H;CsJ-CdCsH
""",
)

entry(
    index = 84,
    label = "CH4O-4 + C5H9-2 <=> C6H12O-3 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.78109e-13,'cm^3/(mol*s)'), n=7.37017, Ea=(209.585,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)H;CsJ-CdCsCs
""",
)

entry(
    index = 85,
    label = "C3H3-2 + CH4O-4 <=> C4H6O-5 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.01409e-07,'cm^3/(mol*s)'), n=5.81184, Ea=(202.721,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)H;CsJ-CtHH
""",
)

entry(
    index = 86,
    label = "C4H5-2 + CH4O-4 <=> C5H8O-5 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.75102e-08,'cm^3/(mol*s)'), n=5.1553, Ea=(197.022,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)H;CsJ-CtCsH
""",
)

entry(
    index = 87,
    label = "C5H7-2 + CH4O-4 <=> C6H10O-2 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.82635e-11,'cm^3/(mol*s)'), n=6.50124, Ea=(198.253,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)H;CsJ-CtCsCs
""",
)

entry(
    index = 88,
    label = "C2H6O-6 + CH3-2 <=> C3H8O-7 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.01263e-06,'cm^3/(mol*s)'), n=5.88794, Ea=(180.765,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(CsHH)H;CsJ-HHH
""",
)

entry(
    index = 89,
    label = "C3H8O-8 + CH3-2 <=> C4H10O-7 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.23057e-06,'cm^3/(mol*s)'), n=5.62998, Ea=(185.928,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(CsCsH)H;CsJ-HHH
""",
)

entry(
    index = 90,
    label = "C4H10O-8 + CH3-2 <=> C5H12O-4 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.02826e-06,'cm^3/(mol*s)'), n=5.07693, Ea=(190.768,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(CsCsCs)H;CsJ-HHH
""",
)

entry(
    index = 91,
    label = "C2H4O-4 + CH3-2 <=> C3H6O-10 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.49946e-07,'cm^3/(mol*s)'), n=5.60717, Ea=(185.794,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cds(H)H;CsJ-HHH
""",
)

entry(
    index = 92,
    label = "C3H6O-11 + CH3-2 <=> C4H8O-10 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.83798e-09,'cm^3/(mol*s)'), n=5.97622, Ea=(183.902,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cds(Cs)H;CsJ-HHH
""",
)

entry(
    index = 93,
    label = "C3H6O-12 + CH3-2 <=> C4H8O-11 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.1701e-05,'cm^3/(mol*s)'), n=4.92691, Ea=(174.219,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(CdHH)H;CsJ-HHH
""",
)

entry(
    index = 94,
    label = "C4H8O-12 + CH3-2 <=> C5H10O-7 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.30403e-08,'cm^3/(mol*s)'), n=5.77538, Ea=(181.145,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(CdCsH)H;CsJ-HHH
""",
)

entry(
    index = 95,
    label = "C5H10O-8 + CH3-2 <=> C6H12O-4 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.76943e-10,'cm^3/(mol*s)'), n=6.31699, Ea=(187.173,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(CdCsCs)H;CsJ-HHH
""",
)

entry(
    index = 96,
    label = "C4H6O-6 + CH3-2 <=> C5H8O-6 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.04813e-07,'cm^3/(mol*s)'), n=5.68858, Ea=(176.718,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(CtCsH)H;CsJ-HHH
""",
)

entry(
    index = 97,
    label = "CH4O + C2H5-2 <=> C2H6O-5 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(17.6374,'cm^3/(mol*s)'), n=3.76118, Ea=(163.166,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(HHH);CsJ-CsHH
""",
)

entry(
    index = 98,
    label = "CH4O + C3H7-2 <=> C3H8O-5 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00208552,'cm^3/(mol*s)'), n=4.62276, Ea=(153.536,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(HHH);CsJ-CsCsH
""",
)

entry(
    index = 99,
    label = "CH4O + C4H9-2 <=> C4H10O-5 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.002356,'cm^3/(mol*s)'), n=4.14669, Ea=(148.795,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(HHH);CsJ-CsCsCs
""",
)

entry(
    index = 100,
    label = "C2H3-2 + CH4O <=> C2H4O-3 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.24935,'cm^3/(mol*s)'), n=4.10349, Ea=(138.885,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(HHH);CdsJ-H
""",
)

entry(
    index = 101,
    label = "CH4O + C3H5-3 <=> C3H6O-7 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(154.741,'cm^3/(mol*s)'), n=2.57143, Ea=(134.996,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(HHH);CdsJ-Cs
""",
)

entry(
    index = 102,
    label = "CH4O + C3H5-4 <=> C3H6O-8 + CH3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.0239308,'cm^3/(mol*s)'), n=4.27768, Ea=(190.279,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(HHH);CsJ-CdHH
""",
)

entry(
    index = 103,
    label = "CH4O + C4H7-2 <=> C4H8O-7 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.84018e-11,'cm^3/(mol*s)'), n=5.87274, Ea=(200.988,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(HHH);CsJ-CdCsH
""",
)

entry(
    index = 104,
    label = "CH4O + C5H9-2 <=> C5H10O-5 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.68446e-15,'cm^3/(mol*s)'), n=8.08814, Ea=(205.211,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(HHH);CsJ-CdCsCs
""",
)

entry(
    index = 105,
    label = "C3H3-2 + CH4O <=> C3H4O-2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.10728,'cm^3/(mol*s)'), n=3.60317, Ea=(184.393,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(HHH);CsJ-CtHH
""",
)

entry(
    index = 106,
    label = "C4H5-2 + CH4O <=> C4H6O-4 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0228734,'cm^3/(mol*s)'), n=4.3476, Ea=(177.877,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(HHH);CsJ-CtCsH
""",
)

entry(
    index = 107,
    label = "C5H7-2 + CH4O <=> C5H8O-4 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00215301,'cm^3/(mol*s)'), n=3.78307, Ea=(171.323,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(HHH);CsJ-CtCsCs
""",
)

entry(
    index = 108,
    label = "HO-2 + H2O-2 <=> H2O2-3 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(29042.8,'cm^3/(mol*s)'), n=2.91678, Ea=(303.816,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HH;OsJ-H
""",
)

entry(
    index = 109,
    label = "HO-2 + CH4O-4 <=> CH4O2-5 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(11.0699,'cm^3/(mol*s)'), n=3.50482, Ea=(276.306,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)H;OsJ-H
""",
)

entry(
    index = 110,
    label = "H2O-2 + CH3O-2 <=> CH4O2-6 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1122.24,'cm^3/(mol*s)'), n=3.18249, Ea=(324.558,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HH;OsJ-Cs
""",
)

entry(
    index = 111,
    label = "CH4O-4 + CH3O-2 <=> C2H6O2-3 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.05378,'cm^3/(mol*s)'), n=3.66741, Ea=(299.373,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)H;OsJ-Cs
""",
)

entry(
    index = 112,
    label = "HO-2 + CH4O <=> H2O2-3 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(27760.5,'cm^3/(mol*s)'), n=2.90036, Ea=(215.201,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(HHH);OsJ-H
""",
)

entry(
    index = 113,
    label = "CH4O + CH3O-2 <=> CH4O2-6 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1244.45,'cm^3/(mol*s)'), n=3.04659, Ea=(238.532,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-HCs(HHH);OsJ-Cs
""",
)

entry(
    index = 114,
    label = "HO-2 + C2H6O-2 <=> CH4O2-5 + CH3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.65288e+07,'cm^3/(mol*s)'), n=1.47906, Ea=(218.997,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)Cs(HHH);OsJ-H
""",
)

entry(
    index = 115,
    label = "CH3O-2 + C2H6O-2 <=> C2H6O2-3 + CH3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(234442,'cm^3/(mol*s)'), n=1.9322, Ea=(240.048,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)""",
    longDesc = 
"""
Converted to training reaction from rate rule: O-Cs(HHH)Cs(HHH);OsJ-Cs
""",
)

entry(
    index = 116,
    label = "HO-2 + H2O2-4 <=> H2O3-3 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00278991,'cm^3/(mol*s)'), n=4.75128, Ea=(254.174,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-O2s(H)H;OsJ-H
""",
)

entry(
    index = 117,
    label = "HO2-2 + H2O-2 <=> H2O3-4 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0267498,'cm^3/(mol*s)'), n=4.5091, Ea=(365.521,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-HH;OsJ-O2s
""",
)

entry(
    index = 118,
    label = "HO-2 + CH4O2-7 <=> CH4O3-4 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.000781287,'cm^3/(mol*s)'), n=5.15922, Ea=(250.967,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-O2s(Cs)H;OsJ-H
""",
)

entry(
    index = 119,
    label = "HO2-2 + CH4O-4 <=> CH4O3-5 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.54686e-05,'cm^3/(mol*s)'), n=5.55622, Ea=(343.153,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-Cs(HHH)H;OsJ-O2s
""",
)

entry(
    index = 120,
    label = "H2O2-4 + CH3O-2 <=> CH4O3-6 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.47435e-05,'cm^3/(mol*s)'), n=5.26357, Ea=(275.524,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-O2s(H)H;OsJ-Cs
""",
)

entry(
    index = 121,
    label = "CH4O2-7 + CH3O-2 <=> C2H6O3-2 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.92558e-06,'cm^3/(mol*s)'), n=5.89053, Ea=(273.758,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-O2s(Cs)H;OsJ-Cs
""",
)

entry(
    index = 122,
    label = "HO-2 + CH4O2-8 <=> H2O3-3 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.376691,'cm^3/(mol*s)'), n=4.46709, Ea=(201.048,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-O2s(H)Cs(HHH);OsJ-H
""",
)

entry(
    index = 123,
    label = "HO2-2 + CH4O <=> H2O3-4 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00368718,'cm^3/(mol*s)'), n=4.90384, Ea=(274.65,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-HCs(HHH);OsJ-O2s
""",
)

entry(
    index = 124,
    label = "CH4O2-8 + CH3O-2 <=> CH4O3-6 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.37223,'cm^3/(mol*s)'), n=3.91986, Ea=(222.936,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-O2s(H)Cs(HHH);OsJ-Cs
""",
)

entry(
    index = 125,
    label = "HO2-2 + C2H6O-2 <=> CH4O3-5 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(13.1108,'cm^3/(mol*s)'), n=3.71859, Ea=(284.305,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-Cs(HHH)Cs(HHH);OsJ-O2s
""",
)

entry(
    index = 126,
    label = "HO-2 + C2H6O2-4 <=> CH4O3-4 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(21552.6,'cm^3/(mol*s)'), n=2.45745, Ea=(202.083,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-O2s(Cs)Cs(HHH);OsJ-H
""",
)

entry(
    index = 127,
    label = "CH3O-2 + C2H6O2-4 <=> C2H6O3-2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0036016,'cm^3/(mol*s)'), n=5.31614, Ea=(66.9829,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-O2s(Cs)Cs(HHH);OsJ-Cs
""",
)

entry(
    index = 128,
    label = "CH3LiO + C2H5-2 <=> C3H8O-6 + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00266112,'cm^3/(mol*s)'), n=4.54216, Ea=(65.2952,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OC + C[CH2] <=> [Li] + COCC
TS method summary for TS2 in [Li]OC + C[CH2] <=> [Li] + COCC:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li      0.95543900   -2.06606100    0.49168200
C      -1.75006400    0.40919300    0.35197900
C      -0.92556700   -0.39675200   -0.59963000
O       0.88790900   -0.39946500    0.11588300
C       1.47810800    0.86505900   -0.03509700
H      -1.29395600    1.37884800    0.56898500
H      -1.90037200   -0.11068200    1.30024000
H      -2.74501400    0.61653300   -0.07202800
H      -1.15395000   -1.45760200   -0.67306700
H      -0.66073800    0.05265400   -1.54957700
H       1.04427800    1.60592100    0.65130900
H       1.36341600    1.24189300   -1.06273700
H       2.55152500    0.80698400    0.17628500

1D rotors:
pivots: [2, 3], dihedral: [6, 2, 3, 9], rotor symmetry: 3, max scan energy: 4.07 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [1, 4, 5, 11], invalidation reason: Two consecutive points are inconsistent by more than 0.60 kJ/molTwo consecutive points are inconsistent by more than 0.75 kJ/molTwo consecutive points are inconsistent by more than 0.80 kJ/mol
ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvp
""",
)

entry(
    index = 129,
    label = "HLiO + H <=> H2O + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.03649e+11,'cm^3/(mol*s)'), n=0.812216, Ea=(-21.6525,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.6576610150461983,B=2.4435784684265482,E=0.404796645816695,L=7.698368077501874,A=0.9750486732350473,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]O + [H] <=> [Li] + O
TS method summary for TS9 in [Li]O + [H] <=> [Li] + O:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li      1.28826489    0.18010119    0.00207350
O      -0.36733064    0.11184220    0.00745957
H       0.39396705   -1.32898954   -0.00633395
H      -1.27901258   -0.17912694    0.00905353


No rotors considered for this TS.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 2114.547977695349 J/mol
""",
)

entry(
    index = 130,
    label = "CH3LiO + H <=> CH4O-2 + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.47113e+11,'cm^3/(mol*s)'), n=0.774968, Ea=(-24.6724,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.4067121409688057,B=1.4628968939845368,E=0.9656443938025181,L=7.661570379273675,A=0.443175955652443,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OC + [H] <=> [Li] + CO
TS method summary for TS11 in [Li]OC + [H] <=> [Li] + CO:
Methods that successfully generated a TS guess:
user guess 0,user guess 0,
The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li      2.05286763    0.11494012   -0.00863872
O       0.38320517    0.12959365   -0.00264163
C      -1.00062168   -0.00723588   -0.00489942
H       0.96172040   -1.23025812    0.00873654
H      -1.46633645    0.98431418   -0.00871499
H      -1.35936775   -0.54162168    0.88336582
H      -1.35623697   -0.54719021   -0.89107706

1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 5], rotor symmetry: 1, max scan energy: 0.65 kJ/mol (set as a FreeRotor)
ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvpused COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 1321.823066484516 J/mol
""",
)

entry(
    index = 131,
    label = "HLiO + CH3-2 <=> CH4O-3 + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.07712e+06,'cm^3/(mol*s)'), n=2.28023, Ea=(85.5904,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.4173362998736376,B=2.357499252462657,E=0.5167298959343533,L=7.9017680525604375,A=1.0064038665607862,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]O + [CH3] <=> [Li] + CO
TS method summary for TS12 in [Li]O + [CH3] <=> [Li] + CO:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li     -0.28748200   -0.18010600    1.00319500
O       0.86993900    0.39784300   -0.11608000
C       2.59811800   -0.51057100   -0.06290500
H       0.96229700    1.06152900   -0.80658800
H       3.25030100    0.31559600    0.18187100
H       2.64875300   -0.90201200   -1.06889700
H       2.43978600   -1.23892300    0.72228500


No rotors considered for this TS.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 2046.4105178239631 J/mol
""",
)

entry(
    index = 132,
    label = "HLiO + C2H5-2 <=> C2H6O-5 + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(26.5507,'cm^3/(mol*s)'), n=3.72095, Ea=(84.1068,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.9913576154323054,B=3.1755887609180435,E=-0.2623364392566645,L=7.244831699370673,A=0.5572363451823703,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]O + C[CH2] <=> [Li] + CCO
TS method summary for TS15 in [Li]O + C[CH2] <=> [Li] + CCO:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li     -2.57304700    0.27516400   -0.65750400
C       1.54543100   -0.31294900   -0.20991200
C       0.50691500    0.68250500    0.19066600
O      -1.20609000   -0.34489700    0.18644900
H       1.31703400   -0.75838900   -1.18091300
H       2.53974800    0.15487200   -0.28938100
H       1.63329600   -1.12303200    0.51949300
H       0.22894600    1.43785900   -0.53575000
H       0.48492400    1.02184600    1.21876200
H      -1.09958300   -1.00876300    0.87538500

1D rotors:
pivots: [2, 3], dihedral: [5, 2, 3, 8], rotor symmetry: 3, max scan energy: 5.59 kJ/mol
ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvpused COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 1614.986893512281 J/mol
""",
)

entry(
    index = 133,
    label = "C2H5LiO + H <=> C2H6O-3 + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.77483e+09,'cm^3/(mol*s)'), n=1.18598, Ea=(-23.16,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-8.623486006056842,B=14.917486429580572,E=-5.719694357458241,L=40.120001635540106,A=-6.502228345652631,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OCC + [H] <=> [Li] + CCO
TS method summary for TS16 in [Li]OCC + [H] <=> [Li] + CCO:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li      2.49143616    0.55729277   -0.12525674
C      -1.41113872    0.44040349   -0.02571704
C      -0.33003762   -0.62547457    0.03698411
O       0.94967788   -0.09370527   -0.11768223
H      -1.37208971    0.96882848   -0.98064514
H      -2.40427692   -0.00332329    0.08351568
H      -1.26743662    1.17043881    0.77319839
H      -0.49296294   -1.36694873   -0.75554854
H      -0.39930548   -1.16567232    0.99075815
H       1.34235779    0.48281906    1.16520496

1D rotors:
pivots: [2, 3], dihedral: [5, 2, 3, 4], rotor symmetry: 3, max scan energy: 13.87 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 1], rotor symmetry: 1, max scan energy: 0.52 kJ/mol (set as a FreeRotor)
ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvpused COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 1.736364652060729e-05 J/mol
""",
)

entry(
    index = 134,
    label = "CH3LiO + CH3-2 <=> C2H6O-4 + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3026.56,'cm^3/(mol*s)'), n=2.80221, Ea=(80.834,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.223920620501668,B=0.8264175269682525,E=0.40415741933873844,L=5.605210034978575,A=0.4397271958947774,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OC + [CH3] <=> [Li] + COC
TS method summary for TS1 in [Li]OC + [CH3] <=> [Li] + COC:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li      6.51706400   -1.13632600   -3.21539400
C       4.02423400   -1.41606000   -2.34418400
O       5.56418700   -0.34050500   -2.05108800
C       5.26882800    0.60085300   -1.05050100
H       3.90830800   -1.82877700   -1.35110600
H       4.26586000   -2.13817000   -3.11854700
H       3.32573800   -0.64407500   -2.63764800
H       4.99996100    0.11042200   -0.10400400
H       4.43692100    1.25540800   -1.34741500
H       6.14543300    1.23014000   -0.86797000

1D rotors:
* Invalidated! pivots: [3, 4], dihedral: [1, 3, 4, 8], invalidation reason: Two consecutive points are inconsistent by more than 1.40 kJ/molTwo consecutive points are inconsistent by more than 1.52 kJ/mol But unable to propose troubleshooting methods.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 1526.5386694571223 J/mol
""",
)

entry(
    index = 135,
    label = "C2H5LiO + CH3-2 <=> C3H8O-7 + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.09569,'cm^3/(mol*s)'), n=3.2546, Ea=(82.2788,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.091886494292463,B=0.5254418313743373,E=1.2963729646265112,L=5.721969023897385,A=0.6575614317431779,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OCC + [CH3] <=> [Li] + COCC
TS method summary for TS3 in [Li]OCC + [CH3] <=> [Li] + COCC:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li     -2.74010800   -4.87944000   -2.74685100
C      -2.29023200   -1.71339600   -1.09005000
C      -3.11923600   -1.87939400   -2.35977600
O      -3.12657200   -3.21901700   -2.79202100
C      -4.17095700   -3.35427200   -4.36839000
H      -1.25332700   -2.01355600   -1.26099300
H      -2.69616100   -2.32265000   -0.27855700
H      -2.29596500   -0.66546600   -0.76876900
H      -4.14967400   -1.54173400   -2.17015500
H      -2.70920200   -1.23314600   -3.15098300
H      -3.61682000   -2.67724300   -5.00431900
H      -5.11687000   -2.99859300   -3.98292400
H      -4.16500100   -4.39266700   -4.68634200

1D rotors:
pivots: [2, 3], dihedral: [6, 2, 3, 4], rotor symmetry: 3, max scan energy: 15.23 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 1], invalidation reason: Two consecutive points are inconsistent by more than 6.75 kJ/molTwo consecutive points are inconsistent by more than 6.75 kJ/molTwo consecutive points are inconsistent by more than 6.64 kJ/mol
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 1616.2708289398845 J/mol
""",
)

