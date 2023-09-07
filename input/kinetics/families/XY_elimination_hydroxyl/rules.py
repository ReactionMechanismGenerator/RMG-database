#!/usr/bin/env python
# encoding: utf-8

name = "XY_elimination_hydroxyl/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(0.00285451,'s^-1'), n=4.62568, w0=(1253.93,'kJ/mol'), E0=(135.843,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3917696014098424, var=52.52930589142705, Tref=1000.0, N=14, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 14 training reactions at node Root
    Total Standard Deviation in ln(k): 15.514084980998286"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root
Total Standard Deviation in ln(k): 15.514084980998286""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root
Total Standard Deviation in ln(k): 15.514084980998286
""",
)

entry(
    index = 2,
    label = "Root_1R!H->C",
    kinetics = ArrheniusBM(A=(3.64531e+07,'s^-1'), n=1.71728, w0=(1225.72,'kJ/mol'), E0=(193.249,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5855571181388681, var=35.63933279604604, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_1R!H->C
    Total Standard Deviation in ln(k): 13.439254314964856"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 13.439254314964856""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 13.439254314964856
""",
)

entry(
    index = 3,
    label = "Root_1R!H->C_5Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(68453,'s^-1'), n=2.17099, w0=(1172.5,'kJ/mol'), E0=(283.281,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_5Br1sCl1sF1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_5Br1sCl1sF1sH->H
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
    index = 4,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(2.17278e+10,'s^-1'), n=0.963056, w0=(1232.38,'kJ/mol'), E0=(188.081,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7392837992584066, var=5.123657724233152, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 6.395314678574009"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 6.395314678574009""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 6.395314678574009
""",
)

entry(
    index = 5,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(7.67554e+10,'s^-1'), n=0.7707, w0=(1276,'kJ/mol'), E0=(187.082,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.772164474828081, var=7.843904779608195, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 7.554767654321687"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 7.554767654321687""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 7.554767654321687
""",
)

entry(
    index = 6,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R",
    kinetics = ArrheniusBM(A=(9.47486e+10,'s^-1'), n=0.762169, w0=(1276,'kJ/mol'), E0=(190.024,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6752920127042139, var=10.54390371806868, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R
    Total Standard Deviation in ln(k): 8.206364594802137"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R
Total Standard Deviation in ln(k): 8.206364594802137""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R
Total Standard Deviation in ln(k): 8.206364594802137
""",
)

entry(
    index = 7,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_7R!H->O",
    kinetics = ArrheniusBM(A=(1.30828e+07,'s^-1'), n=1.83354, w0=(1276,'kJ/mol'), E0=(200.292,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.49335582114639515, var=20.078174816455903, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_7R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_7R!H->O
    Total Standard Deviation in ln(k): 10.222540027456574"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_7R!H->O
Total Standard Deviation in ln(k): 10.222540027456574""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_7R!H->O
Total Standard Deviation in ln(k): 10.222540027456574
""",
)

entry(
    index = 8,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O",
    kinetics = ArrheniusBM(A=(4.26241e+10,'s^-1'), n=0.884589, w0=(1276,'kJ/mol'), E0=(175.737,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7509730348638922, var=0.7499895236794094, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O
    Total Standard Deviation in ln(k): 3.623006300954139"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O
Total Standard Deviation in ln(k): 3.623006300954139""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O
Total Standard Deviation in ln(k): 3.623006300954139
""",
)

entry(
    index = 9,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C",
    kinetics = ArrheniusBM(A=(8.86023e+09,'s^-1'), n=1.0283, w0=(1276,'kJ/mol'), E0=(173.571,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7239647048627136, var=0.5241804487032486, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C
    Total Standard Deviation in ln(k): 3.2704411513231233"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C
Total Standard Deviation in ln(k): 3.2704411513231233""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C
Total Standard Deviation in ln(k): 3.2704411513231233
""",
)

entry(
    index = 10,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.98542e+10,'s^-1'), n=0.978818, w0=(1276,'kJ/mol'), E0=(179.69,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_N-Sp-7BrCClFINPSSi-2C",
    kinetics = ArrheniusBM(A=(1.52349e+10,'s^-1'), n=1.11612, w0=(1276,'kJ/mol'), E0=(175.513,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_N-Sp-7BrCClFINPSSi-2C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_N-Sp-7BrCClFINPSSi-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_N-Sp-7BrCClFINPSSi-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_N-Sp-7BrCClFINPSSi-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(2.2943e+08,'s^-1'), n=1.63527, w0=(1101.5,'kJ/mol'), E0=(190.24,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6304504151364015, var=1.0798359331316199, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 3.6672698218446667"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 3.6672698218446667""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 3.6672698218446667
""",
)

entry(
    index = 13,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_5Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.20378e+08,'s^-1'), n=1.70445, w0=(1128.5,'kJ/mol'), E0=(192.038,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_5Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_5Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_5Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_5Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_N-5Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(3.23964e+08,'s^-1'), n=1.60341, w0=(1074.5,'kJ/mol'), E0=(188.115,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_N-5Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_N-5Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_N-5Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_N-5Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_N-1R!H->C",
    kinetics = ArrheniusBM(A=(3.84885e+11,'s^-1'), n=0.600381, w0=(1304.7,'kJ/mol'), E0=(114.086,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9242126708875531, var=2.1145753649170893, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R!H->C
    Total Standard Deviation in ln(k): 5.237343854331067"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 5.237343854331067""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 5.237343854331067
""",
)

entry(
    index = 16,
    label = "Root_N-1R!H->C_5Br1sCl1sF1sH->F1s",
    kinetics = ArrheniusBM(A=(3.11215e+13,'s^-1'), n=-0.0659839, w0=(1374.5,'kJ/mol'), E0=(113.9,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0226815513193352, var=5.125801261421659, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_5Br1sCl1sF1sH->F1s',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s
    Total Standard Deviation in ln(k): 7.1083184550979075"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s
Total Standard Deviation in ln(k): 7.1083184550979075""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s
Total Standard Deviation in ln(k): 7.1083184550979075
""",
)

entry(
    index = 17,
    label = "Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(5.29418e+10,'s^-1'), n=0.745914, w0=(1374.5,'kJ/mol'), E0=(108.877,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_7R!H->C
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
    index = 18,
    label = "Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(5.65824e+14,'s^-1'), n=-0.436116, w0=(1374.5,'kJ/mol'), E0=(116.081,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9927400314419011, var=19.60363129417426, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.37048434634411"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.37048434634411""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.37048434634411
""",
)

entry(
    index = 19,
    label = "Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(6.14547e+10,'s^-1'), n=0.631481, w0=(1374.5,'kJ/mol'), E0=(87.4383,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s",
    kinetics = ArrheniusBM(A=(4.91718e+09,'s^-1'), n=1.32259, w0=(1200,'kJ/mol'), E0=(116.765,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7915497219668105, var=2.215712995420175, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s
    Total Standard Deviation in ln(k): 4.972920933704612"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s
Total Standard Deviation in ln(k): 4.972920933704612""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s
Total Standard Deviation in ln(k): 4.972920933704612
""",
)

entry(
    index = 21,
    label = "Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_5Br1sCl1sH->Cl1s",
    kinetics = ArrheniusBM(A=(3.42848e+09,'s^-1'), n=1.33002, w0=(1227,'kJ/mol'), E0=(118.674,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_5Br1sCl1sH->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_5Br1sCl1sH->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_5Br1sCl1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_5Br1sCl1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_N-5Br1sCl1sH->Cl1s",
    kinetics = ArrheniusBM(A=(4.74683e+09,'s^-1'), n=1.36442, w0=(1173,'kJ/mol'), E0=(114.427,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_N-5Br1sCl1sH->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_N-5Br1sCl1sH->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_N-5Br1sCl1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_N-5Br1sCl1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

