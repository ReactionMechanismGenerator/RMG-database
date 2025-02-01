#!/usr/bin/env python
# encoding: utf-8

name = "SubstitutionS/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "H + CH4S <=> H2S + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.04e+08,'cm^3/(mol*s)'), n=1.49, Ea=(16.3176,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(HHH);HJ
""",
)

entry(
    index = 1,
    label = "H + C2H6S <=> H2S + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.06e+07,'cm^3/(mol*s)'), n=2.13, Ea=(15.439,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """CAC CBS-QB3 1dhr""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(CsHH);HJ
""",
)

entry(
    index = 2,
    label = "H + C3H8S <=> H2S + C3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.84e+08,'cm^3/(mol*s)'), n=1.59, Ea=(12.9704,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(CsCsH);HJ
""",
)

entry(
    index = 3,
    label = "H + C4H10S <=> H2S + C4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.79e+08,'cm^3/(mol*s)'), n=1.63, Ea=(10.0416,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(CsCsCs);HJ
""",
)

entry(
    index = 4,
    label = "H + C2H4S <=> H2S + C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.9e+08,'cm^3/(mol*s)'), n=1.54, Ea=(25.1877,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCds(H);HJ
""",
)

entry(
    index = 5,
    label = "H + C3H6S <=> H2S + C3H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.19e+06,'cm^3/(mol*s)'), n=2.44, Ea=(25.7316,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCds(Cs);HJ
""",
)

entry(
    index = 6,
    label = "H + C3H6S-2 <=> H2S + C3H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.42e+08,'cm^3/(mol*s)'), n=1.66, Ea=(8.368,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(CdHH);HJ
""",
)

entry(
    index = 7,
    label = "H + C4H8S <=> H2S + C4H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.93e+08,'cm^3/(mol*s)'), n=1.57, Ea=(8.368,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(CdCsH);HJ
""",
)

entry(
    index = 8,
    label = "H + C5H10S <=> H2S + C5H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.66e+08,'cm^3/(mol*s)'), n=1.56, Ea=(7.1128,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(CdCsCs);HJ
""",
)

entry(
    index = 9,
    label = "H + C3H4S <=> H2S + C3H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.81e+08,'cm^3/(mol*s)'), n=1.57, Ea=(12.1336,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(CtHH);HJ
""",
)

entry(
    index = 10,
    label = "H + C4H6S <=> H2S + C4H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.79e+08,'cm^3/(mol*s)'), n=1.49, Ea=(10.46,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(CtCsH);HJ
""",
)

entry(
    index = 11,
    label = "H + C5H8S <=> H2S + C5H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.76e+08,'cm^3/(mol*s)'), n=1.51, Ea=(8.7864,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(CtCsCs);HJ
""",
)

entry(
    index = 12,
    label = "H + C2H6S-2 <=> CH4S-2 + CH3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.28e+08,'cm^3/(mol*s)'), n=1.52, Ea=(14.2256,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)Cs(HHH);HJ
""",
)

entry(
    index = 13,
    label = "H + C3H8S-2 <=> CH4S-2 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.98e+08,'cm^3/(mol*s)'), n=1.51, Ea=(12.552,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)Cs(CsHH);HJ
""",
)

entry(
    index = 14,
    label = "H + C4H10S-2 <=> CH4S-2 + C3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.68e+08,'cm^3/(mol*s)'), n=1.48, Ea=(13.8072,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)Cs(CsCsH);HJ
""",
)

entry(
    index = 15,
    label = "H + C5H12S <=> CH4S-2 + C4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.14e+08,'cm^3/(mol*s)'), n=1.5, Ea=(12.1336,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)Cs(CsCsCs);HJ
""",
)

entry(
    index = 16,
    label = "H + C3H6S-3 <=> CH4S-2 + C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.38e+10,'cm^3/(mol*s)'), n=0.79, Ea=(34.3088,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)Cds(H);HJ
""",
)

entry(
    index = 17,
    label = "H + C4H8S-2 <=> CH4S-2 + C3H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.81e+09,'cm^3/(mol*s)'), n=1.15, Ea=(25.7316,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)Cds(Cs);HJ
""",
)

entry(
    index = 18,
    label = "H + C4H8S-3 <=> CH4S-2 + C3H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.53e+08,'cm^3/(mol*s)'), n=1.54, Ea=(9.2048,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)Cs(CdHH);HJ
""",
)

