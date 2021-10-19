#!/usr/bin/env python
# encoding: utf-8

name = "1,3_sigmatropic_rearrangement/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(5.36025e-75,'s^-1'), n=26.0114, w0=(735278,'J/mol'), E0=(-18847.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0014814239980872, var=102.87700592211432, Tref=1000.0, N=72, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 72 training reactions at node Root
    Total Standard Deviation in ln(k): 22.849972614810042"""),
    rank = 11,
    shortDesc = """BM rule fitted to 72 training reactions at node Root
Total Standard Deviation in ln(k): 22.849972614810042""",
    longDesc = 
"""
BM rule fitted to 72 training reactions at node Root
Total Standard Deviation in ln(k): 22.849972614810042
""",
)

entry(
    index = 2,
    label = "Root_1R!H-inRing",
    kinetics = ArrheniusBM(A=(1.37447e+24,'s^-1'), n=-2.86863, w0=(682344,'J/mol'), E0=(346122,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.24783434109764116, var=169.16650822293855, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R!H-inRing',), comment="""BM rule fitted to 16 training reactions at node Root_1R!H-inRing
    Total Standard Deviation in ln(k): 26.697090843880112"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 26.697090843880112""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 26.697090843880112
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(3.50759e-62,'s^-1'), n=22.1275, w0=(750402,'J/mol'), E0=(-20429.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8800459367924431, var=31.676078103554833, Tref=1000.0, N=56, data_mean=0.0, correlation='Root_N-1R!H-inRing',), comment="""BM rule fitted to 56 training reactions at node Root_N-1R!H-inRing
    Total Standard Deviation in ln(k): 13.494121433083981"""),
    rank = 11,
    shortDesc = """BM rule fitted to 56 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 13.494121433083981""",
    longDesc = 
"""
BM rule fitted to 56 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 13.494121433083981
""",
)

