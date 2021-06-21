#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_CO/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(0.00338196,'m^3/(mol*s)'), n=2.89385, w0=(721643,'J/mol'), E0=(344778,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0010899310181875718, var=45.04414981819316, Tref=1000.0, N=7, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 7 training reactions at node Root
    Total Standard Deviation in ln(k): 13.457505680819366"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 13.457505680819366""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 13.457505680819366
""",
)

entry(
    index = 2,
    label = "Root_2CbCdCsCtHNSSidSis->H",
    kinetics = ArrheniusBM(A=(0.00974488,'m^3/(mol*s)'), n=2.72727, w0=(732667,'J/mol'), E0=(327945,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.003971248169829193, var=12.181379362220616, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_2CbCdCsCtHNSSidSis->H',), comment="""BM rule fitted to 6 training reactions at node Root_2CbCdCsCtHNSSidSis->H
    Total Standard Deviation in ln(k): 7.006870868257926"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_2CbCdCsCtHNSSidSis->H
Total Standard Deviation in ln(k): 7.006870868257926""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_2CbCdCsCtHNSSidSis->H
Total Standard Deviation in ln(k): 7.006870868257926
""",
)

entry(
    index = 3,
    label = "Root_N-2CbCdCsCtHNSSidSis->H",
    kinetics = ArrheniusBM(A=(0.000538,'m^3/(mol*s)'), n=3.29, w0=(655500,'J/mol'), E0=(448511,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2CbCdCsCtHNSSidSis->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-2CbCdCsCtHNSSidSis->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2CbCdCsCtHNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2CbCdCsCtHNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_2CbCdCsCtHNSSidSis->H_1COCbCdCsCtHNOSSidSis->O",
    kinetics = ArrheniusBM(A=(1.27e-07,'m^3/(mol*s)'), n=3.7, w0=(750500,'J/mol'), E0=(243667,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2CbCdCsCtHNSSidSis->H_1COCbCdCsCtHNOSSidSis->O',), comment="""BM rule fitted to 1 training reactions at node Root_2CbCdCsCtHNSSidSis->H_1COCbCdCsCtHNOSSidSis->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2CbCdCsCtHNSSidSis->H_1COCbCdCsCtHNOSSidSis->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2CbCdCsCtHNSSidSis->H_1COCbCdCsCtHNOSSidSis->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O",
    kinetics = ArrheniusBM(A=(0.0511279,'m^3/(mol*s)'), n=2.59114, w0=(729100,'J/mol'), E0=(343282,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0047535486342501505, var=1.828222860697797, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O',), comment="""BM rule fitted to 5 training reactions at node Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O
    Total Standard Deviation in ln(k): 2.722581805942031"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O
Total Standard Deviation in ln(k): 2.722581805942031""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O
Total Standard Deviation in ln(k): 2.722581805942031
""",
)

entry(
    index = 6,
    label = "Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_1CsH->H",
    kinetics = ArrheniusBM(A=(2890,'m^3/(mol*s)'), n=1.16, w0=(763500,'J/mol'), E0=(346610,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_1CsH->H',), comment="""BM rule fitted to 1 training reactions at node Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_1CsH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_1CsH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_1CsH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H",
    kinetics = ArrheniusBM(A=(0.0284052,'m^3/(mol*s)'), n=2.68137, w0=(720500,'J/mol'), E0=(344937,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.005392439484706767, var=2.4583476230267682, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H',), comment="""BM rule fitted to 4 training reactions at node Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H
    Total Standard Deviation in ln(k): 3.156796761185881"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H
Total Standard Deviation in ln(k): 3.156796761185881""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H
Total Standard Deviation in ln(k): 3.156796761185881
""",
)

entry(
    index = 8,
    label = "Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(0.124012,'m^3/(mol*s)'), n=2.4405, w0=(720500,'J/mol'), E0=(342503,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0042638796522202925, var=4.527745803924326, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R',), comment="""BM rule fitted to 3 training reactions at node Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R
    Total Standard Deviation in ln(k): 4.27648888535461"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R
Total Standard Deviation in ln(k): 4.27648888535461""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R
Total Standard Deviation in ln(k): 4.27648888535461
""",
)

entry(
    index = 9,
    label = "Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(0.446802,'m^3/(mol*s)'), n=2.23388, w0=(720500,'J/mol'), E0=(336879,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.604129457181339e-05, var=9.334470434039142, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R',), comment="""BM rule fitted to 2 training reactions at node Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R
    Total Standard Deviation in ln(k): 6.12498020517388"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 6.12498020517388""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 6.12498020517388
""",
)

entry(
    index = 10,
    label = "Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(88.9,'m^3/(mol*s)'), n=1.51, w0=(720500,'J/mol'), E0=(330294,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R_Ext-1Cs-R',), comment="""BM rule fitted to 1 training reactions at node Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R_Ext-1Cs-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2CbCdCsCtHNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

