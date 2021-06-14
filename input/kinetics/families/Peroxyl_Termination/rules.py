#!/usr/bin/env python
# encoding: utf-8

name = "Peroxyl_Termination/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(7.5021e+13,'m^3/(mol*s)'), n=-2.67699, w0=(868500,'J/mol'), E0=(146900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1514911754219608, var=4.223060086659366, Tref=1000.0, N=13, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 13 training reactions at node Root
    Total Standard Deviation in ln(k): 4.500378792257485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root
Total Standard Deviation in ln(k): 4.500378792257485""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root
Total Standard Deviation in ln(k): 4.500378792257485
""",
)

entry(
    index = 2,
    label = "Root_Ext-6R-R",
    kinetics = ArrheniusBM(A=(1.02098e+11,'m^3/(mol*s)'), n=-1.78129, w0=(868500,'J/mol'), E0=(139910,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.15289396113163675, var=4.723856967548265, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-6R-R',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-6R-R
    Total Standard Deviation in ln(k): 4.741334251933517"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-6R-R
Total Standard Deviation in ln(k): 4.741334251933517""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-6R-R
Total Standard Deviation in ln(k): 4.741334251933517
""",
)

entry(
    index = 3,
    label = "Root_Ext-6R-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(5.67271e+10,'m^3/(mol*s)'), n=-1.70819, w0=(868500,'J/mol'), E0=(140517,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.15250949917862072, var=5.046358747276254, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_Ext-6R-R_Ext-1R!H-R',), comment="""BM rule fitted to 11 training reactions at node Root_Ext-6R-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 4.886647005009499"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_Ext-6R-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 4.886647005009499""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_Ext-6R-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 4.886647005009499
""",
)

entry(
    index = 4,
    label = "Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(10.2575,'m^3/(mol*s)'), n=1.27601, w0=(868500,'J/mol'), E0=(86850,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0704547866281544, var=5.9475945134764245, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 5.066107951225832"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 5.066107951225832""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 5.066107951225832
""",
)

entry(
    index = 5,
    label = "Root_Ext-6R-R_Ext-1R!H-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(0.644762,'m^3/(mol*s)'), n=1.49139, w0=(868500,'J/mol'), E0=(86850,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.2388038591025383, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-6R-R_Ext-1R!H-R_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 3.112572510307885"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 3.112572510307885""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 3.112572510307885
""",
)

entry(
    index = 6,
    label = "Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(0.649366,'m^3/(mol*s)'), n=1.98369, w0=(868500,'J/mol'), E0=(86850,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.647729404825706, var=3.8297396649529167, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 8.063234175304059"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 8.063234175304059""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 8.063234175304059
""",
)

entry(
    index = 7,
    label = "Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(25.7369,'m^3/(mol*s)'), n=1.04011, w0=(868500,'J/mol'), E0=(86850,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05742980918283117, var=5.478980786417615, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 4.836824061697511"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 4.836824061697511""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 4.836824061697511
""",
)

entry(
    index = 8,
    label = "Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_1R!H-inRing",
    kinetics = ArrheniusBM(A=(8.7e+06,'m^3/(mol*s)'), n=0, w0=(868500,'J/mol'), E0=(86850,'J/mol'), Tmin=(286,'K'), Tmax=(323,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(1.3e+06,'m^3/(mol*s)'), n=0, w0=(868500,'J/mol'), E0=(86850,'J/mol'), Tmin=(323,'K'), Tmax=(353,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_N-1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_N-1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_N-1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_N-1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(20.1858,'m^3/(mol*s)'), n=0.984606, w0=(868500,'J/mol'), E0=(86850,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05436510918088734, var=2.7953137794187914, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 3.4883507993885647"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 3.4883507993885647""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 3.4883507993885647
""",
)