entry(
    index = 4,
    label = "Root_1R!H-inRing_4R->N",
    kinetics = ArrheniusBM(A=(4.0435e+11,'s^-1'), n=1.01704, w0=(559500,'J/mol'), E0=(135903,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_4R->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_4R->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_4R->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_4R->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_1R!H-inRing_N-4R->N",
    kinetics = ArrheniusBM(A=(1.68103e+23,'s^-1'), n=-2.61902, w0=(690533,'J/mol'), E0=(358178,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.24185951672063075, var=131.1729658832691, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N',), comment="""BM rule fitted to 15 training reactions at node Root_1R!H-inRing_N-4R->N
    Total Standard Deviation in ln(k): 23.56807183139528"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_1R!H-inRing_N-4R->N
Total Standard Deviation in ln(k): 23.56807183139528""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_1R!H-inRing_N-4R->N
Total Standard Deviation in ln(k): 23.56807183139528
""",
)

entry(
    index = 6,
    label = "Root_N-1R!H-inRing_2R!H->C",
    kinetics = ArrheniusBM(A=(0.00280882,'s^-1'), n=4.73143, w0=(762750,'J/mol'), E0=(254186,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0682640946252418, var=221.53427713373026, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_2R!H->C
    Total Standard Deviation in ln(k): 30.01005001707717"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_2R!H->C
Total Standard Deviation in ln(k): 30.01005001707717""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_2R!H->C
Total Standard Deviation in ln(k): 30.01005001707717
""",
)

entry(
    index = 7,
    label = "Root_N-1R!H-inRing_N-2R!H->C",
    kinetics = ArrheniusBM(A=(2.69879e-62,'s^-1'), n=22.1571, w0=(749452,'J/mol'), E0=(-20749.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9531070000081657, var=31.327014816049115, Tref=1000.0, N=52, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C',), comment="""BM rule fitted to 52 training reactions at node Root_N-1R!H-inRing_N-2R!H->C
    Total Standard Deviation in ln(k): 13.615351929384866"""),
    rank = 11,
    shortDesc = """BM rule fitted to 52 training reactions at node Root_N-1R!H-inRing_N-2R!H->C
Total Standard Deviation in ln(k): 13.615351929384866""",
    longDesc = 
"""
BM rule fitted to 52 training reactions at node Root_N-1R!H-inRing_N-2R!H->C
Total Standard Deviation in ln(k): 13.615351929384866
""",
)

entry(
    index = 8,
    label = "Root_1R!H-inRing_N-4R->N_2R!H->O",
    kinetics = ArrheniusBM(A=(3.40031e+71,'s^-1'), n=-16.7831, w0=(726125,'J/mol'), E0=(408378,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.8901812474716291, var=376.0091735555458, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_2R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O
    Total Standard Deviation in ln(k): 41.1103659239092"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O
Total Standard Deviation in ln(k): 41.1103659239092""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O
Total Standard Deviation in ln(k): 41.1103659239092
""",
)

entry(
    index = 9,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O",
    kinetics = ArrheniusBM(A=(863.216,'s^-1'), n=3.33558, w0=(677591,'J/mol'), E0=(334456,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08380078001030873, var=94.54296239857095, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O',), comment="""BM rule fitted to 11 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O
    Total Standard Deviation in ln(k): 19.703236486659"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O
Total Standard Deviation in ln(k): 19.703236486659""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O
Total Standard Deviation in ln(k): 19.703236486659
""",
)

entry(
    index = 10,
    label = "Root_N-1R!H-inRing_2R!H->C_4R->C",
    kinetics = ArrheniusBM(A=(0.00257114,'s^-1'), n=4.34785, w0=(700500,'J/mol'), E0=(369438,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->C_4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->C_4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_N-1R!H-inRing_2R!H->C_N-4R->C",
    kinetics = ArrheniusBM(A=(256.099,'s^-1'), n=3.36485, w0=(783500,'J/mol'), E0=(223926,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.005508982678508988, var=4.333596933699633, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->C_N-4R->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_2R!H->C_N-4R->C
    Total Standard Deviation in ln(k): 4.187157440959891"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_2R!H->C_N-4R->C
Total Standard Deviation in ln(k): 4.187157440959891""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_2R!H->C_N-4R->C
Total Standard Deviation in ln(k): 4.187157440959891
""",
)

entry(
    index = 12,
    label = "Root_N-1R!H-inRing_N-2R!H->C_3R!H->C",
    kinetics = ArrheniusBM(A=(0.0954007,'s^-1'), n=3.97882, w0=(762750,'J/mol'), E0=(250868,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05104117971660031, var=160.05464641490252, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_3R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_3R!H->C
    Total Standard Deviation in ln(k): 25.490690006267023"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_3R!H->C
Total Standard Deviation in ln(k): 25.490690006267023""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_3R!H->C
Total Standard Deviation in ln(k): 25.490690006267023
""",
)

entry(
    index = 13,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C",
    kinetics = ArrheniusBM(A=(1.19221e-62,'s^-1'), n=22.2718, w0=(748344,'J/mol'), E0=(-21081.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9949489040724094, var=31.03257203316843, Tref=1000.0, N=48, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C',), comment="""BM rule fitted to 48 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C
    Total Standard Deviation in ln(k): 13.66762655979622"""),
    rank = 11,
    shortDesc = """BM rule fitted to 48 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C
Total Standard Deviation in ln(k): 13.66762655979622""",
    longDesc = 
"""
BM rule fitted to 48 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C
Total Standard Deviation in ln(k): 13.66762655979622
""",
)

entry(
    index = 14,
    label = "Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing",
    kinetics = ArrheniusBM(A=(2.70002e+39,'s^-1'), n=-7.1515, w0=(732500,'J/mol'), E0=(288782,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24763149641243207, var=87.79679561687634, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing
    Total Standard Deviation in ln(k): 19.40654619814221"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing
Total Standard Deviation in ln(k): 19.40654619814221""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing
Total Standard Deviation in ln(k): 19.40654619814221
""",
)

entry(
    index = 15,
    label = "Root_1R!H-inRing_N-4R->N_2R!H->O_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(2.1761e+10,'s^-1'), n=0.996245, w0=(707000,'J/mol'), E0=(405481,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_2R!H->O_N-3R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_N-3R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_N-3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_N-3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R",
    kinetics = ArrheniusBM(A=(6.42898e-133,'s^-1'), n=43.0224, w0=(700214,'J/mol'), E0=(42887.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.3589376793601295, var=69.21003957276957, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R
    Total Standard Deviation in ln(k): 22.604885725751753"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R
Total Standard Deviation in ln(k): 22.604885725751753""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R
Total Standard Deviation in ln(k): 22.604885725751753
""",
)

entry(
    index = 17,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C",
    kinetics = ArrheniusBM(A=(3.18179e+39,'s^-1'), n=-7.17225, w0=(645667,'J/mol'), E0=(415609,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.42262730356938655, var=78.72060767182978, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C
    Total Standard Deviation in ln(k): 18.84881634829919"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C
Total Standard Deviation in ln(k): 18.84881634829919""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C
Total Standard Deviation in ln(k): 18.84881634829919
""",
)

entry(
    index = 18,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(6.1544e+10,'s^-1'), n=1.34775, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_N-1R!H-inRing_2R!H->C_N-4R->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(28.6641,'s^-1'), n=3.55793, w0=(783500,'J/mol'), E0=(211066,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->C_N-4R->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->C_N-4R->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->C_N-4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->C_N-4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_4R->C",
    kinetics = ArrheniusBM(A=(7040,'s^-1'), n=2.66, w0=(700500,'J/mol'), E0=(384026,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_N-4R->C",
    kinetics = ArrheniusBM(A=(635.413,'s^-1'), n=2.83859, w0=(783500,'J/mol'), E0=(219488,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0012207818220425905, var=12.527101437509526, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_N-4R->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_N-4R->C
    Total Standard Deviation in ln(k): 7.098555561663242"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_N-4R->C
Total Standard Deviation in ln(k): 7.098555561663242""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_N-4R->C
Total Standard Deviation in ln(k): 7.098555561663242
""",
)

entry(
    index = 22,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N",
    kinetics = ArrheniusBM(A=(3.76721e-56,'s^-1'), n=20.4354, w0=(727519,'J/mol'), E0=(-33116.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.8731427039737816, var=23.68673873026742, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N',), comment="""BM rule fitted to 26 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N
    Total Standard Deviation in ln(k): 19.488364241519903"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N
Total Standard Deviation in ln(k): 19.488364241519903""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N
Total Standard Deviation in ln(k): 19.488364241519903
""",
)

entry(
    index = 23,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N",
    kinetics = ArrheniusBM(A=(1.90425e-05,'s^-1'), n=5.18692, w0=(772955,'J/mol'), E0=(109729,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.013830948589540256, var=7.224049258643255, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N',), comment="""BM rule fitted to 22 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N
    Total Standard Deviation in ln(k): 5.422996178518286"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N
Total Standard Deviation in ln(k): 5.422996178518286""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N
Total Standard Deviation in ln(k): 5.422996178518286
""",
)

entry(
    index = 24,
    label = "Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.32322e+24,'s^-1'), n=-2.81453, w0=(745250,'J/mol'), E0=(282167,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.4915944114598476, var=57.075019008093854, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 21.40566214731623"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_5R!H->C
Total Standard Deviation in ln(k): 21.40566214731623""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_5R!H->C
Total Standard Deviation in ln(k): 21.40566214731623
""",
)

entry(
    index = 25,
    label = "Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.23584e+11,'s^-1'), n=1.27308, w0=(707000,'J/mol'), E0=(183610,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN",
    kinetics = ArrheniusBM(A=(3.35262e-129,'s^-1'), n=41.9454, w0=(700917,'J/mol'), E0=(51012.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.36255197685948554, var=131.25054790841853, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN
    Total Standard Deviation in ln(k): 23.8781081550003"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN
Total Standard Deviation in ln(k): 23.8781081550003""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN
Total Standard Deviation in ln(k): 23.8781081550003
""",
)

entry(
    index = 27,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_N-Sp-5R!H-2CN",
    kinetics = ArrheniusBM(A=(8.16507e-20,'s^-1'), n=9.4016, w0=(696000,'J/mol'), E0=(345895,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_N-Sp-5R!H-2CN',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_N-Sp-5R!H-2CN
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_N-Sp-5R!H-2CN
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_N-Sp-5R!H-2CN
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.15835e+39,'s^-1'), n=-7.08112, w0=(661000,'J/mol'), E0=(428856,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.10039660117628249, var=202.96872295848286, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 28.81313043246121"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 28.81313043246121""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 28.81313043246121
""",
)

entry(
    index = 29,
    label = "Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_N-4R->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(205000,'s^-1'), n=2.37, w0=(783500,'J/mol'), E0=(221387,'J/mol'), Tmin=(600,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_N-4R->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_N-4R->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_N-4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_3R!H->C_N-4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_4R->N",
    kinetics = ArrheniusBM(A=(3.81632e+14,'s^-1'), n=-0.222789, w0=(559500,'J/mol'), E0=(147442,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_4R->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_4R->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_4R->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_4R->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N",
    kinetics = ArrheniusBM(A=(1.64685e-57,'s^-1'), n=20.836, w0=(734240,'J/mol'), E0=(-47104.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.7709993395862518, var=15.19742260456597, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N',), comment="""BM rule fitted to 25 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N
    Total Standard Deviation in ln(k): 17.29010623737784"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N
Total Standard Deviation in ln(k): 17.29010623737784""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N
Total Standard Deviation in ln(k): 17.29010623737784
""",
)

entry(
    index = 32,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S",
    kinetics = ArrheniusBM(A=(2628.85,'s^-1'), n=2.78353, w0=(782000,'J/mol'), E0=(89057.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004857179637508415, var=0.25064116944332687, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S
    Total Standard Deviation in ln(k): 1.0158560594211685"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S
Total Standard Deviation in ln(k): 1.0158560594211685""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S
Total Standard Deviation in ln(k): 1.0158560594211685
""",
)

entry(
    index = 33,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S",
    kinetics = ArrheniusBM(A=(0.000221028,'s^-1'), n=4.87215, w0=(771526,'J/mol'), E0=(113206,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0013507450818510233, var=6.7138360241038875, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S
    Total Standard Deviation in ln(k): 5.19787713242361"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S
Total Standard Deviation in ln(k): 5.19787713242361""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S
Total Standard Deviation in ln(k): 5.19787713242361
""",
)

entry(
    index = 34,
    label = "Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_5R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(6.5268e+11,'s^-1'), n=0.396329, w0=(783500,'J/mol'), E0=(259654,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_5R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_5R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_2R!H->O_3R!H-inRing_Ext-3R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_3R!H->C",
    kinetics = ArrheniusBM(A=(7.49767e+07,'s^-1'), n=1.48437, w0=(667000,'J/mol'), E0=(433271,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.470728631562516e-15, var=0.07135570365739116, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_3R!H->C
    Total Standard Deviation in ln(k): 0.5355146250198273"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_3R!H->C
Total Standard Deviation in ln(k): 0.5355146250198273""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_3R!H->C
Total Standard Deviation in ln(k): 0.5355146250198273
""",
)

entry(
    index = 36,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C",
    kinetics = ArrheniusBM(A=(3.70867e-134,'s^-1'), n=43.4476, w0=(717875,'J/mol'), E0=(-5808.39,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.620428518091382, var=89.65743457902248, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C
    Total Standard Deviation in ln(k): 25.56634853630231"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C
Total Standard Deviation in ln(k): 25.56634853630231""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C
Total Standard Deviation in ln(k): 25.56634853630231
""",
)

entry(
    index = 37,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R_3R!H->O",
    kinetics = ArrheniusBM(A=(1.37586e+09,'s^-1'), n=1.6158, w0=(707000,'J/mol'), E0=(400010,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R_3R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R_3R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R_3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R_3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R_N-3R!H->O",
    kinetics = ArrheniusBM(A=(1.04679e+11,'s^-1'), n=1.26667, w0=(615000,'J/mol'), E0=(331277,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R_N-3R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R_N-3R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R_N-3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-4CH-R_5R!H->C_Ext-1R!H-R_N-3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C",
    kinetics = ArrheniusBM(A=(8.63142e-63,'s^-1'), n=22.5022, w0=(679400,'J/mol'), E0=(-40826.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2635762441282121, var=50.24514974463436, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C
    Total Standard Deviation in ln(k): 14.87257854479527"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C
Total Standard Deviation in ln(k): 14.87257854479527""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C
Total Standard Deviation in ln(k): 14.87257854479527
""",
)

entry(
    index = 40,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C",
    kinetics = ArrheniusBM(A=(4.13471e-05,'s^-1'), n=5.26861, w0=(770800,'J/mol'), E0=(119544,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12046792272150078, var=8.981422953803811, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C',), comment="""BM rule fitted to 15 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C
    Total Standard Deviation in ln(k): 6.310678239436273"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C
Total Standard Deviation in ln(k): 6.310678239436273""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C
Total Standard Deviation in ln(k): 6.310678239436273
""",
)

entry(
    index = 41,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(4909.53,'s^-1'), n=2.71698, w0=(782000,'J/mol'), E0=(88826.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1408662726283667e-06, var=3.5438674360202764e-06, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.003776812860711284"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.003776812860711284""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.003776812860711284
""",
)

entry(
    index = 42,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O",
    kinetics = ArrheniusBM(A=(0.00132983,'s^-1'), n=4.6492, w0=(769562,'J/mol'), E0=(116133,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.011878464585718973, var=6.628325949021129, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O
    Total Standard Deviation in ln(k): 5.1911431859520585"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O
Total Standard Deviation in ln(k): 5.1911431859520585""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O
Total Standard Deviation in ln(k): 5.1911431859520585
""",
)

entry(
    index = 43,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O",
    kinetics = ArrheniusBM(A=(1.85399,'s^-1'), n=3.49715, w0=(782000,'J/mol'), E0=(83909.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.004050044991505004, var=0.10935763999388207, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O
    Total Standard Deviation in ln(k): 0.6731271817713865"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O
Total Standard Deviation in ln(k): 0.6731271817713865""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O
Total Standard Deviation in ln(k): 0.6731271817713865
""",
)

entry(
    index = 44,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_3R!H->C_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.885e+08,'s^-1'), n=1.289, w0=(667000,'J/mol'), E0=(434967,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_3R!H->C_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_3R!H->C_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_3R!H->C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_3R!H->C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_2CN->C",
    kinetics = ArrheniusBM(A=(3.62e+09,'s^-1'), n=0.863, w0=(783500,'J/mol'), E0=(255551,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_2CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_2CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_2CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_2CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C",
    kinetics = ArrheniusBM(A=(1.11641e-135,'s^-1'), n=43.925, w0=(696000,'J/mol'), E0=(-144.585,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.08213559833397, var=88.30888828234897, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C
    Total Standard Deviation in ln(k): 26.583117941329068"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C
Total Standard Deviation in ln(k): 26.583117941329068""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C
Total Standard Deviation in ln(k): 26.583117941329068
""",
)

entry(
    index = 47,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O",
    kinetics = ArrheniusBM(A=(8.23714e+08,'s^-1'), n=1.51542, w0=(707000,'J/mol'), E0=(132752,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.014265471420943657, var=4.066288247412202, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O
    Total Standard Deviation in ln(k): 4.078399128613921"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O
Total Standard Deviation in ln(k): 4.078399128613921""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O
Total Standard Deviation in ln(k): 4.078399128613921
""",
)

entry(
    index = 48,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(2.2591e-07,'s^-1'), n=6.06556, w0=(661000,'J/mol'), E0=(221850,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8641639367273353, var=85.7131359414688, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O
    Total Standard Deviation in ln(k): 20.731381982288035"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O
Total Standard Deviation in ln(k): 20.731381982288035""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O
Total Standard Deviation in ln(k): 20.731381982288035
""",
)

entry(
    index = 49,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R",
    kinetics = ArrheniusBM(A=(25.6378,'s^-1'), n=3.66551, w0=(764000,'J/mol'), E0=(129088,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.15106182521201603, var=19.940213171909487, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R
    Total Standard Deviation in ln(k): 9.331589722744125"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R
Total Standard Deviation in ln(k): 9.331589722744125""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R
Total Standard Deviation in ln(k): 9.331589722744125
""",
)

entry(
    index = 50,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.10704e-11,'s^-1'), n=7.19062, w0=(798000,'J/mol'), E0=(103605,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.026122774708554834, var=1.7134819836096122, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 2.6898340818415187"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.6898340818415187""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.6898340818415187
""",
)

entry(
    index = 51,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-3NOS-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5.0652e-17,'s^-1'), n=8.61669, w0=(696000,'J/mol'), E0=(114142,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-3NOS-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-3NOS-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-3NOS-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-3NOS-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S_Ext-1R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(87.5,'s^-1'), n=3.23, w0=(782000,'J/mol'), E0=(84839.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S_Ext-1R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S_Ext-1R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_3NOS->S_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 53,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(0.000164309,'s^-1'), n=4.97161, w0=(787889,'J/mol'), E0=(112114,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.051526042577798054, var=4.08971979394378, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 4.183649319777569"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 4.183649319777569""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 4.183649319777569
""",
)

entry(
    index = 54,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R",
    kinetics = ArrheniusBM(A=(4.74194e-14,'s^-1'), n=7.69802, w0=(798000,'J/mol'), E0=(92033.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.012749512289493472, var=0.8377613591004845, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R
    Total Standard Deviation in ln(k): 1.8669540248408663"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R
Total Standard Deviation in ln(k): 1.8669540248408663""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R
Total Standard Deviation in ln(k): 1.8669540248408663
""",
)

entry(
    index = 55,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_5R!H->O",
    kinetics = ArrheniusBM(A=(1.50087e+11,'s^-1'), n=0.45162, w0=(707000,'J/mol'), E0=(137659,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008012511677798886, var=3.4768369970791304, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_5R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_5R!H->O
    Total Standard Deviation in ln(k): 3.7582167842883063"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_5R!H->O
Total Standard Deviation in ln(k): 3.7582167842883063""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_5R!H->O
Total Standard Deviation in ln(k): 3.7582167842883063
""",
)

entry(
    index = 56,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(4.85602e+09,'s^-1'), n=0.739985, w0=(707000,'J/mol'), E0=(193742,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.82438,'s^-1'), n=3.5005, w0=(782000,'J/mol'), E0=(83092.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.0095089610383627e-06, var=0.12475859351858236, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.7081011849094191"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.7081011849094191""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.7081011849094191
""",
)

entry(
    index = 58,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(3.13351e+10,'s^-1'), n=1.04551, w0=(696000,'J/mol'), E0=(308088,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.30649e-17,'s^-1'), n=8.88181, w0=(696000,'J/mol'), E0=(351768,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->N_N-2R!H->O_Ext-2CN-R_Sp-5R!H-2CN_N-3R!H->C_N-2CN->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O_Ext-4C-R",
    kinetics = ArrheniusBM(A=(7.46723e+09,'s^-1'), n=1.26362, w0=(707000,'J/mol'), E0=(155669,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(7.10378e+09,'s^-1'), n=1.08011, w0=(707000,'J/mol'), E0=(118314,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_5R!H->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing",
    kinetics = ArrheniusBM(A=(1.31843e+16,'s^-1'), n=-0.594645, w0=(651800,'J/mol'), E0=(283810,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06834214918355454, var=83.03772135212918, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing
    Total Standard Deviation in ln(k): 18.439869496605795"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing
Total Standard Deviation in ln(k): 18.439869496605795""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing
Total Standard Deviation in ln(k): 18.439869496605795
""",
)

entry(
    index = 63,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_N-2N-inRing",
    kinetics = ArrheniusBM(A=(6.3785e+07,'s^-1'), n=1.39836, w0=(707000,'J/mol'), E0=(187989,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_N-2N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_N-2N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_N-2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_N-2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3.08866e+12,'s^-1'), n=0.904623, w0=(798000,'J/mol'), E0=(128315,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.8372e-11,'s^-1'), n=7.16536, w0=(747000,'J/mol'), E0=(112893,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008977972048432677, var=25.44819571736246, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 10.135685333227709"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 10.135685333227709""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 10.135685333227709
""",
)

entry(
    index = 66,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O",
    kinetics = ArrheniusBM(A=(2.61055e-12,'s^-1'), n=7.38016, w0=(798000,'J/mol'), E0=(97626.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.012281183960210522, var=4.719030378538201, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O
    Total Standard Deviation in ln(k): 4.385809279805604"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O
Total Standard Deviation in ln(k): 4.385809279805604""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O
Total Standard Deviation in ln(k): 4.385809279805604
""",
)

entry(
    index = 67,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_N-3NOS->O",
    kinetics = ArrheniusBM(A=(5.99955e-18,'s^-1'), n=8.92667, w0=(696000,'J/mol'), E0=(104007,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_N-3NOS->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_N-3NOS->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_N-3NOS->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_N-3NOS->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.83426e-12,'s^-1'), n=7.39498, w0=(798000,'J/mol'), E0=(101379,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01931713628791539, var=2.0216086590715365, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 2.89893371093887"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.89893371093887""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.89893371093887
""",
)

entry(
    index = 69,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_Ext-3NO-R",
    kinetics = ArrheniusBM(A=(8.00067e+12,'s^-1'), n=0.391729, w0=(798000,'J/mol'), E0=(133048,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_Ext-3NO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_Ext-3NO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_Ext-3NO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_Ext-3NO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N",
    kinetics = ArrheniusBM(A=(6.91728e-07,'s^-1'), n=5.62342, w0=(779800,'J/mol'), E0=(106545,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006515153720890275, var=0.8806591803136841, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N
    Total Standard Deviation in ln(k): 1.897682153588295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N
Total Standard Deviation in ln(k): 1.897682153588295""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N
Total Standard Deviation in ln(k): 1.897682153588295
""",
)

entry(
    index = 71,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N",
    kinetics = ArrheniusBM(A=(8.46061e-15,'s^-1'), n=7.98481, w0=(798000,'J/mol'), E0=(96853.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00263383782615601, var=0.4396759609029318, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N
    Total Standard Deviation in ln(k): 1.335918740070374"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N
Total Standard Deviation in ln(k): 1.335918740070374""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N
Total Standard Deviation in ln(k): 1.335918740070374
""",
)

entry(
    index = 72,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.20077e-11,'s^-1'), n=7.05311, w0=(798000,'J/mol'), E0=(100604,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_6R!H->N",
    kinetics = ArrheniusBM(A=(7.35011e-13,'s^-1'), n=7.36802, w0=(798000,'J/mol'), E0=(90879,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_N-6R!H->N",
    kinetics = ArrheniusBM(A=(1.29627e-12,'s^-1'), n=7.28519, w0=(798000,'J/mol'), E0=(101095,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_N-6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_N-6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-3NO-R_Ext-5R!H-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_5R!H->O_Ext-4R-R",
    kinetics = ArrheniusBM(A=(1.88124e+11,'s^-1'), n=0.620515, w0=(707000,'J/mol'), E0=(161496,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_5R!H->O_Ext-4R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_5R!H->O_Ext-4R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_5R!H->O_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-4R-R_5R!H->O_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 76,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O_Ext-1R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(181.401,'s^-1'), n=2.92819, w0=(782000,'J/mol'), E0=(87394.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O_Ext-1R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O_Ext-1R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_N-2OS->O_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 77,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O",
    kinetics = ArrheniusBM(A=(1.07004e+24,'s^-1'), n=-2.80801, w0=(707000,'J/mol'), E0=(245324,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06960442888511502, var=70.04500144656065, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O
    Total Standard Deviation in ln(k): 16.95309309986816"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O
Total Standard Deviation in ln(k): 16.95309309986816""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O
Total Standard Deviation in ln(k): 16.95309309986816
""",
)

entry(
    index = 78,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O",
    kinetics = ArrheniusBM(A=(5.30991e+18,'s^-1'), n=-1.44644, w0=(615000,'J/mol'), E0=(326412,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.10690871308720216, var=25.722674424570492, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O
    Total Standard Deviation in ln(k): 10.436135195906743"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O
Total Standard Deviation in ln(k): 10.436135195906743""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O
Total Standard Deviation in ln(k): 10.436135195906743
""",
)

entry(
    index = 79,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R_3NOS->O",
    kinetics = ArrheniusBM(A=(1.80649e-12,'s^-1'), n=7.52975, w0=(798000,'J/mol'), E0=(96352.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R_3NOS->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R_3NOS->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R_3NOS->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R_3NOS->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R_N-3NOS->O",
    kinetics = ArrheniusBM(A=(3.03331e-17,'s^-1'), n=8.87366, w0=(696000,'J/mol'), E0=(111857,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R_N-3NOS->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R_N-3NOS->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R_N-3NOS->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_Ext-5R!H-R_Ext-5R!H-R_N-3NOS->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 81,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O_Ext-5R!H-R_6R!H->N",
    kinetics = ArrheniusBM(A=(3.31385e-15,'s^-1'), n=8.01833, w0=(798000,'J/mol'), E0=(85225.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O_Ext-5R!H-R_6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O_Ext-5R!H-R_6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O_Ext-5R!H-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O_Ext-5R!H-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O_Ext-5R!H-R_N-6R!H->N",
    kinetics = ArrheniusBM(A=(9.90794e-14,'s^-1'), n=7.92259, w0=(798000,'J/mol'), E0=(95420.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O_Ext-5R!H-R_N-6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O_Ext-5R!H-R_N-6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O_Ext-5R!H-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-2N-R_3NOS->O_Ext-5R!H-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 83,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(2.63375e-12,'s^-1'), n=7.38822, w0=(798000,'J/mol'), E0=(100901,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01164948583439061, var=1.058298597701629, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 2.091614027963185"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 2.091614027963185""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 2.091614027963185
""",
)

entry(
    index = 84,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(8.72733e-17,'s^-1'), n=8.43216, w0=(798000,'J/mol'), E0=(93995.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 85,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_4R->C",
    kinetics = ArrheniusBM(A=(1.93892e+11,'s^-1'), n=0.308436, w0=(707000,'J/mol'), E0=(125262,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C",
    kinetics = ArrheniusBM(A=(7.72033e-12,'s^-1'), n=7.13865, w0=(798000,'J/mol'), E0=(101332,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0009406278385854534, var=0.10603351746797161, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C
    Total Standard Deviation in ln(k): 0.6551610235432553"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C
Total Standard Deviation in ln(k): 0.6551610235432553""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C
Total Standard Deviation in ln(k): 0.6551610235432553
""",
)

entry(
    index = 87,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_Ext-5CO-R_Ext-5CO-R",
    kinetics = ArrheniusBM(A=(2.24517e-15,'s^-1'), n=8.2595, w0=(798000,'J/mol'), E0=(97485.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_Ext-5CO-R_Ext-5CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_Ext-5CO-R_Ext-5CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_Ext-5CO-R_Ext-5CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_Ext-5CO-R_Ext-5CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 88,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_5CO->O",
    kinetics = ArrheniusBM(A=(3.21561e-15,'s^-1'), n=8.08717, w0=(798000,'J/mol'), E0=(97688.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_5CO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_5CO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_5CO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_5CO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_N-5CO->O",
    kinetics = ArrheniusBM(A=(7.48602e-15,'s^-1'), n=8.00071, w0=(798000,'J/mol'), E0=(97935.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_N-5CO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_N-5CO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_N-5CO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_N-5R!H->N_N-5CO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O_5BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(9.16767e+14,'s^-1'), n=-0.000952816, w0=(707000,'J/mol'), E0=(259509,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O_5BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O_5BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O_5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O_5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O_N-5BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(3.03918e+16,'s^-1'), n=-0.601612, w0=(707000,'J/mol'), E0=(201180,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O_N-5BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O_N-5BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O_N-5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_3NOS->O_N-5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 92,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_5BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(9.05172e+10,'s^-1'), n=0.89767, w0=(615000,'J/mol'), E0=(329307,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0565073687571566e-14, var=1.80566058771988, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_5BrCClFINPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_5BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 2.6938601682420895"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 2.6938601682420895""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 2.6938601682420895
""",
)

entry(
    index = 93,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_N-5BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(8.78669e+12,'s^-1'), n=0.204119, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_N-5BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_N-5BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_N-5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_N-5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 94,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.69578e-13,'s^-1'), n=7.6981, w0=(798000,'J/mol'), E0=(101157,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.006581694381035067, var=2.055466972897255, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 2.890705523459266"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.890705523459266""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.890705523459266
""",
)

entry(
    index = 95,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N",
    kinetics = ArrheniusBM(A=(1.65175e-13,'s^-1'), n=7.74458, w0=(798000,'J/mol'), E0=(97939.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.002146257399877121, var=0.23553441622036883, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N
    Total Standard Deviation in ln(k): 0.9783283909230072"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N
Total Standard Deviation in ln(k): 0.9783283909230072""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N
Total Standard Deviation in ln(k): 0.9783283909230072
""",
)

entry(
    index = 96,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-7R!H->N",
    kinetics = ArrheniusBM(A=(1.797e-10,'s^-1'), n=6.92374, w0=(798000,'J/mol'), E0=(99729.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-7R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-7R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 97,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R",
    kinetics = ArrheniusBM(A=(2.19963e-11,'s^-1'), n=6.98648, w0=(798000,'J/mol'), E0=(100797,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006099207969903697, var=0.16754745053310063, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R
    Total Standard Deviation in ln(k): 0.8359140406399651"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R
Total Standard Deviation in ln(k): 0.8359140406399651""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R
Total Standard Deviation in ln(k): 0.8359140406399651
""",
)

entry(
    index = 98,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_5BrCClFINPSSi->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3.54394e+12,'s^-1'), n=0.452411, w0=(615000,'J/mol'), E0=(338565,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_5BrCClFINPSSi->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_5BrCClFINPSSi->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_5BrCClFINPSSi->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_4CH->C_Ext-4C-R_N-5R!H->O_2N-inRing_N-3NOS->O_5BrCClFINPSSi->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 99,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.835e-16,'s^-1'), n=8.51386, w0=(798000,'J/mol'), E0=(95477.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 100,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.77636e-11,'s^-1'), n=7.04941, w0=(798000,'J/mol'), E0=(104855,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 101,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N_5R!H->O",
    kinetics = ArrheniusBM(A=(2.33438e-16,'s^-1'), n=8.59067, w0=(798000,'J/mol'), E0=(93265.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 102,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N_N-5R!H->O",
    kinetics = ArrheniusBM(A=(1.28848e-11,'s^-1'), n=7.11818, w0=(798000,'J/mol'), E0=(96726.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_2NOS->N_N-4R->N_N-4CH->C_Ext-1R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_7R!H->N_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 103,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_7R!H->N",
    kinetics = ArrheniusBM(A=(9.61654e-11,'s^-1'), n=6.78703, w0=(798000,'J/mol'), E0=(99834.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_7R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_7R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 104,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N",
    kinetics = ArrheniusBM(A=(1.1358e-11,'s^-1'), n=7.08342, w0=(798000,'J/mol'), E0=(101820,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.774397504036697e-05, var=0.31280538790524537, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N
    Total Standard Deviation in ln(k): 1.1213232657408565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N
Total Standard Deviation in ln(k): 1.1213232657408565""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N
Total Standard Deviation in ln(k): 1.1213232657408565
""",
)

entry(
    index = 105,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing",
    kinetics = ArrheniusBM(A=(4.38421e-12,'s^-1'), n=7.22006, w0=(798000,'J/mol'), E0=(103463,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 106,
    label = "Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing",
    kinetics = ArrheniusBM(A=(7.07407e-11,'s^-1'), n=6.82872, w0=(798000,'J/mol'), E0=(100753,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C_N-3R!H->C_N-2NOS->N_N-3NOS->S_2OS->O_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

