#!/usr/bin/env python
# encoding: utf-8

name = "Cyclic_Ether_Formation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(8.03971e-25,'s^-1'), n=10.5218, w0=(250000,'J/mol'), E0=(-11538.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7104365344549564, var=5.4172929922627295, Tref=1000.0, N=37, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 37 training reactions at node Root
    Total Standard Deviation in ln(k): 8.96361594843062"""),
    rank = 11,
    shortDesc = """BM rule fitted to 37 training reactions at node Root
Total Standard Deviation in ln(k): 8.96361594843062""",
    longDesc = 
"""
BM rule fitted to 37 training reactions at node Root
Total Standard Deviation in ln(k): 8.96361594843062
""",
)

entry(
    index = 2,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s",
    kinetics = ArrheniusBM(A=(7.23851e-31,'s^-1'), n=12.5811, w0=(250000,'J/mol'), E0=(-24907.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.6407791386250645, var=3.3734172622859875, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s',), comment="""BM rule fitted to 13 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s
    Total Standard Deviation in ln(k): 12.829756110488058"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s
Total Standard Deviation in ln(k): 12.829756110488058""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s
Total Standard Deviation in ln(k): 12.829756110488058
""",
)

entry(
    index = 3,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O",
    kinetics = ArrheniusBM(A=(4.22191e-28,'s^-1'), n=11.2153, w0=(250000,'J/mol'), E0=(5349.83,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5632841452923574, var=1.3743717133941338, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O
    Total Standard Deviation in ln(k): 3.765509913015097"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O
Total Standard Deviation in ln(k): 3.765509913015097""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O
Total Standard Deviation in ln(k): 3.765509913015097
""",
)

