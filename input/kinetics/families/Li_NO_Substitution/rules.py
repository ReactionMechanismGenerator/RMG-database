#!/usr/bin/env python
# encoding: utf-8

name = "Li_NO_Substitution/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(7.97763e+29,'m^3/(mol*s)'), n=-6.04468, w0=(344168,'J/mol'), E0=(110839,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5458441168724937, var=20.203373378765544, Tref=1000.0, N=19, data_mean=0.0, correlation='Root',), solute=SoluteData(S=-0.010565736153913763,B=-0.7253649083879653,E=1.386083637455815,L=6.8165930491637114,A=-1.435888442285531,comment=''), comment="""BM rule fitted to 19 training reactions at node Root
    Total Standard Deviation in ln(k): 10.382383490573236"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root
Total Standard Deviation in ln(k): 10.382383490573236""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root
Total Standard Deviation in ln(k): 10.382383490573236
""",
)

entry(
    index = 2,
    label = "Root_1NO->O",
    kinetics = ArrheniusBM(A=(9.10449e+09,'m^3/(mol*s)'), n=-0.313758, w0=(366633,'J/mol'), E0=(72889.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1611463542360044, var=21.210502202651398, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1NO->O',), solute=SoluteData(S=-0.4736115191982454,B=1.9540822112356036,E=-0.5427233500319099,L=7.130596504385032,A=-1.2432131195339278,comment=''), comment="""BM rule fitted to 9 training reactions at node Root_1NO->O
    Total Standard Deviation in ln(k): 9.637669867210764"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1NO->O
Total Standard Deviation in ln(k): 9.637669867210764""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1NO->O
Total Standard Deviation in ln(k): 9.637669867210764
""",
)

entry(
    index = 3,
    label = "Root_N-1NO->O",
    kinetics = ArrheniusBM(A=(1.34182e+36,'m^3/(mol*s)'), n=-7.84383, w0=(323950,'J/mol'), E0=(115771,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5940410723380585, var=21.164744873534378, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1NO->O',), solute=SoluteData(S=0.3135663119771183,B=-2.600977892124463,E=2.7362485286972222,L=6.596790630508785,A=-1.5707611682116538,comment=''), comment="""BM rule fitted to 10 training reactions at node Root_N-1NO->O
    Total Standard Deviation in ln(k): 10.715380742793819"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1NO->O
Total Standard Deviation in ln(k): 10.715380742793819""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1NO->O
Total Standard Deviation in ln(k): 10.715380742793819
""",
)

entry(
    index = 4,
    label = "Root_1NO->O_Ext-3R-R",
    kinetics = ArrheniusBM(A=(3.63405e+06,'m^3/(mol*s)'), n=0.555377, w0=(366633,'J/mol'), E0=(69161,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.054212270522640466, var=102.09950648040343, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1NO->O_Ext-3R-R',), solute=SoluteData(S=-4.612069846769863,B=6.379083530822041,E=-2.48216933532115,L=17.971289996005464,A=-3.5664728220181066,comment=''), comment="""BM rule fitted to 3 training reactions at node Root_1NO->O_Ext-3R-R
    Total Standard Deviation in ln(k): 20.392917077921744"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1NO->O_Ext-3R-R
Total Standard Deviation in ln(k): 20.392917077921744""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1NO->O_Ext-3R-R
Total Standard Deviation in ln(k): 20.392917077921744
""",
)

entry(
    index = 5,
    label = "Root_1NO->O_3R->C",
    kinetics = ArrheniusBM(A=(1.68239e+12,'m^3/(mol*s)'), n=-0.883108, w0=(366633,'J/mol'), E0=(77852.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09280652235482556, var=38.908608547879545, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1NO->O_3R->C',), solute=SoluteData(S=0.9150724970755462,B=-0.16182584467440603,E=0.38665068600989,L=2.216284779857066,A=-0.16508208990362655,comment=''), comment="""BM rule fitted to 3 training reactions at node Root_1NO->O_3R->C
    Total Standard Deviation in ln(k): 12.738071166933958"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1NO->O_3R->C
