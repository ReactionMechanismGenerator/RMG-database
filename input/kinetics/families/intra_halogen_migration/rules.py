#!/usr/bin/env python
# encoding: utf-8

name = "intra_halogen_migration/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(6038.41,'s^-1'), n=2.50417, w0=(416556,'J/mol'), E0=(163532,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03133558275859258, var=66.16490804632078, Tref=1000.0, N=18, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 18 training reactions at node Root
    Total Standard Deviation in ln(k): 16.385611521472462"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root
Total Standard Deviation in ln(k): 16.385611521472462""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root
Total Standard Deviation in ln(k): 16.385611521472462
""",
)

entry(
    index = 2,
    label = "F",
    kinetics = ArrheniusBM(A=(3.03181e+09,'s^-1'), n=0.874169, w0=(485000,'J/mol'), E0=(201592,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06358755078404826, var=61.63872441983877, Tref=1000.0, N=11, data_mean=0.0, correlation='F',), comment="""BM rule fitted to 11 training reactions at node F
    Total Standard Deviation in ln(k): 15.89900963505276"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node F
Total Standard Deviation in ln(k): 15.89900963505276""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node F
Total Standard Deviation in ln(k): 15.89900963505276
""",
)

entry(
    index = 3,
    label = "Cl",
    kinetics = ArrheniusBM(A=(893.73,'s^-1'), n=2.71684, w0=(327000,'J/mol'), E0=(122883,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0008389315309072592, var=152.99185535827047, Tref=1000.0, N=4, data_mean=0.0, correlation='Cl',), comment="""BM rule fitted to 4 training reactions at node Cl
    Total Standard Deviation in ln(k): 24.798651271638853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Cl
Total Standard Deviation in ln(k): 24.798651271638853""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Cl
Total Standard Deviation in ln(k): 24.798651271638853
""",
)

entry(
    index = 4,
    label = "Br",
    kinetics = ArrheniusBM(A=(4.41068e+09,'s^-1'), n=0.61635, w0=(285000,'J/mol'), E0=(131360,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0008969427611604358, var=19.08034470564394, Tref=1000.0, N=3, data_mean=0.0, correlation='Br',), comment="""BM rule fitted to 3 training reactions at node Br
    Total Standard Deviation in ln(k): 8.759147723835769"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Br
Total Standard Deviation in ln(k): 8.759147723835769""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Br
Total Standard Deviation in ln(k): 8.759147723835769
""",
)

entry(
    index = 5,
    label = "R2F",
    kinetics = ArrheniusBM(A=(9.72231e+13,'s^-1'), n=-0.295801, w0=(485000,'J/mol'), E0=(173488,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0299576143045425, var=17.283834097384105, Tref=1000.0, N=6, data_mean=0.0, correlation='R2F',), comment="""BM rule fitted to 6 training reactions at node R2F
    Total Standard Deviation in ln(k): 8.409722084010028"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node R2F
