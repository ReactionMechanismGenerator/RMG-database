#!/usr/bin/env python
# encoding: utf-8

name = "Retroene/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(3.29914e+17,'s^-1'), n=-1.73308, w0=(1.1099e+06,'J/mol'), E0=(182951,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.16692063000437535, var=8.814681701569807, Tref=1000.0, N=65, correlation='Root',), comment="""BM rule fitted to 2 training reactions at node Root
    Total Standard Deviation in ln(k): 6.371362717619001"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 6.371362717619001""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 6.371362717619001
""",
)

entry(
    index = 2,
    label = "Root_1R!H->C",
    kinetics = ArrheniusBM(A=(2.91917e+21,'s^-1'), n=-2.8733, w0=(1.04926e+06,'J/mol'), E0=(195358,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2181496522400757, var=7.835807828637173, Tref=1000.0, N=31, correlation='Root_1R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C
    Total Standard Deviation in ln(k): 6.159871971405523"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 6.159871971405523""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 6.159871971405523
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H->C",
    kinetics = ArrheniusBM(A=(1.49769e+10,'s^-1'), n=0.382551, w0=(1.16519e+06,'J/mol'), E0=(159233,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0799311574974701, var=12.366847956955514, Tref=1000.0, N=34, correlation='Root_N-1R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C
    Total Standard Deviation in ln(k): 7.250789573970193"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 7.250789573970193""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 7.250789573970193
""",
)

