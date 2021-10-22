#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(370.245,'m^3/(mol*s)'), n=1.32706, w0=(570117,'J/mol'), E0=(21344.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.019559614069635026, var=2.4778043575436723, Tref=1000.0, N=261, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 261 training reactions at node Root
    Total Standard Deviation in ln(k): 3.2048068711925954"""),
    rank = 11,
    shortDesc = """BM rule fitted to 261 training reactions at node Root
Total Standard Deviation in ln(k): 3.2048068711925954""",
    longDesc = 
"""
BM rule fitted to 261 training reactions at node Root
Total Standard Deviation in ln(k): 3.2048068711925954
""",
)

entry(
    index = 2,
    label = "Root_Ext-4R-R",
    kinetics = ArrheniusBM(A=(95.9209,'m^3/(mol*s)'), n=1.48062, w0=(569306,'J/mol'), E0=(18239.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.022809563914139745, var=4.315413824237631, Tref=1000.0, N=116, data_mean=0.0, correlation='Root_Ext-4R-R',), comment="""BM rule fitted to 116 training reactions at node Root_Ext-4R-R
    Total Standard Deviation in ln(k): 4.221861737616908"""),
    rank = 11,
    shortDesc = """BM rule fitted to 116 training reactions at node Root_Ext-4R-R
Total Standard Deviation in ln(k): 4.221861737616908""",
    longDesc = 
"""
BM rule fitted to 116 training reactions at node Root_Ext-4R-R
Total Standard Deviation in ln(k): 4.221861737616908
""",
)

entry(
    index = 3,
    label = "Root_4R->C",
    kinetics = ArrheniusBM(A=(34.7345,'m^3/(mol*s)'), n=1.44841, w0=(549943,'J/mol'), E0=(73339.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1255484547038976, var=1.1713173110575479, Tref=1000.0, N=35, data_mean=0.0, correlation='Root_4R->C',), comment="""BM rule fitted to 35 training reactions at node Root_4R->C
    Total Standard Deviation in ln(k): 2.4851213076379586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 35 training reactions at node Root_4R->C
Total Standard Deviation in ln(k): 2.4851213076379586""",
    longDesc = 
"""
BM rule fitted to 35 training reactions at node Root_4R->C
Total Standard Deviation in ln(k): 2.4851213076379586
""",
)

entry(
    index = 4,
    label = "Root_N-4R->C",
    kinetics = ArrheniusBM(A=(3410.13,'m^3/(mol*s)'), n=1.08901, w0=(577391,'J/mol'), E0=(54267.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03012306179829734, var=1.1874192371035193, Tref=1000.0, N=110, data_mean=0.0, correlation='Root_N-4R->C',), comment="""BM rule fitted to 110 training reactions at node Root_N-4R->C
    Total Standard Deviation in ln(k): 2.260221197807916"""),
    rank = 11,
    shortDesc = """BM rule fitted to 110 training reactions at node Root_N-4R->C
Total Standard Deviation in ln(k): 2.260221197807916""",
    longDesc = 
"""
BM rule fitted to 110 training reactions at node Root_N-4R->C
Total Standard Deviation in ln(k): 2.260221197807916
""",
)

entry(
    index = 5,
    label = "Root_Ext-4R-R_5R!H-u0",
    kinetics = ArrheniusBM(A=(68.6936,'m^3/(mol*s)'), n=1.59832, w0=(568731,'J/mol'), E0=(18558.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.012565876712239915, var=2.459985972256491, Tref=1000.0, N=80, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0',), comment="""BM rule fitted to 80 training reactions at node Root_Ext-4R-R_5R!H-u0
    Total Standard Deviation in ln(k): 3.1758676965742976"""),
    rank = 11,
    shortDesc = """BM rule fitted to 80 training reactions at node Root_Ext-4R-R_5R!H-u0
Total Standard Deviation in ln(k): 3.1758676965742976""",
    longDesc = 
"""
BM rule fitted to 80 training reactions at node Root_Ext-4R-R_5R!H-u0
Total Standard Deviation in ln(k): 3.1758676965742976
""",
)

entry(
    index = 6,
    label = "Root_Ext-4R-R_N-5R!H-u0",
    kinetics = ArrheniusBM(A=(49981.3,'m^3/(mol*s)'), n=0.110697, w0=(570583,'J/mol'), E0=(36563.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11357256409276026, var=0.6863280147957995, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0',), comment="""BM rule fitted to 36 training reactions at node Root_Ext-4R-R_N-5R!H-u0
    Total Standard Deviation in ln(k): 1.9461792970777438"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_Ext-4R-R_N-5R!H-u0
Total Standard Deviation in ln(k): 1.9461792970777438""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_Ext-4R-R_N-5R!H-u0
Total Standard Deviation in ln(k): 1.9461792970777438
""",
)

entry(
    index = 7,
    label = "Root_4R->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.26873e+06,'m^3/(mol*s)'), n=-0.160329, w0=(537647,'J/mol'), E0=(64428.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.004321983584869017, var=1.0761978570055097, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R',), comment="""BM rule fitted to 17 training reactions at node Root_4R->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 2.0905705520260223"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.0905705520260223""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.0905705520260223
""",
)

entry(
    index = 8,
    label = "Root_4R->C_2R!H->C",
    kinetics = ArrheniusBM(A=(85.2535,'m^3/(mol*s)'), n=1.32101, w0=(560045,'J/mol'), E0=(56004.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07657308793870102, var=0.813757256763806, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_4R->C_2R!H->C',), comment="""BM rule fitted to 11 training reactions at node Root_4R->C_2R!H->C
    Total Standard Deviation in ln(k): 2.000836035086864"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_4R->C_2R!H->C
Total Standard Deviation in ln(k): 2.000836035086864""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_4R->C_2R!H->C
Total Standard Deviation in ln(k): 2.000836035086864
""",
)

entry(
    index = 9,
    label = "Root_4R->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(21.8707,'m^3/(mol*s)'), n=1.51282, w0=(563929,'J/mol'), E0=(73568.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07887124859575377, var=1.6671387782300844, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_4R->C_N-2R!H->C
    Total Standard Deviation in ln(k): 2.7866373583117956"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_4R->C_N-2R!H->C
Total Standard Deviation in ln(k): 2.7866373583117956""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_4R->C_N-2R!H->C
Total Standard Deviation in ln(k): 2.7866373583117956
""",
)

