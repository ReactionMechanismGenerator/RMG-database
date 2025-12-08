#!/usr/bin/env python
# encoding: utf-8

name = "1,3_sigmatropic_rearrangement/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(8.40702e+19,'s^-1'), n=-1.98382, w0=(667.083,'kJ/mol'), E0=(310.818,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3139855283509312, var=131.7192055374877, Tref=1000.0, N=36, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 36 training reactions at node Root
    Total Standard Deviation in ln(k): 23.797049920643087"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root
Total Standard Deviation in ln(k): 23.797049920643087""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root
Total Standard Deviation in ln(k): 23.797049920643087
""",
)

entry(
    index = 2,
    label = "Root_1R!H-inRing",
    kinetics = ArrheniusBM(A=(9.68473e+31,'s^-1'), n=-4.91457, w0=(679.848,'kJ/mol'), E0=(347.452,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15167603771058488, var=187.36457689819287, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H-inRing',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H-inRing
    Total Standard Deviation in ln(k): 27.8221460545111"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 27.8221460545111""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 27.8221460545111
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(1.14057e+14,'s^-1'), n=-0.428571, w0=(670.804,'kJ/mol'), E0=(294.736,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2913023167145375, var=130.36009114973498, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_N-1R!H-inRing',), comment="""BM rule fitted to 28 training reactions at node Root_N-1R!H-inRing
    Total Standard Deviation in ln(k): 23.621047022754347"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 23.621047022754347""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 23.621047022754347
""",
)

entry(
    index = 4,
    label = "Root_1R!H-inRing_2R!H->N",
    kinetics = ArrheniusBM(A=(3.65255e+26,'s^-1'), n=-3.3137, w0=(772.948,'kJ/mol'), E0=(375.877,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.034333901676506205, var=90.45906957712619, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->N
    Total Standard Deviation in ln(k): 19.15329598623494"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 19.15329598623494""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 19.15329598623494
""",
)

