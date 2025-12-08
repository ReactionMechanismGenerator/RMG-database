#!/usr/bin/env python
# encoding: utf-8

name = "CO_CF_bond_dissociation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.76431e+11,'s^-1'), n=0.325199, w0=(858.983,'kJ/mol'), E0=(231.209,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.67600310208057, var=182.80126797100408, Tref=1000.0, N=29, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 29 training reactions at node Root
    Total Standard Deviation in ln(k): 28.803324238017257"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root
Total Standard Deviation in ln(k): 28.803324238017257""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root
Total Standard Deviation in ln(k): 28.803324238017257
""",
)

entry(
    index = 2,
    label = "Root_3C-u0",
    kinetics = ArrheniusBM(A=(2.47709e+09,'s^-1'), n=0.861435, w0=(854.9,'kJ/mol'), E0=(277.324,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6672462525439692, var=77.76919376577212, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_3C-u0',), comment="""BM rule fitted to 20 training reactions at node Root_3C-u0
    Total Standard Deviation in ln(k): 19.355623986343026"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_3C-u0
Total Standard Deviation in ln(k): 19.355623986343026""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_3C-u0
Total Standard Deviation in ln(k): 19.355623986343026
""",
)

entry(
    index = 3,
    label = "Root_N-3C-u0",
    kinetics = ArrheniusBM(A=(1.22938e+21,'s^-1'), n=-2.50646, w0=(868.056,'kJ/mol'), E0=(148.182,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8611772546233027, var=182.81174018390885, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3C-u0',), comment="""BM rule fitted to 9 training reactions at node Root_N-3C-u0
    Total Standard Deviation in ln(k): 29.269362299413768"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3C-u0
Total Standard Deviation in ln(k): 29.269362299413768""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3C-u0
Total Standard Deviation in ln(k): 29.269362299413768
""",
)

entry(
    index = 4,
    label = "Root_3C-u0_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.92144e+10,'s^-1'), n=0.470977, w0=(854.9,'kJ/mol'), E0=(298.313,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7161728467346632, var=91.48909890942059, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R',), comment="""BM rule fitted to 15 training reactions at node Root_3C-u0_Ext-3C-R
    Total Standard Deviation in ln(k): 20.97470706471615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_3C-u0_Ext-3C-R
Total Standard Deviation in ln(k): 20.97470706471615""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_3C-u0_Ext-3C-R
Total Standard Deviation in ln(k): 20.97470706471615
""",
)

entry(
    index = 5,
    label = "Root_3C-u0_4F1sH->H",
    kinetics = ArrheniusBM(A=(1.06172e+06,'s^-1'), n=1.81129, w0=(810.5,'kJ/mol'), E0=(200.615,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2914832305231129, var=0.8524145049606803, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_4F1sH->H',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_4F1sH->H
    Total Standard Deviation in ln(k): 2.5832675801593226"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_4F1sH->H
Total Standard Deviation in ln(k): 2.5832675801593226""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_4F1sH->H
Total Standard Deviation in ln(k): 2.5832675801593226
""",
)

