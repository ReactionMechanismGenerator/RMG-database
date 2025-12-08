#!/usr/bin/env python
# encoding: utf-8

name = "1+2_Cycloaddition/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(4.26949e+51,'m^3/(mol*s)'), n=-13.3717, w0=(533.238,'kJ/mol'), E0=(229.709,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9662159874615295, var=162.08250097804572, Tref=1000.0, N=42, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 42 training reactions at node Root
    Total Standard Deviation in ln(k): 27.95028658733177"""),
    rank = 11,
    shortDesc = """BM rule fitted to 42 training reactions at node Root
Total Standard Deviation in ln(k): 27.95028658733177""",
    longDesc = 
"""
BM rule fitted to 42 training reactions at node Root
Total Standard Deviation in ln(k): 27.95028658733177
""",
)

entry(
    index = 2,
    label = "Root_Ext-3R-R",
    kinetics = ArrheniusBM(A=(6.05425e+52,'m^3/(mol*s)'), n=-13.7419, w0=(555.517,'kJ/mol'), E0=(230.782,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9612691398310935, var=179.4014599209648, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_Ext-3R-R',), comment="""BM rule fitted to 29 training reactions at node Root_Ext-3R-R
    Total Standard Deviation in ln(k): 29.26683715285379"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_Ext-3R-R
Total Standard Deviation in ln(k): 29.26683715285379""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_Ext-3R-R
Total Standard Deviation in ln(k): 29.26683715285379
""",
)

entry(
    index = 3,
    label = "Root_1R->C",
    kinetics = ArrheniusBM(A=(2.94176e+08,'m^3/(mol*s)'), n=-0.463393, w0=(476.125,'kJ/mol'), E0=(74.6089,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05349155836154465, var=2.5349342666075474, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_1R->C',), comment="""BM rule fitted to 12 training reactions at node Root_1R->C
    Total Standard Deviation in ln(k): 3.3262352228371874"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_1R->C
Total Standard Deviation in ln(k): 3.3262352228371874""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_1R->C
Total Standard Deviation in ln(k): 3.3262352228371874
""",
)

entry(
    index = 4,
    label = "Root_N-1R->C",
    kinetics = Arrhenius(A=(0.53862,'m^3/(mol*s)'), n=1.86213, Ea=(24.8236,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_Ext-3R-R_Sp-4R!H-3R",
    kinetics = ArrheniusBM(A=(7.02639e+69,'m^3/(mol*s)'), n=-18.5465, w0=(543.529,'kJ/mol'), E0=(230.131,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.5691069645943991, var=333.6547439044764, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R',), comment="""BM rule fitted to 17 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R
    Total Standard Deviation in ln(k): 40.561409076945594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R
Total Standard Deviation in ln(k): 40.561409076945594""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R
Total Standard Deviation in ln(k): 40.561409076945594
""",
)

entry(
    index = 6,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R",
    kinetics = ArrheniusBM(A=(4.20359e-06,'m^3/(mol*s)'), n=2.84095, w0=(572.5,'kJ/mol'), E0=(125.211,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8257237440796173, var=9.72704841264788, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R
    Total Standard Deviation in ln(k): 8.327093912865069"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R
Total Standard Deviation in ln(k): 8.327093912865069""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R
Total Standard Deviation in ln(k): 8.327093912865069
""",
)

entry(
    index = 7,
    label = "Root_1R->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.5716e+09,'m^3/(mol*s)'), n=-0.704858, w0=(474.2,'kJ/mol'), E0=(76.9274,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05741532689874322, var=0.5893395589658034, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.6832637488829607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.6832637488829607""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.6832637488829607
""",
)

entry(
    index = 8,
    label = "Root_1R->C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(3.33384e+09,'m^3/(mol*s)'), n=-0.775738, w0=(480,'kJ/mol'), E0=(85.117,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03181634075216538, var=0.1433731637397793, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->C_Ext-2R-R
    Total Standard Deviation in ln(k): 0.8390264533693597"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->C_Ext-2R-R
Total Standard Deviation in ln(k): 0.8390264533693597""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->C_Ext-2R-R
Total Standard Deviation in ln(k): 0.8390264533693597
""",
)