entry(
    index = 19,
    label = "H + C5H10S-2 <=> CH4S-2 + C4H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.05e+08,'cm^3/(mol*s)'), n=1.49, Ea=(8.368,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)Cs(CdCsH);HJ
""",
)

entry(
    index = 20,
    label = "H + C6H12S <=> CH4S-2 + C5H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.92e+08,'cm^3/(mol*s)'), n=1.57, Ea=(6.6944,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)Cs(CdCsCs);HJ
""",
)

entry(
    index = 21,
    label = "H + C4H6S-2 <=> CH4S-2 + C3H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.33e+08,'cm^3/(mol*s)'), n=1.62, Ea=(10.46,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)Cs(CtHH);HJ
""",
)

entry(
    index = 22,
    label = "H + C5H8S-2 <=> CH4S-2 + C4H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.87e+08,'cm^3/(mol*s)'), n=1.62, Ea=(8.368,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)Cs(CtCsH);HJ
""",
)

entry(
    index = 23,
    label = "H + C6H10S <=> CH4S-2 + C5H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.36e+08,'cm^3/(mol*s)'), n=1.63, Ea=(7.9496,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)Cs(CtCsCs);HJ
""",
)

entry(
    index = 24,
    label = "H + C3H8S-3 <=> C2H6S-3 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.81e+07,'cm^3/(mol*s)'), n=1.48, Ea=(12.1336,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(CsHH)Cs(HHH);HJ
""",
)

entry(
    index = 25,
    label = "H + C4H10S-3 <=> C3H8S-4 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.57e+07,'cm^3/(mol*s)'), n=1.45, Ea=(15.8992,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(CsCsH)Cs(HHH);HJ
""",
)

entry(
    index = 26,
    label = "H + C5H12S-2 <=> C4H10S-4 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.66e+07,'cm^3/(mol*s)'), n=1.54, Ea=(18.828,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(CsCsCs)Cs(HHH);HJ
""",
)

entry(
    index = 27,
    label = "H + C3H6S-4 <=> C2H4S-2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.62e+07,'cm^3/(mol*s)'), n=1.53, Ea=(19.2464,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cds(H)Cs(HHH);HJ
""",
)

entry(
    index = 28,
    label = "H + C4H8S-4 <=> C3H6S-5 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.81e+07,'cm^3/(mol*s)'), n=1.6, Ea=(22.1752,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cds(Cs)Cs(HHH);HJ
""",
)

entry(
    index = 29,
    label = "H + C4H8S-5 <=> C3H6S-6 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.61e+08,'cm^3/(mol*s)'), n=1.54, Ea=(14.644,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(CdHH)Cs(HHH);HJ
""",
)

entry(
    index = 30,
    label = "H + C5H10S-3 <=> C4H8S-6 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.34e+08,'cm^3/(mol*s)'), n=1.43, Ea=(18.4096,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(CdCsH)Cs(HHH);HJ
""",
)

entry(
    index = 31,
    label = "H + C6H12S-2 <=> C5H10S-4 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.31e+08,'cm^3/(mol*s)'), n=1.52, Ea=(21.3384,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(CdCsCs)Cs(HHH);HJ
""",
)

entry(
    index = 32,
    label = "H + C4H6S-3 <=> C3H4S-2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.21e+08,'cm^3/(mol*s)'), n=1.54, Ea=(15.0624,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(CtHH)Cs(HHH);HJ
""",
)

entry(
    index = 33,
    label = "H + C5H8S-3 <=> C4H6S-4 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.42e+08,'cm^3/(mol*s)'), n=1.47, Ea=(15.8992,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(CtCsH)Cs(HHH);HJ
""",
)

entry(
    index = 34,
    label = "H + C6H10S-2 <=> C5H8S-4 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.68e+07,'cm^3/(mol*s)'), n=1.59, Ea=(19.2464,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(CtCsCs)Cs(HHH);HJ
""",
)

entry(
    index = 35,
    label = "C2H6S + CH3-2 <=> CH4S-3 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9810,'cm^3/(mol*s)'), n=2.55, Ea=(48.9528,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(CsHH);CsJ-HHH
""",
)

entry(
    index = 36,
    label = "C3H8S + CH3-2 <=> CH4S-3 + C3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5340,'cm^3/(mol*s)'), n=2.54, Ea=(44.7688,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(CsCsH);CsJ-HHH
""",
)

entry(
    index = 37,
    label = "C4H10S + CH3-2 <=> CH4S-3 + C4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+06,'cm^3/(mol*s)'), n=1.59, Ea=(38.4928,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(CsCsCs);CsJ-HHH
""",
)

entry(
    index = 38,
    label = "C2H4S + CH3-2 <=> CH4S-3 + C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(43200,'cm^3/(mol*s)'), n=2.43, Ea=(86.6506,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCds(H);CsJ-HHH
""",
)

