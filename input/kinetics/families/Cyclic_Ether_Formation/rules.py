#!/usr/bin/env python
# encoding: utf-8

name = "Cyclic_Ether_Formation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(6.70759e-23,'s^-1'), n=10.0447, w0=(250000,'J/mol'), E0=(19684.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5194161034165425, var=13.846531279511755, Tref=1000.0, N=74, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 74 training reactions at node Root
    Total Standard Deviation in ln(k): 8.764870755480315"""),
    rank = 11,
    shortDesc = """BM rule fitted to 74 training reactions at node Root
Total Standard Deviation in ln(k): 8.764870755480315""",
    longDesc = 
"""
BM rule fitted to 74 training reactions at node Root
Total Standard Deviation in ln(k): 8.764870755480315
""",
)

entry(
    index = 2,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s",
    kinetics = ArrheniusBM(A=(6.29283e+11,'s^-1'), n=0.191145, w0=(250000,'J/mol'), E0=(79056.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03403699726171831, var=6.741034077113351, Tref=1000.0, N=30, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s',), comment="""BM rule fitted to 30 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s
    Total Standard Deviation in ln(k): 5.290514303146694"""),
    rank = 11,
    shortDesc = """BM rule fitted to 30 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s
Total Standard Deviation in ln(k): 5.290514303146694""",
    longDesc = 
"""
BM rule fitted to 30 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s
Total Standard Deviation in ln(k): 5.290514303146694
""",
)

entry(
    index = 3,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(3.33686e-12,'s^-1'), n=6.68017, w0=(250000,'J/mol'), E0=(63477.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4510434858698292, var=3.1547733461536236, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 28 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 4.694021711477934"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 4.694021711477934""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 4.694021711477934
""",
)

