#!/usr/bin/env python
# encoding: utf-8

name = "Cation_Addition_MultipleBond_Disprop/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusChargeTransfer(A=(5.16116,'m^3/(mol*s)'), n=2.06799, Ea=(23.8116,'kJ/mol'), V0=(0,'V'), alpha=0.0714286, electrons=1, T0=(1,'K'), uncertainty=RateUncertainty(mu=-7.39083189245573e-16, var=32.42017750533938, Tref=1000.0, N=7, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 7 training reactions at node Root
    Total Standard Deviation in ln(k): 11.414704775475835"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 11.414704775475835""",
    longDesc =
"""
BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 11.414704775475835
""",
)

entry(
    index = 2,
    label = "Root_4R!H->C",
    kinetics = ArrheniusChargeTransfer(A=(4.21373,'m^3/(mol*s)'), n=2.06943, Ea=(32.3362,'kJ/mol'), V0=(0,'V'), alpha=0.0833333, electrons=1, T0=(1,'K'), uncertainty=RateUncertainty(mu=1.968210667012667e-16, var=23.211130849050264, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_4R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_4R!H->C
    Total Standard Deviation in ln(k): 9.658398926110465"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_4R!H->C
Total Standard Deviation in ln(k): 9.658398926110465""",
    longDesc =
"""
BM rule fitted to 6 training reactions at node Root_4R!H->C
Total Standard Deviation in ln(k): 9.658398926110465
""",
)

entry(
    index = 3,
    label = "Root_N-4R!H->C",
    kinetics = ArrheniusChargeTransferBM(A=(17.4272,'m^3/(mol*s)'), n=2.05933, w0=(912800,'J/mol'), E0=(91280,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc =
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_4R!H->C_2R!H->N",
    kinetics = ArrheniusChargeTransferBM(A=(2454.37,'m^3/(mol*s)'), n=0.869935, w0=(741700,'J/mol'), E0=(74170,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc =
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_4R!H->C_N-2R!H->N",
    kinetics = ArrheniusChargeTransfer(A=(1.17927,'m^3/(mol*s)'), n=2.30933, Ea=(46.1668,'kJ/mol'), V0=(0,'V'), alpha=0.1, electrons=1, T0=(1,'K'), uncertainty=RateUncertainty(mu=-8.997534477772191e-17, var=12.290291821566104, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_4R!H->C_N-2R!H->N',), comment="""BM rule fitted to 5 training reactions at node Root_4R!H->C_N-2R!H->N
    Total Standard Deviation in ln(k): 7.028102501974961"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_4R!H->C_N-2R!H->N
Total Standard Deviation in ln(k): 7.028102501974961""",
    longDesc =
"""
BM rule fitted to 5 training reactions at node Root_4R!H->C_N-2R!H->N
Total Standard Deviation in ln(k): 7.028102501974961
""",
)

entry(
    index = 6,
    label = "Root_4R!H->C_N-2R!H->N_Ext-3R!H-R",
    kinetics = ArrheniusChargeTransfer(A=(3.22243,'m^3/(mol*s)'), n=2.25711, Ea=(41.0301,'kJ/mol'), V0=(0,'V'), alpha=0.166667, electrons=1, T0=(1,'K'), uncertainty=RateUncertainty(mu=1.3121404446751113e-16, var=21.950387375810646, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R!H->C_N-2R!H->N_Ext-3R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_4R!H->C_N-2R!H->N_Ext-3R!H-R
    Total Standard Deviation in ln(k): 9.392432527528594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R!H->C_N-2R!H->N_Ext-3R!H-R
Total Standard Deviation in ln(k): 9.392432527528594""",
    longDesc =
"""
BM rule fitted to 3 training reactions at node Root_4R!H->C_N-2R!H->N_Ext-3R!H-R
Total Standard Deviation in ln(k): 9.392432527528594
""",
)

entry(
    index = 7,
    label = "Root_4R!H->C_N-2R!H->N_1R!H->O",
    kinetics = ArrheniusChargeTransferBM(A=(0.419384,'m^3/(mol*s)'), n=2.21898, w0=(918800,'J/mol'), E0=(91880,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-2R!H->N_1R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-2R!H->N_1R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-2R!H->N_1R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc =
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-2R!H->N_1R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_4R!H->C_N-2R!H->N_N-1R!H->O",
    kinetics = ArrheniusChargeTransferBM(A=(0.162517,'m^3/(mol*s)'), n=2.55635, w0=(716200,'J/mol'), E0=(71620,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-2R!H->N_N-1R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-2R!H->N_N-1R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-2R!H->N_N-1R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc =
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-2R!H->N_N-1R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_4R!H->C_N-2R!H->N_Ext-3R!H-R_1R!H->O",
    kinetics = ArrheniusChargeTransfer(A=(14.6322,'m^3/(mol*s)'), n=2.02179, Ea=(27.5025,'kJ/mol'), V0=(0,'V'), alpha=0.25, electrons=1, T0=(1,'K'), uncertainty=RateUncertainty(mu=2.249383619443048e-16, var=22.995040632494337, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R!H->C_N-2R!H->N_Ext-3R!H-R_1R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_4R!H->C_N-2R!H->N_Ext-3R!H-R_1R!H->O
    Total Standard Deviation in ln(k): 9.613335076294824"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R!H->C_N-2R!H->N_Ext-3R!H-R_1R!H->O
Total Standard Deviation in ln(k): 9.613335076294824""",
    longDesc =
"""
BM rule fitted to 2 training reactions at node Root_4R!H->C_N-2R!H->N_Ext-3R!H-R_1R!H->O
Total Standard Deviation in ln(k): 9.613335076294824
""",
)

entry(
    index = 10,
    label = "Root_4R!H->C_N-2R!H->N_Ext-3R!H-R_N-1R!H->O",
    kinetics = ArrheniusChargeTransferBM(A=(0.15629,'m^3/(mol*s)'), n=2.72776, w0=(750800,'J/mol'), E0=(75080,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-2R!H->N_Ext-3R!H-R_N-1R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-2R!H->N_Ext-3R!H-R_N-1R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-2R!H->N_Ext-3R!H-R_N-1R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc =
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-2R!H->N_Ext-3R!H-R_N-1R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_4R!H->C_N-2R!H->N_Ext-3R!H-R_1R!H->O_Ext-7R!H-R_8R!H->C",
    kinetics = ArrheniusChargeTransferBM(A=(95.603,'m^3/(mol*s)'), n=1.70021, w0=(918800,'J/mol'), E0=(91880,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-2R!H->N_Ext-3R!H-R_1R!H->O_Ext-7R!H-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-2R!H->N_Ext-3R!H-R_1R!H->O_Ext-7R!H-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-2R!H->N_Ext-3R!H-R_1R!H->O_Ext-7R!H-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc =
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-2R!H->N_Ext-3R!H-R_1R!H->O_Ext-7R!H-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_4R!H->C_N-2R!H->N_Ext-3R!H-R_1R!H->O_Ext-7R!H-R_N-8R!H->C",
    kinetics = ArrheniusChargeTransferBM(A=(2.23949,'m^3/(mol*s)'), n=2.34337, w0=(918800,'J/mol'), E0=(91880,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-2R!H->N_Ext-3R!H-R_1R!H->O_Ext-7R!H-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-2R!H->N_Ext-3R!H-R_1R!H->O_Ext-7R!H-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-2R!H->N_Ext-3R!H-R_1R!H->O_Ext-7R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc =
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-2R!H->N_Ext-3R!H-R_1R!H->O_Ext-7R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)
