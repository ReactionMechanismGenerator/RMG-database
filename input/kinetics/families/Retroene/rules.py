#!/usr/bin/env python
# encoding: utf-8

name = "Retroene/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.97382e+10,'s^-1'), n=0.376411, w0=(1.11205e+06,'J/mol'), E0=(167693,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00780266474807507, var=12.245936757993622, Tref=1000.0, N=67, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 67 training reactions at node Root
    Total Standard Deviation in ln(k): 7.035013684838923"""),
    rank = 11,
    shortDesc = """BM rule fitted to 67 training reactions at node Root
Total Standard Deviation in ln(k): 7.035013684838923""",
    longDesc = 
"""
BM rule fitted to 67 training reactions at node Root
Total Standard Deviation in ln(k): 7.035013684838923
""",
)

entry(
    index = 2,
    label = "Root_1R!H->C",
    kinetics = ArrheniusBM(A=(2.07189e+11,'s^-1'), n=0.143046, w0=(1.04926e+06,'J/mol'), E0=(181463,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.054649355541500584, var=2.0478878008325494, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_1R!H->C',), comment="""BM rule fitted to 31 training reactions at node Root_1R!H->C
    Total Standard Deviation in ln(k): 3.0061746526559174"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 3.0061746526559174""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 3.0061746526559174
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H->C",
    kinetics = ArrheniusBM(A=(9.81665e+10,'s^-1'), n=0.215208, w0=(1.16612e+06,'J/mol'), E0=(151945,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06617441972298048, var=24.353578080177726, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_N-1R!H->C',), comment="""BM rule fitted to 36 training reactions at node Root_N-1R!H->C
    Total Standard Deviation in ln(k): 10.059503593840045"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 10.059503593840045""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 10.059503593840045
""",
)

entry(
    index = 4,
    label = "Root_1R!H->C_2R!H->C",
    kinetics = ArrheniusBM(A=(1.86585e+11,'s^-1'), n=0.14101, w0=(1.0543e+06,'J/mol'), E0=(179728,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05711294136557333, var=1.8421132701512442, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C',), comment="""BM rule fitted to 27 training reactions at node Root_1R!H->C_2R!H->C
    Total Standard Deviation in ln(k): 2.8644159811459677"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_1R!H->C_2R!H->C
Total Standard Deviation in ln(k): 2.8644159811459677""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_1R!H->C_2R!H->C
Total Standard Deviation in ln(k): 2.8644159811459677
""",
)

entry(
    index = 5,
    label = "Root_1R!H->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(3.56473e+12,'s^-1'), n=0.153065, w0=(1.01525e+06,'J/mol'), E0=(224011,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.745698648703464, var=41.647486026071995, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-2R!H->C
    Total Standard Deviation in ln(k): 22.34883358800863"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 22.34883358800863""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 22.34883358800863
""",
)

entry(
    index = 6,
    label = "Root_N-1R!H->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.78145e+06,'s^-1'), n=1.66111, w0=(1.17869e+06,'J/mol'), E0=(146290,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.23563930036468572, var=3.534544099554761, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 18 training reactions at node Root_N-1R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 4.3610373185158515"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-1R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.3610373185158515""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-1R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.3610373185158515
""",
)

entry(
    index = 7,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(9.54463e+09,'s^-1'), n=0.829688, w0=(1.0865e+06,'J/mol'), E0=(100226,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(1.54025e+10,'s^-1'), n=0.304824, w0=(1.1575e+06,'J/mol'), E0=(161284,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05391444334817388, var=14.101183599024699, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 7.663552913602069"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 7.663552913602069""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 7.663552913602069
""",
)

entry(
    index = 9,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.54761e+09,'s^-1'), n=0.778487, w0=(1.0845e+06,'J/mol'), E0=(188500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.025714245167703532, var=1.7810823313783888, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R',), comment="""BM rule fitted to 15 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.7400718889551374"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.7400718889551374""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.7400718889551374
""",
)

entry(
    index = 10,
    label = "Root_1R!H->C_2R!H->C_5R!H->C",
    kinetics = ArrheniusBM(A=(1.48951e+15,'s^-1'), n=-1.30964, w0=(968000,'J/mol'), E0=(168589,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07569936479566841, var=3.226748716199058, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_5R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C
    Total Standard Deviation in ln(k): 3.7913357340300995"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C
Total Standard Deviation in ln(k): 3.7913357340300995""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C
Total Standard Deviation in ln(k): 3.7913357340300995
""",
)

entry(
    index = 11,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(8.59589e+06,'s^-1'), n=1.3196, w0=(1.0845e+06,'J/mol'), E0=(159011,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02456672035395117, var=1.9417863590451045, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C
    Total Standard Deviation in ln(k): 2.855283554798543"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 2.855283554798543""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 2.855283554798543
""",
)

entry(
    index = 12,
    label = "Root_1R!H->C_N-2R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.8e+12,'s^-1'), n=0, w0=(1.0665e+06,'J/mol'), E0=(216282,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_1R!H->C_N-2R!H->C_2NOS->S",
    kinetics = ArrheniusBM(A=(5.6608e+10,'s^-1'), n=0, w0=(953500,'J/mol'), E0=(110888,'J/mol'), Tmin=(588,'K'), Tmax=(691,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_2NOS->S',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_2NOS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_2NOS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_2NOS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_1R!H->C_N-2R!H->C_N-2NOS->S",
    kinetics = ArrheniusBM(A=(9.80865e+11,'s^-1'), n=-0.428975, w0=(1.0205e+06,'J/mol'), E0=(162372,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0015504653146382998, var=3.7473697542407622, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-2NOS->S',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S
    Total Standard Deviation in ln(k): 3.8846867180435005"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S
Total Standard Deviation in ln(k): 3.8846867180435005""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S
Total Standard Deviation in ln(k): 3.8846867180435005
""",
)

entry(
    index = 15,
    label = "Root_N-1R!H->C_Ext-2R!H-R_1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(1.93151e+06,'s^-1'), n=1.81611, w0=(1.1055e+06,'J/mol'), E0=(159124,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_1BrClFINOPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(3.59737e+09,'s^-1'), n=0.823419, w0=(1.183e+06,'J/mol'), E0=(151557,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07218607168624883, var=3.7412653467613355, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 4.059000953281817"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 4.059000953281817""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 4.059000953281817
""",
)

entry(
    index = 17,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_3R!H-inRing",
    kinetics = ArrheniusBM(A=(2.62744e+10,'s^-1'), n=-0.0358989, w0=(1.0245e+06,'J/mol'), E0=(140443,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.009729245350595292, var=85.99483533521845, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_3R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_3R!H-inRing
    Total Standard Deviation in ln(k): 18.615035385330714"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_3R!H-inRing
Total Standard Deviation in ln(k): 18.615035385330714""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_3R!H-inRing
Total Standard Deviation in ln(k): 18.615035385330714
""",
)

entry(
    index = 18,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(1.49828e+09,'s^-1'), n=0.660807, w0=(1.17523e+06,'J/mol'), E0=(163691,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.006027786053699877, var=15.028913248977284, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing',), comment="""BM rule fitted to 15 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing
    Total Standard Deviation in ln(k): 7.78693020021568"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing
Total Standard Deviation in ln(k): 7.78693020021568""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing
Total Standard Deviation in ln(k): 7.78693020021568
""",
)

entry(
    index = 19,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N",
    kinetics = ArrheniusBM(A=(731778,'s^-1'), n=1.88732, w0=(1.0845e+06,'J/mol'), E0=(170151,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.007620399408995478, var=0.1879960069611533, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N
    Total Standard Deviation in ln(k): 0.8883699172550954"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N
Total Standard Deviation in ln(k): 0.8883699172550954""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N
Total Standard Deviation in ln(k): 0.8883699172550954
""",
)

entry(
    index = 20,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N",
    kinetics = ArrheniusBM(A=(9.53055e+10,'s^-1'), n=0.389268, w0=(1.0845e+06,'J/mol'), E0=(196201,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.019461980130987277, var=1.6458604300821922, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N',), comment="""BM rule fitted to 10 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N
    Total Standard Deviation in ln(k): 2.6207959711761792"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N
Total Standard Deviation in ln(k): 2.6207959711761792""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N
Total Standard Deviation in ln(k): 2.6207959711761792
""",
)

entry(
    index = 21,
    label = "Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.26843e+16,'s^-1'), n=-1.80141, w0=(968000,'J/mol'), E0=(163775,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10844373598081314, var=3.8433144441687306, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 4.202629139672138"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.202629139672138""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.202629139672138
""",
)

entry(
    index = 22,
    label = "Root_1R!H->C_2R!H->C_5R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(3.23333e+11,'s^-1'), n=0, w0=(968000,'J/mol'), E0=(182702,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(6.37974e+09,'s^-1'), n=0.54436, w0=(1.0845e+06,'J/mol'), E0=(161997,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00018539581192034797, var=7.1519259880296655, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 5.361745889411243"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 5.361745889411243""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 5.361745889411243
""",
)

entry(
    index = 24,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(34855.7,'s^-1'), n=1.97686, w0=(1.0845e+06,'J/mol'), E0=(158083,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.004571568961603465, var=0.02917473919887987, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.35390742466173425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.35390742466173425""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.35390742466173425
""",
)

entry(
    index = 25,
    label = "Root_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->N",
    kinetics = ArrheniusBM(A=(7.8141e+10,'s^-1'), n=0, w0=(974500,'J/mol'), E0=(160345,'J/mol'), Tmin=(602,'K'), Tmax=(694,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->N",
    kinetics = ArrheniusBM(A=(4.1009e+10,'s^-1'), n=0, w0=(1.0665e+06,'J/mol'), E0=(166383,'J/mol'), Tmin=(725,'K'), Tmax=(810,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(5.92869e+08,'s^-1'), n=1.03693, w0=(1.183e+06,'J/mol'), E0=(136255,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8657497964465389, var=1.9665168363205905, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R
    Total Standard Deviation in ln(k): 4.986541884893638"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.986541884893638""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.986541884893638
""",
)

entry(
    index = 28,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C",
    kinetics = ArrheniusBM(A=(1.70476e+09,'s^-1'), n=0.923342, w0=(1.183e+06,'J/mol'), E0=(157861,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09070765353639848, var=0.5226110365868454, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C
    Total Standard Deviation in ln(k): 1.6771685844240827"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C
Total Standard Deviation in ln(k): 1.6771685844240827""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C
Total Standard Deviation in ln(k): 1.6771685844240827
""",
)

entry(
    index = 29,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_N-7R!H->C",
    kinetics = ArrheniusBM(A=(6.63512e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(92773.6,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_3R!H-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(550000,'s^-1'), n=0.9, w0=(1.0245e+06,'J/mol'), E0=(132721,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_3R!H-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_3R!H-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_3R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_3R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.15362e+06,'s^-1'), n=1.69206, w0=(1.183e+06,'J/mol'), E0=(171838,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.006483929885847792, var=0.30216611010453276, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 1.118286895875874"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.118286895875874""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.118286895875874
""",
)

entry(
    index = 32,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.02548e+11,'s^-1'), n=-0.0737291, w0=(1.183e+06,'J/mol'), E0=(160071,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.002465108406622806, var=47.764352899025596, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R
    Total Standard Deviation in ln(k): 13.86127057635807"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 13.86127057635807""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 13.86127057635807
""",
)

entry(
    index = 33,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_5R!H->C",
    kinetics = ArrheniusBM(A=(3.33333e+07,'s^-1'), n=1.2, w0=(1.0665e+06,'J/mol'), E0=(165812,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.96667e+10,'s^-1'), n=0.59, w0=(1.183e+06,'J/mol'), E0=(175304,'J/mol'), Tmin=(500,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(198561,'s^-1'), n=2.1263, w0=(1.0845e+06,'J/mol'), E0=(175389,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.003340098044869666, var=0.4720447566985367, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R
    Total Standard Deviation in ln(k): 1.3857557327093604"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.3857557327093604""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.3857557327093604
""",
)

entry(
    index = 36,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R",
    kinetics = ArrheniusBM(A=(9.02892e+07,'s^-1'), n=1.20601, w0=(1.0845e+06,'J/mol'), E0=(168389,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.5646370544072004e-05, var=0.017165999284314972, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R
    Total Standard Deviation in ln(k): 0.2626978576687453"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R
Total Standard Deviation in ln(k): 0.2626978576687453""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R
Total Standard Deviation in ln(k): 0.2626978576687453
""",
)

entry(
    index = 37,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(5.36936e+09,'s^-1'), n=0.76271, w0=(1.0845e+06,'J/mol'), E0=(197618,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.012456938518518881, var=0.8691804671423755, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R
    Total Standard Deviation in ln(k): 1.9003103181397776"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.9003103181397776""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.9003103181397776
""",
)

entry(
    index = 38,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.47547e+13,'s^-1'), n=-0.227985, w0=(1.0845e+06,'J/mol'), E0=(197924,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.021484680057269882, var=4.322323450767497, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R
    Total Standard Deviation in ln(k): 4.221865586649629"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R
Total Standard Deviation in ln(k): 4.221865586649629""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R
Total Standard Deviation in ln(k): 4.221865586649629
""",
)

entry(
    index = 39,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFIOPSSi->C",
    kinetics = ArrheniusBM(A=(11.5839,'s^-1'), n=3.09547, w0=(1.0845e+06,'J/mol'), E0=(157091,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFIOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFIOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFIOPSSi->C",
    kinetics = ArrheniusBM(A=(1.2535e+06,'s^-1'), n=1.80968, w0=(1.0845e+06,'J/mol'), E0=(192216,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFIOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFIOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.60015e+17,'s^-1'), n=-2.03193, w0=(968000,'J/mol'), E0=(157416,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11484378954342243, var=3.190603869818673, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 3.8694624601999856"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 3.8694624601999856""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 3.8694624601999856
""",
)

entry(
    index = 42,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(21.2645,'s^-1'), n=2.97303, w0=(1.0845e+06,'J/mol'), E0=(146407,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(3.78363e+11,'s^-1'), n=0.169307, w0=(1.0845e+06,'J/mol'), E0=(166826,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(6.80655,'s^-1'), n=3.07798, w0=(1.0845e+06,'J/mol'), E0=(149551,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(2419.21,'s^-1'), n=2.3826, w0=(1.0845e+06,'J/mol'), E0=(159829,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.45626e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(141647,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.06342e+08,'s^-1'), n=1.09149, w0=(1.183e+06,'J/mol'), E0=(136771,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.832239178644912, var=1.5737647039728773, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 4.605988935889593"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 4.605988935889593""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 4.605988935889593
""",
)

entry(
    index = 48,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R",
    kinetics = ArrheniusBM(A=(3.02221e+08,'s^-1'), n=1.12055, w0=(1.183e+06,'J/mol'), E0=(152688,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7725153803015032, var=2.302346308791327, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R
    Total Standard Deviation in ln(k): 4.98287507363038"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 4.98287507363038""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 4.98287507363038
""",
)

entry(
    index = 49,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.04987e+09,'s^-1'), n=0.847821, w0=(1.183e+06,'J/mol'), E0=(163374,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2565122382049447, var=0.16460796993248267, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 1.4578623775100181"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.4578623775100181""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.4578623775100181
""",
)

entry(
    index = 50,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.32388e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(154765,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(2.09037e+06,'s^-1'), n=1.78324, w0=(1.183e+06,'J/mol'), E0=(170865,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05226310243295178, var=0.10196646602416379, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 0.7714701108827263"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C
Total Standard Deviation in ln(k): 0.7714701108827263""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C
Total Standard Deviation in ln(k): 0.7714701108827263
""",
)

entry(
    index = 52,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(7.33841e+14,'s^-1'), n=-0.86586, w0=(1.183e+06,'J/mol'), E0=(200050,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-5.3172441301014085e-15, var=0.04558127893527205, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 0.4280063799185306"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 0.4280063799185306""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 0.4280063799185306
""",
)

entry(
    index = 53,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(5.24992e+12,'s^-1'), n=-0.0624971, w0=(1.183e+06,'J/mol'), E0=(172072,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.002544572537582674, var=0.6067043703112922, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 1.5679062073556134"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C
Total Standard Deviation in ln(k): 1.5679062073556134""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C
Total Standard Deviation in ln(k): 1.5679062073556134
""",
)

entry(
    index = 54,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(58002.5,'s^-1'), n=0.286, w0=(1.183e+06,'J/mol'), E0=(125136,'J/mol'), Tmin=(500,'K'), Tmax=(1300,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_8R!H->C",
    kinetics = ArrheniusBM(A=(1708.21,'s^-1'), n=2.62955, w0=(1.0845e+06,'J/mol'), E0=(162541,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(85500.5,'s^-1'), n=2.19797, w0=(1.0845e+06,'J/mol'), E0=(174531,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(111514,'s^-1'), n=2.05353, w0=(1.0845e+06,'J/mol'), E0=(160852,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(6.3077e+06,'s^-1'), n=1.41637, w0=(1.0845e+06,'J/mol'), E0=(158519,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C",
    kinetics = ArrheniusBM(A=(1.62136e+06,'s^-1'), n=1.61446, w0=(1.0845e+06,'J/mol'), E0=(175142,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.002434535667788421, var=2.6091141324141973, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C
    Total Standard Deviation in ln(k): 3.2443158765835345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 3.2443158765835345""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 3.2443158765835345
""",
)

entry(
    index = 60,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C",
    kinetics = ArrheniusBM(A=(3.48012e+12,'s^-1'), n=0.113345, w0=(1.0845e+06,'J/mol'), E0=(218137,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0014664163696416564, var=0.016887009235405925, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C
    Total Standard Deviation in ln(k): 0.2641998385011292"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 0.2641998385011292""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 0.2641998385011292
""",
)

entry(
    index = 61,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(5.12205e+09,'s^-1'), n=0.705257, w0=(1.0845e+06,'J/mol'), E0=(190457,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.01295442511347593, var=3.5243780819818404, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C
    Total Standard Deviation in ln(k): 3.7961035307187814"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C
Total Standard Deviation in ln(k): 3.7961035307187814""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C
Total Standard Deviation in ln(k): 3.7961035307187814
""",
)

entry(
    index = 62,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(3.42527e+16,'s^-1'), n=-1.13447, w0=(1.0845e+06,'J/mol'), E0=(205149,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.008029375976601699, var=19.42449740445788, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 8.85568964043594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C
Total Standard Deviation in ln(k): 8.85568964043594""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C
Total Standard Deviation in ln(k): 8.85568964043594
""",
)

entry(
    index = 63,
    label = "Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(2.04459e+17,'s^-1'), n=-2.16546, w0=(968000,'J/mol'), E0=(148600,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10411378243550995, var=4.239953774890955, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 4.389572093574849"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 4.389572093574849""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 4.389572093574849
""",
)

entry(
    index = 64,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(1.39881e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(134680,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(8.86548e+12,'s^-1'), n=-0.290964, w0=(1.183e+06,'J/mol'), E0=(154304,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0006425506715519331, var=0.04823060643212642, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.44188369577341297"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.44188369577341297""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.44188369577341297
""",
)

entry(
    index = 66,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.62868e+13,'s^-1'), n=-0.48087, w0=(1.183e+06,'J/mol'), E0=(141183,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.010253465064412173, var=1.8433556031398155, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 2.747595950497338"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.747595950497338""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.747595950497338
""",
)

entry(
    index = 67,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(8.39935e+12,'s^-1'), n=-0.296519, w0=(1.183e+06,'J/mol'), E0=(158913,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0011235484084063624, var=0.16510734475511998, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 0.8174150710512402"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.8174150710512402""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.8174150710512402
""",
)

entry(
    index = 68,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_7C-inRing",
    kinetics = ArrheniusBM(A=(7.92445e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(165691,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_7C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 69,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing",
    kinetics = ArrheniusBM(A=(1.67621e+06,'s^-1'), n=1.81437, w0=(1.183e+06,'J/mol'), E0=(170960,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04035847432874979, var=0.06342541515627706, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing
    Total Standard Deviation in ln(k): 0.6062837616486495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing
Total Standard Deviation in ln(k): 0.6062837616486495""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing
Total Standard Deviation in ln(k): 0.6062837616486495
""",
)

entry(
    index = 70,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(7.92445e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(192300,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R",
    kinetics = ArrheniusBM(A=(5.02109e+11,'s^-1'), n=0.249629, w0=(1.183e+06,'J/mol'), E0=(170814,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.447725953338633e-15, var=2.1167297554160425, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R
    Total Standard Deviation in ln(k): 2.9166861328621714"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 2.9166861328621714""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 2.9166861328621714
""",
)

entry(
    index = 72,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C_8R!H->N",
    kinetics = ArrheniusBM(A=(6552.1,'s^-1'), n=2.29082, w0=(1.0845e+06,'J/mol'), E0=(172908,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C_8R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C_8R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C_8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C_8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C_N-8R!H->N",
    kinetics = ArrheniusBM(A=(459.236,'s^-1'), n=2.68918, w0=(1.0845e+06,'J/mol'), E0=(164046,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C_N-8R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C_N-8R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C_N-8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C_N-8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C_8R!H->N",
    kinetics = ArrheniusBM(A=(2.87851e+08,'s^-1'), n=1.30992, w0=(1.0845e+06,'J/mol'), E0=(209000,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C_8R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C_8R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C_8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C_8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C_N-8R!H->N",
    kinetics = ArrheniusBM(A=(6.1395e+07,'s^-1'), n=1.36832, w0=(1.0845e+06,'J/mol'), E0=(198678,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C_N-8R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C_N-8R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C_N-8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C_N-8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 76,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFIOPSSi->C",
    kinetics = ArrheniusBM(A=(1017.11,'s^-1'), n=2.55399, w0=(1.0845e+06,'J/mol'), E0=(162412,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFIOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFIOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 77,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFIOPSSi->C",
    kinetics = ArrheniusBM(A=(1.65185e+07,'s^-1'), n=1.51788, w0=(1.0845e+06,'J/mol'), E0=(195065,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFIOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFIOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 78,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFIOPSSi->C",
    kinetics = ArrheniusBM(A=(2.0173e+12,'s^-1'), n=0.0499164, w0=(1.0845e+06,'J/mol'), E0=(179063,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFIOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFIOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFIOPSSi->C",
    kinetics = ArrheniusBM(A=(8.27867e+08,'s^-1'), n=1.04991, w0=(1.0845e+06,'J/mol'), E0=(197843,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFIOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFIOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(2.19436e+14,'s^-1'), n=-1.56857, w0=(968000,'J/mol'), E0=(119158,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0012137244180685108, var=1.5806989455609748, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 2.52351978290564"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.52351978290564""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.52351978290564
""",
)

entry(
    index = 81,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R_7C-inRing",
    kinetics = ArrheniusBM(A=(1.25594e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(154176,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R_7C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R_7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R_N-7C-inRing",
    kinetics = ArrheniusBM(A=(1.98582e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(159302,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R_N-7C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R_N-7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 83,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.32702e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(115933,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(8.37297e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(150218,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 85,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.38631e+13,'s^-1'), n=-0.370009, w0=(1.183e+06,'J/mol'), E0=(149628,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00016659514212070096, var=0.10913957692340322, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 0.6627084659917322"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 0.6627084659917322""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 0.6627084659917322
""",
)

entry(
    index = 86,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H",
    kinetics = ArrheniusBM(A=(1.11936e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(158039,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 87,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H",
    kinetics = ArrheniusBM(A=(1.99054e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(165246,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 88,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R",
    kinetics = ArrheniusBM(A=(56440.9,'s^-1'), n=2.19216, w0=(1.183e+06,'J/mol'), E0=(164362,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6429117206903832, var=1.0964835789104808, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R
    Total Standard Deviation in ln(k): 3.7145765656219436"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R
Total Standard Deviation in ln(k): 3.7145765656219436""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R
Total Standard Deviation in ln(k): 3.7145765656219436
""",
)

entry(
    index = 89,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3.16053e+06,'s^-1'), n=1.87467, w0=(1.183e+06,'J/mol'), E0=(180012,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(6.96433e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(174114,'J/mol'), Tmin=(900,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(6.5e+10,'s^-1'), n=0, w0=(968000,'J/mol'), E0=(139180,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 92,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing",
    kinetics = ArrheniusBM(A=(1.32702e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(152420,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 93,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing",
    kinetics = ArrheniusBM(A=(1.32702e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(150458,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 94,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(7.94328e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(171260,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R",
    kinetics = ArrheniusBM(A=(7.92445e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(169237,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 96,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(7.92445e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(168009,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

