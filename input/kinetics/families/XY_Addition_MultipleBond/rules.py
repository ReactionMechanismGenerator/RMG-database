#!/usr/bin/env python
# encoding: utf-8

name = "XY_Addition_MultipleBond/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(0.028447,'m^3/(mol*s)'), n=2.23348, w0=(763.58,'kJ/mol'), E0=(196.594,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27198628398189917, var=54.63358014416582, Tref=1000.0, N=44, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 44 training reactions at node Root
    Total Standard Deviation in ln(k): 15.501288090276661"""),
    rank = 11,
    shortDesc = """BM rule fitted to 44 training reactions at node Root
Total Standard Deviation in ln(k): 15.501288090276661""",
    longDesc = 
"""
BM rule fitted to 44 training reactions at node Root
Total Standard Deviation in ln(k): 15.501288090276661
""",
)

entry(
    index = 2,
    label = "YY",
    kinetics = ArrheniusBM(A=(5.93272e-05,'m^3/(mol*s)'), n=2.63647, w0=(575,'kJ/mol'), E0=(143.795,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='YY',), comment="""BM rule fitted to 1 training reactions at node YY
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node YY
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node YY
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "HY",
    kinetics = ArrheniusBM(A=(0.0240004,'m^3/(mol*s)'), n=2.2574, w0=(767.965,'kJ/mol'), E0=(196.747,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2756167650105039, var=55.10697377044372, Tref=1000.0, N=43, data_mean=0.0, correlation='HY',), comment="""BM rule fitted to 43 training reactions at node HY
    Total Standard Deviation in ln(k): 15.574469149614037"""),
    rank = 11,
    shortDesc = """BM rule fitted to 43 training reactions at node HY
Total Standard Deviation in ln(k): 15.574469149614037""",
    longDesc = 
"""
BM rule fitted to 43 training reactions at node HY
Total Standard Deviation in ln(k): 15.574469149614037
""",
)

