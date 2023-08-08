#!/usr/bin/env python
# encoding: utf-8

name = "XY_Addition_MultipleBond/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(18.531,'m^3/(mol*s)'), n=1.32297, w0=(756348,'J/mol'), E0=(210473,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05578922274092243, var=4.422146091546833, Tref=1000.0, N=33, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 33 training reactions at node Root
    Total Standard Deviation in ln(k): 4.355911149190311"""),
    rank = 11,
    shortDesc = """BM rule fitted to 33 training reactions at node Root
Total Standard Deviation in ln(k): 4.355911149190311""",
    longDesc = 
"""
BM rule fitted to 33 training reactions at node Root
Total Standard Deviation in ln(k): 4.355911149190311
""",
)

entry(
    index = 2,
    label = "Root_1Br1sCl1sF1sH->Cl1s",
    kinetics = ArrheniusBM(A=(5.93272e-05,'m^3/(mol*s)'), n=2.63647, w0=(575000,'J/mol'), E0=(140198,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1Br1sCl1sF1sH->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_1Br1sCl1sF1sH->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s",
    kinetics = ArrheniusBM(A=(2.10315,'m^3/(mol*s)'), n=1.61376, w0=(762016,'J/mol'), E0=(211241,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0789142276630321, var=3.378165150564068, Tref=1000.0, N=32, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s',), comment="""BM rule fitted to 32 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s
    Total Standard Deviation in ln(k): 3.8829370247759964"""),
    rank = 11,
    shortDesc = """BM rule fitted to 32 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 3.8829370247759964""",
    longDesc = 
"""
BM rule fitted to 32 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 3.8829370247759964
""",
)

entry(
    index = 4,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(59029.4,'m^3/(mol*s)'), n=0.288781, w0=(866292,'J/mol'), E0=(240067,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.009670056152757593, var=11.544460769953993, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 12 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 6.835813163783375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 6.835813163783375""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 6.835813163783375
""",
)