entry(
    index = 4,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(376.176,'s^-1'), n=2.62989, w0=(250000,'J/mol'), E0=(106299,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.055455977229016344, var=3.0304356647941164, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 16 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 3.6292088293207425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 3.6292088293207425""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 3.6292088293207425
""",
)

entry(
    index = 5,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0",
    kinetics = ArrheniusBM(A=(6.25344e+11,'s^-1'), n=0.191259, w0=(250000,'J/mol'), E0=(78957.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.034358749532645644, var=6.749509916327004, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0',), comment="""BM rule fitted to 28 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0
    Total Standard Deviation in ln(k): 5.294593947734462"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0
Total Standard Deviation in ln(k): 5.294593947734462""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0
Total Standard Deviation in ln(k): 5.294593947734462
""",
)

entry(
    index = 6,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_N-2O2sS-u0",
    kinetics = ArrheniusBM(A=(6.72891e+10,'s^-1'), n=0.726304, w0=(250000,'J/mol'), E0=(110283,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006018531821652568, var=0.2629016607439153, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_N-2O2sS-u0',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_N-2O2sS-u0
    Total Standard Deviation in ln(k): 1.0430285382784328"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_N-2O2sS-u0
Total Standard Deviation in ln(k): 1.0430285382784328""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_N-2O2sS-u0
Total Standard Deviation in ln(k): 1.0430285382784328
""",
)

entry(
    index = 7,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C",
    kinetics = ArrheniusBM(A=(1.1685e-12,'s^-1'), n=6.81109, w0=(250000,'J/mol'), E0=(61793.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.46528951435722815, var=3.323848194875913, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C',), comment="""BM rule fitted to 21 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C
    Total Standard Deviation in ln(k): 4.823986643227463"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C
Total Standard Deviation in ln(k): 4.823986643227463""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C
Total Standard Deviation in ln(k): 4.823986643227463
""",
)

entry(
    index = 8,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.0385301,'s^-1'), n=3.75291, w0=(250000,'J/mol'), E0=(91042.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.9329521967910932, var=3.92281545737638, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C
    Total Standard Deviation in ln(k): 8.827261892173844"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C
Total Standard Deviation in ln(k): 8.827261892173844""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C
Total Standard Deviation in ln(k): 8.827261892173844
""",
)

entry(
    index = 9,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(122548,'s^-1'), n=1.86736, w0=(250000,'J/mol'), E0=(116932,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.027616158688162622, var=1.0066049344189716, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 2.080732086482132"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.080732086482132""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.080732086482132
""",
)

entry(
    index = 10,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.15553e+06,'s^-1'), n=1.6347, w0=(250000,'J/mol'), E0=(92451.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.7763568394002489e-15, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 4.463208139196605e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 4.463208139196605e-15""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 4.463208139196605e-15
""",
)

entry(
    index = 11,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.78537e+07,'s^-1'), n=1.45978, w0=(250000,'J/mol'), E0=(59910.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05657773171321969, var=1.8488060126256476, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R',), comment="""BM rule fitted to 11 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.868009550798379"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.868009550798379""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.868009550798379
""",
)

entry(
    index = 12,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.04969e+16,'s^-1'), n=-1.21797, w0=(250000,'J/mol'), E0=(97794,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1268393435491246, var=13.090955552409367, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R',), comment="""BM rule fitted to 15 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R
    Total Standard Deviation in ln(k): 7.572109114121481"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R
Total Standard Deviation in ln(k): 7.572109114121481""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R
Total Standard Deviation in ln(k): 7.572109114121481
""",
)

entry(
    index = 13,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_N-2O2sS-u0_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.27e+09,'s^-1'), n=1.06, w0=(250000,'J/mol'), E0=(105593,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_N-2O2sS-u0_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_N-2O2sS-u0_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_N-2O2sS-u0_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_N-2O2sS-u0_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H",
    kinetics = ArrheniusBM(A=(9.61553e-30,'s^-1'), n=11.9704, w0=(250000,'J/mol'), E0=(5488.33,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.642368920589455, var=0.9300896811869628, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H
    Total Standard Deviation in ln(k): 3.547381971238793"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H
Total Standard Deviation in ln(k): 3.547381971238793""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H
Total Standard Deviation in ln(k): 3.547381971238793
""",
)

entry(
    index = 15,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.35093e-16,'s^-1'), n=7.79793, w0=(250000,'J/mol'), E0=(-18656,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.43367130413522254, var=0.3823118925558745, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 2.329181654327898"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 2.329181654327898""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 2.329181654327898
""",
)

entry(
    index = 16,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(4.22191e-28,'s^-1'), n=11.2153, w0=(250000,'J/mol'), E0=(5349.83,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5632841452923574, var=1.3743717133941338, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 3.765509913015097"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.765509913015097""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.765509913015097
""",
)

entry(
    index = 17,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Int-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(2.70167e+08,'s^-1'), n=0.912542, w0=(250000,'J/mol'), E0=(122327,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0091670185637663, var=2.748823886331576, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Int-5R!H-3R!H',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Int-5R!H-3R!H
    Total Standard Deviation in ln(k): 3.3467987594833817"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Int-5R!H-3R!H
Total Standard Deviation in ln(k): 3.3467987594833817""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Int-5R!H-3R!H
Total Standard Deviation in ln(k): 3.3467987594833817
""",
)

entry(
    index = 18,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(621500,'s^-1'), n=1.85768, w0=(250000,'J/mol'), E0=(131317,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.008203849520416976, var=0.2756923264723975, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 1.073227139535365"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.073227139535365""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.073227139535365
""",
)

entry(
    index = 19,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(5.13194e+12,'s^-1'), n=-0.579326, w0=(250000,'J/mol'), E0=(125600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.13253595456142747, var=0.2126096490460096, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 1.2573805140915915"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.2573805140915915""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.2573805140915915
""",
)

entry(
    index = 20,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.93488e+08,'s^-1'), n=1.20895, w0=(250000,'J/mol'), E0=(61866.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03323452158007817, var=2.175967060827832, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 3.0407205077772943"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.0407205077772943""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.0407205077772943
""",
)

entry(
    index = 21,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(4.28768e+06,'s^-1'), n=1.69876, w0=(250000,'J/mol'), E0=(67474.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.006084510941035465, var=0.40283284385558615, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 1.2876753086455748"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 1.2876753086455748""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 1.2876753086455748
""",
)

entry(
    index = 22,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(3.32613e+12,'s^-1'), n=0.0376539, w0=(250000,'J/mol'), E0=(101697,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.012674312579452016, var=47.495514338260165, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 9 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 13.847875622871287"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 13.847875622871287""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 13.847875622871287
""",
)

entry(
    index = 23,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-2O2sS-R",
    kinetics = ArrheniusBM(A=(9.27152e+10,'s^-1'), n=0.133324, w0=(250000,'J/mol'), E0=(121007,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0037339776687244828, var=0.5321622773559461, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-2O2sS-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-2O2sS-R
    Total Standard Deviation in ln(k): 1.4718251375665967"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-2O2sS-R
Total Standard Deviation in ln(k): 1.4718251375665967""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-2O2sS-R
Total Standard Deviation in ln(k): 1.4718251375665967
""",
)

entry(
    index = 24,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.8432e+11,'s^-1'), n=-0.00242351, w0=(250000,'J/mol'), E0=(99320.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0066825222566423625, var=0.4807058886644431, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-6R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 1.4067323603574724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.4067323603574724""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.4067323603574724
""",
)

entry(
    index = 25,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H",
    kinetics = ArrheniusBM(A=(6.65727e-17,'s^-1'), n=7.8974, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.432215115943695, var=0.3150737508117761, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H
    Total Standard Deviation in ln(k): 2.2112541079154506"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H
Total Standard Deviation in ln(k): 2.2112541079154506""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H
Total Standard Deviation in ln(k): 2.2112541079154506
""",
)

entry(
    index = 26,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-2O2sS-R",
    kinetics = ArrheniusBM(A=(1.17e+09,'s^-1'), n=0, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-2O2sS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-2O2sS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-2O2sS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-2O2sS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-2O2sS-R",
    kinetics = ArrheniusBM(A=(4.76338e-29,'s^-1'), n=11.5319, w0=(250000,'J/mol'), E0=(-8148.23,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.7678357328038395, var=15.148652715130089, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-2O2sS-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-2O2sS-R
    Total Standard Deviation in ln(k): 9.73191906586784"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-2O2sS-R
Total Standard Deviation in ln(k): 9.73191906586784""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-2O2sS-R
Total Standard Deviation in ln(k): 9.73191906586784
""",
)

entry(
    index = 28,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.43755e-31,'s^-1'), n=12.3015, w0=(250000,'J/mol'), E0=(14387.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.61072390931423, var=17.87006595282664, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 22.571913004394496"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 22.571913004394496""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 22.571913004394496
""",
)

entry(
    index = 29,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Int-5R!H-3R!H_6R!H->C",
    kinetics = ArrheniusBM(A=(1.5149e+08,'s^-1'), n=0.942221, w0=(250000,'J/mol'), E0=(123208,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.005490660518239428, var=1.4845665753717427, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Int-5R!H-3R!H_6R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Int-5R!H-3R!H_6R!H->C
    Total Standard Deviation in ln(k): 2.4564208027791183"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Int-5R!H-3R!H_6R!H->C
Total Standard Deviation in ln(k): 2.4564208027791183""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Int-5R!H-3R!H_6R!H->C
Total Standard Deviation in ln(k): 2.4564208027791183
""",
)

entry(
    index = 30,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Int-5R!H-3R!H_N-6R!H->C",
    kinetics = ArrheniusBM(A=(2.38891e+10,'s^-1'), n=0.588176, w0=(250000,'J/mol'), E0=(125236,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Int-5R!H-3R!H_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Int-5R!H-3R!H_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Int-5R!H-3R!H_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Int-5R!H-3R!H_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.78705e+09,'s^-1'), n=0.83402, w0=(250000,'J/mol'), E0=(146382,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5.94659e+07,'s^-1'), n=0.973724, w0=(250000,'J/mol'), E0=(123535,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 33,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-2O2sS-R",
    kinetics = ArrheniusBM(A=(9.18271e+13,'s^-1'), n=-0.47522, w0=(250000,'J/mol'), E0=(89629.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0018908511124089997, var=0.2580170495707488, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-2O2sS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-2O2sS-R
    Total Standard Deviation in ln(k): 1.023063656376468"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-2O2sS-R
Total Standard Deviation in ln(k): 1.023063656376468""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-2O2sS-R
Total Standard Deviation in ln(k): 1.023063656376468
""",
)

entry(
    index = 34,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.34253e+09,'s^-1'), n=0.952761, w0=(250000,'J/mol'), E0=(60054.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02834323204165119, var=0.2214385871254625, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.0145875810330476"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.0145875810330476""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.0145875810330476
""",
)

entry(
    index = 35,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.49381e+08,'s^-1'), n=1.11685, w0=(250000,'J/mol'), E0=(62482.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.4424906541753475e-15, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 6.1369111913953454e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 6.1369111913953454e-15""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 6.1369111913953454e-15
""",
)

entry(
    index = 36,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(6.81075e+07,'s^-1'), n=1.33311, w0=(250000,'J/mol'), E0=(63289.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.7763568394002489e-15, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 4.463208139196605e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.463208139196605e-15""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.463208139196605e-15
""",
)

entry(
    index = 37,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(9.29513e+07,'s^-1'), n=1.29023, w0=(250000,'J/mol'), E0=(72050.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=8.881784197001247e-16, var=1.944692274331607e-62, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 2.2316040695983036e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.2316040695983036e-15""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.2316040695983036e-15
""",
)

entry(
    index = 38,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(8.50679e+10,'s^-1'), n=0.546937, w0=(250000,'J/mol'), E0=(137794,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.6653345369377362e-15, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 4.184257630496824e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.184257630496824e-15""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.184257630496824e-15
""",
)

entry(
    index = 39,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_5R!H->C",
    kinetics = ArrheniusBM(A=(1.39316e-24,'s^-1'), n=10.708, w0=(250000,'J/mol'), E0=(-34475.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.5994182062711602, var=14.800697117773407, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_5R!H->C
    Total Standard Deviation in ln(k): 11.731190174352808"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_5R!H->C
Total Standard Deviation in ln(k): 11.731190174352808""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_5R!H->C
Total Standard Deviation in ln(k): 11.731190174352808
""",
)

entry(
    index = 40,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-5R!H->C",
    kinetics = ArrheniusBM(A=(2.4664e+21,'s^-1'), n=-2.36645, w0=(250000,'J/mol'), E0=(99832.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0813976698235791, var=12.034380911417225, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-5R!H->C
    Total Standard Deviation in ln(k): 7.159064074175162"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-5R!H->C
Total Standard Deviation in ln(k): 7.159064074175162""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-5R!H->C
Total Standard Deviation in ln(k): 7.159064074175162
""",
)

entry(
    index = 41,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-2O2sS-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(6.49973e+11,'s^-1'), n=-0.123415, w0=(250000,'J/mol'), E0=(124875,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0004997226811695135, var=0.12607169796406748, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-2O2sS-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-2O2sS-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 0.7130683798838977"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-2O2sS-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 0.7130683798838977""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-2O2sS-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 0.7130683798838977
""",
)

entry(
    index = 42,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-6R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.79088e+12,'s^-1'), n=-0.245121, w0=(250000,'J/mol'), E0=(102930,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00047906195141407315, var=0.12280473020872217, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-6R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-6R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 0.7037331273192441"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-6R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 0.7037331273192441""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-6R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 0.7037331273192441
""",
)

entry(
    index = 43,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.32175e-15,'s^-1'), n=7.42132, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4097690300683688, var=0.10555409043770493, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-3R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.6808905909171852"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.6808905909171852""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.6808905909171852
""",
)

entry(
    index = 44,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-2O2sS-R",
    kinetics = ArrheniusBM(A=(6.81699e-20,'s^-1'), n=8.82014, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.732247689467373, var=0.13880440424672924, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-2O2sS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-2O2sS-R
    Total Standard Deviation in ln(k): 15.14952576989008"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-2O2sS-R
Total Standard Deviation in ln(k): 15.14952576989008""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-2O2sS-R
Total Standard Deviation in ln(k): 15.14952576989008
""",
)

entry(
    index = 45,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-2O2sS-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.97983e-31,'s^-1'), n=12.117, w0=(250000,'J/mol'), E0=(-296.321,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05159657178977463, var=18.021703513970937, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-2O2sS-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-2O2sS-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 8.640136367720634"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-2O2sS-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 8.640136367720634""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-2O2sS-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 8.640136367720634
""",
)

entry(
    index = 46,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-3R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.27e+08,'s^-1'), n=0.77, w0=(250000,'J/mol'), E0=(101215,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-3R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-3R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-3R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-3R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Int-5R!H-3R!H_6R!H->C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.07483e+09,'s^-1'), n=0.624153, w0=(250000,'J/mol'), E0=(120126,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Int-5R!H-3R!H_6R!H->C_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Int-5R!H-3R!H_6R!H->C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Int-5R!H-3R!H_6R!H->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-5R!H-R_Int-5R!H-3R!H_6R!H->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 48,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-2O2sS-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.09e+12,'s^-1'), n=0, w0=(250000,'J/mol'), E0=(87086.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-2O2sS-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-2O2sS-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-2O2sS-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-2O2sS-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3.87019e+11,'s^-1'), n=0.301869, w0=(250000,'J/mol'), E0=(65278.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.218847493575586e-15, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 1.0600119330591924e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.0600119330591924e-14""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.0600119330591924e-14
""",
)

entry(
    index = 50,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Sp-6R!H-4R!H",
    kinetics = ArrheniusBM(A=(1.4467e+10,'s^-1'), n=0.719639, w0=(250000,'J/mol'), E0=(64185,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.887379141862768e-15, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Sp-6R!H-4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Sp-6R!H-4R!H
    Total Standard Deviation in ln(k): 4.742158647896402e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Sp-6R!H-4R!H
Total Standard Deviation in ln(k): 4.742158647896402e-15""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Sp-6R!H-4R!H
Total Standard Deviation in ln(k): 4.742158647896402e-15
""",
)

entry(
    index = 51,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-6R!H-4R!H",
    kinetics = ArrheniusBM(A=(3.09e+12,'s^-1'), n=0, w0=(250000,'J/mol'), E0=(59528,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-6R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-6R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-6R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_N-Sp-6R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_5R!H->C_Ext-2O2sS-R",
    kinetics = ArrheniusBM(A=(2.0043e+13,'s^-1'), n=-0.238411, w0=(250000,'J/mol'), E0=(83399.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.945373279193557, var=55.570159453833924, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_5R!H->C_Ext-2O2sS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_5R!H->C_Ext-2O2sS-R
    Total Standard Deviation in ln(k): 27.369937864374403"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_5R!H->C_Ext-2O2sS-R
Total Standard Deviation in ln(k): 27.369937864374403""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_5R!H->C_Ext-2O2sS-R
Total Standard Deviation in ln(k): 27.369937864374403
""",
)

entry(
    index = 53,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-5R!H->C_Ext-2O2sS-R",
    kinetics = ArrheniusBM(A=(6.92e+15,'s^-1'), n=-0.53, w0=(250000,'J/mol'), E0=(79928.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-5R!H->C_Ext-2O2sS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-5R!H->C_Ext-2O2sS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-5R!H->C_Ext-2O2sS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-5R!H->C_Ext-2O2sS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-2O2sS-R_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.31e+11,'s^-1'), n=0, w0=(250000,'J/mol'), E0=(125253,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-2O2sS-R_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-2O2sS-R_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-2O2sS-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-2O2sS-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.31e+11,'s^-1'), n=0, w0=(250000,'J/mol'), E0=(101885,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-3R!H-R_Int-6R!H-4R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(6.74113e-14,'s^-1'), n=6.96696, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.7870181052988094, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 14.54024649572565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 14.54024649572565""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 14.54024649572565
""",
)

entry(
    index = 57,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-2O2sS-R",
    kinetics = ArrheniusBM(A=(3.63e+10,'s^-1'), n=0, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-2O2sS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-2O2sS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-2O2sS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-2O2sS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-2O2sS-R_Ext-3R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.27e+08,'s^-1'), n=0.77, w0=(250000,'J/mol'), E0=(81432,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-2O2sS-R_Ext-3R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-2O2sS-R_Ext-3R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-2O2sS-R_Ext-3R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Ext-2O2sS-R_Ext-3R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-2O2sS-R",
    kinetics = ArrheniusBM(A=(2.57e+10,'s^-1'), n=0, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-2O2sS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-2O2sS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-2O2sS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_5R!H->C_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-2O2sS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

