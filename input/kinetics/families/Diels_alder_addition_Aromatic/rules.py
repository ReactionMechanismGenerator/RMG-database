#!/usr/bin/env python
# encoding: utf-8

name = "Diels_alder_addition_Aromatic/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(4.11393e+21,'m^3/(mol*s)'), n=-4.96127, w0=(542929,'J/mol'), E0=(196526,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.4651452533243257, var=30.086343983587437, Tref=1000.0, N=7, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 7 training reactions at node Root
    Total Standard Deviation in ln(k): 12.164883055192815"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 12.164883055192815""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 12.164883055192815
""",
)

entry(
    index = 2,
    label = "Root_Ext-1CbCbf-R",
    kinetics = ArrheniusBM(A=(5.11966e+06,'m^3/(mol*s)'), n=-1.00646, w0=(553500,'J/mol'), E0=(152881,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1301603542391048, var=34.258277475947885, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-1CbCbf-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-1CbCbf-R
    Total Standard Deviation in ln(k): 14.57342776864884"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-1CbCbf-R
Total Standard Deviation in ln(k): 14.57342776864884""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-1CbCbf-R
Total Standard Deviation in ln(k): 14.57342776864884
""",
)

entry(
    index = 3,
    label = "Root_5Ct-inRing",
    kinetics = ArrheniusBM(A=(0.000968167,'m^3/(mol*s)'), n=2.526, w0=(535000,'J/mol'), E0=(53500,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Ct-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_5Ct-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Ct-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Ct-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_N-5Ct-inRing",
    kinetics = ArrheniusBM(A=(1.18348e+06,'m^3/(mol*s)'), n=-0.13487, w0=(535000,'J/mol'), E0=(175229,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9442310184100462, var=74.4878913684149, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5Ct-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_N-5Ct-inRing
    Total Standard Deviation in ln(k): 19.674580054137156"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5Ct-inRing
Total Standard Deviation in ln(k): 19.674580054137156""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5Ct-inRing
Total Standard Deviation in ln(k): 19.674580054137156
""",
)

entry(
    index = 5,
    label = "Root_Ext-1CbCbf-R_1CbCbf->Cb",
    kinetics = ArrheniusBM(A=(8.46e-06,'m^3/(mol*s)'), n=2.6, w0=(590500,'J/mol'), E0=(190992,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1CbCbf-R_1CbCbf->Cb',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1CbCbf-R_1CbCbf->Cb
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1CbCbf-R_1CbCbf->Cb
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1CbCbf-R_1CbCbf->Cb
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_Ext-1CbCbf-R_N-1CbCbf->Cb",
    kinetics = ArrheniusBM(A=(5.89304,'m^3/(mol*s)'), n=0.718971, w0=(535000,'J/mol'), E0=(127560,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3469736613209595, var=0.6454898770400953, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1CbCbf-R_N-1CbCbf->Cb',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbf-R_N-1CbCbf->Cb
    Total Standard Deviation in ln(k): 2.482445085884605"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1CbCbf-R_N-1CbCbf->Cb
Total Standard Deviation in ln(k): 2.482445085884605""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1CbCbf-R_N-1CbCbf->Cb
Total Standard Deviation in ln(k): 2.482445085884605
""",
)

entry(
    index = 7,
    label = "Root_N-5Ct-inRing_Ext-4CbCbf-R_Ext-7R!H-R_Ext-7R!H-R_Ext-4CbCbf-R",
    kinetics = ArrheniusBM(A=(313.369,'m^3/(mol*s)'), n=1.07014, w0=(535000,'J/mol'), E0=(166607,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.243605515613325, var=342.40568138978, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5Ct-inRing_Ext-4CbCbf-R_Ext-7R!H-R_Ext-7R!H-R_Ext-4CbCbf-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-5Ct-inRing_Ext-4CbCbf-R_Ext-7R!H-R_Ext-7R!H-R_Ext-4CbCbf-R
    Total Standard Deviation in ln(k): 47.75835852248233"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5Ct-inRing_Ext-4CbCbf-R_Ext-7R!H-R_Ext-7R!H-R_Ext-4CbCbf-R
Total Standard Deviation in ln(k): 47.75835852248233""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5Ct-inRing_Ext-4CbCbf-R_Ext-7R!H-R_Ext-7R!H-R_Ext-4CbCbf-R
Total Standard Deviation in ln(k): 47.75835852248233
""",
)

entry(
    index = 8,
    label = "Root_Ext-1CbCbf-R_N-1CbCbf->Cb_2CbCbf->Cb",
    kinetics = ArrheniusBM(A=(1.66411e-05,'m^3/(mol*s)'), n=2.69336, w0=(535000,'J/mol'), E0=(136712,'J/mol'), Tmin=(303.03,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1CbCbf-R_N-1CbCbf->Cb_2CbCbf->Cb',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1CbCbf-R_N-1CbCbf->Cb_2CbCbf->Cb
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1CbCbf-R_N-1CbCbf->Cb_2CbCbf->Cb
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1CbCbf-R_N-1CbCbf->Cb_2CbCbf->Cb
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_Ext-1CbCbf-R_N-1CbCbf->Cb_N-2CbCbf->Cb",
    kinetics = ArrheniusBM(A=(2.162e-05,'m^3/(mol*s)'), n=2.58, w0=(535000,'J/mol'), E0=(127430,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1CbCbf-R_N-1CbCbf->Cb_N-2CbCbf->Cb',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1CbCbf-R_N-1CbCbf->Cb_N-2CbCbf->Cb
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1CbCbf-R_N-1CbCbf->Cb_N-2CbCbf->Cb
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1CbCbf-R_N-1CbCbf->Cb_N-2CbCbf->Cb
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

