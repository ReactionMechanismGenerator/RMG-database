#!/usr/bin/env python
# encoding: utf-8

name = "XY_Addition_MultipleBond/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(85099.9,'m^3/(mol*s)'), n=0.182872, w0=(863175,'J/mol'), E0=(236509,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03349043792019229, var=8.156057728164983, Tref=1000.0, N=20, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 20 training reactions at node Root
    Total Standard Deviation in ln(k): 5.8094321526284425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root
Total Standard Deviation in ln(k): 5.8094321526284425""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root
Total Standard Deviation in ln(k): 5.8094321526284425
""",
)

entry(
    index = 2,
    label = "Root_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(1163.99,'m^3/(mol*s)'), n=0.717561, w0=(865062,'J/mol'), E0=(227061,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.028919976683943638, var=7.455608516642755, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 16 training reactions at node Root_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 5.546584408495413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 5.546584408495413""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 5.546584408495413
""",
)

entry(
    index = 3,
    label = "Root_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(1.84221e+08,'m^3/(mol*s)'), n=-0.741075, w0=(854667,'J/mol'), E0=(275401,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07092136257417955, var=4.263901037659594, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 4.317815056244463"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 4.317815056244463""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 4.317815056244463
""",
)

entry(
    index = 4,
    label = "Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(3.9222,'m^3/(mol*s)'), n=1.33813, w0=(871444,'J/mol'), E0=(210959,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02174311010643981, var=9.212380660869105, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 9 training reactions at node Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 6.139383557223495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 6.139383557223495""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 6.139383557223495
""",
)

entry(
    index = 5,
    label = "Root_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.208149,'m^3/(mol*s)'), n=1.9696, w0=(858500,'J/mol'), E0=(229511,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.008040455320295108, var=4.400333225813735, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 4.225529156126142"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 4.225529156126142""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 4.225529156126142
""",
)

entry(
    index = 6,
    label = "Root_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(1.56721e+32,'m^3/(mol*s)'), n=-7.40875, w0=(847000,'J/mol'), E0=(355628,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(1988.33,'m^3/(mol*s)'), n=0.665323, w0=(858500,'J/mol'), E0=(226625,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05049762500170542, var=16.72016563535322, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 8.324300155340332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 8.324300155340332""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 8.324300155340332
""",
)

entry(
    index = 8,
    label = "Root_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(1.64483e+40,'m^3/(mol*s)'), n=-10.004, w0=(847000,'J/mol'), E0=(368699,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(0.155486,'m^3/(mol*s)'), n=1.84406, w0=(858500,'J/mol'), E0=(243042,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0002592053915720451, var=0.023805321282912618, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 0.30996130688542933"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 0.30996130688542933""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 0.30996130688542933
""",
)

entry(
    index = 10,
    label = "Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(150341,'m^3/(mol*s)'), n=-0.103391, w0=(858500,'J/mol'), E0=(218534,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09847967878753178, var=8.040325250556345, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 5.931956369448201"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 5.931956369448201""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 5.931956369448201
""",
)

entry(
    index = 11,
    label = "Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(477790,'m^3/(mol*s)'), n=-0.0533072, w0=(858500,'J/mol'), E0=(236791,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0946448068498816, var=10.585569615437683, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 6.760301291758461"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 6.760301291758461""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 6.760301291758461
""",
)

entry(
    index = 12,
    label = "Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(0.109156,'m^3/(mol*s)'), n=1.86531, w0=(975000,'J/mol'), E0=(170750,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(4.14111,'m^3/(mol*s)'), n=1.29695, w0=(858500,'J/mol'), E0=(229024,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(52.9173,'m^3/(mol*s)'), n=1.09798, w0=(858500,'J/mol'), E0=(249103,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3Cd-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3Cd-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3Cd-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Ct_Ext-3Cd-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.343967,'m^3/(mol*s)'), n=1.80708, w0=(858500,'J/mol'), E0=(200062,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.2256862191860976e-13, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 3.079613616045471e-13"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 3.079613616045471e-13""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 3.079613616045471e-13
""",
)