entry(
    index = 39,
    label = "C3H6S + CH3-2 <=> CH4S-3 + C3H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(96.1,'cm^3/(mol*s)'), n=3.24, Ea=(87.1946,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCds(Cs);CsJ-HHH
""",
)

entry(
    index = 40,
    label = "C3H6S-2 + CH3-2 <=> CH4S-3 + C3H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2720,'cm^3/(mol*s)'), n=2.64, Ea=(34.3088,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(CdHH);CsJ-HHH
""",
)

entry(
    index = 41,
    label = "C4H8S + CH3-2 <=> CH4S-3 + C4H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3420,'cm^3/(mol*s)'), n=2.69, Ea=(30.5432,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(CdCsH);CsJ-HHH
""",
)

entry(
    index = 42,
    label = "C5H10S + CH3-2 <=> CH4S-3 + C5H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9750,'cm^3/(mol*s)'), n=2.63, Ea=(28.0328,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(CdCsCs);CsJ-HHH
""",
)

entry(
    index = 43,
    label = "C3H4S + CH3-2 <=> CH4S-3 + C3H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3470,'cm^3/(mol*s)'), n=2.64, Ea=(34.7272,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(CtHH);CsJ-HHH
""",
)

entry(
    index = 44,
    label = "C4H6S + CH3-2 <=> CH4S-3 + C4H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7000,'cm^3/(mol*s)'), n=2.65, Ea=(30.1248,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(CtCsH);CsJ-HHH
""",
)

entry(
    index = 45,
    label = "C5H8S + CH3-2 <=> CH4S-3 + C5H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2910,'cm^3/(mol*s)'), n=2.6, Ea=(28.4512,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(CtCsCs);CsJ-HHH
""",
)

entry(
    index = 46,
    label = "H + CH4S2 <=> H2S2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.44e+07,'cm^3/(mol*s)'), n=1.64, Ea=(24.2672,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-S2s(H)Cs(HHH);HJ
""",
)

entry(
    index = 47,
    label = "H + C2H6S2 <=> CH4S2-2 + CH3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.494e+08,'cm^3/(mol*s)'), n=1.66, Ea=(21.3384,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-S2s(Cs)Cs(HHH);HJ
""",
)

entry(
    index = 48,
    label = "H + H2S2-2 <=> H2S + HS",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.086e+09,'cm^3/(mol*s)'), n=1.56, Ea=(3.3472,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HSs(H);HJ
""",
)

entry(
    index = 49,
    label = "H + CH4S2-3 <=> CH4S-2 + HS",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.07e+08,'cm^3/(mol*s)'), n=1.6, Ea=(3.7656,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)S2s(H);HJ
""",
)

entry(
    index = 50,
    label = "H + CH4S2-4 <=> H2S + CH3S",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.03e+09,'cm^3/(mol*s)'), n=1.54, Ea=(3.7656,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HSs(Cs);HJ
""",
)

entry(
    index = 51,
    label = "H + C2H6S2-2 <=> CH4S-2 + CH3S",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.062e+09,'cm^3/(mol*s)'), n=1.6, Ea=(3.7656,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)S2s(Cs);HJ
""",
)

entry(
    index = 52,
    label = "H2S2-2 + CH3-2 <=> CH4S-3 + HS",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(586000,'cm^3/(mol*s)'), n=1.72, Ea=(12.1336,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HSs(H);CsJ-HHH
""",
)

entry(
    index = 53,
    label = "CH4S2-4 + CH3-2 <=> CH4S-3 + CH3S",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3570,'cm^3/(mol*s)'), n=2.63, Ea=(17.1544,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HSs(Cs);CsJ-HHH
""",
)

entry(
    index = 54,
    label = "CH4S2-3 + CH3-2 <=> C2H6S-4 + HS",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2020,'cm^3/(mol*s)'), n=2.72, Ea=(16.3176,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)S2s(H);CsJ-HHH
""",
)

entry(
    index = 55,
    label = "CH3-2 + C2H6S2-2 <=> C2H6S-4 + CH3S",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(10260,'cm^3/(mol*s)'), n=2.66, Ea=(19.6648,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)S2s(Cs);CsJ-HHH
""",
)

entry(
    index = 56,
    label = "H + H2S3 <=> H2S2 + HS",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(6.94e+08,'cm^3/(mol*s)'), n=1.64, Ea=(7.5312,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-S2s(H)S2s(H);HJ
""",
)

