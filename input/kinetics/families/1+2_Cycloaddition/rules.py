#!/usr/bin/env python
# encoding: utf-8

name = "1+2_Cycloaddition/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.18531e+08,'m^3/(mol*s)'), n=-0.419689, w0=(476125,'J/mol'), E0=(47612.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04841965298396951, var=2.5296165798409285, Tref=1000.0, N=12, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 12 training reactions at node Root
    Total Standard Deviation in ln(k): 3.310142131285644"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root
Total Standard Deviation in ln(k): 3.310142131285644""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root
Total Standard Deviation in ln(k): 3.310142131285644
""",
)

entry(
    index = 2,
    label = "Root_Ext-1COCSCdCddCtN-R",
    kinetics = ArrheniusBM(A=(2.6663e+09,'m^3/(mol*s)'), n=-0.710175, w0=(474200,'J/mol'), E0=(47420,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.002619194066175809, var=0.5010693918602309, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-1COCSCdCddCtN-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-1COCSCdCddCtN-R
    Total Standard Deviation in ln(k): 1.4256577766417744"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-1COCSCdCddCtN-R
Total Standard Deviation in ln(k): 1.4256577766417744""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-1COCSCdCddCtN-R
Total Standard Deviation in ln(k): 1.4256577766417744
""",
)

