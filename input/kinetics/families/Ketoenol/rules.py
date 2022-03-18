#!/usr/bin/env python
# encoding: utf-8

name = "Ketoenol/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(6.10397e-09,'s^-1'), n=6.18187, w0=(795076,'J/mol'), E0=(134685,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2195681169559809, var=20.961761804484684, Tref=1000.0, N=33, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 33 training reactions at node Root
    Total Standard Deviation in ln(k): 9.730161101696131"""),
    rank = 11,
    shortDesc = """BM rule fitted to 33 training reactions at node Root
Total Standard Deviation in ln(k): 9.730161101696131""",
    longDesc = 
"""
BM rule fitted to 33 training reactions at node Root
Total Standard Deviation in ln(k): 9.730161101696131
""",
)

entry(
    index = 2,
    label = "Root_1R!H-inRing",
    kinetics = ArrheniusBM(A=(5.26108e-07,'s^-1'), n=5.66028, w0=(798000,'J/mol'), E0=(149674,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2986016055903136, var=12.008348340526611, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_1R!H-inRing',), comment="""BM rule fitted to 17 training reactions at node Root_1R!H-inRing
    Total Standard Deviation in ln(k): 7.697276553951726"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 7.697276553951726""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 7.697276553951726
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(1.08943e-18,'s^-1'), n=8.92199, w0=(791969,'J/mol'), E0=(93809.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08893667560245318, var=37.94025194284002, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R!H-inRing',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R!H-inRing
    Total Standard Deviation in ln(k): 12.571756783434886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 12.571756783434886""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 12.571756783434886
""",
)

entry(
    index = 4,
    label = "Root_1R!H-inRing_Ext-3R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(3.63777e-17,'s^-1'), n=8.55003, w0=(798000,'J/mol'), E0=(118646,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0028809451405216774, var=3.403124387745618, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_5R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 3.705485448648163"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C
Total Standard Deviation in ln(k): 3.705485448648163""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C
Total Standard Deviation in ln(k): 3.705485448648163
""",
)

entry(
    index = 5,
    label = "Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.12949,'s^-1'), n=4.13415, w0=(798000,'J/mol'), E0=(168423,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4467128617852155, var=23.288738414217875, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 10.79692624441642"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 10.79692624441642""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 10.79692624441642
""",
)

entry(
    index = 6,
    label = "Root_N-1R!H-inRing_3R!H->C",
    kinetics = ArrheniusBM(A=(1.80789e-52,'s^-1'), n=18.7686, w0=(785875,'J/mol'), E0=(142261,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=7.096700906046526, var=111.32985920057283, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_3R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_3R!H->C
    Total Standard Deviation in ln(k): 38.98346113476485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_3R!H->C
Total Standard Deviation in ln(k): 38.98346113476485""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_3R!H->C
Total Standard Deviation in ln(k): 38.98346113476485
""",
)