entry(
    index = 5,
    label = "Root_1R!H-inRing_N-2R!H->N",
    kinetics = ArrheniusBM(A=(2.27467e+41,'s^-1'), n=-7.6464, w0=(670.125,'kJ/mol'), E0=(328.774,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.37404021737654225, var=394.1054056822035, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-2R!H->N
    Total Standard Deviation in ln(k): 40.73797710418308"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 40.73797710418308""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 40.73797710418308
""",
)

entry(
    index = 6,
    label = "Root_N-1R!H-inRing_2R!H->N",
    kinetics = Arrhenius(A=(2.6203e+13,'s^-1'), n=0.0689932, Ea=(168.747,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-2.530556571873429e-16, var=72.89065172155313, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R!H-inRing_2R!H->N
    Total Standard Deviation in ln(k): 17.115630653682903"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 17.115630653682903""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 17.115630653682903
""",
)

entry(
    index = 7,
    label = "Root_N-1R!H-inRing_N-2R!H->N",
    kinetics = ArrheniusBM(A=(69845.3,'s^-1'), n=2.11188, w0=(677.5,'kJ/mol'), E0=(292.139,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.027212390969420346, var=103.94594876747756, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N',), comment="""BM rule fitted to 20 training reactions at node Root_N-1R!H-inRing_N-2R!H->N
    Total Standard Deviation in ln(k): 20.50742600185753"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-1R!H-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 20.50742600185753""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-1R!H-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 20.50742600185753
""",
)

entry(
    index = 8,
    label = "Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(7.25006e+21,'s^-1'), n=-1.98514, w0=(799.113,'kJ/mol'), E0=(384.306,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.049872472795071246, var=81.0292335057579, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 18.171178980893234"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 18.171178980893234""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 18.171178980893234
""",
)

entry(
    index = 9,
    label = "Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_N-5R!H->C",
    kinetics = Arrhenius(A=(3.92014e+10,'s^-1'), n=1.31782, Ea=(406.92,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_1R!H-inRing_N-2R!H->N_4R!H->N",
    kinetics = Arrhenius(A=(3.23202e+11,'s^-1'), n=0.959257, Ea=(243.463,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_4R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_1R!H-inRing_N-2R!H->N_N-4R!H->N",
    kinetics = ArrheniusBM(A=(1.10563e+44,'s^-1'), n=-8.43416, w0=(707,'kJ/mol'), E0=(370.69,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.44094775783571755, var=494.57825704381315, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_N-4R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N
    Total Standard Deviation in ln(k): 45.69144381923641"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N
Total Standard Deviation in ln(k): 45.69144381923641""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N
Total Standard Deviation in ln(k): 45.69144381923641
""",
)

entry(
    index = 12,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->N",
    kinetics = Arrhenius(A=(3.05043e+14,'s^-1'), n=-0.280572, Ea=(74.1506,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_N-1R!H-inRing_2R!H->N_N-4R!H->N",
    kinetics = ArrheniusBM(A=(8.52719e-54,'s^-1'), n=19.1249, w0=(667.571,'kJ/mol'), E0=(0.951684,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.330780811704509, var=87.85776473697601, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_N-4R!H->N',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N
    Total Standard Deviation in ln(k): 24.647110824182086"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N
Total Standard Deviation in ln(k): 24.647110824182086""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N
Total Standard Deviation in ln(k): 24.647110824182086
""",
)

entry(
    index = 14,
    label = "Root_N-1R!H-inRing_N-2R!H->N_3R!H->O",
    kinetics = ArrheniusBM(A=(3881.81,'s^-1'), n=2.44739, w0=(700.5,'kJ/mol'), E0=(310.521,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6002066796239935, var=99.00461177453936, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O
    Total Standard Deviation in ln(k): 21.45538374404744"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O
Total Standard Deviation in ln(k): 21.45538374404744""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O
Total Standard Deviation in ln(k): 21.45538374404744
""",
)

entry(
    index = 15,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O",
    kinetics = ArrheniusBM(A=(802611,'s^-1'), n=1.8273, w0=(667.643,'kJ/mol'), E0=(277.601,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5782845303269006, var=149.85227036887014, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O
    Total Standard Deviation in ln(k): 25.993772642551452"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O
Total Standard Deviation in ln(k): 25.993772642551452""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O
Total Standard Deviation in ln(k): 25.993772642551452
""",
)

entry(
    index = 16,
    label = "Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(4.07162e+21,'s^-1'), n=-1.9483, w0=(810.134,'kJ/mol'), E0=(398.112,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22003588140389113, var=198.71575416114501, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 28.812917843504202"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 28.812917843504202""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 28.812917843504202
""",
)

entry(
    index = 17,
    label = "Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-1R!H-R",
    kinetics = Arrhenius(A=(1.61854e+10,'s^-1'), n=0.947053, Ea=(380.965,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C",
    kinetics = Arrhenius(A=(1.42792e+11,'s^-1'), n=1.12171, Ea=(360.677,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C",
    kinetics = Arrhenius(A=(7.48935e+10,'s^-1'), n=1.24936, Ea=(321.691,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_Ext-1R!H-R",
    kinetics = Arrhenius(A=(5.24437e+12,'s^-1'), n=0.139323, Ea=(217.383,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=26.820064402959698, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_Ext-1R!H-R
    Total Standard Deviation in ln(k): 10.382140399071336"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 10.382140399071336""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 10.382140399071336
""",
)

entry(
    index = 21,
    label = "Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_3R!H->N",
    kinetics = ArrheniusBM(A=(3.8336e+16,'s^-1'), n=-0.852118, w0=(615,'kJ/mol'), E0=(312.156,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.384478380813464, var=56.6085302862738, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_3R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_3R!H->N
    Total Standard Deviation in ln(k): 16.049380266806406"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_3R!H->N
Total Standard Deviation in ln(k): 16.049380266806406""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_3R!H->N
Total Standard Deviation in ln(k): 16.049380266806406
""",
)

entry(
    index = 22,
    label = "Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N",
    kinetics = ArrheniusBM(A=(6.31785e-38,'s^-1'), n=14.6824, w0=(707,'kJ/mol'), E0=(12.9877,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.313195670692316, var=61.808893822475234, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N
    Total Standard Deviation in ln(k): 21.573002462549503"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N
Total Standard Deviation in ln(k): 21.573002462549503""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N
Total Standard Deviation in ln(k): 21.573002462549503
""",
)

entry(
    index = 23,
    label = "Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(88.0116,'s^-1'), n=2.82623, w0=(700.5,'kJ/mol'), E0=(296.641,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6063411742792161, var=146.94407085033302, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R
    Total Standard Deviation in ln(k): 25.824967035698478"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 25.824967035698478""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 25.824967035698478
""",
)

entry(
    index = 24,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->N",
    kinetics = ArrheniusBM(A=(2.27357e+12,'s^-1'), n=-0.175689, w0=(707,'kJ/mol'), E0=(140.356,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22902927274512896, var=32.416646910736326, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->N
    Total Standard Deviation in ln(k): 11.989533655349733"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->N
Total Standard Deviation in ln(k): 11.989533655349733""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->N
Total Standard Deviation in ln(k): 11.989533655349733
""",
)

entry(
    index = 25,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N",
    kinetics = ArrheniusBM(A=(5.31438e+06,'s^-1'), n=1.61759, w0=(661.083,'kJ/mol'), E0=(304.931,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.433324903181243, var=101.32009824565873, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N
    Total Standard Deviation in ln(k): 21.267995337567204"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N
Total Standard Deviation in ln(k): 21.267995337567204""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N
Total Standard Deviation in ln(k): 21.267995337567204
""",
)

entry(
    index = 26,
    label = "Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_3R!H->N",
    kinetics = Arrhenius(A=(8.04681e+10,'s^-1'), n=1.21369, Ea=(447.107,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_3R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_N-3R!H->N",
    kinetics = Arrhenius(A=(1.02334e+09,'s^-1'), n=1.56661, Ea=(426.407,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_N-3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_N-3R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_Ext-1R!H-R_2N-inRing",
    kinetics = Arrhenius(A=(2.72427e+12,'s^-1'), n=0.399431, Ea=(242.1,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_Ext-1R!H-R_2N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_Ext-1R!H-R_2N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_Ext-1R!H-R_2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_Ext-1R!H-R_2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_Ext-1R!H-R_N-2N-inRing",
    kinetics = Arrhenius(A=(1.00957e+13,'s^-1'), n=-0.120785, Ea=(192.666,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_Ext-1R!H-R_N-2N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_Ext-1R!H-R_N-2N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_Ext-1R!H-R_N-2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_Ext-1R!H-R_N-2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_3R!H->N_Ext-4BrCClF-R_5R!H->C",
    kinetics = Arrhenius(A=(3.6546e+12,'s^-1'), n=0.372553, Ea=(235.091,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_3R!H->N_Ext-4BrCClF-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_3R!H->N_Ext-4BrCClF-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_3R!H->N_Ext-4BrCClF-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_3R!H->N_Ext-4BrCClF-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_3R!H->N_Ext-4BrCClF-R_N-5R!H->C",
    kinetics = Arrhenius(A=(5.59681e+12,'s^-1'), n=0.174189, Ea=(169.578,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_3R!H->N_Ext-4BrCClF-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_3R!H->N_Ext-4BrCClF-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_3R!H->N_Ext-4BrCClF-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_3R!H->N_Ext-4BrCClF-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N_Ext-4BrCClF-R_5R!H->N",
    kinetics = Arrhenius(A=(1.84179e+16,'s^-1'), n=-0.625332, Ea=(104.652,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N_Ext-4BrCClF-R_5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N_Ext-4BrCClF-R_5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N_Ext-4BrCClF-R_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N_Ext-4BrCClF-R_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N_Ext-4BrCClF-R_N-5R!H->N",
    kinetics = Arrhenius(A=(8.38538e+12,'s^-1'), n=0.316231, Ea=(165.869,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=5.061113143746858e-16, var=10.18594117428569, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N_Ext-4BrCClF-R_N-5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N_Ext-4BrCClF-R_N-5R!H->N
    Total Standard Deviation in ln(k): 6.398196461102977"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N_Ext-4BrCClF-R_N-5R!H->N
Total Standard Deviation in ln(k): 6.398196461102977""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N_Ext-4BrCClF-R_N-5R!H->N
Total Standard Deviation in ln(k): 6.398196461102977
""",
)

entry(
    index = 34,
    label = "Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(1.17226e+07,'s^-1'), n=1.41058, w0=(736.914,'kJ/mol'), E0=(340.775,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4280521057704462, var=124.31920741520162, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 23.428007916211012"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 23.428007916211012""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 23.428007916211012
""",
)

entry(
    index = 35,
    label = "Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    kinetics = Arrhenius(A=(1.575e+06,'s^-1'), n=1.45, Ea=(203.329,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->N_Ext-1R!H-R",
    kinetics = Arrhenius(A=(2.75554e+14,'s^-1'), n=-0.892455, Ea=(121.354,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->N_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->N_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_4R!H->Br",
    kinetics = ArrheniusBM(A=(6.98403e+11,'s^-1'), n=0.407681, w0=(541,'kJ/mol'), E0=(206.795,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005374602454955109, var=0.05576325998065082, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_4R!H->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_4R!H->Br
    Total Standard Deviation in ln(k): 0.4869070930050377"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_4R!H->Br
Total Standard Deviation in ln(k): 0.4869070930050377""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_4R!H->Br
Total Standard Deviation in ln(k): 0.4869070930050377
""",
)

entry(
    index = 38,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br",
    kinetics = ArrheniusBM(A=(1.58091e+07,'s^-1'), n=1.47583, w0=(685.1,'kJ/mol'), E0=(308.741,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3905134384654712, var=98.21980771603684, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br
    Total Standard Deviation in ln(k): 20.849298326830034"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br
Total Standard Deviation in ln(k): 20.849298326830034""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br
Total Standard Deviation in ln(k): 20.849298326830034
""",
)

entry(
    index = 39,
    label = "Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N_Ext-4BrCClF-R_N-5R!H->N_2N-inRing",
    kinetics = Arrhenius(A=(8.05136e+14,'s^-1'), n=-0.0703128, Ea=(172.238,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N_Ext-4BrCClF-R_N-5R!H->N_2N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N_Ext-4BrCClF-R_N-5R!H->N_2N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N_Ext-4BrCClF-R_N-5R!H->N_2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N_Ext-4BrCClF-R_N-5R!H->N_2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N_Ext-4BrCClF-R_N-5R!H->N_N-2N-inRing",
    kinetics = Arrhenius(A=(8.73327e+10,'s^-1'), n=0.702774, Ea=(159.501,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N_Ext-4BrCClF-R_N-5R!H->N_N-2N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N_Ext-4BrCClF-R_N-5R!H->N_N-2N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N_Ext-4BrCClF-R_N-5R!H->N_N-2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->N_N-3R!H->N_Ext-4BrCClF-R_N-5R!H->N_N-2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3.68606e+06,'s^-1'), n=1.59989, w0=(752.551,'kJ/mol'), E0=(342.5,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2231192844612943, var=433.45320073431793, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 42.298261180180546"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 42.298261180180546""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 42.298261180180546
""",
)

entry(
    index = 42,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_4R!H->Br_Ext-2CO-R",
    kinetics = Arrhenius(A=(1.94657e+12,'s^-1'), n=0.28187, Ea=(223.254,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_4R!H->Br_Ext-2CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_4R!H->Br_Ext-2CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_4R!H->Br_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_4R!H->Br_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_4CClF->Cl",
    kinetics = ArrheniusBM(A=(4.2126e+11,'s^-1'), n=0.487024, w0=(583,'kJ/mol'), E0=(230.521,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00544592251535998, var=0.10372712383060487, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_4CClF->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_4CClF->Cl
    Total Standard Deviation in ln(k): 0.6593421453781102"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_4CClF->Cl
Total Standard Deviation in ln(k): 0.6593421453781102""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_4CClF->Cl
Total Standard Deviation in ln(k): 0.6593421453781102
""",
)

entry(
    index = 44,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl",
    kinetics = ArrheniusBM(A=(3.52691e+07,'s^-1'), n=1.36918, w0=(710.625,'kJ/mol'), E0=(311.775,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.34779683837379977, var=97.31678411443004, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl
    Total Standard Deviation in ln(k): 20.650426534724854"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl
Total Standard Deviation in ln(k): 20.650426534724854""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl
Total Standard Deviation in ln(k): 20.650426534724854
""",
)

entry(
    index = 45,
    label = "Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = Arrhenius(A=(7.89e+07,'s^-1'), n=1.5, Ea=(485.946,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_4CClF->Cl_Ext-2CO-R",
    kinetics = Arrhenius(A=(1.046e+12,'s^-1'), n=0.380659, Ea=(252.531,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_4CClF->Cl_Ext-2CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_4CClF->Cl_Ext-2CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_4CClF->Cl_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_4CClF->Cl_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_Ext-2CO-R",
    kinetics = Arrhenius(A=(1.69499e+12,'s^-1'), n=0.570599, Ea=(365.404,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_Ext-2CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_Ext-2CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_2CO->C",
    kinetics = Arrhenius(A=(2.11883e+10,'s^-1'), n=0.811585, Ea=(262.426,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_2CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_2CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_2CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_2CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C",
    kinetics = ArrheniusBM(A=(2.22825e+07,'s^-1'), n=1.41656, w0=(700.5,'kJ/mol'), E0=(311.523,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3304158113394465, var=101.5170646812583, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C
    Total Standard Deviation in ln(k): 21.029034493894162"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C
Total Standard Deviation in ln(k): 21.029034493894162""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C
Total Standard Deviation in ln(k): 21.029034493894162
""",
)

entry(
    index = 50,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R",
    kinetics = ArrheniusBM(A=(162444,'s^-1'), n=1.90885, w0=(700.5,'kJ/mol'), E0=(297.288,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2501112871930188, var=153.21579337651576, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R
    Total Standard Deviation in ln(k): 25.443104748552862"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R
Total Standard Deviation in ln(k): 25.443104748552862""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R
Total Standard Deviation in ln(k): 25.443104748552862
""",
)

entry(
    index = 51,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O",
    kinetics = ArrheniusBM(A=(814.381,'s^-1'), n=2.38084, w0=(700.5,'kJ/mol'), E0=(223.083,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3611790105817507, var=117.41376442524704, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O
    Total Standard Deviation in ln(k): 22.63031955622506"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O
Total Standard Deviation in ln(k): 22.63031955622506""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O
Total Standard Deviation in ln(k): 22.63031955622506
""",
)

entry(
    index = 52,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(7.04046e+08,'s^-1'), n=1.05378, w0=(726.402,'kJ/mol'), E0=(374.722,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3940358245667206, var=173.63083761942818, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O
    Total Standard Deviation in ln(k): 27.406244356335844"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O
Total Standard Deviation in ln(k): 27.406244356335844""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O
Total Standard Deviation in ln(k): 27.406244356335844
""",
)

entry(
    index = 53,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O_Ext-1R!H-R",
    kinetics = Arrhenius(A=(5.4394e+08,'s^-1'), n=0.631892, Ea=(211.416,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O_Ext-1R!H-R",
    kinetics = Arrhenius(A=(8.67544e+08,'s^-1'), n=1.19995, Ea=(366.787,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->N_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