entry(
    index = 3,
    label = "Root_Ext-2CdCddCtNOS-R",
    kinetics = ArrheniusBM(A=(3.54171e+09,'m^3/(mol*s)'), n=-0.784632, w0=(480000,'J/mol'), E0=(48000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0327162239275991, var=0.14329754440144252, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2CdCddCtNOS-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2CdCddCtNOS-R
    Total Standard Deviation in ln(k): 0.8410872575516879"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2CdCddCtNOS-R
Total Standard Deviation in ln(k): 0.8410872575516879""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2CdCddCtNOS-R
Total Standard Deviation in ln(k): 0.8410872575516879
""",
)

entry(
    index = 4,
    label = "Root_1COCSCdCddCtN->Cd",
    kinetics = ArrheniusBM(A=(0.00011503,'m^3/(mol*s)'), n=3.01629, w0=(480000,'J/mol'), E0=(48000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.587997258796586, var=0.16964704494037178, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1COCSCdCddCtN->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_1COCSCdCddCtN->Cd
    Total Standard Deviation in ln(k): 4.815657794528946"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1COCSCdCddCtN->Cd
Total Standard Deviation in ln(k): 4.815657794528946""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1COCSCdCddCtN->Cd
Total Standard Deviation in ln(k): 4.815657794528946
""",
)

entry(
    index = 5,
    label = "Root_N-1COCSCdCddCtN->Cd",
    kinetics = ArrheniusBM(A=(1.77e+09,'m^3/(mol*s)'), n=-0.662, w0=(462500,'J/mol'), E0=(46250,'J/mol'), Tmin=(200,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCSCdCddCtN->Cd',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCSCdCddCtN->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCSCdCddCtN->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCSCdCddCtN->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_Ext-1COCSCdCddCtN-R_Ext-1COCSCdCddCtN-R",
    kinetics = ArrheniusBM(A=(3.18e+07,'m^3/(mol*s)'), n=0, w0=(486000,'J/mol'), E0=(48600,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCdCddCtN-R_Ext-1COCSCdCddCtN-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCdCddCtN-R_Ext-1COCSCdCddCtN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCdCddCtN-R_Ext-1COCSCdCddCtN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCdCddCtN-R_Ext-1COCSCdCddCtN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_Ext-1COCSCdCddCtN-R_1COCSCdCddCtN->Ct",
    kinetics = ArrheniusBM(A=(4.63926e+09,'m^3/(mol*s)'), n=-0.766621, w0=(462500,'J/mol'), E0=(46250,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0009309671137264789, var=1.1655949953965052, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCdCddCtN-R_1COCSCdCddCtN->Ct',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCdCddCtN-R_1COCSCdCddCtN->Ct
    Total Standard Deviation in ln(k): 2.1667057286443416"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCdCddCtN-R_1COCSCdCddCtN->Ct
Total Standard Deviation in ln(k): 2.1667057286443416""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCdCddCtN-R_1COCSCdCddCtN->Ct
Total Standard Deviation in ln(k): 2.1667057286443416
""",
)

entry(
    index = 8,
    label = "Root_Ext-1COCSCdCddCtN-R_N-1COCSCdCddCtN->Ct",
    kinetics = ArrheniusBM(A=(1.04505e+09,'m^3/(mol*s)'), n=-0.622717, w0=(480000,'J/mol'), E0=(48000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08355106414541179, var=0.031111968581513858, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCdCddCtN-R_N-1COCSCdCddCtN->Ct',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCdCddCtN-R_N-1COCSCdCddCtN->Ct
    Total Standard Deviation in ln(k): 0.5635342003474927"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCdCddCtN-R_N-1COCSCdCddCtN->Ct
Total Standard Deviation in ln(k): 0.5635342003474927""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCdCddCtN-R_N-1COCSCdCddCtN->Ct
Total Standard Deviation in ln(k): 0.5635342003474927
""",
)

entry(
    index = 9,
    label = "Root_Ext-2CdCddCtNOS-R_3CN1sOS->C",
    kinetics = ArrheniusBM(A=(4.40802e+09,'m^3/(mol*s)'), n=-0.810618, w0=(474000,'J/mol'), E0=(47400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0395530227295251, var=0.0335984334446083, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2CdCddCtNOS-R_3CN1sOS->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2CdCddCtNOS-R_3CN1sOS->C
    Total Standard Deviation in ln(k): 0.46684489712018756"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2CdCddCtNOS-R_3CN1sOS->C
Total Standard Deviation in ln(k): 0.46684489712018756""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2CdCddCtNOS-R_3CN1sOS->C
Total Standard Deviation in ln(k): 0.46684489712018756
""",
)

entry(
    index = 10,
    label = "Root_Ext-2CdCddCtNOS-R_N-3CN1sOS->C",
    kinetics = ArrheniusBM(A=(3.70748e+06,'m^3/(mol*s)'), n=0.0302911, w0=(486000,'J/mol'), E0=(48600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02516094828390788, var=1.7607258136569388, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2CdCddCtNOS-R_N-3CN1sOS->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2CdCddCtNOS-R_N-3CN1sOS->C
    Total Standard Deviation in ln(k): 2.7233484267253916"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2CdCddCtNOS-R_N-3CN1sOS->C
Total Standard Deviation in ln(k): 2.7233484267253916""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2CdCddCtNOS-R_N-3CN1sOS->C
Total Standard Deviation in ln(k): 2.7233484267253916
""",
)

entry(
    index = 11,
    label = "Root_1COCSCdCddCtN->Cd_3CN1sOS->C",
    kinetics = ArrheniusBM(A=(1.98e+06,'m^3/(mol*s)'), n=0, w0=(474000,'J/mol'), E0=(47400,'J/mol'), Tmin=(296,'K'), Tmax=(728,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCSCdCddCtN->Cd_3CN1sOS->C',), comment="""BM rule fitted to 1 training reactions at node Root_1COCSCdCddCtN->Cd_3CN1sOS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCSCdCddCtN->Cd_3CN1sOS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCSCdCddCtN->Cd_3CN1sOS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_1COCSCdCddCtN->Cd_N-3CN1sOS->C",
    kinetics = ArrheniusBM(A=(700000,'m^3/(mol*s)'), n=0, w0=(486000,'J/mol'), E0=(48600,'J/mol'), Tmin=(300,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCSCdCddCtN->Cd_N-3CN1sOS->C',), comment="""BM rule fitted to 1 training reactions at node Root_1COCSCdCddCtN->Cd_N-3CN1sOS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCSCdCddCtN->Cd_N-3CN1sOS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCSCdCddCtN->Cd_N-3CN1sOS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_Ext-1COCSCdCddCtN-R_1COCSCdCddCtN->Ct_Ext-2CdCddCtNOS-R",
    kinetics = ArrheniusBM(A=(4.7e+09,'m^3/(mol*s)'), n=-0.823, w0=(462500,'J/mol'), E0=(46250,'J/mol'), Tmin=(200,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCdCddCtN-R_1COCSCdCddCtN->Ct_Ext-2CdCddCtNOS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCdCddCtN-R_1COCSCdCddCtN->Ct_Ext-2CdCddCtNOS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCdCddCtN-R_1COCSCdCddCtN->Ct_Ext-2CdCddCtNOS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCdCddCtN-R_1COCSCdCddCtN->Ct_Ext-2CdCddCtNOS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_Ext-1COCSCdCddCtN-R_N-1COCSCdCddCtN->Ct_1CdCdd->Cd",
    kinetics = ArrheniusBM(A=(1.54e+07,'m^3/(mol*s)'), n=0, w0=(486000,'J/mol'), E0=(48600,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCdCddCtN-R_N-1COCSCdCddCtN->Ct_1CdCdd->Cd',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCdCddCtN-R_N-1COCSCdCddCtN->Ct_1CdCdd->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCdCddCtN-R_N-1COCSCdCddCtN->Ct_1CdCdd->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCdCddCtN-R_N-1COCSCdCddCtN->Ct_1CdCdd->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_Ext-1COCSCdCddCtN-R_N-1COCSCdCddCtN->Ct_N-1CdCdd->Cd",
    kinetics = ArrheniusBM(A=(6.38e+08,'m^3/(mol*s)'), n=-0.562, w0=(474000,'J/mol'), E0=(47400,'J/mol'), Tmin=(200,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCdCddCtN-R_N-1COCSCdCddCtN->Ct_N-1CdCdd->Cd',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCdCddCtN-R_N-1COCSCdCddCtN->Ct_N-1CdCdd->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCdCddCtN-R_N-1COCSCdCddCtN->Ct_N-1CdCdd->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCdCddCtN-R_N-1COCSCdCddCtN->Ct_N-1CdCdd->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_Ext-2CdCddCtNOS-R_3CN1sOS->C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.85e+09,'m^3/(mol*s)'), n=-0.7, w0=(474000,'J/mol'), E0=(47400,'J/mol'), Tmin=(200,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2CdCddCtNOS-R_3CN1sOS->C_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2CdCddCtNOS-R_3CN1sOS->C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2CdCddCtNOS-R_3CN1sOS->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2CdCddCtNOS-R_3CN1sOS->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_Ext-2CdCddCtNOS-R_N-3CN1sOS->C_Ext-2CdCddCtNOS-R",
    kinetics = ArrheniusBM(A=(7.6e+06,'m^3/(mol*s)'), n=0, w0=(486000,'J/mol'), E0=(48600,'J/mol'), Tmin=(298,'K'), Tmax=(410,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2CdCddCtNOS-R_N-3CN1sOS->C_Ext-2CdCddCtNOS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2CdCddCtNOS-R_N-3CN1sOS->C_Ext-2CdCddCtNOS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2CdCddCtNOS-R_N-3CN1sOS->C_Ext-2CdCddCtNOS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2CdCddCtNOS-R_N-3CN1sOS->C_Ext-2CdCddCtNOS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

