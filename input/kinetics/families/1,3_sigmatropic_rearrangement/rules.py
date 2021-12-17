#!/usr/bin/env python
# encoding: utf-8

name = "1,3_sigmatropic_rearrangement/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(4.62709e+20,'s^-1'), n=-1.9758, w0=(661.267,'kJ/mol'), E0=(230.31,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1791595854394145, var=100.97114496904264, Tref=1000.0, N=30, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 30 training reactions at node Root
    Total Standard Deviation in ln(k): 20.594609707154852"""),
    rank = 11,
    shortDesc = """BM rule fitted to 30 training reactions at node Root
Total Standard Deviation in ln(k): 20.594609707154852""",
    longDesc = 
"""
BM rule fitted to 30 training reactions at node Root
Total Standard Deviation in ln(k): 20.594609707154852
""",
)

entry(
    index = 2,
    label = "Val7",
    kinetics = ArrheniusBM(A=(1.35042e+06,'s^-1'), n=2.07053, w0=(621.667,'kJ/mol'), E0=(235.218,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13702080962209845, var=45.969217417088366, Tref=1000.0, N=6, data_mean=0.0, correlation='Val7',), comment="""BM rule fitted to 6 training reactions at node Val7
    Total Standard Deviation in ln(k): 13.93649806363523"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Val7
Total Standard Deviation in ln(k): 13.93649806363523""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Val7
Total Standard Deviation in ln(k): 13.93649806363523
""",
)

entry(
    index = 3,
    label = "F",
    kinetics = ArrheniusBM(A=(8.88952e+10,'s^-1'), n=0.725184, w0=(741,'kJ/mol'), E0=(308.465,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005830439029566195, var=4.831276094152293, Tref=1000.0, N=2, data_mean=0.0, correlation='F',), comment="""BM rule fitted to 2 training reactions at node F
    Total Standard Deviation in ln(k): 4.421089921827352"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node F
Total Standard Deviation in ln(k): 4.421089921827352""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node F
Total Standard Deviation in ln(k): 4.421089921827352
""",
)

entry(
    index = 4,
    label = "F_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.72966e+11,'s^-1'), n=0.63878, w0=(741,'kJ/mol'), E0=(308.698,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='F_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node F_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node F_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node F_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Cl",
    kinetics = ArrheniusBM(A=(4.21258e+11,'s^-1'), n=0.487025, w0=(583,'kJ/mol'), E0=(230.521,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005445922515396561, var=0.10372712383063162, Tref=1000.0, N=2, data_mean=0.0, correlation='Cl',), comment="""BM rule fitted to 2 training reactions at node Cl
    Total Standard Deviation in ln(k): 0.6593421453782854"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Cl
Total Standard Deviation in ln(k): 0.6593421453782854""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Cl
Total Standard Deviation in ln(k): 0.6593421453782854
""",
)

entry(
    index = 6,
    label = "Cl_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.046e+12,'s^-1'), n=0.380659, w0=(583,'kJ/mol'), E0=(230.604,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Cl_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Cl_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Cl_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Cl_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Br",
    kinetics = ArrheniusBM(A=(6.98407e+11,'s^-1'), n=0.40768, w0=(541,'kJ/mol'), E0=(206.795,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005374602454959144, var=0.05576325998061254, Tref=1000.0, N=2, data_mean=0.0, correlation='Br',), comment="""BM rule fitted to 2 training reactions at node Br
    Total Standard Deviation in ln(k): 0.4869070930048853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Br
Total Standard Deviation in ln(k): 0.4869070930048853""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Br
Total Standard Deviation in ln(k): 0.4869070930048853
""",
)

entry(
    index = 8,
    label = "Br_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.94657e+12,'s^-1'), n=0.28187, w0=(541,'kJ/mol'), E0=(206.892,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Br_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Br_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Br_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Br_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.5659e-18,'s^-1'), n=8.82896, w0=(636.417,'kJ/mol'), E0=(92.6622,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0427256511248497, var=24.806441277129125, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R
    Total Standard Deviation in ln(k): 12.604710287610498"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R
Total Standard Deviation in ln(k): 12.604710287610498""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R
Total Standard Deviation in ln(k): 12.604710287610498
""",
)