entry(
    index = 6,
    label = "Root_3C-u0_N-4F1sH->H",
    kinetics = ArrheniusBM(A=(2.26103e+08,'s^-1'), n=1.05774, w0=(884.5,'kJ/mol'), E0=(239.235,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7620000383761455, var=1.8615816846978865, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3C-u0_N-4F1sH->H',), comment="""BM rule fitted to 3 training reactions at node Root_3C-u0_N-4F1sH->H
    Total Standard Deviation in ln(k): 4.649829330930682"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3C-u0_N-4F1sH->H
Total Standard Deviation in ln(k): 4.649829330930682""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3C-u0_N-4F1sH->H
Total Standard Deviation in ln(k): 4.649829330930682
""",
)

entry(
    index = 7,
    label = "Root_N-3C-u0_5R->O",
    kinetics = ArrheniusBM(A=(1442.74,'s^-1'), n=2.34038, w0=(884.5,'kJ/mol'), E0=(262.374,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.30913528390655637, var=0.07250119342877302, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3C-u0_5R->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3C-u0_5R->O
    Total Standard Deviation in ln(k): 1.316517700939753"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3C-u0_5R->O
Total Standard Deviation in ln(k): 1.316517700939753""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3C-u0_5R->O
Total Standard Deviation in ln(k): 1.316517700939753
""",
)

entry(
    index = 8,
    label = "Root_N-3C-u0_N-5R->O",
    kinetics = ArrheniusBM(A=(9.55201e+15,'s^-1'), n=-0.959491, w0=(863.357,'kJ/mol'), E0=(88.9182,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7733856761182334, var=5.22234491618635, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-3C-u0_N-5R->O
    Total Standard Deviation in ln(k): 6.524490993116585"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3C-u0_N-5R->O
Total Standard Deviation in ln(k): 6.524490993116585""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3C-u0_N-5R->O
Total Standard Deviation in ln(k): 6.524490993116585
""",
)

entry(
    index = 9,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.88362e+08,'s^-1'), n=1.25682, w0=(854.9,'kJ/mol'), E0=(341.338,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7517889851026477, var=20.614923029867587, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C',), comment="""BM rule fitted to 10 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C
    Total Standard Deviation in ln(k): 10.991147947609864"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 10.991147947609864""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 10.991147947609864
""",
)

entry(
    index = 10,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.720883,'s^-1'), n=3.52593, w0=(854.9,'kJ/mol'), E0=(181.284,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.251288450975649, var=31.37750195424374, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.861026762317394"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.861026762317394""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.861026762317394
""",
)

entry(
    index = 11,
    label = "Root_3C-u0_4F1sH->H_Ext-2C-R_Ext-6R!H-R",
    kinetics = Arrhenius(A=(560000,'s^-1'), n=1.87, Ea=(187.16,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_4F1sH->H_Ext-2C-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_4F1sH->H_Ext-2C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_4F1sH->H_Ext-2C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_4F1sH->H_Ext-2C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.24512e+08,'s^-1'), n=0.995513, w0=(884.5,'kJ/mol'), E0=(242.35,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8599959327159628, var=0.4886018210428627, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C
    Total Standard Deviation in ln(k): 3.5621047972691535"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C
Total Standard Deviation in ln(k): 3.5621047972691535""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C
Total Standard Deviation in ln(k): 3.5621047972691535
""",
)

entry(
    index = 13,
    label = "Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-6R!H->C",
    kinetics = Arrhenius(A=(8.1e+07,'s^-1'), n=1.22, Ea=(203.77,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_7R!H->C",
    kinetics = Arrhenius(A=(5066.67,'s^-1'), n=2.17, Ea=(279.293,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-7R!H->C",
    kinetics = Arrhenius(A=(413.333,'s^-1'), n=2.51, Ea=(275.492,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R",
    kinetics = ArrheniusBM(A=(8.03024e+17,'s^-1'), n=-1.60989, w0=(869.7,'kJ/mol'), E0=(87.2212,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8562052551375626, var=9.315168200050648, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R
    Total Standard Deviation in ln(k): 8.269873396675488"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R
Total Standard Deviation in ln(k): 8.269873396675488""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R
Total Standard Deviation in ln(k): 8.269873396675488
""",
)

entry(
    index = 17,
    label = "Root_N-3C-u0_N-5R->O_4F1sH->H",
    kinetics = Arrhenius(A=(2.78e+10,'s^-1'), n=0.74, Ea=(93.971,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_4F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_4F1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_4F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_4F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-3C-u0_N-5R->O_N-4F1sH->H",
    kinetics = Arrhenius(A=(5.95e+09,'s^-1'), n=1.2, Ea=(114.447,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_N-4F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_N-4F1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_N-4F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_N-4F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H",
    kinetics = ArrheniusBM(A=(5.33486e+06,'s^-1'), n=1.68732, w0=(810.5,'kJ/mol'), E0=(371.48,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.670660638977169, var=2.373095536123419, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H',), comment="""BM rule fitted to 4 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H
    Total Standard Deviation in ln(k): 4.773342274663264"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H
Total Standard Deviation in ln(k): 4.773342274663264""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H
Total Standard Deviation in ln(k): 4.773342274663264
""",
)

entry(
    index = 20,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H",
    kinetics = ArrheniusBM(A=(2.5125e+09,'s^-1'), n=0.944844, w0=(884.5,'kJ/mol'), E0=(316.967,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8138799946201265, var=1.158681637762172, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H',), comment="""BM rule fitted to 6 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H
    Total Standard Deviation in ln(k): 4.2028630514267125"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H
Total Standard Deviation in ln(k): 4.2028630514267125""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H
Total Standard Deviation in ln(k): 4.2028630514267125
""",
)

entry(
    index = 21,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H",
    kinetics = ArrheniusBM(A=(1.26761e+06,'s^-1'), n=1.81828, w0=(810.5,'kJ/mol'), E0=(243.842,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3011800064263425, var=0.07060990627683447, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H
    Total Standard Deviation in ln(k): 1.2894424057733256"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H
Total Standard Deviation in ln(k): 1.2894424057733256""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H
Total Standard Deviation in ln(k): 1.2894424057733256
""",
)

entry(
    index = 22,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H",
    kinetics = ArrheniusBM(A=(3.00432e+11,'s^-1'), n=0.142235, w0=(884.5,'kJ/mol'), E0=(179.422,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6178164571989261, var=0.4264679288100494, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H',), comment="""BM rule fitted to 3 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H
    Total Standard Deviation in ln(k): 2.8614851155470165"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H
Total Standard Deviation in ln(k): 2.8614851155470165""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H
Total Standard Deviation in ln(k): 2.8614851155470165
""",
)

entry(
    index = 23,
    label = "Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = Arrhenius(A=(1.63e+08,'s^-1'), n=1.07, Ea=(213.91,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(7.65e+08,'s^-1'), n=0.9, Ea=(218.355,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O",
    kinetics = ArrheniusBM(A=(1.50376e+20,'s^-1'), n=-2.28936, w0=(866,'kJ/mol'), E0=(94.1353,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.900876006976125, var=13.349325257821501, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O
    Total Standard Deviation in ln(k): 9.588153668781676"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O
Total Standard Deviation in ln(k): 9.588153668781676""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O
Total Standard Deviation in ln(k): 9.588153668781676
""",
)

entry(
    index = 26,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_N-6R!H->O",
    kinetics = Arrhenius(A=(2.59e+10,'s^-1'), n=0.65, Ea=(93.4178,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_N-6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_N-6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C",
    kinetics = ArrheniusBM(A=(2.39759e+07,'s^-1'), n=1.55051, w0=(810.5,'kJ/mol'), E0=(376.445,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.43300657750663496, var=15.076349500593956, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C
    Total Standard Deviation in ln(k): 8.871996740934044"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C
Total Standard Deviation in ln(k): 8.871996740934044""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C
Total Standard Deviation in ln(k): 8.871996740934044
""",
)

entry(
    index = 28,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C",
    kinetics = ArrheniusBM(A=(1.09356e+06,'s^-1'), n=1.83434, w0=(810.5,'kJ/mol'), E0=(366.415,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9059763464226833, var=0.15395528289839308, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C
    Total Standard Deviation in ln(k): 3.062923104012861"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C
Total Standard Deviation in ln(k): 3.062923104012861""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C
Total Standard Deviation in ln(k): 3.062923104012861
""",
)

entry(
    index = 29,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.78614e+10,'s^-1'), n=0.778364, w0=(884.5,'kJ/mol'), E0=(324.662,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7551313941764735, var=5.234997645135004, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R
    Total Standard Deviation in ln(k): 6.484172419572765"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R
Total Standard Deviation in ln(k): 6.484172419572765""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R
Total Standard Deviation in ln(k): 6.484172419572765
""",
)

entry(
    index = 30,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(3.40038e+08,'s^-1'), n=1.04555, w0=(884.5,'kJ/mol'), E0=(303.522,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0007821082272592, var=0.2119403278590143, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 3.4374473425518404"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 3.4374473425518404""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 3.4374473425518404
""",
)

entry(
    index = 31,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(5.66667e+08,'s^-1'), n=1.16, Ea=(347.838,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H_Ext-2C-R",
    kinetics = Arrhenius(A=(1.865e+06,'s^-1'), n=1.71, Ea=(300.769,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C",
    kinetics = ArrheniusBM(A=(6.666e+11,'s^-1'), n=0.00203267, w0=(884.5,'kJ/mol'), E0=(177.986,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.697284958986286, var=1.4477353565343019, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C
    Total Standard Deviation in ln(k): 4.164107089482784"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C
Total Standard Deviation in ln(k): 4.164107089482784""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C
Total Standard Deviation in ln(k): 4.164107089482784
""",
)

entry(
    index = 34,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-7R!H->C",
    kinetics = Arrhenius(A=(6.23333e+10,'s^-1'), n=0.42, Ea=(209.094,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(6.36373e+12,'s^-1'), n=-0.26061, w0=(884.5,'kJ/mol'), E0=(58.3628,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6847717937346992, var=11.02719271076699, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R
    Total Standard Deviation in ln(k): 8.37769945007955"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R
Total Standard Deviation in ln(k): 8.37769945007955""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R
Total Standard Deviation in ln(k): 8.37769945007955
""",
)

entry(
    index = 36,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C_Ext-2C-R",
    kinetics = Arrhenius(A=(1.66e+07,'s^-1'), n=1.5, Ea=(382.799,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C_Ext-2C-R",
    kinetics = Arrhenius(A=(3.895e+06,'s^-1'), n=1.63, Ea=(392.778,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(5.8714e+09,'s^-1'), n=0.800009, w0=(884.5,'kJ/mol'), E0=(319.25,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4735898081875587, var=0.32894092038645445, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C
    Total Standard Deviation in ln(k): 2.3397072944610176"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C
Total Standard Deviation in ln(k): 2.3397072944610176""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C
Total Standard Deviation in ln(k): 2.3397072944610176
""",
)

entry(
    index = 39,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(1.19667e+11,'s^-1'), n=0.77, Ea=(346.77,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = Arrhenius(A=(4.77e+08,'s^-1'), n=1.06, Ea=(337.901,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(2.65e+08,'s^-1'), n=1.02, Ea=(339.685,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = Arrhenius(A=(2.235e+11,'s^-1'), n=0.12, Ea=(209.772,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(1.08e+12,'s^-1'), n=-0.04, Ea=(213.084,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(2.26868e+13,'s^-1'), n=-0.460544, w0=(884.5,'kJ/mol'), E0=(42.1607,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20493121391191868, var=2.5877165065631265, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C
    Total Standard Deviation in ln(k): 3.7397957545966576"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 3.7397957545966576""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 3.7397957545966576
""",
)

entry(
    index = 45,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(3.4e+06,'s^-1'), n=1.62, Ea=(129.638,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = Arrhenius(A=(5.9e+09,'s^-1'), n=0.8, Ea=(332.105,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = Arrhenius(A=(2.49e+09,'s^-1'), n=0.79, Ea=(333.774,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = Arrhenius(A=(4.5e+06,'s^-1'), n=1.39, Ea=(90.007,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(9.25e+06,'s^-1'), n=1.44, Ea=(99.829,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

