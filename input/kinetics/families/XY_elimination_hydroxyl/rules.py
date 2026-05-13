#!/usr/bin/env python
# encoding: utf-8

name = "XY_elimination_hydroxyl/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(0.0419772,'s^-1'), n=4.29118, w0=(1253.93,'kJ/mol'), E0=(138.738,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3792905236289505, var=53.99483846925518, Tref=1000.0, N=14, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 14 training reactions at node Root
    Total Standard Deviation in ln(k): 15.684021217482327"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root
Total Standard Deviation in ln(k): 15.684021217482327""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root
Total Standard Deviation in ln(k): 15.684021217482327
""",
)

entry(
    index = 2,
    label = "Root_1R!H->C",
    kinetics = ArrheniusBM(A=(7.27097e+07,'s^-1'), n=1.63137, w0=(1225.72,'kJ/mol'), E0=(194.303,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5380275800434807, var=36.98957140916843, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_1R!H->C
    Total Standard Deviation in ln(k): 13.544436872602008"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 13.544436872602008""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 13.544436872602008
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H->C",
    kinetics = ArrheniusBM(A=(4.88584e+11,'s^-1'), n=0.570696, w0=(1304.7,'kJ/mol'), E0=(113.626,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8960104819217938, var=2.1432898003755545, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R!H->C
    Total Standard Deviation in ln(k): 5.186210526453891"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 5.186210526453891""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 5.186210526453891
""",
)

entry(
    index = 4,
    label = "Root_1R!H->C_5Br1sCl1sF1sH->H",
    kinetics = Arrhenius(A=(68453,'s^-1'), n=2.17099, Ea=(342.051,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_5Br1sCl1sF1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_5Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_5Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_5Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(4.28531e+10,'s^-1'), n=0.878544, w0=(1232.38,'kJ/mol'), E0=(189.103,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.679645457119547, var=6.128459827793733, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 6.670519182772459"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 6.670519182772459""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 6.670519182772459
""",
)

entry(
    index = 6,
    label = "Root_N-1R!H->C_5Br1sCl1sF1sH->F1s",
    kinetics = ArrheniusBM(A=(4.61996e+13,'s^-1'), n=-0.115143, w0=(1374.5,'kJ/mol'), E0=(113.554,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9957733002431044, var=5.2487105570876444, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_5Br1sCl1sF1sH->F1s',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s
    Total Standard Deviation in ln(k): 7.094803959662611"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s
Total Standard Deviation in ln(k): 7.094803959662611""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s
Total Standard Deviation in ln(k): 7.094803959662611
""",
)

entry(
    index = 7,
    label = "Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s",
    kinetics = ArrheniusBM(A=(4.96592e+09,'s^-1'), n=1.32136, w0=(1200,'kJ/mol'), E0=(116.145,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7614113371620358, var=2.22069369380035, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s
    Total Standard Deviation in ln(k): 4.900548446150431"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s
Total Standard Deviation in ln(k): 4.900548446150431""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s
Total Standard Deviation in ln(k): 4.900548446150431
""",
)

entry(
    index = 8,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_Ext-1C-R",
    kinetics = Arrhenius(A=(1.5706e+11,'s^-1'), n=0.715494, Ea=(287.921,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(1.21698e+12,'s^-1'), n=0.420056, w0=(1276,'kJ/mol'), E0=(182.041,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7626959737795608, var=2.313419891021042, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 4.965509683631242"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 4.965509683631242""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 4.965509683631242
""",
)

entry(
    index = 10,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(2.29983e+08,'s^-1'), n=1.63497, w0=(1101.5,'kJ/mol'), E0=(189.919,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5722455193858291, var=1.082470026398073, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 3.5235656688976333"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 3.5235656688976333""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 3.5235656688976333
""",
)

entry(
    index = 11,
    label = "Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_7R!H->C",
    kinetics = Arrhenius(A=(5.29418e+10,'s^-1'), n=0.745914, Ea=(145.547,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(9.31099e+14,'s^-1'), n=-0.498093, w0=(1374.5,'kJ/mol'), E0=(115.963,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9727059626694703, var=20.185797279969655, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.450980276275871"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.450980276275871""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.450980276275871
""",
)

entry(
    index = 13,
    label = "Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_5Br1sCl1sH->Br1s",
    kinetics = Arrhenius(A=(4.74683e+09,'s^-1'), n=1.36442, Ea=(132.064,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_5Br1sCl1sH->Br1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_5Br1sCl1sH->Br1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_5Br1sCl1sH->Br1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_5Br1sCl1sH->Br1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_N-5Br1sCl1sH->Br1s",
    kinetics = Arrhenius(A=(3.42848e+09,'s^-1'), n=1.33002, Ea=(133.295,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_N-5Br1sCl1sH->Br1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_N-5Br1sCl1sH->Br1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_N-5Br1sCl1sH->Br1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_N-5Br1sCl1sH->Br1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R",
    kinetics = ArrheniusBM(A=(4.30347e+12,'s^-1'), n=0.283291, w0=(1276,'kJ/mol'), E0=(184.925,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6572279863103407, var=3.4824353863463107, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R
    Total Standard Deviation in ln(k): 5.3924197584250715"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R
Total Standard Deviation in ln(k): 5.3924197584250715""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R
Total Standard Deviation in ln(k): 5.3924197584250715
""",
)

entry(
    index = 16,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_5Br1sCl1s->Br1s",
    kinetics = Arrhenius(A=(3.23964e+08,'s^-1'), n=1.60341, Ea=(216.691,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_5Br1sCl1s->Br1s',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_5Br1sCl1s->Br1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_5Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_5Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_N-5Br1sCl1s->Br1s",
    kinetics = Arrhenius(A=(1.20378e+08,'s^-1'), n=1.70445, Ea=(215.418,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_N-5Br1sCl1s->Br1s',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_N-5Br1sCl1s->Br1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_N-5Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_N-5Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_7R!H->O",
    kinetics = Arrhenius(A=(2.6978e+09,'s^-1'), n=1.11971, Ea=(202.466,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_7R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_7R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O",
    kinetics = ArrheniusBM(A=(4.96498e+10,'s^-1'), n=0.865604, w0=(1276,'kJ/mol'), E0=(175.618,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6674896221092742, var=0.8214166741300524, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O
    Total Standard Deviation in ln(k): 3.494041907908673"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O
Total Standard Deviation in ln(k): 3.494041907908673""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O
Total Standard Deviation in ln(k): 3.494041907908673
""",
)

entry(
    index = 20,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFILiNPSSi-2C",
    kinetics = ArrheniusBM(A=(8.61489e+09,'s^-1'), n=1.03179, w0=(1276,'kJ/mol'), E0=(173.459,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6366494453905035, var=0.40288180035507026, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFILiNPSSi-2C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFILiNPSSi-2C
    Total Standard Deviation in ln(k): 2.8720866294368537"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFILiNPSSi-2C
Total Standard Deviation in ln(k): 2.8720866294368537""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFILiNPSSi-2C
Total Standard Deviation in ln(k): 2.8720866294368537
""",
)

entry(
    index = 21,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_N-Sp-7BrCClFILiNPSSi-2C",
    kinetics = Arrhenius(A=(1.52349e+10,'s^-1'), n=1.11612, Ea=(246.995,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_N-Sp-7BrCClFILiNPSSi-2C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_N-Sp-7BrCClFILiNPSSi-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_N-Sp-7BrCClFILiNPSSi-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_N-Sp-7BrCClFILiNPSSi-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