entry(
    index = 5,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(1.74868,'m^3/(mol*s)'), n=1.63746, w0=(699450,'J/mol'), E0=(210999,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07982101879078687, var=3.3410847943152633, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 20 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 3.864937299850754"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 3.864937299850754""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 3.864937299850754
""",
)

entry(
    index = 6,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(1.77089,'m^3/(mol*s)'), n=1.62248, w0=(871625,'J/mol'), E0=(221465,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05571320516261351, var=11.313190983790786, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 6.882926863784101"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 6.882926863784101""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 6.882926863784101
""",
)

entry(
    index = 7,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(1.84221e+08,'m^3/(mol*s)'), n=-0.741075, w0=(854667,'J/mol'), E0=(275401,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07092136257417955, var=4.263901037659594, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 4.317815056244463"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 4.317815056244463""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 4.317815056244463
""",
)

entry(
    index = 8,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(3234.02,'m^3/(mol*s)'), n=0.841082, w0=(690500,'J/mol'), E0=(231106,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08953372930780412, var=8.7042697151113, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 6 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 6.13952889033091"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 6.13952889033091""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 6.13952889033091
""",
)

entry(
    index = 9,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(3.873,'m^3/(mol*s)'), n=1.45743, w0=(703286,'J/mol'), E0=(205682,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.044056942611570095, var=2.2630917047093937, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 14 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 3.1265342294230076"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 3.1265342294230076""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 3.1265342294230076
""",
)

entry(
    index = 10,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(1.56721e+32,'m^3/(mol*s)'), n=-7.40875, w0=(847000,'J/mol'), E0=(355628,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(1.35339e-05,'m^3/(mol*s)'), n=3.0724, w0=(875143,'J/mol'), E0=(200812,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08039416804036821, var=7.687635206276118, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 7 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 5.760441167260633"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 5.760441167260633""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 5.760441167260633
""",
)

entry(
    index = 12,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(1.64483e+40,'m^3/(mol*s)'), n=-10.004, w0=(847000,'J/mol'), E0=(368699,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(0.155486,'m^3/(mol*s)'), n=1.84406, w0=(858500,'J/mol'), E0=(243042,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0002592053915720451, var=0.023805321282912618, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 0.30996130688542933"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 0.30996130688542933""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 0.30996130688542933
""",
)

entry(
    index = 14,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(4402.23,'m^3/(mol*s)'), n=0.832427, w0=(699500,'J/mol'), E0=(224340,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.007734243753195459, var=0.9741359578645888, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 5 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 1.9980727377529526"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 1.9980727377529526""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 1.9980727377529526
""",
)

entry(
    index = 15,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(645500,'J/mol'), E0=(275727,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(103.798,'m^3/(mol*s)'), n=1.02893, w0=(711000,'J/mol'), E0=(207162,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0265270309925669, var=2.1852915220856866, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 12 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 3.030196880314295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 3.030196880314295""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 3.030196880314295
""",
)

entry(
    index = 17,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.0660936,'m^3/(mol*s)'), n=2.05911, w0=(657000,'J/mol'), E0=(219798,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.724983558345639, var=68.1820070515672, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 30.937958818928855"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 30.937958818928855""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 30.937958818928855
""",
)

entry(
    index = 18,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(8.66807e-14,'m^3/(mol*s)'), n=5.44878, w0=(887625,'J/mol'), E0=(174247,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.2961558164851907, var=19.42048908477356, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 12.09127656637391"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.09127656637391""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.09127656637391
""",
)

entry(
    index = 19,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3CdO2d-R",
    kinetics = ArrheniusBM(A=(0.0965843,'m^3/(mol*s)'), n=2.00355, w0=(858500,'J/mol'), E0=(228419,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0012758229263045246, var=11.664448724158145, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3CdO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3CdO2d-R
    Total Standard Deviation in ln(k): 6.8500285488231"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 6.8500285488231""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 6.8500285488231
""",
)

entry(
    index = 20,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(52.9173,'m^3/(mol*s)'), n=1.09798, w0=(858500,'J/mol'), E0=(249103,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3Cd-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3Cd-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3Cd-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3Cd-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.237624,'m^3/(mol*s)'), n=2.2618, w0=(699500,'J/mol'), E0=(218542,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.005716926918813203, var=0.8821332733001921, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 1.8972504194064923"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 1.8972504194064923""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 1.8972504194064923
""",
)

entry(
    index = 22,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3Ct-R",
    kinetics = ArrheniusBM(A=(2.10658,'m^3/(mol*s)'), n=1.73542, w0=(699500,'J/mol'), E0=(212290,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3Ct-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3Ct-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3Ct-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3Ct-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R",
    kinetics = ArrheniusBM(A=(0.861211,'m^3/(mol*s)'), n=1.62393, w0=(711000,'J/mol'), E0=(204231,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04415051193696195, var=3.3076813581525575, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R
    Total Standard Deviation in ln(k): 3.756949050610777"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 3.756949050610777""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 3.756949050610777
""",
)

entry(
    index = 24,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(2.84999e+06,'m^3/(mol*s)'), n=-0.353558, w0=(711000,'J/mol'), E0=(213624,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0011176031788138253, var=0.766425788910674, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 1.757868355229437"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 1.757868355229437""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 1.757868355229437
""",
)

entry(
    index = 25,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s_Ext-3CdO2d-R",
    kinetics = ArrheniusBM(A=(0.882649,'m^3/(mol*s)'), n=1.68333, w0=(657000,'J/mol'), E0=(219941,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s_Ext-3CdO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s_Ext-3CdO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-2Br1sCl1s->Cl1s_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_Ext-3CdO2d-R",
    kinetics = ArrheniusBM(A=(4251.74,'m^3/(mol*s)'), n=0.489676, w0=(858500,'J/mol'), E0=(217340,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.012824852924355307, var=24.354166144100823, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_Ext-3CdO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_Ext-3CdO2d-R
    Total Standard Deviation in ln(k): 9.925578901029992"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 9.925578901029992""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 9.925578901029992
""",
)

entry(
    index = 27,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3CdO2d->O2d",
    kinetics = ArrheniusBM(A=(0.109156,'m^3/(mol*s)'), n=1.86531, w0=(975000,'J/mol'), E0=(170750,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3CdO2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3CdO2d->O2d
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3CdO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3CdO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3CdO2d->O2d",
    kinetics = ArrheniusBM(A=(10.477,'m^3/(mol*s)'), n=1.29062, w0=(858500,'J/mol'), E0=(214595,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3CdO2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3CdO2d->O2d
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3CdO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3CdO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3CdO2d-R_Ext-3CdO2d-R",
    kinetics = ArrheniusBM(A=(4.14111,'m^3/(mol*s)'), n=1.29695, w0=(858500,'J/mol'), E0=(229024,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3CdO2d-R_Ext-3CdO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3CdO2d-R_Ext-3CdO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3CdO2d-R_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3CdO2d-R_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-3Ct-R",
    kinetics = ArrheniusBM(A=(40.7026,'m^3/(mol*s)'), n=1.65435, w0=(699500,'J/mol'), E0=(223829,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-3Ct-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-3Ct-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-3Ct-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-3Ct-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(863.231,'m^3/(mol*s)'), n=0.722812, w0=(711000,'J/mol'), E0=(207515,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.006812385391110879, var=3.4113384386473915, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl
    Total Standard Deviation in ln(k): 3.719823940287308"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.719823940287308""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.719823940287308
""",
)

entry(
    index = 32,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.18057,'m^3/(mol*s)'), n=1.62936, w0=(711000,'J/mol'), E0=(219824,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(1.25612e+07,'m^3/(mol*s)'), n=-0.637747, w0=(711000,'J/mol'), E0=(215085,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->C",
    kinetics = ArrheniusBM(A=(8.97967e+06,'m^3/(mol*s)'), n=-0.518739, w0=(711000,'J/mol'), E0=(212126,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.6085e+08,'m^3/(mol*s)'), n=-0.88707, w0=(711000,'J/mol'), E0=(212590,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_Ext-3CdO2d-R_Ext-3CdO2d-R",
    kinetics = ArrheniusBM(A=(26.4943,'m^3/(mol*s)'), n=1.22463, w0=(858500,'J/mol'), E0=(202816,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_Ext-3CdO2d-R_Ext-3CdO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_Ext-3CdO2d-R_Ext-3CdO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_Ext-3CdO2d-R_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_Ext-3CdO2d-R_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R",
    kinetics = ArrheniusBM(A=(631.246,'m^3/(mol*s)'), n=0.744315, w0=(711000,'J/mol'), E0=(204988,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.007791397538652573, var=13.169458742624444, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R
    Total Standard Deviation in ln(k): 7.294709630031939"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 7.294709630031939""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R
Total Standard Deviation in ln(k): 7.294709630031939
""",
)

entry(
    index = 38,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(5.59096e+06,'m^3/(mol*s)'), n=-0.339093, w0=(711000,'J/mol'), E0=(220112,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(179.755,'m^3/(mol*s)'), n=0.928737, w0=(711000,'J/mol'), E0=(199420,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0015583992925483614, var=35.83408174955999, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 12.004575517732093"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.004575517732093""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.004575517732093
""",
)

entry(
    index = 40,
    label = "Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.0823032,'m^3/(mol*s)'), n=1.92336, w0=(711000,'J/mol'), E0=(210237,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1Br1sCl1sF1sH->Cl1s_N-2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_2Br1sCl1s->Cl1s_Ext-3CdO2d-R_5R!H->Cl_Ext-3CdO2d-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