entry(
    index = 11,
    label = "Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_Sp-10R!H=8R!H",
    kinetics = ArrheniusBM(A=(65.157,'m^3/(mol*s)'), n=0.962887, w0=(868500,'J/mol'), E0=(86850,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.7998102585467847, var=16.943322065274458, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_Sp-10R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_Sp-10R!H=8R!H
    Total Standard Deviation in ln(k): 10.261517521973799"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_Sp-10R!H=8R!H
Total Standard Deviation in ln(k): 10.261517521973799""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_Sp-10R!H=8R!H
Total Standard Deviation in ln(k): 10.261517521973799
""",
)

entry(
    index = 12,
    label = "Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_N-Sp-10R!H=8R!H",
    kinetics = ArrheniusBM(A=(9.24205,'m^3/(mol*s)'), n=0.999085, w0=(868500,'J/mol'), E0=(86850,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.055164597164480966, var=0.020875449473485467, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_N-Sp-10R!H=8R!H',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_N-Sp-10R!H=8R!H
    Total Standard Deviation in ln(k): 0.4282554319675917"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_N-Sp-10R!H=8R!H
Total Standard Deviation in ln(k): 0.4282554319675917""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_N-Sp-10R!H=8R!H
Total Standard Deviation in ln(k): 0.4282554319675917
""",
)

entry(
    index = 13,
    label = "Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_Sp-10R!H=8R!H_1R!H-inRing",
    kinetics = ArrheniusBM(A=(560000,'m^3/(mol*s)'), n=0, w0=(868500,'J/mol'), E0=(86850,'J/mol'), Tmin=(282,'K'), Tmax=(319,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_Sp-10R!H=8R!H_1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_Sp-10R!H=8R!H_1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_Sp-10R!H=8R!H_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_Sp-10R!H=8R!H_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_Sp-10R!H=8R!H_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(25000,'m^3/(mol*s)'), n=0, w0=(868500,'J/mol'), E0=(86850,'J/mol'), Tmin=(313,'K'), Tmax=(333,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_Sp-10R!H=8R!H_N-1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_Sp-10R!H=8R!H_N-1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_Sp-10R!H=8R!H_N-1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_Sp-10R!H=8R!H_N-1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_N-Sp-10R!H=8R!H_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(9.74879,'m^3/(mol*s)'), n=0.999085, w0=(868500,'J/mol'), E0=(86850,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.8298783133793705, var=0.11756257146978773, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_N-Sp-10R!H=8R!H_Ext-11R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_N-Sp-10R!H=8R!H_Ext-11R!H-R
    Total Standard Deviation in ln(k): 2.7724929007519057"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_N-Sp-10R!H=8R!H_Ext-11R!H-R
Total Standard Deviation in ln(k): 2.7724929007519057""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_N-Sp-10R!H=8R!H_Ext-11R!H-R
Total Standard Deviation in ln(k): 2.7724929007519057
""",
)

entry(
    index = 16,
    label = "Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_N-Sp-10R!H=8R!H_Ext-11R!H-R_1R!H-inRing",
    kinetics = ArrheniusBM(A=(19000,'m^3/(mol*s)'), n=0, w0=(868500,'J/mol'), E0=(86850,'J/mol'), Tmin=(285,'K'), Tmax=(333,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_N-Sp-10R!H=8R!H_Ext-11R!H-R_1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_N-Sp-10R!H=8R!H_Ext-11R!H-R_1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_N-Sp-10R!H=8R!H_Ext-11R!H-R_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_N-Sp-10R!H=8R!H_Ext-11R!H-R_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_N-Sp-10R!H=8R!H_Ext-11R!H-R_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(29000,'m^3/(mol*s)'), n=0, w0=(868500,'J/mol'), E0=(86850,'J/mol'), Tmin=(283,'K'), Tmax=(320,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_N-Sp-10R!H=8R!H_Ext-11R!H-R_N-1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_N-Sp-10R!H=8R!H_Ext-11R!H-R_N-1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_N-Sp-10R!H=8R!H_Ext-11R!H-R_N-1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-6R-R_Ext-1R!H-R_Ext-8R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-1R!H-R_N-Sp-10R!H=8R!H_Ext-11R!H-R_N-1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