Total Standard Deviation in ln(k): 8.409722084010028""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node R2F
Total Standard Deviation in ln(k): 8.409722084010028
""",
)

entry(
    index = 6,
    label = "R2Cl",
    kinetics = ArrheniusBM(A=(1.03108e+13,'s^-1'), n=-0.0707693, w0=(327000,'J/mol'), E0=(47264.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R2Cl',), comment="""BM rule fitted to 1 training reactions at node R2Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R2Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R2Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "R3F",
    kinetics = ArrheniusBM(A=(0.00930803,'s^-1'), n=4.16824, w0=(485000,'J/mol'), E0=(227637,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R3F',), comment="""BM rule fitted to 1 training reactions at node R3F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R3F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R3F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "R3Cl",
    kinetics = ArrheniusBM(A=(6.00221e+06,'s^-1'), n=1.90111, w0=(327000,'J/mol'), E0=(169648,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R3Cl',), comment="""BM rule fitted to 1 training reactions at node R3Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R3Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R3Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "R3Br",
    kinetics = ArrheniusBM(A=(5.2885e+08,'s^-1'), n=1.30127, w0=(285000,'J/mol'), E0=(134618,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R3Br',), comment="""BM rule fitted to 1 training reactions at node R3Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R3Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R3Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "R4F",
    kinetics = ArrheniusBM(A=(9.58733e-07,'s^-1'), n=5.29666, w0=(485000,'J/mol'), E0=(227349,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.013351942602990101, var=1.2221974720133415, Tref=1000.0, N=3, data_mean=0.0, correlation='R4F',), comment="""BM rule fitted to 3 training reactions at node R4F
    Total Standard Deviation in ln(k): 2.2498431725504213"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node R4F
Total Standard Deviation in ln(k): 2.2498431725504213""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node R4F
Total Standard Deviation in ln(k): 2.2498431725504213
""",
)

entry(
    index = 11,
    label = "R4Cl",
    kinetics = ArrheniusBM(A=(2.50247e+07,'s^-1'), n=1.58353, w0=(327000,'J/mol'), E0=(156188,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R4Cl',), comment="""BM rule fitted to 1 training reactions at node R4Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R4Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R4Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "R4Br",
    kinetics = ArrheniusBM(A=(9.62119e+10,'s^-1'), n=0.157944, w0=(285000,'J/mol'), E0=(121704,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R4Br',), comment="""BM rule fitted to 1 training reactions at node R4Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R4Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R4Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "R5nF",
    kinetics = ArrheniusBM(A=(1.64853e+07,'s^-1'), n=1.15307, w0=(485000,'J/mol'), E0=(198221,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R5nF',), comment="""BM rule fitted to 1 training reactions at node R5nF
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R5nF
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R5nF
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "R5nCl",
    kinetics = ArrheniusBM(A=(4.11837e-16,'s^-1'), n=7.45351, w0=(327000,'J/mol'), E0=(118459,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R5nCl',), comment="""BM rule fitted to 1 training reactions at node R5nCl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R5nCl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R5nCl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "R5nBr",
    kinetics = ArrheniusBM(A=(1.68639e+09,'s^-1'), n=0.389834, w0=(285000,'J/mol'), E0=(137780,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R5nBr',), comment="""BM rule fitted to 1 training reactions at node R5nBr
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R5nBr
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R5nBr
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "R2F_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(5.90514e+16,'s^-1'), n=-1.0755, w0=(485000,'J/mol'), E0=(191377,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07401473862015331, var=25.994670041374917, Tref=1000.0, N=4, data_mean=0.0, correlation='R2F_Ext-1R!H-R',), comment="""BM rule fitted to 4 training reactions at node R2F_Ext-1R!H-R
    Total Standard Deviation in ln(k): 10.407102139811068"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node R2F_Ext-1R!H-R
Total Standard Deviation in ln(k): 10.407102139811068""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node R2F_Ext-1R!H-R
Total Standard Deviation in ln(k): 10.407102139811068
""",
)

entry(
    index = 17,
    label = "R2F_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.36622e+11,'s^-1'), n=0.48217, w0=(485000,'J/mol'), E0=(152869,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R2F_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node R2F_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R2F_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R2F_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "R4F_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(0.00363316,'s^-1'), n=4.43046, w0=(485000,'J/mol'), E0=(242580,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R4F_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node R4F_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R4F_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R4F_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "R4F_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.000550858,'s^-1'), n=4.50663, w0=(485000,'J/mol'), E0=(241849,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R4F_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node R4F_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R4F_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R4F_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "R2F_Ext-1R!H-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.00763e+12,'s^-1'), n=0.18834, w0=(485000,'J/mol'), E0=(183173,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R2F_Ext-1R!H-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "R2F_Ext-1R!H-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.78041e+19,'s^-1'), n=-1.75898, w0=(485000,'J/mol'), E0=(196019,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09439094690595154, var=46.93619104513436, Tref=1000.0, N=3, data_mean=0.0, correlation='R2F_Ext-1R!H-R_N-4R!H->C',), comment="""BM rule fitted to 3 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C
    Total Standard Deviation in ln(k): 13.971601741914824"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C
Total Standard Deviation in ln(k): 13.971601741914824""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C
Total Standard Deviation in ln(k): 13.971601741914824
""",
)

entry(
    index = 22,
    label = "R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.94868e+19,'s^-1'), n=-1.85415, w0=(485000,'J/mol'), E0=(210642,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.020060994830987895, var=82.6111016070171, Tref=1000.0, N=2, data_mean=0.0, correlation='R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 18.27157182917452"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 18.27157182917452""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 18.27157182917452
""",
)

entry(
    index = 23,
    label = "R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(4.35648e+12,'s^-1'), n=0.369741, w0=(485000,'J/mol'), E0=(181542,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.2804e+11,'s^-1'), n=0.253035, w0=(485000,'J/mol'), E0=(209151,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