entry(
    index = 7,
    label = "Root_N-1R!H-inRing_N-3R!H->C",
    kinetics = ArrheniusBM(A=(2.14216e-12,'s^-1'), n=7.10076, w0=(794000,'J/mol'), E0=(95211.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.027300955354671547, var=2.809838899397277, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R!H-inRing_N-3R!H->C
    Total Standard Deviation in ln(k): 3.4290473906824763"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R!H-inRing_N-3R!H->C
Total Standard Deviation in ln(k): 3.4290473906824763""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R!H-inRing_N-3R!H->C
Total Standard Deviation in ln(k): 3.4290473906824763
""",
)

entry(
    index = 8,
    label = "Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H",
    kinetics = ArrheniusBM(A=(6.35117e-18,'s^-1'), n=8.76855, w0=(798000,'J/mol'), E0=(117401,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.008743366414696061, var=4.057942970727891, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H
    Total Standard Deviation in ln(k): 4.0603740767018035"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H
Total Standard Deviation in ln(k): 4.0603740767018035""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H
Total Standard Deviation in ln(k): 4.0603740767018035
""",
)

entry(
    index = 9,
    label = "Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_N-Sp-5C-3R!H",
    kinetics = ArrheniusBM(A=(6.87223e-13,'s^-1'), n=7.30388, w0=(798000,'J/mol'), E0=(124360,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_N-Sp-5C-3R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_N-Sp-5C-3R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_N-Sp-5C-3R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_N-Sp-5C-3R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.50083e-19,'s^-1'), n=9.25255, w0=(798000,'J/mol'), E0=(127699,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0006427823284157327, var=0.5967826247970905, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 1.5503071008497333"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C
Total Standard Deviation in ln(k): 1.5503071008497333""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C
Total Standard Deviation in ln(k): 1.5503071008497333
""",
)

entry(
    index = 11,
    label = "Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(3.15335e+06,'s^-1'), n=2.03333, w0=(798000,'J/mol'), E0=(184034,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5800252121262526, var=55.895560511264364, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 16.44541751648541"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 16.44541751648541""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 16.44541751648541
""",
)

entry(
    index = 12,
    label = "Root_N-1R!H-inRing_3R!H->C_1R!H->N",
    kinetics = ArrheniusBM(A=(9.27692e-54,'s^-1'), n=19.1913, w0=(793000,'J/mol'), E0=(143942,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_3R!H->C_1R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_3R!H->C_1R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_3R!H->C_1R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_3R!H->C_1R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_N-1R!H-inRing_3R!H->C_N-1R!H->N",
    kinetics = ArrheniusBM(A=(75.1006,'s^-1'), n=3.11041, w0=(783500,'J/mol'), E0=(209076,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00848789959541425, var=6.520606768146176, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_3R!H->C_N-1R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_3R!H->C_N-1R!H->N
    Total Standard Deviation in ln(k): 5.140513384866411"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_3R!H->C_N-1R!H->N
Total Standard Deviation in ln(k): 5.140513384866411""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_3R!H->C_N-1R!H->N
Total Standard Deviation in ln(k): 5.140513384866411
""",
)

entry(
    index = 14,
    label = "Root_N-1R!H-inRing_N-3R!H->C_3NS->S",
    kinetics = ArrheniusBM(A=(1583.91,'s^-1'), n=2.85161, w0=(782000,'J/mol'), E0=(88955.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.003045184023974304, var=0.28211849898893376, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_3NS->S',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S
    Total Standard Deviation in ln(k): 1.0724628112272296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S
Total Standard Deviation in ln(k): 1.0724628112272296""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S
Total Standard Deviation in ln(k): 1.0724628112272296
""",
)

entry(
    index = 15,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S",
    kinetics = ArrheniusBM(A=(1.30473e-11,'s^-1'), n=6.87514, w0=(798000,'J/mol'), E0=(99876.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0117411635116814, var=0.6446492092925814, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S
    Total Standard Deviation in ln(k): 1.6391032023367265"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S
Total Standard Deviation in ln(k): 1.6391032023367265""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S
Total Standard Deviation in ln(k): 1.6391032023367265
""",
)

entry(
    index = 16,
    label = "Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.03729e-10,'s^-1'), n=6.68631, w0=(798000,'J/mol'), E0=(105099,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.69363e-18,'s^-1'), n=8.94137, w0=(798000,'J/mol'), E0=(121373,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0038084715549368104, var=0.5842399037789903, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 1.5419000584052351"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.5419000584052351""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.5419000584052351
""",
)

entry(
    index = 18,
    label = "Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.2013e-18,'s^-1'), n=8.97925, w0=(798000,'J/mol'), E0=(126845,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.007503612341907746, var=0.008054470110497336, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 0.1987716543490167"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 0.1987716543490167""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 0.1987716543490167
""",
)

entry(
    index = 19,
    label = "Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(1.18952e-19,'s^-1'), n=9.32392, w0=(798000,'J/mol'), E0=(137103,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi",
    kinetics = ArrheniusBM(A=(3.33668e-20,'s^-1'), n=9.45072, w0=(798000,'J/mol'), E0=(138622,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.025999023929210666, var=2.2367127697893783, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi
    Total Standard Deviation in ln(k): 3.0635345236969505"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi
Total Standard Deviation in ln(k): 3.0635345236969505""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi
Total Standard Deviation in ln(k): 3.0635345236969505
""",
)

entry(
    index = 21,
    label = "Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_N-Sp-7R!H-5BrClFINOPSSi",
    kinetics = ArrheniusBM(A=(7.03103e-17,'s^-1'), n=8.43292, w0=(798000,'J/mol'), E0=(45092.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_N-Sp-7R!H-5BrClFINOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_N-Sp-7R!H-5BrClFINOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_N-Sp-7R!H-5BrClFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_N-Sp-7R!H-5BrClFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-1R!H-inRing_3R!H->C_N-1R!H->N_Ext-1C-R",
    kinetics = ArrheniusBM(A=(205000,'s^-1'), n=2.37, w0=(783500,'J/mol'), E0=(221387,'J/mol'), Tmin=(600,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_3R!H->C_N-1R!H->N_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_3R!H->C_N-1R!H->N_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_3R!H->C_N-1R!H->N_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_3R!H->C_N-1R!H->N_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(2857.3,'s^-1'), n=2.79065, w0=(782000,'J/mol'), E0=(88663.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.015825826525184e-07, var=0.0007766175206250726, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.05586817935319939"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.05586817935319939""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.05586817935319939
""",
)

entry(
    index = 24,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.09806e-11,'s^-1'), n=6.89792, w0=(798000,'J/mol'), E0=(99858.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0190200390037195, var=1.0964123289271033, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R
    Total Standard Deviation in ln(k): 2.1469413209668056"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.1469413209668056""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.1469413209668056
""",
)

entry(
    index = 25,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(6.24893e-09,'s^-1'), n=6.18216, w0=(798000,'J/mol'), E0=(107861,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_6R!H->N",
    kinetics = ArrheniusBM(A=(3.10725e-11,'s^-1'), n=6.76455, w0=(798000,'J/mol'), E0=(102204,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N",
    kinetics = ArrheniusBM(A=(6.36022e-11,'s^-1'), n=6.62861, w0=(798000,'J/mol'), E0=(100596,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.05792e-18,'s^-1'), n=9.0012, w0=(798000,'J/mol'), E0=(119968,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0011076788615978056, var=1.099229330440946, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C
    Total Standard Deviation in ln(k): 2.104630326801545"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C
Total Standard Deviation in ln(k): 2.104630326801545""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C
Total Standard Deviation in ln(k): 2.104630326801545
""",
)

entry(
    index = 29,
    label = "Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(3.10141e-18,'s^-1'), n=8.86353, w0=(798000,'J/mol'), E0=(123814,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-7.630684147407905e-05, var=0.07260338773725893, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->C
    Total Standard Deviation in ln(k): 0.5403679094229893"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->C
Total Standard Deviation in ln(k): 0.5403679094229893""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->C
Total Standard Deviation in ln(k): 0.5403679094229893
""",
)

entry(
    index = 30,
    label = "Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C_5BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(2.9852e-20,'s^-1'), n=9.42069, w0=(798000,'J/mol'), E0=(121194,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00033558131741877046, var=0.002267350901758185, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C_5BrClFINOPSSi->N',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C_5BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 0.09630205437896223"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C_5BrClFINOPSSi->N
Total Standard Deviation in ln(k): 0.09630205437896223""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C_5BrClFINOPSSi->N
Total Standard Deviation in ln(k): 0.09630205437896223
""",
)

entry(
    index = 31,
    label = "Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C_N-5BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(2.95366e-14,'s^-1'), n=7.77475, w0=(798000,'J/mol'), E0=(142358,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C_N-5BrClFINOPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C_N-5BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C_N-5BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C_N-5BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_7R!H->C",
    kinetics = ArrheniusBM(A=(5.35193e-22,'s^-1'), n=9.96064, w0=(798000,'J/mol'), E0=(136695,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0025574536717999116, var=2.4594978159443808, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_7R!H->C
    Total Standard Deviation in ln(k): 3.1504089146845984"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_7R!H->C
Total Standard Deviation in ln(k): 3.1504089146845984""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_7R!H->C
Total Standard Deviation in ln(k): 3.1504089146845984
""",
)

entry(
    index = 33,
    label = "Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_N-7R!H->C",
    kinetics = ArrheniusBM(A=(2.27189e-19,'s^-1'), n=9.21636, w0=(798000,'J/mol'), E0=(138167,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0005520236756471257, var=10.279324647875598, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_N-7R!H->C
    Total Standard Deviation in ln(k): 6.428845485264807"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_N-7R!H->C
Total Standard Deviation in ln(k): 6.428845485264807""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_N-7R!H->C
Total Standard Deviation in ln(k): 6.428845485264807
""",
)

entry(
    index = 34,
    label = "Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(87.5,'s^-1'), n=3.23, w0=(782000,'J/mol'), E0=(85014.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.87238e-12,'s^-1'), n=7.05581, w0=(798000,'J/mol'), E0=(99707.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02252736485366013, var=0.8629404088644341, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.9188917676717938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.9188917676717938""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.9188917676717938
""",
)

entry(
    index = 36,
    label = "Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_6BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(1.02008e-17,'s^-1'), n=8.71849, w0=(798000,'J/mol'), E0=(119287,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.003881804765101457, var=0.009199804740706677, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_6BrClFINOPSSi->N',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_6BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 0.20203867135609896"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_6BrClFINOPSSi->N
Total Standard Deviation in ln(k): 0.20203867135609896""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_6BrClFINOPSSi->N
Total Standard Deviation in ln(k): 0.20203867135609896
""",
)

entry(
    index = 37,
    label = "Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_N-6BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(5.23245e-20,'s^-1'), n=9.38178, w0=(798000,'J/mol'), E0=(126650,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_N-6BrClFINOPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_N-6BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_N-6BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_N-6BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(9.00746e-18,'s^-1'), n=8.75254, w0=(798000,'J/mol'), E0=(125562,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_N-7R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C_5BrClFINOPSSi->N_Ext-7C-R",
    kinetics = ArrheniusBM(A=(3.57404e-19,'s^-1'), n=9.1193, w0=(798000,'J/mol'), E0=(124449,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C_5BrClFINOPSSi->N_Ext-7C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C_5BrClFINOPSSi->N_Ext-7C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C_5BrClFINOPSSi->N_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_6R!H->C_Ext-6C-R_7R!H->C_5BrClFINOPSSi->N_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_7R!H->C_5BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(2.52338e-22,'s^-1'), n=10.05, w0=(798000,'J/mol'), E0=(131010,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_7R!H->C_5BrClFINOPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_7R!H->C_5BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_7R!H->C_5BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_7R!H->C_5BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_7R!H->C_N-5BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(1.62343e-20,'s^-1'), n=9.5285, w0=(798000,'J/mol'), E0=(144945,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_7R!H->C_N-5BrClFINOPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_7R!H->C_N-5BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_7R!H->C_N-5BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_7R!H->C_N-5BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_N-7R!H->C_Sp-5BrClFINOPSSi-3R!H",
    kinetics = ArrheniusBM(A=(4.58562e-24,'s^-1'), n=10.6226, w0=(798000,'J/mol'), E0=(138683,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_N-7R!H->C_Sp-5BrClFINOPSSi-3R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_N-7R!H->C_Sp-5BrClFINOPSSi-3R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_N-7R!H->C_Sp-5BrClFINOPSSi-3R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_N-7R!H->C_Sp-5BrClFINOPSSi-3R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_N-7R!H->C_N-Sp-5BrClFINOPSSi-3R!H",
    kinetics = ArrheniusBM(A=(2.02819e-14,'s^-1'), n=7.71417, w0=(798000,'J/mol'), E0=(137432,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_N-7R!H->C_N-Sp-5BrClFINOPSSi-3R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_N-7R!H->C_N-Sp-5BrClFINOPSSi-3R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_N-7R!H->C_N-Sp-5BrClFINOPSSi-3R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_Int-7R!H-5BrClFINOPSSi_Sp-7R!H-5BrClFINOPSSi_N-7R!H->C_N-Sp-5BrClFINOPSSi-3R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_5R!H-inRing",
    kinetics = ArrheniusBM(A=(1.68509e-11,'s^-1'), n=6.88807, w0=(798000,'J/mol'), E0=(102832,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_5R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_5R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing",
    kinetics = ArrheniusBM(A=(2.36128e-12,'s^-1'), n=7.07296, w0=(798000,'J/mol'), E0=(99585.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.029593247978928896, var=1.2653129163997325, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing
    Total Standard Deviation in ln(k): 2.3294037749260914"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing
Total Standard Deviation in ln(k): 2.3294037749260914""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing
Total Standard Deviation in ln(k): 2.3294037749260914
""",
)

entry(
    index = 46,
    label = "Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_6BrClFINOPSSi->N_Ext-5C-R",
    kinetics = ArrheniusBM(A=(1.36428e-17,'s^-1'), n=8.68106, w0=(798000,'J/mol'), E0=(119355,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=9.875757718463376e-05, var=0.019447819937148978, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_6BrClFINOPSSi->N_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_6BrClFINOPSSi->N_Ext-5C-R
    Total Standard Deviation in ln(k): 0.2798193482943225"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_6BrClFINOPSSi->N_Ext-5C-R
Total Standard Deviation in ln(k): 0.2798193482943225""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_6BrClFINOPSSi->N_Ext-5C-R
Total Standard Deviation in ln(k): 0.2798193482943225
""",
)

entry(
    index = 47,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(7.93116e-11,'s^-1'), n=6.59023, w0=(798000,'J/mol'), E0=(104253,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004083326014350255, var=0.36678964389307633, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 1.2243905404532403"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 1.2243905404532403""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 1.2243905404532403
""",
)

entry(
    index = 48,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(3.02789e-13,'s^-1'), n=7.48219, w0=(798000,'J/mol'), E0=(95953.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_6BrClFINOPSSi->N_Ext-5C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(9.14825e-17,'s^-1'), n=8.45574, w0=(798000,'J/mol'), E0=(121877,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_6BrClFINOPSSi->N_Ext-5C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_6BrClFINOPSSi->N_Ext-5C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_6BrClFINOPSSi->N_Ext-5C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_6BrClFINOPSSi->N_Ext-5C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_6BrClFINOPSSi->N_Ext-5C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(4.10787e-17,'s^-1'), n=8.57309, w0=(798000,'J/mol'), E0=(122784,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_6BrClFINOPSSi->N_Ext-5C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_6BrClFINOPSSi->N_Ext-5C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_6BrClFINOPSSi->N_Ext-5C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_Ext-3R!H-R_5R!H->C_Sp-5C-3R!H_Ext-5C-R_Ext-6R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R_7R!H->C_6BrClFINOPSSi->N_Ext-5C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_5R!H->N",
    kinetics = ArrheniusBM(A=(8.42992e-10,'s^-1'), n=6.22192, w0=(798000,'J/mol'), E0=(104542,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.0517082806578122e-05, var=0.15820189146844285, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_5R!H->N
    Total Standard Deviation in ln(k): 0.7974520617821278"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_5R!H->N
Total Standard Deviation in ln(k): 0.7974520617821278""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_5R!H->N
Total Standard Deviation in ln(k): 0.7974520617821278
""",
)

entry(
    index = 52,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_N-5R!H->N",
    kinetics = ArrheniusBM(A=(1.30511e-12,'s^-1'), n=7.26372, w0=(798000,'J/mol'), E0=(105105,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_N-5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_N-5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_N-5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_N-5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 53,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_5R!H->N_Ext-6R!H-R_7R!H->N",
    kinetics = ArrheniusBM(A=(1.95577e-10,'s^-1'), n=6.41822, w0=(798000,'J/mol'), E0=(102434,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_5R!H->N_Ext-6R!H-R_7R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_5R!H->N_Ext-6R!H-R_7R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_5R!H->N_Ext-6R!H-R_7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_5R!H->N_Ext-6R!H-R_7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_5R!H->N_Ext-6R!H-R_N-7R!H->N",
    kinetics = ArrheniusBM(A=(5.58698e-10,'s^-1'), n=6.27942, w0=(798000,'J/mol'), E0=(105618,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_5R!H->N_Ext-6R!H-R_N-7R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_5R!H->N_Ext-6R!H-R_N-7R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_5R!H->N_Ext-6R!H-R_N-7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_5R!H->N_Ext-6R!H-R_N-7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