Total Standard Deviation in ln(k): 12.738071166933958""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1NO->O_3R->C
Total Standard Deviation in ln(k): 12.738071166933958
""",
)

entry(
    index = 6,
    label = "Root_1NO->O_N-3R->C",
    kinetics = ArrheniusBM(A=(3.17442e+12,'m^3/(mol*s)'), n=-1.01759, w0=(366633,'J/mol'), E0=(75145.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.18465130592910087, var=26.753910386556523, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1NO->O_N-3R->C',), solute=SoluteData(S=1.3595713550003048,B=0.41468670211798514,E=0.1306579494663836,L=3.1796753263233897,A=-0.413127337631342,comment=''), comment="""BM rule fitted to 3 training reactions at node Root_1NO->O_N-3R->C
    Total Standard Deviation in ln(k): 10.833276273333311"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1NO->O_N-3R->C
Total Standard Deviation in ln(k): 10.833276273333311""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1NO->O_N-3R->C
Total Standard Deviation in ln(k): 10.833276273333311
""",
)

entry(
    index = 7,
    label = "Root_N-1NO->O_Ext-2R-R",
    kinetics = ArrheniusBM(A=(4914.1,'m^3/(mol*s)'), n=1.45953, w0=(303700,'J/mol'), E0=(72713.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.152078718816271, var=9.439366190709487, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1NO->O_Ext-2R-R',), solute=SoluteData(S=0.28057551252457447,B=-0.8246663789161423,E=5.38812625674999,L=-2.0719653167156395,A=0.3282698151699931,comment=''), comment="""BM rule fitted to 2 training reactions at node Root_N-1NO->O_Ext-2R-R
    Total Standard Deviation in ln(k): 6.541365480623387"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1NO->O_Ext-2R-R
Total Standard Deviation in ln(k): 6.541365480623387""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1NO->O_Ext-2R-R
Total Standard Deviation in ln(k): 6.541365480623387
""",
)

entry(
    index = 8,
    label = "Root_N-1NO->O_Ext-1N-R",
    kinetics = ArrheniusBM(A=(3.97301e+35,'m^3/(mol*s)'), n=-7.72356, w0=(330700,'J/mol'), E0=(98644.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4597604209592234, var=18.196341773936673, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1NO->O_Ext-1N-R',), solute=SoluteData(S=0.0913722740670098,B=-3.835487449485473,E=1.767602030374683,L=10.483564935274547,A=-2.3835122888169056,comment=''), comment="""BM rule fitted to 6 training reactions at node Root_N-1NO->O_Ext-1N-R
    Total Standard Deviation in ln(k): 9.706809495929704"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1NO->O_Ext-1N-R