entry(
    index = 57,
    label = "H + H2S3-2 <=> H2S + HS2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.68e+09,'cm^3/(mol*s)'), n=1.56, Ea=(2.092,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HSs(S2s);HJ
""",
)

entry(
    index = 58,
    label = "H + CH4S3 <=> CH4S2-2 + HS",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.14e+08,'cm^3/(mol*s)'), n=1.63, Ea=(6.276,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-S2s(Cs)S2s(H);HJ
""",
)

entry(
    index = 59,
    label = "H + CH4S3-2 <=> CH4S-2 + HS2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.07e+08,'cm^3/(mol*s)'), n=1.58, Ea=(4.184,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)S2s(S2s);HJ
""",
)

entry(
    index = 60,
    label = "H + CH4S3-3 <=> H2S3-3 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.23e+07,'cm^3/(mol*s)'), n=1.64, Ea=(21.3384,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-S2s(S2s)Cs(HHH);HJ
""",
)

entry(
    index = 61,
    label = "H + CH4S3-4 <=> H2S2 + CH3S",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.8e+08,'cm^3/(mol*s)'), n=1.66, Ea=(8.368,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-S2s(H)S2s(Cs);HJ
""",
)

entry(
    index = 62,
    label = "H + C2H6S3 <=> CH4S2-2 + CH3S",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(7.92e+08,'cm^3/(mol*s)'), n=1.66, Ea=(6.6944,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-S2s(Cs)S2s(Cs);HJ
""",
)

entry(
    index = 63,
    label = "H2S3 + CH3-2 <=> CH4S2-5 + HS",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4820,'cm^3/(mol*s)'), n=2.7, Ea=(15.8992,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-S2s(H)S2s(H);CsJ-HHH
""",
)

entry(
    index = 64,
    label = "H2S3-2 + CH3-2 <=> CH4S-3 + HS2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(21400,'cm^3/(mol*s)'), n=2.68, Ea=(7.1128,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HSs(S2s);CsJ-HHH
""",
)

entry(
    index = 65,
    label = "CH4S3-4 + CH3-2 <=> CH4S2-5 + CH3S",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3560,'cm^3/(mol*s)'), n=2.61, Ea=(21.7568,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-S2s(H)S2s(Cs);CsJ-HHH
""",
)

entry(
    index = 66,
    label = "CH4S3-2 + CH3-2 <=> C2H6S-4 + HS2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3850,'cm^3/(mol*s)'), n=2.69, Ea=(6.6944,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)S2s(S2s);CsJ-HHH
""",
)

entry(
    index = 67,
    label = "CH4S3 + CH3-2 <=> C2H6S2-3 + HS",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2490,'cm^3/(mol*s)'), n=2.69, Ea=(15.4808,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-S2s(Cs)S2s(H);CsJ-HHH
""",
)

entry(
    index = 68,
    label = "CH3-2 + C2H6S3 <=> C2H6S2-3 + CH3S",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(7420,'cm^3/(mol*s)'), n=2.65, Ea=(21.3384,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-S2s(Cs)S2s(Cs);CsJ-HHH
""",
)

entry(
    index = 69,
    label = "H2S-2 + CH3-2 <=> CH4S-3 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2960,'cm^3/(mol*s)'), n=2.72, Ea=(80.7512,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HH;CsJ-HHH
""",
)

entry(
    index = 70,
    label = "H2S-2 + C2H5-2 <=> C2H6S-5 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(20.4,'cm^3/(mol*s)'), n=2.96, Ea=(78.6592,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HH;CsJ-CsHH
""",
)

entry(
    index = 71,
    label = "H2S-2 + C3H7-2 <=> C3H8S-5 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.964,'cm^3/(mol*s)'), n=3.24, Ea=(77.404,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HH;CsJ-CsCsH
""",
)

entry(
    index = 72,
    label = "H2S-2 + C4H9-2 <=> C4H10S-5 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.1678,'cm^3/(mol*s)'), n=3.51, Ea=(76.1488,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HH;CsJ-CsCsCs
""",
)

entry(
    index = 73,
    label = "H2S-2 + C2H3-2 <=> C2H4S-3 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(12.86,'cm^3/(mol*s)'), n=3.21, Ea=(34.3088,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HH;CdsJ-H
""",
)

entry(
    index = 74,
    label = "H2S-2 + C3H5-3 <=> C3H6S-7 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.434,'cm^3/(mol*s)'), n=3.37, Ea=(40.5848,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HH;CdsJ-Cs
""",
)