entry(
    index = 4,
    label = "HF",
    kinetics = ArrheniusBM(A=(0.653344,'m^3/(mol*s)'), n=1.80829, w0=(870.853,'kJ/mol'), E0=(228.503,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.34324272310388415, var=60.681258105328595, Tref=1000.0, N=17, data_mean=0.0, correlation='HF',), comment="""BM rule fitted to 17 training reactions at node HF
    Total Standard Deviation in ln(k): 16.4789394740008"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node HF
Total Standard Deviation in ln(k): 16.4789394740008""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node HF
Total Standard Deviation in ln(k): 16.4789394740008
""",
)

entry(
    index = 5,
    label = "HF_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(2676.63,'m^3/(mol*s)'), n=0.732206, w0=(857.35,'kJ/mol'), E0=(267.068,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13214706218215122, var=14.38614219007748, Tref=1000.0, N=10, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 10 training reactions at node HF_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 7.935801153628251"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node HF_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 7.935801153628251""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node HF_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 7.935801153628251
""",
)

entry(
    index = 6,
    label = "HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(281.116,'m^3/(mol*s)'), n=1.03051, w0=(858.5,'kJ/mol'), E0=(265.512,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17160344105964337, var=17.74244203879562, Tref=1000.0, N=7, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 7 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 8.875465065002897"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 8.875465065002897""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 8.875465065002897
""",
)

entry(
    index = 7,
    label = "HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F",
    kinetics = ArrheniusBM(A=(3027.76,'m^3/(mol*s)'), n=0.596786, w0=(858.5,'kJ/mol'), E0=(226.978,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06681560721952781, var=6.699388179313154, Tref=1000.0, N=4, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F',), comment="""BM rule fitted to 4 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F
    Total Standard Deviation in ln(k): 5.356769564290422"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F
Total Standard Deviation in ln(k): 5.356769564290422""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F
Total Standard Deviation in ln(k): 5.356769564290422
""",
)

entry(
    index = 8,
    label = "HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(2440.53,'m^3/(mol*s)'), n=0.555273, w0=(858.5,'kJ/mol'), E0=(216.4,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02490224669972618, var=24.454414706883135, Tref=1000.0, N=2, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 9.976265110848908"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 9.976265110848908""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 9.976265110848908
""",
)

entry(
    index = 9,
    label = "HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(26.4943,'m^3/(mol*s)'), n=1.22463, w0=(858.5,'kJ/mol'), E0=(202.651,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(4.14111,'m^3/(mol*s)'), n=1.29695, w0=(858.5,'kJ/mol'), E0=(229.224,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(2.27849,'m^3/(mol*s)'), n=1.65314, w0=(858.5,'kJ/mol'), E0=(267.218,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1181263725183278, var=20.134991404333217, Tref=1000.0, N=3, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F',), comment="""BM rule fitted to 3 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F
    Total Standard Deviation in ln(k): 9.292453327655394"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F
Total Standard Deviation in ln(k): 9.292453327655394""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F
Total Standard Deviation in ln(k): 9.292453327655394
""",
)

entry(
    index = 12,
    label = "HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_5R!H->C",
    kinetics = ArrheniusBM(A=(3.17276,'m^3/(mol*s)'), n=1.63179, w0=(858.5,'kJ/mol'), E0=(244.477,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.21211,'m^3/(mol*s)'), n=1.56677, w0=(858.5,'kJ/mol'), E0=(279.435,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0965432961962947, var=20.184873005890502, Tref=1000.0, N=2, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_N-5R!H->C
    Total Standard Deviation in ln(k): 9.249360331388786"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_N-5R!H->C
Total Standard Deviation in ln(k): 9.249360331388786""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_N-5R!H->C
Total Standard Deviation in ln(k): 9.249360331388786
""",
)

entry(
    index = 14,
    label = "HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_N-5R!H->C_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(12.2191,'m^3/(mol*s)'), n=1.4473, w0=(858.5,'kJ/mol'), E0=(294.534,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_N-5R!H->C_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_N-5R!H->C_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_N-5R!H->C_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_N-5R!H->C_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "HF_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(51.7395,'m^3/(mol*s)'), n=1.07494, w0=(858.5,'kJ/mol'), E0=(246.546,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07038556604361025, var=0.028808843118544165, Tref=1000.0, N=2, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 2 training reactions at node HF_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 0.5171152080743111"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HF_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 0.5171152080743111""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HF_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 0.5171152080743111
""",
)

entry(
    index = 16,
    label = "HF_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(52.9173,'m^3/(mol*s)'), n=1.09798, w0=(858.5,'kJ/mol'), E0=(248.605,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R',), comment="""BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "HF_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(1.64483e+40,'m^3/(mol*s)'), n=-10.004, w0=(847,'kJ/mol'), E0=(367.576,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "HF_3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(1.56721e+32,'m^3/(mol*s)'), n=-7.40875, w0=(847,'kJ/mol'), E0=(355.078,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node HF_3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "HF_N-3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(7.15746e-06,'m^3/(mol*s)'), n=3.27904, w0=(897.333,'kJ/mol'), E0=(176.779,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.6829136876314708, var=127.63224188496864, Tref=1000.0, N=6, data_mean=0.0, correlation='HF_N-3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 6 training reactions at node HF_N-3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 26.876808706980242"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node HF_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 26.876808706980242""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node HF_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 26.876808706980242
""",
)

entry(
    index = 20,
    label = "HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd",
    kinetics = ArrheniusBM(A=(167.217,'m^3/(mol*s)'), n=1.01268, w0=(858.5,'kJ/mol'), E0=(234.437,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3954564215730427, var=10.649708642214344, Tref=1000.0, N=4, data_mean=0.0, correlation='HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd',), comment="""BM rule fitted to 4 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd
    Total Standard Deviation in ln(k): 10.048402582324789"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd
Total Standard Deviation in ln(k): 10.048402582324789""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd
Total Standard Deviation in ln(k): 10.048402582324789
""",
)

entry(
    index = 21,
    label = "HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(206.949,'m^3/(mol*s)'), n=0.980812, w0=(858.5,'kJ/mol'), E0=(235.915,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.7409598738204388, var=13.196736814099648, Tref=1000.0, N=3, data_mean=0.0, correlation='HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.656934935642514"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.656934935642514""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.656934935642514
""",
)

entry(
    index = 22,
    label = "HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->F",
    kinetics = ArrheniusBM(A=(4.45081,'m^3/(mol*s)'), n=1.42123, w0=(858.5,'kJ/mol'), E0=(210.726,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00864848764295419, var=2.188324134359652, Tref=1000.0, N=2, data_mean=0.0, correlation='HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->F',), comment="""BM rule fitted to 2 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->F
    Total Standard Deviation in ln(k): 2.98733151707349"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->F
Total Standard Deviation in ln(k): 2.98733151707349""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->F
Total Standard Deviation in ln(k): 2.98733151707349
""",
)

entry(
    index = 23,
    label = "HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(10.477,'m^3/(mol*s)'), n=1.29062, w0=(858.5,'kJ/mol'), E0=(214.73,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(25.0352,'m^3/(mol*s)'), n=1.25316, w0=(858.5,'kJ/mol'), E0=(238.936,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd",
    kinetics = ArrheniusBM(A=(7.04118e-08,'m^3/(mol*s)'), n=3.98107, w0=(975,'kJ/mol'), E0=(139.627,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.8966013497491856, var=40.52401585746036, Tref=1000.0, N=2, data_mean=0.0, correlation='HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd',), comment="""BM rule fitted to 2 training reactions at node HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd
    Total Standard Deviation in ln(k): 22.55229366378175"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd
Total Standard Deviation in ln(k): 22.55229366378175""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd
Total Standard Deviation in ln(k): 22.55229366378175
""",
)

entry(
    index = 26,
    label = "HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd_4COCdCddCtO2d->Cdd",
    kinetics = ArrheniusBM(A=(7.80335e-09,'m^3/(mol*s)'), n=4.28272, w0=(975,'kJ/mol'), E0=(135.901,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd_4COCdCddCtO2d->Cdd',), comment="""BM rule fitted to 1 training reactions at node HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd_4COCdCddCtO2d->Cdd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd_4COCdCddCtO2d->Cdd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd_4COCdCddCtO2d->Cdd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd_N-4COCdCddCtO2d->Cdd",
    kinetics = ArrheniusBM(A=(0.109156,'m^3/(mol*s)'), n=1.86531, w0=(975,'kJ/mol'), E0=(171.326,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd_N-4COCdCddCtO2d->Cdd',), comment="""BM rule fitted to 1 training reactions at node HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd_N-4COCdCddCtO2d->Cdd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd_N-4COCdCddCtO2d->Cdd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd_N-4COCdCddCtO2d->Cdd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "HCl",
    kinetics = ArrheniusBM(A=(5.48856e-05,'m^3/(mol*s)'), n=3.0181, w0=(714.278,'kJ/mol'), E0=(162.505,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.0640153826859446, var=78.08557668548691, Tref=1000.0, N=18, data_mean=0.0, correlation='HCl',), comment="""BM rule fitted to 18 training reactions at node HCl
    Total Standard Deviation in ln(k): 22.901019031728016"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node HCl
Total Standard Deviation in ln(k): 22.901019031728016""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node HCl
Total Standard Deviation in ln(k): 22.901019031728016
""",
)

entry(
    index = 29,
    label = "HCl_3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(8927.63,'m^3/(mol*s)'), n=0.40345, w0=(711,'kJ/mol'), E0=(209.763,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14144903840385278, var=2.37892262192723, Tref=1000.0, N=12, data_mean=0.0, correlation='HCl_3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 12 training reactions at node HCl_3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 3.4474541465951307"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node HCl_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 3.4474541465951307""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node HCl_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 3.4474541465951307
""",
)

entry(
    index = 30,
    label = "HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(502.817,'m^3/(mol*s)'), n=0.747227, w0=(711,'kJ/mol'), E0=(207.958,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1764784684970972, var=3.3115852625941296, Tref=1000.0, N=7, data_mean=0.0, correlation='HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R',), comment="""BM rule fitted to 7 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R
    Total Standard Deviation in ln(k): 4.0915823329287555"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R
Total Standard Deviation in ln(k): 4.0915823329287555""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R
Total Standard Deviation in ln(k): 4.0915823329287555
""",
)

entry(
    index = 31,
    label = "HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(24408.1,'m^3/(mol*s)'), n=0.242663, w0=(711,'kJ/mol'), E0=(208.95,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1534023098182822, var=3.4199111846926074, Tref=1000.0, N=6, data_mean=0.0, correlation='HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl',), comment="""BM rule fitted to 6 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl
    Total Standard Deviation in ln(k): 4.092789894407894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl
Total Standard Deviation in ln(k): 4.092789894407894""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl
Total Standard Deviation in ln(k): 4.092789894407894
""",
)

entry(
    index = 32,
    label = "HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(25761.3,'m^3/(mol*s)'), n=0.211093, w0=(711,'kJ/mol'), E0=(206.552,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1695122552558417, var=13.236968003731597, Tref=1000.0, N=3, data_mean=0.0, correlation='HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R',), comment="""BM rule fitted to 3 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
    Total Standard Deviation in ln(k): 7.719666496521855"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
Total Standard Deviation in ln(k): 7.719666496521855""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
Total Standard Deviation in ln(k): 7.719666496521855
""",
)

entry(
    index = 33,
    label = "HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(4061.07,'m^3/(mol*s)'), n=0.468608, w0=(711,'kJ/mol'), E0=(200.462,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18985986566819624, var=36.555013946038976, Tref=1000.0, N=2, data_mean=0.0, correlation='HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 12.597811986024832"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.597811986024832""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.597811986024832
""",
)

entry(
    index = 34,
    label = "HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.0823032,'m^3/(mol*s)'), n=1.92336, w0=(711,'kJ/mol'), E0=(212.188,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(5.59096e+06,'m^3/(mol*s)'), n=-0.339093, w0=(711,'kJ/mol'), E0=(221.524,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.18057,'m^3/(mol*s)'), n=1.62936, w0=(711,'kJ/mol'), E0=(220.864,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(1.24269e+07,'m^3/(mol*s)'), n=-0.625235, w0=(711,'kJ/mol'), E0=(214.368,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14676512464793026, var=1.1892566407540952, Tref=1000.0, N=3, data_mean=0.0, correlation='HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 2.554981220799192"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 2.554981220799192""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 2.554981220799192
""",
)

entry(
    index = 38,
    label = "HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(1.25612e+07,'m^3/(mol*s)'), n=-0.637747, w0=(711,'kJ/mol'), E0=(216.725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.1566e+06,'m^3/(mol*s)'), n=-0.375399, w0=(711,'kJ/mol'), E0=(213.154,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.6085e+08,'m^3/(mol*s)'), n=-0.88707, w0=(711,'kJ/mol'), E0=(213.432,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "HCl_N-3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(3.52442e-47,'m^3/(mol*s)'), n=15.2891, w0=(720.833,'kJ/mol'), E0=(13.9624,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-6.381073649290554, var=105.4750823009359, Tref=1000.0, N=6, data_mean=0.0, correlation='HCl_N-3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 6 training reactions at node HCl_N-3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 36.62169060466086"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node HCl_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 36.62169060466086""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node HCl_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 36.62169060466086
""",
)

entry(
    index = 42,
    label = "HCl_N-3COCdCddCtO2d->Cd_Ext-3COCddCtO2d-R",
    kinetics = ArrheniusBM(A=(23.9499,'m^3/(mol*s)'), n=1.57664, w0=(699.5,'kJ/mol'), E0=(220.022,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11479703517840109, var=2.220048147829502, Tref=1000.0, N=2, data_mean=0.0, correlation='HCl_N-3COCdCddCtO2d->Cd_Ext-3COCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-3COCddCtO2d-R
    Total Standard Deviation in ln(k): 3.2754551443633115"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-3COCddCtO2d-R
Total Standard Deviation in ln(k): 3.2754551443633115""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-3COCddCtO2d-R
Total Standard Deviation in ln(k): 3.2754551443633115
""",
)

entry(
    index = 43,
    label = "HCl_N-3COCdCddCtO2d->Cd_Ext-3COCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(40.7026,'m^3/(mol*s)'), n=1.65435, w0=(699.5,'kJ/mol'), E0=(224.765,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HCl_N-3COCdCddCtO2d->Cd_Ext-3COCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-3COCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-3COCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-3COCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(3.0891e-21,'m^3/(mol*s)'), n=7.90019, w0=(763.5,'kJ/mol'), E0=(84.8721,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-9.186921148287965, var=217.58696518220182, Tref=1000.0, N=2, data_mean=0.0, correlation='HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 52.65422138116475"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 52.65422138116475""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 52.65422138116475
""",
)

entry(
    index = 45,
    label = "HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_3COCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(1.62705,'m^3/(mol*s)'), n=1.85266, w0=(699.5,'kJ/mol'), E0=(214.967,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_3COCddCtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_3COCddCtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_3COCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_3COCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-3COCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(1.09358e-06,'m^3/(mol*s)'), n=3.74071, w0=(827.5,'kJ/mol'), E0=(115.913,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-3COCddCtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-3COCddCtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-3COCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-3COCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "HBr",
    kinetics = ArrheniusBM(A=(6.6953e-10,'m^3/(mol*s)'), n=4.46462, w0=(670.125,'kJ/mol'), E0=(161.234,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7769490982335523, var=71.60651871923542, Tref=1000.0, N=8, data_mean=0.0, correlation='HBr',), comment="""BM rule fitted to 8 training reactions at node HBr
    Total Standard Deviation in ln(k): 18.916328943114383"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node HBr
Total Standard Deviation in ln(k): 18.916328943114383""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node HBr
Total Standard Deviation in ln(k): 18.916328943114383
""",
)

entry(
    index = 48,
    label = "HBr_3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=1.23855e-08, w0=(645.5,'kJ/mol'), E0=(276.822,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HBr_3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node HBr_3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HBr_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HBr_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "HBr_N-3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(4.35386e-09,'m^3/(mol*s)'), n=4.23233, w0=(673.643,'kJ/mol'), E0=(161.619,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7252249399811629, var=72.23265453066445, Tref=1000.0, N=7, data_mean=0.0, correlation='HBr_N-3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 7 training reactions at node HBr_N-3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 18.8603757763477"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node HBr_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 18.8603757763477""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node HBr_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 18.8603757763477
""",
)

entry(
    index = 50,
    label = "HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R",
    kinetics = ArrheniusBM(A=(0.00276936,'m^3/(mol*s)'), n=2.5124, w0=(657,'kJ/mol'), E0=(207.548,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2728397829758924, var=35.358699550569156, Tref=1000.0, N=4, data_mean=0.0, correlation='HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R',), comment="""BM rule fitted to 4 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R
    Total Standard Deviation in ln(k): 12.60631967116444"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R
Total Standard Deviation in ln(k): 12.60631967116444""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R
Total Standard Deviation in ln(k): 12.60631967116444
""",
)

entry(
    index = 51,
    label = "HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.18878,'m^3/(mol*s)'), n=1.76475, w0=(657,'kJ/mol'), E0=(181.27,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.682723,'m^3/(mol*s)'), n=1.82397, w0=(657,'kJ/mol'), E0=(229.072,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15537505922972966, var=37.58518162440205, Tref=1000.0, N=3, data_mean=0.0, correlation='HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C',), comment="""BM rule fitted to 3 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C
    Total Standard Deviation in ln(k): 12.680769743504904"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 12.680769743504904""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 12.680769743504904
""",
)

entry(
    index = 53,
    label = "HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C_Ext-3COCdCddO2d-R",
    kinetics = ArrheniusBM(A=(11.1903,'m^3/(mol*s)'), n=1.45044, w0=(657,'kJ/mol'), E0=(249.23,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.9517481442553708, var=14.45822739136675, Tref=1000.0, N=2, data_mean=0.0, correlation='HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C_Ext-3COCdCddO2d-R',), comment="""BM rule fitted to 2 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C_Ext-3COCdCddO2d-R
    Total Standard Deviation in ln(k): 12.52668962573185"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C_Ext-3COCdCddO2d-R
Total Standard Deviation in ln(k): 12.52668962573185""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C_Ext-3COCdCddO2d-R
Total Standard Deviation in ln(k): 12.52668962573185
""",
)

entry(
    index = 54,
    label = "HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C_Ext-3COCdCddO2d-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.882649,'m^3/(mol*s)'), n=1.68333, w0=(657,'kJ/mol'), E0=(221.222,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C_Ext-3COCdCddO2d-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C_Ext-3COCdCddO2d-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C_Ext-3COCdCddO2d-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C_Ext-3COCdCddO2d-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(1.73679e-06,'m^3/(mol*s)'), n=3.56188, w0=(715.25,'kJ/mol'), E0=(130.344,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.2248323866313604, var=180.89200833193857, Tref=1000.0, N=2, data_mean=0.0, correlation='HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 32.55293600533558"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 32.55293600533558""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 32.55293600533558
""",
)

entry(
    index = 56,
    label = "HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3COCdCddO2d->Cd",
    kinetics = ArrheniusBM(A=(6.29599,'m^3/(mol*s)'), n=1.45405, w0=(657,'kJ/mol'), E0=(183.226,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3COCdCddO2d->Cd',), comment="""BM rule fitted to 1 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3COCdCddO2d->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3COCdCddO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3COCdCddO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3COCdCddO2d->Cd",
    kinetics = ArrheniusBM(A=(2.0193e-06,'m^3/(mol*s)'), n=3.68936, w0=(773.5,'kJ/mol'), E0=(107.088,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3COCdCddO2d->Cd',), comment="""BM rule fitted to 1 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3COCdCddO2d->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3COCdCddO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3COCdCddO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

