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

entry(
    index = 17,
    label = "CHF2-CH2_r423 + H_r1 <=> F_p41 + C2H3F",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(5.24e+16,'cm^3/(mol*s)'), n=-0.933, Ea=(880,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CHF2-CH2 + H <=> CH2:CHF + HF""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CHF2-CH2 + H <=> CH2:CHF + HF
""",
)

entry(
    index = 18,
    label = "CH2F-CF2_r423 + H_r1 <=> F_p41 + C2H2F2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.36e+19,'cm^3/(mol*s)'), n=-2.26, Ea=(1660,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CH2F-CF2 + H <=> CH2:CF2 + HF""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CH2F-CF2 + H <=> CH2:CF2 + HF
""",
)

entry(
    index = 19,
    label = "CF3-CHF_r423 + H_r1 <=> F_p41 + C2HF3",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(6.56e+24,'cm^3/(mol*s)'), n=-3.57, Ea=(4225,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CF3-CHF + H <=> CHF:CF2 + HF""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CF3-CHF + H <=> CHF:CF2 + HF
""",
)

entry(
    index = 20,
    label = "CF2CH_r423 + H_r1 <=> F_p41 + C2HF",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(5.98e+20,'cm^3/(mol*s)'), n=-2.31, Ea=(1940,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CF2:CH + H <=> C2HF + HF""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CF2:CH + H <=> C2HF + HF
""",
)

# entry(
#     index = 21,
#     label = "CO + FF_p41 <=> F_r1 + CFO",
#     degeneracy = 1.0,
#     kinetics = Arrhenius(A=(4.7e+11,'cm^3/(mol*s)'), n=0, Ea=(13500,'cal/mol'), T0=(1,'K')),
#     rank = 10,
#     shortDesc = """The chemkin file reaction is F2 + CO <=> CF:O + F""",
#     longDesc = 
# """
# Training reaction from kinetics library: 2-BTP
# Original entry: F2 + CO <=> CF:O + F
# """,
# )

entry(
    index = 22,
    label = "CDC_p23 + FF_p41 <=> F_r1 + CH2F-CH2_r423",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.8e+10,'cm^3/(mol*s)'), n=0, Ea=(4590,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is C2H4 + F2 <=> CH2F-CH2 + F""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: C2H4 + F2 <=> CH2F-CH2 + F
""",
)