entry(
    index = 75,
    label = "H2S-2 + C3H5-4 <=> C3H6S-8 + H-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(62,'cm^3/(mol*s)'), n=3.29, Ea=(133.051,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HH;CsJ-CdHH
""",
)

entry(
    index = 76,
    label = "H2S-2 + C4H7-2 <=> C4H8S-7 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(5.08,'cm^3/(mol*s)'), n=3.35, Ea=(134.306,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HH;CsJ-CdCsH
""",
)

entry(
    index = 77,
    label = "H2S-2 + C5H9-2 <=> C5H10S-5 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.92,'cm^3/(mol*s)'), n=3.41, Ea=(135.562,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HH;CsJ-CdCsCs
""",
)

entry(
    index = 78,
    label = "H2S-2 + C3H3-2 <=> C3H4S-3 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(58.6,'cm^3/(mol*s)'), n=3.13, Ea=(130.959,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HH;CsJ-CtHH
""",
)

entry(
    index = 79,
    label = "H2S-2 + C4H5-2 <=> C4H6S-5 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.92,'cm^3/(mol*s)'), n=3.23, Ea=(130.541,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HH;CsJ-CtCsH
""",
)

entry(
    index = 80,
    label = "H2S-2 + C5H7-2 <=> C5H8S-5 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.41,'cm^3/(mol*s)'), n=3.46, Ea=(130.541,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HH;CsJ-CtCsCs
""",
)

entry(
    index = 81,
    label = "CH4S-4 + CH3-2 <=> C2H6S-4 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(41.9,'cm^3/(mol*s)'), n=2.89, Ea=(65.6888,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)H;CsJ-HHH
""",
)

entry(
    index = 82,
    label = "CH4S-4 + C2H5-2 <=> C3H8S-6 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.963,'cm^3/(mol*s)'), n=3.09, Ea=(65.6888,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)H;CsJ-CsHH
""",
)

entry(
    index = 83,
    label = "CH4S-4 + C3H7-2 <=> C4H10S-6 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0719,'cm^3/(mol*s)'), n=3.31, Ea=(66.944,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)H;CsJ-CsCsH
""",
)

entry(
    index = 84,
    label = "CH4S-4 + C4H9-2 <=> C5H12S-3 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00752,'cm^3/(mol*s)'), n=3.43, Ea=(69.4544,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)H;CsJ-CsCsCs
""",
)

entry(
    index = 85,
    label = "C2H3-2 + CH4S-4 <=> C3H6S-9 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(34.6,'cm^3/(mol*s)'), n=2.64, Ea=(29.7064,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)H;CdsJ-H
""",
)

entry(
    index = 86,
    label = "CH4S-4 + C3H5-3 <=> C4H8S-8 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.807,'cm^3/(mol*s)'), n=3.02, Ea=(29.7064,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)H;CdsJ-Cs
""",
)

entry(
    index = 87,
    label = "CH4S-4 + C3H5-4 <=> C4H8S-9 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.56,'cm^3/(mol*s)'), n=3.29, Ea=(118.826,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)H;CsJ-CdHH
""",
)

entry(
    index = 88,
    label = "CH4S-4 + C4H7-2 <=> C5H10S-6 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.25,'cm^3/(mol*s)'), n=3.4, Ea=(118.407,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)H;CsJ-CdCsH
""",
)

entry(
    index = 89,
    label = "CH4S-4 + C5H9-2 <=> C6H12S-3 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0101,'cm^3/(mol*s)'), n=3.51, Ea=(120.499,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)H;CsJ-CdCsCs
""",
)

entry(
    index = 90,
    label = "C3H3-2 + CH4S-4 <=> C4H6S-6 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.33,'cm^3/(mol*s)'), n=3.3, Ea=(112.968,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)H;CsJ-CtHH
""",
)

entry(
    index = 91,
    label = "C4H5-2 + CH4S-4 <=> C5H8S-6 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0674,'cm^3/(mol*s)'), n=3.5, Ea=(111.294,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)H;CsJ-CtCsH
""",
)

entry(
    index = 92,
    label = "C5H7-2 + CH4S-4 <=> C6H10S-3 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00339,'cm^3/(mol*s)'), n=3.67, Ea=(113.386,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)H;CsJ-CtCsCs
""",
)

entry(
    index = 93,
    label = "C2H6S-6 + CH3-2 <=> C3H8S-7 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(48.5,'cm^3/(mol*s)'), n=2.83, Ea=(65.6888,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(CsHH)H;CsJ-HHH
""",
)

entry(
    index = 94,
    label = "C3H8S-8 + CH3-2 <=> C4H10S-7 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(26.7,'cm^3/(mol*s)'), n=2.86, Ea=(69.036,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(CsCsH)H;CsJ-HHH
""",
)