entry(
    index = 9,
    label = "Root_1R->C_Sp-2R=1C",
    kinetics = ArrheniusBM(A=(5.30858e+06,'m^3/(mol*s)'), n=-0.130328, w0=(480,'kJ/mol'), E0=(154.657,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.587997258796586, var=0.16964704494037178, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Sp-2R=1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Sp-2R=1C
    Total Standard Deviation in ln(k): 4.815657794528946"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Sp-2R=1C
Total Standard Deviation in ln(k): 4.815657794528946""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Sp-2R=1C
Total Standard Deviation in ln(k): 4.815657794528946
""",
)

entry(
    index = 10,
    label = "Root_1R->C_N-Sp-2R=1C",
    kinetics = Arrhenius(A=(1.77e+09,'m^3/(mol*s)'), n=-0.662, Ea=(0.157737,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-Sp-2R=1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-Sp-2R=1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-Sp-2R=1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-Sp-2R=1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O",
    kinetics = ArrheniusBM(A=(2.81611e+63,'m^3/(mol*s)'), n=-16.921, w0=(572.5,'kJ/mol'), E0=(5.725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.002796207498084, var=507.8244884415765, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O
    Total Standard Deviation in ln(k): 50.20877900118538"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O
Total Standard Deviation in ln(k): 50.20877900118538""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O
Total Standard Deviation in ln(k): 50.20877900118538
""",
)

entry(
    index = 12,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(5.27568e-35,'m^3/(mol*s)'), n=11.4492, w0=(531.458,'kJ/mol'), E0=(33.171,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8736162795346892, var=89.49304033158167, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O
    Total Standard Deviation in ln(k): 21.15996222465328"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O
Total Standard Deviation in ln(k): 21.15996222465328""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O
Total Standard Deviation in ln(k): 21.15996222465328
""",
)

entry(
    index = 13,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.19551e-05,'m^3/(mol*s)'), n=2.6883, w0=(572.5,'kJ/mol'), E0=(125.931,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8572215509293202, var=10.800968308188681, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R',), comment="""BM rule fitted to 11 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R
    Total Standard Deviation in ln(k): 8.742350072315146"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R
Total Standard Deviation in ln(k): 8.742350072315146""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R
Total Standard Deviation in ln(k): 8.742350072315146
""",
)

entry(
    index = 14,
    label = "Root_1R->C_Ext-1C-R_Ext-1C-R",
    kinetics = Arrhenius(A=(3.18e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_1R->C_Ext-1C-R_Sp-2R=1C",
    kinetics = ArrheniusBM(A=(9.41381e+08,'m^3/(mol*s)'), n=-0.607357, w0=(480,'kJ/mol'), E0=(101.897,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2790521167276607, var=0.007777354492480258, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_Sp-2R=1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C
    Total Standard Deviation in ln(k): 0.8779321759564577"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C
Total Standard Deviation in ln(k): 0.8779321759564577""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C
Total Standard Deviation in ln(k): 0.8779321759564577
""",
)

entry(
    index = 16,
    label = "Root_1R->C_Ext-1C-R_N-Sp-2R=1C",
    kinetics = ArrheniusBM(A=(4.65123e+09,'m^3/(mol*s)'), n=-0.763972, w0=(462.5,'kJ/mol'), E0=(90.9129,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0009309671137265228, var=1.1655949953965064, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_N-Sp-2R=1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C
    Total Standard Deviation in ln(k): 2.1667057286443425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C
Total Standard Deviation in ln(k): 2.1667057286443425""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C
Total Standard Deviation in ln(k): 2.1667057286443425
""",
)

entry(
    index = 17,
    label = "Root_1R->C_Ext-2R-R_3R->C",
    kinetics = ArrheniusBM(A=(4.13595e+09,'m^3/(mol*s)'), n=-0.801251, w0=(474,'kJ/mol'), E0=(97.1562,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03955302272952503, var=0.033598433444608056, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_3R->C
    Total Standard Deviation in ln(k): 0.46684489712018606"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_3R->C
Total Standard Deviation in ln(k): 0.46684489712018606""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_3R->C
Total Standard Deviation in ln(k): 0.46684489712018606
""",
)

entry(
    index = 18,
    label = "Root_1R->C_Ext-2R-R_N-3R->C",
    kinetics = ArrheniusBM(A=(3.86082e+06,'m^3/(mol*s)'), n=0.0243326, w0=(486,'kJ/mol'), E0=(92.826,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02516094828390788, var=1.7607258136569388, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R_N-3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C
    Total Standard Deviation in ln(k): 2.7233484267253916"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C
Total Standard Deviation in ln(k): 2.7233484267253916""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C
Total Standard Deviation in ln(k): 2.7233484267253916
""",
)

entry(
    index = 19,
    label = "Root_1R->C_Sp-2R=1C_3R->C",
    kinetics = Arrhenius(A=(1.98e+06,'m^3/(mol*s)'), n=0, Ea=(22.1334,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Sp-2R=1C_3R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Sp-2R=1C_3R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Sp-2R=1C_3R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Sp-2R=1C_3R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_1R->C_Sp-2R=1C_N-3R->C",
    kinetics = Arrhenius(A=(700000,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Sp-2R=1C_N-3R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Sp-2R=1C_N-3R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Sp-2R=1C_N-3R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Sp-2R=1C_N-3R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(6.43208e+53,'m^3/(mol*s)'), n=-15.5793, w0=(572.5,'kJ/mol'), E0=(5.725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.8310244541392278, var=0.34690473860326365, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 5.7813252415369565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 5.7813252415369565""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 5.7813252415369565
""",
)

entry(
    index = 22,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-5R!H-R",
    kinetics = Arrhenius(A=(5.34467e-08,'m^3/(mol*s)'), n=4.75559, Ea=(-201.636,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C",
    kinetics = ArrheniusBM(A=(2.65278e+11,'m^3/(mol*s)'), n=-1.63781, w0=(490.417,'kJ/mol'), E0=(146.247,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13397802269005962, var=5.325801190725484, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C
    Total Standard Deviation in ln(k): 4.9630951538003805"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C
Total Standard Deviation in ln(k): 4.9630951538003805""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C
Total Standard Deviation in ln(k): 4.9630951538003805
""",
)

entry(
    index = 24,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C",
    kinetics = Arrhenius(A=(1.20357e-05,'m^3/(mol*s)'), n=3.03727, Ea=(84.0973,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-6.185804953468382e-16, var=82.69947894371671, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C
    Total Standard Deviation in ln(k): 18.230911214457088"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C
Total Standard Deviation in ln(k): 18.230911214457088""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C
Total Standard Deviation in ln(k): 18.230911214457088
""",
)

entry(
    index = 25,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F",
    kinetics = ArrheniusBM(A=(0.0710543,'m^3/(mol*s)'), n=1.7866, w0=(572.5,'kJ/mol'), E0=(115.679,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.49042332677882267, var=3.5045013281941677, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F
    Total Standard Deviation in ln(k): 4.985146302076766"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F
Total Standard Deviation in ln(k): 4.985146302076766""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F
Total Standard Deviation in ln(k): 4.985146302076766
""",
)

entry(
    index = 26,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(5.07842e-20,'m^3/(mol*s)'), n=6.70339, w0=(572.5,'kJ/mol'), E0=(100.07,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4485085833653957, var=3.096324558603113, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F
    Total Standard Deviation in ln(k): 7.167076065524004"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F
Total Standard Deviation in ln(k): 7.167076065524004""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F
Total Standard Deviation in ln(k): 7.167076065524004
""",
)

entry(
    index = 27,
    label = "Root_1R->C_Ext-1C-R_Sp-2R=1C_Ext-2R-R",
    kinetics = Arrhenius(A=(1.54e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_Sp-2R=1C_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_1R->C_Ext-1C-R_N-Sp-2R=1C_Ext-2R-R",
    kinetics = Arrhenius(A=(4.7e+09,'m^3/(mol*s)'), n=-0.823, Ea=(0.096232,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_N-Sp-2R=1C_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_1R->C_Ext-2R-R_3R->C_Ext-4R!H-R",
    kinetics = Arrhenius(A=(1.85e+09,'m^3/(mol*s)'), n=-0.7, Ea=(-0.281165,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R_3R->C_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-2R-R_3R->C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Ext-2R-R_3R->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Ext-2R-R_3R->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_1R->C_Ext-2R-R_N-3R->C_Ext-2R-R",
    kinetics = Arrhenius(A=(7.6e+06,'m^3/(mol*s)'), n=0, Ea=(0.4184,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R_N-3R->C_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C",
    kinetics = ArrheniusBM(A=(8.37235e+53,'m^3/(mol*s)'), n=-15.5905, w0=(572.5,'kJ/mol'), E0=(5.725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-10.930451044617266, var=0.19087693265558262, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C
    Total Standard Deviation in ln(k): 28.33930285986811"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C
Total Standard Deviation in ln(k): 28.33930285986811""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C
Total Standard Deviation in ln(k): 28.33930285986811
""",
)

entry(
    index = 32,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-8R!H->C",
    kinetics = Arrhenius(A=(9.85919e-16,'m^3/(mol*s)'), n=4.09382, Ea=(-168.948,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F",
    kinetics = ArrheniusBM(A=(3.57904e-20,'m^3/(mol*s)'), n=7.10843, w0=(498.625,'kJ/mol'), E0=(38.3505,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3088674976909773, var=3.7748429757659547, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F
    Total Standard Deviation in ln(k): 4.671039776482464"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F
Total Standard Deviation in ln(k): 4.671039776482464""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F
Total Standard Deviation in ln(k): 4.671039776482464
""",
)

entry(
    index = 34,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F",
    kinetics = ArrheniusBM(A=(0.531381,'m^3/(mol*s)'), n=1.91075, w0=(474,'kJ/mol'), E0=(98.7387,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4682509003578339, var=1.62527706106521, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F
    Total Standard Deviation in ln(k): 3.7322734695657376"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F
Total Standard Deviation in ln(k): 3.7322734695657376""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F
Total Standard Deviation in ln(k): 3.7322734695657376
""",
)

entry(
    index = 35,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R",
    kinetics = ArrheniusBM(A=(0.00193199,'m^3/(mol*s)'), n=2.48798, w0=(572.5,'kJ/mol'), E0=(119.869,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1169441675062353, var=195.41506302672917, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R
    Total Standard Deviation in ln(k): 30.83077203998464"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R
Total Standard Deviation in ln(k): 30.83077203998464""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R
Total Standard Deviation in ln(k): 30.83077203998464
""",
)

entry(
    index = 36,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-4BrCClF-R",
    kinetics = Arrhenius(A=(1.8498e-07,'m^3/(mol*s)'), n=3.40152, Ea=(74.6775,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-4BrCClF-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-4BrCClF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-4BrCClF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-4BrCClF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.98227e-05,'m^3/(mol*s)'), n=2.70596, w0=(572.5,'kJ/mol'), E0=(112.407,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5910490843411947, var=0.27235983911212236, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C
    Total Standard Deviation in ln(k): 2.5312812145992734"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C
Total Standard Deviation in ln(k): 2.5312812145992734""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C
Total Standard Deviation in ln(k): 2.5312812145992734
""",
)

entry(
    index = 38,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_N-6R!H->C",
    kinetics = Arrhenius(A=(0.000352549,'m^3/(mol*s)'), n=2.48352, Ea=(177.184,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.7418e-41,'m^3/(mol*s)'), n=12.7965, w0=(572.5,'kJ/mol'), E0=(2.46242,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.0604941213527934, var=0.29979507405679645, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R
    Total Standard Deviation in ln(k): 8.78734725396888"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R
Total Standard Deviation in ln(k): 8.78734725396888""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R
Total Standard Deviation in ln(k): 8.78734725396888
""",
)

entry(
    index = 40,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-5BrCClILiNOPSSi-R",
    kinetics = Arrhenius(A=(4.4056e-09,'m^3/(mol*s)'), n=3.70948, Ea=(182.077,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-5BrCClILiNOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-5BrCClILiNOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-5BrCClILiNOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-5BrCClILiNOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = Arrhenius(A=(2.09967e-13,'m^3/(mol*s)'), n=3.46188, Ea=(-164.097,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = Arrhenius(A=(5.99786e-14,'m^3/(mol*s)'), n=3.67717, Ea=(-165.36,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-1C-R",
    kinetics = Arrhenius(A=(4.10298e-06,'m^3/(mol*s)'), n=3.07477, Ea=(21.6954,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-2R-R",
    kinetics = Arrhenius(A=(1.01799e-05,'m^3/(mol*s)'), n=2.87159, Ea=(40.5376,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_2R->C",
    kinetics = Arrhenius(A=(2.07011e-05,'m^3/(mol*s)'), n=2.98446, Ea=(43.7961,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_N-2R->C",
    kinetics = Arrhenius(A=(4.81575e-05,'m^3/(mol*s)'), n=2.76922, Ea=(37.8393,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_4BrCCl->Cl",
    kinetics = Arrhenius(A=(8.68219e-05,'m^3/(mol*s)'), n=2.97056, Ea=(7.89502,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_4BrCCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_4BrCCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_4BrCCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_4BrCCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_N-4BrCCl->Cl",
    kinetics = Arrhenius(A=(0.000145611,'m^3/(mol*s)'), n=2.95653, Ea=(-0.108502,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_N-4BrCCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_N-4BrCCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_N-4BrCCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_N-4BrCCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C",
    kinetics = ArrheniusBM(A=(9713.89,'m^3/(mol*s)'), n=0.56391, w0=(572.5,'kJ/mol'), E0=(149.825,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15681013833384969, var=296.2007852032553, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C
    Total Standard Deviation in ln(k): 34.89645779234786"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C
Total Standard Deviation in ln(k): 34.89645779234786""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C
Total Standard Deviation in ln(k): 34.89645779234786
""",
)

entry(
    index = 50,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_N-4BrCClF->C",
    kinetics = Arrhenius(A=(0.00491008,'m^3/(mol*s)'), n=2.38401, Ea=(88.3837,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_N-4BrCClF->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_N-4BrCClF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_N-4BrCClF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_N-4BrCClF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(4.64871e-05,'m^3/(mol*s)'), n=2.69436, w0=(572.5,'kJ/mol'), E0=(112.945,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5944663503659927, var=0.9376777933368575, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 3.434894488402397"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 3.434894488402397""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 3.434894488402397
""",
)

entry(
    index = 52,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(2.81961e-05,'m^3/(mol*s)'), n=2.73363, Ea=(177.495,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 53,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O",
    kinetics = ArrheniusBM(A=(3.1284e-13,'m^3/(mol*s)'), n=4.63541, w0=(572.5,'kJ/mol'), E0=(97.4098,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4039532065468343, var=0.11299844709396699, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O
    Total Standard Deviation in ln(k): 4.201417160098742"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O
Total Standard Deviation in ln(k): 4.201417160098742""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O
Total Standard Deviation in ln(k): 4.201417160098742
""",
)

entry(
    index = 54,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_N-5BrCClILiNOPSSi->O",
    kinetics = ArrheniusBM(A=(7.07451e-15,'m^3/(mol*s)'), n=5.27159, w0=(572.5,'kJ/mol'), E0=(132.375,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.5790558305510576, var=0.11284577614907138, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_N-5BrCClILiNOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_N-5BrCClILiNOPSSi->O
    Total Standard Deviation in ln(k): 4.640918100884243"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_N-5BrCClILiNOPSSi->O
Total Standard Deviation in ln(k): 4.640918100884243""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_N-5BrCClILiNOPSSi->O
Total Standard Deviation in ln(k): 4.640918100884243
""",
)

entry(
    index = 55,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.24121e-05,'m^3/(mol*s)'), n=3.07293, w0=(572.5,'kJ/mol'), E0=(157.079,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.33631353739567055, var=705.9390473680337, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C
    Total Standard Deviation in ln(k): 54.10984458091797"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 54.10984458091797""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 54.10984458091797
""",
)

entry(
    index = 56,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_N-6R!H->C",
    kinetics = Arrhenius(A=(3.87031e-05,'m^3/(mol*s)'), n=3.04873, Ea=(22.9526,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = Arrhenius(A=(6.58773e-05,'m^3/(mol*s)'), n=2.61294, Ea=(182.613,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(4.67866e-05,'m^3/(mol*s)'), n=2.73161, Ea=(179.832,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->F_Ext-2R-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C",
    kinetics = ArrheniusBM(A=(1.96183e-13,'m^3/(mol*s)'), n=4.69331, w0=(572.5,'kJ/mol'), E0=(98.1713,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4488538638401032, var=0.034930851626645595, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C
    Total Standard Deviation in ln(k): 4.015017260000709"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 4.015017260000709""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 4.015017260000709
""",
)

entry(
    index = 60,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-9R!H->C",
    kinetics = Arrhenius(A=(2.22077e-12,'m^3/(mol*s)'), n=4.39186, Ea=(137.315,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_N-5BrCClILiNOPSSi->O_Ext-7R!H-R",
    kinetics = Arrhenius(A=(4.89931e-15,'m^3/(mol*s)'), n=5.3217, Ea=(209.535,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_N-5BrCClILiNOPSSi->O_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_N-5BrCClILiNOPSSi->O_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_N-5BrCClILiNOPSSi->O_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_N-5BrCClILiNOPSSi->O_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = Arrhenius(A=(0.00828286,'m^3/(mol*s)'), n=2.34779, Ea=(55.5774,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(2.67496e-08,'m^3/(mol*s)'), n=3.75287, Ea=(187.312,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C",
    kinetics = Arrhenius(A=(1.69502e-13,'m^3/(mol*s)'), n=4.7063, Ea=(142.786,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C",
    kinetics = Arrhenius(A=(2.27066e-13,'m^3/(mol*s)'), n=4.68033, Ea=(142.625,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->F_Ext-2R-R_Ext-6R!H-R_5BrCClILiNOPSSi->O_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

