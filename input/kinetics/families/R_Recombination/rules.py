#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination/rules"
shortDesc = ""
longDesc = """
For some reason the definition of Cs_rad::

 Cs_rad
 1 * C 1 

which is not mutually exclusive from its L2 siblings such as::

 Cd_rad
 1 * C 1 {2,D}, {3,S}
 2   C 0 {1,D}
 3   R 0 {1,S}

is apparently not causing a problem
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(7.93555e+06,'m^3/(mol*s)'), n=0.0453581, w0=(181.664,'kJ/mol'), E0=(75.0027,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.011153596611116033, var=14.587991955139582, Tref=1000.0, N=370, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 370 training reactions at node Root
    Total Standard Deviation in ln(k): 7.684955349930359"""),
    rank = 11,
    shortDesc = """BM rule fitted to 370 training reactions at node Root
Total Standard Deviation in ln(k): 7.684955349930359""",
    longDesc = 
"""
BM rule fitted to 370 training reactions at node Root
Total Standard Deviation in ln(k): 7.684955349930359
""",
)

entry(
    index = 2,
    label = "Root_1R-inRing",
    kinetics = ArrheniusBM(A=(8.48393e+10,'m^3/(mol*s)'), n=-1.02738, w0=(190.107,'kJ/mol'), E0=(92.3465,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.048733845549542444, var=1.9549336706642162, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_1R-inRing',), comment="""BM rule fitted to 28 training reactions at node Root_1R-inRing
    Total Standard Deviation in ln(k): 2.9254462350330948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_1R-inRing
Total Standard Deviation in ln(k): 2.9254462350330948""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_1R-inRing
Total Standard Deviation in ln(k): 2.9254462350330948
""",
)

entry(
    index = 3,
    label = "Root_N-1R-inRing",
    kinetics = ArrheniusBM(A=(5.19469e+06,'m^3/(mol*s)'), n=0.0919353, w0=(182.221,'kJ/mol'), E0=(74.8362,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.007068040580304948, var=15.460708432098524, Tref=1000.0, N=342, data_mean=0.0, correlation='Root_N-1R-inRing',), comment="""BM rule fitted to 342 training reactions at node Root_N-1R-inRing
    Total Standard Deviation in ln(k): 7.900398744119846"""),
    rank = 11,
    shortDesc = """BM rule fitted to 342 training reactions at node Root_N-1R-inRing
Total Standard Deviation in ln(k): 7.900398744119846""",
    longDesc = 
"""
BM rule fitted to 342 training reactions at node Root_N-1R-inRing
Total Standard Deviation in ln(k): 7.900398744119846
""",
)

entry(
    index = 4,
    label = "Root_1R-inRing_2R->O",
    kinetics = ArrheniusBM(A=(1.90891e+06,'m^3/(mol*s)'), n=0.0381637, w0=(179,'kJ/mol'), E0=(43.5106,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03546200984242961, var=0.4381627376232808, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R-inRing_2R->O',), comment="""BM rule fitted to 4 training reactions at node Root_1R-inRing_2R->O
    Total Standard Deviation in ln(k): 1.4161120993157608"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R-inRing_2R->O
Total Standard Deviation in ln(k): 1.4161120993157608""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R-inRing_2R->O
Total Standard Deviation in ln(k): 1.4161120993157608
""",
)

entry(
    index = 5,
    label = "Root_1R-inRing_N-2R->O",
    kinetics = ArrheniusBM(A=(3.35755e+08,'m^3/(mol*s)'), n=-0.234318, w0=(191.958,'kJ/mol'), E0=(88.3753,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.012525071724623325, var=2.7341591966369014, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O',), comment="""BM rule fitted to 24 training reactions at node Root_1R-inRing_N-2R->O
    Total Standard Deviation in ln(k): 3.3463582493890147"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_1R-inRing_N-2R->O
Total Standard Deviation in ln(k): 3.3463582493890147""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_1R-inRing_N-2R->O
Total Standard Deviation in ln(k): 3.3463582493890147
""",
)

entry(
    index = 6,
    label = "Root_N-1R-inRing_1R->S",
    kinetics = ArrheniusBM(A=(181562,'m^3/(mol*s)'), n=0.790398, w0=(143.909,'kJ/mol'), E0=(19.457,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0766922916159491, var=5.298790957291349, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R-inRing_1R->S',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R-inRing_1R->S
    Total Standard Deviation in ln(k): 4.807414492132214"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R-inRing_1R->S
Total Standard Deviation in ln(k): 4.807414492132214""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R-inRing_1R->S
Total Standard Deviation in ln(k): 4.807414492132214
""",
)

entry(
    index = 7,
    label = "Root_N-1R-inRing_N-1R->S",
    kinetics = ArrheniusBM(A=(2.00071e+07,'m^3/(mol*s)'), n=-0.144823, w0=(183.72,'kJ/mol'), E0=(89.4043,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005688429074173293, var=17.050180272377993, Tref=1000.0, N=331, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S',), comment="""BM rule fitted to 331 training reactions at node Root_N-1R-inRing_N-1R->S
    Total Standard Deviation in ln(k): 8.29221733953757"""),
    rank = 11,
    shortDesc = """BM rule fitted to 331 training reactions at node Root_N-1R-inRing_N-1R->S
Total Standard Deviation in ln(k): 8.29221733953757""",
    longDesc = 
"""
BM rule fitted to 331 training reactions at node Root_N-1R-inRing_N-1R->S
Total Standard Deviation in ln(k): 8.29221733953757
""",
)

entry(
    index = 8,
    label = "Root_1R-inRing_2R->O_Ext-2O-R_Ext-1R-R_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = Arrhenius(A=(27200,'m^3/(mol*s)'), n=0.504, Ea=(-4.37416,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_2R->O_Ext-2O-R_Ext-1R-R_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_2R->O_Ext-2O-R_Ext-1R-R_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_2R->O_Ext-2O-R_Ext-1R-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_2R->O_Ext-2O-R_Ext-1R-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_1R-inRing_2R->O_Ext-2O-R_Ext-1R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R",
    kinetics = Arrhenius(A=(252000,'m^3/(mol*s)'), n=0.34, Ea=(-2.95093,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_2R->O_Ext-2O-R_Ext-1R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_2R->O_Ext-2O-R_Ext-1R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_2R->O_Ext-2O-R_Ext-1R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_2R->O_Ext-2O-R_Ext-1R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->H",
    kinetics = ArrheniusBM(A=(3.59291e+08,'m^3/(mol*s)'), n=-0.14961, w0=(205.5,'kJ/mol'), E0=(99.1137,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02523049198730011, var=2.9455084582689826, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->H',), comment="""BM rule fitted to 14 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H
    Total Standard Deviation in ln(k): 3.504016499400007"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H
Total Standard Deviation in ln(k): 3.504016499400007""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H
Total Standard Deviation in ln(k): 3.504016499400007
""",
)

entry(
    index = 11,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H",
    kinetics = ArrheniusBM(A=(1.26173e+09,'m^3/(mol*s)'), n=-0.614843, w0=(190.669,'kJ/mol'), E0=(20.8886,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.011174083435872676, var=0.26320844618587913, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H',), comment="""BM rule fitted to 10 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H
    Total Standard Deviation in ln(k): 1.0565817535348854"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H
Total Standard Deviation in ln(k): 1.0565817535348854""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H
Total Standard Deviation in ln(k): 1.0565817535348854
""",
)

entry(
    index = 12,
    label = "Root_N-1R-inRing_1R->S_2R->H",
    kinetics = ArrheniusBM(A=(1.676e+07,'m^3/(mol*s)'), n=0.496549, w0=(181.5,'kJ/mol'), E0=(44.7624,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.529191827621723, var=20.63519440789798, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_1R->S_2R->H',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_1R->S_2R->H
    Total Standard Deviation in ln(k): 15.461458407419174"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_1R->S_2R->H
Total Standard Deviation in ln(k): 15.461458407419174""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_1R->S_2R->H
Total Standard Deviation in ln(k): 15.461458407419174
""",
)

entry(
    index = 13,
    label = "Root_N-1R-inRing_1R->S_N-2R->H",
    kinetics = ArrheniusBM(A=(74997.8,'m^3/(mol*s)'), n=0.851454, w0=(129.812,'kJ/mol'), E0=(15.7351,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1804158490422643, var=5.510419329887811, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_1R->S_N-2R->H',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_1R->S_N-2R->H
    Total Standard Deviation in ln(k): 5.159277882615679"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_1R->S_N-2R->H
Total Standard Deviation in ln(k): 5.159277882615679""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_1R->S_N-2R->H
Total Standard Deviation in ln(k): 5.159277882615679
""",
)

entry(
    index = 14,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O",
    kinetics = ArrheniusBM(A=(5.16615e+08,'m^3/(mol*s)'), n=-0.461405, w0=(166.746,'kJ/mol'), E0=(102.766,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.31134646001281885, var=17.59409230874583, Tref=1000.0, N=63, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O',), comment="""BM rule fitted to 63 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O
    Total Standard Deviation in ln(k): 9.191201444287564"""),
    rank = 11,
    shortDesc = """BM rule fitted to 63 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O
Total Standard Deviation in ln(k): 9.191201444287564""",
    longDesc = 
"""
BM rule fitted to 63 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O
Total Standard Deviation in ln(k): 9.191201444287564
""",
)

entry(
    index = 15,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O",
    kinetics = ArrheniusBM(A=(6.26336e+06,'m^3/(mol*s)'), n=-0.0335823, w0=(194.13,'kJ/mol'), E0=(51.9498,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.046466339440430854, var=16.14286745529383, Tref=1000.0, N=268, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O',), comment="""BM rule fitted to 268 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O
    Total Standard Deviation in ln(k): 8.171411766208719"""),
    rank = 11,
    shortDesc = """BM rule fitted to 268 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O
Total Standard Deviation in ln(k): 8.171411766208719""",
    longDesc = 
"""
BM rule fitted to 268 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O
Total Standard Deviation in ln(k): 8.171411766208719
""",
)

entry(
    index = 16,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H",
    kinetics = ArrheniusBM(A=(6.37132e+08,'m^3/(mol*s)'), n=-0.255145, w0=(205.5,'kJ/mol'), E0=(122.254,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1699601053870783, var=11.538436631183735, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H',), comment="""BM rule fitted to 7 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H
    Total Standard Deviation in ln(k): 9.749337367905802"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 9.749337367905802""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 9.749337367905802
""",
)

entry(
    index = 17,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H",
    kinetics = ArrheniusBM(A=(4.42591e+07,'m^3/(mol*s)'), n=0.134893, w0=(205.5,'kJ/mol'), E0=(82.0945,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08996106897615407, var=0.25047067121000666, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H',), comment="""BM rule fitted to 7 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H
    Total Standard Deviation in ln(k): 1.2293435027110153"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 1.2293435027110153""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 1.2293435027110153
""",
)

entry(
    index = 18,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_Sp-3R!H-1R",
    kinetics = ArrheniusBM(A=(1.64652e+10,'m^3/(mol*s)'), n=-0.959714, w0=(173,'kJ/mol'), E0=(33.7245,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09367024940708513, var=0.36713088592648746, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_Sp-3R!H-1R',), comment="""BM rule fitted to 4 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_Sp-3R!H-1R
    Total Standard Deviation in ln(k): 1.4500479636729366"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_Sp-3R!H-1R
Total Standard Deviation in ln(k): 1.4500479636729366""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_Sp-3R!H-1R
Total Standard Deviation in ln(k): 1.4500479636729366
""",
)

entry(
    index = 19,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R",
    kinetics = ArrheniusBM(A=(1.01742e+09,'m^3/(mol*s)'), n=-0.57745, w0=(219.386,'kJ/mol'), E0=(118.162,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.015767425329430415, var=0.22802234773055902, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R',), comment="""BM rule fitted to 6 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R
    Total Standard Deviation in ln(k): 0.9969114377560627"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R
Total Standard Deviation in ln(k): 0.9969114377560627""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R
Total Standard Deviation in ln(k): 0.9969114377560627
""",
)

entry(
    index = 20,
    label = "Root_N-1R-inRing_1R->S_2R->H_Ext-1S-R",
    kinetics = Arrhenius(A=(1.14319e+09,'m^3/(mol*s)'), n=0.324378, Ea=(0.0367173,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_1R->S_2R->H_Ext-1S-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->S_2R->H_Ext-1S-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->S_2R->H_Ext-1S-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_1R->S_2R->H_Ext-1S-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-1R-inRing_1R->S_N-2R->H_2BrCClFNOS->S",
    kinetics = ArrheniusBM(A=(7.78803e+06,'m^3/(mol*s)'), n=0.612733, w0=(125.417,'kJ/mol'), E0=(62.7083,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.477116970636756, var=26.278104303738633, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_1R->S_N-2R->H_2BrCClFNOS->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_1R->S_N-2R->H_2BrCClFNOS->S
    Total Standard Deviation in ln(k): 19.01318253341586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_1R->S_N-2R->H_2BrCClFNOS->S
Total Standard Deviation in ln(k): 19.01318253341586""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_1R->S_N-2R->H_2BrCClFNOS->S
Total Standard Deviation in ln(k): 19.01318253341586
""",
)

entry(
    index = 22,
    label = "Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S",
    kinetics = ArrheniusBM(A=(24544.6,'m^3/(mol*s)'), n=0.916744, w0=(135.417,'kJ/mol'), E0=(10.2993,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.057973724940964165, var=1.6403914587121167, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S
    Total Standard Deviation in ln(k): 2.713282561539479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S
Total Standard Deviation in ln(k): 2.713282561539479""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S
Total Standard Deviation in ln(k): 2.713282561539479
""",
)

entry(
    index = 23,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_2R->Cl",
    kinetics = Arrhenius(A=(4.5295e+12,'m^3/(mol*s)'), n=-2.86943, Ea=(5.69961,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_2R->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_2R->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_2R->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_2R->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl",
    kinetics = ArrheniusBM(A=(4.50978e+08,'m^3/(mol*s)'), n=-0.442161, w0=(167.242,'kJ/mol'), E0=(102.766,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.34574001796579495, var=17.839219627242734, Tref=1000.0, N=62, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl',), comment="""BM rule fitted to 62 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl
    Total Standard Deviation in ln(k): 9.335992894434938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 62 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl
Total Standard Deviation in ln(k): 9.335992894434938""",
    longDesc = 
"""
BM rule fitted to 62 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl
Total Standard Deviation in ln(k): 9.335992894434938
""",
)

entry(
    index = 25,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F",
    kinetics = ArrheniusBM(A=(1230.28,'m^3/(mol*s)'), n=0.751162, w0=(261.734,'kJ/mol'), E0=(26.1734,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04197599604170358, var=21.903839144633924, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F
    Total Standard Deviation in ln(k): 9.4879357214572"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F
Total Standard Deviation in ln(k): 9.4879357214572""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F
Total Standard Deviation in ln(k): 9.4879357214572
""",
)

entry(
    index = 26,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F",
    kinetics = ArrheniusBM(A=(1.49398e+07,'m^3/(mol*s)'), n=-0.113515, w0=(191.509,'kJ/mol'), E0=(54.7899,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13781732611752318, var=15.9637147235311, Tref=1000.0, N=258, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F',), comment="""BM rule fitted to 258 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F
    Total Standard Deviation in ln(k): 8.356117041415592"""),
    rank = 11,
    shortDesc = """BM rule fitted to 258 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F
Total Standard Deviation in ln(k): 8.356117041415592""",
    longDesc = 
"""
BM rule fitted to 258 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F
Total Standard Deviation in ln(k): 8.356117041415592
""",
)

entry(
    index = 27,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H",
    kinetics = ArrheniusBM(A=(4.43148e+10,'m^3/(mol*s)'), n=-1.25313, w0=(205.5,'kJ/mol'), E0=(121.638,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18115675647398793, var=8.027106318125233, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H',), comment="""BM rule fitted to 4 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H
    Total Standard Deviation in ln(k): 6.1350128973174085"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H
Total Standard Deviation in ln(k): 6.1350128973174085""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H
Total Standard Deviation in ln(k): 6.1350128973174085
""",
)

entry(
    index = 28,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing",
    kinetics = ArrheniusBM(A=(2.54203e+07,'m^3/(mol*s)'), n=0.402566, w0=(206.286,'kJ/mol'), E0=(118.197,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.45005049446590045, var=2.2815832761944006, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing
    Total Standard Deviation in ln(k): 4.158914571387202"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing
Total Standard Deviation in ln(k): 4.158914571387202""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing
Total Standard Deviation in ln(k): 4.158914571387202
""",
)

entry(
    index = 29,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_N-5R!H-inRing",
    kinetics = Arrhenius(A=(249317,'m^3/(mol*s)'), n=0.611, Ea=(-1.82422,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_N-5R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_N-5R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_N-5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_N-5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.70417e+07,'m^3/(mol*s)'), n=0.13817, w0=(205.5,'kJ/mol'), E0=(78.8935,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.009807516180730703, var=0.006570527800035662, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.18714340459659667"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.18714340459659667""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.18714340459659667
""",
)

entry(
    index = 31,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5.15096e+07,'m^3/(mol*s)'), n=0.183576, w0=(205.5,'kJ/mol'), E0=(85.895,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1489920501984019, var=0.10041008290210698, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 1.0096033162086009"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.0096033162086009""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.0096033162086009
""",
)

entry(
    index = 32,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_Sp-3R!H-1R_2C-inRing",
    kinetics = Arrhenius(A=(5e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_Sp-3R!H-1R_2C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_Sp-3R!H-1R_2C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_Sp-3R!H-1R_2C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_Sp-3R!H-1R_2C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_Sp-3R!H-1R_N-2C-inRing",
    kinetics = ArrheniusBM(A=(3.13485e+11,'m^3/(mol*s)'), n=-1.32812, w0=(173,'kJ/mol'), E0=(92.2881,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09531566310486411, var=0.30900434361871115, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_Sp-3R!H-1R_N-2C-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_Sp-3R!H-1R_N-2C-inRing
    Total Standard Deviation in ln(k): 1.3538819158032345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_Sp-3R!H-1R_N-2C-inRing
Total Standard Deviation in ln(k): 1.3538819158032345""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_Sp-3R!H-1R_N-2C-inRing
Total Standard Deviation in ln(k): 1.3538819158032345
""",
)

entry(
    index = 34,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.24093e+09,'m^3/(mol*s)'), n=-0.617306, w0=(220.603,'kJ/mol'), E0=(114.086,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.45474451003024274, var=0.5612362823526373, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R
    Total Standard Deviation in ln(k): 2.6444355581190178"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R
Total Standard Deviation in ln(k): 2.6444355581190178""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R
Total Standard Deviation in ln(k): 2.6444355581190178
""",
)

entry(
    index = 35,
    label = "Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S_Ext-1S-R",
    kinetics = ArrheniusBM(A=(28641.6,'m^3/(mol*s)'), n=0.894523, w0=(136,'kJ/mol'), E0=(50.2285,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05017112222653621, var=1.0341867654731403, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S_Ext-1S-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S_Ext-1S-R
    Total Standard Deviation in ln(k): 2.164772903676257"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S_Ext-1S-R
Total Standard Deviation in ln(k): 2.164772903676257""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S_Ext-1S-R
Total Standard Deviation in ln(k): 2.164772903676257
""",
)

entry(
    index = 36,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R",
    kinetics = ArrheniusBM(A=(2.78448e+07,'m^3/(mol*s)'), n=-0.112511, w0=(169.812,'kJ/mol'), E0=(111.03,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6092127073560322, var=18.856248346874803, Tref=1000.0, N=56, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R',), comment="""BM rule fitted to 56 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R
    Total Standard Deviation in ln(k): 10.236003071601752"""),
    rank = 11,
    shortDesc = """BM rule fitted to 56 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R
Total Standard Deviation in ln(k): 10.236003071601752""",
    longDesc = 
"""
BM rule fitted to 56 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R
Total Standard Deviation in ln(k): 10.236003071601752
""",
)

entry(
    index = 37,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_2BrCFHNO->H",
    kinetics = Arrhenius(A=(1.62e+08,'m^3/(mol*s)'), n=0, Ea=(0.6276,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_2BrCFHNO->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_2BrCFHNO->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_2BrCFHNO->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_2BrCFHNO->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H",
    kinetics = ArrheniusBM(A=(1.3006e+07,'m^3/(mol*s)'), n=0.0810435, w0=(139.65,'kJ/mol'), E0=(51.2476,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4851769162695223, var=0.5882539652615187, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H
    Total Standard Deviation in ln(k): 2.756623495975046"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H
Total Standard Deviation in ln(k): 2.756623495975046""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H
Total Standard Deviation in ln(k): 2.756623495975046
""",
)

entry(
    index = 39,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(236.922,'m^3/(mol*s)'), n=0.900639, w0=(262.795,'kJ/mol'), E0=(26.2795,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.052425505559763344, var=22.07316827243216, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 9.550386858162236"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 9.550386858162236""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 9.550386858162236
""",
)

entry(
    index = 40,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_3R!H->O",
    kinetics = Arrhenius(A=(1e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_3R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_3R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_N-3R!H->O",
    kinetics = ArrheniusBM(A=(1.1418e+08,'m^3/(mol*s)'), n=-0.286048, w0=(261.275,'kJ/mol'), E0=(95.4087,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.16835930134859, var=3.4959148572568224, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_N-3R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_N-3R!H->O
    Total Standard Deviation in ln(k): 6.683902630017838"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_N-3R!H->O
Total Standard Deviation in ln(k): 6.683902630017838""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_N-3R!H->O
Total Standard Deviation in ln(k): 6.683902630017838
""",
)

entry(
    index = 42,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H",
    kinetics = ArrheniusBM(A=(1.25202e+07,'m^3/(mol*s)'), n=0.204879, w0=(225.286,'kJ/mol'), E0=(71.6406,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04356029315042632, var=4.197272745869413, Tref=1000.0, N=68, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H',), comment="""BM rule fitted to 68 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H
    Total Standard Deviation in ln(k): 4.216598169109168"""),
    rank = 11,
    shortDesc = """BM rule fitted to 68 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H
Total Standard Deviation in ln(k): 4.216598169109168""",
    longDesc = 
"""
BM rule fitted to 68 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H
Total Standard Deviation in ln(k): 4.216598169109168
""",
)

entry(
    index = 43,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H",
    kinetics = ArrheniusBM(A=(1.53427e+07,'m^3/(mol*s)'), n=-0.165314, w0=(179.421,'kJ/mol'), E0=(12.5044,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.051318217715195256, var=16.56165033622972, Tref=1000.0, N=190, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H',), comment="""BM rule fitted to 190 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H
    Total Standard Deviation in ln(k): 8.287411637722004"""),
    rank = 11,
    shortDesc = """BM rule fitted to 190 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H
Total Standard Deviation in ln(k): 8.287411637722004""",
    longDesc = 
"""
BM rule fitted to 190 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H
Total Standard Deviation in ln(k): 8.287411637722004
""",
)

entry(
    index = 44,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.0097e+07,'m^3/(mol*s)'), n=0.00242488, w0=(205.5,'kJ/mol'), E0=(59.197,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19645913843758778, var=2.298999650560591, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 3.5332859593141843"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.5332859593141843""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.5332859593141843
""",
)

entry(
    index = 45,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing_Sp-3R!H-1R",
    kinetics = Arrhenius(A=(9.42e+06,'m^3/(mol*s)'), n=0.408, Ea=(0.008368,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing_Sp-3R!H-1R',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing_Sp-3R!H-1R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing_Sp-3R!H-1R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing_Sp-3R!H-1R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing_N-Sp-3R!H-1R",
    kinetics = Arrhenius(A=(4.27e+07,'m^3/(mol*s)'), n=0.338, Ea=(-0.661072,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing_N-Sp-3R!H-1R',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing_N-Sp-3R!H-1R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing_N-Sp-3R!H-1R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-3R!H-R_5R!H-inRing_N-Sp-3R!H-1R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_Sp-3R!H-1R",
    kinetics = ArrheniusBM(A=(1.19686e+08,'m^3/(mol*s)'), n=-0.0437934, w0=(205.5,'kJ/mol'), E0=(76.7788,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4766074718582756, var=1.3864689554600855, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_Sp-3R!H-1R',), comment="""BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_Sp-3R!H-1R
    Total Standard Deviation in ln(k): 3.55805001648571"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_Sp-3R!H-1R
Total Standard Deviation in ln(k): 3.55805001648571""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_Sp-3R!H-1R
Total Standard Deviation in ln(k): 3.55805001648571
""",
)

entry(
    index = 48,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_N-Sp-3R!H-1R",
    kinetics = ArrheniusBM(A=(2.45117e+07,'m^3/(mol*s)'), n=0.200434, w0=(235.808,'kJ/mol'), E0=(117.904,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03522532759747092, var=0.010560692695553773, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_N-Sp-3R!H-1R',), comment="""BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_N-Sp-3R!H-1R
    Total Standard Deviation in ln(k): 0.2945229114894717"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_N-Sp-3R!H-1R
Total Standard Deviation in ln(k): 0.2945229114894717""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_N-Sp-3R!H-1R
Total Standard Deviation in ln(k): 0.2945229114894717
""",
)

entry(
    index = 49,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_Sp-3R!H-1R_N-2C-inRing_Ext-2C-R",
    kinetics = Arrhenius(A=(1.668e+09,'m^3/(mol*s)'), n=-0.7, Ea=(-2.092,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_Sp-3R!H-1R_N-2C-inRing_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_Sp-3R!H-1R_N-2C-inRing_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_Sp-3R!H-1R_N-2C-inRing_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_Sp-3R!H-1R_N-2C-inRing_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_2C-inRing",
    kinetics = ArrheniusBM(A=(1.6752e+09,'m^3/(mol*s)'), n=-0.659797, w0=(245.546,'kJ/mol'), E0=(122.773,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.032978833860298, var=2.2202828217281585, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_2C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_2C-inRing
    Total Standard Deviation in ln(k): 5.582602458105897"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_2C-inRing
Total Standard Deviation in ln(k): 5.582602458105897""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_2C-inRing
Total Standard Deviation in ln(k): 5.582602458105897
""",
)

entry(
    index = 51,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=8.79914e-10, w0=(195.66,'kJ/mol'), E0=(79.2224,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 52,
    label = "Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S_Ext-1S-R_3R!H->C",
    kinetics = ArrheniusBM(A=(15609.6,'m^3/(mol*s)'), n=0.89762, w0=(140.553,'kJ/mol'), E0=(70.2764,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.060869374039990834, var=7.222237291452136e-35, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S_Ext-1S-R_3R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S_Ext-1S-R_3R!H->C
    Total Standard Deviation in ln(k): 0.1529381257286202"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S_Ext-1S-R_3R!H->C
Total Standard Deviation in ln(k): 0.1529381257286202""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S_Ext-1S-R_3R!H->C
Total Standard Deviation in ln(k): 0.1529381257286202
""",
)

entry(
    index = 53,
    label = "Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S_Ext-1S-R_N-3R!H->C",
    kinetics = ArrheniusBM(A=(71187.7,'m^3/(mol*s)'), n=0.889878, w0=(136,'kJ/mol'), E0=(61.2718,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3723820346018363, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S_Ext-1S-R_N-3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S_Ext-1S-R_N-3R!H->C
    Total Standard Deviation in ln(k): 0.9356332527684328"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S_Ext-1S-R_N-3R!H->C
Total Standard Deviation in ln(k): 0.9356332527684328""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S_Ext-1S-R_N-3R!H->C
Total Standard Deviation in ln(k): 0.9356332527684328
""",
)

entry(
    index = 54,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C",
    kinetics = ArrheniusBM(A=(2.13315e+10,'m^3/(mol*s)'), n=-0.939036, w0=(170.867,'kJ/mol'), E0=(32.7426,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09451439199234371, var=7.30410689950207, Tref=1000.0, N=30, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C',), comment="""BM rule fitted to 30 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C
    Total Standard Deviation in ln(k): 5.655492671978827"""),
    rank = 11,
    shortDesc = """BM rule fitted to 30 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C
Total Standard Deviation in ln(k): 5.655492671978827""",
    longDesc = 
"""
BM rule fitted to 30 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C
Total Standard Deviation in ln(k): 5.655492671978827
""",
)

entry(
    index = 55,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C",
    kinetics = ArrheniusBM(A=(1.40218e-24,'m^3/(mol*s)'), n=8.85538, w0=(168.596,'kJ/mol'), E0=(5.65985,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06387528278828335, var=17.584355363398043, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C',), comment="""BM rule fitted to 26 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C
    Total Standard Deviation in ln(k): 8.567087406040867"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C
Total Standard Deviation in ln(k): 8.567087406040867""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C
Total Standard Deviation in ln(k): 8.567087406040867
""",
)

entry(
    index = 56,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H_2CNO->C",
    kinetics = ArrheniusBM(A=(6.82467e+07,'m^3/(mol*s)'), n=-0.000194194, w0=(194.01,'kJ/mol'), E0=(162.636,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.305460834090209e-17, var=0.1195344065457376, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H_2CNO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H_2CNO->C
    Total Standard Deviation in ln(k): 0.6931120579847638"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H_2CNO->C
Total Standard Deviation in ln(k): 0.6931120579847638""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H_2CNO->C
Total Standard Deviation in ln(k): 0.6931120579847638
""",
)

entry(
    index = 57,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H_N-2CNO->C",
    kinetics = ArrheniusBM(A=(3.66032e+06,'m^3/(mol*s)'), n=0.234906, w0=(103.41,'kJ/mol'), E0=(32.1271,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4332844885399143, var=0.4208523669671854, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H_N-2CNO->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H_N-2CNO->C
    Total Standard Deviation in ln(k): 2.3891889908232202"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H_N-2CNO->C
Total Standard Deviation in ln(k): 2.3891889908232202""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H_N-2CNO->C
Total Standard Deviation in ln(k): 2.3891889908232202
""",
)

entry(
    index = 58,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(0.133312,'m^3/(mol*s)'), n=1.5787, w0=(268.207,'kJ/mol'), E0=(26.8207,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.29724552584910935, var=10.143186233143348, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 7.1316023524308285"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 7.1316023524308285""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 7.1316023524308285
""",
)

entry(
    index = 59,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(2.35378e+06,'m^3/(mol*s)'), n=0.0927772, w0=(255.578,'kJ/mol'), E0=(169.117,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06576330345823801, var=0.7640665399636376, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 1.9175914000733427"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.9175914000733427""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.9175914000733427
""",
)

entry(
    index = 60,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_N-3R!H->O_3BrCClFILiNPSSi->F",
    kinetics = Arrhenius(A=(1.29467e+07,'m^3/(mol*s)'), n=-0.0161041, Ea=(-2.3334,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_N-3R!H->O_3BrCClFILiNPSSi->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_N-3R!H->O_3BrCClFILiNPSSi->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_N-3R!H->O_3BrCClFILiNPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_N-3R!H->O_3BrCClFILiNPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_N-3R!H->O_N-3BrCClFILiNPSSi->F",
    kinetics = Arrhenius(A=(5e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_N-3R!H->O_N-3BrCClFILiNPSSi->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_N-3R!H->O_N-3BrCClFILiNPSSi->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_N-3R!H->O_N-3BrCClFILiNPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_N-3R!H->O_N-3BrCClFILiNPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_2R->N",
    kinetics = Arrhenius(A=(2.8e+06,'m^3/(mol*s)'), n=0.493, Ea=(-1.2301,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_2R->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_2R->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_2R->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_2R->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N",
    kinetics = ArrheniusBM(A=(1.79784e+07,'m^3/(mol*s)'), n=0.1539, w0=(225.239,'kJ/mol'), E0=(91.8391,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03956100980277158, var=4.474781559911513, Tref=1000.0, N=67, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N',), comment="""BM rule fitted to 67 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N
    Total Standard Deviation in ln(k): 4.340151851193956"""),
    rank = 11,
    shortDesc = """BM rule fitted to 67 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N
Total Standard Deviation in ln(k): 4.340151851193956""",
    longDesc = 
"""
BM rule fitted to 67 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N
Total Standard Deviation in ln(k): 4.340151851193956
""",
)

entry(
    index = 64,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N",
    kinetics = Arrhenius(A=(6.64248e+07,'m^3/(mol*s)'), n=-0.458825, Ea=(-23.0862,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-1.3798798614170067, var=15.937746163118069, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N
    Total Standard Deviation in ln(k): 11.470359626681033"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N
Total Standard Deviation in ln(k): 11.470359626681033""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N
Total Standard Deviation in ln(k): 11.470359626681033
""",
)

entry(
    index = 65,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N",
    kinetics = ArrheniusBM(A=(6.10916e+06,'m^3/(mol*s)'), n=-0.0501019, w0=(182.411,'kJ/mol'), E0=(11.3383,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04717870993322306, var=16.278791004781084, Tref=1000.0, N=184, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N',), comment="""BM rule fitted to 184 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N
    Total Standard Deviation in ln(k): 8.207040838106929"""),
    rank = 11,
    shortDesc = """BM rule fitted to 184 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N
Total Standard Deviation in ln(k): 8.207040838106929""",
    longDesc = 
"""
BM rule fitted to 184 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N
Total Standard Deviation in ln(k): 8.207040838106929
""",
)

entry(
    index = 66,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_Ext-3R!H-R",
    kinetics = Arrhenius(A=(4.55633e+09,'m^3/(mol*s)'), n=-0.593907, Ea=(8.76765,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 67,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_Sp-3R!H=1R",
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_Sp-3R!H=1R',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_Sp-3R!H=1R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_Sp-3R!H=1R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_Sp-3R!H=1R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_N-Sp-3R!H=1R",
    kinetics = Arrhenius(A=(1.5763e+09,'m^3/(mol*s)'), n=-0.786601, Ea=(3.16385,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_N-Sp-3R!H=1R',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_N-Sp-3R!H=1R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_N-Sp-3R!H=1R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-1R-R_Ext-5R!H-R_Int-6R!H-4R!H_Ext-4R!H-R_N-Sp-3R!H=1R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 69,
    label = "Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_N-Sp-3R!H-1R_Ext-4R!H-R",
    kinetics = Arrhenius(A=(1.25e+07,'m^3/(mol*s)'), n=0.284, Ea=(-0.64852,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_N-Sp-3R!H-1R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_N-Sp-3R!H-1R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_N-Sp-3R!H-1R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_2BrCClFHNS->H_Ext-1R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-1R-R_Ext-5R!H-R_N-Sp-3R!H-1R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing_Sp-4R!H-2C",
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing_Sp-4R!H-2C',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing_Sp-4R!H-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing_Sp-4R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing_Sp-4R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing_N-Sp-4R!H-2C",
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing_N-Sp-4R!H-2C',), comment="""BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing_N-Sp-4R!H-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing_N-Sp-4R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R-inRing_N-2R->O_N-2BrCClFHNS->H_Ext-1R-R_N-Sp-3R!H-1R_Ext-2C-R_N-2C-inRing_N-Sp-4R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S_Ext-1S-R_3R!H->C_Ext-2CO-R",
    kinetics = ArrheniusBM(A=(15609.6,'m^3/(mol*s)'), n=0.89762, w0=(139.905,'kJ/mol'), E0=(69.9523,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6642490346951677, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S_Ext-1S-R_3R!H->C_Ext-2CO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S_Ext-1S-R_3R!H->C_Ext-2CO-R
    Total Standard Deviation in ln(k): 1.6689674238572052"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S_Ext-1S-R_3R!H->C_Ext-2CO-R
Total Standard Deviation in ln(k): 1.6689674238572052""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_1R->S_N-2R->H_N-2BrCClFNOS->S_Ext-1S-R_3R!H->C_Ext-2CO-R
Total Standard Deviation in ln(k): 1.6689674238572052
""",
)

entry(
    index = 73,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.33141e+10,'m^3/(mol*s)'), n=-0.952988, w0=(181.104,'kJ/mol'), E0=(58.2512,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09281701987240898, var=7.533327490483813, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R',), comment="""BM rule fitted to 24 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 5.735586480536456"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 5.735586480536456""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 5.735586480536456
""",
)

entry(
    index = 74,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_2BrCFHNO->N",
    kinetics = Arrhenius(A=(1.59771e+09,'m^3/(mol*s)'), n=-0.461068, Ea=(1.75473,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_2BrCFHNO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_2BrCFHNO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_2BrCFHNO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_2BrCFHNO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N",
    kinetics = ArrheniusBM(A=(5.08664e+07,'m^3/(mol*s)'), n=-0.238046, w0=(139.332,'kJ/mol'), E0=(52.8317,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.062153532237387905, var=1.7413961984315292, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N
    Total Standard Deviation in ln(k): 2.8016525900648586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N
Total Standard Deviation in ln(k): 2.8016525900648586""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N
Total Standard Deviation in ln(k): 2.8016525900648586
""",
)

entry(
    index = 76,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_3BrClFILiNOPSSi->Cl",
    kinetics = ArrheniusBM(A=(2.54516e+11,'m^3/(mol*s)'), n=-2.9831, w0=(229.5,'kJ/mol'), E0=(94.7569,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6248817156546443, var=1.2163224389751158e-05, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_3BrClFILiNOPSSi->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_3BrClFILiNOPSSi->Cl
    Total Standard Deviation in ln(k): 1.5770462388199928"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_3BrClFILiNOPSSi->Cl
Total Standard Deviation in ln(k): 1.5770462388199928""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_3BrClFILiNOPSSi->Cl
Total Standard Deviation in ln(k): 1.5770462388199928
""",
)

entry(
    index = 77,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl",
    kinetics = Arrhenius(A=(590126,'m^3/(mol*s)'), n=0.15517, Ea=(18.1581,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=5.3782472211976255, var=19.363084653174262, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl',), comment="""BM rule fitted to 24 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl
    Total Standard Deviation in ln(k): 22.334721002724027"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl
Total Standard Deviation in ln(k): 22.334721002724027""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl
Total Standard Deviation in ln(k): 22.334721002724027
""",
)

entry(
    index = 78,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H_N-2CNO->C_2NO->N",
    kinetics = ArrheniusBM(A=(3.65367e+06,'m^3/(mol*s)'), n=0.2352, w0=(102.495,'kJ/mol'), E0=(51.2476,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4709502203626317, var=0.4813240235668652, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H_N-2CNO->C_2NO->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H_N-2CNO->C_2NO->N
    Total Standard Deviation in ln(k): 2.5741274836274104"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H_N-2CNO->C_2NO->N
Total Standard Deviation in ln(k): 2.5741274836274104""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H_N-2CNO->C_2NO->N
Total Standard Deviation in ln(k): 2.5741274836274104
""",
)

entry(
    index = 79,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H_N-2CNO->C_N-2NO->N",
    kinetics = Arrhenius(A=(1.57e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H_N-2CNO->C_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H_N-2CNO->C_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H_N-2CNO->C_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_N-2BrCFHNO->H_N-2CNO->C_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_3R!H->C",
    kinetics = Arrhenius(A=(5.35143,'m^3/(mol*s)'), n=0.941405, Ea=(15.3812,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_3R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_3R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_3R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_3R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 81,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C",
    kinetics = ArrheniusBM(A=(4.69581,'m^3/(mol*s)'), n=1.19479, w0=(270.045,'kJ/mol'), E0=(27.0045,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08006358164486065, var=18.408909432341083, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C
    Total Standard Deviation in ln(k): 8.802601920617528"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C
Total Standard Deviation in ln(k): 8.802601920617528""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C
Total Standard Deviation in ln(k): 8.802601920617528
""",
)

entry(
    index = 82,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = Arrhenius(A=(1.54647e+06,'m^3/(mol*s)'), n=0.239176, Ea=(-1.29422,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 83,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_6BrClFILiNOPSSi->O",
    kinetics = Arrhenius(A=(3.96079e+06,'m^3/(mol*s)'), n=-0.0332618, Ea=(0.843915,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_6BrClFILiNOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_6BrClFILiNOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_6BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_6BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_N-6BrClFILiNOPSSi->O",
    kinetics = Arrhenius(A=(577559,'m^3/(mol*s)'), n=0.234749, Ea=(-3.42706,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_N-6BrClFILiNOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_N-6BrClFILiNOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_N-6BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_N-6R!H->C_N-6BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 85,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_2BrCClH->H",
    kinetics = ArrheniusBM(A=(1.03472e+06,'m^3/(mol*s)'), n=0.001125, w0=(224.272,'kJ/mol'), E0=(166.021,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3774142242586176, var=47.94959741791935, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_2BrCClH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_2BrCClH->H
    Total Standard Deviation in ln(k): 14.830194859219086"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_2BrCClH->H
Total Standard Deviation in ln(k): 14.830194859219086""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_2BrCClH->H
Total Standard Deviation in ln(k): 14.830194859219086
""",
)

entry(
    index = 86,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H",
    kinetics = ArrheniusBM(A=(1.87642e+07,'m^3/(mol*s)'), n=0.148601, w0=(225.269,'kJ/mol'), E0=(91.8388,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04173533861636665, var=4.45676849056157, Tref=1000.0, N=65, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H',), comment="""BM rule fitted to 65 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H
    Total Standard Deviation in ln(k): 4.337070885127159"""),
    rank = 11,
    shortDesc = """BM rule fitted to 65 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H
Total Standard Deviation in ln(k): 4.337070885127159""",
    longDesc = 
"""
BM rule fitted to 65 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H
Total Standard Deviation in ln(k): 4.337070885127159
""",
)

entry(
    index = 87,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R",
    kinetics = ArrheniusBM(A=(5.5125e+21,'m^3/(mol*s)'), n=-4.51523, w0=(124.9,'kJ/mol'), E0=(64.4424,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.813179805094916, var=34.01876024549015, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R
    Total Standard Deviation in ln(k): 13.735903665661231"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R
Total Standard Deviation in ln(k): 13.735903665661231""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R
Total Standard Deviation in ln(k): 13.735903665661231
""",
)

entry(
    index = 88,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl",
    kinetics = ArrheniusBM(A=(1.413e+14,'m^3/(mol*s)'), n=-2.30694, w0=(178.263,'kJ/mol'), E0=(121.265,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1176310964385151, var=14.080537987722115, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl',), comment="""BM rule fitted to 25 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl
    Total Standard Deviation in ln(k): 7.818132031994865"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl
Total Standard Deviation in ln(k): 7.818132031994865""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl
Total Standard Deviation in ln(k): 7.818132031994865
""",
)

entry(
    index = 89,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl",
    kinetics = ArrheniusBM(A=(5.94966e+06,'m^3/(mol*s)'), n=-0.0465229, w0=(183.063,'kJ/mol'), E0=(10.9499,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04666935970046159, var=16.304148455096335, Tref=1000.0, N=159, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl',), comment="""BM rule fitted to 159 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl
    Total Standard Deviation in ln(k): 8.21205833600957"""),
    rank = 11,
    shortDesc = """BM rule fitted to 159 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl
Total Standard Deviation in ln(k): 8.21205833600957""",
    longDesc = 
"""
BM rule fitted to 159 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl
Total Standard Deviation in ln(k): 8.21205833600957
""",
)

entry(
    index = 90,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.68719e+10,'m^3/(mol*s)'), n=-0.995455, w0=(179,'kJ/mol'), E0=(38.8796,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12428785886025102, var=5.713038066816998, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C
    Total Standard Deviation in ln(k): 5.103991297060439"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 5.103991297060439""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 5.103991297060439
""",
)

entry(
    index = 91,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(6.38111e+07,'m^3/(mol*s)'), n=0.24222, w0=(194.57,'kJ/mol'), E0=(106.538,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6002510304323743, var=9.755007314864045, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 7.769558905478082"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 7.769558905478082""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 7.769558905478082
""",
)

entry(
    index = 92,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N_Ext-2CHO-R",
    kinetics = ArrheniusBM(A=(1.50084e+08,'m^3/(mol*s)'), n=-0.433099, w0=(144.309,'kJ/mol'), E0=(61.6766,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.783043769402872, var=2.1225045148933583, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N_Ext-2CHO-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N_Ext-2CHO-R
    Total Standard Deviation in ln(k): 4.888108660643608"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N_Ext-2CHO-R
Total Standard Deviation in ln(k): 4.888108660643608""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N_Ext-2CHO-R
Total Standard Deviation in ln(k): 4.888108660643608
""",
)

entry(
    index = 93,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_3NO-u0",
    kinetics = ArrheniusBM(A=(8.77076e+07,'m^3/(mol*s)'), n=-0.311111, w0=(90.6667,'kJ/mol'), E0=(17.092,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.4638998721139425, var=15.077123263425959, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_3NO-u0',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_3NO-u0
    Total Standard Deviation in ln(k): 16.487506273803685"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_3NO-u0
Total Standard Deviation in ln(k): 16.487506273803685""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_3NO-u0
Total Standard Deviation in ln(k): 16.487506273803685
""",
)

entry(
    index = 94,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0",
    kinetics = Arrhenius(A=(430176,'m^3/(mol*s)'), n=0.179242, Ea=(20.7919,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=5.223862965053944, var=16.841640263624704, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0',), comment="""BM rule fitted to 21 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0
    Total Standard Deviation in ln(k): 21.352429420670706"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0
Total Standard Deviation in ln(k): 21.352429420670706""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0
Total Standard Deviation in ln(k): 21.352429420670706
""",
)

entry(
    index = 95,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_7R!H->C",
    kinetics = Arrhenius(A=(1489.88,'m^3/(mol*s)'), n=0.313518, Ea=(15.4794,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 96,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(365.575,'m^3/(mol*s)'), n=0.735198, w0=(264.176,'kJ/mol'), E0=(26.4176,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3796940110716313, var=23.2190137010019, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 10.614043909185305"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 10.614043909185305""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 10.614043909185305
""",
)

entry(
    index = 97,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.70428e+07,'m^3/(mol*s)'), n=0.160666, w0=(225.408,'kJ/mol'), E0=(91.8388,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05933313340033892, var=4.493721315507638, Tref=1000.0, N=63, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R',), comment="""BM rule fitted to 63 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R
    Total Standard Deviation in ln(k): 4.398795684459797"""),
    rank = 11,
    shortDesc = """BM rule fitted to 63 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R
Total Standard Deviation in ln(k): 4.398795684459797""",
    longDesc = 
"""
BM rule fitted to 63 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R
Total Standard Deviation in ln(k): 4.398795684459797
""",
)

entry(
    index = 98,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R_Ext-3R!H-R",
    kinetics = Arrhenius(A=(505,'m^3/(mol*s)'), n=0, Ea=(-145.147,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 99,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R_Ext-2R-R",
    kinetics = Arrhenius(A=(2.63e+08,'m^3/(mol*s)'), n=-1.1, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 100,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R_3R!H->N",
    kinetics = Arrhenius(A=(2.4e+06,'m^3/(mol*s)'), n=0.085, Ea=(3.35975,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R_3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R_3R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 101,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R_N-3R!H->N",
    kinetics = ArrheniusBM(A=(1.28974e+10,'m^3/(mol*s)'), n=-0.808938, w0=(133.259,'kJ/mol'), E0=(44.7305,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09518018919310234, var=3.7871649839624, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R_N-3R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R_N-3R!H->N
    Total Standard Deviation in ln(k): 4.14048891195987"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R_N-3R!H->N
Total Standard Deviation in ln(k): 4.14048891195987""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_1BrCClN->N_Ext-1N-R_N-3R!H->N
Total Standard Deviation in ln(k): 4.14048891195987
""",
)

entry(
    index = 102,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R",
    kinetics = ArrheniusBM(A=(4.67575e+13,'m^3/(mol*s)'), n=-2.1574, w0=(175.883,'kJ/mol'), E0=(121.146,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1730539431119633, var=14.622823507127759, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R',), comment="""BM rule fitted to 24 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R
    Total Standard Deviation in ln(k): 8.100875865886826"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R
Total Standard Deviation in ln(k): 8.100875865886826""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R
Total Standard Deviation in ln(k): 8.100875865886826
""",
)

entry(
    index = 103,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R",
    kinetics = ArrheniusBM(A=(5.7149e+06,'m^3/(mol*s)'), n=-0.0425977, w0=(183.079,'kJ/mol'), E0=(9.2489,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05184000896009764, var=16.31233557266732, Tref=1000.0, N=156, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R',), comment="""BM rule fitted to 156 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R
    Total Standard Deviation in ln(k): 8.22708206092876"""),
    rank = 11,
    shortDesc = """BM rule fitted to 156 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R
Total Standard Deviation in ln(k): 8.22708206092876""",
    longDesc = 
"""
BM rule fitted to 156 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R
Total Standard Deviation in ln(k): 8.22708206092876
""",
)

entry(
    index = 104,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_1BrC->Br",
    kinetics = Arrhenius(A=(19036.1,'m^3/(mol*s)'), n=0.381498, Ea=(6.31119,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_1BrC->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_1BrC->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_1BrC->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_1BrC->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 105,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_N-1BrC->Br",
    kinetics = ArrheniusBM(A=(2.7032e+09,'m^3/(mol*s)'), n=-0.671759, w0=(193.572,'kJ/mol'), E0=(113.674,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7001281535011572, var=0.7225535388437554, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_N-1BrC->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_N-1BrC->Br
    Total Standard Deviation in ln(k): 3.4632039141850455"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_N-1BrC->Br
Total Standard Deviation in ln(k): 3.4632039141850455""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_N-1BrC->Br
Total Standard Deviation in ln(k): 3.4632039141850455
""",
)

entry(
    index = 106,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C",
    kinetics = Arrhenius(A=(601527,'m^3/(mol*s)'), n=0.145911, Ea=(-2.53395,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=3.3740754291645717e-16, var=10.35580982124874, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 6.4513265082540565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 6.4513265082540565""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 6.4513265082540565
""",
)

entry(
    index = 107,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.37709e+11,'m^3/(mol*s)'), n=-1.22122, w0=(179,'kJ/mol'), E0=(51.2724,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1295938076610641, var=4.693513668810264, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 15 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 4.668774622581672"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 4.668774622581672""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 4.668774622581672
""",
)

entry(
    index = 108,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_2BrCFHNO->H",
    kinetics = Arrhenius(A=(700000,'m^3/(mol*s)'), n=0.493, Ea=(-1.2301,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_2BrCFHNO->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_2BrCFHNO->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_2BrCFHNO->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_2BrCFHNO->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 109,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H",
    kinetics = ArrheniusBM(A=(3.03247e+11,'m^3/(mol*s)'), n=-0.896035, w0=(198.729,'kJ/mol'), E0=(58.6537,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0523802111712187, var=10.952300865397307, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H
    Total Standard Deviation in ln(k): 6.76613108499744"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H
Total Standard Deviation in ln(k): 6.76613108499744""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H
Total Standard Deviation in ln(k): 6.76613108499744
""",
)

entry(
    index = 110,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N_Ext-2CHO-R_2CHO->C",
    kinetics = ArrheniusBM(A=(7.38323e+06,'m^3/(mol*s)'), n=1.08409e-06, w0=(179,'kJ/mol'), E0=(89.0628,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.3279077205677291, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N_Ext-2CHO-R_2CHO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N_Ext-2CHO-R_2CHO->C
    Total Standard Deviation in ln(k): 1.1479760049827752"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N_Ext-2CHO-R_2CHO->C
Total Standard Deviation in ln(k): 1.1479760049827752""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N_Ext-2CHO-R_2CHO->C
Total Standard Deviation in ln(k): 1.1479760049827752
""",
)

entry(
    index = 111,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N_Ext-2CHO-R_N-2CHO->C",
    kinetics = Arrhenius(A=(1.81e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N_Ext-2CHO-R_N-2CHO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N_Ext-2CHO-R_N-2CHO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N_Ext-2CHO-R_N-2CHO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N_Ext-2CHO-R_N-2CHO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 112,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_3NO-u0_Ext-2BrCFHNO-R",
    kinetics = Arrhenius(A=(122000,'m^3/(mol*s)'), n=0.2, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_3NO-u0_Ext-2BrCFHNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_3NO-u0_Ext-2BrCFHNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_3NO-u0_Ext-2BrCFHNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_3NO-u0_Ext-2BrCFHNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 113,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_2BrCFHNO->N",
    kinetics = ArrheniusBM(A=(1.94707e+33,'m^3/(mol*s)'), n=-8.77465, w0=(100.5,'kJ/mol'), E0=(62.8035,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2718299409938927, var=172.44298933406674, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_2BrCFHNO->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_2BrCFHNO->N
    Total Standard Deviation in ln(k): 29.521242488300285"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_2BrCFHNO->N
Total Standard Deviation in ln(k): 29.521242488300285""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_2BrCFHNO->N
Total Standard Deviation in ln(k): 29.521242488300285
""",
)

entry(
    index = 114,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N",
    kinetics = ArrheniusBM(A=(1.00191e-25,'m^3/(mol*s)'), n=9.19118, w0=(181.658,'kJ/mol'), E0=(18.8538,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6535845759102119, var=22.290373080667294, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N
    Total Standard Deviation in ln(k): 11.10706420034294"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N
Total Standard Deviation in ln(k): 11.10706420034294""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N
Total Standard Deviation in ln(k): 11.10706420034294
""",
)

entry(
    index = 115,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_N-7R!H->C_Ext-6C-R_Ext-6C-R",
    kinetics = Arrhenius(A=(12121.6,'m^3/(mol*s)'), n=0.487299, Ea=(-2.31865,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_N-7R!H->C_Ext-6C-R_Ext-6C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_N-7R!H->C_Ext-6C-R_Ext-6C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_N-7R!H->C_Ext-6C-R_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_1BrCClFHN->F_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-5R!H-R_6R!H->C_N-3R!H->C_Ext-6C-R_N-7R!H->C_Ext-6C-R_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 116,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F",
    kinetics = ArrheniusBM(A=(1.68063e+06,'m^3/(mol*s)'), n=0.382151, w0=(259.211,'kJ/mol'), E0=(25.9211,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3376003050087245, var=16.85316217607203, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F
    Total Standard Deviation in ln(k): 9.078201308691936"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F
Total Standard Deviation in ln(k): 9.078201308691936""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F
Total Standard Deviation in ln(k): 9.078201308691936
""",
)

entry(
    index = 117,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F",
    kinetics = ArrheniusBM(A=(1.89905e+08,'m^3/(mol*s)'), n=-0.110226, w0=(210.812,'kJ/mol'), E0=(109.066,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.256699632185426, var=1.884626395295997, Tref=1000.0, N=44, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F',), comment="""BM rule fitted to 44 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F
    Total Standard Deviation in ln(k): 3.3971082571982425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 44 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F
Total Standard Deviation in ln(k): 3.3971082571982425""",
    longDesc = 
"""
BM rule fitted to 44 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F
Total Standard Deviation in ln(k): 3.3971082571982425
""",
)

entry(
    index = 118,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F",
    kinetics = ArrheniusBM(A=(2.31482e+14,'m^3/(mol*s)'), n=-2.01467, w0=(163.5,'kJ/mol'), E0=(62.3505,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2281166633397407, var=43.26852707303155, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F
    Total Standard Deviation in ln(k): 13.760067535193958"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F
Total Standard Deviation in ln(k): 13.760067535193958""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F
Total Standard Deviation in ln(k): 13.760067535193958
""",
)

entry(
    index = 119,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F",
    kinetics = ArrheniusBM(A=(1.50163e+17,'m^3/(mol*s)'), n=-3.25205, w0=(189.352,'kJ/mol'), E0=(152.055,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05537038551465185, var=7.753255725767487, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F
    Total Standard Deviation in ln(k): 5.72123996900642"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F
Total Standard Deviation in ln(k): 5.72123996900642""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F
Total Standard Deviation in ln(k): 5.72123996900642
""",
)

entry(
    index = 120,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R",
    kinetics = Arrhenius(A=(1.4924e+08,'m^3/(mol*s)'), n=-0.508688, Ea=(0.130245,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.12013627070250489, var=17.03764577210549, Tref=1000.0, N=114, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R',), comment="""BM rule fitted to 114 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R
    Total Standard Deviation in ln(k): 8.576731398297033"""),
    rank = 11,
    shortDesc = """BM rule fitted to 114 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R
Total Standard Deviation in ln(k): 8.576731398297033""",
    longDesc = 
"""
BM rule fitted to 114 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R
Total Standard Deviation in ln(k): 8.576731398297033
""",
)

entry(
    index = 121,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.04387e+08,'m^3/(mol*s)'), n=-0.325375, w0=(173,'kJ/mol'), E0=(89.6563,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.054199560676558296, var=0.32137768603764055, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R',), comment="""BM rule fitted to 22 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.2726677868217293"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.2726677868217293""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.2726677868217293
""",
)

entry(
    index = 122,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C",
    kinetics = ArrheniusBM(A=(3.85282e+10,'m^3/(mol*s)'), n=-1.02579, w0=(195.126,'kJ/mol'), E0=(142.898,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.044444372867729065, var=1.9308726212341463, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C
    Total Standard Deviation in ln(k): 2.8973657986714976"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C
Total Standard Deviation in ln(k): 2.8973657986714976""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C
Total Standard Deviation in ln(k): 2.8973657986714976
""",
)

entry(
    index = 123,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C",
    kinetics = ArrheniusBM(A=(1.27705e+09,'m^3/(mol*s)'), n=-0.69671, w0=(201.393,'kJ/mol'), E0=(55.329,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6597918012696907, var=3.6796421137655533, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C
    Total Standard Deviation in ln(k): 5.503330009588134"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C
Total Standard Deviation in ln(k): 5.503330009588134""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C
Total Standard Deviation in ln(k): 5.503330009588134
""",
)

entry(
    index = 124,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_6R!H->O",
    kinetics = Arrhenius(A=(2.65136e+06,'m^3/(mol*s)'), n=-0.078484, Ea=(-19.163,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 125,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(22027.3,'m^3/(mol*s)'), n=0.570703, w0=(212.974,'kJ/mol'), E0=(8.86788,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7623463273637304, var=25.956246852140886, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O
    Total Standard Deviation in ln(k): 12.129021677877493"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O
Total Standard Deviation in ln(k): 12.129021677877493""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O
Total Standard Deviation in ln(k): 12.129021677877493
""",
)

entry(
    index = 126,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F",
    kinetics = ArrheniusBM(A=(3.44729e+10,'m^3/(mol*s)'), n=-1.05143, w0=(179,'kJ/mol'), E0=(43.6624,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13735224930724416, var=4.235607678351363, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F
    Total Standard Deviation in ln(k): 4.47096962735631"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F
Total Standard Deviation in ln(k): 4.47096962735631""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F
Total Standard Deviation in ln(k): 4.47096962735631
""",
)

entry(
    index = 127,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_N-6R!H->F",
    kinetics = Arrhenius(A=(3.32184e+07,'m^3/(mol*s)'), n=-0.149136, Ea=(-29.6542,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_N-6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_N-6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 128,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_6R!H->O",
    kinetics = Arrhenius(A=(6.04616e+08,'m^3/(mol*s)'), n=0.201065, Ea=(-9.13376,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 129,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(1.39936e+11,'m^3/(mol*s)'), n=-0.907612, w0=(205.417,'kJ/mol'), E0=(102.708,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09850637730223, var=10.254542957769365, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O
    Total Standard Deviation in ln(k): 6.667209525943271"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O
Total Standard Deviation in ln(k): 6.667209525943271""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O
Total Standard Deviation in ln(k): 6.667209525943271
""",
)

entry(
    index = 130,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N_Ext-2CHO-R_2CHO->C_Ext-2C-R_Ext-2C-R",
    kinetics = Arrhenius(A=(9.04e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N_Ext-2CHO-R_2CHO->C_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N_Ext-2CHO-R_2CHO->C_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N_Ext-2CHO-R_2CHO->C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_N-2BrCFHNO->N_Ext-2CHO-R_2CHO->C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 131,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R",
    kinetics = Arrhenius(A=(267934,'m^3/(mol*s)'), n=0.322484, Ea=(25.7535,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=5.247227115244467, var=17.18583707094867, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R
    Total Standard Deviation in ln(k): 21.494778223513553"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R
Total Standard Deviation in ln(k): 21.494778223513553""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R
Total Standard Deviation in ln(k): 21.494778223513553
""",
)

entry(
    index = 132,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_2CHO->H",
    kinetics = Arrhenius(A=(43950,'m^3/(mol*s)'), n=1, Ea=(1.8828,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_2CHO->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_2CHO->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_2CHO->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_2CHO->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 133,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_N-2CHO->H",
    kinetics = ArrheniusBM(A=(20726.2,'m^3/(mol*s)'), n=0.643665, w0=(179,'kJ/mol'), E0=(35.9004,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14945848549575996, var=0.8200717430596174, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_N-2CHO->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_N-2CHO->H
    Total Standard Deviation in ln(k): 2.1909680682692025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_N-2CHO->H
Total Standard Deviation in ln(k): 2.1909680682692025""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_N-2CHO->H
Total Standard Deviation in ln(k): 2.1909680682692025
""",
)

entry(
    index = 134,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.65909e+06,'m^3/(mol*s)'), n=0.385598, w0=(260.27,'kJ/mol'), E0=(26.027,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.32436642957961104, var=16.943091187062468, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R',), comment="""BM rule fitted to 18 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R
    Total Standard Deviation in ln(k): 9.066878814374363"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R
Total Standard Deviation in ln(k): 9.066878814374363""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R
Total Standard Deviation in ln(k): 9.066878814374363
""",
)

entry(
    index = 135,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(6.51484e+09,'m^3/(mol*s)'), n=-0.566644, w0=(210.482,'kJ/mol'), E0=(111.974,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05582085824804805, var=2.2871027355189533, Tref=1000.0, N=38, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C',), comment="""BM rule fitted to 38 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C
    Total Standard Deviation in ln(k): 3.1720483686385235"""),
    rank = 11,
    shortDesc = """BM rule fitted to 38 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C
Total Standard Deviation in ln(k): 3.1720483686385235""",
    longDesc = 
"""
BM rule fitted to 38 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C
Total Standard Deviation in ln(k): 3.1720483686385235
""",
)

entry(
    index = 136,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(2.3625e+06,'m^3/(mol*s)'), n=0.449623, w0=(212.903,'kJ/mol'), E0=(60.3127,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-5.364906387887949, var=57.89639007226252, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C
    Total Standard Deviation in ln(k): 28.733628822828123"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C
Total Standard Deviation in ln(k): 28.733628822828123""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C
Total Standard Deviation in ln(k): 28.733628822828123
""",
)

entry(
    index = 137,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.35017e+16,'m^3/(mol*s)'), n=-2.51834, w0=(163.5,'kJ/mol'), E0=(56.912,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.288191486668048, var=62.50334310244288, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R
    Total Standard Deviation in ln(k): 16.573345455458593"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R
Total Standard Deviation in ln(k): 16.573345455458593""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R
Total Standard Deviation in ln(k): 16.573345455458593
""",
)

entry(
    index = 138,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(6.32527e+15,'m^3/(mol*s)'), n=-2.73838, w0=(187.79,'kJ/mol'), E0=(146.841,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09986028960331599, var=6.190443238681452, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C',), comment="""BM rule fitted to 15 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C
    Total Standard Deviation in ln(k): 5.238806678891656"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C
Total Standard Deviation in ln(k): 5.238806678891656""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C
Total Standard Deviation in ln(k): 5.238806678891656
""",
)

entry(
    index = 139,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_N-3BrCClILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(1.22185e+12,'m^3/(mol*s)'), n=-2.24226, w0=(195.206,'kJ/mol'), E0=(43.5892,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1976196173653206, var=7.388499009521079, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_N-3BrCClILiNOPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_N-3BrCClILiNOPSSi->C
    Total Standard Deviation in ln(k): 5.945761202857524"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_N-3BrCClILiNOPSSi->C
Total Standard Deviation in ln(k): 5.945761202857524""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_N-3BrCClILiNOPSSi->C
Total Standard Deviation in ln(k): 5.945761202857524
""",
)

entry(
    index = 140,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R",
    kinetics = Arrhenius(A=(103579,'m^3/(mol*s)'), n=0.447911, Ea=(-4.03935,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.10935074678984083, var=18.45424407438908, Tref=1000.0, N=60, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R',), comment="""BM rule fitted to 60 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 8.886772401001695"""),
    rank = 11,
    shortDesc = """BM rule fitted to 60 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 8.886772401001695""",
    longDesc = 
"""
BM rule fitted to 60 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 8.886772401001695
""",
)

entry(
    index = 141,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC",
    kinetics = ArrheniusBM(A=(5.83211e+06,'m^3/(mol*s)'), n=0.218069, w0=(173.784,'kJ/mol'), E0=(94.1434,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2608609778017518, var=0.7132945645995049, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC
    Total Standard Deviation in ln(k): 2.3485640440145565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC
Total Standard Deviation in ln(k): 2.3485640440145565""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC
Total Standard Deviation in ln(k): 2.3485640440145565
""",
)

entry(
    index = 142,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC",
    kinetics = ArrheniusBM(A=(5.0389e+06,'m^3/(mol*s)'), n=0.149751, w0=(193.557,'kJ/mol'), E0=(18.465,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8968529857580142, var=5.94429384903393, Tref=1000.0, N=45, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC',), comment="""BM rule fitted to 45 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC
    Total Standard Deviation in ln(k): 7.141128529339425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 45 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC
Total Standard Deviation in ln(k): 7.141128529339425""",
    longDesc = 
"""
BM rule fitted to 45 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC
Total Standard Deviation in ln(k): 7.141128529339425
""",
)

entry(
    index = 143,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC",
    kinetics = ArrheniusBM(A=(1.35457e+09,'m^3/(mol*s)'), n=-0.706533, w0=(173,'kJ/mol'), E0=(97.0193,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2856486240659873, var=1.133222719081651, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC
    Total Standard Deviation in ln(k): 2.8518094226963524"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC
Total Standard Deviation in ln(k): 2.8518094226963524""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC
Total Standard Deviation in ln(k): 2.8518094226963524
""",
)

entry(
    index = 144,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC",
    kinetics = ArrheniusBM(A=(1.92412e+07,'m^3/(mol*s)'), n=-0.0744847, w0=(173,'kJ/mol'), E0=(74.8099,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04592203297472184, var=0.20803229741636936, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC
    Total Standard Deviation in ln(k): 1.0297528417065889"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC
Total Standard Deviation in ln(k): 1.0297528417065889""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC
Total Standard Deviation in ln(k): 1.0297528417065889
""",
)

entry(
    index = 145,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC",
    kinetics = ArrheniusBM(A=(9.1685e+08,'m^3/(mol*s)'), n=-0.612234, w0=(175.641,'kJ/mol'), E0=(48.8358,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.007526157192081558, var=2.9324308198923457, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC
    Total Standard Deviation in ln(k): 3.4518868105181495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC
Total Standard Deviation in ln(k): 3.4518868105181495""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC
Total Standard Deviation in ln(k): 3.4518868105181495
""",
)

entry(
    index = 146,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC",
    kinetics = ArrheniusBM(A=(9.48194e+07,'m^3/(mol*s)'), n=-0.0228726, w0=(214.61,'kJ/mol'), E0=(90.2214,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04954191060468914, var=0.40322123515783614, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC
    Total Standard Deviation in ln(k): 1.3974779935325798"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC
Total Standard Deviation in ln(k): 1.3974779935325798""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC
Total Standard Deviation in ln(k): 1.3974779935325798
""",
)

entry(
    index = 147,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_3BrClFO->O",
    kinetics = ArrheniusBM(A=(1.52618e+07,'m^3/(mol*s)'), n=-4.57861e-08, w0=(173,'kJ/mol'), E0=(71.4771,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15989752451550138, var=0.06567934312931165, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_3BrClFO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_3BrClFO->O
    Total Standard Deviation in ln(k): 0.9155257071693345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_3BrClFO->O
Total Standard Deviation in ln(k): 0.9155257071693345""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_3BrClFO->O
Total Standard Deviation in ln(k): 0.9155257071693345
""",
)

entry(
    index = 148,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O",
    kinetics = ArrheniusBM(A=(3.57752e+14,'m^3/(mol*s)'), n=-2.67072, w0=(214.18,'kJ/mol'), E0=(8.79048,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6294895767340131, var=6.9773747598102664, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O
    Total Standard Deviation in ln(k): 6.877083841023017"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O
Total Standard Deviation in ln(k): 6.877083841023017""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O
Total Standard Deviation in ln(k): 6.877083841023017
""",
)

entry(
    index = 149,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-6BrCClFILiNPSSi-R_7R!H->O",
    kinetics = Arrhenius(A=(2.02037e+09,'m^3/(mol*s)'), n=-0.642574, Ea=(3.82265,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-6BrCClFILiNPSSi-R_7R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-6BrCClFILiNPSSi-R_7R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-6BrCClFILiNPSSi-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-6BrCClFILiNPSSi-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 150,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-6BrCClFILiNPSSi-R_N-7R!H->O",
    kinetics = ArrheniusBM(A=(8303.48,'m^3/(mol*s)'), n=0.587829, w0=(222.247,'kJ/mol'), E0=(170.542,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3129831803152541, var=1.0373951407624917, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-6BrCClFILiNPSSi-R_N-7R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-6BrCClFILiNPSSi-R_N-7R!H->O
    Total Standard Deviation in ln(k): 2.828264628954887"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-6BrCClFILiNPSSi-R_N-7R!H->O
Total Standard Deviation in ln(k): 2.828264628954887""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-6BrCClFILiNPSSi-R_N-7R!H->O
Total Standard Deviation in ln(k): 2.828264628954887
""",
)

entry(
    index = 151,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O",
    kinetics = ArrheniusBM(A=(9.9908e+12,'m^3/(mol*s)'), n=-1.64339, w0=(183.485,'kJ/mol'), E0=(91.7424,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1528559352981638, var=4.896049581784121, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O
    Total Standard Deviation in ln(k): 4.819941200920834"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 4.819941200920834""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 4.819941200920834
""",
)

entry(
    index = 152,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O",
    kinetics = ArrheniusBM(A=(7.34497e+09,'m^3/(mol*s)'), n=-0.889992, w0=(179,'kJ/mol'), E0=(19.259,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1331239729757274, var=4.089448492788784, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O
    Total Standard Deviation in ln(k): 4.388534771171697"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 4.388534771171697""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 4.388534771171697
""",
)

entry(
    index = 153,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-5R!H-R_Ext-3C-R_Ext-5R!H-R_7R!H->O",
    kinetics = Arrhenius(A=(1.1694e+09,'m^3/(mol*s)'), n=-0.278991, Ea=(-22.5191,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-5R!H-R_Ext-3C-R_Ext-5R!H-R_7R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-5R!H-R_Ext-3C-R_Ext-5R!H-R_7R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-5R!H-R_Ext-3C-R_Ext-5R!H-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-5R!H-R_Ext-3C-R_Ext-5R!H-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 154,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-5R!H-R_Ext-3C-R_Ext-5R!H-R_N-7R!H->O",
    kinetics = ArrheniusBM(A=(4.1117e+07,'m^3/(mol*s)'), n=0.0877022, w0=(219.053,'kJ/mol'), E0=(34.7988,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2582460419143793, var=0.5824198310279011, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-5R!H-R_Ext-3C-R_Ext-5R!H-R_N-7R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-5R!H-R_Ext-3C-R_Ext-5R!H-R_N-7R!H->O
    Total Standard Deviation in ln(k): 2.1788017518281895"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-5R!H-R_Ext-3C-R_Ext-5R!H-R_N-7R!H->O
Total Standard Deviation in ln(k): 2.1788017518281895""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-5R!H-R_Ext-3C-R_Ext-5R!H-R_N-7R!H->O
Total Standard Deviation in ln(k): 2.1788017518281895
""",
)

entry(
    index = 155,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F",
    kinetics = ArrheniusBM(A=(3.16234e+07,'m^3/(mol*s)'), n=-0.0149524, w0=(283.614,'kJ/mol'), E0=(177.39,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19803850630986802, var=4.355669154754971, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F
    Total Standard Deviation in ln(k): 4.6815143963913"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F
Total Standard Deviation in ln(k): 4.6815143963913""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F
Total Standard Deviation in ln(k): 4.6815143963913
""",
)

entry(
    index = 156,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F",
    kinetics = ArrheniusBM(A=(55773.9,'m^3/(mol*s)'), n=0.360175, w0=(179,'kJ/mol'), E0=(38.6047,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0936964551021723, var=1.1229498569217244, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F
    Total Standard Deviation in ln(k): 2.359822527339241"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F
Total Standard Deviation in ln(k): 2.359822527339241""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F
Total Standard Deviation in ln(k): 2.359822527339241
""",
)

entry(
    index = 157,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.02469e+16,'m^3/(mol*s)'), n=-2.5541, w0=(262.346,'kJ/mol'), E0=(195.31,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.002367968030327159, var=33.04731287221203, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C',), comment="""BM rule fitted to 15 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C
    Total Standard Deviation in ln(k): 11.53052856648321"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C
Total Standard Deviation in ln(k): 11.53052856648321""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C
Total Standard Deviation in ln(k): 11.53052856648321
""",
)

entry(
    index = 158,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(5.63469e+17,'m^3/(mol*s)'), n=-2.64305, w0=(249.888,'kJ/mol'), E0=(246.807,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-14.37392600611431, var=456.8060472673876, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 78.96263784990126"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C
Total Standard Deviation in ln(k): 78.96263784990126""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C
Total Standard Deviation in ln(k): 78.96263784990126
""",
)

entry(
    index = 159,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.309e+10,'m^3/(mol*s)'), n=-0.863205, w0=(205.5,'kJ/mol'), E0=(186.949,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2437739258293159, var=3.48665239399859, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R',), comment="""BM rule fitted to 18 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R
    Total Standard Deviation in ln(k): 4.355854888300228"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R
Total Standard Deviation in ln(k): 4.355854888300228""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R
Total Standard Deviation in ln(k): 4.355854888300228
""",
)

entry(
    index = 160,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing",
    kinetics = ArrheniusBM(A=(3.82246e+08,'m^3/(mol*s)'), n=-0.106413, w0=(205.5,'kJ/mol'), E0=(105.177,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07756329577677018, var=0.08207199971507625, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing
    Total Standard Deviation in ln(k): 0.7692033889455145"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing
Total Standard Deviation in ln(k): 0.7692033889455145""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing
Total Standard Deviation in ln(k): 0.7692033889455145
""",
)

entry(
    index = 161,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing",
    kinetics = ArrheniusBM(A=(1.99782e+09,'m^3/(mol*s)'), n=-0.419678, w0=(236.076,'kJ/mol'), E0=(89.6673,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.35983202779925816, var=4.7143229179145205, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing
    Total Standard Deviation in ln(k): 5.256879926612"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing
Total Standard Deviation in ln(k): 5.256879926612""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing
Total Standard Deviation in ln(k): 5.256879926612
""",
)

entry(
    index = 162,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_3ClOS->S",
    kinetics = Arrhenius(A=(500000,'m^3/(mol*s)'), n=0.65, Ea=(-1.54808,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_3ClOS->S',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_3ClOS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_3ClOS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_3ClOS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 163,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3ClOS->S",
    kinetics = ArrheniusBM(A=(3.7835e+13,'m^3/(mol*s)'), n=-2.73588, w0=(216.213,'kJ/mol'), E0=(14.2672,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15617756480842182, var=0.3562102440656151, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3ClOS->S',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3ClOS->S
    Total Standard Deviation in ln(k): 1.5888990236713798"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3ClOS->S
Total Standard Deviation in ln(k): 1.5888990236713798""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3ClOS->S
Total Standard Deviation in ln(k): 1.5888990236713798
""",
)

entry(
    index = 164,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R_4R!H->Cl",
    kinetics = Arrhenius(A=(5363.42,'m^3/(mol*s)'), n=1.12404, Ea=(-94.9326,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 165,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(2.61723e+07,'m^3/(mol*s)'), n=-0.0518497, w0=(163.5,'kJ/mol'), E0=(81.3805,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05779466547310243, var=8.301057045299686, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R_N-4R!H->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 5.921166232075081"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.921166232075081""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.921166232075081
""",
)

entry(
    index = 166,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R",
    kinetics = ArrheniusBM(A=(3.89852e+12,'m^3/(mol*s)'), n=-1.81556, w0=(194.432,'kJ/mol'), E0=(113.083,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09396642833921512, var=9.57752467178714, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R
    Total Standard Deviation in ln(k): 6.440265692726275"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R
Total Standard Deviation in ln(k): 6.440265692726275""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R
Total Standard Deviation in ln(k): 6.440265692726275
""",
)

entry(
    index = 167,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-Sp-3C-2R",
    kinetics = ArrheniusBM(A=(8.92064e+17,'m^3/(mol*s)'), n=-3.36029, w0=(174.507,'kJ/mol'), E0=(87.2536,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09522907457024189, var=1.6837903128628227, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-Sp-3C-2R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-Sp-3C-2R
    Total Standard Deviation in ln(k): 2.8406322344890014"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-Sp-3C-2R
Total Standard Deviation in ln(k): 2.8406322344890014""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-Sp-3C-2R
Total Standard Deviation in ln(k): 2.8406322344890014
""",
)

entry(
    index = 168,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_3BrClO->Cl",
    kinetics = ArrheniusBM(A=(8.17544e+14,'m^3/(mol*s)'), n=-3.04515, w0=(175.041,'kJ/mol'), E0=(36.0171,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1135789575912249, var=3.0907683395358485, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_3BrClO->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_3BrClO->Cl
    Total Standard Deviation in ln(k): 3.809815038719634"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_3BrClO->Cl
Total Standard Deviation in ln(k): 3.809815038719634""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_3BrClO->Cl
Total Standard Deviation in ln(k): 3.809815038719634
""",
)

entry(
    index = 169,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3BrClO->Cl",
    kinetics = Arrhenius(A=(1.50059e+20,'m^3/(mol*s)'), n=-4.57992, Ea=(40.8065,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3BrClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3BrClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3BrClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3BrClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 170,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O",
    kinetics = ArrheniusBM(A=(2.37966e+11,'m^3/(mol*s)'), n=-1.0018, w0=(173,'kJ/mol'), E0=(84.2933,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09437458051489195, var=9.11152180449234, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O
    Total Standard Deviation in ln(k): 6.2884745179232"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O
Total Standard Deviation in ln(k): 6.2884745179232""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O
Total Standard Deviation in ln(k): 6.2884745179232
""",
)

entry(
    index = 171,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(633746,'m^3/(mol*s)'), n=0.131339, w0=(180.085,'kJ/mol'), E0=(14.0189,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2571924797019248, var=15.916207435920613, Tref=1000.0, N=51, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O',), comment="""BM rule fitted to 51 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O
    Total Standard Deviation in ln(k): 8.644127269884747"""),
    rank = 11,
    shortDesc = """BM rule fitted to 51 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O
Total Standard Deviation in ln(k): 8.644127269884747""",
    longDesc = 
"""
BM rule fitted to 51 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O
Total Standard Deviation in ln(k): 8.644127269884747
""",
)

entry(
    index = 172,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R",
    kinetics = ArrheniusBM(A=(6.08418e+06,'m^3/(mol*s)'), n=0.210217, w0=(173.359,'kJ/mol'), E0=(94.1434,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2684331659155549, var=0.7085048913984375, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R
    Total Standard Deviation in ln(k): 2.3618954868513806"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R
Total Standard Deviation in ln(k): 2.3618954868513806""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R
Total Standard Deviation in ln(k): 2.3618954868513806
""",
)

entry(
    index = 173,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C",
    kinetics = ArrheniusBM(A=(3.40267e+10,'m^3/(mol*s)'), n=-0.792692, w0=(173.931,'kJ/mol'), E0=(57.1293,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4816964155107994, var=10.41112110812253, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C
    Total Standard Deviation in ln(k): 7.678824615807168"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C
Total Standard Deviation in ln(k): 7.678824615807168""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C
Total Standard Deviation in ln(k): 7.678824615807168
""",
)

entry(
    index = 174,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C",
    kinetics = ArrheniusBM(A=(2.68505e+06,'m^3/(mol*s)'), n=0.217031, w0=(204.384,'kJ/mol'), E0=(63.3492,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13594333964746086, var=10.459316342187233, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C',), comment="""BM rule fitted to 29 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C
    Total Standard Deviation in ln(k): 6.825053094181568"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C
Total Standard Deviation in ln(k): 6.825053094181568""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C
Total Standard Deviation in ln(k): 6.825053094181568
""",
)

entry(
    index = 175,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.9609e+09,'m^3/(mol*s)'), n=-0.904668, w0=(173,'kJ/mol'), E0=(22.7439,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.28018604532803965, var=1.832562473464953, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R
    Total Standard Deviation in ln(k): 3.4178384395333765"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R
Total Standard Deviation in ln(k): 3.4178384395333765""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R
Total Standard Deviation in ln(k): 3.4178384395333765
""",
)

entry(
    index = 176,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.51229e+07,'m^3/(mol*s)'), n=-0.0676006, w0=(173,'kJ/mol'), E0=(49.6983,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.003975165722417502, var=0.08330494045872566, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R
    Total Standard Deviation in ln(k): 0.5886064248045739"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R
Total Standard Deviation in ln(k): 0.5886064248045739""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R
Total Standard Deviation in ln(k): 0.5886064248045739
""",
)

entry(
    index = 177,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(5.38619e+06,'m^3/(mol*s)'), n=0.213797, w0=(186.233,'kJ/mol'), E0=(93.1164,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0017612663798735795, var=0.036594567475474134, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.3879252309045138"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.3879252309045138""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.3879252309045138
""",
)

entry(
    index = 178,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_Ext-2R-R",
    kinetics = ArrheniusBM(A=(8.06003e+08,'m^3/(mol*s)'), n=-0.684834, w0=(179.164,'kJ/mol'), E0=(81.1464,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6906216596550477, var=1.1467118550001338, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_Ext-2R-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_Ext-2R-R
    Total Standard Deviation in ln(k): 3.8819934938942335"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_Ext-2R-R
Total Standard Deviation in ln(k): 3.8819934938942335""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_Ext-2R-R
Total Standard Deviation in ln(k): 3.8819934938942335
""",
)

entry(
    index = 179,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_2R->C",
    kinetics = ArrheniusBM(A=(1.18079e+09,'m^3/(mol*s)'), n=-0.555622, w0=(184.79,'kJ/mol'), E0=(183.741,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2886192288092501, var=0.16825203022957463, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_2R->C
    Total Standard Deviation in ln(k): 1.5474869227976424"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_2R->C
Total Standard Deviation in ln(k): 1.5474869227976424""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_2R->C
Total Standard Deviation in ln(k): 1.5474869227976424
""",
)

entry(
    index = 180,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_N-2R->C",
    kinetics = Arrhenius(A=(2e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 181,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_Sp-3C#1BrBrCC",
    kinetics = Arrhenius(A=(1e+08,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_Sp-3C#1BrBrCC',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_Sp-3C#1BrBrCC
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_Sp-3C#1BrBrCC
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_Sp-3C#1BrBrCC
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 182,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_N-Sp-3C#1BrBrCC",
    kinetics = ArrheniusBM(A=(7.88936e+07,'m^3/(mol*s)'), n=-0.0235682, w0=(199.818,'kJ/mol'), E0=(84.5989,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.36621926002360833, var=0.8151162120739097, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_N-Sp-3C#1BrBrCC',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_N-Sp-3C#1BrBrCC
    Total Standard Deviation in ln(k): 2.730099633468922"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_N-Sp-3C#1BrBrCC
Total Standard Deviation in ln(k): 2.730099633468922""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_N-Sp-3C#1BrBrCC
Total Standard Deviation in ln(k): 2.730099633468922
""",
)

entry(
    index = 183,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_3BrClF->F",
    kinetics = Arrhenius(A=(1.54959e+17,'m^3/(mol*s)'), n=-3.35333, Ea=(9.38611,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=5.281365289817324e-15, var=20.084573741611983, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_3BrClF->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_3BrClF->F
    Total Standard Deviation in ln(k): 8.98438385901949"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_3BrClF->F
Total Standard Deviation in ln(k): 8.98438385901949""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_3BrClF->F
Total Standard Deviation in ln(k): 8.98438385901949
""",
)

entry(
    index = 184,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_N-3BrClF->F",
    kinetics = ArrheniusBM(A=(2.24266e+26,'m^3/(mol*s)'), n=-6.1236, w0=(238.776,'kJ/mol'), E0=(167.749,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06682594197315242, var=0.890868661857234, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_N-3BrClF->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_N-3BrClF->F
    Total Standard Deviation in ln(k): 2.0600904009185426"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_N-3BrClF->F
Total Standard Deviation in ln(k): 2.0600904009185426""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_N-3BrClF->F
Total Standard Deviation in ln(k): 2.0600904009185426
""",
)

entry(
    index = 185,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-6BrCClFILiNPSSi-R_N-7R!H->O_Sp-6BrCClFILiNPSSi-2BrBrCCClFFHILiNNOPSSi",
    kinetics = Arrhenius(A=(11871.3,'m^3/(mol*s)'), n=0.590055, Ea=(16.0013,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-6BrCClFILiNPSSi-R_N-7R!H->O_Sp-6BrCClFILiNPSSi-2BrBrCCClFFHILiNNOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-6BrCClFILiNPSSi-R_N-7R!H->O_Sp-6BrCClFILiNPSSi-2BrBrCCClFFHILiNNOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-6BrCClFILiNPSSi-R_N-7R!H->O_Sp-6BrCClFILiNPSSi-2BrBrCCClFFHILiNNOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-6BrCClFILiNPSSi-R_N-7R!H->O_Sp-6BrCClFILiNPSSi-2BrBrCCClFFHILiNNOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 186,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-6BrCClFILiNPSSi-R_N-7R!H->O_N-Sp-6BrCClFILiNPSSi-2BrBrCCClFFHILiNNOPSSi",
    kinetics = Arrhenius(A=(2058.83,'m^3/(mol*s)'), n=0.714649, Ea=(-10.7967,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-6BrCClFILiNPSSi-R_N-7R!H->O_N-Sp-6BrCClFILiNPSSi-2BrBrCCClFFHILiNNOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-6BrCClFILiNPSSi-R_N-7R!H->O_N-Sp-6BrCClFILiNPSSi-2BrBrCCClFFHILiNNOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-6BrCClFILiNPSSi-R_N-7R!H->O_N-Sp-6BrCClFILiNPSSi-2BrBrCCClFFHILiNNOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-6R!H->O_Ext-6BrCClFILiNPSSi-R_N-7R!H->O_N-Sp-6BrCClFILiNPSSi-2BrBrCCClFFHILiNNOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 187,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O_Ext-4C-R_Ext-3C-R_Ext-7R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.79614e+14,'m^3/(mol*s)'), n=-2.16405, w0=(179,'kJ/mol'), E0=(87.6869,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.0797562575303106, var=2.729232612382721, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O_Ext-4C-R_Ext-3C-R_Ext-7R!H-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O_Ext-4C-R_Ext-3C-R_Ext-7R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 8.537418618787312"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O_Ext-4C-R_Ext-3C-R_Ext-7R!H-R_7R!H->C
Total Standard Deviation in ln(k): 8.537418618787312""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O_Ext-4C-R_Ext-3C-R_Ext-7R!H-R_7R!H->C
Total Standard Deviation in ln(k): 8.537418618787312
""",
)

entry(
    index = 188,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O_Ext-4C-R_Ext-3C-R_Ext-7R!H-R_N-7R!H->C",
    kinetics = Arrhenius(A=(4.35505e+07,'m^3/(mol*s)'), n=0.214807, Ea=(-7.02322,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O_Ext-4C-R_Ext-3C-R_Ext-7R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O_Ext-4C-R_Ext-3C-R_Ext-7R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O_Ext-4C-R_Ext-3C-R_Ext-7R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O_Ext-4C-R_Ext-3C-R_Ext-7R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 189,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C",
    kinetics = Arrhenius(A=(470977,'m^3/(mol*s)'), n=0.386378, Ea=(-0.626618,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=8.247739937957843e-16, var=6.819726288720004, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C
    Total Standard Deviation in ln(k): 5.235286600255217"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C
Total Standard Deviation in ln(k): 5.235286600255217""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C
Total Standard Deviation in ln(k): 5.235286600255217
""",
)

entry(
    index = 190,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C",
    kinetics = ArrheniusBM(A=(3.9113e+14,'m^3/(mol*s)'), n=-2.33418, w0=(179,'kJ/mol'), E0=(36.6265,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2845853559239414, var=1.8241065399612681, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C
    Total Standard Deviation in ln(k): 3.422623521488738"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C
Total Standard Deviation in ln(k): 3.422623521488738""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C
Total Standard Deviation in ln(k): 3.422623521488738
""",
)

entry(
    index = 191,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-5R!H-R_Ext-3C-R_Ext-5R!H-R_N-7R!H->O_Sp-5R!H-2CNO",
    kinetics = Arrhenius(A=(1.68819e+06,'m^3/(mol*s)'), n=0.526236, Ea=(-4.66466,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-5R!H-R_Ext-3C-R_Ext-5R!H-R_N-7R!H->O_Sp-5R!H-2CNO',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-5R!H-R_Ext-3C-R_Ext-5R!H-R_N-7R!H->O_Sp-5R!H-2CNO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-5R!H-R_Ext-3C-R_Ext-5R!H-R_N-7R!H->O_Sp-5R!H-2CNO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-5R!H-R_Ext-3C-R_Ext-5R!H-R_N-7R!H->O_Sp-5R!H-2CNO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 192,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-5R!H-R_Ext-3C-R_Ext-5R!H-R_N-7R!H->O_N-Sp-5R!H-2CNO",
    kinetics = Arrhenius(A=(1.8084e+07,'m^3/(mol*s)'), n=0.148656, Ea=(0.370298,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-5R!H-R_Ext-3C-R_Ext-5R!H-R_N-7R!H->O_N-Sp-5R!H-2CNO',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-5R!H-R_Ext-3C-R_Ext-5R!H-R_N-7R!H->O_N-Sp-5R!H-2CNO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-5R!H-R_Ext-3C-R_Ext-5R!H-R_N-7R!H->O_N-Sp-5R!H-2CNO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_N-4R!H->C_N-2BrCFHNO->H_Ext-3C-R_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-5R!H-R_Ext-3C-R_Ext-5R!H-R_N-7R!H->O_N-Sp-5R!H-2CNO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 193,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C",
    kinetics = ArrheniusBM(A=(7.9084e+06,'m^3/(mol*s)'), n=0.0977399, w0=(266.484,'kJ/mol'), E0=(168.038,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1976675370719043, var=5.370421454107344, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C
    Total Standard Deviation in ln(k): 5.142459209751081"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C
Total Standard Deviation in ln(k): 5.142459209751081""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C
Total Standard Deviation in ln(k): 5.142459209751081
""",
)

entry(
    index = 194,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_N-5R!H->C",
    kinetics = Arrhenius(A=(2.75765e+07,'m^3/(mol*s)'), n=0.181385, Ea=(126.069,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 195,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R",
    kinetics = ArrheniusBM(A=(15.484,'m^3/(mol*s)'), n=1.37634, w0=(179,'kJ/mol'), E0=(19.0946,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2990512759769646, var=1.260279412563258, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R
    Total Standard Deviation in ln(k): 3.0019441547703933"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R
Total Standard Deviation in ln(k): 3.0019441547703933""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R
Total Standard Deviation in ln(k): 3.0019441547703933
""",
)

entry(
    index = 196,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi",
    kinetics = ArrheniusBM(A=(1.1209e+07,'m^3/(mol*s)'), n=-0.210333, w0=(179,'kJ/mol'), E0=(38.6327,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02070667919257134, var=1.33476806369263, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi
    Total Standard Deviation in ln(k): 2.3681406250910806"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi
Total Standard Deviation in ln(k): 2.3681406250910806""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi
Total Standard Deviation in ln(k): 2.3681406250910806
""",
)

entry(
    index = 197,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_N-Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi",
    kinetics = ArrheniusBM(A=(3.24037e+06,'m^3/(mol*s)'), n=2.12948e-08, w0=(179,'kJ/mol'), E0=(31.982,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06321145093973116, var=0.0944925917831317, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_N-Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_N-Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi
    Total Standard Deviation in ln(k): 0.7750712337002329"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_N-Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi
Total Standard Deviation in ln(k): 0.7750712337002329""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_N-Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi
Total Standard Deviation in ln(k): 0.7750712337002329
""",
)

entry(
    index = 198,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.48092e+16,'m^3/(mol*s)'), n=-2.58854, w0=(259.759,'kJ/mol'), E0=(200.607,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17953842973543715, var=31.418822721406812, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.688142009097268"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.688142009097268""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.688142009097268
""",
)

entry(
    index = 199,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C",
    kinetics = ArrheniusBM(A=(1.02279e+36,'m^3/(mol*s)'), n=-10.0662, w0=(270.517,'kJ/mol'), E0=(207.666,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.6609179753085948, var=2.447440824278797, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C
    Total Standard Deviation in ln(k): 12.334553810562252"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C
Total Standard Deviation in ln(k): 12.334553810562252""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C
Total Standard Deviation in ln(k): 12.334553810562252
""",
)

entry(
    index = 200,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_N-Sp-4C-2C",
    kinetics = Arrhenius(A=(2.4e+28,'m^3/(mol*s)'), n=-7.11, Ea=(21.0874,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_N-Sp-4C-2C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_N-Sp-4C-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_N-Sp-4C-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_N-Sp-4C-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 201,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.56997e+11,'m^3/(mol*s)'), n=-0.751575, w0=(236.266,'kJ/mol'), E0=(204.859,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.301639776246612, var=24.332488105172484, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 15.67196606710672"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 15.67196606710672""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 15.67196606710672
""",
)

entry(
    index = 202,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_3C-inRing",
    kinetics = Arrhenius(A=(1.7491e+06,'m^3/(mol*s)'), n=-1.12475, Ea=(-56.954,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_3C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_3C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 203,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing",
    kinetics = ArrheniusBM(A=(2.96838e+07,'m^3/(mol*s)'), n=0.205688, w0=(205.5,'kJ/mol'), E0=(98.4363,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.014036146869937736, var=0.08309259741083669, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing
    Total Standard Deviation in ln(k): 0.6131473563308167"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing
Total Standard Deviation in ln(k): 0.6131473563308167""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing
Total Standard Deviation in ln(k): 0.6131473563308167
""",
)

entry(
    index = 204,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(9.17151e+07,'m^3/(mol*s)'), n=0.103124, w0=(205.5,'kJ/mol'), E0=(105.75,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06473678945074865, var=0.16285884646625448, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 0.971681599438312"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 0.971681599438312""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 0.971681599438312
""",
)

entry(
    index = 205,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(5.24876e+07,'m^3/(mol*s)'), n=0.108701, w0=(205.5,'kJ/mol'), E0=(86.89,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17016890191634107, var=0.29748126830616106, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 1.5209795218558437"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 1.5209795218558437""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 1.5209795218558437
""",
)

entry(
    index = 206,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.83153e+09,'m^3/(mol*s)'), n=-0.472098, w0=(235.104,'kJ/mol'), E0=(88.9793,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5152629133594214, var=6.182178231609377, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R
    Total Standard Deviation in ln(k): 6.27920101952442"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 6.27920101952442""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 6.27920101952442
""",
)

entry(
    index = 207,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Sp-3C#2C",
    kinetics = Arrhenius(A=(1.81e+08,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Sp-3C#2C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Sp-3C#2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Sp-3C#2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Sp-3C#2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 208,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_N-Sp-3C#2C",
    kinetics = ArrheniusBM(A=(1.30121e+08,'m^3/(mol*s)'), n=-0.0104386, w0=(221.434,'kJ/mol'), E0=(112.941,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16819443494880856, var=0.07267224299466185, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_N-Sp-3C#2C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_N-Sp-3C#2C
    Total Standard Deviation in ln(k): 0.9630313506418686"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_N-Sp-3C#2C
Total Standard Deviation in ln(k): 0.9630313506418686""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_N-Sp-3C#2C
Total Standard Deviation in ln(k): 0.9630313506418686
""",
)

entry(
    index = 209,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3ClOS->S_3ClO->Cl",
    kinetics = ArrheniusBM(A=(7.1883e+15,'m^3/(mol*s)'), n=-3.4347, w0=(233.671,'kJ/mol'), E0=(119.145,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02717840416636139, var=0.0944146141836256, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3ClOS->S_3ClO->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3ClOS->S_3ClO->Cl
    Total Standard Deviation in ln(k): 0.6842816161507455"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3ClOS->S_3ClO->Cl
Total Standard Deviation in ln(k): 0.6842816161507455""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3ClOS->S_3ClO->Cl
Total Standard Deviation in ln(k): 0.6842816161507455
""",
)

entry(
    index = 210,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3ClOS->S_N-3ClO->Cl",
    kinetics = Arrhenius(A=(46800,'m^3/(mol*s)'), n=0, Ea=(-18.9535,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3ClOS->S_N-3ClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3ClOS->S_N-3ClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3ClOS->S_N-3ClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3ClOS->S_N-3ClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 211,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R_N-4R!H->Cl_4BrCFILiNOPSSi->F",
    kinetics = ArrheniusBM(A=(3.46638e+07,'m^3/(mol*s)'), n=0.0128888, w0=(164.4,'kJ/mol'), E0=(82.1998,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6374044122877079, var=10.291586159957822, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R_N-4R!H->Cl_4BrCFILiNOPSSi->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R_N-4R!H->Cl_4BrCFILiNOPSSi->F
    Total Standard Deviation in ln(k): 8.032809413015608"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R_N-4R!H->Cl_4BrCFILiNOPSSi->F
Total Standard Deviation in ln(k): 8.032809413015608""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R_N-4R!H->Cl_4BrCFILiNOPSSi->F
Total Standard Deviation in ln(k): 8.032809413015608
""",
)

entry(
    index = 212,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->F",
    kinetics = Arrhenius(A=(2607.44,'m^3/(mol*s)'), n=0.895266, Ea=(-9.25605,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_3R!H->F_Ext-2R-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 213,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(3.46812e+08,'m^3/(mol*s)'), n=-0.724216, w0=(194.286,'kJ/mol'), E0=(50.8279,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23066505821695976, var=11.981083362501556, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R
    Total Standard Deviation in ln(k): 7.5186906169970635"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R
Total Standard Deviation in ln(k): 7.5186906169970635""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R
Total Standard Deviation in ln(k): 7.5186906169970635
""",
)

entry(
    index = 214,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-3C-R",
    kinetics = Arrhenius(A=(13966.5,'m^3/(mol*s)'), n=0.851267, Ea=(-22.3536,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 215,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-Sp-3C-2R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.84656e+14,'m^3/(mol*s)'), n=-2.20814, w0=(167.469,'kJ/mol'), E0=(83.7345,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17021294406340748, var=2.1807981022285645, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-Sp-3C-2R_Ext-2R-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-Sp-3C-2R_Ext-2R-R
    Total Standard Deviation in ln(k): 3.388168356975142"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-Sp-3C-2R_Ext-2R-R
Total Standard Deviation in ln(k): 3.388168356975142""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-Sp-3C-2R_Ext-2R-R
Total Standard Deviation in ln(k): 3.388168356975142
""",
)

entry(
    index = 216,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_3BrClO->Cl_Ext-2R-R",
    kinetics = ArrheniusBM(A=(9.5271e+11,'m^3/(mol*s)'), n=-2.09678, w0=(163.5,'kJ/mol'), E0=(15.8518,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5685971363586392, var=30.87199035050886, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_3BrClO->Cl_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_3BrClO->Cl_Ext-2R-R
    Total Standard Deviation in ln(k): 12.567459057396194"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_3BrClO->Cl_Ext-2R-R
Total Standard Deviation in ln(k): 12.567459057396194""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_3BrClO->Cl_Ext-2R-R
Total Standard Deviation in ln(k): 12.567459057396194
""",
)

entry(
    index = 217,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F",
    kinetics = ArrheniusBM(A=(4.77939e+22,'m^3/(mol*s)'), n=-4.28607, w0=(173,'kJ/mol'), E0=(59.2452,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.43467903456091994, var=2.682579429263594, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F
    Total Standard Deviation in ln(k): 4.375630130556729"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F
Total Standard Deviation in ln(k): 4.375630130556729""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F
Total Standard Deviation in ln(k): 4.375630130556729
""",
)

entry(
    index = 218,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F",
    kinetics = ArrheniusBM(A=(2.0563e+10,'m^3/(mol*s)'), n=-0.674185, w0=(193.635,'kJ/mol'), E0=(175.323,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22434245626962102, var=0.9342469890600731, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F
    Total Standard Deviation in ln(k): 2.5013803294431347"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F
Total Standard Deviation in ln(k): 2.5013803294431347""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F
Total Standard Deviation in ln(k): 2.5013803294431347
""",
)

entry(
    index = 219,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(10328.5,'m^3/(mol*s)'), n=0.616326, w0=(187.906,'kJ/mol'), E0=(74.9137,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.372179537703058, var=37.13361184792571, Tref=1000.0, N=39, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R',), comment="""BM rule fitted to 39 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R
    Total Standard Deviation in ln(k): 20.68913813642008"""),
    rank = 11,
    shortDesc = """BM rule fitted to 39 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R
Total Standard Deviation in ln(k): 20.68913813642008""",
    longDesc = 
"""
BM rule fitted to 39 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R
Total Standard Deviation in ln(k): 20.68913813642008
""",
)

entry(
    index = 220,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_5R!H->F",
    kinetics = Arrhenius(A=(549.624,'m^3/(mol*s)'), n=0.798645, Ea=(-134.259,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 221,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F",
    kinetics = ArrheniusBM(A=(6.6488e+07,'m^3/(mol*s)'), n=-0.295094, w0=(175.882,'kJ/mol'), E0=(34.7426,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3379213658685315, var=2.635780537788078, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F
    Total Standard Deviation in ln(k): 4.10375352126877"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F
Total Standard Deviation in ln(k): 4.10375352126877""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F
Total Standard Deviation in ln(k): 4.10375352126877
""",
)

entry(
    index = 222,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.1806e+08,'m^3/(mol*s)'), n=-0.4, w0=(173,'kJ/mol'), E0=(22.8223,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.293265616277649e-11, var=0.38791698118242224, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_5R!H->C
    Total Standard Deviation in ln(k): 1.2486087818780434"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_5R!H->C
Total Standard Deviation in ln(k): 1.2486087818780434""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_5R!H->C
Total Standard Deviation in ln(k): 1.2486087818780434
""",
)

entry(
    index = 223,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(5.62133e+06,'m^3/(mol*s)'), n=0.224923, w0=(178.558,'kJ/mol'), E0=(83.8354,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00022337126487811446, var=1.4397514310559894, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C
    Total Standard Deviation in ln(k): 2.406035687045363"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C
Total Standard Deviation in ln(k): 2.406035687045363""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C
Total Standard Deviation in ln(k): 2.406035687045363
""",
)

entry(
    index = 224,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.51503e+10,'m^3/(mol*s)'), n=-0.66228, w0=(173,'kJ/mol'), E0=(166.276,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9446358548551101, var=9.006157696757136, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R
    Total Standard Deviation in ln(k): 8.389719227246745"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R
Total Standard Deviation in ln(k): 8.389719227246745""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R
Total Standard Deviation in ln(k): 8.389719227246745
""",
)

entry(
    index = 225,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-1BrC-R",
    kinetics = ArrheniusBM(A=(2.82036e+08,'m^3/(mol*s)'), n=-0.5, w0=(187.402,'kJ/mol'), E0=(139.216,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14995901122765234, var=2.2305291506772655, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-1BrC-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-1BrC-R
    Total Standard Deviation in ln(k): 3.3708444816661607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-1BrC-R
Total Standard Deviation in ln(k): 3.3708444816661607""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-1BrC-R
Total Standard Deviation in ln(k): 3.3708444816661607
""",
)

entry(
    index = 226,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R",
    kinetics = ArrheniusBM(A=(461156,'m^3/(mol*s)'), n=0.510588, w0=(194.62,'kJ/mol'), E0=(64.524,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1259894739863473, var=8.940441785476244, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R',), comment="""BM rule fitted to 21 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R
    Total Standard Deviation in ln(k): 6.310828927771793"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R
Total Standard Deviation in ln(k): 6.310828927771793""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R
Total Standard Deviation in ln(k): 6.310828927771793
""",
)

entry(
    index = 227,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C",
    kinetics = ArrheniusBM(A=(6.45017e+18,'m^3/(mol*s)'), n=-4.53883, w0=(242.043,'kJ/mol'), E0=(27.3342,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.5434654509371417, var=14.853609139484037, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C
    Total Standard Deviation in ln(k): 14.116941939976975"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C
Total Standard Deviation in ln(k): 14.116941939976975""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C
Total Standard Deviation in ln(k): 14.116941939976975
""",
)

entry(
    index = 228,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_N-2R->C",
    kinetics = Arrhenius(A=(3.49e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 229,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R_Sp-5R!H-2R",
    kinetics = ArrheniusBM(A=(2.17421e+13,'m^3/(mol*s)'), n=-2.10968, w0=(173,'kJ/mol'), E0=(84.3596,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11076293667129228, var=0.13376655749343258, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R_Sp-5R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R_Sp-5R!H-2R
    Total Standard Deviation in ln(k): 1.0115128626996137"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R_Sp-5R!H-2R
Total Standard Deviation in ln(k): 1.0115128626996137""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R_Sp-5R!H-2R
Total Standard Deviation in ln(k): 1.0115128626996137
""",
)

entry(
    index = 230,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-5R!H-2R",
    kinetics = ArrheniusBM(A=(250896,'m^3/(mol*s)'), n=0.298496, w0=(173,'kJ/mol'), E0=(70.6961,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06243996161282631, var=0.8653650783542394, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-5R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-5R!H-2R
    Total Standard Deviation in ln(k): 2.0217891484895985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-5R!H-2R
Total Standard Deviation in ln(k): 2.0217891484895985""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-5R!H-2R
Total Standard Deviation in ln(k): 2.0217891484895985
""",
)

entry(
    index = 231,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_Sp-4R!H=3R!H",
    kinetics = ArrheniusBM(A=(3.11826e+08,'m^3/(mol*s)'), n=-0.382134, w0=(173,'kJ/mol'), E0=(75.4719,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09812769830724073, var=0.8853225170864677, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_Sp-4R!H=3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_Sp-4R!H=3R!H
    Total Standard Deviation in ln(k): 2.132838887656121"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_Sp-4R!H=3R!H
Total Standard Deviation in ln(k): 2.132838887656121""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_Sp-4R!H=3R!H
Total Standard Deviation in ln(k): 2.132838887656121
""",
)

entry(
    index = 232,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H",
    kinetics = ArrheniusBM(A=(1.92985e+07,'m^3/(mol*s)'), n=-0.098089, w0=(176.039,'kJ/mol'), E0=(70.9125,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02763614479550622, var=0.08748620497981895, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H
    Total Standard Deviation in ln(k): 0.6623994348951677"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H
Total Standard Deviation in ln(k): 0.6623994348951677""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H
Total Standard Deviation in ln(k): 0.6623994348951677
""",
)

entry(
    index = 233,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R",
    kinetics = Arrhenius(A=(5.749e+06,'m^3/(mol*s)'), n=0.214, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 234,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_Ext-2R-R_4R!H->C",
    kinetics = ArrheniusBM(A=(8.41487e+08,'m^3/(mol*s)'), n=-0.692606, w0=(181.472,'kJ/mol'), E0=(90.7359,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.48601532080825466, var=0.49626155262741123, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_Ext-2R-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_Ext-2R-R_4R!H->C
    Total Standard Deviation in ln(k): 2.633396366652885"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_Ext-2R-R_4R!H->C
Total Standard Deviation in ln(k): 2.633396366652885""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_Ext-2R-R_4R!H->C
Total Standard Deviation in ln(k): 2.633396366652885
""",
)

entry(
    index = 235,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_Ext-2R-R_N-4R!H->C",
    kinetics = Arrhenius(A=(1.81e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_Ext-2R-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_Ext-2R-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_Ext-2R-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_Sp-3C-1BrC_Ext-2R-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 236,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_N-Sp-3C#1BrBrCC_Ext-2R-R",
    kinetics = ArrheniusBM(A=(5.91911e+07,'m^3/(mol*s)'), n=-0.0612704, w0=(223.806,'kJ/mol'), E0=(137.129,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=3.8359635529677596, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_N-Sp-3C#1BrBrCC_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_N-Sp-3C#1BrBrCC_Ext-2R-R
    Total Standard Deviation in ln(k): 3.926397146884914"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_N-Sp-3C#1BrBrCC_Ext-2R-R
Total Standard Deviation in ln(k): 3.926397146884914""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_N-Sp-3C#1BrBrCC_Ext-2R-R
Total Standard Deviation in ln(k): 3.926397146884914
""",
)

entry(
    index = 237,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_N-Sp-3C#1BrBrCC_2R->C",
    kinetics = Arrhenius(A=(7.23e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_N-Sp-3C#1BrBrCC_2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_N-Sp-3C#1BrBrCC_2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_N-Sp-3C#1BrBrCC_2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_N-Sp-3C#1BrBrCC_2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 238,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_N-Sp-3C#1BrBrCC_N-2R->C",
    kinetics = ArrheniusBM(A=(5.19615e+07,'m^3/(mol*s)'), n=2.16888e-09, w0=(169.195,'kJ/mol'), E0=(84.5974,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=2.413897921625164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_N-Sp-3C#1BrBrCC_N-2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_N-Sp-3C#1BrBrCC_N-2R->C
    Total Standard Deviation in ln(k): 3.1147015559000413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_N-Sp-3C#1BrBrCC_N-2R->C
Total Standard Deviation in ln(k): 3.1147015559000413""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_3R!H->C_N-Sp-3C-1BrC_N-Sp-3C#1BrBrCC_N-2R->C
Total Standard Deviation in ln(k): 3.1147015559000413
""",
)

entry(
    index = 239,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_3BrClF->F_Ext-2R-R",
    kinetics = Arrhenius(A=(1.53948e+13,'m^3/(mol*s)'), n=-1.895, Ea=(4.79068,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=6.8887373345443345e-16, var=23.722589588252532, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_3BrClF->F_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_3BrClF->F_Ext-2R-R
    Total Standard Deviation in ln(k): 9.764230815939978"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_3BrClF->F_Ext-2R-R
Total Standard Deviation in ln(k): 9.764230815939978""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_3BrClF->F_Ext-2R-R
Total Standard Deviation in ln(k): 9.764230815939978
""",
)

entry(
    index = 240,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_N-3BrClF->F_3BrCl->Br",
    kinetics = Arrhenius(A=(310000,'m^3/(mol*s)'), n=0, Ea=(-17.9912,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_N-3BrClF->F_3BrCl->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_N-3BrClF->F_3BrCl->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_N-3BrClF->F_3BrCl->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_N-3BrClF->F_3BrCl->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 241,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_N-3BrClF->F_N-3BrCl->Br",
    kinetics = ArrheniusBM(A=(9.26047e+36,'m^3/(mol*s)'), n=-9.23874, w0=(282.184,'kJ/mol'), E0=(193.589,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.973209122599727, var=0.61618795644906, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_N-3BrClF->F_N-3BrCl->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_N-3BrClF->F_N-3BrCl->Br
    Total Standard Deviation in ln(k): 16.58173285619417"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_N-3BrClF->F_N-3BrCl->Br
Total Standard Deviation in ln(k): 16.58173285619417""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_N-3R!H->C_N-3BrClFO->O_N-3BrClF->F_N-3BrCl->Br
Total Standard Deviation in ln(k): 16.58173285619417
""",
)

entry(
    index = 242,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O_Ext-4C-R_Ext-3C-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = Arrhenius(A=(1.86361e+07,'m^3/(mol*s)'), n=-0.226315, Ea=(-14.6549,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O_Ext-4C-R_Ext-3C-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O_Ext-4C-R_Ext-3C-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O_Ext-4C-R_Ext-3C-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O_Ext-4C-R_Ext-3C-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 243,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O_Ext-4C-R_Ext-3C-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(1.57991e+07,'m^3/(mol*s)'), n=-0.0792137, Ea=(-19.9293,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O_Ext-4C-R_Ext-3C-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O_Ext-4C-R_Ext-3C-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O_Ext-4C-R_Ext-3C-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_5BrClFILiNOPSSi->O_Ext-4C-R_Ext-3C-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 244,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-3C-R",
    kinetics = Arrhenius(A=(768882,'m^3/(mol*s)'), n=0.336989, Ea=(-8.12942,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=8.997534477772192e-16, var=11.096127583472597, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 6.677943037435393"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-3C-R
Total Standard Deviation in ln(k): 6.677943037435393""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-3C-R
Total Standard Deviation in ln(k): 6.677943037435393
""",
)

entry(
    index = 245,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-4C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(145.711,'m^3/(mol*s)'), n=1.27167, w0=(212.995,'kJ/mol'), E0=(21.2995,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7420496141100124, var=5.981715029027307, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-4C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-4C-R_7R!H->C
    Total Standard Deviation in ln(k): 6.7675360849102635"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-4C-R_7R!H->C
Total Standard Deviation in ln(k): 6.7675360849102635""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-4C-R_7R!H->C
Total Standard Deviation in ln(k): 6.7675360849102635
""",
)

entry(
    index = 246,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-4C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(1.10694e+07,'m^3/(mol*s)'), n=0.199192, Ea=(8.28905,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-4C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-4C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-4C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-4C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 247,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R",
    kinetics = ArrheniusBM(A=(1.96737e+15,'m^3/(mol*s)'), n=-2.57864, w0=(179,'kJ/mol'), E0=(33.3448,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3240154828178447, var=2.677393202409802, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R
    Total Standard Deviation in ln(k): 4.094405504485947"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R
Total Standard Deviation in ln(k): 4.094405504485947""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R
Total Standard Deviation in ln(k): 4.094405504485947
""",
)

entry(
    index = 248,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_6R!H->O",
    kinetics = Arrhenius(A=(3.35407e+06,'m^3/(mol*s)'), n=0.141943, Ea=(72.6854,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 249,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(678625,'m^3/(mol*s)'), n=0.434559, w0=(283.49,'kJ/mol'), E0=(174.791,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.617327577401619, var=69.46470921968526, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-6R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-6R!H->O
    Total Standard Deviation in ln(k): 30.82245138292829"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-6R!H->O
Total Standard Deviation in ln(k): 30.82245138292829""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-6R!H->O
Total Standard Deviation in ln(k): 30.82245138292829
""",
)

entry(
    index = 250,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_Ext-2CHO-R",
    kinetics = Arrhenius(A=(4.18e+06,'m^3/(mol*s)'), n=-0.085, Ea=(-2.37316,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_Ext-2CHO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_Ext-2CHO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_Ext-2CHO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_Ext-2CHO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 251,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi",
    kinetics = ArrheniusBM(A=(134.737,'m^3/(mol*s)'), n=1.08957, w0=(179,'kJ/mol'), E0=(21.0749,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08154953628019496, var=0.0184455471377257, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi
    Total Standard Deviation in ln(k): 0.47717019372670105"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi
Total Standard Deviation in ln(k): 0.47717019372670105""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi
Total Standard Deviation in ln(k): 0.47717019372670105
""",
)

entry(
    index = 252,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_N-Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi",
    kinetics = Arrhenius(A=(0.004135,'m^3/(mol*s)'), n=2.525, Ea=(8.32198,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_N-Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_N-Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_N-Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_N-Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 253,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_Ext-2CHO-R",
    kinetics = ArrheniusBM(A=(3.45339e+06,'m^3/(mol*s)'), n=0.0013093, w0=(179,'kJ/mol'), E0=(38.6327,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17507732982344096, var=1.2895074408006884, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_Ext-2CHO-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_Ext-2CHO-R
    Total Standard Deviation in ln(k): 2.716399398490379"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_Ext-2CHO-R
Total Standard Deviation in ln(k): 2.716399398490379""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_Ext-2CHO-R
Total Standard Deviation in ln(k): 2.716399398490379
""",
)

entry(
    index = 254,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(290461,'m^3/(mol*s)'), n=0.492985, w0=(250.221,'kJ/mol'), E0=(25.0221,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19003534711761652, var=34.09314056473093, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 12.182989887158273"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R
Total Standard Deviation in ln(k): 12.182989887158273""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R
Total Standard Deviation in ln(k): 12.182989887158273
""",
)

entry(
    index = 255,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-4C-2C",
    kinetics = ArrheniusBM(A=(2.09994e+35,'m^3/(mol*s)'), n=-9.75051, w0=(275.69,'kJ/mol'), E0=(174.945,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.922591837461237, var=2.18410470025557, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-4C-2C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-4C-2C
    Total Standard Deviation in ln(k): 12.818499580810894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-4C-2C
Total Standard Deviation in ln(k): 12.818499580810894""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-4C-2C
Total Standard Deviation in ln(k): 12.818499580810894
""",
)

entry(
    index = 256,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-4C-2C",
    kinetics = ArrheniusBM(A=(3.51907e+15,'m^3/(mol*s)'), n=-3.10485, w0=(271.394,'kJ/mol'), E0=(33.4546,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1489571338938278, var=4.838484481250555, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-4C-2C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-4C-2C
    Total Standard Deviation in ln(k): 4.7839907686272065"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-4C-2C
Total Standard Deviation in ln(k): 4.7839907686272065""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-4C-2C
Total Standard Deviation in ln(k): 4.7839907686272065
""",
)

entry(
    index = 257,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.9764e+07,'m^3/(mol*s)'), n=0.206428, w0=(205.5,'kJ/mol'), E0=(98.6789,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.011957608535409564, var=0.06609898571451558, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R
    Total Standard Deviation in ln(k): 0.5454560779923847"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 0.5454560779923847""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 0.5454560779923847
""",
)

entry(
    index = 258,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C",
    kinetics = Arrhenius(A=(2.09978e+06,'m^3/(mol*s)'), n=0.6, Ea=(-3.3472,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 259,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C",
    kinetics = Arrhenius(A=(7.09e+06,'m^3/(mol*s)'), n=0.412, Ea=(0.037656,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 260,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C",
    kinetics = Arrhenius(A=(3.156e+06,'m^3/(mol*s)'), n=0.461, Ea=(-0.004184,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 261,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C",
    kinetics = Arrhenius(A=(7.22657e+07,'m^3/(mol*s)'), n=0.062, Ea=(-0.184096,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 262,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.59401e+09,'m^3/(mol*s)'), n=-0.338433, w0=(205.5,'kJ/mol'), E0=(107.887,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13041769786182827, var=0.17639824973306983, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C
    Total Standard Deviation in ln(k): 1.1696672132710029"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 1.1696672132710029""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 1.1696672132710029
""",
)

entry(
    index = 263,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(5.15008e+19,'m^3/(mol*s)'), n=-5.14141, w0=(283.352,'kJ/mol'), E0=(28.3352,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.30194898615831717, var=33.39144236487939, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 12.343093375531918"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 12.343093375531918""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 12.343093375531918
""",
)

entry(
    index = 264,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3ClOS->S_3ClO->Cl_Ext-2C-R",
    kinetics = ArrheniusBM(A=(4.805e+20,'m^3/(mol*s)'), n=-4.82, w0=(231.271,'kJ/mol'), E0=(167.983,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.014359010274123, var=8.662505535886095e-06, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3ClOS->S_3ClO->Cl_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3ClOS->S_3ClO->Cl_Ext-2C-R
    Total Standard Deviation in ln(k): 12.604792348898949"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3ClOS->S_3ClO->Cl_Ext-2C-R
Total Standard Deviation in ln(k): 12.604792348898949""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_N-3BrCClILiNOPSSi->C_N-3ClOS->S_3ClO->Cl_Ext-2C-R
Total Standard Deviation in ln(k): 12.604792348898949
""",
)

entry(
    index = 265,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.93132e+10,'m^3/(mol*s)'), n=-1.22628, w0=(163.5,'kJ/mol'), E0=(62.6353,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13970672032504158, var=10.687591926273338, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R
    Total Standard Deviation in ln(k): 6.904878304187348"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R
Total Standard Deviation in ln(k): 6.904878304187348""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R
Total Standard Deviation in ln(k): 6.904878304187348
""",
)

entry(
    index = 266,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-2R-R",
    kinetics = Arrhenius(A=(9.05803e+27,'m^3/(mol*s)'), n=-6.59025, Ea=(75.1144,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 267,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-Sp-3C-2R_Ext-2R-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.92813e+14,'m^3/(mol*s)'), n=-2.36382, w0=(195.754,'kJ/mol'), E0=(181.056,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5081716130487804, var=0.01008918115205773, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-Sp-3C-2R_Ext-2R-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-Sp-3C-2R_Ext-2R-R_Ext-3C-R
    Total Standard Deviation in ln(k): 1.4781785445816902"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-Sp-3C-2R_Ext-2R-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.4781785445816902""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-Sp-3C-2R_Ext-2R-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.4781785445816902
""",
)

entry(
    index = 268,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F_Ext-4O-R_Ext-6R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_7R!H->C",
    kinetics = ArrheniusBM(A=(3.0188e+23,'m^3/(mol*s)'), n=-4.63802, w0=(173,'kJ/mol'), E0=(58.1291,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.1821439404610694, var=0.9697279745421786, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F_Ext-4O-R_Ext-6R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F_Ext-4O-R_Ext-6R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_7R!H->C
    Total Standard Deviation in ln(k): 9.969494731242063"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F_Ext-4O-R_Ext-6R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_7R!H->C
Total Standard Deviation in ln(k): 9.969494731242063""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F_Ext-4O-R_Ext-6R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_7R!H->C
Total Standard Deviation in ln(k): 9.969494731242063
""",
)

entry(
    index = 269,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F_Ext-4O-R_Ext-6R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_N-7R!H->C",
    kinetics = Arrhenius(A=(1.50717e+06,'m^3/(mol*s)'), n=0.686973, Ea=(-36.7041,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F_Ext-4O-R_Ext-6R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F_Ext-4O-R_Ext-6R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F_Ext-4O-R_Ext-6R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F_Ext-4O-R_Ext-6R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 270,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R",
    kinetics = ArrheniusBM(A=(2.32445e+07,'m^3/(mol*s)'), n=0.379879, w0=(218.923,'kJ/mol'), E0=(156.14,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4559368554987122, var=3.6484824489667256, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R
    Total Standard Deviation in ln(k): 4.974814690378331"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R
Total Standard Deviation in ln(k): 4.974814690378331""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R
Total Standard Deviation in ln(k): 4.974814690378331
""",
)

entry(
    index = 271,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-5CO-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.86408e+14,'m^3/(mol*s)'), n=-2.10498, w0=(173,'kJ/mol'), E0=(82.7062,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.5257328068378369, var=5.1290184252937205, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-5CO-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-5CO-R_6R!H->C
    Total Standard Deviation in ln(k): 8.373690468304135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-5CO-R_6R!H->C
Total Standard Deviation in ln(k): 8.373690468304135""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-5CO-R_6R!H->C
Total Standard Deviation in ln(k): 8.373690468304135
""",
)

entry(
    index = 272,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-5CO-R_N-6R!H->C",
    kinetics = Arrhenius(A=(5.71994e+10,'m^3/(mol*s)'), n=-0.836909, Ea=(-7.73384,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-5CO-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-5CO-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-5CO-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-5CO-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 273,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H",
    kinetics = ArrheniusBM(A=(2.43916e+08,'m^3/(mol*s)'), n=-0.344176, w0=(173,'kJ/mol'), E0=(84.0488,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05161563448700158, var=2.721175581086387, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H
    Total Standard Deviation in ln(k): 3.4366957251610586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H
Total Standard Deviation in ln(k): 3.4366957251610586""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H
Total Standard Deviation in ln(k): 3.4366957251610586
""",
)

entry(
    index = 274,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H",
    kinetics = ArrheniusBM(A=(7376.47,'m^3/(mol*s)'), n=0.592177, w0=(192.239,'kJ/mol'), E0=(144.142,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27837985276683336, var=14.57198154688529, Tref=1000.0, N=32, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H',), comment="""BM rule fitted to 32 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H
    Total Standard Deviation in ln(k): 8.352175186721222"""),
    rank = 11,
    shortDesc = """BM rule fitted to 32 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H
Total Standard Deviation in ln(k): 8.352175186721222""",
    longDesc = 
"""
BM rule fitted to 32 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H
Total Standard Deviation in ln(k): 8.352175186721222
""",
)

entry(
    index = 275,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R",
    kinetics = ArrheniusBM(A=(5.95082e+07,'m^3/(mol*s)'), n=-0.292525, w0=(176.388,'kJ/mol'), E0=(49.8429,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0889650717051314, var=3.1336749946380418, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R
    Total Standard Deviation in ln(k): 3.77235027747121"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R
Total Standard Deviation in ln(k): 3.77235027747121""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R
Total Standard Deviation in ln(k): 3.77235027747121
""",
)

entry(
    index = 276,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-1BrC-R",
    kinetics = Arrhenius(A=(2.223e+10,'m^3/(mol*s)'), n=-0.506, Ea=(3.41414,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-1BrC-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-1BrC-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-1BrC-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-1BrC-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 277,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_5R!H->C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(8.53922e+07,'m^3/(mol*s)'), n=-0.366667, w0=(173,'kJ/mol'), E0=(7.30658,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.6724570646883641e-09, var=0.6179647329653195, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_5R!H->C_Ext-2R-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_5R!H->C_Ext-2R-R
    Total Standard Deviation in ln(k): 1.5759369415737927"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_5R!H->C_Ext-2R-R
Total Standard Deviation in ln(k): 1.5759369415737927""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_5R!H->C_Ext-2R-R
Total Standard Deviation in ln(k): 1.5759369415737927
""",
)

entry(
    index = 278,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C_4R!H->F",
    kinetics = Arrhenius(A=(3.03428e+07,'m^3/(mol*s)'), n=0.110658, Ea=(3.72558,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C_4R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C_4R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C_4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C_4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 279,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C_N-4R!H->F",
    kinetics = ArrheniusBM(A=(3.27781e+07,'m^3/(mol*s)'), n=-0.0890342, w0=(173.13,'kJ/mol'), E0=(65.2824,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6608074089847745, var=0.9118052438765222, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C_N-4R!H->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C_N-4R!H->F
    Total Standard Deviation in ln(k): 3.574611452171625"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C_N-4R!H->F
Total Standard Deviation in ln(k): 3.574611452171625""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C_N-4R!H->F
Total Standard Deviation in ln(k): 3.574611452171625
""",
)

entry(
    index = 280,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.65983e+11,'m^3/(mol*s)'), n=-0.84129, w0=(173,'kJ/mol'), E0=(17.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13665755708582394, var=2.914302658448111, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 3.7657098557350004"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.7657098557350004""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.7657098557350004
""",
)

entry(
    index = 281,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(2.55114e+09,'m^3/(mol*s)'), n=-1.1, w0=(174.533,'kJ/mol'), E0=(17.4533,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.34703542482178484, var=0.9009863614976826, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 2.7748488810011707"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 2.7748488810011707""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 2.7748488810011707
""",
)

entry(
    index = 282,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_5R!H->C",
    kinetics = ArrheniusBM(A=(3.41902e+08,'m^3/(mol*s)'), n=-0.65, w0=(179.08,'kJ/mol'), E0=(17.908,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24161022343536306, var=0.5727317376408546, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_5R!H->C
    Total Standard Deviation in ln(k): 2.1242251612479754"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_5R!H->C
Total Standard Deviation in ln(k): 2.1242251612479754""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_5R!H->C
Total Standard Deviation in ln(k): 2.1242251612479754
""",
)

entry(
    index = 283,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_N-5R!H->C",
    kinetics = Arrhenius(A=(1.21e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 284,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl",
    kinetics = ArrheniusBM(A=(3.89957e+09,'m^3/(mol*s)'), n=-0.98926, w0=(187.509,'kJ/mol'), E0=(44.2131,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0999126971999413, var=1.013627731794978, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl
    Total Standard Deviation in ln(k): 2.2693857767521406"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl
Total Standard Deviation in ln(k): 2.2693857767521406""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl
Total Standard Deviation in ln(k): 2.2693857767521406
""",
)

entry(
    index = 285,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl",
    kinetics = Arrhenius(A=(2.01811e+08,'m^3/(mol*s)'), n=-0.554036, Ea=(0.0523578,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-1.4565289384591473, var=5.539979307353025, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl
    Total Standard Deviation in ln(k): 8.378197603018524"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl
Total Standard Deviation in ln(k): 8.378197603018524""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl
Total Standard Deviation in ln(k): 8.378197603018524
""",
)

entry(
    index = 286,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(8.18345e+44,'m^3/(mol*s)'), n=-11.7593, w0=(259.608,'kJ/mol'), E0=(245.323,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5329849788166231, var=6.850369624067075, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_Ext-2C-R
    Total Standard Deviation in ln(k): 6.586193611613672"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 6.586193611613672""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 6.586193611613672
""",
)

entry(
    index = 287,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_3BrClFO->F",
    kinetics = ArrheniusBM(A=(1.39259e+19,'m^3/(mol*s)'), n=-4.6851, w0=(187.193,'kJ/mol'), E0=(93.5967,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.8042318088321334, var=24.438701432953486, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_3BrClFO->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_3BrClFO->F
    Total Standard Deviation in ln(k): 16.95631966381894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_3BrClFO->F
Total Standard Deviation in ln(k): 16.95631966381894""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_3BrClFO->F
Total Standard Deviation in ln(k): 16.95631966381894
""",
)

entry(
    index = 288,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_N-3BrClFO->F",
    kinetics = Arrhenius(A=(2.28e+35,'m^3/(mol*s)'), n=-8.68, Ea=(48.6181,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_N-3BrClFO->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_N-3BrClFO->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_N-3BrClFO->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_N-3BrClFO->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 289,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R_Sp-5R!H-2R_5R!H-inRing",
    kinetics = Arrhenius(A=(3.144e+13,'m^3/(mol*s)'), n=-2.163, Ea=(4.99988,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R_Sp-5R!H-2R_5R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R_Sp-5R!H-2R_5R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R_Sp-5R!H-2R_5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R_Sp-5R!H-2R_5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 290,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R_Sp-5R!H-2R_N-5R!H-inRing",
    kinetics = Arrhenius(A=(1.307e+06,'m^3/(mol*s)'), n=0.192, Ea=(-2.807,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R_Sp-5R!H-2R_N-5R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R_Sp-5R!H-2R_N-5R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R_Sp-5R!H-2R_N-5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_Sp-3R!H=1BrBrCC_Ext-2R-R_Sp-5R!H-2R_N-5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 291,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H",
    kinetics = ArrheniusBM(A=(2.17712e+06,'m^3/(mol*s)'), n=0.213828, w0=(183.244,'kJ/mol'), E0=(26.0427,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8870120301645524, var=2.1424892351432265, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H
    Total Standard Deviation in ln(k): 5.163053170371394"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 5.163053170371394""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 5.163053170371394
""",
)

entry(
    index = 292,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_N-Sp-4R!H-3R!H",
    kinetics = ArrheniusBM(A=(8.05579e+10,'m^3/(mol*s)'), n=-1.31825, w0=(173,'kJ/mol'), E0=(70.1326,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04628379485594601, var=0.016181722463235428, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_N-Sp-4R!H-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_N-Sp-4R!H-3R!H
    Total Standard Deviation in ln(k): 0.3713080775392354"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_N-Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 0.3713080775392354""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_N-Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 0.3713080775392354
""",
)

entry(
    index = 293,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-4C-R_Ext-2BrCFHNO-R",
    kinetics = Arrhenius(A=(6.75066e+08,'m^3/(mol*s)'), n=-0.302945, Ea=(-6.91537,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-4C-R_Ext-2BrCFHNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-4C-R_Ext-2BrCFHNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-4C-R_Ext-2BrCFHNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-4C-R_Ext-2BrCFHNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 294,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-4C-R_Sp-9R!H-2BrCFHNO",
    kinetics = Arrhenius(A=(102604,'m^3/(mol*s)'), n=0.53964, Ea=(5.30695,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-4C-R_Sp-9R!H-2BrCFHNO',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-4C-R_Sp-9R!H-2BrCFHNO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-4C-R_Sp-9R!H-2BrCFHNO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-4C-R_Sp-9R!H-2BrCFHNO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 295,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-4C-R_N-Sp-9R!H-2BrCFHNO",
    kinetics = Arrhenius(A=(6562.48,'m^3/(mol*s)'), n=0.774272, Ea=(-22.7798,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-4C-R_N-Sp-9R!H-2BrCFHNO',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-4C-R_N-Sp-9R!H-2BrCFHNO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-4C-R_N-Sp-9R!H-2BrCFHNO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-4C-R_N-Sp-9R!H-2BrCFHNO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 296,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = Arrhenius(A=(9919.91,'m^3/(mol*s)'), n=0.675528, Ea=(8.78531,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 297,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(218671,'m^3/(mol*s)'), n=0.432585, Ea=(3.55419,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_Sp-4C-3C_Ext-4C-R_Ext-4C-R_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 298,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C",
    kinetics = ArrheniusBM(A=(2.58082e+18,'m^3/(mol*s)'), n=-3.56752, w0=(179,'kJ/mol'), E0=(23.6321,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.43947312676103867, var=4.220042161576061, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C
    Total Standard Deviation in ln(k): 5.222479223749345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C
Total Standard Deviation in ln(k): 5.222479223749345""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C
Total Standard Deviation in ln(k): 5.222479223749345
""",
)

entry(
    index = 299,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_N-7R!H->C",
    kinetics = Arrhenius(A=(5.80475e+06,'m^3/(mol*s)'), n=0.152054, Ea=(2.02856,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 300,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-6R!H->O_6BrCClFILiNPSSi->C",
    kinetics = Arrhenius(A=(25637.8,'m^3/(mol*s)'), n=0.759408, Ea=(87.6633,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-6R!H->O_6BrCClFILiNPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-6R!H->O_6BrCClFILiNPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-6R!H->O_6BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-6R!H->O_6BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 301,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C",
    kinetics = Arrhenius(A=(3.3882e+06,'m^3/(mol*s)'), n=0.317264, Ea=(110.919,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_4R!H->F_Ext-2CHO-R_5R!H->C_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 302,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_Sp-5R!H-4BrCClILiNOPSSi",
    kinetics = Arrhenius(A=(2.94057e+10,'m^3/(mol*s)'), n=-1.39317, Ea=(9.38433,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_Sp-5R!H-4BrCClILiNOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_Sp-5R!H-4BrCClILiNOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_Sp-5R!H-4BrCClILiNOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_Sp-5R!H-4BrCClILiNOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 303,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_N-Sp-5R!H-4BrCClILiNOPSSi",
    kinetics = ArrheniusBM(A=(124.902,'m^3/(mol*s)'), n=1.09941, w0=(179,'kJ/mol'), E0=(16.8874,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.600552335588932, var=0.01543630385496216, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_N-Sp-5R!H-4BrCClILiNOPSSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_N-Sp-5R!H-4BrCClILiNOPSSi
    Total Standard Deviation in ln(k): 1.757999611670843"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_N-Sp-5R!H-4BrCClILiNOPSSi
Total Standard Deviation in ln(k): 1.757999611670843""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Ext-4BrCClILiNOPSSi-R_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_N-Sp-5R!H-4BrCClILiNOPSSi
Total Standard Deviation in ln(k): 1.757999611670843
""",
)

entry(
    index = 304,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_Ext-2CHO-R_5R!H->C",
    kinetics = ArrheniusBM(A=(5.18769e+06,'m^3/(mol*s)'), n=0.00084193, w0=(179,'kJ/mol'), E0=(38.6327,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.305460834090209e-17, var=0.7836333533627092, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_Ext-2CHO-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_Ext-2CHO-R_5R!H->C
    Total Standard Deviation in ln(k): 1.7746529918743192"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_Ext-2CHO-R_5R!H->C
Total Standard Deviation in ln(k): 1.7746529918743192""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_Ext-2CHO-R_5R!H->C
Total Standard Deviation in ln(k): 1.7746529918743192
""",
)

entry(
    index = 305,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_Ext-2CHO-R_N-5R!H->C",
    kinetics = Arrhenius(A=(1.505e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_Ext-2CHO-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_Ext-2CHO-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_Ext-2CHO-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_N-3R!H->C_N-3BrClFILiNOPSSi->Cl_N-3NO-u0_N-2BrCFHNO->N_Ext-2CHO-R_N-4R!H->F_Sp-4BrCClILiNOPSSi-2BrCCClHILiNOOPSSi_Ext-2CHO-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 306,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(260161,'m^3/(mol*s)'), n=0.511319, w0=(245.622,'kJ/mol'), E0=(24.5622,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.31741250560689444, var=36.60036464911672, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 12.925812285199935"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R
Total Standard Deviation in ln(k): 12.925812285199935""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R
Total Standard Deviation in ln(k): 12.925812285199935
""",
)

entry(
    index = 307,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-4C-2C_5R!H->F",
    kinetics = ArrheniusBM(A=(1.32819e+27,'m^3/(mol*s)'), n=-6.74987, w0=(286.189,'kJ/mol'), E0=(195.206,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.536223587017913, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-4C-2C_5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-4C-2C_5R!H->F
    Total Standard Deviation in ln(k): 6.372421072909329"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-4C-2C_5R!H->F
Total Standard Deviation in ln(k): 6.372421072909329""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-4C-2C_5R!H->F
Total Standard Deviation in ln(k): 6.372421072909329
""",
)

entry(
    index = 308,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-4C-2C_N-5R!H->F",
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-4C-2C_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-4C-2C_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-4C-2C_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-4C-2C_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 309,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.88633e+07,'m^3/(mol*s)'), n=0.213913, w0=(205.94,'kJ/mol'), E0=(102.97,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.197902036535014e-05, var=0.012106578798619934, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.2207867766612734"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.2207867766612734""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.2207867766612734
""",
)

entry(
    index = 310,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Sp-3C=2C",
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Sp-3C=2C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Sp-3C=2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Sp-3C=2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Sp-3C=2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 311,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C",
    kinetics = ArrheniusBM(A=(3.01147e+07,'m^3/(mol*s)'), n=0.20296, w0=(205.5,'kJ/mol'), E0=(95.2091,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7074946657604734, var=1.0112844439111153, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C
    Total Standard Deviation in ln(k): 3.7936392947510345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C
Total Standard Deviation in ln(k): 3.7936392947510345""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C
Total Standard Deviation in ln(k): 3.7936392947510345
""",
)

entry(
    index = 312,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C",
    kinetics = ArrheniusBM(A=(1.63901e+09,'m^3/(mol*s)'), n=-0.337292, w0=(205.516,'kJ/mol'), E0=(105.749,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.026716829379172215, var=0.05534958649330833, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C
    Total Standard Deviation in ln(k): 0.5387715662741953"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C
Total Standard Deviation in ln(k): 0.5387715662741953""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C
Total Standard Deviation in ln(k): 0.5387715662741953
""",
)

entry(
    index = 313,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C",
    kinetics = ArrheniusBM(A=(7.49629e+07,'m^3/(mol*s)'), n=-0.0711668, w0=(205.5,'kJ/mol'), E0=(115.882,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17899781099900458, var=3.8553349475711465, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C
    Total Standard Deviation in ln(k): 4.386041945290388"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 4.386041945290388""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 4.386041945290388
""",
)

entry(
    index = 314,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C",
    kinetics = ArrheniusBM(A=(4.36443e+19,'m^3/(mol*s)'), n=-5.46416, w0=(282.202,'kJ/mol'), E0=(28.2202,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.24476889533144483, var=42.99031347460256, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C
    Total Standard Deviation in ln(k): 13.759443490019503"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C
Total Standard Deviation in ln(k): 13.759443490019503""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C
Total Standard Deviation in ln(k): 13.759443490019503
""",
)

entry(
    index = 315,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C",
    kinetics = ArrheniusBM(A=(1.4352e+26,'m^3/(mol*s)'), n=-6.47299, w0=(285.077,'kJ/mol'), E0=(184.723,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.536223587017913, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C
    Total Standard Deviation in ln(k): 6.372421072909329"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 6.372421072909329""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 6.372421072909329
""",
)

entry(
    index = 316,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(228516,'m^3/(mol*s)'), n=0.317874, w0=(163.5,'kJ/mol'), E0=(69.7597,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.49099035658628687, var=28.07779457238084, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.85643140830555"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.85643140830555""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.85643140830555
""",
)

entry(
    index = 317,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R_Ext-2R-R",
    kinetics = Arrhenius(A=(1.17037e+12,'m^3/(mol*s)'), n=-1.62373, Ea=(-5.98089,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 318,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F_Ext-4O-R_Ext-6R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = Arrhenius(A=(9.5241e+06,'m^3/(mol*s)'), n=0.0334041, Ea=(-40.9943,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F_Ext-4O-R_Ext-6R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F_Ext-4O-R_Ext-6R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F_Ext-4O-R_Ext-6R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F_Ext-4O-R_Ext-6R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 319,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F_Ext-4O-R_Ext-6R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(7.05371e+06,'m^3/(mol*s)'), n=0.183451, Ea=(-40.6213,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F_Ext-4O-R_Ext-6R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F_Ext-4O-R_Ext-6R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F_Ext-4O-R_Ext-6R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_5R!H->F_Ext-4O-R_Ext-6R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-4O-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 320,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_8R!H->C",
    kinetics = ArrheniusBM(A=(1.59949e+08,'m^3/(mol*s)'), n=-0.00256204, w0=(218.841,'kJ/mol'), E0=(156.091,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.571723099309207, var=1.041358336153408, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_8R!H->C
    Total Standard Deviation in ln(k): 23.582764043660816"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_8R!H->C
Total Standard Deviation in ln(k): 23.582764043660816""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_8R!H->C
Total Standard Deviation in ln(k): 23.582764043660816
""",
)

entry(
    index = 321,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_N-8R!H->C",
    kinetics = Arrhenius(A=(490958,'m^3/(mol*s)'), n=1.14475, Ea=(24.8684,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 322,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-5CO-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = Arrhenius(A=(2.16906e+08,'m^3/(mol*s)'), n=-0.487462, Ea=(-13.09,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-5CO-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-5CO-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-5CO-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-5CO-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 323,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-5CO-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(8.03493e+09,'m^3/(mol*s)'), n=-0.771497, Ea=(-12.2813,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-5CO-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-5CO-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-5CO-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-5CO-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 324,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F",
    kinetics = ArrheniusBM(A=(2.52979e+09,'m^3/(mol*s)'), n=-0.80585, w0=(173,'kJ/mol'), E0=(78.8627,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09973386526116322, var=2.4694283787225255, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F
    Total Standard Deviation in ln(k): 3.4009114924133734"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F
Total Standard Deviation in ln(k): 3.4009114924133734""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F
Total Standard Deviation in ln(k): 3.4009114924133734
""",
)

entry(
    index = 325,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F",
    kinetics = ArrheniusBM(A=(5.49464e+07,'m^3/(mol*s)'), n=0.06878, w0=(181.927,'kJ/mol'), E0=(159.982,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.35776586488000567, var=0.1663523231528335, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F
    Total Standard Deviation in ln(k): 1.7165667079861093"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F
Total Standard Deviation in ln(k): 1.7165667079861093""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F
Total Standard Deviation in ln(k): 1.7165667079861093
""",
)

entry(
    index = 326,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C",
    kinetics = ArrheniusBM(A=(122.954,'m^3/(mol*s)'), n=1.13877, w0=(190.988,'kJ/mol'), E0=(17.2451,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7533592531007274, var=33.95661383486984, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C
    Total Standard Deviation in ln(k): 13.574915580341774"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C
Total Standard Deviation in ln(k): 13.574915580341774""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C
Total Standard Deviation in ln(k): 13.574915580341774
""",
)

entry(
    index = 327,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C",
    kinetics = ArrheniusBM(A=(5048.96,'m^3/(mol*s)'), n=0.612532, w0=(193.096,'kJ/mol'), E0=(19.3096,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16107434620975464, var=7.6919009567269585, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C
    Total Standard Deviation in ln(k): 5.9646971168945955"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C
Total Standard Deviation in ln(k): 5.9646971168945955""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C
Total Standard Deviation in ln(k): 5.9646971168945955
""",
)

entry(
    index = 328,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_6R!H->O",
    kinetics = Arrhenius(A=(8.73377,'m^3/(mol*s)'), n=1.46972, Ea=(-48.1774,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 329,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(908027,'m^3/(mol*s)'), n=0.255846, w0=(184.475,'kJ/mol'), E0=(46.6323,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02558525803191597, var=2.354236646001844, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O
    Total Standard Deviation in ln(k): 3.1402542262775235"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O
Total Standard Deviation in ln(k): 3.1402542262775235""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O
Total Standard Deviation in ln(k): 3.1402542262775235
""",
)

entry(
    index = 330,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_5R!H->C_Ext-2R-R_6R!H->C",
    kinetics = ArrheniusBM(A=(2.26848e+08,'m^3/(mol*s)'), n=-0.55, w0=(173,'kJ/mol'), E0=(17.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=6.458191251135313e-17, var=0.18719384195212657, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_5R!H->C_Ext-2R-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_5R!H->C_Ext-2R-R_6R!H->C
    Total Standard Deviation in ln(k): 0.8673667472246995"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_5R!H->C_Ext-2R-R_6R!H->C
Total Standard Deviation in ln(k): 0.8673667472246995""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_5R!H->C_Ext-2R-R_6R!H->C
Total Standard Deviation in ln(k): 0.8673667472246995
""",
)

entry(
    index = 331,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_5R!H->C_Ext-2R-R_N-6R!H->C",
    kinetics = Arrhenius(A=(1.21e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_5R!H->C_Ext-2R-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_5R!H->C_Ext-2R-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_5R!H->C_Ext-2R-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_5R!H->C_Ext-2R-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 332,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C_N-4R!H->F_4CO->C",
    kinetics = ArrheniusBM(A=(1.666e+08,'m^3/(mol*s)'), n=-0.226864, w0=(173,'kJ/mol'), E0=(97.2911,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.610921668180418e-17, var=1.2575949623617604, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C_N-4R!H->F_4CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C_N-4R!H->F_4CO->C
    Total Standard Deviation in ln(k): 2.248160866984347"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C_N-4R!H->F_4CO->C
Total Standard Deviation in ln(k): 2.248160866984347""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C_N-4R!H->F_4CO->C
Total Standard Deviation in ln(k): 2.248160866984347
""",
)

entry(
    index = 333,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C_N-4R!H->F_N-4CO->C",
    kinetics = Arrhenius(A=(4.46756e+07,'m^3/(mol*s)'), n=-0.128224, Ea=(0.329128,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C_N-4R!H->F_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C_N-4R!H->F_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C_N-4R!H->F_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Sp-3R!H=1BrBrCC_Ext-2R-R_N-5R!H->C_N-4R!H->F_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 334,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.39195e+11,'m^3/(mol*s)'), n=-0.855542, w0=(173,'kJ/mol'), E0=(80.042,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.0439528017080004, var=1.6830467897769874, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 10.248911405755292"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 10.248911405755292""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 10.248911405755292
""",
)

entry(
    index = 335,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_Ext-2R-R_Ext-1BrC-R",
    kinetics = ArrheniusBM(A=(7.14759e+09,'m^3/(mol*s)'), n=-1.3, w0=(173,'kJ/mol'), E0=(17.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=5.519561616726178, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_Ext-2R-R_Ext-1BrC-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_Ext-2R-R_Ext-1BrC-R
    Total Standard Deviation in ln(k): 4.70987392894025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_Ext-2R-R_Ext-1BrC-R
Total Standard Deviation in ln(k): 4.70987392894025""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_Ext-2R-R_Ext-1BrC-R
Total Standard Deviation in ln(k): 4.70987392894025
""",
)

entry(
    index = 336,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_5R!H->C_Ext-1BrC-R",
    kinetics = ArrheniusBM(A=(4.98065e+08,'m^3/(mol*s)'), n=-0.75, w0=(177.753,'kJ/mol'), E0=(88.8765,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.305460834090209e-17, var=0.8575717470917588, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_5R!H->C_Ext-1BrC-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_5R!H->C_Ext-1BrC-R
    Total Standard Deviation in ln(k): 1.8564883221612534"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_5R!H->C_Ext-1BrC-R
Total Standard Deviation in ln(k): 1.8564883221612534""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_3R!H->C_Ext-2R-R_5R!H->C_Ext-1BrC-R
Total Standard Deviation in ln(k): 1.8564883221612534
""",
)

entry(
    index = 337,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C",
    kinetics = ArrheniusBM(A=(9.01686e+09,'m^3/(mol*s)'), n=-1.1344, w0=(196.518,'kJ/mol'), E0=(44.8581,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.28640255111559104, var=1.1472172968692458, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C
    Total Standard Deviation in ln(k): 2.8668406606455785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C
Total Standard Deviation in ln(k): 2.8668406606455785""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C
Total Standard Deviation in ln(k): 2.8668406606455785
""",
)

entry(
    index = 338,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_N-2R->C",
    kinetics = Arrhenius(A=(410.863,'m^3/(mol*s)'), n=1.33656, Ea=(-10.0134,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 339,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R",
    kinetics = Arrhenius(A=(1.46289e+07,'m^3/(mol*s)'), n=-0.136865, Ea=(1.19118,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-1.3569447583914334, var=5.761094642389121, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R
    Total Standard Deviation in ln(k): 8.221230285541303"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R
Total Standard Deviation in ln(k): 8.221230285541303""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R
Total Standard Deviation in ln(k): 8.221230285541303
""",
)

entry(
    index = 340,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_Ext-2C-R_3BrClFO->F",
    kinetics = ArrheniusBM(A=(9.14376e+25,'m^3/(mol*s)'), n=-6.01387, w0=(239.36,'kJ/mol'), E0=(174.734,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.59157767324251, var=1.2444799571288412, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_Ext-2C-R_3BrClFO->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_Ext-2C-R_3BrClFO->F
    Total Standard Deviation in ln(k): 8.747909205099575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_Ext-2C-R_3BrClFO->F
Total Standard Deviation in ln(k): 8.747909205099575""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_Ext-2C-R_3BrClFO->F
Total Standard Deviation in ln(k): 8.747909205099575
""",
)

entry(
    index = 341,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_Ext-2C-R_N-3BrClFO->F",
    kinetics = ArrheniusBM(A=(1.22366e+25,'m^3/(mol*s)'), n=-6.39447, w0=(279.856,'kJ/mol'), E0=(130.061,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=9.559147155637328, var=77.61705011266918, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_Ext-2C-R_N-3BrClFO->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_Ext-2C-R_N-3BrClFO->F
    Total Standard Deviation in ln(k): 41.679781809116825"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_Ext-2C-R_N-3BrClFO->F
Total Standard Deviation in ln(k): 41.679781809116825""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_2R->C_Ext-2C-R_N-3BrClFO->F
Total Standard Deviation in ln(k): 41.679781809116825
""",
)

entry(
    index = 342,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R",
    kinetics = Arrhenius(A=(2.00965e+06,'m^3/(mol*s)'), n=0.21575, Ea=(-0.017259,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=1.7760025940622112e-15, var=0.06096442255151172, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 0.49498862827653406"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 0.49498862827653406""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 0.49498862827653406
""",
)

entry(
    index = 343,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_N-Sp-4R!H-3R!H_3R!H-inRing",
    kinetics = Arrhenius(A=(5.781e+11,'m^3/(mol*s)'), n=-1.568, Ea=(1.90246,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_N-Sp-4R!H-3R!H_3R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_N-Sp-4R!H-3R!H_3R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_N-Sp-4R!H-3R!H_3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_N-Sp-4R!H-3R!H_3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 344,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_N-Sp-4R!H-3R!H_N-3R!H-inRing",
    kinetics = Arrhenius(A=(5.89e+07,'m^3/(mol*s)'), n=-0.278, Ea=(-1.2688,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_N-Sp-4R!H-3R!H_N-3R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_N-Sp-4R!H-3R!H_N-3R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_N-Sp-4R!H-3R!H_N-3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_N-Sp-4R!H-3R!H_N-3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 345,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C_Ext-7C-R_9R!H->C",
    kinetics = Arrhenius(A=(84.5644,'m^3/(mol*s)'), n=1.13056, Ea=(-29.7265,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C_Ext-7C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C_Ext-7C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C_Ext-7C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C_Ext-7C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 346,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C_Ext-7C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(4.17062e+20,'m^3/(mol*s)'), n=-4.18779, w0=(179,'kJ/mol'), E0=(18.8332,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-5.406120673907335, var=0.4013608704252138, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C_Ext-7C-R_N-9R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C_Ext-7C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 14.853278551604962"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C_Ext-7C-R_N-9R!H->C
Total Standard Deviation in ln(k): 14.853278551604962""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C_Ext-7C-R_N-9R!H->C
Total Standard Deviation in ln(k): 14.853278551604962
""",
)

entry(
    index = 347,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_5R!H->C",
    kinetics = Arrhenius(A=(71244.2,'m^3/(mol*s)'), n=0.431733, Ea=(2.77158,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 348,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.18878e+08,'m^3/(mol*s)'), n=-0.0148343, w0=(250.849,'kJ/mol'), E0=(109.023,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4315791726745988, var=5.000196333372009, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 8.079744514557527"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 8.079744514557527""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 8.079744514557527
""",
)

entry(
    index = 349,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(2.85197e+07,'m^3/(mol*s)'), n=0.213787, w0=(205.932,'kJ/mol'), E0=(102.966,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0001268111880925725, var=0.012046587656288507, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 0.22035222491997694"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.22035222491997694""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.22035222491997694
""",
)

entry(
    index = 350,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.89626e+07,'m^3/(mol*s)'), n=0.120172, w0=(205.5,'kJ/mol'), E0=(29.6951,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03119957587204572, var=5.060225472910453, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 4.58803141017077"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.58803141017077""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.58803141017077
""",
)

entry(
    index = 351,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-3C-R",
    kinetics = Arrhenius(A=(1.12e+41,'m^3/(mol*s)'), n=-10.8, Ea=(17.1544,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 352,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(1.7979e+07,'m^3/(mol*s)'), n=0.240345, w0=(205.5,'kJ/mol'), E0=(73.3774,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06239915174409146, var=9.629649721936181e-35, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C
    Total Standard Deviation in ln(k): 0.15678178830173736"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C
Total Standard Deviation in ln(k): 0.15678178830173736""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C
Total Standard Deviation in ln(k): 0.15678178830173736
""",
)

entry(
    index = 353,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_N-Sp-4R!H-2C",
    kinetics = Arrhenius(A=(6.117e+08,'m^3/(mol*s)'), n=-0.152, Ea=(4.19655,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_N-Sp-4R!H-2C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_N-Sp-4R!H-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_N-Sp-4R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_N-Sp-4R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 354,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_Sp-4C=3C",
    kinetics = Arrhenius(A=(2.92e+07,'m^3/(mol*s)'), n=0.18, Ea=(0.518816,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_Sp-4C=3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_Sp-4C=3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_Sp-4C=3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_Sp-4C=3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 355,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C",
    kinetics = ArrheniusBM(A=(2.33349e+09,'m^3/(mol*s)'), n=-0.385433, w0=(210.716,'kJ/mol'), E0=(96.0261,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07132671758377926, var=0.050317170242682015, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C
    Total Standard Deviation in ln(k): 0.6289047882553402"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C
Total Standard Deviation in ln(k): 0.6289047882553402""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C
Total Standard Deviation in ln(k): 0.6289047882553402
""",
)

entry(
    index = 356,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C_Ext-3C-R",
    kinetics = Arrhenius(A=(5e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 357,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(8.23696e+44,'m^3/(mol*s)'), n=-12.5348, w0=(281.452,'kJ/mol'), E0=(271.331,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.653369690823423, var=91.5545029311063, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R
    Total Standard Deviation in ln(k): 28.361451450432206"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 28.361451450432206""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 28.361451450432206
""",
)

entry(
    index = 358,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_5R!H->F",
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 359,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-5R!H->F",
    kinetics = Arrhenius(A=(2.53123,'m^3/(mol*s)'), n=1.5854, Ea=(-8.16465,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_1BrCCl->Cl_Ext-2R-R_N-3R!H->F_3BrCClILiNOPSSi->C_Sp-3C-2R_Ext-2R-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 360,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = Arrhenius(A=(4.00279e+08,'m^3/(mol*s)'), n=-0.187532, Ea=(24.5987,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 361,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = Arrhenius(A=(6.39094e+07,'m^3/(mol*s)'), n=0.182418, Ea=(24.8914,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_4R!H->O_N-5R!H->F_Ext-1BrC-R_Ext-4O-R_Ext-7R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_Ext-4O-R_Ext-8R!H-R_Ext-4O-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 362,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_7R!H->C",
    kinetics = ArrheniusBM(A=(3.89042e+08,'m^3/(mol*s)'), n=-0.664637, w0=(173,'kJ/mol'), E0=(77.3233,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.052990332270374, var=6.00246333854358, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_7R!H->C
    Total Standard Deviation in ln(k): 5.044727478673219"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_7R!H->C
Total Standard Deviation in ln(k): 5.044727478673219""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_7R!H->C
Total Standard Deviation in ln(k): 5.044727478673219
""",
)

entry(
    index = 363,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(1.64502e+10,'m^3/(mol*s)'), n=-0.947062, w0=(173,'kJ/mol'), E0=(80.4021,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.669752047420594, var=3.987652406659628, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_N-7R!H->C
    Total Standard Deviation in ln(k): 5.6860710472759095"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_N-7R!H->C
Total Standard Deviation in ln(k): 5.6860710472759095""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_N-7R!H->C
Total Standard Deviation in ln(k): 5.6860710472759095
""",
)

entry(
    index = 364,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F_Ext-2R-R_7R!H->C",
    kinetics = ArrheniusBM(A=(2.4737e+07,'m^3/(mol*s)'), n=0.118041, w0=(174.143,'kJ/mol'), E0=(87.0716,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.061182966002177805, var=0.5095297529170788, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F_Ext-2R-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F_Ext-2R-R_7R!H->C
    Total Standard Deviation in ln(k): 1.5847330637581272"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F_Ext-2R-R_7R!H->C
Total Standard Deviation in ln(k): 1.5847330637581272""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F_Ext-2R-R_7R!H->C
Total Standard Deviation in ln(k): 1.5847330637581272
""",
)

entry(
    index = 365,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F_Ext-2R-R_N-7R!H->C",
    kinetics = Arrhenius(A=(7.64581e+08,'m^3/(mol*s)'), n=-0.158759, Ea=(6.33508,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F_Ext-2R-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F_Ext-2R-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F_Ext-2R-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F_Ext-2R-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 366,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R",
    kinetics = ArrheniusBM(A=(5.75054e+07,'m^3/(mol*s)'), n=-0.142635, w0=(173,'kJ/mol'), E0=(85.2825,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06439922973369248, var=9.926829852206447, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R
    Total Standard Deviation in ln(k): 6.478100263971311"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R
Total Standard Deviation in ln(k): 6.478100263971311""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R
Total Standard Deviation in ln(k): 6.478100263971311
""",
)

entry(
    index = 367,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R",
    kinetics = ArrheniusBM(A=(0.371325,'m^3/(mol*s)'), n=1.70829, w0=(200.064,'kJ/mol'), E0=(20.0064,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13038991131944436, var=21.185237363048692, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R
    Total Standard Deviation in ln(k): 9.554891932233062"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R
Total Standard Deviation in ln(k): 9.554891932233062""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R
Total Standard Deviation in ln(k): 9.554891932233062
""",
)

entry(
    index = 368,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R",
    kinetics = ArrheniusBM(A=(2.85705e+07,'m^3/(mol*s)'), n=-0.367494, w0=(210.315,'kJ/mol'), E0=(154.009,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17889909401549772, var=0.02696567964378461, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R
    Total Standard Deviation in ln(k): 0.7786973700967077"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R
Total Standard Deviation in ln(k): 0.7786973700967077""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R
Total Standard Deviation in ln(k): 0.7786973700967077
""",
)

entry(
    index = 369,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_5FO->O",
    kinetics = ArrheniusBM(A=(0.180328,'m^3/(mol*s)'), n=1.37709, w0=(196.484,'kJ/mol'), E0=(19.6484,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.563323530864995, var=28.391540293420228, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_5FO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_5FO->O
    Total Standard Deviation in ln(k): 12.097358527940985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_5FO->O
Total Standard Deviation in ln(k): 12.097358527940985""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_5FO->O
Total Standard Deviation in ln(k): 12.097358527940985
""",
)

entry(
    index = 370,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O",
    kinetics = ArrheniusBM(A=(35025.7,'m^3/(mol*s)'), n=0.424706, w0=(187.277,'kJ/mol'), E0=(67.9657,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0468579876863326, var=17.3425007913932, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O
    Total Standard Deviation in ln(k): 10.978881022217733"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O
Total Standard Deviation in ln(k): 10.978881022217733""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O
Total Standard Deviation in ln(k): 10.978881022217733
""",
)

entry(
    index = 371,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R",
    kinetics = ArrheniusBM(A=(905756,'m^3/(mol*s)'), n=0.256125, w0=(196.794,'kJ/mol'), E0=(98.3971,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.012876425458037171, var=2.311827348602212, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R
    Total Standard Deviation in ln(k): 3.080491268449495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R
Total Standard Deviation in ln(k): 3.080491268449495""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R
Total Standard Deviation in ln(k): 3.080491268449495
""",
)

entry(
    index = 372,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.35318e+08,'m^3/(mol*s)'), n=-0.589787, w0=(184.714,'kJ/mol'), E0=(70.2572,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22608126766388198, var=1.4611110616166147, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R
    Total Standard Deviation in ln(k): 2.9912955194450035"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 2.9912955194450035""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 2.9912955194450035
""",
)

entry(
    index = 373,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_Ext-6R!H-R",
    kinetics = Arrhenius(A=(0.0678417,'m^3/(mol*s)'), n=2.13578, Ea=(0.502021,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 374,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_6R!H->Cl",
    kinetics = Arrhenius(A=(0.0100139,'m^3/(mol*s)'), n=2.40716, Ea=(-5.46198,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 375,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl",
    kinetics = Arrhenius(A=(2.25166e+09,'m^3/(mol*s)'), n=-0.738949, Ea=(2.10897,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-0.5356916568504199, var=6.013803933967703, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl
    Total Standard Deviation in ln(k): 6.26218247519378"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 6.26218247519378""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 6.26218247519378
""",
)

entry(
    index = 376,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R",
    kinetics = Arrhenius(A=(1.8691e+06,'m^3/(mol*s)'), n=0.2165, Ea=(-0.0258013,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=7.310313707882335e-16, var=0.015184462967774382, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 0.2470339870355229"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.2470339870355229""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.2470339870355229
""",
)

entry(
    index = 377,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R",
    kinetics = Arrhenius(A=(3.406e+06,'m^3/(mol*s)'), n=0.211, Ea=(0.029288,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 378,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C_Ext-7C-R_N-9R!H->C_9BrClFILiNOPSSi->O",
    kinetics = Arrhenius(A=(81.1546,'m^3/(mol*s)'), n=1.08303, Ea=(-54.068,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C_Ext-7C-R_N-9R!H->C_9BrClFILiNOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C_Ext-7C-R_N-9R!H->C_9BrClFILiNOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C_Ext-7C-R_N-9R!H->C_9BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C_Ext-7C-R_N-9R!H->C_9BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 379,
    label = "Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C_Ext-7C-R_N-9R!H->C_N-9BrClFILiNOPSSi->O",
    kinetics = Arrhenius(A=(685.965,'m^3/(mol*s)'), n=0.997658, Ea=(-35.8301,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C_Ext-7C-R_N-9R!H->C_N-9BrClFILiNOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C_Ext-7C-R_N-9R!H->C_N-9BrClFILiNOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C_Ext-7C-R_N-9R!H->C_N-9BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_1BrCClFHNO->O_N-2R->Cl_Ext-1O-R_3R!H->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-3C-R_Ext-4C-R_6R!H->F_N-5BrClFILiNOPSSi->O_N-Sp-4C-3C_Ext-4C-R_Ext-3C-R_Ext-4C-R_Ext-2BrCFHNO-R_7R!H->C_Ext-7C-R_N-9R!H->C_N-9BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 380,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.23581e+08,'m^3/(mol*s)'), n=-0.0122597, w0=(240.454,'kJ/mol'), E0=(116.292,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04140576492585387, var=0.09604153040645416, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 0.7253133723300423"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 0.7253133723300423""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 0.7253133723300423
""",
)

entry(
    index = 381,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.83155e+07,'m^3/(mol*s)'), n=0.213711, w0=(205.927,'kJ/mol'), E0=(102.964,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00015371050914907234, var=0.013218501477439701, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.23087409157092473"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.23087409157092473""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.23087409157092473
""",
)

entry(
    index = 382,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R",
    kinetics = Arrhenius(A=(2.591e+07,'m^3/(mol*s)'), n=0.217, Ea=(-0.033472,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 383,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C",
    kinetics = ArrheniusBM(A=(3.22741e+07,'m^3/(mol*s)'), n=0.213, w0=(211.537,'kJ/mol'), E0=(157.489,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0022644853455516876, var=7.490440640908408e-07, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C
    Total Standard Deviation in ln(k): 0.007424706391292111"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C
Total Standard Deviation in ln(k): 0.007424706391292111""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C
Total Standard Deviation in ln(k): 0.007424706391292111
""",
)

entry(
    index = 384,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C",
    kinetics = ArrheniusBM(A=(1.13248e+10,'m^3/(mol*s)'), n=-0.605871, w0=(209.896,'kJ/mol'), E0=(99.2182,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24067984638975376, var=0.0009950635311885177, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C
    Total Standard Deviation in ln(k): 0.6679618536124501"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 0.6679618536124501""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 0.6679618536124501
""",
)

entry(
    index = 385,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_7R!H->C_Ext-7C-R_8R!H->O",
    kinetics = Arrhenius(A=(197057,'m^3/(mol*s)'), n=0.119659, Ea=(-19.7473,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_7R!H->C_Ext-7C-R_8R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_7R!H->C_Ext-7C-R_8R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_7R!H->C_Ext-7C-R_8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_7R!H->C_Ext-7C-R_8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 386,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_7R!H->C_Ext-7C-R_N-8R!H->O",
    kinetics = Arrhenius(A=(180089,'m^3/(mol*s)'), n=0.450629, Ea=(3.41576,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_7R!H->C_Ext-7C-R_N-8R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_7R!H->C_Ext-7C-R_N-8R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_7R!H->C_Ext-7C-R_N-8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_7R!H->C_Ext-7C-R_N-8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 387,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_N-7R!H->C_7BrClFILiNOPSSi->O",
    kinetics = Arrhenius(A=(481183,'m^3/(mol*s)'), n=0.224437, Ea=(-23.5171,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_N-7R!H->C_7BrClFILiNOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_N-7R!H->C_7BrClFILiNOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_N-7R!H->C_7BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_N-7R!H->C_7BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 388,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_N-7R!H->C_N-7BrClFILiNOPSSi->O",
    kinetics = Arrhenius(A=(4.84859e+06,'m^3/(mol*s)'), n=0.192007, Ea=(3.65191,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_N-7R!H->C_N-7BrClFILiNOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_N-7R!H->C_N-7BrClFILiNOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_N-7R!H->C_N-7BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_6R!H->F_Ext-2R-R_N-7R!H->C_N-7BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 389,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F_Ext-2R-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = Arrhenius(A=(916198,'m^3/(mol*s)'), n=0.509204, Ea=(-2.99682,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F_Ext-2R-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F_Ext-2R-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F_Ext-2R-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F_Ext-2R-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 390,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F_Ext-2R-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(4.35356e+07,'m^3/(mol*s)'), n=0.0666425, Ea=(0.0756698,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F_Ext-2R-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F_Ext-2R-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F_Ext-2R-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_Sp-5R!H=3R!H_N-6R!H->F_Ext-2R-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 391,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_8R!H->O",
    kinetics = Arrhenius(A=(237736,'m^3/(mol*s)'), n=0.692477, Ea=(-25.0162,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_8R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_8R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 392,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O",
    kinetics = ArrheniusBM(A=(147596,'m^3/(mol*s)'), n=0.548893, w0=(179.779,'kJ/mol'), E0=(17.9779,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10339424761176351, var=1.022515806745835, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O
    Total Standard Deviation in ln(k): 2.2869631028653354"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O
Total Standard Deviation in ln(k): 2.2869631028653354""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O
Total Standard Deviation in ln(k): 2.2869631028653354
""",
)

entry(
    index = 393,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C",
    kinetics = ArrheniusBM(A=(2.85929,'m^3/(mol*s)'), n=1.98423, w0=(205.402,'kJ/mol'), E0=(20.5402,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03867085602174627, var=27.594870758813926, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C
    Total Standard Deviation in ln(k): 10.628200754285334"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C
Total Standard Deviation in ln(k): 10.628200754285334""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C
Total Standard Deviation in ln(k): 10.628200754285334
""",
)

entry(
    index = 394,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C",
    kinetics = ArrheniusBM(A=(0.133814,'m^3/(mol*s)'), n=1.57032, w0=(197.395,'kJ/mol'), E0=(19.7395,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.052879414489332054, var=11.762371952363472, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C
    Total Standard Deviation in ln(k): 7.008365341147405"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C
Total Standard Deviation in ln(k): 7.008365341147405""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C
Total Standard Deviation in ln(k): 7.008365341147405
""",
)

entry(
    index = 395,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_9R!H->O",
    kinetics = Arrhenius(A=(1.34728e+10,'m^3/(mol*s)'), n=-1.22262, Ea=(11.1088,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_9R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_9R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 396,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O",
    kinetics = ArrheniusBM(A=(3.67062e+06,'m^3/(mol*s)'), n=-0.0824516, w0=(209.567,'kJ/mol'), E0=(153.552,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17862247164368955, var=0.03179551586641061, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O
    Total Standard Deviation in ln(k): 0.8062704490740156"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O
Total Standard Deviation in ln(k): 0.8062704490740156""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O
Total Standard Deviation in ln(k): 0.8062704490740156
""",
)

entry(
    index = 397,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_5FO->O_Ext-3R!H-R_Ext-2R-R_7R!H->C",
    kinetics = Arrhenius(A=(0.141937,'m^3/(mol*s)'), n=1.2083, Ea=(2.41522,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_5FO->O_Ext-3R!H-R_Ext-2R-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_5FO->O_Ext-3R!H-R_Ext-2R-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_5FO->O_Ext-3R!H-R_Ext-2R-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_5FO->O_Ext-3R!H-R_Ext-2R-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 398,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_5FO->O_Ext-3R!H-R_Ext-2R-R_N-7R!H->C",
    kinetics = Arrhenius(A=(1454.87,'m^3/(mol*s)'), n=0.456325, Ea=(6.95226,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_5FO->O_Ext-3R!H-R_Ext-2R-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_5FO->O_Ext-3R!H-R_Ext-2R-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_5FO->O_Ext-3R!H-R_Ext-2R-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_5FO->O_Ext-3R!H-R_Ext-2R-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 399,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R",
    kinetics = ArrheniusBM(A=(35282.4,'m^3/(mol*s)'), n=0.423859, w0=(187.022,'kJ/mol'), E0=(53.1577,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.020700969309321256, var=7.430368563078625, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R
    Total Standard Deviation in ln(k): 5.5166601714312336"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R
Total Standard Deviation in ln(k): 5.5166601714312336""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R
Total Standard Deviation in ln(k): 5.5166601714312336
""",
)

entry(
    index = 400,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_Sp-8R!H=5CCCOOO",
    kinetics = ArrheniusBM(A=(5.39084e+11,'m^3/(mol*s)'), n=-1.45358, w0=(173,'kJ/mol'), E0=(85.9904,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.242435402323583, var=0.4447136384056189, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_Sp-8R!H=5CCCOOO',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_Sp-8R!H=5CCCOOO
    Total Standard Deviation in ln(k): 6.971154542092778"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_Sp-8R!H=5CCCOOO
Total Standard Deviation in ln(k): 6.971154542092778""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_Sp-8R!H=5CCCOOO
Total Standard Deviation in ln(k): 6.971154542092778
""",
)

entry(
    index = 401,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO",
    kinetics = ArrheniusBM(A=(4437.65,'m^3/(mol*s)'), n=0.940006, w0=(206.719,'kJ/mol'), E0=(20.6719,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18527100189215398, var=1.602420737180559, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO
    Total Standard Deviation in ln(k): 3.00323417645241"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO
Total Standard Deviation in ln(k): 3.00323417645241""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO
Total Standard Deviation in ln(k): 3.00323417645241
""",
)

entry(
    index = 402,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_6R!H->Br",
    kinetics = Arrhenius(A=(1.4e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_6R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_6R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 403,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br",
    kinetics = ArrheniusBM(A=(4.5555e+09,'m^3/(mol*s)'), n=-0.95052, w0=(185.671,'kJ/mol'), E0=(92.8784,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2676587380100399, var=1.252628762252613, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br
    Total Standard Deviation in ln(k): 2.91622691223769"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br
Total Standard Deviation in ln(k): 2.91622691223769""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br
Total Standard Deviation in ln(k): 2.91622691223769
""",
)

entry(
    index = 404,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_3BrFO->O",
    kinetics = Arrhenius(A=(280652,'m^3/(mol*s)'), n=0.2441, Ea=(0.368356,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_3BrFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_3BrFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_3BrFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_3BrFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 405,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O",
    kinetics = ArrheniusBM(A=(8.49541e+06,'m^3/(mol*s)'), n=0.324043, w0=(205.503,'kJ/mol'), E0=(171.127,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1974905490274071, var=0.727447136363519, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O
    Total Standard Deviation in ln(k): 2.2060562127214265"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O
Total Standard Deviation in ln(k): 2.2060562127214265""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O
Total Standard Deviation in ln(k): 2.2060562127214265
""",
)

entry(
    index = 406,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.81566e+06,'m^3/(mol*s)'), n=0.214796, w0=(183.599,'kJ/mol'), E0=(130.735,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.01902268217608238, var=0.07674911577845785, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.603180087597218"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.603180087597218""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.603180087597218
""",
)

entry(
    index = 407,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R",
    kinetics = Arrhenius(A=(1.918e+06,'m^3/(mol*s)'), n=0.213, Ea=(-0.004184,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 408,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R_5BrClF->Br",
    kinetics = Arrhenius(A=(1.12e+41,'m^3/(mol*s)'), n=-10.8, Ea=(17.1544,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R_5BrClF->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R_5BrClF->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R_5BrClF->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R_5BrClF->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 409,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R_N-5BrClF->Br",
    kinetics = ArrheniusBM(A=(4.37465e+07,'m^3/(mol*s)'), n=0.123754, w0=(238.943,'kJ/mol'), E0=(110.157,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08217907185790596, var=0.11332476336323197, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R_N-5BrClF->Br',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R_N-5BrClF->Br
    Total Standard Deviation in ln(k): 0.8813489564969024"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R_N-5BrClF->Br
Total Standard Deviation in ln(k): 0.8813489564969024""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R_N-5BrClF->Br
Total Standard Deviation in ln(k): 0.8813489564969024
""",
)

entry(
    index = 410,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(2.79114e+07,'m^3/(mol*s)'), n=0.21356, w0=(205.917,'kJ/mol'), E0=(102.959,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00020750925767200467, var=0.015290320310696642, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 0.24841496097505852"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 0.24841496097505852""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 0.24841496097505852
""",
)

entry(
    index = 411,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R",
    kinetics = Arrhenius(A=(2.591e+07,'m^3/(mol*s)'), n=0.217, Ea=(-0.033472,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 412,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R",
    kinetics = Arrhenius(A=(3.203e+07,'m^3/(mol*s)'), n=0.214, Ea=(0.012552,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 413,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O_8BrCClFILiNPSSi->C",
    kinetics = Arrhenius(A=(944394,'m^3/(mol*s)'), n=0.330618, Ea=(7.97806,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O_8BrCClFILiNPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O_8BrCClFILiNPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O_8BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O_8BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 414,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O_N-8BrCClFILiNPSSi->C",
    kinetics = ArrheniusBM(A=(2.42892e+06,'m^3/(mol*s)'), n=0.194056, w0=(174.419,'kJ/mol'), E0=(87.2094,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3809311792207462, var=0.5293797909500807, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O_N-8BrCClFILiNPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O_N-8BrCClFILiNPSSi->C
    Total Standard Deviation in ln(k): 2.415728492286467"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O_N-8BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 2.415728492286467""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O_N-8BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 2.415728492286467
""",
)

entry(
    index = 415,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C_Ext-5C-R_9R!H->O",
    kinetics = ArrheniusBM(A=(1147.6,'m^3/(mol*s)'), n=1.03136, w0=(209.28,'kJ/mol'), E0=(144.783,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.6233907935562677, var=1.4465669663933907, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C_Ext-5C-R_9R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C_Ext-5C-R_9R!H->O
    Total Standard Deviation in ln(k): 6.490032622042338"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C_Ext-5C-R_9R!H->O
Total Standard Deviation in ln(k): 6.490032622042338""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C_Ext-5C-R_9R!H->O
Total Standard Deviation in ln(k): 6.490032622042338
""",
)

entry(
    index = 416,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C_Ext-5C-R_N-9R!H->O",
    kinetics = Arrhenius(A=(1.22377e+06,'m^3/(mol*s)'), n=0.784573, Ea=(3.00931,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C_Ext-5C-R_N-9R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C_Ext-5C-R_N-9R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C_Ext-5C-R_N-9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C_Ext-5C-R_N-9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 417,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_8R!H->C",
    kinetics = Arrhenius(A=(2842.4,'m^3/(mol*s)'), n=0.906541, Ea=(7.76797,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 418,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C",
    kinetics = ArrheniusBM(A=(0.0779399,'m^3/(mol*s)'), n=1.52237, w0=(196.335,'kJ/mol'), E0=(19.6335,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04633266137586713, var=6.945109454309883, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C
    Total Standard Deviation in ln(k): 5.3996074584516"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C
Total Standard Deviation in ln(k): 5.3996074584516""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C
Total Standard Deviation in ln(k): 5.3996074584516
""",
)

entry(
    index = 419,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_10R!H->O",
    kinetics = Arrhenius(A=(7.45304e+06,'m^3/(mol*s)'), n=-0.171776, Ea=(9.24705,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_10R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_10R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_10R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_10R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 420,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O",
    kinetics = ArrheniusBM(A=(2.57598e+06,'m^3/(mol*s)'), n=-0.0377893, w0=(209.931,'kJ/mol'), E0=(153.775,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1778845539198786, var=0.0007559642205645908, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O
    Total Standard Deviation in ln(k): 3.01462872650812"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O
Total Standard Deviation in ln(k): 3.01462872650812""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O
Total Standard Deviation in ln(k): 3.01462872650812
""",
)

entry(
    index = 421,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_Sp-8R!H=2R",
    kinetics = ArrheniusBM(A=(1.02727e+07,'m^3/(mol*s)'), n=0.120037, w0=(177.745,'kJ/mol'), E0=(88.8724,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.34899392453896144, var=0.0009823616656770534, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_Sp-8R!H=2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_Sp-8R!H=2R
    Total Standard Deviation in ln(k): 0.9397028656203279"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_Sp-8R!H=2R
Total Standard Deviation in ln(k): 0.9397028656203279""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_Sp-8R!H=2R
Total Standard Deviation in ln(k): 0.9397028656203279
""",
)

entry(
    index = 422,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R",
    kinetics = ArrheniusBM(A=(11343.1,'m^3/(mol*s)'), n=0.484624, w0=(188.878,'kJ/mol'), E0=(18.8878,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.01844505859052364, var=5.234916713732423, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R
    Total Standard Deviation in ln(k): 4.63316627132902"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R
Total Standard Deviation in ln(k): 4.63316627132902""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R
Total Standard Deviation in ln(k): 4.63316627132902
""",
)

entry(
    index = 423,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_Sp-8R!H=5CCCOOO_8R!H->C",
    kinetics = Arrhenius(A=(416.944,'m^3/(mol*s)'), n=1.13547, Ea=(-25.4956,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_Sp-8R!H=5CCCOOO_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_Sp-8R!H=5CCCOOO_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_Sp-8R!H=5CCCOOO_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_Sp-8R!H=5CCCOOO_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 424,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_Sp-8R!H=5CCCOOO_N-8R!H->C",
    kinetics = Arrhenius(A=(507407,'m^3/(mol*s)'), n=0.294589, Ea=(-11.7938,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_Sp-8R!H=5CCCOOO_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_Sp-8R!H=5CCCOOO_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_Sp-8R!H=5CCCOOO_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_Sp-8R!H=5CCCOOO_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 425,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C",
    kinetics = ArrheniusBM(A=(5674.88,'m^3/(mol*s)'), n=0.853744, w0=(206.598,'kJ/mol'), E0=(20.6598,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0868486392625791, var=1.90892715576028, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C
    Total Standard Deviation in ln(k): 2.9880334308107153"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C
Total Standard Deviation in ln(k): 2.9880334308107153""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C
Total Standard Deviation in ln(k): 2.9880334308107153
""",
)

entry(
    index = 426,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_N-8R!H->C",
    kinetics = Arrhenius(A=(85564.3,'m^3/(mol*s)'), n=0.794442, Ea=(4.21806,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 427,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_6CClFILiNOPSSi->Cl",
    kinetics = ArrheniusBM(A=(9.20789e+07,'m^3/(mol*s)'), n=-0.490944, w0=(177.136,'kJ/mol'), E0=(48.2739,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23113352765054698, var=0.7850791001606107, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_6CClFILiNOPSSi->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_6CClFILiNOPSSi->Cl
    Total Standard Deviation in ln(k): 2.357026797306611"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_6CClFILiNOPSSi->Cl
Total Standard Deviation in ln(k): 2.357026797306611""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_6CClFILiNOPSSi->Cl
Total Standard Deviation in ln(k): 2.357026797306611
""",
)

entry(
    index = 428,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_N-6CClFILiNOPSSi->Cl",
    kinetics = ArrheniusBM(A=(1.99254e+10,'m^3/(mol*s)'), n=-1.08237, w0=(202.741,'kJ/mol'), E0=(25.6248,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0315988796402227, var=1.243853587150575, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_N-6CClFILiNOPSSi->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_N-6CClFILiNOPSSi->Cl
    Total Standard Deviation in ln(k): 4.827801613908829"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_N-6CClFILiNOPSSi->Cl
Total Standard Deviation in ln(k): 4.827801613908829""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_N-6CClFILiNOPSSi->Cl
Total Standard Deviation in ln(k): 4.827801613908829
""",
)

entry(
    index = 429,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_6BrCFO->Br",
    kinetics = Arrhenius(A=(2.8e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_6BrCFO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_6BrCFO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_6BrCFO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_6BrCFO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 430,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br",
    kinetics = ArrheniusBM(A=(4.4839e+07,'m^3/(mol*s)'), n=0.118212, w0=(210.143,'kJ/mol'), E0=(158.477,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16305686506191244, var=0.6677410384573004, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br
    Total Standard Deviation in ln(k): 2.047868367751913"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br
Total Standard Deviation in ln(k): 2.047868367751913""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br
Total Standard Deviation in ln(k): 2.047868367751913
""",
)

entry(
    index = 431,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(1.71759e+06,'m^3/(mol*s)'), n=0.2141, w0=(183.528,'kJ/mol'), E0=(114.22,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00201287586271257, var=0.002762656896728525, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 0.11042832265502585"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.11042832265502585""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-3R!H-R_N-Sp-3R!H=1BrBrCC_Ext-2R-R_N-Sp-4R!H=3R!H_Sp-4R!H-3R!H_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.11042832265502585
""",
)

entry(
    index = 432,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R_N-5BrClF->Br_5ClF->Cl",
    kinetics = Arrhenius(A=(1.12e+41,'m^3/(mol*s)'), n=-10.8, Ea=(17.1544,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R_N-5BrClF->Br_5ClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R_N-5BrClF->Br_5ClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R_N-5BrClF->Br_5ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R_N-5BrClF->Br_5ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 433,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R_N-5BrClF->Br_N-5ClF->Cl",
    kinetics = ArrheniusBM(A=(5.03719e+06,'m^3/(mol*s)'), n=0.399582, w0=(235.273,'kJ/mol'), E0=(105.031,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.7019201706267022, var=0.744437441521291, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R_N-5BrClF->Br_N-5ClF->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R_N-5BrClF->Br_N-5ClF->Cl
    Total Standard Deviation in ln(k): 6.005882559655709"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R_N-5BrClF->Br_N-5ClF->Cl
Total Standard Deviation in ln(k): 6.005882559655709""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_Ext-2C-R_Ext-4C-R_N-5R!H->C_Ext-4C-R_N-5BrClF->Br_N-5ClF->Cl
Total Standard Deviation in ln(k): 6.005882559655709
""",
)

entry(
    index = 434,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(2.67335e+07,'m^3/(mol*s)'), n=0.213107, w0=(205.888,'kJ/mol'), E0=(102.944,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004025751725425149, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 0.010114954083982785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.010114954083982785""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_1BrCClHN->H_N-2R->N_N-2BrCClH->H_Ext-2C-R_N-3R!H->F_3BrCClILiNOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.010114954083982785
""",
)

entry(
    index = 435,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O_N-8BrCClFILiNPSSi->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_9R!H->O",
    kinetics = Arrhenius(A=(123727,'m^3/(mol*s)'), n=0.557494, Ea=(-8.28865,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O_N-8BrCClFILiNPSSi->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_9R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O_N-8BrCClFILiNPSSi->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_9R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O_N-8BrCClFILiNPSSi->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O_N-8BrCClFILiNPSSi->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 436,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O_N-8BrCClFILiNPSSi->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-9R!H->O",
    kinetics = Arrhenius(A=(127888,'m^3/(mol*s)'), n=0.567397, Ea=(1.95417,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O_N-8BrCClFILiNPSSi->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-9R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O_N-8BrCClFILiNPSSi->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-9R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O_N-8BrCClFILiNPSSi->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_Sp-7R!H=2R_Ext-5C-R_N-8R!H->O_N-8BrCClFILiNPSSi->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 437,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C_Ext-5C-R_9R!H->O_7R!H->C",
    kinetics = Arrhenius(A=(389.12,'m^3/(mol*s)'), n=1.13144, Ea=(10.4702,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C_Ext-5C-R_9R!H->O_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C_Ext-5C-R_9R!H->O_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C_Ext-5C-R_9R!H->O_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C_Ext-5C-R_9R!H->O_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 438,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C_Ext-5C-R_9R!H->O_N-7R!H->C",
    kinetics = Arrhenius(A=(74400,'m^3/(mol*s)'), n=0.546769, Ea=(16.5251,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C_Ext-5C-R_9R!H->O_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C_Ext-5C-R_9R!H->O_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C_Ext-5C-R_9R!H->O_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_Sp-8R!H=5C_Ext-5C-R_9R!H->O_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 439,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_8FO->O",
    kinetics = Arrhenius(A=(0.413045,'m^3/(mol*s)'), n=1.07287, Ea=(10.2039,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_8FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_8FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_8FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_8FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 440,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O",
    kinetics = ArrheniusBM(A=(0.557554,'m^3/(mol*s)'), n=1.33804, w0=(194.132,'kJ/mol'), E0=(19.4132,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04590006118590477, var=5.163318506701904, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O
    Total Standard Deviation in ln(k): 4.670673606222"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O
Total Standard Deviation in ln(k): 4.670673606222""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O
Total Standard Deviation in ln(k): 4.670673606222
""",
)

entry(
    index = 441,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O_Sp-8R!H-7R!H",
    kinetics = Arrhenius(A=(3.77114e+06,'m^3/(mol*s)'), n=-0.0927661, Ea=(9.97811,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O_Sp-8R!H-7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O_Sp-8R!H-7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O_Sp-8R!H-7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O_Sp-8R!H-7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 442,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O_N-Sp-8R!H-7R!H",
    kinetics = Arrhenius(A=(1.75959e+06,'m^3/(mol*s)'), n=0.0171875, Ea=(9.60887,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O_N-Sp-8R!H-7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O_N-Sp-8R!H-7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O_N-Sp-8R!H-7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_Ext-5FO-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-9R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-9R!H->O_Ext-8R!H-R_Ext-7R!H-R_N-10R!H->O_N-Sp-8R!H-7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 443,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_Sp-8R!H=2R_Ext-3R!H-R_Ext-2R-R_9R!H->O",
    kinetics = Arrhenius(A=(541327,'m^3/(mol*s)'), n=0.474199, Ea=(-5.01127,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_Sp-8R!H=2R_Ext-3R!H-R_Ext-2R-R_9R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_Sp-8R!H=2R_Ext-3R!H-R_Ext-2R-R_9R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_Sp-8R!H=2R_Ext-3R!H-R_Ext-2R-R_9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_Sp-8R!H=2R_Ext-3R!H-R_Ext-2R-R_9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 444,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_Sp-8R!H=2R_Ext-3R!H-R_Ext-2R-R_N-9R!H->O",
    kinetics = Arrhenius(A=(858971,'m^3/(mol*s)'), n=0.440882, Ea=(-0.792132,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_Sp-8R!H=2R_Ext-3R!H-R_Ext-2R-R_N-9R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_Sp-8R!H=2R_Ext-3R!H-R_Ext-2R-R_N-9R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_Sp-8R!H=2R_Ext-3R!H-R_Ext-2R-R_N-9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_Sp-8R!H=2R_Ext-3R!H-R_Ext-2R-R_N-9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 445,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_8R!H->C",
    kinetics = ArrheniusBM(A=(30.6005,'m^3/(mol*s)'), n=0.940209, w0=(182.657,'kJ/mol'), E0=(91.3287,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21352708557922928, var=4.366091122090997, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_8R!H->C
    Total Standard Deviation in ln(k): 4.7254329547316125"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_8R!H->C
Total Standard Deviation in ln(k): 4.7254329547316125""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_8R!H->C
Total Standard Deviation in ln(k): 4.7254329547316125
""",
)

entry(
    index = 446,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(49771.8,'m^3/(mol*s)'), n=0.370727, w0=(190.433,'kJ/mol'), E0=(19.0433,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.004539761510313343, var=3.282733297506782, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C
    Total Standard Deviation in ln(k): 3.6436485502651594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C
Total Standard Deviation in ln(k): 3.6436485502651594""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C
Total Standard Deviation in ln(k): 3.6436485502651594
""",
)

entry(
    index = 447,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_9R!H->O",
    kinetics = Arrhenius(A=(5.66199e+07,'m^3/(mol*s)'), n=-0.275895, Ea=(0.00141486,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_9R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_9R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 448,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_N-9R!H->O",
    kinetics = ArrheniusBM(A=(251455,'m^3/(mol*s)'), n=0.37662, w0=(208.552,'kJ/mol'), E0=(177.691,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04970361892258147, var=0.37018495806559254, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_N-9R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_N-9R!H->O
    Total Standard Deviation in ln(k): 1.3446209568262135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_N-9R!H->O
Total Standard Deviation in ln(k): 1.3446209568262135""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_N-9R!H->O
Total Standard Deviation in ln(k): 1.3446209568262135
""",
)

entry(
    index = 449,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_6CClFILiNOPSSi->Cl_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2876.88,'m^3/(mol*s)'), n=0.997885, w0=(173,'kJ/mol'), E0=(12.9133,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10793957791833532, var=0.9828639804840739, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_6CClFILiNOPSSi->Cl_Ext-2C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_6CClFILiNOPSSi->Cl_Ext-2C-R
    Total Standard Deviation in ln(k): 2.2586892354308965"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_6CClFILiNOPSSi->Cl_Ext-2C-R
Total Standard Deviation in ln(k): 2.2586892354308965""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_6CClFILiNOPSSi->Cl_Ext-2C-R
Total Standard Deviation in ln(k): 2.2586892354308965
""",
)

entry(
    index = 450,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_N-6CClFILiNOPSSi->Cl_4R!H->F",
    kinetics = Arrhenius(A=(2.61e+20,'m^3/(mol*s)'), n=-4.16, Ea=(17.1544,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_N-6CClFILiNOPSSi->Cl_4R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_N-6CClFILiNOPSSi->Cl_4R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_N-6CClFILiNOPSSi->Cl_4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_N-6CClFILiNOPSSi->Cl_4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 451,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_N-6CClFILiNOPSSi->Cl_N-4R!H->F",
    kinetics = Arrhenius(A=(1.4e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_N-6CClFILiNOPSSi->Cl_N-4R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_N-6CClFILiNOPSSi->Cl_N-4R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_N-6CClFILiNOPSSi->Cl_N-4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_N-6CClFILiNOPSSi->Cl_N-4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 452,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br_Ext-2R-R",
    kinetics = ArrheniusBM(A=(3.13932e+10,'m^3/(mol*s)'), n=-0.695046, w0=(220.099,'kJ/mol'), E0=(175.922,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15756379792555247, var=0.6734742355060853, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br_Ext-2R-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br_Ext-2R-R
    Total Standard Deviation in ln(k): 2.0410843237968876"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br_Ext-2R-R
Total Standard Deviation in ln(k): 2.0410843237968876""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br_Ext-2R-R
Total Standard Deviation in ln(k): 2.0410843237968876
""",
)

entry(
    index = 453,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O_7R!H->O",
    kinetics = Arrhenius(A=(0.306352,'m^3/(mol*s)'), n=1.17601, Ea=(-2.8366,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O_7R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O_7R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 454,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O_N-7R!H->O",
    kinetics = ArrheniusBM(A=(0.281275,'m^3/(mol*s)'), n=1.50202, w0=(197.291,'kJ/mol'), E0=(19.7291,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05015533332238522, var=6.710368711641281, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O_N-7R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O_N-7R!H->O
    Total Standard Deviation in ln(k): 5.319160225945693"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O_N-7R!H->O
Total Standard Deviation in ln(k): 5.319160225945693""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O_N-7R!H->O
Total Standard Deviation in ln(k): 5.319160225945693
""",
)

entry(
    index = 455,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_8R!H->C_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R",
    kinetics = Arrhenius(A=(11.0219,'m^3/(mol*s)'), n=1.16221, Ea=(-1.66303,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_8R!H->C_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_8R!H->C_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_8R!H->C_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_8R!H->C_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R_Ext-8C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 456,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(71679.7,'m^3/(mol*s)'), n=0.325726, w0=(188.912,'kJ/mol'), E0=(18.8912,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.014144830600174206, var=3.9915268317474983, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R
    Total Standard Deviation in ln(k): 4.040761064485017"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R
Total Standard Deviation in ln(k): 4.040761064485017""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R
Total Standard Deviation in ln(k): 4.040761064485017
""",
)

entry(
    index = 457,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_N-9R!H->O_Ext-1BrC-R",
    kinetics = Arrhenius(A=(81866.3,'m^3/(mol*s)'), n=0.493654, Ea=(8.7441,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_N-9R!H->O_Ext-1BrC-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_N-9R!H->O_Ext-1BrC-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_N-9R!H->O_Ext-1BrC-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_N-9R!H->O_Ext-1BrC-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 458,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_N-9R!H->O_9BrCClFILiNPSSi->C",
    kinetics = Arrhenius(A=(7227.51,'m^3/(mol*s)'), n=0.781616, Ea=(-0.315326,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_N-9R!H->O_9BrCClFILiNPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_N-9R!H->O_9BrCClFILiNPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_N-9R!H->O_9BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_N-9R!H->O_9BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 459,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_N-9R!H->O_N-9BrCClFILiNPSSi->C",
    kinetics = Arrhenius(A=(57189.5,'m^3/(mol*s)'), n=0.620146, Ea=(7.00629,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_N-9R!H->O_N-9BrCClFILiNPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_N-9R!H->O_N-9BrCClFILiNPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_N-9R!H->O_N-9BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_N-5R!H->F_Ext-2R-R_N-6R!H->O_Ext-2R-R_Ext-5CO-R_N-Sp-8R!H=5CCCOOO_8R!H->C_Ext-8C-R_N-9R!H->O_N-9BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 460,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_6CClFILiNOPSSi->Cl_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(264672,'m^3/(mol*s)'), n=0.381484, w0=(173,'kJ/mol'), E0=(73.7349,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0385813605207859, var=0.9147642637194552, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_6CClFILiNOPSSi->Cl_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_6CClFILiNOPSSi->Cl_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 4.526895878994785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_6CClFILiNOPSSi->Cl_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 4.526895878994785""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_3BrClFO->Cl_2R->C_Ext-2C-R_N-6R!H->Br_6CClFILiNOPSSi->Cl_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 4.526895878994785
""",
)

entry(
    index = 461,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br_Ext-2R-R_Ext-2R-R",
    kinetics = Arrhenius(A=(6.69632e+07,'m^3/(mol*s)'), n=0.134221, Ea=(6.02939,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 462,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br_Ext-2R-R_3BrF->Br",
    kinetics = Arrhenius(A=(2.61e+20,'m^3/(mol*s)'), n=-4.16, Ea=(17.1544,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br_Ext-2R-R_3BrF->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br_Ext-2R-R_3BrF->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br_Ext-2R-R_3BrF->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br_Ext-2R-R_3BrF->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 463,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br_Ext-2R-R_N-3BrF->Br",
    kinetics = ArrheniusBM(A=(3.30464e+07,'m^3/(mol*s)'), n=0.0976065, w0=(220.956,'kJ/mol'), E0=(117.734,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7326914187138508, var=0.5483481349258976, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br_Ext-2R-R_N-3BrF->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br_Ext-2R-R_N-3BrF->Br
    Total Standard Deviation in ln(k): 3.32545021094127"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br_Ext-2R-R_N-3BrF->Br
Total Standard Deviation in ln(k): 3.32545021094127""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_N-Sp-3R!H=1BrBrCC_N-3R!H->C_Ext-1BrC-R_N-3BrClFO->Cl_Ext-2R-R_N-6R!H->Cl_N-3BrFO->O_N-6BrCFO->Br_Ext-2R-R_N-3BrF->Br
Total Standard Deviation in ln(k): 3.32545021094127
""",
)

entry(
    index = 464,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O_N-7R!H->O_Ext-5C-R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(9.06931,'m^3/(mol*s)'), n=1.1352, w0=(191.586,'kJ/mol'), E0=(19.1586,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1301215818317162, var=3.980817371511913, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O_N-7R!H->O_Ext-5C-R_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O_N-7R!H->O_Ext-5C-R_Ext-5C-R
    Total Standard Deviation in ln(k): 4.326783226445225"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O_N-7R!H->O_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 4.326783226445225""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O_N-7R!H->O_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 4.326783226445225
""",
)

entry(
    index = 465,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(109830,'m^3/(mol*s)'), n=0.272314, w0=(187.65,'kJ/mol'), E0=(18.765,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.022057064007694367, var=5.085927510381345, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 4.576498514422694"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 4.576498514422694""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 4.576498514422694
""",
)

entry(
    index = 466,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O_N-7R!H->O_Ext-5C-R_Ext-5C-R_Ext-3R!H-R_Ext-2R-R_Ext-2R-R",
    kinetics = Arrhenius(A=(44.3716,'m^3/(mol*s)'), n=1.03011, Ea=(1.319,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O_N-7R!H->O_Ext-5C-R_Ext-5C-R_Ext-3R!H-R_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O_N-7R!H->O_Ext-5C-R_Ext-5C-R_Ext-3R!H-R_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O_N-7R!H->O_Ext-5C-R_Ext-5C-R_Ext-3R!H-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R_N-Sp-7R!H=2R_Ext-5C-R_N-Sp-8R!H=5C_N-8R!H->C_N-8FO->O_N-7R!H->O_Ext-5C-R_Ext-5C-R_Ext-3R!H-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 467,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O",
    kinetics = ArrheniusBM(A=(154826,'m^3/(mol*s)'), n=0.176829, w0=(185.546,'kJ/mol'), E0=(92.7728,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07195271189044192, var=5.563481983228901, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O
    Total Standard Deviation in ln(k): 4.90936125938185"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O
Total Standard Deviation in ln(k): 4.90936125938185""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O
Total Standard Deviation in ln(k): 4.90936125938185
""",
)

entry(
    index = 468,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_N-8FO->O",
    kinetics = Arrhenius(A=(130719,'m^3/(mol*s)'), n=0.51445, Ea=(2.02294,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_N-8FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_N-8FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_N-8FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_N-8FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 469,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R",
    kinetics = ArrheniusBM(A=(430556,'m^3/(mol*s)'), n=0.116778, w0=(184.13,'kJ/mol'), E0=(92.065,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.051904019835314244, var=4.4161773666217154, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R
    Total Standard Deviation in ln(k): 4.343303308340342"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R
Total Standard Deviation in ln(k): 4.343303308340342""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R
Total Standard Deviation in ln(k): 4.343303308340342
""",
)

entry(
    index = 470,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_Sp-13R!H=12R!H",
    kinetics = ArrheniusBM(A=(9.02905e+08,'m^3/(mol*s)'), n=-0.852379, w0=(173,'kJ/mol'), E0=(83.1199,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.956988810098823, var=0.0010566644618766367, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_Sp-13R!H=12R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_Sp-13R!H=12R!H
    Total Standard Deviation in ln(k): 4.982223983433251"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_Sp-13R!H=12R!H
Total Standard Deviation in ln(k): 4.982223983433251""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_Sp-13R!H=12R!H
Total Standard Deviation in ln(k): 4.982223983433251
""",
)

entry(
    index = 471,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_N-Sp-13R!H=12R!H",
    kinetics = ArrheniusBM(A=(205.313,'m^3/(mol*s)'), n=1.08594, w0=(202.02,'kJ/mol'), E0=(20.202,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8241630850652075, var=10.907050630090554, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_N-Sp-13R!H=12R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_N-Sp-13R!H=12R!H
    Total Standard Deviation in ln(k): 8.691564340344877"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_N-Sp-13R!H=12R!H
Total Standard Deviation in ln(k): 8.691564340344877""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_N-Sp-13R!H=12R!H
Total Standard Deviation in ln(k): 8.691564340344877
""",
)

entry(
    index = 472,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_Sp-13R!H=12R!H_13R!H->C",
    kinetics = Arrhenius(A=(12.7316,'m^3/(mol*s)'), n=1.40048, Ea=(-22.3744,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_Sp-13R!H=12R!H_13R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_Sp-13R!H=12R!H_13R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_Sp-13R!H=12R!H_13R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_Sp-13R!H=12R!H_13R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 473,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_Sp-13R!H=12R!H_N-13R!H->C",
    kinetics = Arrhenius(A=(3939.75,'m^3/(mol*s)'), n=0.679875, Ea=(-10.1683,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_Sp-13R!H=12R!H_N-13R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_Sp-13R!H=12R!H_N-13R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_Sp-13R!H=12R!H_N-13R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_Sp-13R!H=12R!H_N-13R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 474,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_N-Sp-13R!H=12R!H_Ext-13R!H-R_14R!H->O",
    kinetics = Arrhenius(A=(1.66595e+07,'m^3/(mol*s)'), n=-0.290889, Ea=(2.29379,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_N-Sp-13R!H=12R!H_Ext-13R!H-R_14R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_N-Sp-13R!H=12R!H_Ext-13R!H-R_14R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_N-Sp-13R!H=12R!H_Ext-13R!H-R_14R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_N-Sp-13R!H=12R!H_Ext-13R!H-R_14R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 475,
    label = "Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_N-Sp-13R!H=12R!H_Ext-13R!H-R_N-14R!H->O",
    kinetics = Arrhenius(A=(926.405,'m^3/(mol*s)'), n=0.868703, Ea=(11.4112,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_N-Sp-13R!H=12R!H_Ext-13R!H-R_N-14R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_N-Sp-13R!H=12R!H_Ext-13R!H-R_N-14R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_N-Sp-13R!H=12R!H_Ext-13R!H-R_N-14R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R-inRing_N-1R->S_N-1BrCClFHNO->O_N-1BrCClFHN->F_N-1BrCClHN->H_N-1BrCClN->N_N-1BrCCl->Cl_Ext-1BrC-R_Ext-1BrC-R_Ext-3R!H-R_N-4R!H->O_Ext-3R!H-R_N-Sp-5R!H=3R!H_N-5R!H->C_N-5FO->O_Ext-1BrC-R_Ext-2R-R_N-Sp-8R!H=2R_N-8R!H->C_Ext-3R!H-R_Ext-2R-R_Ext-2R-R_8FO->O_Ext-8O-R_Ext-12R!H-R_N-Sp-13R!H=12R!H_Ext-13R!H-R_N-14R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