entry(
    index = 95,
    label = "C4H10S-8 + CH3-2 <=> C5H12S-4 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(25.1,'cm^3/(mol*s)'), n=2.82, Ea=(74.8936,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(CsCsCs)H;CsJ-HHH
""",
)

entry(
    index = 96,
    label = "C2H4S-4 + CH3-2 <=> C3H6S-10 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(21.6,'cm^3/(mol*s)'), n=2.93, Ea=(64.0152,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cds(H)H;CsJ-HHH
""",
)

entry(
    index = 97,
    label = "C3H6S-11 + CH3-2 <=> C4H8S-10 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(17,'cm^3/(mol*s)'), n=2.82, Ea=(71.128,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cds(Cs)H;CsJ-HHH
""",
)

entry(
    index = 98,
    label = "C3H6S-12 + CH3-2 <=> C4H8S-11 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(38.7,'cm^3/(mol*s)'), n=2.87, Ea=(64.0152,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(CdHH)H;CsJ-HHH
""",
)

entry(
    index = 99,
    label = "C4H8S-12 + CH3-2 <=> C5H10S-7 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(35,'cm^3/(mol*s)'), n=2.79, Ea=(66.944,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(CdCsH)H;CsJ-HHH
""",
)

entry(
    index = 100,
    label = "C5H10S-8 + CH3-2 <=> C6H12S-4 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(37,'cm^3/(mol*s)'), n=2.83, Ea=(71.128,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(CdCsCs)H;CsJ-HHH
""",
)

entry(
    index = 101,
    label = "C3H4S-4 + CH3-2 <=> C4H6S-7 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(45,'cm^3/(mol*s)'), n=2.88, Ea=(64.0152,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(CtHH)H;CsJ-HHH
""",
)

entry(
    index = 102,
    label = "C4H6S-8 + CH3-2 <=> C5H8S-7 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(60.8,'cm^3/(mol*s)'), n=2.83, Ea=(63.1784,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(CtCsH)H;CsJ-HHH
""",
)

entry(
    index = 103,
    label = "C5H8S-8 + CH3-2 <=> C6H10S-4 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(16.6,'cm^3/(mol*s)'), n=2.91, Ea=(67.7808,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(CtCsCs)H;CsJ-HHH
""",
)

entry(
    index = 104,
    label = "CH4S + C2H5-2 <=> C2H6S-5 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(73.3,'cm^3/(mol*s)'), n=2.76, Ea=(48.116,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(HHH);CsJ-CsHH
""",
)

entry(
    index = 105,
    label = "CH4S + C3H7-2 <=> C3H8S-5 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.62,'cm^3/(mol*s)'), n=2.96, Ea=(44.7688,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(HHH);CsJ-CsCsH
""",
)

entry(
    index = 106,
    label = "CH4S + C4H9-2 <=> C4H10S-5 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(39.6,'cm^3/(mol*s)'), n=2.74, Ea=(39.748,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(HHH);CsJ-CsCsCs
""",
)

entry(
    index = 107,
    label = "C2H3-2 + CH4S <=> C2H4S-3 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(245,'cm^3/(mol*s)'), n=2.88, Ea=(21.3384,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(HHH);CdsJ-H
""",
)

entry(
    index = 108,
    label = "CH4S + C3H5-3 <=> C3H6S-7 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(13.4,'cm^3/(mol*s)'), n=2.97, Ea=(18.828,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(HHH);CdsJ-Cs
""",
)

entry(
    index = 109,
    label = "CH4S + C3H5-4 <=> C3H6S-8 + CH3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(169.2,'cm^3/(mol*s)'), n=3.04, Ea=(94.14,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(HHH);CsJ-CdHH
""",
)

entry(
    index = 110,
    label = "CH4S + C4H7-2 <=> C4H8S-7 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.56,'cm^3/(mol*s)'), n=3.23, Ea=(91.6296,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(HHH);CsJ-CdCsH
""",
)

entry(
    index = 111,
    label = "CH4S + C5H9-2 <=> C5H10S-5 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.93,'cm^3/(mol*s)'), n=3.25, Ea=(92.048,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(HHH);CsJ-CdCsCs
""",
)

entry(
    index = 112,
    label = "C3H3-2 + CH4S <=> C3H4S-3 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(103,'cm^3/(mol*s)'), n=2.96, Ea=(88.7008,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(HHH);CsJ-CtHH
""",
)

