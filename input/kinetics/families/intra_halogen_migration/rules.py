#!/usr/bin/env python
# encoding: utf-8

name = "intra_halogen_migration/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(73600,'s^-1'), n=2.14076, w0=(402.867,'kJ/mol'), E0=(161.119,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.014866566456864828, var=62.49309910848178, Tref=1000.0, N=30, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 30 training reactions at node Root
    Total Standard Deviation in ln(k): 15.885300564366162"""),
    rank = 11,
    shortDesc = """BM rule fitted to 30 training reactions at node Root
Total Standard Deviation in ln(k): 15.885300564366162""",
    longDesc = 
"""
BM rule fitted to 30 training reactions at node Root
Total Standard Deviation in ln(k): 15.885300564366162
""",
)

entry(
    index = 2,
    label = "Root_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(10183.2,'s^-1'), n=2.37014, w0=(399.08,'kJ/mol'), E0=(174.106,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.003546023088271871, var=42.2293323146656, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_Ext-1R!H-R',), comment="""BM rule fitted to 25 training reactions at node Root_Ext-1R!H-R
    Total Standard Deviation in ln(k): 13.036500047116386"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_Ext-1R!H-R
Total Standard Deviation in ln(k): 13.036500047116386""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_Ext-1R!H-R
Total Standard Deviation in ln(k): 13.036500047116386
""",
)

entry(
    index = 3,
    label = "Root_2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(2.61753e+11,'s^-1'), n=0.321632, w0=(485,'kJ/mol'), E0=(140.884,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04898352266967566, var=0.054583316810677664, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 0.5914418920461092"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 0.5914418920461092""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 0.5914418920461092
""",
)

entry(
    index = 4,
    label = "Root_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(1.03108e+13,'s^-1'), n=-0.0707693, w0=(327,'kJ/mol'), E0=(47.2642,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=6.106226635432932e-16, var=2.1672042848442442e-27, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 9.486114379877195e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 9.486114379877195e-14""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 9.486114379877195e-14
""",
)

entry(
    index = 5,
    label = "Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(892713,'s^-1'), n=1.87194, w0=(485,'kJ/mol'), E0=(212.151,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07539747831426202, var=42.06543845186797, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 13 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 13.191726444823049"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 13.191726444823049""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 13.191726444823049
""",
)

entry(
    index = 6,
    label = "Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(41765.8,'s^-1'), n=2.1312, w0=(306,'kJ/mol'), E0=(139.733,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2015698184572226e-09, var=16.490428839011596, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 8.1409102048649"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 8.1409102048649""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 8.1409102048649
""",
)

entry(
    index = 7,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3R!H-R",
    kinetics = Arrhenius(A=(3.36622e+11,'s^-1'), n=0.48217, Ea=(122.23,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H",
    kinetics = ArrheniusBM(A=(3.338e+15,'s^-1'), n=-0.689115, w0=(485,'kJ/mol'), E0=(195.814,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11049932985712133, var=28.039792972116313, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H
    Total Standard Deviation in ln(k): 10.893232718736371"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H
Total Standard Deviation in ln(k): 10.893232718736371""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H
Total Standard Deviation in ln(k): 10.893232718736371
""",
)