entry(
    index = 4,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(8.13137e-20,'s^-1'), n=8.89064, w0=(250000,'J/mol'), E0=(37205,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5025198211949359, var=1.4549572842228722, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O',), comment="""BM rule fitted to 18 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O
    Total Standard Deviation in ln(k): 3.6807563462481987"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O
Total Standard Deviation in ln(k): 3.6807563462481987""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O
Total Standard Deviation in ln(k): 3.6807563462481987
""",
)

entry(
    index = 5,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0",
    kinetics = ArrheniusBM(A=(7.69879e-31,'s^-1'), n=12.5699, w0=(250000,'J/mol'), E0=(-24202.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.7292815557725647, var=2.6655608973088807, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0',), comment="""BM rule fitted to 11 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0
    Total Standard Deviation in ln(k): 12.64309401673515"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0
Total Standard Deviation in ln(k): 12.64309401673515""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0
Total Standard Deviation in ln(k): 12.64309401673515
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
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-2O2sS-R",
    kinetics = ArrheniusBM(A=(4.76338e-29,'s^-1'), n=11.5319, w0=(250000,'J/mol'), E0=(-8148.23,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.7678357328038395, var=15.148652715130089, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-2O2sS-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-2O2sS-R
    Total Standard Deviation in ln(k): 9.73191906586784"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-2O2sS-R
Total Standard Deviation in ln(k): 9.73191906586784""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-2O2sS-R
Total Standard Deviation in ln(k): 9.73191906586784
""",
)

entry(
    index = 8,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-4R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.43755e-31,'s^-1'), n=12.3015, w0=(250000,'J/mol'), E0=(14387.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.61072390931423, var=17.87006595282664, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-4R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-4R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 22.571913004394496"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-4R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 22.571913004394496""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-4R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 22.571913004394496
""",
)

entry(
    index = 9,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H",
    kinetics = ArrheniusBM(A=(9.06947e-30,'s^-1'), n=11.9742, w0=(250000,'J/mol'), E0=(-4623.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6591030671823406, var=1.4299670688224613, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H
    Total Standard Deviation in ln(k): 4.053324731082797"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H
Total Standard Deviation in ln(k): 4.053324731082797""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H
Total Standard Deviation in ln(k): 4.053324731082797
""",
)

entry(
    index = 10,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H",
    kinetics = ArrheniusBM(A=(6.65727e-17,'s^-1'), n=7.8974, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.432215115943695, var=0.3150737508117761, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H
    Total Standard Deviation in ln(k): 2.2112541079154506"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H
Total Standard Deviation in ln(k): 2.2112541079154506""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H
Total Standard Deviation in ln(k): 2.2112541079154506
""",
)

entry(
    index = 11,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-2O2sS-R",
    kinetics = ArrheniusBM(A=(1.17e+09,'s^-1'), n=0, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-2O2sS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-2O2sS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-2O2sS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-2O2sS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.03021e-28,'s^-1'), n=11.8932, w0=(250000,'J/mol'), E0=(-12680.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7920050203632223, var=3.099236587853365, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R
    Total Standard Deviation in ln(k): 8.031790870911895"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R
Total Standard Deviation in ln(k): 8.031790870911895""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R
Total Standard Deviation in ln(k): 8.031790870911895
""",
)

entry(
    index = 13,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.39316e-24,'s^-1'), n=10.708, w0=(250000,'J/mol'), E0=(-34475.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.5994182062711602, var=14.800697117773407, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 11.731190174352808"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.731190174352808""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.731190174352808
""",
)

entry(
    index = 14,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(2.4664e+21,'s^-1'), n=-2.36645, w0=(250000,'J/mol'), E0=(99832.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0813976698235791, var=12.034380911417225, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 7.159064074175162"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 7.159064074175162""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 7.159064074175162
""",
)

entry(
    index = 15,
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
    index = 16,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-2O2sS-R_Ext-4R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.97983e-31,'s^-1'), n=12.117, w0=(250000,'J/mol'), E0=(-296.321,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05159657178977463, var=18.021703513970937, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-2O2sS-R_Ext-4R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-2O2sS-R_Ext-4R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 8.640136367720634"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-2O2sS-R_Ext-4R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 8.640136367720634""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-2O2sS-R_Ext-4R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 8.640136367720634
""",
)

entry(
    index = 17,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-4R!H-R_Ext-3R!H-R_Int-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(1.27e+08,'s^-1'), n=0.77, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-4R!H-R_Ext-3R!H-R_Int-7R!H-6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-4R!H-R_Ext-3R!H-R_Int-7R!H-6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-4R!H-R_Ext-3R!H-R_Int-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-4R!H-R_Ext-3R!H-R_Int-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-2O2sS-R",
    kinetics = ArrheniusBM(A=(9.27152e+10,'s^-1'), n=0.133324, w0=(250000,'J/mol'), E0=(121007,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0037339776687244828, var=0.5321622773559461, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-2O2sS-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-2O2sS-R
    Total Standard Deviation in ln(k): 1.4718251375665967"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-2O2sS-R
Total Standard Deviation in ln(k): 1.4718251375665967""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-2O2sS-R
Total Standard Deviation in ln(k): 1.4718251375665967
""",
)

entry(
    index = 19,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.79088e+12,'s^-1'), n=-0.245121, w0=(250000,'J/mol'), E0=(102930,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00047906195141407315, var=0.12280473020872217, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 0.7037331273192441"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 0.7037331273192441""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 0.7037331273192441
""",
)

entry(
    index = 20,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.32175e-15,'s^-1'), n=7.42132, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4097690300683688, var=0.10555409043770493, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-3R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.6808905909171852"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.6808905909171852""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.6808905909171852
""",
)

entry(
    index = 21,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-2O2sS-R",
    kinetics = ArrheniusBM(A=(6.81699e-20,'s^-1'), n=8.82014, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.732247689467373, var=0.13880440424672924, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-2O2sS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-2O2sS-R
    Total Standard Deviation in ln(k): 15.14952576989008"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-2O2sS-R
Total Standard Deviation in ln(k): 15.14952576989008""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-2O2sS-R
Total Standard Deviation in ln(k): 15.14952576989008
""",
)

entry(
    index = 22,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-2O2sS-R",
    kinetics = ArrheniusBM(A=(9.18271e+13,'s^-1'), n=-0.47522, w0=(250000,'J/mol'), E0=(89629.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0018908511124089997, var=0.2580170495707488, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-2O2sS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-2O2sS-R
    Total Standard Deviation in ln(k): 1.023063656376468"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-2O2sS-R
Total Standard Deviation in ln(k): 1.023063656376468""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-2O2sS-R
Total Standard Deviation in ln(k): 1.023063656376468
""",
)

entry(
    index = 23,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.09e+12,'s^-1'), n=0, w0=(250000,'J/mol'), E0=(59528,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_5R!H->C_Ext-2O2sS-R",
    kinetics = ArrheniusBM(A=(2.0043e+13,'s^-1'), n=-0.238411, w0=(250000,'J/mol'), E0=(83399.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.945373279193557, var=55.570159453833924, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_5R!H->C_Ext-2O2sS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_5R!H->C_Ext-2O2sS-R
    Total Standard Deviation in ln(k): 27.369937864374403"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_5R!H->C_Ext-2O2sS-R
Total Standard Deviation in ln(k): 27.369937864374403""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_5R!H->C_Ext-2O2sS-R
Total Standard Deviation in ln(k): 27.369937864374403
""",
)

entry(
    index = 25,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-5R!H->C_Ext-2O2sS-R",
    kinetics = ArrheniusBM(A=(6.92e+15,'s^-1'), n=-0.53, w0=(250000,'J/mol'), E0=(79928.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-5R!H->C_Ext-2O2sS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-5R!H->C_Ext-2O2sS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-5R!H->C_Ext-2O2sS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-4R!H-R_N-5R!H->C_Ext-2O2sS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-2O2sS-R_Ext-4R!H-R_Ext-3R!H-R_Int-8R!H-7R!H",
    kinetics = ArrheniusBM(A=(1.27e+08,'s^-1'), n=0.77, w0=(250000,'J/mol'), E0=(106828,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-2O2sS-R_Ext-4R!H-R_Ext-3R!H-R_Int-8R!H-7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-2O2sS-R_Ext-4R!H-R_Ext-3R!H-R_Int-8R!H-7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-2O2sS-R_Ext-4R!H-R_Ext-3R!H-R_Int-8R!H-7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_5R!H->O_Ext-2O2sS-R_Ext-4R!H-R_Ext-3R!H-R_Int-8R!H-7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-2O2sS-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(6.49973e+11,'s^-1'), n=-0.123415, w0=(250000,'J/mol'), E0=(124875,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0004997226811695135, var=0.12607169796406748, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-2O2sS-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-2O2sS-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 0.7130683798838977"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-2O2sS-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 0.7130683798838977""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-2O2sS-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 0.7130683798838977
""",
)

entry(
    index = 28,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.31e+11,'s^-1'), n=0, w0=(250000,'J/mol'), E0=(101885,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(6.74113e-14,'s^-1'), n=6.96696, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.7870181052988094, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 14.54024649572565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 14.54024649572565""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 14.54024649572565
""",
)

entry(
    index = 30,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-3R!H-R_Ext-2O2sS-R",
    kinetics = ArrheniusBM(A=(3.63e+10,'s^-1'), n=0, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-3R!H-R_Ext-2O2sS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-3R!H-R_Ext-2O2sS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-3R!H-R_Ext-2O2sS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-3R!H-R_Ext-2O2sS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-2O2sS-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.09e+12,'s^-1'), n=0, w0=(250000,'J/mol'), E0=(87086.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-2O2sS-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-2O2sS-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-2O2sS-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Int-4R!H-1O2s_2O2sS-u0_Ext-3R!H-R_Ext-2O2sS-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-2O2sS-R_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.31e+11,'s^-1'), n=0, w0=(250000,'J/mol'), E0=(125253,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-2O2sS-R_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-2O2sS-R_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-2O2sS-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Int-5BrCClFINPSSi-3R!H_Ext-2O2sS-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-2O2sS-R",
    kinetics = ArrheniusBM(A=(2.57e+10,'s^-1'), n=0, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-2O2sS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-2O2sS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-2O2sS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-2O2sS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