entry(
    index = 113,
    label = "C4H5-2 + CH4S <=> C4H6S-5 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.33,'cm^3/(mol*s)'), n=3.16, Ea=(85.772,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(HHH);CsJ-CtCsH
""",
)

entry(
    index = 114,
    label = "C5H7-2 + CH4S <=> C5H8S-5 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.36,'cm^3/(mol*s)'), n=3.32, Ea=(85.3536,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(HHH);CsJ-CtCsCs
""",
)

entry(
    index = 115,
    label = "H2S2-3 + CH3-2 <=> CH4S2-5 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(88.8,'cm^3/(mol*s)'), n=3.04, Ea=(69.4544,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-S2s(H)H;CsJ-HHH
""",
)

entry(
    index = 116,
    label = "CH4S2-6 + CH3-2 <=> C2H6S2-3 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(11.3,'cm^3/(mol*s)'), n=3.03, Ea=(66.944,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-S2s(Cs)H;CsJ-HHH
""",
)

entry(
    index = 117,
    label = "HS-2 + H2S-2 <=> H2S2-4 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1608,'cm^3/(mol*s)'), n=3.08, Ea=(111.713,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HH;SsJ-H
""",
)

entry(
    index = 118,
    label = "HS-2 + CH4S-4 <=> CH4S2-7 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(75.2,'cm^3/(mol*s)'), n=3.3, Ea=(109.035,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)H;SsJ-H
""",
)

entry(
    index = 119,
    label = "H2S-2 + CH3S-2 <=> CH4S2-8 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.5,'cm^3/(mol*s)'), n=4.01, Ea=(103.763,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HH;SsJ-Cs
""",
)

entry(
    index = 120,
    label = "CH4S-4 + CH3S-2 <=> C2H6S2-4 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0263,'cm^3/(mol*s)'), n=4.22, Ea=(85.6883,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)H;SsJ-Cs
""",
)

entry(
    index = 121,
    label = "HS-2 + CH4S <=> H2S2-4 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(999,'cm^3/(mol*s)'), n=3.08, Ea=(54.7686,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """CAC calc CBS-QB3 1dhr""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(HHH);SsJ-H
""",
)

entry(
    index = 122,
    label = "CH4S + CH3S-2 <=> CH4S2-8 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.28,'cm^3/(mol*s)'), n=3.85, Ea=(52.7184,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(HHH);SsJ-Cs
""",
)

entry(
    index = 123,
    label = "HS-2 + C2H6S-2 <=> CH4S2-7 + CH3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3540,'cm^3/(mol*s)'), n=3.03, Ea=(53.9736,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)Cs(HHH);SsJ-H
""",
)

entry(
    index = 124,
    label = "CH3S-2 + C2H6S-2 <=> C2H6S2-4 + CH3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.34,'cm^3/(mol*s)'), n=3.89, Ea=(50.208,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)Cs(HHH);SsJ-Cs
""",
)

entry(
    index = 125,
    label = "HS-2 + H2S2-3 <=> H2S3-4 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(53.4,'cm^3/(mol*s)'), n=3.36, Ea=(109.035,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-S2s(H)H;SsJ-H
""",
)

entry(
    index = 126,
    label = "HS2-2 + H2S-2 <=> H2S3-5 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.718,'cm^3/(mol*s)'), n=3.89, Ea=(157.318,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HH;SsJ-S2s
""",
)

entry(
    index = 127,
    label = "HS-2 + CH4S2-6 <=> CH4S3-5 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(83.6,'cm^3/(mol*s)'), n=3.33, Ea=(109.035,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-S2s(Cs)H;SsJ-H
""",
)

entry(
    index = 128,
    label = "HS2-2 + CH4S-4 <=> CH4S3-6 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0413,'cm^3/(mol*s)'), n=4.06, Ea=(153.009,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)H;SsJ-S2s
""",
)

entry(
    index = 129,
    label = "H2S3-6 + CH3-2 <=> CH4S3-7 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(137,'cm^3/(mol*s)'), n=3.02, Ea=(62.76,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-S2s(S2s)H;CsJ-HHH
""",
)

entry(
    index = 130,
    label = "H2S2-3 + CH3S-2 <=> CH4S3-8 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.0404,'cm^3/(mol*s)'), n=4.3, Ea=(85.6883,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-S2s(H)H;SsJ-Cs
""",
)

