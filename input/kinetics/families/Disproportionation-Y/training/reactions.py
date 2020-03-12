#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation-Y/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "CHF2-CH2_r423 + H_r1 <=> CDCF_p23 + F_p41",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.24e+16,'cm^3/(mol*s)'), n=-0.933, Ea=(880,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 1,
    label = "CHFCH[Z]_r423 + H_r1 <=> C#C_p23 + F_p41",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.98e+20,'cm^3/(mol*s)'), n=-2.31, Ea=(1940,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 2,
    label = "CF2CH_r423 + H_r1 <=> C#CF_p23 + F_p41",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.98e+20,'cm^3/(mol*s)'), n=-2.31, Ea=(1940,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 3,
    label = "CH2F-CHF_r423 + H_r1 <=> CDCF_p23 + F_p41",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.06e+23,'cm^3/(mol*s)'), n=-3.23, Ea=(2280,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 4,
    label = "CH2F-CH2_r423 + H_r1 <=> CDC_p23 + F_p41",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.44e+20,'cm^3/(mol*s)'), n=-2.12, Ea=(1730,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 5,
    label = "CHFCF[Z]_r423 + H_r1 <=> C#CF_p23 + F_p41",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.98e+20,'cm^3/(mol*s)'), n=-2.31, Ea=(1940,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 6,
    label = "CHFCCF3_r423 + H_r1 <=> F_p41 + C#CC(F)(F)F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+13,'cm^3/(mol*s)'), n=0, Ea=(2000,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 7,
    label = "CF3-CHF_r423 + H_r1 <=> FCDC(F)F_p23 + F_p41",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.56e+24,'cm^3/(mol*s)'), n=-3.57, Ea=(4225,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 8,
    label = "CF3O_r423 + H_r1 <=> ODC(F)F_p23 + F_p41",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 9,
    label = "CF2CF_r423 + H_r1 <=> FC#CF_p23 + F_p41",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.98e+20,'cm^3/(mol*s)'), n=-2.31, Ea=(1940,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 10,
    label = "CH2F-CF2_r423 + H_r1 <=> CDC(F)F_p23 + F_p41",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.36e+19,'cm^3/(mol*s)'), n=-2.26, Ea=(1660,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 11,
    label = "CHF2-CHF_r423 + H_r1 <=> FCDCF_p23 + F_p41",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.86e+20,'cm^3/(mol*s)'), n=-2.29, Ea=(1750,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 12,
    label = "CF3-CF2_r423 + H_r1 <=> FC(F)DC(F)F_p23 + F_p41",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.41e+21,'cm^3/(mol*s)'), n=-2.4, Ea=(3630,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 13,
    label = "CHF2-CF2_r423 + H_r1 <=> FCDC(F)F_p23 + F_p41",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.81e+22,'cm^3/(mol*s)'), n=-2.92, Ea=(3070,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 14,
    label = "CF3O_r423 + F_r1 <=> FF_p41 + ODC(F)F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+13,'cm^3/(mol*s)'), n=0, Ea=(7000,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 15,
    label = "CH-CFCF3_r423 + H_r1 <=> F_p41 + C#CC(F)(F)F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+13,'cm^3/(mol*s)'), n=0, Ea=(2000,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 16,
    label = "CF3-CH2_r423 + H_r1 <=> CDC(F)F_p23 + F_p41",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.12e+21,'cm^3/(mol*s)'), n=-2.27, Ea=(2240,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