entry(
    index = 10,
    label = "Root_Ext-2R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.95709e-15,'s^-1'), n=7.94274, w0=(624.125,'kJ/mol'), E0=(20.1053,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8310518184596639, var=1.434090971903425, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 4.488811066240199"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_5R!H->C
Total Standard Deviation in ln(k): 4.488811066240199""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_5R!H->C
Total Standard Deviation in ln(k): 4.488811066240199
""",
)

entry(
    index = 11,
    label = "Root_Ext-2R!H-R_5R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(7.98007e+11,'s^-1'), n=0.338845, w0=(615,'kJ/mol'), E0=(214.843,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_Ext-2R!H-R_5R!H->C_4R!H->C",
    kinetics = ArrheniusBM(A=(1.5457e-15,'s^-1'), n=7.99283, w0=(661,'kJ/mol'), E0=(73.8713,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04612428440969387, var=12.311106005154134, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R!H->C
    Total Standard Deviation in ln(k): 7.1499413562997525"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R!H->C
Total Standard Deviation in ln(k): 7.1499413562997525""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R!H->C
Total Standard Deviation in ln(k): 7.1499413562997525
""",
)

entry(
    index = 13,
    label = "Root_Ext-2R!H-R_5R!H->C_4R!H->C_3R!H->O",
    kinetics = ArrheniusBM(A=(7.58556e+11,'s^-1'), n=0.301396, w0=(707,'kJ/mol'), E0=(174.853,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C_4R!H->C_3R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R!H->C_3R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R!H->C_3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R!H->C_3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_Ext-2R!H-R_5R!H->C_4R!H->C_N-3R!H->O",
    kinetics = ArrheniusBM(A=(1.00046e+12,'s^-1'), n=0.355217, w0=(615,'kJ/mol'), E0=(207.623,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C_4R!H->C_N-3R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R!H->C_N-3R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R!H->C_N-3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R!H->C_N-3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_Ext-2R!H-R_5R!H->C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(7.5809e+11,'s^-1'), n=0.263048, w0=(559.5,'kJ/mol'), E0=(129.955,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_Ext-2R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.9883e-08,'s^-1'), n=5.93443, w0=(661,'kJ/mol'), E0=(167.822,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07469005080102858, var=48.17978623090899, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 14.102862516717794"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 14.102862516717794""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 14.102862516717794
""",
)

entry(
    index = 17,
    label = "Root_Ext-2R!H-R_N-5R!H->C_3R!H->O",
    kinetics = ArrheniusBM(A=(9.08391e+10,'s^-1'), n=0.559605, w0=(707,'kJ/mol'), E0=(195.781,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_N-5R!H->C_3R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_3R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_Ext-2R!H-R_N-5R!H->C_N-3R!H->O",
    kinetics = ArrheniusBM(A=(3.90941e+10,'s^-1'), n=0.721594, w0=(615,'kJ/mol'), E0=(243.677,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_N-5R!H->C_N-3R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-3R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_1R!H-inRing",
    kinetics = ArrheniusBM(A=(4.09884e+62,'s^-1'), n=-13.6281, w0=(654.062,'kJ/mol'), E0=(393.331,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1335689029548193, var=267.23618516426137, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H-inRing',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H-inRing
    Total Standard Deviation in ln(k): 35.62028946737728"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 35.62028946737728""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 35.62028946737728
""",
)

entry(
    index = 20,
    label = "Root_1R!H-inRing_2R!H->N",
    kinetics = ArrheniusBM(A=(8.55465e+83,'s^-1'), n=-19.7138, w0=(638,'kJ/mol'), E0=(473.955,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.984902132895148, var=290.9878984709789, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->N
    Total Standard Deviation in ln(k): 39.18469878544792"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 39.18469878544792""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 39.18469878544792
""",
)

entry(
    index = 21,
    label = "Root_1R!H-inRing_2R!H->N_3R!H->O",
    kinetics = ArrheniusBM(A=(1.5373e+10,'s^-1'), n=1.12018, w0=(707,'kJ/mol'), E0=(430.011,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_3R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_1R!H-inRing_2R!H->N_N-3R!H->O",
    kinetics = ArrheniusBM(A=(1.87437e+22,'s^-1'), n=-1.94921, w0=(615,'kJ/mol'), E0=(254.763,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12904900725763888, var=8.604042563041212, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_N-3R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->N_N-3R!H->O
    Total Standard Deviation in ln(k): 6.204662632858932"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->N_N-3R!H->O
Total Standard Deviation in ln(k): 6.204662632858932""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->N_N-3R!H->O
Total Standard Deviation in ln(k): 6.204662632858932
""",
)

entry(
    index = 23,
    label = "Root_1R!H-inRing_2R!H->N_N-3R!H->O_Ext-4R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(9.89708e+10,'s^-1'), n=1.27855, w0=(615,'kJ/mol'), E0=(209.592,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.593522517516603, var=1.1713073946783865, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_N-3R!H->O_Ext-4R!H-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H-inRing_2R!H->N_N-3R!H->O_Ext-4R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 3.6609263515593344"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H-inRing_2R!H->N_N-3R!H->O_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 3.6609263515593344""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H-inRing_2R!H->N_N-3R!H->O_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 3.6609263515593344
""",
)

entry(
    index = 24,
    label = "Root_1R!H-inRing_2R!H->N_N-3R!H->O_Ext-4R!H-R_5R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.04679e+11,'s^-1'), n=1.26667, w0=(615,'kJ/mol'), E0=(213.42,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_N-3R!H->O_Ext-4R!H-R_5R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_N-3R!H->O_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_N-3R!H->O_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_N-3R!H->O_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_1R!H-inRing_2R!H->N_N-3R!H->O_Ext-4R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(6.1544e+10,'s^-1'), n=1.34775, w0=(615,'kJ/mol'), E0=(243.181,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_N-3R!H->O_Ext-4R!H-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_N-3R!H->O_Ext-4R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_N-3R!H->O_Ext-4R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_N-3R!H->O_Ext-4R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_1R!H-inRing_N-2R!H->N",
    kinetics = ArrheniusBM(A=(2.11233e+54,'s^-1'), n=-11.2761, w0=(670.125,'kJ/mol'), E0=(348.536,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1010721656624907, var=535.9541571115086, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-2R!H->N
    Total Standard Deviation in ln(k): 49.177500715859736"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 49.177500715859736""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 49.177500715859736
""",
)

entry(
    index = 27,
    label = "Root_1R!H-inRing_N-2R!H->N_4R!H->C",
    kinetics = ArrheniusBM(A=(2.13413e+64,'s^-1'), n=-14.1604, w0=(707,'kJ/mol'), E0=(408.871,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2129077816718887, var=743.8552286585011, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->C
    Total Standard Deviation in ln(k): 57.724069069158396"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->C
Total Standard Deviation in ln(k): 57.724069069158396""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->C
Total Standard Deviation in ln(k): 57.724069069158396
""",
)

entry(
    index = 28,
    label = "Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(2.1761e+10,'s^-1'), n=0.996245, w0=(707,'kJ/mol'), E0=(430.331,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.6259e+11,'s^-1'), n=1.19107, w0=(707,'kJ/mol'), E0=(173.852,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.23586e+11,'s^-1'), n=1.27308, w0=(707,'kJ/mol'), E0=(195.192,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_1R!H-inRing_N-2R!H->N_N-4R!H->C",
    kinetics = ArrheniusBM(A=(4.0435e+11,'s^-1'), n=1.01704, w0=(559.5,'kJ/mol'), E0=(129.258,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(9.0076e+11,'s^-1'), n=0.329287, w0=(705.7,'kJ/mol'), E0=(161.603,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0025732519232941767, var=18.851259202467745, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R!H-inRing',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing
    Total Standard Deviation in ln(k): 8.710631595119949"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 8.710631595119949""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 8.710631595119949
""",
)

entry(
    index = 33,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(9.39365e+11,'s^-1'), n=0.324012, w0=(707,'kJ/mol'), E0=(160.927,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.014478493324023197, var=15.997960675483611, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 8.054807379047233"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 8.054807379047233""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 8.054807379047233
""",
)

entry(
    index = 34,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N",
    kinetics = ArrheniusBM(A=(2.25992e+12,'s^-1'), n=0.319504, w0=(707,'kJ/mol'), E0=(161.393,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.035501914037364954, var=26.701526865360545, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N
    Total Standard Deviation in ln(k): 10.448372634328592"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N
Total Standard Deviation in ln(k): 10.448372634328592""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N
Total Standard Deviation in ln(k): 10.448372634328592
""",
)

entry(
    index = 35,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O",
    kinetics = ArrheniusBM(A=(6.69766e+12,'s^-1'), n=0.201965, w0=(707,'kJ/mol'), E0=(149.484,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04788796823021864, var=12.238168810426563, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O
    Total Standard Deviation in ln(k): 7.133505137612127"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O
Total Standard Deviation in ln(k): 7.133505137612127""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O
Total Standard Deviation in ln(k): 7.133505137612127
""",
)

entry(
    index = 36,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.88231e+11,'s^-1'), n=0.661449, w0=(707,'kJ/mol'), E0=(169.151,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3.57015e+11,'s^-1'), n=0.576299, w0=(707,'kJ/mol'), E0=(134.76,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_N-5R!H->O",
    kinetics = ArrheniusBM(A=(2.30252e+10,'s^-1'), n=0.837267, w0=(707,'kJ/mol'), E0=(195.498,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N",
    kinetics = ArrheniusBM(A=(3.87938e+11,'s^-1'), n=0.329327, w0=(707,'kJ/mol'), E0=(160.454,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05762531572433656, var=20.867881145135676, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N
    Total Standard Deviation in ln(k): 9.302692913286272"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N
Total Standard Deviation in ln(k): 9.302692913286272""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N
Total Standard Deviation in ln(k): 9.302692913286272
""",
)

entry(
    index = 40,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_5R!H->N",
    kinetics = ArrheniusBM(A=(1.75947e+10,'s^-1'), n=0.744308, w0=(707,'kJ/mol'), E0=(181.655,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.034672889254872365, var=21.50295609646255, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_5R!H->N
    Total Standard Deviation in ln(k): 9.383330973910947"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_5R!H->N
Total Standard Deviation in ln(k): 9.383330973910947""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_5R!H->N
Total Standard Deviation in ln(k): 9.383330973910947
""",
)

entry(
    index = 41,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_5R!H->N_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.10312e+11,'s^-1'), n=0.507696, w0=(707,'kJ/mol'), E0=(169.397,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_5R!H->N_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_5R!H->N_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_5R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_5R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_N-5R!H->N",
    kinetics = ArrheniusBM(A=(1.84715e+10,'s^-1'), n=0.67809, w0=(707,'kJ/mol'), E0=(132.312,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.048202910326213814, var=1.7746490017039065, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_N-5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_N-5R!H->N
    Total Standard Deviation in ln(k): 2.7917397697136175"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_N-5R!H->N
Total Standard Deviation in ln(k): 2.7917397697136175""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_N-5R!H->N
Total Standard Deviation in ln(k): 2.7917397697136175
""",
)

entry(
    index = 43,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_N-5R!H->N_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.85823e+11,'s^-1'), n=0.331305, w0=(707,'kJ/mol'), E0=(135.231,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_N-5R!H->N_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_N-5R!H->N_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_N-5R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_N-5R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_N-1R!H-inRing_2R!H->C",
    kinetics = ArrheniusBM(A=(3431.13,'s^-1'), n=2.77015, w0=(700.5,'kJ/mol'), E0=(390.126,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_N-1R!H-inRing_N-2R!H->C",
    kinetics = ArrheniusBM(A=(7040,'s^-1'), n=2.66, w0=(700.5,'kJ/mol'), E0=(390.574,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