entry(
    index = 131,
    label = "CH4S2-6 + CH3S-2 <=> C2H6S3-2 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0168,'cm^3/(mol*s)'), n=4.25, Ea=(85.6883,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-S2s(Cs)H;SsJ-Cs
""",
)

entry(
    index = 132,
    label = "HS-2 + CH4S2 <=> H2S3-4 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(467,'cm^3/(mol*s)'), n=3, Ea=(53.9736,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-S2s(H)Cs(HHH);SsJ-H
""",
)

entry(
    index = 133,
    label = "HS2-2 + CH4S <=> H2S3-5 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.08,'cm^3/(mol*s)'), n=3.79, Ea=(97.4872,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(HHH);SsJ-S2s
""",
)

entry(
    index = 134,
    label = "CH4S2 + CH3S-2 <=> CH4S3-8 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.923,'cm^3/(mol*s)'), n=3.83, Ea=(48.116,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-S2s(H)Cs(HHH);SsJ-Cs
""",
)

entry(
    index = 135,
    label = "HS2-2 + C2H6S-2 <=> CH4S3-6 + CH3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.214,'cm^3/(mol*s)'), n=3.8, Ea=(107.11,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(HHH)Cs(HHH);SsJ-S2s
""",
)

entry(
    index = 136,
    label = "HS-2 + C2H6S2 <=> CH4S3-5 + CH3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4740,'cm^3/(mol*s)'), n=3, Ea=(48.9528,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-S2s(Cs)Cs(HHH);SsJ-H
""",
)

entry(
    index = 137,
    label = "CH3S-2 + C2H6S2 <=> C2H6S3-2 + CH3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.14,'cm^3/(mol*s)'), n=3.86, Ea=(43.0952,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-S2s(Cs)Cs(HHH);SsJ-Cs
""",
)

entry(
    index = 138,
    label = "H + C4H10S-9 <=> C2H6S-3 + C2H5",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.54e+07,'cm^3/(mol*s)'), n=2.26, Ea=(16.0247,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """CAC CBS-QB3 1dhr""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-Cs(CsHH)Cs(CsHH);HJ
""",
)

entry(
    index = 139,
    label = "H + CH2OS <=> H2S + CHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.26e+09,'cm^3/(mol*s)'), n=1.46, Ea=(13.1378,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """CAC CBS-QB3 1dhr""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCO;HJ
""",
)

entry(
    index = 140,
    label = "CH2OS + CH3-2 <=> CH4S-3 + CHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.88e+06,'cm^3/(mol*s)'), n=1.4, Ea=(44.183,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """CAC CBS-QB3 1dhr""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCO;CsJ-HHH
""",
)

entry(
    index = 141,
    label = "H + C2H6OS <=> H2S + C2H5O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.91e+09,'cm^3/(mol*s)'), n=1.32, Ea=(12.7612,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """CAC CBS-QB3 1dhr""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(CsOsH);HJ
""",
)

entry(
    index = 142,
    label = "C2H6OS + CH3-2 <=> CH4S-3 + C2H5O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00296,'cm^3/(mol*s)'), n=5.57, Ea=(35.4385,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """CAC CBS-QB3 1dhr""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(CsOsH);CsJ-HHH
""",
)

entry(
    index = 143,
    label = "C2H6OS + CH3-2 <=> CH4S-3 + C2H5O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00296,'cm^3/(mol*s)'), n=5.57, Ea=(35.4385,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """based on 157""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(CsOsH);CJ
""",
)

entry(
    index = 144,
    label = "HS-2 + C2H6OS <=> H2S2-4 + C2H5O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1180,'cm^3/(mol*s)'), n=3, Ea=(55.6472,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """based on CAC's 131 calc""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(CsOsH);SsJ-H
""",
)

entry(
    index = 145,
    label = "H2S2-2 + C3H5-4 <=> C3H6S-8 + HS",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(3720,'cm^3/(mol*s)'), n=2.61, Ea=(42.1329,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """CAC CBS-QB3, HO approx""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HSs(H);CsJ-CdHH
""",
)

entry(
    index = 146,
    label = "C2H6S + CH3S-2 <=> CH4S2-8 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(72.5,'cm^3/(mol*s)'), n=3.21, Ea=(47.9068,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """CAC CBS-QB3 1dhr""",
    longDesc = 
"""
Converted to training reaction from rate rule: S-HCs(CsHH);SsJ-Cs
""",
)

entry(
    index = 147,
    label = "CH4S + CH3-2 <=> CH4S-3 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5130,'cm^3/(mol*s)'), n=2.54, Ea=(56.0656,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 6,
    shortDesc = """Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: S-HCs(HHH);CsJ-HHH
""",
)