entry(
    index = 4,
    label = "Root_1R!H->C_2R!H->C",
    kinetics = ArrheniusBM(A=(2.02299e+20,'s^-1'), n=-2.53701, w0=(1.0543e+06,'J/mol'), E0=(190314,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2019207829805258, var=6.004435471185692, Tref=1000.0, N=27, correlation='Root_1R!H->C_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C
    Total Standard Deviation in ln(k): 5.419731385064994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C
Total Standard Deviation in ln(k): 5.419731385064994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C
Total Standard Deviation in ln(k): 5.419731385064994
""",
)

entry(
    index = 5,
    label = "Root_1R!H->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(2.60496e+13,'s^-1'), n=-0.343905, w0=(1.01525e+06,'J/mol'), E0=(242252,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=6.4548336266697035, var=111.97246879746811, Tref=1000.0, N=4, correlation='Root_1R!H->C_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C
    Total Standard Deviation in ln(k): 37.43168900536777"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 37.43168900536777""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 37.43168900536777
""",
)

entry(
    index = 6,
    label = "Root_N-1R!H->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.3938e+10,'s^-1'), n=0.63614, w0=(1.183e+06,'J/mol'), E0=(153232,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08208414286485505, var=3.1024986272172126, Tref=1000.0, N=17, correlation='Root_N-1R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.7373640995814643"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.7373640995814643""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.7373640995814643
""",
)

entry(
    index = 7,
    label = "Root_N-1R!H->C_3R!H-inRing",
    kinetics = ArrheniusBM(A=(8.03589e+12,'s^-1'), n=-0.810259, w0=(938500,'J/mol'), E0=(143073,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004915336118469724, var=82.45074987938592, Tref=1000.0, N=2, correlation='Root_N-1R!H->C_3R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_3R!H-inRing
    Total Standard Deviation in ln(k): 18.215824782958304"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_3R!H-inRing
Total Standard Deviation in ln(k): 18.215824782958304""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_3R!H-inRing
Total Standard Deviation in ln(k): 18.215824782958304
""",
)

entry(
    index = 8,
    label = "Root_N-1R!H->C_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(5.71165e+08,'s^-1'), n=0.792569, w0=(1.17523e+06,'J/mol'), E0=(163842,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0634193157121934, var=14.689758651951971, Tref=1000.0, N=15, correlation='Root_N-1R!H->C_N-3R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing
    Total Standard Deviation in ln(k): 7.842937438650996"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing
Total Standard Deviation in ln(k): 7.842937438650996""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing
Total Standard Deviation in ln(k): 7.842937438650996
""",
)

entry(
    index = 9,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.47454e+16,'s^-1'), n=-1.36404, w0=(1.0845e+06,'J/mol'), E0=(190512,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.16017174518575955, var=4.989219283921508, Tref=1000.0, N=15, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.880330175567876"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.880330175567876""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.880330175567876
""",
)

entry(
    index = 10,
    label = "Root_1R!H->C_2R!H->C_5R!H->O",
    kinetics = ArrheniusBM(A=(3.59298e+09,'s^-1'), n=0.614601, w0=(1.0845e+06,'J/mol'), E0=(169310,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07280803979615884, var=3.9519504359180297, Tref=1000.0, N=5, correlation='Root_1R!H->C_2R!H->C_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O
    Total Standard Deviation in ln(k): 4.168250509264941"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O
Total Standard Deviation in ln(k): 4.168250509264941""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O
Total Standard Deviation in ln(k): 4.168250509264941
""",
)

entry(
    index = 11,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->O",
    kinetics = ArrheniusBM(A=(5.70488e+33,'s^-1'), n=-6.74695, w0=(968000,'J/mol'), E0=(200888,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.34291747530997396, var=16.416542173868212, Tref=1000.0, N=7, correlation='Root_1R!H->C_2R!H->C_N-5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O
    Total Standard Deviation in ln(k): 8.984253428860972"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O
Total Standard Deviation in ln(k): 8.984253428860972""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O
Total Standard Deviation in ln(k): 8.984253428860972
""",
)

entry(
    index = 12,
    label = "Root_1R!H->C_N-2R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.50267e+13,'s^-1'), n=-0.29146, w0=(1.0665e+06,'J/mol'), E0=(250540,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1R!H->C_N-2R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_1R!H->C_N-2R!H->C_2NOS->S",
    kinetics = ArrheniusBM(A=(1.43424e+08,'s^-1'), n=0.644242, w0=(953500,'J/mol'), E0=(106636,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1R!H->C_N-2R!H->C_2NOS->S',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_2NOS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_2NOS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_2NOS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_1R!H->C_N-2R!H->C_N-2NOS->S",
    kinetics = ArrheniusBM(A=(5.03649e+09,'s^-1'), n=0.289241, w0=(1.0205e+06,'J/mol'), E0=(165640,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.016015533849458193, var=0.027743929771675672, Tref=1000.0, N=2, correlation='Root_1R!H->C_N-2R!H->C_N-2NOS->S',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S
    Total Standard Deviation in ln(k): 0.3741589167898476"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S
Total Standard Deviation in ln(k): 0.3741589167898476""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S
Total Standard Deviation in ln(k): 0.3741589167898476
""",
)

entry(
    index = 15,
    label = "Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(7.30229e+08,'s^-1'), n=0.995367, w0=(1.183e+06,'J/mol'), E0=(138104,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9718999497707853, var=2.1443634782942387, Tref=1000.0, N=4, correlation='Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 5.377622613249818"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.377622613249818""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.377622613249818
""",
)

entry(
    index = 16,
    label = "Root_N-1R!H->C_Ext-2R!H-R_7R!H->O",
    kinetics = ArrheniusBM(A=(7.47098e+12,'s^-1'), n=-0.267196, w0=(1.183e+06,'J/mol'), E0=(99317.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-1R!H->C_Ext-2R!H-R_7R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_7R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O",
    kinetics = ArrheniusBM(A=(6.01189e+09,'s^-1'), n=0.754213, w0=(1.183e+06,'J/mol'), E0=(159151,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09510814328057031, var=0.387587740300408, Tref=1000.0, N=12, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O
    Total Standard Deviation in ln(k): 1.4870439809451415"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O
Total Standard Deviation in ln(k): 1.4870439809451415""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O
Total Standard Deviation in ln(k): 1.4870439809451415
""",
)

entry(
    index = 18,
    label = "Root_N-1R!H->C_3R!H-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(5279.23,'s^-1'), n=1.38734, w0=(938500,'J/mol'), E0=(119664,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-1R!H->C_3R!H-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_3R!H-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_3R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_3R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(9.86671e+06,'s^-1'), n=1.56749, w0=(1.183e+06,'J/mol'), E0=(173559,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.017669080471101054, var=0.33083863833173466, Tref=1000.0, N=9, correlation='Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 1.1974897084813658"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.1974897084813658""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.1974897084813658
""",
)

entry(
    index = 20,
    label = "Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.02018e+11,'s^-1'), n=-0.0739297, w0=(1.183e+06,'J/mol'), E0=(160258,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0038766176496688475, var=47.42603160880866, Tref=1000.0, N=4, correlation='Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R
    Total Standard Deviation in ln(k): 13.815661203148398"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 13.815661203148398""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 13.815661203148398
""",
)

entry(
    index = 21,
    label = "Root_N-1R!H->C_N-3R!H-inRing_5R!H->O",
    kinetics = ArrheniusBM(A=(1.95284e+06,'s^-1'), n=1.88752, w0=(1.183e+06,'J/mol'), E0=(168117,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-1R!H->C_N-3R!H-inRing_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-1R!H->C_N-3R!H-inRing_N-5R!H->O",
    kinetics = ArrheniusBM(A=(185531,'s^-1'), n=1.69565, w0=(1.0665e+06,'J/mol'), E0=(150436,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-1R!H->C_N-3R!H-inRing_N-5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N",
    kinetics = ArrheniusBM(A=(7.55943e+06,'s^-1'), n=1.59729, w0=(1.0845e+06,'J/mol'), E0=(192525,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.029349407026579746, var=1.204720350666887, Tref=1000.0, N=5, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N
    Total Standard Deviation in ln(k): 2.274134509655974"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N
Total Standard Deviation in ln(k): 2.274134509655974""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N
Total Standard Deviation in ln(k): 2.274134509655974
""",
)

entry(
    index = 24,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N",
    kinetics = ArrheniusBM(A=(1.08743e+12,'s^-1'), n=0.000461227, w0=(1.0845e+06,'J/mol'), E0=(169161,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06744101306807582, var=2.2494036752109094, Tref=1000.0, N=10, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N
    Total Standard Deviation in ln(k): 3.1761538801883664"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N
Total Standard Deviation in ln(k): 3.1761538801883664""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N
Total Standard Deviation in ln(k): 3.1761538801883664
""",
)

entry(
    index = 25,
    label = "Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(4.16224e+08,'s^-1'), n=0.988267, w0=(1.0845e+06,'J/mol'), E0=(162518,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00043434819943897216, var=9.21656333564786, Tref=1000.0, N=2, correlation='Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R
    Total Standard Deviation in ln(k): 6.0872251204039465"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R
Total Standard Deviation in ln(k): 6.0872251204039465""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R
Total Standard Deviation in ln(k): 6.0872251204039465
""",
)

entry(
    index = 26,
    label = "Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(8.08931e+06,'s^-1'), n=1.33845, w0=(1.0845e+06,'J/mol'), E0=(171450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.026710218585040676, var=4.619771263908723, Tref=1000.0, N=2, correlation='Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R
    Total Standard Deviation in ln(k): 4.376019146157587"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.376019146157587""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.376019146157587
""",
)

entry(
    index = 27,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.83014e+38,'s^-1'), n=-8.23851, w0=(968000,'J/mol'), E0=(200906,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.41826346251888336, var=21.571226466455663, Tref=1000.0, N=5, correlation='Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R
    Total Standard Deviation in ln(k): 10.36187210002245"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 10.36187210002245""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 10.36187210002245
""",
)

entry(
    index = 28,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-5C-R",
    kinetics = ArrheniusBM(A=(2.47269e+12,'s^-1'), n=-0.334211, w0=(968000,'J/mol'), E0=(180538,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->O",
    kinetics = ArrheniusBM(A=(2.3921e+11,'s^-1'), n=-0.284346, w0=(1.0665e+06,'J/mol'), E0=(165328,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->O",
    kinetics = ArrheniusBM(A=(1.00939e+08,'s^-1'), n=0.86916, w0=(974500,'J/mol'), E0=(165909,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.56017e+12,'s^-1'), n=-0.119702, w0=(1.183e+06,'J/mol'), E0=(135771,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(7.82163e+08,'s^-1'), n=0.989298, w0=(1.183e+06,'J/mol'), E0=(138899,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9514830544978642, var=2.010530764035632, Tref=1000.0, N=2, correlation='Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 5.2332386811796"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 5.2332386811796""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 5.2332386811796
""",
)

entry(
    index = 33,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R",
    kinetics = ArrheniusBM(A=(8.60671e+08,'s^-1'), n=0.975858, w0=(1.183e+06,'J/mol'), E0=(154165,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.8106533184083914, var=2.476564943200298, Tref=1000.0, N=7, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R
    Total Standard Deviation in ln(k): 5.1916901547713445"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R
Total Standard Deviation in ln(k): 5.1916901547713445""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R
Total Standard Deviation in ln(k): 5.1916901547713445
""",
)

entry(
    index = 34,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.0988e+10,'s^-1'), n=0.632459, w0=(1.183e+06,'J/mol'), E0=(164532,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.14086930923198027, var=0.05370774337580898, Tref=1000.0, N=3, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.8185389619247819"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.8185389619247819""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.8185389619247819
""",
)

entry(
    index = 35,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.19613e+13,'s^-1'), n=-0.375547, w0=(1.183e+06,'J/mol'), E0=(152765,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(4.72908e+06,'s^-1'), n=1.66491, w0=(1.183e+06,'J/mol'), E0=(172562,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06209838620188961, var=0.15842678483127076, Tref=1000.0, N=7, correlation='Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 0.9539680385815258"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C
Total Standard Deviation in ln(k): 0.9539680385815258""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C
Total Standard Deviation in ln(k): 0.9539680385815258
""",
)

entry(
    index = 37,
    label = "Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(5.40789e+14,'s^-1'), n=-0.823434, w0=(1.183e+06,'J/mol'), E0=(200846,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.008726972437150324, var=0.04557818763103101, Tref=1000.0, N=2, correlation='Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 0.44991893248605175"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 0.44991893248605175""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 0.44991893248605175
""",
)

entry(
    index = 38,
    label = "Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(6.72253e+12,'s^-1'), n=-0.0948638, w0=(1.183e+06,'J/mol'), E0=(172576,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0053888222478077645, var=0.5959934434744609, Tref=1000.0, N=3, correlation='Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 1.5612074955319186"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R_7R!H->C
Total Standard Deviation in ln(k): 1.5612074955319186""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R_7R!H->C
Total Standard Deviation in ln(k): 1.5612074955319186
""",
)

entry(
    index = 39,
    label = "Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(981181,'s^-1'), n=-0.141465, w0=(1.183e+06,'J/mol'), E0=(124049,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(8.93565e+06,'s^-1'), n=1.63604, w0=(1.0845e+06,'J/mol'), E0=(201748,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01902332493336781, var=5.776135420717914, Tref=1000.0, N=2, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R
    Total Standard Deviation in ln(k): 4.865895780841525"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.865895780841525""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.865895780841525
""",
)

entry(
    index = 41,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.99481e+07,'s^-1'), n=1.33884, w0=(1.0845e+06,'J/mol'), E0=(186501,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01435034261978941, var=0.03782526341694205, Tref=1000.0, N=2, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R
    Total Standard Deviation in ln(k): 0.42595141028386246"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R
Total Standard Deviation in ln(k): 0.42595141028386246""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R
Total Standard Deviation in ln(k): 0.42595141028386246
""",
)

entry(
    index = 42,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.32129e+11,'s^-1'), n=0.19464, w0=(1.0845e+06,'J/mol'), E0=(175938,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05624842777530617, var=3.336036409379837, Tref=1000.0, N=4, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R
    Total Standard Deviation in ln(k): 3.802940193892467"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.802940193892467""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.802940193892467
""",
)

entry(
    index = 43,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R",
    kinetics = ArrheniusBM(A=(9.59979e+09,'s^-1'), n=0.653803, w0=(1.0845e+06,'J/mol'), E0=(159613,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0061513757544572585, var=1.838372867979581, Tref=1000.0, N=4, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R
    Total Standard Deviation in ln(k): 2.7336080391743205"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R
Total Standard Deviation in ln(k): 2.7336080391743205""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R
Total Standard Deviation in ln(k): 2.7336080391743205
""",
)

entry(
    index = 44,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7CClOSSi->O",
    kinetics = ArrheniusBM(A=(3.45994e+07,'s^-1'), n=1.37339, w0=(1.0845e+06,'J/mol'), E0=(158592,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7CClOSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7CClOSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7CClOSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7CClOSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7CClOSSi->O",
    kinetics = ArrheniusBM(A=(2777.82,'s^-1'), n=2.32292, w0=(1.0845e+06,'J/mol'), E0=(138850,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7CClOSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7CClOSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7CClOSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7CClOSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1871.16,'s^-1'), n=2.39873, w0=(1.0845e+06,'J/mol'), E0=(149513,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(1.20115e+13,'s^-1'), n=-0.161387, w0=(1.0845e+06,'J/mol'), E0=(173499,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(383.322,'s^-1'), n=2.56708, w0=(1.0845e+06,'J/mol'), E0=(152593,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(675934,'s^-1'), n=1.70582, w0=(1.0845e+06,'J/mol'), E0=(178689,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.3594e+40,'s^-1'), n=-8.69663, w0=(968000,'J/mol'), E0=(194614,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.44445263765859844, var=23.11680634729946, Tref=1000.0, N=4, correlation='Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 10.75546940271655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 10.75546940271655""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 10.75546940271655
""",
)

entry(
    index = 51,
    label = "Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(1.72964e+12,'s^-1'), n=-0.154553, w0=(1.183e+06,'J/mol'), E0=(129036,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3.25982e+13,'s^-1'), n=-0.459378, w0=(1.183e+06,'J/mol'), E0=(156365,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.009641817806757116, var=0.05092668070555705, Tref=1000.0, N=2, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.47663304654519345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.47663304654519345""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.47663304654519345
""",
)

entry(
    index = 53,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.26982e+13,'s^-1'), n=-0.442684, w0=(1.183e+06,'J/mol'), E0=(141988,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008973802109952855, var=1.7601356034708961, Tref=1000.0, N=4, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 2.6822313187810094"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.6822313187810094""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.6822313187810094
""",
)

entry(
    index = 54,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(2.41068e+13,'s^-1'), n=-0.43239, w0=(1.183e+06,'J/mol'), E0=(160784,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008055355569653555, var=0.1636224322977239, Tref=1000.0, N=2, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 0.8311603334693084"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.8311603334693084""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.8311603334693084
""",
)

entry(
    index = 55,
    label = "Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_7C-inRing",
    kinetics = ArrheniusBM(A=(1.18223e+12,'s^-1'), n=-0.0806669, w0=(1.183e+06,'J/mol'), E0=(164116,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_7C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing",
    kinetics = ArrheniusBM(A=(3.93467e+06,'s^-1'), n=1.69077, w0=(1.183e+06,'J/mol'), E0=(172691,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.047593991409819986, var=0.10410275539571957, Tref=1000.0, N=6, correlation='Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing
    Total Standard Deviation in ln(k): 0.766409835904944"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing
Total Standard Deviation in ln(k): 0.766409835904944""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing
Total Standard Deviation in ln(k): 0.766409835904944
""",
)

entry(
    index = 57,
    label = "Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C_Ext-7ClNOSSi-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(5.41006e+14,'s^-1'), n=-0.823484, w0=(1.183e+06,'J/mol'), E0=(200218,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C_Ext-7ClNOSSi-R_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C_Ext-7ClNOSSi-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C_Ext-7ClNOSSi-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C_Ext-7ClNOSSi-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R",
    kinetics = ArrheniusBM(A=(6.26347e+11,'s^-1'), n=0.219786, w0=(1.183e+06,'J/mol'), E0=(170925,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0058163353471268765, var=2.1167643769249636, Tref=1000.0, N=2, correlation='Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R
    Total Standard Deviation in ln(k): 2.931323893522042"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 2.931323893522042""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 2.931323893522042
""",
)

entry(
    index = 59,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_8R!H->C",
    kinetics = ArrheniusBM(A=(86311.7,'s^-1'), n=2.17939, w0=(1.0845e+06,'J/mol'), E0=(187331,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(1.87591e+07,'s^-1'), n=1.59301, w0=(1.0845e+06,'J/mol'), E0=(212642,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_N-8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(8.32843e+06,'s^-1'), n=1.5484, w0=(1.0845e+06,'J/mol'), E0=(186060,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(1.89761e+08,'s^-1'), n=1.1305, w0=(1.0845e+06,'J/mol'), E0=(186932,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7CClOSSi->O",
    kinetics = ArrheniusBM(A=(2.30347e+12,'s^-1'), n=0.0733742, w0=(1.0845e+06,'J/mol'), E0=(183974,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.015266294096436867, var=4.881791266034793, Tref=1000.0, N=2, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7CClOSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7CClOSSi->O
    Total Standard Deviation in ln(k): 4.4677747708059945"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7CClOSSi->O
Total Standard Deviation in ln(k): 4.4677747708059945""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7CClOSSi->O
Total Standard Deviation in ln(k): 4.4677747708059945
""",
)

entry(
    index = 64,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7CClOSSi->O",
    kinetics = ArrheniusBM(A=(1.00713e+10,'s^-1'), n=0.423656, w0=(1.0845e+06,'J/mol'), E0=(167123,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03324198521787133, var=13.418124712865499, Tref=1000.0, N=2, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7CClOSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7CClOSSi->O
    Total Standard Deviation in ln(k): 7.42701923178722"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7CClOSSi->O
Total Standard Deviation in ln(k): 7.42701923178722""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7CClOSSi->O
Total Standard Deviation in ln(k): 7.42701923178722
""",
)

entry(
    index = 65,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(2.60089e+07,'s^-1'), n=1.28561, w0=(1.0845e+06,'J/mol'), E0=(152714,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.004127634385233546, var=1.0888059594189994, Tref=1000.0, N=2, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C
    Total Standard Deviation in ln(k): 2.1022291030877542"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C
Total Standard Deviation in ln(k): 2.1022291030877542""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C
Total Standard Deviation in ln(k): 2.1022291030877542
""",
)

entry(
    index = 66,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(5.01584e+11,'s^-1'), n=0.27209, w0=(1.0845e+06,'J/mol'), E0=(164653,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0017558494266727738, var=2.344475790003672, Tref=1000.0, N=2, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 3.073998107322022"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C
Total Standard Deviation in ln(k): 3.073998107322022""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C
Total Standard Deviation in ln(k): 3.073998107322022
""",
)

entry(
    index = 67,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.31787e+40,'s^-1'), n=-8.74581, w0=(968000,'J/mol'), E0=(182985,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5644001667961636, var=32.38162431418706, Tref=1000.0, N=3, correlation='Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 12.82600660003687"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 12.82600660003687""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 12.82600660003687
""",
)

entry(
    index = 68,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_7C-inRing",
    kinetics = ArrheniusBM(A=(1.75623e+14,'s^-1'), n=-0.68222, w0=(1.183e+06,'J/mol'), E0=(156891,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_7C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 69,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_N-7C-inRing",
    kinetics = ArrheniusBM(A=(7.16993e+12,'s^-1'), n=-0.258319, w0=(1.183e+06,'J/mol'), E0=(155989,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_N-7C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_N-7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.01133e+12,'s^-1'), n=-0.317664, w0=(1.183e+06,'J/mol'), E0=(115676,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(5.77584e+12,'s^-1'), n=-0.330794, w0=(1.183e+06,'J/mol'), E0=(148158,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(8.84721e+12,'s^-1'), n=-0.302094, w0=(1.183e+06,'J/mol'), E0=(150154,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006801173647055783, var=0.016504986209969107, Tref=1000.0, N=2, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 0.2746401658299856"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 0.2746401658299856""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 0.2746401658299856
""",
)

entry(
    index = 73,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H",
    kinetics = ArrheniusBM(A=(4.04251e+12,'s^-1'), n=-0.258404, w0=(1.183e+06,'J/mol'), E0=(154724,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H",
    kinetics = ArrheniusBM(A=(7.65417e+13,'s^-1'), n=-0.52566, w0=(1.183e+06,'J/mol'), E0=(166257,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R",
    kinetics = ArrheniusBM(A=(139248,'s^-1'), n=2.06526, w0=(1.183e+06,'J/mol'), E0=(165686,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6647699906393877, var=1.1672292739411867, Tref=1000.0, N=4, correlation='Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R
    Total Standard Deviation in ln(k): 3.836159769370438"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R
Total Standard Deviation in ln(k): 3.836159769370438""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R
Total Standard Deviation in ln(k): 3.836159769370438
""",
)

entry(
    index = 76,
    label = "Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(7.0786e+07,'s^-1'), n=1.38493, w0=(1.183e+06,'J/mol'), E0=(180119,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 77,
    label = "Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.08466e+14,'s^-1'), n=-0.414807, w0=(1.183e+06,'J/mol'), E0=(173074,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 78,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7CClOSSi->O_8R!H->C",
    kinetics = ArrheniusBM(A=(1.18304e+09,'s^-1'), n=0.953965, w0=(1.0845e+06,'J/mol'), E0=(164806,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7CClOSSi->O_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7CClOSSi->O_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7CClOSSi->O_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7CClOSSi->O_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7CClOSSi->O_N-8R!H->C",
    kinetics = ArrheniusBM(A=(3.04101e+10,'s^-1'), n=0.719247, w0=(1.0845e+06,'J/mol'), E0=(192037,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7CClOSSi->O_N-8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7CClOSSi->O_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7CClOSSi->O_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7CClOSSi->O_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7CClOSSi->O_8R!H->C",
    kinetics = ArrheniusBM(A=(69952.6,'s^-1'), n=1.95219, w0=(1.0845e+06,'J/mol'), E0=(145203,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7CClOSSi->O_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7CClOSSi->O_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7CClOSSi->O_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7CClOSSi->O_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 81,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7CClOSSi->O_N-8R!H->C",
    kinetics = ArrheniusBM(A=(4.82682e+06,'s^-1'), n=1.39789, w0=(1.0845e+06,'J/mol'), E0=(170872,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7CClOSSi->O_N-8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7CClOSSi->O_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7CClOSSi->O_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7CClOSSi->O_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7CClOSSi->O",
    kinetics = ArrheniusBM(A=(4.85334e+08,'s^-1'), n=1.04262, w0=(1.0845e+06,'J/mol'), E0=(160490,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7CClOSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7CClOSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7CClOSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7CClOSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 83,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7CClOSSi->O",
    kinetics = ArrheniusBM(A=(237214,'s^-1'), n=1.7551, w0=(1.0845e+06,'J/mol'), E0=(143269,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7CClOSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7CClOSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7CClOSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7CClOSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7CClOSSi->O",
    kinetics = ArrheniusBM(A=(1.01292e+10,'s^-1'), n=0.801049, w0=(1.0845e+06,'J/mol'), E0=(167172,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7CClOSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7CClOSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7CClOSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7CClOSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 85,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7CClOSSi->O",
    kinetics = ArrheniusBM(A=(1.9784e+14,'s^-1'), n=-0.523303, w0=(1.0845e+06,'J/mol'), E0=(164051,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7CClOSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7CClOSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7CClOSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7CClOSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(6.33177e+16,'s^-1'), n=-2.0239, w0=(968000,'J/mol'), E0=(100618,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.023344927135838273, var=2.623167713233261, Tref=1000.0, N=2, correlation='Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 3.305563859910207"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 3.305563859910207""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 3.305563859910207
""",
)

entry(
    index = 87,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing",
    kinetics = ArrheniusBM(A=(8.29948e+12,'s^-1'), n=-0.271204, w0=(1.183e+06,'J/mol'), E0=(151786,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 88,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing",
    kinetics = ArrheniusBM(A=(8.55485e+12,'s^-1'), n=-0.320523, w0=(1.183e+06,'J/mol'), E0=(148430,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.43227e+13,'s^-1'), n=-0.435883, w0=(1.183e+06,'J/mol'), E0=(171149,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R",
    kinetics = ArrheniusBM(A=(7.42317e+12,'s^-1'), n=-0.355627, w0=(1.183e+06,'J/mol'), E0=(168309,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(7.07376e+12,'s^-1'), n=-0.349886, w0=(1.183e+06,'J/mol'), E0=(167015,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 92,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(4.77467e+13,'s^-1'), n=-1.06001, w0=(968000,'J/mol'), E0=(89904,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