entry(
    index = 10,
    label = "Root_N-4R->C_4BrClFHNOS->N",
    kinetics = ArrheniusBM(A=(357.109,'m^3/(mol*s)'), n=1.20693, w0=(569125,'J/mol'), E0=(45095.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06985474913508474, var=0.3429093852723291, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->C_4BrClFHNOS->N
    Total Standard Deviation in ln(k): 1.349456538762701"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->C_4BrClFHNOS->N
Total Standard Deviation in ln(k): 1.349456538762701""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->C_4BrClFHNOS->N
Total Standard Deviation in ln(k): 1.349456538762701
""",
)

entry(
    index = 11,
    label = "Root_N-4R->C_N-4BrClFHNOS->N",
    kinetics = ArrheniusBM(A=(2847.94,'m^3/(mol*s)'), n=1.16198, w0=(578039,'J/mol'), E0=(50332,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.029558914083028562, var=0.7265814328727495, Tref=1000.0, N=102, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N',), comment="""BM rule fitted to 102 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N
    Total Standard Deviation in ln(k): 1.7830997198893535"""),
    rank = 11,
    shortDesc = """BM rule fitted to 102 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N
Total Standard Deviation in ln(k): 1.7830997198893535""",
    longDesc = 
"""
BM rule fitted to 102 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N
Total Standard Deviation in ln(k): 1.7830997198893535
""",
)

entry(
    index = 12,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(13592.6,'m^3/(mol*s)'), n=0.46078, w0=(542539,'J/mol'), E0=(-24586.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.0467898132026217, var=32.63152343535786, Tref=1000.0, N=38, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R',), comment="""BM rule fitted to 38 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R
    Total Standard Deviation in ln(k): 16.59453832673361"""),
    rank = 11,
    shortDesc = """BM rule fitted to 38 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R
Total Standard Deviation in ln(k): 16.59453832673361""",
    longDesc = 
"""
BM rule fitted to 38 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R
Total Standard Deviation in ln(k): 16.59453832673361
""",
)

entry(
    index = 13,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(503915,'m^3/(mol*s)'), n=-0.0523312, w0=(547450,'J/mol'), E0=(60498.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.4637475703145038, var=5.115384119406486, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R
    Total Standard Deviation in ln(k): 8.211910129998985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R
Total Standard Deviation in ln(k): 8.211910129998985""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R
Total Standard Deviation in ln(k): 8.211910129998985
""",
)

entry(
    index = 14,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O",
    kinetics = ArrheniusBM(A=(48.7921,'m^3/(mol*s)'), n=1.70943, w0=(626450,'J/mol'), E0=(2011.64,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.18045080614693276, var=0.6853152405031697, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O
    Total Standard Deviation in ln(k): 2.112989240242881"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O
Total Standard Deviation in ln(k): 2.112989240242881""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O
Total Standard Deviation in ln(k): 2.112989240242881
""",
)

entry(
    index = 15,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O",
    kinetics = ArrheniusBM(A=(201.819,'m^3/(mol*s)'), n=1.41034, w0=(597409,'J/mol'), E0=(25682.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5904296028523917, var=5.647381090815491, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O',), comment="""BM rule fitted to 22 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O
    Total Standard Deviation in ln(k): 6.247587824636625"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O
Total Standard Deviation in ln(k): 6.247587824636625""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O
Total Standard Deviation in ln(k): 6.247587824636625
""",
)

entry(
    index = 16,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(467.676,'m^3/(mol*s)'), n=0.786937, w0=(569967,'J/mol'), E0=(35560.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.428336857667598, var=5.101337871303698, Tref=1000.0, N=30, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H',), comment="""BM rule fitted to 30 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 5.604146270045783"""),
    rank = 11,
    shortDesc = """BM rule fitted to 30 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 5.604146270045783""",
    longDesc = 
"""
BM rule fitted to 30 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 5.604146270045783
""",
)

entry(
    index = 17,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(1.4551e+06,'m^3/(mol*s)'), n=-0.363631, w0=(573667,'J/mol'), E0=(61410.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.3615770948400128, var=7.3620671502103, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 11.373084432538212"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.373084432538212""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.373084432538212
""",
)

entry(
    index = 18,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1",
    kinetics = ArrheniusBM(A=(296324,'m^3/(mol*s)'), n=0.0182049, w0=(537562,'J/mol'), E0=(54946.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0458016683748811, var=0.7234271385475622, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1',), comment="""BM rule fitted to 16 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1
    Total Standard Deviation in ln(k): 1.820197367667697"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1
Total Standard Deviation in ln(k): 1.820197367667697""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1
Total Standard Deviation in ln(k): 1.820197367667697
""",
)

entry(
    index = 19,
    label = "Root_4R->C_Ext-1R!H-R_N-4C-u1",
    kinetics = ArrheniusBM(A=(1.81e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_N-4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_N-4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_4R->C_2R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.09946e+07,'m^3/(mol*s)'), n=-0.4, w0=(536700,'J/mol'), E0=(53670,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.63780826931908e-09, var=3.947898525506449, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_4R->C_2R!H->C_Ext-2C-R',), comment="""BM rule fitted to 5 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 3.9832721612712287"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 3.9832721612712287""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 3.9832721612712287
""",
)

entry(
    index = 21,
    label = "Root_4R->C_2R!H->C_1R!H->N",
    kinetics = ArrheniusBM(A=(69.6524,'m^3/(mol*s)'), n=1.34293, w0=(544000,'J/mol'), E0=(54400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.43780050013999694, var=0.5999111817527254, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_2R!H->C_1R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_1R!H->N
    Total Standard Deviation in ln(k): 2.6527474307051118"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_1R!H->N
Total Standard Deviation in ln(k): 2.6527474307051118""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_1R!H->N
Total Standard Deviation in ln(k): 2.6527474307051118
""",
)

entry(
    index = 22,
    label = "Root_4R->C_2R!H->C_N-1R!H->N",
    kinetics = ArrheniusBM(A=(6.75618e+07,'m^3/(mol*s)'), n=-0.0357896, w0=(597250,'J/mol'), E0=(59725,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.1140300863391768, var=16.478303598214193, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->C_2R!H->C_N-1R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N
    Total Standard Deviation in ln(k): 13.449550070935375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N
Total Standard Deviation in ln(k): 13.449550070935375""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N
Total Standard Deviation in ln(k): 13.449550070935375
""",
)

entry(
    index = 23,
    label = "Root_4R->C_N-2R!H->C_1R!H->C",
    kinetics = ArrheniusBM(A=(275.658,'m^3/(mol*s)'), n=1.19754, w0=(553333,'J/mol'), E0=(46776.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0533865179986996, var=0.877493300103005, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_1R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C
    Total Standard Deviation in ln(k): 2.0120647925151474"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C
Total Standard Deviation in ln(k): 2.0120647925151474""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C
Total Standard Deviation in ln(k): 2.0120647925151474
""",
)

entry(
    index = 24,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C",
    kinetics = ArrheniusBM(A=(0.585606,'m^3/(mol*s)'), n=1.96941, w0=(571875,'J/mol'), E0=(75129.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.30125767549871496, var=0.9430095321770201, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C
    Total Standard Deviation in ln(k): 2.7037005617892276"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C
Total Standard Deviation in ln(k): 2.7037005617892276""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C
Total Standard Deviation in ln(k): 2.7037005617892276
""",
)

entry(
    index = 25,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1",
    kinetics = ArrheniusBM(A=(324.71,'m^3/(mol*s)'), n=1.21139, w0=(577357,'J/mol'), E0=(43789,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06587093377643148, var=0.37537174784171157, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1
    Total Standard Deviation in ln(k): 1.393757709198133"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1
Total Standard Deviation in ln(k): 1.393757709198133""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1
Total Standard Deviation in ln(k): 1.393757709198133
""",
)

entry(
    index = 26,
    label = "Root_N-4R->C_4BrClFHNOS->N_N-2R!H-u1",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(511500,'J/mol'), E0=(51150,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_N-2R!H-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_N-2R!H-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_N-2R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_N-2R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O",
    kinetics = ArrheniusBM(A=(600.41,'m^3/(mol*s)'), n=1.40041, w0=(674250,'J/mol'), E0=(44924.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.4171511586800798, var=2.733540708643918, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O
    Total Standard Deviation in ln(k): 4.362631761172257"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O
Total Standard Deviation in ln(k): 4.362631761172257""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O
Total Standard Deviation in ln(k): 4.362631761172257
""",
)

entry(
    index = 28,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O",
    kinetics = ArrheniusBM(A=(4075.06,'m^3/(mol*s)'), n=1.10894, w0=(569851,'J/mol'), E0=(50332,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03186402994390338, var=0.7576909658126888, Tref=1000.0, N=94, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O',), comment="""BM rule fitted to 94 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O
    Total Standard Deviation in ln(k): 1.8250909646885294"""),
    rank = 11,
    shortDesc = """BM rule fitted to 94 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O
Total Standard Deviation in ln(k): 1.8250909646885294""",
    longDesc = 
"""
BM rule fitted to 94 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O
Total Standard Deviation in ln(k): 1.8250909646885294
""",
)

entry(
    index = 29,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S",
    kinetics = ArrheniusBM(A=(1.27667e-13,'m^3/(mol*s)'), n=4.8323, w0=(527000,'J/mol'), E0=(-25280,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=10.214760863631724, var=288.9982061655396, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S
    Total Standard Deviation in ln(k): 59.74561884662232"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S
Total Standard Deviation in ln(k): 59.74561884662232""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S
Total Standard Deviation in ln(k): 59.74561884662232
""",
)

entry(
    index = 30,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S",
    kinetics = ArrheniusBM(A=(204166,'m^3/(mol*s)'), n=0.158682, w0=(543403,'J/mol'), E0=(20977,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.4132493370151056, var=14.291227207898661, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S',), comment="""BM rule fitted to 36 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S
    Total Standard Deviation in ln(k): 13.64208881010293"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S
Total Standard Deviation in ln(k): 13.64208881010293""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S
Total Standard Deviation in ln(k): 13.64208881010293
""",
)

entry(
    index = 31,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F",
    kinetics = ArrheniusBM(A=(1.41421e+07,'m^3/(mol*s)'), n=7.62613e-07, w0=(533250,'J/mol'), E0=(53325,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 32,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(396797,'m^3/(mol*s)'), n=-0.0236713, w0=(551000,'J/mol'), E0=(60375,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6221184528913813, var=1.1619417856927563, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F
    Total Standard Deviation in ln(k): 3.7240838635128433"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F
Total Standard Deviation in ln(k): 3.7240838635128433""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F
Total Standard Deviation in ln(k): 3.7240838635128433
""",
)

entry(
    index = 33,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(61.3684,'m^3/(mol*s)'), n=1.70616, w0=(626125,'J/mol'), E0=(5641.45,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4986463711130324, var=0.7331814452275135, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 2.9694550883868724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.9694550883868724""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.9694550883868724
""",
)

entry(
    index = 34,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(27.368,'m^3/(mol*s)'), n=1.71766, w0=(627750,'J/mol'), E0=(62775,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8800750993930413, var=0.011227437616225197, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 2.4236649026480563"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.4236649026480563""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.4236649026480563
""",
)

entry(
    index = 35,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_5R!H->N",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(598500,'J/mol'), E0=(24800.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N",
    kinetics = ArrheniusBM(A=(87.6105,'m^3/(mol*s)'), n=1.55846, w0=(597357,'J/mol'), E0=(9204.32,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.036869000357203016, var=0.9285423436071051, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N',), comment="""BM rule fitted to 21 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N
    Total Standard Deviation in ln(k): 2.0244164827658953"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N
Total Standard Deviation in ln(k): 2.0244164827658953""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N
Total Standard Deviation in ln(k): 2.0244164827658953
""",
)

entry(
    index = 37,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C",
    kinetics = ArrheniusBM(A=(469.777,'m^3/(mol*s)'), n=0.785371, w0=(566190,'J/mol'), E0=(35644.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2449691477872364, var=9.374033316766472, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C',), comment="""BM rule fitted to 29 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C
    Total Standard Deviation in ln(k): 6.753406409614387"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 6.753406409614387""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 6.753406409614387
""",
)

entry(
    index = 38,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_N-1R!H->C",
    kinetics = ArrheniusBM(A=(5.7209e+06,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(20095,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_N-1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_N-1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(521886,'m^3/(mol*s)'), n=0.152476, w0=(551500,'J/mol'), E0=(87360.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.017620664343511283, var=5.156740901418075, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 4.596717368737125"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.596717368737125""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.596717368737125
""",
)

entry(
    index = 40,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_1R!H->N",
    kinetics = ArrheniusBM(A=(1.2e+06,'m^3/(mol*s)'), n=-0.34, w0=(684500,'J/mol'), E0=(61113.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_1R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_1R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_1R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_1R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_N-1R!H->N",
    kinetics = ArrheniusBM(A=(2.6e+09,'m^3/(mol*s)'), n=-1.26, w0=(551500,'J/mol'), E0=(36198.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_N-1R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_N-1R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_N-1R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_N-1R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(2.0166e+08,'m^3/(mol*s)'), n=-0.867187, w0=(539000,'J/mol'), E0=(79397.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06744195303402169, var=0.367442855960181, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H',), comment="""BM rule fitted to 14 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.3846637066538496"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.3846637066538496""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.3846637066538496
""",
)

entry(
    index = 43,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(6.45081e+09,'m^3/(mol*s)'), n=-0.959888, w0=(527500,'J/mol'), E0=(88314.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5972510515383959, var=3.7185377329766554, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 5.366463753921281"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 5.366463753921281""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 5.366463753921281
""",
)

entry(
    index = 44,
    label = "Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H",
    kinetics = ArrheniusBM(A=(1.12583e+07,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.1479326330925166e-11, var=0.7152290134567968, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H',), comment="""BM rule fitted to 4 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H
    Total Standard Deviation in ln(k): 1.6954287803482613"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H
Total Standard Deviation in ln(k): 1.6954287803482613""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H
Total Standard Deviation in ln(k): 1.6954287803482613
""",
)

entry(
    index = 45,
    label = "Root_4R->C_2R!H->C_Ext-2C-R_N-Sp-2C-1R!H",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(52750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_2R!H->C_Ext-2C-R_N-Sp-2C-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_N-Sp-2C-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_N-Sp-2C-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_N-Sp-2C-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_4R->C_2R!H->C_1R!H->N_Sp-2C-1N",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(553500,'J/mol'), E0=(55350,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_2R!H->C_1R!H->N_Sp-2C-1N',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_1R!H->N_Sp-2C-1N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_1R!H->N_Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_1R!H->N_Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_4R->C_2R!H->C_1R!H->N_N-Sp-2C-1N",
    kinetics = ArrheniusBM(A=(0.82,'m^3/(mol*s)'), n=1.87, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_2R!H->C_1R!H->N_N-Sp-2C-1N',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_1R!H->N_N-Sp-2C-1N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_1R!H->N_N-Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_1R!H->N_N-Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_4R->C_2R!H->C_N-1R!H->N_1CO->C",
    kinetics = ArrheniusBM(A=(8.11905e+07,'m^3/(mol*s)'), n=-0.34, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=14.717775896447819, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_2R!H->C_N-1R!H->N_1CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C
    Total Standard Deviation in ln(k): 7.690916252578899"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C
Total Standard Deviation in ln(k): 7.690916252578899""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C
Total Standard Deviation in ln(k): 7.690916252578899
""",
)

entry(
    index = 49,
    label = "Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C",
    kinetics = ArrheniusBM(A=(6.61174e+07,'m^3/(mol*s)'), n=-1.09962e-06, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.7507532944488107, var=36.13951493076956, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C
    Total Standard Deviation in ln(k): 21.475698718431726"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C
Total Standard Deviation in ln(k): 21.475698718431726""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C
Total Standard Deviation in ln(k): 21.475698718431726
""",
)

entry(
    index = 50,
    label = "Root_4R->C_N-2R!H->C_1R!H->C_Sp-2NO-1C",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=1.87, w0=(566000,'J/mol'), E0=(56600,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_1R!H->C_Sp-2NO-1C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_Sp-2NO-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_Sp-2NO-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_Sp-2NO-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C",
    kinetics = ArrheniusBM(A=(214.981,'m^3/(mol*s)'), n=1.19754, w0=(547000,'J/mol'), E0=(29023.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6109312103175142, var=1.0748208389560299, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C
    Total Standard Deviation in ln(k): 3.6133833944870597"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C
Total Standard Deviation in ln(k): 3.6133833944870597""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C
Total Standard Deviation in ln(k): 3.6133833944870597
""",
)

entry(
    index = 52,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1",
    kinetics = ArrheniusBM(A=(3.47778e-05,'m^3/(mol*s)'), n=3.22368, w0=(587833,'J/mol'), E0=(53628.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.14359311621870818, var=0.4879531879011808, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1',), comment="""BM rule fitted to 3 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1
    Total Standard Deviation in ln(k): 1.7611672711691464"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1
Total Standard Deviation in ln(k): 1.7611672711691464""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1
Total Standard Deviation in ln(k): 1.7611672711691464
""",
)

entry(
    index = 53,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C_N-2NO-u1",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(524000,'J/mol'), E0=(52400,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C_N-2NO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_N-2NO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(246.827,'m^3/(mol*s)'), n=1.2433, w0=(581125,'J/mol'), E0=(29015.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09502092991108324, var=0.9409657996420207, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 2.183407074220283"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.183407074220283""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.183407074220283
""",
)

entry(
    index = 56,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(209.849,'m^3/(mol*s)'), n=1.2433, w0=(591250,'J/mol'), E0=(59125,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5787018105298811, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.4540246495725655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.4540246495725655""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.4540246495725655
""",
)

entry(
    index = 57,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_4BrClFHO->Cl",
    kinetics = ArrheniusBM(A=(4e+08,'m^3/(mol*s)'), n=0, w0=(664000,'J/mol'), E0=(66400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_4BrClFHO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_4BrClFHO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_4BrClFHO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_4BrClFHO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl",
    kinetics = ArrheniusBM(A=(502.831,'m^3/(mol*s)'), n=1.41893, w0=(675714,'J/mol'), E0=(41897.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2599031407483901, var=1.769290546890677, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl
    Total Standard Deviation in ln(k): 3.3196149428869375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl
Total Standard Deviation in ln(k): 3.3196149428869375""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl
Total Standard Deviation in ln(k): 3.3196149428869375
""",
)

entry(
    index = 59,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl",
    kinetics = ArrheniusBM(A=(1.58084e+07,'m^3/(mol*s)'), n=3.20208e-07, w0=(551367,'J/mol'), E0=(55136.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.011789206171092194, var=2.8781024455425017, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl',), comment="""BM rule fitted to 15 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl
    Total Standard Deviation in ln(k): 3.4306483869182207"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl
Total Standard Deviation in ln(k): 3.4306483869182207""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl
Total Standard Deviation in ln(k): 3.4306483869182207
""",
)

entry(
    index = 60,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl",
    kinetics = ArrheniusBM(A=(2696.06,'m^3/(mol*s)'), n=1.16477, w0=(573361,'J/mol'), E0=(50331.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.035895850070505074, var=0.6890116412707841, Tref=1000.0, N=79, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl',), comment="""BM rule fitted to 79 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl
    Total Standard Deviation in ln(k): 1.7542555128487884"""),
    rank = 11,
    shortDesc = """BM rule fitted to 79 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl
Total Standard Deviation in ln(k): 1.7542555128487884""",
    longDesc = 
"""
BM rule fitted to 79 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl
Total Standard Deviation in ln(k): 1.7542555128487884
""",
)

entry(
    index = 61,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(644,'m^3/(mol*s)'), n=1.19, w0=(515000,'J/mol'), E0=(35435.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O",
    kinetics = ArrheniusBM(A=(92198.4,'m^3/(mol*s)'), n=0.0663312, w0=(563000,'J/mol'), E0=(47852.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.014854612371058814, var=0.2549963919886231, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O',), comment="""BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O
    Total Standard Deviation in ln(k): 1.049657575505014"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O
Total Standard Deviation in ln(k): 1.049657575505014""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O
Total Standard Deviation in ln(k): 1.049657575505014
""",
)

entry(
    index = 63,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O",
    kinetics = ArrheniusBM(A=(208011,'m^3/(mol*s)'), n=0.16611, w0=(534780,'J/mol'), E0=(21405.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.7743672283191323, var=17.040767047714436, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O',), comment="""BM rule fitted to 25 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O
    Total Standard Deviation in ln(k): 15.246411341666843"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O
Total Standard Deviation in ln(k): 15.246411341666843""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O
Total Standard Deviation in ln(k): 15.246411341666843
""",
)

entry(
    index = 64,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_Sp-2R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(52750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 66,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R",
    kinetics = ArrheniusBM(A=(4.86519e+11,'m^3/(mol*s)'), n=-1.79814, w0=(539000,'J/mol'), E0=(73074.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5820229216194461, var=5.413428600282235, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R
    Total Standard Deviation in ln(k): 6.126741325015148"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R
Total Standard Deviation in ln(k): 6.126741325015148""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R
Total Standard Deviation in ln(k): 6.126741325015148
""",
)

entry(
    index = 67,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_4R->C",
    kinetics = ArrheniusBM(A=(333333,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C",
    kinetics = ArrheniusBM(A=(173205,'m^3/(mol*s)'), n=1.35574e-07, w0=(563000,'J/mol'), E0=(46540.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.022311563383785947, var=0.9128396300673464, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C
    Total Standard Deviation in ln(k): 1.9714360478721071"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C
Total Standard Deviation in ln(k): 1.9714360478721071""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C
Total Standard Deviation in ln(k): 1.9714360478721071
""",
)

entry(
    index = 69,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_5R!H->Br",
    kinetics = ArrheniusBM(A=(3.33333e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_5R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_5R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_5R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_5R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br",
    kinetics = ArrheniusBM(A=(61.1993,'m^3/(mol*s)'), n=1.7066, w0=(621929,'J/mol'), E0=(5687.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4986020661624693, var=0.7323039064675139, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br
    Total Standard Deviation in ln(k): 2.968316184836872"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br
Total Standard Deviation in ln(k): 2.968316184836872""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br
Total Standard Deviation in ln(k): 2.968316184836872
""",
)

entry(
    index = 71,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_1R!H->C",
    kinetics = ArrheniusBM(A=(0.014,'m^3/(mol*s)'), n=2.69, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_N-1R!H->C",
    kinetics = ArrheniusBM(A=(0.014,'m^3/(mol*s)'), n=2.69, w0=(684500,'J/mol'), E0=(68450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_N-1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_N-1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O",
    kinetics = ArrheniusBM(A=(42.0837,'m^3/(mol*s)'), n=1.70846, w0=(644100,'J/mol'), E0=(-10136.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0156632286513384, var=1.1623265201453912, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O
    Total Standard Deviation in ln(k): 2.200684752460544"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O
Total Standard Deviation in ln(k): 2.200684752460544""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O
Total Standard Deviation in ln(k): 2.200684752460544
""",
)

entry(
    index = 74,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O",
    kinetics = ArrheniusBM(A=(378.604,'m^3/(mol*s)'), n=1.25967, w0=(554864,'J/mol'), E0=(44537.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.21239797863309964, var=0.46275685403541345, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O',), comment="""BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O
    Total Standard Deviation in ln(k): 1.8974090418706124"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O
Total Standard Deviation in ln(k): 1.8974090418706124""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O
Total Standard Deviation in ln(k): 1.8974090418706124
""",
)

entry(
    index = 75,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(98.4583,'m^3/(mol*s)'), n=0.990174, w0=(567205,'J/mol'), E0=(-8961.97,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-6.482384426366694, var=35.52712378275101, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R',), comment="""BM rule fitted to 22 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 28.23654808479645"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 28.23654808479645""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 28.23654808479645
""",
)

entry(
    index = 76,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.05631e+06,'m^3/(mol*s)'), n=-0.213327, w0=(563000,'J/mol'), E0=(43738.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.6019696989205539, var=10.60267256061033, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 10.552816790348329"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 10.552816790348329""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 10.552816790348329
""",
)

entry(
    index = 77,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(442387,'m^3/(mol*s)'), n=0.250595, w0=(551500,'J/mol'), E0=(95697.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.026547653896902897, var=6.6826228440374145, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 5.249097089975617"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C
Total Standard Deviation in ln(k): 5.249097089975617""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C
Total Standard Deviation in ln(k): 5.249097089975617
""",
)

entry(
    index = 78,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(300000,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(61668.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C",
    kinetics = ArrheniusBM(A=(4.0323e+08,'m^3/(mol*s)'), n=-0.767651, w0=(539000,'J/mol'), E0=(93851.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6686805241504197, var=1.5203969831175077, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C
    Total Standard Deviation in ln(k): 4.152027953233546"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C
Total Standard Deviation in ln(k): 4.152027953233546""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C
Total Standard Deviation in ln(k): 4.152027953233546
""",
)

entry(
    index = 80,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C",
    kinetics = ArrheniusBM(A=(7.85258e+06,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.1035620543197945e-11, var=0.12683959564563585, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C',), comment="""BM rule fitted to 11 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C
    Total Standard Deviation in ln(k): 0.7139773159781367"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C
Total Standard Deviation in ln(k): 0.7139773159781367""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C
Total Standard Deviation in ln(k): 0.7139773159781367
""",
)

entry(
    index = 81,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_5R!H->C",
    kinetics = ArrheniusBM(A=(3e+06,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(80345.8,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_N-5R!H->C",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(52750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 83,
    label = "Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.12583e+07,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=2.413897921625164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H_Ext-2C-R
    Total Standard Deviation in ln(k): 3.1147015559000413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H_Ext-2C-R
Total Standard Deviation in ln(k): 3.1147015559000413""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H_Ext-2C-R
Total Standard Deviation in ln(k): 3.1147015559000413
""",
)

entry(
    index = 84,
    label = "Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_4C-u1",
    kinetics = ArrheniusBM(A=(2.19e+08,'m^3/(mol*s)'), n=-0.68, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 85,
    label = "Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_N-4C-u1",
    kinetics = ArrheniusBM(A=(3.01e+07,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_N-4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_N-4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_4C-u1",
    kinetics = ArrheniusBM(A=(8.49e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 87,
    label = "Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_N-4C-u1",
    kinetics = ArrheniusBM(A=(1.21e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_N-4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_N-4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 88,
    label = "Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C_Ext-2NO-R",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(547000,'J/mol'), E0=(47445.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C_Ext-2NO-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C_Ext-2NO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C_Ext-2NO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C_Ext-2NO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N",
    kinetics = ArrheniusBM(A=(1.99593e-05,'m^3/(mol*s)'), n=3.27437, w0=(562750,'J/mol'), E0=(48247.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.858295964871344, var=0.08142204673665214, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N
    Total Standard Deviation in ln(k): 2.7285646310134792"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N
Total Standard Deviation in ln(k): 2.7285646310134792""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N
Total Standard Deviation in ln(k): 2.7285646310134792
""",
)

entry(
    index = 90,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->N",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(638000,'J/mol'), E0=(77506.6,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N",
    kinetics = ArrheniusBM(A=(207.556,'m^3/(mol*s)'), n=1.2433, w0=(550250,'J/mol'), E0=(17424.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6172896801193773, var=3.9362754729278144, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N
    Total Standard Deviation in ln(k): 5.528383327536255"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N
Total Standard Deviation in ln(k): 5.528383327536255""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N
Total Standard Deviation in ln(k): 5.528383327536255
""",
)

entry(
    index = 92,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N",
    kinetics = ArrheniusBM(A=(4147.31,'m^3/(mol*s)'), n=0.9029, w0=(612000,'J/mol'), E0=(51367.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8754987103028704, var=0.28030785144339526, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N
    Total Standard Deviation in ln(k): 3.2611345968802175"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N
Total Standard Deviation in ln(k): 3.2611345968802175""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N
Total Standard Deviation in ln(k): 3.2611345968802175
""",
)

entry(
    index = 93,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 94,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(648000,'J/mol'), E0=(64800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N",
    kinetics = ArrheniusBM(A=(456.772,'m^3/(mol*s)'), n=1.4304, w0=(657500,'J/mol'), E0=(39796.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.013045707375695456, var=0.8109859100836722, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N
    Total Standard Deviation in ln(k): 1.838137444146553"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N
Total Standard Deviation in ln(k): 1.838137444146553""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N
Total Standard Deviation in ln(k): 1.838137444146553
""",
)

entry(
    index = 96,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N",
    kinetics = ArrheniusBM(A=(7.34936e+07,'m^3/(mol*s)'), n=2.13361e-06, w0=(689375,'J/mol'), E0=(68937.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9201382049416033, var=2.903719867402118, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N
    Total Standard Deviation in ln(k): 5.7280347082365495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N
Total Standard Deviation in ln(k): 5.7280347082365495""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N
Total Standard Deviation in ln(k): 5.7280347082365495
""",
)

entry(
    index = 97,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(9.06644e+06,'m^3/(mol*s)'), n=1.22618e-07, w0=(545200,'J/mol'), E0=(54520,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.004724030202329742, var=3.265960879878607, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R',), comment="""BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.634820575424553"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.634820575424553""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.634820575424553
""",
)

entry(
    index = 98,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(2.15443e+07,'m^3/(mol*s)'), n=9.94521e-08, w0=(543667,'J/mol'), E0=(54366.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.6982780719772782e-09, var=3.9764236524905177, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R
    Total Standard Deviation in ln(k): 3.9976366135869816"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R
Total Standard Deviation in ln(k): 3.9976366135869816""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R
Total Standard Deviation in ln(k): 3.9976366135869816
""",
)

entry(
    index = 99,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_2R!H->C",
    kinetics = ArrheniusBM(A=(6e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 100,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.33333e+08,'m^3/(mol*s)'), n=0, w0=(640000,'J/mol'), E0=(64000,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 101,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1",
    kinetics = ArrheniusBM(A=(1944.68,'m^3/(mol*s)'), n=1.19066, w0=(572735,'J/mol'), E0=(41067.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.027727632105939027, var=0.8813340525175969, Tref=1000.0, N=66, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1',), comment="""BM rule fitted to 66 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1
    Total Standard Deviation in ln(k): 1.951700549424239"""),
    rank = 11,
    shortDesc = """BM rule fitted to 66 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1
Total Standard Deviation in ln(k): 1.951700549424239""",
    longDesc = 
"""
BM rule fitted to 66 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1
Total Standard Deviation in ln(k): 1.951700549424239
""",
)

entry(
    index = 102,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1",
    kinetics = ArrheniusBM(A=(13381.7,'m^3/(mol*s)'), n=0.98371, w0=(576538,'J/mol'), E0=(55091.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01140765570669884, var=0.2459058529005692, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1',), comment="""BM rule fitted to 13 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1
    Total Standard Deviation in ln(k): 1.0227884284647555"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1
Total Standard Deviation in ln(k): 1.0227884284647555""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1
Total Standard Deviation in ln(k): 1.0227884284647555
""",
)

entry(
    index = 103,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(100000,'m^3/(mol*s)'), n=-2.77536e-08, w0=(563000,'J/mol'), E0=(36749.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03683867637879362, var=0.006785440032888532, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.2576970994969242"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.2576970994969242""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.2576970994969242
""",
)

entry(
    index = 104,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.32312e+09,'m^3/(mol*s)'), n=-1.12603, w0=(563000,'J/mol'), E0=(66591.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.052548950627476436, var=0.4586434839738491, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.489703732409137"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.489703732409137""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.489703732409137
""",
)

entry(
    index = 105,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H",
    kinetics = ArrheniusBM(A=(0.00288832,'m^3/(mol*s)'), n=2.60465, w0=(539000,'J/mol'), E0=(60901,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.21696893581342247, var=8.530313977819539, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H
    Total Standard Deviation in ln(k): 6.400317928589529"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H
Total Standard Deviation in ln(k): 6.400317928589529""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H
Total Standard Deviation in ln(k): 6.400317928589529
""",
)

entry(
    index = 106,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H",
    kinetics = ArrheniusBM(A=(366926,'m^3/(mol*s)'), n=0.0907004, w0=(533725,'J/mol'), E0=(21617.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.9948080147013494, var=18.46282444261473, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H',), comment="""BM rule fitted to 20 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H
    Total Standard Deviation in ln(k): 16.13866689677922"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H
Total Standard Deviation in ln(k): 16.13866689677922""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H
Total Standard Deviation in ln(k): 16.13866689677922
""",
)

entry(
    index = 107,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-4R-R",
    kinetics = ArrheniusBM(A=(50000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(27880,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-4R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-4R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 108,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.08e+08,'m^3/(mol*s)'), n=-0.75, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 109,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(173210,'m^3/(mol*s)'), n=-3.90619e-06, w0=(563000,'J/mol'), E0=(47764.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=2.413897921625164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.1147015559000413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.1147015559000413""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.1147015559000413
""",
)

entry(
    index = 110,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_2R!H->C",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(55631.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 111,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C",
    kinetics = ArrheniusBM(A=(61.0108,'m^3/(mol*s)'), n=1.70703, w0=(612333,'J/mol'), E0=(5602.44,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.49688755770898335, var=0.7259146313145405, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C
    Total Standard Deviation in ln(k): 2.9565079937788545"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C
Total Standard Deviation in ln(k): 2.9565079937788545""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C
Total Standard Deviation in ln(k): 2.9565079937788545
""",
)

entry(
    index = 112,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS",
    kinetics = ArrheniusBM(A=(59.8233,'m^3/(mol*s)'), n=1.70883, w0=(646000,'J/mol'), E0=(-7291.46,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6481540739875871, var=1.2661331430625915, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS
    Total Standard Deviation in ln(k): 3.884307492821052"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS
Total Standard Deviation in ln(k): 3.884307492821052""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS
Total Standard Deviation in ln(k): 3.884307492821052
""",
)

entry(
    index = 113,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS",
    kinetics = ArrheniusBM(A=(29.5781,'m^3/(mol*s)'), n=1.70809, w0=(641250,'J/mol'), E0=(15026.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.371079197325291, var=11.754133763518633, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS
    Total Standard Deviation in ln(k): 12.830579739955681"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS
Total Standard Deviation in ln(k): 12.830579739955681""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS
Total Standard Deviation in ln(k): 12.830579739955681
""",
)

entry(
    index = 114,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_2R!H->O",
    kinetics = ArrheniusBM(A=(2.41e+07,'m^3/(mol*s)'), n=0, w0=(631500,'J/mol'), E0=(63150,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_2R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_2R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 115,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O",
    kinetics = ArrheniusBM(A=(373.335,'m^3/(mol*s)'), n=1.26127, w0=(547200,'J/mol'), E0=(44455.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09293098599633158, var=0.14943280685062918, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O
    Total Standard Deviation in ln(k): 1.0084561525585607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O
Total Standard Deviation in ln(k): 1.0084561525585607""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O
Total Standard Deviation in ln(k): 1.0084561525585607
""",
)

entry(
    index = 116,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(0.74368,'m^3/(mol*s)'), n=1.36149, w0=(563000,'J/mol'), E0=(6268.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.28022075084104203, var=1.3066098822820702, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C
    Total Standard Deviation in ln(k): 2.995625515056295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 2.995625515056295""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 2.995625515056295
""",
)

entry(
    index = 117,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(121.636,'m^3/(mol*s)'), n=0.974108, w0=(570115,'J/mol'), E0=(-10346,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.4435507902426001, var=3.440982262501939, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C',), comment="""BM rule fitted to 13 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 7.345772510651407"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 7.345772510651407""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 7.345772510651407
""",
)

entry(
    index = 118,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(7.23e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(95940.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 119,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(379755,'m^3/(mol*s)'), n=-0.0841636, w0=(563000,'J/mol'), E0=(42508.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.4739762940232457, var=17.059429359827508, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 14.496190571894662"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 14.496190571894662""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 14.496190571894662
""",
)

entry(
    index = 120,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(300000,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(62563.8,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 121,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H",
    kinetics = ArrheniusBM(A=(8.32046e+06,'m^3/(mol*s)'), n=-0.32, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=8.610921668180418e-17, var=0.8378904353806431, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H
    Total Standard Deviation in ln(k): 1.83506142460303"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H
Total Standard Deviation in ln(k): 1.83506142460303""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H
Total Standard Deviation in ln(k): 1.83506142460303
""",
)

entry(
    index = 122,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_N-Sp-5C-1R!H",
    kinetics = ArrheniusBM(A=(3.01e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(98614.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_N-Sp-5C-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_N-Sp-5C-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_N-Sp-5C-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_N-Sp-5C-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 123,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(6.5e+06,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0436096431476528e-14, var=3.1115076389305714e-60, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 2.6221347817780225e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.6221347817780225e-14""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.6221347817780225e-14
""",
)

entry(
    index = 124,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(9.19239e+06,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.266445498303389e-11, var=0.28471289712933473, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.0696964628533052"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.0696964628533052""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.0696964628533052
""",
)

entry(
    index = 125,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N_2NO->N",
    kinetics = ArrheniusBM(A=(0.82,'m^3/(mol*s)'), n=1.87, w0=(524000,'J/mol'), E0=(52400,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 126,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N_N-2NO->N",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(601500,'J/mol'), E0=(75469.3,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 127,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->N",
    kinetics = ArrheniusBM(A=(0.46,'m^3/(mol*s)'), n=1.94, w0=(511500,'J/mol'), E0=(51150,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 128,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->N",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(589000,'J/mol'), E0=(45647.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 129,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->N",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(625500,'J/mol'), E0=(52086.6,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 130,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->N",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(598500,'J/mol'), E0=(35577.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 131,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_4BrFHO->O",
    kinetics = ArrheniusBM(A=(1092.77,'m^3/(mol*s)'), n=1.28049, w0=(662000,'J/mol'), E0=(39660.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6700553094724085, var=4.7491833562063475, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_4BrFHO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_4BrFHO->O
    Total Standard Deviation in ln(k): 6.05239925428057"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_4BrFHO->O
Total Standard Deviation in ln(k): 6.05239925428057""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_4BrFHO->O
Total Standard Deviation in ln(k): 6.05239925428057
""",
)

entry(
    index = 132,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_N-4BrFHO->O",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(648500,'J/mol'), E0=(59320.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_N-4BrFHO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_N-4BrFHO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_N-4BrFHO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_N-4BrFHO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 133,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1",
    kinetics = ArrheniusBM(A=(2.43625e+07,'m^3/(mol*s)'), n=4.75653e-07, w0=(692667,'J/mol'), E0=(69266.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.970983714140985e-08, var=0.09267420389677285, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1
    Total Standard Deviation in ln(k): 0.6102903603961687"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1
Total Standard Deviation in ln(k): 0.6102903603961687""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1
Total Standard Deviation in ln(k): 0.6102903603961687
""",
)

entry(
    index = 134,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_N-4BrFHO-u1",
    kinetics = ArrheniusBM(A=(9.04e+07,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(67950,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_N-4BrFHO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_N-4BrFHO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_N-4BrFHO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_N-4BrFHO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 135,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_5R!H->O",
    kinetics = ArrheniusBM(A=(3.66667e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 136,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(4.91226e+06,'m^3/(mol*s)'), n=-4.48064e-08, w0=(544944,'J/mol'), E0=(54494.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.23044180294496538, var=1.6164595104630008, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O
    Total Standard Deviation in ln(k): 3.127820904665338"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O
Total Standard Deviation in ln(k): 3.127820904665338""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O
Total Standard Deviation in ln(k): 3.127820904665338
""",
)

entry(
    index = 137,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(9.99999e+06,'m^3/(mol*s)'), n=1.28714e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 138,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(536000,'J/mol'), E0=(53600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 139,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F",
    kinetics = ArrheniusBM(A=(5.27632e+06,'m^3/(mol*s)'), n=0.134627, w0=(619889,'J/mol'), E0=(61988.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.007433453574601324, var=0.5933475869225935, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F
    Total Standard Deviation in ln(k): 1.5629055766274802"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F
Total Standard Deviation in ln(k): 1.5629055766274802""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F
Total Standard Deviation in ln(k): 1.5629055766274802
""",
)

entry(
    index = 140,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F",
    kinetics = ArrheniusBM(A=(1935.25,'m^3/(mol*s)'), n=1.19131, w0=(565289,'J/mol'), E0=(40542.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.027727325132687376, var=0.8814589058977029, Tref=1000.0, N=57, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F',), comment="""BM rule fitted to 57 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F
    Total Standard Deviation in ln(k): 1.951833081662386"""),
    rank = 11,
    shortDesc = """BM rule fitted to 57 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F
Total Standard Deviation in ln(k): 1.951833081662386""",
    longDesc = 
"""
BM rule fitted to 57 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F
Total Standard Deviation in ln(k): 1.951833081662386
""",
)

entry(
    index = 141,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(21102.1,'m^3/(mol*s)'), n=0.949997, w0=(572250,'J/mol'), E0=(58616.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02317715875828442, var=0.2705083413726282, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.1009051286291296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.1009051286291296""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.1009051286291296
""",
)

entry(
    index = 142,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(11330.1,'m^3/(mol*s)'), n=0.961232, w0=(583400,'J/mol'), E0=(58340,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.029729958794657493, var=0.00022219016772130848, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 0.10458105954761464"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.10458105954761464""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.10458105954761464
""",
)

entry(
    index = 143,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(99999.9,'m^3/(mol*s)'), n=7.43399e-08, w0=(563000,'J/mol'), E0=(35157.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06777427083031706, var=0.013780053907581396, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 0.40561990482767823"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 0.40561990482767823""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 0.40561990482767823
""",
)

entry(
    index = 144,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(141424,'m^3/(mol*s)'), n=-2.38941e-06, w0=(563000,'J/mol'), E0=(43090.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 145,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-5BrCClFNO-R",
    kinetics = ArrheniusBM(A=(84300,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(76679.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-5BrCClFNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-5BrCClFNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-5BrCClFNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-5BrCClFNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 146,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R",
    kinetics = ArrheniusBM(A=(5.7233e-06,'m^3/(mol*s)'), n=3.63493, w0=(539000,'J/mol'), E0=(-15602.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01212298866688248, var=10.62902192556191, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R
    Total Standard Deviation in ln(k): 6.566333314344455"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R
Total Standard Deviation in ln(k): 6.566333314344455""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R
Total Standard Deviation in ln(k): 6.566333314344455
""",
)

entry(
    index = 147,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Sp-5BrCClFNO-4BrCCClFNOS",
    kinetics = ArrheniusBM(A=(964000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(91985.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Sp-5BrCClFNO-4BrCCClFNOS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Sp-5BrCClFNO-4BrCCClFNOS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Sp-5BrCClFNO-4BrCCClFNOS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Sp-5BrCClFNO-4BrCCClFNOS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 148,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_N-Sp-5BrCClFNO-4BrCCClFNOS",
    kinetics = ArrheniusBM(A=(2.41e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_N-Sp-5BrCClFNO-4BrCCClFNOS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_N-Sp-5BrCClFNO-4BrCCClFNOS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_N-Sp-5BrCClFNO-4BrCCClFNOS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_N-Sp-5BrCClFNO-4BrCCClFNOS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 149,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C",
    kinetics = ArrheniusBM(A=(914507,'m^3/(mol*s)'), n=0.00704261, w0=(537029,'J/mol'), E0=(37501.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.4180768060778155, var=0.6354543713079978, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C',), comment="""BM rule fitted to 17 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C
    Total Standard Deviation in ln(k): 2.64852666079703"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C
Total Standard Deviation in ln(k): 2.64852666079703""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C
Total Standard Deviation in ln(k): 2.64852666079703
""",
)

entry(
    index = 150,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C",
    kinetics = ArrheniusBM(A=(2.0979e+11,'m^3/(mol*s)'), n=-1.98489, w0=(515000,'J/mol'), E0=(86112.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.574695201284503, var=31.638150866782397, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C
    Total Standard Deviation in ln(k): 20.25784014884851"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C
Total Standard Deviation in ln(k): 20.25784014884851""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C
Total Standard Deviation in ln(k): 20.25784014884851
""",
)

entry(
    index = 151,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_1R!H->C",
    kinetics = ArrheniusBM(A=(8.03333e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 152,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C",
    kinetics = ArrheniusBM(A=(55.5201,'m^3/(mol*s)'), n=1.72068, w0=(603700,'J/mol'), E0=(5726.82,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4974265036478005, var=0.715585916381764, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C
    Total Standard Deviation in ln(k): 2.945667077087709"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C
Total Standard Deviation in ln(k): 2.945667077087709""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C
Total Standard Deviation in ln(k): 2.945667077087709
""",
)

entry(
    index = 153,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_Ext-5BrCClOS-R",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(56981.6,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_Ext-5BrCClOS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_Ext-5BrCClOS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_Ext-5BrCClOS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_Ext-5BrCClOS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 154,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O",
    kinetics = ArrheniusBM(A=(56.1763,'m^3/(mol*s)'), n=1.71849, w0=(627000,'J/mol'), E0=(-1662.01,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.406650984474472, var=12.833305395099408, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O
    Total Standard Deviation in ln(k): 20.766233586810195"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O
Total Standard Deviation in ln(k): 20.766233586810195""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O
Total Standard Deviation in ln(k): 20.766233586810195
""",
)

entry(
    index = 155,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O",
    kinetics = ArrheniusBM(A=(1.25258e+07,'m^3/(mol*s)'), n=-0.25, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.6129510735315866e-09, var=0.029913004620106633, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O
    Total Standard Deviation in ln(k): 0.34672649236279346"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O
Total Standard Deviation in ln(k): 0.34672649236279346""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O
Total Standard Deviation in ln(k): 0.34672649236279346
""",
)

entry(
    index = 156,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O",
    kinetics = ArrheniusBM(A=(1.81e+08,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(56496.6,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 157,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O",
    kinetics = ArrheniusBM(A=(28.9958,'m^3/(mol*s)'), n=1.71026, w0=(636500,'J/mol'), E0=(12393.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.571623885545163, var=0.5970193635129432, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O
    Total Standard Deviation in ln(k): 8.010365762659578"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O
Total Standard Deviation in ln(k): 8.010365762659578""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O
Total Standard Deviation in ln(k): 8.010365762659578
""",
)

entry(
    index = 158,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS",
    kinetics = ArrheniusBM(A=(3.61e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 159,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS",
    kinetics = ArrheniusBM(A=(369.028,'m^3/(mol*s)'), n=1.26286, w0=(548111,'J/mol'), E0=(44445,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.19432314310503807, var=0.1896009347005461, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS',), comment="""BM rule fitted to 9 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS
    Total Standard Deviation in ln(k): 1.3611746958904072"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS
Total Standard Deviation in ln(k): 1.3611746958904072""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS
Total Standard Deviation in ln(k): 1.3611746958904072
""",
)

entry(
    index = 160,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C",
    kinetics = ArrheniusBM(A=(3.13627e+07,'m^3/(mol*s)'), n=-0.944432, w0=(563000,'J/mol'), E0=(43424.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.10764766642615303, var=0.3151667095440669, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C
    Total Standard Deviation in ln(k): 1.395923992499249"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C
Total Standard Deviation in ln(k): 1.395923992499249""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C
Total Standard Deviation in ln(k): 1.395923992499249
""",
)

entry(
    index = 161,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_N-Sp-6C-1C",
    kinetics = ArrheniusBM(A=(602200,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(39964.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_N-Sp-6C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_N-Sp-6C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_N-Sp-6C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_N-Sp-6C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 162,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(5.20695e+09,'m^3/(mol*s)'), n=-1.78352, w0=(563000,'J/mol'), E0=(-7171.36,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.076458680558956, var=1.2483619426967265, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 4.944562933450632"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.944562933450632""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.944562933450632
""",
)

entry(
    index = 163,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C",
    kinetics = ArrheniusBM(A=(6.52663e+14,'m^3/(mol*s)'), n=-3.14885, w0=(563000,'J/mol'), E0=(2489.62,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.8409285322525404, var=18.467111861243236, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C
    Total Standard Deviation in ln(k): 13.240472329179818"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C
Total Standard Deviation in ln(k): 13.240472329179818""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C
Total Standard Deviation in ln(k): 13.240472329179818
""",
)

entry(
    index = 164,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(300000,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(57975.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 165,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(4.48112e+14,'m^3/(mol*s)'), n=-3.14885, w0=(563000,'J/mol'), E0=(1171.57,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.358982844941349, var=17.022951268563478, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 11.685842033831564"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.685842033831564""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.685842033831564
""",
)

entry(
    index = 166,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_N-6BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(250000,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(44398.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_N-6BrClFINOPSSi->F',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_N-6BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_N-6BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_N-6BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 167,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(6.02e+06,'m^3/(mol*s)'), n=-0.32, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 168,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(6.5e+06,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.996003610813218e-15, var=9.334522916791711e-61, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.2552772891490499e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.2552772891490499e-14""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.2552772891490499e-14
""",
)

entry(
    index = 169,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(9.19239e+06,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 170,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_4BrFHO->O_4O-u1",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(662000,'J/mol'), E0=(66200,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_4BrFHO->O_4O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_4BrFHO->O_4O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_4BrFHO->O_4O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_4BrFHO->O_4O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 171,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_4BrFHO->O_N-4O-u1",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(662000,'J/mol'), E0=(48035.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_4BrFHO->O_N-4O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_4BrFHO->O_N-4O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_4BrFHO->O_N-4O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_4BrFHO->O_N-4O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 172,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_4BrFHO->F",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(732500,'J/mol'), E0=(73250,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_4BrFHO->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_4BrFHO->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_4BrFHO->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_4BrFHO->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 173,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F",
    kinetics = ArrheniusBM(A=(2.19544e+07,'m^3/(mol*s)'), n=5.84356e-07, w0=(672750,'J/mol'), E0=(67275,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=6.458191251135313e-17, var=0.06954925777421293, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F
    Total Standard Deviation in ln(k): 0.5286926091131748"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F
Total Standard Deviation in ln(k): 0.5286926091131748""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F
Total Standard Deviation in ln(k): 0.5286926091131748
""",
)

entry(
    index = 174,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.10064e+07,'m^3/(mol*s)'), n=1.3093e-08, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.5586460192786372e-08, var=0.6944264527262918, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.6705909874654379"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.6705909874654379""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.6705909874654379
""",
)

entry(
    index = 175,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(3.85891e+06,'m^3/(mol*s)'), n=-1.48775e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6669698280313657, var=3.368805659110193, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 5.355355787726706"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 5.355355787726706""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 5.355355787726706
""",
)

entry(
    index = 176,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(4.47213e+06,'m^3/(mol*s)'), n=7.10656e-08, w0=(536000,'J/mol'), E0=(53600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=5.180580787960471, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 4.5629553043324895"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 4.5629553043324895""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 4.5629553043324895
""",
)

entry(
    index = 177,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 178,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(541149,'m^3/(mol*s)'), n=0.403881, w0=(608333,'J/mol'), E0=(60833.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.022300353306577345, var=1.0935717572740768, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R
    Total Standard Deviation in ln(k): 2.152462324155837"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R
Total Standard Deviation in ln(k): 2.152462324155837""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R
Total Standard Deviation in ln(k): 2.152462324155837
""",
)

entry(
    index = 179,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.15443e+07,'m^3/(mol*s)'), n=7.06236e-08, w0=(612167,'J/mol'), E0=(61216.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.4502455195451049e-08, var=1.4663745010001799, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R
    Total Standard Deviation in ln(k): 2.4276129521491097"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.4276129521491097""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.4276129521491097
""",
)

entry(
    index = 180,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_2R!H->C",
    kinetics = ArrheniusBM(A=(1.41421e+07,'m^3/(mol*s)'), n=7.62613e-07, w0=(604500,'J/mol'), E0=(60450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_2R!H->C
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_2R!H->C
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_2R!H->C
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 181,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(708500,'J/mol'), E0=(70850,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 182,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(22986.1,'m^3/(mol*s)'), n=0.874504, w0=(556260,'J/mol'), E0=(12520.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1662985625904309, var=2.9163421704758816, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R',), comment="""BM rule fitted to 25 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.8413820632162765"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.8413820632162765""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.8413820632162765
""",
)

entry(
    index = 183,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(773855,'m^3/(mol*s)'), n=0.263656, w0=(558273,'J/mol'), E0=(55827.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11962743067498456, var=1.127508526348304, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R',), comment="""BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R
    Total Standard Deviation in ln(k): 2.429283426060874"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R
Total Standard Deviation in ln(k): 2.429283426060874""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R
Total Standard Deviation in ln(k): 2.429283426060874
""",
)

entry(
    index = 184,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H",
    kinetics = ArrheniusBM(A=(20606.3,'m^3/(mol*s)'), n=0.974841, w0=(578650,'J/mol'), E0=(69135.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12100722065132712, var=0.28482315574681094, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H',), comment="""BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H
    Total Standard Deviation in ln(k): 1.3739418122073803"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H
Total Standard Deviation in ln(k): 1.3739418122073803""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H
Total Standard Deviation in ln(k): 1.3739418122073803
""",
)

entry(
    index = 185,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H",
    kinetics = ArrheniusBM(A=(494.339,'m^3/(mol*s)'), n=1.27841, w0=(580682,'J/mol'), E0=(60123.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.039837734155486734, var=0.2593306826472448, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H',), comment="""BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H
    Total Standard Deviation in ln(k): 1.120996542436354"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H
Total Standard Deviation in ln(k): 1.120996542436354""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H
Total Standard Deviation in ln(k): 1.120996542436354
""",
)

entry(
    index = 186,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N",
    kinetics = ArrheniusBM(A=(9285.38,'m^3/(mol*s)'), n=1.04814, w0=(574750,'J/mol'), E0=(56311,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.011069718048892015, var=0.2650441677501103, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N
    Total Standard Deviation in ln(k): 1.0598999048793392"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N
Total Standard Deviation in ln(k): 1.0598999048793392""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N
Total Standard Deviation in ln(k): 1.0598999048793392
""",
)

entry(
    index = 187,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N",
    kinetics = ArrheniusBM(A=(105722,'m^3/(mol*s)'), n=0.767089, w0=(569750,'J/mol'), E0=(56975,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5283265097194069, var=1.658934236468343, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N
    Total Standard Deviation in ln(k): 3.9095447233524565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N
Total Standard Deviation in ln(k): 3.9095447233524565""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N
Total Standard Deviation in ln(k): 3.9095447233524565
""",
)

entry(
    index = 188,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(444.29,'m^3/(mol*s)'), n=1.44792, w0=(551500,'J/mol'), E0=(55150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.202693327970796, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_Ext-2R!H-R
    Total Standard Deviation in ln(k): 4.987000417702588"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.987000417702588""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.987000417702588
""",
)

entry(
    index = 189,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N",
    kinetics = ArrheniusBM(A=(11361.3,'m^3/(mol*s)'), n=0.960818, w0=(621500,'J/mol'), E0=(62150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4478648794535599, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N
    Total Standard Deviation in ln(k): 1.1252886418431154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N
Total Standard Deviation in ln(k): 1.1252886418431154""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N
Total Standard Deviation in ln(k): 1.1252886418431154
""",
)

entry(
    index = 190,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->N",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 191,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(100000,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(34811.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 192,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R_Ext-4CS-R",
    kinetics = ArrheniusBM(A=(2.89e+07,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(83476.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R_Ext-4CS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R_Ext-4CS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R_Ext-4CS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R_Ext-4CS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 193,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=1.90562e-08, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 194,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C",
    kinetics = ArrheniusBM(A=(726125,'m^3/(mol*s)'), n=0.0325124, w0=(536767,'J/mol'), E0=(26733.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2280793621008961, var=0.22639694047252357, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C',), comment="""BM rule fitted to 15 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C
    Total Standard Deviation in ln(k): 1.5269404800964796"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C
Total Standard Deviation in ln(k): 1.5269404800964796""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C
Total Standard Deviation in ln(k): 1.5269404800964796
""",
)

entry(
    index = 195,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.02405e+07,'m^3/(mol*s)'), n=-0.333202, w0=(515000,'J/mol'), E0=(48693,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2997294586580246, var=0.0010542338907092693, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.8181807714204364"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.8181807714204364""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.8181807714204364
""",
)

entry(
    index = 196,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N",
    kinetics = ArrheniusBM(A=(55.3682,'m^3/(mol*s)'), n=1.72068, w0=(573833,'J/mol'), E0=(26375.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.16479020172419373, var=0.14297914762848185, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N
    Total Standard Deviation in ln(k): 1.1720878594844713"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N
Total Standard Deviation in ln(k): 1.1720878594844713""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N
Total Standard Deviation in ln(k): 1.1720878594844713
""",
)

entry(
    index = 197,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N",
    kinetics = ArrheniusBM(A=(6.23614e-40,'m^3/(mol*s)'), n=13.8207, w0=(648500,'J/mol'), E0=(-47906.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.127611593067805, var=3.4257180582824334, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N
    Total Standard Deviation in ln(k): 9.056260864310659"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N
Total Standard Deviation in ln(k): 9.056260864310659""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N
Total Standard Deviation in ln(k): 9.056260864310659
""",
)

entry(
    index = 198,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O_2R!H->C",
    kinetics = ArrheniusBM(A=(4.82e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 199,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O_N-2R!H->C",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(598500,'J/mol'), E0=(13428.6,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 200,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(2.85561e+07,'m^3/(mol*s)'), n=-0.375, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.305460834090209e-17, var=0.06912283083491383, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_Ext-4CNS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_Ext-4CNS-R
    Total Standard Deviation in ln(k): 0.5270693322083513"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.5270693322083513""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.5270693322083513
""",
)

entry(
    index = 201,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C",
    kinetics = ArrheniusBM(A=(1.90317e+07,'m^3/(mol*s)'), n=-4.02332e-07, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=1.6812080230698707, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C
    Total Standard Deviation in ln(k): 2.599367689841769"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C
Total Standard Deviation in ln(k): 2.599367689841769""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C
Total Standard Deviation in ln(k): 2.599367689841769
""",
)

entry(
    index = 202,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_N-2R!H->C",
    kinetics = ArrheniusBM(A=(0.014,'m^3/(mol*s)'), n=2.69, w0=(598500,'J/mol'), E0=(17401.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 203,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_2CNS->S",
    kinetics = ArrheniusBM(A=(979000,'m^3/(mol*s)'), n=0, w0=(537500,'J/mol'), E0=(35792.6,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_2CNS->S',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_2CNS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_2CNS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_2CNS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 204,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S",
    kinetics = ArrheniusBM(A=(363.241,'m^3/(mol*s)'), n=1.26521, w0=(549438,'J/mol'), E0=(38971.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.15581149374551953, var=0.09539423188382916, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S
    Total Standard Deviation in ln(k): 1.0106677723528414"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S
Total Standard Deviation in ln(k): 1.0106677723528414""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S
Total Standard Deviation in ln(k): 1.0106677723528414
""",
)

entry(
    index = 205,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=-3.13773e-09, w0=(563000,'J/mol'), E0=(20081.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.499352094098152e-10, var=2.06942654957822e-18, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R
    Total Standard Deviation in ln(k): 4.26565871441613e-09"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R
Total Standard Deviation in ln(k): 4.26565871441613e-09""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R
Total Standard Deviation in ln(k): 4.26565871441613e-09
""",
)

entry(
    index = 206,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(10974.5,'m^3/(mol*s)'), n=1.8387e-08, w0=(563000,'J/mol'), E0=(18973.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.2290956255676566e-17, var=0.06917824979652494, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.5272805777722495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.5272805777722495""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.5272805777722495
""",
)

entry(
    index = 207,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.85329e+12,'m^3/(mol*s)'), n=-2.58013, w0=(563000,'J/mol'), E0=(-11377.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3530200646193378, var=3.9569501506101985, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 4.8748209890591125"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.8748209890591125""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.8748209890591125
""",
)

entry(
    index = 208,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.73553e+14,'m^3/(mol*s)'), n=-3.14885, w0=(563000,'J/mol'), E0=(-3396.91,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.9625539661448168, var=2.873931729472134, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 8.32960223996552"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 8.32960223996552""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 8.32960223996552
""",
)

entry(
    index = 209,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.76152e+14,'m^3/(mol*s)'), n=-3.14885, w0=(563000,'J/mol'), E0=(7412.02,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.9625539661448155, var=15.77167145155163, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 12.892557544298002"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 12.892557544298002""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 12.892557544298002
""",
)

entry(
    index = 210,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(4.48111e+14,'m^3/(mol*s)'), n=-3.14885, w0=(563000,'J/mol'), E0=(2889.35,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.96255396614481, var=30.52594293923303, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F_Ext-2R!H-R
    Total Standard Deviation in ln(k): 16.007259100198016"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 16.007259100198016""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 16.007259100198016
""",
)

entry(
    index = 211,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(6.5e+06,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 212,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F_4HO->O",
    kinetics = ArrheniusBM(A=(2.41e+07,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(67950,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F_4HO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F_4HO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F_4HO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F_4HO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 213,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F_N-4HO->O",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(666000,'J/mol'), E0=(66600,'J/mol'), Tmin=(295,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F_N-4HO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F_N-4HO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F_N-4HO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F_N-4HO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 214,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(1.41421e+07,'m^3/(mol*s)'), n=1.32246e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 215,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(1.41421e+07,'m^3/(mol*s)'), n=1.32246e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 216,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(536000,'J/mol'), E0=(53600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 217,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(616000,'J/mol'), E0=(61600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 218,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(604500,'J/mol'), E0=(60450,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 219,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(604500,'J/mol'), E0=(60450,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 220,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(1.41421e+07,'m^3/(mol*s)'), n=7.62613e-07, w0=(616000,'J/mol'), E0=(61600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 221,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(604500,'J/mol'), E0=(60450,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 222,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(5.73483e+06,'m^3/(mol*s)'), n=0.0494855, w0=(561071,'J/mol'), E0=(56107.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.013183633715737554, var=0.3061106219718662, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN',), comment="""BM rule fitted to 14 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.142289790728978"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.142289790728978""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.142289790728978
""",
)

entry(
    index = 223,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(5890.46,'m^3/(mol*s)'), n=1.07802, w0=(550136,'J/mol'), E0=(4597.48,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0972327622844336, var=5.331784229139727, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 4.873368350449794"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 4.873368350449794""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 4.873368350449794
""",
)

entry(
    index = 224,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN",
    kinetics = ArrheniusBM(A=(1.4839e+06,'m^3/(mol*s)'), n=0.180126, w0=(557800,'J/mol'), E0=(55780,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0693355214740531, var=0.6976392811046382, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN',), comment="""BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN
    Total Standard Deviation in ln(k): 1.8486608883989328"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN
Total Standard Deviation in ln(k): 1.8486608883989328""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN
Total Standard Deviation in ln(k): 1.8486608883989328
""",
)

entry(
    index = 225,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_N-Sp-5R!H-1CN",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_N-Sp-5R!H-1CN',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_N-Sp-5R!H-1CN
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_N-Sp-5R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_N-Sp-5R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 226,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(161459,'m^3/(mol*s)'), n=0.736577, w0=(573286,'J/mol'), E0=(75318.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.23232747438234658, var=0.29894538026548934, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.6798442753401788"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.6798442753401788""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.6798442753401788
""",
)

entry(
    index = 227,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(16039.5,'m^3/(mol*s)'), n=0.960818, w0=(591167,'J/mol'), E0=(59116.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02977097333687675, var=0.0, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 0.07480144054491646"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.07480144054491646""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.07480144054491646
""",
)

entry(
    index = 228,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(581.972,'m^3/(mol*s)'), n=1.28922, w0=(571688,'J/mol'), E0=(60418.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01655073742167548, var=0.2670654695580123, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.0775993275042435"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.0775993275042435""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.0775993275042435
""",
)

entry(
    index = 229,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(330.615,'m^3/(mol*s)'), n=1.27907, w0=(604667,'J/mol'), E0=(60466.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03980613352150107, var=0.0, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 0.10001541085804289"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.10001541085804289""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.10001541085804289
""",
)

entry(
    index = 230,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_2R!H->C",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(577500,'J/mol'), E0=(57750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 231,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C",
    kinetics = ArrheniusBM(A=(4777.26,'m^3/(mol*s)'), n=1.1259, w0=(573833,'J/mol'), E0=(54051,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.014318469347156951, var=0.5255678968362857, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C
    Total Standard Deviation in ln(k): 1.4893300331436168"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C
Total Standard Deviation in ln(k): 1.4893300331436168""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C
Total Standard Deviation in ln(k): 1.4893300331436168
""",
)

entry(
    index = 232,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.00559e+07,'m^3/(mol*s)'), n=6.9906e-07, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0874588644176721, var=2.4138979216251335, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-2R!H-R
    Total Standard Deviation in ln(k): 5.847010260467036"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.847010260467036""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.847010260467036
""",
)

entry(
    index = 233,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 234,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N_2R!H->N",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(684500,'J/mol'), E0=(68450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N_2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N_2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 235,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(558500,'J/mol'), E0=(55850,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 236,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 237,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O",
    kinetics = ArrheniusBM(A=(340825,'m^3/(mol*s)'), n=2.54075e-07, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 238,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O",
    kinetics = ArrheniusBM(A=(731425,'m^3/(mol*s)'), n=0.032825, w0=(536423,'J/mol'), E0=(3638.79,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.39056624947723545, var=0.30848173193814277, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O',), comment="""BM rule fitted to 13 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O
    Total Standard Deviation in ln(k): 2.0947747860388346"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O
Total Standard Deviation in ln(k): 2.0947747860388346""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O
Total Standard Deviation in ln(k): 2.0947747860388346
""",
)

entry(
    index = 239,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R_Ext-5BrCClFNO-R",
    kinetics = ArrheniusBM(A=(763000,'m^3/(mol*s)'), n=0, w0=(515000,'J/mol'), E0=(46820.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R_Ext-5BrCClFNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R_Ext-5BrCClFNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R_Ext-5BrCClFNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R_Ext-5BrCClFNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 240,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N",
    kinetics = ArrheniusBM(A=(55.3682,'m^3/(mol*s)'), n=1.72068, w0=(548000,'J/mol'), E0=(42013.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0406619764046778, var=0.11093145697366305, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N
    Total Standard Deviation in ln(k): 3.2824331527498067"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N
Total Standard Deviation in ln(k): 3.2824331527498067""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N
Total Standard Deviation in ln(k): 3.2824331527498067
""",
)

entry(
    index = 241,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_N-2NO->N",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(625500,'J/mol'), E0=(26769.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 242,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N_2NO->N",
    kinetics = ArrheniusBM(A=(0.0294,'m^3/(mol*s)'), n=2.69, w0=(662000,'J/mol'), E0=(33510,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 243,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N_N-2NO->N",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(635000,'J/mol'), E0=(6334.04,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 244,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_Ext-4CNS-R_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(3.47e+08,'m^3/(mol*s)'), n=-0.75, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_Ext-4CNS-R_Ext-4CNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_Ext-4CNS-R_Ext-4CNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 245,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C_Sp-5C=4CNS",
    kinetics = ArrheniusBM(A=(3.01e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C_Sp-5C=4CNS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C_Sp-5C=4CNS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C_Sp-5C=4CNS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C_Sp-5C=4CNS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 246,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C_N-Sp-5C=4CNS",
    kinetics = ArrheniusBM(A=(1.20333e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C_N-Sp-5C=4CNS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C_N-Sp-5C=4CNS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C_N-Sp-5C=4CNS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C_N-Sp-5C=4CNS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 247,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O",
    kinetics = ArrheniusBM(A=(334.46,'m^3/(mol*s)'), n=1.27744, w0=(593500,'J/mol'), E0=(32251.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2786278929612721, var=0.671686074395935, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O
    Total Standard Deviation in ln(k): 2.3430799122511208"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O
Total Standard Deviation in ln(k): 2.3430799122511208""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O
Total Standard Deviation in ln(k): 2.3430799122511208
""",
)

entry(
    index = 248,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O",
    kinetics = ArrheniusBM(A=(1.3921e+07,'m^3/(mol*s)'), n=-0.30377, w0=(534750,'J/mol'), E0=(34101.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.18817937817650857, var=0.35532683171930624, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O
    Total Standard Deviation in ln(k): 1.6678209990969446"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O
Total Standard Deviation in ln(k): 1.6678209990969446""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O
Total Standard Deviation in ln(k): 1.6678209990969446
""",
)

entry(
    index = 249,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=-1.30785e-08, w0=(563000,'J/mol'), E0=(20314.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 250,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(6.76056e+19,'m^3/(mol*s)'), n=-4.75849, w0=(563000,'J/mol'), E0=(-16313.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.1336541640536497, var=0.9158136442810729, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 7.279434547604328"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 7.279434547604328""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 7.279434547604328
""",
)

entry(
    index = 251,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 252,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 253,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(616000,'J/mol'), E0=(61600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 254,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O",
    kinetics = ArrheniusBM(A=(3.40474e+06,'m^3/(mol*s)'), n=0.0965803, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08627894346154628, var=0.10714425604487637, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O',), comment="""BM rule fitted to 12 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O
    Total Standard Deviation in ln(k): 0.8729891374057825"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O
Total Standard Deviation in ln(k): 0.8729891374057825""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O
Total Standard Deviation in ln(k): 0.8729891374057825
""",
)

entry(
    index = 255,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O",
    kinetics = ArrheniusBM(A=(9.91859e+06,'m^3/(mol*s)'), n=7.07993e-07, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.593098441241876, var=5.180580787960406, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O
    Total Standard Deviation in ln(k): 8.565715206950241"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O
Total Standard Deviation in ln(k): 8.565715206950241""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O
Total Standard Deviation in ln(k): 8.565715206950241
""",
)

entry(
    index = 256,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl",
    kinetics = ArrheniusBM(A=(3.53553e+06,'m^3/(mol*s)'), n=4.89783e-08, w0=(551500,'J/mol'), E0=(55150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 257,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(4565.74,'m^3/(mol*s)'), n=1.12095, w0=(549833,'J/mol'), E0=(4802.34,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06935249396982397, var=6.2849664669379415, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl
    Total Standard Deviation in ln(k): 5.200090337342633"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl
Total Standard Deviation in ln(k): 5.200090337342633""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl
Total Standard Deviation in ln(k): 5.200090337342633
""",
)

entry(
    index = 258,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O",
    kinetics = ArrheniusBM(A=(1.48384e+06,'m^3/(mol*s)'), n=0.19459, w0=(561357,'J/mol'), E0=(56135.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.553853731446543, var=1.2213657934951738, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O
    Total Standard Deviation in ln(k): 3.6071336695960277"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O
Total Standard Deviation in ln(k): 3.6071336695960277""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O
Total Standard Deviation in ln(k): 3.6071336695960277
""",
)

entry(
    index = 259,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O",
    kinetics = ArrheniusBM(A=(1.48465e+06,'m^3/(mol*s)'), n=2.18899e-07, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.04202612563048e-08, var=0.4209388154429199, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O
    Total Standard Deviation in ln(k): 1.3006681900655117"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O
Total Standard Deviation in ln(k): 1.3006681900655117""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O
Total Standard Deviation in ln(k): 1.3006681900655117
""",
)

entry(
    index = 260,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1",
    kinetics = ArrheniusBM(A=(359225,'m^3/(mol*s)'), n=0.629539, w0=(579750,'J/mol'), E0=(76359.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.18775366787754902, var=0.5056744314519345, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1
    Total Standard Deviation in ln(k): 1.8973258153357502"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1
Total Standard Deviation in ln(k): 1.8973258153357502""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1
Total Standard Deviation in ln(k): 1.8973258153357502
""",
)

entry(
    index = 261,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_N-2R!H-u1",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_N-2R!H-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_N-2R!H-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_N-2R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_N-2R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 262,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N",
    kinetics = ArrheniusBM(A=(16039.5,'m^3/(mol*s)'), n=0.960818, w0=(608000,'J/mol'), E0=(60800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4478648794535599, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N
    Total Standard Deviation in ln(k): 1.1252886418431154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N
Total Standard Deviation in ln(k): 1.1252886418431154""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N
Total Standard Deviation in ln(k): 1.1252886418431154
""",
)

entry(
    index = 263,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->N",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(557500,'J/mol'), E0=(55750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 264,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N",
    kinetics = ArrheniusBM(A=(556.026,'m^3/(mol*s)'), n=1.27907, w0=(574750,'J/mol'), E0=(57475,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03980613384668196, var=0.21353467318894948, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N
    Total Standard Deviation in ln(k): 1.0263997235150666"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N
Total Standard Deviation in ln(k): 1.0263997235150666""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N
Total Standard Deviation in ln(k): 1.0263997235150666
""",
)

entry(
    index = 265,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N",
    kinetics = ArrheniusBM(A=(1034.27,'m^3/(mol*s)'), n=1.27325, w0=(568625,'J/mol'), E0=(70032.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.4563726079606476, var=1.944170176183772, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N
    Total Standard Deviation in ln(k): 6.454500002687694"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N
Total Standard Deviation in ln(k): 6.454500002687694""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N
Total Standard Deviation in ln(k): 6.454500002687694
""",
)

entry(
    index = 266,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N",
    kinetics = ArrheniusBM(A=(330.615,'m^3/(mol*s)'), n=1.27907, w0=(621500,'J/mol'), E0=(62150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5988305691570073, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N
    Total Standard Deviation in ln(k): 1.5045994199924806"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N
Total Standard Deviation in ln(k): 1.5045994199924806""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N
Total Standard Deviation in ln(k): 1.5045994199924806
""",
)

entry(
    index = 267,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->N",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 268,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1",
    kinetics = ArrheniusBM(A=(402.603,'m^3/(mol*s)'), n=1.432, w0=(586750,'J/mol'), E0=(45299,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.23124471023692633, var=0.6439912876041309, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1
    Total Standard Deviation in ln(k): 2.1897980705198403"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1
Total Standard Deviation in ln(k): 2.1897980705198403""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1
Total Standard Deviation in ln(k): 2.1897980705198403
""",
)

entry(
    index = 269,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_N-2NO-u1",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_N-2NO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_N-2NO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 270,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 271,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(241000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 272,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(690653,'m^3/(mol*s)'), n=0.03855, w0=(505500,'J/mol'), E0=(15624,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.511937133666525, var=0.2069864860586801, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R
    Total Standard Deviation in ln(k): 4.710906629102865"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R
Total Standard Deviation in ln(k): 4.710906629102865""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R
Total Standard Deviation in ln(k): 4.710906629102865
""",
)

entry(
    index = 273,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R",
    kinetics = ArrheniusBM(A=(3.51432e+06,'m^3/(mol*s)'), n=-0.121857, w0=(545700,'J/mol'), E0=(30896.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1784558131958314, var=0.36279489353899785, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R
    Total Standard Deviation in ln(k): 1.6558826434865987"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R
Total Standard Deviation in ln(k): 1.6558826434865987""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R
Total Standard Deviation in ln(k): 1.6558826434865987
""",
)

entry(
    index = 274,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.00924e+06,'m^3/(mol*s)'), n=-0.0262523, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0014495304618347246, var=3.639688099256267e-05, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.01573656849823323"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.01573656849823323""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.01573656849823323
""",
)

entry(
    index = 275,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C",
    kinetics = ArrheniusBM(A=(1.97085e+06,'m^3/(mol*s)'), n=-0.0393785, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0327092327690802, var=0.00213978781668374, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C
    Total Standard Deviation in ln(k): 0.1749187175813773"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C
Total Standard Deviation in ln(k): 0.1749187175813773""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C
Total Standard Deviation in ln(k): 0.1749187175813773
""",
)

entry(
    index = 276,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_N-Sp-5CF-4C",
    kinetics = ArrheniusBM(A=(1.21e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_N-Sp-5CF-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_N-Sp-5CF-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_N-Sp-5CF-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_N-Sp-5CF-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 277,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N_2N-u1",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(548000,'J/mol'), E0=(39690.4,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 278,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N_N-2N-u1",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 279,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_1CNS->N",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(648000,'J/mol'), E0=(54170.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_1CNS->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_1CNS->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_1CNS->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_1CNS->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 280,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_N-1CNS->N",
    kinetics = ArrheniusBM(A=(2.89e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_N-1CNS->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_N-1CNS->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_N-1CNS->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_N-1CNS->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 281,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS",
    kinetics = ArrheniusBM(A=(9.90493e+06,'m^3/(mol*s)'), n=-0.242077, w0=(533900,'J/mol'), E0=(36741.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2104331510432725, var=0.3469949091049228, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS
    Total Standard Deviation in ln(k): 1.7096412434813608"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS
Total Standard Deviation in ln(k): 1.7096412434813608""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS
Total Standard Deviation in ln(k): 1.7096412434813608
""",
)

entry(
    index = 282,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_N-Sp-5CS-4CCNSS",
    kinetics = ArrheniusBM(A=(1.52e+08,'m^3/(mol*s)'), n=-0.7, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_N-Sp-5CS-4CCNSS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_N-Sp-5CS-4CCNSS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_N-Sp-5CS-4CCNSS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_N-Sp-5CS-4CCNSS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 283,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(20643.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 284,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(18.9153,'m^3/(mol*s)'), n=1.81747, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10035160543507311, var=0.15570237264362138, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R
    Total Standard Deviation in ln(k): 1.0431909321781416"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R
Total Standard Deviation in ln(k): 1.0431909321781416""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R
Total Standard Deviation in ln(k): 1.0431909321781416
""",
)

entry(
    index = 285,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F",
    kinetics = ArrheniusBM(A=(26.8761,'m^3/(mol*s)'), n=1.81747, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.100351597299271, var=0.7152290174734149, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F
    Total Standard Deviation in ln(k): 1.9475684767113888"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F
Total Standard Deviation in ln(k): 1.9475684767113888""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F
Total Standard Deviation in ln(k): 1.9475684767113888
""",
)

entry(
    index = 286,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_N-5R!H->F",
    kinetics = ArrheniusBM(A=(6.66667e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 287,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 288,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(55150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 289,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O",
    kinetics = ArrheniusBM(A=(658.944,'m^3/(mol*s)'), n=1.27993, w0=(555400,'J/mol'), E0=(55540,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5181407789181125, var=1.0420570151630493, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O
    Total Standard Deviation in ln(k): 3.348318755450757"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O
Total Standard Deviation in ln(k): 3.348318755450757""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O
Total Standard Deviation in ln(k): 3.348318755450757
""",
)

entry(
    index = 290,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O",
    kinetics = ArrheniusBM(A=(31713.3,'m^3/(mol*s)'), n=0.961774, w0=(542875,'J/mol'), E0=(31765.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.6423137916398918, var=4.334055419132747, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O
    Total Standard Deviation in ln(k): 8.299953096021015"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O
Total Standard Deviation in ln(k): 8.299953096021015""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O
Total Standard Deviation in ln(k): 8.299953096021015
""",
)

entry(
    index = 291,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(2593.48,'m^3/(mol*s)'), n=1.21164, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06690106550528453, var=0.2548976178770319, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.1802314728939025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.1802314728939025""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.1802314728939025
""",
)

entry(
    index = 292,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(55150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 293,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_5R!H->C",
    kinetics = ArrheniusBM(A=(1.27916e+06,'m^3/(mol*s)'), n=-2.7154e-07, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9639738002758667, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_5R!H->C
    Total Standard Deviation in ln(k): 1.9682923503688117"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_5R!H->C
Total Standard Deviation in ln(k): 1.9682923503688117""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_5R!H->C
Total Standard Deviation in ln(k): 1.9682923503688117
""",
)

entry(
    index = 294,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_N-5R!H->C",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 295,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N",
    kinetics = ArrheniusBM(A=(12497.3,'m^3/(mol*s)'), n=1.03962, w0=(570167,'J/mol'), E0=(68190.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.023693053900012195, var=0.72769164089489, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N
    Total Standard Deviation in ln(k): 1.769666416457713"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N
Total Standard Deviation in ln(k): 1.769666416457713""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N
Total Standard Deviation in ln(k): 1.769666416457713
""",
)

entry(
    index = 296,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N",
    kinetics = ArrheniusBM(A=(48750,'m^3/(mol*s)'), n=0.958373, w0=(589333,'J/mol'), E0=(58933.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.47580866012507, var=4.807609562897205, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N
    Total Standard Deviation in ln(k): 8.103696573709435"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N
Total Standard Deviation in ln(k): 8.103696573709435""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N
Total Standard Deviation in ln(k): 8.103696573709435
""",
)

entry(
    index = 297,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N_2R!H->N",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(671000,'J/mol'), E0=(67100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N_2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N_2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 298,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(545000,'J/mol'), E0=(54500,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 299,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N",
    kinetics = ArrheniusBM(A=(467.561,'m^3/(mol*s)'), n=1.27907, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5988305691570074, var=0.9609060278364029, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N
    Total Standard Deviation in ln(k): 3.469757305105129"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N
Total Standard Deviation in ln(k): 3.469757305105129""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N
Total Standard Deviation in ln(k): 3.469757305105129
""",
)

entry(
    index = 300,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N",
    kinetics = ArrheniusBM(A=(661.23,'m^3/(mol*s)'), n=1.27907, w0=(601500,'J/mol'), E0=(60150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5988305691570073, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N
    Total Standard Deviation in ln(k): 1.5045994199924806"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N
Total Standard Deviation in ln(k): 1.5045994199924806""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N
Total Standard Deviation in ln(k): 1.5045994199924806
""",
)

entry(
    index = 301,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C",
    kinetics = ArrheniusBM(A=(1.68229e+12,'m^3/(mol*s)'), n=-1.58506, w0=(538750,'J/mol'), E0=(91710.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05139266775561785, var=10.28700587203263, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C
    Total Standard Deviation in ln(k): 6.55898680737653"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C
Total Standard Deviation in ln(k): 6.55898680737653""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C
Total Standard Deviation in ln(k): 6.55898680737653
""",
)

entry(
    index = 302,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1003.56,'m^3/(mol*s)'), n=1.27744, w0=(598500,'J/mol'), E0=(59850,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.4209805867496146, var=1.043249572366644, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C
    Total Standard Deviation in ln(k): 3.105368344405712"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C
Total Standard Deviation in ln(k): 3.105368344405712""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C
Total Standard Deviation in ln(k): 3.105368344405712
""",
)

entry(
    index = 303,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N_2R!H->N",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(684500,'J/mol'), E0=(68450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N_2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N_2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 304,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(558500,'J/mol'), E0=(55850,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 305,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1_2NO->N",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 306,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1_N-2NO->N",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(625500,'J/mol'), E0=(52192.4,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 307,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_1R!H-inRing",
    kinetics = ArrheniusBM(A=(0.000675,'m^3/(mol*s)'), n=2.7, w0=(483500,'J/mol'), E0=(33691.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 308,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(73314,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_N-1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_N-1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_N-1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_N-1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 309,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(2.56e+07,'m^3/(mol*s)'), n=-0.35, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 310,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3e+06,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(52750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 311,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_2R!H->C",
    kinetics = ArrheniusBM(A=(2.16e+08,'m^3/(mol*s)'), n=-0.75, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 312,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.9053e+06,'m^3/(mol*s)'), n=-0.0575532, w0=(561500,'J/mol'), E0=(17540.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1352806081598749, var=1.2535632058264505, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C
    Total Standard Deviation in ln(k): 2.5844552807383243"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C
Total Standard Deviation in ln(k): 2.5844552807383243""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C
Total Standard Deviation in ln(k): 2.5844552807383243
""",
)

entry(
    index = 313,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Ext-5CF-R",
    kinetics = ArrheniusBM(A=(783000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Ext-5CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Ext-5CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Ext-5CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Ext-5CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 314,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Sp-5CF-4C",
    kinetics = ArrheniusBM(A=(843000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Sp-5CF-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Sp-5CF-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Sp-5CF-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Sp-5CF-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 315,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_N-Sp-5CF-4C",
    kinetics = ArrheniusBM(A=(843000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_N-Sp-5CF-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_N-Sp-5CF-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_N-Sp-5CF-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_N-Sp-5CF-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 316,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C_Ext-5CF-R",
    kinetics = ArrheniusBM(A=(1.45e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C_Ext-5CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C_Ext-5CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C_Ext-5CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C_Ext-5CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 317,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(7.76827e+08,'m^3/(mol*s)'), n=-0.9, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0763652085225523e-17, var=0.04891149884417046, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R
    Total Standard Deviation in ln(k): 0.4433660913390881"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.4433660913390881""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.4433660913390881
""",
)

entry(
    index = 318,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C",
    kinetics = ArrheniusBM(A=(3.11937e+07,'m^3/(mol*s)'), n=-0.389378, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.032709232769080235, var=0.0016076635746038646, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C
    Total Standard Deviation in ln(k): 0.16256521857885725"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C
Total Standard Deviation in ln(k): 0.16256521857885725""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C
Total Standard Deviation in ln(k): 0.16256521857885725
""",
)

entry(
    index = 319,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_N-1CNS->C",
    kinetics = ArrheniusBM(A=(644,'m^3/(mol*s)'), n=1.19, w0=(513500,'J/mol'), E0=(39978.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_N-1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_N-1CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 320,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(15.5169,'m^3/(mol*s)'), n=1.81747, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10035159271588616, var=0.0, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-1CN-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 0.25213968019066874"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 0.25213968019066874""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 0.25213968019066874
""",
)

entry(
    index = 321,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(21.9442,'m^3/(mol*s)'), n=1.81747, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.5096568970344717, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 5.758265666606295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.758265666606295""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.758265666606295
""",
)

entry(
    index = 322,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(26.8761,'m^3/(mol*s)'), n=1.81747, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.5096568970344721, var=2.413897921625164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F_Ext-2R!H-R
    Total Standard Deviation in ln(k): 6.907809337393689"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.907809337393689""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.907809337393689
""",
)

entry(
    index = 323,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=-8.33353e-08, w0=(551500,'J/mol'), E0=(55150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 324,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_2R!H->N",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 325,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_N-2R!H->N",
    kinetics = ArrheniusBM(A=(0.00558313,'m^3/(mol*s)'), n=2.89583, w0=(551500,'J/mol'), E0=(55150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.4053866559415926, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_N-2R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_N-2R!H->N
    Total Standard Deviation in ln(k): 8.008842950292529"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_N-2R!H->N
Total Standard Deviation in ln(k): 8.008842950292529""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_N-2R!H->N
Total Standard Deviation in ln(k): 8.008842950292529
""",
)

entry(
    index = 326,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(14.1063,'m^3/(mol*s)'), n=1.81747, w0=(538000,'J/mol'), E0=(49991.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00914657571632494, var=0.13660130397161369, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R
    Total Standard Deviation in ln(k): 0.7639236849409741"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R
Total Standard Deviation in ln(k): 0.7639236849409741""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R
Total Standard Deviation in ln(k): 0.7639236849409741
""",
)

entry(
    index = 327,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_2R!H->N",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(557500,'J/mol'), E0=(46201.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 328,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_N-2R!H->N",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(538000,'J/mol'), E0=(53800,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_N-2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_N-2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 329,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_5R!H->C",
    kinetics = ArrheniusBM(A=(1.70765e+07,'m^3/(mol*s)'), n=4.66546e-07, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9494596051172368, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_5R!H->C
    Total Standard Deviation in ln(k): 1.9534182263699047"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_5R!H->C
Total Standard Deviation in ln(k): 1.9534182263699047""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_5R!H->C
Total Standard Deviation in ln(k): 1.9534182263699047
""",
)

entry(
    index = 330,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C",
    kinetics = ArrheniusBM(A=(31.9612,'m^3/(mol*s)'), n=1.81747, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1003515989323806, var=0.14441168773977575, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C
    Total Standard Deviation in ln(k): 1.0139698546247726"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C
Total Standard Deviation in ln(k): 1.0139698546247726""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C
Total Standard Deviation in ln(k): 1.0139698546247726
""",
)

entry(
    index = 331,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_5R!H->C_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(904000,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_5R!H->C_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_5R!H->C_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 332,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_2R!H->C",
    kinetics = ArrheniusBM(A=(400,'m^3/(mol*s)'), n=1.5, w0=(564000,'J/mol'), E0=(56400,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 333,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C",
    kinetics = ArrheniusBM(A=(26.4912,'m^3/(mol*s)'), n=1.82399, w0=(573250,'J/mol'), E0=(52118.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.20148362850470902, var=0.27147237417689896, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C
    Total Standard Deviation in ln(k): 1.5507676079238173"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C
Total Standard Deviation in ln(k): 1.5507676079238173""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C
Total Standard Deviation in ln(k): 1.5507676079238173
""",
)

entry(
    index = 334,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_2R!H->C",
    kinetics = ArrheniusBM(A=(3.61e+06,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 335,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C",
    kinetics = ArrheniusBM(A=(48483.4,'m^3/(mol*s)'), n=0.959594, w0=(609250,'J/mol'), E0=(60925,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6761713695632989, var=0.41113237262952895, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C
    Total Standard Deviation in ln(k): 2.984351249045606"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C
Total Standard Deviation in ln(k): 2.984351249045606""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C
Total Standard Deviation in ln(k): 2.984351249045606
""",
)

entry(
    index = 336,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N_2N-u1",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 337,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N_N-2N-u1",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 338,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N_2CO->C",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(577500,'J/mol'), E0=(57750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N_2CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N_2CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N_2CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N_2CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 339,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N_N-2CO->C",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(625500,'J/mol'), E0=(55881.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N_N-2CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N_N-2CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N_N-2CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N_N-2CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 340,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C_4BrO->Br",
    kinetics = ArrheniusBM(A=(2.37e+06,'m^3/(mol*s)'), n=0, w0=(514500,'J/mol'), E0=(51450,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C_4BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C_4BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C_4BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C_4BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 341,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C_N-4BrO->Br",
    kinetics = ArrheniusBM(A=(2.41e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C_N-4BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C_N-4BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C_N-4BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C_N-4BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 342,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C_2NO->N",
    kinetics = ArrheniusBM(A=(3.6,'m^3/(mol*s)'), n=2, w0=(590000,'J/mol'), E0=(59000,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 343,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C_N-2NO->N",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(607000,'J/mol'), E0=(60700,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 344,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C_Ext-7R!H-R_Ext-5CF-R",
    kinetics = ArrheniusBM(A=(1.94e+06,'m^3/(mol*s)'), n=0, w0=(561500,'J/mol'), E0=(38387.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C_Ext-7R!H-R_Ext-5CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C_Ext-7R!H-R_Ext-5CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C_Ext-7R!H-R_Ext-5CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C_Ext-7R!H-R_Ext-5CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 345,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(2.86e+09,'m^3/(mol*s)'), n=-1.1, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R_Ext-4CNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R_Ext-4CNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 346,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C_Ext-5CS-R",
    kinetics = ArrheniusBM(A=(2.29e+07,'m^3/(mol*s)'), n=-0.35, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C_Ext-5CS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C_Ext-5CS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C_Ext-5CS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C_Ext-5CS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 347,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-1CN-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.2e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-1CN-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-1CN-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-1CN-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-1CN-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 348,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R_5CFO->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(55150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R_5CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R_5CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R_5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R_5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 349,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R_N-5CFO->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(55150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R_N-5CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R_N-5CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R_N-5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R_N-5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 350,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R_5CFO->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(538000,'J/mol'), E0=(82230,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R_5CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R_5CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R_5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R_5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 351,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R_N-5CFO->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(538000,'J/mol'), E0=(78689.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R_N-5CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R_N-5CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R_N-5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R_N-5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 352,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_5R!H->C_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_5R!H->C_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_5R!H->C_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 353,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(31.0338,'m^3/(mol*s)'), n=1.81747, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.509656897034472, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C_Ext-1CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C_Ext-1CN-R
    Total Standard Deviation in ln(k): 3.793107781493648"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 3.793107781493648""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 3.793107781493648
""",
)

entry(
    index = 354,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C_2NO->N",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 355,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C_N-2NO->N",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(612000,'J/mol'), E0=(63725,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 356,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C_2NO->N",
    kinetics = ArrheniusBM(A=(720,'m^3/(mol*s)'), n=1.5, w0=(576500,'J/mol'), E0=(57650,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 357,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C_N-2NO->N",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(642000,'J/mol'), E0=(64200,'J/mol'), Tmin=(300,'K'), Tmax=(1000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