Total Standard Deviation in ln(k): 9.706809495929704""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1NO->O_Ext-1N-R
Total Standard Deviation in ln(k): 9.706809495929704
""",
)

entry(
    index = 9,
    label = "Root_N-1NO->O_2R->C",
    kinetics = Arrhenius(A=(0.0195886,'m^3/(mol*s)'), n=3.14118, Ea=(84.2094,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1NO->O_2R->C',), solute=SoluteData(S=0.4647311008350492,B=-0.6358786386569057,E=2.801006161236384,L=2.7334437301409564,A=-0.9144280152126997,comment=''), comment="""BM rule fitted to 1 training reactions at node Root_N-1NO->O_2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1NO->O_2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1NO->O_2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_N-1NO->O_N-2R->C",
    kinetics = Arrhenius(A=(0.659898,'m^3/(mol*s)'), n=2.58171, Ea=(83.6183,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1NO->O_N-2R->C',), solute=SoluteData(S=1.5615473494849261,B=-0.7116428278426055,E=3.179614429987762,L=4.4770035967308965,A=-1.14864956434239,comment=''), comment="""BM rule fitted to 1 training reactions at node Root_N-1NO->O_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1NO->O_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1NO->O_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_1NO->O_Ext-3R-R_2R->C",
    kinetics = ArrheniusBM(A=(6.40568e-24,'m^3/(mol*s)'), n=9.08157, w0=(349800,'J/mol'), E0=(13091.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.015866472781220723, var=7.6818189250164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1NO->O_Ext-3R-R_2R->C',), solute=SoluteData(S=0.9924180769702984,B=-0.5626434548437547,E=1.2308543810975598,L=1.7706108336453683,A=0.15078931432523807,comment=''), comment="""BM rule fitted to 2 training reactions at node Root_1NO->O_Ext-3R-R_2R->C
    Total Standard Deviation in ln(k): 5.5962081881296575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1NO->O_Ext-3R-R_2R->C
Total Standard Deviation in ln(k): 5.5962081881296575""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1NO->O_Ext-3R-R_2R->C
Total Standard Deviation in ln(k): 5.5962081881296575
""",
)

entry(
    index = 12,
    label = "Root_1NO->O_Ext-3R-R_N-2R->C",
    kinetics = Arrhenius(A=(28.4854,'m^3/(mol*s)'), n=2.01563, Ea=(41.6247,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1NO->O_Ext-3R-R_N-2R->C',), solute=SoluteData(S=-10.216557770510024,B=13.320810516487837,E=-6.195193051739859,L=34.171969158365556,A=-7.2837349583614515,comment=''), comment="""BM rule fitted to 1 training reactions at node Root_1NO->O_Ext-3R-R_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1NO->O_Ext-3R-R_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1NO->O_Ext-3R-R_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_1NO->O_3R->C_Ext-2R-R",
    kinetics = Arrhenius(A=(6.56049e-05,'m^3/(mol*s)'), n=3.90036, Ea=(53.1427,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1NO->O_3R->C_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_1NO->O_3R->C_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1NO->O_3R->C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1NO->O_3R->C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_1NO->O_3R->C_2R->C",
    kinetics = Arrhenius(A=(0.151296,'m^3/(mol*s)'), n=2.99312, Ea=(61.1721,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1NO->O_3R->C_2R->C',), solute=SoluteData(S=1.0238970984530265,B=-0.3025996307928983,E=0.2595121908447656,L=1.6966108246677805,A=-0.015281295369280024,comment=''), comment="""BM rule fitted to 1 training reactions at node Root_1NO->O_3R->C_2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1NO->O_3R->C_2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1NO->O_3R->C_2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_1NO->O_3R->C_N-2R->C",
    kinetics = Arrhenius(A=(3.23504,'m^3/(mol*s)'), n=2.2533, Ea=(40.5055,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1NO->O_3R->C_N-2R->C',), solute=SoluteData(S=0.8062478956980659,B=-0.021052058555913744,E=0.5137891811750144,L=2.735958735046352,A=-0.3148828844379731,comment=''), comment="""BM rule fitted to 1 training reactions at node Root_1NO->O_3R->C_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1NO->O_3R->C_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1NO->O_3R->C_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_1NO->O_N-3R->C_2R->C",
    kinetics = ArrheniusBM(A=(4.84858,'m^3/(mol*s)'), n=2.49415, w0=(349800,'J/mol'), E0=(68008.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06199030811265697, var=0.6767733884365271, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1NO->O_N-3R->C_2R->C',), solute=SoluteData(S=1.3220046813792519,B=0.9177550104512987,E=0.04513290140655837,L=3.840149441710696,A=-0.28757508300632256,comment=''), comment="""BM rule fitted to 2 training reactions at node Root_1NO->O_N-3R->C_2R->C
    Total Standard Deviation in ln(k): 1.8049746693423863"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1NO->O_N-3R->C_2R->C
Total Standard Deviation in ln(k): 1.8049746693423863""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1NO->O_N-3R->C_2R->C
Total Standard Deviation in ln(k): 1.8049746693423863
""",
)

entry(
    index = 17,
    label = "Root_1NO->O_N-3R->C_N-2R->C",
    kinetics = Arrhenius(A=(1667.57,'m^3/(mol*s)'), n=1.38859, Ea=(49.0582,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1NO->O_N-3R->C_N-2R->C',), solute=SoluteData(S=1.4347047022424106,B=-0.591449914548642,E=0.30170804558603403,L=1.858727095548777,A=-0.6642318468813809,comment=''), comment="""BM rule fitted to 1 training reactions at node Root_1NO->O_N-3R->C_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1NO->O_N-3R->C_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1NO->O_N-3R->C_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-1NO->O_Ext-2R-R_Ext-1N-R",
    kinetics = Arrhenius(A=(29.6864,'m^3/(mol*s)'), n=2.19262, Ea=(108.699,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1NO->O_Ext-2R-R_Ext-1N-R',), solute=SoluteData(S=-0.6950335428875951,B=-1.1701886888855062,E=-2.145575219279795,L=0.5523865597784834,A=-0.8229457008818328,comment=''), comment="""BM rule fitted to 1 training reactions at node Root_N-1NO->O_Ext-2R-R_Ext-1N-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1NO->O_Ext-2R-R_Ext-1N-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1NO->O_Ext-2R-R_Ext-1N-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_N-1NO->O_Ext-1N-R_Ext-3R-R",
    kinetics = Arrhenius(A=(0.000854381,'m^3/(mol*s)'), n=3.23101, Ea=(69.319,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1NO->O_Ext-1N-R_Ext-3R-R',), solute=SoluteData(S=0.9762326836232997,B=0.3941281870890212,E=-0.16183134320468961,L=4.026989260299446,A=-0.6740917883591753,comment=''), comment="""BM rule fitted to 1 training reactions at node Root_N-1NO->O_Ext-1N-R_Ext-3R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1NO->O_Ext-1N-R_Ext-3R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1NO->O_Ext-1N-R_Ext-3R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-1NO->O_Ext-1N-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.83741e+33,'m^3/(mol*s)'), n=-7.03422, w0=(323950,'J/mol'), E0=(108551,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.142555979882132, var=30.62281858092808, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1NO->O_Ext-1N-R_Ext-5R!H-R',), solute=SoluteData(S=0.863017030277482,B=-0.7862428964274454,E=0.8580999216461198,L=0.5789259436028682,A=-0.29297988438229017,comment=''), comment="""BM rule fitted to 2 training reactions at node Root_N-1NO->O_Ext-1N-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 21.502212646244704"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1NO->O_Ext-1N-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 21.502212646244704""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1NO->O_Ext-1N-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 21.502212646244704
""",
)

entry(
    index = 21,
    label = "Root_N-1NO->O_Ext-1N-R_3R->C",
    kinetics = Arrhenius(A=(0.0059447,'m^3/(mol*s)'), n=2.92332, Ea=(72.4476,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1NO->O_Ext-1N-R_3R->C',), solute=SoluteData(S=0.5744890931378948,B=0.2855711005089523,E=-1.291148672431544,L=2.4540989125088446,A=-0.2528218771773645,comment=''), comment="""BM rule fitted to 1 training reactions at node Root_N-1NO->O_Ext-1N-R_3R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1NO->O_Ext-1N-R_3R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1NO->O_Ext-1N-R_3R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-1NO->O_Ext-1N-R_N-3R->C",
    kinetics = ArrheniusBM(A=(1.66508e+34,'m^3/(mol*s)'), n=-7.19187, w0=(323950,'J/mol'), E0=(106743,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.505603852756906, var=24.399563143113603, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1NO->O_Ext-1N-R_N-3R->C',), solute=SoluteData(S=-1.3642610964570498,B=-11.06006909582796,E=5.1711961772960455,L=27.631224775816627,A=-6.394100149300156,comment=''), comment="""BM rule fitted to 2 training reactions at node Root_N-1NO->O_Ext-1N-R_N-3R->C
    Total Standard Deviation in ln(k): 21.223184831612095"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1NO->O_Ext-1N-R_N-3R->C
Total Standard Deviation in ln(k): 21.223184831612095""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1NO->O_Ext-1N-R_N-3R->C
Total Standard Deviation in ln(k): 21.223184831612095
""",
)

entry(
    index = 23,
    label = "Root_1NO->O_Ext-3R-R_2R->C_Ext-5R!H-R",
    kinetics = Arrhenius(A=(0.0314082,'m^3/(mol*s)'), n=2.80799, Ea=(51.0438,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1NO->O_Ext-3R-R_2R->C_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1NO->O_Ext-3R-R_2R->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1NO->O_Ext-3R-R_2R->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1NO->O_Ext-3R-R_2R->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_1NO->O_N-3R->C_2R->C_Ext-2C-R",
    kinetics = Arrhenius(A=(0.432458,'m^3/(mol*s)'), n=2.84015, Ea=(54.2306,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1NO->O_N-3R->C_2R->C_Ext-2C-R',), solute=SoluteData(S=1.623170138973233,B=1.2667975612721842,E=-0.32752995070714125,L=3.125868783933266,A=-0.5095858567709188,comment=''), comment="""BM rule fitted to 1 training reactions at node Root_1NO->O_N-3R->C_2R->C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1NO->O_N-3R->C_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1NO->O_N-3R->C_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-1NO->O_Ext-1N-R_Ext-5R!H-R_2R->C",
    kinetics = Arrhenius(A=(0.495802,'m^3/(mol*s)'), n=2.70018, Ea=(96.2062,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1NO->O_Ext-1N-R_Ext-5R!H-R_2R->C',), solute=SoluteData(S=0.7729226689305377,B=-1.2527501488111554,E=0.597866133925776,L=-1.1782169835459175,A=-0.3753151107905479,comment=''), comment="""BM rule fitted to 1 training reactions at node Root_N-1NO->O_Ext-1N-R_Ext-5R!H-R_2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1NO->O_Ext-1N-R_Ext-5R!H-R_2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1NO->O_Ext-1N-R_Ext-5R!H-R_2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_N-1NO->O_Ext-1N-R_Ext-5R!H-R_N-2R->C",
    kinetics = Arrhenius(A=(0.00611439,'m^3/(mol*s)'), n=3.01423, Ea=(78.6803,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1NO->O_Ext-1N-R_Ext-5R!H-R_N-2R->C',), solute=SoluteData(S=0.9531113916244263,B=-0.31973564404373533,E=1.1183337093664636,L=2.336068870751654,A=-0.21064465797403237,comment=''), comment="""BM rule fitted to 1 training reactions at node Root_N-1NO->O_Ext-1N-R_Ext-5R!H-R_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1NO->O_Ext-1N-R_Ext-5R!H-R_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1NO->O_Ext-1N-R_Ext-5R!H-R_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_N-1NO->O_Ext-1N-R_N-3R->C_2R->C",
    kinetics = Arrhenius(A=(1.28885,'m^3/(mol*s)'), n=2.72614, Ea=(98.7959,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1NO->O_Ext-1N-R_N-3R->C_2R->C',), solute=SoluteData(S=4.188534410819756,B=-13.423890383748061,E=-1.8125464291642417,L=29.657494205929744,A=-11.982022615849043,comment=''), comment="""BM rule fitted to 1 training reactions at node Root_N-1NO->O_Ext-1N-R_N-3R->C_2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1NO->O_Ext-1N-R_N-3R->C_2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1NO->O_Ext-1N-R_N-3R->C_2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_N-1NO->O_Ext-1N-R_N-3R->C_N-2R->C",
    kinetics = Arrhenius(A=(0.0346984,'m^3/(mol*s)'), n=2.88658, Ea=(79.6336,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1NO->O_Ext-1N-R_N-3R->C_N-2R->C',), solute=SoluteData(S=-6.9170566037338554,B=-8.69624780790786,E=12.154938783756332,L=25.604955345703505,A=-0.8061776827512686,comment=''), comment="""BM rule fitted to 1 training reactions at node Root_N-1NO->O_Ext-1N-R_N-3R->C_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1NO->O_Ext-1N-R_N-3R->C_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1NO->O_Ext-1N-R_N-3R->C_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

