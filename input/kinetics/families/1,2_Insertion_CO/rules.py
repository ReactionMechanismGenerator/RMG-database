#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_CO/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(3.36648e+06,'m^3/(mol*s)'), n=-0.068205, w0=(721375,'J/mol'), E0=(367741,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0550565369343876, var=44.69777385428915, Tref=1000.0, N=8, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 8 training reactions at node Root
    Total Standard Deviation in ln(k): 16.05383159157377"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root
Total Standard Deviation in ln(k): 16.05383159157377""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root
Total Standard Deviation in ln(k): 16.05383159157377
""",
)

entry(
    index = 2,
    label = "Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(0.00653669,'m^3/(mol*s)'), n=2.78488, w0=(732667,'J/mol'), E0=(328314,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0022347142164816833, var=12.328055475861774, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 6 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 7.044506498262594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 7.044506498262594""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 7.044506498262594
""",
)

entry(
    index = 3,
    label = "Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(5.31422e+13,'m^3/(mol*s)'), n=-2.42603, w0=(687500,'J/mol'), E0=(400343,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.554882583412352, var=79.10863666163978, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 29.275151032402746"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 29.275151032402746""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 29.275151032402746
""",
)

entry(
    index = 4,
    label = "Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtHNOSSidSis->O",
    kinetics = ArrheniusBM(A=(1.27e-07,'m^3/(mol*s)'), n=3.7, w0=(750500,'J/mol'), E0=(243508,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtHNOSSidSis->O',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtHNOSSidSis->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtHNOSSidSis->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtHNOSSidSis->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O",
    kinetics = ArrheniusBM(A=(0.0378156,'m^3/(mol*s)'), n=2.63641, w0=(729100,'J/mol'), E0=(343863,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.006871936773490197, var=1.6911607459889995, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O',), comment="""BM rule fitted to 5 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O
    Total Standard Deviation in ln(k): 2.6243166152465465"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O
Total Standard Deviation in ln(k): 2.6243166152465465""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O
Total Standard Deviation in ln(k): 2.6243166152465465
""",
)

entry(
    index = 6,
    label = "Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtHNOSSidSis->H",
    kinetics = ArrheniusBM(A=(9.26653e+18,'m^3/(mol*s)'), n=-4.11331, w0=(719500,'J/mol'), E0=(396512,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtHNOSSidSis->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtHNOSSidSis->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->H",
    kinetics = ArrheniusBM(A=(0.000538,'m^3/(mol*s)'), n=3.29, w0=(655500,'J/mol'), E0=(448319,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_1CsH->H",
    kinetics = ArrheniusBM(A=(2890,'m^3/(mol*s)'), n=1.16, w0=(763500,'J/mol'), E0=(347090,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_1CsH->H',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_1CsH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_1CsH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_1CsH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H",
    kinetics = ArrheniusBM(A=(0.0194443,'m^3/(mol*s)'), n=2.73894, w0=(720500,'J/mol'), E0=(345583,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.008086649702507345, var=2.2503321319087783, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H',), comment="""BM rule fitted to 4 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H
    Total Standard Deviation in ln(k): 3.027642768730113"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H
Total Standard Deviation in ln(k): 3.027642768730113""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H
Total Standard Deviation in ln(k): 3.027642768730113
""",
)

entry(
    index = 10,
    label = "Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(0.0913089,'m^3/(mol*s)'), n=2.49316, w0=(720500,'J/mol'), E0=(343524,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.007831592214764085, var=4.145490645172328, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R
    Total Standard Deviation in ln(k): 4.101413811918778"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R
Total Standard Deviation in ln(k): 4.101413811918778""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R
Total Standard Deviation in ln(k): 4.101413811918778
""",
)

entry(
    index = 11,
    label = "Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(0.369866,'m^3/(mol*s)'), n=2.27093, w0=(720500,'J/mol'), E0=(338349,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0306105576327384e-05, var=9.046558139596009, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R
    Total Standard Deviation in ln(k): 6.029767182939766"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 6.029767182939766""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 6.029767182939766
""",
)

entry(
    index = 12,
    label = "Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(88.9,'m^3/(mol*s)'), n=1.51, w0=(720500,'J/mol'), E0=(331301,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R_Ext-1Cs-R',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R_Ext-1Cs-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