entry(
    index = 9,
    label = "Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Ext-1R!H-R",
    kinetics = Arrhenius(A=(0.00363316,'s^-1'), n=4.43046, Ea=(275.819,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(0.00149505,'s^-1'), n=4.17007, w0=(485,'kJ/mol'), E0=(206.151,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03078112078819946, var=13.803754304479513, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Ext-3R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Ext-3R!H-R
    Total Standard Deviation in ln(k): 7.525612728287914"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Ext-3R!H-R
Total Standard Deviation in ln(k): 7.525612728287914""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Ext-3R!H-R
Total Standard Deviation in ln(k): 7.525612728287914
""",
)

entry(
    index = 11,
    label = "Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Br1s",
    kinetics = ArrheniusBM(A=(4.41069e+09,'s^-1'), n=0.616349, w0=(285,'kJ/mol'), E0=(131.367,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=9.747329017586542e-16, var=9.769200441791195, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Br1s',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Br1s
    Total Standard Deviation in ln(k): 6.265943862075344"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 6.265943862075344""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 6.265943862075344
""",
)

entry(
    index = 12,
    label = "Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Br1s",
    kinetics = ArrheniusBM(A=(0.39549,'s^-1'), n=3.64605, w0=(327,'kJ/mol'), E0=(148.098,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=7.497945398143493e-16, var=18.750823562185808, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Br1s',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Br1s
    Total Standard Deviation in ln(k): 8.68094816614247"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 8.68094816614247""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 8.68094816614247
""",
)

entry(
    index = 13,
    label = "Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_4R!H->C",
    kinetics = Arrhenius(A=(1.00763e+12,'s^-1'), n=0.18834, Ea=(147.694,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_N-4R!H->C",
    kinetics = ArrheniusBM(A=(2.4588e+16,'s^-1'), n=-0.904809, w0=(485,'kJ/mol'), E0=(199.153,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10546746446034765, var=42.52103840260307, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_N-4R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_N-4R!H->C
    Total Standard Deviation in ln(k): 13.33750175144769"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_N-4R!H->C
Total Standard Deviation in ln(k): 13.33750175144769""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_N-4R!H->C
Total Standard Deviation in ln(k): 13.33750175144769
""",
)

entry(
    index = 15,
    label = "Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Ext-3R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.64853e+07,'s^-1'), n=1.15307, w0=(485,'kJ/mol'), E0=(198.221,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.7208456881725064e-15, var=1.407081952178991e-26, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Ext-3R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Ext-3R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 2.421263805701797e-13"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.421263805701797e-13""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.421263805701797e-13
""",
)

entry(
    index = 16,
    label = "Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = Arrhenius(A=(0.000550858,'s^-1'), n=4.50663, Ea=(210.996,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Br1s_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.27378e+10,'s^-1'), n=0.273889, w0=(285,'kJ/mol'), E0=(129.742,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-5.411542368436271e-09, var=11.345806263616348, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Br1s_Ext-3R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Br1s_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.75265671458043"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Br1s_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.75265671458043""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Br1s_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.75265671458043
""",
)

entry(
    index = 18,
    label = "Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Br1s_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(0.000101519,'s^-1'), n=4.51852, w0=(327,'kJ/mol'), E0=(137.324,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3496301716658287e-15, var=32.23272297005063, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Br1s_Ext-3R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Br1s_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.381656835464497"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Br1s_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.381656835464497""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Br1s_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.381656835464497
""",
)

entry(
    index = 19,
    label = "Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_N-4R!H->C_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(7.4031e+14,'s^-1'), n=-0.53954, w0=(485,'kJ/mol'), E0=(207.588,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.016227018596173114, var=30.942213027442286, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_N-4R!H->C_Ext-3R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_N-4R!H->C_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.192255652591074"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_N-4R!H->C_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.192255652591074""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_N-4R!H->C_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.192255652591074
""",
)

entry(
    index = 20,
    label = "Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Br1s_Ext-3R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.68639e+09,'s^-1'), n=0.389834, w0=(285,'kJ/mol'), E0=(137.78,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.551115122868812e-17, var=1.027171470605204e-26, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Br1s_Ext-3R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Br1s_Ext-3R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 2.0331830924623818e-13"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Br1s_Ext-3R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 2.0331830924623818e-13""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Br1s_Ext-3R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 2.0331830924623818e-13
""",
)

entry(
    index = 21,
    label = "Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Br1s_Ext-3R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.11837e-16,'s^-1'), n=7.45351, w0=(327,'kJ/mol'), E0=(118.459,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.241318310806563e-27, var=1.299342657750844e-26, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Br1s_Ext-3R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Br1s_Ext-3R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 2.285171703766396e-13"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Br1s_Ext-3R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 2.285171703766396e-13""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Br1s_Ext-3R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 2.285171703766396e-13
""",
)

entry(
    index = 22,
    label = "Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_N-4R!H->C_Ext-3R!H-R_5R!H->C",
    kinetics = Arrhenius(A=(4.35648e+12,'s^-1'), n=0.369741, Ea=(221.636,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_N-4R!H->C_Ext-3R!H-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_N-4R!H->C_Ext-3R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_N-4R!H->C_Ext-3R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_N-4R!H->C_Ext-3R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_N-4R!H->C_Ext-3R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.2804e+11,'s^-1'), n=0.253035, w0=(485,'kJ/mol'), E0=(209.151,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.7208456881732416e-15, var=1.6962241258457807e-26, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_N-4R!H->C_Ext-3R!H-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_N-4R!H->C_Ext-3R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 2.654187643275793e-13"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_N-4R!H->C_Ext-3R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 2.654187643275793e-13""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_2Br1sCl1sF1s->F1s_Int-3R!H-1R!H_N-4R!H->C_Ext-3R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 2.654187643275793e-13
""",
)

